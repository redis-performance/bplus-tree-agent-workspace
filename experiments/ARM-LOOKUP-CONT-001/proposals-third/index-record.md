# Exact index-tag masks before record dispatch

Recommend one bounded experiment: replace the approximate index-byte equality mask with an exact scalar mask in member lookup, then remove the now-redundant per-candidate tag-byte recheck. Preserve candidate order, index layout, negative filter, leaf boundary and the complete record matcher. Prefer the lookup-only scope below; select `NONE` if exact codegen does not remove the dispatch chain cheaply or any required guard fails.

This proposal was completed without reading `proposals-third/dispatch.md` or `dependencies.md`. Public author role: index/record-dispatch proposer. No implementation, compilation, timing, profiling or fleet access was performed for this proposal. The author previously implemented H6-A; this hypothesis starts from the original baseline and does not incorporate H6 or another candidate.

## Evidence and distinct mechanism

Baseline source SHA-256 is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`; the controller reports the fresh upstream fetch remains `ee8e7f70152404649ac947157fd662d11b4a00d5`. In `current/src/zset_btree.c`:1855–1862, `zbtIndexTagMask` explicitly documents that subtraction can set bits above a true matching byte. `zbtIndexTableFind`:1980–1987 therefore extracts the candidate position and checks its original byte before reading its leaf ID.

The exact native baseline [assembly](../native-profile/assembly.stdout), SHA-256 `6657940b938bd3aae1d72d8fc4b1f8c7dc36de34fdac944609c86891f5905a63`, exposes the cost:

- Lines 12027–12038 (`0xc3f4`–`0xc420`) load bucket tags, form the approximate mask and branch to candidate selection.
- Lines 12067–12073 (`0xc494`–`0xc4ac`) select the least significant candidate bit, derive its byte position, shift the original tag word by that variable position, compare the byte and branch away if it was a subtraction artifact. The four instructions from `0xc4a0` through `0xc4ac` exist solely for this recheck.
- Only then do lines 12074–12080 load the ID and check deletion/range. The existing leaf call remains at line 12061 (`0xc47c`); success returns through line 12063. Nothing in the proposal removes the ID/free-leaf/migration checks or the leaf search.

This is also present in the saved target baseline [GCC15/LTO assembly](../H2-profiles/arm-gcc15-lto-base/assembly.stdout):5736–5739 (`0x406098`–`0x4060a4`) and 5825–5828 (`0x4061fc`–`0x406208`) contain the same position-to-variable-shift-to-byte-compare branch. This evidence comes from the baseline ELF in that matched-profile cohort, not H2-B's modified implementation.

The native [profile](../native-profile/README.md) assigns 21.77% of whole-process user-cycle sample weight to raw lookup and 41.38% to the leaf helper. This bounds the plausibility of working in index dispatch but does not attribute time to these four instructions or establish their critical-path cost. Setup/warmup are included. The controller's newer H2-B fixed-work cycle/instruction reductions support that candidate's separate hypothesis; they are not evidence for this one.

H1 changed the leaf boundary, H3 changed equality, H4 outlined negative-filter work, H5 separates resize state, and H6 caches record length. Here the missing-member filter remains exactly in place, and `memchr`, packed record decoding and `memcmp` are unchanged. No calls, cache fields or memory-layout changes are proposed. This does not retry H4's unchanged failed boundary: the controller reports its survivor lost the Intel miss guard by 1.32–1.38%. H3's Intel long/external losses likewise remain disqualifying, regardless of its ARM short-hit improvement.

## Falsifiable hypothesis and arithmetic contract

An exact bucket tag mask can remove candidate rechecking at lower total cost than its extra mask-generation work, delivering at least 2% primary improvement in every qualified block while keeping every original/supplemental guard and tree-owned-memory delta at or below 1%.

For a 64-bit XOR word `x = bucket_tags XOR repeated_query_tag`, use the exact-zero identity:

```text
L = 0x7f7f7f7f7f7f7f7f
H = 0x8080808080808080
exact = NOT(((x AND L) + L) OR x) AND H
```

This is scalar unsigned arithmetic over the existing eight-byte word, with no intrinsic, vector load or wider access. In each lane, `(x_byte & 127) + 127` is at most 254, so addition cannot carry into another lane. Its high bit is clear exactly when the low seven input bits are zero; OR with the original byte also rejects inputs with bit 7 set. The final high bit is therefore set exactly for an original zero byte. Every remaining mask bit is a true match, even after repeated `mask &= mask - 1`; keeping `ctz(mask) >> 3` preserves the original ascending slot order. This proof is why removing the recheck becomes valid. Removing it while retaining the existing approximate mask is invalid.

Folded tag zero still maps to one for index lookup. Queries for tag zero used to detect empty slots retain their own meaning. Tombstones remain ID sentinels with potentially nonzero tags; an exact tag match never makes a tombstone a live member. Numeric bucket lane order is built by shifts, so no host-endianness assumption is added. Any leaf-tag-word reuse must retain its existing endian conversion and bounded tail handling.

## Three implementation scopes for one hypothesis

1. **Lookup-only exact helper — preferred.** Add a plainly named exact-mask helper used only by `zbtIndexTableFind`; delete its candidate-byte check. Keep the original approximate helper and every other caller unchanged. This contains the affected behavior to member search and the APIs that inline it, with a small, reviewable pure helper. It gives misses the extra exact-mask work, which must earn its cost.
2. **Exact member and reference searches.** Use the exact helper in both `zbtIndexTableFind` and `zbtIndexTableFindReference`; remove only their respective redundant byte comparisons. Keep the cheaper approximate mask for empty-slot existence tests and leaf scan enumeration. This could also simplify reference repair but expands the churn/update/split/merge guard exposure. It must not be assumed better from a primary-only result.
3. **One exact mask contract everywhere.** Strengthen `zbtIndexTagMask` globally, update its contract and eliminate redundant checks in both index searches and the full-word portion of `zbtLeafTagMatches`. Preserve scalar tails and tag-one's union with leaf tag zero. This avoids two mask helpers but taxes existence-only callers and changes scan enumeration code. Its broader guard burden makes it the least preferred scope, and it is `NONE` if that scope is not justified before measurement.

These are implementation alternatives of one exact-mask hypothesis, not three independent proposal votes. Do not combine them with a negative-filter boundary, H2/H6 metadata, specialized equality or resize dispatch. A selected scope still needs three isolated implementations under the population process and a chair decision before coding.

## Codegen rejection gates and toolchain predictions

Inspect exact native ARM, target GCC15/LTO (including its no-score clone) and Intel ELFs before timing. Candidate selection must reach the ID load without reloading/extracting the stored byte, comparing it with the query tag or branching on that comparison. The exact mask must remain bounded scalar operations with no helper/library call. Preserve the leaf call boundary, memchr/memcmp, record-byte access widths and negative-filter computation. No volatile state, assembly barrier, forced vectorization, fixture assumption, prefetch or batching is allowed to rescue a failed gate.

Native and target ARM have the four-instruction recheck today; both can plausibly trade a small number of upfront ALU operations for removing it. This is a prediction, not an emitted-code result. Constant materialization may cost differently across compilers. Reject before timing if the recheck persists, the replacement adds at least the four dependent scalar steps it intended to remove on a home-hit path, or the raw lookup's saved frame grows relative to its exact cohort baseline. A changed instruction total alone is not a performance claim.

Intel may already schedule the byte check cheaply, while exact-mask construction adds work even when no candidate exists. Intel miss traffic is therefore a leading falsifier, especially after H4. Long/external hits still benefit only from the same index dispatch change; their hashing and record work can dilute any gain. Do not predict or require a win on guards, but enforce their existing 1% limit. Do not use ARM success to waive an Intel failure.

## Correctness and affected guards

Before any timing, require the existing 57 native/57 sanitizer tests, 36 fixture runs and 135k output/external oracle checks. Add a small direct exact-mask oracle against per-byte equality: exhaustive byte values/tags at every lane, all adjacent-byte pairs with adversarial remaining lanes, zero/one borrow chains crossing every position, high-bit bytes, all-equal and no-match words, and deterministic full-word cases. Check the complete mask and full enumeration order, not just whether some match exists. No new reads or padding assumptions are necessary.

Exercise index tag-zero folding, equal-tag collisions, successive unsuccessful leaf candidates, tombstones, missing/free/migrated IDs, narrow/wide bucket forms, displaced/wrapped probes, both resize tables and final resize completion. All optional score/position/insertion outputs retain their original behavior. Options 2/3 additionally need reference-repair and scan-result exact oracles, including leaf tags zero/one, both physical orders, partial final words, scan count/cursor behavior and duplicate suppression. No test may weaken the existing referee.

Keep hit/score/miss/inline256/external384/update, existing iterator/rank/churn guards and the new mixed-member guards where applicable. Independently freeze and qualify collision/displaced/resize traffic before adoption; they cannot be declared passed because an ordinary miss case passes. Option 3 also requires a separately frozen scan traffic guard because it changes scan-mask construction. Proposed tests are not yet executed or qualified. The primary remains the original 500-member workload; no fixture, seed, hash, allocator or timing count changes are part of this experiment.

Separate cohorts, fresh A/A, three ABBA blocks, every row at least 250 ms, primary at least 2% every block, all guards/memory at most 1%, held-out confirmation, matched profiles and independent adversarial review remain unchanged. Any unresolved qualification noise parks the cohort. Any semantics, mechanism or required guard failure rejects the variant; instruction/profile improvements cannot override it.

## Consultation and TMA limits

Fresh own enabled-tool discovery returned no callable cpu-perf/library_status endpoint. The shared controller's actual consultations are recorded in [CONSULTATION.md](../CONSULTATION.md): server 0.1.1, bundled revision `deb5a0bac467`, 3/287 indexed sources and 158 passages, without supporting retrieved passages establishing these workload gains. Controller updates about new screens/profiles are labeled as shared evidence here; no new ask is claimed. The controller will reconsult with this exact arithmetic and miss-risk question before selection. The identity above is justified algebraically, not attributed to an unavailable library passage.

For qualified ARM baseline and any proposed candidate, Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all child shares remain **unavailable**: collector scope/exclusion/formula qualification is absent and this proposal collects nothing. Existing sample shares and fixed-work counters do not substitute for pipeline slots. No branch-misprediction, execution-resource or memory-bound cause is asserted. Exact model/token/cost totals are unknown; private participant records retain backend provenance.
