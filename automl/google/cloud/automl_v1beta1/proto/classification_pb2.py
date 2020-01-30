# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/classification.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    temporal_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_temporal__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/classification.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1B\023ClassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1"
    ),
    serialized_pb=_b(
        '\n6google/cloud/automl_v1beta1/proto/classification.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x30google/cloud/automl_v1beta1/proto/temporal.proto")\n\x18\x43lassificationAnnotation\x12\r\n\x05score\x18\x01 \x01(\x02"\xc7\x01\n\x1dVideoClassificationAnnotation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12X\n\x19\x63lassification_annotation\x18\x02 \x01(\x0b\x32\x35.google.cloud.automl.v1beta1.ClassificationAnnotation\x12>\n\x0ctime_segment\x18\x03 \x01(\x0b\x32(.google.cloud.automl.v1beta1.TimeSegment"\xa9\x07\n\x1f\x43lassificationEvaluationMetrics\x12\x0e\n\x06\x61u_prc\x18\x01 \x01(\x02\x12\x17\n\x0b\x62\x61se_au_prc\x18\x02 \x01(\x02\x42\x02\x18\x01\x12\x0e\n\x06\x61u_roc\x18\x06 \x01(\x02\x12\x10\n\x08log_loss\x18\x07 \x01(\x02\x12u\n\x18\x63onfidence_metrics_entry\x18\x03 \x03(\x0b\x32S.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry\x12\x66\n\x10\x63onfusion_matrix\x18\x04 \x01(\x0b\x32L.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix\x12\x1a\n\x12\x61nnotation_spec_id\x18\x05 \x03(\t\x1a\xfc\x02\n\x16\x43onfidenceMetricsEntry\x12\x1c\n\x14\x63onfidence_threshold\x18\x01 \x01(\x02\x12\x1a\n\x12position_threshold\x18\x0e \x01(\x05\x12\x0e\n\x06recall\x18\x02 \x01(\x02\x12\x11\n\tprecision\x18\x03 \x01(\x02\x12\x1b\n\x13\x66\x61lse_positive_rate\x18\x08 \x01(\x02\x12\x10\n\x08\x66\x31_score\x18\x04 \x01(\x02\x12\x12\n\nrecall_at1\x18\x05 \x01(\x02\x12\x15\n\rprecision_at1\x18\x06 \x01(\x02\x12\x1f\n\x17\x66\x61lse_positive_rate_at1\x18\t \x01(\x02\x12\x14\n\x0c\x66\x31_score_at1\x18\x07 \x01(\x02\x12\x1b\n\x13true_positive_count\x18\n \x01(\x03\x12\x1c\n\x14\x66\x61lse_positive_count\x18\x0b \x01(\x03\x12\x1c\n\x14\x66\x61lse_negative_count\x18\x0c \x01(\x03\x12\x1b\n\x13true_negative_count\x18\r \x01(\x03\x1a\xc0\x01\n\x0f\x43onfusionMatrix\x12\x1a\n\x12\x61nnotation_spec_id\x18\x01 \x03(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x03(\t\x12]\n\x03row\x18\x02 \x03(\x0b\x32P.google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row\x1a\x1c\n\x03Row\x12\x15\n\rexample_count\x18\x01 \x03(\x05*Y\n\x12\x43lassificationType\x12#\n\x1f\x43LASSIFICATION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nMULTICLASS\x10\x01\x12\x0e\n\nMULTILABEL\x10\x02\x42\xb8\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\x13\x43lassificationProtoZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_temporal__pb2.DESCRIPTOR,
    ],
)

_CLASSIFICATIONTYPE = _descriptor.EnumDescriptor(
    name="ClassificationType",
    full_name="google.cloud.automl.v1beta1.ClassificationType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CLASSIFICATION_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MULTICLASS", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MULTILABEL", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1352,
    serialized_end=1441,
)
_sym_db.RegisterEnumDescriptor(_CLASSIFICATIONTYPE)

ClassificationType = enum_type_wrapper.EnumTypeWrapper(_CLASSIFICATIONTYPE)
CLASSIFICATION_TYPE_UNSPECIFIED = 0
MULTICLASS = 1
MULTILABEL = 2


