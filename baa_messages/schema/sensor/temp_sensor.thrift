
namespace py baa_messages.messages.sensor.temperature

struct Reading {
    1: required double temperature
}

struct Setting {
    1: optional double poll_frequency
    2: optional double null_value
}