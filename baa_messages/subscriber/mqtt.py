import baa_messages.subscriber.subscriber as abstract
import baa_messages.awssetup.iot as iot
from pubsub import pub
import baa_messages.codec as bc
import logging, json

# setup logging
log = logging.getLogger()

class MqttMessage():
    def __init__(self, message, message_with_wrapper=False):
        self._decode(message)
        self.full_message = message_with_wrapper

    def meta_data(self):
        return json.loads(bc.encode_object(self.message,
                   encoding=bc.Encoding.TSIMPLEJSON))

    def body(self):
        return json.loads(bc.encode_object(self.payload,
                   encoding=bc.Encoding.TSIMPLEJSON))

    def _decode(self, message):
        self.iot_json = self._event_to_json(message)
        self._unpack_message()
        self._unpack_payload()

    def _unpack_message(self):
        log.info("Unpacking Thrift Message: {}".format(self.iot_json))
        self.message = bc.decode_network_message(self.iot_json)
        log.info('baa_message: {}'.format(self.message))

    def _unpack_payload(self):
        log.info("Unpacking Payload String")
        self.payload = bc.decode_payload(self.message.payload, bc.Encoding.TBINARY,
                                         self.message.payload_class)
        log.info('sensor_message: {}'.format(self.payload))

    def _event_to_json(self, msg):
        return str(msg)


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
        log.info("Got message: {}, {}".format(type(message.payload), message))
        decoded = MqttMessage(message.payload, message_with_wrapper=message)
        pub.sendMessage(self.topic, message=decoded)
