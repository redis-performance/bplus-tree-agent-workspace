/* Control policy always delegates to frozen EXP-007 bulk decoder. */
static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
