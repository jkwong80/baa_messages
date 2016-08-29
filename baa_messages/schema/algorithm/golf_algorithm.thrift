namespace py baa_messages.messages.algorithm.golf

struct GolfReading {
    1: required double metric,
    2: required string sensor_id,
    3: required string message_id,
    4: optional list<i32> fg_counts,
    5: optional list<double> fg_times,
    6: optional list<i32> bg_counts,
    7: optional list<double> bg_times
}

struct GolfSetting {
    1: optional double threshold,
    2: optional string scale,
    3: optional i32 num_fg_samples,
    4: optional i32 num_bg_samples,
}