# COUNTERS-006 — allocator-capacity / compiler factorial

Preregistered before new executions. The prior compact BOUNDARY-014 prediction of
cross-build aggregate layout equality failed. Hypothesis: reported allocator capacity
changes compaction decisions; fixing that capacity policy removes build-dependent
physical-layout differences on this matrix. This is structural evidence, not timing.

Use unchanged baseline source SHA256 d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2,
base commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus uncommitted snapshots.
Freeze all files before builds. Root adapter/referee/source and old evidence stay intact.

Full factorial: ambient unchanged allocator, controlled exact requested payload capacity,
controlled capacity rounded up to 16 bytes; each at O1/O3 and native/ASan+UBSan.
Twelve builds/runs, fixed order policy then optimization then instrumentation. Repeat
no cell. Same assertions, compiler, hash function and matrix. All children <=120 seconds.
All runs serial. No performance numbers or A/A inference from these diagnostic binaries.

Controlled adapters keep aligned capacity metadata before the returned payload, allocate
at least reported capacity, preserve realloc contents, and route SDS frees through the
matching free. Metadata and hidden libc slack are excluded from reported tree payload
capacity: these values are NOT comparable tree-owned-memory guards for optimization.
Ambient cells retain the exact original adapter. Unit checks cover 0..8192 requested
bytes, alignment, full-capacity reads/writes, realloc growth/shrink and SDS free ownership.
Unit children run before semantic children. ASan checks the real underlying allocations.

Retain unchanged semantic checks from zero_physical_oracle.c; append deterministic
per-fixture layout/capacity hashes and physical counters, never pointer addresses.
Enumerate every n=0..96, bytes=16/253/254/319/320, seeds=31121/31123, both insertion
orders: 1,940 fixtures, 289,060 complete model checks and 86,570,560 exact results/cell.
No existing check removed. Omit the unused original main in the new generated wrapper.

Prediction supported only if (1) all semantic/unit checks pass, (2) each controlled
policy gives identical per-fixture structural outputs across all four compiler/build
cells, (3) ambient reproduces a native/sanitizer difference at each optimization level,
and (4) changing exact to rounded capacity changes at least one physical-layout result.
Otherwise record unsupported/inconclusive with all rows preserved. A supported result
establishes capacity-policy sensitivity in this diagnostic, not that every prior difference
has a unique cause; pointer placement and metadata overhead also differ from ambient.
If supported, inspect first differing fixture using a separately declared trace followup.

CPU MCP ask returned tangential passages, not evidence for this hypothesis. Methods/code
05 and 14 consulted; no M4 measurements/core mappings transferred. Existing timer/QoS
observability remains unchanged. Independent reviewer startup failed before execution;
review here is sequential, exact backend/model/cost unknown. No new population/adoption.
