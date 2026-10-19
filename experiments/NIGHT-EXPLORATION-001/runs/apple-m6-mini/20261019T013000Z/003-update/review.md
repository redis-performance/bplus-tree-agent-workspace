# Adversarial self-review — not independent

Mechanism: order checks precede helper, all reads/space checks precede writes; fields,
orientation and current allocation remain valid. A captures logical metadata; B/C move
physical metadata before clearing score fields. Headroom includes offsets+tags and
never extends into records. Existing packed write primitive preserves exact finite
scores/signed zero; no NaN support assumed. C shift is never invoked at64 because
encoding's differing-bit shift is0..63, width growth>64 falls back. Re-encoding can
change leaf layout and invalidate iterators, already allowed by public mutation contract.

Tests exercise reversed leaves, long/external records, exact bits/ties and clones;
two faults confirm metadata and failure-atomicity sensitivity. Full-count/zero-width/
64-bit extremes also occur in original semantic tests, but no exhaustive new private
encoding proof is claimed. Standard mutation fallback remains unchanged. No new allocator,
index/leaf ID field or record ownership transfer. Original upstream assertions intact.

Measurement: failed controls bar adoption;100K primary fails all implementations.
Keep1M as a lead with transient/iteration-count caveat, never a universal gain. B/C
100K losses are positive in every block. Full candidate guards, independent confirmation,
matched adoption profile and independent review absent. No ACCEPT. Initial baseline
oracle UAF was an invalid test pointer retention and is disclosed, not a production bug.
No frequency/counter/core claims, M1/M6 pooling or fabricated agent/model/cost identity.
