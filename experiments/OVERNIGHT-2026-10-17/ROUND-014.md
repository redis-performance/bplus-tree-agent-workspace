# Round 14 — public lifecycle, active relocation and natural wrap

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
Three new correctness suites and two extensions pass. Four branch-count captures
clarify recovery coverage. No timing benchmark, harness revision, baseline qualification,
optimization or population ran. Main source remains the unchanged baseline.

Round began at 03:24:48 UTC; deadline is 03:54:48 UTC and handoff cutoff is 03:53:18 UTC.
All experimental children have finished. This is not the final campaign round; the
final worker still owes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work

| Work | Passing source/build cells | Coverage per cell |
|---|---:|---|
| [BOUNDARY-019](BOUNDARY-019/README.md) | 8 | 4 fixtures, 32 model checks, 293,132 exact public results; public retirement, deferred IDs, active allocation and later reuse |
| [BOUNDARY-020](BOUNDARY-020/README.md) | 8 | 4 fixtures, 32 model checks, 284,714 exact results; relocation during resize, retired defrag cursor recovery and exact allocation visits |
| [Fresh mutation extension](BOUNDARY-020/mutation-extension/README.md) | 8 | 8 fixtures, 448 model checks, 15,054,526 exact results; 1,536 mutations during active resize and 24 header resets |
| [Shrinking extension](BOUNDARY-019/shrink-extension/README.md) | 8 | 4 fixtures, 88 model checks, 574,384 exact results; mixed-table scans, EOF cursor, cloning and ID reuse |
| [BOUNDARY-021](BOUNDARY-021/README.md) | 2 baseline cells | 2 seeds, 131,080 natural resizes, two actual 65535→1 generation wraps and 274 model checks |

The first four rows cover baseline and retained EXP-004 A/B/C, each native/debug
and ASan/UBSan. Generation wrap covers baseline only; variants and full high-water
model checks are not claimed. Eight deliberate fault runs detect five new distinct
fault types plus three repeated controls. No production bug was observed.

[COUNTERS-007](COUNTERS-007/README.md) and its separate
[shrinking capture](COUNTERS-007/shrink-extension/README.md) complete four whole-oracle
execution-count captures. They observe repaired member cursors and retired defrag
cursor recovery. The shrinking fixture reaches EOF fallback eight times; the freed
member-cursor condition stays zero. These are not CPU-time profiles or proof that
an unobserved branch is unreachable.

All 43 original tests pass in each of eight source/build cells. The [read-only
audit](ROUND-014-VERIFY.json) passes 2,863 file hashes and 120 serial command windows,
including four count captures disjoint from builds/tests. Raw branch counts are
recomputed; source, support and prior immutable evidence remain unchanged.

## Failures and evidence

The first lifecycle fixture incorrectly required a stale member cursor; removal
explicitly repairs it. The first mutation fixture could decline the header move
needed for reset coverage. Both failed snapshots remain. Revised plans correct or
strengthen these new fixtures without weakening production assertions or existing
checks. A fault-generator preflight failure is also retained.

Use mapped branch records: the first snippet helper mishandled macro file IDs.
Mutation output field `final` means quiescent allocation visits, not member count.
No execution was repeated solely to fix that label.

Exact commands, flags, timestamps, stdout/stderr, hashes and patches are in the linked
manifests. Entrypoints are the run/fault scripts, explicit attempt002/attempt003 scripts,
`BOUNDARY-019/original-tests.py`, COUNTERS run/analyse scripts and `verify-round014.py`.
`python3 scripts/check-workspace.py --pristine-source` and `git diff --check` pass,
including the final documentation checks. [Sequential review](ROUND-014-REVIEW.md)
records limitations. No child remains active.

## Decision and handoff

Totals: **6 harnesses, 12 baseline explorations, 27 diagnostics, 21 boundary suites,
41 distinct boundary fault types; 4 sequential populations; 0 accepted, 2 rejected,
2 parked optimizations.** This round adds three suites, one diagnostic and five
new fault types. Baseline commit remains `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c`
plus explicitly uncommitted isolated snapshots. All losing patches remain.

CPU MCP ask and methods/code 05 and 14 were consulted. Its broad TailBench retrieval
was irrelevant and is not used as support. The checker returned `no_number` for
the qualitative no-speedup statement. No M4 numbering, frequencies or results transfer.

Exact backend/model/token cost: unknown; the supervisor records CLI usage separately.
Reviewer startup failed, so confirmation and review are sequential coordinator passes.
Frequency, effective QoS, migration within a window, independent review and committed
provenance remain unresolved. No publishing, protected git retry, credential inspection,
runtime/STOP edits or permission changes occurred.

Next: the [growth-side generation-wrap fixture](ROUND-014-NEXT-FIXTURE.md), using
public reserved construction to reverse resize parity, requiring actual growth-wrap
and new-leaf coverage plus full high- and low-water models. The recipe is untested.
Performance needs distinct qualification; do not repeat failed protocols unchanged.
