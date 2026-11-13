# Implementation A — guard the existing output block

Implemented only the chosen successful-match guard in `zbtScoreLeafFindMember()`: compute logical position and write optional outputs only inside `if (score || position)`. The equality result still returns immediately afterward. No scanner, helper body, inlining, assertions, layout, allocation, hashing or referee change.

Base source/referee commit: `4876d21ce62fdf9306572b690c891d2d5ed0e04d`. Upstream unstable: `ee8e7f70152404649ac947157fd662d11b4a00d5`. Candidate C source SHA256: `614af5e4502befea9e9898cd21b181d062093d09e0d57c2e61f26853d2e084f6`. Patch: [candidate.patch](candidate.patch). Detached isolated worktree A; no commit created.

The existing mapping helper only reads count/reversed state and returns arithmetic; skipping it when neither output is requested removes no assertion or side effect. Score-only, position-only and combined callers continue using the identical mapping and output expressions. Main risks are code-generation/layout changes and inadequate measured gain; no architecture speed claim is made here.

Referee hashes were compared with the frozen manifest; every file other than the intentionally changed C source matches exactly. [Hash checks](referee-check.json). Correctness is run through the unchanged `qualify.sh` with its native and ASan/UBSan upstream tests and three-seed fixture cells. The local command performs correctness only; no timing or profiling was run. Final outcomes are recorded below after command completion.

Independent implementer A did not read B/C implementations. Backend Codex; exact model/token/currency costs unknown. Own cpu-perf tool discovery again returned no exposed matching tools. The controller consultation is shared evidence, not this worker's call. The selected hypothesis and existing baseline support are recorded in the chair selection; compiler/performance validation remains for the fleet controller.

## TMA classification

| Category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The baseline CPU-wide collection remains exploratory without continuous exclusion evidence; no candidate capture was run by this implementer. See ../../BASELINE.md. No pipeline-resource explanation follows from this code change alone.

## Completed correctness result

PASS: 57/57 native upstream tests, 57/57 ASan/UBSan upstream tests, 12/12 native fixture cells and 12/12 sanitizer fixture cells (hit/score/miss/long on seeds17/29/43). The unchanged qualification command exited0. Logs are in correctness/. Referee hashes were rechecked after execution and remain identical. Candidate source and patch match the reported SHA256. No performance measurements or source adoption occurred.
