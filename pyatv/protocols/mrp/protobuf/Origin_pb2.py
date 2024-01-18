# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/Origin.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import DeviceInfoMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/Origin.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)pyatv/protocols/mrp/protobuf/Origin.proto\x1a\x34pyatv/protocols/mrp/protobuf/DeviceInfoMessage.proto\"\xba\x01\n\x06Origin\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.Origin.Type\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\x12\n\nidentifier\x18\x03 \x01(\x05\x12&\n\ndeviceInfo\x18\x04 \x01(\x0b\x32\x12.DeviceInfoMessage\x12\x17\n\x0fisLocallyHosted\x18\x05 \x01(\x08\"*\n\x04Type\x12\x0b\n\x07Unknown\x10\x00\x12\t\n\x05Local\x10\x01\x12\n\n\x06\x43ustom\x10\x02'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2.DESCRIPTOR,])



_ORIGIN_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Origin.Type',
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
      name='Local', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Custom', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=244,
  serialized_end=286,
)
_sym_db.RegisterEnumDescriptor(_ORIGIN_TYPE)


_ORIGIN = _descriptor.Descriptor(
  name='Origin',
  full_name='Origin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Origin.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='Origin.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Origin.identifier', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='Origin.deviceInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isLocallyHosted', full_name='Origin.isLocallyHosted', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ORIGIN_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=286,
)

_ORIGIN.fields_by_name['type'].enum_type = _ORIGIN_TYPE
_ORIGIN.fields_by_name['deviceInfo'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2._DEVICEINFOMESSAGE
_ORIGIN_TYPE.containing_type = _ORIGIN
DESCRIPTOR.message_types_by_name['Origin'] = _ORIGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Origin = _reflection.GeneratedProtocolMessageType('Origin', (_message.Message,), {
  'DESCRIPTOR' : _ORIGIN,
  '__module__' : 'pyatv.protocols.mrp.protobuf.Origin_pb2'
  # @@protoc_insertion_point(class_scope:Origin)
  })
_sym_db.RegisterMessage(Origin)


# @@protoc_insertion_point(module_scope)
