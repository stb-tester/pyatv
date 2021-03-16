"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    NewType as typing___NewType,
    Optional as typing___Optional,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SetConnectionStateMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConnectionStateValue = typing___NewType('ConnectionStateValue', builtin___int)
    type___ConnectionStateValue = ConnectionStateValue
    ConnectionState: _ConnectionState
    class _ConnectionState(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[SetConnectionStateMessage.ConnectionStateValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        Connecting = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 1)
        Connected = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 2)
        Disconnected = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 3)
    Connecting = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 1)
    Connected = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 2)
    Disconnected = typing___cast(SetConnectionStateMessage.ConnectionStateValue, 3)

    state: type___SetConnectionStateMessage.ConnectionStateValue = ...

    def __init__(self,
        *,
        state : typing___Optional[type___SetConnectionStateMessage.ConnectionStateValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"state",b"state"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"state",b"state"]) -> None: ...
type___SetConnectionStateMessage = SetConnectionStateMessage

setConnectionStateMessage: google___protobuf___descriptor___FieldDescriptor = ...
