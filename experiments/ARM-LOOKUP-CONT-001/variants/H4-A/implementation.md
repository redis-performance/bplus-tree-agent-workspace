# H4-A: outline the complete home-filter predicate

Status: **correctness ready; exact fleet code-generation gate and performance comparison pending**. Implementer: `cont_helper` (H4-A). Base commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Completed 2026-11-14 02:08 UTC. No other H4 implementation was inspected. No fleet access, benchmark, instruction-count measurement, profiling, commit or push.

## Exact source change

Change only `static inline int zbtIndexHomeMayContain` to `static __attribute__((noinline)) int zbtIndexHomeMayContain`. The function body, all call sites and every other byte of source remain unchanged, verified against the base commit after this one replacement. This includes the filter mathematics, zero-tag fold, insertion-side maintenance, probe/candidate order, tombstone hints, migration checks, leaf helper, scanner and equality.

The intended effect is to prevent computation and retention of the missing-member filter mask before a home-bucket hit that never consumes it. The predicate still runs on the original failure-to-match paths. Its additional calls can hurt misses, displaced hits and reference searches used by mutation; the source transformation makes no speed guarantee.

Candidate source SHA-256: `0ef8edf451945b24712a28add6c7b92ab250af24c3238ebb2fad8e352c763025`.
Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
See [implementation.patch](implementation.patch) and [source-verification.json](source-verification.json).

## Correctness validation

All runs below are local correctness checks using GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). The unchanged `qualify.sh` exited 0; its lookup fixture uses `verify`, whose branch does not read the measurement timer.

| Check | Result | Evidence |
|---|---|---|
| Upstream native `-O2` | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan `-O1` | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixtures × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixtures, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Existing optional-output oracle, ASan/UBSan | 90,000 passed | [output_oracle.json](output_oracle.json) |
| Existing external-record oracle, ASan/UBSan | 45,000 passed | [output_external_oracle.json](output_external_oracle.json) |
| Focused index oracle, ASan/UBSan | 54 reference checks, 21,602 table checks, 16 resize steps, 2 completed resizes | [index-oracle.json](index-oracle.json) |

The new [index_oracle.c](index_oracle.c) is separate from the frozen referee. Its direct four-bucket fixtures run in both narrow and wide representation, using actual wide IDs above 65,535. Hash high bytes zero and one deliberately share the folded tag, with all homes in the final bucket; 24 entries force displacement and wrap through bucket zero. It verifies found bucket/slot identity, absent-filter rejection, a same-tag false positive, tombstone reuse without changing `filled`, continued reachability beyond the tombstone, and the first-tombstone insertion hint for a fully deleted probe run. These are synthetic index fixtures, not measured workload distributions.

Its full-tree portion builds 600 binary members, then starts narrow and wide-destination resizes. The wide destination uses the same bounded ID-gap technique as the upstream tests. Every member is checked through both tables before and after each migration step, with exactly one visible owner and its expected score. The existing structural checker also runs at each stage. Both final resize-completion transitions are observed, followed by public lookups through the replacement table. The original 57 tests additionally cover their broader narrow-to-wide score-movement and late-resize cases.

Both supplied oracles and the added oracle use C11, `-g -Wall -Wextra -O1 -DREDIS_DEBUG -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`; the added oracle also uses `-Werror` and the existing test-only helpers. They link unchanged experiment `standalone.c` and `siphash.c` with `-lm`. All executed tests exit 0 with empty stderr.

The first compile of the **added test** failed `-Werror=sign-compare`: its unsigned mode parameter was compared to the table's signed `wide_ids`. The failed source and compiler log are retained as [index-oracle-first-attempt.c](index-oracle-first-attempt.c) and [index-oracle-first-attempt-build.log](index-oracle-first-attempt-build.log). Changing that test parameter to `int` fixed the warning. The implementation source and test conditions were unchanged; no runtime failure or measurement retry occurred. Original qualification evidence was restored after copying candidate logs into this variant directory. `git diff --check` passes.

## Static code-generation inspection

Built a separate **unexecuted x86-64 ELF** with GCC 13.3, C11, `-O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`, no LTO, unchanged lookup fixture and compatibility sources. Its SHA-256 is `3975ad50ba98cf84ab16e14a80c2766e79b74702d872a5579c6606c39019eb27`. This is static inspection, not local performance evidence or ARM validation.

The [predicate assembly](filter-codegen.txt) contains a distinct `zbtIndexHomeMayContain` at `0x2a70`. The `0x9e3779b97f4a7c15` multiplier, shifts and bit combination are inside this helper. Neither that filter constant nor the zero-fold precomputed filter constant appears in the [raw lookup assembly](raw-codegen.txt). Required tag-byte broadcast arithmetic remains in the caller.

For the current-table narrow path, leaf matching calls the unchanged helper at `0xd8ff`; success branches at `0xd90a` directly to the return epilogue at `0xddbe`. Exhausting the candidate mask leads through `0xd964`, then the probe-zero check at `0xd971`, and only then to the filter call at `0xd97d`. The rehash-destination path likewise branches from successful matching at `0xd6d5` to that return; its filter call is later at `0xd75b` after exhaustion and a probe-zero check. Wide-table paths retain the same separation, with filter calls at `0xdb59` and `0xdd3d`. The outlined helper uses no stack frame in this ELF; raw lookup retains a stack frame and caller preservation.

This confirms the requested boundary in this compiler's local code generation only. Exact ARM native, GCC15/LTO and fleet Intel ELFs must independently prove that successful home hits execute no filter construction or call before any timing. The attribute is not proof against all interprocedural motion or later toolchain changes. Full symbols are retained in [codegen-symbols.txt](codegen-symbols.txt); build output and compiler identity are beside it.

## Remaining gates and limitations

Use the chair's independently qualified cohorts and unchanged ≥2% primary improvement in every block, ≤1% guard/memory regression and ≥250 ms windows. No source representation or allocation changes, but unchanged tree-owned bytes still require fleet validation. Additional collision/displaced/resize **performance** guards must be separately frozen and qualified before adoption; this correctness oracle does not qualify their performance. Fresh confirmation, matched profiles and independent review remain outstanding. Do not combine H1–H3 patches or waive slow-path costs.

## TMA classification

| Category | ARM baseline | H4-A |
|---|---|---|
| Frontend_Bound | Unavailable: scope/formula qualification absent | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Child categories unavailable. No pipeline cause is inferred from assembly, hotspot shares or another architecture. Separately audited Intel baseline captures do not establish an H4 candidate classification.

## Consultation provenance

Own exposed-tool discovery found no `cpu-perf`/`library_status` tools. Consumed the controller's actual shared stdio filter-boundary `library_status` and `ask`; these were not calls made by this implementer. The question included the exact source/assembly, whole-predicate boundary, pure-call motion risk, prior guard failures and index correctness obligations. Its manually entered 02:15 recheck time was a transcription error; the chair records the actual recheck around 02:04 UTC, with unchanged upstream identity.

The bundled library is revision `deb5a0bac467` (2026-10-05), 3/287 sources, 158 passages and zero vectors, with keyword-only retrieval. No supporting source passage matched, so unread entries and unrelated bundled examples supply no evidence for this mechanism. The consultation did not change the selected declaration-only implementation; slow-path overhead and exact fleet control-flow inspection remain explicit gates. Detailed participant accounting remains in the private record.
