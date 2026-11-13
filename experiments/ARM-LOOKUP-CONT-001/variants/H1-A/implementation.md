# H1-A: exact whole-helper inline declaration

Status: correctness passed; eligible for the chair's native diagnostic fleet comparison. No performance result or source acceptance. The GCC 15/LTO cohort remains PARK after its qualification failure; native evidence cannot replace that gate.

Independent implementer: Codex worker `cont_helper`; exact model, tokens and monetary cost unknown. Base commit `73914990698c106c62a1ea09394b7a9147ea1077`, upstream source `ee8e7f70152404649ac947157fd662d11b4a00d5`. This worker did not inspect other implementation trees and did not commit or push.

## Implementation and semantic risk

The only source change is the declaration of `zbtScoreLeafFindMember` in `current/src/zset_btree.c`: replace `static int` with `static inline __attribute__((always_inline)) int`, using the exact two-line declaration from the earlier prototype. The helper body, all other source, and the referees are unchanged. No rejected position-arithmetic patch is included.

The intended mechanism is eliminating the leaf call boundary inside the already-inlined index path, permitting different register allocation and reducing cross-call preservation. This must be verified from the fleet binary; no local assembly or performance claim is made. Expansion affects output-producing and mutation callers too, so code growth or worse spill allocation may regress those guards. Representation, ownership and lookup semantics are unchanged by the source transformation, though compiler correctness and sanitizer coverage still matter.

An exact byte-comparison against the base source, after applying only this declaration replacement, passed. See [source-verification.json](source-verification.json) and [implementation.patch](implementation.patch).

- Candidate source SHA-256: `2ad4b1e3ba5f06b1672fd96d1e3f401274d1c28c251dea0c4f5accbca00a492a`.
- Baseline source SHA-256: `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.

## Correctness validation

Local correctness only, using GCC 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1). No benchmark, timer-based comparison, instruction-count measurement, profile or fleet access was performed. Inspected `lookup.c`: `verify` executes its correctness branch without calling its measurement timer.

| Check | Result | Evidence |
|---|---|---|
| Upstream native, `-O2` | 57 passed, 0 failed | [upstream-native.log](upstream-native.log) |
| Upstream ASan/UBSan, `-O1` | 57 passed, 0 failed | [upstream-sanitizer.log](upstream-sanitizer.log) |
| Six fixture cases × seeds 17/29/43, native | 18 passed | [fixture-native.jsonl](fixture-native.jsonl) |
| Same fixture cases, ASan/UBSan | 18 passed | [fixture-sanitizer.jsonl](fixture-sanitizer.jsonl) |
| Supplied optional-output oracle, ASan/UBSan | 90,000 passed | [output_oracle.json](output_oracle.json) |
| Supplied 384-byte external-record oracle, ASan/UBSan | 45,000 passed | [output_external_oracle.json](output_external_oracle.json) |

Ran the unchanged `sh experiments/ARM-LOOKUP-CONT-001/qualify.sh`; exit status 0. Its compiler output is retained in `qualification-driver.log`. Fixture cases are hit, score, miss, long, external and update. Both supplied oracles test all four score/position pointer combinations, reversed leaves, misses, multiple score encodings and signed zero. The external oracle asserts external storage.

Each oracle was compiled separately with `cc -std=c11 -g -Wall -Wextra -O1 -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`, include paths `current/src`, `current/compat`, `current/vendor`, the oracle C file (which includes the target source), `current/compat/standalone.c`, `current/vendor/siphash.c`, and `-lm`. Both executables exited 0 with empty stderr. Build logs, stderr files and compiler identity are retained beside this report. No failure was retried. `git diff --check` passed.

## Remaining fleet gates

The chair's separately scoped native diagnostic uses unchanged primary improvement ≥2% in every primary block, guard/tree-memory loss ≤1%, and qualified duration ≥250 ms, including the preregistered update work. It requires serial ABBA against the unchanged control. Fresh confirmation, matched profiles, Intel guards and review remain necessary for any later acceptance; none are claimed here. Check actual helper call removal, frame/spill changes and caller growth rather than treating source inlining as proof.

## TMA classification

| Category | Baseline | H1-A |
|---|---|---|
| Frontend_Bound | Unavailable: prior CPU-wide data lack workload qualification | Unavailable: not collected |
| Bad_Speculation | Unavailable: same scope blocker | Unavailable: not collected |
| Backend_Bound | Unavailable: same scope blocker | Unavailable: not collected |
| Retiring | Unavailable: same scope blocker | Unavailable: not collected |

Child categories unavailable. The chair owns the required topdown assessment. This correctness-only worker supplies no pipeline-slot causal explanation.

## Performance MCP provenance

On this implementation turn, own exposed-tool discovery for `cpu-perf`/`library_status` again returned no tools. At 2026-11-13 23:17 UTC, consumed the parent's shared stdio reconsultation (`library_status` and `ask`), not calls made by this worker. The question challenged the fresh helper hotspot, 128-byte frame, whole-helper inline versus selective specialization versus physical-slot kernel, explicitly distinguishing the prior arithmetic rejection. Its qualification status predates the chair's second qualification; this report follows the later chair selection for cohort eligibility.

The shared library is bundled revision `deb5a0bac467` (2026-10-05), 3/287 sources, 158 passages, zero vectors, keyword-only. It returned no supporting passages and marked relevant listed sources unread. No literature assertion or bundled benchmark number is used as validation. This limited consultation did not change the exact declaration-only implementation selected by the chair. Missing worktree memory files were read from the parent checkout; other variants were not read.
