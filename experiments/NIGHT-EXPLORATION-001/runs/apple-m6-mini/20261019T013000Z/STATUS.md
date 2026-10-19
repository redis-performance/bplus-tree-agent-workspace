# M6 scoreboard — core queue complete, source NONE

Updated 2026-10-19 03:08 UTC, round 6. Round deadline 03:35:31.651865 UTC;
mandatory handoff cutoff 03:34:01.651865 UTC. Campaign ends 08:00 UTC / 09:00
Lisbon; no experiments after 07:15 UTC.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE / launcher baseline reused | baseline-attempt002: 120 processes / 960 rows; 4/40 qualified, 14 short cells |
| RANK-001 | REJECT / NONE | Skip exact shorter-side policies; [result](002-rank/RESULTS.md) |
| UPDATE-001 | REJECT dual primary / NONE | 1M lead only; [result](003-update/RESULTS.md) |
| LOOKUP-001 | REJECT dual primary / NONE | B at 100K exploratory only; [result](004-lookup/RESULTS.md) |
| DECODE-001 | REJECT universal policies / NONE | Count-one lead only; [result](005-decode/RESULTS.md) |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Fresh confirmation | NOT ELIGIBLE | No discovery survivor |
| Operator follow-up | PROPOSAL REVIEW / owner external interactive root | [population](006-followup/population.json); decision pending, no worker takeover |

Exact hypothesis/patch/referee identities and acknowledged comparison commits are
in [MORNING-REPORT.md](MORNING-REPORT.md). Prior final handoff published
**e78e0d4fd7abb323755a3046922792e00f78e228**, matching coordinator ack
r5-final-audited-handoff-20261019T030500Z. Current report correction awaits publication.

Round 6 is reporting-only: corrected stale README target/decoder wording, refreshed
supervisor usage through completed round 5, verified 9 launcher hashes and 12 retained
patch hashes, and reviewed existing result/audit links. No build, test, profile,
timing, population or acceptance decision was added. See
[bounded review](ROUND-006-REPORT-REVIEW.json); no repeated evidence inventory.
Core queue's last experimental child remains 03:00:37.811992 UTC.

The operator is running an independent proposal population under 006-followup.
Shared memory explicitly reserves any selected follow-up to that operator. Worker
must stay on report/audit work while that review is active. Do not mutate its files,
spawn duplicate agents, start new trials, or create a BLOCKED.md that stops its work.
No claim about that review's completion or candidate eligibility is made here.

Launcher-verified Apple M6, Clang 21; direct sysctl unavailable and not retried.
Frequency/DVFS/core residency/migration/PMU unknown. Cached M1 4c48fa7e is context
only; exact cross-host replication NOT RUN. Baseline source/referee unchanged.
All four core M6 populations were sequential; independent confirmation/review and
selected-candidate profile gates remain missing. No adoption.

Branch totals unchanged: 11 completed populations (9 sequential + 2 historical
multi-agent), 0 accepted / 6 rejected / 5 parked, 33 patches / 14 harnesses. Pending
operator population and concurrent M1 night counts excluded. Actual supervisor
usage in USAGE.json; exact model/backend/currency cost unknown. Coordinator alone
writes Git; no permission, sysctl, profiler, Git-denial or network-denial retries.
