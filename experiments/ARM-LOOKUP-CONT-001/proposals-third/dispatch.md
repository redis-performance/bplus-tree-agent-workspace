# Population 3: exact index candidate masks shorten candidate dispatch

**Propose one scoped scalar hypothesis:** produce an exact eight-byte equality mask only in `zbtIndexTableFind`, then remove its repeated stored-tag validation before the leaf-ID load. Retain the existing approximate mask for other users. This is a small dependency/control-flow experiment on the original baseline, not a combination with H1–H6. It is eligible for chair consideration, not implementation or acceptance approval.

Baseline upstream remains `ee8e7f70152404649ac947157fd662d11b4a00d5`; independently checked source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. No source/referee change, implementation, build, measurement, fleet access or commit was performed. No other population3 proposal was read.

## Why this is a concrete remaining dependency

In original `current/src/zset_btree.c:1858`, `zbtIndexTagMask` deliberately permits false positive high bits caused by subtraction borrow. Consequently `zbtIndexTableFind` at lines1980–1987 extracts each candidate position, shifts the original tag word and compares its stored byte again before fetching the ID. That check is necessary for the existing mask and must never simply be deleted.

The exact saved ARM native assembly confirms that this is executable work, rather than a source-only redundancy. In `native-profile/assembly.stdout`, the stable narrow-ID candidate path at `0xc494`–`0xc4c8` is:

| Address | Work |
|---|---|
| `c494`, `c498`, `c49c` | Reverse bits/count leading zeros, then divide bit position by eight |
| `c4a0`, `c4a4`, `c4a8`, `c4ac` | Multiply position by eight, variable-shift original tags, compare byte, branch on mismatch |
| `c4b0`, `c4b4` | Form ID index and load the narrow leaf ID |
| `c4b8` onward | Tombstone, ID bounds and leaf validity checks, which remain required |

The proposed exact mask removes the middle four-instruction validation sequence from this path. It adds arithmetic to mask generation. Therefore the hypothesis is a shorter candidate-to-ID dependency with a different per-bucket cost; it is not a claim that all four instructions become net savings or that branch mispredictions caused the current time.

The enclosing `zbtreeScoreRaw` contributes21.77% of the saved native whole-process cycle samples, versus41.38% in the leaf helper and7.65% in SipHash (`native-profile/report.stdout`). The Intel LTO baseline report assigns19.67% to its raw membership clone. These locate meaningful work in the enclosing functions; they do not assign sample cost to this four-instruction subsequence. Source-independent evidence is the exact dependency chain, not an unmeasured hotspot at a particular instruction.

Native assembly SHA256: `6657940b938bd3aae1d72d8fc4b1f8c7dc36de34fdac944609c86891f5905a63`; native report SHA256: `d6a6bc4a1be1e3198b4e96f6eb67b17a3eca81e5c6c597085e8014704e0c223b`. The recorded original native ELF is `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf`. This proposal did not rehash or execute that ELF. Native offsets are not attributed to target-LTO or Intel binaries.

## Proposed scalar transformation and proof obligation

Introduce a small named inline helper, for example `zbtIndexExactTagMask(tags, tag)`, retaining the original XOR broadcast:

```c
uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
uint64_t low = UINT64_C(0x7f7f7f7f7f7f7f7f);
return ~(((x & low) + low) | x | low);
```

This is a proposed unsigned-integer expression, not implemented code. For each byte, the low-seven-bit value plus127 is at most254, so addition cannot carry into the next byte. A zero byte leaves its high bit clear before inversion. A nonzero byte with high bit clear makes the addition's high bit set; a byte with high bit set is eliminated by OR with `x`. OR with `low` makes every non-high result bit zero after inversion. Thus each result high bit corresponds exactly to a zero byte of `x`, including adjacent0/1 borrow adversaries. Numeric byte positions stay consistent with existing `zbtIndexSetTag` and `zbtIndexFirstTag`; no new byte-buffer cast or endian-dependent memory load is introduced.

Use this helper for the candidate mask in `zbtIndexTableFind`, and remove only that function's stored-byte rejection branch. Preserve original tag folding, match order, `matches &= matches-1`, zero-input avoidance for ctz, leaf validity assertions, tombstones, both ID widths, resize migration ownership, negative home filter, insertion hints, leaf matcher and outputs. `zbtIndexTableFindReference` and other approximate-mask users retain their existing checks and cheap boolean tests. There is no cache/layout/record descriptor change or new persistent state.

One maintained scanner body is enough. A local exact helper with this narrow consumer is my preferred implementation shape. An algebraically equivalent explicit-high-bit result can be an independently authored encoding choice, but should not be advertised as a distinct mechanism. Broadly replacing every approximate-mask user increases miss/reference cost without evidence; I do not recommend it. Do not manufacture three structurally different algorithms merely to fill implementation slots.

## Distinction from the completed and active work

