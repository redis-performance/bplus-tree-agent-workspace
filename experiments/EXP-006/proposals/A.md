# Proposal A — inline bounded leaf-tag search

Sequential coordinator pass A, not an independent agent. Exact model/backend/cost unknown.
Frozen input: HARNESS-007attempt002, AA-012 all rows, PROFILE-004 all captures,
baselinea2ff0c5 plus hashed source snapshot; prior rejected dispatch/outlining history.

Mixed16/batch16 qualifies both seeds. Its four profile captures consistently place
memchr first, with the exact-member leaf routine also sampled. Test one hypothesis:
removing generic libc memchr call/setup through a bounded inline tag scan improves
mixed batched lookup by>=2%, without >1%qualified long-hit guard or memory regression.
Target only zbtScoreLeafFindMember's tag search. Keep packed decode, full hash/length/
member comparison and logical-position mapping unchanged. No change to SipHash.

Risk: bytewise search can lose SIMD throughput on long leaves; word search needs
strict bounds, endian correctness and lowest-match semantics with repeated tags.
Predict different implementation costs for small/large spans; no claim setup dominates
without candidate profile/codegen. Falsify with nonbenefit, guard failure, correctness
failure or unchanged hot code. Short-hit/miss unqualified guards still block acceptance.
