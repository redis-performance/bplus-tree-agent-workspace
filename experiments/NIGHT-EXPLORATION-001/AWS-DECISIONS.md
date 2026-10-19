# AWS measured decisions — 19 October 2026


## 19 October — AWS AMD LOWERBOUND-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/865beadd/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/002-lowerbound/implementation-selection.md). Three sequential proposal passes and three isolated
implementations tested lazy packed-member metadata decoding in leaf lower-bound
search. All fail the 2% primary improvement gate at 100K and 1M. Median effects
for A/B/C are −0.434/−0.037/−1.281% at 100K and +0.441/+0.819/−0.702% at 1M.
No fresh confirmation or full performance guards were run after rejection.

Root independently reconstructed all 36 effects from 144 raw CSV processes and
verified serial windows, checksums, operation counts, seeds and owned-memory equality.
The difference from effects calculated using rounded ns/op is below 0.00015 percentage
points. All native/sanitizer and targeted semantic checks passed before timing.
The 1M A/A control remains unqualified. All three patches are retained; source NONE.

Historical Apple counts remain separately scoped, not silently combined with these.

[Independent raw audit](reviews/aws-amd-lowerbound-raw-audit.json).


## 19 October — AWS Intel SIMD-LOOKUP-001: REJECT / NONE

[Published decision](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/b8945b4d/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md).
Three sequential proposal passes and three isolated bounded SSE2 tag scanners were
measured against the frozen baseline. All three slow successful lookup in every
primary block: median A/B/C effects are +11.870/+9.236/+10.614% at 100K and
+9.654/+8.994/+3.891% at 1M (positive means slower). Source selection **NONE**.

Root independently audited 432 raw processes and 108 paired blocks, serial windows,
CPU2 boundaries, operation counts, seeds, checksums, fixture fingerprints and owned
memory. Native/sanitizer correctness and targeted first-match bounds checks passed.
The 1M A/A control remains unqualified; no fresh confirmation or full adoption guards
were needed after rejection. Instrumented whole-process gprof is not a scoped PMU
measurement. All three losing patches remain available on the host branch.

AWS completed measured populations: **2 — 0 accepted / 2 rejected / 0 parked**.
ARM's withdrawn, unmeasured index-mask proposal is excluded from this count.

[Independent Intel raw audit](reviews/aws-intel-sse2-raw-audit.json).
