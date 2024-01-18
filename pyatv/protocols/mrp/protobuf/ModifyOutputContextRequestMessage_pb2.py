# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/ModifyOutputContextRequestMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/protocols/mrp/protobuf/ModifyOutputContextRequestMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDpyatv/protocols/mrp/protobuf/ModifyOutputContextRequestMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"E\n\x1eModifyOutputContextRequestType\"#\n\x04\x45num\x12\x1b\n\x17SharedAudioPresentation\x10\x01\"\x8b\x02\n!ModifyOutputContextRequestMessage\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.ModifyOutputContextRequestType.Enum\x12\x15\n\raddingDevices\x18\x02 \x03(\t\x12\x17\n\x0fremovingDevices\x18\x03 \x03(\t\x12\x16\n\x0esettingDevices\x18\x04 \x03(\t\x12!\n\x19\x63lusterAwareAddingDevices\x18\x05 \x03(\t\x12#\n\x1b\x63lusterAwareRemovingDevices\x18\x06 \x03(\t\x12\"\n\x1a\x63lusterAwareSettingDevices\x18\x07 \x03(\t:_\n!modifyOutputContextRequestMessage\x12\x10.ProtocolMessage\x18\x34 \x01(\x0b\x32\".ModifyOutputContextRequestMessage'
  ,
  dependencies=[pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


MODIFYOUTPUTCONTEXTREQUESTMESSAGE_FIELD_NUMBER = 52
modifyOutputContextRequestMessage = _descriptor.FieldDescriptor(
  name='modifyOutputContextRequestMessage', full_name='modifyOutputContextRequestMessage', index=0,
  number=52, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='ModifyOutputContextRequestType.Enum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SharedAudioPresentation', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=193,
)
_sym_db.RegisterEnumDescriptor(_MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM)


_MODIFYOUTPUTCONTEXTREQUESTTYPE = _descriptor.Descriptor(
  name='ModifyOutputContextRequestType',
  full_name='ModifyOutputContextRequestType',
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
    _MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=193,
)


_MODIFYOUTPUTCONTEXTREQUESTMESSAGE = _descriptor.Descriptor(
  name='ModifyOutputContextRequestMessage',
  full_name='ModifyOutputContextRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ModifyOutputContextRequestMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='addingDevices', full_name='ModifyOutputContextRequestMessage.addingDevices', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='removingDevices', full_name='ModifyOutputContextRequestMessage.removingDevices', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settingDevices', full_name='ModifyOutputContextRequestMessage.settingDevices', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clusterAwareAddingDevices', full_name='ModifyOutputContextRequestMessage.clusterAwareAddingDevices', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clusterAwareRemovingDevices', full_name='ModifyOutputContextRequestMessage.clusterAwareRemovingDevices', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clusterAwareSettingDevices', full_name='ModifyOutputContextRequestMessage.clusterAwareSettingDevices', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=196,
  serialized_end=463,
)

_MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM.containing_type = _MODIFYOUTPUTCONTEXTREQUESTTYPE
_MODIFYOUTPUTCONTEXTREQUESTMESSAGE.fields_by_name['type'].enum_type = _MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM
DESCRIPTOR.message_types_by_name['ModifyOutputContextRequestType'] = _MODIFYOUTPUTCONTEXTREQUESTTYPE
DESCRIPTOR.message_types_by_name['ModifyOutputContextRequestMessage'] = _MODIFYOUTPUTCONTEXTREQUESTMESSAGE
DESCRIPTOR.extensions_by_name['modifyOutputContextRequestMessage'] = modifyOutputContextRequestMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModifyOutputContextRequestType = _reflection.GeneratedProtocolMessageType('ModifyOutputContextRequestType', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYOUTPUTCONTEXTREQUESTTYPE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.ModifyOutputContextRequestMessage_pb2'
  # @@protoc_insertion_point(class_scope:ModifyOutputContextRequestType)
  })
_sym_db.RegisterMessage(ModifyOutputContextRequestType)

ModifyOutputContextRequestMessage = _reflection.GeneratedProtocolMessageType('ModifyOutputContextRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYOUTPUTCONTEXTREQUESTMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.ModifyOutputContextRequestMessage_pb2'
  # @@protoc_insertion_point(class_scope:ModifyOutputContextRequestMessage)
  })
_sym_db.RegisterMessage(ModifyOutputContextRequestMessage)

modifyOutputContextRequestMessage.message_type = _MODIFYOUTPUTCONTEXTREQUESTMESSAGE
pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(modifyOutputContextRequestMessage)

# @@protoc_insertion_point(module_scope)
