# Iterator cache validation before screening

Baseline and A/B/C each pass 43 unchanged original tests, 1,920 iterator fixture cells across native and sanitizer builds, and 28,192 additional state checks per build. Every executable was freshly compiled against its own matching header. A uses24-byte iterator state; baseline/B/C use16. Tree ownership unchanged.

The extra oracle poisons state before all entry points, checks nullable outputs, both directions, copies, successful/failed seeks, sentinel paths, multi-leaf traversal, binary inline/external members, ties and exact signed zeros. Ordinary lexical bounds use equal-score trees, as required. Initial invalid unequal-score lexical expectation failed baseline and is preserved in attempt001-oracle. No existing checks were weakened; timing referee unchanged.

Both deliberate B faults are detected by ASan: omitted successful rank-seek reset and omitted forward leaf-transition reset. The latter proves the fixture changes offset-array geometry across a boundary. Fault sources are retained as patches and were never timed.

Independent root review434e39ef5 verified all11 reset paths, decoder equivalence, bounds and header tradeoffs. Exact patch/source/referee/build hashes are frozen in comparison-freeze.json. Fresh branch inspection: M1 4c48fa7ed, M6 b0aee7484, AMD f8eb45f6a, ARM234333797; current cache hypothesis distinct from their published targets.

Screen remains exploratory:100K primary A/A fails,1M qualifies. Fixed576-row order and300-second phase ceiling retained; a bounded partial result cannot select a winner. Full adoption guards, fresh confirmation and candidate profiles remain pending. Initial local validation-summary assertion used the wrong upstream output spelling (43 tests passed instead of43 passed); corrected without experimental reruns.

Public objdump and diagnostic log copies trim trailing whitespace; private remote originals retained. Initial publication whitespace check caught these before commit.
