# ARM count-one decoder preparation

This is a private decoder microbenchmark, not a public iterator or whole-tree optimization. The control is unchanged root source8fab511e plus the exact frozen EXP-007 B bulk helper and EXP-008 control policy. The referee remains EXP-008 kernel.c and the existing bench/decoder_bench.c; no root files change.

Fresh baseline build, native/sanitizer referee tests and count-one profile precede proposals. Baseline profiling uses width60, forward, count1, 64 leaves; the existing driver caps rounds at65536. Three baseline calibration observations will target at least50ms per sample, preserving the cap limitation. If count-one windows cannot reach10ms, strict qualification fails; do not change the cap after viewing candidate results.

Conditional primary: width60/forward/count1. Initial fixed screen guards: widths0/8/31/57/58/59/61/62/63/64 at count1, both orientations; width60 counts2/4/7/8/16/32/96. Full guards remain all widths0/8/31/57–64, both orientations, all eight counts, empty/partial ranges, finite exact bits and signed zero. Same materialized output and checksums for all variants. Count1 fixtures can be seed invariant; fresh seeds are not new input diversity.

Only count==1 may use the scalar path; counts2+ retain frozen bulk behavior. Cutoffs4/8/16 are prior rejected EXP-008 directions and will not be repeated. Three proposal/chair passes and three isolated implementations will be explicitly sequential if no agents are available. At least2% improvement in every primary confirmation block, qualified controls and no>1% guard/memory loss are required. No source adoption overnight. Every timing phase is bounded300seconds and uses sixABBA blocks, discovery seeds1/2/3 and fresh101/102/103 if justified.

## Root control and conditional interpretation

`base` means the historical, unadopted EXP-007 B bulk decoder appended to the unchanged source, plus the EXP-008 control policy. It is not the current root implementation. `root` adds only the existing EXP-007 scalar range adapter, which invokes unchanged zbtScoreLeafScore for every output, to the same source. Both use the identical materialized-output referee. Shared driver, allocator and hashing objects are identical.

Root control is built and validated in both modes, profiled, and retained beside B in calibration and comparison. Any fallback gain relative to B remains conditional on adopting B; it does not establish a root or whole-tree improvement and does not remove EXP-007 historical guards.
