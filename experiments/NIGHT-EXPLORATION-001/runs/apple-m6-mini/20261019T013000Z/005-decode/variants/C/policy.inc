/* Force the policy into the caller; return early through unchanged bulk. */
__attribute__((always_inline)) static inline void zbtScoreLeafDecodePolicy(
        zbtScoreLeaf *leaf, unsigned start, unsigned count, double *out) {
    if (count != 1) {
        zbtScoreLeafDecodeRange(leaf, start, count, out);
        return;
    }
    out[0] = zbtScoreLeafScore(leaf, start);
}
