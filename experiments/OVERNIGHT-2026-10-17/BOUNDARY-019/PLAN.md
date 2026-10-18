# BOUNDARY-019 — public leaf-ID lifecycle during incremental resize

Preregistered before execution. No timing claim, policy change or source adoption.
Use baseline and retained EXP-004 A/B/C isolated snapshots, native -O3/REDIS_DEBUG
and -O1 ASan/UBSan, unchanged allocator and support; eight cells, child120s,
whole validation matrix600s. Exact baseline commit and SHA256 files frozen by driver.
Main source/referee preserved. Two seeds60101/60127 and two deletion modes per seed.

All construction/mutation uses public APIs. Read-only private observations establish
coverage and allocation accounting. Generate319-byte binary unique members with
big-endian ID prefix, monotonically ordered scores; mode1 adds equal-score groups
and signed zeros. Insert at most65536 members; stop at the first naturally triggered
resize with at least128 uncopied leaves. No lookup/rank checks consume this window.
Mode0 retires the saved next-leaf cursor; mode1 retires an already migrated leaf.
Delete exactly one whole leaf by rank (<=96members), require same active resize,
freed target ID and unchanged highwater. Mode0 requires the cursor still names the
retired ID. Perform at most128 monotonic public insertions to allocate four actual
new leaf IDs while the same resize remains active. Require every retired ID stays
free and no free ID is reused. Fail coverage rather than privately force state.
Finish rehash with at most65536 public lookups, then force another actual leaf
allocation with at most128 insertions. Require LIFO reuse of the saved free-list
head, no highwater growth and no new resize. Preserve any coverage failure.

At each phase, independent sorted-vector model checks forward/reverse iteration,
binary lengths/bytes, exact finite score bits, seek-rank results, scan completeness
(duplicate callbacks permitted) and unchanged observation state. Independently walk
parents/subtree counts, leaf links, registry/free-list and allocator usable-size sum.
After coverage capture, check every live/deleted member lookup and rank; clone active
and settled trees and validate independent ownership. Retain logical digests and
physical transition logs; allocator-dependent IDs need not agree across builds.
Require actual coverage separately in each fixture/build, never infer it from digest.

Two isolated sanitizer faults: premature free-ID reuse during rehash; treating a
retired saved cursor as end-of-rehash instead of restarting at the first live leaf.
Existing tests/checks unchanged. Faults must compile and be detected at runtime.
Run original43tests on each source/build if time permits, otherwise explicitly report
unrun. No acceptance inferred. Independent agent startup failed before execution;
review sequential, exact backend/model/tokencostunknown.
