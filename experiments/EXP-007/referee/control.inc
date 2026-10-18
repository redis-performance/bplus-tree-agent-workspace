/* Experimental bulk decoder, private to EXP-007. Logical forward range.
 * Caller owns a disjoint output buffer with at least count doubles.
 * start <= leaf count; count <= leaf count - start. Zero count is permitted. */
static void zbtScoreLeafDecodeRange(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    for (unsigned i = 0; i < count; i++) out[i] = zbtScoreLeafScore(leaf, start + i);
}
