# AA-001 preregistration — targeted longer batches

Written before measurement on 2026-10-17. Separate baseline qualification after
HARNESS-001, not an optimisation comparison. Falsifiable diagnostic: fixed longer
batches plus ten complete lookup warm-up passes provide sufficient repeatability to
resolve the existing +/-1% A/A precision gate for these targeted fixtures.

Base commit `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c` plus uncommitted HARNESS-001 patch;
git metadata is protected. Freeze manifest in HARNESS-001/freeze.json. Only the frozen
snapshot executable is used, with hash checks before/after. Main tree source unchanged.
One benchmark thread on the authorised local Apple M1, 4 P + 4 E cores, no SMT, 16 GiB,
macOS 26.3, Apple Clang 17.0.0, -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3,
libc allocator, assertions unchanged, no LTO/fast-math. No affinity or QoS changes.
Core microarchitecture residency, effective QoS, clock/frequency and DVFS/turbo state
are unknown. Boundary CPU IDs are opaque, not classified into M4-derived core types.

## Fixed schedule and gates

Six ABBA blocks, four fresh processes per cell/block, A and B the exact same executable.
Eight cells, 192 result rows/processes total; size 100000, seed 1, warmup-passes 10:

| Cell | Case | Member bytes | Requested operations |
|---|---|---:|---:|
| hit16 | lookup-hit | 16 | 20000000 |
| hit320 | lookup-hit | 320 | 5000000 |
| miss16 | lookup-miss | 16 | 20000000 |
| rank16 | rank | 16 | 5000000 |
| iterate16 | iterate | 16 | 50000000 |
| scan16 | scan | 16 | 5000000 |
| update16 | update | 16 | 1000000 |
| hit321 | lookup-hit | 321 | 5000000 |

Rotate cell order left by block index (0..5). Run each ABBA group serially; no agents,
builds, tests or profiles overlap measurements. Before the matrix, exactly one recorded
binary warm-up process: hit16 with 1000000 ops, all other arguments identical. It is
excluded by this plan, not by an observed result. No calibration/count changes follow.
All processes bounded to 120 seconds. Total matrix budget 720 seconds; failure/timeout
is retained, correctness failure stops the run, and incomplete cells cannot qualify.

Primary metric: elapsed wall ns / actual effective operations. Supplementary: raw
thread CPU time, CPU boundary IDs, queried requested QoS/relative priority, warm-up
duration, memory and checksum. Thread time does not substitute for wall time or prove
stable frequency. Equal IDs cannot exclude migration. No outlier removal, optional
stopping, selective runs or threshold changes.

Per cell, report all raw rows, median/min/max/CV, six block effects
100*(mean(B ns/op)/mean(A ns/op)-1), and descriptive Student-t 95% interval using df=5,
t=2.5705818366147395. Qualification requires all 24 successful rows, identical checksum,
operation count and tree-owned memory, every wall region >=10 ms, and the entire
interval inside [-1%, +1%]. Independence/normality assumptions remain limitations.
Individual qualifying cells do not qualify missing guards or the full workload suite.

If qualification fails: PARK the affected comparisons, select no optimisation, and
use a new preregistered diagnostic or stronger boundary checks. Do not repeat this
schedule until it happens to pass. A passing subset may motivate population proposals
only within its coverage; both population stages and all acceptance gates still apply.

Backend/model unknown. Agent startup failed before any agent ran. No population has
been executed; token accounting is recorded separately by the supervisor.
