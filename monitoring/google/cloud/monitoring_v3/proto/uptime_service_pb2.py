# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/uptime_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.monitoring_v3.proto import (
    uptime_pb2 as google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/uptime_service.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\022UptimeServiceProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3"
    ),
    serialized_pb=_b(
        '\n5google/cloud/monitoring_v3/proto/uptime_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a-google/cloud/monitoring_v3/proto/uptime.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto"V\n\x1dListUptimeCheckConfigsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\x94\x01\n\x1eListUptimeCheckConfigsResponse\x12\x45\n\x14uptime_check_configs\x18\x01 \x03(\x0b\x32\'.google.monitoring.v3.UptimeCheckConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"+\n\x1bGetUptimeCheckConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"v\n\x1e\x43reateUptimeCheckConfigRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x44\n\x13uptime_check_config\x18\x02 \x01(\x0b\x32\'.google.monitoring.v3.UptimeCheckConfig"\x97\x01\n\x1eUpdateUptimeCheckConfigRequest\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x44\n\x13uptime_check_config\x18\x03 \x01(\x0b\x32\'.google.monitoring.v3.UptimeCheckConfig".\n\x1e\x44\x65leteUptimeCheckConfigRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"B\n\x19ListUptimeCheckIpsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"t\n\x1aListUptimeCheckIpsResponse\x12=\n\x10uptime_check_ips\x18\x01 \x03(\x0b\x32#.google.monitoring.v3.UptimeCheckIp\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf3\t\n\x12UptimeCheckService\x12\xb7\x01\n\x16ListUptimeCheckConfigs\x12\x33.google.monitoring.v3.ListUptimeCheckConfigsRequest\x1a\x34.google.monitoring.v3.ListUptimeCheckConfigsResponse"2\x82\xd3\xe4\x93\x02,\x12*/v3/{parent=projects/*}/uptimeCheckConfigs\x12\xa6\x01\n\x14GetUptimeCheckConfig\x12\x31.google.monitoring.v3.GetUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"2\x82\xd3\xe4\x93\x02,\x12*/v3/{name=projects/*/uptimeCheckConfigs/*}\x12\xc1\x01\n\x17\x43reateUptimeCheckConfig\x12\x34.google.monitoring.v3.CreateUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"G\x82\xd3\xe4\x93\x02\x41"*/v3/{parent=projects/*}/uptimeCheckConfigs:\x13uptime_check_config\x12\xd5\x01\n\x17UpdateUptimeCheckConfig\x12\x34.google.monitoring.v3.UpdateUptimeCheckConfigRequest\x1a\'.google.monitoring.v3.UptimeCheckConfig"[\x82\xd3\xe4\x93\x02U2>/v3/{uptime_check_config.name=projects/*/uptimeCheckConfigs/*}:\x13uptime_check_config\x12\x9b\x01\n\x17\x44\x65leteUptimeCheckConfig\x12\x34.google.monitoring.v3.DeleteUptimeCheckConfigRequest\x1a\x16.google.protobuf.Empty"2\x82\xd3\xe4\x93\x02,**/v3/{name=projects/*/uptimeCheckConfigs/*}\x12\x93\x01\n\x12ListUptimeCheckIps\x12/.google.monitoring.v3.ListUptimeCheckIpsRequest\x1a\x30.google.monitoring.v3.ListUptimeCheckIpsResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v3/uptimeCheckIps\x1a\xa9\x01\xca\x41\x19monitoring.googleapis.com\xd2\x41\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xaa\x01\n\x18\x63om.google.monitoring.v3B\x12UptimeServiceProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
    ],
)


_LISTUPTIMECHECKCONFIGSREQUEST = _descriptor.Descriptor(
    name="ListUptimeCheckConfigsRequest",
    full_name="google.monitoring.v3.ListUptimeCheckConfigsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsRequest.page_size",
            index=1,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsRequest.page_token",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=276,
    serialized_end=362,
)


_LISTUPTIMECHECKCONFIGSRESPONSE = _descriptor.Descriptor(
    name="ListUptimeCheckConfigsResponse",
    full_name="google.monitoring.v3.ListUptimeCheckConfigsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="uptime_check_configs",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsResponse.uptime_check_configs",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="total_size",
            full_name="google.monitoring.v3.ListUptimeCheckConfigsResponse.total_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=365,
    serialized_end=513,
)


