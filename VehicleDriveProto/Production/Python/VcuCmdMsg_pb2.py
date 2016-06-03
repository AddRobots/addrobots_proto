# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VcuCmdMsg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VcuCmdMsg.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0fVcuCmdMsg.proto\"|\n\x05\x44rive\x12\x10\n\x08velocity\x18\x01 \x01(\x05\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x01\x12\x10\n\x08\x64istance\x18\x04 \x01(\x01\x12\x14\n\x0c\x65\x64geDistance\x18\x05 \x01(\x01\x12\x10\n\x08\x65\x64geSide\x18\x06 \x01(\t\"S\n\x05Orbit\x12\x10\n\x08velocity\x18\x01 \x01(\x01\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x01\x12\x0f\n\x07\x64\x65grees\x18\x04 \x01(\x01\"\x1c\n\x04Halt\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x01 \x01(\x01\"c\n\x11VcuWrapperMessage\x12\x17\n\x05\x64rive\x18\x01 \x01(\x0b\x32\x06.DriveH\x00\x12\x17\n\x05orbit\x18\x02 \x01(\x0b\x32\x06.OrbitH\x00\x12\x15\n\x04halt\x18\x03 \x01(\x0b\x32\x05.HaltH\x00\x42\x05\n\x03msgb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DRIVE = _descriptor.Descriptor(
  name='Drive',
  full_name='Drive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='velocity', full_name='Drive.velocity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Drive.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='Drive.acceleration', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='Drive.distance', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edgeDistance', full_name='Drive.edgeDistance', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edgeSide', full_name='Drive.edgeSide', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=143,
)


_ORBIT = _descriptor.Descriptor(
  name='Orbit',
  full_name='Orbit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='velocity', full_name='Orbit.velocity', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Orbit.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='Orbit.acceleration', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='degrees', full_name='Orbit.degrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=228,
)


_HALT = _descriptor.Descriptor(
  name='Halt',
  full_name='Halt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='Halt.acceleration', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=258,
)


_VCUWRAPPERMESSAGE = _descriptor.Descriptor(
  name='VcuWrapperMessage',
  full_name='VcuWrapperMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drive', full_name='VcuWrapperMessage.drive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orbit', full_name='VcuWrapperMessage.orbit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='halt', full_name='VcuWrapperMessage.halt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='VcuWrapperMessage.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=260,
  serialized_end=359,
)

_VCUWRAPPERMESSAGE.fields_by_name['drive'].message_type = _DRIVE
_VCUWRAPPERMESSAGE.fields_by_name['orbit'].message_type = _ORBIT
_VCUWRAPPERMESSAGE.fields_by_name['halt'].message_type = _HALT
_VCUWRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPERMESSAGE.fields_by_name['drive'])
_VCUWRAPPERMESSAGE.fields_by_name['drive'].containing_oneof = _VCUWRAPPERMESSAGE.oneofs_by_name['msg']
_VCUWRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPERMESSAGE.fields_by_name['orbit'])
_VCUWRAPPERMESSAGE.fields_by_name['orbit'].containing_oneof = _VCUWRAPPERMESSAGE.oneofs_by_name['msg']
_VCUWRAPPERMESSAGE.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPERMESSAGE.fields_by_name['halt'])
_VCUWRAPPERMESSAGE.fields_by_name['halt'].containing_oneof = _VCUWRAPPERMESSAGE.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['Drive'] = _DRIVE
DESCRIPTOR.message_types_by_name['Orbit'] = _ORBIT
DESCRIPTOR.message_types_by_name['Halt'] = _HALT
DESCRIPTOR.message_types_by_name['VcuWrapperMessage'] = _VCUWRAPPERMESSAGE

Drive = _reflection.GeneratedProtocolMessageType('Drive', (_message.Message,), dict(
  DESCRIPTOR = _DRIVE,
  __module__ = 'VcuCmdMsg_pb2'
  # @@protoc_insertion_point(class_scope:Drive)
  ))
_sym_db.RegisterMessage(Drive)

Orbit = _reflection.GeneratedProtocolMessageType('Orbit', (_message.Message,), dict(
  DESCRIPTOR = _ORBIT,
  __module__ = 'VcuCmdMsg_pb2'
  # @@protoc_insertion_point(class_scope:Orbit)
  ))
_sym_db.RegisterMessage(Orbit)

Halt = _reflection.GeneratedProtocolMessageType('Halt', (_message.Message,), dict(
  DESCRIPTOR = _HALT,
  __module__ = 'VcuCmdMsg_pb2'
  # @@protoc_insertion_point(class_scope:Halt)
  ))
_sym_db.RegisterMessage(Halt)

VcuWrapperMessage = _reflection.GeneratedProtocolMessageType('VcuWrapperMessage', (_message.Message,), dict(
  DESCRIPTOR = _VCUWRAPPERMESSAGE,
  __module__ = 'VcuCmdMsg_pb2'
  # @@protoc_insertion_point(class_scope:VcuWrapperMessage)
  ))
_sym_db.RegisterMessage(VcuWrapperMessage)


# @@protoc_insertion_point(module_scope)
