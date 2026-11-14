# Historical server-command context

These results explain the original investigation target. They are the registered13November server comparison, not a new overnight measurement or a result for the later standalone source.

Compare Redis 8.10.3 at `1a2574ce1551d3de6e0b4a56756c0fdbc6659e4f` with squash `51e28c2a724a2632c0c75f376c352cd8aee37e0e`. Each host ran three 120-second measurements per version, with fresh same-host runs, GCC 15.2.0 on DebianBookworm, and `ZINTERCARD 2 ov:1 ov:2 LIMIT 0`: two distinct sorted sets containing the same 500 members. All 12 runs completed with zero failures.

| Host | Redis 8.10.3 median ops/s (observed range) | Squash median ops/s (observed range) | Median throughput change |
|---|---:|---:|---:|
| ARM | 56,480.00 (55,760.62–56,671.42) | 39,088.24 (38,955.44–39,374.61) | −30.79% |
| Intel | 48,586.45 (48,185.62–49,443.99) | 48,169.12 (47,822.52–48,963.35) | −0.86% |

“Overlap” compares observed minimum-to-maximum ranges, not confidence intervals. Intel ranges overlap, so these three repeats do not resolve an Intel regression. ARM ranges are separated. Percentages are throughput changes, calculated as `100 * (squash_median / GA_median - 1)`; they are not elapsed-time changes or comparisons between hosts. This establishes neither a cause nor performance across other commands/workloads.

The [selected12-value projection](results-projection.json) preserves every recorded ops/s value, recomputed medians/ranges and source artifact hashes. Original completion records remain private; machine identities and operational records are omitted. The projection was checked against the exact commit, metric, test, compiler and architecture labels. No benchmark was rerun to prepare this context.

No accepted overnight source or server integration changes these historical observations. Standalone lookup gains cannot be subtracted from this command-level gap to claim recovery.
