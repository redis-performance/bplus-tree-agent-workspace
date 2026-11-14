# H8 classification candidates: statically eligible, timing not admitted

All three independent variants pass correctness and independent source review. Actual ARM native and target LTO lookup code satisfies the frozen classifier, hash-before-pointer, helper-boundary and stack-frame gates. C initially lacked target generic consumer coverage; separate unexecuted build artifacts and a supplemental independent review close that gap. These findings do not establish speed or acceptance.

- A: [source](reviews/H8-A-CODE.md), [actual ARM code](reviews/H8-A-ARM-CODEGEN.md).
- B: [source](reviews/H8-B-CODE.md), [actual ARM code](reviews/H8-BC-ARM-CODEGEN.md).
- C: [source](reviews/H8-C-CODE.md), [lookup audit and initial gap](reviews/H8-BC-ARM-CODEGEN.md), [generic consumer supplement](reviews/H8-C-CONSUMER-CODEGEN.md).

[ARM/Intel native and target build evidence](H8-codegen/PUBLICATION.json) joins original and rendered text. Actual binaries remain private. Candidate correctness artifacts likewise preserve their original and published hashes after operational path normalization. No accepted baseline or referee was modified.

The separate profiler-off timing collector was prepared with a mandatory complete-Q4-PASS dependency. [Q4 failed](Q4-RESULTS.md), so this collector is **NEVER ADMITTED**. Its eleven synthetic offline tests do not qualify a real host or candidate, and the prepared collector has not received independent admission review. No H8 timing, candidate profile or source selection occurred. The population remains unmeasured and adds no completed timing attempt.

Original H2 remains PARK; H7 remains statically rejected. A qualified ARM measurement condition is still required before this H8 screen can run. No threshold waiver or unchanged failed-condition retry follows the static results.
