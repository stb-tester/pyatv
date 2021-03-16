# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/SetStateMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.mrp.protobuf import NowPlayingInfo_pb2 as pyatv_dot_mrp_dot_protobuf_dot_NowPlayingInfo__pb2
from pyatv.mrp.protobuf import PlaybackQueue_pb2 as pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueue__pb2
from pyatv.mrp.protobuf import SupportedCommands_pb2 as pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2
from pyatv.mrp.protobuf import PlaybackQueueCapabilities_pb2 as pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueCapabilities__pb2
from pyatv.mrp.protobuf import PlayerPath_pb2 as pyatv_dot_mrp_dot_protobuf_dot_PlayerPath__pb2
from pyatv.mrp.protobuf import PlaybackQueueRequestMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueRequestMessage__pb2
from pyatv.mrp.protobuf import Common_pb2 as pyatv_dot_mrp_dot_protobuf_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/SetStateMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(pyatv/mrp/protobuf/SetStateMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a\'pyatv/mrp/protobuf/NowPlayingInfo.proto\x1a&pyatv/mrp/protobuf/PlaybackQueue.proto\x1a*pyatv/mrp/protobuf/SupportedCommands.proto\x1a\x32pyatv/mrp/protobuf/PlaybackQueueCapabilities.proto\x1a#pyatv/mrp/protobuf/PlayerPath.proto\x1a\x34pyatv/mrp/protobuf/PlaybackQueueRequestMessage.proto\x1a\x1fpyatv/mrp/protobuf/Common.proto\"\x93\x03\n\x0fSetStateMessage\x12\'\n\x0enowPlayingInfo\x18\x01 \x01(\x0b\x32\x0f.NowPlayingInfo\x12-\n\x11supportedCommands\x18\x02 \x01(\x0b\x32\x12.SupportedCommands\x12%\n\rplaybackQueue\x18\x03 \x01(\x0b\x32\x0e.PlaybackQueue\x12\x11\n\tdisplayID\x18\x04 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x05 \x01(\t\x12*\n\rplaybackState\x18\x06 \x01(\x0e\x32\x13.PlaybackState.Enum\x12=\n\x19playbackQueueCapabilities\x18\x08 \x01(\x0b\x32\x1a.PlaybackQueueCapabilities\x12\x1f\n\nplayerPath\x18\t \x01(\x0b\x32\x0b.PlayerPath\x12-\n\x07request\x18\n \x01(\x0b\x32\x1c.PlaybackQueueRequestMessage\x12\x1e\n\x16playbackStateTimestamp\x18\x0b \x01(\x01:;\n\x0fsetStateMessage\x12\x10.ProtocolMessage\x18\t \x01(\x0b\x32\x10.SetStateMessage'
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_NowPlayingInfo__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueue__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueCapabilities__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_PlayerPath__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueRequestMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_Common__pb2.DESCRIPTOR,])


SETSTATEMESSAGE_FIELD_NUMBER = 9
setStateMessage = _descriptor.FieldDescriptor(
  name='setStateMessage', full_name='setStateMessage', index=0,
  number=9, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_SETSTATEMESSAGE = _descriptor.Descriptor(
  name='SetStateMessage',
  full_name='SetStateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nowPlayingInfo', full_name='SetStateMessage.nowPlayingInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supportedCommands', full_name='SetStateMessage.supportedCommands', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playbackQueue', full_name='SetStateMessage.playbackQueue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayID', full_name='SetStateMessage.displayID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='SetStateMessage.displayName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playbackState', full_name='SetStateMessage.playbackState', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playbackQueueCapabilities', full_name='SetStateMessage.playbackQueueCapabilities', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerPath', full_name='SetStateMessage.playerPath', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='SetStateMessage.request', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playbackStateTimestamp', full_name='SetStateMessage.playbackStateTimestamp', index=9,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=388,
  serialized_end=791,
)

_SETSTATEMESSAGE.fields_by_name['nowPlayingInfo'].message_type = pyatv_dot_mrp_dot_protobuf_dot_NowPlayingInfo__pb2._NOWPLAYINGINFO
_SETSTATEMESSAGE.fields_by_name['supportedCommands'].message_type = pyatv_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2._SUPPORTEDCOMMANDS
_SETSTATEMESSAGE.fields_by_name['playbackQueue'].message_type = pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueue__pb2._PLAYBACKQUEUE
_SETSTATEMESSAGE.fields_by_name['playbackState'].enum_type = pyatv_dot_mrp_dot_protobuf_dot_Common__pb2._PLAYBACKSTATE_ENUM
_SETSTATEMESSAGE.fields_by_name['playbackQueueCapabilities'].message_type = pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueCapabilities__pb2._PLAYBACKQUEUECAPABILITIES
_SETSTATEMESSAGE.fields_by_name['playerPath'].message_type = pyatv_dot_mrp_dot_protobuf_dot_PlayerPath__pb2._PLAYERPATH
_SETSTATEMESSAGE.fields_by_name['request'].message_type = pyatv_dot_mrp_dot_protobuf_dot_PlaybackQueueRequestMessage__pb2._PLAYBACKQUEUEREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['SetStateMessage'] = _SETSTATEMESSAGE
DESCRIPTOR.extensions_by_name['setStateMessage'] = setStateMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetStateMessage = _reflection.GeneratedProtocolMessageType('SetStateMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETSTATEMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.SetStateMessage_pb2'
  # @@protoc_insertion_point(class_scope:SetStateMessage)
  })
_sym_db.RegisterMessage(SetStateMessage)

setStateMessage.message_type = _SETSTATEMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(setStateMessage)

# @@protoc_insertion_point(module_scope)
