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



class BAAMessage:
  """
  Attributes:
   - sender_id
   - message_time
   - payload_class
   - payload
   - receiver_id
   - latitude
   - longitude
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'sender_id', None, None, ), # 1
    (2, TType.DOUBLE, 'message_time', None, None, ), # 2
    (3, TType.STRING, 'payload_class', None, None, ), # 3
    (4, TType.STRING, 'payload', None, None, ), # 4
    (5, TType.STRING, 'receiver_id', None, None, ), # 5
    (6, TType.DOUBLE, 'latitude', None, None, ), # 6
    (7, TType.DOUBLE, 'longitude', None, None, ), # 7
  )

  def __init__(self, sender_id=None, message_time=None, payload_class=None, payload=None, receiver_id=None, latitude=None, longitude=None,):
    self.sender_id = sender_id
    self.message_time = message_time
    self.payload_class = payload_class
    self.payload = payload
    self.receiver_id = receiver_id
    self.latitude = latitude
    self.longitude = longitude

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
        if ftype == TType.DOUBLE:
          self.message_time = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.payload_class = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.payload = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.receiver_id = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.DOUBLE:
          self.latitude = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.DOUBLE:
          self.longitude = iprot.readDouble()
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
    oprot.writeStructBegin('BAAMessage')
    if self.sender_id is not None:
      oprot.writeFieldBegin('sender_id', TType.STRING, 1)
      oprot.writeString(self.sender_id)
      oprot.writeFieldEnd()
    if self.message_time is not None:
      oprot.writeFieldBegin('message_time', TType.DOUBLE, 2)
      oprot.writeDouble(self.message_time)
      oprot.writeFieldEnd()
    if self.payload_class is not None:
      oprot.writeFieldBegin('payload_class', TType.STRING, 3)
      oprot.writeString(self.payload_class)
      oprot.writeFieldEnd()
    if self.payload is not None:
      oprot.writeFieldBegin('payload', TType.STRING, 4)
      oprot.writeString(self.payload)
      oprot.writeFieldEnd()
    if self.receiver_id is not None:
      oprot.writeFieldBegin('receiver_id', TType.STRING, 5)
      oprot.writeString(self.receiver_id)
      oprot.writeFieldEnd()
    if self.latitude is not None:
      oprot.writeFieldBegin('latitude', TType.DOUBLE, 6)
      oprot.writeDouble(self.latitude)
      oprot.writeFieldEnd()
    if self.longitude is not None:
      oprot.writeFieldBegin('longitude', TType.DOUBLE, 7)
      oprot.writeDouble(self.longitude)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.sender_id is None:
      raise TProtocol.TProtocolException(message='Required field sender_id is unset!')
    if self.message_time is None:
      raise TProtocol.TProtocolException(message='Required field message_time is unset!')
    if self.payload_class is None:
      raise TProtocol.TProtocolException(message='Required field payload_class is unset!')
    if self.payload is None:
      raise TProtocol.TProtocolException(message='Required field payload is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sender_id)
    value = (value * 31) ^ hash(self.message_time)
    value = (value * 31) ^ hash(self.payload_class)
    value = (value * 31) ^ hash(self.payload)
    value = (value * 31) ^ hash(self.receiver_id)
    value = (value * 31) ^ hash(self.latitude)
    value = (value * 31) ^ hash(self.longitude)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)