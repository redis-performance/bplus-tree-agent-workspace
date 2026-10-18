# BOUNDARY-012 — changing iterator masks after mixed mutations

New correctness coverage: change optional-output mask on every Next, exercise nonzero
reverse values1,-1,2, copy live iterators and advance copies independently, seek every
rank after mutations. Do not use iterators/member pointers across tree edits: recreate
all iterators after every mutation. Exact finite score bits include signed zero,
subnormals,packed integer boundaries,large finite values and ties; binary keys include
empty/prefix/NUL lengths straddling319/320/321. Independent sorted model drives checks.

Fixed sizes97,513;seeds8303,8311;4096 seeded mixed updates/deletes/reinsertions per
fixture;full verification every16 operations and after final deletion. Four exact
EXP-002 source variants control/A/B/C,release/debug and ASan/UBSan. This adds correctness
coverage,not performance rows,source acceptance or independent review. Two isolated C
fault controls: Boolean-only reverse guard mishandles -1/2;wrong next-leaf start pos.
Preserve all source hashes,commands/stdout/stderr/failures;no existing checks weakened.
