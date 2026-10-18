# Live SCAN cursor through natural widening, bulk renumbering and narrowing

Additive correctness scope with unchanged control/EXP-004 A/B/C sources/allocator.
Seeds68501/68521, both native-O3/debug and-O1ASan/UBSan:16fixed run cells,120schildren,
600sserial matrix. Independent snapshot/patch before first build. No benchmark claim.

Start from original BOUNDARY-023 all-inline319-byte recipe and independent hash-interval
oracle. Designated continuous anchors are the LAST4096initial members, chosen before
SCAN starts. Keep normal append16until natural migration completes. After ONE actual
completed-wide SCAN call, keep its nonzero cursor and delete the appended suffix, then
initial prefix, using public rank-range deletion. Only the last4096initial members
survive. Require actual narrow index, no active resize, next_leaf_id below widening
threshold, dense IDs changed from prior high-valued survivors, and exact cardinality.
Do not inject IDs or change thresholds. Both large deletions return exact model counts.

Expected current model is contiguous [low_id,upper_id), independently reflected in
callback validity, full ordered iteration, rank/seek samples, lookup and interval tests.
Check EVERY removed member absent after the cuts, preserving exact bytes and finite
score=id. Verify parent/subtree/registry/usable allocations; original largest-group
bound continues across contraction. Same numeric cursor must terminate, every designated
continuous anchor seen, current interval complete on every call. Static complete scans
at0/256/ULONG_MAX and clone-after-free retain original checks. No claim deleted anchors
must appear; additions outside their yet-unvisited intervals have no completeness promise.

One sanitizer fault keeps stale leaf IDs while publishing the compacted registry in
zbtScoreRenumberLeaves (new precise fault type). Must compile and fail registry/oracle/
production assertion or sanitizer. Preserve any failed recipe and revise only under a
new preregistration. Existing BOUNDARY-023 checks remain immutable; this model extension
explicitly accounts for deletions. Suite count23unchanged; sourceNONE/performancePARK.
