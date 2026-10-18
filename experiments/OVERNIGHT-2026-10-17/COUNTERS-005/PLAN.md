# COUNTERS-005 — compact reversed-leaf specimen

Preregistered structural diagnostic, no performance claim or source candidate. The
large COUNTERS-004 trees have only64 reversed members. Test a public-API recipe that
concentrates all items in a reversed leaf: insert a strictly lower finite sentinel,
then n members ascending; delete minimum. The sentinel score is nextafter(first model
score,-infinity), not an arbitrarily distant score that forces unrelated packed widths.

336cells/build: n1/2/31/32/63/64/95,bytes16/320,seeds31101/31113,integer/wide/
alternating-zero,construction ascending/trimmed/trimmed-clone/trimmed-cycle. Clone after
trim for third history; reinsert and remove sentinel once more for fourth. Both release/
debug and ASan/UBSan,672children total. n95 leaves room for sentinel within96-item limit;
chosen record sizes are inline-short or external, avoiding long-inline capacity splits.

Prediction: one physical leaf in everycell,allnitems reversed in all three trimmed
histories,zero reversed in ordinaryascending control. Packed-width histograms are
observations: no claim trimming leaves widths identical to ordinaryconstruction.
Independent scalar packed-bit reader plus exact model bits, all8outputmasks and both
iterator directions retained. Within-process read-only memory unchanged; cross-build
structural equality excludes allocator-owned usable sizes only. Clone/source replacement
must preserve exact members/scores and reverse state. Allchildren<=120s,serial.

Two controls: disable reversal for pop (structural recipe must detect this even if public
ordering remains correct); clear returned zero sign (exact-bit oracle must detect this).
These are diagnostic sensitivity controls,not new boundary-suite counts. Root/source/
referee unchanged; fresh ignored snapshot;no gitretry or acceptance. Backend/model/cost
unknown;review sequential after independent reviewer startup failed thisround.
