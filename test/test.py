#!/usr/bin/env python

import unittest
import time
from baa_messages.messages.sensor.ttypes import GPSReading
from baa_messages.messages.core.ttypes import BAAMessage
import baa_messages.codec as bc
import time
from baa_messages.messages.core.ttypes import BAAContext


class TestCodec(unittest.TestCase):
    ctx = BAAContext(parent_id='Seth S', timestamp=time.time(), location=[0.0, 0.0], sensor_id=123, sensor_unit_id=1)
    x = GPSReading(context=ctx, latitude=10, longitude=20)

    def test_encoding(self):
        print 'Testing codec.encode_object...'

        print 'Testing Binary encoding...'
        msg = bc.encode_object(self.x, encoding=bc.Encoding.TBINARY)
        y = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(self.x))
        self.assertIsInstance(y, self.x.__class__, "Decoding yields invalid class")

        print 'Testing TJSON encoding...'
        msg = bc.encode_object(self.x, encoding=bc.Encoding.TJSON)
        y = bc.decode_payload(msg, bc.Encoding.TJSON, bc.get_class_name(self.x))
        self.assertIsInstance(y, self.x.__class__, "Decoding yields invalid class")

        print 'Testing TSimpleJSON encoding...'
        msg = bc.encode_object(self.x, encoding=bc.Encoding.TSIMPLEJSON)
        with self.assertRaises(ValueError):
            y = bc.decode_payload(msg, bc.Encoding.TSIMPLEJSON, bc.get_class_name(self.x))

    def test_network_message(self):
        print 'Testing Network Messages...'
        net_msg = bc.create_network_message('Seth Sender',time.time(),
                                            self.x,receiver_id="Cory Receiver",
                                            latitude=38.5, longitude=-75.2)
        msg = bc.encode_network_message(net_msg)
        y = bc.decode_network_message(msg)
        self.assertIsInstance(y,net_msg.__class__,"Decoding yielded invalid class")
