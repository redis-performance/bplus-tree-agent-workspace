# AWS AMD morning results — 19 October 2026

**Source selection NONE. Campaign lease ACTIVE until 08:00 UTC (09:00 Lisbon); OSS coordinator restoration is pending. This is a results report, not release proof.** The last AMD workload completed06:07:18UTC; a subsequent read-only check found zero active owned jobs and zero btree-bench processes. Existing unrelated Redis/container processes were left intact. No new experiments are planned. Root is separately preparing a bounded observational idle-environment capture; it is not an A/A retry or a causal explanation for noise.

AMD Zen5 / EPYC9R45, Linux, Clang18.1.3, one serial thread pinnedCPU2. Builds, correctness, profiles and timing used owned bounded jobs under the campaign lease. No tree change was adopted. **Four completed AMD optimization populations: zero accepted, three rejected, one parked.** Replications, baseline requalification, diagnoses and reviews are separate and do not inflate this count. All twelve population patches remain available.

## Baselines and identity

Both five-size matrices use100/1K/10K/100K/1M members, all eight public operations,16-byte members,1M requested operations, seeds1–3 and six same-binary ABBA blocks. Each retained120 processes,960 operation rows and240 effects across40 cells; native/sanitizer validation passed.

| Identity | Qualification | Evidence |
|---|---|---|
| Original8fab511e, binarya398415f… | 9/40 qualified;11 short-window cells and20 additional noisy cells | [Root-published001 baseline](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/main/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/001-baseline) |
| Corrected13e459ff8 adapter, binary1ecbe6a4… | 11/40 qualified;11 short-window cells and18 additional noisy cells | [015 results and chart](015-adapter-requalification/RESULT.md) |

The corrected identity includes the separately reviewed `_Noreturn` adapter fix and isolated build support. Tree C/H and the public benchmark bytes are unchanged. Original8fab comparisons remain immutable. No original/corrected speed claim, timing pooling or claim that the adapter caused a performance difference is made. Charts show batch-average ns/op and observed ranges, not operation latency percentiles or confidence intervals.

## Completed AMD populations

| Population | Result and measured evidence | Retained patches |
|---|---|---|
| [002 lower-bound lazy member decode](002-lowerbound/implementation-selection.md) | REJECT.144 rows/36 effects; all three fail both2% primary gates. Best C medians−1.281%/−0.702% at100K/1M.1M controls were unqualified. | [A](002-lowerbound/variants/A/candidate.patch), [B](002-lowerbound/variants/B/candidate.patch), [C](002-lowerbound/variants/C/candidate.patch) |
| [004 builder-write metadata reuse](004-builder-write/implementation-selection.md) | REJECT.144 rows/36 effects; every variant slower. A+1.039%/+1.362%, B+1.250%/+1.745%, C+5.777%/+2.766% median. | [A](004-builder-write/variants/A/candidate.patch), [B](004-builder-write/variants/B/candidate.patch), [C](004-builder-write/variants/C/candidate.patch) |
| [005 full-chunk packed moves](005-full-chunks/implementation-selection.md) | REJECT.144 rows/36 effects; no block achieves2% improvement. Medians A−0.609%/+0.380%, B+0.265%/+0.403%, C−0.824%/+0.854%. | [A](005-full-chunks/variants/A/candidate.patch), [B](005-full-chunks/variants/B/candidate.patch), [C](005-full-chunks/variants/C/candidate.patch) |
| [008 SSE2 all-match tags](008-scan-tags/implementation-selection.md) | PARK.144 rows/36 effects; A and B pass exploratory every-block2% primaries, but1M A/A had failed and guards were unresolved. Medians A−5.255%/−4.360%, B−4.279%/−4.297%; C fails the1M block gate. No qualified winner. | [A](008-scan-tags/variants/A/candidate.patch), [B](008-scan-tags/variants/B/candidate.patch), [C](008-scan-tags/variants/C/candidate.patch) |

002/004/005 used three explicitly sequential proposal passes and three isolated implementation passes by one AMD author, with root independent review; they were not three independent agents.008 used actual independent AMD/Intel/ARM proposals and implementations, with root chair. All source/referee/compiler/fixture identities, raw rows, faults and losing variants are retained. Primary rejections stopped before unneeded guards/confirmation.

008 validation passed123 commands, original43 tests, scan/oracle/fallback coverage and eight detected faults. Its [matched diagnostic](008-scan-tags/mechanism/RESULT.md) reduces instructions/branches about12%, raises branch misses about5%, and improves scoped cycles under1%; it does not validate the exploratory4–5% elapsed magnitude. Root independently reviewed the raw comparison. PARK remains AMD-specific; later Intel rejection is separate evidence, not timing carried across hosts.

## Corrected-source replications and diagnoses

| Work | Outcome |
|---|---|
| [017 corrected scan baseline](017-corrected-scan/RESULT.md) | Fresh48-row5M-op A/A qualifies both sizes; scoped helper sampled-period31.277%/29.900%, with actual015 instruction mapping. No rescue of old8fab controls. |
| [019 exact Intel B replication on corrected AMD](019-corrected-B-replication/RESULT.md) | **REJECT advancement/NONE.**60 correctness commands pass;48 comparison rows retained. Medians−1.848286%/−1.785198%, but only2/6 blocks at each size meet the2% gate. No guards, candidate profile or confirmation after failure. [Exact losing patch](019-corrected-B-replication/candidate.patch). Root independently audited at a1210ec35. |
| [021 corrected rank/update survey](021-corrected-rank-update-profile/RESULT.md) |74 commands,12 scoped captures, all semantic/scope/hash checks pass.1M update SetId share7.921% is mostly structural moves; direct current-member reference search contributes only about0.283% total period. No saved-pointer hypothesis justified. Actual timing-binary mapping preserves seven differing memcpy call-displacement samples. |
| [029 corrected score-only iterator](029-corrected-iterator-plan/RESULT.md) | **Profile valid; controls fail100K; NONE.**51 commands, six captures/1,218 samples, known-work positive/disabled controls pass, reported losses zero.48 A/A rows:100K firstblock+2.430913% fails±1%;1M all six qualify(maxabs0.164846%). Minimum windows212.570/221.156ms. No retry or candidate. |

