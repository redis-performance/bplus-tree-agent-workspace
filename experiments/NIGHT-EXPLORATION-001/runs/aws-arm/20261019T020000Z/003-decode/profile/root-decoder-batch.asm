
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build/root/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b8f0 <decoder_batch>:
 * forces the same output writes before checksum consumption in every variant.
 * The round barrier stops repeat-invariant load hoisting; it emits no instruction
 * on GCC/Clang. There are no timers, allocation, I/O or assertions in this loop. */
__attribute__((noinline)) uint64_t decoder_batch(decoder_fixture *f, unsigned rounds) {
    uint64_t a = 0, b = 0, c = 0, d = 0;
    for (unsigned r = 0; r < rounds; r++) {
    b8f0:	34001801 	cbz	w1, bbf0 <decoder_batch+0x300>
    b8f4:	f81c0ffd 	str	x29, [sp, #-64]!
    b8f8:	a9015ff8 	stp	x24, x23, [sp, #16]
    b8fc:	a90257f6 	stp	x22, x21, [sp, #32]
    b900:	a9034ff4 	stp	x20, x19, [sp, #48]
    b904:	d10c03ff 	sub	sp, sp, #0x300
    b908:	910003e9 	mov	x9, sp
    b90c:	aa1f03e2 	mov	x2, xzr
    b910:	2a1f03e8 	mov	w8, wzr
    b914:	aa1f03f0 	mov	x16, xzr
    b918:	aa1f03f1 	mov	x17, xzr
    b91c:	aa1f03f2 	mov	x18, xzr
    b920:	9101012a 	add	x10, x9, #0x40
    b924:	9100412b 	add	x11, x9, #0x10
    b928:	9280000c 	mov	x12, #0xffffffffffffffff    	// #-1
    b92c:	5280080d 	mov	w13, #0x40                  	// #64
    b930:	14000004 	b	b940 <decoder_batch+0x50>
    b934:	11000508 	add	w8, w8, #0x1
    b938:	6b01011f 	cmp	w8, w1
    b93c:	54001480 	b.eq	bbcc <decoder_batch+0x2dc>  // b.none
        __asm__ volatile("" : : "r"(f) : "memory");
        for (unsigned j = 0; j < f->leaves; j++) {
    b940:	b940040e 	ldr	w14, [x0, #4]
    b944:	34ffff8e 	cbz	w14, b934 <decoder_batch+0x44>
            zbtScoreLeaf *leaf = f->leaf[j];
            double values[96];
            zbtScoreLeafDecodePolicy(leaf, 0, f->count, values);
    b948:	b940000e 	ldr	w14, [x0]
    b94c:	aa1f03ef 	mov	x15, xzr
    b950:	14000005 	b	b964 <decoder_batch+0x74>
        for (unsigned j = 0; j < f->leaves; j++) {
    b954:	b9400403 	ldr	w3, [x0, #4]
    b958:	910005ef 	add	x15, x15, #0x1
    b95c:	eb0301ff 	cmp	x15, x3
    b960:	54fffea2 	b.cs	b934 <decoder_batch+0x44>  // b.hs, b.nlast
/* Experimental bulk decoder, private to EXP-007. Logical forward range.
 * Caller owns a disjoint output buffer with at least count doubles.
 * start <= leaf count; count <= leaf count - start. Zero count is permitted. */
static void zbtScoreLeafDecodeRange(zbtScoreLeaf *leaf, unsigned start,
                                   unsigned count, double *out) {
    for (unsigned i = 0; i < count; i++) out[i] = zbtScoreLeafScore(leaf, start + i);
    b964:	b400062e 	cbz	x14, ba28 <decoder_batch+0x138>
    b968:	f9400404 	ldr	x4, [x0, #8]
    b96c:	aa1f03e3 	mov	x3, xzr
    b970:	f86f7884 	ldr	x4, [x4, x15, lsl #3]
    b974:	f9401485 	ldr	x5, [x4, #40]
    b978:	9100e086 	add	x6, x4, #0x38
    b97c:	14000011 	b	b9c0 <decoder_batch+0xd0>
        if (bits < 64)
    b980:	9ad32195 	lsl	x21, x12, x19
    b984:	7101027f 	cmp	w19, #0x40
    b988:	da952193 	csinv	x19, x12, x21, cs	// cs = hs, nlast
        delta <<= leaf->n.score_shift;
    b98c:	39404c95 	ldrb	w21, [x4, #19]
        if (bits < 64)
    b990:	8a130293 	and	x19, x20, x19
        delta <<= leaf->n.score_shift;
    b994:	9ad52273 	lsl	x19, x19, x21
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
    b998:	710000ff 	cmp	w7, #0x0
    b99c:	da930667 	cneg	x7, x19, ne	// ne = any
    b9a0:	8b0500e7 	add	x7, x7, x5
    if (ordered & (UINT64_C(1) << 63))
    b9a4:	9240f8f3 	and	x19, x7, #0x7fffffffffffffff
    b9a8:	f10000ff 	cmp	x7, #0x0
    b9ac:	da87b267 	csinv	x7, x19, x7, lt	// lt = tstop
    for (unsigned i = 0; i < count; i++) out[i] = zbtScoreLeafScore(leaf, start + i);
    b9b0:	f8237927 	str	x7, [x9, x3, lsl #3]
    b9b4:	91000463 	add	x3, x3, #0x1
    b9b8:	eb0301df 	cmp	x14, x3
    b9bc:	54000360 	b.eq	ba28 <decoder_batch+0x138>  // b.none
    unsigned int bits = leaf->score_bits;
    b9c0:	3940d093 	ldrb	w19, [x4, #52]
    b9c4:	3940d487 	ldrb	w7, [x4, #53]
    if (bits != 0) {
    b9c8:	340002d3 	cbz	w19, ba20 <decoder_batch+0x130>
    b9cc:	aa0303f4 	mov	x20, x3
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    b9d0:	34000087 	cbz	w7, b9e0 <decoder_batch+0xf0>
    b9d4:	39404494 	ldrb	w20, [x4, #17]
    b9d8:	d2407c75 	eor	x21, x3, #0xffffffff
    b9dc:	8b1402b4 	add	x20, x21, x20
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
    b9e0:	92407e94 	and	x20, x20, #0xffffffff
    b9e4:	9bb37e94 	umull	x20, w20, w19
        size_t byte = bitpos / 8;
    b9e8:	d343fe95 	lsr	x21, x20, #3
        delta = intrev64ifbe(delta) >> shift;
    b9ec:	92400a98 	and	x24, x20, #0x7
        unsigned int shift = bitpos & 7;
    b9f0:	72000a96 	ands	w22, w20, #0x7
        memcpy(&delta, leaf->data + byte, sizeof(delta));
    b9f4:	f87568d7 	ldr	x23, [x6, x21]
        delta = intrev64ifbe(delta) >> shift;
    b9f8:	9ad826f4 	lsr	x20, x23, x24
        if (shift && bits > 64 - shift)
    b9fc:	54fffc20 	b.eq	b980 <decoder_batch+0x90>  // b.none
    ba00:	4b1601b6 	sub	w22, w13, w22
    ba04:	6b1302df 	cmp	w22, w19
    ba08:	54fffbc2 	b.cs	b980 <decoder_batch+0x90>  // b.hs, b.nlast
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
    ba0c:	8b0402b5 	add	x21, x21, x4
    ba10:	394102b5 	ldrb	w21, [x21, #64]
    ba14:	9ad622b5 	lsl	x21, x21, x22
    ba18:	aa1402b4 	orr	x20, x21, x20
    ba1c:	17ffffd9 	b	b980 <decoder_batch+0x90>
    ba20:	aa1f03f3 	mov	x19, xzr
    ba24:	17ffffdd 	b	b998 <decoder_batch+0xa8>
    ba28:	b940000e 	ldr	w14, [x0]
            __asm__ volatile("" : : "r"(values) : "memory");
            unsigned i = 0;
            for (; i + 3 < f->count; i += 4) {
    ba2c:	710011df 	cmp	w14, #0x4
    ba30:	54000103 	b.cc	ba50 <decoder_batch+0x160>  // b.lo, b.ul, b.last
    ba34:	d10011c4 	sub	x4, x14, #0x4
    ba38:	927e75c3 	and	x3, x14, #0xfffffffc
    ba3c:	f100309f 	cmp	x4, #0xc
    ba40:	540000c2 	b.cs	ba58 <decoder_batch+0x168>  // b.hs, b.nlast
    ba44:	aa1f03e4 	mov	x4, xzr
    ba48:	52800065 	mov	w5, #0x3                   	// #3
    ba4c:	14000034 	b	bb1c <decoder_batch+0x22c>
    ba50:	aa1f03e3 	mov	x3, xzr
    ba54:	1400003f 	b	bb50 <decoder_batch+0x260>
    ba58:	d342fc84 	lsr	x4, x4, #2
    ba5c:	6f00e403 	movi	v3.2d, #0x0
    ba60:	6f00e402 	movi	v2.2d, #0x0
    ba64:	6f00e401 	movi	v1.2d, #0x0
    ba68:	6f00e400 	movi	v0.2d, #0x0
    ba6c:	52800065 	mov	w5, #0x3                   	// #3
    ba70:	91000486 	add	x6, x4, #0x1
    ba74:	6f00e404 	movi	v4.2d, #0x0
    ba78:	6f00e407 	movi	v7.2d, #0x0
    ba7c:	927ef0c7 	and	x7, x6, #0x7ffffffffffffffc
    ba80:	6f00e406 	movi	v6.2d, #0x0
    ba84:	6f00e405 	movi	v5.2d, #0x0
    ba88:	d342fcf3 	lsr	x19, x7, #2
    ba8c:	4e081c43 	mov	v3.d[0], x2
    ba90:	4e081e02 	mov	v2.d[0], x16
    ba94:	4e081e21 	mov	v1.d[0], x17
    ba98:	4e081e40 	mov	v0.d[0], x18
    ba9c:	d37ef4e4 	lsl	x4, x7, #2
    baa0:	b37cee65 	bfi	x5, x19, #4, #60
    baa4:	aa0703f0 	mov	x16, x7
    baa8:	aa0a03f1 	mov	x17, x10
                a += double_bits(values[i]);
    baac:	d1010232 	sub	x18, x17, #0x40
    bab0:	4c400e30 	ld4	{v16.2d-v19.2d}, [x17]
    bab4:	f1001210 	subs	x16, x16, #0x4
    bab8:	91020231 	add	x17, x17, #0x80
    babc:	4c400e54 	ld4	{v20.2d-v23.2d}, [x18]
    bac0:	4ee48604 	add	v4.2d, v16.2d, v4.2d
                b += double_bits(values[i + 1]);
    bac4:	4ee58625 	add	v5.2d, v17.2d, v5.2d
                c += double_bits(values[i + 2]);
    bac8:	4ee68646 	add	v6.2d, v18.2d, v6.2d
                a += double_bits(values[i]);
    bacc:	4ee38683 	add	v3.2d, v20.2d, v3.2d
                b += double_bits(values[i + 1]);
    bad0:	4ee086a0 	add	v0.2d, v21.2d, v0.2d
                c += double_bits(values[i + 2]);
    bad4:	4ee186c1 	add	v1.2d, v22.2d, v1.2d
                d += double_bits(values[i + 3]);
    bad8:	4ee286e2 	add	v2.2d, v23.2d, v2.2d
    badc:	4ee78667 	add	v7.2d, v19.2d, v7.2d
    bae0:	54fffe61 	b.ne	baac <decoder_batch+0x1bc>  // b.any
            for (; i + 3 < f->count; i += 4) {
    bae4:	4ee38483 	add	v3.2d, v4.2d, v3.2d
    bae8:	4ee284e2 	add	v2.2d, v7.2d, v2.2d
    baec:	eb0700df 	cmp	x6, x7
    baf0:	4ee184c1 	add	v1.2d, v6.2d, v1.2d
    baf4:	4ee084a0 	add	v0.2d, v5.2d, v0.2d
    baf8:	5ef1b863 	addp	d3, v3.2d
    bafc:	5ef1b842 	addp	d2, v2.2d
    bb00:	5ef1b821 	addp	d1, v1.2d
    bb04:	5ef1b800 	addp	d0, v0.2d
    bb08:	9e660062 	fmov	x2, d3
    bb0c:	9e660050 	fmov	x16, d2
    bb10:	9e660031 	fmov	x17, d1
    bb14:	9e660012 	fmov	x18, d0
    bb18:	540001c0 	b.eq	bb50 <decoder_batch+0x260>  // b.none
    bb1c:	8b050d25 	add	x5, x9, x5, lsl #3
    bb20:	8b040d66 	add	x6, x11, x4, lsl #3
    bb24:	91000c84 	add	x4, x4, #0x3
                a += double_bits(values[i]);
    bb28:	a97f4cc7 	ldp	x7, x19, [x6, #-16]
            for (; i + 3 < f->count; i += 4) {
    bb2c:	91001084 	add	x4, x4, #0x4
                c += double_bits(values[i + 2]);
    bb30:	f84204d4 	ldr	x20, [x6], #32
            for (; i + 3 < f->count; i += 4) {
    bb34:	eb0e009f 	cmp	x4, x14
                d += double_bits(values[i + 3]);
    bb38:	f84204b5 	ldr	x21, [x5], #32
                a += double_bits(values[i]);
    bb3c:	8b0200e2 	add	x2, x7, x2
                b += double_bits(values[i + 1]);
    bb40:	8b120272 	add	x18, x19, x18
                c += double_bits(values[i + 2]);
    bb44:	8b110291 	add	x17, x20, x17
                d += double_bits(values[i + 3]);
    bb48:	8b1002b0 	add	x16, x21, x16
            for (; i + 3 < f->count; i += 4) {
    bb4c:	54fffee3 	b.cc	bb28 <decoder_batch+0x238>  // b.lo, b.ul, b.last
            }
            for (; i < f->count; i++) a += double_bits(values[i]);
    bb50:	eb0e007f 	cmp	x3, x14
    bb54:	54fff002 	b.cs	b954 <decoder_batch+0x64>  // b.hs, b.nlast
    bb58:	cb0301c5 	sub	x5, x14, x3
    bb5c:	f10010bf 	cmp	x5, #0x4
    bb60:	54000283 	b.cc	bbb0 <decoder_batch+0x2c0>  // b.lo, b.ul, b.last
    bb64:	6f00e400 	movi	v0.2d, #0x0
    bb68:	6f00e401 	movi	v1.2d, #0x0
    bb6c:	924005c4 	and	x4, x14, #0x3
    bb70:	cb0400a5 	sub	x5, x5, x4
    bb74:	8b040066 	add	x6, x3, x4
    bb78:	4e081c40 	mov	v0.d[0], x2
    bb7c:	8b030d62 	add	x2, x11, x3, lsl #3
    bb80:	8b0300a3 	add	x3, x5, x3
    bb84:	cb0e00c5 	sub	x5, x6, x14
    bb88:	ad7f8c42 	ldp	q2, q3, [x2, #-16]
    bb8c:	b10010a5 	adds	x5, x5, #0x4
    bb90:	91008042 	add	x2, x2, #0x20
    bb94:	4ee08440 	add	v0.2d, v2.2d, v0.2d
    bb98:	4ee18461 	add	v1.2d, v3.2d, v1.2d
    bb9c:	54ffff61 	b.ne	bb88 <decoder_batch+0x298>  // b.any
    bba0:	4ee08420 	add	v0.2d, v1.2d, v0.2d
    bba4:	5ef1b800 	addp	d0, v0.2d
    bba8:	9e660002 	fmov	x2, d0
    bbac:	b4ffed44 	cbz	x4, b954 <decoder_batch+0x64>
    bbb0:	8b030d24 	add	x4, x9, x3, lsl #3
    bbb4:	cb0301c3 	sub	x3, x14, x3
    bbb8:	f8408485 	ldr	x5, [x4], #8
    bbbc:	f1000463 	subs	x3, x3, #0x1
    bbc0:	8b0200a2 	add	x2, x5, x2
    bbc4:	54ffffa1 	b.ne	bbb8 <decoder_batch+0x2c8>  // b.any
    bbc8:	17ffff63 	b	b954 <decoder_batch+0x64>
        }
    }
    return a + b + c + d;
    bbcc:	8b120228 	add	x8, x17, x18
    bbd0:	8b020209 	add	x9, x16, x2
    bbd4:	8b090100 	add	x0, x8, x9
    bbd8:	910c03ff 	add	sp, sp, #0x300
    bbdc:	a9434ff4 	ldp	x20, x19, [sp, #48]
    bbe0:	a94257f6 	ldp	x22, x21, [sp, #32]
    bbe4:	a9415ff8 	ldp	x24, x23, [sp, #16]
    bbe8:	f84407fd 	ldr	x29, [sp], #64
    bbec:	d65f03c0 	ret
    bbf0:	aa1f03e0 	mov	x0, xzr
    bbf4:	d65f03c0 	ret

Disassembly of section .fini:
