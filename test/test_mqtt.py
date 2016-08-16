import unittest
import time
import os
import baa_messages.subscriber.mqtt as subscriber
import baa_messages.publisher.mqtt as publisher
from baa_messages.util import check_internet_connection

"""Integration Tests for baa mqtt messaging, full stack access the online AWS system"""

credentials_dir = os.path.abspath("test/.baa_credentials")


class MQTTSystem(unittest.TestCase):
    def test_publishing(self):

        if not check_internet_connection("http://www.google.com"):
            raise RuntimeError("No active internet connection is present...cannot test MQTT publishing")

        sub = subscriber.Mqtt(
            topic="integrationtest", credentials_dir=credentials_dir)

        def callback(message):
            self.got_pubsub_message = True
            self.message = message
        sub.add_callback(callback)
        self.got_pubsub_message = False

        pub = publisher.Mqtt(
            topic="integrationtest", sensor_id="test",
            credentials_dir=credentials_dir
            )
        pub.publish("hello")
        time.sleep(2)
        assert(self.got_pubsub_message, True)
        assert(self.message, "hello")

    def test_topic_creation(self):
        pass
