# Proposal B — sequential pass 2 (same worker, not an independent agent)

Evidence: the instrumented public rank profile resolves `_platform_memchr` in 337/779 samples at 100K and 618/1,078 at 1M. The source calls `memchr` while searching leaf hash tags. The exact fractions cannot be interpreted as time shares. The earlier EXP-006 inline scanner helped a batched workload but regressed concerning single-query cases, so that patch is a negative control.

Hypothesis: a new bounded portable tag scan tuned to the observed score-leaf tag lengths could reduce single-query rank's leaf search without changing hashing. It would need an untimed shape census first, and a different design from EXP-006's retained inline scanner. Primary prediction would be at least 2% public rank gain at 100K and 1M, with lookup hit/miss and long-key guards.

Falsification: no gain at both rank primaries or any single-query lookup regression over 1%. Semantic risks include first-match selection, collisions, bounded reads and reversed leaf layout. This is broader than rank accumulation and belongs naturally in LOOKUP-001 after that workload's dedicated profile and shape census.

Backend/model/token cost: Codex worker in the GPT-6 family per session instructions; exact backend variant and measured token usage unavailable.
