#!/usr/bin/env python

import unittest
import pkgutil
import baa_messages.messages.sensor as s
import time
import baa_messages.codec as bc
from baa_messages.components.sensor_unit import SensorUnit
from baa_messages.util import get_time
from support import factories
from decimal import Decimal,getcontext


class TestEncoding(unittest.TestCase):
    def test_timestamp_encoding(self):
        sensor_unit = factories.new_sensor_unit(id=1)
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")

        t = time.time()

        t1 = t + 1.2345678e-18
        ts = get_time(t1)
        sr = sensor.create_reading(timestamp_us=ts)


        ts = get_time(t + 1.45698e-7)
        sr2 = sensor.create_reading(timestamp_us=ts)

        ts = get_time(t + 3.42e-5)
        sr3 = sensor.create_reading(timestamp_us=ts)

        msg = bc.encode_object(sr, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertEqual(srd.context.timestamp_us, sr.context.timestamp_us)

        msg = bc.encode_object(sr2, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertEqual(srd.context.timestamp_us, sr.context.timestamp_us)

        msg = bc.encode_object(sr3, bc.Encoding.TBINARY)
        srd = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(sr))
        self.assertNotEqual(srd.context.timestamp_us, sr.context.timestamp_us)


if __name__=="__main__":
    unittest.main()

#
