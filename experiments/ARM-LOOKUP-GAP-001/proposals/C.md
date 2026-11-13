# Proposal C: defer logical-position work for membership-only hits

Independent proposer C, 2026-11-13. Backend: Codex, inherited session model; exact model identifier, token usage and monetary cost unknown. No other proposal was read. No code was changed, benchmark launched, or fleet accessed. This proposal uses source/referee `4876d21ce62fdf9306572b690c891d2d5ed0e04d`, upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`.

## Decision

Propose one small scalar hypothesis: **after a successful byte comparison, computing the logical score position only when a caller requests a score or position removes avoidable successful-lookup work and improves the qualified no-score primary by at least 2%, without a greater-than-1% loss on any registered guard or tree-owned memory.**

Target only `zbtScoreLeafFindMember()` in `current/src/zset_btree.c`, at the successful-match block around lines 1329–1336. Leave hash computation, table probing, leaf-tag search, packed-record decoding, length/byte comparison, data layout and allocator unchanged. In source terms, the physical-to-logical mapping belongs inside the `score || position` condition. This is not a proposal to return before equality has been established.

## Evidence and limits

The registered A/A cohort qualifies all 12 blocks and all four cases. Primary median is 29.867 ns/lookup; its three block effects are −0.151%, −0.135% and −0.594%. Primary sampled user cycles concentrate in the leaf helper (41.91%) and raw lookup (21.91%). These observations identify a useful target, not removable-cycle percentages.

The exact baseline [assembly](../baseline/lookup-assembly.txt) supplies the more specific evidence. In `zbtScoreLeafFindMember.constprop.0`, the successful `memcmp` result at 0x35c8 is followed by a score-pointer load. The block at 0x35d0–0x35e4 then loads the saved leaf count and reverse flag, subtracts and selects the logical position. Only at 0x35e8 does `cbz x7` skip score decoding for a null score pointer. This specialization already has a null position output, yet performs the logical-position mapping for the no-score primary. The source computes `logical` unconditionally before its two optional stores.

The three whole-process perf-stat captures have 100% reported scheduling and nearly identical retired instruction totals. They include startup/warmup/teardown; they cannot price this individual block. The saved frame/register state may change when the source control dependence changes. A speedup is therefore a falsifiable prediction, not a static-instruction-count conclusion.

There is no qualified cache-miss or memory-latency evidence justifying a leaf-layout or allocation change. The 14,272-byte target footprint and the larger 256-byte-member control do not by themselves identify a cache bottleneck. I select **NONE for allocation/layout changes** in this first round.

## Expected workload behavior

| Case | Prediction | Reason and falsifier |
|---|---|---|
| Hit, no score | At least 2% faster | Avoid mapping on every verified hit; below 2% after qualified comparison fails the useful-gain hypothesis. |
| Hit, score | Within ±1% | Mapping remains required. A new branch or worse layout can regress this path; any demonstrated >1% loss rejects. |
| Missing | Within ±1% | No successful-match block is reached. A significant change suggests code-layout/register effects, not the proposed direct mechanism. |
| Hit, 256-byte member | Neutral to modestly faster | Also requests no score, but hashing dominates its baseline profile. A >1% loss rejects; an outsized win requires separate explanation. |
| Tree-owned bytes | Identical | No data-format/allocation mutation is proposed. Any change invalidates the implementation. |

The primary speed prediction is deliberately narrow: GCC13.3 on the qualified Neoverse V2 fixture. No Intel benefit or command-level release parity follows. An Intel regression check is still required before broader adoption.

## Correctness and portability risks

Preserve the exact equality test, collision suffix search, external-record hash check, optional output semantics and return value. Score and position callers must still receive the correct logical position for forward and reversed leaves. Keep finite scores and signed zero unchanged. Insertion/update/rank callers can request position without score and must not be mistaken for membership-only callers.

The change needs no ISA-specific primitive and changes no alignment, aliasing, endianness or record bounds. Its main risk is compiler control-flow/code-layout behavior, including an extra guard on score-returning paths. Do not weaken an assertion or specialize on fixture member names, lengths, leaf count or score range.

## Validation and falsification

Use the unchanged referee and original correctness/sanitizer gates, with targeted checks for all four output combinations on a reversed leaf if the current upstream coverage does not establish them. Require exact equality and collision cases before inspecting speed. Preserve the three independent implementation alternatives and losing patches.

Inspect each exact ARM binary: the no-score successful return must actually bypass the logical-position block. If GCC hoists the work anyway, the proposed mechanism has not been implemented; fewer source statements do not establish a result. Then run registered serial ABBA on all four cases, check ≥2% primary/no >1% guard or memory regression, and use held-out seeds 29/43 for fresh confirmation. Matched profiles should show the intended executed-work reduction; absence of that reduction, or a timing-only win, keeps the result parked.

## Novelty

EXP-006 changed the leaf-tag scanner and had unresolved single-lane/long-key behavior. The ARM mask follow-up changed score-decoder behavior and was rejected on iterator guards. This proposal leaves both scanner and decoder untouched and instead avoids producing a logical position when neither output consumes it. It neither revives those historical candidates nor treats their primary gains as support. General helper inlining is a different hypothesis; do not combine it with this change in the first comparison.

## Consultation and TMA

My own tool discovery filtered available tools for cpu-perf/library_status and returned no directly exposed tools. Under the shared-worker allowance in `docs/PERFORMANCE-MCP.md`, I consumed the controller's actual consultation in [CONSULTATION.md](../CONSULTATION.md): cpu-perf0.1.1, bundled list deb5a0bac467, library_status/ask/read_source. I did not perform or claim those calls myself. Its retrieved coverage did not establish a resource-level explanation. The proposal rests on the qualified fixture and exact baseline source/assembly, not an unread external source.

| TMA category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The controller's topdown-profiler0.2.3 capture explicitly selects CPU2 system-wide; continuous exclusion of other CPU2 activity was not proven. Its genuine slot-denominated output stays exploratory, with no child categories. No stall-cycle or sample percentage is substituted for TMA. Use [BASELINE.md](../BASELINE.md) and [collector identity](../baseline/topdown-collector.json) for actual command, binary, CPU and collection limits. Note that metadata identifies perf version6.17.13 despite the executable residing under a 6.14-labelled tools directory.
