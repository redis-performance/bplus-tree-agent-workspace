# EXP-007: preregistered bounded bulk decoder experiment

User authorized testing once-per-leaf geometry specialization locally. This is a
private bulk helper appended to the original tree in isolated worktrees, not a
production API or scalar iterator modification. The original source remains the
control implementation inside a generic range loop. All variants materialize the
same double array before identical checksum consumption. Do not compare absolute
numbers to the previous direct-checksum harness as if the work were identical.

Primary: width60, forward physical orientation, count96, eight warmed leaves.
Guards: widths0,8,31,57,58,59,60,61,62,63,64, both directions, count96; plus
widths8,60,63,64 at counts1 and7, forward. Total30 cells. Use score shift0 for
timing; semantic checks cover zero/maximal valid shifts, every width0..64, both
directions, counts1/2/7/8/31/95/96, selected partial/empty ranges and exact finite
bits including explicit signed zero/subnormal bases. Finite synthetic leaves are
not necessarily sorted or minimally encoded whole-tree fixtures.

Fixed discovery: six ABBA blocks/cell/variant, seeds81031/81041 alternating;
129 samples/process,16 warmup batches, rounds=ceil(49152/(count*8)). Same-session
baseline/baseline A/A first, followed by baseline/A, baseline/B, baseline/C in
that fixed order; rotate cells per block. 2880 serial processes,371520 measured
batches. All phases combined have a300-second budget; child timeout is bounded
by remaining budget and30seconds. No other builds, profiles or tests overlap.

Report each process minimum/median/p90/max; pair A/B process statistics within
blocks; report median effect and full observed block range, not a confidence
interval. Same-cell A/A is qualified only if all six median effects lie within
±1%. Acceptance requires >=2% improvement on primary and no>1% regression on
any guard with adequately qualified controls. Unqualified or unexplained cases
remain PARK. No post-hoc removal, pooling of inner samples as independent trials,
or extension of failed timing schedules.

Diagnostic shortlist: among semantically valid candidates with primary median
improvement>=2%, prefer the one with fewest guard median regressions>1%, then
best primary median; ties within one percentage point favor smaller patch.
A shortlist is not acceptance. If any candidate has such a primary improvement,
run exactly one fixed fresh confirmation of the shortlisted candidate: same30
cells, six ABBA blocks,129 samples, seeds82037/82051 alternating, preceded by
fresh same-binary A/A. Budget180seconds. Otherwise skip confirmation and select NONE.
No retuning candidates after discovery. Fresh confirmation is a separate same-host
run, not an independent-machine replication.

Inspect generated assembly before timing (retained output stores and decode loops),
and compare selected/control code after measurements. Collect bounded sampling
profiles if the host permits; failed profiling is retained. Hardware counters,
frequency/effective QoS and within-window migration are unknown on this unpinned
M1. Do not infer cycles from wall time. CPU Performance Engineering MCP consulted;
its broad retrieval does not establish this decoder's mechanism.

A bulk-only gain cannot clear EXP-004's original mixed-output iterator guard or
justify changing the scalar API. Scalar integration needs an explicit design and
matching validation. Keep a promising bulk candidate PARK pending that transfer,
independent confirmation and adversarial review. The overnight runner stays stopped.
