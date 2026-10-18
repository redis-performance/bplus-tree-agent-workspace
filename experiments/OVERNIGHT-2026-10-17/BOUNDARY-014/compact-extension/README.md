# BOUNDARY-014 — exhaustive compact-size extension

**All eight semantic runs pass; the preregistered cross-build whole-output equality
prediction fails.** No source or suite-count change. Original plan, runner assertion,
manifest and child output are retained; no child was rerun or oracle weakened.

Control and retained EXP-004 A/B/C, in release/debug and ASan/UBSan, each pass all1,940
fixtures: every size0..96, five record-boundary lengths, two seeds and both insertion
orders. Each checks289,060 complete model states and86,570,560 exact-score results,
matching the totals derived before running. Rank, lookup, scalar packed reading, leaf
ID links, zero score bounds, ownership/memory, clones, updates and draining all pass.
The two original source fault types are caught by the new matrix in sanitizer builds.
This extends BOUNDARY-014; campaign remains14suites/28distinct boundary fault types.

All1,940 per-fixture lines are identical across eight builds. The last aggregate line
has different forward/reversed-leaf and reversal-opportunity counters between release
and sanitizer builds. Every candidate matches its control within each build. Total model
and exact counts match across builds. Native/ASan usable sizes and compiler/instrumentation
differ; allocator-dependent compaction is plausible but not established here. Treat the
cross-build physical-layout claim as unsupported, not as a passed check.

The wrapper renames the original main, producing a missing-return warning in that unused
function. It is never called; the additive main calls the unchanged exercise directly.
No runtime sanitizer error occurred. A future cleaned wrapper should omit the old main
rather than modify the frozen oracle; any such revision needs its own validation.

[Plan](PLAN.md),[retained original manifest](manifest.json),[read-only audit](audit.json),
[exact faults](faults.json). Source and binary hashes retained. Review is sequential;
backend/model/cost unknown. Main baseline unchanged; EXP-004 A/PARK unchanged.
