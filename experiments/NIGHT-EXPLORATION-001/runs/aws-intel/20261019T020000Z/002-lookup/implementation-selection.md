# Intel SIMD lookup population: REJECT / NONE

All three implementations slow successful lookup in every block at both primaries. The100K primary was A/A-qualified;1M was unqualified. Effects are batch-average elapsed time, positive is slower. No candidate qualifies for confirmation. Memory is identical in all108blocks. Raw audit reconstructed432rows and108effects with serial CPU2 boundaries.

| Cell | Variant | Minimum% | Median% | Maximum% |
|---|---|---:|---:|---:|
| lookup-hit-10000-16 | A | 11.363 | 12.479 | 13.965 |
| lookup-hit-10000-16 | B | 9.350 | 9.707 | 14.132 |
| lookup-hit-10000-16 | C | 8.020 | 9.173 | 12.109 |
| lookup-hit-100000-16 | A | 10.518 | 11.870 | 13.529 |
| lookup-hit-100000-16 | B | 8.525 | 9.236 | 11.391 |
| lookup-hit-100000-16 | C | 8.110 | 10.613 | 13.241 |
| lookup-hit-1000000-16 | A | 9.202 | 9.654 | 10.132 |
| lookup-hit-1000000-16 | B | 8.684 | 8.994 | 9.805 |
| lookup-hit-1000000-16 | C | 2.836 | 3.891 | 4.374 |
| lookup-miss-10000-16 | A | -2.627 | -1.952 | 3.850 |
| lookup-miss-10000-16 | B | -2.822 | -0.968 | 0.655 |
| lookup-miss-10000-16 | C | -3.138 | -1.118 | 3.602 |
| lookup-miss-100000-16 | A | 0.711 | 1.272 | 1.726 |
| lookup-miss-100000-16 | B | 0.074 | 1.048 | 2.033 |
| lookup-miss-100000-16 | C | -0.154 | 0.251 | 1.024 |
| lookup-miss-1000000-16 | A | 0.209 | 0.607 | 0.758 |
| lookup-miss-1000000-16 | B | -0.694 | -0.256 | 0.406 |
| lookup-miss-1000000-16 | C | -0.032 | 0.184 | 0.479 |

Correctness: each candidate43original tests in native and sanitizer builds,144independent-query fixtures, and2,433,536first-match/page cases per native/sanitizer/forced-fallback mode. These are separate counts; fallback is compiler-branch testing on Intel, not another architecture. No full long-key/mixed/batch timing guards or fresh confirmation ran because all candidates fail the primaries.

Independent root static review at main038248c1 found no bounds/semantic blocker, including collision suffix calls and C overlap masking. Profile evidence is instrumented whole-process gprof plus release assembly; PMU counters unavailable. The proposed inline scanner removes/reduces memchr calls but produces a clear public-lookup slowdown. No claim that instruction count alone explains it.

Both population steps were three sequential passes by one native worker, not independent proposer/implementer agents. Exact backend/model and token/USD costs unknown. All three losing patches retained. Root source stays unchanged. Next target: separate update-path referee/profile; do not repeat rejected SIMD/SWAR scanners as a new hypothesis.
