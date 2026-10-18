# Overnight round 1 — handoff

Round window: 2026-10-17 21:46:39–22:16:39 UTC. This is not the final campaign round.
Main src/zset_btree.c/.h remain byte-identical to the pinned source. No source candidate,
population, accepted optimisation, network publication or upstream action. Backend/model
unknown; actual CLI usage is recorded separately by the supervisor, not estimated here.

## Completed work and decisions

| Evidence | Result | Decision |
|---|---|---|
| [HARNESS-001](HARNESS-001/README.md) | Repeated traversals and accurate callback counts/checksums; thread CPU time, boundary CPU IDs, queried QoS and fixed warm-up passes | Locally validated separate referee revision; uncommitted |
| [AA-001](AA-001/README.md) | Six fixed ABBA blocks, 192 checked rows, 2/8 cells qualify (iterate16/scan16) | Suite and lookup/rank/update PARK; no source selection |
| [SCAN-PROFILE-001](SCAN-PROFILE-001/README.md) | Benchmark checks pass; sample exits255, cannot inspect child | No escalation/retry; time profile absent, selection NONE |
| [DIAG-001](DIAG-001/README.md) | 42 processes, 72 checked windows; reuse half-CV criterion met1/6 blocks, required4/6 | Reuse remedy not supported; A/A PARK unchanged |
| [BOUNDARY-001](BOUNDARY-001/README.md) | Release/debug + ASan/UBSan: 12 fixtures,24576 mutation steps,1356 full checks per build; four intentional faults detected | Additional semantic coverage validated |
| [BOUNDARY-002](BOUNDARY-002/README.md) | Release/debug + ASan/UBSan:1352 clone range deletions,2706 bound/ownership checks per build | Additional semantic coverage validated |
| [COUNTERS-001](COUNTERS-001/README.md) | Three scoped Clang execution-count captures; all reset-boundary and loop-count checks pass | Path-frequency evidence only; not a time profile |

Optimisation counts remain **0 accepted / 0 rejected / 0 parked**. Population rounds **0**.
Qualification PARK and diagnostic outcomes are separate from optimisation counts.

## Commands and validation

- Release and sanitizer builds of the revised harness: exact commands in
  HARNESS-001/validation build logs/JSON. Original embedded tree tests:43/43 pass in both.
- `python3 tests/test_microbench.py scratch/overnight-harness-001/release/btree-bench -v`
  and sanitizer counterpart: all3 functional groups pass. Frozen snapshot tests also pass.
- `python3 experiments/OVERNIGHT-2026-10-17/AA-001/run.py`: complete; analysis via
  its analyse.py. Manifest verifies source/binary hashes and all raw CSV/stderr hashes.
- DIAG-001/run.py and analyse.py: complete fixed schedule, no removed windows/failures.
- Boundary compile/run commands, flags and source hashes: each manifest.json. Four
  intentional faults were compiled in separate scratch copies and failed specific oracle
  assertions; these are test-strength controls, not optimisation candidates.
- COUNTERS-001/run.py: all three processes and llvm-profdata/llvm-cov tools succeeded.
  Public Clang reset/dump API scopes captures to the operation loop plus boundary
  observations. Setup/cleanup excluded; insertion/deletion counters zero. CSV timings
  from instrumented or sampling-attempt processes never enter A/A comparisons.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: pass.

## Provenance and restrictions

Base workspace commit `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c`. Git staging was denied
once: protected .git/index.lock, Operation not permitted. No retry, worktree creation,
permission changes or bypass. HARNESS-001/freeze.json, saved patches and binary hashes
pin the uncommitted revision; snapshot is scratch/overnight-aa-001/base. Morning commit
review remains required. Public build logs with workspace paths were curated; exact
uncurated originals are retained under ignored scratch/overnight-public-raw.

Agent startup failed before any agent ran (thread-store context load failure). No
independent proposal/review participant is claimed. All reviews here are sequential
coordinator passes. Both three-proposal/chair and three-implementation/measured-selection
stages remain mandatory for a future optimisation. No population was silently skipped
for an accepted change: none was attempted or accepted.

CPU Performance Engineering ask + benchmark05/14 methods/code consulted; broad retrieved
passages were irrelevant and not used as support. Local SDK interfaces inspected first.
Evidence checker rejects promotion of A/A rates with missing frequency/residency; no
portable rate/speedup claim is made. Effective QoS is unknown: the available public query
reports requested class/relative priority. CPU IDs are opaque boundary observations,
not P/E classification or proof against within-window migration. No M4 measurements used.

## Next concrete action

Do not rerun AA-001 or DIAG-001 unchanged. A useful next bounded trial is a preregistered
large-fixture A/A diagnostic (1M members,16-byte keys, longer fixed lookup windows) with
the frozen HARNESS-001 executable, explicitly new fixture/duration coverage. This aligns
with an existing EXP-001 sampled lookup profile, without pretending the failed100K cells
qualified. Freeze counts, blocks, seeds, budget and unchanged gates before running;
serial children <=120s, no builds/agents overlapping measurement. Qualifying one cell
still does not qualify missing guard cases. Alternatively extend semantic coverage to
active-resize scan mutation histories or wide leaf IDs, retaining all prior checks.

For scan, the new scoped counts establish exercised paths (including inline rehashing
and external cached hashes) but do not rank their costs. Time-profile validation remains
open; do not present call counts as a hot-time profile. Do not retry denied sample/git
operations with elevated permissions. A separate capable runner or morning review may
be needed for acceptance. Root baseline must remain untouched by source candidates.

Continue within the supervisor's remaining campaign budget. Final round must write
MORNING-REPORT.md; this intermediate round deliberately does not create that report.
