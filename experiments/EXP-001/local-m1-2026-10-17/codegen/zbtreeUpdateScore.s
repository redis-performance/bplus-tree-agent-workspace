; Diagnostic compiler output; debug location directives omitted.
_zbtreeUpdateScore:                     ; @zbtreeUpdateScore
Lfunc_begin37:
; %bb.0:
	sub	sp, sp, #160
	stp	d9, d8, [sp, #48]               ; 16-byte Folded Spill
	stp	x28, x27, [sp, #64]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #80]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #96]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #112]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #128]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #144]            ; 16-byte Folded Spill
	add	x29, sp, #144
	fmov	d8, d0
	mov	x23, x1
	mov	x19, x0
	ldr	x21, [x2, #16]
	ldp	w22, w20, [x2, #24]
	ldr	w8, [x2, #32]
	ldr	w9, [x0, #92]
	cmp	w8, w9
	b.eq	LBB37_2
; %bb.1:
Lloh205:
	adrp	x0, l_.str@PAGE
Lloh206:
	add	x0, x0, l_.str@PAGEOFF
Lloh207:
	adrp	x2, l_.str.3@PAGE
Lloh208:
	add	x2, x2, l_.str.3@PAGEOFF
	mov	w1, #3650                       ; =0xe42
	bl	_standalone_panic
LBB37_2:
	cbz	x21, LBB37_8
; %bb.3:
	ldrb	w8, [x21, #17]
	cmp	w22, w8
	b.hs	LBB37_8
; %bb.4:
	mov	x3, #0                          ; =0x0
	ldurb	w9, [x23, #-1]
	and	w8, w9, #0x7
	cmp	w8, #1
	b.le	LBB37_13
; %bb.5:
	cmp	w8, #2
	b.eq	LBB37_18
; %bb.6:
	cmp	w8, #3
	b.ne	LBB37_11
LBB37_7:
	ldur	w3, [x23, #-9]
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
	b	LBB37_20
LBB37_8:
Lloh209:
	adrp	x0, l_.str@PAGE
Lloh210:
	add	x0, x0, l_.str@PAGEOFF
Lloh211:
	adrp	x2, l_.str.4@PAGE
Lloh212:
	add	x2, x2, l_.str.4@PAGEOFF
	mov	w1, #3651                       ; =0xe43
	bl	_standalone_panic
	mov	x3, #0                          ; =0x0
	ldurb	w9, [x23, #-1]
	and	w8, w9, #0x7
	cmp	w8, #1
	b.le	LBB37_13
; %bb.9:
	cmp	w8, #2
	b.eq	LBB37_17
; %bb.10:
	cmp	w8, #3
	b.eq	LBB37_7
LBB37_11:
	cmp	w8, #4
	b.ne	LBB37_19
; %bb.12:
	ldur	x3, [x23, #-17]
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
	b	LBB37_20
LBB37_13:
	cbz	w8, LBB37_16
; %bb.14:
	cmp	w8, #1
	b.ne	LBB37_19
; %bb.15:
	ldurb	w3, [x23, #-3]
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
	b	LBB37_20
LBB37_16:
	lsr	x3, x9, #3
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
	b	LBB37_20
LBB37_17:
	ldurh	w3, [x23, #-5]
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
	b	LBB37_20
LBB37_18:
	ldurh	w3, [x23, #-5]
LBB37_19:
	mov	x0, x21
	mov	x1, x22
	fmov	d0, d8
	mov	x2, x23
	bl	_zbtScoreUpdateInPlace
	cbnz	w0, LBB37_101
LBB37_20:
	ldr	w8, [x19, #84]
	mov	w9, #32767                      ; =0x7fff
	cmp	w8, w9
	b.lo	LBB37_29
; %bb.21:
	ldr	x9, [x19, #64]
	cbz	x9, LBB37_26
; %bb.22:
	ldr	w9, [x9, #32]
	cbnz	w9, LBB37_29
; %bb.23:
	mov	w9, #65519                      ; =0xffef
	cmp	w8, w9
	b.hs	LBB37_25
; %bb.24:
	mov	x0, x19
	mov	w1, #4                          ; =0x4
	bl	_zbtIndexRehashStep
	ldr	x8, [x19, #64]
	cbnz	x8, LBB37_29
	b	LBB37_26
LBB37_25:                               ; =>This Inner Loop Header: Depth=1
	mov	x0, x19
	mov	w1, #64                         ; =0x40
	bl	_zbtIndexRehashStep
	ldr	x8, [x19, #64]
	cbnz	x8, LBB37_25
LBB37_26:
	ldr	x8, [x19, #32]
	cbz	x8, LBB37_29
; %bb.27:
	ldr	w8, [x19, #56]
	cbnz	w8, LBB37_29
; %bb.28:
	ldr	x1, [x19, #40]
	mov	x0, x19
	mov	w2, #1                          ; =0x1
	bl	_zbtIndexStartResize
LBB37_29:
	ldrb	w8, [x21, #52]
	mov	w24, #7                         ; =0x7
	cbz	x8, LBB37_31
; %bb.30:
	ldrb	w9, [x21, #17]
	madd	w8, w9, w8, w24
	lsr	w8, w8, #3
	add	w8, w8, #9
	and	x8, x8, #0x7ffe
LBB37_31:
	ldrb	w10, [x21, #53]
	mov	x9, x22
	cbz	w10, LBB37_33
; %bb.32:
	ldrb	w9, [x21, #17]
	mvn	w10, w22
	add	w9, w9, w10
LBB37_33:
	add	x25, x21, #56
	add	x8, x25, x8
	ldrh	w8, [x8, w9, uxtw #1]
	add	x26, x21, x8
	ldrb	w8, [x26]
	cmp	w8, #253
	b.ls	LBB37_36
; %bb.34:
	cmp	w8, #254
	b.ne	LBB37_45
; %bb.35:
	ldurh	w8, [x26, #1]
LBB37_36:
	str	x8, [sp, #16]
LBB37_37:
	add	x8, sp, #8
	add	x8, x8, #24
	mov	x9, #0                          ; =0x0
	ldurb	w11, [x23, #-1]
	and	w10, w11, #0x7
	cmp	w10, #1
	b.le	LBB37_42
; %bb.38:
	cmp	w10, #2
	b.eq	LBB37_53
; %bb.39:
	cmp	w10, #3
	b.eq	LBB37_54
; %bb.40:
	cmp	w10, #4
	b.ne	LBB37_56
; %bb.41:
	ldur	x9, [x23, #-17]
	b	LBB37_56
LBB37_42:
	cbz	w10, LBB37_55
; %bb.43:
	cmp	w10, #1
	b.ne	LBB37_56
; %bb.44:
	ldurb	w9, [x23, #-3]
	b	LBB37_56
LBB37_45:
	ldur	x27, [x26, #13]
	cbz	x27, LBB37_75
LBB37_46:
	ldur	x8, [x26, #5]
	stp	x27, x8, [sp, #8]
	ldur	w8, [x26, #1]
	str	w8, [sp, #24]
	str	x27, [sp, #32]
	cbz	x27, LBB37_37
; %bb.47:
	cmp	w8, w20
	b.eq	LBB37_50
; %bb.48:
Lloh213:
	adrp	x0, l_.str@PAGE
Lloh214:
	add	x0, x0, l_.str@PAGEOFF
Lloh215:
	adrp	x2, l_.str.5@PAGE
Lloh216:
	add	x2, x2, l_.str.5@PAGEOFF
	mov	w1, #3669                       ; =0xe55
	bl	_standalone_panic
	ldrb	w8, [x26]
	cmp	w8, #255
	b.eq	LBB37_50
; %bb.49:
Lloh217:
	adrp	x0, l_.str@PAGE
Lloh218:
	add	x0, x0, l_.str@PAGEOFF
Lloh219:
	adrp	x2, l_.str.10@PAGE
Lloh220:
	add	x2, x2, l_.str.10@PAGEOFF
	mov	w1, #581                        ; =0x245
	bl	_standalone_panic
LBB37_50:
	stur	xzr, [x26, #13]
	str	xzr, [sp, #40]
	ldr	w23, [x21, #48]
	ldrb	w8, [x21, #17]
	cmp	w8, #2
	b.hs	LBB37_57
LBB37_51:
	cmp	w8, #1
	b.ne	LBB37_63
; %bb.52:
	mov	x0, x19
	mov	x1, x21
	bl	_zbtScoreRemoveLeaf
	b	LBB37_64
LBB37_53:
	ldurh	w9, [x23, #-5]
	b	LBB37_56
LBB37_54:
	ldur	w9, [x23, #-9]
	b	LBB37_56
LBB37_55:
	lsr	x9, x11, #3
LBB37_56:
	stp	x23, x9, [sp, #8]
	str	w20, [sp, #24]
	stp	xzr, xzr, [x8]
	ldr	w23, [x21, #48]
	ldrb	w8, [x21, #17]
	cmp	w8, #2
	b.lo	LBB37_51
LBB37_57:
	ldrb	w9, [x21, #52]
	madd	w10, w9, w8, w24
	lsr	w10, w10, #3
	add	w10, w10, #9
	and	x10, x10, #0x7ffe
	cmp	x9, #0
	csel	x9, xzr, x10, eq
	ldrb	w10, [x21, #53]
	mvn	w11, w22
	add	w8, w8, w11
	cmp	w10, #0
	csel	w8, w22, w8, eq
	add	x9, x25, x9
	ldrh	w8, [x9, w8, uxtw #1]
	add	x9, x21, x8
	ldrb	w8, [x9]
	cmp	w8, #254
	b.eq	LBB37_60
; %bb.58:
	cmp	w8, #255
	b.ne	LBB37_61
; %bb.59:
	mov	w8, #0                          ; =0x0
	b	LBB37_62
LBB37_60:
	ldurh	w8, [x9, #1]
LBB37_61:
	add	w9, w8, #3
	cmp	x8, #254
	csinc	w8, w9, w8, hs
	mov	w9, #96                         ; =0x60
	mov	w10, #288                       ; =0x120
	madd	w8, w8, w9, w10
	mov	w9, #8195                       ; =0x2003
	movk	w9, #512, lsl #16
	umull	x8, w8, w9
	lsr	x8, x8, #37
LBB37_62:
	cmp	w8, #1
	csinc	w8, w8, wzr, hi
	ldrb	w9, [x21, #21]
	add	w8, w8, w9
	mov	w9, #255                        ; =0xff
	cmp	w8, #255
	csel	w8, w8, w9, lo
	strb	w8, [x21, #21]
LBB37_63:
	mov	x0, x19
	mov	x1, x21
	mov	x2, x22
	mov	w3, #0                          ; =0x0
	bl	_zbtScoreDeleteInPlace
LBB37_64:
	add	x1, sp, #8
	mov	x0, x19
	fmov	d0, d8
	bl	_zbtScoreInsert
	ldr	w3, [x0, #48]
	cmp	w23, w3
	b.eq	LBB37_67
; %bb.65:
	str	wzr, [sp, #4]
	add	x5, sp, #4
	mov	x0, x19
	mov	x1, x20
	mov	x2, x23
	mov	w4, #0                          ; =0x0
	bl	_zbtIndexMove
	cbnz	w0, LBB37_67
; %bb.66:
Lloh221:
	adrp	x0, l_.str@PAGE
Lloh222:
	add	x0, x0, l_.str@PAGEOFF
Lloh223:
	adrp	x2, l_.str.6@PAGE
Lloh224:
	add	x2, x2, l_.str.6@PAGEOFF
	mov	w1, #3684                       ; =0xe64
	bl	_standalone_panic
LBB37_67:
	ldr	w8, [x19, #84]
	cmp	w8, w23
	b.ls	LBB37_101
; %bb.68:
	ldr	x8, [x19, #72]
	ldr	x20, [x8, x23, lsl #3]
	cbz	x20, LBB37_101
; %bb.69:
	tbnz	w20, #0, LBB37_101
; %bb.70:
	ldr	w8, [x20, #48]
	cmp	w8, w23
	b.eq	LBB37_72
; %bb.71:
Lloh225:
	adrp	x0, l_.str@PAGE
Lloh226:
	add	x0, x0, l_.str@PAGEOFF
Lloh227:
	adrp	x2, l_.str.12@PAGE
Lloh228:
	add	x2, x2, l_.str.12@PAGEOFF
	mov	w1, #3119                       ; =0xc2f
	bl	_standalone_panic
LBB37_72:
	ldrb	w8, [x20, #21]
	cmp	w8, #24
	b.lo	LBB37_101
; %bb.73:
	strb	wzr, [x20, #21]
	ldrb	w8, [x20, #17]
	ldrb	w9, [x20, #52]
	cbz	x9, LBB37_77
; %bb.74:
	madd	w9, w9, w8, w24
	lsr	w9, w9, #3
	add	w9, w9, #9
	and	x11, x9, #0x7ffe
	add	x9, x11, #56
	b	LBB37_78
LBB37_75:
Lloh229:
	adrp	x0, l_.str@PAGE
Lloh230:
	add	x0, x0, l_.str@PAGEOFF
Lloh231:
	adrp	x2, l_.str.15@PAGE
Lloh232:
	add	x2, x2, l_.str.15@PAGEOFF
	mov	w1, #599                        ; =0x257
	bl	_standalone_panic
	ldrb	w8, [x26]
	cmp	w8, #255
	b.eq	LBB37_46
; %bb.76:
Lloh233:
	adrp	x0, l_.str@PAGE
Lloh234:
	add	x0, x0, l_.str@PAGEOFF
Lloh235:
	adrp	x2, l_.str.10@PAGE
Lloh236:
	add	x2, x2, l_.str.10@PAGEOFF
	mov	w1, #567                        ; =0x237
	bl	_standalone_panic
	ldrb	w8, [x26]
	cmp	w8, #255
	b	LBB37_37
LBB37_77:
	mov	x11, #0                         ; =0x0
	mov	w9, #56                         ; =0x38
LBB37_78:
	mov	x10, #0                         ; =0x0
	cbz	w8, LBB37_85
; %bb.79:
	add	x11, x20, x11
	add	x11, x11, #56
	mov	x12, x8
	b	LBB37_81
LBB37_80:                               ;   in Loop: Header=BB37_81 Depth=1
	mov	w13, #21                        ; =0x15
	add	x10, x13, x10
	subs	x12, x12, #1
	b.eq	LBB37_85
LBB37_81:                               ; =>This Inner Loop Header: Depth=1
	ldrh	w13, [x11], #2
	add	x14, x20, x13
	ldrb	w13, [x14]
	cmp	w13, #254
	b.eq	LBB37_84
; %bb.82:                               ;   in Loop: Header=BB37_81 Depth=1
	cmp	w13, #255
	b.eq	LBB37_80
; %bb.83:                               ;   in Loop: Header=BB37_81 Depth=1
	cmp	x13, #254
	add	x14, x13, #3
	csinc	x13, x14, x13, hs
	add	x10, x13, x10
	subs	x12, x12, #1
	b.ne	LBB37_81
	b	LBB37_85
LBB37_84:                               ;   in Loop: Header=BB37_81 Depth=1
	ldurh	w13, [x14, #1]
	cmp	x13, #254
	add	x14, x13, #3
	csinc	x13, x14, x13, hs
	add	x10, x13, x10
	subs	x12, x12, #1
	b.ne	LBB37_81
LBB37_85:
	add	x11, x8, x8, lsl #1
	add	x9, x9, x11
	add	x21, x9, x10
	ldr	x1, [x20, #24]
	cmp	x21, #1535
	b.ls	LBB37_93
; %bb.86:
	sub	x9, x21, #56
	udiv	x22, x9, x8
	cbz	x1, LBB37_90
; %bb.87:
	ldrb	w9, [x1, #17]
	add	w8, w9, w8
	cmp	w8, #72
	b.hi	LBB37_90
; %bb.88:
	madd	x8, x22, x9, x21
	cmp	x8, #3071
	b.hi	LBB37_90
; %bb.89:
	mov	x0, x19
	mov	x2, x20
	mov	w3, #72                         ; =0x48
	mov	w4, #3071                       ; =0xbff
	bl	_zbtScoreMergePair
	cbnz	x0, LBB37_101
LBB37_90:
	ldr	x2, [x20, #32]
	cbz	x2, LBB37_99
; %bb.91:
	ldrb	w9, [x20, #17]
	ldrb	w8, [x2, #17]
	add	w9, w8, w9
	cmp	w9, #72
	b.hi	LBB37_99
; %bb.92:
	madd	x8, x22, x8, x21
	cmp	x8, #3071
	b.ls	LBB37_98
	b	LBB37_99
LBB37_93:
	cbz	x1, LBB37_96
; %bb.94:
	ldrb	w9, [x1, #17]
	add	w8, w9, w8
	cmp	w8, #72
	b.hi	LBB37_96
; %bb.95:
	mov	x0, x19
	mov	x2, x20
	mov	w3, #72                         ; =0x48
	mov	w4, #3071                       ; =0xbff
	bl	_zbtScoreMergePair
	cbnz	x0, LBB37_101
LBB37_96:
	ldr	x2, [x20, #32]
	cbz	x2, LBB37_99
; %bb.97:
	ldrb	w8, [x20, #17]
	ldrb	w9, [x2, #17]
	add	w8, w9, w8
	cmp	w8, #72
	b.hi	LBB37_99
LBB37_98:
	mov	x0, x19
	mov	x1, x20
	mov	w3, #72                         ; =0x48
	mov	w4, #3071                       ; =0xbff
	bl	_zbtScoreMergePair
	cbnz	x0, LBB37_101
LBB37_99:
	mov	x0, x20
	bl	_zmalloc_usable_size
	lsl	x8, x21, #1
	add	x8, x8, #128
	cmp	x0, x8
	b.lo	LBB37_101
; %bb.100:
	mov	x0, x19
	mov	x1, x20
	bl	_zbtScoreCompactLeaf
LBB37_101:
	ldp	x29, x30, [sp, #144]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #128]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #112]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #96]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #80]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #64]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp, #48]               ; 16-byte Folded Reload
	add	sp, sp, #160
	ret
Lfunc_end37:
