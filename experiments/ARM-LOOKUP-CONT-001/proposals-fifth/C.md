# C: one advisory slot hint per bucket, within the existing filter word

Independent source proposal, 2026-11-14. A bounded representation is possible without stealing leaf-ID bits: reserve the high byte of each existing `home_tags` word for a hint belonging only to index slot zero, and retain a conservative 56-bit home filter in the low bits. This is a concrete representation option, not evidence of a speedup or permission to implement. Its usefulness remains unestablished. If changing the filter representation is outside this population's intended scope, my choice is NONE; there is no demonstrated free seven-bit field in each existing narrow ID.

The hypothesis is that some successful queries can avoid the leaf-tag scan by validating this advisory physical position first, while the smaller filter and additional checks still meet every unchanged guard. No speed prediction is made. The recorded hot path motivates looking here; it does not quantify saved work or establish sufficient coverage in the 500-member fixture.

## Source and independence

I read the parent's late index-hint audit, then inspected the frozen `current/src/zset_btree.c`, SHA-256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, extracted from unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`. No other new proposal was read. This document is the only file written for this task. No source edit, implementation, compilation, timing, profiling, fleet access, commit or push occurred. H2 and Q4 remain parked; this proposal does not reopen the failed ARM controls.

The relevant source is `zbtIndexBucket16`/`zbtIndexBucket32` around lines 252–262, ID accessors around 1798–1823, home-filter accessors around 1833–1852, `zbtIndexTableFind` around 1960, and `zbtScoreLeafFindMember` at 1302. The full lifecycle spans `zbtIndexTableInsertRaw`, `zbtIndexCopyLeaf`, `zbtIndexRehashStep`, `zbtIndexReserveLeafId`, `zbtIndexMove`, `zbtIndexDeleteAt`, `zbtIndexInsert` and `zbtIndexRebuild`. `zbtIndexScanSlot` also consumes the home filter and must use the same representation.

## Representation budget and exact option

The existing narrow bucket is 32 bytes and the wide bucket is 48 bytes on the documented target layout. Neither gets a field, padding change, allocation, table mode or side array. Both keep the full existing ID and tag domains. The hint belongs to a fixed physical index slot, zero, avoiding a separate three-bit slot selector.

Interpret `home_tags` numerically as:

- Bits 0–55: a conservative home filter.
- Bits 56–63: zero means no hint; 1–96 means physical leaf position 0–95. Treat all other values as unavailable, never as an unchecked position.

Let `M` be the existing 64-bit result of `zbtIndexTagBits(tag)`. Define the new filter mask as `(M & ((UINT64_C(1) << 56) - 1)) | (M >> 56)`. This folds the old top eight filter bits onto low positions 0–7. Recording a home tag ORs only that folded mask. Checking a home tag compares only the same folded mask. Hint writes replace only the high byte and preserve the low 56 bits. Consequently hint initialization, invalidation and replacement cannot clear filter membership. Folding commutes with OR, so the representation remains conservative: it can admit additional false positives, but cannot reject a member whose tag was recorded. The extra collisions are an explicit risk, not free space.

The source has a second direct filter test in `zbtIndexScanSlot` around line 4254. It must use the folded `zbtIndexTagBits` result too. Index tags themselves, `zbtIndexTagMask`, zero-tag empty slots, tombstones, home-bucket selection, probing, occupancy limits and all ID accessors retain their meanings.

This requires no new steady or transient tree-owned bytes, no additional simultaneous table, no early resize, and no table conversion. Each new table starts zeroed and uses this single interpretation from allocation through release. Old and receiving tables within the candidate have the same interpretation. Promotion remains the existing descriptor assignment in `zbtIndexRehashStep`; there is no new conversion at promotion. This describes rebuilding a candidate from source, not converting already running baseline objects. No persistent format is introduced.

The memory claim is a source-level allocation claim pending layout and allocator validation on supported targets. Existing allocation sizes and lifetimes must remain identical, including dual-table resize and rebuild peaks; acceptance still uses the unchanged <=1% bound. Integer masks avoid byte-order-dependent field addressing. No assumptions about spare padding or a new interpretation of `wide_ids` are needed.

## Legal IDs and bounded maintenance

`ZBT_INDEX_WIDE_ID_AT` is 32767, but it is a widening trigger, not the narrow legal-ID ceiling. `zbtIndexReserveLeafId` permits a receiving narrow resize table to continue accepting higher IDs while migration advances, and uses `ZBT_INDEX_NARROW_ID_LIMIT` near 65535 for its safety margin. The proposed hint never touches any ID bit, so IDs above 32767, tombstone `UINT16_MAX`, the full wide domain and free-ID reuse are unaffected.

Seed hints only where a physical position is already available without another member search:

