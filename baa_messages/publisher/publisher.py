from abc import ABCMeta, abstractmethod

class Broadcaster:
    __metaclass__ = ABCMeta

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def publish(self):
        pass

    def set_topic(self, topic):
        self.topic = topic
