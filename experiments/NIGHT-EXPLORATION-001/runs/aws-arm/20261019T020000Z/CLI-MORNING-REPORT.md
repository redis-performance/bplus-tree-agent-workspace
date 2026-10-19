# AWS ARM early blocker report — round 1

This report records an early infrastructure blocker, not a completed overnight
campaign. Results from other hosts were not inspected.

- Host: aws-arm. Decision: NONE.
- Controller command startup failed with `bwrap: setting up uid map: Permission denied`.
- Existing baseline service and evidence: unverified; do not duplicate its launch.
- Newly run builds, checks, profiles, timing processes, and benchmark rows: zero.
- Candidate proposals, implementations, accepted/rejected/parked patches: none.
- Missing gates: baseline inspection and retrieval, correctness, calibration,
  A/A, baseline profiling, population selection, ABBA, memory/guard evaluation,
  independent confirmation, profile validation, and adversarial review.
- No source changes, remote changes, permission changes, Git writes, or pushes.
- Exact serving model and measured token usage: unknown; no subagents used.

See [BLOCKED.md](BLOCKED.md) for the precise failure and recovery steps. Restore
the managed controller command runtime, then inspect and harvest the existing
baseline with hash verification before choosing further work. The current worker
could not safely read or update existing status, handoff, activity, shared memory,
README, charts, or experiment logs. The publisher should incorporate this blocker
without replacing divergent evidence. Campaign stop-starting-experiments deadline
remains 07:15 UTC, with the existing independent release at 08:00 UTC.
