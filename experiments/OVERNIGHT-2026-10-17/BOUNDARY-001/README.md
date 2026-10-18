# BOUNDARY-001 — exact finite-score and collision oracle: PASS

New standalone sorted-vector oracle: tests/boundary_oracle.c. Release with debug
assertions and ASan/UBSan both pass all 12 fixed fixtures, 24576 mixed mutation steps
and 1356 full oracle verifications per build. No baseline source bug was observed.
Includes raw tags0/1/255, embedded NULs and empty members, lengths around319/320/321,
exact finite score bits and both zero signs, ordered iteration/rank/seek, batch scores,
scan coverage with duplicates, reserve, duplication, insert/update/delete/edge/range.

Four intentional faults each compiled and were rejected by the oracle (SIGABRT):
signed-zero normalization at exact-bit check; binary-NUL truncation at membership;
rank offset at rank check; skipped320-byte scan callbacks at coverage check. See
[MUTATION-PLAN.md](MUTATION-PLAN.md), [mutations](mutations/) and [runner](mutate.py).
These are test-strength controls, not optimisation variants or population members.

[Plan](PLAN.md) and [manifest](manifest.json) preserve exact compiler commands, source
hashes and exit status; stdout/stderr are alongside them. Individual children bounded
to120 seconds. Main source and prior frozen referee snapshots unchanged.

Decision: additional local regression coverage validated; no source optimisation.
Algorithmically independent model, same coordinator; not independent-agent review.
Backend/model and token costs unknown; supervisor accounts for CLI usage.
