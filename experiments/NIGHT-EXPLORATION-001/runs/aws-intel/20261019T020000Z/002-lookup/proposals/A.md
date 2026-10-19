# Sequential proposal pass A

One native worker; not an independent agent. Exact backend/model/token cost unknown. Same baseline8fab511e and frozen profile/A/A evidence.

Bounded inline SSE2 tag search. Instrumented leaf search is38.66% self at100K and31.66% at1M; release has a memchr PLT call. Hypothesis: inline16-byte compare/mask plus bounded tail avoids call dispatch overhead enough to improve100K and1M successful public single-query lookup>=2%. Exact target zbtScoreLeafFindMember's tag search only. Retain hash/order/packed-data handling. Risks: first-match behavior after rejected collisions, page boundaries, zero spans, architecture portability. Require scalar fallback and exact first-match/page tests. Falsified by failure of either primary on fresh qualified blocks or>1% guard/memory regression. SIMD mechanism is distinct from EXP-006's8-byte SWAR scanner. Cache/memory stalls may dominate1M and libc AVX512 may outperform SSE2; these are explicit counterarguments.
