namespace py baa_messages.messages.sensor.neutron

struct NeutronReading {
    1: required double counts,
    2: optional i32 num_channels
    3: optional map<i32,i32> adc_channel_counts,
    4: optional map<double,double> channel_energies
}

struct NeutronSetting {
    1: optional double sample_frequency,
    2: optional double voltage
}
