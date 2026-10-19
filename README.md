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
The **AWS Intel, AMD and Graviton overnight campaign** is now baselining all five
sizes, with optimization work bounded to **19 October, 09:00 Lisbon / 08:00 UTC**.
[Live AWS status and activity](experiments/NIGHT-EXPLORATION-001/AWS-STATUS.md).
Each completed host baseline will be added to the chart below; no AWS values are
plotted until their raw results are verified. Source adoption remains NONE.
<!-- AWS-NIGHT-END -->

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

## Latest results — Apple M1 and M6

### Whole-tree baseline: 100 / 1K / 10K / 100K / 1M members

Both overnight campaigns have completed all eight operations at all five sizes:
16-byte members, three seeds, six same-binary ABBA blocks, 120 serial processes
and 960 rows per host. Native and ASan/UBSan validations pass on both hosts.

The chart overlays **M1 (blue circles)** and **M6 (orange squares)** in each
operation panel, with median batch-average **ns/op** and observed min–max ranges.
Each panel has its own y-axis. Lower is less time. Intel, AMD and AWS Graviton
are reserved in the legend as **NOT RUN**; they have no plotted measurements.

![Apple M1 and M6 latest baselines overlaid across all eight operations and five tree sizes](experiments/NIGHT-EXPLORATION-001/baseline-charts/m1-m6-baseline.png)

[Chart data, pinned source revisions and reproduction](experiments/NIGHT-EXPLORATION-001/baseline-charts/README.md).

Status snapshot: **19 October 2026, 01:41 UTC**. The host links show ongoing updates.

| Host | Compiler | Five-size baseline | Cells with >1% A/A variation | Optimization status / live updates |
|---|---|---|---|---|
| Apple M1 | Apple Clang 17, `-O3` | [Complete; 388.7s timing](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m1-20261019T005019Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/001-baseline/matrix/SUMMARY.md) | 39/40 | [Rank trial rejected; update/lookup diagnosed; decoder next](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m1-20261019T005019Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/STATUS.md) |
| Apple M6 | Apple Clang 21, `-O3` | [Complete; 162.42s timing](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/baseline-attempt002/SUMMARY.md) | 36/40 | [Rank diagnosis running; driver campaign through 09:00 Lisbon](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/exploration/apple-m6-mini-20261019T013000Z/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/STATUS.md) |
| Intel (x86-64) | Pending | **NOT RUN** | — | Placeholder; CPU model and runner not selected |
| AMD (x86-64) | Pending | **NOT RUN** | — | Placeholder; CPU model and runner not selected |
| AWS Graviton (arm64) | Pending | **NOT RUN** | — | Placeholder; generation and runner not selected |

Median batch-average **ns/op** from these overnight baselines; lower is less time.
Full five-size tables, observed ranges, raw rows and precision checks are linked above.

| Operation | M1 · 100K | M6 · 100K | M1 · 1M | M6 · 1M |
|---|---:|---:|---:|---:|
| Insert | 489.02 | 239.51 | 814.90 | 335.40 |
| Hit lookup | 121.26 | 44.66 | 293.74 | 121.45 |
| Miss lookup | 36.60 | 12.14 | 128.65 | 45.60 |
| Rank | 178.24 | 64.92 | 480.32 | 208.22 |
| Forward iteration | 4.58 | 2.39 | 4.86 | 2.47 |
| Scan | 75.24 | 46.06 | 153.10 | 52.09 |
| Score update | 733.07 | 332.67 | 1277.59 | 577.93 |
| Delete | 383.79 | 170.91 | 763.82 | 334.02 |

These are separate host baselines with different compilers and machine conditions.
Their differences are not candidate optimization gains. A/A variation and short
windows require targeted qualification before small performance claims; no tree
optimization has been adopted. Each candidate must beat its own host's baseline.

The [earlier M1 preparation results](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/SUMMARY.md)
and [chart](experiments/SIZE-MATRIX-001/apple-m1-five-sizes/size-matrix.svg) remain
separate from these overnight baselines. [Baseline plan and rerun commands](experiments/SIZE-MATRIX-001/README.md).

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


19October2026 AWS Intel native lookup: **REJECT/NONE**,1completed sequential population(0accepted/1rejected/0parked),3retained patches.432rows/108blocks, all variants slow both primaries; baseline source unchanged. [Intel evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md). Other-host and historical counts remain separate.


19October2026 AWS Intel update diagnosis **NONE**: separate validated five-pattern referee,360semanticcells,15scopedprofiles+disabledcontrol,25censuscells,600baseline rows/25cells(2qualified). No newimplementationpopulation; Intelcount stays1measuredpopulation/1REJECT/3retainedpatches. See experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update/README.md. Source unchanged.


19 October2026 AWS Intel iterator cache: **PARK / NONE**, fixed screen566/576 rows (141 complete blocks plus two trailing rows), budget stopped without extension. A/B conditional leads; C rejected. Intel totals: **2 measured sequential populations,0 accepted /1 rejected /1 parked;6 retained patches**. Iterator population comparison is partial. Update diagnosis NONE adds no implementation population. Source unchanged. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator/README.md).


Intel baseline scan diagnosis:6 scoped captures show TagMatches27.48%/24.14% of captured executable-range samples at100K/1M. This is a coarse hotspot observation, not a speed claim. Source remains NONE; no new population. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/006-scan-profile/README.md).


Intel scan baseline qualification:48 held-out-seed A/A rows complete, both100K/1M controls qualify within±1% with windows>=444ms. No candidate timing or population increment. [Evidence](experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication/README.md).
