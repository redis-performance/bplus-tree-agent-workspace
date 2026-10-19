# M6 scoreboard — core complete; operator caller trial reserved

Updated 2026-10-19T03:18:26.488560+00:00, round 10. Round ends **03:46:40.435158 UTC**;
handoff cutoff **03:45:10.435158 UTC**. Campaign ends **08:00 UTC / 09:00 Lisbon**;
no experiments after **07:15 UTC**.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE / launcher-selected baseline reused | 120 processes, 960 rows; 4/40 qualified, 14 short cells |
| RANK-001 | REJECT / NONE | Skip exact shorter-side policies; [result](002-rank/RESULTS.md) |
| UPDATE-001 | REJECT dual primary / NONE | 1M lead only; [result](003-update/RESULTS.md) |
| LOOKUP-001 | REJECT dual primary / NONE | B at 100K exploratory only; [result](004-lookup/RESULTS.md) |
| DECODE-001 | REJECT universal policies / NONE | Count-one lead only; [result](005-decode/RESULTS.md) |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Core confirmation | NOT ELIGIBLE | No discovery survivor |
| Operator caller trial | IN PROGRESS / static review observed | Await owner's frozen identities and measured outcome |

External interactive operator owns **M6-LOOKUP-CALLER-001** in `006-followup`.
[Population](006-followup/population.json) still explicitly says **PREPARING three
isolated implementations**, following three actual independent proposals/B selection.
[Plan](006-followup/PLAN.json): 101 cells, dual 100K/1M successful score-lookup primaries,
deadline **04:40:20.349829 UTC**. Worker leaves this directory untouched.

New [static review](006-followup/review-caller.json) reports recorded validation PASS
for A/B/C and equivalent `zbtreeScoreRaw` instructions after relocation/assertion-line
normalization. Author C's independent review covers A/B, not own C. These observations
do not establish a timing freeze, candidate ranking, profile validation or adoption.
Review requires rebuilding timing binaries with a common relative frontend path;
validation builds used different paths affecting `__FILE__` and placement. This
common-build gate belongs to the operator. M1: await completed owner decision and
exact published patch/referee identities.
[Checkpoint](ROUND-010-HANDOFF.json) records observed document hashes only.

Prior round 9 final handoff acknowledged **acfba0f86**, request
`r9-final-handoff-20261019T031614204088Z`, ok **03:16:18.805693 UTC**.
Round 10 publication failed; see concrete blocker below. Coordinator alone commits/pushes.

Launcher-recorded Apple M6/Clang 21 metadata and selected baseline summary reused;
earlier failed baseline preserved. Existing sysctl/profiler/network denials stand.
Frequency, DVFS, core residency/migration and PMU remain unknown. Cached M1
`4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9` read as context; current remote UNKNOWN.

No worker agents, builds, tests, profiles or timings this round; no repeated raw/source
inventory. Source selection **NONE**; no new decision. Counts unchanged: 11 completed
populations (9 sequential + 2 historical multi-agent), 0 accepted / 6 rejected /
5 parked, 33 patches / 14 harnesses. Operator trial and concurrent M1 night excluded.
[Usage](USAGE.json) records supervisor counters through completed round 9;
current-round usage, exact serving backend and currency cost unknown.
[Morning report](MORNING-REPORT.md) remains interim. Worker finishes reporting early.

Round 10 publication **FAILED**, request `r10-final-handoff-20261019T031850087694Z`,
checked **03:18:50.408944 UTC**. Coordinator error:
`Public-evidence review required: 006-followup/build.json`.
See [failure record](ROUND-010-PUBLICATION.json). Local evidence is preserved;
no worker Git action or same-blocker retry. Operator/coordinator must resolve that
operator-owned metadata before requesting publication again. No performance decision
changes. Latest successful final handoff remains **acfba0f86**.
