# BOUNDARY-009 — batched-score oracle passes

Release/debug and ASan/UBSan each pass526590 batch calls/7883000 requested score slots,
12 complete model/ordered-iterator checks, two hash seeds and28 batches beginning with
natural active resize. All2^count input hit/miss combinations for every count0..16 are
exercised before/after mutations, alongside duplicates, empty/raw/binary members, exact
finite scores and signed zeros, caller-buffer copies, clone lifetime and output canaries.
Missing-score output values are deliberately unspecified; hit bits/scores and writes
outside the requested count are checked. Read lookups may advance rehash; tests do not
mistake the resulting allocation change for a bug.

Both predeclared intentional faults build and are detected by their specific oracle:
wrong result bit and wrong output score slot. These are sensitivity controls, not source
bugs or candidates. No baseline defect was found. [Plan](PLAN.md), [manifest](manifest.json),
[validation commands](run.py), [fault outcomes](faults.json), and source/oracle patches
preserve exact provenance, flags, stdout/stderr and hashes. Main source/referee unchanged.

Decision: nine additional boundary suites validated,18 detected fault controls overall.
Source NONE/lookup qualification PARK; optimisation/population counts unchanged. Sequential
coordinator review only; independent review and commit-based morning review remain pending.
