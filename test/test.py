#!/usr/bin/python2.4

"""Tests for baa messages object objects."""

__author__ = 'Cory Gwin'

import unittest
from baa_messages.messages.sensor.ttypes import GPSReading
from baa_messages.messages.core.ttypes import BAAMessage
import baa_messages.codec as bc
import time


class ApiBase(unittest.TestCase):
    def test_dev(self) :
        self.assertEqual(True, True)

    def test_json_codec(self):
        try:
            x = GPSReading(sensor_id='sensor_1',
                           timestamp=time.time(),
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
            x = GPSReading(sensor_id='sensor_1',
                           timestamp=time.time(),
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
        try:
            x = GPSReading(sensor_id='sensor_1',
                           timestamp=time.time(),
                           latitude=0,
                           longitude=0
                           )
            msg = bc.encode_network_message('sender 1',
                                            time.time(),
                                            x)
            self.assertTrue(type(msg) == type(str()) , "Encoding yielded invalid type")

            y = bc.decode_network_message(msg)
            self.assertIsInstance(y, BAAMessage().__class__, 'Decoding yields invalid class')

            ypobj = bc.decode_binary(y.payload,y.payload_class)
            self.assertIsInstance(ypobj,x.__class__,'Decoding payload yielded invalid type')
        except Exception as e:
            print 'Exception Occured: ', e
            self.assertEqual(True, False)
