# Corrected-adapter member-index profile

COMPLETE; independent raw audit PASS. No source candidate or performance claim.

All 16 original cells are represented exactly once: lookup-hit, lookup-miss, rank and scan at 100K/1M, seeds 1/2. Each requested 10M operations with 16-byte members and three warmups. Scan callback accounting retains actual operations. All captures exceed the fixed 10-observation minimum and are uncapped.

All 2,469 observations are conserved: 1,422 program text, 1,037 external libraries and 10 import stubs retained with unknown targets. See [independent audit](INDEPENDENT-CAPTURE-AUDIT.md), [raw-derived summary](summary.json) and [source/assembly map](hot-region-map/MAP.md). Locations do not measure cycles, stalls, cache misses or unbiased time shares.

The initial 019 attempt preserves three successful captures and its incomplete metadata result. The separate reviewed 020 repair reconstructs those captures offline and executes only the 13 unstarted cases. Combined capture wall time is 18.689094 seconds; the metadata repair pause is separately 931.704861 seconds. All owned children are reaped; all 53 original and 86 continuation identities remain unchanged. No capture was repeated.

Scan accounts for 417 observations: 367 in ScanSlot, 26 in ScanGroup, 17 in hashing, 5 callbacks and 2 tree-scan observations. Within ScanSlot, 184 observations fall in the inlined scalar tag-matching ranges. The hottest instruction has line-zero debug attribution, so no exact source-statement cost is claimed. Rank's child-count reduction already uses NEON. External memchr accounts for 402 hit and 521 rank observations; these counts do not establish that replacing it is beneficial.

The source-proposal review is separate in 022. Source selection remains NONE and completed optimization counts remain unchanged.
