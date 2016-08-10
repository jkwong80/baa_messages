#!/usr/bin/python2.4

"""Integration Tests for baa mqtt messaging, full stack access the online AWS sytem"""

__author__ = 'Cory Gwin'

import unittest, mock, time, os
import baa_messages.subscriber.mqtt as subscriber
import baa_messages.publisher.mqtt as publisher

credentials_dir = os.path.abspath("test/.baa_credentials")

class MQTTSystem(unittest.TestCase):
    def test_publishing(self):
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
