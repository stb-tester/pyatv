# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/SetVolumeMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/SetVolumeMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3pyatv/protocols/mrp/protobuf/SetVolumeMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\";\n\x10SetVolumeMessage\x12\x0e\n\x06volume\x18\x01 \x01(\x02\x12\x17\n\x0foutputDeviceUID\x18\x02 \x01(\t:=\n\x10setVolumeMessage\x12\x10.ProtocolMessage\x18\x37 \x01(\x0b\x32\x11.SetVolumeMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


SETVOLUMEMESSAGE_FIELD_NUMBER = 55
setVolumeMessage = _descriptor.FieldDescriptor(
  name='setVolumeMessage', full_name='setVolumeMessage', index=0,
  number=55, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_SETVOLUMEMESSAGE = _descriptor.Descriptor(
  name='SetVolumeMessage',
  full_name='SetVolumeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='SetVolumeMessage.volume', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputDeviceUID', full_name='SetVolumeMessage.outputDeviceUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['SetVolumeMessage'] = _SETVOLUMEMESSAGE
DESCRIPTOR.extensions_by_name['setVolumeMessage'] = setVolumeMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetVolumeMessage = _reflection.GeneratedProtocolMessageType('SetVolumeMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETVOLUMEMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.SetVolumeMessage_pb2'
  # @@protoc_insertion_point(class_scope:SetVolumeMessage)
  })
_sym_db.RegisterMessage(SetVolumeMessage)

setVolumeMessage.message_type = _SETVOLUMEMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(setVolumeMessage)

# @@protoc_insertion_point(module_scope)
