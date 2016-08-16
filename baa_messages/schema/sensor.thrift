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
include "sensor/gps_sensor.thrift"
include "sensor/gamma_sensor.thrift"
include "sensor/neutron_sensor.thrift"
include "sensor/temp_sensor.thrift"
namespace py baa_messages.messages.sensor

union Reading {
    1: gps_sensor.Reading gps,
    2: temp_sensor.Reading temperature,
    3: gamma_sensor.Reading gamma,
    4: neutron_sensor.Reading neutron
}

struct SensorReading {
    1: required core.BAAContext context,
    2: required Reading reading
}

union Setting {
    1: gps_sensor.Setting gps,
    2: temp_sensor.Setting temp,
    3: gamma_sensor.Setting gamma,
    4: neutron_sensor.Setting neutron
}

struct SensorSetting {
    1: required core.BAAContext context,
    2: required Setting setting
}

struct SensorReport {
    1: required core.BAAContext context,
    2: list<SensorReading> readings,
    3: list<SensorSetting> settings,
}

