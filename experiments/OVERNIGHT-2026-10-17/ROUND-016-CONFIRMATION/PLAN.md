# Fresh-seed, debug-disabled confirmation

Separate fixed confirmation of final external-ownership and narrowing oracles. No
production source changes and no timing runs. Exact successful source/test/support
snapshots from external-extension and narrowing-extension/attempt-002; preserve files,
change only input arguments and omit REDIS_DEBUG at compilation. All oracle CHECK and
unconditional serverAssert remain. Both -O3 native and-O1ASan/UBSan, original allocator.

External seeds69501/69503 × all3intervention modes × control/A/B/C × both builds =48cells.
Narrowing seeds69521/69541 × control/A/B/C × both builds =16cells. Total64fixed cells,
120schildren,600swhole serial schedule. Freeze before builds; failure stops and remains.
Require existing coverage and semantic checks, equal logical digest per case/seed/mode
across sources/builds, clean sanitizer/runtime stderr, unchanged frozen files. Physical
allocator counts may differ; each cell must pass its own exact accounting invariants.

This adds seed and build-flag coverage, not independent-agent confirmation or performance
guard qualification. Prior debug-enabled results remain; no changed timing assertions.
SourceNONE/performancePARK unchanged; no new suite/diagnostic/population count.
