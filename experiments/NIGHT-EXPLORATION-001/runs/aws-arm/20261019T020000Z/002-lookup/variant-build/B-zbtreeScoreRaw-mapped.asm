
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/build/B-mapped:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

0000000000003500 <zbtreeScoreRaw>:
    3500:	d10283ff 	sub	sp, sp, #0xa0
    3504:	a9047bfd 	stp	x29, x30, [sp, #64]
    3508:	a9056ffc 	stp	x28, x27, [sp, #80]
    350c:	a90667fa 	stp	x26, x25, [sp, #96]
    3510:	a9075ff8 	stp	x24, x23, [sp, #112]
    3514:	a90857f6 	stp	x22, x21, [sp, #128]
    3518:	a9094ff4 	stp	x20, x19, [sp, #144]
    351c:	910103fd 	add	x29, sp, #0x40
    3520:	aa0003f6 	mov	x22, x0
    3524:	f90013e1 	str	x1, [sp, #32]
    3528:	aa0103e0 	mov	x0, x1
    352c:	aa0203e1 	mov	x1, x2
    3530:	a93e8fa2 	stp	x2, x3, [x29, #-24]
    3534:	9400359e 	bl	10bac <dictGenHashFunction>
    3538:	f94022c8 	ldr	x8, [x22, #64]
    353c:	f81f83a0 	stur	x0, [x29, #-8]
    3540:	b40013e8 	cbz	x8, 37bc <zbtreeScoreRaw+0x2bc>
    3544:	aa1603e0 	mov	x0, x22
    3548:	52800021 	mov	w1, #0x1                   	// #1
    354c:	94000ee2 	bl	70d4 <zbtIndexRehashStep>
    3550:	f94022dc 	ldr	x28, [x22, #64]
    3554:	b400135c 	cbz	x28, 37bc <zbtreeScoreRaw+0x2bc>
    3558:	f9400788 	ldr	x8, [x28, #8]
    355c:	b4001308 	cbz	x8, 37bc <zbtreeScoreRaw+0x2bc>
    3560:	f85f83ac 	ldur	x12, [x29, #-8]
    3564:	d1000517 	sub	x23, x8, #0x1
    3568:	b200c3e8 	mov	x8, #0x101010101010101     	// #72340172838076673
    356c:	aa1f03f9 	mov	x25, xzr
    3570:	910062da 	add	x26, x22, #0x18
    3574:	529ffff3 	mov	w19, #0xffff                	// #65535
    3578:	53187d89 	lsr	w9, w12, #24
    357c:	d358fd8a 	lsr	x10, x12, #24
    3580:	92407d8e 	and	x14, x12, #0xffffffff
    3584:	5280002c 	mov	w12, #0x1                   	// #1
    3588:	8a0e02f8 	and	x24, x23, x14
    358c:	7100013f 	cmp	w9, #0x0
    3590:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    3594:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    3598:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    359c:	92401d2b 	and	x11, x9, #0xff
    35a0:	9ac92189 	lsl	x9, x12, x9
    35a4:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    35a8:	9b087d68 	mul	x8, x11, x8
    35ac:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    35b0:	9b0a7d6a 	mul	x10, x11, x10
    35b4:	a90123ee 	stp	x14, x8, [sp, #16]
    35b8:	d37afd4d 	lsr	x13, x10, #58
    35bc:	d364fd4a 	lsr	x10, x10, #36
    35c0:	9acd2188 	lsl	x8, x12, x13
    35c4:	9aca218a 	lsl	x10, x12, x10
    35c8:	aa090108 	orr	x8, x8, x9
    35cc:	aa0a0108 	orr	x8, x8, x10
    35d0:	f90007e8 	str	x8, [sp, #8]
    35d4:	b9402388 	ldr	w8, [x28, #32]
    35d8:	52800409 	mov	w9, #0x20                  	// #32
    35dc:	7100011f 	cmp	w8, #0x0
    35e0:	52800608 	mov	w8, #0x30                  	// #48
    35e4:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    35e8:	f9400389 	ldr	x9, [x28]
    35ec:	9b182514 	madd	x20, x8, x24, x9
    35f0:	f9400fe9 	ldr	x9, [sp, #24]
    35f4:	f9400288 	ldr	x8, [x20]
    35f8:	ca090108 	eor	x8, x8, x9
    35fc:	b201c3e9 	mov	x9, #0x8080808080808080    	// #-9187201950435737472
    3600:	aa481108 	orr	x8, x8, x8, lsr #4
    3604:	aa480908 	orr	x8, x8, x8, lsr #2
    3608:	aa480508 	orr	x8, x8, x8, lsr #1
    360c:	ea281d35 	bics	x21, x9, x8, lsl #7
    3610:	54000661 	b.ne	36dc <zbtreeScoreRaw+0x1dc>  // b.any
    3614:	b5000219 	cbnz	x25, 3654 <zbtreeScoreRaw+0x154>
    3618:	b9402389 	ldr	w9, [x28, #32]
    361c:	b9400b88 	ldr	w8, [x28, #8]
    3620:	5280040a 	mov	w10, #0x20                  	// #32
    3624:	7100013f 	cmp	w9, #0x0
    3628:	f9400be9 	ldr	x9, [sp, #16]
    362c:	51000508 	sub	w8, w8, #0x1
    3630:	8a090108 	and	x8, x8, x9
    3634:	52800609 	mov	w9, #0x30                  	// #48
    3638:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    363c:	f940038a 	ldr	x10, [x28]
    3640:	9ba82928 	umaddl	x8, w9, w8, x10
    3644:	f94007e9 	ldr	x9, [sp, #8]
    3648:	f9400508 	ldr	x8, [x8, #8]
    364c:	ea28013f 	bics	xzr, x9, x8
    3650:	54000b61 	b.ne	37bc <zbtreeScoreRaw+0x2bc>  // b.any
    3654:	f9400288 	ldr	x8, [x20]
    3658:	92401d09 	and	x9, x8, #0xff
    365c:	92781d0a 	and	x10, x8, #0xff00
    3660:	f100013f 	cmp	x9, #0x0
    3664:	92701d09 	and	x9, x8, #0xff0000
    3668:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    366c:	92681d0a 	and	x10, x8, #0xff000000
    3670:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3674:	92601d09 	and	x9, x8, #0xff00000000
    3678:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    367c:	92581d0a 	and	x10, x8, #0xff0000000000
    3680:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3684:	92501d09 	and	x9, x8, #0xff000000000000
    3688:	d378fd08 	lsr	x8, x8, #56
    368c:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3690:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3694:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    3698:	54000920 	b.eq	37bc <zbtreeScoreRaw+0x2bc>  // b.none
    369c:	f9400788 	ldr	x8, [x28, #8]
    36a0:	91000739 	add	x25, x25, #0x1
    36a4:	91000709 	add	x9, x24, #0x1
    36a8:	8a170138 	and	x24, x9, x23
    36ac:	eb08033f 	cmp	x25, x8
    36b0:	54fff923 	b.cc	35d4 <zbtreeScoreRaw+0xd4>  // b.lo, b.ul, b.last
    36b4:	14000042 	b	37bc <zbtreeScoreRaw+0x2bc>
    36b8:	d0000060 	adrp	x0, 11000 <siphash_nocase+0x24>
    36bc:	91230400 	add	x0, x0, #0x8c1
    36c0:	5280f4e1 	mov	w1, #0x7a7                 	// #1959
    36c4:	d0000062 	adrp	x2, 11000 <siphash_nocase+0x24>
    36c8:	9128e442 	add	x2, x2, #0xa39
    36cc:	940034a0 	bl	1094c <standalone_panic>
    36d0:	d10006a8 	sub	x8, x21, #0x1
    36d4:	ea150115 	ands	x21, x8, x21
    36d8:	54fff9e0 	b.eq	3614 <zbtreeScoreRaw+0x114>  // b.none
    36dc:	dac002a8 	rbit	x8, x21
    36e0:	b9402389 	ldr	w9, [x28, #32]
    36e4:	dac01108 	clz	x8, x8
    36e8:	d343fd08 	lsr	x8, x8, #3
    36ec:	340000c9 	cbz	w9, 3704 <zbtreeScoreRaw+0x204>
    36f0:	8b080a88 	add	x8, x20, x8, lsl #2
    36f4:	b9401108 	ldr	w8, [x8, #16]
    36f8:	3100051f 	cmn	w8, #0x1
    36fc:	540000c1 	b.ne	3714 <zbtreeScoreRaw+0x214>  // b.any
    3700:	17fffff4 	b	36d0 <zbtreeScoreRaw+0x1d0>
    3704:	8b080688 	add	x8, x20, x8, lsl #1
    3708:	79402108 	ldrh	w8, [x8, #16]
    370c:	6b13011f 	cmp	w8, w19
    3710:	54fffe00 	b.eq	36d0 <zbtreeScoreRaw+0x1d0>  // b.none
    3714:	b94056c9 	ldr	w9, [x22, #84]
    3718:	6b09011f 	cmp	w8, w9
    371c:	540000e2 	b.cs	3738 <zbtreeScoreRaw+0x238>  // b.hs, b.nlast
    3720:	f94026c9 	ldr	x9, [x22, #72]
    3724:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3728:	92400369 	and	x9, x27, #0x1
    372c:	f100037f 	cmp	x27, #0x0
    3730:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    3734:	540000c0 	b.eq	374c <zbtreeScoreRaw+0x24c>  // b.none
    3738:	f94022c8 	ldr	x8, [x22, #64]
    373c:	b4fffbe8 	cbz	x8, 36b8 <zbtreeScoreRaw+0x1b8>
    3740:	eb1c035f 	cmp	x26, x28
    3744:	54fffc60 	b.eq	36d0 <zbtreeScoreRaw+0x1d0>  // b.none
    3748:	17ffffdc 	b	36b8 <zbtreeScoreRaw+0x1b8>
    374c:	b9403369 	ldr	w9, [x27, #48]
    3750:	6b08013f 	cmp	w9, w8
    3754:	540000e0 	b.eq	3770 <zbtreeScoreRaw+0x270>  // b.none
    3758:	d0000060 	adrp	x0, 11000 <siphash_nocase+0x24>
    375c:	91230400 	add	x0, x0, #0x8c1
    3760:	5280f561 	mov	w1, #0x7ab                 	// #1963
    3764:	d0000062 	adrp	x2, 11000 <siphash_nocase+0x24>
    3768:	91286842 	add	x2, x2, #0xa1a
    376c:	94003478 	bl	1094c <standalone_panic>
    3770:	f94022c8 	ldr	x8, [x22, #64]
    3774:	b4000128 	cbz	x8, 3798 <zbtreeScoreRaw+0x298>
    3778:	79402f69 	ldrh	w9, [x27, #22]
    377c:	7940590a 	ldrh	w10, [x8, #44]
    3780:	eb1c011f 	cmp	x8, x28
    3784:	1a9f17e8 	cset	w8, eq	// eq = none
    3788:	6b0a013f 	cmp	w9, w10
    378c:	1a9f07e9 	cset	w9, ne	// ne = any
    3790:	6b09011f 	cmp	w8, w9
    3794:	54fff9e0 	b.eq	36d0 <zbtreeScoreRaw+0x1d0>  // b.none
    3798:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    379c:	aa1b03e0 	mov	x0, x27
    37a0:	f94013e2 	ldr	x2, [sp, #32]
    37a4:	f85e83a3 	ldur	x3, [x29, #-24]
    37a8:	aa1f03e5 	mov	x5, xzr
    37ac:	94001d8a 	bl	add4 <zbtScoreLeafFindMember>
    37b0:	34fff900 	cbz	w0, 36d0 <zbtreeScoreRaw+0x1d0>
    37b4:	52800020 	mov	w0, #0x1                   	// #1
    37b8:	1400009a 	b	3a20 <zbtreeScoreRaw+0x520>
    37bc:	f94012c8 	ldr	x8, [x22, #32]
    37c0:	b40012e8 	cbz	x8, 3a1c <zbtreeScoreRaw+0x51c>
    37c4:	f85f83ac 	ldur	x12, [x29, #-8]
    37c8:	d100050e 	sub	x14, x8, #0x1
    37cc:	b200c3e8 	mov	x8, #0x101010101010101     	// #72340172838076673
    37d0:	aa1f03fc 	mov	x28, xzr
    37d4:	910062d9 	add	x25, x22, #0x18
    37d8:	d0000078 	adrp	x24, 11000 <siphash_nocase+0x24>
    37dc:	91230718 	add	x24, x24, #0x8c1
    37e0:	53187d89 	lsr	w9, w12, #24
    37e4:	d358fd8a 	lsr	x10, x12, #24
    37e8:	92407d8f 	and	x15, x12, #0xffffffff
    37ec:	5280002c 	mov	w12, #0x1                   	// #1
    37f0:	529ffff4 	mov	w20, #0xffff                	// #65535
    37f4:	7100013f 	cmp	w9, #0x0
    37f8:	8a0f01d3 	and	x19, x14, x15
    37fc:	d000007a 	adrp	x26, 11000 <siphash_nocase+0x24>
    3800:	9128e75a 	add	x26, x26, #0xa39
    3804:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    3808:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    380c:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    3810:	92401d2b 	and	x11, x9, #0xff
    3814:	9ac92189 	lsl	x9, x12, x9
    3818:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    381c:	9b087d68 	mul	x8, x11, x8
    3820:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    3824:	9b0a7d6a 	mul	x10, x11, x10
    3828:	a90123ee 	stp	x14, x8, [sp, #16]
    382c:	d37afd4d 	lsr	x13, x10, #58
    3830:	d364fd4a 	lsr	x10, x10, #36
    3834:	9acd2188 	lsl	x8, x12, x13
    3838:	9aca218a 	lsl	x10, x12, x10
    383c:	aa090108 	orr	x8, x8, x9
    3840:	aa0a0108 	orr	x8, x8, x10
    3844:	a9003fe8 	stp	x8, x15, [sp]
    3848:	b9403ac8 	ldr	w8, [x22, #56]
    384c:	52800409 	mov	w9, #0x20                  	// #32
    3850:	7100011f 	cmp	w8, #0x0
    3854:	52800608 	mov	w8, #0x30                  	// #48
    3858:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    385c:	f9400ec9 	ldr	x9, [x22, #24]
    3860:	9b132515 	madd	x21, x8, x19, x9
    3864:	f9400fe9 	ldr	x9, [sp, #24]
    3868:	f94002a8 	ldr	x8, [x21]
    386c:	ca090108 	eor	x8, x8, x9
    3870:	b201c3e9 	mov	x9, #0x8080808080808080    	// #-9187201950435737472
    3874:	aa481108 	orr	x8, x8, x8, lsr #4
    3878:	aa480908 	orr	x8, x8, x8, lsr #2
    387c:	aa480508 	orr	x8, x8, x8, lsr #1
    3880:	ea281d37 	bics	x23, x9, x8, lsl #7
    3884:	54000601 	b.ne	3944 <zbtreeScoreRaw+0x444>  // b.any
    3888:	b500021c 	cbnz	x28, 38c8 <zbtreeScoreRaw+0x3c8>
    388c:	b9403ac9 	ldr	w9, [x22, #56]
    3890:	b94022c8 	ldr	w8, [x22, #32]
    3894:	5280040a 	mov	w10, #0x20                  	// #32
    3898:	7100013f 	cmp	w9, #0x0
    389c:	f94007e9 	ldr	x9, [sp, #8]
    38a0:	51000508 	sub	w8, w8, #0x1
    38a4:	8a090108 	and	x8, x8, x9
    38a8:	52800609 	mov	w9, #0x30                  	// #48
    38ac:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    38b0:	f9400eca 	ldr	x10, [x22, #24]
    38b4:	9ba82928 	umaddl	x8, w9, w8, x10
    38b8:	f94003e9 	ldr	x9, [sp]
    38bc:	f9400508 	ldr	x8, [x8, #8]
    38c0:	ea28013f 	bics	xzr, x9, x8
    38c4:	54000ac1 	b.ne	3a1c <zbtreeScoreRaw+0x51c>  // b.any
    38c8:	f94002a8 	ldr	x8, [x21]
    38cc:	92401d09 	and	x9, x8, #0xff
    38d0:	92781d0a 	and	x10, x8, #0xff00
    38d4:	f100013f 	cmp	x9, #0x0
    38d8:	92701d09 	and	x9, x8, #0xff0000
    38dc:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38e0:	92681d0a 	and	x10, x8, #0xff000000
    38e4:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38e8:	92601d09 	and	x9, x8, #0xff00000000
    38ec:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38f0:	92581d0a 	and	x10, x8, #0xff0000000000
    38f4:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38f8:	92501d09 	and	x9, x8, #0xff000000000000
    38fc:	d378fd08 	lsr	x8, x8, #56
    3900:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3904:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3908:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    390c:	54000880 	b.eq	3a1c <zbtreeScoreRaw+0x51c>  // b.none
    3910:	f94012c8 	ldr	x8, [x22, #32]
    3914:	9100079c 	add	x28, x28, #0x1
    3918:	91000669 	add	x9, x19, #0x1
    391c:	eb08039f 	cmp	x28, x8
    3920:	f9400be8 	ldr	x8, [sp, #16]
    3924:	8a080133 	and	x19, x9, x8
    3928:	54fff903 	b.cc	3848 <zbtreeScoreRaw+0x348>  // b.lo, b.ul, b.last
    392c:	1400003c 	b	3a1c <zbtreeScoreRaw+0x51c>
    3930:	f94022c8 	ldr	x8, [x22, #64]
    3934:	b40006a8 	cbz	x8, 3a08 <zbtreeScoreRaw+0x508>
    3938:	d10006e8 	sub	x8, x23, #0x1
    393c:	ea170117 	ands	x23, x8, x23
    3940:	54fffa40 	b.eq	3888 <zbtreeScoreRaw+0x388>  // b.none
    3944:	dac002e8 	rbit	x8, x23
    3948:	b9403ac9 	ldr	w9, [x22, #56]
    394c:	dac01108 	clz	x8, x8
    3950:	d343fd08 	lsr	x8, x8, #3
    3954:	340000c9 	cbz	w9, 396c <zbtreeScoreRaw+0x46c>
    3958:	8b080aa8 	add	x8, x21, x8, lsl #2
    395c:	b9401108 	ldr	w8, [x8, #16]
    3960:	3100051f 	cmn	w8, #0x1
    3964:	540000c1 	b.ne	397c <zbtreeScoreRaw+0x47c>  // b.any
    3968:	17fffff4 	b	3938 <zbtreeScoreRaw+0x438>
    396c:	8b0806a8 	add	x8, x21, x8, lsl #1
    3970:	79402108 	ldrh	w8, [x8, #16]
    3974:	6b14011f 	cmp	w8, w20
    3978:	54fffe00 	b.eq	3938 <zbtreeScoreRaw+0x438>  // b.none
    397c:	b94056c9 	ldr	w9, [x22, #84]
    3980:	6b09011f 	cmp	w8, w9
    3984:	54fffd62 	b.cs	3930 <zbtreeScoreRaw+0x430>  // b.hs, b.nlast
    3988:	f94026c9 	ldr	x9, [x22, #72]
    398c:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3990:	92400369 	and	x9, x27, #0x1
    3994:	f100037f 	cmp	x27, #0x0
    3998:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    399c:	54fffca1 	b.ne	3930 <zbtreeScoreRaw+0x430>  // b.any
    39a0:	b9403369 	ldr	w9, [x27, #48]
    39a4:	6b08013f 	cmp	w9, w8
    39a8:	540000c0 	b.eq	39c0 <zbtreeScoreRaw+0x4c0>  // b.none
    39ac:	aa1803e0 	mov	x0, x24
    39b0:	5280f561 	mov	w1, #0x7ab                 	// #1963
    39b4:	d0000062 	adrp	x2, 11000 <siphash_nocase+0x24>
    39b8:	91286842 	add	x2, x2, #0xa1a
    39bc:	940033e4 	bl	1094c <standalone_panic>
    39c0:	f94022c8 	ldr	x8, [x22, #64]
    39c4:	b4000128 	cbz	x8, 39e8 <zbtreeScoreRaw+0x4e8>
    39c8:	79402f69 	ldrh	w9, [x27, #22]
    39cc:	7940590a 	ldrh	w10, [x8, #44]
    39d0:	eb19011f 	cmp	x8, x25
    39d4:	1a9f17e8 	cset	w8, eq	// eq = none
    39d8:	6b0a013f 	cmp	w9, w10
    39dc:	1a9f07e9 	cset	w9, ne	// ne = any
    39e0:	6b09011f 	cmp	w8, w9
    39e4:	54fffaa0 	b.eq	3938 <zbtreeScoreRaw+0x438>  // b.none
    39e8:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    39ec:	aa1b03e0 	mov	x0, x27
    39f0:	f94013e2 	ldr	x2, [sp, #32]
    39f4:	f85e83a3 	ldur	x3, [x29, #-24]
    39f8:	aa1f03e5 	mov	x5, xzr
    39fc:	94001cf6 	bl	add4 <zbtScoreLeafFindMember>
    3a00:	34fff9c0 	cbz	w0, 3938 <zbtreeScoreRaw+0x438>
    3a04:	17ffff6c 	b	37b4 <zbtreeScoreRaw+0x2b4>
    3a08:	aa1803e0 	mov	x0, x24
    3a0c:	5280f4e1 	mov	w1, #0x7a7                 	// #1959
    3a10:	aa1a03e2 	mov	x2, x26
    3a14:	940033ce 	bl	1094c <standalone_panic>
    3a18:	17ffffc8 	b	3938 <zbtreeScoreRaw+0x438>
    3a1c:	2a1f03e0 	mov	w0, wzr
    3a20:	a9494ff4 	ldp	x20, x19, [sp, #144]
    3a24:	a94857f6 	ldp	x22, x21, [sp, #128]
    3a28:	a9475ff8 	ldp	x24, x23, [sp, #112]
    3a2c:	a94667fa 	ldp	x26, x25, [sp, #96]
    3a30:	a9456ffc 	ldp	x28, x27, [sp, #80]
    3a34:	a9447bfd 	ldp	x29, x30, [sp, #64]
    3a38:	910283ff 	add	sp, sp, #0xa0
    3a3c:	d65f03c0 	ret

Disassembly of section .fini:
