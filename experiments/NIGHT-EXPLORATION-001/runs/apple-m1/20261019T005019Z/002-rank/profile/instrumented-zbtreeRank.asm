
scratch/night-apple-m1-20261019T005019Z/round-001/rank-diagnostic/rank-profile-bench:	file format mach-o arm64

Disassembly of section __TEXT,__text:

000000010000497c <_zbtreeRank>:
10000497c: d10303ff    	sub	sp, sp, #0xc0
100004980: a9066ffc    	stp	x28, x27, [sp, #0x60]
100004984: a90767fa    	stp	x26, x25, [sp, #0x70]
100004988: a9085ff8    	stp	x24, x23, [sp, #0x80]
10000498c: a90957f6    	stp	x22, x21, [sp, #0x90]
100004990: a90a4ff4    	stp	x20, x19, [sp, #0xa0]
100004994: a90b7bfd    	stp	x29, x30, [sp, #0xb0]
100004998: 9102c3fd    	add	x29, sp, #0xb0
10000499c: f90023e3    	str	x3, [sp, #0x40]
1000049a0: aa0203f4    	mov	x20, x2
1000049a4: aa0103f5    	mov	x21, x1
1000049a8: aa0003f3    	mov	x19, x0
1000049ac: d2800001    	mov	x1, #0x0                ; =0
1000049b0: 385ff2a9    	ldurb	w9, [x21, #-0x1]
1000049b4: 12000928    	and	w8, w9, #0x7
1000049b8: 7100051f    	cmp	w8, #0x1
1000049bc: 5400012d    	b.le	0x1000049e0 <_zbtreeRank+0x64>
1000049c0: 7100091f    	cmp	w8, #0x2
1000049c4: 54000180    	b.eq	0x1000049f4 <_zbtreeRank+0x78>
1000049c8: 71000d1f    	cmp	w8, #0x3
1000049cc: 54000180    	b.eq	0x1000049fc <_zbtreeRank+0x80>
1000049d0: 7100111f    	cmp	w8, #0x4
1000049d4: 540001a1    	b.ne	0x100004a08 <_zbtreeRank+0x8c>
1000049d8: f85ef2a1    	ldur	x1, [x21, #-0x11]
1000049dc: 1400000b    	b	0x100004a08 <_zbtreeRank+0x8c>
1000049e0: 34000128    	cbz	w8, 0x100004a04 <_zbtreeRank+0x88>
1000049e4: 7100051f    	cmp	w8, #0x1
1000049e8: 54000101    	b.ne	0x100004a08 <_zbtreeRank+0x8c>
1000049ec: 385fd2a1    	ldurb	w1, [x21, #-0x3]
1000049f0: 14000006    	b	0x100004a08 <_zbtreeRank+0x8c>
1000049f4: 785fb2a1    	ldurh	w1, [x21, #-0x5]
1000049f8: 14000004    	b	0x100004a08 <_zbtreeRank+0x8c>
1000049fc: b85f72a1    	ldur	w1, [x21, #-0x9]
100004a00: 14000002    	b	0x100004a08 <_zbtreeRank+0x8c>
100004a04: d343fd21    	lsr	x1, x9, #3
100004a08: aa1503e0    	mov	x0, x21
100004a0c: 940033b3    	bl	0x1000118d8 <_dictGenHashFunction>
100004a10: a904ffe0    	stp	x0, xzr, [sp, #0x48]
100004a14: 385ff2a9    	ldurb	w9, [x21, #-0x1]
100004a18: 12000928    	and	w8, w9, #0x7
100004a1c: 7100051f    	cmp	w8, #0x1
100004a20: b9000ff4    	str	w20, [sp, #0xc]
100004a24: 5400012d    	b.le	0x100004a48 <_zbtreeRank+0xcc>
100004a28: 7100091f    	cmp	w8, #0x2
100004a2c: 54000180    	b.eq	0x100004a5c <_zbtreeRank+0xe0>
100004a30: 71000d1f    	cmp	w8, #0x3
100004a34: 54000180    	b.eq	0x100004a64 <_zbtreeRank+0xe8>
100004a38: 7100111f    	cmp	w8, #0x4
100004a3c: 540001c1    	b.ne	0x100004a74 <_zbtreeRank+0xf8>
100004a40: f85ef2a8    	ldur	x8, [x21, #-0x11]
100004a44: 1400000b    	b	0x100004a70 <_zbtreeRank+0xf4>
100004a48: 34000128    	cbz	w8, 0x100004a6c <_zbtreeRank+0xf0>
100004a4c: 7100051f    	cmp	w8, #0x1
100004a50: 54000121    	b.ne	0x100004a74 <_zbtreeRank+0xf8>
100004a54: 385fd2a8    	ldurb	w8, [x21, #-0x3]
100004a58: 14000006    	b	0x100004a70 <_zbtreeRank+0xf4>
100004a5c: 785fb2a8    	ldurh	w8, [x21, #-0x5]
100004a60: 14000004    	b	0x100004a70 <_zbtreeRank+0xf4>
100004a64: b85f72a8    	ldur	w8, [x21, #-0x9]
100004a68: 14000002    	b	0x100004a70 <_zbtreeRank+0xf4>
100004a6c: d343fd28    	lsr	x8, x9, #3
100004a70: f9002be8    	str	x8, [sp, #0x50]
100004a74: f9001ff5    	str	x21, [sp, #0x38]
100004a78: f9402268    	ldr	x8, [x19, #0x40]
100004a7c: b4001488    	cbz	x8, 0x100004d0c <_zbtreeRank+0x390>
100004a80: aa1303e0    	mov	x0, x19
100004a84: 52800021    	mov	w1, #0x1                ; =1
100004a88: 9400091c    	bl	0x100006ef8 <_zbtIndexRehashStep>
100004a8c: f9402274    	ldr	x20, [x19, #0x40]
100004a90: b40013f4    	cbz	x20, 0x100004d0c <_zbtreeRank+0x390>
100004a94: f9400688    	ldr	x8, [x20, #0x8]
100004a98: b40013a8    	cbz	x8, 0x100004d0c <_zbtreeRank+0x390>
100004a9c: d280001b    	mov	x27, #0x0               ; =0
100004aa0: f94027eb    	ldr	x11, [sp, #0x48]
100004aa4: 53187d69    	lsr	w9, w11, #24
100004aa8: d358fd6a    	lsr	x10, x11, #24
100004aac: 7100013f    	cmp	w9, #0x0
100004ab0: 1a9f1549    	csinc	w9, w10, wzr, ne
100004ab4: d1000508    	sub	x8, x8, #0x1
100004ab8: 2a0b03ea    	mov	w10, w11
100004abc: a90223ea    	stp	x10, x8, [sp, #0x20]
100004ac0: 8a0a011c    	and	x28, x8, x10
100004ac4: 92401d28    	and	x8, x9, #0xff
100004ac8: b200c3ea    	mov	x10, #0x101010101010101 ; =72340172838076673
100004acc: 9b0a7d0a    	mul	x10, x8, x10
100004ad0: f9001bea    	str	x10, [sp, #0x30]
100004ad4: 91006275    	add	x21, x19, #0x18
100004ad8: d28f82aa    	mov	x10, #0x7c15            ; =31765
100004adc: f2afe94a    	movk	x10, #0x7f4a, lsl #16
100004ae0: f2cf372a    	movk	x10, #0x79b9, lsl #32
100004ae4: f2f3c6ea    	movk	x10, #0x9e37, lsl #48
100004ae8: 9b0a7d08    	mul	x8, x8, x10
100004aec: 5280002a    	mov	w10, #0x1               ; =1
100004af0: 9ac9214b    	lsl	x11, x10, x9
100004af4: d37afd0c    	lsr	x12, x8, #58
100004af8: 9acc214c    	lsl	x12, x10, x12
100004afc: aa0b018b    	orr	x11, x12, x11
100004b00: d364fd08    	lsr	x8, x8, #36
100004b04: 9ac82148    	lsl	x8, x10, x8
100004b08: aa080168    	orr	x8, x11, x8
100004b0c: f9000fe8    	str	x8, [sp, #0x18]
100004b10: 12001d38    	and	w24, w9, #0xff
100004b14: f9400288    	ldr	x8, [x20]
100004b18: b9402289    	ldr	w9, [x20, #0x20]
100004b1c: 7100013f    	cmp	w9, #0x0
100004b20: 52800609    	mov	w9, #0x30               ; =48
100004b24: 5280040a    	mov	w10, #0x20              ; =32
100004b28: 9a890149    	csel	x9, x10, x9, eq
100004b2c: 9b1c2136    	madd	x22, x9, x28, x8
100004b30: f94002c8    	ldr	x8, [x22]
100004b34: f9401be9    	ldr	x9, [sp, #0x30]
100004b38: ca090108    	eor	x8, x8, x9
100004b3c: b207dbe9    	mov	x9, #-0x101010101010102 ; =-72340172838076674
100004b40: f29fdfe9    	movk	x9, #0xfeff
100004b44: 8b090109    	add	x9, x8, x9
100004b48: 8a280128    	bic	x8, x9, x8
100004b4c: f201c11a    	ands	x26, x8, #0x8080808080808080
100004b50: 540008c0    	b.eq	0x100004c68 <_zbtreeRank+0x2ec>
100004b54: 910042d7    	add	x23, x22, #0x10
100004b58: 1400000a    	b	0x100004b80 <_zbtreeRank+0x204>
100004b5c: d0000060    	adrp	x0, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004b60: 91279800    	add	x0, x0, #0x9e6
100004b64: 5280f421    	mov	w1, #0x7a1              ; =1953
100004b68: d0000062    	adrp	x2, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004b6c: 912d7842    	add	x2, x2, #0xb5e
100004b70: 940032ef    	bl	0x10001172c <_standalone_panic>
100004b74: d1000748    	sub	x8, x26, #0x1
100004b78: ea1a011a    	ands	x26, x8, x26
100004b7c: 54000760    	b.eq	0x100004c68 <_zbtreeRank+0x2ec>
100004b80: dac00348    	rbit	x8, x26
100004b84: dac01108    	clz	x8, x8
100004b88: f94002c9    	ldr	x9, [x22]
100004b8c: 927d090a    	and	x10, x8, #0x38
100004b90: 9aca2529    	lsr	x9, x9, x10
100004b94: 6b29031f    	cmp	w24, w9, uxtb
100004b98: 54fffee1    	b.ne	0x100004b74 <_zbtreeRank+0x1f8>
100004b9c: d343fd08    	lsr	x8, x8, #3
100004ba0: b9402289    	ldr	w9, [x20, #0x20]
100004ba4: 340000a9    	cbz	w9, 0x100004bb8 <_zbtreeRank+0x23c>
100004ba8: b8687ae8    	ldr	w8, [x23, x8, lsl #2]
100004bac: 3100051f    	cmn	w8, #0x1
100004bb0: 540000c1    	b.ne	0x100004bc8 <_zbtreeRank+0x24c>
100004bb4: 17fffff0    	b	0x100004b74 <_zbtreeRank+0x1f8>
100004bb8: 78687ae8    	ldrh	w8, [x23, x8, lsl #1]
100004bbc: 529fffe9    	mov	w9, #0xffff             ; =65535
100004bc0: 6b09011f    	cmp	w8, w9
100004bc4: 54fffd80    	b.eq	0x100004b74 <_zbtreeRank+0x1f8>
100004bc8: b9405669    	ldr	w9, [x19, #0x54]
100004bcc: 6b09011f    	cmp	w8, w9
100004bd0: 540000e2    	b.hs	0x100004bec <_zbtreeRank+0x270>
100004bd4: f9402669    	ldr	x9, [x19, #0x48]
100004bd8: f8685939    	ldr	x25, [x9, w8, uxtw #3]
100004bdc: 92400329    	and	x9, x25, #0x1
100004be0: f100033f    	cmp	x25, #0x0
100004be4: fa401920    	ccmp	x9, #0x0, #0x0, ne
100004be8: 540000c0    	b.eq	0x100004c00 <_zbtreeRank+0x284>
100004bec: f9402268    	ldr	x8, [x19, #0x40]
100004bf0: b4fffb68    	cbz	x8, 0x100004b5c <_zbtreeRank+0x1e0>
100004bf4: eb1402bf    	cmp	x21, x20
100004bf8: 54fffbe0    	b.eq	0x100004b74 <_zbtreeRank+0x1f8>
100004bfc: 17ffffd8    	b	0x100004b5c <_zbtreeRank+0x1e0>
100004c00: b9403329    	ldr	w9, [x25, #0x30]
100004c04: 6b08013f    	cmp	w9, w8
100004c08: 540000e0    	b.eq	0x100004c24 <_zbtreeRank+0x2a8>
100004c0c: d0000060    	adrp	x0, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004c10: 91279800    	add	x0, x0, #0x9e6
100004c14: 5280f4a1    	mov	w1, #0x7a5              ; =1957
100004c18: d0000062    	adrp	x2, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004c1c: 912cfc42    	add	x2, x2, #0xb3f
100004c20: 940032c3    	bl	0x10001172c <_standalone_panic>
100004c24: f9402268    	ldr	x8, [x19, #0x40]
100004c28: b4000128    	cbz	x8, 0x100004c4c <_zbtreeRank+0x2d0>
100004c2c: eb14011f    	cmp	x8, x20
100004c30: 1a9f17e9    	cset	w9, eq
100004c34: 79402f2a    	ldrh	w10, [x25, #0x16]
100004c38: 79405908    	ldrh	w8, [x8, #0x2c]
100004c3c: 6b08015f    	cmp	w10, w8
100004c40: 1a9f07e8    	cset	w8, ne
100004c44: 6b08013f    	cmp	w9, w8
100004c48: 54fff960    	b.eq	0x100004b74 <_zbtreeRank+0x1f8>
100004c4c: d10153a5    	sub	x5, x29, #0x54
100004c50: aa1903e0    	mov	x0, x25
100004c54: a9448fe1    	ldp	x1, x3, [sp, #0x48]
100004c58: a94393e2    	ldp	x2, x4, [sp, #0x38]
100004c5c: 94001837    	bl	0x10000ad38 <_zbtScoreLeafFindMember>
100004c60: 34fff8a0    	cbz	w0, 0x100004b74 <_zbtreeRank+0x1f8>
100004c64: 140000d1    	b	0x100004fa8 <_zbtreeRank+0x62c>
100004c68: b500021b    	cbnz	x27, 0x100004ca8 <_zbtreeRank+0x32c>
100004c6c: b9400a88    	ldr	w8, [x20, #0x8]
100004c70: 51000508    	sub	w8, w8, #0x1
100004c74: f94013e9    	ldr	x9, [sp, #0x20]
100004c78: 8a090108    	and	x8, x8, x9
100004c7c: f9400289    	ldr	x9, [x20]
100004c80: b940228a    	ldr	w10, [x20, #0x20]
100004c84: 7100015f    	cmp	w10, #0x0
100004c88: 5280060a    	mov	w10, #0x30              ; =48
100004c8c: 5280040b    	mov	w11, #0x20              ; =32
100004c90: 9a8a016a    	csel	x10, x11, x10, eq
100004c94: 9ba82548    	umaddl	x8, w10, w8, x9
100004c98: f9400508    	ldr	x8, [x8, #0x8]
100004c9c: f9400fe9    	ldr	x9, [sp, #0x18]
100004ca0: ea28013f    	bics	xzr, x9, x8
100004ca4: 54000341    	b.ne	0x100004d0c <_zbtreeRank+0x390>
100004ca8: f94002c8    	ldr	x8, [x22]
100004cac: 92401d09    	and	x9, x8, #0xff
100004cb0: 92781d0a    	and	x10, x8, #0xff00
100004cb4: 92701d0b    	and	x11, x8, #0xff0000
100004cb8: 92681d0c    	and	x12, x8, #0xff000000
100004cbc: 92601d0d    	and	x13, x8, #0xff00000000
100004cc0: 92581d0e    	and	x14, x8, #0xff0000000000
100004cc4: 92501d0f    	and	x15, x8, #0xff000000000000
100004cc8: f100013f    	cmp	x9, #0x0
100004ccc: fa401944    	ccmp	x10, #0x0, #0x4, ne
100004cd0: fa401964    	ccmp	x11, #0x0, #0x4, ne
100004cd4: fa401984    	ccmp	x12, #0x0, #0x4, ne
100004cd8: fa4019a4    	ccmp	x13, #0x0, #0x4, ne
100004cdc: fa4019c4    	ccmp	x14, #0x0, #0x4, ne
100004ce0: fa4019e4    	ccmp	x15, #0x0, #0x4, ne
100004ce4: d378fd08    	lsr	x8, x8, #56
100004ce8: fa401904    	ccmp	x8, #0x0, #0x4, ne
100004cec: 54000100    	b.eq	0x100004d0c <_zbtreeRank+0x390>
100004cf0: 91000788    	add	x8, x28, #0x1
100004cf4: f94017e9    	ldr	x9, [sp, #0x28]
100004cf8: 8a09011c    	and	x28, x8, x9
100004cfc: 9100077b    	add	x27, x27, #0x1
100004d00: f9400688    	ldr	x8, [x20, #0x8]
100004d04: eb08037f    	cmp	x27, x8
100004d08: 54fff063    	b.lo	0x100004b14 <_zbtreeRank+0x198>
100004d0c: f9401268    	ldr	x8, [x19, #0x20]
100004d10: b40013a8    	cbz	x8, 0x100004f84 <_zbtreeRank+0x608>
100004d14: d2800014    	mov	x20, #0x0               ; =0
100004d18: 91006269    	add	x9, x19, #0x18
100004d1c: f90017e9    	str	x9, [sp, #0x28]
100004d20: f94027eb    	ldr	x11, [sp, #0x48]
100004d24: 53187d69    	lsr	w9, w11, #24
100004d28: d358fd6a    	lsr	x10, x11, #24
100004d2c: 7100013f    	cmp	w9, #0x0
100004d30: 1a9f1549    	csinc	w9, w10, wzr, ne
100004d34: d1000508    	sub	x8, x8, #0x1
100004d38: 2a0b03ea    	mov	w10, w11
100004d3c: a901a3ea    	stp	x10, x8, [sp, #0x18]
100004d40: 8a0a0118    	and	x24, x8, x10
100004d44: 92401d28    	and	x8, x9, #0xff
100004d48: b200c3ea    	mov	x10, #0x101010101010101 ; =72340172838076673
100004d4c: 9b0a7d0a    	mul	x10, x8, x10
100004d50: f9001bea    	str	x10, [sp, #0x30]
100004d54: d28f82aa    	mov	x10, #0x7c15            ; =31765
100004d58: f2afe94a    	movk	x10, #0x7f4a, lsl #16
100004d5c: f2cf372a    	movk	x10, #0x79b9, lsl #32
100004d60: f2f3c6ea    	movk	x10, #0x9e37, lsl #48
100004d64: 9b0a7d08    	mul	x8, x8, x10
100004d68: 5280002a    	mov	w10, #0x1               ; =1
100004d6c: 9ac9214b    	lsl	x11, x10, x9
100004d70: d37afd0c    	lsr	x12, x8, #58
100004d74: 9acc214c    	lsl	x12, x10, x12
100004d78: aa0b018b    	orr	x11, x12, x11
100004d7c: d364fd08    	lsr	x8, x8, #36
100004d80: 9ac82148    	lsl	x8, x10, x8
100004d84: aa080168    	orr	x8, x11, x8
100004d88: f9000be8    	str	x8, [sp, #0x10]
100004d8c: 12001d36    	and	w22, w9, #0xff
100004d90: 529ffffb    	mov	w27, #0xffff            ; =65535
100004d94: d000007a    	adrp	x26, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004d98: 91279b5a    	add	x26, x26, #0x9e6
100004d9c: f9400e68    	ldr	x8, [x19, #0x18]
100004da0: b9403a69    	ldr	w9, [x19, #0x38]
100004da4: 7100013f    	cmp	w9, #0x0
100004da8: 52800609    	mov	w9, #0x30               ; =48
100004dac: 5280040a    	mov	w10, #0x20              ; =32
100004db0: 9a890149    	csel	x9, x10, x9, eq
100004db4: 9b18213c    	madd	x28, x9, x24, x8
100004db8: f9400388    	ldr	x8, [x28]
100004dbc: f9401be9    	ldr	x9, [sp, #0x30]
100004dc0: ca090108    	eor	x8, x8, x9
100004dc4: b207dbe9    	mov	x9, #-0x101010101010102 ; =-72340172838076674
100004dc8: f29fdfe9    	movk	x9, #0xfeff
100004dcc: 8b090109    	add	x9, x8, x9
100004dd0: 8a280128    	bic	x8, x9, x8
100004dd4: f201c115    	ands	x21, x8, #0x8080808080808080
100004dd8: 54000840    	b.eq	0x100004ee0 <_zbtreeRank+0x564>
100004ddc: 91004397    	add	x23, x28, #0x10
100004de0: 14000006    	b	0x100004df8 <_zbtreeRank+0x47c>
100004de4: f9402268    	ldr	x8, [x19, #0x40]
100004de8: b4000708    	cbz	x8, 0x100004ec8 <_zbtreeRank+0x54c>
100004dec: d10006a8    	sub	x8, x21, #0x1
100004df0: ea150115    	ands	x21, x8, x21
100004df4: 54000760    	b.eq	0x100004ee0 <_zbtreeRank+0x564>
100004df8: dac002a8    	rbit	x8, x21
100004dfc: dac01108    	clz	x8, x8
100004e00: f9400389    	ldr	x9, [x28]
100004e04: 927d090a    	and	x10, x8, #0x38
100004e08: 9aca2529    	lsr	x9, x9, x10
100004e0c: 6b2902df    	cmp	w22, w9, uxtb
100004e10: 54fffee1    	b.ne	0x100004dec <_zbtreeRank+0x470>
100004e14: d343fd08    	lsr	x8, x8, #3
100004e18: b9403a69    	ldr	w9, [x19, #0x38]
100004e1c: 340000a9    	cbz	w9, 0x100004e30 <_zbtreeRank+0x4b4>
100004e20: b8687ae8    	ldr	w8, [x23, x8, lsl #2]
100004e24: 3100051f    	cmn	w8, #0x1
100004e28: 540000a1    	b.ne	0x100004e3c <_zbtreeRank+0x4c0>
100004e2c: 17fffff0    	b	0x100004dec <_zbtreeRank+0x470>
100004e30: 78687ae8    	ldrh	w8, [x23, x8, lsl #1]
100004e34: 6b1b011f    	cmp	w8, w27
100004e38: 54fffda0    	b.eq	0x100004dec <_zbtreeRank+0x470>
100004e3c: b9405669    	ldr	w9, [x19, #0x54]
100004e40: 6b09011f    	cmp	w8, w9
100004e44: 54fffd02    	b.hs	0x100004de4 <_zbtreeRank+0x468>
100004e48: f9402669    	ldr	x9, [x19, #0x48]
100004e4c: f8685939    	ldr	x25, [x9, w8, uxtw #3]
100004e50: 92400329    	and	x9, x25, #0x1
100004e54: f100033f    	cmp	x25, #0x0
100004e58: fa401920    	ccmp	x9, #0x0, #0x0, ne
100004e5c: 54fffc41    	b.ne	0x100004de4 <_zbtreeRank+0x468>
100004e60: b9403329    	ldr	w9, [x25, #0x30]
100004e64: 6b08013f    	cmp	w9, w8
100004e68: 540000c0    	b.eq	0x100004e80 <_zbtreeRank+0x504>
100004e6c: aa1a03e0    	mov	x0, x26
100004e70: 5280f4a1    	mov	w1, #0x7a5              ; =1957
100004e74: d0000062    	adrp	x2, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004e78: 912cfc42    	add	x2, x2, #0xb3f
100004e7c: 9400322c    	bl	0x10001172c <_standalone_panic>
100004e80: f9402268    	ldr	x8, [x19, #0x40]
100004e84: b4000148    	cbz	x8, 0x100004eac <_zbtreeRank+0x530>
100004e88: f94017e9    	ldr	x9, [sp, #0x28]
100004e8c: eb09011f    	cmp	x8, x9
100004e90: 1a9f17e9    	cset	w9, eq
100004e94: 79402f2a    	ldrh	w10, [x25, #0x16]
100004e98: 79405908    	ldrh	w8, [x8, #0x2c]
100004e9c: 6b08015f    	cmp	w10, w8
100004ea0: 1a9f07e8    	cset	w8, ne
100004ea4: 6b08013f    	cmp	w9, w8
100004ea8: 54fffa20    	b.eq	0x100004dec <_zbtreeRank+0x470>
100004eac: d10153a5    	sub	x5, x29, #0x54
100004eb0: aa1903e0    	mov	x0, x25
100004eb4: a9448fe1    	ldp	x1, x3, [sp, #0x48]
100004eb8: a94393e2    	ldp	x2, x4, [sp, #0x38]
100004ebc: 9400179f    	bl	0x10000ad38 <_zbtScoreLeafFindMember>
100004ec0: 34fff960    	cbz	w0, 0x100004dec <_zbtreeRank+0x470>
100004ec4: 14000039    	b	0x100004fa8 <_zbtreeRank+0x62c>
100004ec8: aa1a03e0    	mov	x0, x26
100004ecc: 5280f421    	mov	w1, #0x7a1              ; =1953
100004ed0: d0000062    	adrp	x2, 0x100012000 <_sdsnewlen.cold.1+0x3c>
100004ed4: 912d7842    	add	x2, x2, #0xb5e
100004ed8: 94003215    	bl	0x10001172c <_standalone_panic>
100004edc: 17ffffc4    	b	0x100004dec <_zbtreeRank+0x470>
100004ee0: b5000214    	cbnz	x20, 0x100004f20 <_zbtreeRank+0x5a4>
100004ee4: b9402268    	ldr	w8, [x19, #0x20]
100004ee8: 51000508    	sub	w8, w8, #0x1
100004eec: f9400fe9    	ldr	x9, [sp, #0x18]
100004ef0: 8a090108    	and	x8, x8, x9
100004ef4: f9400e69    	ldr	x9, [x19, #0x18]
100004ef8: b9403a6a    	ldr	w10, [x19, #0x38]
100004efc: 7100015f    	cmp	w10, #0x0
100004f00: 5280060a    	mov	w10, #0x30              ; =48
100004f04: 5280040b    	mov	w11, #0x20              ; =32
100004f08: 9a8a016a    	csel	x10, x11, x10, eq
100004f0c: 9ba82548    	umaddl	x8, w10, w8, x9
100004f10: f9400508    	ldr	x8, [x8, #0x8]
100004f14: f9400be9    	ldr	x9, [sp, #0x10]
100004f18: ea28013f    	bics	xzr, x9, x8
100004f1c: 54000341    	b.ne	0x100004f84 <_zbtreeRank+0x608>
100004f20: f9400388    	ldr	x8, [x28]
100004f24: 92401d09    	and	x9, x8, #0xff
100004f28: 92781d0a    	and	x10, x8, #0xff00
100004f2c: 92701d0b    	and	x11, x8, #0xff0000
100004f30: 92681d0c    	and	x12, x8, #0xff000000
100004f34: 92601d0d    	and	x13, x8, #0xff00000000
100004f38: 92581d0e    	and	x14, x8, #0xff0000000000
100004f3c: 92501d0f    	and	x15, x8, #0xff000000000000
100004f40: f100013f    	cmp	x9, #0x0
100004f44: fa401944    	ccmp	x10, #0x0, #0x4, ne
100004f48: fa401964    	ccmp	x11, #0x0, #0x4, ne
100004f4c: fa401984    	ccmp	x12, #0x0, #0x4, ne
100004f50: fa4019a4    	ccmp	x13, #0x0, #0x4, ne
100004f54: fa4019c4    	ccmp	x14, #0x0, #0x4, ne
100004f58: fa4019e4    	ccmp	x15, #0x0, #0x4, ne
100004f5c: d378fd08    	lsr	x8, x8, #56
100004f60: fa401904    	ccmp	x8, #0x0, #0x4, ne
100004f64: 54000100    	b.eq	0x100004f84 <_zbtreeRank+0x608>
100004f68: 91000708    	add	x8, x24, #0x1
100004f6c: f94013e9    	ldr	x9, [sp, #0x20]
100004f70: 8a090118    	and	x24, x8, x9
100004f74: 91000694    	add	x20, x20, #0x1
100004f78: f9401268    	ldr	x8, [x19, #0x20]
100004f7c: eb08029f    	cmp	x20, x8
100004f80: 54fff0e3    	b.lo	0x100004d9c <_zbtreeRank+0x420>
100004f84: 92800000    	mov	x0, #-0x1               ; =-1
100004f88: a94b7bfd    	ldp	x29, x30, [sp, #0xb0]
100004f8c: a94a4ff4    	ldp	x20, x19, [sp, #0xa0]
100004f90: a94957f6    	ldp	x22, x21, [sp, #0x90]
100004f94: a9485ff8    	ldp	x24, x23, [sp, #0x80]
100004f98: a94767fa    	ldp	x26, x25, [sp, #0x70]
100004f9c: a9466ffc    	ldp	x28, x27, [sp, #0x60]
100004fa0: 910303ff    	add	sp, sp, #0xc0
100004fa4: d65f03c0    	ret
100004fa8: b85ac3a0    	ldur	w0, [x29, #-0x54]
100004fac: f9400329    	ldr	x9, [x25]
100004fb0: b4000589    	cbz	x9, 0x100005060 <_zbtreeRank+0x6e4>
100004fb4: b9400fec    	ldr	w12, [sp, #0xc]
100004fb8: 14000003    	b	0x100004fc4 <_zbtreeRank+0x648>
100004fbc: f9400329    	ldr	x9, [x25]
100004fc0: b4000529    	cbz	x9, 0x100005064 <_zbtreeRank+0x6e8>
100004fc4: 39404328    	ldrb	w8, [x25, #0x10]
100004fc8: aa0903f9    	mov	x25, x9
100004fcc: 34ffff88    	cbz	w8, 0x100004fbc <_zbtreeRank+0x640>
100004fd0: 7100211f    	cmp	w8, #0x8
100004fd4: 54000062    	b.hs	0x100004fe0 <_zbtreeRank+0x664>
100004fd8: d2800009    	mov	x9, #0x0                ; =0
100004fdc: 14000019    	b	0x100005040 <_zbtreeRank+0x6c4>
100004fe0: 927d1109    	and	x9, x8, #0xf8
100004fe4: 6f00e400    	movi.2d	v0, #0000000000000000
100004fe8: 6f00e401    	movi.2d	v1, #0000000000000000
100004fec: 4e081c01    	mov.d	v1[0], x0
100004ff0: 9105232a    	add	x10, x25, #0x148
100004ff4: aa0903eb    	mov	x11, x9
100004ff8: 6f00e402    	movi.2d	v2, #0000000000000000
100004ffc: 6f00e403    	movi.2d	v3, #0000000000000000
100005000: ad7e9544    	ldp	q4, q5, [x10, #-0x30]
100005004: ad7f9d46    	ldp	q6, q7, [x10, #-0x10]
100005008: 4ee18481    	add.2d	v1, v4, v1
10000500c: 4ee084a0    	add.2d	v0, v5, v0
100005010: 4ee284c2    	add.2d	v2, v6, v2
100005014: 4ee384e3    	add.2d	v3, v7, v3
100005018: 9101014a    	add	x10, x10, #0x40
10000501c: f100216b    	subs	x11, x11, #0x8
100005020: 54ffff01    	b.ne	0x100005000 <_zbtreeRank+0x684>
100005024: 4ee18400    	add.2d	v0, v0, v1
100005028: 4ee08440    	add.2d	v0, v2, v0
10000502c: 4ee08460    	add.2d	v0, v3, v0
100005030: 5ef1b800    	addp.2d	d0, v0
100005034: 9e660000    	fmov	x0, d0
100005038: eb08013f    	cmp	x9, x8
10000503c: 54fffc00    	b.eq	0x100004fbc <_zbtreeRank+0x640>
100005040: cb090108    	sub	x8, x8, x9
100005044: 8b090f29    	add	x9, x25, x9, lsl #3
100005048: 91046129    	add	x9, x9, #0x118
10000504c: f840852a    	ldr	x10, [x9], #0x8
100005050: 8b000140    	add	x0, x10, x0
100005054: f1000508    	subs	x8, x8, #0x1
100005058: 54ffffa1    	b.ne	0x10000504c <_zbtreeRank+0x6d0>
10000505c: 17ffffd8    	b	0x100004fbc <_zbtreeRank+0x640>
100005060: b9400fec    	ldr	w12, [sp, #0xc]
100005064: 34fff92c    	cbz	w12, 0x100004f88 <_zbtreeRank+0x60c>
100005068: f9403268    	ldr	x8, [x19, #0x60]
10000506c: aa2003e9    	mvn	x9, x0
100005070: 8b090100    	add	x0, x8, x9
100005074: 17ffffc5    	b	0x100004f88 <_zbtreeRank+0x60c>