- H1 changed leaf call/inlining boundaries and increased the raw frame176→272bytes; all variants failed guards or the primary. This proposal preserves the leaf call. H1's diagnostic instruction increases on score/miss caution against judging the new expression by symbol removal or branch count alone.
- H2 caches score-array displacement or moves metadata. B remains eligible on all11guards; C's20–25% iterator failures remain decisive. This proposal changes neither tree layout nor score/member addresses, and does not include B's patch.
- H3 adds short record equality. All variants are now rejected, including qualified Intel long/external regressions and B's target external loss. This proposal changes neither byte equality nor length dispatch and must still retain those guards.
- H4 defers home-summary mask construction after home candidate failure. This proposal leaves that formula and placement unchanged and changes the *bucket candidate mask*, not the separate negative filter. H4's miss regressions illustrate the principal risk of paying more arithmetic on misses.
- H5 separates resize/stable paths. A alone survives native; B retained forbidden state checks and C missed the primary. This proposal changes neither state dispatch nor rehash progress and does not repeat their outline boundaries.
- H6 stores inline length hints in record-offset bits. Its static/correctness success and pending timing imply no result here. This proposal leaves record offsets and all consumers unchanged.
- Historical EXP-006 replaces bounded leaf `memchr` scanning with scalar first-match scanning; inspected B uses the approximate subtraction mask and relies on the first match. The current proposal operates on the compact index's fixed eight-slot word and its all-candidate validation, not the leaf byte span. Historical ARM mask follow-up concerns score decoding/iterator behavior and remains rejected. No historical SIMD, mask/decoder, leaf-scanner or candidate patch is imported.

I considered routing raw lookup through the existing prehashed public entry to separate hashing from the large scan frame. Current assembly already needs to preserve query arguments across hashing, and an extra boundary would add another preservation/dispatch cost. Unlike the exact-mask chain above, I have no demonstrated redundant work sufficient to support that alternative now: **NONE for that hash-boundary option**. H5-B's failed specialization is additional reason not to infer a gain from a small wrapper.

## Falsification, static gates and risks

Before timing, compare exact native and GCC15/LTO ARM ELFs, including actual no-score clones/call sites, and Intel counterparts. Require elimination of stored-tag shift/compare/branch from the changed scanner, correct exact-mask arithmetic, unchanged leaf call, and no new generic fallback scanner or helper call on a candidate. Count the complete emitted mask-plus-first-candidate sequence, not only removed instructions. If the compiler restores equivalent validation or the sequence has no credible dependency/work reduction, record mechanism NONE. Inspect raw/leaf frame sizes and spills; frame growth above baseline is a warning requiring a concrete justification rather than assumed benefit. No inline assembly, volatile barriers, forced compiler switches or unregistered patch rescue.

Expected direction: hit and scored-hit may improve because their first genuine index candidate loses validation work; long/external hits share that dispatch but gains may be diluted by hashing/comparison. Misses without candidates pay extra mask arithmetic and may regress. Same-tag and borrow-heavy buckets can avoid false candidate work, but dense real collisions still pay the exact mask and full original leaf tests. Update, rank, delete/churn and resize paths use the shared table finder and must be measured. No direct memory-size change is expected. Iterator-only performance may still shift through code generation/layout, as history shows.

The primary falsifier is failure to achieve the registered≥2% in every primary block while keeping every required elapsed/memory guard≤1%; a miss regression rejects even a large hit win. No expected percentage or microarchitectural category reduction is asserted. Qualified matched profiles/counters must test whether the removed dispatch work survives compiler/linker effects and reduces whole-workload demand; unqualified or contrary evidence leaves mechanism unproven. Unchanged retries and stacking with H2/H4/H5/H6 remain excluded.

## Required correctness and guard coverage

Retain all original native/sanitizer, fixture, optional-output and external-record oracles. Add an independent exact-mask oracle comparing all eight output bits against scalar byte equality for every tag and every single-byte value in every position; exhaust adjacent-byte combinations and adversaries such as0/1 sequences after XOR, high-bit bytes, all-zero/all-equal words, no matches and multiple matches. Include tag0 for the helper's mathematical contract while testing actual hash top-byte0→tag1 folding separately. Prove each word load remains the existing in-bounds index field. No timing claim follows from correctness.

Exercise hit/miss, every optional-output combination, narrow/wide IDs, stale/free IDs allowed during resize, new/old migration ownership, final resize step, tombstones, wraparound/full probe paths and saved insertion hints. Require retained six lookup/update cases plus five independently directional iterator/rank/churn guards. Before adoption, freeze additional qualified collision/displacement/resize cases; compare both ordinary no-candidate misses and constructed multiple-candidate/borrow patterns. Fresh seeds29/43, separate compiler/host controls and Intel portability remain mandatory. Bounded big-endian correctness execution is useful if available; absence must remain a coverage gap, not an inferred pass.

## TMA and consultation limits

ARM baseline and this unimplemented candidate: Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and child shares are unavailable as qualified categories. Intel baseline classifications have their own audited workload scope in `reviews/INTEL-TMA-BASELINE.md`; they are not this candidate's categories or an ARM cause. Function sample percentages and the dependency diagram do not supply pipeline-slot shares.

Own tool-name discovery again found no exposed cpu-perf/library_status endpoint. The controller's actual screen consultations are shared evidence, recorded in `CONSULTATION.md` and selection reports: server0.1.1, bundled `deb5a0bac467`, limited3/287 sources and158 passages, with no retrieved primary passage establishing the screened mechanisms' gain. I made none of those calls and have not received a specific library endorsement of this exact-mask proposal. Root will reconsult actual MCP before selection. This proposal rests on inspected source/assembly and an explicit unsigned-byte proof, not an external authority claim. Actual backend/model/token/currency costs remain unknown.
