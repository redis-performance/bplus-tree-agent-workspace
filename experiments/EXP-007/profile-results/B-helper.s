_zbtScoreLeafDecodeRange:               ; @zbtScoreLeafDecodeRange
Lfunc_begin56:
; %bb.0:
	cbz	w2, LBB56_25
Ltmp4549:
; %bb.1:
	ldrb	w11, [x0, #52]
Ltmp4550:
	ldr	x8, [x0, #40]
Ltmp4551:
	cbz	w11, LBB56_10
Ltmp4552:
; %bb.2:
	ldrb	w9, [x0, #19]
	ldrb	w14, [x0, #53]
Ltmp4553:
	ldrb	w15, [x0, #17]
Ltmp4554:
	mov	x10, #-1                        ; =0xffffffffffffffff
	lsl	x12, x10, x11
	cmp	w11, #64
	csinv	x10, x10, x12, eq
Ltmp4555:
	tst	w11, #0x7
Ltmp4556:
	b.eq	LBB56_12
Ltmp4557:
; %bb.3:
	add	x12, x0, #56
	mov	w13, w2
Ltmp4558:
	cmp	w11, #59
	b.lo	LBB56_16
Ltmp4559:
; %bb.4:
	cmp	w11, #60
	b.eq	LBB56_16
Ltmp4560:
; %bb.5:
	mvn	w16, w1
	add	w15, w16, w15
Ltmp4561:
	mov	w16, #64                        ; =0x40
	b	LBB56_7
Ltmp4562:
LBB56_6:                                ;   in Loop: Header=BB56_7 Depth=1
	and	x17, x17, x10
Ltmp4563:
	lsl	x17, x17, x9
Ltmp4564:
	tst	w14, #0xff
	cneg	x17, x17, ne
Ltmp4565:
	add	x17, x17, x8
Ltmp4566:
	and	x0, x17, #0x7fffffffffffffff
	cmp	x17, #0
	csinv	x17, x0, x17, lt
Ltmp4567:
	str	x17, [x3], #8
Ltmp4568:
	add	w1, w1, #1
Ltmp4569:
	sub	w15, w15, #1
	subs	x13, x13, #1
Ltmp4570:
	b.eq	LBB56_25
Ltmp4571:
LBB56_7:                                ; =>This Inner Loop Header: Depth=1
	tst	w14, #0xff
	csel	w17, w1, w15, eq
Ltmp4572:
	umull	x2, w11, w17
Ltmp4573:
	lsr	x0, x2, #3
Ltmp4574:
	ldr	x17, [x12, x0]
Ltmp4575:
	and	x4, x2, #0x7
	lsr	x17, x17, x4
Ltmp4576:
	ands	w2, w2, #0x7
Ltmp4577:
	b.eq	LBB56_6
Ltmp4578:
; %bb.8:                                ;   in Loop: Header=BB56_7 Depth=1
	sub	w2, w16, w2
Ltmp4579:
	cmp	w2, w11
	b.hs	LBB56_6
Ltmp4580:
; %bb.9:                                ;   in Loop: Header=BB56_7 Depth=1
	add	x0, x0, x12
Ltmp4581:
	ldrb	w0, [x0, #8]
	lsl	x0, x0, x2
	orr	x17, x0, x17
Ltmp4582:
	b	LBB56_6
Ltmp4583:
LBB56_10:
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4584:
	mov	w9, w2
Ltmp4585:
	cmp	w2, #8
	b.hs	LBB56_20
Ltmp4586:
; %bb.11:
	mov	x10, #0                         ; =0x0
	b	LBB56_23
Ltmp4587:
LBB56_12:
	lsr	x11, x11, #3
Ltmp4588:
	add	x12, x0, #56
Ltmp4589:
	mov	w13, w2
	tst	w14, #0xff
	b.eq	LBB56_15
Ltmp4590:
; %bb.13:
	mvn	w14, w1
Ltmp4591:
	add	w14, w14, w15
Ltmp4592:
LBB56_14:                               ; =>This Inner Loop Header: Depth=1
	umull	x15, w11, w14
	ldr	x15, [x12, x15]
Ltmp4593:
	and	x15, x15, x10
Ltmp4594:
	lsl	x15, x15, x9
Ltmp4595:
	sub	x15, x8, x15
Ltmp4596:
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4597:
	str	x15, [x3], #8
Ltmp4598:
	sub	w14, w14, #1
	subs	x13, x13, #1
Ltmp4599:
	b.ne	LBB56_14
	b	LBB56_25
Ltmp4600:
LBB56_15:                               ; =>This Inner Loop Header: Depth=1
	umull	x14, w11, w1
	ldr	x14, [x12, x14]
Ltmp4601:
	and	x14, x14, x10
Ltmp4602:
	lsl	x14, x14, x9
Ltmp4603:
	add	x14, x14, x8
Ltmp4604:
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4605:
	str	x14, [x3], #8
Ltmp4606:
	add	w1, w1, #1
Ltmp4607:
	subs	x13, x13, #1
Ltmp4608:
	b.ne	LBB56_15
	b	LBB56_25
Ltmp4609:
LBB56_16:
	tst	w14, #0xff
	b.eq	LBB56_19
Ltmp4610:
; %bb.17:
	mvn	w14, w1
Ltmp4611:
	add	w14, w14, w15
Ltmp4612:
LBB56_18:                               ; =>This Inner Loop Header: Depth=1
	umull	x15, w11, w14
Ltmp4613:
	lsr	x16, x15, #3
	ldr	x16, [x12, x16]
Ltmp4614:
	and	x15, x15, #0x7
Ltmp4615:
	lsr	x15, x16, x15
	and	x15, x15, x10
	lsl	x15, x15, x9
Ltmp4616:
	sub	x15, x8, x15
Ltmp4617:
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4618:
	str	x15, [x3], #8
Ltmp4619:
	sub	w14, w14, #1
	subs	x13, x13, #1
Ltmp4620:
	b.ne	LBB56_18
	b	LBB56_25
Ltmp4621:
LBB56_19:                               ; =>This Inner Loop Header: Depth=1
	umull	x14, w11, w1
Ltmp4622:
	lsr	x15, x14, #3
	ldr	x15, [x12, x15]
Ltmp4623:
	and	x14, x14, #0x7
Ltmp4624:
	lsr	x14, x15, x14
	and	x14, x14, x10
	lsl	x14, x14, x9
Ltmp4625:
	add	x14, x14, x8
Ltmp4626:
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4627:
	str	x14, [x3], #8
Ltmp4628:
	add	w1, w1, #1
Ltmp4629:
	subs	x13, x13, #1
Ltmp4630:
	b.ne	LBB56_19
	b	LBB56_25
Ltmp4631:
LBB56_20:
	and	x10, x9, #0xfffffff8
	dup.2d	v0, x8
	add	x11, x3, #32
Ltmp4632:
	mov	x12, x10
Ltmp4633:
LBB56_21:                               ; =>This Inner Loop Header: Depth=1
	stp	q0, q0, [x11, #-32]
	stp	q0, q0, [x11], #64
	subs	x12, x12, #8
	b.ne	LBB56_21
Ltmp4634:
; %bb.22:
	cmp	x10, x9
	b.eq	LBB56_25
Ltmp4635:
LBB56_23:
	add	x11, x3, x10, lsl #3
	sub	x9, x9, x10
Ltmp4636:
LBB56_24:                               ; =>This Inner Loop Header: Depth=1
	str	x8, [x11], #8
Ltmp4637:
	subs	x9, x9, #1
Ltmp4638:
	b.ne	LBB56_24
Ltmp4639:
LBB56_25:
	ret
Ltmp4640:
Lfunc_end56:
