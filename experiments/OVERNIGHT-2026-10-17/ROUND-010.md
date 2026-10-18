# Round 10 — ordered fixtures and concentrated reversed-leaf coverage

**No source was accepted. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.** The main
source, header and referee retain their prior-round hashes. This is not the final campaign
round; the final worker still owes MORNING-REPORT.md before 07:00 UTC.

Round started at 01:45 UTC, with a 02:15 UTC deadline and 02:13:30 handoff cutoff.
All performance measurements ended by 01:57:02 UTC. Later work was structural/correctness
coverage, evidence auditing and handoff. No new source population was started: this round
extends the already completed EXP-004 population with additional guards.

## Completed work and outcomes

HARNESS-005 is a separate, frozen referee revision over HARNESS-004. It adds ascending
and descending insertion, plus alternating signed-zero scores. Big-endian member IDs
make lexical tie order agree with the independent model beyond ID255. High score bits
are folded into the checksum so repeated negative zeros do not disappear through simple
sign-bit cancellation. This changes timed checksum cost, requiring new qualification.
Full bytes, exact score bits, order, output masks, iterator-copy state, exhaustion sentinels,
effective counts and unchanged tree-owned memory remain checked.

Release and ASan/UBSan each pass 1,408 fixture cells, all original43 tests, and five invalid
input checks: 2,832 validation commands. Three intentional faults are detected. The first
fault driver expected assertion wording absent from the adapter; its length fault had
already been caught. The original failure remains, and only the two unfinished controls
were subsequently run. Root referee/source and all old snapshots remain unchanged.

COUNTERS-004 passes 96 structural children in two builds. It establishes that the large
alternating-zero fixture uses one-bit packed scores. Descending insertion produces only
64 reversed members at both tested sizes, 4,096 and 100,000. Thus large monotonic fixtures
add useful construction coverage but barely stress reversed physical leaves.

AA-010 completes its fixed 384-row A/A schedule and one prospective whole-binary warmup.
Fourteen of16 cell/seed combinations qualify; six ofeight cells qualify on BOTH seeds.
Integer forward score-only with ascending or descending construction fails the joint
rule and remains PARK. All exact/checksum/count/memory/fingerprint invariants pass.
No row was dropped, no child failed, and no threshold changed after measurement.

EXP-004's ordered-guard extension uses the byte-identical qualified control and exact
retained A/B/C source hashes in isolated snapshots. All three variants pass 1,194 new
validation commands across both builds, including original tests, 192 new fixture cells
per build, exhaustive packed-bit decoding and the existing exact-zero mutation oracle.
Twelve matched scoped profiles and two calibrations pass conservation, symbol and minimum
sample-count controls. Sample bias and effective delivery cadence remain unknown.

All 432 screening rows, four prospective warmups, and 432 precommitted fresh-seed rows
complete. All three variants pass all six new regression guards on both fresh seeds,
with exact memory equality. These are additive guards, not new primary cases. The original
integer mixed-output guard is unresolved, and independent confirmation/review and committed
provenance are still absent. **A/PARK is unchanged; no new selection or speed headline.**

COUNTERS-005 establishes a compact public-API recipe: insert a sentinel at the next finite
score below the first model score, insert the data ascending, then delete the minimum.
All 672 structural runs pass. At sizes1..95 in the tested matrix, every trimmed history
has one fully reversed leaf; ordinary ascending controls have one ordinary leaf. Clone
and sentinel reinsertion/removal histories pass. Two sensitivity faults are caught.
One driver anticipated a later direct-score assertion, but the iterator-copy oracle caught
zero-sign loss earlier. A read-only stderr audit corrects that classification without
rerunning children. Packed widths can differ by history and are recorded explicitly.

BOUNDARY-014's compact extension runs the unchanged semantic oracle at EVERY size0..96,
across five member-record boundary lengths, two seeds and both insertion orders. All
four sources in both builds pass: each run checks 1,940 fixtures, 289,060 complete model
states and 86,570,560 exact-score results. The two existing fault types are detected on
the new matrix. This extends an existing suite; it does not increment suite/fault-type counts.

