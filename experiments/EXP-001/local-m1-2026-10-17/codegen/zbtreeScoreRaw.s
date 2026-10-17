; Diagnostic compiler output; debug location directives omitted.
_zbtreeScoreRaw:                        ; @zbtreeScoreRaw
Lfunc_begin14:
; %bb.0:
	sub	sp, sp, #176
	stp	x28, x27, [sp, #80]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #96]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #112]            ; 16-byte Folded Spill
	stp	x22, x21, [sp, #128]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #144]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #160]            ; 16-byte Folded Spill
	add	x29, sp, #160
	stp	x2, x3, [sp, #56]               ; 16-byte Folded Spill
	mov	x22, x0
	str	x1, [sp, #48]                   ; 8-byte Folded Spill
	mov	x0, x1
	mov	x1, x2
	bl	_dictGenHashFunction
	str	x0, [sp, #72]                   ; 8-byte Folded Spill
	ldr	x8, [x22, #64]
	cbz	x8, LBB14_25
; %bb.1:
	mov	x0, x22
	mov	w1, #1                          ; =0x1
	bl	_zbtIndexRehashStep
	ldr	x28, [x22, #64]
	cbz	x28, LBB14_25
; %bb.2:
	ldr	x8, [x28, #8]
	cbz	x8, LBB14_25
; %bb.3:
	mov	x25, #0                         ; =0x0
	ldr	x11, [sp, #72]                  ; 8-byte Folded Reload
	lsr	w9, w11, #24
	lsr	x10, x11, #24
	cmp	w9, #0
	csinc	w9, w10, wzr, ne
	sub	x8, x8, #1
	mov	w10, w11
	stp	x10, x8, [sp, #24]              ; 16-byte Folded Spill
	and	x26, x8, x10
	and	x8, x9, #0xff
	mov	x10, #72340172838076673         ; =0x101010101010101
	mul	x10, x8, x10
	str	x10, [sp, #40]                  ; 8-byte Folded Spill
	add	x19, x22, #24
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
	and	w21, w9, #0xff
LBB14_4:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB14_8 Depth 2
	ldr	x8, [x28]
	ldr	w9, [x28, #32]
	cmp	w9, #0
	mov	w9, #48                         ; =0x30
	mov	w10, #32                        ; =0x20
	csel	x9, x10, x9, eq
	madd	x23, x9, x26, x8
	ldr	x8, [x23]
	ldr	x9, [sp, #40]                   ; 8-byte Folded Reload
	eor	x8, x8, x9
	mov	x9, #-72340172838076674         ; =0xfefefefefefefefe
	movk	x9, #65279
	add	x9, x8, x9
	bic	x8, x9, x8
	ands	x24, x8, #0x8080808080808080
	b.eq	LBB14_21
; %bb.5:                                ;   in Loop: Header=BB14_4 Depth=1
	add	x20, x23, #16
	b	LBB14_8
LBB14_6:                                ;   in Loop: Header=BB14_8 Depth=2
Lloh24:
	adrp	x0, l_.str@PAGE
Lloh25:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #1953                       ; =0x7a1
Lloh26:
	adrp	x2, l_.str.14@PAGE
Lloh27:
	add	x2, x2, l_.str.14@PAGEOFF
	bl	_standalone_panic
LBB14_7:                                ;   in Loop: Header=BB14_8 Depth=2
	sub	x8, x24, #1
	ands	x24, x8, x24
	b.eq	LBB14_21
LBB14_8:                                ;   Parent Loop BB14_4 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	rbit	x8, x24
	clz	x8, x8
	ldr	x9, [x23]
	and	x10, x8, #0x38
	lsr	x9, x9, x10
	cmp	w21, w9, uxtb
	b.ne	LBB14_7
; %bb.9:                                ;   in Loop: Header=BB14_8 Depth=2
	lsr	x8, x8, #3
	ldr	w9, [x28, #32]
	cbz	w9, LBB14_11
; %bb.10:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	w8, [x20, x8, lsl #2]
	cmn	w8, #1
	b.ne	LBB14_12
	b	LBB14_7
LBB14_11:                               ;   in Loop: Header=BB14_8 Depth=2
	ldrh	w8, [x20, x8, lsl #1]
	mov	w9, #65535                      ; =0xffff
	cmp	w8, w9
	b.eq	LBB14_7
LBB14_12:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	w9, [x22, #84]
	cmp	w8, w9
	b.hs	LBB14_14
; %bb.13:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	x9, [x22, #72]
	ldr	x27, [x9, w8, uxtw #3]
	and	x9, x27, #0x1
	cmp	x27, #0
	ccmp	x9, #0, #0, ne
	b.eq	LBB14_16
LBB14_14:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	x8, [x22, #64]
	cbz	x8, LBB14_6
; %bb.15:                               ;   in Loop: Header=BB14_8 Depth=2
	cmp	x19, x28
	b.eq	LBB14_7
	b	LBB14_6
LBB14_16:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	w9, [x27, #48]
	cmp	w9, w8
	b.eq	LBB14_18
; %bb.17:                               ;   in Loop: Header=BB14_8 Depth=2
Lloh28:
	adrp	x0, l_.str@PAGE
Lloh29:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #1957                       ; =0x7a5
Lloh30:
	adrp	x2, l_.str.12@PAGE
Lloh31:
	add	x2, x2, l_.str.12@PAGEOFF
	bl	_standalone_panic
LBB14_18:                               ;   in Loop: Header=BB14_8 Depth=2
	ldr	x8, [x22, #64]
	cbz	x8, LBB14_20
; %bb.19:                               ;   in Loop: Header=BB14_8 Depth=2
	cmp	x8, x28
	cset	w9, eq
	ldrh	w10, [x27, #22]
	ldrh	w8, [x8, #44]
	cmp	w10, w8
	cset	w8, ne
	cmp	w9, w8
	b.eq	LBB14_7
LBB14_20:                               ;   in Loop: Header=BB14_8 Depth=2
	mov	x0, x27
	ldp	x4, x1, [sp, #64]               ; 16-byte Folded Reload
                                        ; kill: def $w1 killed $w1 killed $x1
	ldp	x2, x3, [sp, #48]               ; 16-byte Folded Reload
	mov	x5, #0                          ; =0x0
	bl	_zbtScoreLeafFindMember
	cbz	w0, LBB14_7
	b	LBB14_48
LBB14_21:                               ;   in Loop: Header=BB14_4 Depth=1
	cbnz	x25, LBB14_23
; %bb.22:                               ;   in Loop: Header=BB14_4 Depth=1
	ldr	w8, [x28, #8]
	sub	w8, w8, #1
	ldr	x9, [sp, #24]                   ; 8-byte Folded Reload
	and	x8, x8, x9
	ldr	x9, [x28]
	ldr	w10, [x28, #32]
	cmp	w10, #0
	mov	w10, #48                        ; =0x30
	mov	w11, #32                        ; =0x20
	csel	x10, x11, x10, eq
	umaddl	x8, w10, w8, x9
	ldr	x8, [x8, #8]
	ldr	x9, [sp, #16]                   ; 8-byte Folded Reload
	bics	xzr, x9, x8
	b.ne	LBB14_25
LBB14_23:                               ;   in Loop: Header=BB14_4 Depth=1
	ldr	x8, [x23]
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
	b.eq	LBB14_25
; %bb.24:                               ;   in Loop: Header=BB14_4 Depth=1
	add	x8, x26, #1
	ldr	x9, [sp, #32]                   ; 8-byte Folded Reload
	and	x26, x8, x9
	add	x25, x25, #1
	ldr	x8, [x28, #8]
	cmp	x25, x8
	b.lo	LBB14_4
LBB14_25:
	ldr	x8, [x22, #32]
	cbz	x8, LBB14_47
; %bb.26:
	mov	x28, #0                         ; =0x0
	add	x9, x22, #24
	str	x9, [sp, #32]                   ; 8-byte Folded Spill
	ldr	x11, [sp, #72]                  ; 8-byte Folded Reload
	lsr	w9, w11, #24
	lsr	x10, x11, #24
	cmp	w9, #0
	csinc	w9, w10, wzr, ne
	sub	x8, x8, #1
	mov	w10, w11
	stp	x10, x8, [sp, #16]              ; 16-byte Folded Spill
	and	x20, x8, x10
	and	x8, x9, #0xff
	mov	x10, #72340172838076673         ; =0x101010101010101
	mul	x10, x8, x10
	str	x10, [sp, #40]                  ; 8-byte Folded Spill
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
	str	x8, [sp, #8]                    ; 8-byte Folded Spill
	and	w23, w9, #0xff
	mov	w25, #65535                     ; =0xffff
Lloh32:
	adrp	x24, l_.str@PAGE
Lloh33:
	add	x24, x24, l_.str@PAGEOFF
LBB14_27:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB14_31 Depth 2
	ldr	x8, [x22, #24]
	ldr	w9, [x22, #56]
	cmp	w9, #0
	mov	w9, #48                         ; =0x30
	mov	w10, #32                        ; =0x20
	csel	x9, x10, x9, eq
	madd	x26, x9, x20, x8
	ldr	x8, [x26]
	ldr	x9, [sp, #40]                   ; 8-byte Folded Reload
	eor	x8, x8, x9
	mov	x9, #-72340172838076674         ; =0xfefefefefefefefe
	movk	x9, #65279
	add	x9, x8, x9
	bic	x8, x9, x8
	ands	x19, x8, #0x8080808080808080
	b.eq	LBB14_43
; %bb.28:                               ;   in Loop: Header=BB14_27 Depth=1
	add	x21, x26, #16
	b	LBB14_31
LBB14_29:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	x8, [x22, #64]
	cbz	x8, LBB14_42
LBB14_30:                               ;   in Loop: Header=BB14_31 Depth=2
	sub	x8, x19, #1
	ands	x19, x8, x19
	b.eq	LBB14_43
LBB14_31:                               ;   Parent Loop BB14_27 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	rbit	x8, x19
	clz	x8, x8
	ldr	x9, [x26]
	and	x10, x8, #0x38
	lsr	x9, x9, x10
	cmp	w23, w9, uxtb
	b.ne	LBB14_30
; %bb.32:                               ;   in Loop: Header=BB14_31 Depth=2
	lsr	x8, x8, #3
	ldr	w9, [x22, #56]
	cbz	w9, LBB14_34
; %bb.33:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	w8, [x21, x8, lsl #2]
	cmn	w8, #1
	b.ne	LBB14_35
	b	LBB14_30
LBB14_34:                               ;   in Loop: Header=BB14_31 Depth=2
	ldrh	w8, [x21, x8, lsl #1]
	cmp	w8, w25
	b.eq	LBB14_30
LBB14_35:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	w9, [x22, #84]
	cmp	w8, w9
	b.hs	LBB14_29
; %bb.36:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	x9, [x22, #72]
	ldr	x27, [x9, w8, uxtw #3]
	and	x9, x27, #0x1
	cmp	x27, #0
	ccmp	x9, #0, #0, ne
	b.ne	LBB14_29
; %bb.37:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	w9, [x27, #48]
	cmp	w9, w8
	b.eq	LBB14_39
; %bb.38:                               ;   in Loop: Header=BB14_31 Depth=2
	mov	x0, x24
	mov	w1, #1957                       ; =0x7a5
Lloh34:
	adrp	x2, l_.str.12@PAGE
Lloh35:
	add	x2, x2, l_.str.12@PAGEOFF
	bl	_standalone_panic
LBB14_39:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	x8, [x22, #64]
	cbz	x8, LBB14_41
; %bb.40:                               ;   in Loop: Header=BB14_31 Depth=2
	ldr	x9, [sp, #32]                   ; 8-byte Folded Reload
	cmp	x8, x9
	cset	w9, eq
	ldrh	w10, [x27, #22]
	ldrh	w8, [x8, #44]
	cmp	w10, w8
	cset	w8, ne
	cmp	w9, w8
	b.eq	LBB14_30
LBB14_41:                               ;   in Loop: Header=BB14_31 Depth=2
	mov	x0, x27
	ldp	x4, x1, [sp, #64]               ; 16-byte Folded Reload
                                        ; kill: def $w1 killed $w1 killed $x1
	ldp	x2, x3, [sp, #48]               ; 16-byte Folded Reload
	mov	x5, #0                          ; =0x0
	bl	_zbtScoreLeafFindMember
	cbz	w0, LBB14_30
	b	LBB14_48
LBB14_42:                               ;   in Loop: Header=BB14_31 Depth=2
	mov	x0, x24
	mov	w1, #1953                       ; =0x7a1
Lloh36:
	adrp	x2, l_.str.14@PAGE
Lloh37:
	add	x2, x2, l_.str.14@PAGEOFF
	bl	_standalone_panic
	b	LBB14_30
LBB14_43:                               ;   in Loop: Header=BB14_27 Depth=1
	cbnz	x28, LBB14_45
; %bb.44:                               ;   in Loop: Header=BB14_27 Depth=1
	ldr	w8, [x22, #32]
	sub	w8, w8, #1
	ldr	x9, [sp, #16]                   ; 8-byte Folded Reload
	and	x8, x8, x9
	ldr	x9, [x22, #24]
	ldr	w10, [x22, #56]
	cmp	w10, #0
	mov	w10, #48                        ; =0x30
	mov	w11, #32                        ; =0x20
	csel	x10, x11, x10, eq
	umaddl	x8, w10, w8, x9
	ldr	x8, [x8, #8]
	ldr	x9, [sp, #8]                    ; 8-byte Folded Reload
	bics	xzr, x9, x8
	b.ne	LBB14_47
LBB14_45:                               ;   in Loop: Header=BB14_27 Depth=1
	ldr	x8, [x26]
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
	b.eq	LBB14_47
; %bb.46:                               ;   in Loop: Header=BB14_27 Depth=1
	add	x8, x20, #1
	ldr	x9, [sp, #24]                   ; 8-byte Folded Reload
	and	x20, x8, x9
	add	x28, x28, #1
	ldr	x8, [x22, #32]
	cmp	x28, x8
	b.lo	LBB14_27
LBB14_47:
	mov	w0, #0                          ; =0x0
	b	LBB14_49
LBB14_48:
	mov	w0, #1                          ; =0x1
LBB14_49:
	ldp	x29, x30, [sp, #160]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #144]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #128]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #112]            ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #96]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #80]             ; 16-byte Folded Reload
	add	sp, sp, #176
	ret
Lfunc_end14:
