#!/usr/bin/env python

import unittest
import pkgutil
import baa_messages.messages.sensor as s
import time
import baa_messages.codec as bc
from baa_messages.util import get_time
#
# import json
# from decimal import Decimal
# from baa_messages.messages.sensor.gps.ttypes import Reading as GPSReading
# import baa_messages.codec as bc
# import time
# from baa_messages.messages.core.ttypes import BAAContext
# from baa_messages.messages.sensor.ttypes import SensorReading
# import baa_messages


class TestSensor(unittest.TestCase):
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
        time_us, remainder = get_time(timestamp, 20)
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
        ctx = BAAContext(parent_id=parent_id, timestamp=time_us, timestamp_remainder=remainder,
                         location=[ctxlat, ctxlng], sensor_id=sensor_id, sensor_unit_id=sensor_unit_id)

        print 'TIME::: {0}, {0:15.10f}, ctx.time: {1:15.10f} '.format(timestamp,ctx.timestamp)




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

        print 'Decoded Time: {0:15.10f}  Orig time: {1:15.10f}'.format(jd.context.timestamp, timestamp)
        self.assertEqual(jd.context.timestamp,time_us)
        self.assertEqual(jd.context.timestamp_remainder, remainder)
        # exit()
        # print "Time: {0}, ctx.timestamp: {1}  json time: {2}".format(Decimal(jd["context"]["timestamp"]),ctx.timestamp,Decimal(timestamp))
        #
        # print "Testing Timestamp {0} == {1}: {2}".format(float(jd["context"]["timestamp"]),float(timestamp),float(jd["context"]["timestamp"]) == float(timestamp))
        # self.assertEqual(jd["context"]["parent_id"], parent_id, msg="Invalid context.parent_id in encoding")
        # self.assertEqual(float(jd["context"]["timestamp"]), timestamp, msg = "Invalid context.timestamp in encoding")
        # self.assertEqual(jd["readings"][0]["reading"]["gps"]["latitude"],grlat, msg = "Invalid gps.lat in encoding")
        # print payload_bytes

    def test_sensor_factory(self):
        print 'Testing components.sensor.SensorFactory...'

        from baa_messages.components.sensor import SensorFactory
        sf = SensorFactory()
        gr = sf.create_sensor_reading("gps")
        self.assertRaises(ValueError,sf.create_sensor_reading,"time")

        x = time.time()
        lat = 10
        lng = 20
        gr2 = sf.create_sensor_reading("gps",
                                       timestamp=x,
                                       latitude=lat,
                                       longitude=lng)
        self.assertEqual(gr2.context.timestamp,x)
        self.assertEqual(gr2.reading.gps.latitude,lat)
        self.assertEqual(gr2.reading.gps.longitude,lng)


        temp_reading = sf.create_sensor_reading("temperature",temperature=98.7)
        gamma_reading = sf.create_sensor_setting("gamma",high_voltage=1000)

        gt = sf.create_sensor_setting("gps",timestamp=time.time())

        sr = sf.create_sensor_report(readings=[gr,gr2],settings=[gt])
        payload_bytes = bc.encode_object(sr,bc.Encoding.TBINARY)


if __name__=="__main__":
    unittest.main()

#
# class TestCodec(unittest.TestCase):
#     ctx = BAAContext(parent_id='Seth S', timestamp=time.time(), location=[0.0, 0.0], sensor_id=123, sensor_unit_id=1)
#     x = GPSReading(context=ctx, latitude=10, longitude=20)
#
#     def test_encoding(self):
#         print 'Testing codec.encode_object...'
#
#         print 'Testing Binary encoding...'
#         msg = bc.encode_object(self.x, encoding=bc.Encoding.TBINARY)
#         y = bc.decode_payload(msg, bc.Encoding.TBINARY, bc.get_class_name(self.x))
#         self.assertIsInstance(y, self.x.__class__, "Decoding yields invalid class")
#
#         print 'Testing TJSON encoding...'
#         msg = bc.encode_object(self.x, encoding=bc.Encoding.TJSON)
#         y = bc.decode_payload(msg, bc.Encoding.TJSON, bc.get_class_name(self.x))
#         self.assertIsInstance(y, self.x.__class__, "Decoding yields invalid class")
#
#         print 'Testing TSimpleJSON encoding...'
#         msg = bc.encode_object(self.x, encoding=bc.Encoding.TSIMPLEJSON)
#         with self.assertRaises(ValueError):
#             y = bc.decode_payload(msg, bc.Encoding.TSIMPLEJSON, bc.get_class_name(self.x))
#
#     def test_network_message(self):
#         print 'Testing Network Messages...'
#         net_msg = bc.create_network_message('Seth Sender', time.time(),
#                                             self.x,receiver_id="Cory Receiver",
#                                             latitude=38.5, longitude=-75.2)
#         msg = bc.encode_network_message(net_msg)
#         y = bc.decode_network_message(msg)
#         self.assertIsInstance(y,net_msg.__class__,"Decoding yielded invalid class")
#


