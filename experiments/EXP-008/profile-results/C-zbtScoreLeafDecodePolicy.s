_zbtScoreLeafDecodePolicy:              ; @zbtScoreLeafDecodePolicy
Lfunc_begin56:
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	.loc	1 6051 9 prologue_end is_stmt 1 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6051:9
	cbz	w2, LBB56_34
Ltmp4549:
; %bb.1:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6053 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6053:9
	cmp	w2, #16
	b.hi	LBB56_12
Ltmp4550:
; %bb.2:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	mov	x8, #0                          ; =0x0
	ldr	x9, [x0, #40]
Ltmp4551:
	;DEBUG_VALUE: i <- 0
	add	x10, x0, #56
	mov	x11, #-1                        ; =0xffffffffffffffff
	mov	w12, #64                        ; =0x40
	mov	x13, x1
Ltmp4552:
	.loc	1 6054 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6054:32
	mov	w14, w2
	b	LBB56_5
Ltmp4553:
LBB56_3:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	.loc	1 511 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:511:13
	lsl	x2, x11, x16
	cmp	w16, #64
	csinv	x16, x11, x2, hs
Ltmp4554:
	and	x16, x17, x16
Ltmp4555:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x16
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:513:27
	ldrb	w17, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:513:15
	lsl	x16, x16, x17
Ltmp4556:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x16
LBB56_4:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x16
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:515:24
	cmp	w15, #0
	cneg	x15, x16, ne
	add	x15, x9, x15
Ltmp4557:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
Ltmp4558:
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4559:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6055 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6055:20
	str	x15, [x3], #8
Ltmp4560:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	.loc	1 6054 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6054:42
	add	x8, x8, #1
Ltmp4561:
	;DEBUG_VALUE: i <- $x8
	.loc	1 6054 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6054:32
	add	w13, w13, #1
	subs	x14, x14, #1
Ltmp4562:
	.loc	1 6054 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6054:9
	b.eq	LBB56_34
Ltmp4563:
LBB56_5:                                ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	.loc	1 500 31 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:500:31
	ldrb	w16, [x0, #52]
Ltmp4564:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:0
	ldrb	w15, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:503:9
	cbz	w16, LBB56_11
Ltmp4565:
; %bb.6:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	mov	x17, x13
Ltmp4566:
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	.loc	1 372 12 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:372:12
	cbz	w15, LBB56_8
Ltmp4567:
; %bb.7:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:372:37
	ldrb	w17, [x0, #17]
	add	w2, w8, w1
Ltmp4568:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- [DW_OP_LLVM_entry_value 1] $w2
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w2
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w2
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:372:49
	mvn	w2, w2
Ltmp4569:
	add	w17, w17, w2
Ltmp4570:
LBB56_8:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:504:68
	umull	x4, w16, w17
Ltmp4571:
	;DEBUG_VALUE: bitpos <- $x4
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:505:30
	lsr	x2, x4, #3
Ltmp4572:
	;DEBUG_VALUE: byte <- $x2
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:507:9
	ldr	x17, [x10, x2]
Ltmp4573:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:508:37
	and	x5, x4, #0x7
	lsr	x17, x17, x5
Ltmp4574:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:506:30
	ands	w4, w4, #0x7
Ltmp4575:
	;DEBUG_VALUE: shift <- $w4
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:509:19
	b.eq	LBB56_3
Ltmp4576:
; %bb.9:                                ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: shift <- $w4
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	;DEBUG_VALUE: byte <- $x2
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 509 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:509:32
	sub	w4, w12, w4
Ltmp4577:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:509:13
	cmp	w4, w16
	b.hs	LBB56_3
Ltmp4578:
; %bb.10:                               ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	;DEBUG_VALUE: byte <- $x2
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:510:48
	add	x2, x2, x10
Ltmp4579:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:510:32
	ldrb	w2, [x2, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:510:53
	lsl	x2, x2, x4
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:510:19
	orr	x17, x2, x17
Ltmp4580:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x17
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:19
	b	LBB56_3
Ltmp4581:
LBB56_11:                               ;   in Loop: Header=BB56_5 Depth=1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w16
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	mov	x16, #0                         ; =0x0
Ltmp4582:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:503:9
	b	LBB56_4
Ltmp4583:
LBB56_12:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	.loc	1 5981 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5981:33
	ldrb	w11, [x0, #52]
Ltmp4584:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:score_shift <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 5985 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5985:33
	ldr	x8, [x0, #40]
Ltmp4585:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	.loc	1 5987 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5987:9
	cbz	w11, LBB56_21
Ltmp4586:
; %bb.13:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	ldrb	w9, [x0, #19]
	ldrb	w14, [x0, #53]
Ltmp4587:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	ldrb	w15, [x0, #17]
Ltmp4588:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	mov	x10, #-1                        ; =0xffffffffffffffff
	.loc	1 5993 27 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5993:27
	lsl	x12, x10, x11
	cmp	w11, #64
	csinv	x10, x10, x12, eq
Ltmp4589:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	.loc	1 5995 15                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5995:15
	tst	w11, #0x7
Ltmp4590:
	.loc	1 5995 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5995:9
	b.eq	LBB56_26
Ltmp4591:
; %bb.14:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	add	x12, x0, #56
	mov	w13, w2
Ltmp4592:
	.loc	1 6011 20 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6011:20
	cmp	w11, #59
	b.lo	LBB56_30
Ltmp4593:
; %bb.15:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	cmp	w11, #60
	b.eq	LBB56_30
Ltmp4594:
; %bb.16:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6029 5                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6029:5
	mvn	w16, w1
	add	w15, w16, w15
Ltmp4595:
	.loc	1 0 5 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:5
	mov	w16, #64                        ; =0x40
	b	LBB56_18
Ltmp4596:
LBB56_17:                               ;   in Loop: Header=BB56_18 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6040 24 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6040:24
	and	x17, x17, x10
Ltmp4597:
	.loc	1 6040 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6040:32
	lsl	x17, x17, x9
Ltmp4598:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6041 34 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6041:34
	tst	w14, #0xff
	cneg	x17, x17, ne
Ltmp4599:
	add	x17, x17, x8
Ltmp4600:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x17
	;DEBUG_VALUE: ordered <- $x17
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x0, x17, #0x7fffffffffffffff
	cmp	x17, #0
	csinv	x17, x0, x17, lt
Ltmp4601:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x17
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x17
	.loc	1 6042 16                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6042:16
	str	x17, [x3], #8
Ltmp4602:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6029 28                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6029:28
	add	w1, w1, #1
Ltmp4603:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	sub	w15, w15, #1
	sub	x13, x13, #1
Ltmp4604:
	.loc	1 6029 5 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6029:5
	cbz	x13, LBB56_34
Ltmp4605:
LBB56_18:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6031 35 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6031:35
	tst	w14, #0xff
	csel	w17, w1, w15, eq
Ltmp4606:
	;DEBUG_VALUE: physical <- $w17
	.loc	1 6032 48                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6032:48
	umull	x2, w11, w17
Ltmp4607:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- [DW_OP_LLVM_entry_value 1] $w2
	;DEBUG_VALUE: bitpos <- $x2
	.loc	1 6033 36                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6033:36
	lsr	x0, x2, #3
Ltmp4608:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- [DW_OP_LLVM_entry_value 1] $x0
	;DEBUG_VALUE: byte <- $x0
	.loc	1 6036 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6036:9
	ldr	x17, [x12, x0]
Ltmp4609:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6037 37                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6037:37
	and	x4, x2, #0x7
	lsr	x17, x17, x4
Ltmp4610:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6034 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6034:32
	ands	w2, w2, #0x7
Ltmp4611:
	;DEBUG_VALUE: shift <- $w2
	.loc	1 0 32 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:32
	b.eq	LBB56_17
Ltmp4612:
; %bb.19:                               ;   in Loop: Header=BB56_18 Depth=1
	;DEBUG_VALUE: shift <- $w2
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6038 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6038:32
	sub	w2, w16, w2
Ltmp4613:
	.loc	1 6038 13 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6038:13
	cmp	w2, w11
	b.hs	LBB56_17
Ltmp4614:
; %bb.20:                               ;   in Loop: Header=BB56_18 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6039 48 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6039:48
	add	x0, x0, x12
Ltmp4615:
	.loc	1 6039 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6039:32
	ldrb	w0, [x0, #8]
	.loc	1 6039 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6039:53
	lsl	x0, x0, x2
	.loc	1 6039 19                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6039:19
	orr	x17, x0, x17
Ltmp4616:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:19
	b	LBB56_17
Ltmp4617:
LBB56_21:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x8
	.loc	1 331 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4618:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:32
	mov	w9, w2
Ltmp4619:
	.loc	1 5989 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:9
	and	x10, x9, #0xfffffff8
	dup.2d	v0, x8
	add	x11, x3, #32
Ltmp4620:
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	mov	x12, x10
Ltmp4621:
LBB56_22:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:53
	stp	q0, q0, [x11, #-32]
	stp	q0, q0, [x11], #64
	.loc	1 5989 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:42
	subs	x12, x12, #8
	b.ne	LBB56_22
Ltmp4622:
; %bb.23:
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:9
	subs	x10, x9, x10
	b.eq	LBB56_34
Ltmp4623:
; %bb.24:
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	lsl	x9, x9, #3
	and	x9, x9, #0x7ffffffc0
	add	x9, x3, x9
Ltmp4624:
LBB56_25:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551608, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 8, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:53
	str	x8, [x9], #8
Ltmp4625:
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551608, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_consts 8, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:32
	subs	x10, x10, #1
Ltmp4626:
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5989:9
	b.ne	LBB56_25
	b	LBB56_34
Ltmp4627:
LBB56_26:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: stride <- [DW_OP_constu 3, DW_OP_shr, DW_OP_stack_value] $w11
	.loc	1 5998 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5998:38
	lsr	x11, x11, #3
Ltmp4628:
	;DEBUG_VALUE: stride <- $x11
	.loc	1 0 38 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:38
	add	x12, x0, #56
Ltmp4629:
	;DEBUG_VALUE: i <- 0
	.loc	1 5999 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:32
	mov	w13, w2
	tst	w14, #0xff
	b.eq	LBB56_29
Ltmp4630:
; %bb.27:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: stride <- $x11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:9
	mvn	w14, w1
Ltmp4631:
	add	w14, w14, w15
Ltmp4632:
LBB56_28:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: stride <- $x11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	;DEBUG_VALUE: physical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 18446744073709551615, DW_OP_mul, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 32 7, DW_OP_plus, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6003:13
	umull	x15, w11, w14
	ldr	x15, [x12, x15]
Ltmp4633:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6004:42
	and	x15, x15, x10
Ltmp4634:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6004:50
	lsl	x15, x15, x9
Ltmp4635:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6005:38
	sub	x15, x8, x15
Ltmp4636:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4637:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6006:20
	str	x15, [x3], #8
Ltmp4638:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4639:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:9
	cbnz	x13, LBB56_28
	b	LBB56_34
Ltmp4640:
LBB56_29:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: stride <- $x11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	;DEBUG_VALUE: physical <- undef
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6003:13
	umull	x14, w11, w1
	ldr	x14, [x12, x14]
Ltmp4641:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6004:42
	and	x14, x14, x10
Ltmp4642:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6004:50
	lsl	x14, x14, x9
Ltmp4643:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6005:38
	add	x14, x14, x8
Ltmp4644:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4645:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6006:20
	str	x14, [x3], #8
Ltmp4646:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:32
	add	w1, w1, #1
Ltmp4647:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4648:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:5999:9
	b.ne	LBB56_29
	b	LBB56_34
Ltmp4649:
LBB56_30:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:0:9
	tst	w14, #0xff
	;DEBUG_VALUE: i <- 0
	b.eq	LBB56_33
Ltmp4650:
; %bb.31:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6014 9 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6014:9
	mvn	w14, w1
Ltmp4651:
	add	w14, w14, w15
Ltmp4652:
LBB56_32:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	;DEBUG_VALUE: physical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 18446744073709551615, DW_OP_mul, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 32 7, DW_OP_plus, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6017 52                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6017:52
	umull	x15, w11, w14
Ltmp4653:
	;DEBUG_VALUE: bitpos <- $x15
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6019:13
	lsr	x16, x15, #3
	ldr	x16, [x12, x16]
Ltmp4654:
	;DEBUG_VALUE: delta <- $x16
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:54
	and	x15, x15, #0x7
Ltmp4655:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:43
	lsr	x15, x16, x15
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:60
	and	x15, x15, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:68
	lsl	x15, x15, x9
Ltmp4656:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6021:38
	sub	x15, x8, x15
Ltmp4657:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4658:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6022:20
	str	x15, [x3], #8
Ltmp4659:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6014:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4660:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6014:9
	cbnz	x13, LBB56_32
	b	LBB56_34
Ltmp4661:
LBB56_33:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	;DEBUG_VALUE: physical <- undef
	.loc	1 6017 52 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6017:52
	umull	x14, w11, w1
Ltmp4662:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6019:13
	lsr	x15, x14, #3
	ldr	x15, [x12, x15]
Ltmp4663:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:54
	and	x14, x14, #0x7
Ltmp4664:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:43
	lsr	x14, x15, x14
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:60
	and	x14, x14, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6020:68
	lsl	x14, x14, x9
Ltmp4665:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6021:38
	add	x14, x14, x8
Ltmp4666:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4667:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6022:20
	str	x14, [x3], #8
Ltmp4668:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6014:32
	add	w1, w1, #1
Ltmp4669:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4670:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6014:9
	b.ne	LBB56_33
Ltmp4671:
LBB56_34:
	.loc	1 6060 1 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-C/src/zset_btree.c:6060:1
	ret
Ltmp4672:
