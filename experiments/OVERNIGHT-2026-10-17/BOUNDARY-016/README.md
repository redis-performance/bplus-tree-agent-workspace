# Packed insertion/deletion overlap oracle — PASS

All eight baseline/A/B/C native and ASan+UBSan cells pass with identical output.
Each checks 146,250 operations: 67,860 insertions and 78,390 deletions across every
valid position in the selected counts, widths0..64 and two fixed seeds. There are
128,160 cases spanning multiple move chunks, plus 2,250 zero-width and 2,250 full-width
cases per cell. The complete-buffer digest is f1e55fd35eece517 everywhere.

The oracle builds the expected result bit by bit from an immutable original buffer,
independent of the source's packed readers/writers. It checks all 824 data/spare/canary
bytes, the unchanged original count/width, and the exact cleared deletion tail. This
tests private integer streams, without feeding NaN to any score API. It complements
the decoder geometry and public mixed-score mutation suites.

Both intentional source faults compile and fail the byte oracle: copying overlapping
insertion chunks in the wrong direction, and writing ones into the deletion tail.
No baseline defect observed. No earlier source/test/referee was changed.

[Plan](PLAN.md), [exact commands and hashes](manifest.json), [summary](summary.json),
[fault patches and commands](faults/manifest.json), [additive oracle patch](oracle.patch).
All snapshots are isolated under ignored scratch/overnight-boundary-016. Provenance
is base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit uncommitted hashes.
No git retry, publishing, timing claim or source adoption. Sequential review only;
backend/model/token cost unknown. Sixteen boundary suites / 32 distinct boundary fault
types now validated. Optimization, population, harness and baseline counts unchanged.
