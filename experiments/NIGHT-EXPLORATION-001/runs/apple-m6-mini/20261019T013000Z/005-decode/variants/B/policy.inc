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
