# BOUNDARY-002 — score bounds and ownership: PASS

New tests/score_boundary_oracle.c passed release/debug and ASan/UBSan. Each build
checks two insertion directions, 1352 score-range deletions on independent clones,
and2706 full bound/ownership verifications. Caller member buffers are poisoned and
freed after insertion. Clone deletions leave original exact members/scores intact.
Inclusive/exclusive forward/reverse seeks, rank results, score counts and deletes
are compared with a sorted-vector model over13 finite boundary scores. Empty members,
embedded NULs, inline/external lengths, exact signed zero and subnormals are included.
No NaNs and no source changes. No baseline bug observed.

[Plan](PLAN.md), [manifest](manifest.json) and adjacent stdout/stderr contain exact
commands, source hashes and successful exit status. Child bounds120 seconds.
Decision: additional regression coverage validated; no optimisation/population count.
Single coordinator, not independent-agent review. Backend/model/token costs unknown.
