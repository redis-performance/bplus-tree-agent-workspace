_decoder_batch:                         ; @decoder_batch
Lfunc_begin56:
; %bb.0:
	sub	sp, sp, #112
	stp	x28, x27, [sp, #16]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #32]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #48]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #64]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #80]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #96]             ; 16-byte Folded Spill
Ltmp4455:
	str	w1, [sp, #12]                   ; 4-byte Folded Spill
Ltmp4456:
	cbz	w1, LBB56_55
Ltmp4457:
; %bb.1:
	mov	x8, #0                          ; =0x0
	mov	w1, #0                          ; =0x0
	mov	x9, #0                          ; =0x0
	mov	x11, #0                         ; =0x0
	mov	x12, #0                         ; =0x0
	mov	x13, #-1                        ; =0xffffffffffffffff
	mov	w14, #64                        ; =0x40
	b	LBB56_3
Ltmp4458:
LBB56_2:                                ;   in Loop: Header=BB56_3 Depth=1
	add	w1, w1, #1
Ltmp4459:
	ldr	w10, [sp, #12]                  ; 4-byte Folded Reload
Ltmp4460:
	cmp	w1, w10
	b.eq	LBB56_54
Ltmp4461:
LBB56_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB56_7 Depth 2
                                        ;       Child Loop BB56_11 Depth 3
                                        ;       Child Loop BB56_49 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4462:
	ldr	w15, [x0, #4]
Ltmp4463:
	cbz	w15, LBB56_2
Ltmp4464:
; %bb.4:                                ;   in Loop: Header=BB56_3 Depth=1
	mov	x16, #0                         ; =0x0
	ldr	x17, [x0, #8]
	ldr	w2, [x0]
	and	w3, w2, #0xfffffffc
	b	LBB56_7
Ltmp4465:
LBB56_5:                                ;   in Loop: Header=BB56_7 Depth=2
	and	x4, x19, #0x7fffffffffffffff
	cmp	x19, #0
	csinv	x4, x4, x19, lt
Ltmp4466:
	mvn	w5, w5
Ltmp4467:
	add	w5, w2, w5
	madd	x4, x4, x5, x4
Ltmp4468:
	add	x8, x8, x4
Ltmp4469:
LBB56_6:                                ;   in Loop: Header=BB56_7 Depth=2
	add	x16, x16, #1
Ltmp4470:
	cmp	x16, x15
	b.eq	LBB56_2
Ltmp4471:
LBB56_7:                                ;   Parent Loop BB56_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB56_11 Depth 3
                                        ;       Child Loop BB56_49 Depth 3
	ldr	x4, [x17, x16, lsl #3]
Ltmp4472:
	cmp	w2, #4
	b.lo	LBB56_44
Ltmp4473:
; %bb.8:                                ;   in Loop: Header=BB56_7 Depth=2
	mov	w5, #0                          ; =0x0
	ldrb	w6, [x4, #52]
	ldrb	w7, [x4, #53]
	add	x19, x4, #56
	lsl	x20, x13, x6
	cmp	w6, #64
	csinv	x20, x13, x20, hs
	ldr	x21, [x4, #40]
	mov	w22, #3                         ; =0x3
	mov	w23, #-1                        ; =0xffffffff
	b	LBB56_11
Ltmp4474:
LBB56_9:                                ;   in Loop: Header=BB56_11 Depth=3
	and	x10, x25, x20
Ltmp4475:
	ldrb	w25, [x4, #19]
	lsl	x25, x10, x25
Ltmp4476:
LBB56_10:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x8, x24, x8
Ltmp4477:
	add	x12, x26, x12
Ltmp4478:
	add	x11, x27, x11
Ltmp4479:
	cmp	w7, #0
	cneg	x10, x25, ne
	add	x10, x10, x21
Ltmp4480:
	and	x24, x10, #0x7fffffffffffffff
	cmp	x10, #0
	csinv	x10, x24, x10, lt
Ltmp4481:
	add	x9, x10, x9
Ltmp4482:
	add	w5, w5, #4
Ltmp4483:
	add	w22, w22, #4
	sub	w23, w23, #4
Ltmp4484:
	cmp	w22, w2
	b.hs	LBB56_45
Ltmp4485:
LBB56_11:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_7 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	cbz	w6, LBB56_18
Ltmp4486:
; %bb.12:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x24, x5
Ltmp4487:
	cbz	w7, LBB56_14
Ltmp4488:
; %bb.13:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w24, [x4, #17]
	add	w24, w23, w24
Ltmp4489:
LBB56_14:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x26, w6, w24
Ltmp4490:
	lsr	x25, x26, #3
Ltmp4491:
	ldr	x24, [x19, x25]
Ltmp4492:
	and	x27, x26, #0x7
	lsr	x24, x24, x27
Ltmp4493:
	ands	w26, w26, #0x7
Ltmp4494:
	b.eq	LBB56_17
Ltmp4495:
; %bb.15:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w26, w14, w26
Ltmp4496:
	cmp	w26, w6
	b.hs	LBB56_17
Ltmp4497:
; %bb.16:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x25, x25, x19
Ltmp4498:
	ldrb	w25, [x25, #8]
	lsl	x25, x25, x26
	orr	x24, x25, x24
Ltmp4499:
LBB56_17:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x24, x24, x20
Ltmp4500:
	ldrb	w25, [x4, #19]
	lsl	x24, x24, x25
Ltmp4501:
	b	LBB56_19
Ltmp4502:
LBB56_18:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4503:
LBB56_19:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w25, w22, #3
Ltmp4504:
	cmp	w7, #0
	cneg	x24, x24, ne
Ltmp4505:
	add	x24, x21, x24
Ltmp4506:
	and	x26, x24, #0x7fffffffffffffff
	cmp	x24, #0
	csinv	x24, x26, x24, lt
Ltmp4507:
	cbz	w6, LBB56_22
Ltmp4508:
; %bb.20:                               ;   in Loop: Header=BB56_11 Depth=3
	cbz	w7, LBB56_23
Ltmp4509:
; %bb.21:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w26, [x4, #17]
	eor	w27, w25, #0xfffffffe
	add	w26, w27, w26
	b	LBB56_24
Ltmp4510:
LBB56_22:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x26, #0                         ; =0x0
	b	LBB56_28
Ltmp4511:
LBB56_23:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w26, w22, #2
Ltmp4512:
LBB56_24:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x28, w6, w26
Ltmp4513:
	lsr	x27, x28, #3
Ltmp4514:
	ldr	x26, [x19, x27]
Ltmp4515:
	and	x30, x28, #0x7
	lsr	x26, x26, x30
Ltmp4516:
	ands	w28, w28, #0x7
Ltmp4517:
	b.eq	LBB56_27
Ltmp4518:
; %bb.25:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w28, w14, w28
Ltmp4519:
	cmp	w28, w6
	b.hs	LBB56_27
Ltmp4520:
; %bb.26:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x27, x27, x19
Ltmp4521:
	ldrb	w27, [x27, #8]
	lsl	x27, x27, x28
	orr	x26, x27, x26
Ltmp4522:
LBB56_27:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x26, x26, x20
Ltmp4523:
	ldrb	w27, [x4, #19]
	lsl	x26, x26, x27
Ltmp4524:
LBB56_28:                               ;   in Loop: Header=BB56_11 Depth=3
	cmp	w7, #0
	cneg	x26, x26, ne
Ltmp4525:
	add	x26, x26, x21
Ltmp4526:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp4527:
	cbz	w6, LBB56_31
Ltmp4528:
; %bb.29:                               ;   in Loop: Header=BB56_11 Depth=3
	cbz	w7, LBB56_32
Ltmp4529:
; %bb.30:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w27, [x4, #17]
	eor	w28, w25, #0xfffffffd
	add	w27, w28, w27
	b	LBB56_33
Ltmp4530:
LBB56_31:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x27, #0                         ; =0x0
	b	LBB56_37
Ltmp4531:
LBB56_32:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w27, w22, #1
Ltmp4532:
LBB56_33:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x30, w6, w27
Ltmp4533:
	lsr	x28, x30, #3
Ltmp4534:
	ldr	x27, [x19, x28]
Ltmp4535:
	and	x10, x30, #0x7
	lsr	x27, x27, x10
Ltmp4536:
	ands	w30, w30, #0x7
Ltmp4537:
	b.eq	LBB56_36
Ltmp4538:
; %bb.34:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w30, w14, w30
Ltmp4539:
	cmp	w30, w6
	b.hs	LBB56_36
Ltmp4540:
; %bb.35:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x10, x28, x19
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x30
	orr	x27, x10, x27
Ltmp4541:
LBB56_36:                               ;   in Loop: Header=BB56_11 Depth=3
	and	x10, x27, x20
Ltmp4542:
	ldrb	w27, [x4, #19]
	lsl	x27, x10, x27
Ltmp4543:
LBB56_37:                               ;   in Loop: Header=BB56_11 Depth=3
	cmp	w7, #0
	cneg	x10, x27, ne
	add	x10, x10, x21
Ltmp4544:
	and	x27, x10, #0x7fffffffffffffff
Ltmp4545:
	cmp	x10, #0
	csinv	x27, x27, x10, lt
Ltmp4546:
	cbz	w6, LBB56_43
Ltmp4547:
; %bb.38:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x28, x22
Ltmp4548:
	cbz	w7, LBB56_40
Ltmp4549:
; %bb.39:                               ;   in Loop: Header=BB56_11 Depth=3
	ldrb	w10, [x4, #17]
	eor	w25, w25, #0xfffffffc
	add	w28, w25, w10
Ltmp4550:
LBB56_40:                               ;   in Loop: Header=BB56_11 Depth=3
	umull	x10, w6, w28
Ltmp4551:
	lsr	x28, x10, #3
Ltmp4552:
	ldr	x25, [x19, x28]
Ltmp4553:
	and	x30, x10, #0x7
	lsr	x25, x25, x30
Ltmp4554:
	ands	w30, w10, #0x7
Ltmp4555:
	b.eq	LBB56_9
Ltmp4556:
; %bb.41:                               ;   in Loop: Header=BB56_11 Depth=3
	sub	w30, w14, w30
Ltmp4557:
	cmp	w30, w6
	b.hs	LBB56_9
Ltmp4558:
; %bb.42:                               ;   in Loop: Header=BB56_11 Depth=3
	add	x10, x28, x19
Ltmp4559:
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x30
	orr	x25, x10, x25
Ltmp4560:
	b	LBB56_9
Ltmp4561:
LBB56_43:                               ;   in Loop: Header=BB56_11 Depth=3
	mov	x25, #0                         ; =0x0
	b	LBB56_10
Ltmp4562:
LBB56_44:                               ;   in Loop: Header=BB56_7 Depth=2
	mov	w5, #0                          ; =0x0
Ltmp4563:
	subs	w6, w2, w5
	b.ls	LBB56_6
	b	LBB56_46
Ltmp4564:
LBB56_45:                               ;   in Loop: Header=BB56_7 Depth=2
	mov	x5, x3
Ltmp4565:
	subs	w6, w2, w5
	b.ls	LBB56_6
Ltmp4566:
LBB56_46:                               ;   in Loop: Header=BB56_7 Depth=2
	ldrb	w7, [x4, #52]
	lsl	x19, x13, x7
	cmp	w7, #64
	csinv	x20, x13, x19, hs
	ldr	x19, [x4, #40]
	cbz	w7, LBB56_5
Ltmp4567:
; %bb.47:                               ;   in Loop: Header=BB56_7 Depth=2
	ldrb	w21, [x4, #53]
	add	x22, x4, #56
	ldrb	w23, [x4, #19]
	mvn	w24, w5
	b	LBB56_49
Ltmp4568:
LBB56_48:                               ;   in Loop: Header=BB56_49 Depth=3
	and	x10, x25, x20
Ltmp4569:
	lsl	x10, x10, x23
Ltmp4570:
	cmp	w21, #0
	cneg	x10, x10, ne
	add	x10, x19, x10
Ltmp4571:
	and	x25, x10, #0x7fffffffffffffff
	cmp	x10, #0
	csinv	x10, x25, x10, lt
Ltmp4572:
	add	x8, x10, x8
Ltmp4573:
	add	w5, w5, #1
Ltmp4574:
	sub	w24, w24, #1
	sub	w6, w6, #1
Ltmp4575:
	cbz	w6, LBB56_6
Ltmp4576:
LBB56_49:                               ;   Parent Loop BB56_3 Depth=1
                                        ;     Parent Loop BB56_7 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	mov	x25, x5
Ltmp4577:
	cbz	w21, LBB56_51
Ltmp4578:
; %bb.50:                               ;   in Loop: Header=BB56_49 Depth=3
	ldrb	w10, [x4, #17]
	add	w25, w24, w10
Ltmp4579:
LBB56_51:                               ;   in Loop: Header=BB56_49 Depth=3
	umull	x10, w7, w25
Ltmp4580:
	lsr	x26, x10, #3
Ltmp4581:
	ldr	x25, [x22, x26]
Ltmp4582:
	and	x27, x10, #0x7
	lsr	x25, x25, x27
Ltmp4583:
	ands	w27, w10, #0x7
Ltmp4584:
	b.eq	LBB56_48
Ltmp4585:
; %bb.52:                               ;   in Loop: Header=BB56_49 Depth=3
	sub	w27, w14, w27
Ltmp4586:
	cmp	w27, w7
	b.hs	LBB56_48
Ltmp4587:
; %bb.53:                               ;   in Loop: Header=BB56_49 Depth=3
	add	x10, x26, x22
Ltmp4588:
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x27
	orr	x25, x10, x25
Ltmp4589:
	b	LBB56_48
Ltmp4590:
LBB56_54:
	add	x10, x11, x12
	add	x8, x9, x8
Ltmp4591:
	add	x0, x10, x8
Ltmp4592:
	b	LBB56_56
Ltmp4593:
LBB56_55:
	mov	x0, #0                          ; =0x0
Ltmp4594:
LBB56_56:
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #80]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #64]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #48]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #32]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #112
	ret
Ltmp4595:
Lfunc_end56:
