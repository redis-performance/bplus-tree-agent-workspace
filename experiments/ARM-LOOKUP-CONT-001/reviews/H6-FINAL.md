# Independent H6 final rejection audit

**REJECT A, B and C; source selection NONE.** Every native ARM variant misses the registered≥2% primary improvement in every block. A also fails update guards; B's first score block exceeds1% and remains in the evidence. No H6 Intel, target-LTO or descriptor-guard timing, fresh confirmation or source adoption follows this failed primary screen.

I authored [H6-INDEPENDENT.md](H6-INDEPENDENT.md), the earlier source/codegen screen, but did not implement any H6 candidate or author its correctness/guard harness. This overlap is disclosed: the current work independently reconstructs the measured decision rather than supplying a second independent source review. The earlier static PASS was explicitly not performance acceptance. Exact model, tokens and cost are unknown. No fleet access, new measurements, source/collector edits, commits or pushes occurred; only final review documents were written.

## Complete evidence reconstruction

Read private `build/arm-cont-private/fleet/H6-native`:216 rows,54 complete ABBA blocks, exactly three variants × six cases × three blocks × four slots. Every row joins one successful saved command and matching JSON stdout with empty stderr. Verified CPU2 launcher, native cohort, seed17, fixed scale1 counts, exact baseline/candidate path and ELF hash, ABBA labels/order, operations/hits/score sums and owned-byte joins. Commands are serial within the phase. All six saved fixture verifications succeed for each candidate.

All rows exceed250ms; the shortest is493.057ms. Owned bytes match exactly within every baseline/candidate block and reproduce per case/binary. Recomputed effects and eligibility match every saved analysis entry. No score block, initial observation or other row was discarded or retried.

Independently reconstructed the original native control grid from `fleet/native-requalification`:72 rows/18 blocks, A/A−0.397978…+0.264268%, shortest495.198ms. Every block passes±1%, with exact stdout/command/model/memory joins. Its baseline ELF is the same H6 control binary, SHA256 `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf`. These existing qualified controls are not a new qualification attempt; earlier failed cohorts remain preserved.

Baseline upstream is `ee8e7f70152404649ac947157fd662d11b4a00d5`, C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. I rehashed all three isolated final sources and all three saved native ELFs, matching timing metadata and row identities. Nine frozen referee files per worktree, including lookup/build/qualification, header, compatibility and vendor sources, remain byte-identical to the root referee.

| Variant | Source SHA256 | Native ELF SHA256 |
|---|---|---|
| A | `ffd548a1fba1db452e98fbe1dd3902b2ba34f44af797edeaed9976783444e744` | `35e580eeb9c13804abc54db235e11d256a09c48dcc39fd51557169694a764449` |
| B | `5f6bfd216350dceee6ed486d5fc6e1535162a64c037c3ceee746ceae9b0813ae` | `770aae745abc3ff95820cbac01d54837d8591977f97637a6b68740d4f40c5bfb` |
| C | `bf2cbbe66b36d178692ba214fd192af1b5dc6b1c67f1619e2d782c839b2da825` | `3af61e2ac8203e22a7247ed34b4cb3eaeea057efdd73bfa97d5a109867198b7d` |

## Gates and retained failures

Effects are100×(mean candidate elapsed / mean baseline elapsed−1), with negative favoring the candidate. Primary acceptance requires≤−2% in **every** hit block, all guards≤+1% in every block, owned-memory≤+1%, and qualified duration/control gates.

| Variant | Hit blocks0/1/2 % | Additional failed guards | Decision |
|---|---|---|---|
| A | +0.838433 / +0.819504 / +0.874595 | Update +1.336631 / +1.747632 / +1.885253% | REJECT |
| B | −0.215957 / +0.276701 / −0.124205 | Score block0 **+2.656275%**; blocks1/2−0.099324/+0.078217% retained | REJECT |
| C | +1.625850 / +1.294770 / +1.048972 | None needed; all original non-primary guards≤1% | REJECT |

B's mixed-sign small hit effects are not a2% gain. Its first score block cannot be averaged away by the following two; the review does not claim a stable causal score regression from that one block. The primary failure alone already rejects B, independently of that guard interpretation. A's update regression repeats in all three blocks. C's largest update block+0.983479% remains a pass under the unchanged1% threshold; it is neither rounded into a failure nor used to rescue the failed primary.

All original case ranges are retained for completeness:

| Case delta range % | A | B | C |
|---|---:|---:|---:|
| Score | +0.586…+0.839 | −0.099…+2.656 | +0.266…+0.664 |
| Miss | −0.413…+0.108 | −0.192…+0.358 | −0.751…+0.218 |
| Long | −0.081…−0.032 | +0.131…+0.163 | −0.036…+0.061 |
| External | −0.086…+0.065 | +0.080…+0.166 | +0.184…+0.330 |
| Update | +1.337…+1.885 | −0.607…+0.077 | +0.369…+0.983 |

The raw `comparison.jsonl` SHA256 is `5a7e0239900ca452337adeecd6e2741147a4374d35abd53517684642fe3427de`; metadata `a39d11290077a2a5de172ca43c178bb835d6a89c92eea250e3c4f29de0539621`; command log `96c6c10230f0ddcff1314420ee0bf73160ff1884087d30e828c7edfa4f2dc890`. All216 observations and losing patches remain preserved.

## Scope and stopping rule

The previous review verified actual native/LTO hinted branches bypassed record headers, exact ELF bytes,128-byte leaf frames, masked offset consumers and physical external-short fallback. Those static/correctness facts remain valid. They do not imply an end-to-end benefit or identify the cause of the measured result. This experiment does not justify another spelling of the same descriptor mechanism or an unchanged timing retry.

Saved ARM LTO and Intel H6 native/LTO build directories have no comparison rows. They remain unused build/codegen evidence, not measured cohorts or missing comparisons that must now be filled. The descriptor-guard harness and its correctness review remain preparatory artifacts; no descriptor-guard timing qualifies an H6 candidate. Stopping before those gates is correct after all variants fail the primary screen.

| Qualified total-slot category | Matched ARM baseline | H6-A | H6-B | H6-C |
|---|---|---|---|---|
| Frontend_Bound | unavailable | unavailable | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable | unavailable | unavailable |
| Retiring | unavailable | unavailable | unavailable | unavailable |

No qualified matched H6 pipeline captures or children were collected. Assembly, elapsed-time ratios and unrelated Intel baseline fractions cannot fill them. No microarchitectural cause is asserted.

## Population accounting and consultation

H6 adds **one rejected ARM population**, one completed attempt and no acceptance. Three implementations, unused target/Intel builds, correctness matrices and guard preparation do not add populations, replications or qualifications. Together with [H4's one closure](H4-FINAL.md), the prior42/23PARK/19REJECT ledger becomes **44 attempts /23PARK /21REJECT /0 approved; ARM32 /Intel6 /AMD6;27 populations /5 replications /12 qualifications**. Each sum independently equals44. H2/H5 remain active and excluded; the earlier AMD qualification is still counted once across both compilers.

Own fresh tool discovery found no callable cpu-perf endpoint. The controller's descriptor-specific consultation is shared evidence documented in [H6-selection.md](../H6-selection.md) and the prior review; it supplied no supporting passage proving a gain or explaining this rejection. No consultation by another agent is claimed as this reviewer's call.
