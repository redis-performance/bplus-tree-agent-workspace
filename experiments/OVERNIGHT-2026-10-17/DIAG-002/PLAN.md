# DIAG-002 preregistration — dependent-add brackets around lookup

Written before build and measurement. Distinct diagnostic after AA-002 lookup failed.
Hypothesis: a common execution-rate factor contributes enough observed variation that
adjacent dependent-add durations positively track lookup durations. This is not a clock
measurement, attribution proof, precision remedy or substitute for wall-time A/A gates.

Isolated snapshot of HARNESS-001 unchanged tree/support plus diagnostic harness only;
base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c, uncommitted provenance. Root harness frozen.
Apple M1, installed4P+4E cores, one thread, no SMT,16GiB,macOS26.3. Apple Clang17,
-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3,libc,unchanged asserts/hash.
No affinity/QoS/policy changes. Frequency, residency and effective QoS unknown.

Use one million16-byte members, seed1, shuffled lookup-hit, ten warmup passes, four
successive fixed5000000-lookup windows/process, six fresh serial processes:24 windows.
Each lookup window bracketed by exactly128000000 dependent integer adds before/after.
Eight explicit AArch64 add instructions per loop iteration; require returned count
exact and inspect emitted assembly before timing. No GHz/cycle conversion: instruction
latency, loop overhead, scheduling and placement are not separately established here.
Record wall/thread times and CPU IDs for all three regions, actual requested QoS,
checksums, tree bytes, fixture parameters and load averages. Wall lookup time primary.

Exactly one small correctness/sanitizer smoke (1000 members,10000 lookups,two windows,
80000 adds) per build is excluded prospectively. Recorded normal-fixture binary warmup
one process (four windows) excluded prospectively, then six measured processes. All
children <=120s, full schedule <=300s. No concurrent build/test/profile/agent activity.
All rows/failures preserved, no outliers, optional stopping or adaptive counts.

Before analysis freeze: X=mean(pre/post wall ns/add), Y=lookup wall ns/op; compute
Pearson r over all24 windows and CV(Y/X)/CV(Y). The diagnostic criterion is r>=0.70
AND normalized-CV ratio<=0.50 with all counts/checksums/memory stable, all regions>=10ms,
all24 windows valid. Report process-mean correlation and within-process ranges as
limitations, not substitute criteria. If criterion fails, common-rate explanation not
established; retain A/A PARK. If it passes, motivate a new independent diagnostic only:
no normalization applied to acceptance timings. Correlation cannot identify DVFS and
nearby brackets do not establish clock/residency during lookup.

Method inspiration: CPU Performance Engineering benchmark14 code uses dependent-add
brackets, thread CPU time and CPU IDs (read via MCP). No M4 numbers or ID mapping used.
https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/14-pcore-vs-ecore/bench.c
Backend/model/cost unknown. Single coordinator, independent agent startup unavailable.
