# LOOKUP-001 independent-query profile

Status: referee preparation. Launch source is commit
77d32df82cd5da02b95c6afb6193fcf83f67223f, tree SHA256
d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
The new separate referee SHA256 is
7c37bb1b1fffa3dd0331179d0ae61f1cce554bc8a1f93eca389eec264a898aa2.
Its only semantic change to the baseline benchmark is a separate seeded
query permutation for lookup-hit and lookup-miss, including the hit checksum.
Construction and query permutations are independent. The source patch is
retained. No candidate comparison uses this referee before a separate
commit and baseline requalification.

Validate release and ASan/UBSan hit/miss checks at 10K, 100K and 1M where
feasible. Profile public hit and miss at 10K/100K/1M, 16-byte keys, with
the existing scoped in-process sampler as external attachment is denied.
Use 1,000 microsecond requested sampling, preserve raw PC logs locally,
summarize code regions without interpreting PC shares as exact time.
Inspect actual release assembly for zbtIndexFind and leaf-tag search.

The first six profile captures yielded fewer than 100 interrupted PCs each
(10–58). One bounded 10× operation-count capture per cell is allowed to
improve code-region coverage; retain both sets and do not use profiler
elapsed time as performance evidence. If coverage remains sparse, stop
profiling and report the limit.

A separate source-instrumented pass will count tag candidates and complete
member comparisons. It is diagnostic only; its durations are excluded from
timing results. If profile/code/counters support a new bounded hypothesis,
freeze both population steps and a full guard schedule before candidates.
The earlier EXP-006 inline scanner is an unchanged control, not a new idea.
No hashing or uniform-length assumption is allowed.
