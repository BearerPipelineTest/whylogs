# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x1a\x1cgoogle/protobuf/struct.proto\"~\n\x08\x44\x61taType\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x0e.DataType.Type\"T\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04NULL\x10\x01\x12\x0e\n\nFRACTIONAL\x10\x02\x12\x0c\n\x08INTEGRAL\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\x12\n\n\x06STRING\x10\x05\"0\n\x10HllSketchMessage\x12\x0e\n\x06sketch\x18\x01 \x01(\x0c\x12\x0c\n\x04lg_k\x18\x02 \x01(\x05\">\n\x1a\x46requentItemsSketchMessage\x12\x0e\n\x06sketch\x18\x01 \x01(\x0c\x12\x10\n\x08lg_max_k\x18\x02 \x01(\x05\"K\n\x10KllSketchMessage\x12\x0e\n\x06sketch\x18\x01 \x01(\x0c\x12\r\n\x01k\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x0c\n\x04mean\x18\x03 \x01(\x01\x12\n\n\x02m2\x18\x04 \x01(\x01\"\x82\x02\n\x0eTrackerMessage\x12\x0b\n\x01n\x18\x01 \x01(\x03H\x00\x12\x0b\n\x01\x64\x18\x02 \x01(\x01H\x00\x12\x1a\n\x10serialized_bytes\x18\x03 \x01(\x0cH\x00\x12\x35\n\x0e\x66requent_items\x18\x04 \x01(\x0b\x32\x1b.FrequentItemsSketchMessageH\x00\x12\x30\n\x13\x63\x61rdinality_tracker\x18\x05 \x01(\x0b\x32\x11.HllSketchMessageH\x00\x12&\n\thistogram\x18\x06 \x01(\x0b\x32\x11.KllSketchMessageH\x00\x12 \n\x06\x63ustom\x18\x0f \x01(\x0b\x32\x0e.PluginMessageH\x00\x42\x07\n\x05value\"q\n\nPluginType\x12\x19\n\x11plugin_class_name\x18\x01 \x01(\t\x12&\n\x08language\x18\x02 \x01(\x0e\x32\x14.PluginType.Language\" \n\x08Language\x12\n\n\x06PYTHON\x10\x00\x12\x08\n\x04JAVA\x10\x01\"\x8f\x01\n\rPluginMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x0cplugin_types\x18\x02 \x03(\x0b\x32\x0b.PluginType\x12)\n\x06params\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x1a\n\x10serialized_bytes\x18\x04 \x01(\x0cH\x00\x42\x06\n\x04item\"\x81\x01\n\rColumnMessage\x12.\n\x08trackers\x18\x01 \x03(\x0b\x32\x1c.ColumnMessage.TrackersEntry\x1a@\n\rTrackersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.TrackerMessage:\x02\x38\x01\"\xd4\x02\n\x11\x44\x61tasetProperties\x12\x1c\n\x14schema_major_version\x18\x01 \x01(\r\x12\x1c\n\x14schema_minor_version\x18\x02 \x01(\r\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12\x19\n\x11session_timestamp\x18\x04 \x01(\x03\x12\x16\n\x0e\x64\x61ta_timestamp\x18\x05 \x01(\x03\x12*\n\x04tags\x18\x06 \x03(\x0b\x32\x1c.DatasetProperties.TagsEntry\x12\x32\n\x08metadata\x18\x07 \x03(\x0b\x32 .DatasetProperties.MetadataEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbf\x02\n\x15\x44\x61tasetProfileMessage\x12&\n\nproperties\x18\x01 \x01(\x0b\x32\x12.DatasetProperties\x12\x34\n\x07\x63olumns\x18\x02 \x03(\x0b\x32#.DatasetProfileMessage.ColumnsEntry\x12\x41\n\x0emetric_plugins\x18\x03 \x03(\x0b\x32).DatasetProfileMessage.MetricPluginsEntry\x1a>\n\x0c\x43olumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.ColumnMessage:\x02\x38\x01\x1a\x45\n\x12MetricPluginsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.TrackerMessage:\x02\x38\x01\"\x1d\n\x0c\x43ountMessage\x12\r\n\x05value\x18\x01 \x01(\x03\x42&\n\x18\x63om.whylogs.core.messageB\x08MessagesP\x01\x62\x06proto3')



