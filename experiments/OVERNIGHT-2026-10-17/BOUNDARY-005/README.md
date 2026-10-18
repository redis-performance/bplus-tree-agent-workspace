# BOUNDARY-005 — controlled collision paths validated

Final strengthened fixture passes release/debug and ASan/UBSan: two seeds, four
fixtures,622 cumulative full sorted-vector verifications per build. Observed lookup
wraparound to distance23,92 cumulative tag-mask false candidates,64 tombstone reuses,
22 cached-slot revision invalidations and six scans begun during active resize.
Both planned isolated faults were detected: clearing a tombstone tag breaks deletion
lookup; omitting home-tag recording breaks member lookup. Main source unchanged.

The first fixture design failed its >=23 lookup-distance precondition; attempt2 added
observations and also failed. Index entries can name the same leaf, so a member may be
found through an earlier matching-tag entry. Attempt3 gives the final bucket distinct
tags, preserving the >=23 requirement and every semantic check. Both failures remain
in [initial manifest](manifest.json) / [attempt2](attempt2/manifest.json), with exact
source snapshots. This was a test-design correction, not an observed source bug.

[Plan and amendment](PLAN.md), [final oracle](../../../tests/index_probe_oracle.c),
[final patch](attempt3/oracle.patch), [final commands/hashes](attempt3/manifest.json),
[fault plan](MUTATION-PLAN.md), [fault patches/logs](mutations/).
Private fields are read-only observations; normal APIs construct/mutate all fixtures.
Immediate FindForAdd/InsertNew pairs test invalidation during insertion. Successful
update positions and iterators are never retained across mutations. Reserve on an
existing set is correctly observed to be a no-op, not used to force a resize.

Decision: additional semantic coverage validated, no performance/candidate acceptance.
Source NONE, lookup qualification PARK. Review is sequential coordinator work; agent
startup failed, exact backend/model/token cost unknown. Uncommitted frozen snapshots
await morning review; protected git metadata and denied sampling were not retried.
