# M6 morning report — interim, all queued comparisons complete

Updated 2026-10-19T03:04:04.162366+00:00; campaign still authorized through08:00UTC/09:00Lisbon.
No new experiments after07:15UTC. Source selection **NONE**.

The measured five-size baseline was reused from the launcher-selected
baseline-attempt002:120 serial processes/960 rows,162.423s. Earlier failed attempt
preserved. 4/40 baseline cells meet the numerical fine-precision rule.
No baseline or completed target was rerun. Launcher verified Apple M6; direct
sysctl denied previously, not retried. Frequency/residency/DVFS/PMU unknown.

| Target | Finding | Decision / M1 action |
|---|---|---|
| Rank | All100K candidate blocks regress | REJECT/NONE; skip exact patches |
| Updates | Repacking fails100K;1M-only lead | REJECT/NONE; no relabeled primary |
| Lookup | B improves100K4.80% but fails1M | REJECT dual primary; exploratory100K only |
| Count-one decoder | B/C improve primary≈30%; repeated larger-range guard losses | REJECT universal policies; private lead only |
| Iterator | Not selected for optional slot | SKIPPED |
| Fresh confirmation | No candidate passes discovery gates | NOT ELIGIBLE |

[Rank](002-rank/RESULTS.md), [update](003-update/RESULTS.md),
[lookup](004-lookup/RESULTS.md), [decoder](005-decode/RESULTS.md) retain exact pins,
patches, commands and raw evidence. Decoder source/referee freeze6e9e4ec8; no
private-helper gain is a public iterator or whole-tree improvement.

What changed understanding: rank accumulation and update repacking did not clear
the declared public dual primaries; physical score decoding is a100K lookup lead;
count1 benefits from scalar caller dispatch but changes hurt larger-range guards
even with unchanged bulk helper source. Required guards cannot be replaced by
stronger-looking primary numbers. No changes merged into baseline src/.

M6/M1 are separate: cached M1 branch4c48fa7e contains no exact M6 candidate result.
M1 compiler17-series versus M6 Clang21 is a confounder. No cross-host replication or
pooled data. M1 should skip the rejected exact universal/dual-primary candidates.

Limitations: failed controls, capped decoder cells, insufficient profiles, no
selected-candidate profile/fresh independent confirmation or independent review.
All populations this M6 campaign were sequential fallback. Decoder phases were
successive A/B/C rather than rotated candidate order; no qualified variant ranking.
The document-only selection filename collision and first failed audit remain
recorded; executable freezes match. All three losing patches/target are retained.
Actual supervisor usage is inUSAGE.json; exact backend/model/currency cost unknown.

Last experimental child2026-10-19T03:00:37.811992+00:00; none active.
Next is final reporting/publication review, with no eligible new timing schedule.
Branch totals11 populations(9 sequential+2 multi-agent),0 accepted/6 rejected/5 parked,
33 patches/14 harnesses. M1 night counts separate pending reconciliation. Coordinator
alone publishes; final audited decision/handoff acknowledgement follows.

Final round5 verification 2026-10-19T03:05:11.524964+00:00: decision/audit/report publication
acknowledged **c2b5d710547612028e1406b789a4377492f9bdf7**. Evidence seal34988 files
verifies; all9 launcher source/referee hashes unchanged; committed whitespace check
passes. No active experimental child; last remains03:00:37.811992UTC.
This final handoff is saved more than90s before03:08:25UTC. Final handoff publication
requested next; read its matching acknowledgement on resume. All queued comparisons
complete, no eligible confirmation, next work is reporting review only.
