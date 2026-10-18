# BOUNDARY-006 — bulk-delete thresholds validated

All48 cases pass release/debug and ASan/UBSan,240 full verifications/build. Exactly24
incremental and24 rebuild deletions straddle both >1024 and >=length/10 conditions;
24 cuts begin during naturally active resize. Prefix/middle/suffix, clone ownership,
reinsertion, full-range ULONG_MAX clipping, binary keys and signed zero pass. Batched
lookup count0..16, repeated members and output canaries are checked in every verification.

Two separately planned faults are detected: omitting the bulk index rebuild fails
a stale-index lookup invariant; shortening the oversized endpoint fails exact full-deletion count.
No baseline failures, root source changes, speed claim or optimisation acceptance.

[Plan](PLAN.md), [oracle](../../../tests/bulk_delete_oracle.c), [patch](oracle.patch),
[commands/source/binary hashes](manifest.json), [fault plan](MUTATION-PLAN.md),
[fault evidence](mutations/). Each child completed within its120s bound. The original
is not looked up before active-resize cuts: a duplicate is verified first, and the
original scan is checked not to progress migration. Private state is observed only.

Decision: sixth additional semantic suite validated; source NONE, lookup PARK.
Sequential coordinator review only; independent agent startup unavailable. Backend,
model and costs unknown; supervisor records CLI usage. Exact uncommitted snapshot
retained pending morning commit/review, no protected metadata or sampling retry.
