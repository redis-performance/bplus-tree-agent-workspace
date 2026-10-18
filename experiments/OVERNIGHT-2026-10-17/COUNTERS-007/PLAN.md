# COUNTERS-007 — whole-oracle lifecycle branch census

Preregistered execution-count diagnostic, not CPU-time profiling or a performance
claim. The first BOUNDARY-019 plan incorrectly assumed leaf removal leaves a stale
member-rehash cursor. Source removal instead repairs it. Determine which recovery
paths the three corrected public-API oracles actually execute; avoid claiming
coverage just because a source comment describes a defensive path.

Three serial baseline-only whole-process captures: BOUNDARY-019 attempt002,
BOUNDARY-020 base, BOUNDARY-020 mutation-extension attempt002. Exact frozen source/
referee/adapter copies, -O1 -DREDIS_DEBUG -fprofile-instr-generate -fcoverage-mapping.
LLVM public instrumentation/export only, no source counters inserted. One execution
of each fixed oracle schedule,120s child, whole360s. No builds/tests/other profiles
overlap a capture. All current correctness children must finish before first capture.

Preserve raw profraw/profdata/export locally with hashes; curate all regions/branch
counts for RegisterLeaf,ReleaseLeafId,RemoveLeaf,RehashStep,DefragStart,DefragStep,
and LeafById, plus relevant public entry counts and source-line snippets. Assert
oracle semantic PASS, unchanged source/binary hashes, expected fixture count4/4/8,
public mutation counts nonzero, defrag entry counts zero for lifecycle-only and
positive in both relocation fixtures. Classify observed member-cursor repair,
free-ID reuse condition, retired-defrag recovery, and freed-member-rehash-cursor
branch separately. A zero count is absence in these schedules, not a proof of
unreachability. Whole-process setup and model helper calls included. No cycles,
time fractions or replacement of required baseline time profiles. No source adoption.
