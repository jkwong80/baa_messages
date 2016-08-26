from baa_messages.components.sensor_unit import SensorUnit
import helpers

def new_sensor_unit(id=1):
    return SensorUnit(id=id, cloud_publish=False)

def create_sensor_gps_reading(sensor, time):
    lat = helpers.random_coordinate()
    lng = helpers.random_coordinate()
    return sensor.create_reading(timestamp_us=time, latitude=lat, longitude=lng)

