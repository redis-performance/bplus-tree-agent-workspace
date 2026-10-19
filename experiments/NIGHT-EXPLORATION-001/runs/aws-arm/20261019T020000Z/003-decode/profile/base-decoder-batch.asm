
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build/base/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000bb6c <decoder_batch>:
/* Throughput loop with four independent unsigned checksum chains. This is not
 * dependent-operation latency. The compiler may inline/unroll/vectorise normally. A materialization barrier
 * forces the same output writes before checksum consumption in every variant.
 * The round barrier stops repeat-invariant load hoisting; it emits no instruction
 * on GCC/Clang. There are no timers, allocation, I/O or assertions in this loop. */
__attribute__((noinline)) uint64_t decoder_batch(decoder_fixture *f, unsigned rounds) {
    bb6c:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
    bb70:	a9016ffc 	stp	x28, x27, [sp, #16]
    bb74:	a90267fa 	stp	x26, x25, [sp, #32]
    bb78:	a9035ff8 	stp	x24, x23, [sp, #48]
    bb7c:	a90457f6 	stp	x22, x21, [sp, #64]
    bb80:	a9054ff4 	stp	x20, x19, [sp, #80]
    bb84:	910003fd 	mov	x29, sp
    bb88:	d10c43ff 	sub	sp, sp, #0x310
    bb8c:	b90007e1 	str	w1, [sp, #4]
    uint64_t a = 0, b = 0, c = 0, d = 0;
    for (unsigned r = 0; r < rounds; r++) {
    bb90:	34001161 	cbz	w1, bdbc <decoder_batch+0x250>
    bb94:	910023f6 	add	x22, sp, #0x8
    bb98:	aa0003f4 	mov	x20, x0
    bb9c:	aa1f03f3 	mov	x19, xzr
    bba0:	2a1f03f5 	mov	w21, wzr
    bba4:	aa1f03fa 	mov	x26, xzr
    bba8:	aa1f03fb 	mov	x27, xzr
    bbac:	aa1f03fc 	mov	x28, xzr
    bbb0:	910102d7 	add	x23, x22, #0x40
    bbb4:	910042d8 	add	x24, x22, #0x10
    bbb8:	14000005 	b	bbcc <decoder_batch+0x60>
    bbbc:	b94007e8 	ldr	w8, [sp, #4]
    bbc0:	110006b5 	add	w21, w21, #0x1
    bbc4:	6b0802bf 	cmp	w21, w8
    bbc8:	54000f20 	b.eq	bdac <decoder_batch+0x240>  // b.none
        __asm__ volatile("" : : "r"(f) : "memory");
        for (unsigned j = 0; j < f->leaves; j++) {
    bbcc:	b9400688 	ldr	w8, [x20, #4]
    bbd0:	34ffff68 	cbz	w8, bbbc <decoder_batch+0x50>
            zbtScoreLeaf *leaf = f->leaf[j];
            double values[96];
            zbtScoreLeafDecodePolicy(leaf, 0, f->count, values);
    bbd4:	b9400282 	ldr	w2, [x20]
    bbd8:	aa1f03f9 	mov	x25, xzr
    bbdc:	14000005 	b	bbf0 <decoder_batch+0x84>
        for (unsigned j = 0; j < f->leaves; j++) {
    bbe0:	b9400688 	ldr	w8, [x20, #4]
    bbe4:	91000739 	add	x25, x25, #0x1
    bbe8:	eb08033f 	cmp	x25, x8
    bbec:	54fffe82 	b.cs	bbbc <decoder_batch+0x50>  // b.hs, b.nlast
            zbtScoreLeaf *leaf = f->leaf[j];
    bbf0:	f9400688 	ldr	x8, [x20, #8]
            zbtScoreLeafDecodePolicy(leaf, 0, f->count, values);
    bbf4:	910023e3 	add	x3, sp, #0x8
    bbf8:	2a1f03e1 	mov	w1, wzr
            zbtScoreLeaf *leaf = f->leaf[j];
    bbfc:	f8797900 	ldr	x0, [x8, x25, lsl #3]
            zbtScoreLeafDecodePolicy(leaf, 0, f->count, values);
    bc00:	97ffff49 	bl	b924 <zbtScoreLeafDecodePolicy>
    bc04:	b9400282 	ldr	w2, [x20]
            __asm__ volatile("" : : "r"(values) : "memory");
            unsigned i = 0;
            for (; i + 3 < f->count; i += 4) {
    bc08:	7100105f 	cmp	w2, #0x4
    bc0c:	54000103 	b.cc	bc2c <decoder_batch+0xc0>  // b.lo, b.ul, b.last
    bc10:	d1001049 	sub	x9, x2, #0x4
    bc14:	121e7448 	and	w8, w2, #0xfffffffc
    bc18:	f100313f 	cmp	x9, #0xc
    bc1c:	540000c2 	b.cs	bc34 <decoder_batch+0xc8>  // b.hs, b.nlast
    bc20:	aa1f03e9 	mov	x9, xzr
    bc24:	5280006a 	mov	w10, #0x3                   	// #3
    bc28:	14000034 	b	bcf8 <decoder_batch+0x18c>
    bc2c:	2a1f03e8 	mov	w8, wzr
    bc30:	1400003f 	b	bd2c <decoder_batch+0x1c0>
    bc34:	d342fd29 	lsr	x9, x9, #2
    bc38:	6f00e403 	movi	v3.2d, #0x0
    bc3c:	6f00e402 	movi	v2.2d, #0x0
    bc40:	6f00e401 	movi	v1.2d, #0x0
    bc44:	6f00e400 	movi	v0.2d, #0x0
    bc48:	5280006a 	mov	w10, #0x3                   	// #3
    bc4c:	9100052b 	add	x11, x9, #0x1
    bc50:	6f00e404 	movi	v4.2d, #0x0
    bc54:	6f00e407 	movi	v7.2d, #0x0
    bc58:	927ef16c 	and	x12, x11, #0x7ffffffffffffffc
    bc5c:	6f00e406 	movi	v6.2d, #0x0
    bc60:	6f00e405 	movi	v5.2d, #0x0
    bc64:	d342fd8d 	lsr	x13, x12, #2
    bc68:	4e081e63 	mov	v3.d[0], x19
    bc6c:	4e081f42 	mov	v2.d[0], x26
    bc70:	4e081f61 	mov	v1.d[0], x27
    bc74:	4e081f80 	mov	v0.d[0], x28
    bc78:	d37ef589 	lsl	x9, x12, #2
    bc7c:	b37cedaa 	bfi	x10, x13, #4, #60
    bc80:	aa0c03ed 	mov	x13, x12
    bc84:	aa1703ee 	mov	x14, x23
                a += double_bits(values[i]);
    bc88:	d10101cf 	sub	x15, x14, #0x40
    bc8c:	4c400dd0 	ld4	{v16.2d-v19.2d}, [x14]
    bc90:	f10011ad 	subs	x13, x13, #0x4
    bc94:	910201ce 	add	x14, x14, #0x80
    bc98:	4c400df4 	ld4	{v20.2d-v23.2d}, [x15]
    bc9c:	4ee48604 	add	v4.2d, v16.2d, v4.2d
                b += double_bits(values[i + 1]);
    bca0:	4ee58625 	add	v5.2d, v17.2d, v5.2d
                c += double_bits(values[i + 2]);
    bca4:	4ee68646 	add	v6.2d, v18.2d, v6.2d
                a += double_bits(values[i]);
    bca8:	4ee38683 	add	v3.2d, v20.2d, v3.2d
                b += double_bits(values[i + 1]);
    bcac:	4ee086a0 	add	v0.2d, v21.2d, v0.2d
                c += double_bits(values[i + 2]);
    bcb0:	4ee186c1 	add	v1.2d, v22.2d, v1.2d
                d += double_bits(values[i + 3]);
    bcb4:	4ee286e2 	add	v2.2d, v23.2d, v2.2d
    bcb8:	4ee78667 	add	v7.2d, v19.2d, v7.2d
    bcbc:	54fffe61 	b.ne	bc88 <decoder_batch+0x11c>  // b.any
            for (; i + 3 < f->count; i += 4) {
    bcc0:	4ee38483 	add	v3.2d, v4.2d, v3.2d
    bcc4:	4ee284e2 	add	v2.2d, v7.2d, v2.2d
    bcc8:	eb0c017f 	cmp	x11, x12
    bccc:	4ee184c1 	add	v1.2d, v6.2d, v1.2d
    bcd0:	4ee084a0 	add	v0.2d, v5.2d, v0.2d
    bcd4:	5ef1b863 	addp	d3, v3.2d
    bcd8:	5ef1b842 	addp	d2, v2.2d
    bcdc:	5ef1b821 	addp	d1, v1.2d
    bce0:	5ef1b800 	addp	d0, v0.2d
    bce4:	9e660073 	fmov	x19, d3
    bce8:	9e66005a 	fmov	x26, d2
    bcec:	9e66003b 	fmov	x27, d1
    bcf0:	9e66001c 	fmov	x28, d0
    bcf4:	540001c0 	b.eq	bd2c <decoder_batch+0x1c0>  // b.none
    bcf8:	8b0a0eca 	add	x10, x22, x10, lsl #3
    bcfc:	8b090f0b 	add	x11, x24, x9, lsl #3
    bd00:	91000d29 	add	x9, x9, #0x3
                a += double_bits(values[i]);
    bd04:	a97f356c 	ldp	x12, x13, [x11, #-16]
            for (; i + 3 < f->count; i += 4) {
    bd08:	91001129 	add	x9, x9, #0x4
                c += double_bits(values[i + 2]);
    bd0c:	f842056e 	ldr	x14, [x11], #32
            for (; i + 3 < f->count; i += 4) {
    bd10:	eb02013f 	cmp	x9, x2
                d += double_bits(values[i + 3]);
    bd14:	f842054f 	ldr	x15, [x10], #32
                a += double_bits(values[i]);
    bd18:	8b130193 	add	x19, x12, x19
                b += double_bits(values[i + 1]);
    bd1c:	8b1c01bc 	add	x28, x13, x28
                c += double_bits(values[i + 2]);
    bd20:	8b1b01db 	add	x27, x14, x27
                d += double_bits(values[i + 3]);
    bd24:	8b1a01fa 	add	x26, x15, x26
            for (; i + 3 < f->count; i += 4) {
    bd28:	54fffee3 	b.cc	bd04 <decoder_batch+0x198>  // b.lo, b.ul, b.last
            }
            for (; i < f->count; i++) a += double_bits(values[i]);
    bd2c:	6b02011f 	cmp	w8, w2
    bd30:	54fff582 	b.cs	bbe0 <decoder_batch+0x74>  // b.hs, b.nlast
    bd34:	2a0803e8 	mov	w8, w8
    bd38:	cb08004a 	sub	x10, x2, x8
    bd3c:	f100115f 	cmp	x10, #0x4
    bd40:	54000283 	b.cc	bd90 <decoder_batch+0x224>  // b.lo, b.ul, b.last
    bd44:	6f00e400 	movi	v0.2d, #0x0
    bd48:	6f00e401 	movi	v1.2d, #0x0
    bd4c:	92400449 	and	x9, x2, #0x3
    bd50:	cb09014b 	sub	x11, x10, x9
    bd54:	8b09010c 	add	x12, x8, x9
    bd58:	8b080f0a 	add	x10, x24, x8, lsl #3
    bd5c:	8b080168 	add	x8, x11, x8
    bd60:	cb02018b 	sub	x11, x12, x2
    bd64:	4e081e60 	mov	v0.d[0], x19
    bd68:	ad7f8d42 	ldp	q2, q3, [x10, #-16]
    bd6c:	b100116b 	adds	x11, x11, #0x4
    bd70:	9100814a 	add	x10, x10, #0x20
    bd74:	4ee08440 	add	v0.2d, v2.2d, v0.2d
    bd78:	4ee18461 	add	v1.2d, v3.2d, v1.2d
    bd7c:	54ffff61 	b.ne	bd68 <decoder_batch+0x1fc>  // b.any
    bd80:	4ee08420 	add	v0.2d, v1.2d, v0.2d
    bd84:	5ef1b800 	addp	d0, v0.2d
    bd88:	9e660013 	fmov	x19, d0
    bd8c:	b4fff2a9 	cbz	x9, bbe0 <decoder_batch+0x74>
    bd90:	8b080ec9 	add	x9, x22, x8, lsl #3
    bd94:	cb080048 	sub	x8, x2, x8
    bd98:	f840852a 	ldr	x10, [x9], #8
    bd9c:	f1000508 	subs	x8, x8, #0x1
    bda0:	8b130153 	add	x19, x10, x19
    bda4:	54ffffa1 	b.ne	bd98 <decoder_batch+0x22c>  // b.any
    bda8:	17ffff8e 	b	bbe0 <decoder_batch+0x74>
        }
    }
    return a + b + c + d;
    bdac:	8b1c0368 	add	x8, x27, x28
    bdb0:	8b130349 	add	x9, x26, x19
    bdb4:	8b090100 	add	x0, x8, x9
    bdb8:	14000002 	b	bdc0 <decoder_batch+0x254>
    bdbc:	aa1f03e0 	mov	x0, xzr
    bdc0:	910c43ff 	add	sp, sp, #0x310
    bdc4:	a9454ff4 	ldp	x20, x19, [sp, #80]
    bdc8:	a94457f6 	ldp	x22, x21, [sp, #64]
    bdcc:	a9435ff8 	ldp	x24, x23, [sp, #48]
    bdd0:	a94267fa 	ldp	x26, x25, [sp, #32]
    bdd4:	a9416ffc 	ldp	x28, x27, [sp, #16]
    bdd8:	a8c67bfd 	ldp	x29, x30, [sp], #96
    bddc:	d65f03c0 	ret

Disassembly of section .fini:
