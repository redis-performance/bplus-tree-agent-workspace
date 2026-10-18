# Compact index storage boundary oracle — validated

All eight baseline/EXP-004A/B/C × release/debug/ASan+UBSan cells pass with identical
logical digests. Each checks 1,048,624 ID stores, 4,096 tag stores and 524,288 tag-mask
patterns. Entire buffers match an independent reference, including tags, filters,
adjacent IDs and canaries. Documented mask borrow false positives are permitted;
all real matches and first-candidate positions are checked.

Both intentional sanitizer faults are detected: a narrow tombstone decoded as a
live ID and a tag store clearing its neighbor. No production source changed.
This is private-integer storage coverage, not a public tree fixture or speed claim.

[Plan](PLAN.md), [oracle](../../../tests/index_storage_oracle.c), [patch](oracle.patch),
[manifest](manifest.json), [summary](summary.json), [fault evidence](faults/manifest.json).
Seventeenth boundary suite,34 distinct boundary fault types. Source NONE and existing
PARK decisions unchanged. Backend/model/cost unknown; review sequential.
