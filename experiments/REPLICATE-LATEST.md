# Reproduce the latest benchmarks on a second Apple host

This runbook covers the five-size whole-tree baseline and three standalone decoder campaigns: EXP-004's packed
score decoder microbenchmark, EXP-007's private bulk specialization, and EXP-008's
scalar/bulk cutoff matrix. The checked-in observations are from an **Apple M1**. Run a
second machine such as the user's Apple M6 mini into a separate output tree; do not pool
or overwrite M1 rows. Record each host's own A/A qualification and report both hosts
side by side.

Use a clean checkout of the commit containing this file and EXP-008. Save that commit
hash with the new results. On macOS, capture the host and toolchain before any build:

```sh
REPLICA_ROOT=experiments/replications/apple-m6-mini
mkdir -p "$REPLICA_ROOT/host"
git rev-parse HEAD > "$REPLICA_ROOT/host/commit.txt"
sw_vers > "$REPLICA_ROOT/host/macos.txt"
system_profiler SPHardwareDataType > "$REPLICA_ROOT/host/hardware.txt"
clang --version > "$REPLICA_ROOT/host/clang.txt"
sysctl -n machdep.cpu.brand_string hw.physicalcpu hw.logicalcpu > "$REPLICA_ROOT/host/cpu-sysctl.txt"
```

Frequency, DVFS/turbo behavior, effective QoS, affinity and within-window migration may
remain unknown. Record them as unknown; do not infer frequency from elapsed time.
Run the matrix campaigns serially on an idle machine, with no other benchmark, build,
sanitizer or profiler active during a timing window.

## Whole-tree size matrix: 100 / 1K / 10K / 100K / 1M

For autonomous exploration, use the [shared overnight plan](NIGHT-EXPLORATION-001/README.md).

This runs all eight standard operations with 16-byte members, three seeds and
six same-binary ABBA blocks. It builds and validates native/sanitizer binaries
before timing. Run from the repository root; the output directory must be new.

```sh
python3 scripts/run-size-matrix.py --out "$REPLICA_ROOT/size-matrix" --budget-seconds 600
python3 scripts/analyse-size-matrix.py "$REPLICA_ROOT/size-matrix"
```

Compare its `SUMMARY.md` with
[the Apple M1 baseline](SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md), operation by operation
at the same size. Check variation and short timing windows before interpreting
small differences. Do not combine samples across hosts. The runner captures the
actual CPU, compiler, source and binary hashes; record compiler differences when
comparing machines. Run one campaign at a time.

[Plan, workload definitions and optional chart command](SIZE-MATRIX-001/README.md).

## EXP-004 focused decoder baseline

```sh
make decoder-check
make decoder-sanitize
python3 scripts/run-decoder.py --out "$REPLICA_ROOT/EXP-004/discovery" --budget-seconds 300
python3 scripts/analyse-decoder.py "$REPLICA_ROOT/EXP-004/discovery"
```

This is the fixed 960-process, baseline/A matrix. Preserve its raw files and A/A
qualification. It measures the score-decoder loop only; it does not clear the iterator
guard or adopt EXP-004 A.

## EXP-007 bulk helper

```sh
python3 experiments/EXP-007/build.py
python3 experiments/EXP-007/build.py --sanitize
python3 tests/test_decoder.py build/exp007/base/decoder-bench
python3 tests/test_decoder.py build/exp007/A/decoder-bench
python3 tests/test_decoder.py build/exp007/B/decoder-bench
python3 tests/test_decoder.py build/exp007/C/decoder-bench
python3 tests/test_decoder.py build/exp007-sanitize/base/decoder-bench
python3 tests/test_decoder.py build/exp007-sanitize/A/decoder-bench
python3 tests/test_decoder.py build/exp007-sanitize/B/decoder-bench
python3 tests/test_decoder.py build/exp007-sanitize/C/decoder-bench
python3 experiments/EXP-007/profile.py base --out-dir "$REPLICA_ROOT/EXP-007/profiles"
python3 experiments/EXP-007/profile.py B --out-dir "$REPLICA_ROOT/EXP-007/profiles"
python3 experiments/EXP-007/run.py --out "$REPLICA_ROOT/EXP-007/discovery" --budget-seconds 300
python3 experiments/EXP-007/analyse.py "$REPLICA_ROOT/EXP-007/discovery"
python3 experiments/EXP-007/audit.py "$REPLICA_ROOT/EXP-007/discovery" --kind discovery
```

EXP-007's original M1 result includes a fresh confirmation. Repeating it on M6 is a
new-host replication of discovery, not permission to overwrite the old confirmation. A
new confirmation should be run only if the M6 discovery meets the already recorded
selection and guard rules; save it under `$REPLICA_ROOT/EXP-007/confirmation` and use
`--confirmation B --budget-seconds 180` with the exact candidate selected by those rules.

## EXP-008 scalar/bulk crossover

```sh
python3 experiments/EXP-008/build.py
python3 experiments/EXP-008/build.py --sanitize
python3 tests/test_decoder.py build/exp008/base/decoder-bench
python3 tests/test_decoder.py build/exp008/A/decoder-bench
python3 tests/test_decoder.py build/exp008/B/decoder-bench
python3 tests/test_decoder.py build/exp008/C/decoder-bench
python3 tests/test_decoder.py build/exp008-sanitize/base/decoder-bench
python3 tests/test_decoder.py build/exp008-sanitize/A/decoder-bench
python3 tests/test_decoder.py build/exp008-sanitize/B/decoder-bench
python3 tests/test_decoder.py build/exp008-sanitize/C/decoder-bench
python3 experiments/EXP-008/profile.py base --out-dir "$REPLICA_ROOT/EXP-008/profiles"
python3 experiments/EXP-008/run.py --out "$REPLICA_ROOT/EXP-008/discovery" --budget-seconds 300
python3 experiments/EXP-008/analyse.py "$REPLICA_ROOT/EXP-008/discovery"
python3 experiments/EXP-008/audit.py "$REPLICA_ROOT/EXP-008/discovery" --kind discovery
```

The M1 discovery failed the fixed count16/count96 gain gates and count16 A/A precision,
so it has no confirmation. On M6, use the same selection rule in `EXP-008/PLAN.md`.
Only if one frozen candidate qualifies should a new fresh confirmation be run with that
candidate, the fixed fresh seeds and the 180-second budget, for example:

```sh
python3 experiments/EXP-008/run.py --out "$REPLICA_ROOT/EXP-008/confirmation" --confirmation B --budget-seconds 180
python3 experiments/EXP-008/analyse.py "$REPLICA_ROOT/EXP-008/confirmation"
python3 experiments/EXP-008/audit.py "$REPLICA_ROOT/EXP-008/confirmation" --kind confirmation
``` Do not tune cutoffs after
seeing M6 results. The likely count1-only follow-up is a separate experiment and is not
part of this replication.

Each runner writes the host fingerprint, compiler/build hashes, binary hashes, process
schedule and raw samples beside its output. Analyze and audit each host's data in place.
Do not average M1 and M6 values; compare direction, magnitude, A/A precision, guard
outcomes and generated code separately. Both remain single-machine observations.
