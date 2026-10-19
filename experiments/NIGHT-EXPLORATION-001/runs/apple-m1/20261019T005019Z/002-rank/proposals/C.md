# Proposal C — sequential pass 3 (same worker, not an independent agent)

Evidence: public rank samples include the existing ancestor accumulation loop. The private census observes 2 parents at 10K and 3 at 100K/1M, with mean preceding child counts 13.376, 27.823 and 37.418. This suggests a repeated sum that might be precomputed, but no mutation-cost profile supports extra maintenance yet.

Hypothesis: store an exclusive prefix count beside each inner child so rank needs one prefix load per parent. Predictions: rank gains at 100K and 1M; inserts, deletes and score moves pay for summary maintenance and owned memory grows unless packed in existing space. Those mutation/memory costs must be measured under the same frozen guard matrix before any selection.

Falsification: any >1% mutation or tree-owned memory regression under qualified controls, rank gain below 2% at either primary, or a correctness failure after split/merge/reorder. This design changes layout and multiple update paths, so it is too broad for the first bounded rank trial.

Backend/model/token cost: Codex worker in the GPT-6 family per session instructions; exact backend variant and measured token usage unavailable.