_CLASSIFICATIONANNOTATION = _descriptor.Descriptor(
    name="ClassificationAnnotation",
    full_name="google.cloud.automl.v1beta1.ClassificationAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.automl.v1beta1.ClassificationAnnotation.score",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_start=167,
    serialized_end=208,
)


_VIDEOCLASSIFICATIONANNOTATION = _descriptor.Descriptor(
    name="VideoClassificationAnnotation",
    full_name="google.cloud.automl.v1beta1.VideoClassificationAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.cloud.automl.v1beta1.VideoClassificationAnnotation.type",
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
            name="classification_annotation",
            full_name="google.cloud.automl.v1beta1.VideoClassificationAnnotation.classification_annotation",
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
        _descriptor.FieldDescriptor(
            name="time_segment",
            full_name="google.cloud.automl.v1beta1.VideoClassificationAnnotation.time_segment",
            index=2,
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
    serialized_start=211,
    serialized_end=410,
)


_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY = _descriptor.Descriptor(
    name="ConfidenceMetricsEntry",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="confidence_threshold",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.confidence_threshold",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="position_threshold",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.position_threshold",
            index=1,
            number=14,
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
            name="recall",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.recall",
            index=2,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="precision",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.precision",
            index=3,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="false_positive_rate",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.false_positive_rate",
            index=4,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="f1_score",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.f1_score",
            index=5,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="recall_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.recall_at1",
            index=6,
            number=5,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="precision_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.precision_at1",
            index=7,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="false_positive_rate_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.false_positive_rate_at1",
            index=8,
            number=9,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="f1_score_at1",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.f1_score_at1",
            index=9,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="true_positive_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.true_positive_count",
            index=10,
            number=10,
            type=3,
            cpp_type=2,
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
            name="false_positive_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.false_positive_count",
            index=11,
            number=11,
            type=3,
            cpp_type=2,
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
            name="false_negative_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.false_negative_count",
            index=12,
            number=12,
            type=3,
            cpp_type=2,
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
            name="true_negative_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.true_negative_count",
            index=13,
            number=13,
            type=3,
            cpp_type=2,
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
    serialized_start=775,
    serialized_end=1155,
)

_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW = _descriptor.Descriptor(
    name="Row",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="example_count",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row.example_count",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
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
    serialized_start=1322,
    serialized_end=1350,
)

_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX = _descriptor.Descriptor(
    name="ConfusionMatrix",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.annotation_spec_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
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
            name="display_name",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.display_name",
            index=1,
            number=3,
            type=9,
            cpp_type=9,
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
            name="row",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.row",
            index=2,
            number=2,
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
    ],
    extensions=[],
    nested_types=[_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1158,
    serialized_end=1350,
)

_CLASSIFICATIONEVALUATIONMETRICS = _descriptor.Descriptor(
    name="ClassificationEvaluationMetrics",
    full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="au_prc",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.au_prc",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="base_au_prc",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.base_au_prc",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\030\001"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="au_roc",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.au_roc",
            index=2,
            number=6,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="log_loss",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.log_loss",
            index=3,
            number=7,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="confidence_metrics_entry",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.confidence_metrics_entry",
            index=4,
            number=3,
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
            name="confusion_matrix",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.confusion_matrix",
            index=5,
            number=4,
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
            name="annotation_spec_id",
            full_name="google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.annotation_spec_id",
            index=6,
            number=5,
            type=9,
            cpp_type=9,
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
    ],
    extensions=[],
    nested_types=[
        _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
        _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=413,
    serialized_end=1350,
)

_VIDEOCLASSIFICATIONANNOTATION.fields_by_name[
    "classification_annotation"
].message_type = _CLASSIFICATIONANNOTATION
_VIDEOCLASSIFICATIONANNOTATION.fields_by_name[
    "time_segment"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_temporal__pb2._TIMESEGMENT
)
_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS
)
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX
)
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX.fields_by_name[
    "row"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW
_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX.containing_type = (
    _CLASSIFICATIONEVALUATIONMETRICS
)
_CLASSIFICATIONEVALUATIONMETRICS.fields_by_name[
    "confidence_metrics_entry"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY
_CLASSIFICATIONEVALUATIONMETRICS.fields_by_name[
    "confusion_matrix"
].message_type = _CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX
DESCRIPTOR.message_types_by_name["ClassificationAnnotation"] = _CLASSIFICATIONANNOTATION
DESCRIPTOR.message_types_by_name[
    "VideoClassificationAnnotation"
] = _VIDEOCLASSIFICATIONANNOTATION
DESCRIPTOR.message_types_by_name[
    "ClassificationEvaluationMetrics"
] = _CLASSIFICATIONEVALUATIONMETRICS
DESCRIPTOR.enum_types_by_name["ClassificationType"] = _CLASSIFICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassificationAnnotation = _reflection.GeneratedProtocolMessageType(
    "ClassificationAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CLASSIFICATIONANNOTATION,
        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
        __doc__="""Contains annotation details specific to classification.
  
  
  Attributes:
      score:
          Output only. A confidence estimate between 0.0 and 1.0. A
          higher value means greater confidence that the annotation is
          positive. If a user approves an annotation as negative or
          positive, the score value remains unchanged. If a user creates
          an annotation, the score is 0 for negative or 1 for positive.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationAnnotation)
    ),
)
_sym_db.RegisterMessage(ClassificationAnnotation)

VideoClassificationAnnotation = _reflection.GeneratedProtocolMessageType(
    "VideoClassificationAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_VIDEOCLASSIFICATIONANNOTATION,
        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
        __doc__="""Contains annotation details specific to video
  classification.
  
  
  Attributes:
      type:
          Output only. Expresses the type of video classification.
          Possible values:  -  ``segment`` - Classification done on a
          specified by user time segment    of a video. AnnotationSpec
          is answered to be present in that time    segment, if it is
          present in any part of it. The video ML model    evaluations
          are done only for this type of classification.  -  ``shot``-
          Shot-level classification. AutoML Video Intelligence
          determines the boundaries for each camera shot in the entire
          segment    of the video that user specified in the request
          configuration. AutoML    Video Intelligence then returns
          labels and their confidence scores    for each detected shot,
          along with the start and end time of the    shot. WARNING:
          Model evaluation is not done for this classification    type,
          the quality of it depends on training data, but there are no
          metrics provided to describe that quality.  -  ``1s_interval``
          - AutoML Video Intelligence returns labels and their
          confidence scores for each second of the entire segment of the
          video    that user specified in the request configuration.
          WARNING: Model    evaluation is not done for this
          classification type, the quality of    it depends on training
          data, but there are no metrics provided to    describe that
          quality.
      classification_annotation:
          Output only . The classification details of this annotation.
      time_segment:
          Output only . The time segment of the video to which the
          annotation applies.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.VideoClassificationAnnotation)
    ),
)
_sym_db.RegisterMessage(VideoClassificationAnnotation)

