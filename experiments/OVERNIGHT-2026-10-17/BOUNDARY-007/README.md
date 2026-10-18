# BOUNDARY-007 — lexical boundaries validated

Release/debug and ASan/UBSan pass all36 fixtures,180 full model verifications,4075200
lexical seeks and9616452 checked Next results per build. Two intentional faults are
detected: dropped reverse exclusive equality and incorrect reverse maximum-sentinel
rank. No baseline failure or source change.

[Plan](PLAN.md), [new oracle patch](oracle.patch), [commands/source/output hashes](manifest.json),
[fault patches and results](faults.json). Root test source is tests/lex_boundary_oracle.c.
Sorted-vector expected bounds are independent of tree implementation. Coverage includes
empty/tiny/multiple-leaf sets,binary prefix/embedded-NUL/high-byte members,exact signed
zeros/finite extremes,min/max sentinel identity,forward/reverse exclusive bounds,
absolute optional rank and all8 Next output masks. Tests repeat after deleting every
third key,reinsertion,clone-original free and complete deletion. Iterators/pointers are
reacquired after mutation, respecting invalidation; lexical tests use equal scores only.

Sequential coordinator review, not independent agent review. Mutation controls are
separate snapshots and are not optimisation candidates. Exact backend/model/cost unknown.
Uncommitted evidence awaits morning review. Seven added boundary suites now validated;
lookup PARK and source NONE unchanged, no performance/population acceptance.