Its preregistered whole-output cross-build equality prediction FAILS. All 1,940 per-fixture
lines and all semantic totals match across eight runs; only the final physical-leaf and
reversal-opportunity counters differ between release and sanitizer builds. Each candidate
matches its control within each build. Allocator-dependent compaction is plausible, but
allocator and compiler/instrumentation differ together, so causality is unknown. The
original runner assertion, manifest and raw outputs remain; no rerun or weakened oracle.
An unused renamed original main also emits a missing-return warning; it is never called.

## Commands and evidence

Exact arguments, compiler flags, source/binary hashes and child stdout/stderr are in the
linked manifests. All commands ran locally from the repository root.

- HARNESS-005 `create.py`, `validate.py`, `faults.py`, `faults-continue.py`: validation
  passes; the initial driver-message mismatch is preserved and explained.
- COUNTERS-004 `run.py`: PASS, 96 structural children.
- AA-010 `run.py`, `analyse.py`: complete; six jointly qualified cells, two PARK.
- EXP-004/ordered-guards `prepare.py`, `validate.py`, `profile.py`, `analyse-profile.py`,
  `run.py screen`, `analyse.py screen`, `run.py confirm`, `analyse.py confirm`: complete;
  fresh guards pass, A/PARK unchanged.
- COUNTERS-005 `run.py`, `faults.py`, `audit-faults.py`: structural and semantic controls
  pass; the early-assertion classification is audited without reruns.
- BOUNDARY-014/compact-extension `run.py`: eight semantic children pass, post-run
  cross-build aggregate-equality assertion fails. `faults.py` and `audit.py`: PASS.
- `verify-round010.py`: PASS, 176 wall/thread intervals recomputed from raw rows,
  1,267 serial measurement windows, and 4,812 timestamped nonmeasurement commands
  disjoint from those windows. The compact extension is audited separately afterward.
- Final workspace/pristine-source, diff, public-curation and hash checks are recorded
  in ROUND-010-FINAL-CHECKS.json and ROUND-010-CURATION.json.

[Harness](HARNESS-005/README.md), [large-layout census](COUNTERS-004/README.md),
[qualification](AA-010/README.md), [ordered guards](../EXP-004/ordered-guards/README.md),
[compact recipe](COUNTERS-005/README.md),
[compact boundary extension](BOUNDARY-014/compact-extension/README.md),
[timing audit](ROUND-010-VERIFY.json), [method record](ROUND-010-METHOD.json).
Raw profiles and method responses remain in ignored scratch with hashes. Curated public
records contain no private machine paths or hostnames. Existing git denial was not retried.

## Decisions and next action

Campaign totals: **five harness revisions, eleven baseline explorations, nineteen additional
diagnostics, fourteen boundary suites / 28 distinct boundary fault types; four sequential
population rounds; zero accepted, two rejected, two parked optimizations.** Source selection
for adoption is NONE. All losing patches and the main baseline are preserved.

This round retains 1,248 measured rows, five prospective warmups, twelve profiles and two
calibrations: 1,267 serial measurement windows. No measured child failed or timed out.
Preparation/driver failures and the unsupported cross-build layout prediction remain visible.

Exact backend/model/cost are unknown; the supervisor records actual CLI usage separately.
The independent reviewer failed before execution. All reviews and fresh-seed confirmation
were by the coordinator and are explicitly sequential. CPU MCP ask and methods/code05/14
were consulted; irrelevant retrieved passages were not cited. Both evidence-checker calls
returned drop_number; no portable speed claim or M4 measurement is transferred.

Next concrete action: add COUNTERS-005's compact deletion history to a separate referee
revision, retaining exact scalar/API oracles, then freeze, profile and preregister A/A for
the small-tree workload. Do not time the source-included census as if it were the existing
separately compiled referee. Preserve recorded history-dependent widths. Alternatively,
investigate the compact extension's build-dependent physical counters with a predeclared
allocator/build diagnostic; do not relabel its failed equality prediction as passed.

Do not repeat unchanged mask6 duration/QoS/caller/placement trials or pool old/new checksum
harness timings. Both population stages remain mandatory for a new optimization hypothesis.
No source adoption, publishing, git retry, permission changes, supervisor/runtime/STOP edits,
or detached process. Keep the baseline for the separate morning review.
