#!/usr/bin/env python

import unittest, pkgutil, time
import baa_messages.messages.sensor as s
import baa_messages.codec as bc
from baa_messages.util import get_time
from baa_messages.components.sensor import SensorFactory
from baa_messages.components.sensor_unit import SensorUnit
from baa_messages.messages.core.ttypes import BAAContext
import support.helpers as helpers

class TestSensor(unittest.TestCase):
    def test_sensor_validates_sensor_id(self):
        sensor_unit = SensorUnit(id=1)
        with self.assertRaises(ValueError):
            sensor_unit.add_sensor(type="gps")

    def test_sensor_validates_sensor_type(self):
        sensor_unit = SensorUnit(id=1)
        with self.assertRaises(ValueError):
            sensor_unit.add_sensor(type="time", id=2)

    def test_sensor_has_a_sensor_unit(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gps", id=2)
        assert sensor_unit == sensor.sensor_unit

    def test_sensor_attributes(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        assert sensor.sensor_unit_id == sensor_unit.id
        assert sensor.type == "gps"
        assert sensor.name == "test"

    def test_sensor_reading(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        x = time.time()
        report = sensor.create_reading(timestamp=x, latitude=lat, longitude=lng)

        self.assertEqual(report.context.timestamp, x)
        assert report.reading.gps.latitude == lat
        assert report.reading.gps.longitude == lng
        assert report.context.sensor_id == sensor.id
        assert report.context.sensor_unit_id == sensor_unit.id

    def test_sensor_reading_uses_context(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gps", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        x = time.time()
        context = BAAContext(timestamp=1234)
        report = sensor.create_reading(context=context, timestamp=x, latitude=lat, longitude=lng)
        assert report.context.timestamp == 1234

    def test_sensor_settings(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gamma", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        x = time.time()

        gamma_reading = sensor.create_settings(high_voltage=1000, timestamp=x)
        assert gamma_reading.setting.gamma.high_voltage == 1000
        self.assertEqual(gamma_reading.context.timestamp, x)
        assert gamma_reading.context.sensor_id == sensor.id
        assert gamma_reading.context.sensor_unit_id == sensor_unit.id

    def test_sensor_report(self):
        sensor_unit = SensorUnit(id=1)
        sensor = sensor_unit.add_sensor(type="gamma", id=2, name="test")
        lat = helpers.random_coordinate()
        lng = helpers.random_coordinate()
        x = time.time()

        setting = sensor.create_settings(high_voltage=1000, timestamp=x)
        reading = sensor.create_reading(timestamp=x, latitude=lat, longitude=lng)
        report = sensor.create_report(readings=[reading], settings=[setting], timestamp=x)

        assert report.settings[0] == setting
        assert report.readings[0] == reading
        assert report.context.timestamp == x
        assert report.context.sensor_id == sensor.id
        assert report.context.sensor_unit_id == sensor_unit.id


if __name__=="__main__":
    unittest.main()
