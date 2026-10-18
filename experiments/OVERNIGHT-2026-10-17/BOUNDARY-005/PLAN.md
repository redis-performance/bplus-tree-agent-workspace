# BOUNDARY-005 — controlled bucket wraparound and insertion revisions

New semantic coverage; no performance run/candidate. Root source/referee unchanged.
Two deterministic hash seeds (7,107), mixed binary lengths16/319/320/321. Generate257
unique keys whose actual SipHash low six bits all equal63 and whose upper byte cycles
254/255/0/1. This forces shared home buckets, wraparound and repeated tags/folded zero;
no hash stub or private-state construction. Fixed nonce search cap10000000/key.

Reuse the unchanged sorted-vector oracle from boundary_oracle.c, adding an entry point
and including tree implementation for read-only precondition observations. Construct
and mutate through public APIs only. Two fixtures/seed:

1. Reserve a fresh tree for320 members (64 buckets); insert192. Assert a probe distance
   of at least23 buckets, wraparound, and actual tag-mask borrow false candidates. Delete
   first32 keys, confirm tombstone occupancy/filled count, verify downstream hits/misses,
   then insert32 absent keys and confirm tombstone reuse without filled growth. Check
   ignored Reserve on nonempty tree. Full model verifies score bits, ranks, batch/raw
   lookup, binary ownership, iteration and complete scans.
2. Fresh unreserved tree, insert all257 through immediate FindForAdd/InsertNew pairs.
   Observe saved-slot revisions invalidated by insertion-triggered natural growth.
   Scan active resizes before full lookup verification drains migration; require active
   resize and cached-slot invalidation observations. Use no stale successful update
   position or retained iterator/member pointer across a mutation. Validity assertions
   are not bypassed. Finish delete/reinsert and independently owned duplicate coverage.

Run release/debug and ASan/UBSan, each child <=120s. Save commands, hashes, all failures
and exact source patch. Then fixed isolated fault controls for tombstone termination
and missing home-tag recording. No performance acceptance; tests augment, never weaken,
prior checks. Independent agent startup failed; sequential coordinator review only.
Backend/model/cost unknown; supervisor records actual tokens. Base commit plus exact
uncommitted snapshot provenance; protected git metadata not retried.

## Fixture amendment before attempt3

Initial precondition failed: maximum *lookup* distance20 despite192 entries in24
buckets. Attempt2 only added observation output, revealing48 false mask candidates
and151 wrap hits. Lookups may find a member via an earlier entry with the same tag
and score-leaf ID, so physical occupied distance does not imply lookup distance.
This is a fixture-design failure, not a baseline bug. Retain all initial outputs,
snapshots and hashes. Strengthen the fixture: keys184..191 use unique upper hash
bytes100..107 rather than the four-tag cycle, preventing earlier same-tag matches.
The >=23 actual lookup-distance requirement and every other check stay unchanged.
No timings, optional performance stopping or acceptance are involved.
