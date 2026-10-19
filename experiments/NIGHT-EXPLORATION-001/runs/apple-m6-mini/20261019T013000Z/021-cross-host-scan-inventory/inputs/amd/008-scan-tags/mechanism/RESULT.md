# Matched mechanism diagnostic: partial support, speed magnitude unresolved

One predeclared diagnostic of fixed-priority A versus baseline completed03:31:36–03:31:59UTC on CPU2,180-second cap. Both sizes100K/1M, seeds1/2/3, original1Mrequested scan operations and16byte members;12 counter captures and12 sampled captures. FIFO controller enables after build/warmup immediately before timer and disables after elapsed read. It includes small controller/timer edges, excludes construction/warmup and post-checks. Prior disabled-zero/enabled-positive control is preserved under002-lowerbound. Diagnostic source, binary/raw-profile hashes, commands and all counters/sample summaries retained; large raw profiles remain local.

| Metric, median A/base change across3seeds |100K|1M|
|---|---:|---:|
| User cycles |−0.683%|−0.826%|
| User instructions |−12.151%|−11.579%|
| User branches |−12.079%|−11.932%|
| User branch misses |+4.764%|+5.154%|

All counter events reported100% running (no multiplex scaling). Every capture matches checksum/actual operations/tree-owned bytes across versions and modes, CPU2. Exact assembly contains bounded unaligned16byte loads, byte-equality comparisons and movemasks, replacing portable word-mask work. Thus reduced instruction/branch work has direct support. Increased branch misses are observed, but no measurement attributes them to a specific instruction or proves they explain the cycle result.

Same-IP inclusive helper attribution, aggregated across3seeds:100K baseline36.545%→A32.329% of periods,63→56 helper events from199→198 total;1M30.562%→29.924%,75→77 helper events from269→270 total. Nested inline symbols overlap and must not be summed. These are small sample counts and approximate attribution, not a precise causal allocation of savings.

**The diagnostic does not validate the exploratory4–5% elapsed magnitude.** Its cycle changes remain below1% and sampled1M helper share barely changes. The instrumented referee is a separate binary: scan-slot entry is0x10f80 versus0x10da0 in timing binaries, changing within-cache-line alignment. Controller overhead, layout and sampling perturbation are plausible limitations, not established explanations. No extra sampling, timing or tuning is authorized to resolve this discrepancy inside this frozen round. Preserve every result rather than replacing the fixed screen with diagnostic elapsed times.

PARK/NONE remains unchanged: failed primary A/A, incomplete performance guards, no qualified implementation winner, pending independent replication/adversarial review. No source adoption overnight.
