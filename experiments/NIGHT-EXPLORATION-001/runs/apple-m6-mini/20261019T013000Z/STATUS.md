# M6 driver campaign — baseline reused; rank diagnosis running

Updated 2026-10-19 01:41 UTC. Deadline 08:00 UTC; reporting starts 07:15 UTC.
Actual CPU Apple M6, arm64, 12 physical/logical cores, macOS 27.0, Apple Clang 21.
Provenance: launcher sysctl capture in launch-manifest.json; direct worker sysctl denied
in preflight and will not be retried. Frequency, DVFS and core residency unknown.
Launch/baseline published commit `5ba51e40`; source plan `e52c26c4` and exact hashes
in launch-manifest.json. All baseline native/sanitizer validations pass.

| Target | Status | M1 action |
|---|---|---|
| Five-size baseline | COMPLETE | Reused baseline-attempt002: 120 processes, 960 rows, 40 cells, 162.42 seconds; 36/40 fail strict A/A, 14/40 short windows. Host-local baseline only. |
| RANK-001 | RUNNING diagnosis | No M6 candidate decision; profiling and one calibrated harness next. |
| UPDATE-001 | NOT STARTED | Await bounded rank work. |
| LOOKUP-001 | NOT STARTED | No M6 decision. |
| Optional | CONDITIONAL | No selection. |

M1 published context inspected at 01:40 UTC: branch exploration/apple-m1-20261019T005019Z,
revision `c53b1d91ab8103f7e923791f5380c434db5da0c7`. Rank shorter-side accumulation is an M1 exploratory hypothesis,
not M6 evidence. M1 controls failed and no adoption was claimed. No M6 veto yet.
Baseline src unchanged. No population has started. Backend identity exposed as GPT-6
family/Codex; exact model identifier and measured token cost unavailable. No agents used.
Earlier interrupted baseline evidence preserved; no baseline rerun.

Rank referee validation complete at 2026-10-19T01:40:29.447611+00:00: 138 native/sanitizer harness checks pass; injected public rank +1 fault detected. No candidate timing. Frozen bench/night-rank.c and diagnostic sources in 002-rank/freeze.json. Previous status acknowledgement 48b00870.
