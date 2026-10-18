# Scoped batched lookup profiles

Both known-arithmetic calibrations and all eight preregistered captures pass sample,
resolution and overflow checks. Long-key hit captures are led by SipHash; mixed short
batches are led by memchr with substantial index/leaf lookup work. These are descriptive
interrupted-PC counts, not unbiased time shares, PMU data, or throughput comparisons.

[Plan](PLAN.md), [driver](run.py), [manifest](manifest.json), [summary](summary.json)
and [instrumentation patch](profile.patch) retain commands, hashes and full distributions.
Raw PCs, symbols and diagnostic binaries stay under ignored scratch with checksums.
Every capture is confined to the work loop; dump follows timing endpoints. Sampler
stop overhead still affects instrumented thread time; no timing enters A/A tables.
Frequency/effective QoS/migration/aliasing/perturbation remain unknown. No M4 transfer.
Source NONE; relevant AA-012 subsets qualify, other original guards remain PARK.
