from enum import Enum
from thrift.transport import TTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from thrift.protocol.TJSONProtocol import TJSONProtocol
import lz4f
import base64
from baa_messages.messages.core.ttypes import BAAMessage
OutputType = Enum("BINARY","JSON")


def get_class_object(schema_class):
    payload_class = schema_class.split(".")
    cls_ns = '.'.join(payload_class[:-1])
    cls_name = payload_class[-1]
    exec ('from {0} import {1}'.format(cls_ns, cls_name))
    thrift_cls = eval(cls_name)
    return thrift_cls


def encode_object(schema_object, output_type=None):
    if output_type not in OutputType:
        raise ValueError("Unexpected type {0} in {1}".format(output_type, "encode_object"))

    if output_type == OutputType.BINARY:
        # Packaging the Schema Object as Binary
        trans = TTransport.TMemoryBuffer()
        p = TBinaryProtocolAccelerated(trans)
        schema_object.write(p)
        msg = trans.getvalue()
        msg = bytearray(lz4f.compressFrame(msg))
        trans.close()
        msg = base64.urlsafe_b64encode(msg)
        return msg

    elif output_type == OutputType.JSON:
        # Packaging the Schema Object as JSON
        trans = TTransport.TMemoryBuffer()
        p = TJSONProtocol(trans)
        schema_object.write(p)
        msg = trans.getvalue()
        trans.close()
        return msg


def decode_binary(byte_string, schema_class):
    thrift_cls = get_class_object(schema_class)
    thrift_obj = thrift_cls()
    byte_string = base64.urlsafe_b64decode(byte_string)
    ctx = lz4f.createDecompContext()
    byte_string = str(lz4f.decompressFrame(byte_string,ctx)['decomp'])
    trans = TTransport.TMemoryBuffer(byte_string)
    p = TBinaryProtocolAccelerated(trans)
    thrift_obj.read(p)
    trans.close()
    return thrift_obj


def decode_json(json_string, schema_class):
    thrift_cls = get_class_object(schema_class)
    trans = TTransport.TMemoryBuffer(json_string)
    p = TJSONProtocol(trans)
    thrift_obj = thrift_cls()
    thrift_obj.read(p)
    trans.close()
    return thrift_obj


def encode_network_message(sender_id,message_time,schema_object,receiver_id=None,latitude=None,longitude=None):
    payload_string = encode_object(schema_object,output_type=OutputType.BINARY)
    payload_cls = str(schema_object.__class__)
    print 'encode_netowrk_message...'
    if latitude is None:
        latitude = 0.0

    if longitude is None:
        longitude = 0.0
        
    envelope = BAAMessage(sender_id=sender_id,
                          message_time=message_time,
                          payload_class=payload_cls,
                          payload=payload_string,
                          receiver_id=receiver_id,
                          gps_coordinates=[float(latitude),float(longitude)])
    
    msg = encode_object(envelope,output_type=OutputType.JSON)
    return msg


def decode_network_message(msg_string):
    envelope = decode_json(msg_string,str(BAAMessage().__class__))
    return envelope

