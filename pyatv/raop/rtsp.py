"""Implementation of the RTSP protocol."""
import asyncio
import logging
from random import randrange
import re
from socket import socket
from typing import Dict, Mapping, NamedTuple, Optional, Tuple, Union

from pyatv import exceptions
from pyatv.dmap import tags
from pyatv.raop import timing
from pyatv.raop.metadata import AudioMetadata

_LOGGER = logging.getLogger(__name__)

FRAMES_PER_PACKET = 352
USER_AGENT = "AirPlay/540.31"

ANNOUNCE_PAYLOAD = (
    "v=0\r\n"
    + "o=iTunes {session_id} 0 IN IP4 {local_ip}\r\n"
    + "s=iTunes\r\n"
    + "c=IN IP4 {remote_ip}\r\n"
    + "t=0 0\r\n"
    + "m=audio 0 RTP/AVP 96\r\n"
    + "a=rtpmap:96 AppleLossless\r\n"
    + f"a=fmtp:96 {FRAMES_PER_PACKET} 0 "
    + "{bits_per_channel} 40 10 14 {channels} 255 0 0 {sample_rate}\r\n"
)


class RtspContext:
    """Data used for one RTSP session.

    This class holds a bit too much information, should be
    restructured a bit.
    """

    def __init__(self) -> None:
        """Initialize a new RtspContext."""
        self.sample_rate: int = 44100
        self.channels: int = 2
        self.bytes_per_channel: int = 2
        self.latency = 22050 + self.sample_rate

        self.rtpseq: int = 0
        self.start_ts = 0
        self.head_ts = 0

        self.server_port: int = 0
        self.control_port: int = 0
        self.timing_port: int = 0
        self.rtsp_session: int = 0

        # TODO: Not entirely sure about the ranges for these
        self.session_id: int = randrange(2 ** 32)
        self.dacp_id: str = f"{randrange(2 ** 64):X}"
        self.active_remote: int = randrange(2 ** 32)

    def reset(self) -> None:
        """Reset seasion.

        Must be done when sample rate changes.
        """
        self.rtpseq = randrange(2 ** 16)
        self.start_ts = timing.ntp2ts(timing.ntp_now(), self.sample_rate)
        self.head_ts = self.start_ts
        self.latency = 22050 + self.sample_rate

    @property
    def rtptime(self) -> int:
        """Current RTP time with latency."""
        return self.head_ts - (self.start_ts - self.latency)


class RtspResponse(NamedTuple):
    """RTSP response message."""

    code: int
    message: str
    headers: Mapping[str, str]
    body: str


def parse_response(response: str) -> Tuple[RtspResponse, str]:
    """Parse RTSP response."""
    try:
        header_str, body = response.split("\r\n\r\n", maxsplit=1)
    except ValueError as ex:
        raise ValueError("missing end lines") from ex
    headers = header_str.split("\r\n")

    match = re.match(r"RTSP/1.0 (\d+) (.+)", headers[0])
    if not match:
        raise ValueError(f"bad first line: {headers[0]}")

    code, message = match.groups()
    resp_headers = {}

    for line in headers[1:]:
        if line:
            key, value = line.split(": ")
            resp_headers[key] = value

    content_length = int(resp_headers.get("Content-Length", 0))
    if body and len(body) < content_length:
        raise ValueError("too short body")

    return (
        RtspResponse(int(code), message, resp_headers, body[0:content_length]),
        body[content_length:],
    )


