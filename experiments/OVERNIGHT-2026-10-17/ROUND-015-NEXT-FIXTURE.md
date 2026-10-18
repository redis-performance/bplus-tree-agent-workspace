# Next distinct scope: carry a SCAN cursor across natural ID widening

Preparation from source inspection, NOT a result or preregistered execution schedule.
BOUNDARY-003 observes natural narrow→wide migration and runs a complete static scan
inside it; its mutable cursor begins later, after widening has finished. BOUNDARY-022
now carries a cursor through colliding growth/shrink and validates same-size cleanup,
but uses narrow leaf IDs. A cursor spanning the actual ID-width transition is a
separate reachable coverage claim. No existing performance PARK is affected.

Proposed public recipe: insert sorted319-byte binary members, observe read-only
`next_score_leaf_id`, and stop about32IDs below `ZBT_INDEX_WIDE_ID_AT`. Do not hardcode
393194members as portable geometry; that was BOUNDARY-003's observed local result.
Bound construction at850000members and fail if coverage cannot be reached. Begin a
real SCAN at cursor0, require a nonzero returned cursor before width changes, then
append a fixed small number (e.g.16, to be preregistered) of absent ordered members
between scan calls. Preserve all initially present members as continuous anchors.
Observe actual old-narrow/destination-wide fields while cursor remains nonzero;
require later completed-wide state. Keep a bounded cardinality and largest-group
termination bound; missing transition is failure, not an excuse to inject private IDs.

For efficient independent interval checks, precompute and sort scalar-bit-reversed
`hash>>2` values of the initially present anchors. Each call's interval can binary-
search that vector instead of rescanning hundreds of thousands of hashes per call.
Callbacks must still check exact key lengths/bytes and score bits for EVERY currently
live member, permit duplicates, and mark all continuous anchors. Full ordered iterator
validation and complete scan after migration can be linear; preregister bounded rank
samples if full all-rank verification is unaffordable. Clearly label that scope.

Inspect local API/constants first, freeze exact source and test snapshots, choose fresh
seeds/counts/builds/fault controls and wall budget BEFORE running. Baseline native/debug
and sanitizer first; retained variants are a separate fixed expansion if time permits.
Possible controls: existing omit-old-table scan fault, plus a width/stride confusion
fault during mixed-width migration. Preserve failures. No benchmark or performance
claim from this correctness test; all source acceptance gates remain unchanged.

Other next action: a separately qualified performance runner or a new justified method.
Do not repeat failed duration/warmup/QoS/caller/placement/bookkeeping/transport schedules
unchanged. Keep root baseline until morning review. Final worker still owes the actual
MORNING-REPORT.md before07:00UTC/08:00Europe/Lisbon.