_DATATYPE = DESCRIPTOR.message_types_by_name['DataType']
_HLLSKETCHMESSAGE = DESCRIPTOR.message_types_by_name['HllSketchMessage']
_FREQUENTITEMSSKETCHMESSAGE = DESCRIPTOR.message_types_by_name['FrequentItemsSketchMessage']
_KLLSKETCHMESSAGE = DESCRIPTOR.message_types_by_name['KllSketchMessage']
_TRACKERMESSAGE = DESCRIPTOR.message_types_by_name['TrackerMessage']
_PLUGINTYPE = DESCRIPTOR.message_types_by_name['PluginType']
_PLUGINMESSAGE = DESCRIPTOR.message_types_by_name['PluginMessage']
_COLUMNMESSAGE = DESCRIPTOR.message_types_by_name['ColumnMessage']
_COLUMNMESSAGE_TRACKERSENTRY = _COLUMNMESSAGE.nested_types_by_name['TrackersEntry']
_DATASETPROPERTIES = DESCRIPTOR.message_types_by_name['DatasetProperties']
_DATASETPROPERTIES_TAGSENTRY = _DATASETPROPERTIES.nested_types_by_name['TagsEntry']
_DATASETPROPERTIES_METADATAENTRY = _DATASETPROPERTIES.nested_types_by_name['MetadataEntry']
_DATASETPROFILEMESSAGE = DESCRIPTOR.message_types_by_name['DatasetProfileMessage']
_DATASETPROFILEMESSAGE_COLUMNSENTRY = _DATASETPROFILEMESSAGE.nested_types_by_name['ColumnsEntry']
_DATASETPROFILEMESSAGE_METRICPLUGINSENTRY = _DATASETPROFILEMESSAGE.nested_types_by_name['MetricPluginsEntry']
_COUNTMESSAGE = DESCRIPTOR.message_types_by_name['CountMessage']
_DATATYPE_TYPE = _DATATYPE.enum_types_by_name['Type']
_PLUGINTYPE_LANGUAGE = _PLUGINTYPE.enum_types_by_name['Language']
DataType = _reflection.GeneratedProtocolMessageType('DataType', (_message.Message,), {
  'DESCRIPTOR' : _DATATYPE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:DataType)
  })
_sym_db.RegisterMessage(DataType)

HllSketchMessage = _reflection.GeneratedProtocolMessageType('HllSketchMessage', (_message.Message,), {
  'DESCRIPTOR' : _HLLSKETCHMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:HllSketchMessage)
  })
_sym_db.RegisterMessage(HllSketchMessage)

FrequentItemsSketchMessage = _reflection.GeneratedProtocolMessageType('FrequentItemsSketchMessage', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENTITEMSSKETCHMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:FrequentItemsSketchMessage)
  })
_sym_db.RegisterMessage(FrequentItemsSketchMessage)

KllSketchMessage = _reflection.GeneratedProtocolMessageType('KllSketchMessage', (_message.Message,), {
  'DESCRIPTOR' : _KLLSKETCHMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:KllSketchMessage)
  })
_sym_db.RegisterMessage(KllSketchMessage)

TrackerMessage = _reflection.GeneratedProtocolMessageType('TrackerMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRACKERMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:TrackerMessage)
  })
_sym_db.RegisterMessage(TrackerMessage)

PluginType = _reflection.GeneratedProtocolMessageType('PluginType', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINTYPE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:PluginType)
  })
_sym_db.RegisterMessage(PluginType)

PluginMessage = _reflection.GeneratedProtocolMessageType('PluginMessage', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:PluginMessage)
  })
_sym_db.RegisterMessage(PluginMessage)

ColumnMessage = _reflection.GeneratedProtocolMessageType('ColumnMessage', (_message.Message,), {

  'TrackersEntry' : _reflection.GeneratedProtocolMessageType('TrackersEntry', (_message.Message,), {
    'DESCRIPTOR' : _COLUMNMESSAGE_TRACKERSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:ColumnMessage.TrackersEntry)
    })
  ,
  'DESCRIPTOR' : _COLUMNMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ColumnMessage)
  })
_sym_db.RegisterMessage(ColumnMessage)
_sym_db.RegisterMessage(ColumnMessage.TrackersEntry)

DatasetProperties = _reflection.GeneratedProtocolMessageType('DatasetProperties', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETPROPERTIES_TAGSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:DatasetProperties.TagsEntry)
    })
  ,

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETPROPERTIES_METADATAENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:DatasetProperties.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _DATASETPROPERTIES,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:DatasetProperties)
  })
_sym_db.RegisterMessage(DatasetProperties)
_sym_db.RegisterMessage(DatasetProperties.TagsEntry)
_sym_db.RegisterMessage(DatasetProperties.MetadataEntry)

