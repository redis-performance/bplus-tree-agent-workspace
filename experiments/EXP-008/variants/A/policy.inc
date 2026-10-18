/* Count-only policy for the EXP-008 isolated decoder comparison.
 * The caller supplies a valid logical range and disjoint output storage. */
static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                     unsigned count, double *out) {
    if (count == 0) return;

    if (count <= 4) {
        for (unsigned i = 0; i < count; i++)
            out[i] = zbtScoreLeafScore(leaf, start + i);
        return;
    }

    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
