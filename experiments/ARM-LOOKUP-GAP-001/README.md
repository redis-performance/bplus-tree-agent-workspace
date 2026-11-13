# ARM membership lookup gap isolation

Status: investigation requested; source and harness qualification precede measurements. This is a new standalone diagnostic, with no candidate accepted and no new result yet.

The objective is to isolate the packed B+ tree membership cost observed in the two-key, 500-member, full-overlap intersection case. Keep Redis server, networking, command dispatch and persistence outside this workspace. Any eventual command-level confirmation belongs to the Redis integration campaign.

## Source qualification

The current standalone extraction records upstream `a7ecd959374d66847c095250bf2d373edf7316c5`. The motivating merged Redis source is `51e28c2a724a2632c0c75f376c352cd8aee37e0e`; its parent is `df10f323951f024df7f3a9a86274ef2fab7a7fa1`. Audit relevant source/API differences before attributing current Redis behavior to this harness. Prepare a separate qualified extraction/fixture when needed; preserve the main source and sealed historical experiments.

Freeze a primary fixture reproducing 500 short members `m:1` through `m:500`, ascending scores and successful membership lookups without score extraction. Separate lookup from iteration and fixture construction. Retain score-returning, missing-member and longer-member controls. Qualify fixture/harness changes before freezing a comparison; do not change the referee between candidate runs.

## Questions to resolve

1. Does the isolated current-source lookup reproduce the ARM cost concentration?
2. How much work comes from hash/index probing, leaf tag search, packed-record decoding, byte comparison, and helper boundaries?
3. Which small change improves qualified ARM measurements without losing correctness, memory behavior, or Intel performance?

These are investigation questions, not selected implementation hypotheses. Follow AGENTS.md and docs/POPULATION.md after baseline evidence is qualified; consult historical rejected/parked work first. Use three independent proposals and a chair decision, then isolated implementation alternatives if justified. Keep batching, explicit SIMD and prefetch outside the first experiment. Select NONE when evidence is insufficient.

## Execution and reporting

All performance work, including pilots, A/A, instruction counts and profiles, must run on a reserved benchmark fleet host. Never run timings on this workstation or historical Apple hosts. Existing local builds and correctness tests are permitted. Check live reservations and actual runner state, record ownership, and install bounded cleanup before use. Use the smallest focused case set that satisfies qualified A/A, at least three ABBA blocks, guards and fresh confirmation.

Use cpu-perf per docs/PERFORMANCE-MCP.md and topdown-profiler per docs/TMA-REPORTING.md. Inspect actual collector commands, scope and affinity: PID labels do not establish process isolation. Do not convert ARM stall-cycle percentages into pipeline-slot TMA. Preserve unsupported categories as unavailable.

This repository is public: keep credentials, host addresses and private operational artifacts out. Record sanitized source/build/fixture identities, results, losing variants and decisions here. No upstream PR or comment is part of this dispatch.

## TMA classification

| Category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No capture has run for this standalone investigation. The earlier integration Intel funnel had CPU-wide scope and cannot supply these entries.
