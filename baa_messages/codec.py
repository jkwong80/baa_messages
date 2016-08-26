from enum import Enum
from thrift.transport import TTransport
from thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from thrift.protocol.TJSONProtocol import TJSONProtocol,TSimpleJSONProtocol
import lz4f
import base64
from baa_messages.messages.core.ttypes import BAAMessage,BAAContext
# OutputType = Enum("BINARY","JSON")
import warnings

Encoding = Enum("TBINARY","TJSON","TSIMPLEJSON")


def get_class_object(schema_class):
    payload_class = schema_class.split(".")
    cls_ns = '.'.join(payload_class[:-1])
    cls_name = payload_class[-1]
    try:
        exec ('from {0} import {1}'.format(cls_ns, cls_name))
        thrift_cls = eval(cls_name)
        return thrift_cls
    except Exception as e:
        print 'Invalid class name: {0} in {1}'.format(schema_class,'get_class_object')
        raise e


def get_class_name(schema_object):
    return str(schema_object.__class__)


def encode_object(schema_object, encoding=None):

    if encoding == Encoding.TBINARY:
        # Packaging the Schema Object as Binary
        trans = TTransport.TMemoryBuffer()
        p = TBinaryProtocolAccelerated(trans)
        schema_object.write(p)
        msg = trans.getvalue()
        msg = bytearray(lz4f.compressFrame(msg))
        trans.close()
        msg = base64.urlsafe_b64encode(msg)
        return msg

    elif encoding == Encoding.TJSON:
        # Packaging the Schema Object as JSON
        trans = TTransport.TMemoryBuffer()
        p = TJSONProtocol(trans)
        schema_object.write(p)
        msg = trans.getvalue()
        trans.close()
        return msg

    elif encoding == Encoding.TSIMPLEJSON:
        # Packaging the Schema Object as JSON
        trans = TTransport.TMemoryBuffer()
        p = TSimpleJSONProtocol(trans)
        schema_object.write(p)
        msg = trans.getvalue()
        trans.close()
        return msg

    else:
        raise ValueError("Unexpected type {0} in {1}".format(encoding, "encode_object"))


def decode_payload(payload, encoding, schema_class):

    if encoding == Encoding.TBINARY:
        thrift_cls = get_class_object(schema_class)
        thrift_obj = thrift_cls()
        byte_string = base64.urlsafe_b64decode(payload)
        ctx = lz4f.createDecompContext()
        byte_string = str(lz4f.decompressFrame(byte_string, ctx)['decomp'])
        trans = TTransport.TMemoryBuffer(byte_string)
        p = TBinaryProtocolAccelerated(trans)
        thrift_obj.read(p)
        trans.close()
        return thrift_obj
    elif encoding == Encoding.TJSON:
        thrift_cls = get_class_object(schema_class)
        trans = TTransport.TMemoryBuffer(payload)
        p = TJSONProtocol(trans)
        thrift_obj = thrift_cls()
        thrift_obj.read(p)
        trans.close()
        return thrift_obj
    elif encoding == Encoding.TSIMPLEJSON:
        raise ValueError("decode_payload does not support decoding TSimpleJSON at this time...")
    else:
        raise ValueError("Unexpected type {0} in {1}".format(encoding, "decode_payload"))


def create_network_message(sender_id,message_time,schema_object,receiver_id=None,latitude=None,longitude=None):
    payload_string = encode_object(schema_object, encoding=Encoding.TBINARY)
    payload_cls = str(schema_object.__class__)

    if latitude is None:
        latitude = 0.0

    if longitude is None:
        longitude = 0.0

    msg_ctx = BAAContext(parent_id=sender_id, timestamp_us=message_time, location=[float(latitude), float(longitude)])
    envelope = BAAMessage(context=msg_ctx,
                          payload_class=payload_cls,
                          payload=payload_string,
                          receiver_id=receiver_id,
                          )
    return envelope


def encode_network_message(network_message):
    msg = encode_object(network_message, encoding=Encoding.TJSON)
    return msg


def decode_network_message(msg_string):
    envelope = decode_payload(payload=msg_string, encoding=Encoding.TJSON, schema_class=get_class_name(BAAMessage()))
    return envelope

