_decoder_batch:                         ; @decoder_batch
Lfunc_begin56:
; %bb.0:
	cbz	w1, LBB56_50
Ltmp4459:
; %bb.1:
	stp	x28, x27, [sp, #-96]!           ; 16-byte Folded Spill
	stp	x26, x25, [sp, #16]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #32]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #48]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #64]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	mov	x8, #0                          ; =0x0
	mov	w10, #0                         ; =0x0
	mov	x9, #0                          ; =0x0
	mov	x11, #0                         ; =0x0
	mov	x12, #0                         ; =0x0
	mov	x13, #-1                        ; =0xffffffffffffffff
	b	LBB56_3
Ltmp4460:
LBB56_2:                                ;   in Loop: Header=BB56_3 Depth=1
	add	w10, w10, #1
Ltmp4461:
	cmp	w10, w1
	b.eq	LBB56_49
Ltmp4462:
LBB56_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB56_7 Depth 2
                                        ;       Child Loop BB56_11 Depth 3
                                        ;       Child Loop BB56_45 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4463:
	ldr	w14, [x0, #4]
Ltmp4464:
	cbz	w14, LBB56_2
Ltmp4465:
; %bb.4:                                ;   in Loop: Header=BB56_3 Depth=1
	mov	x15, #0                         ; =0x0
	ldr	x16, [x0, #8]
	ldr	w17, [x0]
	and	w2, w17, #0xfffffffc
	b	LBB56_7
Ltmp4466:
LBB56_5:                                ;   in Loop: Header=BB56_7 Depth=2
	and	x3, x7, #0x7fffffffffffffff
	cmp	x7, #0
	csinv	x3, x3, x7, lt
Ltmp4467:
	mvn	w4, w4
Ltmp4468:
	add	w4, w17, w4
	madd	x3, x3, x4, x3
Ltmp4469:
	add	x8, x8, x3
Ltmp4470:
LBB56_6:                                ;   in Loop: Header=BB56_7 Depth=2
	add	x15, x15, #1
Ltmp4471:
	cmp	x15, x14
	b.eq	LBB56_2
Ltmp4472:
LBB56_7:                                ;   Parent Loop BB56_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB56_11 Depth 3
                                        ;       Child Loop BB56_45 Depth 3
	ldr	x3, [x16, x15, lsl #3]
Ltmp4473:
	cmp	w17, #4
	b.lo	LBB56_40
Ltmp4474:
; %bb.8:                                ;   in Loop: Header=BB56_7 Depth=2
	mov	w4, #0                          ; =0x0
	ldrb	w5, [x3, #52]
	add	x6, x3, #56
	lsl	x7, x13, x5
	cmp	w5, #64
	csinv	x7, x13, x7, hs
	ldr	x19, [x3, #40]
	ldrb	w20, [x3, #53]
	mov	w21, #3                         ; =0x3
	mov	w22, #-1                        ; =0xffffffff
	b	LBB56_11
Ltmp4475:
LBB56_9:                                ;   in Loop: Header=BB56_11 Depth=3
	and	x24, x24, x7
Ltmp4476:
	ldrb	w27, [x3, #19]
	lsl	x24, x24, x27
Ltmp4477:
LBB56_10:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x8, x23, x8
Ltmp4478:
	add	x12, x25, x12
Ltmp4479:
	add	x11, x26, x11
Ltmp4480:
	cmp	w20, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
Ltmp4481:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4482:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4483:
	add	x9, x23, x9
Ltmp4484:
	add	w4, w4, #4
Ltmp4485:
	add	w21, w21, #4
	sub	w22, w22, #4
Ltmp4486:
	cmp	w21, w17
	b.hs	LBB56_41
Ltmp4487:
LBB56_11:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_7 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	cbz	w5, LBB56_17
Ltmp4488:
; %bb.12:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x23, x4
Ltmp4489:
	cbz	w20, LBB56_14
Ltmp4490:
; %bb.13:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w23, [x3, #17]
	add	w23, w22, w23
Ltmp4491:
LBB56_14:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x23, w5, w23
Ltmp4492:
	lsr	x25, x23, #3
Ltmp4493:
	and	w24, w23, #0x7
Ltmp4494:
	ldr	x26, [x6, x25]
Ltmp4495:
	and	x23, x23, #0x7
Ltmp4496:
	lsr	x23, x26, x23
Ltmp4497:
	add	w26, w24, w5
Ltmp4498:
	cmp	w26, #65
	b.lo	LBB56_16
Ltmp4499:
; %bb.15:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x25, x25, x6
Ltmp4500:
	ldrb	w25, [x25, #8]
	neg	w24, w24
Ltmp4501:
	lsl	x24, x25, x24
	orr	x23, x24, x23
Ltmp4502:
LBB56_16:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x23, x23, x7
Ltmp4503:
	ldrb	w24, [x3, #19]
	lsl	x23, x23, x24
Ltmp4504:
	b	LBB56_18
Ltmp4505:
LBB56_17:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x23, #0                         ; =0x0
Ltmp4506:
LBB56_18:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w24, w21, #3
Ltmp4507:
	cmp	w20, #0
	cneg	x23, x23, ne
Ltmp4508:
	add	x23, x19, x23
Ltmp4509:
	and	x25, x23, #0x7fffffffffffffff
	cmp	x23, #0
	csinv	x23, x25, x23, lt
Ltmp4510:
	cbz	w5, LBB56_21
Ltmp4511:
; %bb.19:                               ;   in Loop: Header=BB56_11 Depth=3
	cbz	w20, LBB56_22
Ltmp4512:
; %bb.20:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w25, [x3, #17]
	eor	w26, w24, #0xfffffffe
	add	w25, w26, w25
	b	LBB56_23
Ltmp4513:
LBB56_21:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x25, #0                         ; =0x0
	b	LBB56_26
Ltmp4514:
LBB56_22:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w25, w21, #2
Ltmp4515:
LBB56_23:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x25, w5, w25
Ltmp4516:
	lsr	x27, x25, #3
Ltmp4517:
	and	w26, w25, #0x7
Ltmp4518:
	ldr	x28, [x6, x27]
Ltmp4519:
	and	x25, x25, #0x7
Ltmp4520:
	lsr	x25, x28, x25
Ltmp4521:
	add	w28, w26, w5
Ltmp4522:
	cmp	w28, #65
	b.lo	LBB56_25
Ltmp4523:
; %bb.24:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x27, x27, x6
Ltmp4524:
	ldrb	w27, [x27, #8]
	neg	w26, w26
Ltmp4525:
	lsl	x26, x27, x26
	orr	x25, x26, x25
Ltmp4526:
LBB56_25:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x25, x25, x7
Ltmp4527:
	ldrb	w26, [x3, #19]
	lsl	x25, x25, x26
Ltmp4528:
LBB56_26:                               ;   in Loop: Header=BB56_11 Depth=3
	cmp	w20, #0
	cneg	x25, x25, ne
Ltmp4529:
	add	x25, x25, x19
Ltmp4530:
	and	x26, x25, #0x7fffffffffffffff
	cmp	x25, #0
	csinv	x25, x26, x25, lt
Ltmp4531:
	cbz	w5, LBB56_29
Ltmp4532:
; %bb.27:                               ;   in Loop: Header=BB56_11 Depth=3
	cbz	w20, LBB56_30
Ltmp4533:
; %bb.28:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w26, [x3, #17]
	eor	w27, w24, #0xfffffffd
	add	w26, w27, w26
	b	LBB56_31
Ltmp4534:
LBB56_29:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x26, #0                         ; =0x0
	b	LBB56_34
Ltmp4535:
LBB56_30:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w26, w21, #1
Ltmp4536:
LBB56_31:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x26, w5, w26
Ltmp4537:
	lsr	x28, x26, #3
Ltmp4538:
	and	w27, w26, #0x7
Ltmp4539:
	ldr	x30, [x6, x28]
Ltmp4540:
	and	x26, x26, #0x7
Ltmp4541:
	lsr	x26, x30, x26
Ltmp4542:
	add	w30, w27, w5
Ltmp4543:
	cmp	w30, #65
	b.lo	LBB56_33
Ltmp4544:
; %bb.32:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x28, x28, x6
Ltmp4545:
	ldrb	w28, [x28, #8]
	neg	w27, w27
Ltmp4546:
	lsl	x27, x28, x27
	orr	x26, x27, x26
Ltmp4547:
LBB56_33:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x26, x26, x7
Ltmp4548:
	ldrb	w27, [x3, #19]
	lsl	x26, x26, x27
Ltmp4549:
LBB56_34:                               ;   in Loop: Header=BB56_11 Depth=3
	cmp	w20, #0
	cneg	x26, x26, ne
Ltmp4550:
	add	x26, x26, x19
Ltmp4551:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4552:
	cbz	w5, LBB56_39
Ltmp4553:
; %bb.35:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x27, x21
Ltmp4554:
	cbz	w20, LBB56_37
Ltmp4555:
; %bb.36:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w27, [x3, #17]
	eor	w24, w24, #0xfffffffc
	add	w27, w24, w27
Ltmp4556:
LBB56_37:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x24, w5, w27
Ltmp4557:
	lsr	x28, x24, #3
Ltmp4558:
	and	w27, w24, #0x7
Ltmp4559:
	ldr	x30, [x6, x28]
Ltmp4560:
	and	x24, x24, #0x7
Ltmp4561:
	lsr	x24, x30, x24
Ltmp4562:
	add	w30, w27, w5
Ltmp4563:
	cmp	w30, #65
	b.lo	LBB56_9
Ltmp4564:
; %bb.38:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x28, x28, x6
Ltmp4565:
	ldrb	w28, [x28, #8]
	neg	w27, w27
Ltmp4566:
	lsl	x27, x28, x27
	orr	x24, x27, x24
Ltmp4567:
	b	LBB56_9
Ltmp4568:
LBB56_39:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x24, #0                         ; =0x0
	b	LBB56_10
Ltmp4569:
LBB56_40:                               ;   in Loop: Header=BB56_7 Depth=2
	mov	w4, #0                          ; =0x0
Ltmp4570:
	subs	w5, w17, w4
	b.ls	LBB56_6
	b	LBB56_42
Ltmp4571:
LBB56_41:                               ;   in Loop: Header=BB56_7 Depth=2
	mov	x4, x2
Ltmp4572:
	subs	w5, w17, w4
	b.ls	LBB56_6
Ltmp4573:
LBB56_42:                               ;   in Loop: Header=BB56_7 Depth=2
	ldrb	w6, [x3, #52]
	lsl	x7, x13, x6
	cmp	w6, #64
	csinv	x19, x13, x7, hs
	ldr	x7, [x3, #40]
	cbz	w6, LBB56_5
Ltmp4574:
; %bb.43:                               ;   in Loop: Header=BB56_7 Depth=2
	add	x20, x3, #56
	ldrb	w21, [x3, #53]
	ldrb	w22, [x3, #19]
	mvn	w23, w4
	b	LBB56_45
Ltmp4575:
LBB56_44:                               ;   in Loop: Header=BB56_45 Depth=3
	and	x24, x24, x19
Ltmp4576:
	lsl	x24, x24, x22
Ltmp4577:
	cmp	w21, #0
	cneg	x24, x24, ne
Ltmp4578:
	add	x24, x7, x24
Ltmp4579:
	and	x25, x24, #0x7fffffffffffffff
	cmp	x24, #0
	csinv	x24, x25, x24, lt
Ltmp4580:
	add	x8, x24, x8
Ltmp4581:
	add	w4, w4, #1
Ltmp4582:
	sub	w23, w23, #1
	sub	w5, w5, #1
Ltmp4583:
	cbz	w5, LBB56_6
Ltmp4584:
LBB56_45:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_7 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	mov	x24, x4
Ltmp4585:
	cbz	w21, LBB56_47
Ltmp4586:
; %bb.46:                               ;   in Loop: Header=BB56_45 Depth=3
	ldrb	w24, [x3, #17]
	add	w24, w23, w24
Ltmp4587:
LBB56_47:                               ;   in Loop: Header=BB56_45 Depth=3
	umull	x24, w6, w24
Ltmp4588:
	lsr	x26, x24, #3
Ltmp4589:
	and	w25, w24, #0x7
Ltmp4590:
	ldr	x27, [x20, x26]
Ltmp4591:
	and	x24, x24, #0x7
Ltmp4592:
	lsr	x24, x27, x24
Ltmp4593:
	add	w27, w25, w6
Ltmp4594:
	cmp	w27, #65
	b.lo	LBB56_44
Ltmp4595:
; %bb.48:                               ;   in Loop: Header=BB56_45 Depth=3
	add	x26, x26, x20
Ltmp4596:
	ldrb	w26, [x26, #8]
	neg	w25, w25
Ltmp4597:
	lsl	x25, x26, x25
	orr	x24, x25, x24
Ltmp4598:
	b	LBB56_44
Ltmp4599:
LBB56_49:
	add	x10, x11, x12
	add	x8, x9, x8
Ltmp4600:
	add	x0, x10, x8
Ltmp4601:
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
Ltmp4602:
LBB56_50:
	mov	x0, #0                          ; =0x0
Ltmp4603:
	ret
Ltmp4604:
Lfunc_end56:
