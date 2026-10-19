# BUILDER-WRITE-001 implementation selection

Decision: **REJECT / NONE**. All three isolated variants are slower in every one of the six preregistered ABBA blocks at both primary sizes. No candidate advances to confirmation, performance guards, or adoption. Baseline source stays unchanged.

| Variant | 100K median elapsed change | 1M median elapsed change |
|---|---:|---:|
| A | +1.039% | +1.362% |
| B | +1.250% | +1.745% |
| C | +5.777% | +2.766% |

Positive means slower. Fixed screen completed 2026-10-19 02:36:48 UTC: 144 serial processes, 36 paired effects; exactly 1,000,000 updates per process at both sizes, 16-byte members, seeds 1/2/3 twice, same-session ABBA on leased AMD Zen 5 CPU 2. All process statuses, checksums, owned-byte equality checks and final binary hash checks passed. A/A had qualified both sizes before screen. The required improvement was at least 2% in every primary block. No post-result extra timing.

Correctness: all 59 patch/build/test commands passed, including four snapshots times native and ASan/UBSan original tests and unchanged score-boundary, physical-zero, and packed-decode oracles. [Independent root static review](independent-pre-screen-review.md) found no blocker. Rejection needs no independent performance confirmation. [Concrete guards](GUARDS.md) were frozen before screen; they were not run because no contender survived. The new tied-score performance referee remains unimplemented and cannot be represented as covered by correctness oracles.

Fresh scoped baseline profiles motivated the hypothesis, but smaller source metadata work did not improve measured update elapsed time. Assembly and text sizes are retained in codegen/; these alone do not establish a causal slowdown. No further candidate profiles are needed to reject clear gate failures. Raw per-process files and paired summary are in screen/. All losing patches remain in variants/.

Population: three sequential proposal passes and chair; three isolated implementations evaluated sequentially. These were not independent agents. Root supplied independent pre-screen review. Backend/model: inherited native Codex agent, exact model unavailable; measured token and USD cost unavailable. AMD completed totals: 2 populations, 0 accepted, 2 rejected, 0 parked.

Published decision UTC: 2026-10-19T02:39:28.158993+00:00.
