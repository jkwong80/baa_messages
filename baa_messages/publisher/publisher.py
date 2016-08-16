from abc import ABCMeta, abstractmethod

class Broadcaster:
    __metaclass__ = ABCMeta

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def publish(self, msg, topic=None):
        pass

    def set_topic(self, topic):
        self.topic = topic

    def set_serializer(self,func):
        self.serializer = func
