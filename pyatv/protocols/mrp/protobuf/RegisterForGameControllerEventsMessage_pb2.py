# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/RegisterForGameControllerEventsMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/RegisterForGameControllerEventsMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nIpyatv/protocols/mrp/protobuf/RegisterForGameControllerEventsMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"\xbc\x01\n&RegisterForGameControllerEventsMessage\x12N\n\x0einputModeFlags\x18\x01 \x01(\x0e\x32\x36.RegisterForGameControllerEventsMessage.InputModeFlags\"B\n\x0eInputModeFlags\x12\x08\n\x04None\x10\x00\x12\n\n\x06Motion\x10\x01\x12\x0b\n\x07\x42uttons\x10\x02\x12\r\n\tDigitizer\x10\x03:i\n&registerForGameControllerEventsMessage\x12\x10.ProtocolMessage\x18\x1b \x01(\x0b\x32\'.RegisterForGameControllerEventsMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


REGISTERFORGAMECONTROLLEREVENTSMESSAGE_FIELD_NUMBER = 27
registerForGameControllerEventsMessage = _descriptor.FieldDescriptor(
  name='registerForGameControllerEventsMessage', full_name='registerForGameControllerEventsMessage', index=0,
  number=27, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_REGISTERFORGAMECONTROLLEREVENTSMESSAGE_INPUTMODEFLAGS = _descriptor.EnumDescriptor(
  name='InputModeFlags',
  full_name='RegisterForGameControllerEventsMessage.InputModeFlags',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='None', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Motion', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Buttons', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Digitizer', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=252,
  serialized_end=318,
)
_sym_db.RegisterEnumDescriptor(_REGISTERFORGAMECONTROLLEREVENTSMESSAGE_INPUTMODEFLAGS)


_REGISTERFORGAMECONTROLLEREVENTSMESSAGE = _descriptor.Descriptor(
  name='RegisterForGameControllerEventsMessage',
  full_name='RegisterForGameControllerEventsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputModeFlags', full_name='RegisterForGameControllerEventsMessage.inputModeFlags', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTERFORGAMECONTROLLEREVENTSMESSAGE_INPUTMODEFLAGS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=318,
)

_REGISTERFORGAMECONTROLLEREVENTSMESSAGE.fields_by_name['inputModeFlags'].enum_type = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE_INPUTMODEFLAGS
_REGISTERFORGAMECONTROLLEREVENTSMESSAGE_INPUTMODEFLAGS.containing_type = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE
DESCRIPTOR.message_types_by_name['RegisterForGameControllerEventsMessage'] = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE
DESCRIPTOR.extensions_by_name['registerForGameControllerEventsMessage'] = registerForGameControllerEventsMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterForGameControllerEventsMessage = _reflection.GeneratedProtocolMessageType('RegisterForGameControllerEventsMessage', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERFORGAMECONTROLLEREVENTSMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.RegisterForGameControllerEventsMessage_pb2'
  # @@protoc_insertion_point(class_scope:RegisterForGameControllerEventsMessage)
  })
_sym_db.RegisterMessage(RegisterForGameControllerEventsMessage)

registerForGameControllerEventsMessage.message_type = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(registerForGameControllerEventsMessage)

# @@protoc_insertion_point(module_scope)
