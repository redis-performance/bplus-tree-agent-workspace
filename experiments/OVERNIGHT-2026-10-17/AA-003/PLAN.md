# AA-003 preregistration — independent query fixture

Written before measurement. Hypothesis: HARNESS-002 independent-query fixture has
sufficient local repeatability for the existing +/-1% descriptive A/A precision gate.
DIAG-005 warrants decoupled fixture coverage; it does not predict a noise cure. This is
a new fixture, not a rerun of coupled AA-001/002. No source change or source comparison.

Freeze: HARNESS-002/freeze.json and release binary hash recorded in manifest before
runs; base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit uncommitted referee
patch over HARNESS-001. Root source/referee preserved. Commit review pending.
Apple M1 per established campaign metadata, 4P+4E installed, one thread, no SMT,
16GiB, macOS26.3, Apple Clang17; -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3;
libc allocator, original assertions/SipHash, no LTO/fast-math/QoS/affinity change.
Clock, turbo/DVFS state, effective QoS and within-window residency unknown. Boundary
CPU IDs are opaque and thread CPU time is explanatory; no M4 constants transferred.

## Fixed schedule and gates

100000 members, fresh fixture/hash/construction seed503, query seed701, independent
query mode, 10 fixed full query warmup passes per child. Four cells:

| Cell | Case | Member bytes | Operations |
|---|---|---:|---:|
| hit16 | lookup-hit |16|20000000|
| miss16 | lookup-miss |16|20000000|
| hit320 | lookup-hit |320|5000000|
| miss320 | lookup-miss |320|5000000|

Six ABBA blocks using identical executable A/B, rotating cell order by(block-1)%4;
96 measured fresh processes/rows. One separately recorded binary warmup before the
matrix: hit16,1000000 ops, excluded prospectively. All children <=120s, matrix <=600s.
No builds/tests/profiles/local agent computation overlap. Incomplete cells cannot
qualify. Failure/timeout stops matrix and remains evidence. No outlier removal,
optional stopping, adaptive counts, thresholds or post-hoc chosen cells.

Wall elapsed_ns/operations primary. Per-cell six effects:100*(mean(B)/mean(A)-1);
95% descriptive Student-t interval,df5,t=2.5705818366147395. All24 rows valid, each
window>=10ms, operations/checksum/tree bytes/construction and query fingerprints
invariant; whole interval must lie in[-1,+1]%. Same gate as AA-001/002, no relaxation.
Report median/min/max/CV, all block effects, thread/wall ratios, boundary IDs and QoS.
Full permutations imply hit checksums999990000000(short) or249997500000(long);
miss checksum0. Python fixture oracle separately validated fingerprints/partial passes.

No cell is accepted source performance; qualifying cells permit only scoped follow-up.
Matching time profiles, qualified guards, both population stages, fresh confirmation,
unchanged memory and adversarial review remain mandatory. Failure means PARK, then
new diagnostic or boundary work, never repeat this unchanged schedule.

CPU MCP ask and benchmarks05/14 methods/code consulted. Retrieved Roofline passage
irrelevant; Google Benchmark timer passage only clarifies CPU timer scope. No source
passage claims independent queries fix precision. Reviewer-agent startup failed before
execution; sequential coordinator passes only. Backend/model/token cost unknown.
