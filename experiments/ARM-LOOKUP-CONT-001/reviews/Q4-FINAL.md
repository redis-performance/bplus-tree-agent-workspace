# Independent Q4 final audit — PARK / NONE

**PARK; selected source NONE.** The first Q4 cohort, ARM GCC15/LTO seed43, completes all72 baseline A/A rows but fails hit block0 at **+1.0198832566%**, beyond the frozen absolute1% limit. Seventeen other blocks pass. The collector correctly stops before target29, target17 and native17. No candidate executes. H2R1 and the proposed H8 screen are not admitted because Q4's qualification prerequisite failed. Original [H2 remains PARK/NONE](H2-FINAL.md).

This review independently reconstructed saved rows, commands, launch/child records, isolation captures, executable/source identities and publication checksums. The reviewer previously reviewed Q4's collector/cleanup/deployment and authored the Intel profile parser and H2 audits, but implemented neither Q4 collector/cleanup nor H2-B. No fleet query, workload execution, new measurement, build, source edit or publication occurred. Only this review and the H2R1 prerequisite-status update were written. Detailed participant provenance remains private; exact model/token/cost accounting is unknown.

## The failed control is retained without a waiver

The [raw A/A rows](../Q4-results/Q4-lto-43/aa.jsonl) use the same baseline executable on both A and B labels. Each hit process uses seed43,250,000 sweeps and125,000,000 reported lookups. The frozen binary supplies the unchanged1,000-sweep untimed warmup.

| Slot | Timed-loop elapsed ns | Whole-child user+system CPU s | Voluntary / involuntary switches | Minor / major faults | Owned bytes |
|---|---:|---:|---:|---:|---:|
| A0 | 3,768,919,926 | 3.785421 | 1 /29 | 332 /0 | 14,272 |
| B1, baseline again | 3,866,293,920 | 3.883117 | 1 /27 | 330 /0 | 14,272 |
| B2, baseline again | 3,764,814,306 | 3.781056 | 1 /25 | 333 /0 | 14,272 |
| A3 | 3,785,145,650 | 3.801633 | 1 /27 | 334 /0 | 14,272 |

A elapsed sum is7,554,065,576ns; B sum is7,631,108,226ns. The recomputed contrast is `100 × (B/A − 1) = +1.0198832565707638%`. The collector uses the exact integer test `100 × abs(B−A) <= A`, so this is not a floating-point tolerance decision. The excess above the1% bound is0.0198832566percentage points, or0.750997ms in B's mean beyond the allowed mean for this block. Its narrow margin does not authorize rounding to a pass, dropping B1, changing the statistic, widening the bound or retrying unchanged.

Every row lasts2385.362127–6720.835707ms, comfortably exceeding250ms. Within each case, all12 processes report identical owned bytes: hit/score/miss14,272; inline256146,656; external384217,600; update14,432. These are the registered tree-owned endpoints, not transient peak allocation or process RSS. Duration, model and memory checks pass; the failed elapsed contrast alone parks the cohort.

| Case | Three-block A/A elapsed range % | Result |
|---|---:|---|
| Hit | −0.216430…+1.019883 | Block0 fails; blocks1/2 pass |
| Score | −0.166732…+0.005938 | Pass |
| Miss | −0.227072…+0.006828 | Pass |
| Inline256 | −0.015144…+0.086301 | Pass |
| External384 | −0.051673…+0.093500 | Pass |
| Update | −0.304927…+0.035556 | Pass |

Every independently reconstructed block exactly equals the saved [analysis](../Q4-results/Q4-lto-43/analysis.json). The [phase result](../Q4-results/Q4-lto-43/result.json) correctly says PARK, complete72rows, candidate_executed=false and source_adoption=false. The [overall result](../Q4-results/Q4-profiler-off/result.json) stops at `Q4-lto-43` and lists only that completed phase. Later cohort directories are absent; unrun cohorts are not passes.

## Process and isolation evidence

The record contains78 unique baseline commands: six verification processes followed by72 measurement processes. Every command joins one pre-launch record, one child-start record, exact stdout/stderr and a successful return. All launches use the original target baseline, CPU2, seed43 and fixed case counts. No candidate path appears. Measurement order is the complete six-case × three-block × four-slot ABBA grid, with no duplicates, missing rows or overlapping workload intervals. All six verification outputs pass their case/seed/500-member model. All measurement outputs match independently derived operation, hit and score-sum expectations; measurement stderr is empty.

Every child has the enforced-and-verified preexec CPU2 guarantee and an available parent observation of affinity `[2]`. No unavailable-observation exception was needed in this capture. All78 whole-child diagnostic records contain finite nonnegative user/system CPU and fault/switch counters; fault/switch counts are integers. These observations match their child-start and command records.

I reconstructed **156 pre/post isolation snapshots** and **936 operational commands**: two timers, two cleanup ExecStart queries, profiler state and Docker state at each boundary. Every command succeeds with empty stderr. Preflight commands finish before their child launches; postflight commands begin after that child finishes. Each snapshot records controllerCPU0, the exact saved coordinator identity in stopped state, online CPU2 with sibling list2, no detected profiler processes and a passing boundary check. Each raw service capture is inactive/dead with MainPID0 and unchanged empty CPUAffinity/AllowedCPUs policy; each Docker capture is empty.

Both reviewed v2 timers remain active with exact recorded realtime/monotonic schedules and reviewed service targets. Their raw ExecStart hashes match the admitted cleanup commands. Every boundary remains more than300seconds before the timer fire and lease deadline. The reviewed [deployment](Q4-DEPLOYMENT.md) retains the corrected209.780-second separation and independent recovery budgets; the rejected earlier overlapping schedule remains historical evidence and was not used for Q4.

