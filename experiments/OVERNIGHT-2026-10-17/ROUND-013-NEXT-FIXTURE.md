# Public leaf-ID lifecycle fixture: source inspection for the next worker

Preparation only; no new experiment, test result or coverage claim. Source hash remains
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
The relevant code is in [zset_btree.c](../../src/zset_btree.c).

The main trap is that checking the fixture can change it. zbtIndexFind advances an
active rehash by one leaf at entry (line2268). ScoreRaw, Score, Rank and FindForAdd
therefore consume the very active-resize window the proposed test needs to observe.
Do not call a full lookup-based model verifier between setup and the deferred-ID
coverage assertions. Iterator traversal and the existing scan path can check exact
public results without that lookup-driven step; inspect them again before relying on
this distinction. After coverage is captured, full lookup/rank verification is useful.

Potential bounded construction recipe, still untested:

1. Insert unique finite-scored,319-byte inline members using the public insert API
   until a naturally triggered member-table resize is observed with enough uncopied
   score leaves remaining. Observe private fields read-only; do not force rehash or
   edit its cursor. Inline members create more leaves per member than external records.
2. Record a complete leaf's rank interval and ID, then delete that small interval with
   DeleteRangeByRank. Its small-deletion branch begins at line3780 and removes leaf
   runs without an explicit zbtIndexRehashStep. Keep the deletion at most1024 members
   to avoid the large-delete rebuild branch, which renumbers IDs and ends rehash.
   Other internal deletion paths may migrate leaves; assert the actual resulting state.
3. Require that the removed ID is marked free while the same resize remains active.
   Insert at a score-tree edge until a new leaf is actually allocated; capture before/
   after ID high-water marks and the released-ID set. New IDs must not reuse any
   deferred free ID. The insertion path advances rehash, so bound the insertion count
   and fail a coverage precondition if resize ends first.
4. Finish rehash using bounded public lookups. Then create another actual leaf and
   observe reuse from the free list, checking that public order, exact scores, member
   lengths, ranks, scan completeness and memory ownership remain valid.

Source reasons: RegisterLeaf lines798–827 excludes reuse while member_rehash exists;
ReleaseLeafId lines832–837 encodes ID+1 links. RehashStep lines2107–2141 resumes from
the first leaf if its saved leaf ID was retired and skips already copied leaves.
IndexInsert lines2410–2451 may copy a touched leaf and advances rehash. IndexRebuild
lines3726–3752 renumbers IDs, so it is a different transition and must not silently
satisfy this fixture's coverage counters. Existing natural wide-ID tests cover widening
and mutable scans, but do not explicitly prove this entire retire/defer/reuse sequence.

Preregister exact sizes/seeds, maximum search/insert budgets and required coverage
before execution. If the proposed recipe cannot reach the state, preserve the failure
and treat it as fixture preparation; do not weaken the coverage assertions or mutate
private state to call it public-API coverage. Native and sanitizer allocator differences
can change leaf packing, so require semantic/transition coverage per build rather than
identical physical IDs between builds. This work does not address timing precision.
