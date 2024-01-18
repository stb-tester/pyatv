# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/LanguageOption.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/LanguageOption.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1pyatv/protocols/mrp/protobuf/LanguageOption.proto\"u\n\x0eLanguageOption\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x13\n\x0blanguageTag\x18\x02 \x01(\t\x12\x17\n\x0f\x63haracteristics\x18\x03 \x03(\t\x12\x13\n\x0b\x64isplayName\x18\x04 \x01(\t\x12\x12\n\nidentifier\x18\x05 \x01(\t'
)




_LANGUAGEOPTION = _descriptor.Descriptor(
  name='LanguageOption',
  full_name='LanguageOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='LanguageOption.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='languageTag', full_name='LanguageOption.languageTag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='characteristics', full_name='LanguageOption.characteristics', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='LanguageOption.displayName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='LanguageOption.identifier', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=53,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['LanguageOption'] = _LANGUAGEOPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LanguageOption = _reflection.GeneratedProtocolMessageType('LanguageOption', (_message.Message,), {
  'DESCRIPTOR' : _LANGUAGEOPTION,
  '__module__' : 'pyatv.protocols.mrp.protobuf.LanguageOption_pb2'
  # @@protoc_insertion_point(class_scope:LanguageOption)
  })
_sym_db.RegisterMessage(LanguageOption)


# @@protoc_insertion_point(module_scope)
