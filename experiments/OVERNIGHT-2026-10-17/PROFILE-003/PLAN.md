# PROFILE-003 — traversal bottleneck coverage

Prior short-key iterate/scan cells qualified AA-001, but traversal time profiling was
blocked by external sample permissions. Public self-process sampler now exists; this
is a new profiled target, no retry of denied external profiling or failed lookup matrix.
No candidate/proposal before profile evidence and new scoped baseline qualification.

Frozen isolated HARNESS-003 plus DIAG-006 corrected stop/dump sampler and DIAG-009
calibration driver. Source, allocator, flags/assertions unchanged; only instrumentation.
Compile release and sanitizer; all-case tiny smoke both. Known-function calibrations
1000/3001us,400m iterations each; >=20 samples and >=90% known function required.
Then12 fixed captures:seed3407/query3607 and seed3803/query4001, each requested interval
1000/3001us, cases scan16,scan320,iterate16,100m requested visits each,100000 members,
10 warmups. All sequential, child<=120s,total captures<=240s. Preserve failures and all
PCs; no optional stopping or discarding samples. Symbolicate own executable with atos.
Report counts, unresolved symbols, requested/effective operation counts, checksums,
owned bytes and wall time. >=30 samples per capture for coarse descriptive coverage.

No unbiased profile proportions/cycles/frequency claim: DIAG-009 showed delivered rate
can differ from requested cadence. Sampling overhead/aliasing remain unknown; prior
lookup perturbation cannot transfer to traversal. Thread endpoint precedes dump, but
boundary syscalls still affect interval. Separate uninstrumented A/A required; never
reuse instrumented timings as source speedups. Root source/referee preserved, provenance
uncommitted. All agents idle; reviewer startup unavailable, sequential audit only.
