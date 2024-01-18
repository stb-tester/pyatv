# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/TextInputMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/TextInputMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3pyatv/protocols/mrp/protobuf/TextInputMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"S\n\nActionType\"E\n\x04\x45num\x12\x0b\n\x07Unknown\x10\x00\x12\n\n\x06Insert\x10\x01\x12\x07\n\x03Set\x10\x02\x12\n\n\x06\x44\x65lete\x10\x03\x12\x0f\n\x0b\x43learAction\x10\x04\"Y\n\x10TextInputMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x0c\n\x04text\x18\x02 \x01(\t\x12$\n\nactionType\x18\x03 \x01(\x0e\x32\x10.ActionType.Enum:=\n\x10textInputMessage\x12\x10.ProtocolMessage\x18\x1e \x01(\x0b\x32\x11.TextInputMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


TEXTINPUTMESSAGE_FIELD_NUMBER = 30
textInputMessage = _descriptor.FieldDescriptor(
  name='textInputMessage', full_name='textInputMessage', index=0,
  number=30, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_ACTIONTYPE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='ActionType.Enum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Insert', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Set', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Delete', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ClearAction', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=121,
  serialized_end=190,
)
_sym_db.RegisterEnumDescriptor(_ACTIONTYPE_ENUM)


_ACTIONTYPE = _descriptor.Descriptor(
  name='ActionType',
  full_name='ActionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTIONTYPE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=190,
)


_TEXTINPUTMESSAGE = _descriptor.Descriptor(
  name='TextInputMessage',
  full_name='TextInputMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='TextInputMessage.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='TextInputMessage.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actionType', full_name='TextInputMessage.actionType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=192,
  serialized_end=281,
)

_ACTIONTYPE_ENUM.containing_type = _ACTIONTYPE
_TEXTINPUTMESSAGE.fields_by_name['actionType'].enum_type = _ACTIONTYPE_ENUM
DESCRIPTOR.message_types_by_name['ActionType'] = _ACTIONTYPE
DESCRIPTOR.message_types_by_name['TextInputMessage'] = _TEXTINPUTMESSAGE
DESCRIPTOR.extensions_by_name['textInputMessage'] = textInputMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionType = _reflection.GeneratedProtocolMessageType('ActionType', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONTYPE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.TextInputMessage_pb2'
  # @@protoc_insertion_point(class_scope:ActionType)
  })
_sym_db.RegisterMessage(ActionType)

TextInputMessage = _reflection.GeneratedProtocolMessageType('TextInputMessage', (_message.Message,), {
  'DESCRIPTOR' : _TEXTINPUTMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.TextInputMessage_pb2'
  # @@protoc_insertion_point(class_scope:TextInputMessage)
  })
_sym_db.RegisterMessage(TextInputMessage)

textInputMessage.message_type = _TEXTINPUTMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(textInputMessage)

# @@protoc_insertion_point(module_scope)
