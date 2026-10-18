# BOUNDARY-003 — natural widening and mutation scan validated

Two fixed seeds7/19 pass release/debug and ASan/UBSan. Each run constructs850000
inline319-byte binary members plus4096 external320/321/1024-byte members. Natural
widening observed at393194 members / leaf ID32767; final next leaf ID70834. No test
writes private tree fields or changes thresholds. Original source remains pristine.

Each seed performs five full model validations and seven scans, including active
narrow-to-wide migration, interior rank deletion/reinsertion, scan across score moves
and delete/reinsert churn, then clone verification after freeing the original. Mutable
scan calls3283/3287 stay below the observed32768-group bound. All callbacks check live
membership, full binary bytes and exact score bits; continuously present members must
be seen, legal duplicate callbacks allowed. Lookup, forward/reverse iteration, sampled
rank/seek and independent sorted ordering agree. No baseline bug observed.

Both preregistered intentional faults detected: late-widen reaches the narrow ID range
assertion; omit-small-scan fails complete membership during natural widening. These are
test-strength controls, not optimisation variants. Exact stderr/patches in mutations/.

[Plan](PLAN.md), [oracle patch](oracle.patch), [commands/source hashes](manifest.json),
[mutation plan](MUTATION-PLAN.md), [fault evidence](mutations/). All six baseline commands
(two builds/four runs) succeed. Each child bounded120s; no timing claims.

Sequential coordinator review checked scan continuity accounting, callback-time model
validity, iterator lifetime, exact signed zero and independent clone ownership. A
reviewer agent failed to start (thread-store context unavailable); no independent
review claimed. Backend/model/cost unknown. Protected git metadata not retried;
uncommitted test/evidence draft, morning review pending. This does not close performance
profile, independent confirmation or optimisation acceptance gates. Selection NONE.
