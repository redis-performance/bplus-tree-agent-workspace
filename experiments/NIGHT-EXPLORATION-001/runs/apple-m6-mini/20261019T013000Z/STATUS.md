# M6 scoreboard — core queue complete, operator trial in preparation

Updated 2026-10-19T03:13:49.147693+00:00, round 8. Round ends **03:42:29.322879 UTC**;
handoff cutoff **03:40:59.322879 UTC**. Campaign ends08:00UTC /09:00Lisbon;
no experiments after07:15UTC.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE / launcher baseline reused | baseline-attempt002:120processes/960rows;4/40qualified,14short cells |
| RANK-001 | REJECT / NONE | Skip exact shorter-side policies; [result](002-rank/RESULTS.md) |
| UPDATE-001 | REJECT dual primary / NONE | 1M lead only; [result](003-update/RESULTS.md) |
| LOOKUP-001 | REJECT dual primary / NONE | B100K exploratory only; [result](004-lookup/RESULTS.md) |
| DECODE-001 | REJECT universal policies / NONE | Count-one lead only; [result](005-decode/RESULTS.md) |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Core confirmation | NOT ELIGIBLE | No discovery survivor |
| Operator follow-up | PREREGISTERED / implementation preparation | Await exact patches, referee freeze and completed outcome |

Operator owns **M6-LOOKUP-CALLER-001**, selected after three actual independent
proposals: [selection](006-followup/selection.md), [plan](006-followup/PLAN.json),
[population](006-followup/population.json). Latest explicit population status remains
PREPARING three isolated implementations. Dual100K/1M successful score-lookup
primaries,101required cells, independent deadline04:40:20.349829UTC. No candidate
performance or replication eligibility claimed. Worker does not duplicate the trial
or edit its owned directory. [Round8 checkpoint](ROUND-008-HANDOFF.json) records
observed document hashes; these are not timing freezes.

Round7 final handoff has matching ok coordinator acknowledgement: **fa62b37cd**,
request `r7-final-handoff-20261019T031210001515Z`, checked03:12:13UTC.
Round8 publication follows. Coordinator alone commits/pushes; no worker Git writes.

Launcher-verified Apple M6 / Clang21 metadata reused with explicit provenance;
direct sysctl/profiler restrictions are unchanged and not retried. Frequency/DVFS/
core residency/migration/PMU unknown. The selected baseline summary was read without
rerunning measurements. Earlier failed baseline preserved. Baseline source unchanged.

No worker agents, builds, tests, profiles, timings or repeated evidence inventory
this round. No new experimental decision; counts unchanged:11completed populations
(9sequential+2historical multi-agent),0accepted/6rejected/5parked,33patches/14harnesses.
Operator trial and concurrent M1 night excluded from these completed counts.
[Morning report](MORNING-REPORT.md) remains interim. [Usage](USAGE.json) records actual
supervisor counters through completed round7; round8/exact backend/currency cost unknown.
Cached M1 `4c48fa7e` is context only; current remote state UNKNOWN. No sample pooling.

Round8 reporting checkpoint acknowledged **c0fb84636**, request
`r8-reporting-handoff-20261019T031349149187Z`, ok03:13:50UTC. See
[acknowledgement](ROUND-008-PUBLICATION.json). Final handoff publication follows;
read matching acknowledgement on resume. No worker experimental children.
