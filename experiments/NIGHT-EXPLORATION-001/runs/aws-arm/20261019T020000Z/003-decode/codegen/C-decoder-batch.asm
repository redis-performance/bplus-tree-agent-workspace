
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/build-long/C/decoder-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000bc20 <decoder_batch>:
    bc20:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
    bc24:	a9016ffc 	stp	x28, x27, [sp, #16]
    bc28:	a90267fa 	stp	x26, x25, [sp, #32]
    bc2c:	a9035ff8 	stp	x24, x23, [sp, #48]
    bc30:	a90457f6 	stp	x22, x21, [sp, #64]
    bc34:	a9054ff4 	stp	x20, x19, [sp, #80]
    bc38:	910003fd 	mov	x29, sp
    bc3c:	d10c43ff 	sub	sp, sp, #0x310
    bc40:	b90007e1 	str	w1, [sp, #4]
    bc44:	34001161 	cbz	w1, be70 <decoder_batch+0x250>
    bc48:	910023f6 	add	x22, sp, #0x8
    bc4c:	aa0003f4 	mov	x20, x0
    bc50:	aa1f03f3 	mov	x19, xzr
    bc54:	2a1f03f5 	mov	w21, wzr
    bc58:	aa1f03fa 	mov	x26, xzr
    bc5c:	aa1f03fb 	mov	x27, xzr
    bc60:	aa1f03fc 	mov	x28, xzr
    bc64:	910102d7 	add	x23, x22, #0x40
    bc68:	910042d8 	add	x24, x22, #0x10
    bc6c:	14000005 	b	bc80 <decoder_batch+0x60>
    bc70:	b94007e8 	ldr	w8, [sp, #4]
    bc74:	110006b5 	add	w21, w21, #0x1
    bc78:	6b0802bf 	cmp	w21, w8
    bc7c:	54000f20 	b.eq	be60 <decoder_batch+0x240>  // b.none
    bc80:	b9400688 	ldr	w8, [x20, #4]
    bc84:	34ffff68 	cbz	w8, bc70 <decoder_batch+0x50>
    bc88:	b9400282 	ldr	w2, [x20]
    bc8c:	aa1f03f9 	mov	x25, xzr
    bc90:	14000005 	b	bca4 <decoder_batch+0x84>
    bc94:	b9400688 	ldr	w8, [x20, #4]
    bc98:	91000739 	add	x25, x25, #0x1
    bc9c:	eb08033f 	cmp	x25, x8
    bca0:	54fffe82 	b.cs	bc70 <decoder_batch+0x50>  // b.hs, b.nlast
    bca4:	f9400688 	ldr	x8, [x20, #8]
    bca8:	910023e3 	add	x3, sp, #0x8
    bcac:	2a1f03e1 	mov	w1, wzr
    bcb0:	f8797900 	ldr	x0, [x8, x25, lsl #3]
    bcb4:	97ffff1e 	bl	b92c <zbtScoreLeafDecodePolicy>
    bcb8:	b9400282 	ldr	w2, [x20]
    bcbc:	7100105f 	cmp	w2, #0x4
    bcc0:	54000103 	b.cc	bce0 <decoder_batch+0xc0>  // b.lo, b.ul, b.last
    bcc4:	d1001049 	sub	x9, x2, #0x4
    bcc8:	121e7448 	and	w8, w2, #0xfffffffc
    bccc:	f100313f 	cmp	x9, #0xc
    bcd0:	540000c2 	b.cs	bce8 <decoder_batch+0xc8>  // b.hs, b.nlast
    bcd4:	aa1f03e9 	mov	x9, xzr
    bcd8:	5280006a 	mov	w10, #0x3                   	// #3
    bcdc:	14000034 	b	bdac <decoder_batch+0x18c>
    bce0:	2a1f03e8 	mov	w8, wzr
    bce4:	1400003f 	b	bde0 <decoder_batch+0x1c0>
    bce8:	d342fd29 	lsr	x9, x9, #2
    bcec:	6f00e403 	movi	v3.2d, #0x0
    bcf0:	6f00e402 	movi	v2.2d, #0x0
    bcf4:	6f00e401 	movi	v1.2d, #0x0
    bcf8:	6f00e400 	movi	v0.2d, #0x0
    bcfc:	5280006a 	mov	w10, #0x3                   	// #3
    bd00:	9100052b 	add	x11, x9, #0x1
    bd04:	6f00e404 	movi	v4.2d, #0x0
    bd08:	6f00e407 	movi	v7.2d, #0x0
    bd0c:	927ef16c 	and	x12, x11, #0x7ffffffffffffffc
    bd10:	6f00e406 	movi	v6.2d, #0x0
    bd14:	6f00e405 	movi	v5.2d, #0x0
    bd18:	d342fd8d 	lsr	x13, x12, #2
    bd1c:	4e081e63 	mov	v3.d[0], x19
    bd20:	4e081f42 	mov	v2.d[0], x26
    bd24:	4e081f61 	mov	v1.d[0], x27
    bd28:	4e081f80 	mov	v0.d[0], x28
    bd2c:	d37ef589 	lsl	x9, x12, #2
    bd30:	b37cedaa 	bfi	x10, x13, #4, #60
    bd34:	aa0c03ed 	mov	x13, x12
    bd38:	aa1703ee 	mov	x14, x23
    bd3c:	d10101cf 	sub	x15, x14, #0x40
    bd40:	4c400dd0 	ld4	{v16.2d-v19.2d}, [x14]
    bd44:	f10011ad 	subs	x13, x13, #0x4
    bd48:	910201ce 	add	x14, x14, #0x80
    bd4c:	4c400df4 	ld4	{v20.2d-v23.2d}, [x15]
    bd50:	4ee48604 	add	v4.2d, v16.2d, v4.2d
    bd54:	4ee58625 	add	v5.2d, v17.2d, v5.2d
    bd58:	4ee68646 	add	v6.2d, v18.2d, v6.2d
    bd5c:	4ee38683 	add	v3.2d, v20.2d, v3.2d
    bd60:	4ee086a0 	add	v0.2d, v21.2d, v0.2d
    bd64:	4ee186c1 	add	v1.2d, v22.2d, v1.2d
    bd68:	4ee286e2 	add	v2.2d, v23.2d, v2.2d
    bd6c:	4ee78667 	add	v7.2d, v19.2d, v7.2d
    bd70:	54fffe61 	b.ne	bd3c <decoder_batch+0x11c>  // b.any
    bd74:	4ee38483 	add	v3.2d, v4.2d, v3.2d
    bd78:	4ee284e2 	add	v2.2d, v7.2d, v2.2d
    bd7c:	eb0c017f 	cmp	x11, x12
    bd80:	4ee184c1 	add	v1.2d, v6.2d, v1.2d
    bd84:	4ee084a0 	add	v0.2d, v5.2d, v0.2d
    bd88:	5ef1b863 	addp	d3, v3.2d
    bd8c:	5ef1b842 	addp	d2, v2.2d
    bd90:	5ef1b821 	addp	d1, v1.2d
    bd94:	5ef1b800 	addp	d0, v0.2d
    bd98:	9e660073 	fmov	x19, d3
    bd9c:	9e66005a 	fmov	x26, d2
    bda0:	9e66003b 	fmov	x27, d1
    bda4:	9e66001c 	fmov	x28, d0
    bda8:	540001c0 	b.eq	bde0 <decoder_batch+0x1c0>  // b.none
    bdac:	8b0a0eca 	add	x10, x22, x10, lsl #3
    bdb0:	8b090f0b 	add	x11, x24, x9, lsl #3
    bdb4:	91000d29 	add	x9, x9, #0x3
    bdb8:	a97f356c 	ldp	x12, x13, [x11, #-16]
    bdbc:	91001129 	add	x9, x9, #0x4
    bdc0:	f842056e 	ldr	x14, [x11], #32
    bdc4:	eb02013f 	cmp	x9, x2
    bdc8:	f842054f 	ldr	x15, [x10], #32
    bdcc:	8b130193 	add	x19, x12, x19
    bdd0:	8b1c01bc 	add	x28, x13, x28
    bdd4:	8b1b01db 	add	x27, x14, x27
    bdd8:	8b1a01fa 	add	x26, x15, x26
    bddc:	54fffee3 	b.cc	bdb8 <decoder_batch+0x198>  // b.lo, b.ul, b.last
    bde0:	6b02011f 	cmp	w8, w2
    bde4:	54fff582 	b.cs	bc94 <decoder_batch+0x74>  // b.hs, b.nlast
    bde8:	2a0803e8 	mov	w8, w8
    bdec:	cb08004a 	sub	x10, x2, x8
    bdf0:	f100115f 	cmp	x10, #0x4
    bdf4:	54000283 	b.cc	be44 <decoder_batch+0x224>  // b.lo, b.ul, b.last
    bdf8:	6f00e400 	movi	v0.2d, #0x0
    bdfc:	6f00e401 	movi	v1.2d, #0x0
    be00:	92400449 	and	x9, x2, #0x3
    be04:	cb09014b 	sub	x11, x10, x9
    be08:	8b09010c 	add	x12, x8, x9
    be0c:	8b080f0a 	add	x10, x24, x8, lsl #3
    be10:	8b080168 	add	x8, x11, x8
    be14:	cb02018b 	sub	x11, x12, x2
    be18:	4e081e60 	mov	v0.d[0], x19
    be1c:	ad7f8d42 	ldp	q2, q3, [x10, #-16]
    be20:	b100116b 	adds	x11, x11, #0x4
    be24:	9100814a 	add	x10, x10, #0x20
    be28:	4ee08440 	add	v0.2d, v2.2d, v0.2d
    be2c:	4ee18461 	add	v1.2d, v3.2d, v1.2d
    be30:	54ffff61 	b.ne	be1c <decoder_batch+0x1fc>  // b.any
    be34:	4ee08420 	add	v0.2d, v1.2d, v0.2d
    be38:	5ef1b800 	addp	d0, v0.2d
    be3c:	9e660013 	fmov	x19, d0
    be40:	b4fff2a9 	cbz	x9, bc94 <decoder_batch+0x74>
    be44:	8b080ec9 	add	x9, x22, x8, lsl #3
    be48:	cb080048 	sub	x8, x2, x8
    be4c:	f840852a 	ldr	x10, [x9], #8
    be50:	f1000508 	subs	x8, x8, #0x1
    be54:	8b130153 	add	x19, x10, x19
    be58:	54ffffa1 	b.ne	be4c <decoder_batch+0x22c>  // b.any
    be5c:	17ffff8e 	b	bc94 <decoder_batch+0x74>
    be60:	8b1c0368 	add	x8, x27, x28
    be64:	8b130349 	add	x9, x26, x19
    be68:	8b090100 	add	x0, x8, x9
    be6c:	14000002 	b	be74 <decoder_batch+0x254>
    be70:	aa1f03e0 	mov	x0, xzr
    be74:	910c43ff 	add	sp, sp, #0x310
    be78:	a9454ff4 	ldp	x20, x19, [sp, #80]
    be7c:	a94457f6 	ldp	x22, x21, [sp, #64]
    be80:	a9435ff8 	ldp	x24, x23, [sp, #48]
    be84:	a94267fa 	ldp	x26, x25, [sp, #32]
    be88:	a9416ffc 	ldp	x28, x27, [sp, #16]
    be8c:	a8c67bfd 	ldp	x29, x30, [sp], #96
    be90:	d65f03c0 	ret

Disassembly of section .fini:
