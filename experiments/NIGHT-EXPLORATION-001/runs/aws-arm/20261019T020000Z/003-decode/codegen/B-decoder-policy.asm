
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build-long/B/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b92c <zbtScoreLeafDecodePolicy>:
    b92c:	34000f62 	cbz	w2, bb18 <zbtScoreLeafDecodePolicy+0x1ec>
    b930:	7100045f 	cmp	w2, #0x1
    b934:	54000401 	b.ne	b9b4 <zbtScoreLeafDecodePolicy+0x88>  // b.any
    b938:	3940d009 	ldrb	w9, [x0, #52]
    b93c:	3940d408 	ldrb	w8, [x0, #53]
    b940:	34000a29 	cbz	w9, ba84 <zbtScoreLeafDecodePolicy+0x158>
    b944:	34000088 	cbz	w8, b954 <zbtScoreLeafDecodePolicy+0x28>
    b948:	3940440a 	ldrb	w10, [x0, #17]
    b94c:	2a2103eb 	mvn	w11, w1
    b950:	0b0b0141 	add	w1, w10, w11
    b954:	9ba17d2a 	umull	x10, w9, w1
    b958:	d343fd4b 	lsr	x11, x10, #3
    b95c:	9240094e 	and	x14, x10, #0x7
    b960:	8b0b000c 	add	x12, x0, x11
    b964:	f9401d8d 	ldr	x13, [x12, #56]
    b968:	7200094c 	ands	w12, w10, #0x7
    b96c:	9ace25aa 	lsr	x10, x13, x14
    b970:	54000120 	b.eq	b994 <zbtScoreLeafDecodePolicy+0x68>  // b.none
    b974:	5280080d 	mov	w13, #0x40                  	// #64
    b978:	4b0c01ac 	sub	w12, w13, w12
    b97c:	6b09019f 	cmp	w12, w9
    b980:	540000a2 	b.cs	b994 <zbtScoreLeafDecodePolicy+0x68>  // b.hs, b.nlast
    b984:	8b00016b 	add	x11, x11, x0
    b988:	3941016b 	ldrb	w11, [x11, #64]
    b98c:	9acc216b 	lsl	x11, x11, x12
    b990:	aa0a016a 	orr	x10, x11, x10
    b994:	9280000b 	mov	x11, #0xffffffffffffffff    	// #-1
    b998:	7101013f 	cmp	w9, #0x40
    b99c:	9ac9216c 	lsl	x12, x11, x9
    b9a0:	da8c2169 	csinv	x9, x11, x12, cs	// cs = hs, nlast
    b9a4:	39404c0b 	ldrb	w11, [x0, #19]
    b9a8:	8a090149 	and	x9, x10, x9
    b9ac:	9acb2129 	lsl	x9, x9, x11
    b9b0:	14000036 	b	ba88 <zbtScoreLeafDecodePolicy+0x15c>
    b9b4:	3940d00b 	ldrb	w11, [x0, #52]
    b9b8:	f9401408 	ldr	x8, [x0, #40]
    b9bc:	3400078b 	cbz	w11, baac <zbtScoreLeafDecodePolicy+0x180>
    b9c0:	9280000a 	mov	x10, #0xffffffffffffffff    	// #-1
    b9c4:	39404c09 	ldrb	w9, [x0, #19]
    b9c8:	3940d40e 	ldrb	w14, [x0, #53]
    b9cc:	9acb214c 	lsl	x12, x10, x11
    b9d0:	7101017f 	cmp	w11, #0x40
    b9d4:	3940440f 	ldrb	w15, [x0, #17]
    b9d8:	da8c014a 	csinv	x10, x10, x12, eq	// eq = none
    b9dc:	7200097f 	tst	w11, #0x7
    b9e0:	54000760 	b.eq	bacc <zbtScoreLeafDecodePolicy+0x1a0>  // b.none
    b9e4:	7100ed7f 	cmp	w11, #0x3b
    b9e8:	9100e00c 	add	x12, x0, #0x38
    b9ec:	2a0203ed 	mov	w13, w2
    b9f0:	54000b03 	b.cc	bb50 <zbtScoreLeafDecodePolicy+0x224>  // b.lo, b.ul, b.last
    b9f4:	7100f17f 	cmp	w11, #0x3c
    b9f8:	54000ac0 	b.eq	bb50 <zbtScoreLeafDecodePolicy+0x224>  // b.none
    b9fc:	2a2103f0 	mvn	w16, w1
    ba00:	0b0f020f 	add	w15, w16, w15
    ba04:	52800810 	mov	w16, #0x40                  	// #64
    ba08:	1400000e 	b	ba40 <zbtScoreLeafDecodePolicy+0x114>
    ba0c:	8a0a0231 	and	x17, x17, x10
    ba10:	72001ddf 	tst	w14, #0xff
    ba14:	d10005ad 	sub	x13, x13, #0x1
    ba18:	9ac92231 	lsl	x17, x17, x9
    ba1c:	11000421 	add	w1, w1, #0x1
    ba20:	510005ef 	sub	w15, w15, #0x1
    ba24:	da910631 	cneg	x17, x17, ne	// ne = any
    ba28:	8b080231 	add	x17, x17, x8
    ba2c:	9240fa32 	and	x18, x17, #0x7fffffffffffffff
    ba30:	f100023f 	cmp	x17, #0x0
    ba34:	da91b251 	csinv	x17, x18, x17, lt	// lt = tstop
    ba38:	f8008471 	str	x17, [x3], #8
    ba3c:	b40006ed 	cbz	x13, bb18 <zbtScoreLeafDecodePolicy+0x1ec>
    ba40:	72001ddf 	tst	w14, #0xff
    ba44:	1a8f0031 	csel	w17, w1, w15, eq	// eq = none
    ba48:	9bb17d71 	umull	x17, w11, w17
    ba4c:	d343fe32 	lsr	x18, x17, #3
    ba50:	92400a25 	and	x5, x17, #0x7
    ba54:	72000a22 	ands	w2, w17, #0x7
    ba58:	f8726984 	ldr	x4, [x12, x18]
    ba5c:	9ac52491 	lsr	x17, x4, x5
    ba60:	54fffd60 	b.eq	ba0c <zbtScoreLeafDecodePolicy+0xe0>  // b.none
    ba64:	4b020202 	sub	w2, w16, w2
    ba68:	6b0b005f 	cmp	w2, w11
    ba6c:	54fffd02 	b.cs	ba0c <zbtScoreLeafDecodePolicy+0xe0>  // b.hs, b.nlast
    ba70:	8b000252 	add	x18, x18, x0
    ba74:	39410252 	ldrb	w18, [x18, #64]
    ba78:	9ac22252 	lsl	x18, x18, x2
    ba7c:	aa110251 	orr	x17, x18, x17
    ba80:	17ffffe3 	b	ba0c <zbtScoreLeafDecodePolicy+0xe0>
    ba84:	aa1f03e9 	mov	x9, xzr
    ba88:	f940140a 	ldr	x10, [x0, #40]
    ba8c:	7100011f 	cmp	w8, #0x0
    ba90:	da890528 	cneg	x8, x9, ne	// ne = any
    ba94:	8b080148 	add	x8, x10, x8
    ba98:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    ba9c:	f100011f 	cmp	x8, #0x0
    baa0:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
    baa4:	f9000068 	str	x8, [x3]
    baa8:	d65f03c0 	ret
    baac:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    bab0:	f100011f 	cmp	x8, #0x0
    bab4:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
    bab8:	7100105f 	cmp	w2, #0x4
    babc:	2a0203e9 	mov	w9, w2
    bac0:	54000902 	b.cs	bbe0 <zbtScoreLeafDecodePolicy+0x2b4>  // b.hs, b.nlast
    bac4:	aa1f03ea 	mov	x10, xzr
    bac8:	14000050 	b	bc08 <zbtScoreLeafDecodePolicy+0x2dc>
    bacc:	d343fd6b 	lsr	x11, x11, #3
    bad0:	72001ddf 	tst	w14, #0xff
    bad4:	9100e00c 	add	x12, x0, #0x38
    bad8:	2a0203ed 	mov	w13, w2
    badc:	54000200 	b.eq	bb1c <zbtScoreLeafDecodePolicy+0x1f0>  // b.none
    bae0:	2a2103ee 	mvn	w14, w1
    bae4:	0b0f01ce 	add	w14, w14, w15
    bae8:	9bae7d6f 	umull	x15, w11, w14
    baec:	d10005ad 	sub	x13, x13, #0x1
    baf0:	510005ce 	sub	w14, w14, #0x1
    baf4:	f86f698f 	ldr	x15, [x12, x15]
    baf8:	8a0a01ef 	and	x15, x15, x10
    bafc:	9ac921ef 	lsl	x15, x15, x9
    bb00:	cb0f010f 	sub	x15, x8, x15
    bb04:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    bb08:	f10001ff 	cmp	x15, #0x0
    bb0c:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
    bb10:	f800846f 	str	x15, [x3], #8
    bb14:	b5fffead 	cbnz	x13, bae8 <zbtScoreLeafDecodePolicy+0x1bc>
    bb18:	d65f03c0 	ret
    bb1c:	9ba17d6e 	umull	x14, w11, w1
    bb20:	11000421 	add	w1, w1, #0x1
    bb24:	f86e698e 	ldr	x14, [x12, x14]
    bb28:	8a0a01ce 	and	x14, x14, x10
    bb2c:	9ac921ce 	lsl	x14, x14, x9
    bb30:	8b0801ce 	add	x14, x14, x8
    bb34:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    bb38:	f10001df 	cmp	x14, #0x0
    bb3c:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
    bb40:	f10005ad 	subs	x13, x13, #0x1
    bb44:	f800846e 	str	x14, [x3], #8
    bb48:	54fffea1 	b.ne	bb1c <zbtScoreLeafDecodePolicy+0x1f0>  // b.any
    bb4c:	17fffff3 	b	bb18 <zbtScoreLeafDecodePolicy+0x1ec>
    bb50:	72001ddf 	tst	w14, #0xff
    bb54:	54000260 	b.eq	bba0 <zbtScoreLeafDecodePolicy+0x274>  // b.none
    bb58:	2a2103ee 	mvn	w14, w1
    bb5c:	0b0f01ce 	add	w14, w14, w15
    bb60:	9bae7d6f 	umull	x15, w11, w14
    bb64:	d10005ad 	sub	x13, x13, #0x1
    bb68:	510005ce 	sub	w14, w14, #0x1
    bb6c:	d343fdf0 	lsr	x16, x15, #3
    bb70:	924009ef 	and	x15, x15, #0x7
    bb74:	f8706990 	ldr	x16, [x12, x16]
    bb78:	9acf260f 	lsr	x15, x16, x15
    bb7c:	8a0a01ef 	and	x15, x15, x10
    bb80:	9ac921ef 	lsl	x15, x15, x9
    bb84:	cb0f010f 	sub	x15, x8, x15
    bb88:	9240f9f0 	and	x16, x15, #0x7fffffffffffffff
    bb8c:	f10001ff 	cmp	x15, #0x0
    bb90:	da8fb20f 	csinv	x15, x16, x15, lt	// lt = tstop
    bb94:	f800846f 	str	x15, [x3], #8
    bb98:	b5fffe4d 	cbnz	x13, bb60 <zbtScoreLeafDecodePolicy+0x234>
    bb9c:	17ffffdf 	b	bb18 <zbtScoreLeafDecodePolicy+0x1ec>
    bba0:	9ba17d6e 	umull	x14, w11, w1
    bba4:	11000421 	add	w1, w1, #0x1
    bba8:	d343fdcf 	lsr	x15, x14, #3
    bbac:	924009ce 	and	x14, x14, #0x7
    bbb0:	f86f698f 	ldr	x15, [x12, x15]
    bbb4:	9ace25ee 	lsr	x14, x15, x14
    bbb8:	8a0a01ce 	and	x14, x14, x10
    bbbc:	9ac921ce 	lsl	x14, x14, x9
    bbc0:	8b0801ce 	add	x14, x14, x8
    bbc4:	9240f9cf 	and	x15, x14, #0x7fffffffffffffff
    bbc8:	f10001df 	cmp	x14, #0x0
    bbcc:	da8eb1ee 	csinv	x14, x15, x14, lt	// lt = tstop
    bbd0:	f10005ad 	subs	x13, x13, #0x1
    bbd4:	f800846e 	str	x14, [x3], #8
    bbd8:	54fffe41 	b.ne	bba0 <zbtScoreLeafDecodePolicy+0x274>  // b.any
    bbdc:	17ffffcf 	b	bb18 <zbtScoreLeafDecodePolicy+0x1ec>
    bbe0:	4e080d00 	dup	v0.2d, x8
    bbe4:	927e752a 	and	x10, x9, #0xfffffffc
    bbe8:	9100406b 	add	x11, x3, #0x10
    bbec:	aa0a03ec 	mov	x12, x10
    bbf0:	ad3f8160 	stp	q0, q0, [x11, #-16]
    bbf4:	f100118c 	subs	x12, x12, #0x4
    bbf8:	9100816b 	add	x11, x11, #0x20
    bbfc:	54ffffa1 	b.ne	bbf0 <zbtScoreLeafDecodePolicy+0x2c4>  // b.any
    bc00:	eb09015f 	cmp	x10, x9
    bc04:	54fff8a0 	b.eq	bb18 <zbtScoreLeafDecodePolicy+0x1ec>  // b.none
    bc08:	8b0a0c6b 	add	x11, x3, x10, lsl #3
    bc0c:	cb0a0129 	sub	x9, x9, x10
    bc10:	f1000529 	subs	x9, x9, #0x1
    bc14:	f8008568 	str	x8, [x11], #8
    bc18:	54ffffc1 	b.ne	bc10 <zbtScoreLeafDecodePolicy+0x2e4>  // b.any
    bc1c:	17ffffbf 	b	bb18 <zbtScoreLeafDecodePolicy+0x1ec>

Disassembly of section .fini:
