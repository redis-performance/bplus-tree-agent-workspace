# BOUNDARY-023 — live SCAN cursor across natural leaf-ID widening

Preregistered correctness scope, 2026-10-18 round16; no timing or speed claim.
Sources: unchanged control and retained EXP-004 A/B/C, exact freeze.json hashes.
Public construction/mutation only; private fields are read-only coverage observations.
Unchanged ambient allocator and referee; new oracle isolated per source. No git retry.

Seeds65521/65537. Every child receives one seed and is bounded120s. First run control
native-O3/debug then-O1ASan/UBSan; after both seeds pass, fixed expansion A/B/C with
both builds and both seeds. Matrix budget900s, serial commands, no optional skipping
of failed cells. A failure stops this recipe; preserve it before any new plan.

Generate up to850000 distinct319-byte binary members, IDs encoded in first8bytes;
finite exact score=id. Precompute independent scalar reverse64(hash>>2), sort all
possible IDs once and binary-search each returned cursor interval. Build by public
append until observed next_score_leaf_id reaches ZBT_INDEX_WIDE_ID_AT-32, with cap850000;
require still narrow. Complete independent forward/reverse models, all live lookups,
rank/seek every997members, subtree/parent/leaf registry and owned-memory accounting.
Full checks may drain earlier narrow growth but must not change IDs or width.

Start SCAN cursor0 with hint1, require nonzero cursor while still narrow. Between
calls append exactly16 absent members while wide migration has not finished. Require
actual source-narrow/destination-wide resize at nonzero cursor, destination.used<length,
and eventual completed-wide state before that same scan ends. Preserve every initial
member continuously. Cardinality never exceeds850000. Cursor intervals must strictly
increase in scalar bit-reversed order; bound calls by largest observed group count+1.
For every call check all currently present members whose independent hash belongs to
its interval were returned. Callbacks validate full binary bytes/length/exact score,
allow duplicates and mark continuous anchors. SCAN itself must leave resize pointer,
cursor, table accounting, revision and owned bytes unchanged. No internal helper is
used to derive expected cursor arithmetic. Print observed transition/geometry.

After live scan, require every initial anchor returned, full model, and static complete
scans with hints0/256/ULONG_MAX. Clone, free original, full model and complete clone
scan. Full rank checks are sampled, not claimed exhaustive. No private ID injection,
no hardcoded portable cardinality and no fabricated model/agent/token provenance.

Two isolated sanitizer sensitivity controls: omit old-table scan (repeat fault type),
and force narrow ID decoding only in zbtIndexScanSlot while reading a wide table (new
width-confusion fault). Require successful build and oracle/assertion/sanitizer failure;
retain survivors honestly. All success/error output, commands, timestamps, hashes,
patches and snapshots saved. Source selection NONE; existing performance PARK remains.
Independent reviewer startup failed; coordinator review is sequential.
