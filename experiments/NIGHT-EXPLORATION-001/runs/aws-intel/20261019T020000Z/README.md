# Intel overnight experiment ledger

No candidate has been adopted. The corrected-source profile and controls passed independent review. The corrected exact-B guard-first attempt is parked: two fresh baseline guard blocks failed precision, so no candidate guard or primary comparison ran. The runner is idle.

The two local measured populations produced **0 acceptances, 1 rejection and 1 parked result**; all six implementation patches remain available. The separately counted AMD-to-Intel SCAN architecture replication is **rejected**. The coordinator maintains the campaign-wide counts across machines.

| Work | Result | Evidence |
|---|---|---|
| SSE2 first-match lookup population | REJECT / NONE | All primary blocks were slower; 432 process rows retained. |
| Iterator cache population | PARK / NONE | The fixed screen ended at its cap and controls remained unresolved. |
| Original-source SSE2 SCAN replication | REJECT / NONE | Primary discovery and independent confirmation passed, but a qualified supplemental guard regressed in every block. |
| Corrected-adapter baseline | No candidate | All 960 rows retained; 10 of 40 cells qualify. |
| Corrected-source SCAN profile and controls | Baseline qualified; independently reviewed | All 60 captures and 48 fresh A/A rows retained. No candidate was timed. |
| Corrected exact-B guard-first attempt | PARK before candidate timing | The fresh known guard fails two of six A/A blocks; no retry or candidate comparison. |

The decisive SCAN guard uses seven fully reversed members, each 319 bytes, with alternating signed-zero scores. All six blocks are slower by more than 1%, with a median of **+4.931%**. This fixture has no full 16-byte or 8-byte tag chunk, so it demonstrates an overhead/tail guard regression without identifying its CPU-level cause. See [the decision](014-scan-supplement/DECISION.json). Independent audit `1217ba80a` reconstructs the same result. No alternate-source retry is permitted.

The corrected adapter is a separate frozen source, `13e459ff8`. Its baseline-only SCAN diagnosis is:

| Size | Captured helper samples / text samples | Largest absolute A/A effect | Minimum A/A window |
|---:|---:|---:|---:|
| 100,000 | 368 / 1,315 (27.985%) | 0.288% | 436.623 ms |
| 1,000,000 | 478 / 1,740 (27.471%) | 0.196% | 582.990 ms |

Helper sample attribution matches the actual timing binary's instructions and source locations. These are captured executable-text samples, not whole CPU time or cycles. The initial metadata failure and its read-only correction are preserved; no measurement was repeated. The old-source rejection remains final. The separately qualified 319-byte signed-zero guard failed fresh A/A precision (−1.417% and −1.047% in two blocks), stopping the corrected-source plan before candidate timing. No retry is authorized.

See [EXPERIMENTS.md](EXPERIMENTS.md), [SUMMARY.md](SUMMARY.md), [ACTIVITY.md](ACTIVITY.md), and [NATIVE-STATUS.json](NATIVE-STATUS.json). Exact backend/model and measured token/USD costs are unknown.

[Read-only AMD iterator critique](019-amd-iterator-review/REVIEW.md) distinguishes score-only decoding from the earlier member cache. It selects no candidate and does not change the counts or failed controls.

[Morning report](MORNING-REPORT.md): no adopted source; lease remains ACTIVE until coordinator-verified 08:00 UTC release. The read-only mask discussion is exact historical EXP-005 A overlap, not a new hypothesis.
