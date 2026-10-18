# COUNTERS-008 — natural-wrap and colliding-SCAN reachability census

Preregistered execution-count diagnostic only; not CPU-time profiles, timed-loop
counters or speed evidence. Three serial baseline-only captures from final passing
snapshots: singleton growth wrap(two fixtures), multi-member wrap(four fixtures),
colliding scan(two fixtures). Compile-O1/debug with Clang profile instrumentation and
coverage mapping; unchanged source/allocator; run complete correctness oracle120s child.
All builds finish before captures. llvm-profdata merge and llvm-cov export remain local;
commit curated counts, commands and SHA256, not large raw files/private absolute paths.

Record function totals and branches for zbtIndexStartResize, zbtIndexCopyLeaf,
zbtIndexLeafMigrated, zbtreeAppendBatchFlush, zbtreeScan, zbtIndexScanGroup,
zbtIndexScanSlot and zbtLeafTagMatches. Resolve branch file IDs against each function's
filenames. Require actual skip-zero branch2(singleton)/4(batch), active batch flushes,
and scan collision-disambiguation and displaced-group callback paths nonzero. Map
exact statements; no inference that an unobserved path is impossible or a hot spot.
No counter modification, no production patch and no comparison timing. Preserve raw
captures and any failure. One baseline capture per fixture; no repeated measurement.
Source NONE and prior PARK remain; independent review not available.
