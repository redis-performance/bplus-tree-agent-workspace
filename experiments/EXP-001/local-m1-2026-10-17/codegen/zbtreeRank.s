; Diagnostic compiler output; debug location directives omitted.
_zbtreeRank:                            ; @zbtreeRank
Lfunc_begin18:
; %bb.0:
	sub	sp, sp, #192
	stp	x28, x27, [sp, #96]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #112]            ; 16-byte Folded Spill
	stp	x24, x23, [sp, #128]            ; 16-byte Folded Spill
	stp	x22, x21, [sp, #144]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #160]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #176]            ; 16-byte Folded Spill
	add	x29, sp, #176
	str	x3, [sp, #64]                   ; 8-byte Folded Spill
	mov	x20, x2
	mov	x21, x1
	mov	x19, x0
	mov	x1, #0                          ; =0x0
	ldurb	w9, [x21, #-1]
	and	w8, w9, #0x7
	cmp	w8, #1
	b.le	LBB18_5
; %bb.1:
	cmp	w8, #2
	b.eq	LBB18_8
; %bb.2:
	cmp	w8, #3
	b.eq	LBB18_9
; %bb.3:
	cmp	w8, #4
	b.ne	LBB18_11
; %bb.4:
	ldur	x1, [x21, #-17]
	b	LBB18_11
LBB18_5:
	cbz	w8, LBB18_10
; %bb.6:
	cmp	w8, #1
	b.ne	LBB18_11
; %bb.7:
	ldurb	w1, [x21, #-3]
	b	LBB18_11
LBB18_8:
	ldurh	w1, [x21, #-5]
	b	LBB18_11
LBB18_9:
	ldur	w1, [x21, #-9]
	b	LBB18_11
LBB18_10:
	lsr	x1, x9, #3
LBB18_11:
	mov	x0, x21
	bl	_dictGenHashFunction
	stp	x0, xzr, [sp, #72]              ; 16-byte Folded Spill
	ldurb	w9, [x21, #-1]
	and	w8, w9, #0x7
	cmp	w8, #1
	str	w20, [sp, #12]                  ; 4-byte Folded Spill
	b.le	LBB18_16
; %bb.12:
	cmp	w8, #2
	b.eq	LBB18_19
; %bb.13:
	cmp	w8, #3
	b.eq	LBB18_20
; %bb.14:
	cmp	w8, #4
	b.ne	LBB18_23
; %bb.15:
	ldur	x8, [x21, #-17]
	b	LBB18_22
LBB18_16:
	cbz	w8, LBB18_21
; %bb.17:
	cmp	w8, #1
	b.ne	LBB18_23
; %bb.18:
	ldurb	w8, [x21, #-3]
	b	LBB18_22
LBB18_19:
	ldurh	w8, [x21, #-5]
	b	LBB18_22
LBB18_20:
	ldur	w8, [x21, #-9]
	b	LBB18_22
LBB18_21:
	lsr	x8, x9, #3
LBB18_22:
	str	x8, [sp, #80]                   ; 8-byte Folded Spill
LBB18_23:
	str	x21, [sp, #56]                  ; 8-byte Folded Spill
	ldr	x8, [x19, #64]
	cbz	x8, LBB18_48
; %bb.24:
	mov	x0, x19
	mov	w1, #1                          ; =0x1
	bl	_zbtIndexRehashStep
	ldr	x20, [x19, #64]
	cbz	x20, LBB18_48
; %bb.25:
	ldr	x8, [x20, #8]
	cbz	x8, LBB18_48
; %bb.26:
	mov	x27, #0                         ; =0x0
	ldr	x11, [sp, #72]                  ; 8-byte Folded Reload
	lsr	w9, w11, #24
	lsr	x10, x11, #24
	cmp	w9, #0
	csinc	w9, w10, wzr, ne
	sub	x8, x8, #1
	mov	w10, w11
	stp	x10, x8, [sp, #32]              ; 16-byte Folded Spill
	and	x28, x8, x10
	and	x8, x9, #0xff
	mov	x10, #72340172838076673         ; =0x101010101010101
	mul	x10, x8, x10
	str	x10, [sp, #48]                  ; 8-byte Folded Spill
	add	x21, x19, #24
	mov	x10, #31765                     ; =0x7c15
	movk	x10, #32586, lsl #16
	movk	x10, #31161, lsl #32
	movk	x10, #40503, lsl #48
	mul	x8, x8, x10
	mov	w10, #1                         ; =0x1
	lsl	x11, x10, x9
	lsr	x12, x8, #58
	lsl	x12, x10, x12
	orr	x11, x12, x11
	lsr	x8, x8, #36
	lsl	x8, x10, x8
	orr	x8, x11, x8
	str	x8, [sp, #24]                   ; 8-byte Folded Spill
	and	w24, w9, #0xff
LBB18_27:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB18_31 Depth 2
	ldr	x8, [x20]
	ldr	w9, [x20, #32]
	cmp	w9, #0
	mov	w9, #48                         ; =0x30
	mov	w10, #32                        ; =0x20
	csel	x9, x10, x9, eq
	madd	x22, x9, x28, x8
	ldr	x8, [x22]
	ldr	x9, [sp, #48]                   ; 8-byte Folded Reload
	eor	x8, x8, x9
	mov	x9, #-72340172838076674         ; =0xfefefefefefefefe
	movk	x9, #65279
	add	x9, x8, x9
	bic	x8, x9, x8
	ands	x26, x8, #0x8080808080808080
	b.eq	LBB18_44
; %bb.28:                               ;   in Loop: Header=BB18_27 Depth=1
	add	x23, x22, #16
	b	LBB18_31
LBB18_29:                               ;   in Loop: Header=BB18_31 Depth=2
Lloh80:
	adrp	x0, l_.str@PAGE
Lloh81:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #1953                       ; =0x7a1
Lloh82:
	adrp	x2, l_.str.14@PAGE
Lloh83:
	add	x2, x2, l_.str.14@PAGEOFF
	bl	_standalone_panic
LBB18_30:                               ;   in Loop: Header=BB18_31 Depth=2
	sub	x8, x26, #1
	ands	x26, x8, x26
	b.eq	LBB18_44
LBB18_31:                               ;   Parent Loop BB18_27 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	rbit	x8, x26
	clz	x8, x8
	ldr	x9, [x22]
	and	x10, x8, #0x38
	lsr	x9, x9, x10
	cmp	w24, w9, uxtb
	b.ne	LBB18_30
; %bb.32:                               ;   in Loop: Header=BB18_31 Depth=2
	lsr	x8, x8, #3
	ldr	w9, [x20, #32]
	cbz	w9, LBB18_34
; %bb.33:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	w8, [x23, x8, lsl #2]
	cmn	w8, #1
	b.ne	LBB18_35
	b	LBB18_30
LBB18_34:                               ;   in Loop: Header=BB18_31 Depth=2
	ldrh	w8, [x23, x8, lsl #1]
	mov	w9, #65535                      ; =0xffff
	cmp	w8, w9
	b.eq	LBB18_30
LBB18_35:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	w9, [x19, #84]
	cmp	w8, w9
	b.hs	LBB18_37
; %bb.36:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	x9, [x19, #72]
	ldr	x25, [x9, w8, uxtw #3]
	and	x9, x25, #0x1
	cmp	x25, #0
	ccmp	x9, #0, #0, ne
	b.eq	LBB18_39
LBB18_37:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	x8, [x19, #64]
	cbz	x8, LBB18_29
; %bb.38:                               ;   in Loop: Header=BB18_31 Depth=2
	cmp	x21, x20
	b.eq	LBB18_30
	b	LBB18_29
LBB18_39:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	w9, [x25, #48]
	cmp	w9, w8
	b.eq	LBB18_41
; %bb.40:                               ;   in Loop: Header=BB18_31 Depth=2
Lloh84:
	adrp	x0, l_.str@PAGE
Lloh85:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #1957                       ; =0x7a5
Lloh86:
	adrp	x2, l_.str.12@PAGE
Lloh87:
	add	x2, x2, l_.str.12@PAGEOFF
	bl	_standalone_panic
LBB18_41:                               ;   in Loop: Header=BB18_31 Depth=2
	ldr	x8, [x19, #64]
	cbz	x8, LBB18_43
; %bb.42:                               ;   in Loop: Header=BB18_31 Depth=2
	cmp	x8, x20
	cset	w9, eq
	ldrh	w10, [x25, #22]
	ldrh	w8, [x8, #44]
	cmp	w10, w8
	cset	w8, ne
	cmp	w9, w8
	b.eq	LBB18_30
LBB18_43:                               ;   in Loop: Header=BB18_31 Depth=2
	sub	x5, x29, #84
	mov	x0, x25
	ldp	x1, x3, [sp, #72]               ; 16-byte Folded Reload
                                        ; kill: def $w1 killed $w1 killed $x1
	ldp	x2, x4, [sp, #56]               ; 16-byte Folded Reload
	bl	_zbtScoreLeafFindMember
	cbz	w0, LBB18_30
	b	LBB18_72
LBB18_44:                               ;   in Loop: Header=BB18_27 Depth=1
	cbnz	x27, LBB18_46
; %bb.45:                               ;   in Loop: Header=BB18_27 Depth=1
	ldr	w8, [x20, #8]
	sub	w8, w8, #1
	ldr	x9, [sp, #32]                   ; 8-byte Folded Reload
	and	x8, x8, x9
	ldr	x9, [x20]
	ldr	w10, [x20, #32]
	cmp	w10, #0
	mov	w10, #48                        ; =0x30
	mov	w11, #32                        ; =0x20
	csel	x10, x11, x10, eq
	umaddl	x8, w10, w8, x9
	ldr	x8, [x8, #8]
	ldr	x9, [sp, #24]                   ; 8-byte Folded Reload
	bics	xzr, x9, x8
	b.ne	LBB18_48
LBB18_46:                               ;   in Loop: Header=BB18_27 Depth=1
	ldr	x8, [x22]
	and	x9, x8, #0xff
	and	x10, x8, #0xff00
	and	x11, x8, #0xff0000
	and	x12, x8, #0xff000000
	and	x13, x8, #0xff00000000
	and	x14, x8, #0xff0000000000
	and	x15, x8, #0xff000000000000
	cmp	x9, #0
	ccmp	x10, #0, #4, ne
	ccmp	x11, #0, #4, ne
	ccmp	x12, #0, #4, ne
	ccmp	x13, #0, #4, ne
	ccmp	x14, #0, #4, ne
	ccmp	x15, #0, #4, ne
	lsr	x8, x8, #56
	ccmp	x8, #0, #4, ne
	b.eq	LBB18_48
; %bb.47:                               ;   in Loop: Header=BB18_27 Depth=1
	add	x8, x28, #1
	ldr	x9, [sp, #40]                   ; 8-byte Folded Reload
	and	x28, x8, x9
	add	x27, x27, #1
	ldr	x8, [x20, #8]
	cmp	x27, x8
	b.lo	LBB18_27
LBB18_48:
	ldr	x8, [x19, #32]
	cbz	x8, LBB18_70
; %bb.49:
	mov	x20, #0                         ; =0x0
	add	x9, x19, #24
	str	x9, [sp, #40]                   ; 8-byte Folded Spill
	ldr	x11, [sp, #72]                  ; 8-byte Folded Reload
	lsr	w9, w11, #24
	lsr	x10, x11, #24
	cmp	w9, #0
	csinc	w9, w10, wzr, ne
	sub	x8, x8, #1
	mov	w10, w11
	stp	x10, x8, [sp, #24]              ; 16-byte Folded Spill
	and	x24, x8, x10
	and	x8, x9, #0xff
	mov	x10, #72340172838076673         ; =0x101010101010101
	mul	x10, x8, x10
	str	x10, [sp, #48]                  ; 8-byte Folded Spill
	mov	x10, #31765                     ; =0x7c15
	movk	x10, #32586, lsl #16
	movk	x10, #31161, lsl #32
	movk	x10, #40503, lsl #48
	mul	x8, x8, x10
	mov	w10, #1                         ; =0x1
	lsl	x11, x10, x9
	lsr	x12, x8, #58
	lsl	x12, x10, x12
	orr	x11, x12, x11
	lsr	x8, x8, #36
	lsl	x8, x10, x8
	orr	x8, x11, x8
	str	x8, [sp, #16]                   ; 8-byte Folded Spill
	and	w22, w9, #0xff
	mov	w27, #65535                     ; =0xffff
Lloh88:
	adrp	x26, l_.str@PAGE
Lloh89:
	add	x26, x26, l_.str@PAGEOFF
LBB18_50:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB18_54 Depth 2
	ldr	x8, [x19, #24]
	ldr	w9, [x19, #56]
	cmp	w9, #0
	mov	w9, #48                         ; =0x30
	mov	w10, #32                        ; =0x20
	csel	x9, x10, x9, eq
	madd	x28, x9, x24, x8
	ldr	x8, [x28]
	ldr	x9, [sp, #48]                   ; 8-byte Folded Reload
	eor	x8, x8, x9
	mov	x9, #-72340172838076674         ; =0xfefefefefefefefe
	movk	x9, #65279
	add	x9, x8, x9
	bic	x8, x9, x8
	ands	x21, x8, #0x8080808080808080
	b.eq	LBB18_66
; %bb.51:                               ;   in Loop: Header=BB18_50 Depth=1
	add	x23, x28, #16
	b	LBB18_54
LBB18_52:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	x8, [x19, #64]
	cbz	x8, LBB18_65
LBB18_53:                               ;   in Loop: Header=BB18_54 Depth=2
	sub	x8, x21, #1
	ands	x21, x8, x21
	b.eq	LBB18_66
LBB18_54:                               ;   Parent Loop BB18_50 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	rbit	x8, x21
	clz	x8, x8
	ldr	x9, [x28]
	and	x10, x8, #0x38
	lsr	x9, x9, x10
	cmp	w22, w9, uxtb
	b.ne	LBB18_53
; %bb.55:                               ;   in Loop: Header=BB18_54 Depth=2
	lsr	x8, x8, #3
	ldr	w9, [x19, #56]
	cbz	w9, LBB18_57
; %bb.56:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	w8, [x23, x8, lsl #2]
	cmn	w8, #1
	b.ne	LBB18_58
	b	LBB18_53
LBB18_57:                               ;   in Loop: Header=BB18_54 Depth=2
	ldrh	w8, [x23, x8, lsl #1]
	cmp	w8, w27
	b.eq	LBB18_53
LBB18_58:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	w9, [x19, #84]
	cmp	w8, w9
	b.hs	LBB18_52
; %bb.59:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	x9, [x19, #72]
	ldr	x25, [x9, w8, uxtw #3]
	and	x9, x25, #0x1
	cmp	x25, #0
	ccmp	x9, #0, #0, ne
	b.ne	LBB18_52
; %bb.60:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	w9, [x25, #48]
	cmp	w9, w8
	b.eq	LBB18_62
; %bb.61:                               ;   in Loop: Header=BB18_54 Depth=2
	mov	x0, x26
	mov	w1, #1957                       ; =0x7a5
Lloh90:
	adrp	x2, l_.str.12@PAGE
Lloh91:
	add	x2, x2, l_.str.12@PAGEOFF
	bl	_standalone_panic
LBB18_62:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	x8, [x19, #64]
	cbz	x8, LBB18_64
; %bb.63:                               ;   in Loop: Header=BB18_54 Depth=2
	ldr	x9, [sp, #40]                   ; 8-byte Folded Reload
	cmp	x8, x9
	cset	w9, eq
	ldrh	w10, [x25, #22]
	ldrh	w8, [x8, #44]
	cmp	w10, w8
	cset	w8, ne
	cmp	w9, w8
	b.eq	LBB18_53
LBB18_64:                               ;   in Loop: Header=BB18_54 Depth=2
	sub	x5, x29, #84
	mov	x0, x25
	ldp	x1, x3, [sp, #72]               ; 16-byte Folded Reload
                                        ; kill: def $w1 killed $w1 killed $x1
	ldp	x2, x4, [sp, #56]               ; 16-byte Folded Reload
	bl	_zbtScoreLeafFindMember
	cbz	w0, LBB18_53
	b	LBB18_72
LBB18_65:                               ;   in Loop: Header=BB18_54 Depth=2
	mov	x0, x26
	mov	w1, #1953                       ; =0x7a1
Lloh92:
	adrp	x2, l_.str.14@PAGE
Lloh93:
	add	x2, x2, l_.str.14@PAGEOFF
	bl	_standalone_panic
	b	LBB18_53
LBB18_66:                               ;   in Loop: Header=BB18_50 Depth=1
	cbnz	x20, LBB18_68
; %bb.67:                               ;   in Loop: Header=BB18_50 Depth=1
	ldr	w8, [x19, #32]
	sub	w8, w8, #1
	ldr	x9, [sp, #24]                   ; 8-byte Folded Reload
	and	x8, x8, x9
	ldr	x9, [x19, #24]
	ldr	w10, [x19, #56]
	cmp	w10, #0
	mov	w10, #48                        ; =0x30
	mov	w11, #32                        ; =0x20
	csel	x10, x11, x10, eq
	umaddl	x8, w10, w8, x9
	ldr	x8, [x8, #8]
	ldr	x9, [sp, #16]                   ; 8-byte Folded Reload
	bics	xzr, x9, x8
	b.ne	LBB18_70
LBB18_68:                               ;   in Loop: Header=BB18_50 Depth=1
	ldr	x8, [x28]
	and	x9, x8, #0xff
	and	x10, x8, #0xff00
	and	x11, x8, #0xff0000
	and	x12, x8, #0xff000000
	and	x13, x8, #0xff00000000
	and	x14, x8, #0xff0000000000
	and	x15, x8, #0xff000000000000
	cmp	x9, #0
	ccmp	x10, #0, #4, ne
	ccmp	x11, #0, #4, ne
	ccmp	x12, #0, #4, ne
	ccmp	x13, #0, #4, ne
	ccmp	x14, #0, #4, ne
	ccmp	x15, #0, #4, ne
	lsr	x8, x8, #56
	ccmp	x8, #0, #4, ne
	b.eq	LBB18_70
; %bb.69:                               ;   in Loop: Header=BB18_50 Depth=1
	add	x8, x24, #1
	ldr	x9, [sp, #32]                   ; 8-byte Folded Reload
	and	x24, x8, x9
	add	x20, x20, #1
	ldr	x8, [x19, #32]
	cmp	x20, x8
	b.lo	LBB18_50
LBB18_70:
	mov	x0, #-1                         ; =0xffffffffffffffff
LBB18_71:
	ldp	x29, x30, [sp, #176]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #160]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #144]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #128]            ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #112]            ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #96]             ; 16-byte Folded Reload
	add	sp, sp, #192
	ret
LBB18_72:
	;DEBUG_LABEL: zbtIndexFind:found
	ldur	w0, [x29, #-84]
	ldr	x9, [x25]
	cbz	x9, LBB18_83
; %bb.73:
	ldr	w12, [sp, #12]                  ; 4-byte Folded Reload
	b	LBB18_75
LBB18_74:                               ;   in Loop: Header=BB18_75 Depth=1
	ldr	x9, [x25]
	cbz	x9, LBB18_84
LBB18_75:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB18_79 Depth 2
                                        ;     Child Loop BB18_82 Depth 2
	ldrb	w8, [x25, #16]
	mov	x25, x9
	cbz	w8, LBB18_74
; %bb.76:                               ;   in Loop: Header=BB18_75 Depth=1
	cmp	w8, #8
	b.hs	LBB18_78
; %bb.77:                               ;   in Loop: Header=BB18_75 Depth=1
	mov	x9, #0                          ; =0x0
	b	LBB18_81
LBB18_78:                               ;   in Loop: Header=BB18_75 Depth=1
	and	x9, x8, #0xf8
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x0
	add	x10, x25, #328
	mov	x11, x9
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
LBB18_79:                               ;   Parent Loop BB18_75 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldp	q4, q5, [x10, #-48]
	ldp	q6, q7, [x10, #-16]
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	add	x10, x10, #64
	subs	x11, x11, #8
	b.ne	LBB18_79
; %bb.80:                               ;   in Loop: Header=BB18_75 Depth=1
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x0, d0
	cmp	x9, x8
	b.eq	LBB18_74
LBB18_81:                               ;   in Loop: Header=BB18_75 Depth=1
	sub	x8, x8, x9
	add	x9, x25, x9, lsl #3
	add	x9, x9, #280
LBB18_82:                               ;   Parent Loop BB18_75 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	x10, [x9], #8
	add	x0, x10, x0
	subs	x8, x8, #1
	b.ne	LBB18_82
	b	LBB18_74
LBB18_83:
	ldr	w12, [sp, #12]                  ; 4-byte Folded Reload
LBB18_84:
	cbz	w12, LBB18_71
; %bb.85:
	ldr	x8, [x19, #96]
	mvn	x9, x0
	add	x0, x8, x9
	b	LBB18_71
Lfunc_end18:
