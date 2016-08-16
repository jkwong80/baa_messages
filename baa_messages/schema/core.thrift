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


namespace py baa_messages.messages.core

struct BAAContext {
    1: required string parent_id,
    2: required i64 timestamp, // Unix Epoch time in microseconds (truncated)
    3: optional i32 timestamp_remainder, // number of femtoseconds to add to timestamp
    4: optional list<double> location,
    5: optional i32 sensor_id,
    6: optional i32 sensor_unit_id
}

struct BAAMessage {
    1: required BAAContext context,
    2: required string payload_class,
    3: required binary payload,
    4: optional string receiver_id
}
