# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/RegisterVoiceInputDeviceMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.mrp.protobuf import VoiceInputDeviceDescriptorMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_VoiceInputDeviceDescriptorMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/RegisterVoiceInputDeviceMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8pyatv/mrp/protobuf/RegisterVoiceInputDeviceMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a:pyatv/mrp/protobuf/VoiceInputDeviceDescriptorMessage.proto\"X\n\x1fRegisterVoiceInputDeviceMessage\x12\x35\n\x10\x64\x65viceDescriptor\x18\x01 \x01(\x0b\x32\x1b.VoiceInputDeviceDescriptor:[\n\x1fregisterVoiceInputDeviceMessage\x12\x10.ProtocolMessage\x18! \x01(\x0b\x32 .RegisterVoiceInputDeviceMessage'
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_VoiceInputDeviceDescriptorMessage__pb2.DESCRIPTOR,])


REGISTERVOICEINPUTDEVICEMESSAGE_FIELD_NUMBER = 33
registerVoiceInputDeviceMessage = _descriptor.FieldDescriptor(
  name='registerVoiceInputDeviceMessage', full_name='registerVoiceInputDeviceMessage', index=0,
  number=33, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_REGISTERVOICEINPUTDEVICEMESSAGE = _descriptor.Descriptor(
  name='RegisterVoiceInputDeviceMessage',
  full_name='RegisterVoiceInputDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceDescriptor', full_name='RegisterVoiceInputDeviceMessage.deviceDescriptor', index=0,
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
  serialized_start=162,
  serialized_end=250,
)

_REGISTERVOICEINPUTDEVICEMESSAGE.fields_by_name['deviceDescriptor'].message_type = pyatv_dot_mrp_dot_protobuf_dot_VoiceInputDeviceDescriptorMessage__pb2._VOICEINPUTDEVICEDESCRIPTOR
DESCRIPTOR.message_types_by_name['RegisterVoiceInputDeviceMessage'] = _REGISTERVOICEINPUTDEVICEMESSAGE
DESCRIPTOR.extensions_by_name['registerVoiceInputDeviceMessage'] = registerVoiceInputDeviceMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterVoiceInputDeviceMessage = _reflection.GeneratedProtocolMessageType('RegisterVoiceInputDeviceMessage', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERVOICEINPUTDEVICEMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.RegisterVoiceInputDeviceMessage_pb2'
  # @@protoc_insertion_point(class_scope:RegisterVoiceInputDeviceMessage)
  })
_sym_db.RegisterMessage(RegisterVoiceInputDeviceMessage)

registerVoiceInputDeviceMessage.message_type = _REGISTERVOICEINPUTDEVICEMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(registerVoiceInputDeviceMessage)

# @@protoc_insertion_point(module_scope)
