# Structural census and counter support diagnostic

No source is selected. The baseline census closes the proposed negative cache as NONE for the six fixed workloads. The separate counter diagnostic stopped at its support probe; no measurement captures ran. H2 and Q4 remain PARK, and H8 timing remains unadmitted.

## Structural counts

The original seed 17 fixtures ran once per case on four admitted instrumented baseline binaries: ARM and Intel, each native and target LTO. All 24 outputs pass the frozen model checker. Corresponding raw outputs are byte-identical across all four builds. Every original leaf lookup executes; shadow state only counts prior failed visits. Clock-denial wrappers prevent entering a timing path.

There were zero repeated failed leaf lookups in every case. The primary hit fixture has 489 successful home hits and 11 filter evaluations among 500 queries. Those observations provide no opportunity for the proposed per-table-call negative cache in these fixtures. The exact home-filter table remains NONE for implementation under the current primary objective: target LTO already bypasses filter arithmetic on successful home hits, and the diagnostic does not measure the remaining path's cost. Counts are not speed estimates.

Coverage is limited to these warm seed 17 fixtures, narrow IDs, and inactive resizing. Other seeds, tree sizes, and mutation histories are not characterized. The four matching grids establish cross-toolchain consistency rather than independent workload populations.

- [Independent final review and complete count table](reviews/PROBE-CENSUS-FINAL.md)
- [Source and parser review](reviews/PROBE-CENSUS-CODE.md)
- [Exact fleet artifact review](reviews/PROBE-CENSUS-FLEET-CODEGEN.md)
- [Raw results and build text manifest](probe-census-results/manifest.json)
- [Frozen preparation protocol](probe-census/PROTOCOL.md)

## Counter diagnostic support failure

A separately reviewed collector attempted one support probe using the unchanged target baseline, seed 43, and the fixed nine-event perf command. The workload exited successfully and returned the expected model. The frozen parser rejected the output before D0; none of the four planned measurement captures ran. The attempt is consumed, with no parser change or retry.

The output contains both per-CPU verbose reads and aggregate verbose reads. The parser recognized only the former. It also expected task-clock in milliseconds, while the observed command emitted its raw count with an empty unit under `--no-scale`. The code and source reviews missed these output forms. Thirty offline tests passed but did not establish installed-tool support. This failure provides no variance characterization and cannot explain the earlier Q4 failure.

- [Independent final support-failure audit](reviews/VARIANCE-FINAL.md)
- [Independent code review](reviews/VARIANCE-CODE.md)
- [Frozen protocol](diagnostic-variance/PROTOCOL.md)
- [Raw support output](diagnostic-variance-results/support.counters.csv)
- [Stopped result](diagnostic-variance-results/result.json)
- [Publication manifest](diagnostic-variance-results/manifest.json)

Preparation files retain their historical PREPARED status and exact hashes. This report records the later attempt without rewriting the admitted protocol. Published operational paths are normalized; manifests distinguish original and published hashes. Private service and process snapshots remain retained with their hashes. Actual ELF files remain private.

## TMA classification

| Category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | Unavailable | No candidate |
| Bad_Speculation | Unavailable | No candidate |
| Backend_Bound | Unavailable | No candidate |
| Retiring | Unavailable | No candidate |
| Child categories | Unavailable | No candidate |

The census collects logical path counts. The support probe does not provide a qualified pipeline-slot funnel. No category is inferred from counts, assembly, ratios, or another machine.

These diagnostics add no measured optimization population, replication, or qualification. The ledger remains 47 completed attempts: 25 PARK, 22 REJECT, and zero approved. Original sources and referees are unchanged. Further work addresses bounded portability correctness coverage; it cannot replace failed performance gates.

The ARM host was released after these diagnostics. Independent read-only verification confirms the original coordinator resumed, the saved profiler affinity was restored, all recovery timers are inactive, and no owned work or containers remain. Intel remains reserved for the bounded portability checks.
