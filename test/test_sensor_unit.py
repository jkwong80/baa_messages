#!/usr/bin/env python
from support import factories
import unittest, pkgutil, os
import baa_messages.components.sensor_unit as su

class TestSensorUnit(unittest.TestCase):
    def test_sensor_unit_attributes(self):
        unit = su.SensorUnit(id=1, name="user defined name", cloud_publish=False)
        assert unit.id == 1
        assert unit.name == "user defined name"

    def test_sensor_unit_has_many_sensors(self):
        unit = factories.new_sensor_unit(id=1)
        unit.add_sensor(type="gps", id=2)
        unit.add_sensor(type="gamma", id=3)
        assert len(unit.sensors) == 2

    def test_sensor_knows_its_sensor_unit(self):
        unit = factories.new_sensor_unit(id=1)
        sensor = unit.add_sensor(type="gps", id=2)
        assert sensor.sensor_unit_id == 1
        assert sensor.sensor_unit == unit

    def validates_params(self):
        assertRaises(ValueError, su.SensorUnit(name="user defined name", cloud_publish=False))

    def test_get_sensor(self):
        unit = factories.new_sensor_unit(id=1)
        sensor = unit.add_sensor(type="gps", id=2)
        assert unit.get_sensor(2) == sensor

    def test_unit_location(self):
        unit = factories.new_sensor_unit(id=1)
        unit.set_latitude(123)
        unit.set_longitude(456)
        assert unit.latitude == 123
        assert unit.longitude == 456

if __name__=="__main__":
    unittest.main()

