# Pass C — node summary

Provenance: one Codex/GPT-6-family worker, exact serving model and measured token
cost unknown. Three sequential passes, NOT independent agents. Each pass uses the
same M6 profile, release assembly, A/A and shared target/guard definitions. M1
shorter-side proposal is prior context, not independent confirmation.

The same parent walk visits3ancestors at both primaries. Hypothesis: cache child
prefix totals to turn each ancestor into one load. This would change inner-node
layout or summary maintenance at splits, merges and count updates. Existing code
has subtree totals but no frozen prefix-maintenance implementation. Requires new
mutation correctness and all update/insert/delete/memory guards. Likely larger
working set and more mutation writes; exact cost unknown. Falsification includes
any stale count after split/merge or>1%tree-owned memory increase. Reject for this
bounded round: the layout-preserving shorter-side hypothesis has lower risk and
requires less speculative bookkeeping. Retain as an untested future proposal.
