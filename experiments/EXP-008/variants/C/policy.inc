/* EXP-008 C: use the original scalar decoder for ranges up to 16 scores;
 * route longer ranges through the frozen EXP-007 B bulk helper. This helper is
 * private to the experiment and adds no per-leaf or iterator state. */
static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                     unsigned count, double *out) {
    if (count == 0) return;

    if (count <= 16) {
        for (unsigned i = 0; i < count; i++)
            out[i] = zbtScoreLeafScore(leaf, start + i);
        return;
    }

    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
