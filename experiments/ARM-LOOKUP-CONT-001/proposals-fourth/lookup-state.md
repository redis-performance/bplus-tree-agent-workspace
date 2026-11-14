# Fourth proposal: lookup state and the home-filter dependency

Role: independent proposal reviewer. Recommendation: **NONE for implementation now; perform a baseline-only probe-path census if this lead remains worth pursuing.** The distinct screened hypothesis is replacing the exact three-bit home-filter computation with immutable lookup data. Native assembly makes it attractive, but the target GCC15/LTO assembly already keeps that computation off successful home-leaf hits. The available profiles do not quantify the remaining fallback opportunity. Another native-only improvement would repeat the portability problem exposed by H5.

No source, fixture, build flags, allocator, hashing, timing scripts or frozen referees were changed. No new workload execution, measurement or fleet access occurred. Other fourth-round drafts were not read. Earlier work on H1/H2/H3/H4/H5/H6/H7/H8 was implementation or review work in this campaign; this proposal is independent of the other fourth-round proposal authors, not independent of that campaign history.

## Revision1 and frozen evidence

Revision1 changes only the input-packet status and its implications. Revision0 is retained byte-for-byte in private history, SHA-256 `21aa0247a24b864a94686f5346fbf4dc8e22494b67e76464a9bab155d7873f3d`. **Recommendation unchanged: NONE pending the specified baseline-only probe-path census.** H2's final qualification failure neither supplies new mask-path attribution nor proves a candidate regression. H7's frame rejection strengthens the need to retain the independent frame gate; H8's static eligibility supplies no timing evidence for this different mechanism. No fourth-round tags or metadata draft was read.

