# Partial batches across natural width promotion

All eight discovery source/build cells pass, with18independent active-resize clones
per cell covering counts1,2,3,7,15,16 and all-hit/all-miss/alternating layouts. Each
cell checks25sorted models and21,864,700exact iterator/member results. Count1's
alternating case is a hit, not mixed coverage. Actual promotion occurs inside every
matrix batch. The last-lane attribution follows the observed remaining-leaf count
and inspected one-step-per-lookup implementation; direct lane instrumentation is pending.

The full retained live cursor oracle still passes:260external score updates, six
original model boundaries, continuous anchors, SCAN intervals, source ownership,
lengths and usable-byte accounting. Additional clone models explain the total25.
Every clone has disjoint external storage and both index tables. Zero count preserves
resize state with null inputs; outside-count canaries and exact hit masks/scores pass.
Miss output values are not constrained. No private state is mutated by the oracle.

Fresh seed80521 confirmation passes all eight cells with REDIS_DEBUG omitted. All
three promotion-specific faults are detected: stale table cache (ASan UAF), omitted
last hit, and outside-count output write. The first two repeat existing fault families;
the third adds one distinct type. No original check was weakened. Exact fault sources
and outcomes are in faults/ and faults.py, with the separate FAULT-PLAN.md.
[Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json), [driver](run.py),
[patch](oracle.patch) and [sequential review](REVIEW.md) preserve provenance and limits.
No production defect or source speedup is claimed. Source selection NONE; existing
EXP-004A/PARK and EXP-005PARK/NONE remain. Main source/referee are unchanged.
