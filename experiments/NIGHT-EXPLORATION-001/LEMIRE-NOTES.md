# What we take from Lemire's benchmark template

Inspected template revision `f60916ef25bd05982637e81d5f5aca3b26ef3697` and its pinned
`lemire/counters` dependency `v3.2.0`. These are source-code observations, not measured
claims about M1 or M6. Source links:

- [Template benchmark.cpp](https://github.com/lemire/benchmark_template/blob/f60916ef25bd05982637e81d5f5aca3b26ef3697/benchmarks/benchmark.cpp)
- [Build configuration](https://github.com/lemire/benchmark_template/blob/f60916ef25bd05982637e81d5f5aca3b26ef3697/CMakeLists.txt)
- [Counters repetition implementation](https://github.com/lemire/counters/blob/v3.2.0/include/counters/bench.h)

## Practices to adopt

| Template practice | Application here |
|---|---|
| Constructs input before invoking the benchmark callable | Keep tree/fixture setup outside the operation timer. |
| Consumes the computed count through a volatile sink | Retain checksums and inspect assembly; a sink alone does not prove all intended work remains. |
| Inner repetition makes short calls measurable | Batch small operations; freeze the calibrated repeat count for all candidates. |
| Separate warmup and measurement phases | Warm the actual operation, not just successful lookup; record duration/count. |
| Reports fastest ns/value and throughput | Publish minimum as an idealized throughput observation alongside median/range and raw rows. |
| Prints cycles/instructions only when available | Optional separate counter pass; missing counters remain unavailable. Never infer cycles from M1 wall time. |
| Minimal benchmark callable and release build | Keep targeted experiments small, build quickly, inspect generated code, then verify public-API transfer. |

The dependency defaults to a 30,000 ns inner-block target and a 400,000,000 ns total
warmup target, with bounded repetition. Those are its defaults, not universal accuracy
guarantees. Our comparative plan uses baseline-only calibration and longer fixed
windows; adopting its exact constants is not necessary.

## Adaptation for a mutable tree

Repeated insertion into the same tree is not the same workload after the first call;
repeated deletion empties it. Prepare independent tree replicas or explicitly restore
state outside timing. Record working-set/allocator changes caused by replication.
Score updates must alternate reversible states, not silently drift across iterations.
A callback's measured cost includes its loop/checksum overhead; do not subtract an
unrelated empty-loop measurement.

The sample callable sums string lengths (despite the printed name `trim_classic`).
It is scaffolding, not a complete benchmark suite or an oracle for our data structure.
It uses C++23 and adds a counters dependency; our existing C11 target need not migrate.
We will borrow the measurement practices in a separately validated harness revision,
not import a dependency blindly. The inspected v3.2.0 runtime repetition dispatcher
also maps its 10,000 case to the 1,000-call helper, whereas final measurement dispatch
uses 10,000; audit any adopted repetition/accounting code with explicit call counts.

For reporting, keep fastest observations and distributions together. An isolated best
sample is insufficient to accept a candidate or demonstrate portability. The two-host
plan still requires same-session baseline comparisons and fresh confirmation.
