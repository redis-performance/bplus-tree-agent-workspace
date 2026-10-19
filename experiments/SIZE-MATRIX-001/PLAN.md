# Four-size sorted-set baseline

Requested matrix: 100, 1,000, 10,000 and 100,000 members, all eight operations in
`bench/microbench.c`. Baseline coverage only; no candidate or population selection.

Freeze before timing: existing tree/referee, Clang C11 -O3 with frame pointers,
libc allocator, 16-byte binary members, integer scores, seeds 1/2/3. One unpinned
thread on Apple M1; frequency/core residency unknown. No Redis server.

Six same-binary ABBA blocks per size, seeds 1/2/3 repeated twice. Rotate size order
by block; each process runs the fixed eight-case order. Total 96 processes / 768
rows / 32 cells. One million requested operations, one lookup warmup pass; setup
and fixture creation outside timing. Insert/delete each process one complete
lifecycle of N members; iteration rounds to full traversals, scan counts callbacks.
Update raises scores by N each visit. Other point operations repeat a shuffled order.
The eight cases each use a separate tree; there is no interleaved read/write mix.

Use the existing harness without changes. Build from scratch, run native and
ASan/UBSan tree tests, then all four sizes through the sanitizer benchmark with
2N+1 requested operations and seed 101. No tests/builds/profiles overlap timing.
Timing budget 300 seconds; no adaptive retries or removed outliers. Preserve all
rows, hashes, commands, compiler and machine metadata. Fail rather than report a
complete matrix when commands, checksums or expected coverage fail.

Report median/min/max batch-average ns/op and all six A/A block effects per cell.
Report the shortest timing window and flag <10 ms, especially small insert/delete.
These baseline observations do not establish precision for 1% comparisons or
individual-operation latency percentiles. Same-size A/A differences show variation;
size differences are different workloads, not optimization speedups. No cache-miss
or cycle claims without counters. The CPU Performance Engineering MCP was consulted
about repeated controls; its retrieved material is not evidence for this tree.

The same scripts must accept a new host-specific output directory for the planned
Apple M6 mini run. Keep both hosts' raw results and summaries separate.
