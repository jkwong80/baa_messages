import pkgutil
import baa_messages.messages.sensor
from baa_messages.messages.core.ttypes import BAAContext
import baa_messages.messages.sensor.ttypes as st


class SensorFactory:
    _sensor_module = {}

    def __init__(self):
        self._import_message_schema_submodules()

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

    def create_sensor_reading(self, sensor_type, **kwargs):
        if sensor_type not in self._sensor_module:
            raise ValueError("Invalid sensor_type: {0} in {1}".format(sensor_type,
                                                                      "SensorFactory.create_sensor_reading"))


        #Checking kwargs for context or reading
        if "context" in kwargs.keys():
            ctx = kwargs["context"]
        else:
            ctx = BAAContext()

        if "reading" in kwargs.keys():
            reading = kwargs["reading"]
        else:
            exec ("from {0}.ttypes import Reading".format(self._sensor_module[sensor_type]))
            reading = Reading()

        for k, v in kwargs.iteritems():
            for i in [ctx, reading]:
                if hasattr(i, k):
                    setattr(i, k, v)

        sr = st.Reading()
        setattr(sr,sensor_type,reading)

        return st.SensorReading(ctx, sr)

    def create_sensor_setting(self, sensor_type, **kwargs):
        if sensor_type not in self._sensor_module:
            raise ValueError("Invalid sensor_type: {0} in {1}".format(sensor_type,
                                                                      "SensorFactory.create_sensor_reading"))

        # Checking kwargs for context or reading
        if "context" in kwargs.keys():
            ctx = kwargs["context"]
        else:
            ctx = BAAContext()

        if "setting" in kwargs.keys():
            setting = kwargs["setting"]
        else:
            exec ("from {0}.ttypes import Setting".format(self._sensor_module[sensor_type]))
            setting = Setting()

        for k, v in kwargs.iteritems():
            for i in [ctx, setting]:
                if hasattr(i, k):
                    setattr(i, k, v)

        sensor_setting = st.Setting()
        setattr(sensor_setting, sensor_type, setting)

        return st.SensorSetting(ctx, sensor_setting)

    def create_sensor_report(self,**kwargs):
        if "context" in kwargs.keys():
            ctx = kwargs["context"]
        else:
            ctx = BAAContext()

        if "readings" in kwargs.keys():
            readings = kwargs["readings"]
        else:
            readings = []

        if "settings" in kwargs.keys():
            settings = kwargs["settings"]
        else:
            settings = []

        for k,v in kwargs.iteritems():
            if hasattr(ctx, k):
                setattr(ctx, k, v)

        return st.SensorReport(ctx, readings, settings)











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

