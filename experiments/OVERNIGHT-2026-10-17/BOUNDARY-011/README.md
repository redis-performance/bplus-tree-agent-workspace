# Active-resize clone oracle — passes

[Plan](PLAN.md), [commands/source hashes](manifest.json), [fault records](faults.json).
Twelve fixtures per build pass release/debug and ASan/UBSan:74 full model checks,
22 cloned pairs,6 active-resize clones,10 clones retaining free IDs,274718 owned
allocation observations. Original tree/referee unchanged. Two isolated faults caught.

The oracle inspects copy state before any draining lookup, sums usable bytes independently,
compares table contents and IDs, requires all owned pointers disjoint, verifies sorted
iteration/ranks/lookup/scan, mutates copies and exercises both freeing orders. Natural
resize/free-ID preconditions pass without private-state manipulation. Empty/presized/
previously populated clones included. Exact finite scores, signed zeros and binary lengths.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-011/run.py` passes both
builds/runs. `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-011/faults.py` built and
detected both faults, but its second expected-message check failed: shallow external
ownership was caught earlier by the owned-byte accounting check. Original failed driver,
stdout/stderr/patches retained; [read-only review](fault-review.json) verifies the earlier
assertion. No weakened check, source/test change, rerun or fabricated successful driver.

New test [clone_resize_oracle.c](../../../tests/clone_resize_oracle.c), isolated source
snapshots under scratch; uncommitted provenance and base commit in manifest. No timing
claim or optimisation. Sequential review only, independent confirmation pending.
