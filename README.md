# Standalone B+ tree experiments

Microbenchmarks and optimization experiments for the packed B+ tree and compact
member index from [Redis PR #15635](https://github.com/redis/redis/pull/15635).
The data structure runs as a standalone C program; no Redis server is needed.

**Current state:** the benchmarks work. Bulk score decoding shows a promising local
speedup, but short-range regressions still prevent adoption. No optimization has
been merged into `src/`; experimental implementations and results live in `experiments/`.

The [shared overnight exploration plan](experiments/NIGHT-EXPLORATION-001/README.md)
is running on separate M1 and M6 host branches: rank, update paths, single-query
lookup, and an optional decoder experiment. Both hosts have completed the
**100 / 1K / 10K / 100K / 1M** baseline. See the latest results and live status links below.

<!-- AWS-NIGHT-START -->
The **AWS Intel, AMD and Graviton campaign** is bounded to **19 October,
09:00 Lisbon / 08:00 UTC**. [Baselines and plan](experiments/NIGHT-EXPLORATION-001/AWS-STATUS.md),
[live workers and activity](experiments/NIGHT-EXPLORATION-001/AWS-WORKERS.md).
Each host publishes its completed decisions and evidence on a separate branch.
Source adoption remains NONE.
<!-- AWS-NIGHT-END -->

AWS completed measured populations: **7 — 0 accepted / 4 rejected / 3 parked**.
One additional ARM architecture replication is parked.
[Decision ledger](experiments/NIGHT-EXPLORATION-001/AWS-DECISIONS.md).

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

## Latest results — Apple M1, M6 and three AWS architectures

### Whole-tree baseline: 100 / 1K / 10K / 100K / 1M members

All five hosts have completed all eight operations at all five sizes:
16-byte members, three seeds, six same-binary ABBA blocks, 120 serial processes
and 960 rows per host. Native and ASan/UBSan validations pass on all five hosts.

The chart overlays **Apple M1, Apple M6, AWS Intel, AWS AMD and AWS Graviton**
in each operation panel, with median batch-average **ns/op** and observed min–max
ranges. Each panel has its own y-axis. Lower is less time. All five series are
measured; AWS observations are pinned to CPU2, while the Apple runs were unpinned.

![Measured M1 M6 Intel AMD and Graviton baselines across eight operations and five sizes](experiments/NIGHT-EXPLORATION-001/baseline-charts/m1-m6-baseline.png)

[Chart data, pinned source revisions and reproduction](experiments/NIGHT-EXPLORATION-001/baseline-charts/README.md).

Status snapshot: **19 October 2026, 02:03 UTC**. The host links show ongoing updates.

| Host | Compiler | Five-size baseline | Cells with >1% A/A variation | Optimization status / live updates |
|---|---|---|---|---|
| Apple M1 | Apple Clang 17, `-O3` | [Complete; 388.7s timing](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m1-20261019T005019Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/001-baseline/matrix/SUMMARY.md) | 39/40 | [Rank trial rejected; update/lookup diagnosed; decoder next](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m1-20261019T005019Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/STATUS.md) |
| Apple M6 | Apple Clang 21, `-O3` | [Complete; 162.42s timing](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/baseline-attempt002/SUMMARY.md) | 36/40 | [Five trials rejected; source NONE; geometry diagnosis active](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/STATUS.md) |
| Intel Sapphire Rapids (x86-64) | Clang18.1.3, `-O3`, CPU2 | [Complete; 338.54s timing](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/001-baseline/SUMMARY.md) | 27/40 | [Native worker: profiling and optimization](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/aws-intel-20261019T020000Z/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/STATUS.md) |
| AMD Zen 5 (x86-64) | Clang18.1.3, `-O3`, CPU2 | [Complete; 325.44s timing](experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/001-baseline/SUMMARY.md) | 30/40 | [Native worker: profiling and optimization](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/aws-amd-20261019T020000Z/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/STATUS.md) |
| AWS Graviton / Neoverse V2 (arm64) | Clang18.1.3, `-O3`, CPU2 | [Complete; 377.83s timing](experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/001-baseline/SUMMARY.md) | 19/40 | [Native worker: profiling and optimization](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/aws-arm-20261019T020000Z/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/STATUS.md) |

Median batch-average **ns/op** from these overnight baselines; lower is less time.
Full five-size tables, observed ranges, raw rows and precision checks are linked above.

**100,000 members — ns/op**

| Operation | Apple M1 | Apple M6 | AWS Intel | AWS AMD | AWS Graviton |
|---|---:|---:|---:|---:|---:|
| Insert | 489.02 | 239.51 | 557.98 | 385.01 | 512.41 |
| Hit lookup | 121.26 | 44.66 | 132.10 | 71.40 | 139.87 |
| Miss lookup | 36.60 | 12.14 | 71.19 | 35.72 | 59.57 |
| Rank | 178.24 | 64.92 | 173.68 | 103.67 | 175.64 |
| Forward iteration | 4.58 | 2.39 | 4.51 | 4.51 | 4.81 |
| Scan | 75.24 | 46.06 | 87.61 | 68.40 | 84.27 |
| Score update | 733.07 | 332.67 | 734.98 | 492.17 | 665.28 |
| Delete | 383.79 | 170.91 | 354.05 | 220.36 | 328.82 |

**1,000,000 members — ns/op**

| Operation | Apple M1 | Apple M6 | AWS Intel | AWS AMD | AWS Graviton |
|---|---:|---:|---:|---:|---:|
| Insert | 814.90 | 335.40 | 779.74 | 700.16 | 787.01 |
| Hit lookup | 293.74 | 121.45 | 213.14 | 296.79 | 336.90 |
| Miss lookup | 128.65 | 45.60 | 149.40 | 179.61 | 191.78 |
| Rank | 480.32 | 208.22 | 297.65 | 355.49 | 412.77 |
| Forward iteration | 4.86 | 2.47 | 5.01 | 4.59 | 5.14 |
| Scan | 153.10 | 52.09 | 118.96 | 95.60 | 112.40 |
| Score update | 1277.59 | 577.93 | 1039.10 | 1099.21 | 1104.32 |
| Delete | 763.82 | 334.02 | 571.45 | 611.89 | 601.81 |

These are separate host baselines with different compilers and machine conditions.
Their differences are not candidate optimization gains. A/A variation and short
windows require targeted qualification before small performance claims; no tree
optimization has been adopted. Each candidate must beat its own host's baseline.

The [earlier M1 preparation results](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md)
and [chart](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/size-matrix.svg) remain
separate from these overnight baselines. [Baseline plan and rerun commands](experiments/SIZE-MATRIX-001/README.md).

### M6 campaign decisions

[The first M6 rank population](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/002-rank/RESULTS.md)
rejects all three shorter-side summation implementations: the 100K primary took
about 3.4–3.9% longer by median block effect. The 1M signals remain inside A/A noise.
Source stays unchanged. [M6 update repacking](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/003-update/RESULTS.md) also fails its 100K primary; its 1M reductions remain exploratory. [M6 lookup physical-score decoding](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/RESULTS.md) has a 100K-only exploratory lead but no dual-primary winner. The population steps were
sequential passes, with all patches preserved.

[M6 count-one decoder policies](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/005-decode/RESULTS.md) retain a roughly30% private count-one lead, but repeated qualified guard losses reject all three universal policies. Baseline source stays unchanged.

[Call-boundary lookup follow-up](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/RESULTS.md) also rejects all three implementations: A's qualified100K lead is−2.71%, while no variant clears both100K/1M gates. Three actual independent agents completed both population stages. Baseline source stays unchanged.

![M6 caller specialization: all six blocks, observed ranges and control qualification](experiments/NIGHT-EXPLORATION-001/latest-charts/m6-caller-screens.png)

M6 branch totals (AWS and concurrent M1 night separate): **12 populations; 0 accepted / 7 rejected / 5 parked;
36 retained patches; 15 validated harnesses**. [Chart data and pinned reproduction](experiments/NIGHT-EXPLORATION-001/latest-charts/README.md).

### Decoder experiments

The decoder results below were measured on **Apple M1**, using Apple Clang 17,
`-O3`, and one unpinned thread. They isolate packed-score decoding; their gains
are not whole-tree speedups. M6 decoder replication is pending.

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

For **Apple M6 decoder** reruns, follow the
[replication instructions](experiments/REPLICATE-LATEST.md). Save those results
separately from M1; the completed M6 whole-tree baseline is linked above.

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
