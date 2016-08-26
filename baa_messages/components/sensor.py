import pkgutil
import baa_messages.messages.sensor
from baa_messages.messages.core.ttypes import BAAContext
import baa_messages.messages.sensor.ttypes as st
from baa_messages.codec import create_network_message
from baa_messages.util import get_time

class SensorFactory:
    def create_sensor(self, id=False, type=False, sensor_unit=False, name="unnamed"):
        return Sensor(id=id, type=type, name=name, sensor_unit=sensor_unit)


class Sensor():
    _sensor_module = {}

    def __init__(self, id=False, type=False, name="unknown", sensor_unit=False):
        self._import_message_schema_submodules()
        if type not in self._sensor_module:
            raise ValueError("Invalid sensor_type: {0} in {1} options include {2}".
                    format(type, "Sensor", self._sensor_module.keys()))

        if id == False:
            raise ValueError("A sensor id is required.")
        if sensor_unit == False:
            raise ValueError("A sensor unit is required.")
        self.id = id
        self.sensor_unit_id = sensor_unit.id
        self.type = type
        self.name = name
        self.sensor_unit = sensor_unit
        self.latest_reading = None
        self.latest_setting = None

    def create_reading(self, **kwargs):
        if 'context' in kwargs.keys() or 'schema' in kwargs.keys():
            raise ValueError("Cannot provide context / schema as kwargs")

        class_name = self._sensor_module[self.type].split(".")[-1].title()
        exec ("from {0}.ttypes import {1}Reading as Reading".
                format(self._sensor_module[self.type], class_name))
        context = BAAContext()
        reading = Reading()
        self._set_attributes(context=context, schema=reading, **kwargs)
        self._set_sensor_context(context)
        sr = st.Reading()
        setattr(sr, self.type, reading)
        reading = st.SensorReading(context, sr)
        reading.validate()
        self.latest_reading = reading

        return reading

    def create_setting(self, **kwargs):
        if 'context' in kwargs.keys() or 'schema' in kwargs.keys():
            raise ValueError("Cannot provide context / schema as kwargs")
        class_name = self._sensor_module[self.type].split(".")[-1].title()
        exec ("from {0}.ttypes import {1}Setting as Setting".
                format(self._sensor_module[self.type], class_name))
        context = BAAContext()
        setting = Setting()
        self._set_attributes(context=context, schema=setting, **kwargs)
        self._set_sensor_context(context)
        sensor_setting = st.Setting()
        setattr(sensor_setting, self.type, setting)
        sensor_setting.validate()
        self.latest_setting = st.SensorSetting(context, sensor_setting)

        return self.latest_setting

    def clear_latest_data(self):
        self.latest_setting = None
        self.latest_reading = None

    # private

    def _set_attributes(self, context=False, schema=False, **kwargs):
        for k, v in kwargs.iteritems():
            if hasattr(context,k):
                # TODO: lets do something smart here with the timestamp
                #if(k == "timestamp_us"):
                #   v = get_time(str(v))
                setattr(context,k,v)
            elif hasattr(schema, k):
                setattr(schema,k,v)
            else:
                raise ValueError("{0} has no Attribute: {1}".format(self,k))

    def _set_sensor_context(self, context):
        context.sensor_id = self.id
        context.sensor_unit_id = self.sensor_unit.id

    def _import_message_schema_submodules(self):
        # Finding all sensor schemas
        package = baa_messages.messages.sensor
        prefix = package.__name__ + "."
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            if ispkg:
                module = __import__(modname, fromlist="dummy")
                # Importing the reading and setting from each sensor schema
                exec ("from {0}.ttypes import *".format(modname))
                # This provides a reference to be used to import the specific module by its schema name
                self._sensor_module[modname.split(".")[-1]] = modname
