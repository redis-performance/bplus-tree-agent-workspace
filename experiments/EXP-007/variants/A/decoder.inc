/* Experimental bulk decoder, private to EXP-007. Logical forward range.
 * Caller owns a disjoint output buffer with at least count doubles.
 * start <= leaf count; count <= leaf count - start. Zero count is permitted. */
static void zbtScoreLeafDecodeRange(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    if (count == 0) return;

    unsigned int bits = leaf->score_bits;
    /* Only these widths can extend past the loaded eight-byte word. */
    if (bits == 59 || bits == 61 || bits == 62 || bits == 63) {
        for (unsigned i = 0; i < count; i++)
            out[i] = zbtScoreLeafScore(leaf, start + i);
        return;
    }

    if (bits == 0) {
        double score = zbtOrderedToScore(leaf->score_base);
        for (unsigned i = 0; i < count; i++) out[i] = score;
        return;
    }

    uint64_t mask = bits == 64 ? UINT64_MAX : (UINT64_C(1) << bits) - 1;
    unsigned int score_shift = leaf->n.score_shift;
    uint64_t base = leaf->score_base;
    unsigned int reversed = leaf->reversed;
    for (unsigned i = 0; i < count; i++) {
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, start + i) * bits;
        uint64_t delta;
        memcpy(&delta, leaf->data + bitpos / 8, sizeof(delta));
        delta = (intrev64ifbe(delta) >> (bitpos & 7)) & mask;
        delta <<= score_shift;
        uint64_t ordered = reversed ? base - delta : base + delta;
        out[i] = zbtOrderedToScore(ordered);
    }
}
