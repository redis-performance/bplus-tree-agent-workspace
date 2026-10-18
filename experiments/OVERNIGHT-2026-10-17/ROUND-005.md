# Overnight round5 — evidence and handoff

Bounded round:2026-10-17 23:31:40 through2026-10-18 00:01:40 UTC. This is not the final
campaign round. Measurements/tests are complete, with no active benchmark/profile child;
handoff saved before the final90s. Main src/zset_btree.c/.h and root HARNESS-001 referee
remain byte-identical to their pins. No candidate, population, publishing or permission
change. Exact backend/model/token cost unknown; supervisor records actual CLI usage.

## Completed work and decisions

| Evidence | Completed result | Decision |
|---|---|---|
| [DIAG-007](DIAG-007/README.md) |24 processes/384 fine contiguous lookup windows, all controls pass;1/4 phase cells meets criterion, required2 | Overall early/late phase hypothesis unsupported |
| [BOUNDARY-009](BOUNDARY-009/README.md) |526590 batched-score calls/7883000 slots per build,12 complete model checks,28 active-resize batches; two faults detected | Batch mask/exact-score/output-bound coverage validated |
| [DIAG-008](DIAG-008/README.md) |48 fresh-seed ABBA processes/768 windows; primary short-miss warmup contrast meets preregistered criterion | Operation-matched miss warmup warranted; no precision claim |
| [HARNESS-003](HARNESS-003/README.md) | Miss warmup/metadata revision passes43 upstream tests,3 referee groups and80 query-fixture cells/build | Third locally validated isolated referee; uncommitted |
| [AA-004](AA-004/README.md) |96 fixed fresh A/A rows;0/4 cells qualify unchanged gate, all semantics/memory controls pass | Lookup qualification PARK; source NONE |
| [BOUNDARY-010](BOUNDARY-010/README.md) |4 fixtures/33 raw lengths,260 guard mappings,652 raw queries,12 model checks/build; two faults detected | Raw-buffer length/ownership coverage validated; first compile failure retained |
| [DIAG-009](DIAG-009/README.md) |18 fixed known-function calibrations pass controls; timer delivery-rate equivalence criterion fails | Rate-equivalence hypothesis unsupported; corrected helper interface saved |

Round totals:168 measured tree processes (24+48+96),1152 diagnostic tree windows plus
96 A/A rows;18 additional arithmetic calibration processes. One separately recorded,
prospectively excluded binary warmup for AA-004. No measured rows removed, normal-run
failures or timeouts. Two boundary suites and four intentional faults. Test/smoke times
are not performance data. One initial test compile failed, retained and corrected.

Campaign totals: **three** locally validated harness revisions, **five** baseline
explorations, **twelve** additional measurement/path-count/profile diagnostics,
**ten** boundary suites and **twenty** detected fault controls. Optimisations **0 accepted /
0 rejected /0 parked**; population rounds **0**. Qualification PARK remains separate.

## Findings and limits

DIAG-007 observes16 consecutive windows without validation/output between them. One
process-level outer bracket bounds untimed gaps; this does not prove observer neutrality.
Its overall hypothesis failed. The short-miss pattern motivated a different intervention:
DIAG-008 compares equal-count hit versus miss warmup on fresh seeds with unchanged
measured loops. It meets the primary phase criterion. Warmup operations also take different
elapsed times, so no cache-only, branch-only or frequency explanation is established.

HARNESS-003 therefore changes miss warmup and reports warmup_case; other cases retain
successful-lookup warmup. Timed bodies and checks remain intact. AA-004 shows this phase
improvement does not suffice for tight comparisons: all four cells remain PARK under the
original rule, including a nearly qualifying long-key hit cell. No candidate population
started because meaningful comparison precision is absent. Never loosen gates or repeat
this schedule unchanged. Root HARNESS-001 remains preserved for morning review.

The new batch oracle exercises every hit/miss input mask for counts0..16 before/after
mutation, duplicates, both zeros/exact finite extremes, binary/empty members, output
canaries, clone lifetime and natural incremental resize. Missing-score slots are unspecified
and are not checked. Batch lookups may advance rehash, so memory invariance during resize
is not falsely asserted. Both predeclared mask/output-slot faults are detected.

