# Proposal A — exact index match mask

Sequential pass 1 by the native Codex worker; not an independent agent. Exact backend/model variant and token cost are unknown.

Hypothesis: an exact byte equality mask in zbtIndexTableFind permits removal of its dependent byte verification and improves 100K/1M public hit lookup by at least 2%, without guard regressions. The current mask permits borrow-induced extra bits and verifies every candidate. The new helper applies only to this lookup; the original mask and its other callers remain unchanged.

Evidence: the frozen 100K independent-query whole-process profile attributes 36.00% of samples to zbtreeScoreRaw, with 19.49% of its local samples at the tag-verification CMP. EOR after the tag load accounts for 38.50% locally but may represent load latency or sampling skid. Source and assembly show a shift, compare and conditional skip for each candidate.

Predictions: hits may improve by eliminating that dependency; misses and long keys can regress if exact-mask creation costs more. Layout and owned memory remain unchanged. Either primary failing the fixed screen, or a guard regression, falsifies the speed gate. Correctness risks are exact mask bits, numeric lane order, collisions, tombstones and resize behavior. Preserve the existing general-mask oracle, which deliberately requires false bits; add a separate exact-helper oracle.
