/* EXP-007 private bulk helper: classify crossing eligibility once per range.
 * start/count form a valid logical forward subrange; out is disjoint storage. */
static void zbtScoreLeafDecodeRange(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    if (count == 0) return;
    unsigned bits = leaf->score_bits;

    /* Only widths 59, 61, 62 and 63 have reachable offsets crossing bit 64.
     * Keep the original scalar decoder for these less simple layouts. */
    if (bits > 58 && (bits & 3) != 0) {
        for (unsigned i = 0; i < count; i++)
            out[i] = zbtScoreLeafScore(leaf, start + i);
        return;
    }

    /* The scalar algorithm with only its unreachable ninth-byte arm removed.
     * Preserve zero-width handling and avoid shifting a mask by 64. */
    for (unsigned i = 0; i < count; i++) {
        uint64_t delta = 0;
        if (bits != 0) {
            size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, start + i) * bits;
            size_t byte = bitpos / 8;
            unsigned shift = bitpos & 7;
            memcpy(&delta, leaf->data + byte, sizeof(delta));
            delta = intrev64ifbe(delta) >> shift;
            if (bits < 64)
                delta &= (UINT64_C(1) << bits) - 1;
            delta <<= leaf->n.score_shift;
        }
        uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
                                             leaf->score_base + delta;
        out[i] = zbtOrderedToScore(ordered);
    }
}
