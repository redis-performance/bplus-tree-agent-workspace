# RANK-001 chair decision — 2026-10-19 round 1

The three proposal files were written in **three sequential passes by one worker**. They are not independent agents. No implementation population has started. Model family is GPT-6 per session instructions; exact backend variant and measured token cost are unavailable; no participant or independence is invented.

| Proposal | Profile support | Scope/risk | Decision |
|---|---|---|---|
| A: choose shorter sibling side | 154 rank-accumulation PCs at each primary; structural census predicts 14.933 and 19.842 fewer child-count visits per member at 100K/1M if the shorter side is chosen | Layout preserving, but extra branch/subtraction may lose | **CHOOSE for one exploratory population** |
| B: new leaf-tag search | `memchr` is hotter by PC count, especially at 1M; earlier EXP-006 single-query concern remains | Broader lookup guards and shape census needed | Defer to LOOKUP-001 |
| C: prefix summaries | Rank accumulation is visible, but no mutation-cost profile | Layout/memory change and split/merge maintenance | Defer; memory/mutation risk too broad |

Chosen falsifiable hypothesis: use `parent->n.subtree - node->subtree - sum(following child_count)` on nodes where the following side is shorter; retain preceding sum otherwise. The choice census counted an average 14.933 and 19.842 fewer child-count visits at 100K and 1M. These are predicted visits, **not** a measured public speedup. Clang already vectorizes groups of eight additions, so implementation/codegen review must check that saved visits offset the extra control and arithmetic.

Both primary A/A controls failed strict ±1% qualification (max absolute block effects 37.66% at 100K and 6.71% at 1M). The measurement protocol permits one fixed exploratory comparison but forbids adoption under these controls. No candidate may be accepted without later qualified same-session controls and the full guard/confirmation/review gates. A small effect buried in A/A variation receives no ranking. Three isolated implementations from the same launch source and referee are planned for the next bounded phase; exact patches/builds and all losses must be retained.

The published M6 branch query attempted during this round failed because DNS could not resolve github.com. M6 status is **UNKNOWN**, with no branch/commit/outcome observed. Check again immediately before implementation or timing. No M6 binary or performance number was used.
