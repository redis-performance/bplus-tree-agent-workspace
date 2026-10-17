# Live status — 2026-10-17

Standalone workspace prepared from PR #15635 at a7ecd959374d66847c095250bf2d373edf7316c5.
Only the data structure and minimal support are present; no Redis checkout is required.
Population selection and implementation are documented and have not run.

Next: EXP-001 on a dedicated runner, qualify A/A and profile the direct API harness.
No optimisation accepted; no upstream action requested. Preparation evidence and
validation limits are in experiments/PREP-001/README.md.

CI is a draft in docs/ci-check.yml: the write account lacks workflow scope. Repository
creation and pushes use the existing fcostaoliveira credential without changing the
default gh login; filipecosta90 has read access only. Never write credentials here.
