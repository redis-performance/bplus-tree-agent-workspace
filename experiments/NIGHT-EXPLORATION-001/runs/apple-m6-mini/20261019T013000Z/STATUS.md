# M6 scoreboard — core queue complete, operator follow-up reserved

Updated 2026-10-19T03:15:42.156304+00:00, round 9. Round ends **03:44:27.298341 UTC**;
handoff cutoff **03:42:57.298341 UTC**. Campaign ends **08:00 UTC / 09:00 Lisbon**;
no experiments after **07:15 UTC**.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE / launcher-selected baseline reused | baseline-attempt002: 120 processes, 960 rows; 4/40 qualified, 14 short cells |
| RANK-001 | REJECT / NONE | Skip exact shorter-side policies; [result](002-rank/RESULTS.md) |
| UPDATE-001 | REJECT dual primary / NONE | 1M lead only; [result](003-update/RESULTS.md) |
| LOOKUP-001 | REJECT dual primary / NONE | B at 100K exploratory only; [result](004-lookup/RESULTS.md) |
| DECODE-001 | REJECT universal policies / NONE | Count-one lead only; [result](005-decode/RESULTS.md) |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Core confirmation | NOT ELIGIBLE | No discovery survivor |
| Operator follow-up | PREREGISTERED / implementation preparation | Await frozen exact patch/referee identities and completed result |

Operator owns **M6-LOOKUP-CALLER-001**, selected after three actual independent
proposals: [selection](006-followup/selection.md), [plan](006-followup/PLAN.json),
[population](006-followup/population.json). Latest explicit implementation status:
**PREPARING three isolated implementations**. Dual 100K/1M successful score-lookup primaries,
101 required cells, deadline **04:40:20.349829 UTC**. No candidate performance or
replication eligibility claimed. Worker remains reporting-only and leaves the
operator directory untouched. [Round 9 checkpoint](ROUND-009-HANDOFF.json) records
observed document hashes, not timing freezes.

Prior round 8 final handoff has matching ok coordinator acknowledgement:
**19d1a8f87**, request `r8-final-handoff-20261019T031409730977Z`, checked 03:14:14 UTC.
Round 9 reporting/handoff publication follows. Coordinator alone commits/pushes.

Launcher-verified Apple M6 / Clang 21 metadata and selected baseline analyzer summary
were read without rerunning measurements. Failed baseline attempt retained. Direct
sysctl/profiler denials stand; frequency, DVFS, core residency/migration and PMU remain
unknown. Baseline source unchanged. Cached M1 `4c48fa7e` is context only; current
remote state UNKNOWN. No host pooling or denied-network retry.

No worker experimental children, agents or repeated evidence inventory this round.
No new decision; totals unchanged: 11 completed populations (9 sequential + 2 historical
multi-agent), 0 accepted / 6 rejected / 5 parked, 33 patches / 14 harnesses.
Operator trial and concurrent M1 night excluded from completed counts.
[Morning report](MORNING-REPORT.md) remains interim. [Usage](USAGE.json) now records
supervisor counters through completed round 8; round 9 usage, exact backend and
currency cost unknown. Worker hands off early while the operator trial continues.

Round 9 reporting checkpoint acknowledged **a4df5a725**, request
`r9-reporting-handoff-20261019T031546233097Z`, ok 03:15:50 UTC. See
[acknowledgement](ROUND-009-PUBLICATION.json). Final handoff publication follows;
read matching acknowledgement on resume. No worker experimental children.
