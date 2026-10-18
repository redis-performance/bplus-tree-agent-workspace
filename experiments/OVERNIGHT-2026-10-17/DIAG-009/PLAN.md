# DIAG-009 — timer delivery-rate calibration and helper consolidation

Preregistered2026-10-17 before build/measurement. PROFILE-002 observed similar sample
counts for requested1000us/3001us; requested intervals are not established effective
cadences. DIAG-006 corrected profile dump timing but retained an archival calibrate.c
with the old helper interface. This fresh isolated diagnostic fixes that interface and
measures aggregate delivered-sample rates on a known noinline arithmetic function.

Hypothesis: requested1000us and3001us yield similar delivered samples per thread CPU
second (ratio in[0.90,1.10]) while requested17011us yields a lower rate (ratio to1000us
<0.75). This is a diagnostic of this timer implementation, not CPU clock/frequency,
exact signal interarrival intervals, unbiased-PC sampling or source performance.
No timestamp or library call added inside the signal handler. Installed SDK sigaction
manual does not list clock_gettime as async-safe, so timestamps remain outside handler.
Lock-free atomics/context-only handler is unchanged from DIAG-006. Public getitimer
values are observed after arming; denominator includes setup/stop, handler overhead
and boundaries. Profile output remains after wall/thread endpoints. Aggregate rates
can include coalescing/delivery delays and censoring at boundaries; no attribution to
specific kernel tick or exact quantization without further evidence.

Frozen snapshot derived from DIAG-006: only calibrate.c changes. Known loop400000000
iterations,8 dependent AArch64 adds/iteration, exact result3200000000. Six fresh blocks,
three requests/block in rotating order(1000,3001,17011) by(block-1)%3.18 measured processes.
No excluded normal-sized warmup. Small10000-iteration mode with requested0/1000 validates
both release and ASan/UBSan; excluded prospectively. All builds/tests finish first;
serial measurements with child<=120s/full campaign<=120s. Preserve failures/no optional
stopping/count adaptation/outlier filtering. Symbolicate after all measurement processes.

Require >=20 samples each, no overflow, correct checksum, >=90% PCs resolve to known
function, all clocks valid. Criterion:1000/3001 rate ratio within[.90,1.10] in>=5/6 pairs
AND median in same interval;17011/1000 ratio<.75 in>=5/6 pairs AND median<.75. Both arms
required; otherwise unsupported/inconclusive. Save individual rows,actual getitimer
interval values,thread/wall durations,PC counts,known-function shares,all six ratios.
No profile-derived speedup or previously parked source claim will be promoted.

Apple M1 ARM64 established4P+4E/noSMT inventory, one thread, macOS26.3, Apple Clang17,
C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer; libc support. CPU clock/turbo/effective
QoS/residency unknown. Same compiler/assertion options, no frequency conversion or M4
value transfer. Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus saved uncommitted
snapshots/patches. Root untouched. SDK getitimer/sigaction inspected; MCP methods already
consulted this round, evidence checker before headline. Sequential coordinator only;
backend/model/cost unknown. Raw PC/symbol output retained ignored scratch with hashes.
