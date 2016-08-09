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



class Context:
  """
  Attributes:
   - parent_id
   - timestamp
   - location
   - sensor_id
   - sensor_unit_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'parent_id', None, None, ), # 1
    (2, TType.DOUBLE, 'timestamp', None, None, ), # 2
    (3, TType.LIST, 'location', (TType.DOUBLE,None), None, ), # 3
    (4, TType.I32, 'sensor_id', None, None, ), # 4
    (5, TType.I32, 'sensor_unit_id', None, None, ), # 5
  )

  def __init__(self, parent_id=None, timestamp=None, location=None, sensor_id=None, sensor_unit_id=None,):
    self.parent_id = parent_id
    self.timestamp = timestamp
    self.location = location
    self.sensor_id = sensor_id
    self.sensor_unit_id = sensor_unit_id

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
          self.parent_id = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.timestamp = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.location = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readDouble()
            self.location.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.sensor_id = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.sensor_unit_id = iprot.readI32()
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
    oprot.writeStructBegin('Context')
    if self.parent_id is not None:
      oprot.writeFieldBegin('parent_id', TType.STRING, 1)
      oprot.writeString(self.parent_id)
      oprot.writeFieldEnd()
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.DOUBLE, 2)
      oprot.writeDouble(self.timestamp)
      oprot.writeFieldEnd()
    if self.location is not None:
      oprot.writeFieldBegin('location', TType.LIST, 3)
      oprot.writeListBegin(TType.DOUBLE, len(self.location))
      for iter6 in self.location:
        oprot.writeDouble(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.sensor_id is not None:
      oprot.writeFieldBegin('sensor_id', TType.I32, 4)
      oprot.writeI32(self.sensor_id)
      oprot.writeFieldEnd()
    if self.sensor_unit_id is not None:
      oprot.writeFieldBegin('sensor_unit_id', TType.I32, 5)
      oprot.writeI32(self.sensor_unit_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.parent_id is None:
      raise TProtocol.TProtocolException(message='Required field parent_id is unset!')
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.parent_id)
    value = (value * 31) ^ hash(self.timestamp)
    value = (value * 31) ^ hash(self.location)
    value = (value * 31) ^ hash(self.sensor_id)
    value = (value * 31) ^ hash(self.sensor_unit_id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BAAMessage:
  """
  Attributes:
   - context
   - payload_class
   - payload
   - receiver_id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'context', (Context, Context.thrift_spec), None, ), # 1
    (2, TType.STRING, 'payload_class', None, None, ), # 2
    (3, TType.STRING, 'payload', None, None, ), # 3
    (4, TType.STRING, 'receiver_id', None, None, ), # 4
  )

  def __init__(self, context=None, payload_class=None, payload=None, receiver_id=None,):
    self.context = context
    self.payload_class = payload_class
    self.payload = payload
    self.receiver_id = receiver_id

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
        if ftype == TType.STRUCT:
          self.context = Context()
          self.context.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.payload_class = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.payload = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.receiver_id = iprot.readString()
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
    if self.context is not None:
      oprot.writeFieldBegin('context', TType.STRUCT, 1)
      self.context.write(oprot)
      oprot.writeFieldEnd()
    if self.payload_class is not None:
      oprot.writeFieldBegin('payload_class', TType.STRING, 2)
      oprot.writeString(self.payload_class)
      oprot.writeFieldEnd()
    if self.payload is not None:
      oprot.writeFieldBegin('payload', TType.STRING, 3)
      oprot.writeString(self.payload)
      oprot.writeFieldEnd()
    if self.receiver_id is not None:
      oprot.writeFieldBegin('receiver_id', TType.STRING, 4)
      oprot.writeString(self.receiver_id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.context is None:
      raise TProtocol.TProtocolException(message='Required field context is unset!')
    if self.payload_class is None:
      raise TProtocol.TProtocolException(message='Required field payload_class is unset!')
    if self.payload is None:
      raise TProtocol.TProtocolException(message='Required field payload is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.context)
    value = (value * 31) ^ hash(self.payload_class)
    value = (value * 31) ^ hash(self.payload)
    value = (value * 31) ^ hash(self.receiver_id)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
