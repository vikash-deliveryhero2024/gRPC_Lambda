# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: your_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'your_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12your_service.proto\"\x1b\n\x0bYourRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\x0cYourResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2;\n\x0bYourService\x12,\n\rYourRpcMethod\x12\x0c.YourRequest\x1a\r.YourResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'your_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_YOURREQUEST']._serialized_start=22
  _globals['_YOURREQUEST']._serialized_end=49
  _globals['_YOURRESPONSE']._serialized_start=51
  _globals['_YOURRESPONSE']._serialized_end=82
  _globals['_YOURSERVICE']._serialized_start=84
  _globals['_YOURSERVICE']._serialized_end=143
# @@protoc_insertion_point(module_scope)
