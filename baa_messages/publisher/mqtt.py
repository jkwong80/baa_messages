import baa_messages.publisher.publisher as abstract
import baa_messages.awssetup.iot as iot
import baa_messages.codec as bc
import logging
# setup logging
log = logging.getLogger()

class Mqtt(abstract.Broadcaster, iot.AWSIoTSetup):
    def __init__(self, topic="", credentials_dir=False, encoded=True):
        self.topic = topic
        self.__aws_setup__(credentials_dir=credentials_dir)
        self.encoded = encoded

    def destroy(self):
        self.mqClient.disconnect()

    def publish(self, msg, topic=None):
        if topic is not None:
            self.set_topic(topic)
        if self.encoded == True:
            msg = self._encode(msg)
        log.info("mqtt publishing: {} to {}".format(msg, topic))
        self.mqClient.publish(self.topic, msg, 0)

    def _encode(self, msg):
        msg.payload = bc.encode_object(msg.payload, encoding=bc.Encoding.TBINARY)
        msg = bc.encode_object(msg, encoding=bc.Encoding.TJSON)
        return msg
