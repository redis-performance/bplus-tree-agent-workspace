# Scoped lookup path counts — equal across batch sizes

The installed Clang17 public reset/dump interface was inspected and used directly.
The scope calibration exports0before/20inside/0after calls, confirming that setup and
post-dump work are excluded. All16 captures pass expected API/query counts, original
checksum/memory checks and scoped zero counts for tree insertion/free.

For each seed, control/C and prefetchon/off have identical zbtIndexFind and leaf-search
function/branch counts at batch1 and16. Hash/SipHash counts also agree. Each window
contains32,768index queries. Leaf searches are33,048 for seed83103 and33,040 for83111;
additional searches arise in the index path, not an operation-count discrepancy.
API calls are32,768 at batch1 versus2,048 at batch16. C helper branch counts agree
between batch sizes. Whole owned bytes agree across all8conditions per seed.

This rules out a changed logical path census for these fixed streams under instrumented
builds; it does not explain time, branch prediction, cache residency, code placement,
frequency or migration. No timing numbers from these builds are usable candidates.
Raw profraw/profdata/export files stay in ignored scratch with hashes in manifest.json.
Public *-counts.json resolves every LLVM branch file ID to its source snippet.
The distinct scope model is recorded; older whole-process profiles are not reinterpreted.

SourceNONE, EXP-006C/PARK and all old guard failures remain. Adds one diagnostic,
total34. No harness/baseline/population count change. Sequential review only; exact
backend/model/token cost unknown. All experiment children completed successfully.

[Post-hoc helper census](HELPER-CENSUS.md) retains branch-flow conservation and distinguishes source word examinations from machine loads. It also shows that equal-length filtering cannot remove comparisons in the current fixed-length streams. No new capture or count change.
