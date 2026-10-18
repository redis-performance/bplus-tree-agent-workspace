_zbtScoreLeafDecodePolicy:              ; @zbtScoreLeafDecodePolicy
Lfunc_begin56:
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	.loc	1 5979 9 prologue_end is_stmt 1 ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5979:9
	cbz	w2, LBB56_25
Ltmp4549:
; %bb.1:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- $x3
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- $w2
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- $w1
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- $x0
	.loc	1 5981 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5981:33
	ldrb	w11, [x0, #52]
Ltmp4550:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:score_shift <- undef
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 5985 33                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5985:33
	ldr	x8, [x0, #40]
Ltmp4551:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	.loc	1 5987 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5987:9
	cbz	w11, LBB56_10
Ltmp4552:
; %bb.2:
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
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:9
	ldrb	w9, [x0, #19]
	ldrb	w14, [x0, #53]
Ltmp4553:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	ldrb	w15, [x0, #17]
Ltmp4554:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:leaf_count <- $w15
	mov	x10, #-1                        ; =0xffffffffffffffff
	.loc	1 5993 27 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5993:27
	lsl	x12, x10, x11
	cmp	w11, #64
	csinv	x10, x10, x12, eq
Ltmp4555:
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	.loc	1 5995 15                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5995:15
	tst	w11, #0x7
Ltmp4556:
	.loc	1 5995 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5995:9
	b.eq	LBB56_12
Ltmp4557:
; %bb.3:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:9
	add	x12, x0, #56
	mov	w13, w2
Ltmp4558:
	.loc	1 6011 20 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6011:20
	cmp	w11, #59
	b.lo	LBB56_16
Ltmp4559:
; %bb.4:
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
	b.eq	LBB56_16
Ltmp4560:
; %bb.5:
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
	.loc	1 6029 5                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6029:5
	mvn	w16, w1
	add	w15, w16, w15
Ltmp4561:
	.loc	1 0 5 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:5
	mov	w16, #64                        ; =0x40
	b	LBB56_7
Ltmp4562:
LBB56_6:                                ;   in Loop: Header=BB56_7 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6040 24 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6040:24
	and	x17, x17, x10
Ltmp4563:
	.loc	1 6040 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6040:32
	lsl	x17, x17, x9
Ltmp4564:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6041 34 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6041:34
	tst	w14, #0xff
	cneg	x17, x17, ne
Ltmp4565:
	add	x17, x17, x8
Ltmp4566:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x17
	;DEBUG_VALUE: ordered <- $x17
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x0, x17, #0x7fffffffffffffff
	cmp	x17, #0
	csinv	x17, x0, x17, lt
Ltmp4567:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x17
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x17
	.loc	1 6042 16                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6042:16
	str	x17, [x3], #8
Ltmp4568:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6029 28                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6029:28
	add	w1, w1, #1
Ltmp4569:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	sub	w15, w15, #1
	sub	x13, x13, #1
Ltmp4570:
	.loc	1 6029 5 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6029:5
	cbz	x13, LBB56_25
Ltmp4571:
LBB56_7:                                ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_stack_value] undef
	;DEBUG_VALUE: logical <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6031 35 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6031:35
	tst	w14, #0xff
	csel	w17, w1, w15, eq
Ltmp4572:
	;DEBUG_VALUE: physical <- $w17
	.loc	1 6032 48                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6032:48
	umull	x2, w11, w17
Ltmp4573:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:count <- [DW_OP_LLVM_entry_value 1] $w2
	;DEBUG_VALUE: bitpos <- $x2
	.loc	1 6033 36                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6033:36
	lsr	x0, x2, #3
Ltmp4574:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:leaf <- [DW_OP_LLVM_entry_value 1] $x0
	;DEBUG_VALUE: byte <- $x0
	.loc	1 6036 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6036:9
	ldr	x17, [x12, x0]
Ltmp4575:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6037 37                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6037:37
	and	x4, x2, #0x7
	lsr	x17, x17, x4
Ltmp4576:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 6034 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6034:32
	ands	w2, w2, #0x7
Ltmp4577:
	;DEBUG_VALUE: shift <- $w2
	.loc	1 0 32 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:32
	b.eq	LBB56_6
Ltmp4578:
; %bb.8:                                ;   in Loop: Header=BB56_7 Depth=1
	;DEBUG_VALUE: shift <- $w2
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6038 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6038:32
	sub	w2, w16, w2
Ltmp4579:
	.loc	1 6038 13 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6038:13
	cmp	w2, w11
	b.hs	LBB56_6
Ltmp4580:
; %bb.9:                                ;   in Loop: Header=BB56_7 Depth=1
	;DEBUG_VALUE: delta <- $x17
	;DEBUG_VALUE: byte <- $x0
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:mask <- $x10
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:reversed <- [DW_OP_LLVM_convert 8 7, DW_OP_LLVM_convert 32 7, DW_OP_stack_value] $w14
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:base <- $x8
	;DEBUG_VALUE: zbtScoreLeafDecodeRange:bits <- $w11
	.loc	1 6039 48 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6039:48
	add	x0, x0, x12
Ltmp4581:
	.loc	1 6039 32 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6039:32
	ldrb	w0, [x0, #8]
	.loc	1 6039 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6039:53
	lsl	x0, x0, x2
	.loc	1 6039 19                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6039:19
	orr	x17, x0, x17
Ltmp4582:
	;DEBUG_VALUE: delta <- $x17
	.loc	1 0 19                          ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:19
	b	LBB56_6
Ltmp4583:
LBB56_10:
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
	.loc	1 331 9 is_stmt 1               ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
Ltmp4584:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: value <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x8
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x8
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:32
	mov	w9, w2
Ltmp4585:
	.loc	1 5989 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:9
	cmp	w2, #8
	b.hs	LBB56_20
Ltmp4586:
; %bb.11:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:9
	mov	x10, #0                         ; =0x0
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:9
	b	LBB56_23
Ltmp4587:
LBB56_12:
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
	.loc	1 5998 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5998:38
	lsr	x11, x11, #3
Ltmp4588:
	;DEBUG_VALUE: stride <- $x11
	.loc	1 0 38 is_stmt 0                ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:38
	add	x12, x0, #56
Ltmp4589:
	;DEBUG_VALUE: i <- 0
	.loc	1 5999 32 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:32
	mov	w13, w2
	tst	w14, #0xff
	b.eq	LBB56_15
Ltmp4590:
; %bb.13:
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
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:9
	mvn	w14, w1
Ltmp4591:
	add	w14, w14, w15
Ltmp4592:
LBB56_14:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6003:13
	umull	x15, w11, w14
	ldr	x15, [x12, x15]
Ltmp4593:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6004:42
	and	x15, x15, x10
Ltmp4594:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6004:50
	lsl	x15, x15, x9
Ltmp4595:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6005:38
	sub	x15, x8, x15
Ltmp4596:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4597:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6006:20
	str	x15, [x3], #8
Ltmp4598:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4599:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:9
	cbnz	x13, LBB56_14
	b	LBB56_25
Ltmp4600:
LBB56_15:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6003 13 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6003:13
	umull	x14, w11, w1
	ldr	x14, [x12, x14]
Ltmp4601:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6004 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6004:42
	and	x14, x14, x10
Ltmp4602:
	.loc	1 6004 50 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6004:50
	lsl	x14, x14, x9
Ltmp4603:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6005 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6005:38
	add	x14, x14, x8
Ltmp4604:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4605:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6006 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6006:20
	str	x14, [x3], #8
Ltmp4606:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5999 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:32
	add	w1, w1, #1
Ltmp4607:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4608:
	.loc	1 5999 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5999:9
	b.ne	LBB56_15
	b	LBB56_25
Ltmp4609:
LBB56_16:
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
	.loc	1 0 9                           ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:9
	tst	w14, #0xff
	;DEBUG_VALUE: i <- 0
	b.eq	LBB56_19
Ltmp4610:
; %bb.17:
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
	.loc	1 6014 9 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6014:9
	mvn	w14, w1
Ltmp4611:
	add	w14, w14, w15
Ltmp4612:
LBB56_18:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6017 52                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6017:52
	umull	x15, w11, w14
Ltmp4613:
	;DEBUG_VALUE: bitpos <- $x15
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6019:13
	lsr	x16, x15, #3
	ldr	x16, [x12, x16]
Ltmp4614:
	;DEBUG_VALUE: delta <- $x16
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:54
	and	x15, x15, #0x7
Ltmp4615:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:43
	lsr	x15, x16, x15
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:60
	and	x15, x15, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:68
	lsl	x15, x15, x9
Ltmp4616:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6021:38
	sub	x15, x8, x15
Ltmp4617:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x15
	;DEBUG_VALUE: ordered <- $x15
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x16, x15, #0x7fffffffffffffff
	cmp	x15, #0
	csinv	x15, x16, x15, lt
Ltmp4618:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x15
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x15
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6022:20
	str	x15, [x3], #8
Ltmp4619:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6014:32
	sub	w14, w14, #1
	sub	x13, x13, #1
Ltmp4620:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6014:9
	cbnz	x13, LBB56_18
	b	LBB56_25
Ltmp4621:
LBB56_19:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 6017 52 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6017:52
	umull	x14, w11, w1
Ltmp4622:
	;DEBUG_VALUE: bitpos <- $x14
	.loc	1 6019 13                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6019:13
	lsr	x15, x14, #3
	ldr	x15, [x12, x15]
Ltmp4623:
	;DEBUG_VALUE: delta <- $x15
	.loc	1 6020 54                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:54
	and	x14, x14, #0x7
Ltmp4624:
	.loc	1 6020 43 is_stmt 0             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:43
	lsr	x14, x15, x14
	.loc	1 6020 60                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:60
	and	x14, x14, x10
	.loc	1 6020 68                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6020:68
	lsl	x14, x14, x9
Ltmp4625:
	;DEBUG_VALUE: delta <- $x14
	.loc	1 6021 38 is_stmt 1             ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6021:38
	add	x14, x14, x8
Ltmp4626:
	;DEBUG_VALUE: zbtOrderedToScore:ordered <- $x14
	;DEBUG_VALUE: ordered <- $x14
	.loc	1 331 9                         ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:331:9
	and	x15, x14, #0x7fffffffffffffff
	cmp	x14, #0
	csinv	x14, x15, x14, lt
Ltmp4627:
	;DEBUG_VALUE: zbtOrderedToScore:score <- $x14
	;DEBUG_VALUE: zbtOrderedToScore:bits <- $x14
	.loc	1 6022 20                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6022:20
	str	x14, [x3], #8
Ltmp4628:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:out <- [DW_OP_LLVM_entry_value 1] $x3
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 6014 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6014:32
	add	w1, w1, #1
Ltmp4629:
	;DEBUG_VALUE: zbtScoreLeafDecodePolicy:start <- [DW_OP_LLVM_entry_value 1] $w1
	subs	x13, x13, #1
Ltmp4630:
	.loc	1 6014 9 is_stmt 0              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6014:9
	b.ne	LBB56_19
	b	LBB56_25
Ltmp4631:
LBB56_20:
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
	.loc	1 5989 9 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:9
	and	x10, x9, #0xfffffff8
	dup.2d	v0, x8
	add	x11, x3, #32
Ltmp4632:
	.loc	1 0 9 is_stmt 0                 ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:0:9
	mov	x12, x10
Ltmp4633:
LBB56_21:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:53
	stp	q0, q0, [x11, #-32]
	stp	q0, q0, [x11], #64
	.loc	1 5989 42                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:42
	subs	x12, x12, #8
	b.ne	LBB56_21
Ltmp4634:
; %bb.22:
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
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:9
	cmp	x10, x9
	b.eq	LBB56_25
Ltmp4635:
LBB56_23:
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
Ltmp4636:
LBB56_24:                               ; =>This Inner Loop Header: Depth=1
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
	.loc	1 5989 53                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:53
	str	x8, [x10], #8
Ltmp4637:
	;DEBUG_VALUE: i <- [DW_OP_LLVM_arg 0, DW_OP_LLVM_arg 0, DW_OP_LLVM_convert 64 7, DW_OP_consts 18446744073709551615, DW_OP_LLVM_arg 0, DW_OP_mul, DW_OP_plus, DW_OP_minus, DW_OP_consts 18446744073709551615, DW_OP_div, DW_OP_consts 1, DW_OP_LLVM_arg 0, DW_OP_plus, DW_OP_plus, DW_OP_stack_value] undef
	.loc	1 5989 32                       ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:32
	subs	x9, x9, #1
Ltmp4638:
	.loc	1 5989 9                        ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:5989:9
	b.ne	LBB56_24
Ltmp4639:
LBB56_25:
	.loc	1 6050 1 is_stmt 1              ; experiments/EXP-008/referee/../../../worktrees/exp008-base/src/zset_btree.c:6050:1
	ret
Ltmp4640:
