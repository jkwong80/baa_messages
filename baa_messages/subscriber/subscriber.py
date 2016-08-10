from abc import ABCMeta, abstractmethod

class Subscriber:
    __metaclass__ = ABCMeta

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def subscribe_to_topic(self):
        pass

    @abstractmethod
    def add_callback(self, function):
        pass

    @abstractmethod
    def remove_callback(self, function):
        pass


    def set_topic(self, topic):
        self.topic = topic
