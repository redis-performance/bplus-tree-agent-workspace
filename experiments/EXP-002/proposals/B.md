# Sequential proposal pass B — scan tag matching

Participant: coordinator pass B, not an independent agent; not independent confirmation.
Shared context identical to A; no separate backend/model/cost visible.
PROFILE-003 scan samples concentrate in zbtIndexScanSlot; zbtLeafTagMatches is inlined.
Hypothesis: replacing position-list tag collection with direct callback consumption
reduces scan work by>=2% without changing reachable-home filtering or duplicates.
Target scan leaf-tag matching; preserve zero/one tag mapping, physical reversal,
old/new resize membership, displaced buckets and cursor termination. Risks high: exact
scan semantics under resizing and same-tag collisions. Existing mutation/scan tests
required. Prediction short-key scan benefits; long-key effect could differ.
Falsification: no wall gain or changed emitted coverage/checksum/cursor semantics.
Recommendation PARK: both fresh AA-005 scan cells fail precision. Symbol counts do not
resolve that gate; do not implement a scan candidate this round.
