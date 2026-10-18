_zbtScoreLeafDecodePolicy:              ; @zbtScoreLeafDecodePolicy
Lfunc_begin56:
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	.loc	1 6050 9 prologue_end is_stmt 1 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6050:9
	cbz	w2, LBB56_28
Ltmp4549:
; %bb.1:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6052 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6052:9
	cmp	w2, #4
	b.hi	LBB56_9
Ltmp4550:
; %bb.2:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	ldr	x8, [x0, #40]
Ltmp4551:
	;DEBUG_VALUE: i <- 0
	add	x9, x0, #56
Ltmp4552:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	.loc	1 500 31 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4553:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	cbz	w11, LBB56_18
Ltmp4554:
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
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	mov	x12, x1
Ltmp4555:
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	.loc	1 372 12 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:12
	cbz	w10, LBB56_5
Ltmp4556:
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
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:49
	mvn	w13, w1
	add	w12, w12, w13
Ltmp4557:
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
	.loc	1 504 68 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4558:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4559:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4560:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4561:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4562:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:19
	b.eq	LBB56_8
Ltmp4563:
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
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4564:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_8
Ltmp4565:
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
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4566:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4567:
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
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
Ltmp4568:
	and	x11, x12, x11
Ltmp4569:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4570:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 0 15                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:15
	b	LBB56_19
Ltmp4571:
LBB56_9:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	.loc	1 5981 33 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5981:33
	ldrb	w11, [x0, #52]
Ltmp4572:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:score_shift <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 5985 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5985:33
	ldr	x8, [x0, #40]
Ltmp4573:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	.loc	1 5987 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5987:9
	cbz	w11, LBB56_23
Ltmp4574:
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
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	ldrb	w9, [x0, #19]
	ldrb	w14, [x0, #53]
Ltmp4575:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	ldrb	w15, [x0, #17]
Ltmp4576:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	mov	x10, #-1                        ; =0xffffffffffffffff
	.loc	1 5993 27 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5993:27
	lsl	x12, x10, x11
	cmp	w11, #64
	csinv	x10, x10, x12, eq
Ltmp4577:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	.loc	1 5995 15                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5995:15
	tst	w11, #0x7
Ltmp4578:
	.loc	1 5995 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5995:9
	b.eq	LBB56_25
Ltmp4579:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	add	x12, x0, #56
	mov	w13, w2
Ltmp4580:
	.loc	1 6011 20 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6011:20
	cmp	w11, #59
	b.lo	LBB56_30
Ltmp4581:
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
	b.eq	LBB56_30
Ltmp4582:
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
	.loc	1 6029 5                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6029:5
	mvn	w16, w1
	add	w15, w16, w15
Ltmp4583:
	.loc	1 0 5 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:5
	mov	w16, #64                        ; =0x40
	b	LBB56_15
Ltmp4584:
LBB56_14:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6040 24 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6040:24
	and	x17, x17, x10
Ltmp4585:
	.loc	1 6040 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6040:32
	lsl	x17, x17, x9
Ltmp4586:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6041 34 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6041:34
	tst	w14, #0xff
	cneg	x17, x17, ne
Ltmp4587:
	add	x17, x17, x8
Ltmp4588:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x17
	;DEBUG_VALUE: ordered <- $x17
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x0, x17, #0x7fffffffffffffff
	cmp	x17, #0
	csinv	x17, x0, x17, lt
Ltmp4589:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x17
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x17
	.loc	1 6042 16                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6042:16
	str	x17, [x3], #8
Ltmp4590:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6029 28                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6029:28
	add	w1, w1, #1
Ltmp4591:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	sub	w15, w15, #1
	sub	x13, x13, #1
Ltmp4592:
	.loc	1 6029 5 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6029:5
	cbz	x13, LBB56_28
Ltmp4593:
LBB56_15:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6031 35 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6031:35
	tst	w14, #0xff
	csel	w17, w1, w15, eq
Ltmp4594:
	;DEBUG_VALUE: physical <- $w17
	.loc	1 6032 48                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6032:48
	umull	x2, w11, w17
Ltmp4595:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- [DW_OP_LLVM_entry_value 1] $w2
	;DEBUG_VALUE: bitpos <- $x2
	.loc	1 6033 36                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6033:36
	lsr	x0, x2, #3
Ltmp4596:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- [DW_OP_LLVM_entry_value 1] $x0
	;DEBUG_VALUE: byte <- $x0
	.loc	1 6036 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6036:9
	ldr	x17, [x12, x0]
Ltmp4597:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6037 37                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6037:37
	and	x4, x2, #0x7
	lsr	x17, x17, x4
Ltmp4598:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6034 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6034:32
	ands	w2, w2, #0x7
Ltmp4599:
	;DEBUG_VALUE: shift <- $w2
	.loc	1 0 32 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:32
	b.eq	LBB56_14
Ltmp4600:
; %bb.16:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: shift <- $w2
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6038 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6038:32
	sub	w2, w16, w2
Ltmp4601:
	.loc	1 6038 13 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6038:13
	cmp	w2, w11
	b.hs	LBB56_14
Ltmp4602:
; %bb.17:                               ;   in Loop: Header=BB56_15 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6039 48 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6039:48
	add	x0, x0, x12
Ltmp4603:
	.loc	1 6039 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6039:32
	ldrb	w0, [x0, #8]
	.loc	1 6039 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6039:53
	lsl	x0, x0, x2
	.loc	1 6039 19                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6039:19
	orr	x17, x0, x17
Ltmp4604:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	b	LBB56_14
Ltmp4605:
LBB56_18:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	mov	x11, #0                         ; =0x0
Ltmp4606:
LBB56_19:
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w1
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4607:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4608:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4609:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6054 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:20
	str	x10, [x3]
Ltmp4610:
	;DEBUG_VALUE: i <- 1
	.loc	1 6053 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6053:9
	cmp	w2, #1
	b.eq	LBB56_28
Ltmp4611:
; %bb.20:
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
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4612:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	cbz	w11, LBB56_34
Ltmp4613:
; %bb.21:
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
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:12
	cbz	w10, LBB56_40
Ltmp4614:
; %bb.22:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #2
	b	LBB56_41
Ltmp4615:
LBB56_23:
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
	.loc	1 331 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4616:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:32
	mov	w9, w2
Ltmp4617:
	.loc	1 5989 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:9
	cmp	w2, #8
	b.hs	LBB56_35
Ltmp4618:
; %bb.24:
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	mov	x10, #0                         ; =0x0
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:9
	b	LBB56_38
Ltmp4619:
LBB56_25:
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
	.loc	1 5998 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5998:38
	lsr	x11, x11, #3
Ltmp4620:
	;DEBUG_VALUE: stride <- $x11
	.loc	1 0 38 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:38
	add	x12, x0, #56
Ltmp4621:
	;DEBUG_VALUE: i <- 0
	.loc	1 5999 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:32
	mov	w13, w2
	tst	w14, #0xff
	b.eq	LBB56_29
Ltmp4622:
; %bb.26:
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
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:9
	mvn	w14, w1
Ltmp4623:
	add	w14, w14, w15
Ltmp4624:
LBB56_27:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6003:13
	umull	x15, w11, w14
	ldr	x15, [x12, x15]
Ltmp4625:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6004:42
	and	x15, x15, x10
Ltmp4626:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6004:50
	lsl	x15, x15, x9
Ltmp4627:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6005:38
	sub	x15, x8, x15
Ltmp4628:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4629:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6006:20
	str	x15, [x3], #8
Ltmp4630:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4631:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:9
	cbnz	x13, LBB56_27
Ltmp4632:
LBB56_28:
	.loc	1 6059 1 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6059:1
	ret
LBB56_29:                               ; =>This Inner Loop Header: Depth=1
Ltmp4633:
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
	.loc	1 6003 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6003:13
	umull	x14, w11, w1
	ldr	x14, [x12, x14]
Ltmp4634:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6004:42
	and	x14, x14, x10
Ltmp4635:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6004:50
	lsl	x14, x14, x9
Ltmp4636:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6005:38
	add	x14, x14, x8
Ltmp4637:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4638:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6006:20
	str	x14, [x3], #8
Ltmp4639:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:32
	add	w1, w1, #1
Ltmp4640:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4641:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5999:9
	b.ne	LBB56_29
	b	LBB56_28
Ltmp4642:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	tst	w14, #0xff
	;DEBUG_VALUE: i <- 0
	b.eq	LBB56_33
Ltmp4643:
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
	.loc	1 6014 9 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6014:9
	mvn	w14, w1
Ltmp4644:
	add	w14, w14, w15
Ltmp4645:
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
	.loc	1 6017 52                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6017:52
	umull	x15, w11, w14
Ltmp4646:
	;DEBUG_VALUE: bitpos <- $x15
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6019:13
	lsr	x16, x15, #3
	ldr	x16, [x12, x16]
Ltmp4647:
	;DEBUG_VALUE: delta <- $x16
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:54
	and	x15, x15, #0x7
Ltmp4648:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:43
	lsr	x15, x16, x15
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:60
	and	x15, x15, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:68
	lsl	x15, x15, x9
Ltmp4649:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6021:38
	sub	x15, x8, x15
Ltmp4650:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4651:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6022:20
	str	x15, [x3], #8
Ltmp4652:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6014:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4653:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6014:9
	cbnz	x13, LBB56_32
	b	LBB56_28
Ltmp4654:
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
	.loc	1 6017 52 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6017:52
	umull	x14, w11, w1
Ltmp4655:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6019:13
	lsr	x15, x14, #3
	ldr	x15, [x12, x15]
Ltmp4656:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:54
	and	x14, x14, #0x7
Ltmp4657:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:43
	lsr	x14, x15, x14
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:60
	and	x14, x14, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6020:68
	lsl	x14, x14, x9
Ltmp4658:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6021:38
	add	x14, x14, x8
Ltmp4659:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4660:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6022:20
	str	x14, [x3], #8
Ltmp4661:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6014:32
	add	w1, w1, #1
Ltmp4662:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4663:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6014:9
	b.ne	LBB56_33
	b	LBB56_28
Ltmp4664:
LBB56_34:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 1, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	mov	x11, #0                         ; =0x0
Ltmp4665:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	b	LBB56_45
Ltmp4666:
LBB56_35:
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:9
	and	x10, x9, #0xfffffff8
	dup.2d	v0, x8
	add	x11, x3, #32
Ltmp4667:
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:9
	mov	x12, x10
Ltmp4668:
LBB56_36:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:53
	stp	q0, q0, [x11, #-32]
	stp	q0, q0, [x11], #64
	.loc	1 5989 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:42
	subs	x12, x12, #8
	b.ne	LBB56_36
Ltmp4669:
; %bb.37:
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
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:9
	cmp	x10, x9
	b.eq	LBB56_28
Ltmp4670:
LBB56_38:
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
	sub	x9, x9, x10
	add	x10, x3, x10, lsl #3
Ltmp4671:
LBB56_39:                               ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:53
	str	x8, [x10], #8
Ltmp4672:
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:32
	subs	x9, x9, #1
Ltmp4673:
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:5989:9
	b.ne	LBB56_39
	b	LBB56_28
Ltmp4674:
LBB56_40:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6054 0 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:0
	add	w12, w1, #1
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4675:
LBB56_41:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4676:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4677:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4678:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4679:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4680:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:19
	b.eq	LBB56_44
Ltmp4681:
; %bb.42:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4682:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_44
Ltmp4683:
; %bb.43:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4684:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4685:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_44:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4686:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4687:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_45:
	;DEBUG_VALUE: i <- 1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4688:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4689:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4690:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6054 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:20
	str	x10, [x3, #8]
Ltmp4691:
	;DEBUG_VALUE: i <- 2
	.loc	1 6053 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6053:9
	cmp	w2, #2
	b.eq	LBB56_28
Ltmp4692:
; %bb.46:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 2, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4693:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	cbz	w11, LBB56_49
Ltmp4694:
; %bb.47:
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
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:12
	cbz	w10, LBB56_50
Ltmp4695:
; %bb.48:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #3
	b	LBB56_51
Ltmp4696:
LBB56_49:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 2, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:49
	mov	x11, #0                         ; =0x0
Ltmp4697:
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	b	LBB56_55
Ltmp4698:
LBB56_50:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6054 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:0
	add	w12, w1, #2
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4699:
LBB56_51:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4700:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4701:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4702:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4703:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4704:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:19
	b.eq	LBB56_54
Ltmp4705:
; %bb.52:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4706:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_54
Ltmp4707:
; %bb.53:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:48
	add	x13, x13, x9
Ltmp4708:
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:32
	ldrb	w13, [x13, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:53
	lsl	x13, x13, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:19
	orr	x12, x13, x12
Ltmp4709:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_54:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	x13, #-1                        ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:511:13
	lsl	x14, x13, x11
	cmp	w11, #64
	csinv	x11, x13, x14, hs
	and	x11, x12, x11
Ltmp4710:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:27
	ldrb	w12, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:15
	lsl	x11, x11, x12
Ltmp4711:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
LBB56_55:
	;DEBUG_VALUE: i <- 2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x11
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x10, x11, ne
	add	x10, x8, x10
Ltmp4712:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x10
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x10
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x11, x10, #0x7fffffffffffffff
Ltmp4713:
	cmp	x10, #0
	csinv	x10, x11, x10, lt
Ltmp4714:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x10
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x10
	.loc	1 6054 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:20
	str	x10, [x3, #16]
Ltmp4715:
	;DEBUG_VALUE: i <- 3
	.loc	1 6053 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6053:9
	cmp	w2, #3
	b.eq	LBB56_28
Ltmp4716:
; %bb.56:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 3, DW_OP_stack_value] $w1
	.loc	1 500 31                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:500:31
	ldrb	w11, [x0, #52]
Ltmp4717:
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	.loc	1 0 0 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:0
	ldrb	w10, [x0, #53]
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	cbz	w11, LBB56_59
Ltmp4718:
; %bb.57:
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
	.loc	1 372 12                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:12
	cbz	w10, LBB56_60
Ltmp4719:
; %bb.58:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 372 37 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:37
	ldrb	w12, [x0, #17]
	.loc	1 372 49                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:372:49
	sub	w12, w12, w1
	sub	w12, w12, #4
	b	LBB56_61
Ltmp4720:
LBB56_59:
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- [DW_OP_plus_uconst 3, DW_OP_stack_value] $w1
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- 0
	;DEBUG_VALUE: zbtScoreLeafScore:bits <- $w11
	;DEBUG_VALUE: zbtScoreLeafScore:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 49                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:49
	mov	x9, #0                          ; =0x0
	.loc	1 503 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:503:9
	b	LBB56_65
Ltmp4721:
LBB56_60:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 6054 0                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:0
	add	w12, w1, #3
	;DEBUG_VALUE: zbtScoreLeafPhysicalPos:pos <- $w12
	;DEBUG_VALUE: zbtScoreLeafScore:pos <- $w12
Ltmp4722:
LBB56_61:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 504 68                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:504:68
	umull	x14, w11, w12
Ltmp4723:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 505 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:505:30
	lsr	x13, x14, #3
Ltmp4724:
	;DEBUG_VALUE: byte <- $x13
	.loc	1 507 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:507:9
	ldr	x12, [x9, x13]
Ltmp4725:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 508 37                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:508:37
	and	x15, x14, #0x7
	lsr	x12, x12, x15
Ltmp4726:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 506 30                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:506:30
	ands	w14, w14, #0x7
Ltmp4727:
	;DEBUG_VALUE: shift <- $w14
	.loc	1 509 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:19
	b.eq	LBB56_64
Ltmp4728:
; %bb.62:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: shift <- $w14
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 0 19 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	w15, #64                        ; =0x40
	.loc	1 509 32                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:32
	sub	w14, w15, w14
Ltmp4729:
	.loc	1 509 13                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:509:13
	cmp	w14, w11
	b.hs	LBB56_64
Ltmp4730:
; %bb.63:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 510 48 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:48
	add	x9, x13, x9
	.loc	1 510 32 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:32
	ldrb	w9, [x9, #8]
	.loc	1 510 53                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:53
	lsl	x9, x9, x14
	.loc	1 510 19                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:510:19
	orr	x12, x9, x12
Ltmp4731:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
LBB56_64:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	;DEBUG_VALUE: byte <- $x13
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x12
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:0:19
	mov	x9, #-1                         ; =0xffffffffffffffff
	.loc	1 511 13 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:511:13
	lsl	x13, x9, x11
Ltmp4732:
	cmp	w11, #64
	csinv	x9, x9, x13, hs
	and	x9, x12, x9
Ltmp4733:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
	.loc	1 513 27                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:27
	ldrb	w11, [x0, #19]
	.loc	1 513 15 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:513:15
	lsl	x9, x9, x11
Ltmp4734:
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
LBB56_65:
	;DEBUG_VALUE: i <- 3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafScore:delta <- $x9
	.loc	1 515 24 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:515:24
	cmp	w10, #0
	cneg	x9, x9, ne
Ltmp4735:
	add	x8, x8, x9
Ltmp4736:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x8
	;DEBUG_VALUE: zbtScoreLeafScore:ordered <- $x8
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4737:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 6054 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6054:20
	str	x8, [x3, #24]
Ltmp4738:
	;DEBUG_VALUE: i <- 4
	.loc	1 6059 1                        ; experiments/EXP-008/referee/../../../worktrees/exp008-A/src/zset_btree.c:6059:1
	ret
Ltmp4739:
