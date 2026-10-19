
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build/base/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b924 <zbtScoreLeafDecodePolicy>:
/* EXP-007 B: dispatch once for zero, byte-aligned, noncrossing, or crossing
 * geometry. Private bulk helper; no persistent leaf/iterator state is changed.
 * Logical forward subrange; output is disjoint and has room for count doubles. */
static void zbtScoreLeafDecodeRange(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    if (count == 0) return;
    b924:	34001222 	cbz	w2, bb68 <zbtScoreLeafDecodePolicy+0x244>

    const unsigned bits = leaf->score_bits;
    b928:	3940d00b 	ldrb	w11, [x0, #52]
    const unsigned score_shift = leaf->n.score_shift;
    const unsigned reversed = leaf->reversed;
    const unsigned leaf_count = leaf->n.count;
    const uint64_t base = leaf->score_base;
    b92c:	f9401408 	ldr	x8, [x0, #40]

    if (bits == 0) {
    b930:	3400064b 	cbz	w11, b9f8 <zbtScoreLeafDecodePolicy+0xd4>
    b934:	9280000a 	mov	x10, #0xffffffffffffffff    	// #-1
    b938:	39404c09 	ldrb	w9, [x0, #19]
    b93c:	3940d40e 	ldrb	w14, [x0, #53]
        const double value = zbtOrderedToScore(base);
        for (unsigned i = 0; i < count; i++) out[i] = value;
        return;
    }

    const uint64_t mask = bits == 64 ? UINT64_MAX : (UINT64_C(1) << bits) - 1;
    b940:	9acb214c 	lsl	x12, x10, x11
    b944:	7101017f 	cmp	w11, #0x40
    b948:	3940440f 	ldrb	w15, [x0, #17]
    b94c:	da8c014a 	csinv	x10, x10, x12, eq	// eq = none

    if ((bits & 7) == 0) {
    b950:	7200097f 	tst	w11, #0x7
    b954:	54000620 	b.eq	ba18 <zbtScoreLeafDecodePolicy+0xf4>  // b.none
            out[i] = zbtOrderedToScore(ordered);
        }
        return;
    }

    if (bits <= 58 || bits == 60) {
    b958:	7100ed7f 	cmp	w11, #0x3b
    b95c:	9100e00c 	add	x12, x0, #0x38
    b960:	2a0203ed 	mov	w13, w2
    b964:	540009c3 	b.cc	ba9c <zbtScoreLeafDecodePolicy+0x178>  // b.lo, b.ul, b.last
    b968:	7100f17f 	cmp	w11, #0x3c
    b96c:	54000980 	b.eq	ba9c <zbtScoreLeafDecodePolicy+0x178>  // b.none
        return;
    }

    /* Only 59,61,62,63 remain for valid widths. Preserve the scalar
     * crossing predicate and its protection against a shift by 64. */
    for (unsigned i = 0; i < count; i++) {
    b970:	2a2103f0 	mvn	w16, w1
    b974:	0b0f020f 	add	w15, w16, w15
    b978:	52800810 	mov	w16, #0x40                  	// #64
    b97c:	1400000e 	b	b9b4 <zbtScoreLeafDecodePolicy+0x90>
        uint64_t delta;
        memcpy(&delta, leaf->data + byte, sizeof(delta));
        delta = intrev64ifbe(delta) >> shift;
        if (shift && bits > 64 - shift)
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
        delta = (delta & mask) << score_shift;
    b980:	8a0a0231 	and	x17, x17, x10
        const uint64_t ordered = reversed ? base - delta : base + delta;
    b984:	72001ddf 	tst	w14, #0xff
    for (unsigned i = 0; i < count; i++) {
    b988:	d10005ad 	sub	x13, x13, #0x1
        delta = (delta & mask) << score_shift;
    b98c:	9ac92231 	lsl	x17, x17, x9
    for (unsigned i = 0; i < count; i++) {
    b990:	11000421 	add	w1, w1, #0x1
    b994:	510005ef 	sub	w15, w15, #0x1
        const uint64_t ordered = reversed ? base - delta : base + delta;
    b998:	da910631 	cneg	x17, x17, ne	// ne = any
    b99c:	8b080231 	add	x17, x17, x8
    if (ordered & (UINT64_C(1) << 63))
    b9a0:	9240fa32 	and	x18, x17, #0x7fffffffffffffff
    b9a4:	f100023f 	cmp	x17, #0x0
    b9a8:	da91b251 	csinv	x17, x18, x17, lt	// lt = tstop
        out[i] = zbtOrderedToScore(ordered);
    b9ac:	f8008471 	str	x17, [x3], #8
    for (unsigned i = 0; i < count; i++) {
    b9b0:	b4000dcd 	cbz	x13, bb68 <zbtScoreLeafDecodePolicy+0x244>
        const unsigned physical = reversed ? leaf_count - 1 - logical : logical;
    b9b4:	72001ddf 	tst	w14, #0xff
    b9b8:	1a8f0031 	csel	w17, w1, w15, eq	// eq = none
        const size_t bitpos = (size_t)physical * bits;
    b9bc:	9bb17d71 	umull	x17, w11, w17
        const size_t byte = bitpos / 8;
    b9c0:	d343fe32 	lsr	x18, x17, #3
        delta = intrev64ifbe(delta) >> shift;
    b9c4:	92400a25 	and	x5, x17, #0x7
        const unsigned shift = bitpos & 7;
    b9c8:	72000a22 	ands	w2, w17, #0x7
        memcpy(&delta, leaf->data + byte, sizeof(delta));
    b9cc:	f8726984 	ldr	x4, [x12, x18]
        delta = intrev64ifbe(delta) >> shift;
    b9d0:	9ac52491 	lsr	x17, x4, x5
    b9d4:	54fffd60 	b.eq	b980 <zbtScoreLeafDecodePolicy+0x5c>  // b.none
        if (shift && bits > 64 - shift)
    b9d8:	4b020202 	sub	w2, w16, w2
    b9dc:	6b0b005f 	cmp	w2, w11
    b9e0:	54fffd02 	b.cs	b980 <zbtScoreLeafDecodePolicy+0x5c>  // b.hs, b.nlast
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
    b9e4:	8b000252 	add	x18, x18, x0
    b9e8:	39410252 	ldrb	w18, [x18, #64]
    b9ec:	9ac22252 	lsl	x18, x18, x2
    b9f0:	aa110251 	orr	x17, x18, x17
    b9f4:	17ffffe3 	b	b980 <zbtScoreLeafDecodePolicy+0x5c>
    if (ordered & (UINT64_C(1) << 63))
    b9f8:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    b9fc:	f100011f 	cmp	x8, #0x0
    ba00:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
        for (unsigned i = 0; i < count; i++) out[i] = value;
    ba04:	7100105f 	cmp	w2, #0x4
    ba08:	2a0203e9 	mov	w9, w2
    ba0c:	54000902 	b.cs	bb2c <zbtScoreLeafDecodePolicy+0x208>  // b.hs, b.nlast
    ba10:	aa1f03ea 	mov	x10, xzr
    ba14:	14000050 	b	bb54 <zbtScoreLeafDecodePolicy+0x230>
        const unsigned stride = bits / 8;
    ba18:	d343fd6b 	lsr	x11, x11, #3
    ba1c:	72001ddf 	tst	w14, #0xff
    ba20:	9100e00c 	add	x12, x0, #0x38
        for (unsigned i = 0; i < count; i++) {
    ba24:	2a0203ed 	mov	w13, w2
            const unsigned physical = reversed ? leaf_count - 1 - logical : logical;
    ba28:	54000200 	b.eq	ba68 <zbtScoreLeafDecodePolicy+0x144>  // b.none
        for (unsigned i = 0; i < count; i++) {
    ba2c:	2a2103ee 	mvn	w14, w1
    ba30:	0b0f01ce 	add	w14, w14, w15
            memcpy(&delta, leaf->data + (size_t)physical * stride, sizeof(delta));
    ba34:	9bae7d6f 	umull	x15, w11, w14
        for (unsigned i = 0; i < count; i++) {
    ba38:	d10005ad 	sub	x13, x13, #0x1
    ba3c:	510005ce 	sub	w14, w14, #0x1
            memcpy(&delta, leaf->data + (size_t)physical * stride, sizeof(delta));
    ba40:	f86f698f 	ldr	x15, [x12, x15]
            delta = (intrev64ifbe(delta) & mask) << score_shift;
    ba44:	8a0a01ef 	and	x15, x15, x10
    ba48:	9ac921ef 	lsl	x15, x15, x9
            const uint64_t ordered = reversed ? base - delta : base + delta;
    ba4c:	cb0f010f 	sub	x15, x8, x15
    if (ordered & (UINT64_C(1) << 63))
    ba50:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    ba54:	f10001ff 	cmp	x15, #0x0
    ba58:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
            out[i] = zbtOrderedToScore(ordered);
    ba5c:	f800846f 	str	x15, [x3], #8
        for (unsigned i = 0; i < count; i++) {
    ba60:	b5fffead 	cbnz	x13, ba34 <zbtScoreLeafDecodePolicy+0x110>
    ba64:	14000041 	b	bb68 <zbtScoreLeafDecodePolicy+0x244>
            memcpy(&delta, leaf->data + (size_t)physical * stride, sizeof(delta));
    ba68:	9ba17d6e 	umull	x14, w11, w1
        for (unsigned i = 0; i < count; i++) {
    ba6c:	11000421 	add	w1, w1, #0x1
            memcpy(&delta, leaf->data + (size_t)physical * stride, sizeof(delta));
    ba70:	f86e698e 	ldr	x14, [x12, x14]
            delta = (intrev64ifbe(delta) & mask) << score_shift;
    ba74:	8a0a01ce 	and	x14, x14, x10
    ba78:	9ac921ce 	lsl	x14, x14, x9
            const uint64_t ordered = reversed ? base - delta : base + delta;
    ba7c:	8b0801ce 	add	x14, x14, x8
    if (ordered & (UINT64_C(1) << 63))
    ba80:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    ba84:	f10001df 	cmp	x14, #0x0
    ba88:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
        for (unsigned i = 0; i < count; i++) {
    ba8c:	f10005ad 	subs	x13, x13, #0x1
            out[i] = zbtOrderedToScore(ordered);
    ba90:	f800846e 	str	x14, [x3], #8
        for (unsigned i = 0; i < count; i++) {
    ba94:	54fffea1 	b.ne	ba68 <zbtScoreLeafDecodePolicy+0x144>  // b.any
    ba98:	14000034 	b	bb68 <zbtScoreLeafDecodePolicy+0x244>
    ba9c:	72001ddf 	tst	w14, #0xff
            const unsigned physical = reversed ? leaf_count - 1 - logical : logical;
    baa0:	54000260 	b.eq	baec <zbtScoreLeafDecodePolicy+0x1c8>  // b.none
        for (unsigned i = 0; i < count; i++) {
    baa4:	2a2103ee 	mvn	w14, w1
    baa8:	0b0f01ce 	add	w14, w14, w15
            const size_t bitpos = (size_t)physical * bits;
    baac:	9bae7d6f 	umull	x15, w11, w14
        for (unsigned i = 0; i < count; i++) {
    bab0:	d10005ad 	sub	x13, x13, #0x1
    bab4:	510005ce 	sub	w14, w14, #0x1
            memcpy(&delta, leaf->data + bitpos / 8, sizeof(delta));
    bab8:	d343fdf0 	lsr	x16, x15, #3
            delta = ((intrev64ifbe(delta) >> (bitpos & 7)) & mask) << score_shift;
    babc:	924009ef 	and	x15, x15, #0x7
            memcpy(&delta, leaf->data + bitpos / 8, sizeof(delta));
    bac0:	f8706990 	ldr	x16, [x12, x16]
            delta = ((intrev64ifbe(delta) >> (bitpos & 7)) & mask) << score_shift;
    bac4:	9acf260f 	lsr	x15, x16, x15
    bac8:	8a0a01ef 	and	x15, x15, x10
    bacc:	9ac921ef 	lsl	x15, x15, x9
            const uint64_t ordered = reversed ? base - delta : base + delta;
    bad0:	cb0f010f 	sub	x15, x8, x15
    if (ordered & (UINT64_C(1) << 63))
    bad4:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    bad8:	f10001ff 	cmp	x15, #0x0
    badc:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
            out[i] = zbtOrderedToScore(ordered);
    bae0:	f800846f 	str	x15, [x3], #8
        for (unsigned i = 0; i < count; i++) {
    bae4:	b5fffe4d 	cbnz	x13, baac <zbtScoreLeafDecodePolicy+0x188>
    bae8:	14000020 	b	bb68 <zbtScoreLeafDecodePolicy+0x244>
            const size_t bitpos = (size_t)physical * bits;
    baec:	9ba17d6e 	umull	x14, w11, w1
        for (unsigned i = 0; i < count; i++) {
    baf0:	11000421 	add	w1, w1, #0x1
            memcpy(&delta, leaf->data + bitpos / 8, sizeof(delta));
    baf4:	d343fdcf 	lsr	x15, x14, #3
            delta = ((intrev64ifbe(delta) >> (bitpos & 7)) & mask) << score_shift;
    baf8:	924009ce 	and	x14, x14, #0x7
            memcpy(&delta, leaf->data + bitpos / 8, sizeof(delta));
    bafc:	f86f698f 	ldr	x15, [x12, x15]
            delta = ((intrev64ifbe(delta) >> (bitpos & 7)) & mask) << score_shift;
    bb00:	9ace25ee 	lsr	x14, x15, x14
    bb04:	8a0a01ce 	and	x14, x14, x10
    bb08:	9ac921ce 	lsl	x14, x14, x9
            const uint64_t ordered = reversed ? base - delta : base + delta;
    bb0c:	8b0801ce 	add	x14, x14, x8
    if (ordered & (UINT64_C(1) << 63))
    bb10:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    bb14:	f10001df 	cmp	x14, #0x0
    bb18:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
        for (unsigned i = 0; i < count; i++) {
    bb1c:	f10005ad 	subs	x13, x13, #0x1
            out[i] = zbtOrderedToScore(ordered);
    bb20:	f800846e 	str	x14, [x3], #8
        for (unsigned i = 0; i < count; i++) {
    bb24:	54fffe41 	b.ne	baec <zbtScoreLeafDecodePolicy+0x1c8>  // b.any
    bb28:	14000010 	b	bb68 <zbtScoreLeafDecodePolicy+0x244>
        for (unsigned i = 0; i < count; i++) out[i] = value;
    bb2c:	4e080d00 	dup	v0.2d, x8
    bb30:	927e752a 	and	x10, x9, #0xfffffffc
    bb34:	9100406b 	add	x11, x3, #0x10
    bb38:	aa0a03ec 	mov	x12, x10
    bb3c:	ad3f8160 	stp	q0, q0, [x11, #-16]
    bb40:	f100118c 	subs	x12, x12, #0x4
    bb44:	9100816b 	add	x11, x11, #0x20
    bb48:	54ffffa1 	b.ne	bb3c <zbtScoreLeafDecodePolicy+0x218>  // b.any
    bb4c:	eb09015f 	cmp	x10, x9
    bb50:	540000c0 	b.eq	bb68 <zbtScoreLeafDecodePolicy+0x244>  // b.none
    bb54:	8b0a0c6b 	add	x11, x3, x10, lsl #3
    bb58:	cb0a0129 	sub	x9, x9, x10
    bb5c:	f1000529 	subs	x9, x9, #0x1
    bb60:	f8008568 	str	x8, [x11], #8
    bb64:	54ffffc1 	b.ne	bb5c <zbtScoreLeafDecodePolicy+0x238>  // b.any
}
/* Control policy always delegates to frozen EXP-007 bulk decoder. */
static void zbtScoreLeafDecodePolicy(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    zbtScoreLeafDecodeRange(leaf, start, count, out);
}
    bb68:	d65f03c0 	ret

Disassembly of section .fini:
