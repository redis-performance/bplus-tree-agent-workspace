# Sequential proposalA

One nativeworker; not independent agents. Exactbackend/model/token/USDcost unknown. Same8fab511e baseline,004referee/profiles/A/A.

Cache the per-leaf MEMBER offset-array base in iterator state, computed lazily on first member/length output and reset on every leaf assignment. Profile captured80–96%in IteratorNext;75/368full-forward samples land at prefix-compare PC after dependent offset/prefix loads. This does not make cmp the cause, but release assembly shows repeated width×count/rounding before those loads. Hypothesis: removing repeated offset-base calculation shortens the dependency path enough to improve both100K/1M full-output forward integer traversal>=2%. Preserve nullable-output semantics and all seek/reset paths. Main risk is stale/uninitialized cache, not ownership transfer. Memorytradeoff declared below; all treeownedmemory exact.
