# H2 — metadata address dependency

The user expanded the campaign to six unattended hours,01:24:14–07:24:14UTC on14November, and multiple available OSS fleet hosts with separate controls. This supersedes the initial three-track work-budget limit, not evidence gates. H1 stays separate and measured serially; H2 implementation preparation may run concurrently off the fleet.

Select the second independently proposed hypothesis: metadata addresses currently depend on count×score_bits sizing/rounding before offsets/tags can be searched. GCC already eliminates duplicate source arithmetic; simple hoisting is not selected. Remove this dependency by caching score_bytes or changing within-leaf ordering, without helper-boundary, scanner or equality changes. Exact upstream ee8e7f701 and unchanged referee at e13d9fc88; each variant starts baseline, not an H1 candidate.

A caches uint16 score_bytes in an added leaf field. Its header may grow56→64bytes; this cost is declared before measurement and still must stay≤1% tree-owned memory in every case. B packs existing boolean/shift fields to make room for cached uint16 bytes while preserving node24/leaf56bytes and all shift0..63 semantics. C places offsets/tags before the packed score stream, preserving allocation footprint and external records, so their address no longer depends on score width. These test the same address-dependency hypothesis with distinct state/layout tradeoffs.

Require all count/score-width mutations, builds, repacks, in-place insert/delete, split/merge, duplicate/defrag and reversal semantics. Existing suites/oracles plus focused invariant tests must pass; preserve all failed artifacts. No fixture-specific cache values, hashes or lengths. No cached pointer requiring relocation fixups.

Primary six-case native discovery uses fresh new-lease72-row A/A (all18blocks pass), same exact ELFs/control environment and seed17. Update20000sweeps, other sweeps unchanged. Three ABBA blocks per case per eligible variant, serial per host.≥2% improvement every hitblock;≤1% demonstrated guard/memory regression; allrows≥250ms. GCC15 old cohort remains PARK. New hosts/cohorts need separate qualification and no mixed control effects. Any source acceptance still needs fresh confirmation, matched profiles, Intel guards and independent review.

## TMA classification

Baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring unavailable as qualified workload categories. CPU-wide raw labels lack continuous exclusion/formula qualification; children unavailable. The address dependency is directly visible in assembly, but no backend-bound claim is made. Mandatory actual cpu-perf reconsultation asks specifically about these three layout/cache options and mutation/footprint tradeoffs; source coverage limits remain disclosed.
