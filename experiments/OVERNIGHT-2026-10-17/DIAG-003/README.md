# DIAG-003 — repeated-order advantage not established

Completed all24 preregistered windows in six serial process blocks, with no failures,
timeouts or exclusions. Release and ASan/UBSan smoke passed both window orders.
Exact lookup counts/checksums, access permutations and tree memory validated. The
fixed repeated-order advantage criterion failed; no fixture-order remedy established.
A/A lookup PARK and source selection NONE remain. No optimisation/population added.

[Plan](PLAN.md), [instrument](diagnostic-main.c), [patch](diagnostic-harness.patch),
[freeze](freeze.json), [build/smoke commands](validation.json), [run manifest](manifest.json),
[raw windows](raw/), [analysis](analyse.py), [descriptive results](SUMMARY.md).
The added access arrays change the baseline working set; these are not original
HARNESS-001 timings. I reshuffles per pass but reuses its precomputed stream per window.
Physical array assignment and scheduling order alternate together; no separate layout
causality inferred. Two windows per arm per process are clustered, not24 independent
samples. A block contains visible dispersion; all observations retained as planned.

CPU MCP ask and benchmark05/14 methods/code consulted. Retrieved HdrHistogram/general
repeatability passages do not support the access-order hypothesis; it is a local,
falsifiable design. Benchmark05 states "Every pass is printed as a SAMPLE line";
benchmark14 states "nothing is pinned". Those are method context only, no M4 results
or CPU-number mappings transferred. Sources:
https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/05-measurement-pitfalls/bench.c
https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/14-pcore-vs-ecore/bench.c
Evidence checker consulted: no_number for qualitative conclusion; clock unknown.
Its heuristic missed explicit one-thread/compiler context. No portable performance,
frequency, migration-free residency, effective QoS or causal cache claim.

Independent reviewer startup failed before any agent ran; sequential coordinator
review only. Backend/model/cost unknown; supervisor records CLI tokens. Uncommitted
snapshot provenance retained; root source/referee unchanged. Next: controlled index
probe/tombstone and saved-insertion-position boundaries, not another identical trial.
