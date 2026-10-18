# Next distinct scope: score moves during actual mixed-width migration

Preparation only, not an executed or preregistered experiment. Round16 continuously
scans through natural widening, clone/relocation, external ownership, bulk renumbering
and narrowing. Inserted scores remain monotone. BOUNDARY-003's random score movement
begins after its large wide fixture has finished migration. Natural mixed-width score
moves crossing old/destination leaf ownership while the same cursor is live remain a
distinct candidate coverage scope.

Possible recipe: reuse bounded natural inline construction near threshold and observe
an incomplete narrow→wide resize before mutation. Update two continuously present
anchors via fresh public FindForAdd/UpdateScore calls between each SCAN call, moving
one across the minimum and another across the maximum; include exact signed-zero
updates separately without assuming identical physical score encodings. Preserve all
key bytes, hashes and continuous memberships. Add separately allocated members if
external detach/reattach is targeted. Private state is read-only, no forced generation.

The current simple ID-order model cannot validate that recipe unchanged. Build an
independent score/member sorted model, track CURRENT exact score bits at callback time,
and avoid O(N²) verification for the natural~400k-member fixture. Bound full model checks
at declared state boundaries; per-call interval checks can reuse sorted immutable hashes
with current-score lookup by ID. Fresh successful positions only; never reuse stale
score positions. Observe migrated/unmigrated source/target leaf ownership before asserting
coverage; extra lookups themselves advance resize. Require actual cross-table movement,
not just an active flag. Preregister bounded seeds/mutations/builds and fault controls.

Performance work needs a separately qualified runner or a distinctly justified new
method. No unchanged retry of failed duration/warmup/QoS/caller/placement/bookkeeping/
transport trials; no substitution for the original unresolved guard. Keep baseline
through separate morning review. Final worker owes MORNING-REPORT.md by07:00UTC.
