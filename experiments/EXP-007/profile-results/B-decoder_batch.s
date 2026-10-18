_decoder_batch:                         ; @decoder_batch
Lfunc_begin57:
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
	sub	sp, sp, #800
Lloh357:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh358:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh359:
	ldr	x8, [x8]
	stur	x8, [x29, #-160]
Ltmp4641:
	str	w1, [sp, #4]                    ; 4-byte Folded Spill
Ltmp4642:
	cbz	w1, LBB57_25
Ltmp4643:
; %bb.1:
	mov	x20, x0
Ltmp4644:
	mov	x25, #0                         ; =0x0
	mov	w21, #0                         ; =0x0
	mov	x27, #0                         ; =0x0
	mov	x28, #0                         ; =0x0
	mov	x19, #0                         ; =0x0
	add	x22, sp, #16
	add	x23, x22, #128
	add	x24, x22, #16
	add	x8, x22, #32
	str	x8, [sp, #8]                    ; 8-byte Folded Spill
	b	LBB57_3
Ltmp4645:
LBB57_2:                                ;   in Loop: Header=BB57_3 Depth=1
	add	w21, w21, #1
Ltmp4646:
	ldr	w8, [sp, #4]                    ; 4-byte Folded Reload
Ltmp4647:
	cmp	w21, w8
	b.eq	LBB57_23
Ltmp4648:
LBB57_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB57_6 Depth 2
                                        ;       Child Loop BB57_11 Depth 3
                                        ;       Child Loop BB57_14 Depth 3
                                        ;       Child Loop BB57_19 Depth 3
                                        ;       Child Loop BB57_22 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4649:
	ldr	w8, [x20, #4]
Ltmp4650:
	cbz	w8, LBB57_2
Ltmp4651:
; %bb.4:                                ;   in Loop: Header=BB57_3 Depth=1
	mov	x26, #0                         ; =0x0
Ltmp4652:
	ldr	w2, [x20]
	b	LBB57_6
Ltmp4653:
LBB57_5:                                ;   in Loop: Header=BB57_6 Depth=2
	add	x26, x26, #1
Ltmp4654:
	ldr	w8, [x20, #4]
Ltmp4655:
	cmp	x26, x8
	b.hs	LBB57_2
Ltmp4656:
LBB57_6:                                ;   Parent Loop BB57_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB57_11 Depth 3
                                        ;       Child Loop BB57_14 Depth 3
                                        ;       Child Loop BB57_19 Depth 3
                                        ;       Child Loop BB57_22 Depth 3
	ldr	x8, [x20, #8]
	ldr	x0, [x8, x26, lsl #3]
Ltmp4657:
	add	x3, sp, #16
	mov	w1, #0                          ; =0x0
                                        ; kill: def $w2 killed $w2 killed $x2
	bl	_zbtScoreLeafDecodeRange
Ltmp4658:
	; InlineAsm Start
	; InlineAsm End
Ltmp4659:
	ldr	w2, [x20]
Ltmp4660:
	cmp	w2, #4
	b.lo	LBB57_9
Ltmp4661:
; %bb.7:                                ;   in Loop: Header=BB57_6 Depth=2
	and	w8, w2, #0xfffffffc
	sub	x9, x2, #4
	cmp	x9, #27
	b.hi	LBB57_10
Ltmp4662:
; %bb.8:                                ;   in Loop: Header=BB57_6 Depth=2
	mov	x9, #0                          ; =0x0
	b	LBB57_13
Ltmp4663:
LBB57_9:                                ;   in Loop: Header=BB57_6 Depth=2
	mov	w8, #0                          ; =0x0
	b	LBB57_15
Ltmp4664:
LBB57_10:                               ;   in Loop: Header=BB57_6 Depth=2
	lsr	x9, x9, #2
	add	x10, x9, #1
	and	x11, x10, #0x7ffffffffffffff8
	lsl	x9, x11, #2
	movi.2d	v3, #0000000000000000
	movi.2d	v4, #0000000000000000
	mov.d	v4[0], x25
	movi.2d	v2, #0000000000000000
	mov.d	v2[0], x27
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x28
	movi.2d	v0, #0000000000000000
	mov.d	v0[0], x19
	mov	x12, x11
	movi.2d	v22, #0000000000000000
	mov	x13, x23
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
Ltmp4665:
LBB57_11:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	sub	x14, x13, #128
	sub	x15, x13, #64
	ld4.2d	{ v24, v25, v26, v27 }, [x14]
	ld4.2d	{ v28, v29, v30, v31 }, [x15]
	mov	x14, x13
	ld4.2d	{ v8, v9, v10, v11 }, [x14], #64
	ld4.2d	{ v12, v13, v14, v15 }, [x14]
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
	add	x13, x13, #256
	subs	x12, x12, #8
	b.ne	LBB57_11
Ltmp4666:
; %bb.12:                               ;   in Loop: Header=BB57_6 Depth=2
	add.2d	v3, v3, v4
	add.2d	v3, v22, v3
	add.2d	v3, v23, v3
	addp.2d	d3, v3
	fmov	x25, d3
Ltmp4667:
	add.2d	v2, v19, v2
	add.2d	v2, v20, v2
	add.2d	v2, v21, v2
	addp.2d	d2, v2
	fmov	x27, d2
Ltmp4668:
	add.2d	v1, v16, v1
	add.2d	v1, v17, v1
	add.2d	v1, v18, v1
	addp.2d	d1, v1
	fmov	x28, d1
Ltmp4669:
	add.2d	v0, v5, v0
	add.2d	v0, v6, v0
	add.2d	v0, v7, v0
	addp.2d	d0, v0
	fmov	x19, d0
Ltmp4670:
	cmp	x10, x11
	b.eq	LBB57_15
Ltmp4671:
LBB57_13:                               ;   in Loop: Header=BB57_6 Depth=2
	add	x10, x9, #3
	add	x9, x24, x9, lsl #3
Ltmp4672:
LBB57_14:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	x11, x12, [x9, #-16]
	add	x25, x11, x25
Ltmp4673:
	add	x19, x12, x19
Ltmp4674:
	ldp	x11, x12, [x9], #32
	add	x28, x11, x28
Ltmp4675:
	add	x27, x12, x27
Ltmp4676:
	add	x10, x10, #4
Ltmp4677:
	cmp	x10, x2
	b.lo	LBB57_14
Ltmp4678:
LBB57_15:                               ;   in Loop: Header=BB57_6 Depth=2
	cmp	w8, w2
	b.hs	LBB57_5
Ltmp4679:
; %bb.16:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	w11, w8
	sub	x9, x2, x11
	cmp	x9, #7
	b.hi	LBB57_18
Ltmp4680:
; %bb.17:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x8, x11
Ltmp4681:
	b	LBB57_21
Ltmp4682:
LBB57_18:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x10, x9, #0xfffffffffffffff8
	add	x8, x10, x11
Ltmp4683:
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x25
	ldr	x12, [sp, #8]                   ; 8-byte Folded Reload
	add	x11, x12, x11, lsl #3
	mov	x12, x10
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
Ltmp4684:
LBB57_19:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	q4, q5, [x11, #-32]
	ldp	q6, q7, [x11], #64
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	subs	x12, x12, #8
	b.ne	LBB57_19
Ltmp4685:
; %bb.20:                               ;   in Loop: Header=BB57_6 Depth=2
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x25, d0
Ltmp4686:
	cmp	x9, x10
	b.eq	LBB57_5
Ltmp4687:
LBB57_21:                               ;   in Loop: Header=BB57_6 Depth=2
	add	x9, x22, x8, lsl #3
	sub	x8, x2, x8
Ltmp4688:
LBB57_22:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	x10, [x9], #8
	add	x25, x10, x25
Ltmp4689:
	subs	x8, x8, #1
	b.ne	LBB57_22
	b	LBB57_5
Ltmp4690:
LBB57_23:
	add	x8, x28, x19
	add	x9, x27, x25
	add	x0, x8, x9
	ldur	x8, [x29, #-160]
Lloh360:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh361:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh362:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB57_26
Ltmp4691:
LBB57_24:
	add	sp, sp, #800
Ltmp4692:
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
Ltmp4693:
LBB57_25:
	mov	x0, #0                          ; =0x0
Ltmp4694:
	ldur	x8, [x29, #-160]
Lloh363:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh364:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh365:
	ldr	x9, [x9]
	cmp	x9, x8
	b.eq	LBB57_24
Ltmp4695:
LBB57_26:
	bl	___stack_chk_fail
Ltmp4696:
	.loh AdrpLdrGotLdr	Lloh357, Lloh358, Lloh359
	.loh AdrpLdrGotLdr	Lloh360, Lloh361, Lloh362
	.loh AdrpLdrGotLdr	Lloh363, Lloh364, Lloh365
Lfunc_end57:
