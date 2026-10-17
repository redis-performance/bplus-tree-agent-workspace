# Live status — 2026-10-17

Standalone workspace prepared from PR #15635 at a7ecd959374d66847c095250bf2d373edf7316c5.
Only the data structure and minimal support are present; no Redis checkout is required.
Population selection and implementation are documented and have not run.

User subsequently authorised local microbenchmarks and CPU Performance Engineering MCP
exploration. EXP-001 local M1 run completed: 144 processes, 984 rows, all checks passed,
four profiles. Qualification parked: 40/41 cells fail precision/duration gates.
Short-key leaf memchr and long-key SipHash dominate their respective sampled lookup paths;
the 321-byte allocator request gets 384 usable bytes. Source/referee unchanged.
Next: improve placement/thread-time/duration observability in a separate harness commit,
then requalify before population decisions. See experiments/EXP-001/local-m1-2026-10-17/README.md.
No optimisation accepted; no upstream action requested.

CI is a draft in docs/ci-check.yml: the write account lacks workflow scope. Repository
creation and pushes use the existing fcostaoliveira credential without changing the
default gh login; filipecosta90 has read access only. Never write credentials here.
