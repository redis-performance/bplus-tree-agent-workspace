
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/build/C-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

0000000000003500 <zbtreeScoreRaw>:
    3500:	d10283ff 	sub	sp, sp, #0xa0
    3504:	fd001be8 	str	d8, [sp, #48]
    3508:	a9047bfd 	stp	x29, x30, [sp, #64]
    350c:	a9056ffc 	stp	x28, x27, [sp, #80]
    3510:	a90667fa 	stp	x26, x25, [sp, #96]
    3514:	a9075ff8 	stp	x24, x23, [sp, #112]
    3518:	a90857f6 	stp	x22, x21, [sp, #128]
    351c:	a9094ff4 	stp	x20, x19, [sp, #144]
    3520:	910103fd 	add	x29, sp, #0x40
    3524:	aa0003f6 	mov	x22, x0
    3528:	a9018be1 	stp	x1, x2, [sp, #24]
    352c:	aa0103e0 	mov	x0, x1
    3530:	aa0203e1 	mov	x1, x2
    3534:	f81e83a3 	stur	x3, [x29, #-24]
    3538:	9400356f 	bl	10af4 <dictGenHashFunction>
    353c:	f94022c8 	ldr	x8, [x22, #64]
    3540:	f81f83a0 	stur	x0, [x29, #-8]
    3544:	b4001328 	cbz	x8, 37a8 <zbtreeScoreRaw+0x2a8>
    3548:	aa1603e0 	mov	x0, x22
    354c:	52800021 	mov	w1, #0x1                   	// #1
    3550:	94000eb3 	bl	701c <zbtIndexRehashStep>
    3554:	f94022dc 	ldr	x28, [x22, #64]
    3558:	b400129c 	cbz	x28, 37a8 <zbtreeScoreRaw+0x2a8>
    355c:	f9400788 	ldr	x8, [x28, #8]
    3560:	b4001248 	cbz	x8, 37a8 <zbtreeScoreRaw+0x2a8>
    3564:	f85f83ac 	ldur	x12, [x29, #-8]
    3568:	d1000517 	sub	x23, x8, #0x1
    356c:	52800028 	mov	w8, #0x1                   	// #1
    3570:	aa1f03f9 	mov	x25, xzr
    3574:	910062da 	add	x26, x22, #0x18
    3578:	529ffff8 	mov	w24, #0xffff                	// #65535
    357c:	53187d89 	lsr	w9, w12, #24
    3580:	d358fd8a 	lsr	x10, x12, #24
    3584:	92407d8d 	and	x13, x12, #0xffffffff
    3588:	8a0d02f3 	and	x19, x23, x13
    358c:	7100013f 	cmp	w9, #0x0
    3590:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    3594:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    3598:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    359c:	92401d2b 	and	x11, x9, #0xff
    35a0:	9ac9210c 	lsl	x12, x8, x9
    35a4:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    35a8:	0e010d28 	dup	v8.8b, w9
    35ac:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    35b0:	9b0a7d6a 	mul	x10, x11, x10
    35b4:	d37afd4b 	lsr	x11, x10, #58
    35b8:	d364fd4a 	lsr	x10, x10, #36
    35bc:	9acb210b 	lsl	x11, x8, x11
    35c0:	9aca2108 	lsl	x8, x8, x10
    35c4:	aa0c0169 	orr	x9, x11, x12
    35c8:	aa080128 	orr	x8, x9, x8
    35cc:	a900b7e8 	stp	x8, x13, [sp, #8]
    35d0:	b9402388 	ldr	w8, [x28, #32]
    35d4:	52800409 	mov	w9, #0x20                  	// #32
    35d8:	7100011f 	cmp	w8, #0x0
    35dc:	52800608 	mov	w8, #0x30                  	// #48
    35e0:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    35e4:	f9400389 	ldr	x9, [x28]
    35e8:	9b132514 	madd	x20, x8, x19, x9
    35ec:	fd400280 	ldr	d0, [x20]
    35f0:	2e208d00 	cmeq	v0.8b, v8.8b, v0.8b
    35f4:	9e660008 	fmov	x8, d0
    35f8:	f201c115 	ands	x21, x8, #0x8080808080808080
    35fc:	54000661 	b.ne	36c8 <zbtreeScoreRaw+0x1c8>  // b.any
    3600:	b5000219 	cbnz	x25, 3640 <zbtreeScoreRaw+0x140>
    3604:	b9402389 	ldr	w9, [x28, #32]
    3608:	b9400b88 	ldr	w8, [x28, #8]
    360c:	5280040a 	mov	w10, #0x20                  	// #32
    3610:	7100013f 	cmp	w9, #0x0
    3614:	f9400be9 	ldr	x9, [sp, #16]
    3618:	51000508 	sub	w8, w8, #0x1
    361c:	8a090108 	and	x8, x8, x9
    3620:	52800609 	mov	w9, #0x30                  	// #48
    3624:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    3628:	f940038a 	ldr	x10, [x28]
    362c:	9ba82928 	umaddl	x8, w9, w8, x10
    3630:	f94007e9 	ldr	x9, [sp, #8]
    3634:	f9400508 	ldr	x8, [x8, #8]
    3638:	ea28013f 	bics	xzr, x9, x8
    363c:	54000b61 	b.ne	37a8 <zbtreeScoreRaw+0x2a8>  // b.any
    3640:	f9400288 	ldr	x8, [x20]
    3644:	92401d09 	and	x9, x8, #0xff
    3648:	92781d0a 	and	x10, x8, #0xff00
    364c:	f100013f 	cmp	x9, #0x0
    3650:	92701d09 	and	x9, x8, #0xff0000
    3654:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3658:	92681d0a 	and	x10, x8, #0xff000000
    365c:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3660:	92601d09 	and	x9, x8, #0xff00000000
    3664:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3668:	92581d0a 	and	x10, x8, #0xff0000000000
    366c:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3670:	92501d09 	and	x9, x8, #0xff000000000000
    3674:	d378fd08 	lsr	x8, x8, #56
    3678:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    367c:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3680:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    3684:	54000920 	b.eq	37a8 <zbtreeScoreRaw+0x2a8>  // b.none
    3688:	f9400788 	ldr	x8, [x28, #8]
    368c:	91000739 	add	x25, x25, #0x1
    3690:	91000669 	add	x9, x19, #0x1
    3694:	8a170133 	and	x19, x9, x23
    3698:	eb08033f 	cmp	x25, x8
    369c:	54fff9a3 	b.cc	35d0 <zbtreeScoreRaw+0xd0>  // b.lo, b.ul, b.last
    36a0:	14000042 	b	37a8 <zbtreeScoreRaw+0x2a8>
    36a4:	d0000060 	adrp	x0, 11000 <siphash_nocase+0xdc>
    36a8:	91204400 	add	x0, x0, #0x811
    36ac:	5280f601 	mov	w1, #0x7b0                 	// #1968
    36b0:	d0000062 	adrp	x2, 11000 <siphash_nocase+0xdc>
    36b4:	91267442 	add	x2, x2, #0x99d
    36b8:	94003477 	bl	10894 <standalone_panic>
    36bc:	d10006a8 	sub	x8, x21, #0x1
    36c0:	ea150115 	ands	x21, x8, x21
    36c4:	54fff9e0 	b.eq	3600 <zbtreeScoreRaw+0x100>  // b.none
    36c8:	dac002a8 	rbit	x8, x21
    36cc:	b9402389 	ldr	w9, [x28, #32]
    36d0:	dac01108 	clz	x8, x8
    36d4:	d343fd08 	lsr	x8, x8, #3
    36d8:	340000c9 	cbz	w9, 36f0 <zbtreeScoreRaw+0x1f0>
    36dc:	8b080a88 	add	x8, x20, x8, lsl #2
    36e0:	b9401108 	ldr	w8, [x8, #16]
    36e4:	3100051f 	cmn	w8, #0x1
    36e8:	540000c1 	b.ne	3700 <zbtreeScoreRaw+0x200>  // b.any
    36ec:	17fffff4 	b	36bc <zbtreeScoreRaw+0x1bc>
    36f0:	8b080688 	add	x8, x20, x8, lsl #1
    36f4:	79402108 	ldrh	w8, [x8, #16]
    36f8:	6b18011f 	cmp	w8, w24
    36fc:	54fffe00 	b.eq	36bc <zbtreeScoreRaw+0x1bc>  // b.none
    3700:	b94056c9 	ldr	w9, [x22, #84]
    3704:	6b09011f 	cmp	w8, w9
    3708:	540000e2 	b.cs	3724 <zbtreeScoreRaw+0x224>  // b.hs, b.nlast
    370c:	f94026c9 	ldr	x9, [x22, #72]
    3710:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3714:	92400369 	and	x9, x27, #0x1
    3718:	f100037f 	cmp	x27, #0x0
    371c:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    3720:	540000c0 	b.eq	3738 <zbtreeScoreRaw+0x238>  // b.none
    3724:	f94022c8 	ldr	x8, [x22, #64]
    3728:	b4fffbe8 	cbz	x8, 36a4 <zbtreeScoreRaw+0x1a4>
    372c:	eb1c035f 	cmp	x26, x28
    3730:	54fffc60 	b.eq	36bc <zbtreeScoreRaw+0x1bc>  // b.none
    3734:	17ffffdc 	b	36a4 <zbtreeScoreRaw+0x1a4>
    3738:	b9403369 	ldr	w9, [x27, #48]
    373c:	6b08013f 	cmp	w9, w8
    3740:	540000e0 	b.eq	375c <zbtreeScoreRaw+0x25c>  // b.none
    3744:	d0000060 	adrp	x0, 11000 <siphash_nocase+0xdc>
    3748:	91204400 	add	x0, x0, #0x811
    374c:	5280f681 	mov	w1, #0x7b4                 	// #1972
    3750:	d0000062 	adrp	x2, 11000 <siphash_nocase+0xdc>
    3754:	9125f842 	add	x2, x2, #0x97e
    3758:	9400344f 	bl	10894 <standalone_panic>
    375c:	f94022c8 	ldr	x8, [x22, #64]
    3760:	b4000128 	cbz	x8, 3784 <zbtreeScoreRaw+0x284>
    3764:	79402f69 	ldrh	w9, [x27, #22]
    3768:	7940590a 	ldrh	w10, [x8, #44]
    376c:	eb1c011f 	cmp	x8, x28
    3770:	1a9f17e8 	cset	w8, eq	// eq = none
    3774:	6b0a013f 	cmp	w9, w10
    3778:	1a9f07e9 	cset	w9, ne	// ne = any
    377c:	6b09011f 	cmp	w8, w9
    3780:	54fff9e0 	b.eq	36bc <zbtreeScoreRaw+0x1bc>  // b.none
    3784:	a9418fe2 	ldp	x2, x3, [sp, #24]
    3788:	aa1b03e0 	mov	x0, x27
    378c:	f85e83a4 	ldur	x4, [x29, #-24]
    3790:	f85f83a1 	ldur	x1, [x29, #-8]
    3794:	aa1f03e5 	mov	x5, xzr
    3798:	94001d61 	bl	ad1c <zbtScoreLeafFindMember>
    379c:	34fff900 	cbz	w0, 36bc <zbtreeScoreRaw+0x1bc>
    37a0:	52800020 	mov	w0, #0x1                   	// #1
    37a4:	14000095 	b	39f8 <zbtreeScoreRaw+0x4f8>
    37a8:	f94012c8 	ldr	x8, [x22, #32]
    37ac:	b4001248 	cbz	x8, 39f4 <zbtreeScoreRaw+0x4f4>
    37b0:	f85f83ac 	ldur	x12, [x29, #-8]
    37b4:	d100050d 	sub	x13, x8, #0x1
    37b8:	52800028 	mov	w8, #0x1                   	// #1
    37bc:	aa1f03fc 	mov	x28, xzr
    37c0:	910062d9 	add	x25, x22, #0x18
    37c4:	d0000078 	adrp	x24, 11000 <siphash_nocase+0xdc>
    37c8:	91204718 	add	x24, x24, #0x811
    37cc:	53187d89 	lsr	w9, w12, #24
    37d0:	d358fd8a 	lsr	x10, x12, #24
    37d4:	92407d8e 	and	x14, x12, #0xffffffff
    37d8:	529ffff4 	mov	w20, #0xffff                	// #65535
    37dc:	d000007a 	adrp	x26, 11000 <siphash_nocase+0xdc>
    37e0:	9126775a 	add	x26, x26, #0x99d
    37e4:	7100013f 	cmp	w9, #0x0
    37e8:	8a0e01b3 	and	x19, x13, x14
    37ec:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    37f0:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    37f4:	a900b7ee 	stp	x14, x13, [sp, #8]
    37f8:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    37fc:	92401d2b 	and	x11, x9, #0xff
    3800:	9ac9210c 	lsl	x12, x8, x9
    3804:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    3808:	0e010d28 	dup	v8.8b, w9
    380c:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    3810:	9b0a7d6a 	mul	x10, x11, x10
    3814:	d37afd4b 	lsr	x11, x10, #58
    3818:	d364fd4a 	lsr	x10, x10, #36
    381c:	9acb210b 	lsl	x11, x8, x11
    3820:	9aca2108 	lsl	x8, x8, x10
    3824:	aa0c0169 	orr	x9, x11, x12
    3828:	aa080128 	orr	x8, x9, x8
    382c:	f90003e8 	str	x8, [sp]
    3830:	b9403ac8 	ldr	w8, [x22, #56]
    3834:	52800409 	mov	w9, #0x20                  	// #32
    3838:	7100011f 	cmp	w8, #0x0
    383c:	52800608 	mov	w8, #0x30                  	// #48
    3840:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    3844:	f9400ec9 	ldr	x9, [x22, #24]
    3848:	9b132515 	madd	x21, x8, x19, x9
    384c:	fd4002a0 	ldr	d0, [x21]
    3850:	2e208d00 	cmeq	v0.8b, v8.8b, v0.8b
    3854:	9e660008 	fmov	x8, d0
    3858:	f201c117 	ands	x23, x8, #0x8080808080808080
    385c:	54000601 	b.ne	391c <zbtreeScoreRaw+0x41c>  // b.any
    3860:	b500021c 	cbnz	x28, 38a0 <zbtreeScoreRaw+0x3a0>
    3864:	b9403ac9 	ldr	w9, [x22, #56]
    3868:	b94022c8 	ldr	w8, [x22, #32]
    386c:	5280040a 	mov	w10, #0x20                  	// #32
    3870:	7100013f 	cmp	w9, #0x0
    3874:	f94007e9 	ldr	x9, [sp, #8]
    3878:	51000508 	sub	w8, w8, #0x1
    387c:	8a090108 	and	x8, x8, x9
    3880:	52800609 	mov	w9, #0x30                  	// #48
    3884:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    3888:	f9400eca 	ldr	x10, [x22, #24]
    388c:	9ba82928 	umaddl	x8, w9, w8, x10
    3890:	f94003e9 	ldr	x9, [sp]
    3894:	f9400508 	ldr	x8, [x8, #8]
    3898:	ea28013f 	bics	xzr, x9, x8
    389c:	54000ac1 	b.ne	39f4 <zbtreeScoreRaw+0x4f4>  // b.any
    38a0:	f94002a8 	ldr	x8, [x21]
    38a4:	92401d09 	and	x9, x8, #0xff
    38a8:	92781d0a 	and	x10, x8, #0xff00
    38ac:	f100013f 	cmp	x9, #0x0
    38b0:	92701d09 	and	x9, x8, #0xff0000
    38b4:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38b8:	92681d0a 	and	x10, x8, #0xff000000
    38bc:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38c0:	92601d09 	and	x9, x8, #0xff00000000
    38c4:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38c8:	92581d0a 	and	x10, x8, #0xff0000000000
    38cc:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38d0:	92501d09 	and	x9, x8, #0xff000000000000
    38d4:	d378fd08 	lsr	x8, x8, #56
    38d8:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38dc:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38e0:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    38e4:	54000880 	b.eq	39f4 <zbtreeScoreRaw+0x4f4>  // b.none
    38e8:	f94012c8 	ldr	x8, [x22, #32]
    38ec:	9100079c 	add	x28, x28, #0x1
    38f0:	91000669 	add	x9, x19, #0x1
    38f4:	eb08039f 	cmp	x28, x8
    38f8:	f9400be8 	ldr	x8, [sp, #16]
    38fc:	8a080133 	and	x19, x9, x8
    3900:	54fff983 	b.cc	3830 <zbtreeScoreRaw+0x330>  // b.lo, b.ul, b.last
    3904:	1400003c 	b	39f4 <zbtreeScoreRaw+0x4f4>
    3908:	f94022c8 	ldr	x8, [x22, #64]
    390c:	b40006a8 	cbz	x8, 39e0 <zbtreeScoreRaw+0x4e0>
    3910:	d10006e8 	sub	x8, x23, #0x1
    3914:	ea170117 	ands	x23, x8, x23
    3918:	54fffa40 	b.eq	3860 <zbtreeScoreRaw+0x360>  // b.none
    391c:	dac002e8 	rbit	x8, x23
    3920:	b9403ac9 	ldr	w9, [x22, #56]
    3924:	dac01108 	clz	x8, x8
    3928:	d343fd08 	lsr	x8, x8, #3
    392c:	340000c9 	cbz	w9, 3944 <zbtreeScoreRaw+0x444>
    3930:	8b080aa8 	add	x8, x21, x8, lsl #2
    3934:	b9401108 	ldr	w8, [x8, #16]
    3938:	3100051f 	cmn	w8, #0x1
    393c:	540000c1 	b.ne	3954 <zbtreeScoreRaw+0x454>  // b.any
    3940:	17fffff4 	b	3910 <zbtreeScoreRaw+0x410>
    3944:	8b0806a8 	add	x8, x21, x8, lsl #1
    3948:	79402108 	ldrh	w8, [x8, #16]
    394c:	6b14011f 	cmp	w8, w20
    3950:	54fffe00 	b.eq	3910 <zbtreeScoreRaw+0x410>  // b.none
    3954:	b94056c9 	ldr	w9, [x22, #84]
    3958:	6b09011f 	cmp	w8, w9
    395c:	54fffd62 	b.cs	3908 <zbtreeScoreRaw+0x408>  // b.hs, b.nlast
    3960:	f94026c9 	ldr	x9, [x22, #72]
    3964:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3968:	92400369 	and	x9, x27, #0x1
    396c:	f100037f 	cmp	x27, #0x0
    3970:	fa401920 	ccmp	x9, #0x0, #0x0, ne	// ne = any
    3974:	54fffca1 	b.ne	3908 <zbtreeScoreRaw+0x408>  // b.any
    3978:	b9403369 	ldr	w9, [x27, #48]
    397c:	6b08013f 	cmp	w9, w8
    3980:	540000c0 	b.eq	3998 <zbtreeScoreRaw+0x498>  // b.none
    3984:	aa1803e0 	mov	x0, x24
    3988:	5280f681 	mov	w1, #0x7b4                 	// #1972
    398c:	d0000062 	adrp	x2, 11000 <siphash_nocase+0xdc>
    3990:	9125f842 	add	x2, x2, #0x97e
    3994:	940033c0 	bl	10894 <standalone_panic>
    3998:	f94022c8 	ldr	x8, [x22, #64]
    399c:	b4000128 	cbz	x8, 39c0 <zbtreeScoreRaw+0x4c0>
    39a0:	79402f69 	ldrh	w9, [x27, #22]
    39a4:	7940590a 	ldrh	w10, [x8, #44]
    39a8:	eb19011f 	cmp	x8, x25
    39ac:	1a9f17e8 	cset	w8, eq	// eq = none
    39b0:	6b0a013f 	cmp	w9, w10
    39b4:	1a9f07e9 	cset	w9, ne	// ne = any
    39b8:	6b09011f 	cmp	w8, w9
    39bc:	54fffaa0 	b.eq	3910 <zbtreeScoreRaw+0x410>  // b.none
    39c0:	a9418fe2 	ldp	x2, x3, [sp, #24]
    39c4:	aa1b03e0 	mov	x0, x27
    39c8:	f85e83a4 	ldur	x4, [x29, #-24]
    39cc:	f85f83a1 	ldur	x1, [x29, #-8]
    39d0:	aa1f03e5 	mov	x5, xzr
    39d4:	94001cd2 	bl	ad1c <zbtScoreLeafFindMember>
    39d8:	34fff9c0 	cbz	w0, 3910 <zbtreeScoreRaw+0x410>
    39dc:	17ffff71 	b	37a0 <zbtreeScoreRaw+0x2a0>
    39e0:	aa1803e0 	mov	x0, x24
    39e4:	5280f601 	mov	w1, #0x7b0                 	// #1968
    39e8:	aa1a03e2 	mov	x2, x26
    39ec:	940033aa 	bl	10894 <standalone_panic>
    39f0:	17ffffc8 	b	3910 <zbtreeScoreRaw+0x410>
    39f4:	2a1f03e0 	mov	w0, wzr
    39f8:	a9494ff4 	ldp	x20, x19, [sp, #144]
    39fc:	fd401be8 	ldr	d8, [sp, #48]
    3a00:	a94857f6 	ldp	x22, x21, [sp, #128]
    3a04:	a9475ff8 	ldp	x24, x23, [sp, #112]
    3a08:	a94667fa 	ldp	x26, x25, [sp, #96]
    3a0c:	a9456ffc 	ldp	x28, x27, [sp, #80]
    3a10:	a9447bfd 	ldp	x29, x30, [sp, #64]
    3a14:	910283ff 	add	sp, sp, #0xa0
    3a18:	d65f03c0 	ret

Disassembly of section .fini:
