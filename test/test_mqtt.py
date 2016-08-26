import unittest, time, os, json
import baa_messages.subscriber.mqtt as subscriber
import baa_messages.publisher.mqtt as publisher
from baa_messages.util import check_internet_connection
import baa_messages.codec as bc
import baa_messages.components.sensor_unit as su
import support.helpers as helpers
import support.factories as factories

"""Integration Tests for baa mqtt messaging, full stack access the online AWS system"""

credentials_dir = os.path.abspath("test/.baa_credentials")


class MQTTSystem(unittest.TestCase):
    def test_publishing_encoding_decoding(self):
        if not check_internet_connection("http://www.google.com"):
            raise RuntimeError("No active internet connection is present...cannot test MQTT publishing")

        unit = su.SensorUnit(id=1, env="test", credentials_dir=credentials_dir)
        sensor = unit.add_sensor("gps", id=1)
        t = helpers.formatted_time()
        reading = factories.create_sensor_gps_reading(sensor, t)

        sub = subscriber.Mqtt(
                topic="test/1/1/data", credentials_dir=credentials_dir)

        self.message = False
        self.got_pubsub_message = False
        def callback(message):
            self.got_pubsub_message = True
            self.message = message
        sub.add_callback(callback)

        unit.publish()
        time.sleep(2)

        msg = bc.encode_object(reading, bc.Encoding.TSIMPLEJSON)
        assert(self.got_pubsub_message, True)
        for key in json.loads(msg).keys():
            self.assertEqual(self.message.body()[key], json.loads(msg)[key])

    def test_topic_change(self):
        pub = publisher.Mqtt(
            topic="integrationtest",
            credentials_dir=credentials_dir
        )
        pub.set_topic("test")
        assert pub.topic == "test"
