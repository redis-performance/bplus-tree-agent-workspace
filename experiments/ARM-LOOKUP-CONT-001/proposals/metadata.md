# Proposal: remove score-width decoding from membership metadata addressing

Proposer: independent Codex worker `cont_metadata`; exact model, tokens and monetary cost unavailable. Date: 2026-11-13. Primary lens: member-index ID → leaf metadata → record. This proposal was written without reading the other continuation proposals. No source edits, builds, fleet access or measurements were performed by this worker.

## Evidence and limits

The source under review is current `src/zset_btree.c`, derived from upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. The sealed evidence is [ARM-LOOKUP-GAP-001 baseline](../../ARM-LOOKUP-GAP-001/BASELINE.md), source/referee `4876d21ce62fdf9306572b690c891d2d5ed0e04d`, particularly [the exact ARM assembly](../../ARM-LOOKUP-GAP-001/baseline/lookup-assembly.txt). These are historical qualified measurements, not a newly qualified continuation control.

The baseline was Neoverse V2, 96 cores, a single thread pinned to CPU2 without SMT, nominal 2.8 GHz; effective frequency was unavailable. It used GCC13.3, Ubuntu libc2.39, C11/O3 without LTO. Its 500-member successful no-score case measured 29.867 ns/lookup and 14,272 tree-owned bytes; all 48 A/A rows and 12 ABBA blocks passed the ±1% qualification. Process-wide user-cycle samples localized 41.91% to the leaf helper, 21.91% to raw lookup, 6.75% to SipHash and 3.45% to named memcmp. Those samples include construction/warmup, and unresolved libc addresses must not be assigned to a function here. They do not assign a measured fraction of cycles to metadata arithmetic.

`zbtIndexTableFind` resolves a bucket match into a leaf ID and then `score_leaf_by_id[id]`. The leaf helper then needs the leaf's count and score width to locate lookup metadata:

```
score_bytes = bits ? (((count * bits + 7) / 8 + 9) & ~1) : 0
offsets     = leaf->data + score_bytes
tags        = offsets + count
record      = leaf + offsets[matching_tag_position]
```

The two source calls deriving offsets and tags **do not produce duplicate arithmetic in the captured GCC13 code**. It already shares the result. At helper PCs `34f4`/`34f8`, it loads score width and count; `3508` branches on zero width, and `3510`–`351c` perform `umaddl`, shift, add and mask. `3524`–`3528` derive tags from that displacement. After memchr, `3590` loads the selected offset using the same displacement, and `3594`/`3598` address/read the record. A source-only hoist or “calculate offsets once” therefore has no demonstrated opportunity in this binary.

The remaining concrete opportunity is the score-width-dependent address chain before tag search. Whether it lies on the effective critical path, and whether removing it saves at least 2%, remain unproven. This is a code-generation/dependency hypothesis, not a DRAM or execution-port diagnosis. It does not depend on changing logical-position arithmetic, helper inlining, tag scanning or record comparison.

## One falsifiable hypothesis

For successful membership of short members, making the offset/tag location independent of decoding `count * score_bits` at lookup time will shorten useful work after resolving the leaf pointer sufficiently to pass the unchanged ≥2% primary gate, without a demonstrated >1% regression in any registered guard or memory case.

The hypothesis changes only how lookup metadata is located. Member-index probing, hash matching, exact byte comparison, score precision, record format and index semantics remain the control behavior. It has three genuinely different implementation options, to be evaluated independently rather than combined.

## Implementation options

### A — explicit cached score-byte displacement

Add a `uint16_t score_bytes` field to the leaf and make `zbtScoreLeafOffsets` consume it. Preserve the current array order. The maximum current displacement is 776 bytes for 96 scores of width64, so uint16 is ample; zero-width encoding stores zero. Set it from the existing formula on construction and every count/width change. This is the simplest correctness prototype of the actual dependency hypothesis: one load should replace the width-dependent arithmetic and branch.

The existing header is 56 bytes with its padding already occupied. **Do not describe a new field as free.** Appending it changes the flexible-array offset and can change allocation classes, capacity, leaf splits and whole-tree memory. Preregister the unchanged 1% memory guard before any timing; enumerate all registered fixture footprints first. A failed footprint gate makes this implementation ineligible even if it is fast. No retrospective trade-off waiver. This option adds no per-member index hint and no extra allocation.

### B — cached displacement in a repacked, same-size header

Keep the node header24 and leaf header56 by replacing the separate `isleaf`, `score_shift` and `has_external` bytes with explicit masks in one byte: six bits of shift and one bit for each Boolean. Preserve the full eight-bit `moved_out` counter; it saturates at255 and is not a Boolean. Preserve all16 bits of `index_resize`. The resulting tail can hold `parent_index`, `count`, packed flags/shift, `moved_out`, `uint16_t index_resize`, `uint16_t score_bytes` within the original eight bytes. Keep the leaf's `score_bits`, `reversed` and `record_start` fields unchanged.

`zbtScoreEncoding` produces shift0 for equal scores; otherwise ctz of a nonzero uint64 produces0..63. Use explicit masks/accessors, not implementation-defined C bitfields. Initialize inner-node flags explicitly and audit every former direct field access. Compile-time size/offset assertions must establish the original headers on supported targets. This preserves the data layout and allocation requests while moving work into setters and potentially adding masking to score decode/node-type checks. It is more invasive than A, but avoids A's known memory risk and preserves fast append/prepend array placement. Recommend this as the most plausible eligible implementation if header-access code remains reviewable; do not infer that it is faster before assembly and fleet validation.

### C — place offsets and tags before packed scores

