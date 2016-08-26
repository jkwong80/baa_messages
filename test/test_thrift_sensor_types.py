#!/usr/bin/env python

import unittest
import pkgutil
import baa_messages.messages.sensor as s
import time
import baa_messages.codec as bc
from baa_messages.util import get_time


class TestSensorTypes(unittest.TestCase):
    def test_individual_constructors(self):
        print '\nTesting Construction of all Sensor Schemas...'
        package = s
        prefix = package.__name__ + "."
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            if ispkg:
                print "Found submodule %s (is a package: %s)" % (modname, ispkg)
                module = __import__(modname, fromlist="dummy")
                exec("from {0}.ttypes import Reading as Reading".format(modname))
                exec("from {0}.ttypes import Setting as Setting".format(modname))

                print "Imported", module

                print 'Constructing Reading'
                reading=Reading()
                self.assertIsInstance(reading,module.ttypes.Reading)
                print 'Constructing Setting'
                setting = Setting()
                self.assertIsInstance(setting,module.ttypes.Setting)

        def get_reading(modname):
            exec ("from {0}.ttypes import Reading as Reading".format(modname))

        def get_setting(modname):
            exec ("from {0}.ttypes import Setting as Setting".format(modname))

        self.assertRaises(ImportError, get_reading, "bunny")
        self.assertRaises(ImportError, get_setting, "bunny")

    def test_sensor(self):
        # Testing Parameters
        parent_id = "Bugs Bunny"
        timestamp = time.time()
        time_us = get_time(timestamp)
        grlat = 10
        grlng = 10
        gspoll = 1
        gsnull=-5
        ctxlat=20
        ctxlng=50
        sensor_id = 123
        sensor_unit_id = 1

        #Run Test

        print '\nTesting Construction of Sensor...'
        import baa_messages.messages.sensor.gps.ttypes as gt
        import baa_messages.messages.sensor.ttypes as st

        print 'Constructing GPS Reading'
        gr=gt.Reading(latitude=grlat,longitude=grlng)
        print 'Constructing GPS Setting'
        gs = gt.Setting(poll_frequency=gspoll, null_value=gsnull)
        from baa_messages.messages.core.ttypes import BAAContext
        ctx = BAAContext(parent_id=parent_id, timestamp_us=time_us, timestamp_remainder=0,
                         location=[ctxlat, ctxlng], sensor_id=sensor_id, sensor_unit_id=sensor_unit_id)


        print 'Constructing Sensor Reading'
        sr = st.SensorReading(ctx,st.Reading(gr))
        print 'Constructing Sensor Setting'
        ss = st.SensorSetting(ctx,st.Setting(gs))

        print 'Constructing Sensor Report'
        my_rep = st.SensorReport(ctx,[sr,sr],[ss])

        print 'Serializing Sensor Report into TBinary'
        payload_bytes = bc.encode_object(my_rep,bc.Encoding.TBINARY)


        # print payload_bytes
        jd = bc.decode_payload(payload_bytes,bc.Encoding.TBINARY,bc.get_class_name(my_rep))

        self.assertEqual(jd.context.timestamp_us,time_us)
        self.assertEqual(jd.context.timestamp_remainder, 0)
        # exit()
        # print "Time: {0}, ctx.timestamp: {1}  json time: {2}".format(Decimal(jd["context"]["timestamp"]),ctx.timestamp,Decimal(timestamp))
        #
        # print "Testing Timestamp {0} == {1}: {2}".format(float(jd["context"]["timestamp"]),float(timestamp),float(jd["context"]["timestamp"]) == float(timestamp))
        # self.assertEqual(jd["context"]["parent_id"], parent_id, msg="Invalid context.parent_id in encoding")
        # self.assertEqual(float(jd["context"]["timestamp"]), timestamp, msg = "Invalid context.timestamp in encoding")
        # self.assertEqual(jd["readings"][0]["reading"]["gps"]["latitude"],grlat, msg = "Invalid gps.lat in encoding")
        # print payload_bytes



if __name__=="__main__":
    unittest.main()

