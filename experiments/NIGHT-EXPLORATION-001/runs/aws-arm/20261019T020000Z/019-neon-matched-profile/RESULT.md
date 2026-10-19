# Exact-binary matched ARM profile result

The generated fold-predicate reconstruction is materially sampled in rejected
implementation B: **17.67% of timed-call-site sampled period at100K and16.87% at1M**.
The preregistered diagnostic support thresholds pass at both sizes. This identifies
measurable work in the generated predicate; it does not establish the causal share
of the55–79% regression, predict a replacement's performance, or rescue population017.
The population remains **REJECT, source NONE**. No new candidate was implemented.

| Source | Size | Timed samples | Whole zbtIndexScanSlot period | B predicate period | Predicate samples |
|---|---:|---:|---:|---:|---:|
| Baseline | 100K | 1261 | 92.47% | Not applicable | Not applicable |
| Baseline | 1M | 1608 | 87.44% | Not applicable | Not applicable |
| B | 100K | 2264 | 95.54% | 17.67% | 400 |
| B | 1M | 2496 | 92.27% | 16.87% | 421 |

B predicate seed1/2/3 percentages are17.73/18.16/17.11% at100K and17.25/17.94/15.40%
at1M. The70 exact instruction addresses (35 in each forward/reverse loop) were frozen
before capture from018. Only sampled instruction IPs count, not descendant/ancestor
rollups. The candidate-specific predicate map is not applied to baseline addresses;
zero placeholder fields in machine-readable baseline rows mean not applicable.
Whole zbtIndexScanSlot includes ID, migration and later decode work and is explicitly
not labeled as only the all-match helper.

## Scope and controls

All12 full-process captures and16 plain/disabled controls completed in one42.8-second
CPU2 job, well within the600-second cap. All52 command outcomes passed. Exact existing
baseline869425ed and B1e584193 timing binaries and all pinned source/referee hashes
matched before and after. No build, source change, duration adjustment or retry occurred.
All28 CSV rows pass exact fixture/output/actual-operations/owned-memory/traversal/warmup
parity; all start/end CPU2. Four disabled controls report zero/not-counted cycles.
Seven frozen parser controls pass. perf reports zero lost samples in each capture;
the only nonempty stderr is the four expected `Events disabled` messages.

The PMU covered the entire process. The analysis was post-filtered by exact physical
main return PC0x1d1c (+0xe04) for timed scan_count; PC0x1ea8 (+0xf90) identifies scan_verify.
It is not physically timed-only PMU capture. Of17482 unfiltered samples,7629 are timed,
2129 verification,7654 other and70 incomplete; none are ambiguous. All sampled
zbtIndexScanSlot events were assignable to the timed or verification caller, satisfying
the90% per-capture gate. Other/incomplete stacks remain in full raw text and per-sample
classification. None are silently counted as timed or discarded from the accounting.

Raw perf.data remains on the runner with hashes/byte sizes in profiles/result.json;
all unfiltered textual callchains, full-process reports, stderr and classifications
are published. analysis/summary.json and capture-summary.json retain separate source,
size and seed results. No source/host pooling or instrumented elapsed-time comparison
supports this report. Sampling skid, attribution boundaries, dependency overlap and
unequal instruction cost limit causal interpretation. Reported loss0 does not prove
perfect sampling. Independent root review remains the next gate; runner is idle.
