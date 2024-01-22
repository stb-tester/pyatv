"""Module containing all protocol logic."""

import typing
from typing import Any, Dict, Generator, Mapping

from pyatv import interface
from pyatv.const import Protocol
from pyatv.core import Core, MutableService, SetupData
from pyatv.core.scan import ScanHandlerDeviceInfoName
from pyatv.interface import BaseService, DeviceInfo


class _ProtocolModule(typing.Protocol):
    def setup(self, core: Core) -> Generator[SetupData, None, None]:
        ...

    def scan(self) -> Mapping[str, ScanHandlerDeviceInfoName]:
        ...

    def pair(self, core: Core, **kwargs) -> interface.PairingHandler:
        ...

    def device_info(
            self, service_type: str,
            properties: Mapping[str, Any]) -> Dict[str, Any]:
        ...

    async def service_info(
        self,
        service: MutableService,
        devinfo: DeviceInfo,
        services: Mapping[Protocol, BaseService],
    ) -> None:
        ...


def get_protocol(protocol: Protocol) -> _ProtocolModule:
    """Look up protocol module for a protocol."""
    match protocol:
        case Protocol.Companion:
            from . import companion as companion_proto
            return companion_proto
        case Protocol.DMAP:
            from . import dmap as dmap_proto
            return dmap_proto
        case Protocol.MRP:
            from . import mrp as mrp_proto
            return mrp_proto
        case Protocol.RAOP:
            from . import raop as raop_proto
            return raop_proto
        case Protocol.AirPlay:
            from . import airplay as airplay_proto
            return airplay_proto
        case _:
            raise ValueError(f"unknown protocol: {protocol}")
