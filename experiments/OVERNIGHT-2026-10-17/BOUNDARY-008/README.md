# BOUNDARY-008 — append-batch ownership and flushes validated

All18 fixtures/162 full model checks pass release/debug and ASan/UBSan. Both planned
faults fail: borrowing inline caller bytes loses lookup correctness, and omitting final
flush loses length. Source target and frozen root referee remain unchanged.

[Plan](PLAN.md), [oracle patch](oracle.patch), [commands/source/raw hashes](manifest.json),
[fault controls](faults.json). New test source: tests/append_batch_oracle.c.
Two hash seeds,three key distributions,three existing-tree prefixes. Reusable caller
buffers are overwritten immediately after Add/AddWithHash; exact binary member and
signed-zero bits must survive Finish. Empty/partial/count/byte flush boundaries, exact
precomputed hashes, natural active resizes, ordered iteration, ranks, scans and clone
ownership are covered. Per build:346 observed count flushes,3650 byte flushes,89014 Adds
starting with active rehash. Observations read private fields; all edits use public APIs.

Sequential coordinator review only; backend/model/cost unknown. Uncommitted snapshot
awaits morning review. Eight added boundary suites/16 fault controls now validated.
No performance claim, accepted optimisation or population; source NONE/lookup PARK.
