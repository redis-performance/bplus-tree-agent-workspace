
build/size-matrix/btree-bench:	file format mach-o arm64

Disassembly of section __TEXT,__text:

00000001000044fc <_zbtreeRank>:
1000044fc: d10303ff    	sub	sp, sp, #0xc0
100004500: a9066ffc    	stp	x28, x27, [sp, #0x60]
100004504: a90767fa    	stp	x26, x25, [sp, #0x70]
100004508: a9085ff8    	stp	x24, x23, [sp, #0x80]
10000450c: a90957f6    	stp	x22, x21, [sp, #0x90]
100004510: a90a4ff4    	stp	x20, x19, [sp, #0xa0]
100004514: a90b7bfd    	stp	x29, x30, [sp, #0xb0]
100004518: 9102c3fd    	add	x29, sp, #0xb0
10000451c: f90023e3    	str	x3, [sp, #0x40]
100004520: aa0203f4    	mov	x20, x2
100004524: aa0103f5    	mov	x21, x1
100004528: aa0003f3    	mov	x19, x0
10000452c: d2800001    	mov	x1, #0x0                ; =0
100004530: 385ff2a9    	ldurb	w9, [x21, #-0x1]
100004534: 12000928    	and	w8, w9, #0x7
100004538: 7100051f    	cmp	w8, #0x1
10000453c: 5400012d    	b.le	0x100004560 <_zbtreeRank+0x64>
100004540: 7100091f    	cmp	w8, #0x2
100004544: 54000180    	b.eq	0x100004574 <_zbtreeRank+0x78>
100004548: 71000d1f    	cmp	w8, #0x3
10000454c: 54000180    	b.eq	0x10000457c <_zbtreeRank+0x80>
100004550: 7100111f    	cmp	w8, #0x4
100004554: 540001a1    	b.ne	0x100004588 <_zbtreeRank+0x8c>
100004558: f85ef2a1    	ldur	x1, [x21, #-0x11]
10000455c: 1400000b    	b	0x100004588 <_zbtreeRank+0x8c>
100004560: 34000128    	cbz	w8, 0x100004584 <_zbtreeRank+0x88>
100004564: 7100051f    	cmp	w8, #0x1
100004568: 54000101    	b.ne	0x100004588 <_zbtreeRank+0x8c>
10000456c: 385fd2a1    	ldurb	w1, [x21, #-0x3]
100004570: 14000006    	b	0x100004588 <_zbtreeRank+0x8c>
100004574: 785fb2a1    	ldurh	w1, [x21, #-0x5]
100004578: 14000004    	b	0x100004588 <_zbtreeRank+0x8c>
10000457c: b85f72a1    	ldur	w1, [x21, #-0x9]
100004580: 14000002    	b	0x100004588 <_zbtreeRank+0x8c>
100004584: d343fd21    	lsr	x1, x9, #3
100004588: aa1503e0    	mov	x0, x21
10000458c: 940033b3    	bl	0x100011458 <_dictGenHashFunction>
100004590: a904ffe0    	stp	x0, xzr, [sp, #0x48]
100004594: 385ff2a9    	ldurb	w9, [x21, #-0x1]
100004598: 12000928    	and	w8, w9, #0x7
10000459c: 7100051f    	cmp	w8, #0x1
1000045a0: b9000ff4    	str	w20, [sp, #0xc]
1000045a4: 5400012d    	b.le	0x1000045c8 <_zbtreeRank+0xcc>
1000045a8: 7100091f    	cmp	w8, #0x2
1000045ac: 54000180    	b.eq	0x1000045dc <_zbtreeRank+0xe0>
1000045b0: 71000d1f    	cmp	w8, #0x3
1000045b4: 54000180    	b.eq	0x1000045e4 <_zbtreeRank+0xe8>
1000045b8: 7100111f    	cmp	w8, #0x4
1000045bc: 540001c1    	b.ne	0x1000045f4 <_zbtreeRank+0xf8>
1000045c0: f85ef2a8    	ldur	x8, [x21, #-0x11]
1000045c4: 1400000b    	b	0x1000045f0 <_zbtreeRank+0xf4>
1000045c8: 34000128    	cbz	w8, 0x1000045ec <_zbtreeRank+0xf0>
1000045cc: 7100051f    	cmp	w8, #0x1
1000045d0: 54000121    	b.ne	0x1000045f4 <_zbtreeRank+0xf8>
1000045d4: 385fd2a8    	ldurb	w8, [x21, #-0x3]
1000045d8: 14000006    	b	0x1000045f0 <_zbtreeRank+0xf4>
1000045dc: 785fb2a8    	ldurh	w8, [x21, #-0x5]
1000045e0: 14000004    	b	0x1000045f0 <_zbtreeRank+0xf4>
1000045e4: b85f72a8    	ldur	w8, [x21, #-0x9]
1000045e8: 14000002    	b	0x1000045f0 <_zbtreeRank+0xf4>
1000045ec: d343fd28    	lsr	x8, x9, #3
1000045f0: f9002be8    	str	x8, [sp, #0x50]
1000045f4: f9001ff5    	str	x21, [sp, #0x38]
1000045f8: f9402268    	ldr	x8, [x19, #0x40]
1000045fc: b4001488    	cbz	x8, 0x10000488c <_zbtreeRank+0x390>
100004600: aa1303e0    	mov	x0, x19
100004604: 52800021    	mov	w1, #0x1                ; =1
100004608: 9400091c    	bl	0x100006a78 <_zbtIndexRehashStep>
10000460c: f9402274    	ldr	x20, [x19, #0x40]
100004610: b40013f4    	cbz	x20, 0x10000488c <_zbtreeRank+0x390>
100004614: f9400688    	ldr	x8, [x20, #0x8]
100004618: b40013a8    	cbz	x8, 0x10000488c <_zbtreeRank+0x390>
10000461c: d280001b    	mov	x27, #0x0               ; =0
100004620: f94027eb    	ldr	x11, [sp, #0x48]
100004624: 53187d69    	lsr	w9, w11, #24
100004628: d358fd6a    	lsr	x10, x11, #24
10000462c: 7100013f    	cmp	w9, #0x0
100004630: 1a9f1549    	csinc	w9, w10, wzr, ne
100004634: d1000508    	sub	x8, x8, #0x1
100004638: 2a0b03ea    	mov	w10, w11
10000463c: a90223ea    	stp	x10, x8, [sp, #0x20]
100004640: 8a0a011c    	and	x28, x8, x10
100004644: 92401d28    	and	x8, x9, #0xff
100004648: b200c3ea    	mov	x10, #0x101010101010101 ; =72340172838076673
10000464c: 9b0a7d0a    	mul	x10, x8, x10
100004650: f9001bea    	str	x10, [sp, #0x30]
100004654: 91006275    	add	x21, x19, #0x18
100004658: d28f82aa    	mov	x10, #0x7c15            ; =31765
10000465c: f2afe94a    	movk	x10, #0x7f4a, lsl #16
100004660: f2cf372a    	movk	x10, #0x79b9, lsl #32
100004664: f2f3c6ea    	movk	x10, #0x9e37, lsl #48
100004668: 9b0a7d08    	mul	x8, x8, x10
10000466c: 5280002a    	mov	w10, #0x1               ; =1
100004670: 9ac9214b    	lsl	x11, x10, x9
100004674: d37afd0c    	lsr	x12, x8, #58
100004678: 9acc214c    	lsl	x12, x10, x12
10000467c: aa0b018b    	orr	x11, x12, x11
100004680: d364fd08    	lsr	x8, x8, #36
100004684: 9ac82148    	lsl	x8, x10, x8
100004688: aa080168    	orr	x8, x11, x8
10000468c: f9000fe8    	str	x8, [sp, #0x18]
100004690: 12001d38    	and	w24, w9, #0xff
100004694: f9400288    	ldr	x8, [x20]
100004698: b9402289    	ldr	w9, [x20, #0x20]
10000469c: 7100013f    	cmp	w9, #0x0
1000046a0: 52800609    	mov	w9, #0x30               ; =48
1000046a4: 5280040a    	mov	w10, #0x20              ; =32
1000046a8: 9a890149    	csel	x9, x10, x9, eq
1000046ac: 9b1c2136    	madd	x22, x9, x28, x8
1000046b0: f94002c8    	ldr	x8, [x22]
1000046b4: f9401be9    	ldr	x9, [sp, #0x30]
1000046b8: ca090108    	eor	x8, x8, x9
1000046bc: b207dbe9    	mov	x9, #-0x101010101010102 ; =-72340172838076674
1000046c0: f29fdfe9    	movk	x9, #0xfeff
1000046c4: 8b090109    	add	x9, x8, x9
1000046c8: 8a280128    	bic	x8, x9, x8
1000046cc: f201c11a    	ands	x26, x8, #0x8080808080808080
1000046d0: 540008c0    	b.eq	0x1000047e8 <_zbtreeRank+0x2ec>
1000046d4: 910042d7    	add	x23, x22, #0x10
1000046d8: 1400000a    	b	0x100004700 <_zbtreeRank+0x204>
1000046dc: d0000060    	adrp	x0, 0x100012000 <_strtoull+0x100012000>
1000046e0: 910a8800    	add	x0, x0, #0x2a2
1000046e4: 5280f421    	mov	w1, #0x7a1              ; =1953
1000046e8: d0000062    	adrp	x2, 0x100012000 <_strtoull+0x100012000>
1000046ec: 91106842    	add	x2, x2, #0x41a
1000046f0: 940032ef    	bl	0x1000112ac <_standalone_panic>
1000046f4: d1000748    	sub	x8, x26, #0x1
1000046f8: ea1a011a    	ands	x26, x8, x26
1000046fc: 54000760    	b.eq	0x1000047e8 <_zbtreeRank+0x2ec>
100004700: dac00348    	rbit	x8, x26
100004704: dac01108    	clz	x8, x8
100004708: f94002c9    	ldr	x9, [x22]
10000470c: 927d090a    	and	x10, x8, #0x38
100004710: 9aca2529    	lsr	x9, x9, x10
100004714: 6b29031f    	cmp	w24, w9, uxtb
100004718: 54fffee1    	b.ne	0x1000046f4 <_zbtreeRank+0x1f8>
10000471c: d343fd08    	lsr	x8, x8, #3
100004720: b9402289    	ldr	w9, [x20, #0x20]
100004724: 340000a9    	cbz	w9, 0x100004738 <_zbtreeRank+0x23c>
100004728: b8687ae8    	ldr	w8, [x23, x8, lsl #2]
10000472c: 3100051f    	cmn	w8, #0x1
100004730: 540000c1    	b.ne	0x100004748 <_zbtreeRank+0x24c>
100004734: 17fffff0    	b	0x1000046f4 <_zbtreeRank+0x1f8>
100004738: 78687ae8    	ldrh	w8, [x23, x8, lsl #1]
10000473c: 529fffe9    	mov	w9, #0xffff             ; =65535
100004740: 6b09011f    	cmp	w8, w9
100004744: 54fffd80    	b.eq	0x1000046f4 <_zbtreeRank+0x1f8>
100004748: b9405669    	ldr	w9, [x19, #0x54]
10000474c: 6b09011f    	cmp	w8, w9
100004750: 540000e2    	b.hs	0x10000476c <_zbtreeRank+0x270>
100004754: f9402669    	ldr	x9, [x19, #0x48]
100004758: f8685939    	ldr	x25, [x9, w8, uxtw #3]
10000475c: 92400329    	and	x9, x25, #0x1
100004760: f100033f    	cmp	x25, #0x0
100004764: fa401920    	ccmp	x9, #0x0, #0x0, ne
100004768: 540000c0    	b.eq	0x100004780 <_zbtreeRank+0x284>
10000476c: f9402268    	ldr	x8, [x19, #0x40]
100004770: b4fffb68    	cbz	x8, 0x1000046dc <_zbtreeRank+0x1e0>
100004774: eb1402bf    	cmp	x21, x20
100004778: 54fffbe0    	b.eq	0x1000046f4 <_zbtreeRank+0x1f8>
10000477c: 17ffffd8    	b	0x1000046dc <_zbtreeRank+0x1e0>
100004780: b9403329    	ldr	w9, [x25, #0x30]
100004784: 6b08013f    	cmp	w9, w8
100004788: 540000e0    	b.eq	0x1000047a4 <_zbtreeRank+0x2a8>
10000478c: d0000060    	adrp	x0, 0x100012000 <_strtoull+0x100012000>
100004790: 910a8800    	add	x0, x0, #0x2a2
100004794: 5280f4a1    	mov	w1, #0x7a5              ; =1957
100004798: d0000062    	adrp	x2, 0x100012000 <_strtoull+0x100012000>
10000479c: 910fec42    	add	x2, x2, #0x3fb
1000047a0: 940032c3    	bl	0x1000112ac <_standalone_panic>
1000047a4: f9402268    	ldr	x8, [x19, #0x40]
1000047a8: b4000128    	cbz	x8, 0x1000047cc <_zbtreeRank+0x2d0>
1000047ac: eb14011f    	cmp	x8, x20
1000047b0: 1a9f17e9    	cset	w9, eq
1000047b4: 79402f2a    	ldrh	w10, [x25, #0x16]
1000047b8: 79405908    	ldrh	w8, [x8, #0x2c]
1000047bc: 6b08015f    	cmp	w10, w8
1000047c0: 1a9f07e8    	cset	w8, ne
1000047c4: 6b08013f    	cmp	w9, w8
1000047c8: 54fff960    	b.eq	0x1000046f4 <_zbtreeRank+0x1f8>
1000047cc: d10153a5    	sub	x5, x29, #0x54
1000047d0: aa1903e0    	mov	x0, x25
1000047d4: a9448fe1    	ldp	x1, x3, [sp, #0x48]
1000047d8: a94393e2    	ldp	x2, x4, [sp, #0x38]
1000047dc: 94001837    	bl	0x10000a8b8 <_zbtScoreLeafFindMember>
1000047e0: 34fff8a0    	cbz	w0, 0x1000046f4 <_zbtreeRank+0x1f8>
1000047e4: 140000d1    	b	0x100004b28 <_zbtreeRank+0x62c>
1000047e8: b500021b    	cbnz	x27, 0x100004828 <_zbtreeRank+0x32c>
1000047ec: b9400a88    	ldr	w8, [x20, #0x8]
1000047f0: 51000508    	sub	w8, w8, #0x1
1000047f4: f94013e9    	ldr	x9, [sp, #0x20]
1000047f8: 8a090108    	and	x8, x8, x9
1000047fc: f9400289    	ldr	x9, [x20]
100004800: b940228a    	ldr	w10, [x20, #0x20]
100004804: 7100015f    	cmp	w10, #0x0
100004808: 5280060a    	mov	w10, #0x30              ; =48
10000480c: 5280040b    	mov	w11, #0x20              ; =32
100004810: 9a8a016a    	csel	x10, x11, x10, eq
100004814: 9ba82548    	umaddl	x8, w10, w8, x9
100004818: f9400508    	ldr	x8, [x8, #0x8]
10000481c: f9400fe9    	ldr	x9, [sp, #0x18]
100004820: ea28013f    	bics	xzr, x9, x8
100004824: 54000341    	b.ne	0x10000488c <_zbtreeRank+0x390>
100004828: f94002c8    	ldr	x8, [x22]
10000482c: 92401d09    	and	x9, x8, #0xff
100004830: 92781d0a    	and	x10, x8, #0xff00
100004834: 92701d0b    	and	x11, x8, #0xff0000
100004838: 92681d0c    	and	x12, x8, #0xff000000
10000483c: 92601d0d    	and	x13, x8, #0xff00000000
100004840: 92581d0e    	and	x14, x8, #0xff0000000000
100004844: 92501d0f    	and	x15, x8, #0xff000000000000
100004848: f100013f    	cmp	x9, #0x0
10000484c: fa401944    	ccmp	x10, #0x0, #0x4, ne
100004850: fa401964    	ccmp	x11, #0x0, #0x4, ne
100004854: fa401984    	ccmp	x12, #0x0, #0x4, ne
100004858: fa4019a4    	ccmp	x13, #0x0, #0x4, ne
10000485c: fa4019c4    	ccmp	x14, #0x0, #0x4, ne
100004860: fa4019e4    	ccmp	x15, #0x0, #0x4, ne
100004864: d378fd08    	lsr	x8, x8, #56
100004868: fa401904    	ccmp	x8, #0x0, #0x4, ne
10000486c: 54000100    	b.eq	0x10000488c <_zbtreeRank+0x390>
100004870: 91000788    	add	x8, x28, #0x1
100004874: f94017e9    	ldr	x9, [sp, #0x28]
100004878: 8a09011c    	and	x28, x8, x9
10000487c: 9100077b    	add	x27, x27, #0x1
100004880: f9400688    	ldr	x8, [x20, #0x8]
100004884: eb08037f    	cmp	x27, x8
100004888: 54fff063    	b.lo	0x100004694 <_zbtreeRank+0x198>
10000488c: f9401268    	ldr	x8, [x19, #0x20]
100004890: b40013a8    	cbz	x8, 0x100004b04 <_zbtreeRank+0x608>
100004894: d2800014    	mov	x20, #0x0               ; =0
100004898: 91006269    	add	x9, x19, #0x18
10000489c: f90017e9    	str	x9, [sp, #0x28]
1000048a0: f94027eb    	ldr	x11, [sp, #0x48]
1000048a4: 53187d69    	lsr	w9, w11, #24
1000048a8: d358fd6a    	lsr	x10, x11, #24
1000048ac: 7100013f    	cmp	w9, #0x0
1000048b0: 1a9f1549    	csinc	w9, w10, wzr, ne
1000048b4: d1000508    	sub	x8, x8, #0x1
1000048b8: 2a0b03ea    	mov	w10, w11
1000048bc: a901a3ea    	stp	x10, x8, [sp, #0x18]
1000048c0: 8a0a0118    	and	x24, x8, x10
1000048c4: 92401d28    	and	x8, x9, #0xff
1000048c8: b200c3ea    	mov	x10, #0x101010101010101 ; =72340172838076673
1000048cc: 9b0a7d0a    	mul	x10, x8, x10
1000048d0: f9001bea    	str	x10, [sp, #0x30]
1000048d4: d28f82aa    	mov	x10, #0x7c15            ; =31765
1000048d8: f2afe94a    	movk	x10, #0x7f4a, lsl #16
1000048dc: f2cf372a    	movk	x10, #0x79b9, lsl #32
1000048e0: f2f3c6ea    	movk	x10, #0x9e37, lsl #48
1000048e4: 9b0a7d08    	mul	x8, x8, x10
1000048e8: 5280002a    	mov	w10, #0x1               ; =1
1000048ec: 9ac9214b    	lsl	x11, x10, x9
1000048f0: d37afd0c    	lsr	x12, x8, #58
1000048f4: 9acc214c    	lsl	x12, x10, x12
1000048f8: aa0b018b    	orr	x11, x12, x11
1000048fc: d364fd08    	lsr	x8, x8, #36
100004900: 9ac82148    	lsl	x8, x10, x8
100004904: aa080168    	orr	x8, x11, x8
100004908: f9000be8    	str	x8, [sp, #0x10]
10000490c: 12001d36    	and	w22, w9, #0xff
100004910: 529ffffb    	mov	w27, #0xffff            ; =65535
100004914: d000007a    	adrp	x26, 0x100012000 <_strtoull+0x100012000>
100004918: 910a8b5a    	add	x26, x26, #0x2a2
10000491c: f9400e68    	ldr	x8, [x19, #0x18]
100004920: b9403a69    	ldr	w9, [x19, #0x38]
100004924: 7100013f    	cmp	w9, #0x0
100004928: 52800609    	mov	w9, #0x30               ; =48
10000492c: 5280040a    	mov	w10, #0x20              ; =32
100004930: 9a890149    	csel	x9, x10, x9, eq
100004934: 9b18213c    	madd	x28, x9, x24, x8
100004938: f9400388    	ldr	x8, [x28]
10000493c: f9401be9    	ldr	x9, [sp, #0x30]
100004940: ca090108    	eor	x8, x8, x9
100004944: b207dbe9    	mov	x9, #-0x101010101010102 ; =-72340172838076674
100004948: f29fdfe9    	movk	x9, #0xfeff
10000494c: 8b090109    	add	x9, x8, x9
100004950: 8a280128    	bic	x8, x9, x8
100004954: f201c115    	ands	x21, x8, #0x8080808080808080
100004958: 54000840    	b.eq	0x100004a60 <_zbtreeRank+0x564>
10000495c: 91004397    	add	x23, x28, #0x10
100004960: 14000006    	b	0x100004978 <_zbtreeRank+0x47c>
100004964: f9402268    	ldr	x8, [x19, #0x40]
100004968: b4000708    	cbz	x8, 0x100004a48 <_zbtreeRank+0x54c>
10000496c: d10006a8    	sub	x8, x21, #0x1
100004970: ea150115    	ands	x21, x8, x21
100004974: 54000760    	b.eq	0x100004a60 <_zbtreeRank+0x564>
100004978: dac002a8    	rbit	x8, x21
10000497c: dac01108    	clz	x8, x8
100004980: f9400389    	ldr	x9, [x28]
100004984: 927d090a    	and	x10, x8, #0x38
100004988: 9aca2529    	lsr	x9, x9, x10
10000498c: 6b2902df    	cmp	w22, w9, uxtb
100004990: 54fffee1    	b.ne	0x10000496c <_zbtreeRank+0x470>
100004994: d343fd08    	lsr	x8, x8, #3
100004998: b9403a69    	ldr	w9, [x19, #0x38]
10000499c: 340000a9    	cbz	w9, 0x1000049b0 <_zbtreeRank+0x4b4>
1000049a0: b8687ae8    	ldr	w8, [x23, x8, lsl #2]
1000049a4: 3100051f    	cmn	w8, #0x1
1000049a8: 540000a1    	b.ne	0x1000049bc <_zbtreeRank+0x4c0>
1000049ac: 17fffff0    	b	0x10000496c <_zbtreeRank+0x470>
1000049b0: 78687ae8    	ldrh	w8, [x23, x8, lsl #1]
1000049b4: 6b1b011f    	cmp	w8, w27
1000049b8: 54fffda0    	b.eq	0x10000496c <_zbtreeRank+0x470>
1000049bc: b9405669    	ldr	w9, [x19, #0x54]
1000049c0: 6b09011f    	cmp	w8, w9
1000049c4: 54fffd02    	b.hs	0x100004964 <_zbtreeRank+0x468>
1000049c8: f9402669    	ldr	x9, [x19, #0x48]
1000049cc: f8685939    	ldr	x25, [x9, w8, uxtw #3]
1000049d0: 92400329    	and	x9, x25, #0x1
1000049d4: f100033f    	cmp	x25, #0x0
1000049d8: fa401920    	ccmp	x9, #0x0, #0x0, ne
1000049dc: 54fffc41    	b.ne	0x100004964 <_zbtreeRank+0x468>
1000049e0: b9403329    	ldr	w9, [x25, #0x30]
1000049e4: 6b08013f    	cmp	w9, w8
1000049e8: 540000c0    	b.eq	0x100004a00 <_zbtreeRank+0x504>
1000049ec: aa1a03e0    	mov	x0, x26
1000049f0: 5280f4a1    	mov	w1, #0x7a5              ; =1957
1000049f4: d0000062    	adrp	x2, 0x100012000 <_strtoull+0x100012000>
1000049f8: 910fec42    	add	x2, x2, #0x3fb
1000049fc: 9400322c    	bl	0x1000112ac <_standalone_panic>
100004a00: f9402268    	ldr	x8, [x19, #0x40]
100004a04: b4000148    	cbz	x8, 0x100004a2c <_zbtreeRank+0x530>
100004a08: f94017e9    	ldr	x9, [sp, #0x28]
100004a0c: eb09011f    	cmp	x8, x9
100004a10: 1a9f17e9    	cset	w9, eq
100004a14: 79402f2a    	ldrh	w10, [x25, #0x16]
100004a18: 79405908    	ldrh	w8, [x8, #0x2c]
100004a1c: 6b08015f    	cmp	w10, w8
100004a20: 1a9f07e8    	cset	w8, ne
100004a24: 6b08013f    	cmp	w9, w8
100004a28: 54fffa20    	b.eq	0x10000496c <_zbtreeRank+0x470>
100004a2c: d10153a5    	sub	x5, x29, #0x54
100004a30: aa1903e0    	mov	x0, x25
100004a34: a9448fe1    	ldp	x1, x3, [sp, #0x48]
100004a38: a94393e2    	ldp	x2, x4, [sp, #0x38]
100004a3c: 9400179f    	bl	0x10000a8b8 <_zbtScoreLeafFindMember>
100004a40: 34fff960    	cbz	w0, 0x10000496c <_zbtreeRank+0x470>
100004a44: 14000039    	b	0x100004b28 <_zbtreeRank+0x62c>
100004a48: aa1a03e0    	mov	x0, x26
100004a4c: 5280f421    	mov	w1, #0x7a1              ; =1953
100004a50: d0000062    	adrp	x2, 0x100012000 <_strtoull+0x100012000>
100004a54: 91106842    	add	x2, x2, #0x41a
100004a58: 94003215    	bl	0x1000112ac <_standalone_panic>
100004a5c: 17ffffc4    	b	0x10000496c <_zbtreeRank+0x470>
100004a60: b5000214    	cbnz	x20, 0x100004aa0 <_zbtreeRank+0x5a4>
100004a64: b9402268    	ldr	w8, [x19, #0x20]
100004a68: 51000508    	sub	w8, w8, #0x1
100004a6c: f9400fe9    	ldr	x9, [sp, #0x18]
100004a70: 8a090108    	and	x8, x8, x9
100004a74: f9400e69    	ldr	x9, [x19, #0x18]
100004a78: b9403a6a    	ldr	w10, [x19, #0x38]
100004a7c: 7100015f    	cmp	w10, #0x0
100004a80: 5280060a    	mov	w10, #0x30              ; =48
100004a84: 5280040b    	mov	w11, #0x20              ; =32
100004a88: 9a8a016a    	csel	x10, x11, x10, eq
100004a8c: 9ba82548    	umaddl	x8, w10, w8, x9
100004a90: f9400508    	ldr	x8, [x8, #0x8]
100004a94: f9400be9    	ldr	x9, [sp, #0x10]
100004a98: ea28013f    	bics	xzr, x9, x8
100004a9c: 54000341    	b.ne	0x100004b04 <_zbtreeRank+0x608>
100004aa0: f9400388    	ldr	x8, [x28]
100004aa4: 92401d09    	and	x9, x8, #0xff
100004aa8: 92781d0a    	and	x10, x8, #0xff00
100004aac: 92701d0b    	and	x11, x8, #0xff0000
100004ab0: 92681d0c    	and	x12, x8, #0xff000000
100004ab4: 92601d0d    	and	x13, x8, #0xff00000000
100004ab8: 92581d0e    	and	x14, x8, #0xff0000000000
100004abc: 92501d0f    	and	x15, x8, #0xff000000000000
100004ac0: f100013f    	cmp	x9, #0x0
100004ac4: fa401944    	ccmp	x10, #0x0, #0x4, ne
100004ac8: fa401964    	ccmp	x11, #0x0, #0x4, ne
100004acc: fa401984    	ccmp	x12, #0x0, #0x4, ne
100004ad0: fa4019a4    	ccmp	x13, #0x0, #0x4, ne
100004ad4: fa4019c4    	ccmp	x14, #0x0, #0x4, ne
100004ad8: fa4019e4    	ccmp	x15, #0x0, #0x4, ne
100004adc: d378fd08    	lsr	x8, x8, #56
100004ae0: fa401904    	ccmp	x8, #0x0, #0x4, ne
100004ae4: 54000100    	b.eq	0x100004b04 <_zbtreeRank+0x608>
100004ae8: 91000708    	add	x8, x24, #0x1
100004aec: f94013e9    	ldr	x9, [sp, #0x20]
100004af0: 8a090118    	and	x24, x8, x9
100004af4: 91000694    	add	x20, x20, #0x1
100004af8: f9401268    	ldr	x8, [x19, #0x20]
100004afc: eb08029f    	cmp	x20, x8
100004b00: 54fff0e3    	b.lo	0x10000491c <_zbtreeRank+0x420>
100004b04: 92800000    	mov	x0, #-0x1               ; =-1
100004b08: a94b7bfd    	ldp	x29, x30, [sp, #0xb0]
100004b0c: a94a4ff4    	ldp	x20, x19, [sp, #0xa0]
100004b10: a94957f6    	ldp	x22, x21, [sp, #0x90]
100004b14: a9485ff8    	ldp	x24, x23, [sp, #0x80]
100004b18: a94767fa    	ldp	x26, x25, [sp, #0x70]
100004b1c: a9466ffc    	ldp	x28, x27, [sp, #0x60]
100004b20: 910303ff    	add	sp, sp, #0xc0
100004b24: d65f03c0    	ret
100004b28: b85ac3a0    	ldur	w0, [x29, #-0x54]
100004b2c: f9400329    	ldr	x9, [x25]
100004b30: b4000589    	cbz	x9, 0x100004be0 <_zbtreeRank+0x6e4>
100004b34: b9400fec    	ldr	w12, [sp, #0xc]
100004b38: 14000003    	b	0x100004b44 <_zbtreeRank+0x648>
100004b3c: f9400329    	ldr	x9, [x25]
100004b40: b4000529    	cbz	x9, 0x100004be4 <_zbtreeRank+0x6e8>
100004b44: 39404328    	ldrb	w8, [x25, #0x10]
100004b48: aa0903f9    	mov	x25, x9
100004b4c: 34ffff88    	cbz	w8, 0x100004b3c <_zbtreeRank+0x640>
100004b50: 7100211f    	cmp	w8, #0x8
100004b54: 54000062    	b.hs	0x100004b60 <_zbtreeRank+0x664>
100004b58: d2800009    	mov	x9, #0x0                ; =0
100004b5c: 14000019    	b	0x100004bc0 <_zbtreeRank+0x6c4>
100004b60: 927d1109    	and	x9, x8, #0xf8
100004b64: 6f00e400    	movi.2d	v0, #0000000000000000
100004b68: 6f00e401    	movi.2d	v1, #0000000000000000
100004b6c: 4e081c01    	mov.d	v1[0], x0
100004b70: 9105232a    	add	x10, x25, #0x148
100004b74: aa0903eb    	mov	x11, x9
100004b78: 6f00e402    	movi.2d	v2, #0000000000000000
100004b7c: 6f00e403    	movi.2d	v3, #0000000000000000
100004b80: ad7e9544    	ldp	q4, q5, [x10, #-0x30]
100004b84: ad7f9d46    	ldp	q6, q7, [x10, #-0x10]
100004b88: 4ee18481    	add.2d	v1, v4, v1
100004b8c: 4ee084a0    	add.2d	v0, v5, v0
100004b90: 4ee284c2    	add.2d	v2, v6, v2
100004b94: 4ee384e3    	add.2d	v3, v7, v3
100004b98: 9101014a    	add	x10, x10, #0x40
100004b9c: f100216b    	subs	x11, x11, #0x8
100004ba0: 54ffff01    	b.ne	0x100004b80 <_zbtreeRank+0x684>
100004ba4: 4ee18400    	add.2d	v0, v0, v1
100004ba8: 4ee08440    	add.2d	v0, v2, v0
100004bac: 4ee08460    	add.2d	v0, v3, v0
100004bb0: 5ef1b800    	addp.2d	d0, v0
100004bb4: 9e660000    	fmov	x0, d0
100004bb8: eb08013f    	cmp	x9, x8
100004bbc: 54fffc00    	b.eq	0x100004b3c <_zbtreeRank+0x640>
100004bc0: cb090108    	sub	x8, x8, x9
100004bc4: 8b090f29    	add	x9, x25, x9, lsl #3
100004bc8: 91046129    	add	x9, x9, #0x118
100004bcc: f840852a    	ldr	x10, [x9], #0x8
100004bd0: 8b000140    	add	x0, x10, x0
100004bd4: f1000508    	subs	x8, x8, #0x1
100004bd8: 54ffffa1    	b.ne	0x100004bcc <_zbtreeRank+0x6d0>
100004bdc: 17ffffd8    	b	0x100004b3c <_zbtreeRank+0x640>
100004be0: b9400fec    	ldr	w12, [sp, #0xc]
100004be4: 34fff92c    	cbz	w12, 0x100004b08 <_zbtreeRank+0x60c>
100004be8: f9403268    	ldr	x8, [x19, #0x60]
100004bec: aa2003e9    	mvn	x9, x0
100004bf0: 8b090100    	add	x0, x8, x9
100004bf4: 17ffffc5    	b	0x100004b08 <_zbtreeRank+0x60c>
