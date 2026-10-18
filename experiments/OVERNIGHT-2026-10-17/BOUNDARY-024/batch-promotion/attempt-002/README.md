# Corrected alternating batch lanes

The only oracle change from the retained initial trial is `1+i%2` to `1+(i/4)%2`.
This makes four repeated lanes alternate IDs1 and2 as intended. All other tests and
parameters remain frozen. Discovery uses seed75503/debug; fresh confirmation uses
seed75521 without REDIS_DEBUG. Both use all four sources and native/ASan-UBSan builds.

All eight discovery and eight fresh-confirmation cells pass. The repeated stale-cache
fault is detected by ASan heap-use-after-free. See manifest.json, summary.json and
confirmation/ for exact outcomes.
The fixed fixture checks exact result masks and current score bits, count0..16 canaries,
negative/positive zero, duplicate/missing members and actual promotion inside a16-lane
zbtreeScores call. SCAN intervals/anchors, current sorted models and external ownership
checks remain. Missing output lanes are not constrained.

The sensitivity fault caches the current table before batch lookups, then uses that
cache after normal lookup finishes migration. It represents a stale-table fast-path
assumption, not a discovered production defect. All raw outputs, patch and source hashes
are retained; private absolute paths in sanitizer output are curated with originals
kept under scratch. Source NONE and all existing performance PARK remain.
