/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */


namespace py messages.sensor


enum SensorType {
    RADIATION=1,
    TEMPERATURE=2,
    GPS=3

}

struct GPSReading {
    1: required string sensor_id,
    2: required double timestamp,
    3: required double latitude,
    4: required double longitude
}

struct TemperatureReading{
    1:
    1: required double timestamp,
    2: required double temperature
}

struct GammaReading{
    1: required double start_time,
    2: required double duration,
    3: required double live_time,
    4: required list<i32> adc_channel_counts,
    5: optional list<double> bin_energies
}

struct NeutronReading {
    1: required double counts
}

union SensorReading {
    1: GPSReading gps,
    2: TemperatureReading temp,
    3: GammaReading gamma,
    4: NeutronReading neutron
}

struct SensorReadingReport {
    1: required string sensor_id,
    2: required double timestamp,
    3: required SensorType sensor_type,
    4: required SensorReading sensor_reading,

    5: optional string sensor_unit_id
}

struct GPSSetting {
    1: optional double sample_frequency,
}

struct TemperatureSetting {
    1: optional double sample_frequency,
}

struct GammaSetting {
    1: optional double sample_frequency,
    2: optional double fine_gain,
    3: optional double high_voltage,
    4: optional double lld,
    5: optional double uld
}

struct NeutronSetting {
    1: optional double sample_frequency,
    2: optional double voltage
}

union SensorSetting {
    1: GPSSetting gps,
    2: TemperatureSetting temp,
    3: GammaSetting gamma,
    4: NeutronSetting neutron
}

struct SensorSettingReport {
    1: required string sensor_id,
    2: required double timestamp,
    3: required SensorType sensor_type,
    4: required SensorReading sensor_setting,

    5: optional string sensor_unit_id
}



