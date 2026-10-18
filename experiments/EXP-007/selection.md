# Step 1 chair decision

Select width-class specialization, using the explicit bulk-helper alternative
recorded in proposal B. Rank B, A, C for this user's literal once-per-leaf goal.
All three independent proposers prefer a smaller scalar change as a lower-risk
production edit. The chair preserves that dissent: the scalar API cannot guarantee
once-per-leaf dispatch without extra state, and adding a width predicate could
repeat the very overhead we want to eliminate. The bulk experiment tests the
amortization directly while making no scalar iterator claim.

The selected hypothesis: choosing a crossing-capable versus simpler decode loop
once per logical leaf range reduces bulk decode cost at noncrossing widths, with
no changed leaf representation. Only widths 59/61/62/63 can cross the loaded word.
Do not combine with prefetch, packed-format changes or a persistent iterator cache.
Metadata hoisting and an aligned subcase are implementations of this same geometry
specialization; unchanged scalar fallback is allowed.

Evidence shared with all proposers: EXP-004's original baseline profile audit and
iterator assembly, and the 19 October focused kernel's raw A/A/control-A results
and generated assembly. Historical samples locate decoder/scaffold PCs but are
not fresh bulk-loop cost attribution. Fresh referee qualification and codegen are
required before interpreting new measurements. This remains diagnostic preparation
until those checks, not a production acceptance decision.

Three real agents independently wrote A/B/C without reading each other's proposals.
They then independently implemented A/B/C against source commit
4fd3a3fdbce5acca18ee292642a3d80a79f50362 plus the common reference bulk helper.
Separate detached source worktrees/build directories isolate each variant. The
shared kernel, original driver, adapter and flags are identical. The new referee
must be committed separately before candidate timings; all samples retained.
Exact backend/model and per-agent token/currency cost are unavailable, not estimated.
