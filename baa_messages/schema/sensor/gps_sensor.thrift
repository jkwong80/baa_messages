namespace py baa_messages.messages.sensor.gps

struct GpsReading {
    1: required double latitude,
    2: required double longitude
}

struct GpsSetting {
    1: optional double poll_frequency
    2: optional double null_value
}