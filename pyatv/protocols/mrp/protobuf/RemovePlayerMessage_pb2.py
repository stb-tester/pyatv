# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import PlayerPath_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6pyatv/protocols/mrp/protobuf/RemovePlayerMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a-pyatv/protocols/mrp/protobuf/PlayerPath.proto\"6\n\x13RemovePlayerMessage\x12\x1f\n\nplayerPath\x18\x01 \x01(\x0b\x32\x0b.PlayerPath:C\n\x13removePlayerMessage\x12\x10.ProtocolMessage\x18: \x01(\x0b\x32\x14.RemovePlayerMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2.DESCRIPTOR,])


REMOVEPLAYERMESSAGE_FIELD_NUMBER = 58
removePlayerMessage = _descriptor.FieldDescriptor(
  name='removePlayerMessage', full_name='removePlayerMessage', index=0,
  number=58, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_REMOVEPLAYERMESSAGE = _descriptor.Descriptor(
  name='RemovePlayerMessage',
  full_name='RemovePlayerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerPath', full_name='RemovePlayerMessage.playerPath', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=157,
  serialized_end=211,
)

_REMOVEPLAYERMESSAGE.fields_by_name['playerPath'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2._PLAYERPATH
DESCRIPTOR.message_types_by_name['RemovePlayerMessage'] = _REMOVEPLAYERMESSAGE
DESCRIPTOR.extensions_by_name['removePlayerMessage'] = removePlayerMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemovePlayerMessage = _reflection.GeneratedProtocolMessageType('RemovePlayerMessage', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPLAYERMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.RemovePlayerMessage_pb2'
  # @@protoc_insertion_point(class_scope:RemovePlayerMessage)
  })
_sym_db.RegisterMessage(RemovePlayerMessage)

removePlayerMessage.message_type = _REMOVEPLAYERMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(removePlayerMessage)

# @@protoc_insertion_point(module_scope)
