# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/RemoveEndpointsMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/RemoveEndpointsMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9pyatv/protocols/mrp/protobuf/RemoveEndpointsMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\".\n\x16RemoveEndpointsMessage\x12\x14\n\x0c\x65ndpointUIDs\x18\x01 \x03(\t:I\n\x16removeEndpointsMessage\x12\x10.ProtocolMessage\x18T \x01(\x0b\x32\x17.RemoveEndpointsMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


REMOVEENDPOINTSMESSAGE_FIELD_NUMBER = 84
removeEndpointsMessage = _descriptor.FieldDescriptor(
  name='removeEndpointsMessage', full_name='removeEndpointsMessage', index=0,
  number=84, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_REMOVEENDPOINTSMESSAGE = _descriptor.Descriptor(
  name='RemoveEndpointsMessage',
  full_name='RemoveEndpointsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpointUIDs', full_name='RemoveEndpointsMessage.endpointUIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=113,
  serialized_end=159,
)

DESCRIPTOR.message_types_by_name['RemoveEndpointsMessage'] = _REMOVEENDPOINTSMESSAGE
DESCRIPTOR.extensions_by_name['removeEndpointsMessage'] = removeEndpointsMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveEndpointsMessage = _reflection.GeneratedProtocolMessageType('RemoveEndpointsMessage', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEENDPOINTSMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.RemoveEndpointsMessage_pb2'
  # @@protoc_insertion_point(class_scope:RemoveEndpointsMessage)
  })
_sym_db.RegisterMessage(RemoveEndpointsMessage)

removeEndpointsMessage.message_type = _REMOVEENDPOINTSMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(removeEndpointsMessage)

# @@protoc_insertion_point(module_scope)
