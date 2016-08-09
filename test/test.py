#!/usr/bin/env python

import unittest
import time
from baa_messages.messages.sensor.ttypes import GPSReading
from baa_messages.messages.core.ttypes import BAAMessage
import baa_messages.codec as bc
import time
from baa_messages.messages.core.ttypes import BAAContext

ctx = BAAContext(parent_id='Seth S',timestamp=time.time(),location=[0.0,0.0],sensor_id=123,sensor_unit_id=1)


class ApiBase(unittest.TestCase):
    def test_dev(self) :
        print 'Hello'
        self.assertEqual(True, True)

    def test_json_codec(self):
        try:
            x = GPSReading(context=ctx,
                           latitude=0,
                           longitude=0
                           )
            msg = bc.encode_object(x,bc.OutputType.JSON)
            self.assertEqual(type(msg),type(str()),'Encoding yields invalid type')

            y = bc.decode_json(msg,str(x.__class__))
            self.assertIsInstance(y,x.__class__,'Decoding yields invalid class')

        except Exception as e:
            print 'Exception Occured: ', e
            self.assertEqual(True,False,'An unexpected exception occured')

    def test_binary_codec(self):
        try:
            x = GPSReading(context=ctx,
                           latitude=0,
                           longitude=0
                           )
            msg = bc.encode_object(x, bc.OutputType.BINARY)
            self.assertTrue(type(msg) == type(str()) or type(msg) == type(bytearray()),"Encoding yielded invalid type")

            y = bc.decode_binary(msg, str(x.__class__))
            self.assertIsInstance(y, x.__class__, 'Decoding yields invalid class')

        except Exception as e:
            print 'Exception Occured: ',e
            self.assertEqual(True, False)


    def test_network_message_codec(self):
        print " Starting test_netowr..."
        try:
            x = GPSReading(context=ctx,
                           latitude=0,
                           longitude=0
                           )
            print 'I got to here'
            msg = bc.encode_network_message('sender 1',
                                            time.time(),
                                            x)
            print 'I got to here as well...msg'
            self.assertTrue(type(msg) == type(str()) , "Encoding yielded invalid type")

            y = bc.decode_network_message(msg)
            self.assertIsInstance(y, BAAMessage().__class__, 'Decoding yields invalid class')

            ypobj = bc.decode_binary(y.payload,y.payload_class)
            self.assertIsInstance(ypobj,x.__class__,'Decoding payload yielded invalid type')
        except Exception as e:
            print 'Exception Occured: ', e
            self.assertEqual(True, False)
