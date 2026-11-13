# Proposal A — avoid unused logical-position conversion

Decision: propose a bounded experiment. No source change or acceptance yet.

Independent proposer A, Codex backend; exact model, tokens and monetary cost are unknown. This proposal did not read proposals B or C and did not access a runner or execute measurements. Source/referee commit `4876d21ce62fdf9306572b690c891d2d5ed0e04d`; current upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`.

## Evidence and hypothesis

All 12 registered A/A blocks pass, including the no-score primary and score/missing/long guards. The primary baseline is 29.867 ns/lookup; leaf helper accounts for 41.91% of all captured user-cycle sample weight. This is whole-process sampling, including setup/warmup, not a measured fraction of exact timed-loop cycles.

In `current/src/zset_btree.c`, `zbtScoreLeafFindMember()` computes `zbtScoreLeafPhysicalPos(leaf, physical)` after a successful member comparison, before testing either optional output pointer. Membership callers pass both outputs as NULL. The captured `baseline/lookup-assembly.txt` corroborates that unused work survives in GCC13.3 code: the specialized helper loads count and the reversed-leaf flag, computes the logical position, and only then branches on the score pointer (addresses `0x35d0` through `0x35e8`). Its position pointer is already specialized away. These are static code observations, not measured instruction costs or proof of a specific pipeline bottleneck.

**Falsifiable hypothesis:** computing the physical-to-logical conversion only when `score || position` is non-null reduces the qualified 500-member no-score hit time by at least 2%, without a demonstrated >1% loss in any registered guard or tree-owned memory. Successful membership needs only equality; it does not need a rank-like position or decoded score.

Target exactly the successful-match block in `zbtScoreLeafFindMember()`. Retain memchr, tag collision continuation, packed record decoding, length comparison, memcmp, external hash filtering and every memory layout. Put the existing logical conversion and output writes inside an optional-output guard. Do not change the physical/logical helper itself or its iterator callers. Do not combine this with force-inlining, a new scanner or a short-string comparison.

## Predictions and mechanism check

| Fixture | Prediction |
|---|---|
| 500 short no-score hits | Primary improvement; each successful lookup can skip unused logical conversion. |
| Short score-returning hits | Approximately neutral; same conversion and score decode remain required. A compiler-generated extra branch could instead regress and must be measured. |
| Missing short members | Approximately neutral; matching-success block is not entered. |
| 256-byte no-score hits | Nonnegative small improvement expected; same unused work disappears, but hashing dominates the baseline and limits relative effect. |
| Tree-owned bytes | Exactly unchanged; no fields or allocations change. |

Require matched assembly to show the score-null branch preceding reverse/count-dependent mapping, and require process-scoped matched counters/profiles under the existing protocol. A leaf-symbol sample-share decrease alone is insufficient. The effect could be below the speed gate; no cycle saving is promised from static instruction observations.

## Correctness and portability

Mapping has no required side effects. Nevertheless, preserve both optional outputs independently: score-only, position-only and both-output callers must retain the same logical position and exact score. Preserve reversed leaf semantics, signed zero, finite scores, byte lengths, external-member handling, collisions and assertions. No mutation/index maintenance path changes. Original 57-test native/sanitizer runs and frozen fixture checks remain mandatory; position-producing add/rank/update callers must retain coverage. This is portable C, with no ISA or alignment assumptions. Compiler code layout and branch scheduling can create architecture-specific regressions even when semantics are unchanged.

## Falsification and decision limits

Reject this candidate if matched compilation still performs the conversion on null-output success, if any semantic or sanitizer check fails, if qualified primary improvement is below 2%, or if a required guard/memory loss exceeds 1%. Follow the existing three-block comparison, fresh seeds 29/43, profile validation and independent review gates; no retries or threshold changes. Intel performance remains unmeasured until separately qualified. Even an ARM pass is not a release-parity or integration claim.

## Historical novelty

EXP-006 replaced memchr with bounded inline tag scanners and remained PARK with long/single-lane concerns. This proposal retains memchr unchanged. The ARM mask follow-up changed packed decoding and was rejected on iterator guards. This proposal retains decoder implementation and iterator behavior unchanged and only avoids an unused lookup result. It is a narrower scalar hypothesis, not a renamed revival of either historical candidate.

## Consultation and TMA

Own availability discovery searched exposed tools for cpu-perf/library_status and returned no tools. Per the documented worker provision, this proposal consumes the controller's **shared** consultation in `CONSULTATION.md`: cpu-perf0.1.1, bundled list `deb5a0bac467`, library_status2/287 indexed, actual ask with source/fixture/counter context and source follow-up. Those calls are the controller's, not this proposer's. Source passages did not establish a microarchitectural explanation; the hypothesis above instead rests on the qualified standalone fleet experiment's measured hotspot and exact assembly. No claim is attributed to unread primary manuals.

| TMA category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The shared topdown-profiler capture is explicitly CPU-wide and lacks continuous exclusion evidence. Its exploratory slot numbers cannot identify the cost of these instructions or qualify an isolated process funnel. No candidate exists yet; no child category is established. See `BASELINE.md` for actual collector revision, command, raw capture and scope.