_GETUPTIMECHECKCONFIGREQUEST = _descriptor.Descriptor(
    name="GetUptimeCheckConfigRequest",
    full_name="google.monitoring.v3.GetUptimeCheckConfigRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.GetUptimeCheckConfigRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=515,
    serialized_end=558,
)


_CREATEUPTIMECHECKCONFIGREQUEST = _descriptor.Descriptor(
    name="CreateUptimeCheckConfigRequest",
    full_name="google.monitoring.v3.CreateUptimeCheckConfigRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.monitoring.v3.CreateUptimeCheckConfigRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="uptime_check_config",
            full_name="google.monitoring.v3.CreateUptimeCheckConfigRequest.uptime_check_config",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=560,
    serialized_end=678,
)


_UPDATEUPTIMECHECKCONFIGREQUEST = _descriptor.Descriptor(
    name="UpdateUptimeCheckConfigRequest",
    full_name="google.monitoring.v3.UpdateUptimeCheckConfigRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.monitoring.v3.UpdateUptimeCheckConfigRequest.update_mask",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="uptime_check_config",
            full_name="google.monitoring.v3.UpdateUptimeCheckConfigRequest.uptime_check_config",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=681,
    serialized_end=832,
)


_DELETEUPTIMECHECKCONFIGREQUEST = _descriptor.Descriptor(
    name="DeleteUptimeCheckConfigRequest",
    full_name="google.monitoring.v3.DeleteUptimeCheckConfigRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.DeleteUptimeCheckConfigRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=834,
    serialized_end=880,
)


_LISTUPTIMECHECKIPSREQUEST = _descriptor.Descriptor(
    name="ListUptimeCheckIpsRequest",
    full_name="google.monitoring.v3.ListUptimeCheckIpsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.monitoring.v3.ListUptimeCheckIpsRequest.page_size",
            index=0,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.monitoring.v3.ListUptimeCheckIpsRequest.page_token",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=882,
    serialized_end=948,
)


_LISTUPTIMECHECKIPSRESPONSE = _descriptor.Descriptor(
    name="ListUptimeCheckIpsResponse",
    full_name="google.monitoring.v3.ListUptimeCheckIpsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="uptime_check_ips",
            full_name="google.monitoring.v3.ListUptimeCheckIpsResponse.uptime_check_ips",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.monitoring.v3.ListUptimeCheckIpsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=950,
    serialized_end=1066,
)

_LISTUPTIMECHECKCONFIGSRESPONSE.fields_by_name[
    "uptime_check_configs"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG
)
_CREATEUPTIMECHECKCONFIGREQUEST.fields_by_name[
    "uptime_check_config"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG
)
_UPDATEUPTIMECHECKCONFIGREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEUPTIMECHECKCONFIGREQUEST.fields_by_name[
    "uptime_check_config"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG
)
_LISTUPTIMECHECKIPSRESPONSE.fields_by_name[
    "uptime_check_ips"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKIP
)
DESCRIPTOR.message_types_by_name[
    "ListUptimeCheckConfigsRequest"
] = _LISTUPTIMECHECKCONFIGSREQUEST
DESCRIPTOR.message_types_by_name[
    "ListUptimeCheckConfigsResponse"
] = _LISTUPTIMECHECKCONFIGSRESPONSE
DESCRIPTOR.message_types_by_name[
    "GetUptimeCheckConfigRequest"
] = _GETUPTIMECHECKCONFIGREQUEST
DESCRIPTOR.message_types_by_name[
    "CreateUptimeCheckConfigRequest"
] = _CREATEUPTIMECHECKCONFIGREQUEST
DESCRIPTOR.message_types_by_name[
    "UpdateUptimeCheckConfigRequest"
] = _UPDATEUPTIMECHECKCONFIGREQUEST
DESCRIPTOR.message_types_by_name[
    "DeleteUptimeCheckConfigRequest"
] = _DELETEUPTIMECHECKCONFIGREQUEST
DESCRIPTOR.message_types_by_name[
    "ListUptimeCheckIpsRequest"
] = _LISTUPTIMECHECKIPSREQUEST
DESCRIPTOR.message_types_by_name[
    "ListUptimeCheckIpsResponse"
] = _LISTUPTIMECHECKIPSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListUptimeCheckConfigsRequest = _reflection.GeneratedProtocolMessageType(
    "ListUptimeCheckConfigsRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTUPTIMECHECKCONFIGSREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``ListUptimeCheckConfigs`` request.
  
  
  Attributes:
      parent:
          The project whose Uptime check configurations are listed. The
          format is ``projects/[PROJECT_ID]``.
      page_size:
          The maximum number of results to return in a single response.
          The server may further constrain the maximum number of results
          returned in a single page. If the page\_size is <=0, the
          server will decide the number of results to be returned.
      page_token:
          If this field is not empty then it must contain the
          ``nextPageToken`` value returned by a previous call to this
          method. Using this field causes the method to return more
          results from the previous method call.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListUptimeCheckConfigsRequest)
    ),
)
_sym_db.RegisterMessage(ListUptimeCheckConfigsRequest)

