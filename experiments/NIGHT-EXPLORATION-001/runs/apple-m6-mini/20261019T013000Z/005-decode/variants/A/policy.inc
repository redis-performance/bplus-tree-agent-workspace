/* Scalar at exactly one; frozen bulk for all other valid ranges. */
static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    if (count == 1) {
        out[0] = zbtScoreLeafScore(leaf, start);
        return;
    }
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
