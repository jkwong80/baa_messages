import baa_messages.subscriber.subscriber as abstract
import baa_messages.awssetup.iot as iot
from pubsub import pub

class Mqtt(abstract.Subscriber, iot.AWSIoTSetup):
    def __init__(self, topic="", sensor_id="",
                 credentials_dir=False):
        self.topic = topic
        self.__aws_setup__(credentials_dir=credentials_dir)
        self.subscribe_to_topic()

    def destroy(self):
        self.mqClient.unsubscribe(self.topic)
        self.mqClient.disconnect()

    def subscribe_to_topic(self):
        self.mqClient.subscribe(
            self.topic, 1, self.__trigger_callbacks__)

    def add_callback(self, fun):
        pub.subscribe(fun, self.topic)

    def remove_callback(self, fun):
        pub.unsubscribe(fun, self.topic)

    # Private

    def __trigger_callbacks__(self, client, userdata, message):
        pub.sendMessage(self.topic, message=message.payload)
