# Round 12 — mixed-score invariants and process-history sensitivity

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
Two new boundary suites pass; neither timing diagnostic establishes a precision remedy.
The main tree, header, adapter, root benchmark and original test entry point are unchanged.
No new optimization population was started and no candidate was adopted.

Round began at 02:39:50 UTC; deadline 03:09:50 UTC, handoff cutoff 03:08:20 UTC.
The last measured child ended at 02:56:41 UTC. Subsequent work is read-only auditing,
review and evidence curation. This is not the final campaign round: a later worker must
write MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed experiments

BOUNDARY-015 extends the prior allocator-capacity diagnostic to mixed finite-score
mutations. All 24 baseline/A/B/C × ambient/exact/rounded-capacity × native/sanitizer
cells pass 96 fixtures and 2,751 model states each, including 2,721,586 exact-score
comparisons. Every cell also passes the original 43 tests. Logical digests agree
everywhere; complete outputs agree across all eight cells within each controlled
capacity policy. Ambient physical outputs can differ, as preregistered. The oracle
checks independent scalar packed decoding and sorted public-API results through
updates, clone mutation, range deletion, refill and minimum-edge draining.

The first attempt failed a new, invalid exactly-once SCAN assertion. SCAN explicitly
permits duplicates even after rehash settles. That failed snapshot and all output remain;
the corrected additive oracle validates every callback's member and exact value and
requires complete coverage. Existing tests were not weakened. Both planned new source
faults—corrupting a finite low bit and skipping a changed numeric update—are detected.

BOUNDARY-016 adds an independent out-of-place bit reference for private packed insertion
and deletion. All eight baseline/A/B/C native/sanitizer cells pass 146,250 operations
each: 67,860 insertions and 78,390 deletions, including every position in the selected
counts and widths0..64. Complete-buffer equality checks untouched bits, spare bytes,
canaries and cleared deletion tails. All outputs match. Both overlap-direction and
tail-clearing faults are detected. This is integer-stream validation, not NaN score input.

DIAG-014 tests the workload of the immediately preceding fresh process. Discovery
completes 96 target +96 predecessor rows plus one prospective warmup. The alternating-zero
score-plus-length target meets its directional criterion on both seeds; the integer
no-output target does not. A separately preregistered mirrored-label confirmation uses
two fresh seeds and a same-predecessor placebo: another 96 target +96 predecessor rows
plus warmup. Both repeated contrast bounds pass, but one placebo interval fails precision.
The joint robustness criterion therefore **PARKS**. No timing policy is adopted.

DIAG-015 tests a distinct fixed idle interval between predecessor exit and target launch.
All 144 target +144 predecessor rows plus one warmup pass functional and duration controls.
The predeclared attenuation criterion is **unsupported**: neither idle contrast nor
placebo qualifies, and neither paired interaction clears its bound. No row is removed
or protocol repeated. These interventions do not establish frequency, cache or placement
causality and do not replace any source guard.

## Commands and retained evidence

Exact argument vectors, flags, seeds, timestamps, stdout/stderr and file/binary hashes
are recorded in the linked manifests. All measured children ran serially, bounded to
120 seconds; no build/test/profile or independent agent overlapped them.

- [BOUNDARY-015](BOUNDARY-015/README.md): `run.py` retains the initial failed oracle;
  `run-attempt002.py`, `analyse.py`, `faults.py` pass the corrected matrix and controls.
- [BOUNDARY-016](BOUNDARY-016/README.md): `run.py` and `faults.py` pass all eight cells
  and both fault controls, with deterministic complete-buffer digests.
- [DIAG-014](DIAG-014/README.md): `run.py`, `analyse.py`, `confirm.py`,
  `analyse-confirm.py` complete their fixed schedules; joint robustness PARK.
- [DIAG-015](DIAG-015/README.md): `run.py` and `analyse.py` complete; criterion unsupported.
- [Read-only audit](ROUND-012-VERIFY.json): `verify-round012.py` passes, independently
  recomputing all 32 wall/thread intervals and validating 675 measurement windows
  disjoint from 122 build/test/fault windows, raw hashes and frozen sources.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`: PASS.
  [Sequential review](ROUND-012-REVIEW.md), [method provenance](ROUND-012-METHOD.json)
  and final SHA256/curation record accompany the report.

The source base remains a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicitly uncommitted
isolated snapshots. Patches, source hashes and losing variants remain intact. Protected
git actions are not retried. No publishing, upstream changes, private credential lookup,
permission changes, runtime/STOP edits, detached processes or source adoption occurred.

## Decision and next action

Campaign totals: **six harness revisions, twelve baseline explorations, twenty-three
additional diagnostics, sixteen boundary suites / 32 distinct boundary fault types;
four sequential population rounds; zero accepted, two rejected, two parked optimizations.**
This round adds 672 diagnostic rows plus three warmups, two boundary suites and four fault
types. No harness, baseline or optimization count is added. All measurements completed.

Independent reviewer startup failed before execution, so confirmation and adversarial
review are explicitly sequential. Exact backend/model/token cost are unknown; the
supervisor records CLI usage separately. Clock, effective QoS and within-window migration
remain unknown. CPU MCP ask, methods/code05/14 and its evidence checker were consulted;
the checker returned drop_number. No portable speed headline or M4 measurement is used.
The method record corrects an extra -Werror in the checker prompt: the actual frozen timing
build never used that flag, and no binary or result changed.

Next concrete action: preregister a **coordinator-bookkeeping placebo diagnostic**.
DIAG-014 defers hashing/manifest work until target exit, but that work can still alter the
next predecessor's starting conditions. Compare buffered bookkeeping after a full block
with the current per-pair serialization, preserving crash-safe raw rows, fixed child
commands and all observations. Measure coordinator CPU/launch gaps directly and keep
wall time primary. This is an untested follow-up, not a remedy. Alternatively use a
separately qualified runner. Do not repeat unchanged warmup, idle-gap, duration, QoS,
caller or placement trials, pool harness versions, or substitute for the original guard.
Keep main source at baseline for separate morning review.
