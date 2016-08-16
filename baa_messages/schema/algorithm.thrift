include "core.thrift"
include "algorithm/golf_algorithm.thrift"

namespace py baa_messages.messages.algorithm

union AlgorithmReading {
    1: golf_algorithm.Reading golf
}

union AlgorithmSetting {
    1: golf_algorithm.Setting golf
}

struct AlgorithmReport {
    1: required core.BAAContext context,
    2: list<AlgorithmReading> readings,
    3: list<AlgorithmSetting> settings,
}
