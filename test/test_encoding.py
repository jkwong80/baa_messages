#!/usr/bin/env python

import unittest
import pkgutil
import baa_messages.messages.sensor as s
import time
import baa_messages.codec as bc
from baa_messages.components.sensor import SensorFactory
from baa_messages.util import get_time

from decimal import Decimal,getcontext


class TestEncoding(unittest.TestCase):
    def test_timestamp_encoding(self):
        sf = SensorFactory()

        t = time.time()+1.2345678e-18
        ts, r = get_time(t,15)
        sr = sf.create_sensor_reading("gps",timestamp=ts)

        getcontext().prec = 15
        tf1 = Decimal(t)
        ts, r = get_time(tf1,15)
        sr2 = sf.create_sensor_reading("gps",timestamp=ts)

        getcontext().prec = 28
        tf2 = Decimal(t)
        ts, r = get_time(tf2,28)
        sr3 = sf.create_sensor_reading("gps",timestamp=ts)

        msg = bc.encode_object(sr, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertEqual(srd.context.timestamp, sr.context.timestamp)

        msg = bc.encode_object(sr2, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertEqual(srd.context.timestamp, sr.context.timestamp)

        msg = bc.encode_object(sr3, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertNotEqual(srd.context.timestamp, sr.context.timestamp)


if __name__=="__main__":
    unittest.main()

#