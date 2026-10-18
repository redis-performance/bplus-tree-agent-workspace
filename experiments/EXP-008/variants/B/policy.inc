static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                     unsigned count, double *out) {
    if (count <= 8) {
        for (unsigned i = 0; i < count; i++)
            out[i] = zbtScoreLeafScore(leaf, start + i);
        return;
    }
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
