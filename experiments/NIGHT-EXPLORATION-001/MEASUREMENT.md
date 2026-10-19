# Shared measurement and decision protocol

## Freeze and calibration

Both hosts use the same source revision, benchmark definitions, seed schedule,
Clang C11 -O3 without LTO, allocator and assertion policy within each comparison.
Record actual compiler versions; compiler differences across hosts are a confounder,
not a reason to hide results. Never run a sanitizer binary for timing.

Before candidates, calibrate baseline only: three untabulated observations per cell,
choose a fixed operation count targeting at least 50 ms using the fastest positive
observation; cap at 100 million operations. Freeze counts once, use them for baseline
and every candidate, and retain calibration. No per-candidate adaptive counts.
If the cap cannot reach the target, record that and do not claim fine precision.

For short insert/delete cases, a separate harness revision may batch independent
whole lifecycles under one timer. Prepare empty/populated trees outside timing as
appropriate; time the intended insert/delete work across replicas; retain total
operations and per-tree correctness. Cap replicas at 4096 and estimated tree-owned
memory at 64 MiB. Record actual working-set size: replicas change cache conditions.
Do not add construction/destruction to a delete-only time, subtract empty-loop cost,
or silently replace the historical benchmark. Requalify a changed harness.

Use monotonic wall time. Report minimum, median and observed range of batch-average
ns/op, never call these individual-operation latency percentiles. Preserve checksum
consumption, final-state checks, and generated assembly showing intended work remains.
Separate setup, warmup, correctness, profiling/counters and timed measurements.

## Fixed comparison schedule

Discovery seeds 1/2/3, each used in two of six blocks. Confirmation seeds 101/102/103,
also six blocks. Each block is A B B A, one process at a time. Rotate cell/variant
order deterministically before running. Use identical baseline A/A controls first.
No overlapping builds, tests, profilers or local agent work during timing.

A/A effect per block = 100 × (mean B ns/op / mean A ns/op − 1), with identical code.
A cell is qualified for the strict adoption gate only if every A/A block lies within
±1% and each timed window is at least 10 ms. Failure does not invalidate coverage;
it prevents fine-grained acceptance. Permit one separately frozen causal diagnostic,
then PARK unresolved comparisons rather than rerunning until they pass.

Candidate effect uses the same formula; negative means less time. For adoption require
both declared primary cells to improve by at least 2% in every fresh confirmation
block, no guard block above +1%, qualified same-session controls, and no >1% owned-memory
increase. This conservative observed-range rule is not a confidence interval.
No guard may be dropped because it is noisy or inconvenient. Memory/speed trade-offs
need a separately declared experiment, not a changed gate after measurement.

Per comparison phase: 300-second timing budget; confirmation 300 seconds; each child
at most 120 seconds and bounded by the round deadline. If the full declared matrix
cannot fit, retain partial evidence and defer acceptance. A bounded primary-only
screen can reject candidates but cannot accept one. Prefer fewer hypotheses over
silently shrinking required guards. No outlier removal or optional stopping for wins.

## Two population decisions

1. After profiles, three independent proposals inspect the same evidence; a chair
   chooses one falsifiable hypothesis or NONE and records reasons for all three.
2. Three isolated implementations start from the same source/harness. Native tests,
   ASan/UBSan and targeted semantic checks precede serial comparison. Retain every
   patch and loss. Shortlist only a candidate that passes the discovery gates.

Use actual independent agents when permitted and available. Otherwise label three
sequential passes explicitly; do not claim independence. Record actual identities,
model and measured usage, leaving unavailable information unknown. Do not launch
agent populations just to prepare documents or while timing is active.

A shortlist receives fresh confirmation, baseline/candidate profiling, assembly
inspection and adversarial review. Missing independent review keeps adoption pending;
fresh seeds on one host are not another-machine replication. Keep main tree source
unchanged overnight, even when a candidate passes locally.

## M1 and M6 comparison

Capture actual CPU, architecture, core count, OS, compiler/flags, source/binary hashes,
workload and method. Frequency, DVFS, core residency and counters remain unknown when
not measured. Never assign M1/M4 CPU numbering, frequencies or results to M6.

Use paths runs/<host>/<run-id>/<experiment>/<phase>. Store baseline and candidate on
each host, compare locally, then compare effect direction/size across hosts. Never
pool samples, copy binaries, or compare M1 baseline directly to M6 candidate as a gain.
Shared contender identity requires the same patch and harness hashes. If hosts choose
different candidates, replicate both exact candidates later rather than blending them.

A candidate can be M1-only, M6-only, conflicting, or reproduced on both. Mark NOT RUN
when the other host has not tested it. Publication records both passing and failing
workloads and any toolchain differences. Use CPU Performance Engineering MCP for
method/code questions, but do not let a heuristic audit replace the actual evidence.
