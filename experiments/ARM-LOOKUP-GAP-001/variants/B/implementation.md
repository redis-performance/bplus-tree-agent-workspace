# Implementation B: early success for no-output lookup

Implemented one line in `zbtScoreLeafFindMember`: after length equality and complete `memcmp` success, return1 if both `score` and `position` are null. Otherwise execute the original logical-position calculation and optional output writes unchanged. No hash, probe, scanner, decoder, helper-inline, allocation, or layout changes.

Base commit `4876d21ce62fdf9306572b690c891d2d5ed0e04d`, current upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`. Candidate C-file SHA256 `2051a7e1942701eb45498403447910d5aba84c48624c74fc7754d96b3ce2ff12`. Independent implementer B used an isolated detached worktree and did not read implementations A/C. [Patch](candidate.patch) and [referee hash check](referee-check.json) preserve the exact change and unchanged inputs.

Correctness: `sh experiments/ARM-LOOKUP-GAP-001/qualify.sh` exited0. All57 native and57 ASan/UBSan upstream checks passed;12 native and12 sanitizer fixture cases passed across hit/score/miss/long and seeds17/29/43. [Validation](validation.json) contains exact counts and log hashes; [logs](correctness/) are retained. No local timings, instruction counts or profiles were run; no runner access occurred.

The early return is after verified membership, including the existing external-member hash/length checks. Output-requesting callers execute the same body, preserving reversed-leaf mapping, exact scores and signed zero. No side effect or assertion is skipped by omitting `zbtScoreLeafPhysicalPos`, which is pure arithmetic. Remaining risk is compiler/layout sensitivity: the source expression may not improve generated code or may affect other call paths. Serial fleet comparison, matched assembly/profiles, guards and fresh confirmation remain pending. Correctness is not a speed result.

Backend Codex; exact model/token/currency costs unknown. This worker's renewed tool discovery found no directly exposed cpu-perf/library_status tool. Root's consultation and post-profile reconsultation are explicitly shared evidence; the worker did not make those calls. No novel causal performance claim was added during implementation.

## TMA classification

| Category | Qualified baseline | Candidate B |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Baseline CPU-wide capture lacks continuous exclusion evidence; candidate profiles are uncollected. See [baseline scope](../../BASELINE.md#tma-classification). No TMA child category or mechanism is inferred from this correctness-only implementation.
