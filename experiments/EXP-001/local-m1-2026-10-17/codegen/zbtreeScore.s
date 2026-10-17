; Diagnostic compiler output; debug location directives omitted.
_zbtreeScore:                           ; @zbtreeScore
Lfunc_begin15:
; %bb.0:
	mov	x3, x2
	mov	x2, #0                          ; =0x0
	ldurb	w9, [x1, #-1]
	and	w8, w9, #0x7
	cmp	w8, #1
	b.le	LBB15_5
; %bb.1:
	cmp	w8, #2
	b.eq	LBB15_8
; %bb.2:
	cmp	w8, #3
	b.eq	LBB15_9
; %bb.3:
	cmp	w8, #4
	b.ne	LBB15_10
; %bb.4:
	ldur	x2, [x1, #-17]
	b	_zbtreeScoreRaw
LBB15_5:
	cbz	w8, LBB15_11
; %bb.6:
	cmp	w8, #1
	b.ne	LBB15_10
; %bb.7:
	ldurb	w2, [x1, #-3]
	b	_zbtreeScoreRaw
LBB15_8:
	ldurh	w2, [x1, #-5]
	b	_zbtreeScoreRaw
LBB15_9:
	ldur	w2, [x1, #-9]
LBB15_10:
	b	_zbtreeScoreRaw
LBB15_11:
	lsr	x2, x9, #3
	b	_zbtreeScoreRaw
Lfunc_end15:
