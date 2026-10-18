# Same-size tombstone cleanup SCAN interval extension

New correctness coverage, not a timing trial. Seeds63503/63521, control/EXP-004 A/B/C
native-O3/debug and-O1ASan/UBSan;120sserial children,600swhole matrix. Same frozen
source and unchanged ambient allocator. Reuse independent per-call interval and full
sorted-vector/owned-memory checks from BOUNDARY-022, frozen separately before execution.

Construct448real-hash binary keys: seven per each home bucket0..63, mixed16/319/320/321
bytes and folded upper tags0/1/254/255. Reserve320 gives64buckets; verify filled448.
Delete first224members (home0..31), leaving224live and448filled, above shrink threshold.
Add31new members at home32..62, raising filled479. The32nd new member (home63) must
start a SAME-SIZE64→64 cleanup because filled+1 hits15/16 while live256fits64buckets.
No private mutation or assumed flag: require actual same-sized source/destination,
uncopied leaves and destination.used<length. Save a valid miss insertion position
before additions, use it for the triggering insertion; the resize inside that insertion must make its
revision stale, and production must validate/reject the cached position normally.

Before lookup checks can drain cleanup: run all SCAN hints0/1/7/ULONG_MAX and require
per-call interval completeness, exact values and non-mutating scan metadata. Clone
while cleanup active; verify clone independently; original pointer/cursor/revision and
ownership must remain unchanged. Verify original to finish cleanup. Use another saved
miss position after old table is released to exercise revision fallback without private
state edits, then verify. Check all state transitions, not just final cardinality.

One isolated sanitizer fault treats equal source/destination scan masks as one table
and skips the destination. Must build and fail per-call interval completeness. Existing
SCAN faults are not rerun because this fixture deliberately creates little displacement.
Missing recipe coverage is failure; keep it and preregister any change. Source NONE,
existing PARK unchanged, sequential review only; no optimizer/suite count increment.

Attempt002 preserves original failed precondition and frozen snapshot. Source inspection
shows ordinary insertions do not advance member_revision; resize start/copy/completion
do. Require revision SAME immediately before triggering insertion and DIFFERENT after
the actual cleanup begins. Print filled/size/used/revision before this assertion. All
cardinality, filled-slot, active-copy, full-model and ownership checks are unchanged.
The invalid precondition belonged only to this new fixture, not production/existing tests.
