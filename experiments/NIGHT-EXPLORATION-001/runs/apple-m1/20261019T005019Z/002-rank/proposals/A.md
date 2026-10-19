# Proposal A — sequential pass 1 (same worker, not an independent agent)

Evidence: public rank's accumulation instruction range received 154 of 779 sampled PCs at 100K and 154 of 1,078 at 1M. The private census found mean preceding siblings of 27.823 and 37.418 respectively; mean following siblings were 26.941 and 36.630. Clang already vectorizes groups of eight child counts. These PC counts are coarse hotspot evidence, not exact time fractions.

Hypothesis: for nodes near the right edge of a parent, compute preceding count as `parent->n.subtree - node->subtree - sum(following child_count)`; otherwise retain the original preceding sum. A shorter loop may reduce dependent child-count work without changing layout, memory, or mutation maintenance.

Primary prediction: public successful rank at 100K and 1M improves by at least 2% under a qualified same-session comparison. Guards: all smaller rank sizes, reverse rank, absent member, optional score, ties/mixed scores, and every standard mutation/owned-memory cell. Falsify if both primaries do not meet the fixed gate or any guard fails. An unqualified A/A leaves the result exploratory and ineligible for adoption.

Risk: subtree-count assumptions, unsigned arithmetic, branch cost, and differing cache behavior can erase the saved additions. Use exact rank oracle and sanitizer checks. The source/harness baseline is launch HEAD 77d32df with tree hash d9123c82; no source edit is made by this proposal.

Backend/model/token cost: Codex worker in the GPT-6 family per session instructions; exact backend variant and measured token usage unavailable.