1. `zbtIndexCopyLeaf` already iterates logical position `i`. Pass `zbtScoreLeafPhysicalPos(leaf, i)` to raw insertion. If insertion lands in bucket slot zero, encode that position.
2. The corresponding existing loop in `zbtIndexRebuild` can supply the same position. This adds constant work to an existing rebuild; it must never cause an extra rebuild.
3. Ordinary `zbtIndexInsert`, reference moves and other raw insertion sites without a proven current position supply “unavailable.” Do not search a leaf just to create a hint.

Make `zbtIndexSetId` clear the high-byte hint whenever it writes index slot zero, including tombstoning or relabeling. A raw insertion with a known position sets the hint after writing the ID. Other slots leave it untouched. `zbtIndexRecordHomeTag` may update this same bucket or a different home bucket, but changes only the low filter bits. Saved insertion cursors retain the original revision/ownership checks.

Inserts, deletes, reverse physical ordering, compaction and same-ID leaf replacement can stale a hint without touching its index ID. Leave those hints stale. Do not update shifted members, add a leaf traversal, scan a table, or refresh an index during a read. Existing per-leaf migration still copies at most the existing leaf bound; hint work is constant per copied entry. Existing transition logic and any pre-existing last-resort completion paths are unchanged, and no new unbounded transition is permitted.

This conservative seeding policy may provide little or no useful coverage for the primary fixture. That is an open question, not a reason to extend the scope to extra searches or eager refreshes.

## Current-record validation and interchangeable references

At the existing successful-tag candidate in `zbtIndexTableFind`, first retain all tombstone, ID-range, live-leaf, leaf-ID and migration checks. Only then, for index slot zero with a valid encoded hint below current leaf count, read the current offset through `zbtScoreLeafOffsets` and check the current leaf tag against the original, unfolded leaf tag `hash >> 24`.

Use one shared complete record predicate for the hinted slot and the existing full scan: external-record hash check, packed length decoding, exact length and byte equality. A successful predicate retains original logical-position conversion and optional score/position outputs. A hint mismatch or out-of-range hint calls the unchanged complete leaf scan from its original beginning. Do not use the hint to establish absence, skip fallback candidates, or read a record through a cached byte offset.

`zbtIndexTableFindReference` intentionally treats matching index tag plus leaf ID as interchangeable. It must continue to ignore hints. Relabeling clears slot-zero hints, but even an in-range stale hint can name a different current record after movement or ID reuse. Complete validation makes that harmless. If it happens to match the query exactly, the existing index entry is already a valid interchangeable reference by the original invariant; otherwise fallback is mandatory. Correctness must not depend on the hint continuing to identify its insertion-time member.

## Risks, guards and falsifiers

The option trades eight home-filter bits for a sparse hint; it does not evade the representation cost. Misses, long members, overflowing probe runs and scan may do more work because the filter is weaker. A stale hint can add a failed record access before the original scan. Only slot-zero entries can benefit, and only some receive seeds. Mutation paths gain bit manipulation, while the shared predicate may alter compiler outlining and register allocation. All are reasons the unchanged <=1% guard may reject this option.

Before implementation admission, a separately authorized correctness-only diagnostic should count useful seeded hints and their survival in the original fixture and mutation guards, without changing construction. Zero usable hinted hits in the primary fixture falsifies the proposed opportunity under this seeding policy: choose NONE rather than quietly broaden it. A useful-hit census is still not performance evidence.

Required correctness coverage includes all narrow IDs around 32767 and the upper narrow range while a narrow receiver is active; widening; all relevant table promotion and free-ID reuse cases; colliding tags and interchangeable references; slot-zero deletion/reuse; both physical encodings; split/merge/compaction; stale valid and out-of-range hints; binary and external records; scan during resize; and optional-output combinations. Exhaustively check all tag values against filter record/check operations and hint replacement to prove no false negative. Verify allocation and peak lifetime parity on 32-bit and 64-bit layouts without assuming padding.

Any false negative, wrong output or reference, new whole-table transition, extra allocation, or threshold breach rejects the candidate. Future performance admission needs a new protocol and live reserved fleet capacity, exact emitted-code review, qualified A/A, unchanged guards and memory bounds, paired comparisons, matched profiles and independent confirmation. No existing failed ARM control may be retried or reinterpreted on this proposal's behalf. No performance acceptance follows from this document.

## Consultation, provenance and TMA

Review cost metadata is unavailable. My exposed-tool discovery for `cpu-perf` and `library_status` returned no tools before the pause and again after resumption. The parent's fresh actual stdio discovery, `library_status` and `ask` in the late index-hint audit are shared evidence, not calls made by this worker. They report bundled revision `deb5a0bac467`, 3/287 sources and 158 passages, with no supporting passages. The specific 56-bit-filter/single-hint representation here was derived from source after that consultation and has not itself been consulted. No literature-backed performance claim is made.

| TMA category, share of total pipeline slots | Baseline for this mechanism | Proposed candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Qualified roots and children were not collected for this mechanism. There is no candidate binary, collection scope or run ID. Historical hotspot samples cannot supply these shares or predict a gain.
