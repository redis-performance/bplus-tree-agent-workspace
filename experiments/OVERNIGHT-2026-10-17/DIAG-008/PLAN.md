# DIAG-008 — operation-matched warmup intervention

Preregistered before build/measurement,2026-10-17. DIAG-007's overall phase hypothesis
failed; miss16 alone met its cell criterion. Its warmup uses successful lookups for
both hit/miss measurements. This motivates a controlled intervention with fresh seeds,
not a claim that the prior phase pattern was caused by cache state or frequency.

Hypothesis: warming the actual miss operation reduces early/late phase drift relative
to equally many successful-lookup warmup operations. One binary, same tree/hash/query,
same16 contiguous measurement windows; A performs10 hit warmup passes, B performs10
miss warmup passes. Fixed counts, not time-controlled settling. Both arms check every
warmup result; total operations identical, warmup durations can differ and are recorded.
No code path or checks differ during measurement. No clock/QoS/affinity intervention.
This tests the warmup-operation bundle; it cannot isolate elapsed warmup time, cache,
branch training, frequency or placement. It is not a source optimisation or A/A gate.

Primary cell miss16; secondary contrast miss320. Fresh construction/hash seed1723 and
query seed1861. Each process100000 members,16 windows x500000 misses,10 warmup passes.
Same independent-query driver derived from DIAG-007; only warmup selector/metadata and
seed change. All source/support snapshots/hash checks unchanged at baseline. Root intact.

Schedule six blocks, both cells/block, ABBA per cell, cell order short/long on odd
blocks and long/short on even blocks.48 processes/768 windows. No normal-sized discarded
warmup process. Smoke n997,ops1999,4 windows: both hit/miss measured cases,16/320bytes,
query seeds1861/1871 and both warmup modes in release and ASan/UBSan. Smoke excluded
prospectively; all observations/checks preserved. Children<=120s, full campaign<=240s.
No concurrent local builds/tests/profiles/agents. No optional stopping/outlier removal.
Failure/timeout stops with incomplete status; no retry on same schedule.

For each process r=mean(first4 wall ns/op)/mean(last4 wall ns/op). Within each block,
pA=mean(two A r values),pB=mean(two B r values),contrast=pA/pB. Primary support requires
median(six contrasts)>=1.02, at least5/6 contrasts>1, AND median(six pB) in[0.99,1.01].
All768 windows must be>=10ms, gap fraction<=1%, checksums0, matched memory/counts and
fingerprints for each cell, no failed child. Otherwise unsupported/inconclusive, not a
relaxed gate. Secondary cell does not rescue a failed primary. Record all24 process
phase ratios/cell, six contrasts, means/dispersion, absolute early/late costs and observed
thread/CPU/QoS. All windows clustered, no pretend768 independent observations. No row
filtered by CPU IDs/thread share. Qualification remains PARK even if hypothesis passes;
a distinct frozen-referee revision and fresh A/A would still be required.

Apple M1 ARM64, established4P+4E/16GiB/noSMT inventory; one thread, macOS26.3, Apple
Clang17,C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer,libc allocator, assertions/hash
intact. Clock/turbo/effective QoS/within-window residency unknown. Boundary IDs opaque.
MCP ask/methods05/14 already inspected this round; evidence checker before headline.
No M4 values transferred. Source base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus
explicit uncommitted harness/diagnostic snapshots, no protected-git retry. Sequential
coordinator review only; agent startup failed. Backend/model/token cost unknown.
