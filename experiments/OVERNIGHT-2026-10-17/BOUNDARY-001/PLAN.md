# BOUNDARY-001 — additional semantic oracle validation

No timing comparison. Root tree source remains pristine; no candidate population.
Add an independent sorted-vector model (algorithmic oracle, same coordinator, not an
independent reviewer). Exercise exact finite-score bits including signed zero, binary
members at inline/external lengths, raw/SDS lookup and insert, batch score masks,
forward/reverse order, rank and seek, scan coverage with duplicate callbacks permitted,
reserve, duplication and mixed insert/update/delete/edge/rank-range operations.

Preselected seeds 1,2,3,101,102,103; two fixtures per seed (mixed lengths including empty
and short members; deliberately raw leaf tags0/1/255 with lengths8/16/319/320/321).
257-key pool, 2048 mutation steps per fixture, verification at selected insertion
boundaries and every31 mutation steps, plus final drain. Compare exact double bits,
not just approximate equality. No NaNs. Do not weaken assertions if baseline fails;
preserve failure and isolate a reproducer. Release with debug assertions and ASan/UBSan,
child timeout120s each. No timing claim, performance conclusions or source optimisation.
Original upstream tests and frozen referee remain intact.
