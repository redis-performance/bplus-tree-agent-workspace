# M6 driver worker — authorized until 09:00 Lisbon

The user has explicitly authorized this M6 overnight optimization campaign and
publication of all status updates so the concurrent M1 session can follow. Execute
the shared WORKER.md, PLAN.md and MEASUREMENT.md with the host-specific instructions
below. This file is frozen before launch. Do useful bounded experiments; resume the
host HANDOFF.md on each new round. Do not restart completed steps.

## Scope and deadline

The verified CPU is Apple M6. Record the actual host and hashes, never infer CPU
frequency, performance-core residency or counters. Read launch-manifest.json in the
injected evidence directory. The deadline is **2026-10-19 08:00 UTC / 09:00 Lisbon**.
The launcher verified sysctl outside the worker sandbox. The worker's read-only
preflight found sysctl denied by its existing workspace-write sandbox. Use the
launcher-recorded metadata with explicit provenance; do not retry denied sysctl or
change sandbox settings. New targeted harnesses may read that saved metadata and
record unavailable direct observations. A profiler permission denial is a limitation,
not authorization to change permissions. Public supported instrumentation/assembly
may answer a bounded mechanism question; missing profile validation blocks adoption.
Start no experiments after **07:15 UTC**; use the last 45 minutes for review, audit,
MORNING-REPORT.md and publication. This is a shorter-than-eight-hour authorized pass.

Target ceilings (advance early when a target concludes):

| UTC | Target |
|---|---|
| Launch–02:15 | Baseline, native/sanitizer checks, rank profiling/calibration |
| 02:15–03:45 | RANK-001 |
| 03:45–05:00 | UPDATE-001 |
| 05:00–06:15 | LOOKUP-001 |
| 06:15–07:15 | Fresh confirmation of eligible contenders; one optional target only if earlier work finishes early |
| 07:15–08:00 | Final audit, report, publication and handoff |

The shared target definitions, guards and selection gates still apply. Missing
time means explicitly deferred work, never weaker gates. Do not consume the night
with repeated unqualified timing schedules or unrelated correctness matrices.

## M6 leads the coordination

Publish a clear scoreboard and exact hypothesis/candidate/patch/harness identity.
Give the M1 session an actionable decision: REJECT (why), PARK (exact missing
evidence), exploratory lead (limitations), or eligible for replication. On M6,
inspect the published M1 branch for context, but the shared instruction to defer to
M6 decisions applies to the M1 worker. Do not wait for your own M6 result remotely.
Do not change or merge the baseline src/. Preserve all three implementation patches
and build each in an isolated worktree/build. Follow both population steps after
profiling. Actual independent agents may be used where tools/session rules permit;
otherwise explicitly record sequential passes and leave independent review pending.
Do not invent model names, agent independence, token costs or performance counters.

## Publication barrier: one Git writer

An external coordinator owns Git commits and pushes on this host branch. **Do not
run git add/commit/push yourself.** Read-only Git operations and isolated worktree
creation are allowed by session permissions; if a write is denied, record it once
and use isolated copied source/build directories with hashes. Do not bypass denials.

After each meaningful status update, profile diagnosis, harness freeze, completed
comparison, decision and round handoff:

1. Save STATUS.md and HANDOFF.md plus the relevant reproducible evidence under the
   injected host campaign directory. Make all public paths generic; keep raw
   transcripts and any private absolute paths in ignored scratch/. Update shared
   experiment logs/memory at decisions. No large duplicate evidence inventories.
2. Atomically write `publish-request.json` under the injected runtime directory:
   `{"id":"unique-milestone-id","paths":[]}`. Use a fresh ID each time. `paths` may
   list exact new/changed harness files such as scripts/... or bench/... or tests/...
   that need committing before timing. Do not request directories, src/, compat/,
   vendor/, tests/upstream.c, or another campaign. The coordinator always includes
   this host campaign and shared experiment/status/memory logs.
3. Wait for `publish-ack.json` with matching `request_id` and `status: ok` (poll at
   five-second intervals, at most 120 seconds). Keep source/evidence stable and
   perform no builds, tests, profiles or timings during this barrier. Record the
   acknowledged published commit in the next status update. Harness/source pins for
   comparisons are the acknowledged Git commit plus exact source/referee hashes.
4. If publication fails or times out, record the concrete failure once, preserve
   local evidence and continue useful bounded local work. Do not retry denied Git
   operations, change credentials or permission settings. Publication remains
   unresolved until coordinator acknowledgement succeeds.

The coordinator also publishes completed rounds, preserving partial evidence from
failed rounds. Keep each final handoff at least 90 seconds before round end.
Use the supervisor's exact injected deadlines. No detached experiments, supervisor
edits, STOP/deadline changes, permission changes, upstream PRs or main-branch pushes.
Missing profiling tools are a reported limitation; inspect actual release assembly
and public profiler availability rather than fabricate profile validation.

## First concrete action

Check the saved preflight/host metadata and launch status. The launcher runs the
shared five-size matrix before worker startup because
that runner captures sysctl metadata. If its manifest says complete, reuse the
measured baseline without rerunning it. Read `LAUNCH-STATUS.json` for the exact
selected `baseline_path`; preserve earlier failed attempts. Read its analyzer summary and publish the
measured baseline status. If incomplete, preserve it and record the exact blocker;
never silently overwrite it. Continue with public rank
profiling and one frozen calibrated rank harness. Use serial timings with no
compilation/test/profile overlap. Later rounds resume this saved work.
