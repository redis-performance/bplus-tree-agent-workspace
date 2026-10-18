# DIAG-004 — ascending-insertion advantage not supported

Complete fixed48-process schedule, no failures/timeouts/exclusions; all checksums,
counts and per-fixture structure stable. The preregistered short-key advantage
criterion failed: ascending construction was slower in all six primary blocks.
Long-key observations also point in that direction. These are local fixture-history
observations, not source regressions or portable rates. Original hypothesis remains
not supported; no posthoc promotion of the opposite direction to a validated speed claim.

[Plan](PLAN.md), [patch](diagnostic-harness.patch), [freeze](freeze.json),
[build/smoke validation](validation.json), [commands/raw hashes](manifest.json),
[raw rows](raw/), [analysis](analyse.py), [descriptive table](SUMMARY.md).
Both release and ASan/UBSan smoke pass both orders and member lengths. Leaf count/min/max
come from read-only public iterator boundaries. Source and root referee unchanged.

Interpretation: this harness couples shuffled construction and lookup order. Ascending
construction changes that relation, leaf occupancy, tree allocation and allocation
history together. Fewer leaves alone does not establish faster lookup. The observed
long-key contrast motivates a new preregistered independent-query-order factorial
follow-up with fresh seeds, not a causal claim about caches or hashing.

CPU MCP evidence checker consulted: no_number for the qualitative result; frequency
unknown. Benchmark05/14 context as DIAG-003; no M4 observations transferred. Requested
QoS/opaque CPU IDs/thread time do not establish clock, residency or effective QoS.
No A/A requalification, independent confirmation, source candidate or population.
Lookup PARK, selection NONE. Backend/model/cost unknown; supervisor records usage.
All snapshots/evidence remain uncommitted pending morning review.
