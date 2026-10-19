
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build-long/base/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000bb74 <decoder_batch>:
    bb74:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
    bb78:	a9016ffc 	stp	x28, x27, [sp, #16]
    bb7c:	a90267fa 	stp	x26, x25, [sp, #32]
    bb80:	a9035ff8 	stp	x24, x23, [sp, #48]
    bb84:	a90457f6 	stp	x22, x21, [sp, #64]
    bb88:	a9054ff4 	stp	x20, x19, [sp, #80]
    bb8c:	910003fd 	mov	x29, sp
    bb90:	d10c43ff 	sub	sp, sp, #0x310
    bb94:	b90007e1 	str	w1, [sp, #4]
    bb98:	34001161 	cbz	w1, bdc4 <decoder_batch+0x250>
    bb9c:	910023f6 	add	x22, sp, #0x8
    bba0:	aa0003f4 	mov	x20, x0
    bba4:	aa1f03f3 	mov	x19, xzr
    bba8:	2a1f03f5 	mov	w21, wzr
    bbac:	aa1f03fa 	mov	x26, xzr
    bbb0:	aa1f03fb 	mov	x27, xzr
    bbb4:	aa1f03fc 	mov	x28, xzr
    bbb8:	910102d7 	add	x23, x22, #0x40
    bbbc:	910042d8 	add	x24, x22, #0x10
    bbc0:	14000005 	b	bbd4 <decoder_batch+0x60>
    bbc4:	b94007e8 	ldr	w8, [sp, #4]
    bbc8:	110006b5 	add	w21, w21, #0x1
    bbcc:	6b0802bf 	cmp	w21, w8
    bbd0:	54000f20 	b.eq	bdb4 <decoder_batch+0x240>  // b.none
    bbd4:	b9400688 	ldr	w8, [x20, #4]
    bbd8:	34ffff68 	cbz	w8, bbc4 <decoder_batch+0x50>
    bbdc:	b9400282 	ldr	w2, [x20]
    bbe0:	aa1f03f9 	mov	x25, xzr
    bbe4:	14000005 	b	bbf8 <decoder_batch+0x84>
    bbe8:	b9400688 	ldr	w8, [x20, #4]
    bbec:	91000739 	add	x25, x25, #0x1
    bbf0:	eb08033f 	cmp	x25, x8
    bbf4:	54fffe82 	b.cs	bbc4 <decoder_batch+0x50>  // b.hs, b.nlast
    bbf8:	f9400688 	ldr	x8, [x20, #8]
    bbfc:	910023e3 	add	x3, sp, #0x8
    bc00:	2a1f03e1 	mov	w1, wzr
    bc04:	f8797900 	ldr	x0, [x8, x25, lsl #3]
    bc08:	97ffff49 	bl	b92c <zbtScoreLeafDecodePolicy>
    bc0c:	b9400282 	ldr	w2, [x20]
    bc10:	7100105f 	cmp	w2, #0x4
    bc14:	54000103 	b.cc	bc34 <decoder_batch+0xc0>  // b.lo, b.ul, b.last
    bc18:	d1001049 	sub	x9, x2, #0x4
    bc1c:	121e7448 	and	w8, w2, #0xfffffffc
    bc20:	f100313f 	cmp	x9, #0xc
    bc24:	540000c2 	b.cs	bc3c <decoder_batch+0xc8>  // b.hs, b.nlast
    bc28:	aa1f03e9 	mov	x9, xzr
    bc2c:	5280006a 	mov	w10, #0x3                   	// #3
    bc30:	14000034 	b	bd00 <decoder_batch+0x18c>
    bc34:	2a1f03e8 	mov	w8, wzr
    bc38:	1400003f 	b	bd34 <decoder_batch+0x1c0>
    bc3c:	d342fd29 	lsr	x9, x9, #2
    bc40:	6f00e403 	movi	v3.2d, #0x0
    bc44:	6f00e402 	movi	v2.2d, #0x0
    bc48:	6f00e401 	movi	v1.2d, #0x0
    bc4c:	6f00e400 	movi	v0.2d, #0x0
    bc50:	5280006a 	mov	w10, #0x3                   	// #3
    bc54:	9100052b 	add	x11, x9, #0x1
    bc58:	6f00e404 	movi	v4.2d, #0x0
    bc5c:	6f00e407 	movi	v7.2d, #0x0
    bc60:	927ef16c 	and	x12, x11, #0x7ffffffffffffffc
    bc64:	6f00e406 	movi	v6.2d, #0x0
    bc68:	6f00e405 	movi	v5.2d, #0x0
    bc6c:	d342fd8d 	lsr	x13, x12, #2
    bc70:	4e081e63 	mov	v3.d[0], x19
    bc74:	4e081f42 	mov	v2.d[0], x26
    bc78:	4e081f61 	mov	v1.d[0], x27
    bc7c:	4e081f80 	mov	v0.d[0], x28
    bc80:	d37ef589 	lsl	x9, x12, #2
    bc84:	b37cedaa 	bfi	x10, x13, #4, #60
    bc88:	aa0c03ed 	mov	x13, x12
    bc8c:	aa1703ee 	mov	x14, x23
    bc90:	d10101cf 	sub	x15, x14, #0x40
    bc94:	4c400dd0 	ld4	{v16.2d-v19.2d}, [x14]
    bc98:	f10011ad 	subs	x13, x13, #0x4
    bc9c:	910201ce 	add	x14, x14, #0x80
    bca0:	4c400df4 	ld4	{v20.2d-v23.2d}, [x15]
    bca4:	4ee48604 	add	v4.2d, v16.2d, v4.2d
    bca8:	4ee58625 	add	v5.2d, v17.2d, v5.2d
    bcac:	4ee68646 	add	v6.2d, v18.2d, v6.2d
    bcb0:	4ee38683 	add	v3.2d, v20.2d, v3.2d
    bcb4:	4ee086a0 	add	v0.2d, v21.2d, v0.2d
    bcb8:	4ee186c1 	add	v1.2d, v22.2d, v1.2d
    bcbc:	4ee286e2 	add	v2.2d, v23.2d, v2.2d
    bcc0:	4ee78667 	add	v7.2d, v19.2d, v7.2d
    bcc4:	54fffe61 	b.ne	bc90 <decoder_batch+0x11c>  // b.any
    bcc8:	4ee38483 	add	v3.2d, v4.2d, v3.2d
    bccc:	4ee284e2 	add	v2.2d, v7.2d, v2.2d
    bcd0:	eb0c017f 	cmp	x11, x12
    bcd4:	4ee184c1 	add	v1.2d, v6.2d, v1.2d
    bcd8:	4ee084a0 	add	v0.2d, v5.2d, v0.2d
    bcdc:	5ef1b863 	addp	d3, v3.2d
    bce0:	5ef1b842 	addp	d2, v2.2d
    bce4:	5ef1b821 	addp	d1, v1.2d
    bce8:	5ef1b800 	addp	d0, v0.2d
    bcec:	9e660073 	fmov	x19, d3
    bcf0:	9e66005a 	fmov	x26, d2
    bcf4:	9e66003b 	fmov	x27, d1
    bcf8:	9e66001c 	fmov	x28, d0
    bcfc:	540001c0 	b.eq	bd34 <decoder_batch+0x1c0>  // b.none
    bd00:	8b0a0eca 	add	x10, x22, x10, lsl #3
    bd04:	8b090f0b 	add	x11, x24, x9, lsl #3
    bd08:	91000d29 	add	x9, x9, #0x3
    bd0c:	a97f356c 	ldp	x12, x13, [x11, #-16]
    bd10:	91001129 	add	x9, x9, #0x4
    bd14:	f842056e 	ldr	x14, [x11], #32
    bd18:	eb02013f 	cmp	x9, x2
    bd1c:	f842054f 	ldr	x15, [x10], #32
    bd20:	8b130193 	add	x19, x12, x19
    bd24:	8b1c01bc 	add	x28, x13, x28
    bd28:	8b1b01db 	add	x27, x14, x27
    bd2c:	8b1a01fa 	add	x26, x15, x26
    bd30:	54fffee3 	b.cc	bd0c <decoder_batch+0x198>  // b.lo, b.ul, b.last
    bd34:	6b02011f 	cmp	w8, w2
    bd38:	54fff582 	b.cs	bbe8 <decoder_batch+0x74>  // b.hs, b.nlast
    bd3c:	2a0803e8 	mov	w8, w8
    bd40:	cb08004a 	sub	x10, x2, x8
    bd44:	f100115f 	cmp	x10, #0x4
    bd48:	54000283 	b.cc	bd98 <decoder_batch+0x224>  // b.lo, b.ul, b.last
    bd4c:	6f00e400 	movi	v0.2d, #0x0
    bd50:	6f00e401 	movi	v1.2d, #0x0
    bd54:	92400449 	and	x9, x2, #0x3
    bd58:	cb09014b 	sub	x11, x10, x9
    bd5c:	8b09010c 	add	x12, x8, x9
    bd60:	8b080f0a 	add	x10, x24, x8, lsl #3
    bd64:	8b080168 	add	x8, x11, x8
    bd68:	cb02018b 	sub	x11, x12, x2
    bd6c:	4e081e60 	mov	v0.d[0], x19
    bd70:	ad7f8d42 	ldp	q2, q3, [x10, #-16]
    bd74:	b100116b 	adds	x11, x11, #0x4
    bd78:	9100814a 	add	x10, x10, #0x20
    bd7c:	4ee08440 	add	v0.2d, v2.2d, v0.2d
    bd80:	4ee18461 	add	v1.2d, v3.2d, v1.2d
    bd84:	54ffff61 	b.ne	bd70 <decoder_batch+0x1fc>  // b.any
    bd88:	4ee08420 	add	v0.2d, v1.2d, v0.2d
    bd8c:	5ef1b800 	addp	d0, v0.2d
    bd90:	9e660013 	fmov	x19, d0
    bd94:	b4fff2a9 	cbz	x9, bbe8 <decoder_batch+0x74>
    bd98:	8b080ec9 	add	x9, x22, x8, lsl #3
    bd9c:	cb080048 	sub	x8, x2, x8
    bda0:	f840852a 	ldr	x10, [x9], #8
    bda4:	f1000508 	subs	x8, x8, #0x1
    bda8:	8b130153 	add	x19, x10, x19
    bdac:	54ffffa1 	b.ne	bda0 <decoder_batch+0x22c>  // b.any
    bdb0:	17ffff8e 	b	bbe8 <decoder_batch+0x74>
    bdb4:	8b1c0368 	add	x8, x27, x28
    bdb8:	8b130349 	add	x9, x26, x19
    bdbc:	8b090100 	add	x0, x8, x9
    bdc0:	14000002 	b	bdc8 <decoder_batch+0x254>
    bdc4:	aa1f03e0 	mov	x0, xzr
    bdc8:	910c43ff 	add	sp, sp, #0x310
    bdcc:	a9454ff4 	ldp	x20, x19, [sp, #80]
    bdd0:	a94457f6 	ldp	x22, x21, [sp, #64]
    bdd4:	a9435ff8 	ldp	x24, x23, [sp, #48]
    bdd8:	a94267fa 	ldp	x26, x25, [sp, #32]
    bddc:	a9416ffc 	ldp	x28, x27, [sp, #16]
    bde0:	a8c67bfd 	ldp	x29, x30, [sp], #96
    bde4:	d65f03c0 	ret

Disassembly of section .fini:
