# Next index-probe hypothesis: defer the absent-member filter

Recommendation: one new, bounded control-flow experiment. Keep the existing three-bit filter formula and index representation, but keep its query-mask construction out of lookups that succeed in the home bucket. Use an explicit slow-path boundary where necessary to prevent the compiler from moving that work ahead of the successful lookup. This is a proposal, not an accepted change or a claim that the filter dominates lookup time.

## Evidence and distinct scope

Exact baseline: upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`, continuation source SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. The [native profile](../native-profile/README.md) identifies raw lookup as21.77% of whole-process user-cycle sample weight. The [exact assembly](../native-profile/assembly.stdout), SHA256 `6cfa41d17795ee7026a8f3cbcdd923576ddfba49673601139692e9d6c8960238`, provides the specific code-generation evidence:

- `zbtreeScoreRaw` begins at`c1c0` with a176-byte frame. The initial null-rehash branch reaches the current-table path at`c394`.
- For a nonzero high hash byte, branch`c3b4` reaches`c580`. Before even loading the home-bucket tags, `c580`–`c5cc` materializes the filter constant, multiplies the tag at`c5a8`, derives its two mixed-bit indices, shifts/ORs the three bits, and stores that mask at`[sp,#160]`. The separate repeated-byte tag mask at`c59c` remains necessary for candidate matching and is not the proposed removal.
- Control then reaches the bucket scan at`c3e0`/`c3f4`. A verified member match returns via`c484`→`c968`. Only the exhausted-candidate path loads the prepared filter mask at`c4e4` and tests it at`c4ec`.
- The rehash-destination path similarly builds the absent-member mask at`c238`–`c284` before scanning its candidates. The source comment in `zbtIndexTableFind` already says home-bucket hits need no missing-member filter, and the source call is after candidate matching. Moving the same expression text lower is therefore insufficient: it is already lower in source, but hoisted in this ELF.

Thus some successfully completed home-bucket lookups execute work whose result is never consumed. We have not measured the fraction of successful lookups resolved in their home bucket, or assigned individual sample PCs to the filter arithmetic, so the potential gain remains uncertain. This is not a claim that all raw-lookup samples are removable.

The [failed H1 diagnostic](../H1-diagnostic/RESULTS.md) matters as a guard lesson: selective leaf inlining lowered hit instructions6.832% but increased score1.843% and miss6.369%; the caller frame grew176→272bytes. Removing one call or branch count is insufficient. H1 changes the leaf boundary; this proposal changes only the boundary of the index's negative-result filter. It does not repeat the rejected optional-output position arithmetic, replace any tag scanner, cache leaf metadata as H2 does, or change record equality as H3 does. H1 remains rejected; H2 and H3 retain their separate decisions and evidence.

## One falsifiable hypothesis

Preventing eager construction/live retention of the home-bucket absent-member filter mask improves successful raw lookup by≥2% in every registered primary block, without demonstrated>1% guard or tree-owned-memory regressions. The proposed cause is less executed work/live state before a home-bucket hit, not a specific pipeline resource.

Change only `zbtIndexHomeMayContain` and/or the control-flow packaging of its call from `zbtIndexTableFind`. Preserve `zbtIndexTagBits` mathematics, zero→one tag folding, all filter updates, match order, leaf-ID validation, migration checks, optional outputs, and first-tombstone insertion hints. Do not include any H1/H2/H3 change in the first comparison. A standalone index experiment must start from the exact unchanged baseline.

## Three implementation options

| Option | Implementation choice | Main risk / static gate |
|---|---|---|
| A: outline the complete filter predicate | Make the existing `zbtIndexHomeMayContain(table, hash)` a small non-inlined read helper. Leave its call at the current post-candidate location, only for `probes==0`. The unchanged body loads `home_tags` and computes/tests the original mask. | A call is added to misses and displaced hits. Verify that both mask construction and this call occur only after the home candidates fail; reject if compiler motion defeats that boundary. This is the smallest maintainable first choice. |
| B: outline query-mask construction only | Keep table addressing/filter load in the caller; use a separate non-inlined query helper to produce exactly the existing three-bit mask after home candidates fail. Leave the insertion-side `zbtIndexTagBits` helper untouched and inline so mutation/filter maintenance gains no extra call. | A pure helper may still be moved by optimization. Require actual ARM and GCC15/LTO control-flow proof; do not add volatile state, compiler barriers or artificial effects to rescue it. Compare extra calling convention/live-state cost against A. |
| C: outline the probe continuation | Keep the original first-bucket candidate resolution on the inline path, then enter a non-inlined continuation for the existing home filter check and subsequent bucket traversal. Reuse a shared candidate-matching body so the leaf helper/scanner stays identical; preserve first-bucket tombstone/insertion bookkeeping on the insertion path. | Most invasive: duplicate filtering, changed probe order or lost first-tombstone hints are unacceptable. Reject if maintaining one probe implementation requires substantial duplication or a large state object. Codegen must place no filter-mask work on a successful home hit. |

These are three ways to enforce the same existing filter-use boundary. No new hash, alternate filter, saved member position, ISA-specific instruction, prefetch, batching, allocation field, or fixture-derived assumption is part of this hypothesis. If B cannot resist hoisting or C cannot stay small and auditable, preserve their failed/ineligible artifacts rather than expanding scope.

## Predictions and evidence gates

| Workload | Prediction to test |
|---|---|
| Short successful membership | Best opportunity, but magnitude depends on home-bucket-hit fraction |
| Score-returning hits | Can share the saving; a regression exposes caller/layout cost |
| Missing members | Highest regression risk: filter still runs and may gain a call; strict1% guard remains |
| Inline256 / external384 hits | Same index saving when resolved at home; smaller relative effect under hash/comparison cost |
| Existing-member updates | No memory change; output-producing index callers must stay correct and within guard |
| Collision-heavy/displaced hits and active resize | Mandatory extra guards before acceptance: slow continuation and rehash work must remain bounded and exact |

Static prerequisite: inspect the exact candidate ELF for each compiler cohort, trace the successful-home branch, and confirm that the mask multiply/shifts/OR/store no longer execute on that path. Preserve the byte-match broadcast needed for tags. Record frame and text size, but do not use them as speed evidence. If the codegen gate fails, select NONE for that implementation without a performance run.

Use the existing fixed primary/six-case ABBA gates on independently qualified native and target GCC15/LTO cohorts; no cross-cohort averaging. Add a separately frozen bounded collision/resize guard suite before adoption. Its correctness must include absent home-filter rejection, false positives, zero high-byte folding, same-tag distinct members, wraparound probing, deleted slots, narrow/wide IDs, source/destination migration, and the final rehash step that frees the old table. Insertions must retain the earliest usable tombstone, and lookups must still advance the original one-step rehash policy. Existing suites/oracles, assertions and referee stay unchanged.

Require zero memory increase, every primary block≥2%, no demonstrated>1% guard regression, fresh held-out confirmation, matched process-scoped counters/profiles, Intel guards and independent review. The matched measurement should show lower executed work for the primary rather than merely fewer symbol samples. If misses lose>1%, a primary win does not rescue the candidate; do not disable the filter or alter the fixture after seeing results. If no implementation passes, record REJECT/NONE and retain every artifact.

## Independence, consultation and TMA

Independent proposer: index-probe worker; exact model, tokens and currency cost unknown. Reviewed common H1/H2/H3 reports, native baseline and failed-H1 diagnostic; did not read other `proposals-next` files. No source/build/referee changes, no new measurement or runner access, and no commit/push.

Own tool discovery on2026-11-14 found no exposed cpu-perf/library_status tool. Consumed the controller's explicitly shared actual stdio consultation in [CONSULTATION.md](../CONSULTATION.md): server0.1.1, bundled list`deb5a0bac467`,3/287 indexed sources,158 passages, and documented ask/source-coverage limits. Those are controller calls, not calls by this proposer. No retrieved primary passage establishes this filter-work mechanism; the evidence is the pinned source and exact captured assembly. Reconsult on this specific boundary before implementation, including the risk that outlining taxes misses and that LTO moves pure work.

| TMA category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The recorded topdown-profiler captures are CPU2-wide without the required continuous exclusion/formula qualification. Children and a matched candidate funnel are unavailable. The raw exploratory percentages neither establish a backend resource cause nor quantify the saving from this proposal.
