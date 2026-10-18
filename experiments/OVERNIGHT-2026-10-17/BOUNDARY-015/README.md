# Mixed finite scores and allocator capacity — PASS

All 24 predeclared cells pass: baseline and retained EXP-004 A/B/C, ambient/exact/
16-byte-rounded capacity, O3/debug native and O1/debug ASan+UBSan. Each cell checks
96 fixtures and 2,751 model states. Logical digest be91811078f52d30 agrees everywhere.
Each also passes all 43 original tests. The two new isolated source faults are detected:
corrupting a finite score's low bit and silently skipping a changed numeric score.

Both controlled policies produce byte-identical complete oracle output across all
eight source/build combinations. Ambient physical outputs differ, consistent with
COUNTERS-006; ambient equality was not required. All cells cover zero/partial/full
score widths, shifted deltas, forward/reversed leaves, and leaf-count increases and
decreases. These are observed transitions, not exact counts of named split/merge helpers.

The independent scalar decoder reads each packed bit without the source's bit helpers,
then checks exact finite-score bits against a separately sorted model. The public oracle
also covers binary/empty/long members, signed zeros, both directions, all optional-output
masks, lookup/raw/batch lookup, rank and score seeks, score counts, linked-leaf IDs,
recursive subtree counts, complete settled scans and read-only memory equality. Clone
mutation does not change its original. Controlled adapters assert zero outstanding
allocations after each fixture. They remain diagnostics, never timing or memory guards.

The first attempt failed an invalid exactly-once SCAN assertion. Its frozen files and
outputs remain; the [erratum](SCAN-PRECONDITION-ERRATUM.md) cites the local contract and
existing tests that permit duplicates. Attempt 2 checks every emitted member/value and
complete coverage while allowing legal duplicates. No existing test was weakened.

[Plan](PLAN.md), [driver](run-attempt002.py), [manifest](attempt-002/manifest.json),
[raw-derived summary](summary.json), [fault patches and commands](faults/manifest.json).
Frozen snapshots live under ignored scratch/overnight-boundary-015-attempt002; the new
oracle patch is retained alongside the manifest. Exact commands, output hashes, binary
hashes, source hashes and timestamps are recorded. Base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c
plus explicit uncommitted snapshots; protected git is not retried.

Decision: one additional validated boundary suite, two new fault types. Source NONE;
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged. No optimization population, timing claim
or source adoption. Review is sequential after reviewer startup failure; backend/model/
token cost unknown. Separate morning commit and independent review remain pending.
