# Public shrinking-resize and end-of-list cursor extension

Preregistered after COUNTERS-007 shows its three public schedules never enter the
member-cursor NULL fallback. New coverage question, not a retry of timing evidence.
Same BOUNDARY-019 suite; all four source snapshots × native/debug and ASan/UBSan.
Two fresh seeds60413/60427 × two monotonic score families, four fixtures per cell.

Reserve a fresh tree for4096members and insert4096binary319-byte members publicly.
Delete three inclusive prefix ranges of1024members each (small-delete branch must
not rebuild/renumber). Require no resize after the firsttwo and a naturally started
smaller member table after the third, with length1024 and unmigrated last leaf.
Check full sorted-vector/scan/ownership model after each deletion without lookups.

Drive rehash solely with bounded4096public lookups of the last member. Verify full
model after every7lookups, requiring observation with both tables populated. Require
same active shrinking resize when next_leaf_id becomes ZBT_NO_LEAF_ID and all live
members are copied. Check model/scan at that sentinel state and clone it. One further
lookup must finish both source and cloned resize independently. Then insert at most128
new unique members until one real leaf allocation reuses the exact free-list head,
with no highwater growth/new resize. Check all lookups/ranks, clone ownership and
exact usable-size sums. Capture physical counts separately; no timing claim.

One new isolated sanitizer fault disables small/large table orientation swap in
zbtreeScan; require runtime detection. Exact sources/commands/hashes and all failures
retained. Child120s,matrix600s. Existing original suite/checks unchanged; no new suite
count. A separate branch capture after correctness may test the new fallback route;
its data will remain distinct from COUNTERS-007's completed three captures.