ClassificationEvaluationMetrics = _reflection.GeneratedProtocolMessageType(
    "ClassificationEvaluationMetrics",
    (_message.Message,),
    dict(
        ConfidenceMetricsEntry=_reflection.GeneratedProtocolMessageType(
            "ConfidenceMetricsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFIDENCEMETRICSENTRY,
                __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                __doc__="""Metrics for a single confidence threshold.
    
    
    Attributes:
        confidence_threshold:
            Output only. Metrics are computed with an assumption that the
            model never returns predictions with score lower than this
            value.
        position_threshold:
            Output only. Metrics are computed with an assumption that the
            model always returns at most this many predictions (ordered by
            their score, descendingly), but they all still need to meet
            the confidence\_threshold.
        recall:
            Output only. Recall (True Positive Rate) for the given
            confidence threshold.
        precision:
            Output only. Precision for the given confidence threshold.
        false_positive_rate:
            Output only. False Positive Rate for the given confidence
            threshold.
        f1_score:
            Output only. The harmonic mean of recall and precision.
        recall_at1:
            Output only. The Recall (True Positive Rate) when only
            considering the label that has the highest prediction score
            and not below the confidence threshold for each example.
        precision_at1:
            Output only. The precision when only considering the label
            that has the highest prediction score and not below the
            confidence threshold for each example.
        false_positive_rate_at1:
            Output only. The False Positive Rate when only considering the
            label that has the highest prediction score and not below the
            confidence threshold for each example.
        f1_score_at1:
            Output only. The harmonic mean of [recall\_at1][google.cloud.a
            utoml.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetric
            sEntry.recall\_at1] and [precision\_at1][google.cloud.automl.v
            1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.
            precision\_at1].
        true_positive_count:
            Output only. The number of model created labels that match a
            ground truth label.
        false_positive_count:
            Output only. The number of model created labels that do not
            match a ground truth label.
        false_negative_count:
            Output only. The number of ground truth labels that are not
            matched by a model created label.
        true_negative_count:
            Output only. The number of labels that were not created by the
            model, but if they would, they would not match a ground truth
            label.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
            ),
        ),
        ConfusionMatrix=_reflection.GeneratedProtocolMessageType(
            "ConfusionMatrix",
            (_message.Message,),
            dict(
                Row=_reflection.GeneratedProtocolMessageType(
                    "Row",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX_ROW,
                        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                        __doc__="""Output only. A row in the confusion matrix.
      
      
      Attributes:
          example_count:
              Output only. Value of the specific cell in the confusion
              matrix. The number of values each row has (i.e. the length of
              the row) is equal to the length of the ``annotation_spec_id``
              field or, if that one is not populated, length of the [display
              \_name][google.cloud.automl.v1beta1.ClassificationEvaluationMe
              trics.ConfusionMatrix.display\_name] field.
      """,
                        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix.Row)
                    ),
                ),
                DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS_CONFUSIONMATRIX,
                __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
                __doc__="""Confusion matrix of the model running the classification.
    
    
    Attributes:
        annotation_spec_id:
            Output only. IDs of the annotation specs used in the confusion
            matrix. For Tables CLASSIFICATION  [prediction\_type][google.c
            loud.automl.v1beta1.TablesModelMetadata.prediction\_type] only
            list of [annotation\_spec\_display\_name-s][] is populated.
        display_name:
            Output only. Display name of the annotation specs used in the
            confusion matrix, as they were at the moment of the
            evaluation. For Tables CLASSIFICATION  [prediction\_type-s][go
            ogle.cloud.automl.v1beta1.TablesModelMetadata.prediction\_type
            ], distinct values of the target column at the moment of the
            model evaluation are populated here.
        row:
            Output only. Rows in the confusion matrix. The number of rows
            is equal to the size of ``annotation_spec_id``.
            ``row[i].example_count[j]`` is the number of examples that
            have ground truth of the ``annotation_spec_id[i]`` and are
            predicted as ``annotation_spec_id[j]`` by the model being
            evaluated.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics.ConfusionMatrix)
            ),
        ),
        DESCRIPTOR=_CLASSIFICATIONEVALUATIONMETRICS,
        __module__="google.cloud.automl_v1beta1.proto.classification_pb2",
        __doc__="""Model evaluation metrics for classification problems.
  Note: For Video Classification this metrics only describe quality of the
  Video Classification predictions of "segment\_classification" type.
  
  
  Attributes:
      au_prc:
          Output only. The Area Under Precision-Recall Curve metric.
          Micro-averaged for the overall evaluation.
      base_au_prc:
          Output only. The Area Under Precision-Recall Curve metric
          based on priors. Micro-averaged for the overall evaluation.
          Deprecated.
      au_roc:
          Output only. The Area Under Receiver Operating Characteristic
          curve metric. Micro-averaged for the overall evaluation.
      log_loss:
          Output only. The Log Loss metric.
      confidence_metrics_entry:
          Output only. Metrics for each confidence\_threshold in
          0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and
          position\_threshold = INT32\_MAX\_VALUE. ROC and precision-
          recall curves, and other aggregated metrics are derived from
          them. The confidence metrics entries may also be supplied for
          additional values of position\_threshold, but from these no
          aggregated metrics are computed.
      confusion_matrix:
          Output only. Confusion matrix of the evaluation. Only set for
          MULTICLASS classification problems where number of labels is
          no more than 10. Only set for model level evaluation, not for
          evaluation per label.
      annotation_spec_id:
          Output only. The annotation spec ids used for this evaluation.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ClassificationEvaluationMetrics)
    ),
)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfidenceMetricsEntry)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix)
_sym_db.RegisterMessage(ClassificationEvaluationMetrics.ConfusionMatrix.Row)


DESCRIPTOR._options = None
_CLASSIFICATIONEVALUATIONMETRICS.fields_by_name["base_au_prc"]._options = None
# @@protoc_insertion_point(module_scope)
