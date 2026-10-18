_zbtScoreLeafDecodePolicy:              ; @zbtScoreLeafDecodePolicy
Lfunc_begin56:
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	.loc	1 6048 9 prologue_end is_stmt 1 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6048:9
	cmp	w2, #8
	b.hi	LBB56_9
Ltmp4549:
; %bb.1:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 0
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cbz	w2, LBB56_23
Ltmp4550:
; %bb.2:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	add	x9, x0, #56
	ldr	x8, [x0, #40]
Ltmp4551:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: i <- 0
	.loc	1 500 31 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4552:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_24
Ltmp4553:
; %bb.3:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	mov	x12, x1
Ltmp4554:
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	.loc	1 372 12 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_5
Ltmp4555:
; %bb.4:
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	mvn	w13, w1
	add	w12, w12, w13
Ltmp4556:
LBB56_5:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4557:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4558:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4559:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4560:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4561:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_8
Ltmp4562:
; %bb.6:
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4563:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_8
Ltmp4564:
; %bb.7:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4565:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4566:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_8:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
Ltmp4567:
	and	x11, x12, x11
Ltmp4568:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4569:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 0 15                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:15
	b	LBB56_25
Ltmp4570:
LBB56_9:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	.loc	1 5981 33 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5981:33
	ldrb	w11, [x0, #52]
Ltmp4571:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:score_shift <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 5985 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5985:33
	ldr	x8, [x0, #40]
Ltmp4572:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	.loc	1 5987 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5987:9
	cbz	w11, LBB56_18
Ltmp4573:
; %bb.10:
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
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	ldrb	w9, [x0, #19]
	ldrb	w14, [x0, #53]
Ltmp4574:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	ldrb	w15, [x0, #17]
Ltmp4575:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	mov	x10, #-1                        ; =0xffffffffffffffff
	.loc	1 5993 27 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5993:27
	lsl	x12, x10, x11
	cmp	w11, #64
	csinv	x10, x10, x12, eq
Ltmp4576:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	.loc	1 5995 15                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5995:15
	tst	w11, #0x7
Ltmp4577:
	.loc	1 5995 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5995:9
	b.eq	LBB56_29
Ltmp4578:
; %bb.11:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	add	x12, x0, #56
	mov	w13, w2
Ltmp4579:
	.loc	1 6011 20 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6011:20
	cmp	w11, #59
	b.lo	LBB56_33
Ltmp4580:
; %bb.12:
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
	b.eq	LBB56_33
Ltmp4581:
; %bb.13:
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
	.loc	1 6029 5                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6029:5
	mvn	w16, w1
	add	w15, w16, w15
Ltmp4582:
	.loc	1 0 5 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:5
	mov	w16, #64                        ; =0x40
	b	LBB56_15
Ltmp4583:
LBB56_14:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6040 24 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6040:24
	and	x17, x17, x10
Ltmp4584:
	.loc	1 6040 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6040:32
	lsl	x17, x17, x9
Ltmp4585:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6041 34 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6041:34
	tst	w14, #0xff
	cneg	x17, x17, ne
Ltmp4586:
	add	x17, x17, x8
Ltmp4587:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x17
	;DEBUG_VALUE: ordered <- $x17
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x0, x17, #0x7fffffffffffffff
	cmp	x17, #0
	csinv	x17, x0, x17, lt
Ltmp4588:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x17
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x17
	.loc	1 6042 16                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6042:16
	str	x17, [x3], #8
Ltmp4589:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6029 28                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6029:28
	add	w1, w1, #1
Ltmp4590:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	sub	w15, w15, #1
	sub	x13, x13, #1
Ltmp4591:
	.loc	1 6029 5 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6029:5
	cbz	x13, LBB56_23
Ltmp4592:
LBB56_15:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6031 35 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6031:35
	tst	w14, #0xff
	csel	w17, w1, w15, eq
Ltmp4593:
	;DEBUG_VALUE: physical <- $w17
	.loc	1 6032 48                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6032:48
	umull	x2, w11, w17
Ltmp4594:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- [DW_OP_LLVM_entry_value 1] $w2
	;DEBUG_VALUE: bitpos <- $x2
	.loc	1 6033 36                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6033:36
	lsr	x0, x2, #3
Ltmp4595:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- [DW_OP_LLVM_entry_value 1] $x0
	;DEBUG_VALUE: byte <- $x0
	.loc	1 6036 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6036:9
	ldr	x17, [x12, x0]
Ltmp4596:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6037 37                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6037:37
	and	x4, x2, #0x7
	lsr	x17, x17, x4
Ltmp4597:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6034 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6034:32
	ands	w2, w2, #0x7
Ltmp4598:
	;DEBUG_VALUE: shift <- $w2
	.loc	1 0 32 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:32
	b.eq	LBB56_14
Ltmp4599:
; %bb.16:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: shift <- $w2
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6038 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6038:32
	sub	w2, w16, w2
Ltmp4600:
	.loc	1 6038 13 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6038:13
	cmp	w2, w11
	b.hs	LBB56_14
Ltmp4601:
; %bb.17:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6039 48 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6039:48
	add	x0, x0, x12
Ltmp4602:
	.loc	1 6039 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6039:32
	ldrb	w0, [x0, #8]
	.loc	1 6039 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6039:53
	lsl	x0, x0, x2
	.loc	1 6039 19                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6039:19
	orr	x17, x0, x17
Ltmp4603:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	b	LBB56_14
Ltmp4604:
LBB56_18:
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
	.loc	1 331 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4605:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:32
	mov	w9, w2
Ltmp4606:
	.loc	1 5989 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:9
	and	x10, x9, #0xfffffff8
	dup.2d	v0, x8
	add	x11, x3, #32
Ltmp4607:
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	mov	x12, x10
Ltmp4608:
LBB56_19:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:53
	stp	q0, q0, [x11, #-32]
	stp	q0, q0, [x11], #64
	.loc	1 5989 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:42
	subs	x12, x12, #8
	b.ne	LBB56_19
Ltmp4609:
; %bb.20:
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
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:9
	subs	x10, x9, x10
	b.eq	LBB56_23
Ltmp4610:
; %bb.21:
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
Ltmp4611:
LBB56_22:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:53
	str	x8, [x9], #8
Ltmp4612:
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551608, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_consts 8, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 8, DW_OP_div, DW_OP_mul, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:32
	subs	x10, x10, #1
Ltmp4613:
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5989:9
	b.ne	LBB56_22
Ltmp4614:
LBB56_23:
	.loc	1 6054 1 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6054:1
	ret
LBB56_24:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
Ltmp4615:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 1 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:1
	mov	x11, #0                         ; =0x0
Ltmp4616:
LBB56_25:
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4617:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4618:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4619:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3]
Ltmp4620:
	;DEBUG_VALUE: i <- 1
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #1
	b.eq	LBB56_23
Ltmp4621:
; %bb.26:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 1, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4622:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_37
Ltmp4623:
; %bb.27:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 1, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_38
Ltmp4624:
; %bb.28:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #2
	b	LBB56_39
Ltmp4625:
LBB56_29:
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
	.loc	1 5998 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5998:38
	lsr	x11, x11, #3
Ltmp4626:
	;DEBUG_VALUE: stride <- $x11
	.loc	1 0 38 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:38
	add	x12, x0, #56
Ltmp4627:
	;DEBUG_VALUE: i <- 0
	.loc	1 5999 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:32
	mov	w13, w2
	tst	w14, #0xff
	b.eq	LBB56_32
Ltmp4628:
; %bb.30:
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
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:9
	mvn	w14, w1
Ltmp4629:
	add	w14, w14, w15
Ltmp4630:
LBB56_31:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6003:13
	umull	x15, w11, w14
	ldr	x15, [x12, x15]
Ltmp4631:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6004:42
	and	x15, x15, x10
Ltmp4632:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6004:50
	lsl	x15, x15, x9
Ltmp4633:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6005:38
	sub	x15, x8, x15
Ltmp4634:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4635:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6006:20
	str	x15, [x3], #8
Ltmp4636:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4637:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:9
	cbnz	x13, LBB56_31
	b	LBB56_23
Ltmp4638:
LBB56_32:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6003:13
	umull	x14, w11, w1
	ldr	x14, [x12, x14]
Ltmp4639:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6004:42
	and	x14, x14, x10
Ltmp4640:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6004:50
	lsl	x14, x14, x9
Ltmp4641:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6005:38
	add	x14, x14, x8
Ltmp4642:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4643:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6006:20
	str	x14, [x3], #8
Ltmp4644:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:32
	add	w1, w1, #1
Ltmp4645:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4646:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:5999:9
	b.ne	LBB56_32
	b	LBB56_23
Ltmp4647:
LBB56_33:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	tst	w14, #0xff
	;DEBUG_VALUE: i <- 0
	b.eq	LBB56_36
Ltmp4648:
; %bb.34:
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
	.loc	1 6014 9 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6014:9
	mvn	w14, w1
Ltmp4649:
	add	w14, w14, w15
Ltmp4650:
LBB56_35:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6017 52                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6017:52
	umull	x15, w11, w14
Ltmp4651:
	;DEBUG_VALUE: bitpos <- $x15
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6019:13
	lsr	x16, x15, #3
	ldr	x16, [x12, x16]
Ltmp4652:
	;DEBUG_VALUE: delta <- $x16
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:54
	and	x15, x15, #0x7
Ltmp4653:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:43
	lsr	x15, x16, x15
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:60
	and	x15, x15, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:68
	lsl	x15, x15, x9
Ltmp4654:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6021:38
	sub	x15, x8, x15
Ltmp4655:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4656:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6022:20
	str	x15, [x3], #8
Ltmp4657:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6014:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4658:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6014:9
	cbnz	x13, LBB56_35
	b	LBB56_23
Ltmp4659:
LBB56_36:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6017 52 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6017:52
	umull	x14, w11, w1
Ltmp4660:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6019:13
	lsr	x15, x14, #3
	ldr	x15, [x12, x15]
Ltmp4661:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:54
	and	x14, x14, #0x7
Ltmp4662:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:43
	lsr	x14, x15, x14
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:60
	and	x14, x14, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6020:68
	lsl	x14, x14, x9
Ltmp4663:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6021:38
	add	x14, x14, x8
Ltmp4664:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4665:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6022:20
	str	x14, [x3], #8
Ltmp4666:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6014:32
	add	w1, w1, #1
Ltmp4667:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4668:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6014:9
	b.ne	LBB56_36
	b	LBB56_23
Ltmp4669:
LBB56_37:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 1, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:9
	mov	x11, #0                         ; =0x0
Ltmp4670:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_43
Ltmp4671:
LBB56_38:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4672:
LBB56_39:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4673:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4674:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4675:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4676:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4677:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_42
Ltmp4678:
; %bb.40:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4679:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_42
Ltmp4680:
; %bb.41:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4681:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4682:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_42:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4683:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4684:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_43:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4685:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4686:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4687:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #8]
Ltmp4688:
	;DEBUG_VALUE: i <- 2
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #2
	b.eq	LBB56_23
Ltmp4689:
; %bb.44:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 2, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4690:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_47
Ltmp4691:
; %bb.45:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 2, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_48
Ltmp4692:
; %bb.46:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #3
	b	LBB56_49
Ltmp4693:
LBB56_47:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 2, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4694:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_53
Ltmp4695:
LBB56_48:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #2
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4696:
LBB56_49:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4697:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4698:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4699:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4700:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4701:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_52
Ltmp4702:
; %bb.50:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4703:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_52
Ltmp4704:
; %bb.51:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4705:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4706:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_52:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4707:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4708:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_53:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4709:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4710:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4711:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #16]
Ltmp4712:
	;DEBUG_VALUE: i <- 3
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #3
	b.eq	LBB56_23
Ltmp4713:
; %bb.54:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 3, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4714:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_57
Ltmp4715:
; %bb.55:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 3, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_58
Ltmp4716:
; %bb.56:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #4
	b	LBB56_59
Ltmp4717:
LBB56_57:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 3, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4718:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_63
Ltmp4719:
LBB56_58:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #3
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4720:
LBB56_59:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4721:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4722:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4723:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4724:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4725:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_62
Ltmp4726:
; %bb.60:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4727:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_62
Ltmp4728:
; %bb.61:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4729:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4730:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_62:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4731:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4732:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_63:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4733:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4734:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4735:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #24]
Ltmp4736:
	;DEBUG_VALUE: i <- 4
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #4
	b.eq	LBB56_23
Ltmp4737:
; %bb.64:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 4, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4738:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_67
Ltmp4739:
; %bb.65:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 4, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_68
Ltmp4740:
; %bb.66:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #5
	b	LBB56_69
Ltmp4741:
LBB56_67:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 4, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4742:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_73
Ltmp4743:
LBB56_68:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #4
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4744:
LBB56_69:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4745:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4746:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4747:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4748:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4749:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_72
Ltmp4750:
; %bb.70:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4751:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_72
Ltmp4752:
; %bb.71:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4753:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4754:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_72:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4755:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4756:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_73:
	;DEBUG_VALUE: i <- 4
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4757:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4758:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4759:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #32]
Ltmp4760:
	;DEBUG_VALUE: i <- 5
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #5
	b.eq	LBB56_23
Ltmp4761:
; %bb.74:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 5, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4762:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_77
Ltmp4763:
; %bb.75:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 5, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_78
Ltmp4764:
; %bb.76:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #6
	b	LBB56_79
Ltmp4765:
LBB56_77:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 5, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4766:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_83
Ltmp4767:
LBB56_78:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #5
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4768:
LBB56_79:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4769:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4770:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4771:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4772:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4773:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_82
Ltmp4774:
; %bb.80:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4775:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_82
Ltmp4776:
; %bb.81:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4777:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4778:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_82:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4779:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4780:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_83:
	;DEBUG_VALUE: i <- 5
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4781:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4782:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4783:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #40]
Ltmp4784:
	;DEBUG_VALUE: i <- 6
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #6
	b.eq	LBB56_23
Ltmp4785:
; %bb.84:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 6, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4786:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_87
Ltmp4787:
; %bb.85:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 6, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_88
Ltmp4788:
; %bb.86:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #7
	b	LBB56_89
Ltmp4789:
LBB56_87:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 6, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4790:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_93
Ltmp4791:
LBB56_88:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #6
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4792:
LBB56_89:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4793:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4794:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4795:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4796:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4797:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_92
Ltmp4798:
; %bb.90:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4799:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_92
Ltmp4800:
; %bb.91:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4801:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4802:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_92:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4803:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4804:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_93:
	;DEBUG_VALUE: i <- 6
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4805:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4806:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4807:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x10, [x3, #48]
Ltmp4808:
	;DEBUG_VALUE: i <- 7
	.loc	1 6049 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6049:9
	cmp	w2, #7
	b.eq	LBB56_23
Ltmp4809:
; %bb.94:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 7, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4810:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	cbz	w11, LBB56_97
Ltmp4811:
; %bb.95:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 7, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- undef
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- undef
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:12
	cbz	w10, LBB56_98
Ltmp4812:
; %bb.96:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #8
	b	LBB56_99
Ltmp4813:
LBB56_97:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 7, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:49
	mov	x9, #0                          ; =0x0
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:503:9
	b	LBB56_103
Ltmp4814:
LBB56_98:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6050 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:0
	add	w12, w1, #7
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4815:
LBB56_99:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4816:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4817:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4818:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4819:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4820:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:19
	b.eq	LBB56_102
Ltmp4821:
; %bb.100:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4822:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_102
Ltmp4823:
; %bb.101:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:48
	add	x9, x13, x9
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:32
	ldrb	w9, [x9, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:53
	lsl	x9, x9, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:510:19
	orr	x12, x9, x12
Ltmp4824:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_102:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:0:19
	mov	x9, #-1                         ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:511:13
	lsl	x13, x9, x11
Ltmp4825:
	cmp	w11, #64
	csinv	x9, x9, x13, hs
	and	x9, x12, x9
Ltmp4826:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:27
	ldrb	w11, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:513:15
	lsl	x9, x9, x11
Ltmp4827:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
LBB56_103:
	;DEBUG_VALUE: i <- 7
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x9, x9, ne
Ltmp4828:
	add	x8, x8, x9
Ltmp4829:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x8
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x8
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4830:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 6050 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6050:20
	str	x8, [x3, #56]
Ltmp4831:
	;DEBUG_VALUE: i <- 8
	.loc	1 6054 1                        ; experiments/EXP-008/referee/../../../worktrees/exp008-B/src/zset_btree.c:6054:1
	ret
Ltmp4832:
