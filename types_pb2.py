# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: types.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'types.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x04\x63hat\"\x1a\n\nApiRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"B\n\x0b\x41piResponse\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\t\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APIREQUEST']._serialized_start=21
  _globals['_APIREQUEST']._serialized_end=47
  _globals['_APIRESPONSE']._serialized_start=49
  _globals['_APIRESPONSE']._serialized_end=115
# @@protoc_insertion_point(module_scope)
