# COUNTERS-010 — actual score-move paths in mixed-width fixtures

Preregistered execution coverage only; no CPU-time/profile hotness or speed claim.
After both BOUNDARY-024 matrices pass, run two fixed serial unchanged-control captures:
inline seed70501 and external seed71503. Copy their frozen manifests exactly into new
isolated snapshots. Compile O1/debug with Clang profile-instr-generate/coverage-mapping
and unchanged allocator; execute once each, bounded120s. Merge/export with available
xcrun llvm-profdata/llvm-cov; preserve hashes of raw data locally and mapped source
branch counts publicly. No benchmark, build or other child overlaps either capture.

Require normal oracle PASS, UpdateScore260calls each, external detach path reached
only in external fixture, and both in-place and delete/reinsert score paths observed.
Inspect zbtIndexMove's copied-target, destination relabel and old-to-new insertion
branches. Their counts include construction/mutations/verification, not only score
moves; source/target observations in the oracle provide phase-specific coverage.
Map LLVM branch file IDs before quoting source snippets. Retain failures, don't
substitute whole-process counts for measured time or qualified performance guards.
SourceNONE; existing PARK remains. Models/backend/token costs unknown.
