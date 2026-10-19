scratch/night-apple-m1-20261019T005019Z/round-002/lookup-bench-release:
(__TEXT,__text) section
_zbtScoreLeafFindMember:
10000a9ec:	ff 43 02 d1	sub	sp, sp, #0x90
10000a9f0:	fc 6f 03 a9	stp	x28, x27, [sp, #0x30]
10000a9f4:	fa 67 04 a9	stp	x26, x25, [sp, #0x40]
10000a9f8:	f8 5f 05 a9	stp	x24, x23, [sp, #0x50]
10000a9fc:	f6 57 06 a9	stp	x22, x21, [sp, #0x60]
10000aa00:	f4 4f 07 a9	stp	x20, x19, [sp, #0x70]
10000aa04:	fd 7b 08 a9	stp	x29, x30, [sp, #0x80]
10000aa08:	fd 03 02 91	add	x29, sp, #0x80
10000aa0c:	f6 03 03 aa	mov	x22, x3
10000aa10:	e2 17 00 f9	str	x2, [sp, #0x28]
10000aa14:	e1 27 00 b9	str	w1, [sp, #0x24]
10000aa18:	f5 03 00 aa	mov	x21, x0
10000aa1c:	09 d0 40 39	ldrb	w9, [x0, #0x34]
10000aa20:	89 01 00 b4	cbz	x9, 0x10000aa50
10000aa24:	eb 03 15 aa	mov	x11, x21
10000aa28:	68 1d 41 38	ldrb	w8, [x11, #0x11]!
10000aa2c:	ea 00 80 52	mov	w10, #0x7
10000aa30:	09 29 09 1b	madd	w9, w8, w9, w10
10000aa34:	29 7d 03 53	lsr	w9, w9, #3
10000aa38:	29 25 00 11	add	w9, w9, #0x9
10000aa3c:	29 35 7f 92	and	x9, x9, #0x7ffe
10000aa40:	aa 02 09 8b	add	x10, x21, x9
10000aa44:	5a e1 00 91	add	x26, x10, #0x38
10000aa48:	c8 00 00 b5	cbnz	x8, 0x10000aa60
10000aa4c:	47 00 00 14	b	0x10000ab68
10000aa50:	eb 03 15 aa	mov	x11, x21
10000aa54:	68 1d 41 38	ldrb	w8, [x11, #0x11]!
10000aa58:	7a 9d 00 91	add	x26, x11, #0x27
10000aa5c:	68 08 00 b4	cbz	x8, 0x10000ab68
10000aa60:	eb 93 00 a9	stp	x11, x4, [sp, #0x8]
10000aa64:	e5 0f 00 f9	str	x5, [sp, #0x18]
10000aa68:	aa e2 00 91	add	x10, x21, #0x38
10000aa6c:	ea 03 00 f9	str	x10, [sp]
10000aa70:	49 01 09 8b	add	x9, x10, x9
10000aa74:	34 05 08 8b	add	x20, x9, x8, lsl #1
10000aa78:	e9 27 40 b9	ldr	w9, [sp, #0x24]
10000aa7c:	39 7d 18 53	lsr	w25, w9, #24
10000aa80:	98 02 08 8b	add	x24, x20, x8
10000aa84:	e0 03 14 aa	mov	x0, x20
10000aa88:	09 00 00 14	b	0x10000aaac
10000aa8c:	e0 03 13 aa	mov	x0, x19
10000aa90:	e1 17 40 f9	ldr	x1, [sp, #0x28]
10000aa94:	e2 03 16 aa	mov	x2, x22
10000aa98:	c4 1c 00 94	bl	0x100011da8 ; symbol stub for: _memcmp
10000aa9c:	80 07 00 34	cbz	w0, 0x10000ab8c
10000aaa0:	80 07 00 91	add	x0, x28, #0x1
10000aaa4:	1f 00 18 eb	cmp	x0, x24
10000aaa8:	02 06 00 54	b.hs	0x10000ab68
10000aaac:	02 03 00 cb	sub	x2, x24, x0
10000aab0:	e1 03 19 aa	mov	x1, x25
10000aab4:	ba 1c 00 94	bl	0x100011d9c ; symbol stub for: _memchr
10000aab8:	a0 05 00 b4	cbz	x0, 0x10000ab6c
10000aabc:	fc 03 00 aa	mov	x28, x0
10000aac0:	1b 00 14 cb	sub	x27, x0, x20
10000aac4:	48 5b 7b 78	ldrh	w8, [x26, w27, uxtw #1]
10000aac8:	b7 02 08 8b	add	x23, x21, x8
10000aacc:	e8 02 40 39	ldrb	w8, [x23]
10000aad0:	1f f9 03 71	cmp	w8, #0xfe
10000aad4:	80 03 00 54	b.eq	0x10000ab44
10000aad8:	1f fd 03 71	cmp	w8, #0xff
10000aadc:	e1 03 00 54	b.ne	0x10000ab58
10000aae0:	e8 12 40 b8	ldur	w8, [x23, #0x1]
10000aae4:	e9 27 40 b9	ldr	w9, [sp, #0x24]
10000aae8:	1f 01 09 6b	cmp	w8, w9
10000aaec:	a1 fd ff 54	b.ne	0x10000aaa0
10000aaf0:	f3 d2 40 f8	ldur	x19, [x23, #0xd]
10000aaf4:	13 02 00 b5	cbnz	x19, 0x10000ab34
10000aaf8:	40 00 00 90	adrp	x0, 8 ; 0x100012000
10000aafc:	00 68 11 91	add	x0, x0, #0x45a ; literal pool for: "src/zset_btree.c"
10000ab00:	e1 4a 80 52	mov	w1, #0x257
10000ab04:	42 00 00 90	adrp	x2, 8 ; 0x100012000
10000ab08:	42 08 18 91	add	x2, x2, #0x602 ; literal pool for: "ptr != NULL"
10000ab0c:	35 1a 00 94	bl	_standalone_panic
10000ab10:	e8 02 40 39	ldrb	w8, [x23]
10000ab14:	1f fd 03 71	cmp	w8, #0xff
10000ab18:	e0 00 00 54	b.eq	0x10000ab34
10000ab1c:	40 00 00 90	adrp	x0, 8 ; 0x100012000
10000ab20:	00 68 11 91	add	x0, x0, #0x45a ; literal pool for: "src/zset_btree.c"
10000ab24:	e1 46 80 52	mov	w1, #0x237
10000ab28:	42 00 00 90	adrp	x2, 8 ; 0x100012000
10000ab2c:	42 48 16 91	add	x2, x2, #0x592 ; literal pool for: "record[0] == ZBT_PACKED_EXTERNAL"
10000ab30:	2c 1a 00 94	bl	_standalone_panic
10000ab34:	e8 52 40 f8	ldur	x8, [x23, #0x5]
10000ab38:	1f 01 16 eb	cmp	x8, x22
10000ab3c:	21 fb ff 54	b.ne	0x10000aaa0
10000ab40:	d3 ff ff 17	b	0x10000aa8c
10000ab44:	e8 12 40 78	ldurh	w8, [x23, #0x1]
10000ab48:	f3 0e 00 91	add	x19, x23, #0x3
10000ab4c:	1f 01 16 eb	cmp	x8, x22
10000ab50:	e0 f9 ff 54	b.eq	0x10000aa8c
10000ab54:	d3 ff ff 17	b	0x10000aaa0
10000ab58:	f3 06 00 91	add	x19, x23, #0x1
10000ab5c:	1f 01 16 eb	cmp	x8, x22
10000ab60:	01 fa ff 54	b.ne	0x10000aaa0
10000ab64:	ca ff ff 17	b	0x10000aa8c
10000ab68:	00 00 80 52	mov	w0, #0x0
10000ab6c:	fd 7b 48 a9	ldp	x29, x30, [sp, #0x80]
10000ab70:	f4 4f 47 a9	ldp	x20, x19, [sp, #0x70]
10000ab74:	f6 57 46 a9	ldp	x22, x21, [sp, #0x60]
10000ab78:	f8 5f 45 a9	ldp	x24, x23, [sp, #0x50]
10000ab7c:	fa 67 44 a9	ldp	x26, x25, [sp, #0x40]
10000ab80:	fc 6f 43 a9	ldp	x28, x27, [sp, #0x30]
10000ab84:	ff 43 02 91	add	sp, sp, #0x90
10000ab88:	c0 03 5f d6	ret
10000ab8c:	a8 d6 40 39	ldrb	w8, [x21, #0x35]
10000ab90:	08 01 00 34	cbz	w8, 0x10000abb0
10000ab94:	eb bf 40 a9	ldp	x11, x15, [sp, #0x8]
10000ab98:	69 01 40 39	ldrb	w9, [x11]
10000ab9c:	ea 03 3b 2a	mvn	w10, w27
10000aba0:	3b 01 0a 0b	add	w27, w9, w10
10000aba4:	ee 0f 40 f9	ldr	x14, [sp, #0x18]
10000aba8:	af 00 00 b5	cbnz	x15, 0x10000abbc
10000abac:	2d 00 00 14	b	0x10000ac60
10000abb0:	ef 3b 41 a9	ldp	x15, x14, [sp, #0x10]
10000abb4:	eb 07 40 f9	ldr	x11, [sp, #0x8]
10000abb8:	4f 05 00 b4	cbz	x15, 0x10000ac60
10000abbc:	a9 d2 40 39	ldrb	w9, [x21, #0x34]
10000abc0:	e9 03 00 34	cbz	w9, 0x10000ac3c
10000abc4:	ea 03 1b aa	mov	x10, x27
10000abc8:	88 00 00 34	cbz	w8, 0x10000abd8
10000abcc:	6a 01 40 39	ldrb	w10, [x11]
10000abd0:	eb 03 3b 2a	mvn	w11, w27
10000abd4:	4a 01 0b 0b	add	w10, w10, w11
10000abd8:	2c 7d aa 9b	umull	x12, w9, w10
10000abdc:	8b fd 43 d3	lsr	x11, x12, #3
10000abe0:	ea 03 40 f9	ldr	x10, [sp]
10000abe4:	4a 69 6b f8	ldr	x10, [x10, x11]
10000abe8:	8d 09 40 92	and	x13, x12, #0x7
10000abec:	4a 25 cd 9a	lsr	x10, x10, x13
10000abf0:	8c 09 00 72	ands	w12, w12, #0x7
10000abf4:	40 01 00 54	b.eq	0x10000ac1c
10000abf8:	0d 08 80 52	mov	w13, #0x40
10000abfc:	ac 01 0c 4b	sub	w12, w13, w12
10000ac00:	9f 01 09 6b	cmp	w12, w9
10000ac04:	c2 00 00 54	b.hs	0x10000ac1c
10000ac08:	ed 03 40 f9	ldr	x13, [sp]
10000ac0c:	6b 01 0d 8b	add	x11, x11, x13
10000ac10:	6b 21 40 39	ldrb	w11, [x11, #0x8]
10000ac14:	6b 21 cc 9a	lsl	x11, x11, x12
10000ac18:	6a 01 0a aa	orr	x10, x11, x10
10000ac1c:	0b 00 80 92	mov	x11, #-0x1
10000ac20:	6c 21 c9 9a	lsl	x12, x11, x9
10000ac24:	3f 01 01 71	cmp	w9, #0x40
10000ac28:	69 21 8c da	csinv	x9, x11, x12, hs
10000ac2c:	49 01 09 8a	and	x9, x10, x9
10000ac30:	aa 4e 40 39	ldrb	w10, [x21, #0x13]
10000ac34:	29 21 ca 9a	lsl	x9, x9, x10
10000ac38:	02 00 00 14	b	0x10000ac40
10000ac3c:	09 00 80 d2	mov	x9, #0x0
10000ac40:	aa 16 40 f9	ldr	x10, [x21, #0x28]
10000ac44:	1f 01 00 71	cmp	w8, #0x0
10000ac48:	28 05 89 da	cneg	x8, x9, ne
10000ac4c:	48 01 08 8b	add	x8, x10, x8
10000ac50:	09 f9 40 92	and	x9, x8, #0x7fffffffffffffff
10000ac54:	1f 01 00 f1	cmp	x8, #0x0
10000ac58:	28 b1 88 da	csinv	x8, x9, x8, lt
10000ac5c:	e8 01 00 f9	str	x8, [x15]
10000ac60:	4e 00 00 b4	cbz	x14, 0x10000ac68
10000ac64:	db 01 00 b9	str	w27, [x14]
10000ac68:	20 00 80 52	mov	w0, #0x1
10000ac6c:	c0 ff ff 17	b	0x10000ab6c
