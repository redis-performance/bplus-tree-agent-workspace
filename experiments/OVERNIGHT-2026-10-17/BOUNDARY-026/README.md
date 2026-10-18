# Heterogeneous prefix and duplicate batch lanes — PASS

All32 planned source/build/seed cells pass, including16fresh confirmations with
debug-only assertions disabled. Each checks1,345 keys across64binary prefix families
and the empty key, six sorted live-vector models,342,975batches and2,743,800lanes.
Every cell checks1,567,343 exact-score results,1,452,600aliased lanes,1,291,200copied
lanes and195,025heterogeneous batches. Full digests agree across all sources/seeds/
builds; complete output including owned-byte checkpoints agrees per build and seed.

All counts0..16 are checked through empty/all-hit/deleted-mixed/reinserted-cloned/
cleared states. Exact signed zeros, finite extremes, prefix lengths through4,096,
input fingerprints, hit masks, outside-count canaries, rank and both iterator orders
pass. Miss output slots are not constrained. Public queries settle migration before
owned-memory equality checks; this is not an active-resize coverage claim.

Both deliberate lane0-hash and lane0-length reuse controls are detected. They are
reported separately and not added to the54historical distinct boundary fault types
without a taxonomy review. No production defect found. Initial missing math.h build
failure and its exact source remain; attempt002 adds only that required include.

Freeze/plan, added-test patch and discovery/confirm/fault manifests are in attempt-002/.
All sources are isolated EXP-006 control/A/B/C snapshots; main source and15optimization
patches remain. SourceNONE; EXP-006C/PARK unchanged. One new named boundary suite,
total26. Correctness adds coverage; it does not repair failed performance guards.
Review/confirmation sequential, backend/model/token cost unknown.
