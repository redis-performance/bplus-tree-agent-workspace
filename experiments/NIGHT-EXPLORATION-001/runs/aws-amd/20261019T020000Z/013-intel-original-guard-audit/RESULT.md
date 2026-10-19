# Independent original-guard verdict: PARK / source NONE

Immutable Intel evidence da9b83734 independently reconstructs all120 A/A and120 B processes,1,920 raw rows and480 block effects. The exact frozen schedule, command arguments, CPU2 endpoints, serial boundaries, raw hashes/CSV identity, unrounded elapsed-per-actual-operation calculations and per-fixture semantics/tree memory agree. Both1440-second bounded job records pass; B completes in1111.54seconds. The separate final read-only artifact snapshot verifies all22 original base/B source/referee/test/build-recipe/binary hashes against the immutable007 manifest. No rebuilt source or binary was substituted.

Of80 cells,57 A/A cells qualify. Twelve have short windows and11 others fail precision. B passes every block of56 qualified cells. One qualified cell fails the positive1% guard bound in one block:

| Cell | A/A effects | B effects | Shortest B window | Verdict |
|---|---|---|---:|---|
|100 members,16 bytes,iterate|−0.207%,+0.167%,−0.243%|+0.304%,−0.825%,+1.329%|21.604ms|PARK: mixed bound exceedance|

No qualified cell has all three B effects above+1%, so the preregistered demonstrated-regression rejection condition is not met. The mixed iteration result still fails its guard; its+0.304% median cannot override the+1.329% block. The other23 cells remain exploratory rather than retroactively qualified. Thus24 original cells remain unresolved:23 failed controls plus this one mixed guard.

The unqualified100-member/128-byte insert cell has all three candidate effects above+1% (+7.399%,+2.584%,+11.591%), but its A/A effects include+7.499% and its minimum control window is only0.07072ms. This is not admissible evidence of a demonstrated regression under the frozen protocol. It is retained, not excluded or counted as a pass.

The changed all-match helper belongs to scan source paths. That does not justify dismissing the iteration guard or attributing it to layout, compiler behavior or background interference without direct evidence. No additional measurement, retry or source A fallback is warranted by this audit.

The independently confirmed primary scan improvement remains a narrow valid result, but these guards prevent adoption. Missing length boundaries, predominantly reversed and active resize/migration performance and matched-profile requirements remain separate. AMD results do not inherit Intel qualification. Overnight source NONE remains unchanged; no optimization population count increments.

Evidence: complete-independent.json contains all480 recomputed effects and80 per-phase cells with qualification joins; provenance-independent.json contains independently checked jobs and final artifact identities. audit.py and audit-provenance.py are independently authored and do not read/import Intel audit-b.py. Raw hashes point to the complete immutable Intel source evidence; no runner was accessed for this review. Model and measured token/USD costs remain unknown.
