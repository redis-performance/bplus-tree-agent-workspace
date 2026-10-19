# Sequential implementation C

One contiguous span chosen before a shared reduction loop; conditional correction after reduction.

Only zbtScoreRank changes. Same shorter-side hypothesis, no layout, allocator,
hash, assertion, mutation or API change. Requires parent and current node subtree
counts to equal child totals. Existing prefix + inner rank is preserved algebraically.
Unsigned intermediate is bounded by parent subtree when invariants hold. Risks:
stale subtree counts after mutation, different vectorization, extra metadata and
branch costs. Full upstream and targeted semantic native/sanitizer checks precede
timing. One worker, not an independent implementer. Exact model/cost unknown.
