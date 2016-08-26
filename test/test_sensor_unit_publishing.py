#!/usr/bin/env python

import unittest, pkgutil, os, time
import baa_messages.components.sensor_unit as su
import support.helpers as helpers
from baa_messages.util import get_time
from mock import patch
from baa_messages.publisher.mqtt import Mqtt

import support.helpers as helpers
import support.factories as factories


class TestSensorUnitPublishing(unittest.TestCase):
    def test_sensor_unit_cloud_publish_data(self):
        with patch.object(Mqtt, 'publish', return_value=True) as mock_method:
            with patch.object(Mqtt, '__aws_setup__', return_value=True) as mock_aws:
                unit = su.SensorUnit(id=1, name="user defined name")
                sensor = unit.add_sensor(type="gps", id=2)

                t = helpers.formatted_time()
                reading = factories.create_sensor_gps_reading(sensor, t)
                with patch.object(unit, '_wrap_message_with_unit_context', return_value=reading) as mock_wrapper:
                    unit.publish()
        mock_method.assert_any_call(reading, topic='prod/1/2/data')

    def test_sensor_unit_cloud_publish_setting(self):
        with patch.object(Mqtt, 'publish', return_value=True) as mock_method:
            with patch.object(Mqtt, '__aws_setup__', return_value=True) as mock_aws:
                unit = su.SensorUnit(id=1, name="user defined name")
                sensor = unit.add_sensor(type="gamma", id=2)

                t = helpers.formatted_time()
                setting = sensor.create_setting(high_voltage=1000, timestamp_us=t)

                with patch.object(unit, '_wrap_message_with_unit_context', return_value=setting) as mock_wrapper:
                    unit.publish()
        mock_method.assert_any_call(setting, topic='prod/1/2/setting')

    def test_publish_mode_off(self):
        with patch.object(Mqtt, 'publish', return_value=True) as mock_method:
            with patch.object(Mqtt, '__aws_setup__', return_value=True) as mock_aws:
                unit = su.SensorUnit(id=1, name="user defined name", publishing=False)
                sensor = unit.add_sensor(type="gamma", id=2)
                t = helpers.formatted_time()
                setting = sensor.create_setting(high_voltage=1000, timestamp_us=time)
                unit.publish()
        mock_method.assert_not_called()

    def test_wont_double_publish(self):
        with patch.object(Mqtt, 'publish', return_value=True) as mock_method:
            with patch.object(Mqtt, '__aws_setup__', return_value=True) as mock_aws:
                unit = su.SensorUnit(id=1, name="user defined name")
                sensor = unit.add_sensor(type="gamma", id=2)

                t = helpers.formatted_time()
                setting = sensor.create_setting(high_voltage=1000, timestamp_us=time)
                reading = sensor.create_reading(num_channels=32)
                unit.publish()
                assert sensor.latest_setting == None
                assert sensor.latest_reading == None

    def test_wraps_messages_with_context(self):
        unit = su.SensorUnit(id=1, name="user defined name", publishing=False)
        unit.set_latitude(123)
        unit.set_longitude(456)
        sensor = unit.add_sensor(type="gamma", id=2)

        time = helpers.formatted_time()
        setting = sensor.create_setting(high_voltage=1000, timestamp_us=time)
        reading = sensor.create_reading(num_channels=32)
        wrapped_setting = unit._wrap_message_with_unit_context(setting, timestamp=1472503525.281369)
        wrapped_reading = unit._wrap_message_with_unit_context(reading, timestamp=1472503525.281369)

        self.assertEqual(wrapped_setting.context.timestamp_us, 1472503525281369)
        self.assertEqual(wrapped_setting.context.location, [float(123), float(456)])
        self.assertEqual(wrapped_setting.context.parent_id, "Sensor Unit 1")

        self.assertEqual(wrapped_reading.context.timestamp_us, 1472503525281369)
        self.assertEqual(wrapped_setting.payload_class, str(setting.__class__))
        self.assertEqual(wrapped_reading.payload_class, str(reading.__class__))

    def test_sensor_unit_wrapper_uses_correct_time_format(self):
        unit = su.SensorUnit(id=1, name="user defined name", publishing=False)
        sensor = unit.add_sensor(type="gamma", id=2)

        t = helpers.formatted_time()
        setting = sensor.create_setting(high_voltage=1000, timestamp_us=t)
        p_time = time.time()
        wrapped_setting = unit._wrap_message_with_unit_context(setting, timestamp=1472503525.281369, publish_time=p_time)
        self.assertEqual(wrapped_setting.context.timestamp_us, 1472503525281369)
        published_at = wrapped_setting.context.publish_timestamp_us
        self.assertEqual(published_at, get_time(p_time))


    def test_publish_time_sync(self):
        unit = su.SensorUnit(id=1, name="user defined name", publishing=False)
        sensor = unit.add_sensor(type="gamma", id=2)

        time = helpers.formatted_time()
        setting = sensor.create_setting(high_voltage=1000, timestamp_us=time)
        reading = sensor.create_reading(num_channels=32)
        wrapped_setting = unit._wrap_message_with_unit_context(setting)
        wrapped_reading = unit._wrap_message_with_unit_context(reading)

        self.assertEqual(wrapped_setting.context.publish_timestamp_us, wrapped_reading.context.publish_timestamp_us)


    def test_custom_publisher(self):
        pass

if __name__=="__main__":
    unittest.main()

