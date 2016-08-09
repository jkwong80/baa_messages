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

include "core.thrift"
namespace py baa_messages.messages.sensor


enum SensorType {
    RADIATION=1,
    TEMPERATURE=2,
    GPS=3

}

struct GPSReading {
    1: required core.BAAContext context,
    2: required double latitude,
    3: required double longitude,
    4: optional string status
}

struct TemperatureReading{
    1: required core.BAAContext context,
    2: required double temperature,
    3: optional string status
}

struct GammaReading{
    1: required core.BAAContext context,
    2: required double start_time,
    3: required double duration,
    4: required double live_time,
    5: required i32 num_channels,
    6: required map<i32,i32> adc_channel_counts,
    7: optional map<double,double> channel_energies,
    8: optional double gross_counts
}

struct NeutronReading {
    1: required core.BAAContext context,
    2: required double counts,
    3: optional i32 num_channels
    4: optional map<i32,i32> adc_channel_counts,
    5: optional map<double,double> channel_energies
}

union SensorReading {
    1: GPSReading gps,
    2: TemperatureReading temp,
    3: GammaReading gamma,
    4: NeutronReading neutron
}

struct GPSSetting {
    1: required core.BAAContext context,
    2: optional double poll_frequency,
    3: optional list<double> null_value
}

struct TemperatureSetting {
    1: required core.BAAContext context,
    2: optional double poll_frequency,
    3: optional list<double> null_value
}

struct GammaSetting {
    1: required core.BAAContext context,
    2: optional double sample_frequency,
    3: optional double fine_gain,
    4: optional double high_voltage,
    5: optional double lld,
    6: optional double uld
}

struct NeutronSetting {
    1: required core.BAAContext context,
    2: optional double sample_frequency,
    3: optional double voltage
}

union SensorSetting {
    1: GPSSetting gps,
    2: TemperatureSetting temp,
    3: GammaSetting gamma,
    4: NeutronSetting neutron
}

struct SensorReport {
    1: required core.BAAContext context,
    2: list<SensorReading> readings,
    3: list<SensorSetting> settings,
    4: list<SensorType> sensor_type
}
