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
Lloh339:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh340:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh341:
	ldr	x8, [x8]
	stur	x8, [x29, #-160]
Ltmp4561:
	cbz	w1, LBB56_115
Ltmp4562:
; %bb.1:
	mov	x4, #0                          ; =0x0
	mov	w8, #0                          ; =0x0
	mov	x17, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	x3, #0                          ; =0x0
	mov	w9, #-3                         ; =0xfffffffd
	mov	x10, sp
	add	x11, x10, #16
	add	x12, x10, #32
	add	x13, x10, #128
	mov	x14, #-1                        ; =0xffffffffffffffff
	mov	w15, #64                        ; =0x40
	b	LBB56_3
Ltmp4563:
LBB56_2:                                ;   in Loop: Header=BB56_3 Depth=1
	add	w8, w8, #1
Ltmp4564:
	cmp	w8, w1
	b.eq	LBB56_113
Ltmp4565:
LBB56_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB56_6 Depth 2
                                        ;       Child Loop BB56_30 Depth 3
                                        ;       Child Loop BB56_20 Depth 3
                                        ;       Child Loop BB56_69 Depth 3
                                        ;       Child Loop BB56_13 Depth 3
                                        ;       Child Loop BB56_92 Depth 3
                                        ;       Child Loop BB56_95 Depth 3
                                        ;       Child Loop BB56_101 Depth 3
                                        ;       Child Loop BB56_104 Depth 3
                                        ;       Child Loop BB56_109 Depth 3
                                        ;       Child Loop BB56_112 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4566:
	ldr	w16, [x0, #4]
Ltmp4567:
	cbz	w16, LBB56_2
Ltmp4568:
; %bb.4:                                ;   in Loop: Header=BB56_3 Depth=1
	mov	x16, #0                         ; =0x0
Ltmp4569:
	ldr	w5, [x0]
	b	LBB56_6
Ltmp4570:
LBB56_5:                                ;   in Loop: Header=BB56_6 Depth=2
	add	x16, x16, #1
Ltmp4571:
	ldr	w6, [x0, #4]
Ltmp4572:
	cmp	x16, x6
	b.hs	LBB56_2
Ltmp4573:
LBB56_6:                                ;   Parent Loop BB56_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB56_30 Depth 3
                                        ;       Child Loop BB56_20 Depth 3
                                        ;       Child Loop BB56_69 Depth 3
                                        ;       Child Loop BB56_13 Depth 3
                                        ;       Child Loop BB56_92 Depth 3
                                        ;       Child Loop BB56_95 Depth 3
                                        ;       Child Loop BB56_101 Depth 3
                                        ;       Child Loop BB56_104 Depth 3
                                        ;       Child Loop BB56_109 Depth 3
                                        ;       Child Loop BB56_112 Depth 3
	cbz	x5, LBB56_96
Ltmp4574:
; %bb.7:                                ;   in Loop: Header=BB56_6 Depth=2
	ldr	x6, [x0, #8]
	ldr	x6, [x6, x16, lsl #3]
Ltmp4575:
	ldrb	w19, [x6, #52]
Ltmp4576:
	and	w20, w19, #0x3
	add	x7, x6, #56
Ltmp4577:
	cmp	w19, #59
	ccmp	w20, #0, #4, hs
	b.ne	LBB56_15
Ltmp4578:
; %bb.8:                                ;   in Loop: Header=BB56_6 Depth=2
	lsl	x20, x14, x19
	cmp	w19, #64
	csinv	x20, x14, x20, hs
	cbz	w19, LBB56_64
Ltmp4579:
; %bb.9:                                ;   in Loop: Header=BB56_6 Depth=2
	ldrb	w21, [x6, #19]
	ldr	x22, [x6, #40]
Ltmp4580:
	cmp	x5, #8
	b.hs	LBB56_66
Ltmp4581:
; %bb.10:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x23, #0                         ; =0x0
Ltmp4582:
LBB56_11:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x5, x5, #0x7
Ltmp4583:
	cbnz	x5, LBB56_13
	b	LBB56_96
Ltmp4584:
LBB56_12:                               ;   in Loop: Header=BB56_13 Depth=3
	mov	w25, w25
	umull	x25, w25, w19
Ltmp4585:
	lsr	x26, x25, #3
Ltmp4586:
	and	x25, x25, #0x7
Ltmp4587:
	ldr	x26, [x7, x26]
Ltmp4588:
	lsr	x25, x26, x25
Ltmp4589:
	and	x25, x25, x20
Ltmp4590:
	lsl	x25, x25, x21
Ltmp4591:
	cmp	w24, #0
	cneg	x24, x25, ne
	add	x24, x24, x22
Ltmp4592:
	and	x25, x24, #0x7fffffffffffffff
	cmp	x24, #0
	csinv	x24, x25, x24, lt
Ltmp4593:
	str	x24, [x10, x23, lsl #3]
Ltmp4594:
	add	x23, x23, #1
Ltmp4595:
	subs	x5, x5, #1
	b.eq	LBB56_96
Ltmp4596:
LBB56_13:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w24, [x6, #53]
	mov	x25, x23
	cbz	w24, LBB56_12
Ltmp4597:
; %bb.14:                               ;   in Loop: Header=BB56_13 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x23, #0xffffffff
	add	x25, x26, x25
	b	LBB56_12
Ltmp4598:
LBB56_15:                               ;   in Loop: Header=BB56_6 Depth=2
	ldr	x19, [x6, #40]
Ltmp4599:
	cmp	x5, #4
	b.hs	LBB56_27
Ltmp4600:
; %bb.16:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x20, #0                         ; =0x0
Ltmp4601:
LBB56_17:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x5, x5, #0x3
Ltmp4602:
	cbnz	x5, LBB56_20
	b	LBB56_96
Ltmp4603:
LBB56_18:                               ;   in Loop: Header=BB56_20 Depth=3
	lsl	x24, x14, x22
	cmp	w22, #64
	csinv	x22, x14, x24, hs
Ltmp4604:
	and	x22, x23, x22
Ltmp4605:
	ldrb	w23, [x6, #19]
	lsl	x22, x22, x23
Ltmp4606:
LBB56_19:                               ;   in Loop: Header=BB56_20 Depth=3
	cmp	w21, #0
	cneg	x21, x22, ne
	add	x21, x21, x19
Ltmp4607:
	and	x22, x21, #0x7fffffffffffffff
Ltmp4608:
	cmp	x21, #0
	csinv	x21, x22, x21, lt
Ltmp4609:
	str	x21, [x10, x20, lsl #3]
	add	x20, x20, #1
Ltmp4610:
	subs	x5, x5, #1
	b.eq	LBB56_96
Ltmp4611:
LBB56_20:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w22, [x6, #52]
Ltmp4612:
	ldrb	w21, [x6, #53]
	cbz	w22, LBB56_26
Ltmp4613:
; %bb.21:                               ;   in Loop: Header=BB56_20 Depth=3
	mov	x23, x20
Ltmp4614:
	cbz	w21, LBB56_23
Ltmp4615:
; %bb.22:                               ;   in Loop: Header=BB56_20 Depth=3
	ldrb	w23, [x6, #17]
	eor	x24, x20, #0xffffffff
	add	x23, x24, x23
Ltmp4616:
LBB56_23:                               ;   in Loop: Header=BB56_20 Depth=3
	mov	w23, w23
	umull	x25, w23, w22
Ltmp4617:
	lsr	x24, x25, #3
Ltmp4618:
	ldr	x23, [x7, x24]
Ltmp4619:
	and	x26, x25, #0x7
	lsr	x23, x23, x26
Ltmp4620:
	ands	w25, w25, #0x7
Ltmp4621:
	b.eq	LBB56_18
Ltmp4622:
; %bb.24:                               ;   in Loop: Header=BB56_20 Depth=3
	sub	w25, w15, w25
Ltmp4623:
	cmp	w25, w22
	b.hs	LBB56_18
Ltmp4624:
; %bb.25:                               ;   in Loop: Header=BB56_20 Depth=3
	add	x24, x24, x7
Ltmp4625:
	ldrb	w24, [x24, #8]
	lsl	x24, x24, x25
	orr	x23, x24, x23
Ltmp4626:
	b	LBB56_18
Ltmp4627:
LBB56_26:                               ;   in Loop: Header=BB56_20 Depth=3
	mov	x22, #0                         ; =0x0
Ltmp4628:
	b	LBB56_19
Ltmp4629:
LBB56_27:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x20, #0                         ; =0x0
	and	x21, x5, #0xfffffffc
	mov	x22, x11
	b	LBB56_30
Ltmp4630:
LBB56_28:                               ;   in Loop: Header=BB56_30 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4631:
	and	x24, x25, x24
Ltmp4632:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4633:
LBB56_29:                               ;   in Loop: Header=BB56_30 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4634:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4635:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4636:
	str	x23, [x22, #8]
	add	x20, x20, #4
Ltmp4637:
	add	x22, x22, #32
	cmp	x21, x20
	b.eq	LBB56_17
Ltmp4638:
LBB56_30:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w24, [x6, #52]
Ltmp4639:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_37
Ltmp4640:
; %bb.31:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	x25, x20
Ltmp4641:
	cbz	w23, LBB56_33
Ltmp4642:
; %bb.32:                               ;   in Loop: Header=BB56_30 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xffffffff
	add	x25, x26, x25
Ltmp4643:
LBB56_33:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4644:
	lsr	x26, x27, #3
Ltmp4645:
	ldr	x25, [x7, x26]
Ltmp4646:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4647:
	ands	w27, w27, #0x7
Ltmp4648:
	b.eq	LBB56_36
Ltmp4649:
; %bb.34:                               ;   in Loop: Header=BB56_30 Depth=3
	sub	w27, w15, w27
Ltmp4650:
	cmp	w27, w24
	b.hs	LBB56_36
Ltmp4651:
; %bb.35:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x26, x26, x7
Ltmp4652:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4653:
LBB56_36:                               ;   in Loop: Header=BB56_30 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4654:
	and	x24, x25, x24
Ltmp4655:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4656:
	b	LBB56_38
Ltmp4657:
LBB56_37:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4658:
LBB56_38:                               ;   in Loop: Header=BB56_30 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4659:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4660:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4661:
	stur	x23, [x22, #-16]
Ltmp4662:
	ldrb	w24, [x6, #52]
Ltmp4663:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_41
Ltmp4664:
; %bb.39:                               ;   in Loop: Header=BB56_30 Depth=3
	cbz	w23, LBB56_42
Ltmp4665:
; %bb.40:                               ;   in Loop: Header=BB56_30 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xfffffffe
	add	x25, x26, x25
	b	LBB56_43
Ltmp4666:
LBB56_41:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4667:
	b	LBB56_47
Ltmp4668:
LBB56_42:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x25, x20, #1
Ltmp4669:
LBB56_43:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4670:
	lsr	x26, x27, #3
Ltmp4671:
	ldr	x25, [x7, x26]
Ltmp4672:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4673:
	ands	w27, w27, #0x7
Ltmp4674:
	b.eq	LBB56_46
Ltmp4675:
; %bb.44:                               ;   in Loop: Header=BB56_30 Depth=3
	sub	w27, w15, w27
Ltmp4676:
	cmp	w27, w24
	b.hs	LBB56_46
Ltmp4677:
; %bb.45:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x26, x26, x7
Ltmp4678:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4679:
LBB56_46:                               ;   in Loop: Header=BB56_30 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4680:
	and	x24, x25, x24
Ltmp4681:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4682:
LBB56_47:                               ;   in Loop: Header=BB56_30 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4683:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4684:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4685:
	stur	x23, [x22, #-8]
Ltmp4686:
	ldrb	w24, [x6, #52]
Ltmp4687:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_50
Ltmp4688:
; %bb.48:                               ;   in Loop: Header=BB56_30 Depth=3
	cbz	w23, LBB56_51
Ltmp4689:
; %bb.49:                               ;   in Loop: Header=BB56_30 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, x9
	add	x25, x26, x25
	b	LBB56_52
Ltmp4690:
LBB56_50:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4691:
	b	LBB56_56
Ltmp4692:
LBB56_51:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x25, x20, #2
Ltmp4693:
LBB56_52:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4694:
	lsr	x26, x27, #3
Ltmp4695:
	ldr	x25, [x7, x26]
Ltmp4696:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4697:
	ands	w27, w27, #0x7
Ltmp4698:
	b.eq	LBB56_55
Ltmp4699:
; %bb.53:                               ;   in Loop: Header=BB56_30 Depth=3
	sub	w27, w15, w27
Ltmp4700:
	cmp	w27, w24
	b.hs	LBB56_55
Ltmp4701:
; %bb.54:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x26, x26, x7
Ltmp4702:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4703:
LBB56_55:                               ;   in Loop: Header=BB56_30 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4704:
	and	x24, x25, x24
Ltmp4705:
	ldrb	w25, [x6, #19]
	lsl	x24, x24, x25
Ltmp4706:
LBB56_56:                               ;   in Loop: Header=BB56_30 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4707:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4708:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4709:
	str	x23, [x22]
Ltmp4710:
	ldrb	w24, [x6, #52]
Ltmp4711:
	ldrb	w23, [x6, #53]
	cbz	w24, LBB56_59
Ltmp4712:
; %bb.57:                               ;   in Loop: Header=BB56_30 Depth=3
	cbz	w23, LBB56_60
Ltmp4713:
; %bb.58:                               ;   in Loop: Header=BB56_30 Depth=3
	ldrb	w25, [x6, #17]
	eor	x26, x20, #0xfffffffc
	add	x25, x26, x25
	b	LBB56_61
Ltmp4714:
LBB56_59:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4715:
	b	LBB56_29
Ltmp4716:
LBB56_60:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x25, x20, #3
Ltmp4717:
LBB56_61:                               ;   in Loop: Header=BB56_30 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4718:
	lsr	x26, x27, #3
Ltmp4719:
	ldr	x25, [x7, x26]
Ltmp4720:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4721:
	ands	w27, w27, #0x7
Ltmp4722:
	b.eq	LBB56_28
Ltmp4723:
; %bb.62:                               ;   in Loop: Header=BB56_30 Depth=3
	sub	w27, w15, w27
Ltmp4724:
	cmp	w27, w24
	b.hs	LBB56_28
Ltmp4725:
; %bb.63:                               ;   in Loop: Header=BB56_30 Depth=3
	add	x26, x26, x7
Ltmp4726:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4727:
	b	LBB56_28
Ltmp4728:
LBB56_64:                               ;   in Loop: Header=BB56_6 Depth=2
	ldr	x6, [x6, #40]
Ltmp4729:
	and	x7, x6, #0x7fffffffffffffff
	cmp	x6, #0
	csinv	x6, x7, x6, lt
Ltmp4730:
	cmp	x5, #8
	b.hs	LBB56_91
Ltmp4731:
; %bb.65:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x7, #0                          ; =0x0
	b	LBB56_94
Ltmp4732:
LBB56_66:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x23, #0                         ; =0x0
	and	x24, x5, #0xfffffff8
	mov	x25, x12
	b	LBB56_69
Ltmp4733:
LBB56_67:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #7
Ltmp4734:
LBB56_68:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4735:
	lsr	x28, x27, #3
Ltmp4736:
	and	x27, x27, #0x7
Ltmp4737:
	ldr	x28, [x7, x28]
Ltmp4738:
	lsr	x27, x28, x27
Ltmp4739:
	and	x27, x27, x20
Ltmp4740:
	lsl	x27, x27, x21
Ltmp4741:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4742:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4743:
	str	x26, [x25, #24]
Ltmp4744:
	add	x23, x23, #8
Ltmp4745:
	add	x25, x25, #64
	cmp	x24, x23
	b.eq	LBB56_11
Ltmp4746:
LBB56_69:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w26, [x6, #53]
	mov	x27, x23
	cbz	w26, LBB56_71
Ltmp4747:
; %bb.70:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	eor	x28, x23, #0xffffffff
	add	x27, x28, x27
Ltmp4748:
LBB56_71:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4749:
	lsr	x28, x27, #3
Ltmp4750:
	ldr	x28, [x7, x28]
Ltmp4751:
	and	x27, x27, #0x7
Ltmp4752:
	lsr	x27, x28, x27
Ltmp4753:
	and	x27, x27, x20
Ltmp4754:
	lsl	x27, x27, x21
Ltmp4755:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4756:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4757:
	stur	x26, [x25, #-32]
Ltmp4758:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_73
Ltmp4759:
; %bb.72:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	eor	x28, x23, #0xfffffffe
	add	x27, x28, x27
	b	LBB56_74
Ltmp4760:
LBB56_73:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #1
Ltmp4761:
LBB56_74:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4762:
	lsr	x28, x27, #3
Ltmp4763:
	ldr	x28, [x7, x28]
Ltmp4764:
	and	x27, x27, #0x7
Ltmp4765:
	lsr	x27, x28, x27
Ltmp4766:
	and	x27, x27, x20
Ltmp4767:
	lsl	x27, x27, x21
Ltmp4768:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4769:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4770:
	stur	x26, [x25, #-24]
Ltmp4771:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_76
Ltmp4772:
; %bb.75:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	eor	x28, x23, x9
	add	x27, x28, x27
	b	LBB56_77
Ltmp4773:
LBB56_76:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #2
Ltmp4774:
LBB56_77:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4775:
	lsr	x28, x27, #3
Ltmp4776:
	ldr	x28, [x7, x28]
Ltmp4777:
	and	x27, x27, #0x7
Ltmp4778:
	lsr	x27, x28, x27
Ltmp4779:
	and	x27, x27, x20
Ltmp4780:
	lsl	x27, x27, x21
Ltmp4781:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4782:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4783:
	stur	x26, [x25, #-16]
Ltmp4784:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_79
Ltmp4785:
; %bb.78:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	eor	x28, x23, #0xfffffffc
	add	x27, x28, x27
	b	LBB56_80
Ltmp4786:
LBB56_79:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #3
Ltmp4787:
LBB56_80:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4788:
	lsr	x28, x27, #3
Ltmp4789:
	ldr	x28, [x7, x28]
Ltmp4790:
	and	x27, x27, #0x7
Ltmp4791:
	lsr	x27, x28, x27
Ltmp4792:
	and	x27, x27, x20
Ltmp4793:
	lsl	x27, x27, x21
Ltmp4794:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4795:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4796:
	stur	x26, [x25, #-8]
Ltmp4797:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_82
Ltmp4798:
; %bb.81:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	sub	x28, x9, #2
	eor	x28, x23, x28
	add	x27, x28, x27
	b	LBB56_83
Ltmp4799:
LBB56_82:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #4
Ltmp4800:
LBB56_83:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4801:
	lsr	x28, x27, #3
Ltmp4802:
	ldr	x28, [x7, x28]
Ltmp4803:
	and	x27, x27, #0x7
Ltmp4804:
	lsr	x27, x28, x27
Ltmp4805:
	and	x27, x27, x20
Ltmp4806:
	lsl	x27, x27, x21
Ltmp4807:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4808:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4809:
	str	x26, [x25]
Ltmp4810:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_85
Ltmp4811:
; %bb.84:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	sub	x28, x9, #3
	eor	x28, x23, x28
	add	x27, x28, x27
	b	LBB56_86
Ltmp4812:
LBB56_85:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #5
Ltmp4813:
LBB56_86:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4814:
	lsr	x28, x27, #3
Ltmp4815:
	ldr	x28, [x7, x28]
Ltmp4816:
	and	x27, x27, #0x7
Ltmp4817:
	lsr	x27, x28, x27
Ltmp4818:
	and	x27, x27, x20
Ltmp4819:
	lsl	x27, x27, x21
Ltmp4820:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4821:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4822:
	str	x26, [x25, #8]
Ltmp4823:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_88
Ltmp4824:
; %bb.87:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	sub	x28, x9, #4
	eor	x28, x23, x28
	add	x27, x28, x27
	b	LBB56_89
Ltmp4825:
LBB56_88:                               ;   in Loop: Header=BB56_69 Depth=3
	add	x27, x23, #6
Ltmp4826:
LBB56_89:                               ;   in Loop: Header=BB56_69 Depth=3
	mov	w27, w27
	umull	x27, w27, w19
Ltmp4827:
	lsr	x28, x27, #3
Ltmp4828:
	ldr	x28, [x7, x28]
Ltmp4829:
	and	x27, x27, #0x7
Ltmp4830:
	lsr	x27, x28, x27
Ltmp4831:
	and	x27, x27, x20
Ltmp4832:
	lsl	x27, x27, x21
Ltmp4833:
	cmp	w26, #0
	cneg	x26, x27, ne
	add	x26, x26, x22
Ltmp4834:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4835:
	str	x26, [x25, #16]
Ltmp4836:
	ldrb	w26, [x6, #53]
	cbz	w26, LBB56_67
Ltmp4837:
; %bb.90:                               ;   in Loop: Header=BB56_69 Depth=3
	ldrb	w27, [x6, #17]
	eor	x28, x23, #0xfffffff8
	add	x27, x28, x27
	b	LBB56_68
Ltmp4838:
LBB56_91:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x7, x5, #0xfffffff8
	dup.2d	v0, x6
	mov	x19, x7
Ltmp4839:
	mov	x20, x12
Ltmp4840:
LBB56_92:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	stp	q0, q0, [x20, #-32]
	stp	q0, q0, [x20], #64
Ltmp4841:
	subs	x19, x19, #8
	b.ne	LBB56_92
Ltmp4842:
; %bb.93:                               ;   in Loop: Header=BB56_6 Depth=2
	cmp	x7, x5
	b.eq	LBB56_96
Ltmp4843:
LBB56_94:                               ;   in Loop: Header=BB56_6 Depth=2
	sub	x5, x5, x7
Ltmp4844:
	add	x7, x10, x7, lsl #3
Ltmp4845:
LBB56_95:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	str	x6, [x7], #8
Ltmp4846:
	subs	x5, x5, #1
Ltmp4847:
	b.ne	LBB56_95
Ltmp4848:
LBB56_96:                               ;   in Loop: Header=BB56_6 Depth=2
	; InlineAsm Start
	; InlineAsm End
Ltmp4849:
	ldr	w5, [x0]
Ltmp4850:
	cmp	w5, #4
	b.lo	LBB56_99
Ltmp4851:
; %bb.97:                               ;   in Loop: Header=BB56_6 Depth=2
	and	x6, x5, #0xfffffffc
	sub	x7, x5, #4
	cmp	x7, #27
	b.hi	LBB56_100
Ltmp4852:
; %bb.98:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x7, #0                          ; =0x0
	b	LBB56_103
Ltmp4853:
LBB56_99:                               ;   in Loop: Header=BB56_6 Depth=2
	mov	x6, #0                          ; =0x0
	b	LBB56_105
Ltmp4854:
LBB56_100:                              ;   in Loop: Header=BB56_6 Depth=2
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
Ltmp4855:
	movi.2d	v22, #0000000000000000
	mov	x2, x13
Ltmp4856:
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
Ltmp4857:
LBB56_101:                              ;   Parent Loop BB56_3 Depth=1
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
	b.ne	LBB56_101
Ltmp4858:
; %bb.102:                              ;   in Loop: Header=BB56_6 Depth=2
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
	b.eq	LBB56_105
Ltmp4859:
LBB56_103:                              ;   in Loop: Header=BB56_6 Depth=2
	add	x19, x7, #3
	add	x7, x11, x7, lsl #3
Ltmp4860:
LBB56_104:                              ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	x20, x21, [x7, #-16]
	add	x4, x20, x4
Ltmp4861:
	add	x3, x21, x3
Ltmp4862:
	ldp	x20, x21, [x7], #32
	add	x2, x20, x2
Ltmp4863:
	add	x17, x21, x17
Ltmp4864:
	add	x19, x19, #4
Ltmp4865:
	cmp	x19, x5
	b.lo	LBB56_104
Ltmp4866:
LBB56_105:                              ;   in Loop: Header=BB56_6 Depth=2
	cmp	x6, x5
	b.hs	LBB56_5
Ltmp4867:
; %bb.106:                              ;   in Loop: Header=BB56_6 Depth=2
	sub	x19, x5, x6
	cmp	x19, #7
	b.hi	LBB56_108
Ltmp4868:
; %bb.107:                              ;   in Loop: Header=BB56_6 Depth=2
	mov	x7, x6
	b	LBB56_111
Ltmp4869:
LBB56_108:                              ;   in Loop: Header=BB56_6 Depth=2
	and	x20, x19, #0xfffffffffffffff8
	add	x7, x20, x6
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x4
	add	x4, x12, x6, lsl #3
Ltmp4870:
	mov	x6, x20
Ltmp4871:
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
Ltmp4872:
LBB56_109:                              ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	q4, q5, [x4, #-32]
	ldp	q6, q7, [x4], #64
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	subs	x6, x6, #8
	b.ne	LBB56_109
Ltmp4873:
; %bb.110:                              ;   in Loop: Header=BB56_6 Depth=2
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x4, d0
	cmp	x19, x20
	b.eq	LBB56_5
Ltmp4874:
LBB56_111:                              ;   in Loop: Header=BB56_6 Depth=2
	add	x6, x10, x7, lsl #3
	sub	x7, x5, x7
Ltmp4875:
LBB56_112:                              ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	x19, [x6], #8
	add	x4, x19, x4
Ltmp4876:
	subs	x7, x7, #1
	b.ne	LBB56_112
	b	LBB56_5
Ltmp4877:
LBB56_113:
	add	x8, x2, x3
	add	x9, x17, x4
	add	x0, x8, x9
Ltmp4878:
	ldur	x8, [x29, #-160]
Lloh342:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh343:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh344:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB56_116
Ltmp4879:
LBB56_114:
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
Ltmp4880:
LBB56_115:
	mov	x0, #0                          ; =0x0
Ltmp4881:
	ldur	x8, [x29, #-160]
Lloh345:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh346:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh347:
	ldr	x9, [x9]
	cmp	x9, x8
	b.eq	LBB56_114
Ltmp4882:
LBB56_116:
	bl	___stack_chk_fail
Ltmp4883:
	.loh AdrpLdrGotLdr	Lloh339, Lloh340, Lloh341
	.loh AdrpLdrGotLdr	Lloh342, Lloh343, Lloh344
	.loh AdrpLdrGotLdr	Lloh345, Lloh346, Lloh347
Lfunc_end56:
