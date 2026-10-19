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

AWS measured optimization populations: **1**; **0 accepted / 1 rejected / 0 parked**.
ARM withdrew one unmeasured index-mask proposal after correcting profile attribution;
it is not counted as a completed measured population. Intel's screen is in progress.
Historical Apple counts remain separately scoped, not silently combined with these.

[Independent raw audit](reviews/aws-amd-lowerbound-raw-audit.json).
