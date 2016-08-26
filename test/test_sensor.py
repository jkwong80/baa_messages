#!/usr/bin/env python

import unittest
import time
from baa_messages.components.sensor_unit import SensorUnit
from baa_messages.messages.core.ttypes import BAAContext
import support.helpers as helpers
import support.factories as factories


class TestSensor(unittest.TestCase):
    def test_sensor_validates_sensor_id(self):
        sensor_unit = factories.new_sensor_unit()
        with self.assertRaises(ValueError):
            sensor_unit.add_sensor(type="gps")

    def test_sensor_validates_sensor_type(self):
        sensor_unit = factories.new_sensor_unit()
        with self.assertRaises(ValueError):
            sensor_unit.add_sensor(type="time", id=2)

    def test_sensor_has_a_sensor_unit(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gps", id=2)
        assert sensor_unit == sensor.sensor_unit

    def test_sensor_attributes(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        assert sensor.sensor_unit_id == sensor_unit.id
        assert sensor.type == "gps"
        assert sensor.name == "test"

    def test_sensor_reading(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        t = time.time()
        report = sensor.create_reading(timestamp_us=t, latitude=lat, longitude=lng)

        assert report.reading.gps.latitude == lat
        assert report.reading.gps.longitude == lng
        assert report.context.sensor_id == sensor.id
        assert report.context.sensor_unit_id == sensor_unit.id
        assert sensor.latest_reading == report

    # NEEDS IMPLEMENTING!!!!
    @unittest.skip("not implemented yet")
    def test_buidling_reports_casts_time_intelligently(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        t = time.time()
        report = sensor.create_reading(timestamp_us=t, latitude=lat, longitude=lng)

        #self.fail(report.context.timestamp_us, helpers.get_time(t))
        self.fail("use the encoded time intellegently")



    def test_sensor_reading_uses_context(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        x = time.time()
        context = BAAContext(timestamp_us=1234)
        with self.assertRaises(ValueError):
            report = sensor.create_reading(context=context, timestamp_us=x, latitude=lat, longitude=lng)
        report = sensor.create_reading(timestamp_us=x, latitude=lat, longitude=lng)

        assert report.context.timestamp_us != 1234
        assert report.context.timestamp_us == x

    def test_sensor_settings(self):
        sensor_unit = factories.new_sensor_unit()
        sensor = sensor_unit.add_sensor(type="gamma", id=2, name="test")
        x = time.time()

        gamma_setting = sensor.create_setting(high_voltage=1000, timestamp_us=x)
        assert gamma_setting.setting.gamma.high_voltage == 1000
        self.assertEqual(gamma_setting.context.timestamp_us, x)
        assert gamma_setting.context.sensor_id == sensor.id
        assert gamma_setting.context.sensor_unit_id == sensor_unit.id
        assert sensor.latest_setting == gamma_setting

if __name__=="__main__":
    unittest.main()