029's [profile](029-corrected-iterator-plan/PROFILE-RESULT.md) maps every sampled tree instruction exactly to actual015; caller-code differences/missing mappings remain explicit. This is instruction equivalence, not whole-function equivalence or causal cost attribution. ARM independently reconstructed all51 commands,1,218 samples,110 public hashes and48 A/A rows in [review58fec78b7](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/58fec78b7/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/023-amd-iterator-review/RAW-REVIEW.md). The [read-only diagnosis](029-corrected-iterator-plan/READONLY-DIAGNOSIS.md) preserves score-only versus full-member output contracts and identifies overlap with historical EXP002/004/005, not a new supported hypothesis.

Earlier [003 packed-move census](003-packed-move/README.md) supplied profile/census evidence for004/005. [006 query-length](006-query-length/DECISION.md) selected NONE because samples concentrated at the mandatory first key header, not the removable second dispatch. [007 inner-child](007-inner-child/DECISION.md) selected NONE: limited scan-loop headroom and no causal layout evidence. [009 delete-offset](009-delete/DECISION.md) received three actual independent proposals but root chair selected NONE before implementation:1M noise up to4.682% versus approximate5.496% loop attribution, and only seven100K events. No retries or hidden candidate populations followed.

## Independent work for the other hosts

These results belong to their measured host/source. They are not additional AMD populations.

| Work | Evidence and outcome |
|---|---|
| Intel original B independent primary confirmation | [012](012-intel-confirmation/RESULT.md): explicit idle handoff,48 held-out A/A then48 comparison rows, seeds201–203 twice. All12 primary blocks passed; remaining guards still required. Runner returned idle. |
| Intel original guards/profile/focused guards | [010 source/referee review](010-intel-scan-review/), [013 guard audit](013-intel-original-guard-audit/RESULT.md), [016 profile review](016-intel-profile-review/), [022 focused audit](022-intel-focused-guard-review/RESULT.md). Original guards:56/57 qualified pass, one mixed and23 other gaps. Focused:22 qualified cells pass all six comparisons,14 noisy cells retained. Profile supports SSE2 mechanism, not precise elapsed magnitude. |
| Intel supplemental B guard rejection | [026 independent audit](026-intel-supplement-review/REVIEW.md):2,124 processes including calibration,360 effects,30 cells. Qualified trim/319-byte/signed-zero guard has all six regressions>1%, median+4.930768%: exact old-adapter B REJECT. Eight other qualified cells pass, one mixed and20 noisy remain. No fallback variant or retry. |
| ARM proposals and C implementation | [011](011-arm-scan-proposal/), [018](018-arm-corrected-scan-proposal/), [020 C patch](020-arm-corrected-implementation-C/candidate.patch). Original ARM control failure stopped implementation. Corrected ARM had actual independent authors; AMD C was sealed without peer reads, then validated by ARM. |
| ARM corrected NEON raw/static/profile reviews | [023](023-arm-neon-validation-review/DISCOVERY-REVIEW.md), [025](025-arm-codegen-review/), [027](027-arm-profile-review/).145 validation commands pass;144 comparison rows show all three slower. B medians+78.161%/+55.342%; all rejected.35 predicate-reconstruction instructions corroborated statically; matched post-filtered profile supports material17% predicate share but not enough inferred recovery to beat baseline. AMD C authorship disclosed; root independently reviewed source. |
| ARM confirmation and later fold proposal | [024](024-arm-independent-confirmation/DECISION.md): held-out confirmation protocol sealed but ineligible/unexecuted because no discovery survivor. [028 independent proposal](028-arm-fold-proposal/proposal-amd.md): NONE; no implementation, no new measurements. |
| Release auditor review | [014](014-release-auditor-review/): reviewed root's nested-cgroup lookup correction and fail-closed semantics. This code review is not proof that08:00 restoration has occurred. |

## Remaining gates and handoff

There is no implementation eligible for adoption. Rejected candidates have final failed gates; they are not awaiting permission to repeat. AMD008 remains exploratory/PARK with failed original1M A/A, missing qualified guards, independent confirmation and unresolved elapsed/profile magnitude. Corrected019 and029 failed their own fixed gates; no retuning or controls from another identity can replace them. Any genuinely new future hypothesis needs fresh evidence, the required population process, correctness/benchmark/profile validation, qualified guards, independent confirmation and adversarial review before acceptance.

Raw timing rows and validation failures are public. Large raw perf files remain local and on the owned runner with hashes; full sample text, commands, summaries and source-linked assembly are published. Redacted/normalized public copies record raw/public checksums. No private connection details, credentials or customer data are published. Initial external CLI startup failures and stopped supervisor reports remain under `round-01-controller-blocked`/RUNTIME-SUMMARY; native work did not change permissions. The old supervisor's stopped status is not the current lease state.

Native work used the inherited Codex agent; exact serving model, native token usage and USD cost are unknown. Old CLI usage fields describe only that failed launch and are not native campaign totals. The benchmark parity checklist was consulted as a reference for one standalone review, not a completed stronger-model/memtier/server panel.

README, activity, status and immutable evidence commits are updated. Root owns the remaining observational capture and08:00 release/restoration verification. **Lease ACTIVE, restoration pending; source NONE.**