These are complete **boundary checks**, not continuous proof that no unrelated daemon, interrupt, frequency change or scheduling event could affect CPU2. No new system-wide exclusion or causal attribution follows from empty profiler/Docker results. This review does not claim that restoration has already executed or that the runner has been released; actual cleanup and its final restoration proof close separately.

## Identity and publication joins

The metadata, admitted records, actual saved bytes and launch arguments agree on:

- Upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`; baseline C SHA256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`.
- Target baseline ELF `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`.
- Collector `531bbabc2b50e26737a0be44773e7d195fa2576ba149e75bdf63a1a5698da743`.
- Isolation record `1b22ec08fa256b91e341c2628f4baef9c6d7ac055376abeda4a995057e827674` and independent approval record `ca9a80f17fa708df9db3d2e2cbb54b071d102c0e6ddb2c29f073e06298beee26`.

Every source/header/compatibility/vendor/referee pin matches the frozen local bytes. The reviewed collector rechecks all identity pins and the immutable lease before and after each child; retained operational captures independently substantiate the recorded boundary states. Original raw AA SHA256 is `842ef6d09892ee1c4a41dc84bc0ae6f097371884a8ed9dbedb4ad3dd8545ce68`; command-log SHA256 is `631630638bc80a15ee4a43b295460632ad7c707f97e042576daace4308fbe705`; analysis SHA256 is `1af4095b59452850630a0c4531dc45c55f00211614cba94e238a928a525e5363`.

All165 original/published file pairs and all2029 retained-private operational hashes in [PUBLICATION.json](../Q4-results/PUBLICATION.json) independently match. Public commands normalize the owned run root; original and rendered hashes remain distinct. Operational service/process evidence stays private. Neither sanitization nor publication substitutes a modified measurement row.

## Archive chronology: evidence and limitation

The first verification command starts04:03:57.843924UTC. The last workload finishes04:09:12.766799UTC and its final operational command finishes04:09:12.822253UTC. The controller supplied an explicit saved execution-owner attestation: a bounded progress query observed MainPID0, exit status0 and inactive unit state; a subsequent fetch command independently asserted MainPID0 with a checked return before invoking the archive operation. The clock read after completed fetch was04:10:57UTC. The owner reports no earlier Q4 archive invocation, only bounded progress queries during the run.

The fetch precondition's stdout and controller start timestamp were **not separately persisted as a timestamped remote capture**. Therefore no-transfer-overlap is supported here by the execution-owner attestation/tool-call chronology, not independently proved from archive mtimes or an invented fetch timestamp. This limitation is retained rather than presenting the saved workload timestamps as complete transfer telemetry. It does not turn the failed control into an acceptable result.

## What the CPU diagnostics do and do not show

The collector brackets only the taskset/baseline child with `RUSAGE_CHILDREN`; its operational audit subprocesses finish outside that bracket. User+system CPU therefore covers setup, verification/warmup, the measured loop, final validation and teardown. It is not timed-loop CPU time, a hardware cycle count, an instruction count or an independently qualified acceptance metric.

The failed block's whole-child CPU ABBA contrast is **+1.0164551353%**, alongside the timed-loop wall contrast+1.0198832566%. The longer B1 row also has higher accounted whole-child CPU. The four hit processes each have one voluntary switch,25–29 involuntary switches and zero major faults. Across all72 measurements there are no major faults,330–539 minor faults,1–2 voluntary switches and15–48 involuntary switches per child.

Those are bounded observations, not a diagnosis. CPU time covers a different interval, switch counts omit the duration and placement of interruptions, and fault counts do not identify latency. The controller's launch-to-reap wall interval also includes launch and wait/polling overhead; subtracting child CPU from it would not yield exact timed-loop off-CPU time. No scheduler trace, frequency trace or PMU capture exists here to identify a cause. In particular, do not infer a frequency/cache/branch problem, prove absence of descheduling, or retroactively assign a cause to original H2's different failed miss block.

The observed profiler-off condition did not qualify this attempt. This does not prove either that Parca caused the original failure or that removing it can never affect variability. Neither the close CPU contrast nor the17 passing blocks can waive the registered failed wall-time control.

| Qualified ARM pipeline-slot category | Q4 baseline | Candidate |
|---|---|---|
| Frontend_Bound | Unavailable | Not run |
| Bad_Speculation | Unavailable | Not run |
| Backend_Bound | Unavailable | Not run |
| Retiring | Unavailable | Not run |

All child categories remain unavailable. Q4 collected no TMA or candidate profile; resource-usage counters cannot fill that gap. Own cpu-perf tool discovery found no callable endpoint. The controller's actual shared Q4 consultation had limited source coverage and no causal proof; no new consultation is claimed by this reviewer.

## Closure and accounting

Q4 closes as **one ARM qualification attempt, PARK**, not four attempts for its planned cohorts and not a candidate population. The resulting ledger is **47 completed =25 PARK+22 REJECT+0 approved =35 ARM+6 Intel+6 AMD =29 populations+5 replications+13 qualifications**. This is the prior46-attempt ledger plus one parked ARM qualification; its arithmetic agrees in every classification. H8 screening and H2R1 were never admitted and add no completed attempt or accepted source.

The [H2R1 protocol review](H2R1-PROTOCOL-REVIEW.md) is now NOT ADMITTED because its explicit Q4 prerequisite failed. Preserve its preparation and this failed attempt. No unchanged retry, substituted seed, adjusted count, relaxed threshold, dropped first block or candidate execution follows. Any future investigation needs a distinct justified preregistration and independent admission; no result in this review authorizes it. Historical root source and every frozen extraction remain unchanged. Original H2 stays PARK/NONE.
