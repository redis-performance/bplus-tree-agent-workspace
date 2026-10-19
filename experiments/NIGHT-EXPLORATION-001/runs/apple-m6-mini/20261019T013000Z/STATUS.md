# M6 scoreboard — core queue complete, source NONE

Updated round 7, 19 October 2026. Round deadline 03:40:06.072034 UTC;
handoff cutoff 03:38:36.072034 UTC. Campaign ends 08:00 UTC / 09:00 Lisbon;
no experiments after 07:15 UTC.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE / launcher baseline reused | baseline-attempt002: 120 processes / 960 rows; 4/40 qualified, 14 short cells |
| RANK-001 | REJECT / NONE | Skip exact shorter-side policies; [result](002-rank/RESULTS.md) |
| UPDATE-001 | REJECT dual primary / NONE | 1M lead only; [result](003-update/RESULTS.md) |
| LOOKUP-001 | REJECT dual primary / NONE | B at 100K exploratory only; [result](004-lookup/RESULTS.md) |
| DECODE-001 | REJECT universal policies / NONE | Count-one lead only; [result](005-decode/RESULTS.md) |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Core confirmation | NOT ELIGIBLE | No discovery survivor |
| Operator follow-up | PREREGISTERED / implementation preparation | M6-LOOKUP-CALLER-001; no measured result or replication eligibility |

New operator decision: [chair selection](006-followup/selection.md) chooses proposal
B's leaf-search call-boundary hypothesis after three actual independent proposals.
[Plan](006-followup/PLAN.json) declares both 100K/1M successful score-lookup primaries,
101 required cells, unchanged memory/semantic guards, and deadline
04:40:20.349829 UTC. [Population](006-followup/population.json) records implementation
preparation as observed in [round 7 checkpoint](ROUND-007-HANDOFF.json). This is an
operator-owned new hypothesis, not a reopening of the four rejected objectives.
Do not infer implementation completion, frozen comparison provenance or eligibility.

Worker stays on reporting while the operator owns this trial; no duplicate agents,
builds, tests, profiles or timings. No large evidence audit was repeated. The saved
launcher baseline is complete and preserved; direct sysctl/profiler permission
limitations remain. Last core experimental child: 03:00:37.811992 UTC.

Round 6 final handoff has matching ok coordinator acknowledgement: **60613cc05**,
request `r6-final-handoff-20261019T030943224909Z`. Round 7 publication follows.
Coordinator alone commits/pushes; worker performs no Git writes or permission changes.

Exact core identities and reproduction: [morning report](MORNING-REPORT.md).
Launcher-verified Apple M6 / Clang21; frequency/DVFS/core residency/migration/PMU
unknown. Cached M1 4c48fa7e read as context only; remote state UNKNOWN, no cross-host
sample pooling. All four completed core populations were sequential. Candidate
profiles, qualified complete guards, fresh independent confirmation and independent
review remain absent for adoption. Baseline source remains unchanged.

Completed branch totals unchanged: 11 populations (9 sequential + 2 historical
multi-agent), 0 accepted / 6 rejected / 5 parked, 33 patches / 14 harnesses. In-flight
operator implementation population and concurrent M1 night excluded. [Usage](USAGE.json)
now records completed round 6; round 7/exact backend/currency cost remain unknown.