ListUptimeCheckConfigsResponse = _reflection.GeneratedProtocolMessageType(
    "ListUptimeCheckConfigsResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTUPTIMECHECKCONFIGSRESPONSE,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``ListUptimeCheckConfigs`` response.
  
  
  Attributes:
      uptime_check_configs:
          The returned Uptime check configurations.
      next_page_token:
          This field represents the pagination token to retrieve the
          next page of results. If the value is empty, it means no
          further results for the request. To retrieve the next page of
          results, the value of the next\_page\_token is passed to the
          subsequent List method call (in the request message's
          page\_token field).
      total_size:
          The total number of Uptime check configurations for the
          project, irrespective of any pagination.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListUptimeCheckConfigsResponse)
    ),
)
_sym_db.RegisterMessage(ListUptimeCheckConfigsResponse)

GetUptimeCheckConfigRequest = _reflection.GeneratedProtocolMessageType(
    "GetUptimeCheckConfigRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GETUPTIMECHECKCONFIGREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``GetUptimeCheckConfig`` request.
  
  
  Attributes:
      name:
          The Uptime check configuration to retrieve. The format is ``pr
          ojects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID]``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.GetUptimeCheckConfigRequest)
    ),
)
_sym_db.RegisterMessage(GetUptimeCheckConfigRequest)

CreateUptimeCheckConfigRequest = _reflection.GeneratedProtocolMessageType(
    "CreateUptimeCheckConfigRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CREATEUPTIMECHECKCONFIGREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``CreateUptimeCheckConfig`` request.
  
  
  Attributes:
      parent:
          The project in which to create the Uptime check. The format is
          ``projects/[PROJECT_ID]``.
      uptime_check_config:
          The new Uptime check configuration.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.CreateUptimeCheckConfigRequest)
    ),
)
_sym_db.RegisterMessage(CreateUptimeCheckConfigRequest)

UpdateUptimeCheckConfigRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateUptimeCheckConfigRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_UPDATEUPTIMECHECKCONFIGREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``UpdateUptimeCheckConfig`` request.
  
  
  Attributes:
      update_mask:
          Optional. If present, only the listed fields in the current
          Uptime check configuration are updated with values from the
          new configuration. If this field is empty, then the current
          configuration is completely replaced with the new
          configuration.
      uptime_check_config:
          Required. If an ``updateMask`` has been specified, this field
          gives the values for the set of fields mentioned in the
          ``updateMask``. If an ``updateMask`` has not been given, this
          Uptime check configuration replaces the current configuration.
          If a field is mentioned in ``updateMask`` but the corresonding
          field is omitted in this partial Uptime check configuration,
          it has the effect of deleting/clearing the field from the
          configuration on the server.  The following fields can be
          updated: ``display_name``, ``http_check``, ``tcp_check``,
          ``timeout``, ``content_matchers``, and ``selected_regions``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.UpdateUptimeCheckConfigRequest)
    ),
)
_sym_db.RegisterMessage(UpdateUptimeCheckConfigRequest)

DeleteUptimeCheckConfigRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteUptimeCheckConfigRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETEUPTIMECHECKCONFIGREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``DeleteUptimeCheckConfig`` request.
  
  
  Attributes:
      name:
          The Uptime check configuration to delete. The format is ``proj
          ects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID]``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.DeleteUptimeCheckConfigRequest)
    ),
)
_sym_db.RegisterMessage(DeleteUptimeCheckConfigRequest)

ListUptimeCheckIpsRequest = _reflection.GeneratedProtocolMessageType(
    "ListUptimeCheckIpsRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTUPTIMECHECKIPSREQUEST,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``ListUptimeCheckIps`` request.
  
  
  Attributes:
      page_size:
          The maximum number of results to return in a single response.
          The server may further constrain the maximum number of results
          returned in a single page. If the page\_size is <=0, the
          server will decide the number of results to be returned. NOTE:
          this field is not yet implemented
      page_token:
          If this field is not empty then it must contain the
          ``nextPageToken`` value returned by a previous call to this
          method. Using this field causes the method to return more
          results from the previous method call. NOTE: this field is not
          yet implemented
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListUptimeCheckIpsRequest)
    ),
)
_sym_db.RegisterMessage(ListUptimeCheckIpsRequest)

