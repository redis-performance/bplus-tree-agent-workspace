# Guarded physical-slot lookup — adversarial preparation C

Read-only preparation; **no hypothesis selection or source adoption**. Await the new shared frozen packet and fresh corrected-adapter baseline profile/A/A before any independent proposal. No build, native executable, profile, timer, Git mutation or agent launch occurred. Only this scratch note was written. Reviewer `/root/followup_proposal_c`, prior author of 006 variant C (disclosed); GPT-6/Codex family, exact serving variant/token/currency cost unknown. Root alone publishes.

## Natural semantic boundary

A guard based on independently nullable output pointers is a legitimate API/operation property. It does not depend on tree size, seed, benchmark name or host. The generic helper at current source line1275 receives `score` and `position` independently. Position is a **logical** leaf ordinal. The tag/record search already identifies a physical ordinal; the mapping at line370 is the involution `reversed ? count - pos - 1 : pos`. Original score decoding maps the logical ordinal back to physical storage.

| score pointer | position pointer | Required behavior after a full member match |
|---|---|---|
| NULL | NULL | Return found; no output store and no score decode required |
| non-NULL | NULL | Store exact score bits; no logical ordinal is externally required |
| NULL | non-NULL | Store original logical ordinal; no score store/decode required |
| non-NULL | non-NULL | Store exact score bits and original logical ordinal |

A prospective score-only specialization can therefore have a natural boundary at non-NULL score / NULL position, or a read-only no-position boundary that separately honors NULL score. This establishes semantic viability only; it is not a recommendation of either form. Do not treat `position == NULL` as permission to dereference `score`. Do not omit the generic logical mapping when position is requested. A late guard inside the successful-match arm avoids changing miss behavior semantically, but its actual code generation and performance still need inspection.

Public `zbtreeScoreRaw` passes no position; `zbtreeScore` delegates to it. `zbtreeScores` also passes no position and a per-lane non-NULL score. Thus a pointer guard can affect both scalar and batch paths, regardless of a scalar-primary label. Insert/update/delete/rank callers requesting positions remain important fallback guards. Index searches also execute rehash steps and validate live leaf IDs/migration; preserve those semantics, the original tag scanner, external-record full-hash rejection, binary length/memcmp, home filters and first successful match. No ownership, index/layout, allocator or public API change follows from this preparation.

A representation guard (reversal, score width or bit alignment) is natural only if justified by fresh geometry/profile/codegen, frozen before comparative results and correct for its full metadata domain. Never use the observed fixture width as an implicit permission to weaken semantics or relabel 100K as the sole primary. Whether such a guard is worth testing is explicitly undecided.

## Exactness hazards

`zbtScoreLeafScore` (line499) reads physical little-endian packed deltas with endian conversion, optional ninth-byte spill, a guarded width mask and score shift, then subtracts from the base for reversed leaves or adds otherwise. Reconstruction uses ordered integer score bits and `zbtOrderedToScore`; preserve this path's bit-level result, including −0.0 versus +0.0. Numerical `==` cannot validate zero sign. No floating shortcut, cast-to-integer checksum, finite-only bound relaxation or NaN assumption can replace exact-bit tests. Width0 must not read a score field: its score area has zero bytes and offset storage follows immediately. Width64 must avoid `1ULL << 64`; widths below64 can cross the loaded word boundary and need a ninth byte. For actual width64 fields, `physical * 64` has zero bit shift (the byte address can still be unaligned). Existing eight spare bytes permit the original unaligned read; do not assume a different load pattern is safe merely because those bytes exist.

Both orientation-dependent **base arithmetic** and physical/logical position mapping matter. A correct physical decoder must bypass the redundant ordinal round trip while retaining subtraction for reversed leaves, rather than passing a physical ordinal to a decoder expecting logical input. Finite-score preservation includes wide bit patterns, subnormals, extremes and zero transitions. Endian conversions remain part of portable semantics; M6 execution alone is not big-endian validation.

## Existing semantic evidence and concrete gaps

004 physical-oracle.c is valuable unchanged regression coverage: 4,160 synthetic cells across 16 leaf counts (1..8 and19..96 step11), widths0..64, both orientations and two shift settings (0 and3 where permitted). It constructs expected score bits from the chosen physical delta independently of the decoder, uses colliding tags, checks every physical member against all four optional-output combinations, and checks logical positions. Width0 explicitly checks both signed-zero bases. Its historical native/sanitizer runs and deliberate reversed-base/logical-position faults are recorded; they are evidence for those old source/binary identities, not execution of a future candidate.

The oracle does **not** cover all legal score shifts, all bit-offset/count boundaries, full public mutation histories or all binary member lengths: records are fixed eight-byte inline values. All tags collide but keys are distinct; its printed “first-match” wording is not proof of duplicate identical-member search order. Missing-member checks pass NULL/NULL only and do not verify non-NULL output sentinels remain untouched on misses. It does not prove that an unnecessary score read was avoided when outputs are NULL. A future additive referee should cover these gaps without editing or weakening the original oracle. Link a source-included oracle with no second tree C translation unit.

