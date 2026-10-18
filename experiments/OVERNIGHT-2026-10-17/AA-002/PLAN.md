# AA-002 preregistration — larger lookup fixture

Written before runs, 2026-10-17 round 2. New fixture coverage, not a repeat of AA-001.
Hypothesis: fixed batches on one-million-member fixtures provide enough repeatability
for the unchanged +/-1% A/A gate in the four selected lookup/rank cells. Failure means
PARK, not increased repetitions. This does not isolate fixture size from duration.

Use the exact frozen HARNESS-001 executable and source hashes (freeze.json).
Base commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus uncommitted harness patch;
protected git metadata, no new staging/worktree attempt. No source changes.
Apple M1, 4 P+4 E installed cores, one benchmark thread, no SMT, 16 GiB, macOS 26.3;
Apple Clang 17.0.0; -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3;
libc allocator, unchanged assertions/hashing, no LTO/fast-math/affinity/QoS change.
Frequency/DVFS, actual core residency and effective QoS remain unknown. Boundary
CPU IDs are opaque observations, not M4-derived topology or exclusion of migration.

## Fixed schedule

Size 1000000, seed 1, warmup-passes 10 in every process. Four cells:

| Cell | Case | Member bytes | Operations |
|---|---|---:|---:|
| hit16 | lookup-hit | 16 | 20000000 |
| miss16 | lookup-miss | 16 | 20000000 |
| rank16 | rank | 16 | 5000000 |
| hit320 | lookup-hit | 320 | 5000000 |

Six serial ABBA blocks, exact same executable for A and B, four fresh processes per
cell/block: 96 measured rows. Rotate cell order by (block-1) modulo four. Before matrix,
one recorded binary warmup (hit16, one million operations), excluded prospectively.
Every child <=120s; matrix budget 900s. No build, test, profiling or agent computation
concurrent with measurement. An incomplete cell cannot qualify. Failures preserved;
correctness failure stops matrix. No outliers removed, adaptive counts or optional stopping.

Wall ns / actual operation count is primary. Thread time, requested QoS, boundary CPU
IDs and load averages are explanatory only. Report all rows, checksums, memory, median,
min/max/CV, six effects 100*(mean(B)/mean(A)-1) and descriptive 95% Student-t interval
(df=5,t=2.5705818366147395). Same gate as AA-001: 24 valid rows/cell, unchanged counts,
checksum and tree-owned memory, each interval >=10ms, whole effect CI inside [-1,+1]%.
This is a descriptive precision rule; independence/normality remain assumptions.

A qualifying cell enables only scoped follow-up; missing guards and profile validation
remain mandatory. No source optimisation accepted. On failure, undertake new semantic
boundary coverage rather than repeating this schedule. Backend/model/token cost unknown;
supervisor records actual CLI usage separately. CPU MCP ask consulted, but retrieved
OpenVINO text irrelevant and not supporting evidence. Benchmark05/14 method/code read;
no measurements or CPU numbering transferred from their M4 Pro.
