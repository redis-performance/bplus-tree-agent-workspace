# Intel overnight report — source adoption NONE

Finalized 2026-10-19T08:03:11.134250+00:00. **COMPLETE; lease RELEASED.** The coordinator verified all three live OSS coordinators RUNNING during 2026-10-19 08:00:20–08:00:25 UTC (09:00 Lisbon), with inactive owned slices, zero owned units/processes and fresh saved RUNNING status matching live PIDs. The private fleet reservation was released and pushed. [Immutable release proof](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/06785a454/experiments/NIGHT-EXPLORATION-001/reviews/aws-release-final.json). Release markers identify attempt start, not restoration completion; this worker checked the retained proof locally and performed no additional runner access. All timing is closed; no new experiment phase started after 07:15 UTC.

The two Intel measured populations finished with **0 acceptances, 1 rejection and 1 parked result**. Six implementation patches are retained. The distinct cross-host SCAN replication is rejected; the later corrected-source guard-first attempt is parked before candidate timing. These are separate accounting categories, not extra accepted populations.

| Work | Actual outcome | Evidence |
|---|---|---|
| First-match SSE2 lookup | All primary blocks slower; REJECT/NONE | 002, 432 process rows/108 blocks; root audit `11fe15b1` |
| Update direction diagnosis | No supported candidate; NONE | 003, profile/census and failed broad controls retained |
| Member-offset iterator cache | Conditional full-output gains; failed precision/incomplete fixed screen; PARK/NONE | 004, 566 of 576 fixed rows; root audit `847ed4096` |
| Original-source exact SSE2 SCAN B | Primary and independent confirmation pass, but qualified guard regresses; REJECT/NONE | 007–014; independent confirmation `27fed33a7`, supplemental result `fcb17380a`, independent audit `1217ba80a` |
| Corrected adapter baseline | 960 rows, 10/40 cells qualify; no candidate | 013 result `01a7b464d`, root audit `bdb3d87f9` |
| Corrected SCAN baseline profile/A/A | 60 retained captures; both primary sizes qualify in 48 fresh A/A rows | 016 result `8d8687467`; actual timing binary unchanged |
| Corrected exact-B guard-first attempt | Correctness and baseline text parity pass; two fresh guard A/A blocks fail; PARK before any B timing | 017 result `ee07ed065`; 30 calibration +24 A/A rows, zero candidate guard/primary rows |

The old-source B had independent primary median elapsed improvements of 6.783% at 100K and 3.656% at 1M. Those observations are not an accepted speedup: the seven-member, fully reversed, 319-byte signed-zero guard was slower in all six qualified blocks, median +4.931% (range +1.566% to +6.877%). It contains no full 16-byte or 8-byte tag chunk, so the regression cannot be attributed directly to SIMD compare cost. No alternate A fallback followed.

Full original guards retained all 80 cells: 57 qualified, 56 passed and one mixed, leaving 24 unresolved including 23 control gaps. The focused 36-cell matrix passed all 22 qualified cells, with 14 noisy controls retained. Supplemental 30-cell guards had 10 qualified cells: eight pass, one demonstrated regression and one mixed; twenty noisy cells remain. Passing subsets never erase the failed or unresolved cells.

Corrected adapter `13e459ff8` is separately qualified evidence. Its baseline actual timing binary SHA256 is `eee1da2c6c3202a2799eb7d71b1e281ec2faf81998800c02c7ce0a1655e84523`. Native reproduced baseline text matches exactly (71,349 bytes). Corrected exact-B preparation passed original tests, exhaustive V2 oracle, supplemental models and fresh signed-zero guard semantics. However, fresh guard A/A effects include −1.417% and −1.047%, beyond the fixed ±1% gate. Candidate timing stopped before launch; no retry, seed/count substitution or source switch occurred. Old-source rejection remains final.

Profiling retained controls, source-linked actual-binary maps and every captured row. Intel perf permissions were unavailable; validated profil(3) captured text samples provide coarse attribution, not CPU cycle costs. The corrected profile's absent-linker-symbol metadata failure and approved read-only repair remain preserved; none of its 60 captures or controls was rerun. All original protected source/referee/timing hashes remained unchanged at post-phase checks.

Remaining acceptance gates are substantive: independently justified precision for the known guard, successful corrected-source primary/guard comparisons, full guard coverage without unresolved noise, fresh independent confirmation and adversarial review. The existing failed schedules cannot be rerun to fill those gates. No new candidate is currently selected or authorized.

Cross-worker contributions include independently authored proposals/implementations and reviews; original SSE2 implementation B and corrected ARM NEON B remain immutable patches with losing outcomes preserved. Read-only AMD029 critique now explicitly maps the mask expression to historical EXP-005 variant A/PARK, selects NONE and does not revive it. Score-only AMD iteration bypasses the old member-offset cache; evidence cannot be carried across output contracts or machines.

All decisions, raw rows, patches, commands, profiles/maps and checksums are retained on branch `exploration/aws-intel-20261019T020000Z`; root maintains campaign-wide README/chart/counts. No upstream merge, source adoption or force push occurred. Exact model/backend, measured token usage and monetary cost are unknown. Fleet handback is now verified by the coordinator’s immutable proof linked above; no future coordinator uptime is implied.


Final reporting reviews are sealed: ARM historical mask raw audit `16f074fbe` and chart/reporting audit `208dff5cc`. The ARM score-only primary replay remains a separate PARK with missing guards, fresh confirmation and matched profile, not an Intel result or new population. The known 570-command wording is corrected in the final main report: 570 validation commands comprise 536 correctness/fault executions and 34 preparation/build/inspection commands. No experimental decision changed at handback.
