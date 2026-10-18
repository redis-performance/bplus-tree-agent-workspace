# Next distinct fixture: batched lookup spanning mixed-width promotion

Preparation only, not an executed or preregistered experiment. Round17 adds current
score movement, external ownership and finite/equal-score order while SCAN remains
live across natural widening. BOUNDARY-009 exhaustively covers batch masks/counts and
small active resizes, but does not establish natural narrow-to-wide promotion inside
one zbtreeScores call after score movement.

Possible bounded recipe: start from a final round17 oracle with its independent current
score model. After its declared mutations, replace the existing group of16ordinary
lookups between SCAN calls with one16-lane zbtreeScores call. Each batch should contain
hits in previously migrated/unmigrated leaves, deliberately absent IDs and duplicates;
include moved/current exact-score members. Capture read-only width/rehash state before
and after. Require an actual narrow-current/wide-destination state at entry and completed
wide-current state on return from at least one batch. Rehash lookups advance once per
lane; observing only an active batch does not prove promotion occurred inside it.

Use fresh seeds, all source/build cells and separate frozen snapshots. Add per-lane
expected hit bits, exact finite score bits for hits, and output canaries outside the
requested count. Missing output lanes are unspecified: do not require their guard
value to remain unchanged. Count0 permits NULL arrays; test0..16 separately at declared
states without exhausting migration before the required16-lane transition. Preserve
all live-cursor intervals/continuous anchors/termination and exact memory accounting;
read lookup accounting may change because rehash progresses. Never assert allocation
size is unchanged across zbtreeScores itself. The SCAN call still must not mutate it.

Production zbtreeScores precomputes hashes and performs prefetches before iterating
zbtIndexFind; the latter may finish a resize during the loop. Instrumented counts can
confirm reachability but not time or cache effects. Fault controls should target
stale-table assumptions across promotion, not just repeat a wrong result-mask bit
already caught by BOUNDARY-009. Validate fault compilation and preserve survivors.

This recipe is untested. Do not substitute it for performance guards or rerun old
failed timing protocols. Keep main baseline for morning review. The final worker
still owes MORNING-REPORT.md by07:00UTC /08:00Europe/Lisbon.
