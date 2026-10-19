
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/build/base:     file format elf64-littleaarch64


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
    3534:	940035d3 	bl	10c80 <dictGenHashFunction>
    3538:	f94022c8 	ldr	x8, [x22, #64]
    353c:	f81f83a0 	stur	x0, [x29, #-8]
    3540:	b4001468 	cbz	x8, 37cc <zbtreeScoreRaw+0x2cc>
    3544:	aa1603e0 	mov	x0, x22
    3548:	52800021 	mov	w1, #0x1                   	// #1
    354c:	94000f17 	bl	71a8 <zbtIndexRehashStep>
    3550:	f94022dc 	ldr	x28, [x22, #64]
    3554:	b40013dc 	cbz	x28, 37cc <zbtreeScoreRaw+0x2cc>
    3558:	f9400788 	ldr	x8, [x28, #8]
    355c:	b4001388 	cbz	x8, 37cc <zbtreeScoreRaw+0x2cc>
    3560:	f85f83ac 	ldur	x12, [x29, #-8]
    3564:	d100050f 	sub	x15, x8, #0x1
    3568:	b200c3e8 	mov	x8, #0x101010101010101     	// #72340172838076673
    356c:	aa1f03f9 	mov	x25, xzr
    3570:	910062da 	add	x26, x22, #0x18
    3574:	529ffff8 	mov	w24, #0xffff                	// #65535
    3578:	53187d89 	lsr	w9, w12, #24
    357c:	d358fd8a 	lsr	x10, x12, #24
    3580:	92407d90 	and	x16, x12, #0xffffffff
    3584:	5280002c 	mov	w12, #0x1                   	// #1
    3588:	8a1001f3 	and	x19, x15, x16
    358c:	7100013f 	cmp	w9, #0x0
    3590:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    3594:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    3598:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    359c:	92401d2b 	and	x11, x9, #0xff
    35a0:	9ac9218e 	lsl	x14, x12, x9
    35a4:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    35a8:	9b087d68 	mul	x8, x11, x8
    35ac:	12001d34 	and	w20, w9, #0xff
    35b0:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    35b4:	9b0a7d6a 	mul	x10, x11, x10
    35b8:	a90123ef 	stp	x15, x8, [sp, #16]
    35bc:	d37afd4d 	lsr	x13, x10, #58
    35c0:	d364fd4a 	lsr	x10, x10, #36
    35c4:	9acd2188 	lsl	x8, x12, x13
    35c8:	9aca218a 	lsl	x10, x12, x10
    35cc:	aa0e0108 	orr	x8, x8, x14
    35d0:	aa0a0108 	orr	x8, x8, x10
    35d4:	a90043e8 	stp	x8, x16, [sp]
    35d8:	b9402388 	ldr	w8, [x28, #32]
    35dc:	52800409 	mov	w9, #0x20                  	// #32
    35e0:	7100011f 	cmp	w8, #0x0
    35e4:	52800608 	mov	w8, #0x30                  	// #48
    35e8:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    35ec:	f9400389 	ldr	x9, [x28]
    35f0:	9b132515 	madd	x21, x8, x19, x9
    35f4:	f9400fe9 	ldr	x9, [sp, #24]
    35f8:	f94002a8 	ldr	x8, [x21]
    35fc:	ca090108 	eor	x8, x8, x9
    3600:	b207dbe9 	mov	x9, #0xfefefefefefefefe    	// #-72340172838076674
    3604:	f29fdfe9 	movk	x9, #0xfeff
    3608:	8b090109 	add	x9, x8, x9
    360c:	8a280128 	bic	x8, x9, x8
    3610:	f201c117 	ands	x23, x8, #0x8080808080808080
    3614:	54000681 	b.ne	36e4 <zbtreeScoreRaw+0x1e4>  // b.any
    3618:	b5000219 	cbnz	x25, 3658 <zbtreeScoreRaw+0x158>
    361c:	b9402389 	ldr	w9, [x28, #32]
    3620:	b9400b88 	ldr	w8, [x28, #8]
    3624:	5280040a 	mov	w10, #0x20                  	// #32
    3628:	7100013f 	cmp	w9, #0x0
    362c:	f94007e9 	ldr	x9, [sp, #8]
    3630:	51000508 	sub	w8, w8, #0x1
    3634:	8a090108 	and	x8, x8, x9
    3638:	52800609 	mov	w9, #0x30                  	// #48
    363c:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    3640:	f940038a 	ldr	x10, [x28]
    3644:	9ba82928 	umaddl	x8, w9, w8, x10
    3648:	f94003e9 	ldr	x9, [sp]
    364c:	f9400508 	ldr	x8, [x8, #8]
    3650:	ea28013f 	bics	xzr, x9, x8
    3654:	54000bc1 	b.ne	37cc <zbtreeScoreRaw+0x2cc>  // b.any
    3658:	f94002a8 	ldr	x8, [x21]
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
    369c:	54000980 	b.eq	37cc <zbtreeScoreRaw+0x2cc>  // b.none
    36a0:	f9400788 	ldr	x8, [x28, #8]
    36a4:	91000739 	add	x25, x25, #0x1
    36a8:	91000669 	add	x9, x19, #0x1
    36ac:	eb08033f 	cmp	x25, x8
    36b0:	f9400be8 	ldr	x8, [sp, #16]
    36b4:	8a080133 	and	x19, x9, x8
    36b8:	54fff903 	b.cc	35d8 <zbtreeScoreRaw+0xd8>  // b.lo, b.ul, b.last
    36bc:	14000044 	b	37cc <zbtreeScoreRaw+0x2cc>
    36c0:	d0000060 	adrp	x0, 11000 <siphash+0x110>
    36c4:	91264400 	add	x0, x0, #0x991
    36c8:	5280f421 	mov	w1, #0x7a1                 	// #1953
    36cc:	d0000062 	adrp	x2, 11000 <siphash+0x110>
    36d0:	912c2442 	add	x2, x2, #0xb09
    36d4:	940034d3 	bl	10a20 <standalone_panic>
    36d8:	d10006e8 	sub	x8, x23, #0x1
    36dc:	ea170117 	ands	x23, x8, x23
    36e0:	54fff9c0 	b.eq	3618 <zbtreeScoreRaw+0x118>  // b.none
    36e4:	dac002e8 	rbit	x8, x23
    36e8:	f94002a9 	ldr	x9, [x21]
    36ec:	dac01108 	clz	x8, x8
    36f0:	927d090a 	and	x10, x8, #0x38
    36f4:	9aca2529 	lsr	x9, x9, x10
    36f8:	6b29029f 	cmp	w20, w9, uxtb
    36fc:	54fffee1 	b.ne	36d8 <zbtreeScoreRaw+0x1d8>  // b.any
    3700:	b9402389 	ldr	w9, [x28, #32]
    3704:	d343fd08 	lsr	x8, x8, #3
    3708:	340000c9 	cbz	w9, 3720 <zbtreeScoreRaw+0x220>
    370c:	8b080aa8 	add	x8, x21, x8, lsl #2
    3710:	b9401108 	ldr	w8, [x8, #16]
    3714:	3100051f 	cmn	w8, #0x1
    3718:	540000c1 	b.ne	3730 <zbtreeScoreRaw+0x230>  // b.any
    371c:	17ffffef 	b	36d8 <zbtreeScoreRaw+0x1d8>
    3720:	8b0806a8 	add	x8, x21, x8, lsl #1
    3724:	79402108 	ldrh	w8, [x8, #16]
    3728:	6b18011f 	cmp	w8, w24
    372c:	54fffd60 	b.eq	36d8 <zbtreeScoreRaw+0x1d8>  // b.none
    3730:	b94056c9 	ldr	w9, [x22, #84]
    3734:	6b09011f 	cmp	w8, w9
    3738:	54000402 	b.cs	37b8 <zbtreeScoreRaw+0x2b8>  // b.hs, b.nlast
    373c:	f94026c9 	ldr	x9, [x22, #72]
    3740:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    3744:	b40003bb 	cbz	x27, 37b8 <zbtreeScoreRaw+0x2b8>
    3748:	3700039b 	tbnz	w27, #0, 37b8 <zbtreeScoreRaw+0x2b8>
    374c:	b9403369 	ldr	w9, [x27, #48]
    3750:	6b08013f 	cmp	w9, w8
    3754:	540000e0 	b.eq	3770 <zbtreeScoreRaw+0x270>  // b.none
    3758:	d0000060 	adrp	x0, 11000 <siphash+0x110>
    375c:	91264400 	add	x0, x0, #0x991
    3760:	5280f4a1 	mov	w1, #0x7a5                 	// #1957
    3764:	d0000062 	adrp	x2, 11000 <siphash+0x110>
    3768:	912ba842 	add	x2, x2, #0xaea
    376c:	940034ad 	bl	10a20 <standalone_panic>
    3770:	f94022c8 	ldr	x8, [x22, #64]
    3774:	b4000128 	cbz	x8, 3798 <zbtreeScoreRaw+0x298>
    3778:	79402f69 	ldrh	w9, [x27, #22]
    377c:	7940590a 	ldrh	w10, [x8, #44]
    3780:	eb1c011f 	cmp	x8, x28
    3784:	1a9f17e8 	cset	w8, eq	// eq = none
    3788:	6b0a013f 	cmp	w9, w10
    378c:	1a9f07e9 	cset	w9, ne	// ne = any
    3790:	6b09011f 	cmp	w8, w9
    3794:	54fffa20 	b.eq	36d8 <zbtreeScoreRaw+0x1d8>  // b.none
    3798:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    379c:	aa1b03e0 	mov	x0, x27
    37a0:	f94013e2 	ldr	x2, [sp, #32]
    37a4:	f85e83a3 	ldur	x3, [x29, #-24]
    37a8:	aa1f03e5 	mov	x5, xzr
    37ac:	94001dbf 	bl	aea8 <zbtScoreLeafFindMember>
    37b0:	34fff940 	cbz	w0, 36d8 <zbtreeScoreRaw+0x1d8>
    37b4:	140000a4 	b	3a44 <zbtreeScoreRaw+0x544>
    37b8:	f94022c8 	ldr	x8, [x22, #64]
    37bc:	b4fff828 	cbz	x8, 36c0 <zbtreeScoreRaw+0x1c0>
    37c0:	eb1c035f 	cmp	x26, x28
    37c4:	54fff8a0 	b.eq	36d8 <zbtreeScoreRaw+0x1d8>  // b.none
    37c8:	17ffffbe 	b	36c0 <zbtreeScoreRaw+0x1c0>
    37cc:	f94012c8 	ldr	x8, [x22, #32]
    37d0:	b4001368 	cbz	x8, 3a3c <zbtreeScoreRaw+0x53c>
    37d4:	f85f83ac 	ldur	x12, [x29, #-8]
    37d8:	910062cd 	add	x13, x22, #0x18
    37dc:	d100050f 	sub	x15, x8, #0x1
    37e0:	f9000fed 	str	x13, [sp, #24]
    37e4:	b200c3e8 	mov	x8, #0x101010101010101     	// #72340172838076673
    37e8:	aa1f03fc 	mov	x28, xzr
    37ec:	53187d89 	lsr	w9, w12, #24
    37f0:	d358fd8a 	lsr	x10, x12, #24
    37f4:	92407d90 	and	x16, x12, #0xffffffff
    37f8:	5280002c 	mov	w12, #0x1                   	// #1
    37fc:	d0000078 	adrp	x24, 11000 <siphash+0x110>
    3800:	91264718 	add	x24, x24, #0x991
    3804:	7100013f 	cmp	w9, #0x0
    3808:	8a1001f7 	and	x23, x15, x16
    380c:	529ffff9 	mov	w25, #0xffff                	// #65535
    3810:	1a9f1549 	csinc	w9, w10, wzr, ne	// ne = any
    3814:	d28f82aa 	mov	x10, #0x7c15                	// #31765
    3818:	a900bff0 	stp	x16, x15, [sp, #8]
    381c:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
    3820:	92401d2b 	and	x11, x9, #0xff
    3824:	9ac9218e 	lsl	x14, x12, x9
    3828:	f2cf372a 	movk	x10, #0x79b9, lsl #32
    382c:	9b087d74 	mul	x20, x11, x8
    3830:	12001d35 	and	w21, w9, #0xff
    3834:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
    3838:	9b0a7d6a 	mul	x10, x11, x10
    383c:	d37afd4d 	lsr	x13, x10, #58
    3840:	d364fd4a 	lsr	x10, x10, #36
    3844:	9acd2188 	lsl	x8, x12, x13
    3848:	9aca218a 	lsl	x10, x12, x10
    384c:	aa0e0108 	orr	x8, x8, x14
    3850:	aa0a0108 	orr	x8, x8, x10
    3854:	f90003e8 	str	x8, [sp]
    3858:	b9403ac8 	ldr	w8, [x22, #56]
    385c:	52800409 	mov	w9, #0x20                  	// #32
    3860:	7100011f 	cmp	w8, #0x0
    3864:	52800608 	mov	w8, #0x30                  	// #48
    3868:	9a880128 	csel	x8, x9, x8, eq	// eq = none
    386c:	f9400ec9 	ldr	x9, [x22, #24]
    3870:	9b17251a 	madd	x26, x8, x23, x9
    3874:	b207dbe9 	mov	x9, #0xfefefefefefefefe    	// #-72340172838076674
    3878:	f29fdfe9 	movk	x9, #0xfeff
    387c:	f9400348 	ldr	x8, [x26]
    3880:	ca140108 	eor	x8, x8, x20
    3884:	8b090109 	add	x9, x8, x9
    3888:	8a280128 	bic	x8, x9, x8
    388c:	f201c113 	ands	x19, x8, #0x8080808080808080
    3890:	54000601 	b.ne	3950 <zbtreeScoreRaw+0x450>  // b.any
    3894:	b500021c 	cbnz	x28, 38d4 <zbtreeScoreRaw+0x3d4>
    3898:	b9403ac9 	ldr	w9, [x22, #56]
    389c:	b94022c8 	ldr	w8, [x22, #32]
    38a0:	5280040a 	mov	w10, #0x20                  	// #32
    38a4:	7100013f 	cmp	w9, #0x0
    38a8:	f94007e9 	ldr	x9, [sp, #8]
    38ac:	51000508 	sub	w8, w8, #0x1
    38b0:	8a090108 	and	x8, x8, x9
    38b4:	52800609 	mov	w9, #0x30                  	// #48
    38b8:	9a890149 	csel	x9, x10, x9, eq	// eq = none
    38bc:	f9400eca 	ldr	x10, [x22, #24]
    38c0:	9ba82928 	umaddl	x8, w9, w8, x10
    38c4:	f94003e9 	ldr	x9, [sp]
    38c8:	f9400508 	ldr	x8, [x8, #8]
    38cc:	ea28013f 	bics	xzr, x9, x8
    38d0:	54000b61 	b.ne	3a3c <zbtreeScoreRaw+0x53c>  // b.any
    38d4:	f9400348 	ldr	x8, [x26]
    38d8:	92401d09 	and	x9, x8, #0xff
    38dc:	92781d0a 	and	x10, x8, #0xff00
    38e0:	f100013f 	cmp	x9, #0x0
    38e4:	92701d09 	and	x9, x8, #0xff0000
    38e8:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38ec:	92681d0a 	and	x10, x8, #0xff000000
    38f0:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    38f4:	92601d09 	and	x9, x8, #0xff00000000
    38f8:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    38fc:	92581d0a 	and	x10, x8, #0xff0000000000
    3900:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3904:	92501d09 	and	x9, x8, #0xff000000000000
    3908:	d378fd08 	lsr	x8, x8, #56
    390c:	fa401944 	ccmp	x10, #0x0, #0x4, ne	// ne = any
    3910:	fa401924 	ccmp	x9, #0x0, #0x4, ne	// ne = any
    3914:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
    3918:	54000920 	b.eq	3a3c <zbtreeScoreRaw+0x53c>  // b.none
    391c:	f94012c8 	ldr	x8, [x22, #32]
    3920:	9100079c 	add	x28, x28, #0x1
    3924:	910006e9 	add	x9, x23, #0x1
    3928:	eb08039f 	cmp	x28, x8
    392c:	f9400be8 	ldr	x8, [sp, #16]
    3930:	8a080137 	and	x23, x9, x8
    3934:	54fff923 	b.cc	3858 <zbtreeScoreRaw+0x358>  // b.lo, b.ul, b.last
    3938:	14000041 	b	3a3c <zbtreeScoreRaw+0x53c>
    393c:	f94022c8 	ldr	x8, [x22, #64]
    3940:	b4000728 	cbz	x8, 3a24 <zbtreeScoreRaw+0x524>
    3944:	d1000668 	sub	x8, x19, #0x1
    3948:	ea130113 	ands	x19, x8, x19
    394c:	54fffa40 	b.eq	3894 <zbtreeScoreRaw+0x394>  // b.none
    3950:	dac00268 	rbit	x8, x19
    3954:	f9400349 	ldr	x9, [x26]
    3958:	dac01108 	clz	x8, x8
    395c:	927d090a 	and	x10, x8, #0x38
    3960:	9aca2529 	lsr	x9, x9, x10
    3964:	6b2902bf 	cmp	w21, w9, uxtb
    3968:	54fffee1 	b.ne	3944 <zbtreeScoreRaw+0x444>  // b.any
    396c:	b9403ac9 	ldr	w9, [x22, #56]
    3970:	d343fd08 	lsr	x8, x8, #3
    3974:	340000c9 	cbz	w9, 398c <zbtreeScoreRaw+0x48c>
    3978:	8b080b48 	add	x8, x26, x8, lsl #2
    397c:	b9401108 	ldr	w8, [x8, #16]
    3980:	3100051f 	cmn	w8, #0x1
    3984:	540000c1 	b.ne	399c <zbtreeScoreRaw+0x49c>  // b.any
    3988:	17ffffef 	b	3944 <zbtreeScoreRaw+0x444>
    398c:	8b080748 	add	x8, x26, x8, lsl #1
    3990:	79402108 	ldrh	w8, [x8, #16]
    3994:	6b19011f 	cmp	w8, w25
    3998:	54fffd60 	b.eq	3944 <zbtreeScoreRaw+0x444>  // b.none
    399c:	b94056c9 	ldr	w9, [x22, #84]
    39a0:	6b09011f 	cmp	w8, w9
    39a4:	54fffcc2 	b.cs	393c <zbtreeScoreRaw+0x43c>  // b.hs, b.nlast
    39a8:	f94026c9 	ldr	x9, [x22, #72]
    39ac:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
    39b0:	b4fffc7b 	cbz	x27, 393c <zbtreeScoreRaw+0x43c>
    39b4:	3707fc5b 	tbnz	w27, #0, 393c <zbtreeScoreRaw+0x43c>
    39b8:	b9403369 	ldr	w9, [x27, #48]
    39bc:	6b08013f 	cmp	w9, w8
    39c0:	540000c0 	b.eq	39d8 <zbtreeScoreRaw+0x4d8>  // b.none
    39c4:	aa1803e0 	mov	x0, x24
    39c8:	5280f4a1 	mov	w1, #0x7a5                 	// #1957
    39cc:	d0000062 	adrp	x2, 11000 <siphash+0x110>
    39d0:	912ba842 	add	x2, x2, #0xaea
    39d4:	94003413 	bl	10a20 <standalone_panic>
    39d8:	f94022c8 	ldr	x8, [x22, #64]
    39dc:	b4000148 	cbz	x8, 3a04 <zbtreeScoreRaw+0x504>
    39e0:	f9400feb 	ldr	x11, [sp, #24]
    39e4:	79402f69 	ldrh	w9, [x27, #22]
    39e8:	7940590a 	ldrh	w10, [x8, #44]
    39ec:	eb0b011f 	cmp	x8, x11
    39f0:	1a9f17e8 	cset	w8, eq	// eq = none
    39f4:	6b0a013f 	cmp	w9, w10
    39f8:	1a9f07e9 	cset	w9, ne	// ne = any
    39fc:	6b09011f 	cmp	w8, w9
    3a00:	54fffa20 	b.eq	3944 <zbtreeScoreRaw+0x444>  // b.none
    3a04:	a97f07a4 	ldp	x4, x1, [x29, #-16]
    3a08:	aa1b03e0 	mov	x0, x27
    3a0c:	f94013e2 	ldr	x2, [sp, #32]
    3a10:	f85e83a3 	ldur	x3, [x29, #-24]
    3a14:	aa1f03e5 	mov	x5, xzr
    3a18:	94001d24 	bl	aea8 <zbtScoreLeafFindMember>
    3a1c:	34fff940 	cbz	w0, 3944 <zbtreeScoreRaw+0x444>
    3a20:	14000009 	b	3a44 <zbtreeScoreRaw+0x544>
    3a24:	aa1803e0 	mov	x0, x24
    3a28:	5280f421 	mov	w1, #0x7a1                 	// #1953
    3a2c:	d0000062 	adrp	x2, 11000 <siphash+0x110>
    3a30:	912c2442 	add	x2, x2, #0xb09
    3a34:	940033fb 	bl	10a20 <standalone_panic>
    3a38:	17ffffc3 	b	3944 <zbtreeScoreRaw+0x444>
    3a3c:	2a1f03e0 	mov	w0, wzr
    3a40:	14000002 	b	3a48 <zbtreeScoreRaw+0x548>
    3a44:	52800020 	mov	w0, #0x1                   	// #1
    3a48:	a9494ff4 	ldp	x20, x19, [sp, #144]
    3a4c:	a94857f6 	ldp	x22, x21, [sp, #128]
    3a50:	a9475ff8 	ldp	x24, x23, [sp, #112]
    3a54:	a94667fa 	ldp	x26, x25, [sp, #96]
    3a58:	a9456ffc 	ldp	x28, x27, [sp, #80]
    3a5c:	a9447bfd 	ldp	x29, x30, [sp, #64]
    3a60:	910283ff 	add	sp, sp, #0xa0
    3a64:	d65f03c0 	ret

Disassembly of section .fini:
