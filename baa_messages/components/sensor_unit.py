from sets import Set
import time
from baa_messages.components.sensor import SensorFactory
import baa_messages.publisher.mqtt as publisher
from baa_messages.messages.core.ttypes import BAAMessage, BAAContext
from baa_messages.util import get_time

class SensorUnit():
    def __init__(self, id=False, name="annonymous",
	cloud_publish=True, env="prod", publishing=True, credentials_dir=False):
        if id == False:
            raise ValueError("A sensor unit id is required.")

        self.id = id
        self.name = name
        self.sensors = Set([])
        self.sensors_by_id = {}
        self.publishers = []
        if cloud_publish and publishing:
            self._setup_cloud_publisher(credentials_dir)
        self.env = env
        self.longitude = None
        self.latitude = None

    def add_sensor(self, type=False, id=False, name=False):
        sensor = SensorFactory().create_sensor(id=id, type=type, sensor_unit = self, name=name)
        self.sensors.add(sensor)
        self.sensors_by_id[sensor.id] = sensor
        return sensor

    def get_sensor(self, sensor_id):
        return self.sensors_by_id[sensor_id]

    def publish(self):
        p_time = time.time()
        for sensor in self.sensors:
            for publisher in self.publishers:
                self._publish_sensor_data(sensor, publisher, publish_time = p_time)
                self._publish_sensor_settings(sensor, publisher, publish_time = p_time)
            sensor.clear_latest_data()

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    # private

    def _wrap_message_with_unit_context(self, message,
            timestamp=time.time(), receiver_id=None, publish_time=time.time()):
        payload_cls = str(message.__class__)
        if self.latitude is None:
            self.latitude = 0.0

        if self.longitude is None:
            self.longitude = 0.0

        msg_ctx = BAAContext(parent_id = "Sensor Unit {}".format(self.id),
                timestamp_us = get_time(timestamp),
                publish_timestamp_us = get_time(publish_time),
                location = [float(self.latitude), float(self.longitude)])
        msg_ctx.validate()
        message = BAAMessage(context = msg_ctx,
                payload_class = payload_cls,
                payload = message,
                receiver_id = receiver_id)
        message.validate()
        return message

    def _setup_cloud_publisher(self, credentials_dir):
        pub = publisher.Mqtt(topic="", credentials_dir=credentials_dir)
        self.publishers.append(pub)

    def _publish_sensor_data(self, sensor, publisher, publish_time=None, receiver_id=None):
        if sensor.latest_reading == None:
             return False
        data = sensor.latest_reading
        topic = "{}/{}/{}/data".format(self.env, self.id, sensor.id)
        message = self._wrap_message_with_unit_context(data, publish_time = publish_time,
                receiver_id = receiver_id)
        publisher.publish(message, topic=topic)

    def _publish_sensor_settings(self, sensor, publisher, publish_time=None, receiver_id=None):
        if sensor.latest_setting == None:
            return False
        data = sensor.latest_setting
        topic = "{}/{}/{}/setting".format(self.env, self.id, sensor.id)
        message = self._wrap_message_with_unit_context(data, publish_time = publish_time,
                receiver_id = receiver_id)

        publisher.publish(message, topic=topic)

