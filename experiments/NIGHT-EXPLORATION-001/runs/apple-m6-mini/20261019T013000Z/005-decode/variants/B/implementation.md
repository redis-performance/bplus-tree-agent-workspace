# Implementation B

Hypothesis M6-DECODE-COUNT1-001. This is sequential implementation pass B
by the same worker, not an independent agent. Chair commit e62f839d; referee80177d1e.
Exact model/backend/cost unknown; visible Codex/GPT-6 family.

Policy:

```c
/* Outline only the bulk bridge so the small scalar policy can inline. */
__attribute__((noinline)) static void zbtDecodeBulkBridge(zbtScoreLeaf *leaf,
        unsigned start, unsigned count, double *out) {
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
static inline void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                          unsigned count, double *out) {
    if (count == 1) out[0] = zbtScoreLeafScore(leaf, start);
    else zbtDecodeBulkBridge(leaf, start, count, out);
}
```

Only count1 uses original scalar. Other counts retain frozen B helper.
No source edits to baseline src/, helpers/packing/allocator/assertions unchanged.
Copied isolated source/build directories under scratch/m6-decode preserve full hashes.
Risk: compiler inlining/outlining changes code size and caller registers/call costs;
all count2+ guards still required despite algorithm equality. All logical starts,
orientations, empty ranges and exact signed-zero bits must pass the referee.
