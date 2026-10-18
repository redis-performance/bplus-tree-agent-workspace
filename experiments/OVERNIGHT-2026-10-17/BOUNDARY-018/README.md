# Leaf-ID registry state machine — validated

All eight baseline/EXP-004A/B/C × release/debug/ASan+UBSan cells pass with identical
logical digests. Each checks 38 fixtures, 1,458,668 registrations and releases,
81,310 pointer replacements, 602 full registry audits, 213,534 fresh IDs during
active rehash, and 391,368 reused IDs after rehash ends. Sizes cover growth and
16-bit boundaries through65,537. Registry ownership matches actual usable bytes;
reuse preserves high-water mark, capacity and allocation size.

Both intentional sanitizer faults are detected: premature ID reuse during rehash
and16-bit truncation of free-list links. Synthetic registry structs are never
presented as a public tree, scanned or timed. Main source remains unchanged.

The first compile failed on an unavailable allocator API name. The corrected oracle
calls the adapter's existing zmalloc_usable_size; no assertion was weakened. Initial
source snapshot, patch and errors remain. [Erratum](ERRATUM.md).

[Plan](PLAN.md), [oracle](../../../tests/leaf_id_registry_oracle.c),
[corrected patch](attempt-002/oracle.patch), [manifest](attempt-002/manifest.json),
[summary](attempt-002/summary.json), [fault evidence](attempt-002/faults/manifest.json).
Eighteenth boundary suite,36 distinct boundary fault types. Source NONE and existing
PARK decisions unchanged. Backend/model/cost unknown; review sequential.
