_dependent_adds:                        ; @dependent_adds
Lfunc_begin2:
	.cfi_startproc
; %bb.0:
	;DEBUG_VALUE: dependent_adds:count <- $x0
	;DEBUG_VALUE: dependent_adds:x <- 0
	;DEBUG_VALUE: i <- 0
	.loc	0 76 5 prologue_end             ; bench/microbench.c:76:5
	cbz	x0, LBB2_4
Ltmp303:
; %bb.1:
	;DEBUG_VALUE: i <- 0
	;DEBUG_VALUE: dependent_adds:x <- 0
	;DEBUG_VALUE: dependent_adds:count <- $x0
	.loc	0 0 5 is_stmt 0                 ; bench/microbench.c:0:5
	mov	x9, #0                          ; =0x0
	mov	x8, #0                          ; =0x0
Ltmp304:
LBB2_2:                                 ; =>This Inner Loop Header: Depth=1
	;DEBUG_VALUE: dependent_adds:count <- $x0
	;DEBUG_VALUE: dependent_adds:x <- $x8
	;DEBUG_VALUE: i <- $x9
	.loc	0 77 9 is_stmt 1                ; bench/microbench.c:77:9
	; InlineAsm Start
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1
	add	x8, x8, #1

	; InlineAsm End
Ltmp305:
	;DEBUG_VALUE: dependent_adds:x <- $x8
	.loc	0 76 32                         ; bench/microbench.c:76:32
	add	x9, x9, #8
Ltmp306:
	;DEBUG_VALUE: i <- $x9
	.loc	0 76 5 is_stmt 0                ; bench/microbench.c:76:5
	cmp	x9, x0
	b.lo	LBB2_2
Ltmp307:
; %bb.3:
	;DEBUG_VALUE: dependent_adds:x <- $x8
	;DEBUG_VALUE: dependent_adds:count <- $x0
	.loc	0 83 5 is_stmt 1                ; bench/microbench.c:83:5
	mov	x0, x8
Ltmp308:
	;DEBUG_VALUE: dependent_adds:count <- [DW_OP_LLVM_entry_value 1] $x0
	ret
Ltmp309:
LBB2_4:
	;DEBUG_VALUE: dependent_adds:x <- 0
	;DEBUG_VALUE: dependent_adds:count <- $x0
	.loc	0 0 5 is_stmt 0                 ; bench/microbench.c:0:5
	mov	x8, #0                          ; =0x0
	.loc	0 83 5                          ; bench/microbench.c:83:5
	mov	x0, x8
Ltmp310:
	;DEBUG_VALUE: dependent_adds:count <- [DW_OP_LLVM_entry_value 1] $x0
	ret
Ltmp311:
Lfunc_end2:
	