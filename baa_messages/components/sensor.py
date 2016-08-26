import pkgutil
import baa_messages.messages.sensor
from baa_messages.messages.core.ttypes import BAAContext
import baa_messages.messages.sensor.ttypes as st


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

    def create_reading(self, **kwargs):
        if 'context' in kwargs.keys() or 'schema' in kwargs.keys():
            raise ValueError("Cannot provide context / schema as kwargs")

        exec ("from {0}.ttypes import Reading".format(self._sensor_module[self.type]))
        context = BAAContext()
        reading = Reading()
        self._set_attributes(context=context, schema=reading, **kwargs)
        self._set_sensor_context(context)
        sr = st.Reading()
        setattr(sr, self.type, reading)

        return st.SensorReading(context, sr)

    def create_setting(self, **kwargs):
        if 'context' in kwargs.keys() or 'schema' in kwargs.keys():
            raise ValueError("Cannot provide context / schema as kwargs")
        exec ("from {0}.ttypes import Setting".format(self._sensor_module[self.type]))
        context = BAAContext()
        setting = Setting()
        self._set_attributes(context=context, schema=setting, **kwargs)
        self._set_sensor_context(context)
        sensor_setting = st.Setting()
        setattr(sensor_setting, self.type, setting)

        return st.SensorSetting(context, sensor_setting)

    def create_report(self, context=BAAContext(), readings=[], settings=[], **kwargs):
        for k,v in kwargs.iteritems():
            if hasattr(context, k):
                setattr(context, k, v)

        self._set_sensor_context(context)
        return st.SensorReport(context, readings, settings)


    # private

    def _set_attributes(self, context=False, schema=False, **kwargs):
        for k, v in kwargs.iteritems():
            if hasattr(context,k):
                setattr(context,k,v)
            elif hasattr(schema, k):
                setattr(schema,k,v)
            else:
                raise ValueError("{0} has no Attribute: {1}".format(self,k))
            #
            #
            # for i in [context, schema]:
            #     if hasattr(i, k) and getattr(i, k) is None:
            #         setattr(i, k, v)
            #     else:
            #         raise ValueError("Cannot pass {0} and {0}.{1} simultaneously".format(i.__class__.__name__,k))

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
                exec ("from {0}.ttypes import Reading as Reading".format(modname))
                exec ("from {0}.ttypes import Setting as Setting".format(modname))

                # This provides a reference to be used to import the specific module by its schema name
                self._sensor_module[modname.split(".")[-1]] = modname





# from baa_messages.publisher.mqtt import Mqtt
# from baa_messages.publisher.publisher import Broadcaster
# from baa_messages.codec import create_network_message
# import time
#
#
# class SensorPublisher(Broadcaster):
#     def __init__(self):
#         self.set_serializer(create_network_message)
#         self.client_id = '123'
#
#     def publish(self, msg, topic=None):
#
#         env = self.serializer(self.client_id,time.time(),msg)
#         print env
#         # if topic is not None:
#         #     self.set_topic(topic)
#         # self._mqtt_pub.publish()
#
#     def destroy(self):
#         pass
#

