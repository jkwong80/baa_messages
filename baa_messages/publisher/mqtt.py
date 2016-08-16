import baa_messages.publisher.publisher as abstract
import baa_messages.awssetup.iot as iot


class Mqtt(abstract.Broadcaster, iot.AWSIoTSetup):
    def __init__(self, topic="", sensor_id="", credentials_dir=False):
        self.topic = topic
        self.__aws_setup__(credentials_dir=credentials_dir)

    def destroy(self):
        self.mqClient.disconnect()

    def publish(self, msg, topic=None):
        if topic is not None:
            self.set_topic(topic)
        self.mqClient.publish(self.topic, msg, 0)
