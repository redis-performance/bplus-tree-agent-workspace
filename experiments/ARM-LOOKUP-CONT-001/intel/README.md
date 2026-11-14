# Intel baseline evidence

Both compiler cohorts pass their independent 72-row A/A qualification (18/18 blocks each). They are separate host/compiler cohorts, never pooled with ARM or each other. Raw controls are in `qualification/`.

Corrected v3 baseline profile captures pass the independent scope, scheduling, formula and partition audit in [INTEL-TMA-BASELINE.md](../reviews/INTEL-TMA-BASELINE.md). That report includes all four total-slot roots and eight measured children, intervals/ranges, tools and limitations. These are bounded CPU-wide workload attributions and unweighted means of interval percentages; counters and samples have process-user scope. No candidate or ARM resource cause is inferred from these baselines.

The first native launch exceeded the frozen sweep limit and aborted before collection; its raw capture is unusable. The second launch's first raw capture was valid but the inline parser failed on advisory text. V3 retains that first capture byte-for-byte and collects only the remaining two under an identical binary/workload, plus auxiliary captures. GCC15/LTO has three fresh captures. Original failed attempts remain, with a companion correction to the first launch's inaccurate termination flag. See INTEL-COHORT.md for the predeclared repair and quality gates.

Original-byte checksums identify private raw artifacts, including perf.data. Public files sanitize owned directory paths; their separate published hashes describe those copies. No invalid capture is included in the qualified means.
