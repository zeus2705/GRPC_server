# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functionplusone.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66unctionplusone.proto\"\x13\n\x06number\x12\t\n\x01x\x18\x01 \x01(\x03\"\x1d\n\x0cplusonereply\x12\r\n\x05reply\x18\x01 \x01(\x03\x32\x30\n\tQuickMath\x12#\n\x07Plusone\x12\x07.number\x1a\r.plusonereply\"\x00\x42\'\n\x0fio.grpc.PlusoneB\x0cPlusoneProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_NUMBER = DESCRIPTOR.message_types_by_name['number']
_PLUSONEREPLY = DESCRIPTOR.message_types_by_name['plusonereply']
number = _reflection.GeneratedProtocolMessageType('number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'functionplusone_pb2'
  # @@protoc_insertion_point(class_scope:number)
  })
_sym_db.RegisterMessage(number)

plusonereply = _reflection.GeneratedProtocolMessageType('plusonereply', (_message.Message,), {
  'DESCRIPTOR' : _PLUSONEREPLY,
  '__module__' : 'functionplusone_pb2'
  # @@protoc_insertion_point(class_scope:plusonereply)
  })
_sym_db.RegisterMessage(plusonereply)

_QUICKMATH = DESCRIPTOR.services_by_name['QuickMath']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017io.grpc.PlusoneB\014PlusoneProtoP\001\242\002\003HLW'
  _NUMBER._serialized_start=25
  _NUMBER._serialized_end=44
  _PLUSONEREPLY._serialized_start=46
  _PLUSONEREPLY._serialized_end=75
  _QUICKMATH._serialized_start=77
  _QUICKMATH._serialized_end=125
# @@protoc_insertion_point(module_scope)
