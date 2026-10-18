# DIAG-010 — requested QoS intervention

Preregistered before measurement; new intervention, not an unchanged A/A retry.
One falsifiable hypothesis: requesting user-initiated instead of user-interactive
reduces short-hit process repeat variation by at least half. Both arms invoke the
same public setter once before fixture allocation, relative priority0. Same binary,
HARNESS-003 timed loops, independent query seed3209/construction seed3001,100000
members,10 operation-matched warmup passes. A=user-interactive; B=user-initiated.
Primary hit16,20000000 operations; secondary miss16,20000000 and hit/miss320,5000000.
Six fixed ABBA blocks per cell, rotating cell order by block;96 rows. One explicitly
recorded binary warmup hit16,1000000 operations,A, prospectively excluded. No settle
sleep added. Children<=120s,total matrix<=600s. No agent/build/test/profile overlap.

For each block/cell compute repeat distance d=abs(x1-x2)/mean(x1,x2) separately
for the two A and two B wall-ns/op observations. Support requires median(dB) <=
0.5*median(dA), dB<dA in>=5/6 blocks, and median(dB)<=0.01 for primary hit16.
If median(dA)==0 the reduction hypothesis is unsupported. Secondary cells descriptive;
no post-hoc replacement of primary. Report all ABBA mean contrasts, repeat distances,
raw integer wall/thread duration, boundary CPU IDs, QoS, checksums and tree bytes.
Controls:96 successful rows, exact fixture fingerprints/ops/checksums and invariant
owned bytes per cell, >=10ms measured duration, requested QoS observed at both bounds,
relative priority0,effective QoS unknown. Any failure makes support false. Preserve
all failures/rows; no outlier removal, adaptive counts, normalization or changed gates.

This does not qualify comparisons or prove core placement/frequency/cache mechanism.
Even if supported, a separate fresh A/A under the chosen request is required, with
unchanged[-1,+1]% precision interval gate. Both populations and all source acceptance
gates remain pending. No source mutation. Diagnostic wrapper in isolated snapshot,
base commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus frozen uncommitted patches.

CPU MCP ask consulted; unrelated passages not support. Benchmarks05/14 methods/code
read: retain checks and repeated raw samples;14 says "nothing pinned". No M4 Pro
measurements/numbering transferred. Installed pthread/qos.h explicitly describes
setter/getter as requested QoS; return errors are fatal with no permission retry.
Reviewer startup failed; sequential passes only. Exact backend/model/cost unknown.
