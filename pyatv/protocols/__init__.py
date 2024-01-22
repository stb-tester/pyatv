"""Module containing all protocol logic."""

import typing
from typing import Any, Dict, Generator, Mapping

from pyatv import interface
from pyatv.const import Protocol
from pyatv.core import Core, MutableService, SetupData
from pyatv.core.scan import ScanHandlerDeviceInfoName
from pyatv.interface import BaseService, DeviceInfo
from pyatv.protocols import airplay as airplay_proto
from pyatv.protocols import companion as companion_proto
from pyatv.protocols import dmap as dmap_proto
from pyatv.protocols import mrp as mrp_proto
from pyatv.protocols import raop as raop_proto


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


PROTOCOLS: Dict[Protocol, _ProtocolModule] = {
    Protocol.AirPlay: airplay_proto,
    Protocol.Companion: companion_proto,
    Protocol.DMAP: dmap_proto,
    Protocol.MRP: mrp_proto,
    Protocol.RAOP: raop_proto,
}
