# BOUNDARY-025 preregistration — partial batches at width promotion

Frozen before execution, round18. Hypothesis: public batched score lookup remains
correct when natural narrow-to-wide index promotion completes on the last requested
lane for counts1,2,3,7,15,16, with all-hit, all-miss and alternating layouts.
Count1 alternating degenerates to a hit and is not mixed hit/miss coverage.

Retain the complete round17 corrected live-score oracle and all its checks, in a new
file. After its128 score-move pairs, inspect uncopied leaves read-only and advance
only through public raw miss lookups until15remain. Clone this state independently
for18cases. Public misses advance each clone until count-1uncopied leaves remain;
one further lookup completes promotion after all leaves are copied. No private
cursor/generation/ID writes. Require active narrow/wide entry and completed wide exit,
exact hit masks/bits, unchanged outside-count canaries and unchanged length. Miss
score slots remain unspecified. Count0 must not advance or write, with null inputs.

For each clone require separate member-table allocations, disjoint external buffers,
exact own usable-byte accounting, full forward/reverse sorted model and lookups,
sampled ranks, and unchanged source metadata/owned bytes. Free each clone and retain
source for the original liveSCAN/anchor/score-transfer checks. Cloning may use distinct
usable allocation sizes; never impose cross-allocator byte equality.

Control and retained EXP-004A/B/C, all from EXP-004freeze base+SHA256 snapshots.
Discovery seed80503 with REDIS_DEBUG; nativeO3 and O1ASan/UBSan,8cells. Fresh confirmation
seed80521 without REDIS_DEBUG, same8cells, separately frozen before it starts. All
unconditional oracle checks remain. Children serial, each120s limit, driver900s cap.
No timings or performance claims, no source adoption, no new population.

Sensitivity controls after passing matrix: retained stale-table-cache fault (repeat),
a last-lane hit-mask omission fault, and count-overrun output write. Record survivors.
First fail stops normal matrix; preserve all outputs and failed snapshots. A fixture
correction is a separately frozen attempt, never an overwritten result.

Review is sequential because reviewer agent startup failed before running. Exact
backend/model/token cost unknown; supervisor records usage separately. Root source,
referee and all prior evidence stay unchanged. No git metadata retry or publication.
