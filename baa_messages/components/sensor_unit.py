from sets import Set
from baa_messages.components.sensor import SensorFactory

class SensorUnit():
    def __init__(self, id=False, name="annonymous"):
        if id == False:
            raise ValueError("A sensor unit id is required.")

        self.id = id
        self.name = name
        self.sensors = Set([])
        self.sensors_by_id = {}

    def add_sensor(self, type=False, id=False, name=False):
        sensor = SensorFactory().create_sensor(id=id, type=type, sensor_unit = self, name=name)
        self.sensors.add(sensor)
        self.sensors_by_id[sensor.id] = sensor
        return sensor

    def get_sensor(self, sensor_id):
        return self.sensors_by_id[sensor_id]
