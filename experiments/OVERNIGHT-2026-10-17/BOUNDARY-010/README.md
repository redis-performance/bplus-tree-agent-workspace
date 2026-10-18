# BOUNDARY-010 — guarded raw-buffer oracle passes

The corrected test passes release/debug and ASan/UBSan: four seed/alignment fixtures,
33 lengths spanning empty through65536 bytes,260 guarded mappings,652 raw queries and
12 complete ordered/model checks per build. Buffers are read-only during raw operations,
then overwritten/unmapped before further tree checks and cloning. Zero-length right-
aligned buffers point at the inaccessible guard and are never dereferenced. Binary
prefixes, exact finite scores and signed zeros remain intact.

Both planned faults are detected: a one-byte overread terminates at a guard page, and
truncated hashing fails the expected raw-lookup assertion. Neither is a baseline defect.
No baseline source bug was found. Root source/referee unchanged;10 boundary suites and
20 detected fault controls overall. Source NONE/lookup qualification PARK unchanged.

The initial test build failed because its standalone include list omitted string.h.
That source snapshot, compiler errors, manifest.json, oracle.patch and run.py remain
untouched. The only test correction added the required declaration header; no assertion
or fixture weakened. Final evidence is [manifest-final.json](manifest-final.json),
[run-final.py](run-final.py), oracle-final.patch and final-* logs. Fault results and both
patches are in [faults.json](faults.json). The initial failure is not counted as a pass.
[Predeclared plan](PLAN.md) preserves both fixtures and fault choices.

All work local with test-owned mmap/mprotect allocations. No external inspection,
permission change or publishing. Sequential review only; exact backend/model/cost unknown.
