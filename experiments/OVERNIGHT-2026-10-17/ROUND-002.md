# Overnight round 2 — evidence and handoff

Round window2026-10-17 22:13:35–22:43:35 UTC; not the final campaign round.
Main src/zset_btree.c/.h and frozen HARNESS-001 referee remain unchanged. No source
candidate, population, accepted optimisation, network publication or upstream action.
Backend/model and token cost unknown; supervisor separately records actual CLI usage.

## Completed work and decisions

| Evidence | Completed result | Decision |
|---|---|---|
| [AA-002](AA-002/README.md) | Six fixed ABBA blocks,96 checked rows at1M members; rank16 alone qualifies | Lookup comparisons PARK, no rank time profile, source NONE |
| [BOUNDARY-003](BOUNDARY-003/README.md) | Natural ID widening to70834; active migration/scan continuity, two seeds pass release/debug and ASan/UBSan | Additional semantic coverage validated; two faults detected |
| [DIAG-002](DIAG-002/README.md) |24 lookup windows bracketed by inspected dependent-add loops; fixed association criterion fails | Common execution-rate explanation not established; no normalization remedy |
| [BOUNDARY-004](BOUNDARY-004/README.md) | Four relocation fixtures,2673 full model checks/build; release/debug and ASan/UBSan pass | Pointer/accounting coverage validated; two faults detected |

Optimisations **0 accepted /0 rejected /0 parked**; population rounds **0**.
Campaign totals: three baseline explorations, three additional measurement diagnostics,
four additional boundary suites and one locally validated harness revision. Qualification
PARK and failed diagnostic hypotheses do not count as parked optimisation candidates.

## Commands/tests and evidence

- `python3 experiments/OVERNIGHT-2026-10-17/AA-002/run.py` completed all96 planned
  measurements plus excluded preregistered warmup; `analyse.py` reports1/4 qualified.
  Manifest pins source/referee/binary hashes before/after, exact arguments, UTC stamps,
  load averages and raw CSV/stderr checksums. All operations/checksums/memory invariant.
- BOUNDARY-003 manifest records two build commands and four seed/build runs, all exit0.
  Natural widening observed during ordinary append calls; no test writes private tree
  fields. Five full validations/seven scans per seed. Late widening and omitted small
  scan-table faults both fail in isolated snapshots; exact patches/stderr retained.
- DIAG-002 prepare.py creates a new isolated snapshot from HARNESS-001; release and
  sanitizer smoke pass. Assembly inspection originally assumed x0, while Clang usedx8:
  inspection-script error preserved in ASSEMBLY-REVIEW.md, corrected before timing,
  no code/count changes. Eight dependent adds verified; loop overhead not subtracted.
  run.py completes six measured processes/four windows each plus one excluded warmup.
  analyse.py retains every window and reports failed preregistered criterion.
- BOUNDARY-004 manifest records release/debug and sanitizer build/run commands, all
  exit0. Callbacks relocate allocations and change usable sizes, decline some moves,
  and use the API's distinct Start/Step free conventions. Sorted-vector oracle reused
  unchanged. Missing ID repair causes ASan UAF; missing accounting causes exact delta
  assertion. External ASan symbolizer failed only on the intentional UAF; raw report
  and binary-relative frames retained. No baseline sanitizer errors.
- `python3 experiments/OVERNIGHT-2026-10-17/verify-round002.py`: read-only audit passes
  raw hashes, schedules, expected checksums, independently recomputed A/A intervals,
  frozen binary/source hashes and all expected fault outcomes. This is a sequential
  coordinator audit, not independent performance confirmation.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: pass.
  Round hash manifest pins new public evidence and final oracle source. Absolute local
  paths in one intentional-fault ASan log were curated; original bytes and checksums
  retained under ignored scratch/, mapped in ROUND-002-CURATION.json.

## Evidence limits and review

Lookup A/A still cannot enforce the1% guard. Rank's newly qualifying local cell lacks
its own sampled time profile; previous EXP-001 lookup profiles are not rank profiles.
Therefore neither population stage started. Both remain mandatory, including three
separate proposals/chair, three isolated implementations, serial comparisons, fresh
confirmation and adversarial review. No qualified guard/profile gate was bypassed.

CPU MCP ask consulted, but OpenVINO retrieval passages irrelevant and not supporting
claims. Benchmark05/14 method/code read; no M4 results, clocks or CPU numbering used.
MCP evidence checker consulted for A/A and bracket diagnostic; no portable timing or
GHz claim promoted. Add durations are a second workload, not measured core frequency.
They cannot establish frequency/residency during lookup. CPU IDs are opaque boundary
observations; effective QoS and clock remain unknown. All timing regions primary wall.

One independent reviewer startup attempted and failed before the agent ran due to
thread-store context error. All reviews this round were sequential coordinator passes,
not independent agents or a population. No invented participant/model/token accounting.
No git staging, worktree or sample retry: previous sandbox denials respected. All work
is local draft evidence over base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c and explicit
patches/SHA256. Commit-based acceptance remains pending morning review.

## Next concrete action

Do not repeat AA-001/AA-002, process-reuse DIAG-001 or bracket DIAG-002 unchanged.
Useful next work is a new preregistered diagnostic that varies lookup access/fixture
history (for example repeat-permutation versus precomputed independent access streams),
with allocation/checksum/memory controls and clearly scoped interpretation. The add
bracket result does not identify cache effects, but motivates testing a different
explanation rather than declaring stable frequency. Keep root source/referee frozen.

Alternatively extend deterministic hash/index collision coverage to controlled bucket
probe runs or stale insertion-position revision boundaries, inspecting preconditions
first. Relocation coverage now exists; do not repeat it unchanged. Rank source/path
inspection or scoped counts may help design a future profiler run, but counts do not
replace time profiling. Do not retry denied sampling with elevated permissions.

A capable independently profiled/qualified runner may still be needed for acceptance.
No runner access was inferred from credentials or other workspaces. Main baseline stays
unchanged until separate morning review. Campaign ends2026-10-18 07:00 UTC; final round
must write MORNING-REPORT.md. This intermediate round does not create that report.
