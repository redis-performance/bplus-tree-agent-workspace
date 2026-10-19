
scratch/night-apple-m1-20261019T005019Z/round-001/rank-diagnostic/timing:	file format mach-o arm64

Disassembly of section __TEXT,__text:

0000000100008f98 <_main>:
100008f98: d104c3ff    	sub	sp, sp, #0x130
100008f9c: 6d0c23e9    	stp	d9, d8, [sp, #0xc0]
100008fa0: a90d6ffc    	stp	x28, x27, [sp, #0xd0]
100008fa4: a90e67fa    	stp	x26, x25, [sp, #0xe0]
100008fa8: a90f5ff8    	stp	x24, x23, [sp, #0xf0]
100008fac: a91057f6    	stp	x22, x21, [sp, #0x100]
100008fb0: a9114ff4    	stp	x20, x19, [sp, #0x110]
100008fb4: a9127bfd    	stp	x29, x30, [sp, #0x120]
100008fb8: 910483fd    	add	x29, sp, #0x120
100008fbc: aa0103f4    	mov	x20, x1
100008fc0: 90000068    	adrp	x8, 0x100014000 <_strtoull+0x100014000>
100008fc4: f9400d08    	ldr	x8, [x8, #0x18]
100008fc8: f9400108    	ldr	x8, [x8]
100008fcc: f81903a8    	stur	x8, [x29, #-0x70]
100008fd0: 71000c1f    	cmp	w0, #0x3
100008fd4: 540000e0    	b.eq	0x100008ff0 <_main+0x58>
100008fd8: 90000040    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
100008fdc: 913e0400    	add	x0, x0, #0xf81
100008fe0: 90000042    	adrp	x2, 0x100010000 <_zbtIndexScanSlot+0x464>
100008fe4: 913f9442    	add	x2, x2, #0xfe5
100008fe8: 52800401    	mov	w1, #0x20               ; =32
100008fec: 94001d13    	bl	0x100010438 <_standalone_panic>
100008ff0: 529c2016    	mov	w22, #0xe100            ; =57600
100008ff4: 72a0beb6    	movk	w22, #0x5f5, lsl #16
100008ff8: f9400695    	ldr	x21, [x20, #0x8]
100008ffc: 9101a3e1    	add	x1, sp, #0x68
100009000: aa1503e0    	mov	x0, x21
100009004: 52800142    	mov	w2, #0xa                ; =10
100009008: 94001f8a    	bl	0x100010e30 <_strtoull+0x100010e30>
10000900c: aa0003f3    	mov	x19, x0
100009010: 394002a8    	ldrb	w8, [x21]
100009014: 340000e8    	cbz	w8, 0x100009030 <_main+0x98>
100009018: f94037e8    	ldr	x8, [sp, #0x68]
10000901c: 39400108    	ldrb	w8, [x8]
100009020: d1000669    	sub	x9, x19, #0x1
100009024: 7100011f    	cmp	w8, #0x0
100009028: fa560122    	ccmp	x9, x22, #0x2, eq
10000902c: 540000e3    	b.lo	0x100009048 <_main+0xb0>
100009030: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
100009034: 913e0400    	add	x0, x0, #0xf81
100009038: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
10000903c: 91174c42    	add	x2, x2, #0x5d3
100009040: 52800361    	mov	w1, #0x1b               ; =27
100009044: 94001cfd    	bl	0x100010438 <_standalone_panic>
100009048: f9400a95    	ldr	x21, [x20, #0x10]
10000904c: 9101a3e1    	add	x1, sp, #0x68
100009050: aa1503e0    	mov	x0, x21
100009054: 52800142    	mov	w2, #0xa                ; =10
100009058: 94001f76    	bl	0x100010e30 <_strtoull+0x100010e30>
10000905c: aa0003fc    	mov	x28, x0
100009060: 394002a8    	ldrb	w8, [x21]
100009064: 340000e8    	cbz	w8, 0x100009080 <_main+0xe8>
100009068: f94037e8    	ldr	x8, [sp, #0x68]
10000906c: 39400108    	ldrb	w8, [x8]
100009070: d1000789    	sub	x9, x28, #0x1
100009074: 7100011f    	cmp	w8, #0x0
100009078: fa560122    	ccmp	x9, x22, #0x2, eq
10000907c: 540000e3    	b.lo	0x100009098 <_main+0x100>
100009080: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
100009084: 913e0400    	add	x0, x0, #0xf81
100009088: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
10000908c: 91174c42    	add	x2, x2, #0x5d3
100009090: 52800361    	mov	w1, #0x1b               ; =27
100009094: 94001ce9    	bl	0x100010438 <_standalone_panic>
100009098: f0000028    	adrp	x8, 0x100010000 <_zbtIndexScanSlot+0x464>
10000909c: 3dc39100    	ldr	q0, [x8, #0xe40]
1000090a0: 3c9803a0    	stur	q0, [x29, #-0x80]
1000090a4: d10203a0    	sub	x0, x29, #0x80
1000090a8: 94001d4a    	bl	0x1000105d0 <_dictSetHashFunctionSeed>
1000090ac: d37df276    	lsl	x22, x19, #3
1000090b0: aa1603e0    	mov	x0, x22
1000090b4: 94001cf1    	bl	0x100010478 <_zmalloc>
1000090b8: aa0003f5    	mov	x21, x0
1000090bc: aa1603e0    	mov	x0, x22
1000090c0: 94001cee    	bl	0x100010478 <_zmalloc>
1000090c4: aa0003f6    	mov	x22, x0
1000090c8: d37cee60    	lsl	x0, x19, #4
1000090cc: 94001ceb    	bl	0x100010478 <_zmalloc>
1000090d0: aa0003f7    	mov	x23, x0
1000090d4: b40007d3    	cbz	x19, 0x1000091cc <_main+0x234>
1000090d8: d2800014    	mov	x20, #0x0               ; =0
1000090dc: b205cff8    	mov	x24, #0x7878787878787878 ; =8680820740569200760
1000090e0: f9004ff8    	str	x24, [sp, #0x98]
1000090e4: 390243f4    	strb	w20, [sp, #0x90]
1000090e8: d348fe88    	lsr	x8, x20, #8
1000090ec: 390247e8    	strb	w8, [sp, #0x91]
1000090f0: d350fe88    	lsr	x8, x20, #16
1000090f4: 39024be8    	strb	w8, [sp, #0x92]
1000090f8: d358fe88    	lsr	x8, x20, #24
1000090fc: 39024fe8    	strb	w8, [sp, #0x93]
100009100: d360fe88    	lsr	x8, x20, #32
100009104: 390253e8    	strb	w8, [sp, #0x94]
100009108: d368fe88    	lsr	x8, x20, #40
10000910c: 390257e8    	strb	w8, [sp, #0x95]
100009110: d370fe88    	lsr	x8, x20, #48
100009114: 39025be8    	strb	w8, [sp, #0x96]
100009118: d378fe88    	lsr	x8, x20, #56
10000911c: 39025fe8    	strb	w8, [sp, #0x97]
100009120: 910243e0    	add	x0, sp, #0x90
100009124: 52800201    	mov	w1, #0x10               ; =16
100009128: 94001d33    	bl	0x1000105f4 <_sdsnewlen>
10000912c: f8347aa0    	str	x0, [x21, x20, lsl #3]
100009130: f8347ad4    	str	x20, [x22, x20, lsl #3]
100009134: 91000694    	add	x20, x20, #0x1
100009138: eb14027f    	cmp	x19, x20
10000913c: 54fffd21    	b.ne	0x1000090e0 <_main+0x148>
100009140: f100067f    	cmp	x19, #0x1
100009144: 54000440    	b.eq	0x1000091cc <_main+0x234>
100009148: d10022c8    	sub	x8, x22, #0x8
10000914c: d287acc9    	mov	x9, #0x3d66             ; =15718
100009150: f2ae7e49    	movk	x9, #0x73f2, lsl #16
100009154: f2c2aa29    	movk	x9, #0x1551, lsl #32
100009158: f2f035e9    	movk	x9, #0x81af, lsl #48
10000915c: d29cb72a    	mov	x10, #0xe5b9            ; =58809
100009160: f2a39c8a    	movk	x10, #0x1ce4, lsl #16
100009164: f2c8edaa    	movk	x10, #0x476d, lsl #32
100009168: f2f7eb0a    	movk	x10, #0xbf58, lsl #48
10000916c: d2823d6b    	mov	x11, #0x11eb            ; =4587
100009170: f2a2662b    	movk	x11, #0x1331, lsl #16
100009174: f2c9376b    	movk	x11, #0x49bb, lsl #32
100009178: f2f29a0b    	movk	x11, #0x94d0, lsl #48
10000917c: d28f82ac    	mov	x12, #0x7c15            ; =31765
100009180: f2afe94c    	movk	x12, #0x7f4a, lsl #16
100009184: f2cf372c    	movk	x12, #0x79b9, lsl #32
100009188: f2f3c6ec    	movk	x12, #0x9e37, lsl #48
10000918c: aa1303ed    	mov	x13, x19
100009190: ca49792e    	eor	x14, x9, x9, lsr #30
100009194: 9b0a7dce    	mul	x14, x14, x10
100009198: ca4e6dce    	eor	x14, x14, x14, lsr #27
10000919c: 9b0b7dce    	mul	x14, x14, x11
1000091a0: ca4e7dce    	eor	x14, x14, x14, lsr #31
1000091a4: 9acd09cf    	udiv	x15, x14, x13
1000091a8: 9b0db9ee    	msub	x14, x15, x13, x14
1000091ac: f86d790f    	ldr	x15, [x8, x13, lsl #3]
1000091b0: f86e7ad0    	ldr	x16, [x22, x14, lsl #3]
1000091b4: f82d7910    	str	x16, [x8, x13, lsl #3]
1000091b8: f82e7acf    	str	x15, [x22, x14, lsl #3]
1000091bc: d10005ad    	sub	x13, x13, #0x1
1000091c0: 8b0c0129    	add	x9, x9, x12
1000091c4: f10005bf    	cmp	x13, #0x1
1000091c8: 54fffe48    	b.hi	0x100009190 <_main+0x1f8>
1000091cc: 9101a3f4    	add	x20, sp, #0x68
1000091d0: 9101a3e1    	add	x1, sp, #0x68
1000091d4: 52800e00    	mov	w0, #0x70               ; =112
1000091d8: 94001cbc    	bl	0x1000104c8 <_zmalloc_usable>
1000091dc: aa0003f8    	mov	x24, x0
1000091e0: 6f00e400    	movi.2d	v0, #0000000000000000
1000091e4: ad028000    	stp	q0, q0, [x0, #0x50]
1000091e8: ad000000    	stp	q0, q0, [x0]
1000091ec: ad010000    	stp	q0, q0, [x0, #0x20]
1000091f0: 3d801000    	str	q0, [x0, #0x40]
1000091f4: f0000068    	adrp	x8, 0x100018000 <_shared>
1000091f8: b9401109    	ldr	w9, [x8, #0x10]
1000091fc: 1100052a    	add	w10, w9, #0x1
100009200: 7100055f    	cmp	w10, #0x1
100009204: 5280002a    	mov	w10, #0x1               ; =1
100009208: 1a899549    	csinc	w9, w10, w9, ls
10000920c: b9001109    	str	w9, [x8, #0x10]
100009210: b9005c09    	str	w9, [x0, #0x5c]
100009214: f94037e8    	ldr	x8, [sp, #0x68]
100009218: f9003408    	str	x8, [x0, #0x68]
10000921c: b40019f3    	cbz	x19, 0x100009558 <_main+0x5c0>
100009220: f9001bfc    	str	x28, [sp, #0x30]
100009224: d2800019    	mov	x25, #0x0               ; =0
100009228: 14000019    	b	0x10000928c <_main+0x2f4>
10000922c: 785fb37a    	ldurh	w26, [x27, #-0x5]
100009230: 7e61d808    	ucvtf	d8, d0
100009234: b9405ffc    	ldr	w28, [sp, #0x5c]
100009238: aa1803e0    	mov	x0, x24
10000923c: 52800021    	mov	w1, #0x1                ; =1
100009240: 97ffdcf7    	bl	0x10000061c <_zbtIndexExpandIfNeeded>
100009244: a906ebfb    	stp	x27, x26, [sp, #0x68]
100009248: b9007bfc    	str	w28, [sp, #0x78]
10000924c: a901fe9f    	stp	xzr, xzr, [x20, #0x18]
100009250: 9101a3e1    	add	x1, sp, #0x68
100009254: aa1803e0    	mov	x0, x24
100009258: 1e604100    	fmov	d0, d8
10000925c: 97ffe8eb    	bl	0x100003608 <_zbtScoreInsert>
100009260: f9403308    	ldr	x8, [x24, #0x60]
100009264: 91000508    	add	x8, x8, #0x1
100009268: f9003308    	str	x8, [x24, #0x60]
10000926c: b9403002    	ldr	w2, [x0, #0x30]
100009270: 910103e3    	add	x3, sp, #0x40
100009274: aa1803e0    	mov	x0, x24
100009278: aa1c03e1    	mov	x1, x28
10000927c: 97ffe934    	bl	0x10000374c <_zbtIndexInsert>
100009280: 91000739    	add	x25, x25, #0x1
100009284: eb19027f    	cmp	x19, x25
100009288: 540004c0    	b.eq	0x100009320 <_main+0x388>
10000928c: f8797ac8    	ldr	x8, [x22, x25, lsl #3]
100009290: f8687abb    	ldr	x27, [x21, x8, lsl #3]
100009294: 9100e3e2    	add	x2, sp, #0x38
100009298: 910103e3    	add	x3, sp, #0x40
10000929c: aa1803e0    	mov	x0, x24
1000092a0: aa1b03e1    	mov	x1, x27
1000092a4: 97ffe42b    	bl	0x100002350 <_zbtreeFindForAdd>
1000092a8: 340000e0    	cbz	w0, 0x1000092c4 <_main+0x32c>
1000092ac: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
1000092b0: 913e0400    	add	x0, x0, #0xf81
1000092b4: 52800721    	mov	w1, #0x39               ; =57
1000092b8: f0000022    	adrp	x2, 0x100010000 <_zbtIndexScanSlot+0x464>
1000092bc: 913fbc42    	add	x2, x2, #0xfef
1000092c0: 94001c5e    	bl	0x100010438 <_standalone_panic>
1000092c4: d280001a    	mov	x26, #0x0               ; =0
1000092c8: fc797ac0    	ldr	d0, [x22, x25, lsl #3]
1000092cc: 385ff369    	ldurb	w9, [x27, #-0x1]
1000092d0: 12000928    	and	w8, w9, #0x7
1000092d4: 7100051f    	cmp	w8, #0x1
1000092d8: 5400012d    	b.le	0x1000092fc <_main+0x364>
1000092dc: 7100091f    	cmp	w8, #0x2
1000092e0: 54fffa60    	b.eq	0x10000922c <_main+0x294>
1000092e4: 71000d1f    	cmp	w8, #0x3
1000092e8: 54000140    	b.eq	0x100009310 <_main+0x378>
1000092ec: 7100111f    	cmp	w8, #0x4
1000092f0: 54fffa01    	b.ne	0x100009230 <_main+0x298>
1000092f4: f85ef37a    	ldur	x26, [x27, #-0x11]
1000092f8: 17ffffce    	b	0x100009230 <_main+0x298>
1000092fc: 340000e8    	cbz	w8, 0x100009318 <_main+0x380>
100009300: 7100051f    	cmp	w8, #0x1
100009304: 54fff961    	b.ne	0x100009230 <_main+0x298>
100009308: 385fd37a    	ldurb	w26, [x27, #-0x3]
10000930c: 17ffffc9    	b	0x100009230 <_main+0x298>
100009310: b85f737a    	ldur	w26, [x27, #-0x9]
100009314: 17ffffc7    	b	0x100009230 <_main+0x298>
100009318: d343fd3a    	lsr	x26, x9, #3
10000931c: 17ffffc5    	b	0x100009230 <_main+0x298>
100009320: d280001a    	mov	x26, #0x0               ; =0
100009324: f0000039    	adrp	x25, 0x100010000 <_zbtIndexScanSlot+0x464>
100009328: 913e0739    	add	x25, x25, #0xf81
10000932c: 90000054    	adrp	x20, 0x100011000 <_strtoull+0x100011000>
100009330: 91005a94    	add	x20, x20, #0x16
100009334: 9000005b    	adrp	x27, 0x100011000 <_strtoull+0x100011000>
100009338: 9101577b    	add	x27, x27, #0x55
10000933c: 9000005c    	adrp	x28, 0x100011000 <_strtoull+0x100011000>
100009340: 91010b9c    	add	x28, x28, #0x42
100009344: 14000004    	b	0x100009354 <_main+0x3bc>
100009348: 9100075a    	add	x26, x26, #0x1
10000934c: eb13035f    	cmp	x26, x19
100009350: 540009a0    	b.eq	0x100009484 <_main+0x4ec>
100009354: f87a7aa1    	ldr	x1, [x21, x26, lsl #3]
100009358: 910103e2    	add	x2, sp, #0x40
10000935c: 9101a3e3    	add	x3, sp, #0x68
100009360: aa1803e0    	mov	x0, x24
100009364: 97ffe3fb    	bl	0x100002350 <_zbtreeFindForAdd>
100009368: 34000740    	cbz	w0, 0x100009450 <_main+0x4b8>
10000936c: fd4023e0    	ldr	d0, [sp, #0x40]
100009370: 9e630341    	ucvtf	d1, x26
100009374: 1e612000    	fcmp	d0, d1
100009378: 540007c1    	b.ne	0x100009470 <_main+0x4d8>
10000937c: 8b1a12ea    	add	x10, x23, x26, lsl #4
100009380: f9403fe8    	ldr	x8, [sp, #0x78]
100009384: b94083e9    	ldr	w9, [sp, #0x80]
100009388: f9000148    	str	x8, [x10]
10000938c: b9000949    	str	w9, [x10, #0x8]
100009390: f940010b    	ldr	x11, [x8]
100009394: b400050b    	cbz	x11, 0x100009434 <_main+0x49c>
100009398: 3940410a    	ldrb	w10, [x8, #0x10]
10000939c: aa0b03e8    	mov	x8, x11
1000093a0: 34ffff8a    	cbz	w10, 0x100009390 <_main+0x3f8>
1000093a4: 7100215f    	cmp	w10, #0x8
1000093a8: 54000062    	b.hs	0x1000093b4 <_main+0x41c>
1000093ac: d280000b    	mov	x11, #0x0               ; =0
1000093b0: 14000019    	b	0x100009414 <_main+0x47c>
1000093b4: 927d114b    	and	x11, x10, #0xf8
1000093b8: 6f00e400    	movi.2d	v0, #0000000000000000
1000093bc: 6f00e401    	movi.2d	v1, #0000000000000000
1000093c0: 4e081d21    	mov.d	v1[0], x9
1000093c4: 91052109    	add	x9, x8, #0x148
1000093c8: aa0b03ec    	mov	x12, x11
1000093cc: 6f00e402    	movi.2d	v2, #0000000000000000
1000093d0: 6f00e403    	movi.2d	v3, #0000000000000000
1000093d4: ad7e9524    	ldp	q4, q5, [x9, #-0x30]
1000093d8: ad7f9d26    	ldp	q6, q7, [x9, #-0x10]
1000093dc: 4ee18481    	add.2d	v1, v4, v1
1000093e0: 4ee084a0    	add.2d	v0, v5, v0
1000093e4: 4ee284c2    	add.2d	v2, v6, v2
1000093e8: 4ee384e3    	add.2d	v3, v7, v3
1000093ec: 91010129    	add	x9, x9, #0x40
1000093f0: f100218c    	subs	x12, x12, #0x8
1000093f4: 54ffff01    	b.ne	0x1000093d4 <_main+0x43c>
1000093f8: 4ee18400    	add.2d	v0, v0, v1
1000093fc: 4ee08440    	add.2d	v0, v2, v0
100009400: 4ee08460    	add.2d	v0, v3, v0
100009404: 5ef1b800    	addp.2d	d0, v0
100009408: 9e660009    	fmov	x9, d0
10000940c: eb0a017f    	cmp	x11, x10
100009410: 54fffc00    	b.eq	0x100009390 <_main+0x3f8>
100009414: cb0b014a    	sub	x10, x10, x11
100009418: 8b0b0d0b    	add	x11, x8, x11, lsl #3
10000941c: 9104616b    	add	x11, x11, #0x118
100009420: f840856c    	ldr	x12, [x11], #0x8
100009424: 8b090189    	add	x9, x12, x9
100009428: f100054a    	subs	x10, x10, #0x1
10000942c: 54ffffa1    	b.ne	0x100009420 <_main+0x488>
100009430: 17ffffd8    	b	0x100009390 <_main+0x3f8>
100009434: eb1a013f    	cmp	x9, x26
100009438: 54fff880    	b.eq	0x100009348 <_main+0x3b0>
10000943c: aa1903e0    	mov	x0, x25
100009440: 52800861    	mov	w1, #0x43               ; =67
100009444: aa1b03e2    	mov	x2, x27
100009448: 94001bfc    	bl	0x100010438 <_standalone_panic>
10000944c: 17ffffbf    	b	0x100009348 <_main+0x3b0>
100009450: aa1903e0    	mov	x0, x25
100009454: 52800801    	mov	w1, #0x40               ; =64
100009458: aa1403e2    	mov	x2, x20
10000945c: 94001bf7    	bl	0x100010438 <_standalone_panic>
100009460: fd4023e0    	ldr	d0, [sp, #0x40]
100009464: 9e630341    	ucvtf	d1, x26
100009468: 1e612000    	fcmp	d0, d1
10000946c: 54fff880    	b.eq	0x10000937c <_main+0x3e4>
100009470: aa1903e0    	mov	x0, x25
100009474: 52800821    	mov	w1, #0x41               ; =65
100009478: aa1c03e2    	mov	x2, x28
10000947c: 94001bef    	bl	0x100010438 <_standalone_panic>
100009480: 17ffffbf    	b	0x10000937c <_main+0x3e4>
100009484: d2800008    	mov	x8, #0x0                ; =0
100009488: d2800009    	mov	x9, #0x0                ; =0
10000948c: f9401bfc    	ldr	x28, [sp, #0x30]
100009490: 14000005    	b	0x1000094a4 <_main+0x50c>
100009494: 8b080168    	add	x8, x11, x8
100009498: 91000529    	add	x9, x9, #0x1
10000949c: eb13013f    	cmp	x9, x19
1000094a0: 540005e0    	b.eq	0x10000955c <_main+0x5c4>
1000094a4: f8697aca    	ldr	x10, [x22, x9, lsl #3]
1000094a8: 8b0a12eb    	add	x11, x23, x10, lsl #4
1000094ac: f940016a    	ldr	x10, [x11]
1000094b0: b940096b    	ldr	w11, [x11, #0x8]
1000094b4: f940014d    	ldr	x13, [x10]
1000094b8: b4fffeed    	cbz	x13, 0x100009494 <_main+0x4fc>
1000094bc: 3940414c    	ldrb	w12, [x10, #0x10]
1000094c0: aa0d03ea    	mov	x10, x13
1000094c4: 34ffff8c    	cbz	w12, 0x1000094b4 <_main+0x51c>
1000094c8: 7100219f    	cmp	w12, #0x8
1000094cc: 54000062    	b.hs	0x1000094d8 <_main+0x540>
1000094d0: d280000d    	mov	x13, #0x0               ; =0
1000094d4: 14000019    	b	0x100009538 <_main+0x5a0>
1000094d8: 927d118d    	and	x13, x12, #0xf8
1000094dc: 6f00e400    	movi.2d	v0, #0000000000000000
1000094e0: 6f00e401    	movi.2d	v1, #0000000000000000
1000094e4: 4e081d61    	mov.d	v1[0], x11
1000094e8: 9105214b    	add	x11, x10, #0x148
1000094ec: aa0d03ee    	mov	x14, x13
1000094f0: 6f00e402    	movi.2d	v2, #0000000000000000
1000094f4: 6f00e403    	movi.2d	v3, #0000000000000000
1000094f8: ad7e9564    	ldp	q4, q5, [x11, #-0x30]
1000094fc: ad7f9d66    	ldp	q6, q7, [x11, #-0x10]
100009500: 4ee18481    	add.2d	v1, v4, v1
100009504: 4ee084a0    	add.2d	v0, v5, v0
100009508: 4ee284c2    	add.2d	v2, v6, v2
10000950c: 4ee384e3    	add.2d	v3, v7, v3
100009510: 9101016b    	add	x11, x11, #0x40
100009514: f10021ce    	subs	x14, x14, #0x8
100009518: 54ffff01    	b.ne	0x1000094f8 <_main+0x560>
10000951c: 4ee18400    	add.2d	v0, v0, v1
100009520: 4ee08440    	add.2d	v0, v2, v0
100009524: 4ee08460    	add.2d	v0, v3, v0
100009528: 5ef1b800    	addp.2d	d0, v0
10000952c: 9e66000b    	fmov	x11, d0
100009530: eb0c01bf    	cmp	x13, x12
100009534: 54fffc00    	b.eq	0x1000094b4 <_main+0x51c>
100009538: cb0d018c    	sub	x12, x12, x13
10000953c: 8b0d0d4d    	add	x13, x10, x13, lsl #3
100009540: 910461ad    	add	x13, x13, #0x118
100009544: f84085ae    	ldr	x14, [x13], #0x8
100009548: 8b0b01cb    	add	x11, x14, x11
10000954c: f100058c    	subs	x12, x12, #0x1
100009550: 54ffffa1    	b.ne	0x100009544 <_main+0x5ac>
100009554: 17ffffd8    	b	0x1000094b4 <_main+0x51c>
100009558: d2800008    	mov	x8, #0x0                ; =0
10000955c: d1000669    	sub	x9, x19, #0x1
100009560: 9b137d29    	mul	x9, x9, x19
100009564: eb49051f    	cmp	x8, x9, lsr #1
100009568: 540000e0    	b.eq	0x100009584 <_main+0x5ec>
10000956c: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
100009570: 913e0400    	add	x0, x0, #0xf81
100009574: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
100009578: 91020842    	add	x2, x2, #0x82
10000957c: 52800b81    	mov	w1, #0x5c               ; =92
100009580: 94001bae    	bl	0x100010438 <_standalone_panic>
100009584: 9101a3e1    	add	x1, sp, #0x68
100009588: 528000c0    	mov	w0, #0x6                ; =6
10000958c: 94001e02    	bl	0x100010d94 <_strtoull+0x100010d94>
100009590: 340000e0    	cbz	w0, 0x1000095ac <_main+0x614>
100009594: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
100009598: 913e0400    	add	x0, x0, #0xf81
10000959c: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
1000095a0: 9117e842    	add	x2, x2, #0x5fa
1000095a4: 528002a1    	mov	w1, #0x15               ; =21
1000095a8: 94001ba4    	bl	0x100010438 <_standalone_panic>
1000095ac: b400073c    	cbz	x28, 0x100009690 <_main+0x6f8>
1000095b0: d2800008    	mov	x8, #0x0                ; =0
1000095b4: d280001a    	mov	x26, #0x0               ; =0
1000095b8: d2800019    	mov	x25, #0x0               ; =0
1000095bc: 14000006    	b	0x1000095d4 <_main+0x63c>
1000095c0: 8b190179    	add	x25, x11, x25
1000095c4: 8b1a013a    	add	x26, x9, x26
1000095c8: 91000508    	add	x8, x8, #0x1
1000095cc: eb1c011f    	cmp	x8, x28
1000095d0: 54000640    	b.eq	0x100009698 <_main+0x700>
1000095d4: 9ad30909    	udiv	x9, x8, x19
1000095d8: 9b13a129    	msub	x9, x9, x19, x8
1000095dc: f8697ac9    	ldr	x9, [x22, x9, lsl #3]
1000095e0: 8b0912eb    	add	x11, x23, x9, lsl #4
1000095e4: f940016a    	ldr	x10, [x11]
1000095e8: b940096b    	ldr	w11, [x11, #0x8]
1000095ec: f940014d    	ldr	x13, [x10]
1000095f0: b4fffe8d    	cbz	x13, 0x1000095c0 <_main+0x628>
1000095f4: 3940414c    	ldrb	w12, [x10, #0x10]
1000095f8: aa0d03ea    	mov	x10, x13
1000095fc: 34ffff8c    	cbz	w12, 0x1000095ec <_main+0x654>
100009600: 7100219f    	cmp	w12, #0x8
100009604: 54000062    	b.hs	0x100009610 <_main+0x678>
100009608: d280000d    	mov	x13, #0x0               ; =0
10000960c: 14000019    	b	0x100009670 <_main+0x6d8>
100009610: 927d118d    	and	x13, x12, #0xf8
100009614: 6f00e400    	movi.2d	v0, #0000000000000000
100009618: 6f00e401    	movi.2d	v1, #0000000000000000
10000961c: 4e081d61    	mov.d	v1[0], x11
100009620: 9105214b    	add	x11, x10, #0x148
100009624: aa0d03ee    	mov	x14, x13
100009628: 6f00e402    	movi.2d	v2, #0000000000000000
10000962c: 6f00e403    	movi.2d	v3, #0000000000000000
100009630: ad7e9564    	ldp	q4, q5, [x11, #-0x30]
100009634: ad7f9d66    	ldp	q6, q7, [x11, #-0x10]
100009638: 4ee18481    	add.2d	v1, v4, v1
10000963c: 4ee084a0    	add.2d	v0, v5, v0
100009640: 4ee284c2    	add.2d	v2, v6, v2
100009644: 4ee384e3    	add.2d	v3, v7, v3
100009648: 9101016b    	add	x11, x11, #0x40
10000964c: f10021ce    	subs	x14, x14, #0x8
100009650: 54ffff01    	b.ne	0x100009630 <_main+0x698>
100009654: 4ee18400    	add.2d	v0, v0, v1
100009658: 4ee08440    	add.2d	v0, v2, v0
10000965c: 4ee08460    	add.2d	v0, v3, v0
100009660: 5ef1b800    	addp.2d	d0, v0
100009664: 9e66000b    	fmov	x11, d0
100009668: eb0c01bf    	cmp	x13, x12
10000966c: 54fffc00    	b.eq	0x1000095ec <_main+0x654>
100009670: cb0d018c    	sub	x12, x12, x13
100009674: 8b0d0d4d    	add	x13, x10, x13, lsl #3
100009678: 910461ad    	add	x13, x13, #0x118
10000967c: f84085ae    	ldr	x14, [x13], #0x8
100009680: 8b0b01cb    	add	x11, x14, x11
100009684: f100058c    	subs	x12, x12, #0x1
100009688: 54ffffa1    	b.ne	0x10000967c <_main+0x6e4>
10000968c: 17ffffd8    	b	0x1000095ec <_main+0x654>
100009690: d2800019    	mov	x25, #0x0               ; =0
100009694: d280001a    	mov	x26, #0x0               ; =0
100009698: a946d3fb    	ldp	x27, x20, [sp, #0x68]
10000969c: 9101a3e1    	add	x1, sp, #0x68
1000096a0: 528000c0    	mov	w0, #0x6                ; =6
1000096a4: 94001dbc    	bl	0x100010d94 <_strtoull+0x100010d94>
1000096a8: 340000e0    	cbz	w0, 0x1000096c4 <_main+0x72c>
1000096ac: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
1000096b0: 913e0400    	add	x0, x0, #0xf81
1000096b4: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
1000096b8: 9117e842    	add	x2, x2, #0x5fa
1000096bc: 528002a1    	mov	w1, #0x15               ; =21
1000096c0: 94001b5e    	bl	0x100010438 <_standalone_panic>
1000096c4: a946a7e8    	ldp	x8, x9, [sp, #0x68]
1000096c8: cb1b0108    	sub	x8, x8, x27
1000096cc: 5299400a    	mov	w10, #0xca00            ; =51712
1000096d0: 72a7734a    	movk	w10, #0x3b9a, lsl #16
1000096d4: cb140129    	sub	x9, x9, x20
1000096d8: 9b0a2514    	madd	x20, x8, x10, x9
1000096dc: eb1a033f    	cmp	x25, x26
1000096e0: 540000e0    	b.eq	0x1000096fc <_main+0x764>
1000096e4: f0000020    	adrp	x0, 0x100010000 <_zbtIndexScanSlot+0x464>
1000096e8: 913e0400    	add	x0, x0, #0xf81
1000096ec: 90000042    	adrp	x2, 0x100011000 <_strtoull+0x100011000>
1000096f0: 91027842    	add	x2, x2, #0x9e
1000096f4: 52800ca1    	mov	w1, #0x65               ; =101
1000096f8: 94001b50    	bl	0x100010438 <_standalone_panic>
1000096fc: f0000068    	adrp	x8, 0x100018000 <_shared>
100009700: f9400d09    	ldr	x9, [x8, #0x18]
100009704: ca190129    	eor	x9, x9, x25
100009708: f9000d09    	str	x9, [x8, #0x18]
10000970c: 90000040    	adrp	x0, 0x100011000 <_strtoull+0x100011000>
100009710: 91188c00    	add	x0, x0, #0x623
100009714: 94001dbe    	bl	0x100010e0c <_strtoull+0x100010e0c>
100009718: 9e630280    	ucvtf	d0, x20
10000971c: 9e630381    	ucvtf	d1, x28
100009720: 1e611800    	fdiv	d0, d0, d1
100009724: f9403708    	ldr	x8, [x24, #0x68]
100009728: a90223f9    	stp	x25, x8, [sp, #0x20]
10000972c: fd000fe0    	str	d0, [sp, #0x18]
100009730: a900d3fc    	stp	x28, x20, [sp, #0x8]
100009734: f90003f3    	str	x19, [sp]
100009738: 90000040    	adrp	x0, 0x100011000 <_strtoull+0x100011000>
10000973c: 9102b800    	add	x0, x0, #0xae
100009740: 94001db0    	bl	0x100010e00 <_strtoull+0x100010e00>
100009744: aa1803e0    	mov	x0, x24
100009748: 97ffdd5a    	bl	0x100000cb0 <_zbtreeFree>
10000974c: b40000d3    	cbz	x19, 0x100009764 <_main+0x7cc>
100009750: aa1503f4    	mov	x20, x21
100009754: f8408680    	ldr	x0, [x20], #0x8
100009758: 94001be1    	bl	0x1000106dc <_sdsfree>
10000975c: f1000673    	subs	x19, x19, #0x1
100009760: 54ffffa1    	b.ne	0x100009754 <_main+0x7bc>
100009764: aa1503e0    	mov	x0, x21
100009768: 94001b57    	bl	0x1000104c4 <_zfree>
10000976c: aa1603e0    	mov	x0, x22
100009770: 94001b55    	bl	0x1000104c4 <_zfree>
100009774: aa1703e0    	mov	x0, x23
100009778: 94001b53    	bl	0x1000104c4 <_zfree>
10000977c: f85903a8    	ldur	x8, [x29, #-0x70]
100009780: f0000049    	adrp	x9, 0x100014000 <_strtoull+0x100014000>
100009784: f9400d29    	ldr	x9, [x9, #0x18]
100009788: f9400129    	ldr	x9, [x9]
10000978c: eb08013f    	cmp	x9, x8
100009790: 54000161    	b.ne	0x1000097bc <_main+0x824>
100009794: 52800000    	mov	w0, #0x0                ; =0
100009798: a9527bfd    	ldp	x29, x30, [sp, #0x120]
10000979c: a9514ff4    	ldp	x20, x19, [sp, #0x110]
1000097a0: a95057f6    	ldp	x22, x21, [sp, #0x100]
1000097a4: a94f5ff8    	ldp	x24, x23, [sp, #0xf0]
1000097a8: a94e67fa    	ldp	x26, x25, [sp, #0xe0]
1000097ac: a94d6ffc    	ldp	x28, x27, [sp, #0xd0]
1000097b0: 6d4c23e9    	ldp	d9, d8, [sp, #0xc0]
1000097b4: 9104c3ff    	add	sp, sp, #0x130
1000097b8: d65f03c0    	ret
1000097bc: 94001d6a    	bl	0x100010d64 <_strtoull+0x100010d64>
