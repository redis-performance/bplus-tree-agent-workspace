# COUNTERS-002 — query-order path-frequency controls

Preregistered after DIAG-005. Four scoped Clang source-count captures, seed211,
100000 members,320-byte keys,1000000 hits,10 warmup passes. Cells AS,BS,AI,BI exactly
as DIAG-005. No timing comparison; instrumented CSV times are noncomparable and never
added to benchmark results. No denied process inspection retry or permission change.

Hypothesis/control: complete-permutation lookup queries over a fixed read-only tree
execute identical aggregate tree-function/region/branch counts for S and I within
construction arm. Compare every exported function, region and branch count belonging
to zset_btree.c, not only selected functions. Any difference is retained and investigated;
it cannot be removed or normalized. Calls/regions are execution frequencies, not time,
cycles, cache misses, stalls or proof of a causal runtime mechanism.

Copy the DIAG-005 snapshot; insert public Clang reset immediately before timed operation
clock, dump after wall/thread/CPU/QoS observations and before verification/cleanup. Read
installed Clang17 profile/instr_prof_interface.h: reset clears counters; dump prevents
exit re-dump. Check exact lookup entry count and zero insertion/deletion counts. Tree
source remains unchanged. All four cells serial, no build/test/agent overlap; children
<=120s. Save raw profraw/profdata/export under ignored scratch, public hashes, commands,
stdout/stderr and function/count summaries. Freeze patch/source/build provenance first.

Same -O3 compiler flags plus -fprofile-instr-generate -fcoverage-mapping. Backend/model
cost unknown; coordinator review only. Does not satisfy required time-profile validation,
precision qualification, independent confirmation or either population stage. Source NONE.
