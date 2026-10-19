# Independent clock-attribution review A

All three failed 1M wall controls also exceed ±1% when reconstructed from recorded thread CPU time. The recorded wall-minus-thread residual alone does not account for those contrasts. This is a failed diagnostic predicate, **not a formal causal falsification of descheduling alone**: the clocks cover different brackets and their differential accounting error has no independently established bound. EXP-009 remains PARK/source NONE under its original wall-clock gate.

Authorship: `/root/followup_proposal_a`, inherited Codex/GPT-6 family; exact serving model, tokens and currency cost unknown. Independent offline clock analysis; I previously authored the EXP-009 mapper and raw audit, not its driver or original A/A statistics. No peer new reports were read. No workload, build, profile, source edit, rerun or Git write occurred. This is not an optimization population or independent timing confirmation.

## Reconstruction and exact decomposition

The new script reads all 48 raw CSVs, verifies all 96 public stream hashes against the journal and public manifest, checks all five diagnostic input pins, and reconstructs all twelve ABBA blocks independently. It checks the fixed count/seed/size/position schedule, identical commands, successful cleanup, serial UTC ordering, nonempty valid clocks and unchanged checksum/tree-byte fingerprints within each block. It imports neither the driver nor another analyzer. The original summary is hash-checked as a pinned artifact, never used for statistics. Script and raw/source hashes are in A.json. Run from the canonical worktree:

`PYTHONDONTWRITEBYTECODE=1 python3 experiments/M6-METROLOGY-001/analyze-a.py`

The offline pass completed successfully under a 180-second Python alarm. The script writes A.json exclusively; preserve/move an existing own result before reproducing it. Blocks below are zero-based, as in the frozen schedule. For each clock, A sums positions 0 and 3 and B sums positions 1 and 2. Let ΔW = B_W−A_W, ΔT = B_T−A_T, and ΔR = ΔW−ΔT. Integer arithmetic gives **ΔW/A_W = ΔT/A_W + ΔR/A_W** exactly. Thus the two contribution columns use the same wall denominator; the ordinary thread percentage uses A_T. All integer sums/deltas and all 48 observations remain in A.json.

| Size | Block / seed | Wall % | Thread % | Thread contribution (wall pp) | Residual contribution (wall pp) |
|---|---|---:|---:|---:|---:|
| 100K | 0 / 1 | +0.066263 | +0.062961 | +0.062887 | +0.003377 |
| 1M | 0 / 1 | −0.614488 | −0.619500 | −0.618588 | +0.004099 |
| 1M | 1 / 2 | −0.593165 | −0.596221 | −0.595336 | +0.002172 |
| 100K | 1 / 2 | +0.220646 | +0.237541 | +0.237227 | −0.016582 |
| 100K | 2 / 3 | −0.016887 | +0.004118 | +0.004112 | −0.020999 |
| 1M | 2 / 3 | **−1.414059** | **−1.401384** | −1.399288 | −0.014772 |
| 1M | 3 / 1 | +0.841157 | +0.843931 | +0.842655 | −0.001498 |
| 100K | 3 / 1 | +0.299162 | +0.288096 | +0.287768 | +0.011394 |
| 100K | 4 / 2 | +0.147094 | +0.146667 | +0.146469 | +0.000625 |
| 1M | 4 / 2 | **+1.036273** | **+1.008640** | +1.007295 | +0.028978 |
| 1M | 5 / 3 | **+2.567325** | **+2.542454** | +2.539296 | +0.028029 |
| 100K | 5 / 3 | −0.636548 | −0.629651 | −0.628808 | −0.007740 |

Both clock diagnostics therefore yield 100K 6/6 within ±1%, 1M 3/6. No control or observation was removed. For failed 1M blocks 2/4/5, residual contrasts are −183,208 / +354,667 / +342,167 ns, respectively: only 1.044635% / 2.796397% / 1.091755% of their signed wall contrasts. Assigning the entire recorded differential residual to descheduling still leaves recorded thread contrasts of −17,354,792 / +12,328,333 / +30,998,833 ns.

The residual per individual run is positive in all 48 rows, ranging 623,167–1,058,542 ns. These are observed differences, not confidence bounds on off-CPU time. Relative shares become misleading near a zero wall contrast: the retained 100K block 2 has a 124.35% residual share with opposite-signed thread and residual contributions. It remains in the table and is not evidence of an accounting failure by itself.

## What this does and does not bound

The frozen lookup harness calls CLOCK_THREAD_CPUTIME_ID before the wall CLOCK_MONOTONIC start, then records the wall end before the thread end. Native A/A has neither sampling nor counter hooks enabled. Additional CPU work around the wall interval and differing clock error enter R with unknown signs. Consequently R is not exact off-CPU time; no finite causal bound on differential descheduling follows without independently bounded wrapper CPU and accounting error.

The recorded-data bound is precise: the residual component of the three failed wall contrasts has magnitude at most 0.028979 wall percentage points, leaving at least 1.007294 wall percentage points in the thread-clock component. That is algebra, not a physical descheduling bound. The near-threshold block 4 thread sum exceeds the ±1% diagnostic by only 105,604.67 ns, so calibration error could matter to that binary classification. Blocks 2 and 5 exceed it by about 4.970751 and 18.806350 ms per paired sum. Their much larger margins still do not supply an absent error bound.

No endpoint-based migration count, continuous residency, frequency, cycles, core type, DVFS, cache placement, thermal state or causal on-CPU mechanism is established. A large thread-clock contrast identifies a remaining measurement discrepancy; it does not identify its cause. Nothing here authorizes switching acceptance clocks, relaxing the gate, or resuming candidate work.

## Required consultation and a bounded next diagnostic

Own availability discovery found zero callable cpu-perf/library_status/ask tools in this participant's exposed tool catalog (checked by 11:35:06 UTC). I explicitly consumed the controller's **shared** real stdio consultation, not an own ask. Its 11:32:56 UTC library_status/ask/read_source calls are preserved in the ignored consultation journal; A.json records its hash and hashes of all four exact records. Actual server cpu-perf 0.1.1, bundled library commit deb5a0bac467, keyword-only 0/287 indexed, no direct passages matching the ask. Recommendations and other-machine examples are not evidence here. The actual shared ask requests falsifiable paired-clock/ABBA analysis, its limits for DVFS/migration/cache, and a materially different future diagnostic; its context records this source/compiler and failed EXP-009 controls. The journal retains exact inputs/responses rather than reconstructing them from this summary.

The shared read_source actually fetched [LLVM's benchmarking guidance](https://llvm.org/docs/Benchmarking.html). It supports separating reduced noise from measurement bias; it does not establish macOS thread-clock error, a cause of these controls, or transferable numerical stability. The ask's unread source suggestions and example benchmark numbers are unused.

A justified next step is a **separate clock-attribution calibration**, subject to a new reviewed plan rather than an EXP-009 rerun: use the same nested clock brackets around a fixed CPU-work control and a controlled blocking interval, independently bracket that blocking interval, and retain every wall/thread/residual observation. Preregister whether the residual detects the blocking perturbation within a stated uncertainty and whether differential empty-wrapper/clock overhead can be bounded below the 105.605 µs paired-sum margin of block 4. Failure leaves attribution unresolved; success validates that estimator only, not baseline repeatability or a tree optimization. This directly tests the missing measurement assumption and uses no guessed hardware counters or permission changes. It is proposed only; no native work is authorized or executed by this review, and its feasibility/error model must be established before launch.

Decision: recorded residual-only explanation fails; strict descheduling causality remains unresolved. Retain PARK/source NONE and all twelve original controls.
