# HARNESS-003 — miss-operation warmup, locally validated

A separate isolated referee revision over HARNESS-002: lookup-miss now performs
misses during its fixed warmup, with the same query permutation/count and assertions.
Other warmups retain their existing successful-lookups behavior. A new warmup_case CSV
column states the actual operation (none for insertion). No claim that all cases have
operation-matched warmup. Timed operation bodies and their semantic checks are unchanged.

DIAG-008's fresh-seed intervention supports this fixture improvement; it does not prove
precision or identify a hardware mechanism. AA-004 preregisters fresh A/A before any
candidate comparisons. Main source and root HARNESS-001 referee remain untouched.

Both release/debug and ASan/UBSan validation pass:43 retained upstream tests, all3
original referee test groups,80 all-case query fixture cells/build plus explicit warmup
metadata checks. Independent Python oracle reconstructs query/construct permutations,
partial-pass checksums and exact traversal/count invariants. Commands/stdout/stderr and
source hashes in [validation.json](validation.json), [freeze.json](freeze.json), saved
patch and scripts. No weakened test or replacement of the frozen upstream entry point.

Decision: third locally validated harness revision, qualification pending AA-004.
Source NONE, optimisation/population counts unchanged. Uncommitted isolated snapshot
provenance; protected git not retried. Commit-based acceptance and independent review
remain pending morning review. Backend/model/token cost unknown.
