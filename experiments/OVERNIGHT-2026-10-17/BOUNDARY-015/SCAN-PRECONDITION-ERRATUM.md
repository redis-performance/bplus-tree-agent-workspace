# Initial oracle failure: invalid exactly-once SCAN assumption

Attempt 1 compiled cleanly and failed the new scan uniqueness assertion in its
first native baseline cell after the n33 fixtures. The source documents that
zbtIndexScanGroup may repeat displaced members from earlier home groups, even when
rehash has settled. Existing tests/boundary_oracle.c explicitly permits duplicates.
This is an oracle specification error, not a tree bug or a candidate failure.

Attempt 1's complete frozen sources, commands, stdout/stderr and manifest remain.
The corrected additive oracle still validates every callback's member and exact
score, rejects absent/unknown members, requires all live members, and bounds cursor
termination. It permits duplicate callbacks as the API does. No existing test or
source check is changed. The complete predeclared matrix is run in attempt-002;
this correction is not a timing rerun and changes no optimization gate.
