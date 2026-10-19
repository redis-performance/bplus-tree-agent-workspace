
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build-long/base/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b92c <zbtScoreLeafDecodePolicy>:
    b92c:	34001222 	cbz	w2, bb70 <zbtScoreLeafDecodePolicy+0x244>
    b930:	3940d00b 	ldrb	w11, [x0, #52]
    b934:	f9401408 	ldr	x8, [x0, #40]
    b938:	3400064b 	cbz	w11, ba00 <zbtScoreLeafDecodePolicy+0xd4>
    b93c:	9280000a 	mov	x10, #0xffffffffffffffff    	// #-1
    b940:	39404c09 	ldrb	w9, [x0, #19]
    b944:	3940d40e 	ldrb	w14, [x0, #53]
    b948:	9acb214c 	lsl	x12, x10, x11
    b94c:	7101017f 	cmp	w11, #0x40
    b950:	3940440f 	ldrb	w15, [x0, #17]
    b954:	da8c014a 	csinv	x10, x10, x12, eq	// eq = none
    b958:	7200097f 	tst	w11, #0x7
    b95c:	54000620 	b.eq	ba20 <zbtScoreLeafDecodePolicy+0xf4>  // b.none
    b960:	7100ed7f 	cmp	w11, #0x3b
    b964:	9100e00c 	add	x12, x0, #0x38
    b968:	2a0203ed 	mov	w13, w2
    b96c:	540009c3 	b.cc	baa4 <zbtScoreLeafDecodePolicy+0x178>  // b.lo, b.ul, b.last
    b970:	7100f17f 	cmp	w11, #0x3c
    b974:	54000980 	b.eq	baa4 <zbtScoreLeafDecodePolicy+0x178>  // b.none
    b978:	2a2103f0 	mvn	w16, w1
    b97c:	0b0f020f 	add	w15, w16, w15
    b980:	52800810 	mov	w16, #0x40                  	// #64
    b984:	1400000e 	b	b9bc <zbtScoreLeafDecodePolicy+0x90>
    b988:	8a0a0231 	and	x17, x17, x10
    b98c:	72001ddf 	tst	w14, #0xff
    b990:	d10005ad 	sub	x13, x13, #0x1
    b994:	9ac92231 	lsl	x17, x17, x9
    b998:	11000421 	add	w1, w1, #0x1
    b99c:	510005ef 	sub	w15, w15, #0x1
    b9a0:	da910631 	cneg	x17, x17, ne	// ne = any
    b9a4:	8b080231 	add	x17, x17, x8
    b9a8:	9240fa32 	and	x18, x17, #0x7fffffffffffffff
    b9ac:	f100023f 	cmp	x17, #0x0
    b9b0:	da91b251 	csinv	x17, x18, x17, lt	// lt = tstop
    b9b4:	f8008471 	str	x17, [x3], #8
    b9b8:	b4000dcd 	cbz	x13, bb70 <zbtScoreLeafDecodePolicy+0x244>
    b9bc:	72001ddf 	tst	w14, #0xff
    b9c0:	1a8f0031 	csel	w17, w1, w15, eq	// eq = none
    b9c4:	9bb17d71 	umull	x17, w11, w17
    b9c8:	d343fe32 	lsr	x18, x17, #3
    b9cc:	92400a25 	and	x5, x17, #0x7
    b9d0:	72000a22 	ands	w2, w17, #0x7
    b9d4:	f8726984 	ldr	x4, [x12, x18]
    b9d8:	9ac52491 	lsr	x17, x4, x5
    b9dc:	54fffd60 	b.eq	b988 <zbtScoreLeafDecodePolicy+0x5c>  // b.none
    b9e0:	4b020202 	sub	w2, w16, w2
    b9e4:	6b0b005f 	cmp	w2, w11
    b9e8:	54fffd02 	b.cs	b988 <zbtScoreLeafDecodePolicy+0x5c>  // b.hs, b.nlast
    b9ec:	8b000252 	add	x18, x18, x0
    b9f0:	39410252 	ldrb	w18, [x18, #64]
    b9f4:	9ac22252 	lsl	x18, x18, x2
    b9f8:	aa110251 	orr	x17, x18, x17
    b9fc:	17ffffe3 	b	b988 <zbtScoreLeafDecodePolicy+0x5c>
    ba00:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    ba04:	f100011f 	cmp	x8, #0x0
    ba08:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
    ba0c:	7100105f 	cmp	w2, #0x4
    ba10:	2a0203e9 	mov	w9, w2
    ba14:	54000902 	b.cs	bb34 <zbtScoreLeafDecodePolicy+0x208>  // b.hs, b.nlast
    ba18:	aa1f03ea 	mov	x10, xzr
    ba1c:	14000050 	b	bb5c <zbtScoreLeafDecodePolicy+0x230>
    ba20:	d343fd6b 	lsr	x11, x11, #3
    ba24:	72001ddf 	tst	w14, #0xff
    ba28:	9100e00c 	add	x12, x0, #0x38
    ba2c:	2a0203ed 	mov	w13, w2
    ba30:	54000200 	b.eq	ba70 <zbtScoreLeafDecodePolicy+0x144>  // b.none
    ba34:	2a2103ee 	mvn	w14, w1
    ba38:	0b0f01ce 	add	w14, w14, w15
    ba3c:	9bae7d6f 	umull	x15, w11, w14
    ba40:	d10005ad 	sub	x13, x13, #0x1
    ba44:	510005ce 	sub	w14, w14, #0x1
    ba48:	f86f698f 	ldr	x15, [x12, x15]
    ba4c:	8a0a01ef 	and	x15, x15, x10
    ba50:	9ac921ef 	lsl	x15, x15, x9
    ba54:	cb0f010f 	sub	x15, x8, x15
    ba58:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    ba5c:	f10001ff 	cmp	x15, #0x0
    ba60:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
    ba64:	f800846f 	str	x15, [x3], #8
    ba68:	b5fffead 	cbnz	x13, ba3c <zbtScoreLeafDecodePolicy+0x110>
    ba6c:	14000041 	b	bb70 <zbtScoreLeafDecodePolicy+0x244>
    ba70:	9ba17d6e 	umull	x14, w11, w1
    ba74:	11000421 	add	w1, w1, #0x1
    ba78:	f86e698e 	ldr	x14, [x12, x14]
    ba7c:	8a0a01ce 	and	x14, x14, x10
    ba80:	9ac921ce 	lsl	x14, x14, x9
    ba84:	8b0801ce 	add	x14, x14, x8
    ba88:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    ba8c:	f10001df 	cmp	x14, #0x0
    ba90:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
    ba94:	f10005ad 	subs	x13, x13, #0x1
    ba98:	f800846e 	str	x14, [x3], #8
    ba9c:	54fffea1 	b.ne	ba70 <zbtScoreLeafDecodePolicy+0x144>  // b.any
    baa0:	14000034 	b	bb70 <zbtScoreLeafDecodePolicy+0x244>
    baa4:	72001ddf 	tst	w14, #0xff
    baa8:	54000260 	b.eq	baf4 <zbtScoreLeafDecodePolicy+0x1c8>  // b.none
    baac:	2a2103ee 	mvn	w14, w1
    bab0:	0b0f01ce 	add	w14, w14, w15
    bab4:	9bae7d6f 	umull	x15, w11, w14
    bab8:	d10005ad 	sub	x13, x13, #0x1
    babc:	510005ce 	sub	w14, w14, #0x1
    bac0:	d343fdf0 	lsr	x16, x15, #3
    bac4:	924009ef 	and	x15, x15, #0x7
    bac8:	f8706990 	ldr	x16, [x12, x16]
    bacc:	9acf260f 	lsr	x15, x16, x15
    bad0:	8a0a01ef 	and	x15, x15, x10
    bad4:	9ac921ef 	lsl	x15, x15, x9
    bad8:	cb0f010f 	sub	x15, x8, x15
    badc:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    bae0:	f10001ff 	cmp	x15, #0x0
    bae4:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
    bae8:	f800846f 	str	x15, [x3], #8
    baec:	b5fffe4d 	cbnz	x13, bab4 <zbtScoreLeafDecodePolicy+0x188>
    baf0:	14000020 	b	bb70 <zbtScoreLeafDecodePolicy+0x244>
    baf4:	9ba17d6e 	umull	x14, w11, w1
    baf8:	11000421 	add	w1, w1, #0x1
    bafc:	d343fdcf 	lsr	x15, x14, #3
    bb00:	924009ce 	and	x14, x14, #0x7
    bb04:	f86f698f 	ldr	x15, [x12, x15]
    bb08:	9ace25ee 	lsr	x14, x15, x14
    bb0c:	8a0a01ce 	and	x14, x14, x10
    bb10:	9ac921ce 	lsl	x14, x14, x9
    bb14:	8b0801ce 	add	x14, x14, x8
    bb18:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    bb1c:	f10001df 	cmp	x14, #0x0
    bb20:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
    bb24:	f10005ad 	subs	x13, x13, #0x1
    bb28:	f800846e 	str	x14, [x3], #8
    bb2c:	54fffe41 	b.ne	baf4 <zbtScoreLeafDecodePolicy+0x1c8>  // b.any
    bb30:	14000010 	b	bb70 <zbtScoreLeafDecodePolicy+0x244>
    bb34:	4e080d00 	dup	v0.2d, x8
    bb38:	927e752a 	and	x10, x9, #0xfffffffc
    bb3c:	9100406b 	add	x11, x3, #0x10
    bb40:	aa0a03ec 	mov	x12, x10
    bb44:	ad3f8160 	stp	q0, q0, [x11, #-16]
    bb48:	f100118c 	subs	x12, x12, #0x4
    bb4c:	9100816b 	add	x11, x11, #0x20
    bb50:	54ffffa1 	b.ne	bb44 <zbtScoreLeafDecodePolicy+0x218>  // b.any
    bb54:	eb09015f 	cmp	x10, x9
    bb58:	540000c0 	b.eq	bb70 <zbtScoreLeafDecodePolicy+0x244>  // b.none
    bb5c:	8b0a0c6b 	add	x11, x3, x10, lsl #3
    bb60:	cb0a0129 	sub	x9, x9, x10
    bb64:	f1000529 	subs	x9, x9, #0x1
    bb68:	f8008568 	str	x8, [x11], #8
    bb6c:	54ffffc1 	b.ne	bb64 <zbtScoreLeafDecodePolicy+0x238>  // b.any
    bb70:	d65f03c0 	ret

Disassembly of section .fini:
