# M6 driver campaign — launch preparation

Updated: 2026-10-19 01:30 UTC. CPU verified: Apple M6, arm64. The user authorized
execution and continuous Git publication through **09:00 Europe/Lisbon today
(08:00 UTC)**. Final reporting starts 07:15 UTC.

Branch: `exploration/apple-m6-mini-20261019T013000Z`.
Starting plan/source revision: `e52c26c4`; exact hashes and host/toolchain details are
in [launch-manifest.json](launch-manifest.json).

| Target | Status | M1 action |
|---|---|---|
| Five-size baseline | QUEUED | M6 results pending; do not pool hosts |
| RANK-001 | NOT STARTED | No M6 hypothesis decision yet |
| UPDATE-001 | NOT STARTED | No M6 hypothesis decision yet |
| LOOKUP-001 | NOT STARTED | No M6 hypothesis decision yet |
| Optional decoder / iterator | CONDITIONAL | Lower priority; may be deferred |
| Confirmation / final report | RESERVED | Report due by 08:00 UTC |

No M6 optimization has been selected or rejected yet. The unchanged baseline tree
is the control. Candidates stay isolated. Publication uses a coordinator barrier
after status/decision updates, plus completed-round publication. Actual model usage
and costs remain unknown until emitted and measured.
