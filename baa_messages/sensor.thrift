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

/**
 * This Thrift file can be included by other Thrift files that want to share
 * these definitions.
 */

namespace py sensor

enum SensorType {
    radiation=1,
    temperature=2
}

struct Spectrum {
    1: string sensor_id,
    2: i64 sample_time,
    3: string timestamp,
    4: i64 real_time,
    5: i64 live_time,
    6: list<i32> adc_channel_counts,
    7: list<double> bin_energies
}

struct RadiationSensorSettings {
    1: string sensor_id,
    2: double high_voltage,
    3: double fine_gain
}

struct RadiationSensorReport {
    1: SensorType stype=SensorType.radiation,
    2: list<string> sensor_ids,
    3: list<Spectrum> sensor_spectra,
    4: list<RadiationSensorSettings> sensor_settings,
}