ListUptimeCheckIpsResponse = _reflection.GeneratedProtocolMessageType(
    "ListUptimeCheckIpsResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTUPTIMECHECKIPSRESPONSE,
        __module__="google.cloud.monitoring_v3.proto.uptime_service_pb2",
        __doc__="""The protocol for the ``ListUptimeCheckIps`` response.
  
  
  Attributes:
      uptime_check_ips:
          The returned list of IP addresses (including region and
          location) that the checkers run from.
      next_page_token:
          This field represents the pagination token to retrieve the
          next page of results. If the value is empty, it means no
          further results for the request. To retrieve the next page of
          results, the value of the next\_page\_token is passed to the
          subsequent List method call (in the request message's
          page\_token field). NOTE: this field is not yet implemented
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListUptimeCheckIpsResponse)
    ),
)
_sym_db.RegisterMessage(ListUptimeCheckIpsResponse)


DESCRIPTOR._options = None

_UPTIMECHECKSERVICE = _descriptor.ServiceDescriptor(
    name="UptimeCheckService",
    full_name="google.monitoring.v3.UptimeCheckService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\031monitoring.googleapis.com\322A\211\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read"
    ),
    serialized_start=1069,
    serialized_end=2336,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListUptimeCheckConfigs",
            full_name="google.monitoring.v3.UptimeCheckService.ListUptimeCheckConfigs",
            index=0,
            containing_service=None,
            input_type=_LISTUPTIMECHECKCONFIGSREQUEST,
            output_type=_LISTUPTIMECHECKCONFIGSRESPONSE,
            serialized_options=_b(
                "\202\323\344\223\002,\022*/v3/{parent=projects/*}/uptimeCheckConfigs"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="GetUptimeCheckConfig",
            full_name="google.monitoring.v3.UptimeCheckService.GetUptimeCheckConfig",
            index=1,
            containing_service=None,
            input_type=_GETUPTIMECHECKCONFIGREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG,
            serialized_options=_b(
                "\202\323\344\223\002,\022*/v3/{name=projects/*/uptimeCheckConfigs/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="CreateUptimeCheckConfig",
            full_name="google.monitoring.v3.UptimeCheckService.CreateUptimeCheckConfig",
            index=2,
            containing_service=None,
            input_type=_CREATEUPTIMECHECKCONFIGREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG,
            serialized_options=_b(
                '\202\323\344\223\002A"*/v3/{parent=projects/*}/uptimeCheckConfigs:\023uptime_check_config'
            ),
        ),
        _descriptor.MethodDescriptor(
            name="UpdateUptimeCheckConfig",
            full_name="google.monitoring.v3.UptimeCheckService.UpdateUptimeCheckConfig",
            index=3,
            containing_service=None,
            input_type=_UPDATEUPTIMECHECKCONFIGREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_uptime__pb2._UPTIMECHECKCONFIG,
            serialized_options=_b(
                "\202\323\344\223\002U2>/v3/{uptime_check_config.name=projects/*/uptimeCheckConfigs/*}:\023uptime_check_config"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="DeleteUptimeCheckConfig",
            full_name="google.monitoring.v3.UptimeCheckService.DeleteUptimeCheckConfig",
            index=4,
            containing_service=None,
            input_type=_DELETEUPTIMECHECKCONFIGREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=_b(
                "\202\323\344\223\002,**/v3/{name=projects/*/uptimeCheckConfigs/*}"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="ListUptimeCheckIps",
            full_name="google.monitoring.v3.UptimeCheckService.ListUptimeCheckIps",
            index=5,
            containing_service=None,
            input_type=_LISTUPTIMECHECKIPSREQUEST,
            output_type=_LISTUPTIMECHECKIPSRESPONSE,
            serialized_options=_b("\202\323\344\223\002\024\022\022/v3/uptimeCheckIps"),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_UPTIMECHECKSERVICE)

DESCRIPTOR.services_by_name["UptimeCheckService"] = _UPTIMECHECKSERVICE

# @@protoc_insertion_point(module_scope)
