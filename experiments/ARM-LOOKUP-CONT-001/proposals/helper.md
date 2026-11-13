# Independent proposal: expose the leaf match across the helper boundary

Status: **PROPOSE**, with the exact earlier inline patch as the first implementation option. No new performance result or source acceptance. This proposal concerns helper boundaries and specialization only; it does not select another track's scanner or metadata changes.

## Identity and evidence

Author: independent Codex worker `cont_helper`. Exact model, token usage and monetary cost: unknown. Inspection completed 2026-11-13 23:06 UTC. No other continuation proposal was read. No source changes, builds, fleet access or measurements were performed by this worker.

Target source: `experiments/ARM-LOOKUP-GAP-001/current/src/zset_btree.c`, extracted from upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`; prior frozen source/referee commit `4876d21ce62fdf9306572b690c891d2d5ed0e04d`. The chair reports a fresh upstream fetch with the same head. The preceding experiment stays sealed and rejected.

The [qualified standalone baseline](../../ARM-LOOKUP-GAP-001/BASELINE.md) uses GCC 13.3, no LTO, Ubuntu/glibc 2.39 and the 500-member full-overlap raw lookup fixture. Its whole-process user-cycle profile places 41.91% in the leaf helper and 21.91% in raw lookup. Setup/warmup are included; these are not exact timed-loop fractions. About one fifth of samples remain unresolved libc PCs, so this proposal does not label them `memchr` cost.

The [captured assembly](../../ARM-LOOKUP-GAP-001/baseline/lookup-assembly.txt) gives a concrete boundary to investigate:

- `zbtreeScoreRaw` begins with a 176-byte frame. At `c0c0`/`c0c4` it stores four caller registers before the leaf call at `c0c8`, then reloads them at `c0cc`/`c0d4`.
- `zbtScoreLeafFindMember.constprop.0` begins at `34c4` with a separate 128-byte frame and saves several callee registers. It still calls libc routines internally.
- `zbtIndexFind` and `zbtIndexTableFind` are already forced inline in source. The leaf helper remains an out-of-line boundary inside that otherwise exposed lookup path.
- The raw API's score pointer is a runtime argument in the no-LTO standalone build. Even an inlined leaf need not see a constant NULL score. Position and several index-result pointers are constant NULL in this API.

The privately archived integration prototype was audited exactly: its entire patch changes `static int zbtScoreLeafFindMember` to `static inline __attribute__((always_inline)) int zbtScoreLeafFindMember`. It changes no helper body, scanner, prefetch, batch path or arithmetic. Its GCC 15.2/Bookworm/LTO diagnostic reported +5.02% throughput, three samples per binary with disjoint ranges. The helper symbol disappeared; whole executable text decreased from 4,710,646 to 4,710,190 bytes despite local raw-lookup growth. This is a reason to test the boundary, **not a qualified standalone effect or acceptance claim**: its server workload, compiler, runtime and link configuration differ; guard, A/A and acceptance coverage were incomplete. Exact integration link flags must be frozen from the build record before any matched-toolchain cohort.

The [sealed prior rejection](../../ARM-LOOKUP-GAP-001/RESULTS.md) tested only ways of avoiding unused logical-position work. Its three primary median improvements, 1.39–1.84%, missed the 2% gate. None removed this leaf call. Do not incorporate any of those patches into this experiment's baseline or silently combine them with inlining.

## Falsifiable hypothesis

For successful short membership checks, exposing leaf matching to the already-inlined index lookup will remove enough cross-function register preservation and permit better allocation/scheduling to improve the qualified primary by at least 2%, with no demonstrated greater-than-1% guard or tree-memory loss. Constant propagation may contribute, but it is not sufficient evidence by itself: the selected implementation must demonstrably change the helper boundary or its live-state cost beyond the previous position-only patches.

This is a code-generation hypothesis, not a claim that the processor is frontend-, backend- or memory-bound. Removing the call may only move spills into the caller, and growth can outweigh the benefit. The existing profiles cannot distinguish those possibilities.

## Three implementation options for this one hypothesis

| Option | Concrete change | Distinguishing prediction and risk |
|---|---|---|
| A — exact global leaf inline | Apply only the archived `static inline __attribute__((always_inline))` declaration change. Leave the original helper body intact. | Direct replication of the strongest existing lead. The hot leaf call must disappear. Compiler allocation can eliminate caller/callee preservation, but all index callers may grow; score and mutation paths are the main risk. GCC 13 need not obtain the same constant propagation as GCC 15/LTO. |
| B — selective membership specialization | Factor the original body into one shared inline implementation; retain a normal generic wrapper for output-producing callers. Provide a membership-only inline wrapper passing literal NULL outputs. In the raw API, explicitly dispatch the NULL-score case through the already-inlined index path to the membership wrapper; retain the original generic path for requested score/position outputs. Select the wrapper using output requirements so mutation callers remain generic. Do not duplicate the scanner or handwrite the rejected logical-mapping shortcut. | Exposes a literal NULL score despite the no-LTO API boundary and restricts leaf expansion to membership. Expected stronger no-LTO specialization and less mutation caller growth than A, with an extra dispatch/code-layout risk for scored lookup and misses. Inspect the actual compiler result: a shared core accidentally inlined everywhere would defeat the scope of this option. |
| C — separate match kernel from result materialization | Extract one shared inline leaf-match kernel that preserves tag search, external-hash filtering, packed decoding and equality, returning a physical slot or explicit no-match sentinel. Materialize logical position/score in the existing generic wrapper or index success path, after match. Keep a generic wrapper for output-producing uses. No new fast scanner or packed format. | Lets the index caller integrate candidate matching without carrying score-decoding state through its scan. Unlike B, changes the internal result contract and lifetime of the physical slot. May reduce the inline region, but extra slot plumbing or additional generic calls can lose. If generated code is merely the old unused-position patch with the same helper boundary, reject this option as non-distinct before timing. |

These are different scope and dataflow choices, not three spellings of the same conditional. A is the smallest and best anchored; B limits affected callers and addresses the no-LTO NULL visibility explicitly; C tests a narrower kernel boundary at higher review/correctness cost. Separate implementers should retain all three actual patches and inspect their code generation before ranking them. Do not use global `flatten`, forced hash inlining, iteration duplication, batching, prefetch or explicit SIMD.

## Predictions, guard coverage and correctness

Primary: the unchanged successful short, NULL-score 500-member fixture. Existing score, miss and 256-byte guards stay frozen. The 256-byte member uses inline storage; a separate 384-byte fixture is required for external records. Allocation/tree-owned bytes should be exactly unchanged for all options, since no persistent layout changes.

A may help both membership and score lookup but has the broadest code-growth exposure. B should most favor NULL-score membership while leaving mutation internals close to baseline; its dispatch can cost misses and scored lookups. C may improve membership with less scoring state but regress output-producing lookup. Long and external members should improve less because hashing/comparison dominate more; any greater-than-1% regression still fails the guard.

Add only focused mutation coverage relevant to changed callers: existing-member update and missing-member insertion through `zbtreeFindForAdd`, including a split and member-index resize transition, plus deletion validity. Measure a bounded, preregistered mutation guard rather than introducing a blanket suite. Correctness must cover binary/zero-length members, same-tag collisions, external full-hash mismatch, reversed leaves, finite scores and signed zero, all optional-output combinations, and rehash migration. C must distinguish physical from logical position and never dereference its no-match sentinel. Preserve insertion-position outputs and revision/invalidation semantics.

Run the existing native, sanitizer and output oracles, preserving referee identity; add any missing relevant oracle before freezing the new harness. The previous correctness passes are useful baseline evidence, not validation of these unimplemented options.

## Toolchain transfer and decision protocol

1. First qualify a fresh GCC 13.3/no-LTO baseline on the reserved ARM fleet and compare all eligible variants serially with fixed same-session A/A and ABBA. Freeze source, fixtures, seed, allocator, compiler/linker flags and binary hashes. At least three ABBA blocks, unchanged 2% primary and 1% guard/memory gates, predefined uncertainty and retry rules.
2. Treat GCC 15.2/Bookworm/LTO as a separate deployment-like cohort with its own unchanged control and A/A qualification. Never compare raw times across cohorts or attribute a discrepancy to architecture. Compiler, libc, link mode and whole-server context are confounded in the existing evidence.
3. If attribution to LTO becomes necessary, compare LTO on/off using the **same compiler/runtime** in a separately registered cohort. A standalone LTO program can expose a different call graph from a server build; compare actual helper, raw and mutation assembly. A GCC 15 win cannot repair a failed GCC 13 gate retrospectively; it would be a separately scoped result.
4. Require fresh independent confirmation for any selected passing variant, matched baseline/candidate profiles and Intel guards before acceptance. Command-level transfer remains a separate integration handoff.

Record helper calls, frame sizes, spills/reloads and caller/text sizes from each exact binary. Symbol disappearance or lower instruction count alone is not a win. Matched owned-process counters and profiles should show whether total work or preservation costs changed; disclose setup/warmup boundaries. A retained hot helper boundary, displaced/worse spills, a gain below 2%, any failed guard, correctness failure, or unexplained timing win falsifies or parks the proposal as appropriate. Do not repeat failed trials unchanged until one passes.

## TMA classification

| Pipeline-slot category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | Unavailable: earlier CPU-wide collection lacks continuous exclusion proof | Unavailable: unimplemented/uncollected |
| Bad_Speculation | Unavailable: same scope blocker | Unavailable: unimplemented/uncollected |
| Backend_Bound | Unavailable: same scope blocker | Unavailable: unimplemented/uncollected |
| Retiring | Unavailable: same scope blocker | Unavailable: unimplemented/uncollected |

Qualified child categories are also unavailable. The parent must perform the required topdown assessment for new measurements with exact scope/affinity evidence; unsupported categories remain unavailable. Do not substitute IPC, cycle-sample shares or stall events for pipeline-slot categories.

## Performance MCP consultation provenance

Own availability discovery at 2026-11-13 23:06:44 UTC searched the exposed tool catalog for `cpu-perf`/`library_status`; it returned no tools. This worker consumed the parent's fresh **shared stdio** `library_status` and `ask` responses, not calls made by this worker. The parent's recorded question explicitly covered helper specialization, GCC 13/no-LTO versus GCC 15/LTO transfer, and mutation/score/long guards with the current source and baseline context.

The shared library reports bundled revision `deb5a0bac467` (2026-10-05), 3/287 linked sources indexed, 158 passages, zero vectors and keyword-only retrieval. `ask` matched no supporting source passages and marked its listed sources unread. Consequently no library citation or claimed literature support is used here, and no source reading is falsely attributed to this worker. The consultation provides no answer establishing the mechanism; direct source/assembly and the limited earlier diagnostic remain the evidence. The proposed matched-toolchain controls are this worker's methodological recommendation. Reconsult if implementation or new measurements reveal a different mechanism.
