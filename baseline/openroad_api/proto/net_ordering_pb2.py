# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/net_ordering.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/net_ordering.proto',
  package='openroad_api.net_ordering',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18proto/net_ordering.proto\x12\x19openroad_api.net_ordering\"\xc7\x01\n\x04Node\x12\x0e\n\x06maze_x\x18\x01 \x01(\x11\x12\x0e\n\x06maze_y\x18\x02 \x01(\x11\x12\x0e\n\x06maze_z\x18\x03 \x01(\x11\x12\x0f\n\x07point_x\x18\x04 \x01(\x11\x12\x0f\n\x07point_y\x18\x05 \x01(\x11\x12\x0f\n\x07point_z\x18\x06 \x01(\x11\x12\x31\n\x04type\x18\x07 \x01(\x0e\x32#.openroad_api.net_ordering.NodeType\x12\x0f\n\x07is_used\x18\x08 \x01(\x08\x12\x0b\n\x03net\x18\t \x01(\x11\x12\x0b\n\x03pin\x18\n \x01(\x11\"\xcf\x01\n\x07Request\x12\r\n\x05\x64im_x\x18\x01 \x01(\r\x12\r\n\x05\x64im_y\x18\x02 \x01(\r\x12\r\n\x05\x64im_z\x18\x03 \x01(\r\x12.\n\x05nodes\x18\x04 \x03(\x0b\x32\x1f.openroad_api.net_ordering.Node\x12\x18\n\x10reward_violation\x18\x05 \x01(\r\x12\x1a\n\x12reward_wire_length\x18\x06 \x01(\r\x12\x12\n\nreward_via\x18\x07 \x01(\r\x12\x0f\n\x07is_done\x18\x08 \x01(\x08\x12\x0c\n\x04nets\x18\t \x03(\r\"\x1d\n\x08Response\x12\x11\n\tnet_index\x18\x01 \x01(\x11\"\x84\x01\n\x07Message\x12\x35\n\x07request\x18\x01 \x01(\x0b\x32\".openroad_api.net_ordering.RequestH\x00\x12\x37\n\x08response\x18\x02 \x01(\x0b\x32#.openroad_api.net_ordering.ResponseH\x00\x42\t\n\x07wrapper*0\n\x08NodeType\x12\x0c\n\x08\x42LOCKAGE\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\n\n\x06\x41\x43\x43\x45SS\x10\x02\x62\x06proto3')
)

_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='openroad_api.net_ordering.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLOCKAGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=633,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_NODETYPE)

NodeType = enum_type_wrapper.EnumTypeWrapper(_NODETYPE)
BLOCKAGE = 0
NORMAL = 1
ACCESS = 2



_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='openroad_api.net_ordering.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maze_x', full_name='openroad_api.net_ordering.Node.maze_x', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maze_y', full_name='openroad_api.net_ordering.Node.maze_y', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maze_z', full_name='openroad_api.net_ordering.Node.maze_z', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_x', full_name='openroad_api.net_ordering.Node.point_x', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_y', full_name='openroad_api.net_ordering.Node.point_y', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='point_z', full_name='openroad_api.net_ordering.Node.point_z', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='openroad_api.net_ordering.Node.type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_used', full_name='openroad_api.net_ordering.Node.is_used', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net', full_name='openroad_api.net_ordering.Node.net', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pin', full_name='openroad_api.net_ordering.Node.pin', index=9,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=255,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='openroad_api.net_ordering.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim_x', full_name='openroad_api.net_ordering.Request.dim_x', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_y', full_name='openroad_api.net_ordering.Request.dim_y', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_z', full_name='openroad_api.net_ordering.Request.dim_z', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='openroad_api.net_ordering.Request.nodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_violation', full_name='openroad_api.net_ordering.Request.reward_violation', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_wire_length', full_name='openroad_api.net_ordering.Request.reward_wire_length', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_via', full_name='openroad_api.net_ordering.Request.reward_via', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_done', full_name='openroad_api.net_ordering.Request.is_done', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nets', full_name='openroad_api.net_ordering.Request.nets', index=8,
      number=9, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=465,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='openroad_api.net_ordering.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='net_index', full_name='openroad_api.net_ordering.Response.net_index', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=496,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='openroad_api.net_ordering.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='openroad_api.net_ordering.Message.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='openroad_api.net_ordering.Message.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='wrapper', full_name='openroad_api.net_ordering.Message.wrapper',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=499,
  serialized_end=631,
)

_NODE.fields_by_name['type'].enum_type = _NODETYPE
_REQUEST.fields_by_name['nodes'].message_type = _NODE
_MESSAGE.fields_by_name['request'].message_type = _REQUEST
_MESSAGE.fields_by_name['response'].message_type = _RESPONSE
_MESSAGE.oneofs_by_name['wrapper'].fields.append(
  _MESSAGE.fields_by_name['request'])
_MESSAGE.fields_by_name['request'].containing_oneof = _MESSAGE.oneofs_by_name['wrapper']
_MESSAGE.oneofs_by_name['wrapper'].fields.append(
  _MESSAGE.fields_by_name['response'])
_MESSAGE.fields_by_name['response'].containing_oneof = _MESSAGE.oneofs_by_name['wrapper']
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['NodeType'] = _NODETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'proto.net_ordering_pb2'
  # @@protoc_insertion_point(class_scope:openroad_api.net_ordering.Node)
  ))
_sym_db.RegisterMessage(Node)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'proto.net_ordering_pb2'
  # @@protoc_insertion_point(class_scope:openroad_api.net_ordering.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'proto.net_ordering_pb2'
  # @@protoc_insertion_point(class_scope:openroad_api.net_ordering.Response)
  ))
_sym_db.RegisterMessage(Response)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'proto.net_ordering_pb2'
  # @@protoc_insertion_point(class_scope:openroad_api.net_ordering.Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
