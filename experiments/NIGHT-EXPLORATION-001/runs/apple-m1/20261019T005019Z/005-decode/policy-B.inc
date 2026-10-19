static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                     unsigned count, double *out) {
    const unsigned bits = leaf->score_bits;
    if (count == 1 && ((bits & 7) == 0 || bits <= 58 || bits == 60)) {
        out[0] = zbtScoreLeafScore(leaf, start);
        return;
    }
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
