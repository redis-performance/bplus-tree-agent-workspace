# Next hypothesis — separate steady-state raw lookup from resize handling

Independent proposal, raw-dispatch/live-state lens. Recommend a bounded experiment, not adoption. Start from exact unmodified upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`; do not layer H1, H2 or H3. Backend/model/token/currency costs unknown. No other next proposals were read. No source edit, build, measurement or runner access was performed.

## Evidence and limit

The baseline `native-profile/assembly.stdout` shows that `zbtreeScoreRaw` owns a176-byte frame (`0xc1c0`) and contains both incremental-resize lookup and ordinary table lookup. It loads `member_rehash`, branches around the rehash step (`0xc1f8`–`0xc210`), then joins the ordinary-table code at `0xc394`. That ordinary-table path still carries resize state: `0xc444` tests the retained resize pointer before the migration-ID checks at `0xc448`–`0xc464`. It spills live probe state around the unchanged leaf call at `0xc478`–`0xc47c`. This is exact code-generation evidence of a combined function, not a measurement of the cost of those individual instructions.

The frozen failed H1-B diagnostic strengthens the reason to challenge this combined state: selective leaf inlining grew the raw frame176→272bytes; hit instructions decreased6.83% but score instructions increased1.84% and miss instructions increased6.37%. Its timing guards also failed. It does **not** prove spills caused those losses, nor imply a smaller frame is necessarily faster. The generic leaf helper remains a real boundary in the baseline; preserving it gives this experiment a different mechanism from H1.

## One hypothesis

Separating the no-resize, read-only raw lookup path from incremental-resize handling will reduce live resize state and shared cold code in ordinary lookup, improving the500-member successful-hit primary by at least2% with no demonstrated>1% regression in score/miss/long/external/update guards or tree-owned memory.

Exact source scope: `zbtreeScoreRaw`, `zbtreeScoreRawWithHash`, a small internal raw-read dispatcher, and the boundary around the existing `zbtIndexFind` resize fallback. Stable reads should reuse `zbtIndexTableFind` with all insertion/position outputs NULL and the requested score output unchanged. The existing leaf helper, memchr, packed decoder, equality checks, logical mapping and index structure stay unchanged. Do not duplicate or simplify tag-probe semantics. Do not change SipHash or add metadata caches.

A readable semantic shape is: compute hash once where needed; if no resize is active, search the current member-index table with no insertion bookkeeping; otherwise call a separate helper that preserves the existing `zbtIndexFind` behavior, including its rehash step and both-table search. Ordinary mutation callers can keep the original path. The desired distinction is stable-state versus resizing state, not no-score versus score specialization.

## Three isolated implementation choices

1. **Outline only the raw resize fallback.** Add an internal non-inlined wrapper around the existing generic `zbtIndexFind` call for raw readers. Public raw entries keep the no-resize table lookup inline and branch to the fallback only when `member_rehash` is non-null. Reuse all existing lookup logic. This is the preferred minimal scope.
2. **Separate both raw kernels.** Use the same dispatch but place the stable single-table read in its own non-inlined helper, as well as the resize fallback. The public hashing entry becomes a small wrapper, potentially tail-calling the selected kernel. This trades one boundary for independently allocated live state; it must earn its cost on hits and misses. No leaf inlining.
3. **Partition the existing index dispatcher.** Keep public raw entry APIs unchanged, but give `zbtIndexFind` an early no-resize return through the existing table finder and outline its resizing remainder. Preserve all requested score/position/insertion outputs in this version, including insertion-slot hints. This is a broader alternative that could also help updates, but has higher mutation risk and must be compared independently, not combined with choices1/2.

All three test the same state-separation hypothesis. They are not permission for a handwritten second probe implementation, scanner changes, global inlining changes, H1 patch stacking, or compile-option tuning. `noinline` is a deliberate tested code boundary, not a performance guarantee; compiler/LTO behavior must be inspected independently.

## Code-generation and semantic preconditions

Before timing, verify on the fleet compiler that the steady-state kernel is distinct from the resize loop and no longer carries the per-candidate migration branch from the combined path. Report stack frames and live-state spills as static evidence, not as measured resource utilization. A reduced frame is useful supporting evidence but is neither required to claim semantic separation nor sufficient for acceptance. If GCC/LTO folds the split back together, retains the identical migration checks/state, or simply adds a call without the intended separation, retain that failed implementation and do not claim the mechanism happened.

The stable branch assumes no active resize **at dispatch**. The resize fallback must retain the original one-step progress, reload of resize state after the step, new-table-first search, old-table migration filtering, deleted/free leaf handling, and assertions. A rehash step may finish the resize and free its context: never retain a pointer across that step. No caller may skip resize progress solely because it asks for membership. Hash once with the same seed; preserve raw/prehashed API equivalence and optional score semantics. Tree-owned memory must remain exact.

The hot fixture is expected to reach a stable table after warmup, but explicitly verify that fact through an untimed structural check on the fleet; do not assume the scenario labels prove it. Separately add correctness coverage during resize, near completion, after deletion/shrink, with narrow/wide IDs and same-tag collisions. Frozen correctness/referee gates remain unchanged. Any necessary new harness is a separate freeze/requalification, never a mid-comparison edit.

## Predictions, falsifiers and guard risks

- **Hit and scored hit:** both should benefit if separating state is useful; no-score-only win paired with another scored regression would repeat the rejected trade-off and fail.
- **Miss:** the key adverse guard. It may benefit from smaller state or regress from an extra dispatch/call and changed branch layout. The previous H1 miss loss gives no reason to waive this bound.
- **Inline256 and external384:** expected smaller relative effect because hashing/record work dominate; require the same≤1% guard bound.
- **Update:** choices1/2 should leave mutation source paths unchanged, though whole-file layout can still affect generated code. Choice3 directly changes their dispatch and requires stronger correctness/mutation profiling.
- **Resize-heavy lookup:** a new cold-path call may regress this workload even if steady-state results improve. Add a preregistered, qualified resize-progress guard before adoption; never call it irrelevant because the primary is stable.

Reject on any correctness failure, failure to realize the stated separation, failure of the fixed primary gate, or a demonstrated>1% required guard/memory regression. Park uncertain controls. Use same-session serial ABBA and separate held-out confirmation; no reuse of H1's faster hit as candidate evidence. Compare matched process-scoped instructions/cycles and sample paths to check whether work actually decreases. Do not infer a gain from frame size, symbol size or branch count alone. Native/LTO/Intel are separate cohorts; a native pass cannot qualify portability.

## Why this is distinct

H1 grew the raw function by importing leaf-search work and distinguishing membership from scored lookup. This proposal keeps the leaf boundary and separates resize handling from stable read dispatch. H2 changes metadata access/layout; H3 changes short-record equality. Neither change appears here. The exact distinction is testable even if this candidate ultimately fails the speed gate.

## Consultation and TMA

Own exposed-tool discovery for cpu-perf/library_status returned no tools. This proposal consumes the shared controller `CONSULTATION.md` under the documented worker provision: actual stdio library_status/ask, server0.1.1, bundled list deb5a0bac467,3/287 sources and158 passages, no retrieved primary passage establishing these mechanisms. Those calls belong to the controller, not this worker. The evidence used here is the frozen source, assembly and matched H1 diagnostic; no external source authority or causal pipeline explanation is asserted. Reconsult the controller's CPU-perf service with this exact hypothesis and emitted code before implementation.

| TMA category | Qualified baseline | New candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Existing topdown captures are CPU-wide without complete exclusion/formula qualification. No new candidate or child-category capture exists. See `H1-diagnostic/RESULTS.md` for the diagnostic's scope limitations. Frame size and instruction changes do not supply pipeline-slot classification.
