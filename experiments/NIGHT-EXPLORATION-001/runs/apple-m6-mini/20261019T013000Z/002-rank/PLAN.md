# M6 rank diagnosis and one referee freeze

Started round 1. Baseline source is launch-manifest.json SHA256, acknowledged status
commit 48b00870. No candidate. All actions serial; no builds/test/profile overlap
with timing. Build clang C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer, no LTO;
compat allocator and assertions unchanged. Sanitizer is -O1 ASan/UBSan, never timed.

Public harness: bench/night-rank.c includes frozen historical bench/microbench.c
for helpers. Construction and query RNG streams independent, fixed binary members,
16-byte primary. Sorted score/member oracle checks all ranks, reverse, score bits,
misses and traversal. Layouts integer/ties/finite; finite includes signed zeros and
extreme finite doubles. Native and sanitizer checks must pass before timing.

Public profile at 10K/100K/1M: external sample availability/permission recorded once;
existing SIGPROF sampler in separate instrumented binary if available. Requested
1ms cadence is not guaranteed. Calibrate known busy function and inspect release
and instrumented assembly. Never use instrumented elapsed times as performance.
Missing valid profiling blocks adoption. CPU Performance Engineering MCP is absent
from callable tool catalog; no fabricated audit. No hardware counters requested.

Private diagnostic: adapted exact published M1 accumulation-diagnostic.c; moves
expected checksum construction outside timer. Pre-resolves leaf/position, verifies
ranks then times zbtScoreRank; separate COUNT_MODE emits depth/sibling census. Private
cache path differs from public; never subtract timings to estimate components.

Baseline calibration: three untabulated observations per cell at 1M operations,
10K/100K/1M, choose ceil(50ms / fastest positive ns/op), cap 100M. Freeze counts once.
Use three warmed batches per process for retained min/median/range, not independent
replicates. Six serial process-level ABBA blocks, seeds1/2/3/1/2/3; rotate sizes by
block. Qualification requires every block within +-1% and every window >=10ms.
300s timing budget, 120s child cap. No outlier deletion or rerun. Candidate plans
will be frozen separately only after profiles and sequential proposal/chair passes.
Primary public rank100K and1M; all shared PLAN guards remain mandatory for adoption.
This round may finish diagnosis and calibration without beginning implementation.