Guarded raw inputs sit against inaccessible pages on both sides in separate fixtures,
covering empty through65536-byte members. Read-only queries and raw insertion must respect
explicit lengths, then preserve ownership after caller pages are overwritten/unmapped.
Both release/debug and sanitizers pass. Overread and truncated-hash faults are detected.
Initial compile failed for missing string.h; the failed snapshot/logs/manifest/patch remain
intact. Final snapshot adds only that header, with all assertions/fixtures preserved.

DIAG-009 resolves the copied calibration driver's stale stop/dump interface in a fresh
snapshot. Requested1000/3001us do not satisfy the preregistered delivery-rate equivalence
bound. Slower17011us meets its separate bound, but overall support required both. Known-
function symbol calibration passes all18 runs. Counts/thread-duration rates do not measure
exact interarrival intervals or CPU frequency; rates on arithmetic cannot be transferred
to tree workloads. No clock/library call added to handler: installed SDK sigaction does
not list clock_gettime as async-safe. Frequency/effective QoS/residency remain unknown.

## Commands and provenance

- Each diagnostic/referee has prepare.py, saved patch and freeze.json with exact baseline
  commit and source hashes. Validation scripts record compiler flags, commands, stdout,
  stderr and outcomes. HARNESS-003 validates both retained tests and an independent Python
  query/fingerprint/checksum oracle. DIAG-007/008 small partial-pass fixtures pass both builds.
- DIAG-007/008 and AA-004 run.py/analyse.py retain fixed schedules, every raw integer wall
  observation and recomputable decisions. DIAG-009 retains18 calibration rows, raw PC/symbol
  hashes, symbolication commands, dSYM/UUID checks and atomic import inspection. Raw profile
  data stays ignored scratch. Output occurs after timing endpoints in corrected helper.
- BOUNDARY-009 run.py/faults.py; BOUNDARY-010 run-final.py/faults.py pass. Original BOUNDARY-010
  run.py and manifest.json preserve the compile failure; manifest-final.json pins final suite.
- `python3 experiments/OVERNIGHT-2026-10-17/verify-round005.py` passes root/snapshot/validation/
  raw hashes, all fixed schedules, independently reconstructed measured fixture fingerprints,
  recomputed phase/ABBA/rate decisions, sample conservation and fault outcomes. This is a
  separate sequential audit, not independent performance confirmation.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check` are recorded
  in ROUND-005-FINAL-CHECKS.json. Public-evidence privacy/whitespace scan and final inventory
  pin scripts, summaries, sources and shared memory. [Method metadata](ROUND-005-METHOD.json)
  records CPU MCP retrieval hashes, SDK source hashes and compiler/platform observations.
- [Adversarial review](ROUND-005-REVIEW.md) covers measurement, semantics, portability and
  acceptance limits. Reviewer-agent startup failed at thread-store context loading; no
  agent ran. All reviews sequential, no fabricated participant/model/token data. CPU MCP
  checker's DIAG-009 drop_number verdict is recorded; no portable performance figure promoted.

Workspace base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c; target source pin remains
Redis PR#15635 a7ecd959374d66847c095250bf2d373edf7316c5. All new work has explicit
uncommitted isolated-snapshot provenance. Commit-based acceptance awaits morning review.
Prior git/sample/sysctl denials not retried. No credentials/private hosts/settings,
upstream actions, network publication or supervisor runtime/STOP modifications.

## Next concrete action

Use isolated HARNESS-003 for new independent-query work; preserve root baseline. Do not
repeat AA-004 or the unsupported DIAG-007/009 schedules. A [public requested-QoS
capability probe](ROUND-005-QOS-PROBE.json) succeeds in a short-lived child: inherited user-interactive changes to user-initiated. SDK constants and
AA-004 reported QoS agree; current runs already request user-interactive, so a future
comparison is not a simple priority increase. This probe is preparation, not another
measurement diagnostic or qualification. A distinct preregistered QoS intervention could
test placement sensitivity; it cannot by itself prove frequency/core type/residency or replace A/A. A controlled dedicated runner
may still be necessary. Alternatively target an uncovered fixture/API contract.

For sampler work, DIAG-009 supplies a calibrated driver using DIAG-006's corrected stop/
dump interface. Preserve all cadence/bias limitations and existing frozen snapshots.
Both population stages, qualified target/guards, matched profiles, fresh independent
confirmation, adversarial review and morning source-commit review remain required.
Final campaign worker must write MORNING-REPORT.md before2026-10-18 07:00UTC/08:00Lisbon.