006 C's supplemental readonly-oracle retains the original generic assertions and adds score-only helper checks (score non-NULL/NULL). It is useful if a future source has that actual helper, but my own authorship is not independent candidate validation. New guards require deliberate false-guard/fallback tests and exact miss-output sentinels as well as native/sanitizer public model histories. Include reverse creation by prepending, width changes under update/repack/split/merge, signed-zero transitions, ties, binary prefixes/embedded NULs, short/long/external boundary records, resize/rehash and reused leaf IDs. Existing original43 tests remain mandatory.

## Performance preservation is not implied by a branch

006 PLAN retains101 cells:40 standard operations,30 scalar hit/miss/mixed lookup cells (including8/16/319/320/321/1024-byte keys),6 batch1/16 cells and25 update-pattern cells. Reuse this inventory as a required floor; its old outcomes do not qualify new controls. Its fixtures chiefly store integer IDs as scores. Existing synthetic reverse/width correctness does **not** supply reversed/wide-finite lookup throughput guards. Before candidate code, freeze supplemental public-lookup workloads exercising reversed leaves, wide finite packed scores, signed zero/ties and mixed representations, including guard-taken/guard-false/NULL-score modes where meaningful. Freeze exact score-bit checksums, expected operations, units and owned-memory checks with these frontends; keep each old referee separate and unchanged.

Even an unchanged fallback source body can suffer caller growth, altered inlining, stack allocation, register spills, literal layout and branch/code placement. Static normalized codegen can show what changed but cannot certify equal runtime. Corrected-adapter baseline/native codegen, explicit both-output/generic-path workloads and the complete retained guards are needed. Batch hit/miss/mixed and update discovery must not be deferred as irrelevant because a scalar score-only primary passes. Fixed process-level serial ABBA with at least six preregistered blocks, deterministic order/seed rotation, all per-run raw rows and exact integer elapsed/operation arithmetic should preserve the existing every-block ±1% A/A, ≥2% primary, ≤1% guard/memory and ≥10ms minimum-window gates. Both100K and1M primaries remain. Noisy or unqualified fallback guards remain PARK; no dropping/retuning after candidate effects. Held-out seeds, matched candidate profile and independent adversarial/confirmation steps remain required for acceptance.

## Provenance and evidence needed next

Current C/H hashes are d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. Current corrected `_Noreturn` adapter H/C hashes are468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7 /c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3. In contrast004 freeze uses old adapter H/C79b3c9cfa8aec6e003dcf10e6d1c3af71799e357db7d0a0526dca0fd575af0be /adf0f87cd7cd7bc043eeb1743b47f90e4484459c090024ffa837cfd34d9b3d63. 006 also predates the separate correction. Original data remain valid for their own adapter identities; neither earlier A/A nor −4.800% exploratory100K B result transfers. 004 B failed the1M dual-primary gate; no candidate full guards/fresh/profile ran. 006 was a distinct call-boundary family that preserved the decoder; do not bundle it into a physical-score hypothesis.

Fresh evidence must identify current exact commit/source/H/adapter/referee/compiler/flags/allocator/binary hashes and source-equivalent profile instrumentation, all builds with identical paths/maps/assertions. Profile and geometry must describe which output modes, orientations, widths, shifts and spill positions are reached; PC locations are not cycle fractions, and external memchr samples do not show decoder cost. Fresh corrected-adapter A/A must qualify the actual fixed primary and guard workload, not borrow011/023 controls or old100K precision. Establish sufficient fixed sample capture without retry-shopping; insufficient profile or controls support NONE/PARK. Await that frozen common packet before actual independent proposals.

Read inspection note: an attempted read of referee `lookup-batch.c` found no such file; the actual frozen frontend is006-followup/referees/batch.c and was then inspected. No benchmark failure or source alteration occurred.

## Input hashes

- `src/zset_btree.c`: `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`
- `src/zset_btree.h`: `496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83`
- `compat/server.h`: `468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7`
- `compat/standalone.c`: `c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/physical-oracle.c`: `ac37c96fd1b583a6c74f8be083e3f68bff9a74989929cdc4fddcce8d8177f59a`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/variants/B/candidate.patch`: `b1ca29ae4594f00e0e5d5761462e9c1058d5249fde5708ad761c7329a91ec513`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/freeze.json`: `e5e75e9e9934c175b5c9838ba84af044b74396a169a7bcabcb85784c5c4a6e29`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/RESULTS.md`: `293c707e97515336e213b0c125573536179dc8de0f5599b9ee4c82f5858bb87f`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/PLAN.json`: `bc97ba17ce7565504bf46db901e498b8432795cfc80515c8219cb62882881eb2`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/referees/lookup.c`: `a325dbc6429f770c7c09188c9091ff9dcdcdfbb544996dc237923c647d0d2ea6`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/referees/batch.c`: `89bfbfd799347db3b822f9344d9cf2cb52b43fde4038c0ca8eac34c100b34f8c`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/variants/C/readonly-oracle.c`: `fd059e476c362321d342858ba42072d7e9c8632e6b39d5c4041af3d8ff9d2db6`
- `experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/REVIEW-CALLER.md`: `78c8f33011615bf47fcdb94a2898ba49f94c179f5095fc4ca659b52cc3ea686e`
