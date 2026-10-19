
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/build/A-mapped:     file format elf64-littleaarch64


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
    3534:	940035a8 	bl	10bd4 <dictGenHashFunction>
    3538:	f94022c8 	ldr	x8, [x22, #64]
    353c:	f81f83a0 	stur	x0, [x29, #-8]
    3540:	b4001408 	cbz	x8, 37c0 <zbtreeScoreRaw+0x2c0>
    3544:	aa1603e0 	mov	x0, x22
    3548:	52800021 	mov	w1, #0x1                   	// #1
    354c:	94000eec 	bl	70fc <zbtIndexRehashStep>
    3550:	f94022dc 	ldr	x28, [x22, #64]
    3554:	b400137c 	cbz	x28, 37c0 <zbtreeScoreRaw+0x2c0>
    3558:	f9400788 	ldr	x8, [x28, #8]
    355c:	b4001328 	cbz	x8, 37c0 <zbtreeScoreRaw+0x2c0>
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
    35dc:	b200dbea 	mov	x10, #0x7f7f7f7f7f7f7f7f    	// #9187201950435737471
    35e0:	7100011f 	cmp	w8, #0x0
    35e4:	52800608 	mov	w8, #0x30                  	// #48
    35e8:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    35ec:	f9400389 	ldr	x9, [x28]
    35f0:	9b182514 	madd	x20, x8, x24, x9
    35f4:	f9400fe9 	ldr	x9, [sp, #24]
    35f8:	f9400288 	ldr	x8, [x20]
    35fc:	ca090108 	eor	x8, x8, x9
    3600:	9200d909 	and	x9, x8, #0x7f7f7f7f7f7f7f7f
    3604:	8b0a0129 	add	x9, x9, x10
    3608:	aa080128 	orr	x8, x9, x8
    360c:	b201c3e9 	mov	x9, #0x8080808080808080    	// #-9187201950435737472
    3610:	ea280135 	bics	x21, x9, x8
    3614:	54000661 	b.ne	36e0 <zbtreeScoreRaw+0x1e0>  // b.any
    3618:	b5000219 	cbnz	x25, 3658 <zbtreeScoreRaw+0x158>
    361c:	b9402389 	ldr	w9, [x28, #32]
    3620:	b9400b88 	ldr	w8, [x28, #8]
    3624:	5280040a 	mov	w10, #0x20                  	// #32
    3628:	7100013f 	cmp	w9, #0x0
    362c:	f9400be9 	ldr	x9, [sp, #16]
    3630:	51000508 	sub	w8, w8, #0x1
    3634:	8a090108 	and	x8, x8, x9
    3638:	52800609 	mov	w9, #0x30                  	// #48
    363c:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    3640:	f940038a 	ldr	x10, [x28]
    3644:	9ba82928 	umaddl	x8, w9, w8, x10
    3648:	f94007e9 	ldr	x9, [sp, #8]
    364c:	f9400508 	ldr	x8, [x8, #8]
    3650:	ea28013f 	bics	xzr, x9, x8
    3654:	54000b61 	b.ne	37c0 <zbtreeScoreRaw+0x2c0>  // b.any
    3658:	f9400288 	ldr	x8, [x20]
    365c:	92401d09 	and	x9, x8, #0xff
    3660:	92781d0a 	and	x10, x8, #0xff00
    3664:	f100013f 	cmp	x9, #0x0
    3668:	92701d09 	and	x9, x8, #0xff0000
    366c:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3670:	92681d0a 	and	x10, x8, #0xff000000
    3674:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3678:	92601d09 	and	x9, x8, #0xff00000000
    367c:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3680:	92581d0a 	and	x10, x8, #0xff0000000000
    3684:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3688:	92501d09 	and	x9, x8, #0xff000000000000
    368c:	d378fd08 	lsr	x8, x8, #56
    3690:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3694:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3698:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    369c:	54000920 	b.eq	37c0 <zbtreeScoreRaw+0x2c0>  // b.none
    36a0:	f9400788 	ldr	x8, [x28, #8]
    36a4:	91000739 	add	x25, x25, #0x1
    36a8:	91000709 	add	x9, x24, #0x1
    36ac:	8a170138 	and	x24, x9, x23
    36b0:	eb08033f 	cmp	x25, x8
    36b4:	54fff903 	b.cc	35d4 <zbtreeScoreRaw+0xd4>  // b.lo, b.ul, b.last
    36b8:	14000042 	b	37c0 <zbtreeScoreRaw+0x2c0>
    36bc:	d0000060 	adrp	x0, 11000 <siphash+0x1bc>
    36c0:	9123c400 	add	x0, x0, #0x8f1
    36c4:	5280f4a1 	mov	w1, #0x7a5                 	// #1957
    36c8:	d0000062 	adrp	x2, 11000 <siphash+0x1bc>
    36cc:	9129a442 	add	x2, x2, #0xa69
    36d0:	940034a9 	bl	10974 <standalone_panic>
    36d4:	d10006a8 	sub	x8, x21, #0x1
    36d8:	ea150115 	ands	x21, x8, x21
    36dc:	54fff9e0 	b.eq	3618 <zbtreeScoreRaw+0x118>  // b.none
    36e0:	dac002a8 	rbit	x8, x21
    36e4:	b9402389 	ldr	w9, [x28, #32]
    36e8:	dac01108 	clz	x8, x8
    36ec:	d343fd08 	lsr	x8, x8, #3
    36f0:	340000c9 	cbz	w9, 3708 <zbtreeScoreRaw+0x208>
    36f4:	8b080a88 	add	x8, x20, x8, lsl #2
    36f8:	b9401108 	ldr	w8, [x8, #16]
    36fc:	3100051f 	cmn	w8, #0x1
    3700:	540000c1 	b.ne	3718 <zbtreeScoreRaw+0x218>  // b.any
    3704:	17fffff4 	b	36d4 <zbtreeScoreRaw+0x1d4>
    3708:	8b080688 	add	x8, x20, x8, lsl #1
    370c:	79402108 	ldrh	w8, [x8, #16]
    3710:	6b13011f 	cmp	w8, w19
    3714:	54fffe00 	b.eq	36d4 <zbtreeScoreRaw+0x1d4>  // b.none
    3718:	b94056c9 	ldr	w9, [x22, #84]
    371c:	6b09011f 	cmp	w8, w9
    3720:	540000e2 	b.cs	373c <zbtreeScoreRaw+0x23c>  // b.hs, b.nlast
    3724:	f94026c9 	ldr	x9, [x22, #72]
    3728:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    372c:	92400369 	and	x9, x27, #0x1
    3730:	f100037f 	cmp	x27, #0x0
    3734:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    3738:	540000c0 	b.eq	3750 <zbtreeScoreRaw+0x250>  // b.none
    373c:	f94022c8 	ldr	x8, [x22, #64]
    3740:	b4fffbe8 	cbz	x8, 36bc <zbtreeScoreRaw+0x1bc>
    3744:	eb1c035f 	cmp	x26, x28
    3748:	54fffc60 	b.eq	36d4 <zbtreeScoreRaw+0x1d4>  // b.none
    374c:	17ffffdc 	b	36bc <zbtreeScoreRaw+0x1bc>
    3750:	b9403369 	ldr	w9, [x27, #48]
    3754:	6b08013f 	cmp	w9, w8
    3758:	540000e0 	b.eq	3774 <zbtreeScoreRaw+0x274>  // b.none
    375c:	d0000060 	adrp	x0, 11000 <siphash+0x1bc>
    3760:	9123c400 	add	x0, x0, #0x8f1
    3764:	5280f521 	mov	w1, #0x7a9                 	// #1961
    3768:	d0000062 	adrp	x2, 11000 <siphash+0x1bc>
    376c:	91292842 	add	x2, x2, #0xa4a
    3770:	94003481 	bl	10974 <standalone_panic>
    3774:	f94022c8 	ldr	x8, [x22, #64]
    3778:	b4000128 	cbz	x8, 379c <zbtreeScoreRaw+0x29c>
    377c:	79402f69 	ldrh	w9, [x27, #22]
    3780:	7940590a 	ldrh	w10, [x8, #44]
    3784:	eb1c011f 	cmp	x8, x28
    3788:	1a9f17e8 	cset	w8, eq	// eq = none
    378c:	6b0a013f 	cmp	w9, w10
    3790:	1a9f07e9 	cset	w9, ne	// ne = any
    3794:	6b09011f 	cmp	w8, w9
    3798:	54fff9e0 	b.eq	36d4 <zbtreeScoreRaw+0x1d4>  // b.none
    379c:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    37a0:	aa1b03e0 	mov	x0, x27
    37a4:	f94013e2 	ldr	x2, [sp, #32]
    37a8:	f85e83a3 	ldur	x3, [x29, #-24]
    37ac:	aa1f03e5 	mov	x5, xzr
    37b0:	94001d93 	bl	adfc <zbtScoreLeafFindMember>
    37b4:	34fff900 	cbz	w0, 36d4 <zbtreeScoreRaw+0x1d4>
    37b8:	52800020 	mov	w0, #0x1                   	// #1
    37bc:	1400009b 	b	3a28 <zbtreeScoreRaw+0x528>
    37c0:	f94012c8 	ldr	x8, [x22, #32]
    37c4:	b4001308 	cbz	x8, 3a24 <zbtreeScoreRaw+0x524>
    37c8:	f85f83ac 	ldur	x12, [x29, #-8]
    37cc:	d100050e 	sub	x14, x8, #0x1
    37d0:	b200c3e8 	mov	x8, #0x101010101010101     	// #72340172838076673
    37d4:	aa1f03fc 	mov	x28, xzr
    37d8:	910062d9 	add	x25, x22, #0x18
    37dc:	d0000078 	adrp	x24, 11000 <siphash+0x1bc>
    37e0:	9123c718 	add	x24, x24, #0x8f1
    37e4:	53187d89 	lsr	w9, w12, #24
    37e8:	d358fd8a 	lsr	x10, x12, #24
    37ec:	92407d8f 	and	x15, x12, #0xffffffff
    37f0:	5280002c 	mov	w12, #0x1                   	// #1
    37f4:	529ffff4 	mov	w20, #0xffff                	// #65535
    37f8:	7100013f 	cmp	w9, #0x0
    37fc:	8a0f01d3 	and	x19, x14, x15
    3800:	d000007a 	adrp	x26, 11000 <siphash+0x1bc>
    3804:	9129a75a 	add	x26, x26, #0xa69
    3808:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    380c:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    3810:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    3814:	92401d2b 	and	x11, x9, #0xff
    3818:	9ac92189 	lsl	x9, x12, x9
    381c:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    3820:	9b087d68 	mul	x8, x11, x8
    3824:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    3828:	9b0a7d6a 	mul	x10, x11, x10
    382c:	a90123ee 	stp	x14, x8, [sp, #16]
    3830:	d37afd4d 	lsr	x13, x10, #58
    3834:	d364fd4a 	lsr	x10, x10, #36
    3838:	9acd2188 	lsl	x8, x12, x13
    383c:	9aca218a 	lsl	x10, x12, x10
    3840:	aa090108 	orr	x8, x8, x9
    3844:	aa0a0108 	orr	x8, x8, x10
    3848:	a9003fe8 	stp	x8, x15, [sp]
    384c:	b9403ac8 	ldr	w8, [x22, #56]
    3850:	52800409 	mov	w9, #0x20                  	// #32
    3854:	b200dbea 	mov	x10, #0x7f7f7f7f7f7f7f7f    	// #9187201950435737471
    3858:	7100011f 	cmp	w8, #0x0
    385c:	52800608 	mov	w8, #0x30                  	// #48
    3860:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    3864:	f9400ec9 	ldr	x9, [x22, #24]
    3868:	9b132515 	madd	x21, x8, x19, x9
    386c:	f9400fe9 	ldr	x9, [sp, #24]
    3870:	f94002a8 	ldr	x8, [x21]
    3874:	ca090108 	eor	x8, x8, x9
    3878:	9200d909 	and	x9, x8, #0x7f7f7f7f7f7f7f7f
    387c:	8b0a0129 	add	x9, x9, x10
    3880:	aa080128 	orr	x8, x9, x8
    3884:	b201c3e9 	mov	x9, #0x8080808080808080    	// #-9187201950435737472
    3888:	ea280137 	bics	x23, x9, x8
    388c:	54000601 	b.ne	394c <zbtreeScoreRaw+0x44c>  // b.any
    3890:	b500021c 	cbnz	x28, 38d0 <zbtreeScoreRaw+0x3d0>
    3894:	b9403ac9 	ldr	w9, [x22, #56]
    3898:	b94022c8 	ldr	w8, [x22, #32]
    389c:	5280040a 	mov	w10, #0x20                  	// #32
    38a0:	7100013f 	cmp	w9, #0x0
    38a4:	f94007e9 	ldr	x9, [sp, #8]
    38a8:	51000508 	sub	w8, w8, #0x1
    38ac:	8a090108 	and	x8, x8, x9
    38b0:	52800609 	mov	w9, #0x30                  	// #48
    38b4:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    38b8:	f9400eca 	ldr	x10, [x22, #24]
    38bc:	9ba82928 	umaddl	x8, w9, w8, x10
    38c0:	f94003e9 	ldr	x9, [sp]
    38c4:	f9400508 	ldr	x8, [x8, #8]
    38c8:	ea28013f 	bics	xzr, x9, x8
    38cc:	54000ac1 	b.ne	3a24 <zbtreeScoreRaw+0x524>  // b.any
    38d0:	f94002a8 	ldr	x8, [x21]
    38d4:	92401d09 	and	x9, x8, #0xff
    38d8:	92781d0a 	and	x10, x8, #0xff00
    38dc:	f100013f 	cmp	x9, #0x0
    38e0:	92701d09 	and	x9, x8, #0xff0000
    38e4:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38e8:	92681d0a 	and	x10, x8, #0xff000000
    38ec:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38f0:	92601d09 	and	x9, x8, #0xff00000000
    38f4:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38f8:	92581d0a 	and	x10, x8, #0xff0000000000
    38fc:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3900:	92501d09 	and	x9, x8, #0xff000000000000
    3904:	d378fd08 	lsr	x8, x8, #56
    3908:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    390c:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3910:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    3914:	54000880 	b.eq	3a24 <zbtreeScoreRaw+0x524>  // b.none
    3918:	f94012c8 	ldr	x8, [x22, #32]
    391c:	9100079c 	add	x28, x28, #0x1
    3920:	91000669 	add	x9, x19, #0x1
    3924:	eb08039f 	cmp	x28, x8
    3928:	f9400be8 	ldr	x8, [sp, #16]
    392c:	8a080133 	and	x19, x9, x8
    3930:	54fff8e3 	b.cc	384c <zbtreeScoreRaw+0x34c>  // b.lo, b.ul, b.last
    3934:	1400003c 	b	3a24 <zbtreeScoreRaw+0x524>
    3938:	f94022c8 	ldr	x8, [x22, #64]
    393c:	b40006a8 	cbz	x8, 3a10 <zbtreeScoreRaw+0x510>
    3940:	d10006e8 	sub	x8, x23, #0x1
    3944:	ea170117 	ands	x23, x8, x23
    3948:	54fffa40 	b.eq	3890 <zbtreeScoreRaw+0x390>  // b.none
    394c:	dac002e8 	rbit	x8, x23
    3950:	b9403ac9 	ldr	w9, [x22, #56]
    3954:	dac01108 	clz	x8, x8
    3958:	d343fd08 	lsr	x8, x8, #3
    395c:	340000c9 	cbz	w9, 3974 <zbtreeScoreRaw+0x474>
    3960:	8b080aa8 	add	x8, x21, x8, lsl #2
    3964:	b9401108 	ldr	w8, [x8, #16]
    3968:	3100051f 	cmn	w8, #0x1
    396c:	540000c1 	b.ne	3984 <zbtreeScoreRaw+0x484>  // b.any
    3970:	17fffff4 	b	3940 <zbtreeScoreRaw+0x440>
    3974:	8b0806a8 	add	x8, x21, x8, lsl #1
    3978:	79402108 	ldrh	w8, [x8, #16]
    397c:	6b14011f 	cmp	w8, w20
    3980:	54fffe00 	b.eq	3940 <zbtreeScoreRaw+0x440>  // b.none
    3984:	b94056c9 	ldr	w9, [x22, #84]
    3988:	6b09011f 	cmp	w8, w9
    398c:	54fffd62 	b.cs	3938 <zbtreeScoreRaw+0x438>  // b.hs, b.nlast
    3990:	f94026c9 	ldr	x9, [x22, #72]
    3994:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3998:	92400369 	and	x9, x27, #0x1
    399c:	f100037f 	cmp	x27, #0x0
    39a0:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    39a4:	54fffca1 	b.ne	3938 <zbtreeScoreRaw+0x438>  // b.any
    39a8:	b9403369 	ldr	w9, [x27, #48]
    39ac:	6b08013f 	cmp	w9, w8
    39b0:	540000c0 	b.eq	39c8 <zbtreeScoreRaw+0x4c8>  // b.none
    39b4:	aa1803e0 	mov	x0, x24
    39b8:	5280f521 	mov	w1, #0x7a9                 	// #1961
    39bc:	d0000062 	adrp	x2, 11000 <siphash+0x1bc>
    39c0:	91292842 	add	x2, x2, #0xa4a
    39c4:	940033ec 	bl	10974 <standalone_panic>
    39c8:	f94022c8 	ldr	x8, [x22, #64]
    39cc:	b4000128 	cbz	x8, 39f0 <zbtreeScoreRaw+0x4f0>
    39d0:	79402f69 	ldrh	w9, [x27, #22]
    39d4:	7940590a 	ldrh	w10, [x8, #44]
    39d8:	eb19011f 	cmp	x8, x25
    39dc:	1a9f17e8 	cset	w8, eq	// eq = none
    39e0:	6b0a013f 	cmp	w9, w10
    39e4:	1a9f07e9 	cset	w9, ne	// ne = any
    39e8:	6b09011f 	cmp	w8, w9
    39ec:	54fffaa0 	b.eq	3940 <zbtreeScoreRaw+0x440>  // b.none
    39f0:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    39f4:	aa1b03e0 	mov	x0, x27
    39f8:	f94013e2 	ldr	x2, [sp, #32]
    39fc:	f85e83a3 	ldur	x3, [x29, #-24]
    3a00:	aa1f03e5 	mov	x5, xzr
    3a04:	94001cfe 	bl	adfc <zbtScoreLeafFindMember>
    3a08:	34fff9c0 	cbz	w0, 3940 <zbtreeScoreRaw+0x440>
    3a0c:	17ffff6b 	b	37b8 <zbtreeScoreRaw+0x2b8>
    3a10:	aa1803e0 	mov	x0, x24
    3a14:	5280f4a1 	mov	w1, #0x7a5                 	// #1957
    3a18:	aa1a03e2 	mov	x2, x26
    3a1c:	940033d6 	bl	10974 <standalone_panic>
    3a20:	17ffffc8 	b	3940 <zbtreeScoreRaw+0x440>
    3a24:	2a1f03e0 	mov	w0, wzr
    3a28:	a9494ff4 	ldp	x20, x19, [sp, #144]
    3a2c:	a94857f6 	ldp	x22, x21, [sp, #128]
    3a30:	a9475ff8 	ldp	x24, x23, [sp, #112]
    3a34:	a94667fa 	ldp	x26, x25, [sp, #96]
    3a38:	a9456ffc 	ldp	x28, x27, [sp, #80]
    3a3c:	a9447bfd 	ldp	x29, x30, [sp, #64]
    3a40:	910283ff 	add	sp, sp, #0xa0
    3a44:	d65f03c0 	ret

Disassembly of section .fini:
