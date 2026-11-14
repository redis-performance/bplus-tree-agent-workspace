# Independent advisory physical-slot hint assessment

**Selection: NONE for this campaign.** An advisory slot can be made semantically safe, but I have not derived a useful bounded representation that preserves the original leaf-ID domain, index layout and missing-member filter while satisfying the existing memory, guard and transition constraints. This is a decision not to admit implementation, not a proof that every possible sparse hint scheme is impossible. H2 and Q4 remain PARK, and the released ARM runner remains released.

I read the controller's late index-hint audit and independently followed the frozen source. The exact upstream pin is `ee8e7f70152404649ac947157fd662d11b4a00d5`; independently checked `current/src/zset_btree.c` SHA256 is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. All line references below are to that file. No other new proposal was read. No implementation, build, test, measurement, profile, fleet access, commit or push was performed.

## Mechanism and its safety contract

The current index resolves a leaf ID at lines 1987–2007, then calls `zbtScoreLeafFindMember`. The leaf finder at lines 1302–1341 searches hash tags with `memchr`, resolves a physical record offset, checks external full hash, decodes length/data and compares bytes. An advisory physical slot could try that current record before the scan. A successful validated hint could omit the initial tag search. Neither useful hint frequency nor saved work has been measured here, so there is no speed prediction.

The following ordering is necessary even with a correct representation:

1. Preserve original index tag matching, tombstone exclusion, ID bounds, live/free-pointer checks, ID assertion and resize migration ownership before accessing a hint's leaf. A hint cannot rescue an entry the original index rejects.
2. Check `physical < leaf->n.count` before loading any slot-dependent offset or tag. Compute the current offsets and tags through the original accessors at lines 356–379. Never retain an old record address or byte offset across mutation.
3. Preserve the raw leaf tag check, `tags[physical] == (uint8_t)(hash >> 24)`. The original `memchr` establishes this before the record predicate. The index folds hash tag zero into one, so index-tag agreement alone is not this condition. Even if normal callers supply the correct prehash, removing this condition would not preserve the complete original search behavior.
4. Invoke one shared full current-record predicate: external full-hash rejection, original packed-data/length decoding, exact binary-length comparison and bounded byte equality. Only a successful predicate may write optional outputs. Map the accepted physical position back through the original reversed-leaf mapping before score decoding or returning logical position, preserving signed zero and all output combinations.
5. On an invalid, stale or nonmatching hint, run the original full scan from its original start. The hint cannot prove absence, suppress another candidate, change the insertion hint, or skip a leaf. Do not refresh the index on a read. A stale attempt may add a duplicate record comparison on fallback; that is a performance risk, not grounds to weaken the scan.

Factoring the record predicate is plausible but not automatically free. Passing an extra slot/output state or altering inlining can enlarge generic, miss and external paths. A new helper boundary needs exact emitted-code review, independently of correctness.

## Independent representation audit

| Proposed storage | Source evidence | Assessment |
|---|---|---|
| Reserve bit 15 of a narrow leaf ID | Narrow ID accessors at lines 1798–1822 preserve IDs below `UINT16_MAX`; widening starts at 32767 but an already active narrow destination continues receiving IDs. `zbtIndexReserveLeafId`, lines 2197–2220, uses the later limit 65519 to force completion. | Unsafe aliasing. An ID above 32767 is not a hint marker. This is a live lifecycle case, not just a theoretical integer range. |
| Pack a small leaf-ID domain plus seven slot bits | A leaf holds up to 96 elements, line 144. The set-wide next-ID counter and free list are independent of current member count, lines 824–864. | Requires an escape or mode transition before the smaller domain fills. Current count or early leaf numbering cannot authorize permanent reinterpretation. No safe bounded transition is supplied. |
| Treat high IDs as impossible while a narrow resize receives inserts | Existing tests at lines 5735 onward deliberately start a narrow resize and move the next ID to 40000 or near `UINT16_MAX`, then exercise score changes. | Contradicted by source and regression coverage. Changing those tests or lowering the accepted ID range is not an option. |
| Widen every ID or append a full per-entry byte | Bucket definitions at lines 252–267 contain eight tag bytes, eight summary bytes and eight 16-bit or 32-bit IDs. Narrow/wide sizes are 32/48 bytes as documented at lines 248–251. | Widening increases index bucket bytes by 50%, not necessarily total tree bytes by 50%. A byte per entry needs eight additional bytes per bucket before alignment. Neither provides a justified total-memory bound of 1%. |
| Reuse descriptor or bucket padding | Bucket fields already occupy their stated 32/48 bytes. `zbtIndexTable`, lines 269–275, has only table-level metadata; possible ABI padding is not per-entry storage. | No demonstrated portable slot capacity. Padding claims would need actual 32-bit and 64-bit layout evidence; no such new builds were run here. |
| Add a small-domain mode and later convert | Resize setup at lines 2096–2134 and receiving-table protection at lines 2197–2220 already manage a current table and one destination. | A whole-table conversion adds work proportional to table size at a new transition. A third incremental representation needs memory, progress and ownership rules not present in this proposal. Neither is admitted. |

The safety margin near the narrow limit is not a seven-bit hint field. Even if a future proof identifies a few unreachable encodings in one specific narrow state, it does not provide arbitrary physical positions for useful entries across all receiving tables and wide-ID states. No scheme may infer available bits from the 500-member fixture or from its current number of leaves.