DatasetProfileMessage = _reflection.GeneratedProtocolMessageType('DatasetProfileMessage', (_message.Message,), {

  'ColumnsEntry' : _reflection.GeneratedProtocolMessageType('ColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETPROFILEMESSAGE_COLUMNSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:DatasetProfileMessage.ColumnsEntry)
    })
  ,

  'MetricPluginsEntry' : _reflection.GeneratedProtocolMessageType('MetricPluginsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASETPROFILEMESSAGE_METRICPLUGINSENTRY,
    '__module__' : 'messages_pb2'
    # @@protoc_insertion_point(class_scope:DatasetProfileMessage.MetricPluginsEntry)
    })
  ,
  'DESCRIPTOR' : _DATASETPROFILEMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:DatasetProfileMessage)
  })
_sym_db.RegisterMessage(DatasetProfileMessage)
_sym_db.RegisterMessage(DatasetProfileMessage.ColumnsEntry)
_sym_db.RegisterMessage(DatasetProfileMessage.MetricPluginsEntry)

CountMessage = _reflection.GeneratedProtocolMessageType('CountMessage', (_message.Message,), {
  'DESCRIPTOR' : _COUNTMESSAGE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:CountMessage)
  })
_sym_db.RegisterMessage(CountMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.whylogs.core.messageB\010MessagesP\001'
  _KLLSKETCHMESSAGE.fields_by_name['k']._options = None
  _KLLSKETCHMESSAGE.fields_by_name['k']._serialized_options = b'\030\001'
  _COLUMNMESSAGE_TRACKERSENTRY._options = None
  _COLUMNMESSAGE_TRACKERSENTRY._serialized_options = b'8\001'
  _DATASETPROPERTIES_TAGSENTRY._options = None
  _DATASETPROPERTIES_TAGSENTRY._serialized_options = b'8\001'
  _DATASETPROPERTIES_METADATAENTRY._options = None
  _DATASETPROPERTIES_METADATAENTRY._serialized_options = b'8\001'
  _DATASETPROFILEMESSAGE_COLUMNSENTRY._options = None
  _DATASETPROFILEMESSAGE_COLUMNSENTRY._serialized_options = b'8\001'
  _DATASETPROFILEMESSAGE_METRICPLUGINSENTRY._options = None
  _DATASETPROFILEMESSAGE_METRICPLUGINSENTRY._serialized_options = b'8\001'
  _DATATYPE._serialized_start=48
  _DATATYPE._serialized_end=174
  _DATATYPE_TYPE._serialized_start=90
  _DATATYPE_TYPE._serialized_end=174
  _HLLSKETCHMESSAGE._serialized_start=176
  _HLLSKETCHMESSAGE._serialized_end=224
  _FREQUENTITEMSSKETCHMESSAGE._serialized_start=226
  _FREQUENTITEMSSKETCHMESSAGE._serialized_end=288
  _KLLSKETCHMESSAGE._serialized_start=290
  _KLLSKETCHMESSAGE._serialized_end=365
  _TRACKERMESSAGE._serialized_start=368
  _TRACKERMESSAGE._serialized_end=626
  _PLUGINTYPE._serialized_start=628
  _PLUGINTYPE._serialized_end=741
  _PLUGINTYPE_LANGUAGE._serialized_start=709
  _PLUGINTYPE_LANGUAGE._serialized_end=741
  _PLUGINMESSAGE._serialized_start=744
  _PLUGINMESSAGE._serialized_end=887
  _COLUMNMESSAGE._serialized_start=890
  _COLUMNMESSAGE._serialized_end=1019
  _COLUMNMESSAGE_TRACKERSENTRY._serialized_start=955
  _COLUMNMESSAGE_TRACKERSENTRY._serialized_end=1019
  _DATASETPROPERTIES._serialized_start=1022
  _DATASETPROPERTIES._serialized_end=1362
  _DATASETPROPERTIES_TAGSENTRY._serialized_start=1270
  _DATASETPROPERTIES_TAGSENTRY._serialized_end=1313
  _DATASETPROPERTIES_METADATAENTRY._serialized_start=1315
  _DATASETPROPERTIES_METADATAENTRY._serialized_end=1362
  _DATASETPROFILEMESSAGE._serialized_start=1365
  _DATASETPROFILEMESSAGE._serialized_end=1684
  _DATASETPROFILEMESSAGE_COLUMNSENTRY._serialized_start=1551
  _DATASETPROFILEMESSAGE_COLUMNSENTRY._serialized_end=1613
  _DATASETPROFILEMESSAGE_METRICPLUGINSENTRY._serialized_start=1615
  _DATASETPROFILEMESSAGE_METRICPLUGINSENTRY._serialized_end=1684
  _COUNTMESSAGE._serialized_start=1686
  _COUNTMESSAGE._serialized_end=1715
# @@protoc_insertion_point(module_scope)
