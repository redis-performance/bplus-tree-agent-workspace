# Proposal B — empty bucket check for read-only lookup

Sequential pass 2 by the same worker; not independent. Model variant and cost are unknown.

Hypothesis: specialize the read-only empty-slot path to one word-level zero-byte test instead of eight byte checks, improving public misses at 100K/1M. Generated assembly contains eight masks and conditional comparisons after tag candidates and the home filter. Read-only callers have NULL insertion outputs and need no tombstone bookkeeping.

Evidence gap: the current hit profiles do not establish that this path is material. The home filter can reject misses before this loop. A miss profile and probe-path census are prerequisites. Risks include insertion positions and tombstone reuse for add callers. Expected hit impact is small except for collisions. PARK as a separate later hypothesis; do not combine it with exact masks.
