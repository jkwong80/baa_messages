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



class GammaReading:
  """
  Attributes:
   - start_time
   - duration
   - live_time
   - num_channels
   - adc_channel_counts
   - channel_energies
   - gross_counts
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'start_time', None, None, ), # 1
    (2, TType.DOUBLE, 'duration', None, None, ), # 2
    (3, TType.DOUBLE, 'live_time', None, None, ), # 3
    (4, TType.I32, 'num_channels', None, None, ), # 4
    (5, TType.MAP, 'adc_channel_counts', (TType.I32,None,TType.I32,None), None, ), # 5
    (6, TType.MAP, 'channel_energies', (TType.DOUBLE,None,TType.DOUBLE,None), None, ), # 6
    (7, TType.DOUBLE, 'gross_counts', None, None, ), # 7
  )

  def __init__(self, start_time=None, duration=None, live_time=None, num_channels=None, adc_channel_counts=None, channel_energies=None, gross_counts=None,):
    self.start_time = start_time
    self.duration = duration
    self.live_time = live_time
    self.num_channels = num_channels
    self.adc_channel_counts = adc_channel_counts
    self.channel_energies = channel_energies
    self.gross_counts = gross_counts

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
        if ftype == TType.DOUBLE:
          self.start_time = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.duration = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.live_time = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.num_channels = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.MAP:
          self.adc_channel_counts = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readI32()
            _val6 = iprot.readI32()
            self.adc_channel_counts[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.channel_energies = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin()
          for _i11 in xrange(_size7):
            _key12 = iprot.readDouble()
            _val13 = iprot.readDouble()
            self.channel_energies[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.DOUBLE:
          self.gross_counts = iprot.readDouble()
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
    oprot.writeStructBegin('GammaReading')
    if self.start_time is not None:
      oprot.writeFieldBegin('start_time', TType.DOUBLE, 1)
      oprot.writeDouble(self.start_time)
      oprot.writeFieldEnd()
    if self.duration is not None:
      oprot.writeFieldBegin('duration', TType.DOUBLE, 2)
      oprot.writeDouble(self.duration)
      oprot.writeFieldEnd()
    if self.live_time is not None:
      oprot.writeFieldBegin('live_time', TType.DOUBLE, 3)
      oprot.writeDouble(self.live_time)
      oprot.writeFieldEnd()
    if self.num_channels is not None:
      oprot.writeFieldBegin('num_channels', TType.I32, 4)
      oprot.writeI32(self.num_channels)
      oprot.writeFieldEnd()
    if self.adc_channel_counts is not None:
      oprot.writeFieldBegin('adc_channel_counts', TType.MAP, 5)
      oprot.writeMapBegin(TType.I32, TType.I32, len(self.adc_channel_counts))
      for kiter14,viter15 in self.adc_channel_counts.items():
        oprot.writeI32(kiter14)
        oprot.writeI32(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.channel_energies is not None:
      oprot.writeFieldBegin('channel_energies', TType.MAP, 6)
      oprot.writeMapBegin(TType.DOUBLE, TType.DOUBLE, len(self.channel_energies))
      for kiter16,viter17 in self.channel_energies.items():
        oprot.writeDouble(kiter16)
        oprot.writeDouble(viter17)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.gross_counts is not None:
      oprot.writeFieldBegin('gross_counts', TType.DOUBLE, 7)
      oprot.writeDouble(self.gross_counts)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.start_time is None:
      raise TProtocol.TProtocolException(message='Required field start_time is unset!')
    if self.duration is None:
      raise TProtocol.TProtocolException(message='Required field duration is unset!')
    if self.live_time is None:
      raise TProtocol.TProtocolException(message='Required field live_time is unset!')
    if self.num_channels is None:
      raise TProtocol.TProtocolException(message='Required field num_channels is unset!')
    if self.adc_channel_counts is None:
      raise TProtocol.TProtocolException(message='Required field adc_channel_counts is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.start_time)
    value = (value * 31) ^ hash(self.duration)
    value = (value * 31) ^ hash(self.live_time)
    value = (value * 31) ^ hash(self.num_channels)
    value = (value * 31) ^ hash(self.adc_channel_counts)
    value = (value * 31) ^ hash(self.channel_energies)
    value = (value * 31) ^ hash(self.gross_counts)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GammaSetting:
  """
  Attributes:
   - sample_frequency
   - fine_gain
   - high_voltage
   - lld
   - uld
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'sample_frequency', None, None, ), # 1
    (2, TType.DOUBLE, 'fine_gain', None, None, ), # 2
    (3, TType.DOUBLE, 'high_voltage', None, None, ), # 3
    (4, TType.DOUBLE, 'lld', None, None, ), # 4
    (5, TType.DOUBLE, 'uld', None, None, ), # 5
  )

  def __init__(self, sample_frequency=None, fine_gain=None, high_voltage=None, lld=None, uld=None,):
    self.sample_frequency = sample_frequency
    self.fine_gain = fine_gain
    self.high_voltage = high_voltage
    self.lld = lld
    self.uld = uld

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
        if ftype == TType.DOUBLE:
          self.sample_frequency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.fine_gain = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.high_voltage = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.lld = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.DOUBLE:
          self.uld = iprot.readDouble()
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
    oprot.writeStructBegin('GammaSetting')
    if self.sample_frequency is not None:
      oprot.writeFieldBegin('sample_frequency', TType.DOUBLE, 1)
      oprot.writeDouble(self.sample_frequency)
      oprot.writeFieldEnd()
    if self.fine_gain is not None:
      oprot.writeFieldBegin('fine_gain', TType.DOUBLE, 2)
      oprot.writeDouble(self.fine_gain)
      oprot.writeFieldEnd()
    if self.high_voltage is not None:
      oprot.writeFieldBegin('high_voltage', TType.DOUBLE, 3)
      oprot.writeDouble(self.high_voltage)
      oprot.writeFieldEnd()
    if self.lld is not None:
      oprot.writeFieldBegin('lld', TType.DOUBLE, 4)
      oprot.writeDouble(self.lld)
      oprot.writeFieldEnd()
    if self.uld is not None:
      oprot.writeFieldBegin('uld', TType.DOUBLE, 5)
      oprot.writeDouble(self.uld)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sample_frequency)
    value = (value * 31) ^ hash(self.fine_gain)
    value = (value * 31) ^ hash(self.high_voltage)
    value = (value * 31) ^ hash(self.lld)
    value = (value * 31) ^ hash(self.uld)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
