; Diagnostic compiler output; debug location directives omitted.
_zbtScoreLeafLowerBound:                ; @zbtScoreLeafLowerBound
Lfunc_begin48:
; %bb.0:
	sub	sp, sp, #128
	stp	d9, d8, [sp, #16]               ; 16-byte Folded Spill
	stp	x28, x27, [sp, #32]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #48]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #64]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #80]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #96]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #112]            ; 16-byte Folded Spill
	add	x29, sp, #112
	stp	x1, x2, [sp]                    ; 16-byte Folded Spill
	ldrb	w27, [x0, #17]
	cbz	w27, LBB48_29
; %bb.1:
	fmov	d8, d0
	mov	x21, x0
	mov	w22, #0                         ; =0x0
	add	x28, x0, #56
	ldrb	w23, [x0, #52]
	mov	x25, #-1                        ; =0xffffffffffffffff
	b	LBB48_4
LBB48_2:                                ;   in Loop: Header=BB48_4 Depth=1
	mov	w0, #-1                         ; =0xffffffff
LBB48_3:                                ;   in Loop: Header=BB48_4 Depth=1
	cmp	w0, #0
	csel	w27, w27, w24, lt
	csinc	w22, w22, w24, ge
	cmp	w22, w27
	b.hs	LBB48_30
LBB48_4:                                ; =>This Inner Loop Header: Depth=1
	cbz	w23, LBB48_21
; %bb.5:                                ;   in Loop: Header=BB48_4 Depth=1
	ldrb	w8, [x21, #17]
	mov	w9, #7                          ; =0x7
	madd	w8, w8, w23, w9
	lsr	w8, w8, #3
	add	w8, w8, #9
	and	x9, x8, #0x7ffe
	sub	w8, w27, w22
	add	w24, w22, w8, lsr #1
	ldrb	w8, [x21, #53]
	mov	x10, x24
	cbz	w8, LBB48_7
LBB48_6:                                ;   in Loop: Header=BB48_4 Depth=1
	ldrb	w10, [x21, #17]
	mvn	w11, w24
	add	w10, w10, w11
LBB48_7:                                ;   in Loop: Header=BB48_4 Depth=1
	add	x9, x28, x9
	ldrh	w9, [x9, w10, uxtw #1]
	add	x19, x21, x9
	ldrb	w20, [x19]
	cmp	w20, #253
	b.hi	LBB48_15
; %bb.8:                                ;   in Loop: Header=BB48_4 Depth=1
	add	x26, x19, #1
	cbz	w23, LBB48_17
LBB48_9:                                ;   in Loop: Header=BB48_4 Depth=1
	mov	x9, x24
	cbz	w8, LBB48_11
; %bb.10:                               ;   in Loop: Header=BB48_4 Depth=1
	ldrb	w9, [x21, #17]
	mvn	w10, w24
	add	w9, w9, w10
LBB48_11:                               ;   in Loop: Header=BB48_4 Depth=1
	umull	x11, w9, w23
	lsr	x10, x11, #3
	ldr	x9, [x28, x10]
	and	x12, x11, #0x7
	lsr	x9, x9, x12
	ands	w11, w11, #0x7
	b.eq	LBB48_14
; %bb.12:                               ;   in Loop: Header=BB48_4 Depth=1
	mov	w12, #64                        ; =0x40
	sub	w11, w12, w11
	cmp	w11, w23
	b.hs	LBB48_14
; %bb.13:                               ;   in Loop: Header=BB48_4 Depth=1
	add	x10, x10, x28
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x11
	orr	x9, x10, x9
LBB48_14:                               ;   in Loop: Header=BB48_4 Depth=1
	mov	w10, w23
	lsl	x10, x25, x10
	cmp	w23, #64
	csinv	x10, x25, x10, hs
	and	x9, x9, x10
	ldrb	w10, [x21, #19]
	lsl	x9, x9, x10
	b	LBB48_18
LBB48_15:                               ;   in Loop: Header=BB48_4 Depth=1
	cmp	w20, #254
	b.ne	LBB48_22
; %bb.16:                               ;   in Loop: Header=BB48_4 Depth=1
	ldurh	w20, [x19, #1]
	add	x26, x19, #3
	cbnz	w23, LBB48_9
LBB48_17:                               ;   in Loop: Header=BB48_4 Depth=1
	mov	x9, #0                          ; =0x0
LBB48_18:                               ;   in Loop: Header=BB48_4 Depth=1
	ldr	x10, [x21, #40]
	cmp	w8, #0
	cneg	x8, x9, ne
	add	x8, x10, x8
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
	fmov	d0, x8
	fcmp	d0, d8
	b.mi	LBB48_2
; %bb.19:                               ;   in Loop: Header=BB48_4 Depth=1
	b.le	LBB48_26
; %bb.20:                               ;   in Loop: Header=BB48_4 Depth=1
	mov	w0, #1                          ; =0x1
	b	LBB48_3
LBB48_21:                               ;   in Loop: Header=BB48_4 Depth=1
	mov	x9, #0                          ; =0x0
	sub	w8, w27, w22
	add	w24, w22, w8, lsr #1
	ldrb	w8, [x21, #53]
	mov	x10, x24
	cbnz	w8, LBB48_6
	b	LBB48_7
LBB48_22:                               ;   in Loop: Header=BB48_4 Depth=1
	ldur	x26, [x19, #13]
	cbnz	x26, LBB48_25
; %bb.23:                               ;   in Loop: Header=BB48_4 Depth=1
Lloh299:
	adrp	x0, l_.str@PAGE
Lloh300:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #599                        ; =0x257
Lloh301:
	adrp	x2, l_.str.15@PAGE
Lloh302:
	add	x2, x2, l_.str.15@PAGEOFF
	bl	_standalone_panic
	ldrb	w8, [x19]
	cmp	w8, #255
	b.eq	LBB48_25
; %bb.24:                               ;   in Loop: Header=BB48_4 Depth=1
Lloh303:
	adrp	x0, l_.str@PAGE
Lloh304:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #567                        ; =0x237
Lloh305:
	adrp	x2, l_.str.10@PAGE
Lloh306:
	add	x2, x2, l_.str.10@PAGEOFF
	bl	_standalone_panic
LBB48_25:                               ;   in Loop: Header=BB48_4 Depth=1
	ldur	x20, [x19, #5]
	ldrb	w23, [x21, #52]
	ldrb	w8, [x21, #53]
	cbnz	w23, LBB48_9
	b	LBB48_17
LBB48_26:                               ;   in Loop: Header=BB48_4 Depth=1
	ldp	x1, x8, [sp]                    ; 16-byte Folded Reload
	cmp	x20, x8
	csel	x2, x20, x8, lo
	mov	x0, x26
	bl	_memcmp
	cbnz	w0, LBB48_3
; %bb.27:                               ;   in Loop: Header=BB48_4 Depth=1
	ldr	x8, [sp, #8]                    ; 8-byte Folded Reload
	cmp	x20, x8
	b.lo	LBB48_2
; %bb.28:                               ;   in Loop: Header=BB48_4 Depth=1
	cset	w0, hi
	b	LBB48_3
LBB48_29:
	mov	w22, #0                         ; =0x0
LBB48_30:
	mov	x0, x22
	ldp	x29, x30, [sp, #112]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #96]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #80]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #64]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #48]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #32]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp, #16]               ; 16-byte Folded Reload
	add	sp, sp, #128
	ret
Lfunc_end48:
