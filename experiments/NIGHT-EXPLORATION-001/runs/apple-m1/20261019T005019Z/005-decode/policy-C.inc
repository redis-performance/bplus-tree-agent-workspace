static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                     unsigned count, double *out) {
    if (count == 1 && leaf->score_bits == 60) {
        out[0] = zbtScoreLeafScore(leaf, start);
        return;
    }
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
