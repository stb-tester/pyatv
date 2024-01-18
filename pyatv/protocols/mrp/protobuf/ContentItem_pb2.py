# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/ContentItem.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ContentItemMetadata_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ContentItemMetadata__pb2
from pyatv.protocols.mrp.protobuf import LanguageOption_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/ContentItem.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.pyatv/protocols/mrp/protobuf/ContentItem.proto\x1a\x36pyatv/protocols/mrp/protobuf/ContentItemMetadata.proto\x1a\x31pyatv/protocols/mrp/protobuf/LanguageOption.proto\"\x8c\x01\n\x13LanguageOptionGroup\x12\x1b\n\x13\x61llowEmptySelection\x18\x01 \x01(\x08\x12.\n\x15\x64\x65\x66\x61ultLanguageOption\x18\x02 \x01(\x0b\x32\x0f.LanguageOption\x12(\n\x0flanguageOptions\x18\x03 \x03(\x0b\x32\x0f.LanguageOption\"\xf4\x02\n\x0b\x43ontentItem\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.ContentItemMetadata\x12\x13\n\x0b\x61rtworkData\x18\x03 \x01(\x0c\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x36\n\x18\x61vailableLanguageOptions\x18\x05 \x03(\x0b\x32\x14.LanguageOptionGroup\x12/\n\x16\x63urrentLanguageOptions\x18\x06 \x03(\x0b\x32\x0f.LanguageOption\x12\x18\n\x10parentIdentifier\x18\t \x01(\t\x12\x1a\n\x12\x61ncestorIdentifier\x18\n \x01(\t\x12\x17\n\x0fqueueIdentifier\x18\x0b \x01(\t\x12\x19\n\x11requestIdentifier\x18\x0c \x01(\t\x12\x18\n\x10\x61rtworkDataWidth\x18\r \x01(\x05\x12\x19\n\x11\x61rtworkDataHeight\x18\x0e \x01(\x05'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ContentItemMetadata__pb2.DESCRIPTOR,pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2.DESCRIPTOR,])




_LANGUAGEOPTIONGROUP = _descriptor.Descriptor(
  name='LanguageOptionGroup',
  full_name='LanguageOptionGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowEmptySelection', full_name='LanguageOptionGroup.allowEmptySelection', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defaultLanguageOption', full_name='LanguageOptionGroup.defaultLanguageOption', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='languageOptions', full_name='LanguageOptionGroup.languageOptions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=158,
  serialized_end=298,
)


_CONTENTITEM = _descriptor.Descriptor(
  name='ContentItem',
  full_name='ContentItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='ContentItem.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ContentItem.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artworkData', full_name='ContentItem.artworkData', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='ContentItem.info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='availableLanguageOptions', full_name='ContentItem.availableLanguageOptions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentLanguageOptions', full_name='ContentItem.currentLanguageOptions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parentIdentifier', full_name='ContentItem.parentIdentifier', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ancestorIdentifier', full_name='ContentItem.ancestorIdentifier', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queueIdentifier', full_name='ContentItem.queueIdentifier', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestIdentifier', full_name='ContentItem.requestIdentifier', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artworkDataWidth', full_name='ContentItem.artworkDataWidth', index=10,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='artworkDataHeight', full_name='ContentItem.artworkDataHeight', index=11,
      number=14, type=5, cpp_type=1, label=1,
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
  serialized_start=301,
  serialized_end=673,
)

_LANGUAGEOPTIONGROUP.fields_by_name['defaultLanguageOption'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2._LANGUAGEOPTION
_LANGUAGEOPTIONGROUP.fields_by_name['languageOptions'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2._LANGUAGEOPTION
_CONTENTITEM.fields_by_name['metadata'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ContentItemMetadata__pb2._CONTENTITEMMETADATA
_CONTENTITEM.fields_by_name['availableLanguageOptions'].message_type = _LANGUAGEOPTIONGROUP
_CONTENTITEM.fields_by_name['currentLanguageOptions'].message_type = pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_LanguageOption__pb2._LANGUAGEOPTION
DESCRIPTOR.message_types_by_name['LanguageOptionGroup'] = _LANGUAGEOPTIONGROUP
DESCRIPTOR.message_types_by_name['ContentItem'] = _CONTENTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LanguageOptionGroup = _reflection.GeneratedProtocolMessageType('LanguageOptionGroup', (_message.Message,), {
  'DESCRIPTOR' : _LANGUAGEOPTIONGROUP,
  '__module__' : 'pyatv.protocols.mrp.protobuf.ContentItem_pb2'
  # @@protoc_insertion_point(class_scope:LanguageOptionGroup)
  })
_sym_db.RegisterMessage(LanguageOptionGroup)

ContentItem = _reflection.GeneratedProtocolMessageType('ContentItem', (_message.Message,), {
  'DESCRIPTOR' : _CONTENTITEM,
  '__module__' : 'pyatv.protocols.mrp.protobuf.ContentItem_pb2'
  # @@protoc_insertion_point(class_scope:ContentItem)
  })
_sym_db.RegisterMessage(ContentItem)


# @@protoc_insertion_point(module_scope)