class RtspSession(asyncio.Protocol):
    """Representation of an RTSP session."""

    def __init__(self, context: RtspContext) -> None:
        """Initialize a new RtspSession."""
        self.context = context
        self.transport = None
        self.requests: Dict[int, Tuple[asyncio.Semaphore, RtspResponse]] = {}
        self.cseq = 0

    @property
    def local_ip(self) -> str:
        """Return IP address of local interface."""
        return self._get_socket().getsockname()[0]

    @property
    def remote_ip(self) -> str:
        """Return IP address of remote instance."""
        return self._get_socket().getpeername()[0]

    def _get_socket(self) -> socket:
        if self.transport is None:
            raise RuntimeError("not connected to remote")
        return self.transport.get_extra_info("socket")

    @property
    def uri(self) -> str:
        """Return URI used for session requests."""
        return f"rtsp://{self.local_ip}/{self.context.session_id}"

    def close(self) -> None:
        """Close RTSP session."""
        if self.transport:
            transport = self.transport
            self.transport = None
            transport.close()

    def connection_made(self, transport) -> None:
        """Handle that connection succeeded."""
        self.transport = transport
        _LOGGER.debug("RTSP connected to %s", self.remote_ip)

    def data_received(self, data: bytes) -> None:
        """Handle incoming RTSP data."""
        _LOGGER.debug("Received: %s", data)
        rest = data.decode("utf-8")
        while rest != "":
            parsed, rest = parse_response(rest)
            if "CSeq" in parsed.headers:
                cseq = int(parsed.headers["CSeq"])
                if cseq in self.requests:
                    semaphore, _ = self.requests[cseq]
                    self.requests[cseq] = (semaphore, parsed)
                    semaphore.release()

    @staticmethod
    def error_received(exc) -> None:
        """Handle a connection error."""
        _LOGGER.error("Error received: %s", exc)

    def connection_lost(self, exc) -> None:
        """Handle that connection was lost."""
        _LOGGER.debug("RTSP Connection closed")

    async def announce(self) -> RtspResponse:
        """Send ANNOUNCE message."""
        body = ANNOUNCE_PAYLOAD.format(
            session_id=self.context.session_id,
            local_ip=self.local_ip,
            remote_ip=self.remote_ip,
            bits_per_channel=8 * self.context.bytes_per_channel,
            channels=self.context.channels,
            sample_rate=self.context.sample_rate,
        )
        return await self.send_and_receive(
            "ANNOUNCE",
            content_type="application/sdp",
            body=body,
        )

    async def setup(self, control_port: int, timing_port: int) -> RtspResponse:
        """Send SETUP message."""
        return await self.send_and_receive(
            "SETUP",
            headers={
                "Transport": "RTP/AVP/UDP;unicast;interleaved=0-1;mode=record;"
                + f"control_port={control_port};timing_port={timing_port}",
            },
        )

    async def record(self, rtpseq: int, rtptime: int) -> RtspResponse:
        """Send RECORD message."""
        return await self.send_and_receive(
            "RECORD",
            headers={
                "Range": "npt=0-",
                "Session": self.context.rtsp_session,
                "RTP-Info": f"seq={rtpseq};rtptime={rtptime}",
            },
        )

    async def set_parameter(self, parameter: str, value: str) -> RtspResponse:
        """Send SET_PARAMETER message."""
        return await self.send_and_receive(
            "SET_PARAMETER",
            content_type="text/parameters",
            body=f"{parameter}: {value}",
        )

    async def set_metadata(
        self,
        rtpseq: int,
        rtptime: int,
        metadata: AudioMetadata,
    ) -> RtspResponse:
        """Change metadata for what is playing."""
        payload = b""
        if metadata.title:
            payload += tags.string_tag("minm", metadata.title)
        if metadata.album:
            payload += tags.string_tag("asal", metadata.album)
        if metadata.artist:
            payload += tags.string_tag("asar", metadata.artist)

        return await self.send_and_receive(
            "SET_PARAMETER",
            content_type="application/x-dmap-tagged",
            headers={
                "Session": self.context.rtsp_session,
                "RTP-Info": f"seq={rtpseq};rtptime={rtptime}",
            },
            body=tags.container_tag("mlit", payload),
        )

    async def send_and_receive(
        self,
        method: str,
        content_type: Optional[str] = None,
        headers: Mapping[str, object] = None,
        body: Union[str, bytes] = None,
    ) -> RtspResponse:
        """Send a RTSP message and return response."""
        cseq = self.cseq
        self.cseq += 1

        if isinstance(body, str):
            body = body.encode("utf-8")

        msg = f"{method} {self.uri} RTSP/1.0"
        msg += f"\r\nCSeq: {cseq}"
        msg += f"\r\nUser-Agent: {USER_AGENT}"
        msg += f"\r\nDACP-ID: {self.context.dacp_id}"
        msg += f"\r\nActive-Remote: {self.context.active_remote}"
        msg += f"\r\nClient-Instance: {self.context.dacp_id}"
        if content_type:
            msg += f"\r\nContent-Type: {content_type}"

        if body:
            msg += f"\r\nContent-Length: {len(body) if body else 0}"
        for key, value in (headers or {}).items():
            msg += f"\r\n{key}: {value}"
        msg += 2 * "\r\n"

        output = msg.encode("utf-8")
        if body:
            output += body

        _LOGGER.debug("Sending RTSP message: %s", output)
        if self.transport:
            self.transport.write(output)
        else:
            raise RuntimeError("not connected to remote")

        self.requests[cseq] = (asyncio.Semaphore(value=0), None)
        try:
            await asyncio.wait_for(self.requests[cseq][0].acquire(), 4)
            response = self.requests[cseq][1]
        finally:
            del self.requests[cseq]

        _LOGGER.debug("Got RTSP response to %d: %s:", cseq, response)

        # Positive response
        if 200 <= response.code < 300:
            return response

        if response.code in [401, 403]:
            raise exceptions.AuthenticationError("not authenticated")

        raise exceptions.ProtocolError(f"RTSP method {method} failed")