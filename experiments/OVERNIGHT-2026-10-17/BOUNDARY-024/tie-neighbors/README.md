# Actual equal-neighbor ordering rejection

All 16 fixed source/build/seed cells pass the separately frozen neighbor fixture.
ID256 changes to score255 and ID511 to score512 while migration is mixed-width and
the SCAN cursor remains live. Their binary keys require reordering past the equal
neighbor, even though both updates retain the same leaf ID. Each cell passes six
full sorted current-score models, 336 inclusive/exclusive range counts, both exact
signed-zero updates, all live SCAN intervals/anchors and owned-memory accounting.

The previously surviving skip-equal-neighbor-order fault is now **detected** by the
unconditional sorted-model oracle in its successfully compiled sanitizer binary.
The earlier survivor remains unchanged under ../finite-ties/faults/. This is a new
fixture with an explicit missing branch precondition, not a rerun of the old trial.
No production bug is claimed; no original test or threshold was weakened.

Each fixture makes 262 total score updates: 260 general and two tagged signed-zero
updates. The two added neighbor moves retain their leaf ID; 258 other updates cross
leaves. Output digests agree across all four sources and both builds per seed. New deliberate fault
type count increases by one. Source NONE; all existing performance PARK remains.
See PLAN.md, run.py, manifest.json, summary.json, oracle.patch and faults/ for commands,
raw evidence and explicitly uncommitted snapshot provenance. No timing result.
