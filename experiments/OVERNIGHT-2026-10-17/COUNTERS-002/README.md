# COUNTERS-002 — query-order aggregate paths match

Four scoped Clang captures complete: AS,BS,AI,BI. All reset-boundary/entry-count checks
pass. Within each construction arm, S and I have byte-identical canonical exports of
every tree function count, coverage region and branch count. Each capture has exactly
1000000 lookup and SipHash entries; setup insertion and deletion entries are zero.

This rules out a change in these aggregate instrumented tree execution frequencies as
the explanation for the query-order contrast in this fixture. It does not measure time
per function, hardware instructions/cycles, cache misses or prefetch behavior. Different
construction arms do have some differing path counts; only within-arm S/I equality was
preregistered. Instrumented CSV timings are not comparative performance evidence.

[Plan](PLAN.md), [instrument patch](instrument.patch), [freeze](freeze.json),
[build command](build.json), [run/tool commands and raw hashes](manifest.json).
Per-cell directories contain CSV, tool stderr, function summaries and complete tree
count exports. Raw profraw/profdata/full exports stay under ignored scratch with hashes.
Installed Clang17 public reset/dump interface was inspected; root tree/source unchanged.

Decision: path-frequency control validated, not a time profile or optimisation.
Lookup qualification PARK, source NONE. Backend/model/cost unknown; supervisor records
CLI usage. Sequential coordinator review only; no independent confirmation claimed.
Future independent-query fixture A/A and capable time profiling remain necessary.
