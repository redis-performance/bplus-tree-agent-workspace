; Diagnostic compiler output; debug location directives omitted.
_zbtScoreLeafFindMember:                ; @zbtScoreLeafFindMember
Lfunc_begin54:
; %bb.0:
	sub	sp, sp, #144
	stp	x28, x27, [sp, #48]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #64]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #80]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #96]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #112]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #128]            ; 16-byte Folded Spill
	add	x29, sp, #128
	mov	x22, x3
	str	x2, [sp, #40]                   ; 8-byte Folded Spill
	str	w1, [sp, #36]                   ; 4-byte Folded Spill
	mov	x21, x0
	ldrb	w9, [x0, #52]
	cbz	x9, LBB54_2
; %bb.1:
	mov	x11, x21
	ldrb	w8, [x11, #17]!
	mov	w10, #7                         ; =0x7
	madd	w9, w8, w9, w10
	lsr	w9, w9, #3
	add	w9, w9, #9
	and	x9, x9, #0x7ffe
	add	x10, x21, x9
	add	x26, x10, #56
	cbnz	x8, LBB54_3
	b	LBB54_16
LBB54_2:
	mov	x11, x21
	ldrb	w8, [x11, #17]!
	add	x26, x11, #39
	cbz	x8, LBB54_16
LBB54_3:
	stp	x11, x4, [sp, #8]               ; 16-byte Folded Spill
	str	x5, [sp, #24]                   ; 8-byte Folded Spill
	add	x10, x21, #56
	str	x10, [sp]                       ; 8-byte Folded Spill
	add	x9, x10, x9
	add	x20, x9, x8, lsl #1
	ldr	w9, [sp, #36]                   ; 4-byte Folded Reload
	lsr	w25, w9, #24
	add	x24, x20, x8
	mov	x0, x20
	b	LBB54_6
LBB54_4:                                ;   in Loop: Header=BB54_6 Depth=1
	mov	x0, x19
	ldr	x1, [sp, #40]                   ; 8-byte Folded Reload
	mov	x2, x22
	bl	_memcmp
	cbz	w0, LBB54_18
LBB54_5:                                ;   in Loop: Header=BB54_6 Depth=1
	add	x0, x28, #1
	cmp	x0, x24
	b.hs	LBB54_16
LBB54_6:                                ; =>This Inner Loop Header: Depth=1
	sub	x2, x24, x0
	mov	x1, x25
	bl	_memchr
	cbz	x0, LBB54_17
; %bb.7:                                ;   in Loop: Header=BB54_6 Depth=1
	mov	x28, x0
	sub	x27, x0, x20
	ldrh	w8, [x26, w27, uxtw #1]
	add	x23, x21, x8
	ldrb	w8, [x23]
	cmp	w8, #254
	b.eq	LBB54_14
; %bb.8:                                ;   in Loop: Header=BB54_6 Depth=1
	cmp	w8, #255
	b.ne	LBB54_15
; %bb.9:                                ;   in Loop: Header=BB54_6 Depth=1
	ldur	w8, [x23, #1]
	ldr	w9, [sp, #36]                   ; 4-byte Folded Reload
	cmp	w8, w9
	b.ne	LBB54_5
; %bb.10:                               ;   in Loop: Header=BB54_6 Depth=1
	ldur	x19, [x23, #13]
	cbnz	x19, LBB54_13
; %bb.11:                               ;   in Loop: Header=BB54_6 Depth=1
Lloh319:
	adrp	x0, l_.str@PAGE
Lloh320:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #599                        ; =0x257
Lloh321:
	adrp	x2, l_.str.15@PAGE
Lloh322:
	add	x2, x2, l_.str.15@PAGEOFF
	bl	_standalone_panic
	ldrb	w8, [x23]
	cmp	w8, #255
	b.eq	LBB54_13
; %bb.12:                               ;   in Loop: Header=BB54_6 Depth=1
Lloh323:
	adrp	x0, l_.str@PAGE
Lloh324:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #567                        ; =0x237
Lloh325:
	adrp	x2, l_.str.10@PAGE
Lloh326:
	add	x2, x2, l_.str.10@PAGEOFF
	bl	_standalone_panic
LBB54_13:                               ;   in Loop: Header=BB54_6 Depth=1
	ldur	x8, [x23, #5]
	cmp	x8, x22
	b.ne	LBB54_5
	b	LBB54_4
LBB54_14:                               ;   in Loop: Header=BB54_6 Depth=1
	ldurh	w8, [x23, #1]
	add	x19, x23, #3
	cmp	x8, x22
	b.eq	LBB54_4
	b	LBB54_5
LBB54_15:                               ;   in Loop: Header=BB54_6 Depth=1
	add	x19, x23, #1
	cmp	x8, x22
	b.ne	LBB54_5
	b	LBB54_4
LBB54_16:
	mov	w0, #0                          ; =0x0
LBB54_17:
	ldp	x29, x30, [sp, #128]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #112]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #96]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #80]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #64]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #48]             ; 16-byte Folded Reload
	add	sp, sp, #144
	ret
LBB54_18:
	ldrb	w8, [x21, #53]
	cbz	w8, LBB54_20
; %bb.19:
	ldp	x11, x15, [sp, #8]              ; 16-byte Folded Reload
	ldrb	w9, [x11]
	mvn	w10, w27
	add	w27, w9, w10
	ldr	x14, [sp, #24]                  ; 8-byte Folded Reload
	cbnz	x15, LBB54_21
	b	LBB54_30
LBB54_20:
	ldp	x15, x14, [sp, #16]             ; 16-byte Folded Reload
	ldr	x11, [sp, #8]                   ; 8-byte Folded Reload
	cbz	x15, LBB54_30
LBB54_21:
	ldrb	w9, [x21, #52]
	cbz	w9, LBB54_28
; %bb.22:
	mov	x10, x27
	cbz	w8, LBB54_24
; %bb.23:
	ldrb	w10, [x11]
	mvn	w11, w27
	add	w10, w10, w11
LBB54_24:
	umull	x12, w9, w10
	lsr	x11, x12, #3
	ldr	x10, [sp]                       ; 8-byte Folded Reload
	ldr	x10, [x10, x11]
	and	x13, x12, #0x7
	lsr	x10, x10, x13
	ands	w12, w12, #0x7
	b.eq	LBB54_27
; %bb.25:
	mov	w13, #64                        ; =0x40
	sub	w12, w13, w12
	cmp	w12, w9
	b.hs	LBB54_27
; %bb.26:
	ldr	x13, [sp]                       ; 8-byte Folded Reload
	add	x11, x11, x13
	ldrb	w11, [x11, #8]
	lsl	x11, x11, x12
	orr	x10, x11, x10
LBB54_27:
	mov	x11, #-1                        ; =0xffffffffffffffff
	lsl	x12, x11, x9
	cmp	w9, #64
	csinv	x9, x11, x12, hs
	and	x9, x10, x9
	ldrb	w10, [x21, #19]
	lsl	x9, x9, x10
	b	LBB54_29
LBB54_28:
	mov	x9, #0                          ; =0x0
LBB54_29:
	ldr	x10, [x21, #40]
	cmp	w8, #0
	cneg	x8, x9, ne
	add	x8, x10, x8
	and	x9, x8, #0x7fffffffffffffff
	cmp	x8, #0
	csinv	x8, x9, x8, lt
	str	x8, [x15]
LBB54_30:
	cbz	x14, LBB54_32
; %bb.31:
	str	w27, [x14]
LBB54_32:
	mov	w0, #1                          ; =0x1
	b	LBB54_17
Lfunc_end54:
