_decoder_batch:                         ; @decoder_batch
Lfunc_begin56:
; %bb.0:
	stp	d15, d14, [sp, #-160]!          ; 16-byte Folded Spill
	stp	d13, d12, [sp, #16]             ; 16-byte Folded Spill
	stp	d11, d10, [sp, #32]             ; 16-byte Folded Spill
	stp	d9, d8, [sp, #48]               ; 16-byte Folded Spill
	stp	x28, x27, [sp, #64]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #80]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #96]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #112]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #128]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #144]            ; 16-byte Folded Spill
	add	x29, sp, #144
	sub	sp, sp, #784
Lloh343:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh344:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh345:
	ldr	x8, [x8]
	stur	x8, [x29, #-160]
Ltmp4567:
	cbz	w1, LBB56_75
Ltmp4568:
; %bb.1:
	mov	x4, #0                          ; =0x0
	mov	w8, #0                          ; =0x0
	mov	x17, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	x3, #0                          ; =0x0
	mov	x9, sp
	add	x10, x9, #16
	add	x11, x9, #128
	add	x12, x9, #32
	mov	x13, #-1                        ; =0xffffffffffffffff
	mov	w14, #64                        ; =0x40
	mov	w15, #-3                        ; =0xfffffffd
	b	LBB56_3
Ltmp4569:
LBB56_2:                                ;   in Loop: Header=BB56_3 Depth=1
	add	w8, w8, #1
Ltmp4570:
	cmp	w8, w1
	b.eq	LBB56_73
Ltmp4571:
LBB56_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB56_6 Depth 2
                                        ;       Child Loop BB56_26 Depth 3
                                        ;       Child Loop BB56_15 Depth 3
                                        ;       Child Loop BB56_61 Depth 3
                                        ;       Child Loop BB56_64 Depth 3
                                        ;       Child Loop BB56_69 Depth 3
                                        ;       Child Loop BB56_72 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4572:
	ldr	w16, [x0, #4]
Ltmp4573:
	cbz	w16, LBB56_2
Ltmp4574:
; %bb.4:                                ;   in Loop: Header=BB56_3 Depth=1
	mov	x16, #0                         ; =0x0
Ltmp4575:
	ldr	w5, [x0]
	b	LBB56_6
Ltmp4576:
LBB56_5:                                ;   in Loop: Header=BB56_6 Depth=2
	add	x16, x16, #1
Ltmp4577:
	ldr	w6, [x0, #4]
Ltmp4578:
	cmp	x16, x6
	b.hs	LBB56_2
Ltmp4579:
LBB56_6:                                ;   Parent Loop BB56_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB56_26 Depth 3
                                        ;       Child Loop BB56_15 Depth 3
                                        ;       Child Loop BB56_61 Depth 3
                                        ;       Child Loop BB56_64 Depth 3
                                        ;       Child Loop BB56_69 Depth 3
                                        ;       Child Loop BB56_72 Depth 3
	cbz	x5, LBB56_10
Ltmp4580:
; %bb.7:                                ;   in Loop: Header=BB56_6 Depth=2
	ldr	x6, [x0, #8]
	ldr	x6, [x6, x16, lsl #3]
Ltmp4581:
	add	x7, x6, #56
	ldr	x19, [x6, #40]
	cmp	x5, #4
	b.hs	LBB56_23
Ltmp4582:
; %bb.8:                                ;   in Loop: Header=BB56_6 Depth=2
	mov	x20, #0                         ; =0x0
Ltmp4583:
LBB56_9:                                ;   in Loop: Header=BB56_6 Depth=2
	and	x5, x5, #0x3
Ltmp4584:
	cbnz	x5, LBB56_15
Ltmp4585:
LBB56_10:                               ;   in Loop: Header=BB56_6 Depth=2
	; InlineAsm Start
	; InlineAsm End
Ltmp4586:
	ldr	w5, [x0]
Ltmp4587:
	cmp	w5, #4
	b.lo	LBB56_22
Ltmp4588:
; %bb.11:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x6, x5, #0xfffffffc
	sub	x7, x5, #4
	cmp	x7, #27
	b.hi	LBB56_60
Ltmp4589:
; %bb.12:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x7, #0                          ; =0x0
	b	LBB56_63
Ltmp4590:
LBB56_13:                               ;   in Loop: Header=BB56_15 Depth=3
	lsl	x24, x13, x22
	cmp	w22, #64
	csinv	x22, x13, x24, hs
Ltmp4591:
	and	x22, x23, x22
Ltmp4592:
	ldrb	w23, [x6, #19]
	lsl	x22, x22, x23
Ltmp4593:
LBB56_14:                               ;   in Loop: Header=BB56_15 Depth=3
	cmp	w21, #0
	cneg	x21, x22, ne
	add	x21, x21, x19
Ltmp4594:
	and	x22, x21, #0x7fffffffffffffff
Ltmp4595:
	cmp	x21, #0
	csinv	x21, x22, x21, lt
Ltmp4596:
	str	x21, [x9, x20, lsl #3]
	add	x20, x20, #1
Ltmp4597:
	subs	x5, x5, #1
	b.eq	LBB56_10
Ltmp4598:
LBB56_15:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w22, [x6, #52]
Ltmp4599:
	ldrb	w21, [x6, #53]
	cbz	w22, LBB56_21
Ltmp4600:
; %bb.16:                               ;   in Loop: Header=BB56_15 Depth=3
	mov	x23, x20
Ltmp4601:
	cbz	w21, LBB56_18
Ltmp4602:
; %bb.17:                               ;   in Loop: Header=BB56_15 Depth=3
	ldrb	w23, [x6, #17]
	eor	x24, x20, #0xffffffff
	add	x23, x24, x23
Ltmp4603:
LBB56_18:                               ;   in Loop: Header=BB56_15 Depth=3
	mov	w23, w23
	umull	x25, w23, w22
Ltmp4604:
	lsr	x24, x25, #3
Ltmp4605:
	ldr	x23, [x7, x24]
Ltmp4606:
	and	x26, x25, #0x7
	lsr	x23, x23, x26
Ltmp4607:
	ands	w25, w25, #0x7
Ltmp4608:
	b.eq	LBB56_13
Ltmp4609:
; %bb.19:                               ;   in Loop: Header=BB56_15 Depth=3
	sub	w25, w14, w25
Ltmp4610:
	cmp	w25, w22
	b.hs	LBB56_13
Ltmp4611:
; %bb.20:                               ;   in Loop: Header=BB56_15 Depth=3
	add	x24, x24, x7
Ltmp4612:
	ldrb	w24, [x24, #8]
	lsl	x24, x24, x25
	orr	x23, x24, x23
Ltmp4613:
	b	LBB56_13
Ltmp4614:
LBB56_21:                               ;   in Loop: Header=BB56_15 Depth=3
	mov	x22, #0                         ; =0x0
Ltmp4615:
	b	LBB56_14
Ltmp4616:
LBB56_22:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x6, #0                          ; =0x0
Ltmp4617:
	b	LBB56_65
Ltmp4618:
LBB56_23:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x20, #0                         ; =0x0
Ltmp4619:
	and	x21, x5, #0xfffffffc
	mov	x22, x10
	b	LBB56_26
Ltmp4620:
LBB56_24:                               ;   in Loop: Header=BB56_26 Depth=3
	lsl	x26, x13, x24
	cmp	w24, #64
	csinv	x24, x13, x26, hs
Ltmp4621:
	and	x24, x25, x24
Ltmp4622:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4623:
LBB56_25:                               ;   in Loop: Header=BB56_26 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4624:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4625:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4626:
	str	x23, [x22, #8]
	add	x20, x20, #4
Ltmp4627:
	add	x22, x22, #32
	cmp	x21, x20
	b.eq	LBB56_9
Ltmp4628:
LBB56_26:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w24, [x6, #52]
Ltmp4629:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_33
Ltmp4630:
; %bb.27:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	x25, x20
Ltmp4631:
	cbz	w23, LBB56_29
Ltmp4632:
; %bb.28:                               ;   in Loop: Header=BB56_26 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xffffffff
	add	x25, x26, x25
Ltmp4633:
LBB56_29:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4634:
	lsr	x26, x27, #3
Ltmp4635:
	ldr	x25, [x7, x26]
Ltmp4636:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4637:
	ands	w27, w27, #0x7
Ltmp4638:
	b.eq	LBB56_32
Ltmp4639:
; %bb.30:                               ;   in Loop: Header=BB56_26 Depth=3
	sub	w27, w14, w27
Ltmp4640:
	cmp	w27, w24
	b.hs	LBB56_32
Ltmp4641:
; %bb.31:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x26, x26, x7
Ltmp4642:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4643:
LBB56_32:                               ;   in Loop: Header=BB56_26 Depth=3
	lsl	x26, x13, x24
	cmp	w24, #64
	csinv	x24, x13, x26, hs
Ltmp4644:
	and	x24, x25, x24
Ltmp4645:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4646:
	b	LBB56_34
Ltmp4647:
LBB56_33:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4648:
LBB56_34:                               ;   in Loop: Header=BB56_26 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4649:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4650:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4651:
	stur	x23, [x22, #-16]
Ltmp4652:
	ldrb	w24, [x6, #52]
Ltmp4653:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_37
Ltmp4654:
; %bb.35:                               ;   in Loop: Header=BB56_26 Depth=3
	cbz	w23, LBB56_38
Ltmp4655:
; %bb.36:                               ;   in Loop: Header=BB56_26 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xfffffffe
	add	x25, x26, x25
	b	LBB56_39
Ltmp4656:
LBB56_37:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4657:
	b	LBB56_43
Ltmp4658:
LBB56_38:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x25, x20, #1
Ltmp4659:
LBB56_39:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4660:
	lsr	x26, x27, #3
Ltmp4661:
	ldr	x25, [x7, x26]
Ltmp4662:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4663:
	ands	w27, w27, #0x7
Ltmp4664:
	b.eq	LBB56_42
Ltmp4665:
; %bb.40:                               ;   in Loop: Header=BB56_26 Depth=3
	sub	w27, w14, w27
Ltmp4666:
	cmp	w27, w24
	b.hs	LBB56_42
Ltmp4667:
; %bb.41:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x26, x26, x7
Ltmp4668:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4669:
LBB56_42:                               ;   in Loop: Header=BB56_26 Depth=3
	lsl	x26, x13, x24
	cmp	w24, #64
	csinv	x24, x13, x26, hs
Ltmp4670:
	and	x24, x25, x24
Ltmp4671:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4672:
LBB56_43:                               ;   in Loop: Header=BB56_26 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4673:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4674:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4675:
	stur	x23, [x22, #-8]
Ltmp4676:
	ldrb	w24, [x6, #52]
Ltmp4677:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_46
Ltmp4678:
; %bb.44:                               ;   in Loop: Header=BB56_26 Depth=3
	cbz	w23, LBB56_47
Ltmp4679:
; %bb.45:                               ;   in Loop: Header=BB56_26 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, x15
	add	x25, x26, x25
	b	LBB56_48
Ltmp4680:
LBB56_46:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4681:
	b	LBB56_52
Ltmp4682:
LBB56_47:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x25, x20, #2
Ltmp4683:
LBB56_48:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4684:
	lsr	x26, x27, #3
Ltmp4685:
	ldr	x25, [x7, x26]
Ltmp4686:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4687:
	ands	w27, w27, #0x7
Ltmp4688:
	b.eq	LBB56_51
Ltmp4689:
; %bb.49:                               ;   in Loop: Header=BB56_26 Depth=3
	sub	w27, w14, w27
Ltmp4690:
	cmp	w27, w24
	b.hs	LBB56_51
Ltmp4691:
; %bb.50:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x26, x26, x7
Ltmp4692:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4693:
LBB56_51:                               ;   in Loop: Header=BB56_26 Depth=3
	lsl	x26, x13, x24
	cmp	w24, #64
	csinv	x24, x13, x26, hs
Ltmp4694:
	and	x24, x25, x24
Ltmp4695:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4696:
LBB56_52:                               ;   in Loop: Header=BB56_26 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4697:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4698:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4699:
	str	x23, [x22]
Ltmp4700:
	ldrb	w24, [x6, #52]
Ltmp4701:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_55
Ltmp4702:
; %bb.53:                               ;   in Loop: Header=BB56_26 Depth=3
	cbz	w23, LBB56_56
Ltmp4703:
; %bb.54:                               ;   in Loop: Header=BB56_26 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xfffffffc
	add	x25, x26, x25
	b	LBB56_57
Ltmp4704:
LBB56_55:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4705:
	b	LBB56_25
Ltmp4706:
LBB56_56:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x25, x20, #3
Ltmp4707:
LBB56_57:                               ;   in Loop: Header=BB56_26 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4708:
	lsr	x26, x27, #3
Ltmp4709:
	ldr	x25, [x7, x26]
Ltmp4710:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4711:
	ands	w27, w27, #0x7
Ltmp4712:
	b.eq	LBB56_24
Ltmp4713:
; %bb.58:                               ;   in Loop: Header=BB56_26 Depth=3
	sub	w27, w14, w27
Ltmp4714:
	cmp	w27, w24
	b.hs	LBB56_24
Ltmp4715:
; %bb.59:                               ;   in Loop: Header=BB56_26 Depth=3
	add	x26, x26, x7
Ltmp4716:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4717:
	b	LBB56_24
Ltmp4718:
LBB56_60:                               ;   in Loop: Header=BB56_6 Depth=2
	lsr	x7, x7, #2
	add	x19, x7, #1
	and	x20, x19, #0x7ffffffffffffff8
	lsl	x7, x20, #2
	movi.2d	v3, #0000000000000000
	movi.2d	v4, #0000000000000000
	mov.d	v4[0], x4
	movi.2d	v2, #0000000000000000
	mov.d	v2[0], x17
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x2
	movi.2d	v0, #0000000000000000
	mov.d	v0[0], x3
	mov	x17, x20
Ltmp4719:
	movi.2d	v22, #0000000000000000
	mov	x2, x11
Ltmp4720:
	movi.2d	v23, #0000000000000000
	movi.2d	v19, #0000000000000000
	movi.2d	v20, #0000000000000000
	movi.2d	v21, #0000000000000000
	movi.2d	v16, #0000000000000000
	movi.2d	v17, #0000000000000000
	movi.2d	v18, #0000000000000000
	movi.2d	v5, #0000000000000000
	movi.2d	v6, #0000000000000000
	movi.2d	v7, #0000000000000000
Ltmp4721:
LBB56_61:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	sub	x3, x2, #128
	sub	x4, x2, #64
	ld4.2d	{ v24, v25, v26, v27 }, [x3]
	ld4.2d	{ v28, v29, v30, v31 }, [x4]
	mov	x3, x2
	ld4.2d	{ v8, v9, v10, v11 }, [x3], #64
	ld4.2d	{ v12, v13, v14, v15 }, [x3]
	add.2d	v4, v24, v4
	add.2d	v3, v28, v3
	add.2d	v22, v8, v22
	add.2d	v23, v12, v23
	add.2d	v0, v25, v0
	add.2d	v5, v29, v5
	add.2d	v6, v9, v6
	add.2d	v7, v13, v7
	add.2d	v1, v26, v1
	add.2d	v16, v30, v16
	add.2d	v17, v10, v17
	add.2d	v18, v14, v18
	add.2d	v2, v27, v2
	add.2d	v19, v31, v19
	add.2d	v20, v11, v20
	add.2d	v21, v15, v21
	add	x2, x2, #256
	subs	x17, x17, #8
	b.ne	LBB56_61
Ltmp4722:
; %bb.62:                               ;   in Loop: Header=BB56_6 Depth=2
	add.2d	v3, v3, v4
	add.2d	v3, v22, v3
	add.2d	v3, v23, v3
	addp.2d	d3, v3
	fmov	x4, d3
	add.2d	v2, v19, v2
	add.2d	v2, v20, v2
	add.2d	v2, v21, v2
	addp.2d	d2, v2
	fmov	x17, d2
	add.2d	v1, v16, v1
	add.2d	v1, v17, v1
	add.2d	v1, v18, v1
	addp.2d	d1, v1
	fmov	x2, d1
	add.2d	v0, v5, v0
	add.2d	v0, v6, v0
	add.2d	v0, v7, v0
	addp.2d	d0, v0
	fmov	x3, d0
	cmp	x19, x20
	b.eq	LBB56_65
Ltmp4723:
LBB56_63:                               ;   in Loop: Header=BB56_6 Depth=2
	add	x19, x7, #3
	add	x7, x10, x7, lsl #3
Ltmp4724:
LBB56_64:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	x20, x21, [x7, #-16]
	add	x4, x20, x4
Ltmp4725:
	add	x3, x21, x3
Ltmp4726:
	ldp	x20, x21, [x7], #32
	add	x2, x20, x2
Ltmp4727:
	add	x17, x21, x17
Ltmp4728:
	add	x19, x19, #4
Ltmp4729:
	cmp	x19, x5
	b.lo	LBB56_64
Ltmp4730:
LBB56_65:                               ;   in Loop: Header=BB56_6 Depth=2
	cmp	x6, x5
	b.hs	LBB56_5
Ltmp4731:
; %bb.66:                               ;   in Loop: Header=BB56_6 Depth=2
	sub	x19, x5, x6
	cmp	x19, #7
	b.hi	LBB56_68
Ltmp4732:
; %bb.67:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x7, x6
	b	LBB56_71
Ltmp4733:
LBB56_68:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x20, x19, #0xfffffffffffffff8
	add	x7, x20, x6
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x4
	add	x4, x12, x6, lsl #3
Ltmp4734:
	mov	x6, x20
Ltmp4735:
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
Ltmp4736:
LBB56_69:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	q4, q5, [x4, #-32]
	ldp	q6, q7, [x4], #64
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	subs	x6, x6, #8
	b.ne	LBB56_69
Ltmp4737:
; %bb.70:                               ;   in Loop: Header=BB56_6 Depth=2
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x4, d0
	cmp	x19, x20
	b.eq	LBB56_5
Ltmp4738:
LBB56_71:                               ;   in Loop: Header=BB56_6 Depth=2
	add	x6, x9, x7, lsl #3
	sub	x7, x5, x7
Ltmp4739:
LBB56_72:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	x19, [x6], #8
	add	x4, x19, x4
Ltmp4740:
	subs	x7, x7, #1
	b.ne	LBB56_72
	b	LBB56_5
Ltmp4741:
LBB56_73:
	add	x8, x2, x3
	add	x9, x17, x4
	add	x0, x8, x9
Ltmp4742:
	ldur	x8, [x29, #-160]
Lloh346:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh347:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh348:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB56_76
Ltmp4743:
LBB56_74:
	add	sp, sp, #784
	ldp	x29, x30, [sp, #144]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #128]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #112]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #96]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #80]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #64]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp, #48]               ; 16-byte Folded Reload
	ldp	d11, d10, [sp, #32]             ; 16-byte Folded Reload
	ldp	d13, d12, [sp, #16]             ; 16-byte Folded Reload
	ldp	d15, d14, [sp], #160            ; 16-byte Folded Reload
	ret
Ltmp4744:
LBB56_75:
	mov	x0, #0                          ; =0x0
Ltmp4745:
	ldur	x8, [x29, #-160]
Lloh349:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh350:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh351:
	ldr	x9, [x9]
	cmp	x9, x8
	b.eq	LBB56_74
Ltmp4746:
LBB56_76:
	bl	___stack_chk_fail
Ltmp4747:
	.loh AdrpLdrGotLdr	Lloh343, Lloh344, Lloh345
	.loh AdrpLdrGotLdr	Lloh346, Lloh347, Lloh348
	.loh AdrpLdrGotLdr	Lloh349, Lloh350, Lloh351
Lfunc_end56:
