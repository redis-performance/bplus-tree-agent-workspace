# BOUNDARY-004 preregistration — relocating allocations through standalone API

Additional correctness experiment, no Redis server/defragmenter integration.
Existing tests/boundary_oracle.c is reused unchanged as sorted-vector/model oracle;
new test translation unit calls the standalone DefragStart/Step APIs directly.
Seeds11/29, both binary-length and colliding-tag fixture families, N257. Release/debug
and ASan/UBSan builds, each child <=120s. No timing measurements or algorithm change.

Callbacks explicitly copy live allocations to different addresses, sometimes decline
to move, and request64 extra bytes to test exact usable-size accounting. Start callback
frees old objects itself (no free callback in that API); Step callback leaves freeing
to the supplied release callback, after pointer repair. Observe old/new usable sizes.

Uninterrupted passes require zbtreeAllocSize delta exactly equals callback usable-size
deltas and verify lookups, binary bytes, exact finite score bits, rank/iteration/scan
after every slice. Verify moving/no-move branches. Then bounded inter-slice score moves,
delete-all/refill and state reset exercise stale leaf cursor handling; stop mutations
before checking eventual completion. Clone, free original, relocate and verify clone.
All ownership/lifetime checks retain original oracle assertions; no artificial IDs.

Any failure first investigated for callback/oracle contract errors; preserve all logs.
No claim of independent review (agent startup failed). Backend/model/cost unknown.
Source base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus uncommitted test drafts.