The input is extraction `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, source SHA-256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. The source hash was checked during this pass. H1, H3, H4, H5 and H6 remain rejected; H2-A/C remain rejected. The [final H2 review](../reviews/H2-FINAL.md) closes H2 as **PARK / no accepted source**: both hosts pass seed29, but ARM seed43 misses the fresh±1% A/A bound in one miss block (−3.601147%), so its candidate comparison and supplemental phase do not run. This is failed qualification, not a measured H2-B regression. Intel seed43 cannot rescue the incomplete target confirmation; the final review also preserves the cross-host stopping deviation. Prior H2 profile evidence remains bounded historical support for H2's mechanism only.

[H7 is static NONE](../H7-RESULTS.md) for all three variants: target general raw frames grow176→192 bytes while no-score clones stay176. No H7 performance cohort ran; exact-mask success in assembly cannot waive frame growth. H8-A and B are [statically eligible](../reviews/H8-A-ARM-CODEGEN.md), with B established by the [B/C audit](../reviews/H8-BC-ARM-CODEGEN.md); the [C consumer supplement](../reviews/H8-C-CONSUMER-CODEGEN.md) closes C's initial target-caller coverage gap and makes C statically eligible too. H8 is **unmeasured in this frozen packet**, not accepted. H7 exact masks and H8 range-first classification remain excluded assigned mechanisms. No H2 or other candidate patch is stacked.

The [matched ARM assessment](../H2-ARM-PROFILES.md) and [independent audit](../reviews/H2-ARM-PROFILE-AUDIT.md) establish exact ELF joins and process-user counters. H2-B cycles change −4.914% native and −5.150% LTO, with instructions −2.300% and −2.101%; these support H2's own mechanism and are not predicted gains for this proposal. Original native whole-process user-cycle shares are leaf helper41.38%, raw lookup21.77%, SipHash7.65%, named memcmp2.82%. Whole-function shares cannot attribute the raw function's cost to a particular multiply or load. The [matched Intel review](../reviews/H2-PROFILE-GUARD-AUDIT.md) likewise does not isolate this mask computation.

## Exact source and code evidence

At [source line1833](../current/src/zset_btree.c#L1833), `zbtIndexTagBits(tag)` multiplies the eight-bit tag by `0x9e3779b97f4a7c15`, then ORs bits at `tag & 63`, `mixed >> 58`, and `(mixed >> 36) & 63`. This is the missing-member filter, **not** the bucket equality mask already screened as H7. The exact mapping must remain unchanged. `zbtIndexHomeMayContain` consumes it at1847–1852. Insert bookkeeping uses the same mapping at1843, the reference finder at2062, and scan at4254. The ordinary finder calls the predicate only after home candidates fail, at2022; success returns at2014.

| Actual saved baseline | PCs and assembly lines | Consequence |
|---|---|---|
| ARM native, [assembly](../native-profile/assembly.stdout) | `c580–c5cc`, lines12126–12145: constant construction, multiply `c5a8`, extraction, shifts and ORs; result stored at `[sp,#160]`. `c59c` is separate tag broadcast and must remain. | GCC13 hoists the mask arithmetic before the home search. A lookup table could remove executed arithmetic even for home hits. |
| ARM GCC15/LTO, [matched assembly](../H2-profiles/arm-gcc15-lto-base/assembly.stdout) | No-score clone `406820`; current-table home candidates `406a14–406af0`, lines6345–6400; leaf call `406a9c`, success branch `406aac → 406ff0`; fallback `406b04 → 406bfc`, then mask `406c00–406c40`, lines6468–6484. | Successful home hits bypass this arithmetic already. The same is true for the rehash-table home path: leaf call `40694c`, success `40695c → 406ff0`, fallback `406b98 → 406c4c`. |
| ARM GCC15/LTO general reader, same assembly | Predicate materializations `4064dc–406520`, `406530–406574`, and wide-ID counterparts `406734–40677c`, `406788–4067d0`. | Audit the scored/general reader separately; absence of a multiply in one clone is insufficient. |
| Intel native, [matched assembly](../intel/H2-profile-native-base/assembly.stdout) | `d600–d630`, lines13125–13138: constant, multiply `d60a`, shifts/bit-set/OR, spill. Another table path at `d878–d8a9`. | Native Intel has the arithmetic too, but a replacement load may compete with the pointer loads; arithmetic count is not a latency guarantee. |

The target already demonstrates the ordinary load dependency after candidate validation: leaf-pointer table load `406a44`, indexed leaf load `406a4c`, leaf-ID assertion `406a58–406a60`, resize test `406a64`, then leaf helper `406a9c`. Merely copying the pointer-table and ID-limit fields into earlier locals is not a credible distinct optimization: no measured dependency attribution shows that the hardware cannot overlap these loads, and the compiler may sink them or extend live ranges. Removing their checks, assuming no resize, changing layout or forcing scheduling would violate the current scope or repeat earlier mechanisms. Physical/logical score-position work also does not explain the no-score primary case.

## One falsifiable hypothesis; three conditional options

Hypothesis: an immutable exact tag-to-filter mapping can reduce work on paths that actually evaluate the home filter enough to improve the original primary lookup by at least2%, without adding more than1% to any guard. **Not selected:** the target's common path skips the work, and the eligible fallback fraction/cost is presently unknown.

If a baseline census supports reopening it, the alternatives would be independent baseline implementations, with all existing helper boundaries and predicate placement preserved:

| Option | Source change | Tradeoff and static prediction |
|---|---|---|
| A, lookup-only full mask | Add `static const uint64_t[256]`; use it only in `zbtIndexHomeMayContain`; leave the shared arithmetic helper for insertion/scan. | 2048 bytes static read-only data, one indexed64-bit load. Removes lookup mask multiplication/extraction/shifts; insertion/scan retain arithmetic. Reference finder users are affected too, so this is not raw-reader-only. |
| B, shared full mask | Same256-entry table replaces `zbtIndexTagBits` for every consumer. | Same2048-byte data, a single mapping implementation, broader insertion/reference/scan exposure. No mutable cache or per-tree memory. |
| C, packed positions | A256-entry `uint16_t` table holds the two mixed six-bit positions; existing first-bit computation, shifts and ORs construct the mask. | 512-byte data; removes multiplication/mixed extraction while retaining several scalar operations. Smaller footprint but weaker speed hypothesis and an added dependent load. |

The entries must encode the original unsigned64-bit wraparound formula for every tag0–255, including folded-zero behavior. A short constant-expression initializer mechanism or a reproducibly generated table with an independent exhaustive oracle is preferable to unexplained literals. No runtime initialization, mutable state, tag remapping, altered filter false-positive behavior or changed hash is permitted. These options are not H4 helper outlining: no new calls or moved boundaries are allowed. They are also not H6 record hints or H7 equality masks.

These are static-data versus arithmetic tradeoffs, not zero-memory changes: A/B add2KiB and C adds512B before alignment/linker effects, even if tree-owned bytes remain identical. Report total ELF sections as well as the unchanged≤1% tree-owned-memory gate. No post-result memory exception.

## Recommended baseline-only diagnostic

First review saved exact ELF control flow and any existing per-PC samples offline, keeping native and LTO separate. Samples are a localization check, not exact path counts or a measured dependency chain. Do not run a new local profiler.

If additional evidence is required, register a separate diagnostic harness before execution. Use the frozen baseline implementation, original fixture constructors/hash/seeds, query order and warmup; add counters only to a diagnostic copy, never the referee or timing executable. Count one fixed deterministic query sweep after the original setup/warmup, with explicit per-table accounting: home success before predicate, predicate evaluations, true/false predicate results, displaced success, terminal miss, candidate leaves examined, stale/free-ID skips, resize-table versus current-table visits, narrow/wide representation and resize state before/after. Also check tag occupancy and folded-zero counts. Preserve full result/output checksums and owned bytes before/immediately after the diagnostic sweep. Repeat original six fixtures and member-based rank cases; state separately that the five score-only guards are not all raw lookups. Seeds17/29/43 are evidence diversity, never knobs for selecting a favorable fixture.

This is structural diagnostic instrumentation, not a new comparison or a timing result. All execution that collects performance or dynamic instruction information belongs on the reserved fleet; this proposal requests no local calibration. Never time the instrumented build or merge its counters into candidate code. A reviewed diagnostic census with zero/rare target filter evaluations weakens or rejects the table lead; it does not justify moving the computation back onto hits. A material count alone is insufficient: existing process samples must also support fallback relevance, or preserve NONE. Do not infer “2% saved” by multiplying a path fraction by static instruction count.

Before any future comparison, static rejection gates are: no table load added to a target home-success path; arithmetic removed where promised; no new call, initialization, branch hint, allocation, probe reordering or expanded leaf-helper boundary; no raw-frame growth or extra spills; all narrow/wide/current/rehash paths preserve assertions, tombstones and migration checks. If compilers reconstruct arithmetic, hoist a new load onto target hits, or enlarge hot frames, reject that implementation without broadening the patch. Both raw clones and general/scored paths must be inspected in native and target LTO on ARM and Intel.

## All11 frozen-case predictions, if reopened

These are qualitative risks, not forecasts or acceptance evidence. The primary remains the original500-member hit case; no candidate is eligible merely for a miss win.

| Case | Expected effect/risk |
|---|---|
| Hit | Native may remove eager arithmetic; target home hits have no direct saving. Fallback census determines whether any primary opportunity remains. |
| Score | Similar filter exposure but distinct reader/code generation; no score decoding change. Must inspect general reader separately. |
| Miss | Most direct arithmetic-saving opportunity; indexed-load latency/cache pressure can regress. H4's Intel miss failure makes this a leading falsifier, although no new call is proposed. |
| Long inline256 | Same filter mechanism with hash/comparison dilution; no presumed protection against1% code-layout/load regressions. |
| External384 | Same dilution plus external hash/pointer work; preserve external ownership and rejection order. |
| Update | Reference lookups affected by A; B additionally changes insertion mapping; C retains more arithmetic. No presumed neutral result. |
| Iterator forward | Score-only iteration has no direct mask benefit; static-data/cache/code-layout effects remain a guard. |
| Iterator reverse | Same lack of direct benefit, independently guarded. |
| Rank forward | Member lookup can benefit only on executed filter paths; score-tree/rank costs dilute it. |
| Rank reverse | Same mechanism with separately verified order/rank/output behavior. |
| Churn | Lookup, insert/delete, ID reuse and resize paths expose wider effects, especially B; preserve all ownership/memory endpoints. |

Any implementation would still require original57 native+57 sanitizer tests,36 fixtures,135k output/external oracles, plus exhaustive256-tag mapping equality, folded zero, same-tag/filter collisions, displaced/wrap/tombstone/full-table cases, active/completed resize, narrow/wide IDs and scan/reference equivalence. These tests have not been run for this unimplemented proposal. The original≥2% primary,≤1% guard/memory, qualified A/A, independent confirmation and adversarial review gates remain unchanged.

## TMA classification and consultation limits

| Pipeline slots category | Qualified ARM baseline | Proposed candidate |
|---|---|---|
| Frontend_Bound and children | Unavailable | Unavailable: no candidate |
| Bad_Speculation and children | Unavailable | Unavailable: no candidate |
| Backend_Bound and children | Unavailable | Unavailable: no candidate |
| Retiring and children | Unavailable | Unavailable: no candidate |

The saved ARM collector rendered CPU-wide generic values without qualified scope/formulas; no100% pipeline tree can be supplied. Intel's separately qualified baseline roots/children are in the [matched review](../reviews/H2-PROFILE-GUARD-AUDIT.md), with its CPU-wide accounting and parser caveats. They do not classify an ARM dependency or predict this table's cache behavior. No unmeasured candidate TMA values are invented.

Own tool discovery found no callable cpu-perf/library_status endpoint. This pass therefore consumes the controller's actual prior shared consultations as disclosed in [CONSULTATION.md](../CONSULTATION.md) and the matched-profile report: server0.1.1, library revisiondeb5a0bac467,3/287 indexed sources,158 passages. Earlier home-filter consultation supplied no supporting primary passage; later matched-profile retrieval returned generic pmu-tools release/features material that does not establish this cause. Those are shared calls, not calls by this reviewer. This exact immutable-table/target-fallback question has not received a fresh consultation; the controller must reconsult before selecting it. No unavailable retrieval is represented as support. Detailed execution provenance remains separate; exact model and token cost are unknown.