Rotate the arrays to `header | u16 offsets | tags | packed scores | free | records`. Offsets then have the fixed base `leaf->data`; tags require only `2 * count`; scores have base `leaf->data + 3 * count`. Keep the existing score-byte reservation, including its spare bytes, so total requested bytes and record capacity are unchanged. The offset array remains aligned. Score reads/writes must continue using memcpy/byte operations because the new score base can be odd.

This removes the dependency without cached state or header repacking. It requires one score-data accessor and an audit of every direct `leaf->data` score access, bulk builder, reversal, score update and in-place insert/delete. The important counterargument is mutation cost: changing count shifts the score base, potentially moving the packed-score stream even for a prepend that previously avoided it. Correct overlap ordering is mandatory. Treat this as a broad but testable alternative with a substantial risk of failing the mutation guard, not as a free layout change.

## Invariants and mutation obligations

For A/B, the maintained invariant is `cached_score_bytes == zbtScoreLeafScoreBytes(count, score_bits)` whenever a leaf is externally observable or an array accessor is used. Establish one clear old-state/new-state transition in fast insertion/deletion: do not update the cache early while old arrays are still being read, or late while new array accessors are already being used. Add correctness assertions at validation boundaries rather than timing-loop counters.

Audit construction/build and bulk build; re-encoding insertion; fast insertion; deletion/record compaction; split/merge; reversed left-edge leaves and pop; score changes; duplication and defrag/relocation. Copy paths must preserve or recompute the cache. Zero-bit scores, maximum width64, count1/96, width changes, reversed physical positions and external ownership are mandatory correctness cases. B additionally audits inner-node type checks and every shift/flag setter. C audits score spare-byte bounds and all overlapping moves.

The existing optional-output and external-member oracles remain controls, supplemented by targeted mutation checks against the reference. Binary members, embedded NULs, tag collisions, signed zero, infinity and short/16-bit-length/external transitions cannot be inferred correct from the 500-member primary. In particular, the 256-byte timing guard is inline; actual external storage begins at320 bytes. Preserve a ≥320-byte correctness case such as the existing384-byte oracle.

A direct member-position hint is deliberately not an implementation here: it changes index storage and adds position maintenance across splits, deletes, rehash, reversal and defrag. This proposal has no evidence that those costs satisfy the memory/mutation gates. Do not add such a hint to rescue a losing cache/layout variant.

## Predictions and falsification

| Case or observation | Preregistered prediction / failure criterion |
|---|---|
| Successful short, no score | Largest likely benefit; ≥2% remains required, not promised. Less improvement rejects this as an accepted optimization. |
| Successful short with score | A/B may help metadata address formation, but B adds shift extraction; C relocates score addressing. Demonstrated >1% loss rejects the variant. |
| Missing member | Many misses avoid the leaf entirely, so little effect is expected. Collision-heavy misses may improve; >1% loss still rejects. |
| Successful 256-byte inline | Expected smaller relative benefit because SipHash dominates the historical profile. No >1% loss. Do not call this an external-member timing test. |
| Count-changing mutation, including prepend/pop | A/B add cache maintenance; B changes shared-header access. C can add a score-stream move. Preregister append/prepend, arbitrary insert/delete and score-update guard fixtures before runs; any demonstrated >1% loss rejects. |
| Tree-owned bytes | A risks size-class/capacity changes. B/C predict identical requests/footprints. Any >1% increase rejects; unexpected difference in B/C requires explanation before timing. |
| Equal-score / zero-width leaves | The original arithmetic already branches around the multiply, so less opportunity. A/B can lose from a cache load; retain this as a diagnostic/correctness case. |
| Mechanism assembly | A/B must replace the width/multiply/rounding chain with the cache load. C must give offsets a fixed base. If the chain remains, the implementation does not test the hypothesis. |
| Matched profile/counters | A passing timing result still needs a plausible changed lookup path. Flat helper localization alone does not prove dependency latency; unexplained gains stay PARKED. |

Before measuring, freeze mutation and memory cells in the continuation referee, freshly qualify A/A and run variants serially on the reserved fleet with the same seeds/build controls and at least three ABBA blocks. Do not reuse old A/A as a current lease's qualification. Keep the baseline and the previously rejected logical-position changes separate. Inspect code size/spills as well as the target address chain. A GCC13/noLTO result requires its own GCC15/LTO comparison before server-transfer claims; do not mix those compilers within an A/B comparison. Any candidate needs fresh independent confirmation, Intel guards and review under the parent experiment's gates.

## TMA and consultation provenance

| Category | Qualified sealed baseline | This proposed candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The old CPU-wide `perf stat --topdown -a -C2` slot output lacks continuous exclusion evidence and validated ARM formulas; no category is promoted from it. No child category or hardware resource cause is asserted here.

Own availability discovery, repeated at2026-11-13 23:06:41 UTC: filtering the exposed tool catalog for `cpu.perf` or `library_status` returned an empty list. This worker consumed the controller's fresh shared stdio consultation (`initialize`/discovery, `library_status`, `ask`), not calls made by this worker. Raw responses remain in the ignored private build area. The shared server is cpu-perf0.1.1 with bundled list `deb5a0bac467` (2026-10-05), coverage3/287 sources,158 passages,0 vectors, keyword-only. Its question covered the three distinct continuation tracks, GCC13/noLTO versus GCC15/LTO, metadata computation and mutation/score/long guards. No source passage supported this particular mechanism; unread GCC/LTO and array-layout entries are leads only, not citations or performance evidence. The plan follows the exact source/assembly and controlled experimental method, not an MCP-implied speedup. Reconsult on the selected concrete implementation before measurement, especially if packing flags or relocating scores is selected.

Disposition: **propose for the continuation population**, with B the strongest memory-preserving cache option, A a simple gated mechanism prototype and C an independently falsifiable layout alternative. A small existing arithmetic rejection does not settle this distinct dependency hypothesis; neither does the present evidence establish a win.
