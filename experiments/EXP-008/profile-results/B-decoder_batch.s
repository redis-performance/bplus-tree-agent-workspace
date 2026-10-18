_decoder_batch:                         ; @decoder_batch
Lfunc_begin57:
	.loc	0 122 0                         ; experiments/EXP-008/referee/kernel.c:122:0
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: decoder_batch:f <- $x0
	;DEBUG_VALUE: decoder_batch:rounds <- $w1
	;DEBUG_VALUE: decoder_batch:f <- $x0
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
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset w21, -40
	.cfi_offset w22, -48
	.cfi_offset w23, -56
	.cfi_offset w24, -64
	.cfi_offset w25, -72
	.cfi_offset w26, -80
	.cfi_offset w27, -88
	.cfi_offset w28, -96
	.cfi_offset b8, -104
	.cfi_offset b9, -112
	.cfi_offset b10, -120
	.cfi_offset b11, -128
	.cfi_offset b12, -136
	.cfi_offset b13, -144
	.cfi_offset b14, -152
	.cfi_offset b15, -160
Lloh357:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh358:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh359:
	ldr	x8, [x8]
	stur	x8, [x29, #-160]
Ltmp4833:
	;DEBUG_VALUE: r <- 0
	;DEBUG_VALUE: decoder_batch:d <- 0
	;DEBUG_VALUE: decoder_batch:c <- 0
	;DEBUG_VALUE: decoder_batch:b <- 0
	;DEBUG_VALUE: decoder_batch:a <- 0
	str	w1, [sp, #4]                    ; 4-byte Folded Spill
Ltmp4834:
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 124 5 prologue_end            ; experiments/EXP-008/referee/kernel.c:124:5
	cbz	w1, LBB57_25
Ltmp4835:
; %bb.1:
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- 0
	;DEBUG_VALUE: decoder_batch:b <- 0
	;DEBUG_VALUE: decoder_batch:c <- 0
	;DEBUG_VALUE: decoder_batch:d <- 0
	;DEBUG_VALUE: r <- 0
	;DEBUG_VALUE: decoder_batch:f <- $x0
	.loc	0 0 5 is_stmt 0                 ; experiments/EXP-008/referee/kernel.c:0:5
	mov	x20, x0
Ltmp4836:
	;DEBUG_VALUE: decoder_batch:f <- $x20
	mov	x25, #0                         ; =0x0
	mov	w21, #0                         ; =0x0
	mov	x27, #0                         ; =0x0
	mov	x28, #0                         ; =0x0
	mov	x19, #0                         ; =0x0
	add	x22, sp, #16
	.loc	0 124 5                         ; experiments/EXP-008/referee/kernel.c:124:5
	add	x23, x22, #128
	add	x24, x22, #16
	add	x8, x22, #32
	str	x8, [sp, #8]                    ; 8-byte Folded Spill
	b	LBB57_3
Ltmp4837:
LBB57_2:                                ;   in Loop: Header=BB57_3 Depth=1
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 124 39                        ; experiments/EXP-008/referee/kernel.c:124:39
	add	w21, w21, #1
Ltmp4838:
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	.loc	0 0 39                          ; experiments/EXP-008/referee/kernel.c:0:39
	ldr	w8, [sp, #4]                    ; 4-byte Folded Reload
Ltmp4839:
	.loc	0 124 5                         ; experiments/EXP-008/referee/kernel.c:124:5
	cmp	w21, w8
	b.eq	LBB57_23
Ltmp4840:
LBB57_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB57_6 Depth 2
                                        ;       Child Loop BB57_11 Depth 3
                                        ;       Child Loop BB57_14 Depth 3
                                        ;       Child Loop BB57_19 Depth 3
                                        ;       Child Loop BB57_22 Depth 3
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: r <- $w21
	.loc	0 125 9 is_stmt 1               ; experiments/EXP-008/referee/kernel.c:125:9
	; InlineAsm Start
	; InlineAsm End
Ltmp4841:
	;DEBUG_VALUE: j <- 0
	.loc	0 126 37                        ; experiments/EXP-008/referee/kernel.c:126:37
	ldr	w8, [x20, #4]
Ltmp4842:
	.loc	0 126 9 is_stmt 0               ; experiments/EXP-008/referee/kernel.c:126:9
	cbz	w8, LBB57_2
Ltmp4843:
; %bb.4:                                ;   in Loop: Header=BB57_3 Depth=1
	;DEBUG_VALUE: j <- 0
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 0 9                           ; experiments/EXP-008/referee/kernel.c:0:9
	mov	x26, #0                         ; =0x0
Ltmp4844:
	.loc	0 129 50 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:129:50
	ldr	w2, [x20]
	b	LBB57_6
Ltmp4845:
LBB57_5:                                ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 126 46                        ; experiments/EXP-008/referee/kernel.c:126:46
	add	x26, x26, #1
Ltmp4846:
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	.loc	0 126 37 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:126:37
	ldr	w8, [x20, #4]
Ltmp4847:
	.loc	0 126 9                         ; experiments/EXP-008/referee/kernel.c:126:9
	cmp	x26, x8
	b.hs	LBB57_2
Ltmp4848:
LBB57_6:                                ;   Parent Loop BB57_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB57_11 Depth 3
                                        ;       Child Loop BB57_14 Depth 3
                                        ;       Child Loop BB57_19 Depth 3
                                        ;       Child Loop BB57_22 Depth 3
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: j <- $x26
	.loc	0 127 37 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:127:37
	ldr	x8, [x20, #8]
	.loc	0 127 34 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:127:34
	ldr	x0, [x8, x26, lsl #3]
Ltmp4849:
	;DEBUG_VALUE: leaf <- $x0
	.loc	0 129 13 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:129:13
	add	x3, sp, #16
	mov	w1, #0                          ; =0x0
                                        ; kill: def $w2 killed $w2 killed $x2
	bl	_zbtScoreLeafDecodePolicy
Ltmp4850:
	.loc	0 130 13                        ; experiments/EXP-008/referee/kernel.c:130:13
	; InlineAsm Start
	; InlineAsm End
Ltmp4851:
	;DEBUG_VALUE: i <- 0
	.loc	0 0 13 is_stmt 0                ; experiments/EXP-008/referee/kernel.c:0:13
	ldr	w2, [x20]
Ltmp4852:
	.loc	0 132 13 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:132:13
	cmp	w2, #4
	b.lo	LBB57_9
Ltmp4853:
; %bb.7:                                ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	and	w8, w2, #0xfffffffc
	sub	x9, x2, #4
	cmp	x9, #27
	b.hi	LBB57_10
Ltmp4854:
; %bb.8:                                ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 0 13 is_stmt 0                ; experiments/EXP-008/referee/kernel.c:0:13
	mov	x9, #0                          ; =0x0
	b	LBB57_13
Ltmp4855:
LBB57_9:                                ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	mov	w8, #0                          ; =0x0
	.loc	0 132 13                        ; experiments/EXP-008/referee/kernel.c:132:13
	b	LBB57_15
Ltmp4856:
LBB57_10:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
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
Ltmp4857:
LBB57_11:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 133 34 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:133:34
	sub	x14, x13, #128
	sub	x15, x13, #64
	ld4.2d	{ v24, v25, v26, v27 }, [x14]
	ld4.2d	{ v28, v29, v30, v31 }, [x15]
	mov	x14, x13
	ld4.2d	{ v8, v9, v10, v11 }, [x14], #64
	ld4.2d	{ v12, v13, v14, v15 }, [x14]
	.loc	0 133 19 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:133:19
	add.2d	v4, v24, v4
	add.2d	v3, v28, v3
	add.2d	v22, v8, v22
	add.2d	v23, v12, v23
	.loc	0 134 19 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:134:19
	add.2d	v0, v25, v0
	add.2d	v5, v29, v5
	add.2d	v6, v9, v6
	add.2d	v7, v13, v7
	.loc	0 135 19                        ; experiments/EXP-008/referee/kernel.c:135:19
	add.2d	v1, v26, v1
	add.2d	v16, v30, v16
	add.2d	v17, v10, v17
	add.2d	v18, v14, v18
	.loc	0 136 19                        ; experiments/EXP-008/referee/kernel.c:136:19
	add.2d	v2, v27, v2
	add.2d	v19, v31, v19
	add.2d	v20, v11, v20
	add.2d	v21, v15, v21
	add	x13, x13, #256
	subs	x12, x12, #8
	b.ne	LBB57_11
Ltmp4858:
; %bb.12:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 132 13                        ; experiments/EXP-008/referee/kernel.c:132:13
	add.2d	v3, v3, v4
	add.2d	v3, v22, v3
	add.2d	v3, v23, v3
	addp.2d	d3, v3
	fmov	x25, d3
Ltmp4859:
	add.2d	v2, v19, v2
	add.2d	v2, v20, v2
	add.2d	v2, v21, v2
	addp.2d	d2, v2
	fmov	x27, d2
Ltmp4860:
	add.2d	v1, v16, v1
	add.2d	v1, v17, v1
	add.2d	v1, v18, v1
	addp.2d	d1, v1
	fmov	x28, d1
Ltmp4861:
	add.2d	v0, v5, v0
	add.2d	v0, v6, v0
	add.2d	v0, v7, v0
	addp.2d	d0, v0
	fmov	x19, d0
Ltmp4862:
	cmp	x10, x11
	b.eq	LBB57_15
Ltmp4863:
LBB57_13:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	add	x10, x9, #3
	add	x9, x24, x9, lsl #3
Ltmp4864:
LBB57_14:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: i <- [DW_OP_constu 3, DW_OP_minus, DW_OP_stack_value] $x10
	.loc	0 133 34                        ; experiments/EXP-008/referee/kernel.c:133:34
	ldp	x11, x12, [x9, #-16]
	.loc	0 133 19 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:133:19
	add	x25, x11, x25
Ltmp4865:
	;DEBUG_VALUE: decoder_batch:a <- $x25
	.loc	0 134 19 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:134:19
	add	x19, x12, x19
Ltmp4866:
	;DEBUG_VALUE: decoder_batch:b <- $x19
	.loc	0 135 34                        ; experiments/EXP-008/referee/kernel.c:135:34
	ldp	x11, x12, [x9], #32
	.loc	0 135 19 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:135:19
	add	x28, x11, x28
Ltmp4867:
	;DEBUG_VALUE: decoder_batch:c <- $x28
	.loc	0 136 19 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:136:19
	add	x27, x12, x27
Ltmp4868:
	;DEBUG_VALUE: i <- [DW_OP_plus_uconst 1, DW_OP_stack_value] $x10
	;DEBUG_VALUE: decoder_batch:d <- $x27
	.loc	0 132 26                        ; experiments/EXP-008/referee/kernel.c:132:26
	add	x10, x10, #4
Ltmp4869:
	.loc	0 132 13 is_stmt 0              ; experiments/EXP-008/referee/kernel.c:132:13
	cmp	x10, x2
	b.lo	LBB57_14
Ltmp4870:
LBB57_15:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: i <- $w8
	.loc	0 138 13 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:138:13
	cmp	w8, w2
	b.hs	LBB57_5
Ltmp4871:
; %bb.16:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- $w8
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	mov	w11, w8
	sub	x9, x2, x11
	cmp	x9, #7
	b.hi	LBB57_18
Ltmp4872:
; %bb.17:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- $w8
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 0 13 is_stmt 0                ; experiments/EXP-008/referee/kernel.c:0:13
	mov	x8, x11
Ltmp4873:
	b	LBB57_21
Ltmp4874:
LBB57_18:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: i <- $w8
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 138 13                        ; experiments/EXP-008/referee/kernel.c:138:13
	and	x10, x9, #0xfffffffffffffff8
	add	x8, x10, x11
Ltmp4875:
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x25
	ldr	x12, [sp, #8]                   ; 8-byte Folded Reload
	add	x11, x12, x11, lsl #3
	mov	x12, x10
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
Ltmp4876:
LBB57_19:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 138 56                        ; experiments/EXP-008/referee/kernel.c:138:56
	ldp	q4, q5, [x11, #-32]
	ldp	q6, q7, [x11], #64
	.loc	0 138 41                        ; experiments/EXP-008/referee/kernel.c:138:41
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	subs	x12, x12, #8
	b.ne	LBB57_19
Ltmp4877:
; %bb.20:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 138 13                        ; experiments/EXP-008/referee/kernel.c:138:13
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x25, d0
Ltmp4878:
	cmp	x9, x10
	b.eq	LBB57_5
Ltmp4879:
LBB57_21:                               ;   in Loop: Header=BB57_6 Depth=2
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	add	x9, x22, x8, lsl #3
	sub	x8, x2, x8
Ltmp4880:
LBB57_22:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	;DEBUG_VALUE: j <- $x26
	;DEBUG_VALUE: r <- $w21
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_consts 8, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_minus, DW_OP_consts 8, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	0 138 56                        ; experiments/EXP-008/referee/kernel.c:138:56
	ldr	x10, [x9], #8
	.loc	0 138 41                        ; experiments/EXP-008/referee/kernel.c:138:41
	add	x25, x10, x25
Ltmp4881:
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_consts 8, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_minus, DW_OP_consts 8, DW_OP_div, DW_OP_consts 1, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	;DEBUG_VALUE: decoder_batch:a <- $x25
	.loc	0 138 22                        ; experiments/EXP-008/referee/kernel.c:138:22
	subs	x8, x8, #1
	b.ne	LBB57_22
	b	LBB57_5
Ltmp4882:
LBB57_23:
	;DEBUG_VALUE: decoder_batch:d <- $x27
	;DEBUG_VALUE: decoder_batch:c <- $x28
	;DEBUG_VALUE: decoder_batch:b <- $x19
	;DEBUG_VALUE: decoder_batch:a <- $x25
	;DEBUG_VALUE: decoder_batch:f <- $x20
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 141 14 is_stmt 1              ; experiments/EXP-008/referee/kernel.c:141:14
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
Ltmp4883:
LBB57_24:
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	.loc	0 141 5 epilogue_begin is_stmt 0 ; experiments/EXP-008/referee/kernel.c:141:5
	add	sp, sp, #800
Ltmp4884:
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
Ltmp4885:
LBB57_25:
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	;DEBUG_VALUE: decoder_batch:a <- 0
	;DEBUG_VALUE: decoder_batch:b <- 0
	;DEBUG_VALUE: decoder_batch:c <- 0
	;DEBUG_VALUE: decoder_batch:d <- 0
	;DEBUG_VALUE: r <- 0
	;DEBUG_VALUE: decoder_batch:f <- $x0
	.loc	0 0 5                           ; experiments/EXP-008/referee/kernel.c:0:5
	mov	x0, #0                          ; =0x0
Ltmp4886:
	;DEBUG_VALUE: decoder_batch:f <- [DW_OP_LLVM_entry_value 1] $x0
	ldur	x8, [x29, #-160]
Lloh363:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh364:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh365:
	ldr	x9, [x9]
	cmp	x9, x8
	b.eq	LBB57_24
Ltmp4887:
LBB57_26:
	;DEBUG_VALUE: decoder_batch:rounds <- [DW_OP_plus_uconst 4] [$sp+0]
	bl	___stack_chk_fail
Ltmp4888:
	.loh AdrpLdrGotLdr	Lloh357, Lloh358, Lloh359
	.loh AdrpLdrGotLdr	Lloh360, Lloh361, Lloh362
	.loh AdrpLdrGotLdr	Lloh363, Lloh364, Lloh365
