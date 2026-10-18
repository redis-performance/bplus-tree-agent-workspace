# Preserved first-attempt failure

The first unchanged control run fails the new allocation equality assertion, before
any candidate executes. zbtreeScore/rank can advance incremental rehash; this is an
existing documented mutation, not a source defect. The first oracle, patch, isolated
source and stdout/stderr remain in the initial manifest/snapshot. Attempt 002 explicitly
finishes active rehash before taking its read-only allocation baseline. The exact
allocation equality assertion, all score/order/ownership checks and full fixture matrix
remain. This oracle targets packed score mutations; active-rehash ownership is covered
by earlier suites. No benchmark or optimization gate changes.
