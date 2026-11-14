# Independent H1 review — REJECT / source NONE

The H1 rejection is supported. None of the three implementations satisfies the frozen native discovery gates. This review closes H1 only; it does not stop the ongoing campaign or qualify its parked GCC15/LTO objective. Independent calculations and identity checks are retained in [H1-audit.json](H1-audit.json).

## Decisive findings

| Variant | Median primary elapsed change | Failed requirements |
|---|---:|---|
| A: whole-helper inline | −1.287299% | All three primary blocks miss2%; all three miss guards regress1.708–2.023% |
| B: selective membership | −6.786754% | All three blocks of score, miss and update regress; ranges2.340–2.662%,3.422–3.909%,1.812–2.099% |
| C: physical-slot kernel | −2.307831% | All three score and miss blocks regress; ranges2.880–3.459%,2.554–3.197% |

B and C pass every primary block, but their repeated guard losses independently block selection. A fails both primary and guard requirements. Memory is equal and correctness passes do not waive timing regressions. No fresh confirmation, Intel replication or diagnostic profile can retrospectively repair these failures.

## Raw reconstruction and qualification

I independently reconstructed216 comparison rows into54 ABBA blocks and72 renewed native A/A rows into18 blocks. Every row joins its individual stdout, successful command record, CPU2 affinity argument, case, seed17, sweep count, operation count, expected hits/score sum and binary selection. Slots and labels are exactly0/1/2/3 and ABBA. Process stderr is empty; no duplicate comparison cells exist. Published row/process evidence matches the retained private originals. All effects, pass decisions and zero memory deltas agree with the saved analysis. Minimum windows are485.682386ms for comparisons and495.197746ms for renewed A/A; every native A/A effect passes±1%.

Qualification2's original GCC15/LTO update block2 independently reconstructs to−1.318388652%, outside±1%, despite adequate duration. It remains PARK. Native exploration was separately declared before candidate measurement, and the lease interruption prompted fresh native qualification with unchanged binaries. The original failed qualification attempts remain retained. Native results supply no LTO or Redis command-level recovery claim.

The metadata `started` value for H1 belongs to the earlier build phase, not the renewed comparison start. It should not be interpreted as a per-row timing timestamp. Command order and the separate requalification/completion artifacts document the intended sequence; this reviewer did not observe live scheduling or runner isolation.

## Source, code generation and correctness

The frozen baseline C source has SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. I applied each retained unified patch in memory, verified its context, and obtained the exact candidate source hash recorded in H1 metadata and the isolated implementation tree. Eleven relevant referee/header/dependency files match across all three trees. I independently hashed the fetched baseline and all three ARM candidate ELFs; they match qualification metadata and per-row identities. Commands retain the same native GCC/O3/no-LTO build configuration across candidates.

A changes only the helper declaration. B preserves the original helper body inside one shared inline implementation, with explicit generic-output and membership paths. C returns a physical slot from the shared scanner, checks the no-match sentinel before mapping to logical position, and leaves index bookkeeping at the original successful-match point. The96-element leaf bound cannot collide with `UINT_MAX`. No concrete source-semantic defect was found. These are distinct helper-boundary variants; none changes record layout, hashing or the referee.

Saved ARM disassembly confirms A removes the generic leaf symbol, while B/C retain generic output helpers and embed matching in raw lookup. All three raw lookup frames are272 bytes and include direct memchr/memcmp calls. Recorded text sizes91119/98607/95135 bytes agree with the report. Symbol removal and these static sizes do not establish fewer dynamic spills, a pipeline bottleneck or a speedup.

For each variant, saved evidence supports57 native and57 sanitizer upstream tests,18 fixture cells per mode,90,000 optional-output oracle checks and45,000 separate external-record oracle checks. The latter explicitly asserts384-byte external records. The oracles exercise reversed leaves, exact score bits, misses and four score/position masks through the leaf helper. They are not an exhaustive matrix of B/C's public index-dispatch paths; integration coverage additionally comes from upstream tests and fixture cells. This limitation supplies no evidence of a defect and does not weaken the already decisive rejection. GNU compiler attributes and native-only measurements also do not demonstrate broad compiler/architecture portability.

## Ledger and diagnostic scope

The canonical `experiments/EXPERIMENTS.md` and `experiments/SUMMARY.md` correctly add two PARK qualification attempts and one REJECT population to the prior35:38 completed attempts,20 PARK,18 REJECT,0 approved; ARM28/Intel5/AMD5;24 populations,5 replications,9 qualification attempts. Renewed native A/A belongs within H1, and the failed-B diagnostic adds no implementation population or completed optimization attempt. Root-level ledgers explicitly preserve historical Intel notes and point to the canonical ledgers; my preliminary concern about missing root entries was withdrawn after checking those pointers. Active work is excluded.

`H1-DIAGNOSTIC.md` separately freezes failed-B whole-process counters/samples. Its instrumented timings are excluded from the216 discovery rows. This review does not independently validate its counter analysis; any resulting explanation must retain setup/warmup, sampling and single-pair limitations and cannot change H1's rejection.

## TMA and consultation provenance

| Category | Qualified baseline | Qualified H1 candidate |
|---|---|---|
| Frontend_Bound | Unavailable | Unavailable |
| Bad_Speculation | Unavailable | Unavailable |
| Backend_Bound | Unavailable | Unavailable |
| Retiring | Unavailable | Unavailable |

Qualified child categories are unavailable. CPU-wide baseline labels lack continuous exclusion/formula qualification; no validated candidate funnel accompanies this discovery decision. Samples, elapsed effects and static instruction listings are not slot shares.

This independent reviewer inspected files and analyzed saved evidence only: no fleet operations, measurements, source edits or subagents. Own enabled-tool discovery found no cpu-perf/library_status tools. I consumed the controller's actual shared stdio consultation/reconsultation recorded in `CONSULTATION.md`, not calls made by this reviewer: server0.1.1, bundled revision `deb5a0bac467`,3/287 indexed sources and158 passages, with no supporting primary passage for the proposed mechanism. The shared topdown explanation supplies scope guidance, not causal proof. Reviewer backend is Codex; exact model, tokens and monetary cost are unreported. Independence is from the three proposers/implementers; no candidate adoption is authorized.
