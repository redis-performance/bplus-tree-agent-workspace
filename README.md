# Standalone B+ tree experiments

Microbenchmarks and optimization experiments for the packed B+ tree and compact
member index from [Redis PR #15635](https://github.com/redis/redis/pull/15635).
The data structure runs as a standalone C program; no Redis server is needed.

**Current state:** the benchmarks work. Bulk score decoding shows a promising local
speedup, but short-range regressions still prevent adoption. No optimization has
been merged into `src/`; experimental implementations and results live in `experiments/`.

Current optimization decisions: **0 accepted / 3 rejected / 6 parked across
9 populations**.

The [shared overnight exploration](experiments/NIGHT-EXPLORATION-001/README.md)
is running on M1; its [current result and handoff](experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/STATUS.md)
cover the five-size baseline, rank trial and parked private decoder policy trial.
M6 results remain separate.
The original four-size data is preserved.

## Build and test

Requires a C11 compiler (Clang or GCC), Make, and Python 3. Supports macOS and Linux.

```sh
git clone https://github.com/redis-performance/bplus-tree-agent-workspace.git
cd bplus-tree-agent-workspace
make -j2
make check
make sanitize
```

`make check` runs the upstream tree tests. `make sanitize` runs them in a separate
AddressSanitizer/UndefinedBehaviorSanitizer build.

## Run microbenchmarks

### Whole data structure

```sh
# All operations, with 100,000 members.
build/btree-bench --size 100000 --ops 1000000 --member-bytes 16 --seed 1

# One operation, saving CSV output.
build/btree-bench --case lookup-hit --size 100000 --ops 1000000 \
  --member-bytes 16 --seed 1 > lookup.csv
```

Available cases: `insert`, `lookup-hit`, `lookup-miss`, `rank`, `iterate`, `scan`,
`update`, and `delete`. CSV includes elapsed time, ns/op, operations/sec, tree-owned
memory, and a result checksum. Iteration and scan report time per visited member.
Use `make smoke` for a quick small-fixture check.

To run **all eight operations at 100, 1K, 10K, 100K and 1M members**, including build,
correctness checks, and repeated measurements:

```sh
python3 scripts/run-size-matrix.py --out scratch/size-matrix --budget-seconds 600
python3 scripts/analyse-size-matrix.py scratch/size-matrix
```

Use a new output directory each time. The [size-matrix guide](experiments/SIZE-MATRIX-001/README.md)
explains the workload and how to rerun it on another machine.

### Packed-score decoder

This smaller benchmark isolates score decoding for fast iterations: warmed fixtures,
repeated short batches, result checksums, and generated assembly for inspection.
It compares the original decoder with EXP-004's predicate change.

```sh
make decoder-check
make decoder-sanitize

# Use a new output directory for each run.
python3 scripts/run-decoder.py --out scratch/decoder-example
python3 scripts/analyse-decoder.py scratch/decoder-example
```

The runner saves raw samples and compares the baseline against itself to estimate
noise, then against the candidate. For bulk decoding and scalar/bulk cutoffs, use the
[latest experiment runbook](experiments/REPLICATE-LATEST.md).
See the [decoder guide](docs/DECODER-MICROBENCHMARK.md) and
[tree benchmark guide](docs/MICROBENCHMARKS.md) for measurement details.

## Latest results — Apple M1

All results below were measured on **Apple M1**, using Apple Clang 17, `-O3`, and
one unpinned thread.

### Whole-tree baseline: 100 / 1K / 10K / 100K / 1M members

All eight operations have now been measured at all five sizes with 16-byte members.
The chart shows median batch-average ns/op and the full observed min–max range;
each panel has its own y-axis. These are baseline costs, not optimization speedups.
Identical-binary controls show variation above 1%, and small insert/delete windows
are short. See the [results and timing details](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md).

![Apple M1 sorted-set operation costs by size](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/size-matrix.svg)

[Plan, raw data and M6 rerun commands](experiments/SIZE-MATRIX-001/README.md).

### Decoder experiments

These isolate packed-score decoding; their gains are not whole-tree speedups.

| Experiment | What we learned | Outcome |
|---|---|---|
| [EXP-004: simpler scalar predicate](experiments/EXP-004/decoder-microbench-2026-10-19/README.md) | Decoding took about 16% longer for 8-bit scores and 10% longer for 64-bit scores. | No general decoder improvement. |
| [EXP-007: specialized bulk decoder](experiments/EXP-007/RESULTS.md) | For 96 scores, decode time fell 33% at 60 bits and about 43% at 8/64 bits versus the scalar output loop. Three short-range cases regressed. | Promising for bulk work; not adopted. |
| [EXP-008: scalar fallback for short ranges](experiments/EXP-008/RESULTS.md) | Switching to scalar at cutoffs of 4, 8, or 16 scores introduced substantial short-range regressions versus the bulk decoder. | None of the three cutoffs selected. |

The latest chart compares those three cutoffs with **EXP-007's bulk decoder** at
60-bit score width, forward direction. Below zero means less time; above zero means
more time. Bars show the observed range across measurement blocks.

![Apple M1: scalar fallback cutoffs versus the bulk decoder](experiments/EXP-008/discovery/threshold-effects.svg)

The next hypothesis is a scalar fallback **only for a single score**. That policy
has not been tested yet. The complete [experiment log](experiments/EXPERIMENTS.md)
retains earlier attempts and their evidence.

For the planned **Apple M6 mini** rerun, follow the
[replication instructions](experiments/REPLICATE-LATEST.md). Save its results separately
and compare them with M1; no M6 results have been collected here.

## How optimization decisions work

Each experiment starts with profiling, then uses two population-based steps:

1. **Choose the idea:** three independent proposals examine the same baseline and
   profiles. A chair selects one hypothesis, or none, and records the reasons.
2. **Choose the implementation:** three isolated implementations compete on correctness
   and serial benchmarks. A candidate needs fresh confirmation, profiling, and review
   before adoption. If none passes, keep the baseline.

When independent agents are unavailable, record sequential passes explicitly.
Full procedure: [population protocol](docs/POPULATION.md).

## Code and documentation

- [`src/`](src/): B+ tree and compact member index.
- [`bench/`](bench/) and [`tests/`](tests/): microbenchmarks and correctness checks.
- [`experiments/`](experiments/): candidate patches, reports, profiles, and raw results.
- [`compat/`](compat/) and [`vendor/redis/`](vendor/redis/): standalone adapter and required upstream support.
- [Source manifest](source-manifest.json), [extraction notes](docs/STANDALONE.md), and [licensing](NOTICE.md).
