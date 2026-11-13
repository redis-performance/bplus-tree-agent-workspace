# Independent review: baseline duration repair

Verdict: the proposed qualification2 is a legitimate, separately preregistered duration correction. It does not qualify either original cohort or waive the original failure. No candidate performance conclusion follows from this review.

I independently reconstructed all 36 A/A blocks from the retained 144 rows and joined every row to its individual process stdout and successful command record. Slots 0–3, ABBA labels, seed17, operation counts, expected hits and score sums, empty stderr, and within-block memory equality agree. The independently computed effects, minimum windows and pass decisions match `analysis.json`. All 36 absolute effects are within1%; the maximum is0.609013113%. Exactly24 rows, comprising all six update blocks, are shorter than250ms. The other30 blocks pass both numeric gates.

| Cohort | Update rows | Minimum duration | Maximum duration | Rows below250ms |
|---|---:|---:|---:|---:|
| native | 12 | 247.550318ms | 249.276377ms | 12 |
| gcc15-lto | 12 | 237.641450ms | 240.814550ms | 12 |

The code performs500 updates per sweep and returns scores to integers after an even number of sweeps. Changing the runtime update count from10,000 to20,000 doubles operations from5,000,000 to10,000,000 while preserving that final-state assertion, the500-member fixture, update sequence and warmup. This addresses the observed minimum-duration defect without changing the noise or improvement thresholds. It is a changed-duration attempt, not an unchanged retry. A longer duration is expected but must be verified from the new observations.

The correction is valid subject to these explicit conditions in the new frozen protocol:

- Preserve the entire original144-row attempt and its failed-cohort decisions. Do not relabel it as passing or pool its passing cells into qualification2.
- Freeze qualification2 before collecting its observations, identifying the duration change and retaining source, ELF, compiler/linker flags, case definitions, seeds, order, warmup and thresholds. Reuse and verify the same binaries; no source modification is required for this argument change.
- Rerun the complete144-row qualification. Each cohort must independently pass every duration, noise and correctness gate. Another failure remains a failure; this review grants no repeated retry allowance.
- Use20,000 update sweeps consistently in subsequent candidate comparisons, native transfer and fresh-seed confirmations. Qualifying a longer update window and then comparing candidates at the failed shorter duration would not satisfy this repair.

`analyse_baseline.py` checks block label order and counts, checksums, memory, durations and effects. It does not itself enforce slot numbers, expected seed/operation counts or joins to process files. Those omissions do not invalidate these observations because this review independently checked them; future qualification analysis should retain equivalent checks.

Scope and consultation: this reviewer performed only source inspection and offline analysis of existing files, with no fleet access, timing or profiling. Own enabled-tool discovery returned no cpu-perf or library_status tool. I consumed the controller's shared `CONSULTATION.md`: its reported local stdio cpu-perf0.1.1 discovery/ask and topdown metric explanation are controller calls, not mine. The consultation returned no supporting primary passage and supplies no causal performance authority. Validated four-category TMA remains unavailable and is unnecessary for the directly observed duration failure. Backend/model/cost are unreported; I make no identity or cost assertion. This review is independent of the three implementation proposers.
