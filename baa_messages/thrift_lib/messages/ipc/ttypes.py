#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class RequestType:
  NO_RESP = 1
  RESP = 2

  _VALUES_TO_NAMES = {
    1: "NO_RESP",
    2: "RESP",
  }

  _NAMES_TO_VALUES = {
    "NO_RESP": 1,
    "RESP": 2,
  }


class IPCMessage:
  """
  Attributes:
   - sender_id
   - receiver_id
   - request_type
   - payload
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'sender_id', None, None, ), # 1
    (2, TType.STRING, 'receiver_id', None, None, ), # 2
    (3, TType.I32, 'request_type', None, None, ), # 3
    (4, TType.STRING, 'payload', None, None, ), # 4
  )

  def __init__(self, sender_id=None, receiver_id=None, request_type=None, payload=None,):
    self.sender_id = sender_id
    self.receiver_id = receiver_id
    self.request_type = request_type
    self.payload = payload

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.sender_id = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.receiver_id = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.request_type = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.payload = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IPCMessage')
    if self.sender_id is not None:
      oprot.writeFieldBegin('sender_id', TType.STRING, 1)
      oprot.writeString(self.sender_id)
      oprot.writeFieldEnd()
    if self.receiver_id is not None:
      oprot.writeFieldBegin('receiver_id', TType.STRING, 2)
      oprot.writeString(self.receiver_id)
      oprot.writeFieldEnd()
    if self.request_type is not None:
      oprot.writeFieldBegin('request_type', TType.I32, 3)
      oprot.writeI32(self.request_type)
      oprot.writeFieldEnd()
    if self.payload is not None:
      oprot.writeFieldBegin('payload', TType.STRING, 4)
      oprot.writeString(self.payload)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.sender_id is None:
      raise TProtocol.TProtocolException(message='Required field sender_id is unset!')
    if self.receiver_id is None:
      raise TProtocol.TProtocolException(message='Required field receiver_id is unset!')
    if self.request_type is None:
      raise TProtocol.TProtocolException(message='Required field request_type is unset!')
    if self.payload is None:
      raise TProtocol.TProtocolException(message='Required field payload is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sender_id)
    value = (value * 31) ^ hash(self.receiver_id)
    value = (value * 31) ^ hash(self.request_type)
    value = (value * 31) ^ hash(self.payload)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)