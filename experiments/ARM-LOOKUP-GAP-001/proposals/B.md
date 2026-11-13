# Proposal B: defer unused logical-position work

Decision: propose one bounded scalar experiment, not adoption. On successful membership-only lookup, compute the leaf's logical position only when a score or position output is requested. Keep hashing, index probing, tag search, byte comparison, and helper boundaries unchanged.

## Frozen evidence

Independent proposer B, Codex backend; exact model, token and currency costs unknown. Read only the common source/evidence/history, not proposals A/C. No build, measurement or runner access performed by this proposer. Baseline/referee commit `4876d21ce62fdf9306572b690c891d2d5ed0e04d`; upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`; baseline binary SHA256 `d54311ffae324cf623a000f1c026f377c3657f5810c76cd1b2284645b9411431`.

The [qualified A/A analysis](../baseline/aa-analysis.json) passes all twelve blocks for four cases. [Profile](../baseline/report-hit.stdout) puts 41.91% of whole-process user-cycle sample weight in `zbtScoreLeafFindMember.constprop.0` and 21.91% in raw lookup. This identifies a place to inspect; it does not assign that entire share to output work.

[Exact assembly](../baseline/lookup-assembly.txt) supplies the narrower evidence. After successful `memcmp`, addresses `35d0`–`35e4` reload the count, load the reversed flag, subtract and select the logical position. Only at `35e8` does `cbz x7` test the score pointer. The compiler has specialized away the position output for this clone, but the membership-only caller still executes this calculation. The source helper `zbtScoreLeafPhysicalPos` is pure arithmetic with no assertion or side effect. The existing raw-lookup entry point already inlines the index helpers, so simply inlining those again is not a new hypothesis.

## Hypothesis and exact change

Hypothesis: avoiding unused logical-position calculation after a verified hit will reduce primary no-score lookup time by at least the registered 2%, without a demonstrated >1% guard or memory loss.

Target only the successful-match output block in `zbtScoreLeafFindMember`, around current-source lines1330–1336. Guard the computation and its existing writes with `if (score || position)`, or an equivalent early success return when both outputs are null. Do not change the shared `zbtScoreLeafPhysicalPos` implementation. Do not force helper inlining, replace `memchr`, alter tag masks, specialize member lengths, cache hashes, or change index layout in this experiment.

The expected mechanism is removed executed work on the no-output hit path, not a claim about a specific CPU execution resource. The magnitude is uncertain: several instructions and a flag load may be too little to clear 2%, and code layout may offset them. The proposed mechanism must be visible in the matched binary before a timing effect is attributed to it.

| Case | Prediction | Reason |
|---|---|---|
| Short hit, no score | Improvement; ≥2% is the falsifiable objective | Logical position is unused |
| Short hit, score | Approximately neutral | Original position and score work is still required |
| Missing | Approximately neutral | Match-success block is never reached |
| 256-byte hit, no score | Same saving in work, smaller relative effect | Hashing/comparison dominate more of this control |
| Tree-owned memory | Identical | No allocation or layout change |

## Correctness, rejection and novelty

Preserve raw byte equality and lengths, external-member hash checks, score bits and signed zero, reversed-leaf position semantics, index migration and every requested output. The null/null path must return only after a full verified match; checking the output pointers before validating membership would be wrong. Exercise score-only, position-only, both-output and neither-output call paths, including reversed leaves. Existing upstream tests remain the referee and cannot be weakened.

First falsifier: matched ARM assembly still performs the count/reversed/position work for null/null hits. Second: registered primary effect fails ≥2%, or score/missing/long guards demonstrate >1% regression, correctness differs, or memory changes. Even a timing win remains parked if assembly/counters fail to support the proposed mechanism. Follow three-implementation selection, same-session ABBA, held-out seeds and independent review; do not adapt cases after observing results.

This differs from historical EXP-006, which replaced the leaf `memchr` scanner with byte/SWAR/unrolled scans, and the rejected ARM mask follow-up, which changed shared decoder behavior and lost iterator guards. This proposal preserves both scanner and decoder implementations and changes only whether an unused result is computed. Historical results provide no acceptance evidence for this change.

## Consultation and TMA limits

2026-11-13T22:31–22:33Z: own available-tool discovery found no directly exposed cpu-perf/library_status tool. Consumed root's explicitly shared stdio `library_status`, initial `ask` and source-reading record in [CONSULTATION](../CONSULTATION.md), plus its completed post-profile reconsultation stored outside public evidence. These were root calls, not this proposer's calls. Initial coverage was2/287 sources; reconsultation3/287/158 passages. Retrieved snippets do not establish this proposed mechanism; source and exact assembly do. No external benchmark number qualifies this host.

| TMA category | Qualified baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

The [baseline classification](../BASELINE.md#tma-classification) remains unavailable for a qualified process classification because actual collection is CPU-wide without continuous exclusion evidence. No children are qualified. Exploratory CPU2 slot percentages neither prove nor disprove this output-work hypothesis; no stall/sample percentage is converted into TMA.
