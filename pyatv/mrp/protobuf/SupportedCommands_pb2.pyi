# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.CommandInfo_pb2 import (
    CommandInfo as pyatv___mrp___protobuf___CommandInfo_pb2___CommandInfo,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class SupportedCommands(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def supportedCommands(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pyatv___mrp___protobuf___CommandInfo_pb2___CommandInfo]: ...

    def __init__(self,
        *,
        supportedCommands : typing___Optional[typing___Iterable[pyatv___mrp___protobuf___CommandInfo_pb2___CommandInfo]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> SupportedCommands: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"supportedCommands"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"supportedCommands",b"supportedCommands"]) -> None: ...
