# External-member ownership with a live mixed-width cursor — validated

All48fixed source/build/seed/mode cells pass. Initial392809inline319-byte anchors stay
unchanged; added members rotate320/321/1024/4097bytes. Natural migration starts at
call193and completes at2240; same live cursor terminates within16384calls. Every
per-call hash interval, exact binary value, continuous anchor and final model passes.

At intervention there are3088external allocations among38042owned allocations. All-move
visits/moves/releases all38042; selective mode moves25362and declines12680, including
2059moved and1029declined external buffers. Each uninterrupted walk completes35856steps.
Exact usable-byte deltas match at every step. Active clone allocations are independently
owned, including every external buffer; original is freed before continuing its cursor.
Final428649members pass lookups/iteration/sampled ranks/scan hints and clone-after-free.

[Plan](PLAN.md), [commands/hashes](manifest.json), [summary](summary.json),
[oracle patch](oracle.patch), [fault evidence](faults/manifest.json). Deliberately shallow
external clone ownership is detected by the external-pointer disjointness check; this is
a repeat fault type and adds no distinct-fault count.
No production changes or speed claim.23suites/47distinct fault types unchanged. SourceNONE,
priorPARK unchanged; sequential review, unknown backend/model/cost. Observed geometry
and allocator counts are local to these snapshots; no portable cardinalities claimed.
