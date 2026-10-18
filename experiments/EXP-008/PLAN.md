# EXP-008: hybrid scalar-short / specialized-bulk-long crossover

Test whether retaining the original inline scalar range loop for short requests
removes EXP-007 B's short-range regressions while keeping its measured bulk gains.
No change to public iterator, tree representation or root production source.
Control calls frozen B for every range. Candidates use the same B helper above the
chosen threshold and the original scalar decoder loop below it. Cutoffs are inclusive:
A uses scalar for count<=4; B for count<=8; C for count<=16. A/A and every candidate
share the same double output array, materialization barrier and four checksum chains.

Primary: width60, forward orientation, count16, paired median ns/score, minimum2% gain
over control. Also require a >=2% gain at width60,count96. Full fixed matrix: widths
8,57,58,59,60,61,62,63,64 × both physical orientations × counts1,2,4,7,8,16,32,96.
Width0 with counts1,7,16,96×both orientations is a zero-width diagnostic. All are guards
except the two width60 forward primary cells. Reports include each cell individually.
Short count1 is intentionally seed-invariant (delta0 fixture); longer fixture values
use alternating seeds. Correctness covers widths0..64, both directions, zero/max shifts,
counts1,2,4,7,8,16,32,96, selected partial/empty ranges, finite extremes and signed zero.

Fixed measurement: six ABBA blocks/cell; seeds81031/81041 alternating;129 in-process
samples and16 warmups. Same-session B/B A/A across all cells, then control/A, control/B,
control/C. Rotate cell order by block. 10 widths×2 orientations×8 sizes=160 cells;
Each phase has160×6×4=3840 processes. A/A plus three candidate phases total15360 serial processes and1981440 measured batches. Batch rounds=ceil(49152/(count×8)). Count-one fixture values have delta0, so those cells are seed-invariant; fresh runs change their measurement session, not input values. Campaign wall budget300 seconds, each
child capped at30 seconds/remaining budget. No overlapping builds/profiles/tests.

Discovery threshold-selection rule: eliminate any candidate with a median paired
guard regression>1% in cells whose A/A all six median effects are within±1%; unresolved
A/A guard cells stay PARK. Require both declared primary gates. Among eligible variants,
choose the fewest guard losses, then lower count-threshold; never choose from one noisy
primary alone. If none eligible, skip confirmation and select NONE/PARK.

If a candidate qualifies, confirm exactly one: same160 cells, six ABBA blocks,129
samples, new A/A, seeds82037/82051, total budget180seconds. This is same-host confirmation,
not independent-machine replication. Preserve all rows, no outlier removal, no post-hoc
threshold changes. Report medians, minima, block ranges (not confidence intervals),
source/binary hashes, owned bytes and observed stack usage if available.

Inspect codegen before timing: threshold must be outside the score loop, short path
must inline/avoid the B helper call, long path must retain B decoder loops and output
stores. Profile baseline and selected candidate on their actual binary; system sampling
includes setup/warmup and is not timed-only CPU attribution. No cycle inference from Mac
elapsed time. Existing B stack output storage is part of the referee; no tree-owned leaf
memory increase allowed. A bulk crossover does not prove scalar iterator performance;
that needs a separate design, benchmark and guards.

Reproduce with build.py, validate.py, run.py and analyse.py. Source baseline is frozen
EXP-007's root source commit4fd3a3f; bulk helper bytes are frozen at EXP-007 B. Referee
must be committed before timing. Keep every threshold patch. EXP-007 remains PARK until
a distinct guarded policy qualifies.