There are bounded *tradeoff* ideas, but none is an established solution under the current gates. For example, taking seven bits from `home_tags` could store one physical hint for a fixed bucket slot while retaining a reduced summary in the other bits. Correctly masking the writer and reader could avoid false negatives, but would weaken the absent-member filter and help only part of the entries. It is not preservation of the existing filter: its additional miss/displacement cost is unknown, and no evidence supports the 1% guard bound. A fuller hint plus bucket-slot selector would consume more summary bits. This should not be called a free encoding or silently incorporated as an implementation detail.

A sparse sidecar might cap requested bytes, but allocation rounding, extra metadata, small trees, both resize tables and duplication still need an actual bound on owned and transient bytes. Existing allocator slack is not a portable capacity guarantee. A fixed deterministic guessed slot uses no storage, but would be a different heuristic without measured usefulness, not an index entry carrying its inserted member's position. None of these alternatives is selected here.

## Lifecycle and hint usefulness

`zbtScoreRegisterLeaf` at lines 824–850 refuses free-ID reuse during active resize because old entries remain. On completion, lines 2178–2185 move the destination descriptor into the current table and free the old one. Preserve that rule exactly. A hint must remain subordinate to the current ID/migration checks, including after reuse, not become a second identity that validates an otherwise stale entry.

`zbtIndexTableFindReference` deliberately permits interchangeability of entries with the same folded tag and leaf ID, lines 2050–2087. `zbtIndexMove` at lines 2387–2442 relabels or deletes whichever such entry is found, with different handling for incomplete destinations and copied leaves. The same-tag exchange regression beginning around line 5246 demonstrates that entry-to-member association can change without changing the basic table invariants. A stored slot cannot become authoritative identity, and reference search must not require that slot to match a requested member. Full current-record validation plus fallback is essential even when insertion once supplied an exact slot.

There are bounded places to produce an exact hint without another search: `zbtIndexCopyLeaf` at lines 2145–2155 and `zbtIndexRebuild` at lines 3822–3838 already enumerate members of a completed leaf. Their logical indices would need the original physical mapping. Bulk construction also knows member positions, but changing batching is outside this proposal. Ordinary `zbtreeInsertNewRaw` at lines 3375–3384 receives the inserted leaf, not the member's physical slot; the current `zbtIndexInsert` interface at line 2462 accepts only hash, ID and optional index position. Supplying a hint there requires either propagating position through insertion/split paths or an additional search. That cost cannot be assumed absent.

In-place insertion, score changes, reversal, split, merge and compaction can leave hints stale. Correct advisory semantics avoid updating every shifted record, but do not ensure the hint remains useful. Deletion and reuse of a bucket slot need a defined disabled or newly written hint; stale contents can at most trigger the validated attempt. Duplication at lines 2945–2983 copies index tables and rebuilds leaf addresses; hints must use indices, never addresses, and any sidecar would need explicit copying/accounting. Rebuild and renumbering cannot reuse a hint as a leaf ID. No additional table sweep or unbounded transition is authorized merely to restore hint accuracy.

The existing repeated-negative-leaf census says nothing about valid positive-slot hints. It supplies neither a hint hit-rate estimate nor a construction/update/churn coverage claim.

## Distinction and falsifiers

This mechanism seeks a validated positive record location before leaf-tag scanning. H6 stores length metadata in record-offset descriptors and still resolves candidates through the leaf search. H7 changes exactness of the index tag mask. The negative-leaf cache would reuse a failed leaf result; this advisory hint can never reuse failure as proof of absence. No H6, H7, H2 or other patch is stacked, and their existing decisions remain unchanged.

To overturn NONE, a future independent proposal must provide all of the following before implementation admission:

- A complete encoding/decoding and lifecycle argument for every original valid ID, both ID widths, all receiving resize states, tombstones, free reuse, duplication and reference interchangeability. It must identify actual storage rather than an assumed spare bit.
- A bounded initialization/transition policy with no new whole-table conversion, no extra unbounded mutation work and a defensible owned/transient memory budget. A different memory or latency tradeoff requires its own explicit objective, not a waiver of this campaign's bounds.
- A useful source of hints without a hidden extra member search or mass refresh. Any separately admitted census must distinguish disabled, out-of-range, wrong-tag, failed-predicate and successful hints, including the original construction and update/churn traffic. It must not run now on the released fleet or locally as a performance measurement.
- One shared complete predicate with adversarial stale in-range slots, raw tag zero/one, binary strings, short and external records, all optional outputs, reversed leaves, signed zero, same-tag exchanges and active/final resize coverage. A hinted equality failure must demonstrably retain the full original search.
- Exact compiler/ELF review showing the intended fast path without unbounded reads or generic-path expansion being hidden. Later qualification must retain the existing primary threshold, every original and affected guard at no more than 1% regression, and the 1% memory bound. Regressions or unresolved controls are decisive; no speed prediction is offered here.

Until then, a physically safe advisory lookup alone is insufficient to admit this optimization.

## TMA and consultation provenance

For this proposed mechanism, baseline and candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all children are unavailable. No qualified matched capture exists. Earlier hotspot observations cannot establish saved cycles, resource categories or a gain.

Own enabled-tool discovery found no exposed cpu-perf/library_status endpoint. I consumed the parent's actual late-index-hint consultation as shared evidence, not my own calls: bundled revision `deb5a0bac467`, 3 of 287 indexed sources, 158 passages, and no supporting retrieved passages. No redundant call was made and no literature-backed gain is claimed. Detailed private audit/consultation paths are intentionally omitted from this public proposal. Review cost metadata is unavailable. Only this sanitized proposal was written.
