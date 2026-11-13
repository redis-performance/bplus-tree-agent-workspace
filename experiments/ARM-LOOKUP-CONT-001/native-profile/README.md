# Matched native baseline profile

Exact qualified native ELF, source ee8e7f701, GCC13/O3/noLTO, hostlibc2.39, CPU2 affinity asserted, no running containers. Wholeprocess captures include setup/warmup. Leaf41.38%, raw21.77%, SipHash7.65%, namedmemcmp2.82% usercycle sample shares; no lost samples. Binary text95143bytes. Raw perf data retained privately by checksum; sanitized reports/assembly/commands/counters published.

## TMA classification

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring unavailable as validated workload categories. The actual topdown-profiler-generated perf command uses CPU-wide `-a -C2`, not process attribution; continuous occupancy exclusion and underlying formula qualification are absent. Raw exploratory labels retained unchanged. Candidate and children unavailable. Sample shares, instructions and IPC do not replace slot categories. This baseline supports a call-boundary/code-generation hypothesis, not a pipeline-bottleneck causal claim.
