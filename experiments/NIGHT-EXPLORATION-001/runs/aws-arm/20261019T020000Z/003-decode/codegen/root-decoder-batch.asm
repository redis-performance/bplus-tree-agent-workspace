
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build-long/root/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b8f8 <decoder_batch>:
    b8f8:	34001801 	cbz	w1, bbf8 <decoder_batch+0x300>
    b8fc:	f81c0ffd 	str	x29, [sp, #-64]!
    b900:	a9015ff8 	stp	x24, x23, [sp, #16]
    b904:	a90257f6 	stp	x22, x21, [sp, #32]
    b908:	a9034ff4 	stp	x20, x19, [sp, #48]
    b90c:	d10c03ff 	sub	sp, sp, #0x300
    b910:	910003e9 	mov	x9, sp
    b914:	aa1f03e2 	mov	x2, xzr
    b918:	2a1f03e8 	mov	w8, wzr
    b91c:	aa1f03f0 	mov	x16, xzr
    b920:	aa1f03f1 	mov	x17, xzr
    b924:	aa1f03f2 	mov	x18, xzr
    b928:	9101012a 	add	x10, x9, #0x40
    b92c:	9100412b 	add	x11, x9, #0x10
    b930:	9280000c 	mov	x12, #0xffffffffffffffff    	// #-1
    b934:	5280080d 	mov	w13, #0x40                  	// #64
    b938:	14000004 	b	b948 <decoder_batch+0x50>
    b93c:	11000508 	add	w8, w8, #0x1
    b940:	6b01011f 	cmp	w8, w1
    b944:	54001480 	b.eq	bbd4 <decoder_batch+0x2dc>  // b.none
    b948:	b940040e 	ldr	w14, [x0, #4]
    b94c:	34ffff8e 	cbz	w14, b93c <decoder_batch+0x44>
    b950:	b940000e 	ldr	w14, [x0]
    b954:	aa1f03ef 	mov	x15, xzr
    b958:	14000005 	b	b96c <decoder_batch+0x74>
    b95c:	b9400403 	ldr	w3, [x0, #4]
    b960:	910005ef 	add	x15, x15, #0x1
    b964:	eb0301ff 	cmp	x15, x3
    b968:	54fffea2 	b.cs	b93c <decoder_batch+0x44>  // b.hs, b.nlast
    b96c:	b400062e 	cbz	x14, ba30 <decoder_batch+0x138>
    b970:	f9400404 	ldr	x4, [x0, #8]
    b974:	aa1f03e3 	mov	x3, xzr
    b978:	f86f7884 	ldr	x4, [x4, x15, lsl #3]
    b97c:	f9401485 	ldr	x5, [x4, #40]
    b980:	9100e086 	add	x6, x4, #0x38
    b984:	14000011 	b	b9c8 <decoder_batch+0xd0>
    b988:	9ad32195 	lsl	x21, x12, x19
    b98c:	7101027f 	cmp	w19, #0x40
    b990:	da952193 	csinv	x19, x12, x21, cs	// cs = hs, nlast
    b994:	39404c95 	ldrb	w21, [x4, #19]
    b998:	8a130293 	and	x19, x20, x19
    b99c:	9ad52273 	lsl	x19, x19, x21
    b9a0:	710000ff 	cmp	w7, #0x0
    b9a4:	da930667 	cneg	x7, x19, ne	// ne = any
    b9a8:	8b0500e7 	add	x7, x7, x5
    b9ac:	9240f8f3 	and	x19, x7, #0x7fffffffffffffff
    b9b0:	f10000ff 	cmp	x7, #0x0
    b9b4:	da87b267 	csinv	x7, x19, x7, lt	// lt = tstop
    b9b8:	f8237927 	str	x7, [x9, x3, lsl #3]
    b9bc:	91000463 	add	x3, x3, #0x1
    b9c0:	eb0301df 	cmp	x14, x3
    b9c4:	54000360 	b.eq	ba30 <decoder_batch+0x138>  // b.none
    b9c8:	3940d093 	ldrb	w19, [x4, #52]
    b9cc:	3940d487 	ldrb	w7, [x4, #53]
    b9d0:	340002d3 	cbz	w19, ba28 <decoder_batch+0x130>
    b9d4:	aa0303f4 	mov	x20, x3
    b9d8:	34000087 	cbz	w7, b9e8 <decoder_batch+0xf0>
    b9dc:	39404494 	ldrb	w20, [x4, #17]
    b9e0:	d2407c75 	eor	x21, x3, #0xffffffff
    b9e4:	8b1402b4 	add	x20, x21, x20
    b9e8:	92407e94 	and	x20, x20, #0xffffffff
    b9ec:	9bb37e94 	umull	x20, w20, w19
    b9f0:	d343fe95 	lsr	x21, x20, #3
    b9f4:	92400a98 	and	x24, x20, #0x7
    b9f8:	72000a96 	ands	w22, w20, #0x7
    b9fc:	f87568d7 	ldr	x23, [x6, x21]
    ba00:	9ad826f4 	lsr	x20, x23, x24
    ba04:	54fffc20 	b.eq	b988 <decoder_batch+0x90>  // b.none
    ba08:	4b1601b6 	sub	w22, w13, w22
    ba0c:	6b1302df 	cmp	w22, w19
    ba10:	54fffbc2 	b.cs	b988 <decoder_batch+0x90>  // b.hs, b.nlast
    ba14:	8b0402b5 	add	x21, x21, x4
    ba18:	394102b5 	ldrb	w21, [x21, #64]
    ba1c:	9ad622b5 	lsl	x21, x21, x22
    ba20:	aa1402b4 	orr	x20, x21, x20
    ba24:	17ffffd9 	b	b988 <decoder_batch+0x90>
    ba28:	aa1f03f3 	mov	x19, xzr
    ba2c:	17ffffdd 	b	b9a0 <decoder_batch+0xa8>
    ba30:	b940000e 	ldr	w14, [x0]
    ba34:	710011df 	cmp	w14, #0x4
    ba38:	54000103 	b.cc	ba58 <decoder_batch+0x160>  // b.lo, b.ul, b.last
    ba3c:	d10011c4 	sub	x4, x14, #0x4
    ba40:	927e75c3 	and	x3, x14, #0xfffffffc
    ba44:	f100309f 	cmp	x4, #0xc
    ba48:	540000c2 	b.cs	ba60 <decoder_batch+0x168>  // b.hs, b.nlast
    ba4c:	aa1f03e4 	mov	x4, xzr
    ba50:	52800065 	mov	w5, #0x3                   	// #3
    ba54:	14000034 	b	bb24 <decoder_batch+0x22c>
    ba58:	aa1f03e3 	mov	x3, xzr
    ba5c:	1400003f 	b	bb58 <decoder_batch+0x260>
    ba60:	d342fc84 	lsr	x4, x4, #2
    ba64:	6f00e403 	movi	v3.2d, #0x0
    ba68:	6f00e402 	movi	v2.2d, #0x0
    ba6c:	6f00e401 	movi	v1.2d, #0x0
    ba70:	6f00e400 	movi	v0.2d, #0x0
    ba74:	52800065 	mov	w5, #0x3                   	// #3
    ba78:	91000486 	add	x6, x4, #0x1
    ba7c:	6f00e404 	movi	v4.2d, #0x0
    ba80:	6f00e407 	movi	v7.2d, #0x0
    ba84:	927ef0c7 	and	x7, x6, #0x7ffffffffffffffc
    ba88:	6f00e406 	movi	v6.2d, #0x0
    ba8c:	6f00e405 	movi	v5.2d, #0x0
    ba90:	d342fcf3 	lsr	x19, x7, #2
    ba94:	4e081c43 	mov	v3.d[0], x2
    ba98:	4e081e02 	mov	v2.d[0], x16
    ba9c:	4e081e21 	mov	v1.d[0], x17
    baa0:	4e081e40 	mov	v0.d[0], x18
    baa4:	d37ef4e4 	lsl	x4, x7, #2
    baa8:	b37cee65 	bfi	x5, x19, #4, #60
    baac:	aa0703f0 	mov	x16, x7
    bab0:	aa0a03f1 	mov	x17, x10
    bab4:	d1010232 	sub	x18, x17, #0x40
    bab8:	4c400e30 	ld4	{v16.2d-v19.2d}, [x17]
    babc:	f1001210 	subs	x16, x16, #0x4
    bac0:	91020231 	add	x17, x17, #0x80
    bac4:	4c400e54 	ld4	{v20.2d-v23.2d}, [x18]
    bac8:	4ee48604 	add	v4.2d, v16.2d, v4.2d
    bacc:	4ee58625 	add	v5.2d, v17.2d, v5.2d
    bad0:	4ee68646 	add	v6.2d, v18.2d, v6.2d
    bad4:	4ee38683 	add	v3.2d, v20.2d, v3.2d
    bad8:	4ee086a0 	add	v0.2d, v21.2d, v0.2d
    badc:	4ee186c1 	add	v1.2d, v22.2d, v1.2d
    bae0:	4ee286e2 	add	v2.2d, v23.2d, v2.2d
    bae4:	4ee78667 	add	v7.2d, v19.2d, v7.2d
    bae8:	54fffe61 	b.ne	bab4 <decoder_batch+0x1bc>  // b.any
    baec:	4ee38483 	add	v3.2d, v4.2d, v3.2d
    baf0:	4ee284e2 	add	v2.2d, v7.2d, v2.2d
    baf4:	eb0700df 	cmp	x6, x7
    baf8:	4ee184c1 	add	v1.2d, v6.2d, v1.2d
    bafc:	4ee084a0 	add	v0.2d, v5.2d, v0.2d
    bb00:	5ef1b863 	addp	d3, v3.2d
    bb04:	5ef1b842 	addp	d2, v2.2d
    bb08:	5ef1b821 	addp	d1, v1.2d
    bb0c:	5ef1b800 	addp	d0, v0.2d
    bb10:	9e660062 	fmov	x2, d3
    bb14:	9e660050 	fmov	x16, d2
    bb18:	9e660031 	fmov	x17, d1
    bb1c:	9e660012 	fmov	x18, d0
    bb20:	540001c0 	b.eq	bb58 <decoder_batch+0x260>  // b.none
    bb24:	8b050d25 	add	x5, x9, x5, lsl #3
    bb28:	8b040d66 	add	x6, x11, x4, lsl #3
    bb2c:	91000c84 	add	x4, x4, #0x3
    bb30:	a97f4cc7 	ldp	x7, x19, [x6, #-16]
    bb34:	91001084 	add	x4, x4, #0x4
    bb38:	f84204d4 	ldr	x20, [x6], #32
    bb3c:	eb0e009f 	cmp	x4, x14
    bb40:	f84204b5 	ldr	x21, [x5], #32
    bb44:	8b0200e2 	add	x2, x7, x2
    bb48:	8b120272 	add	x18, x19, x18
    bb4c:	8b110291 	add	x17, x20, x17
    bb50:	8b1002b0 	add	x16, x21, x16
    bb54:	54fffee3 	b.cc	bb30 <decoder_batch+0x238>  // b.lo, b.ul, b.last
    bb58:	eb0e007f 	cmp	x3, x14
    bb5c:	54fff002 	b.cs	b95c <decoder_batch+0x64>  // b.hs, b.nlast
    bb60:	cb0301c5 	sub	x5, x14, x3
    bb64:	f10010bf 	cmp	x5, #0x4
    bb68:	54000283 	b.cc	bbb8 <decoder_batch+0x2c0>  // b.lo, b.ul, b.last
    bb6c:	6f00e400 	movi	v0.2d, #0x0
    bb70:	6f00e401 	movi	v1.2d, #0x0
    bb74:	924005c4 	and	x4, x14, #0x3
    bb78:	cb0400a5 	sub	x5, x5, x4
    bb7c:	8b040066 	add	x6, x3, x4
    bb80:	4e081c40 	mov	v0.d[0], x2
    bb84:	8b030d62 	add	x2, x11, x3, lsl #3
    bb88:	8b0300a3 	add	x3, x5, x3
    bb8c:	cb0e00c5 	sub	x5, x6, x14
    bb90:	ad7f8c42 	ldp	q2, q3, [x2, #-16]
    bb94:	b10010a5 	adds	x5, x5, #0x4
    bb98:	91008042 	add	x2, x2, #0x20
    bb9c:	4ee08440 	add	v0.2d, v2.2d, v0.2d
    bba0:	4ee18461 	add	v1.2d, v3.2d, v1.2d
    bba4:	54ffff61 	b.ne	bb90 <decoder_batch+0x298>  // b.any
    bba8:	4ee08420 	add	v0.2d, v1.2d, v0.2d
    bbac:	5ef1b800 	addp	d0, v0.2d
    bbb0:	9e660002 	fmov	x2, d0
    bbb4:	b4ffed44 	cbz	x4, b95c <decoder_batch+0x64>
    bbb8:	8b030d24 	add	x4, x9, x3, lsl #3
    bbbc:	cb0301c3 	sub	x3, x14, x3
    bbc0:	f8408485 	ldr	x5, [x4], #8
    bbc4:	f1000463 	subs	x3, x3, #0x1
    bbc8:	8b0200a2 	add	x2, x5, x2
    bbcc:	54ffffa1 	b.ne	bbc0 <decoder_batch+0x2c8>  // b.any
    bbd0:	17ffff63 	b	b95c <decoder_batch+0x64>
    bbd4:	8b120228 	add	x8, x17, x18
    bbd8:	8b020209 	add	x9, x16, x2
    bbdc:	8b090100 	add	x0, x8, x9
    bbe0:	910c03ff 	add	sp, sp, #0x300
    bbe4:	a9434ff4 	ldp	x20, x19, [sp, #48]
    bbe8:	a94257f6 	ldp	x22, x21, [sp, #32]
    bbec:	a9415ff8 	ldp	x24, x23, [sp, #16]
    bbf0:	f84407fd 	ldr	x29, [sp], #64
    bbf4:	d65f03c0 	ret
    bbf8:	aa1f03e0 	mov	x0, xzr
    bbfc:	d65f03c0 	ret

Disassembly of section .fini:
