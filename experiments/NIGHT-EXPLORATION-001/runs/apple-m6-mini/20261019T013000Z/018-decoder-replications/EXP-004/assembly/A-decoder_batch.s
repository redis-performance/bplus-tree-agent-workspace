_decoder_batch:
	cbz	w1, LBB56_50
	stp	x28, x27, [sp, #-96]!
	stp	x26, x25, [sp, #16]
	stp	x24, x23, [sp, #32]
	stp	x22, x21, [sp, #48]
	stp	x20, x19, [sp, #64]
	stp	x29, x30, [sp, #80]
	mov	x8, #0
	mov	w10, #0
	mov	x9, #0
	mov	x11, #0
	mov	x12, #0
	mov	x13, #-1
	b	LBB56_3
LBB56_2:
	add	w10, w10, #1
	cmp	w10, w1
	b.eq	LBB56_49
LBB56_3:
	ldr	w14, [x0, #4]
	cbz	w14, LBB56_2
	mov	x15, #0
	ldr	x16, [x0, #8]
	ldr	w17, [x0]
	and	w2, w17, #0xfffffffc
	b	LBB56_7
LBB56_5:
	and	x3, x7, #0x7fffffffffffffff
	cmp	x7, #0
	csinv	x3, x3, x7, lt
	mvn	w4, w4
	add	w4, w17, w4
	madd	x3, x3, x4, x3
	add	x8, x8, x3
LBB56_6:
	add	x15, x15, #1
	cmp	x15, x14
	b.eq	LBB56_2
LBB56_7:
	ldr	x3, [x16, x15, lsl #3]
	cmp	w17, #4
	b.lo	LBB56_40
	mov	w4, #0
	ldrb	w5, [x3, #52]
	add	x6, x3, #56
	lsl	x7, x13, x5
	cmp	w5, #64
	csinv	x7, x13, x7, hs
	ldr	x19, [x3, #40]
	ldrb	w20, [x3, #53]
	mov	w21, #3
	mov	w22, #-1
	b	LBB56_11
LBB56_9:
	and	x24, x24, x7
	ldrb	w27, [x3, #19]
	lsl	x24, x24, x27
LBB56_10:
	add	x8, x23, x8
	add	x12, x25, x12
	add	x11, x26, x11
	cmp	w20, #0
	cneg	x23, x24, ne
	add	x23, x23, x19
	and	x24, x23, #0x7fffffffffffffff
	cmp	x23, #0
	csinv	x23, x24, x23, lt
	add	x9, x23, x9
	add	w4, w4, #4
	add	w21, w21, #4
	sub	w22, w22, #4
	cmp	w21, w17
	b.hs	LBB56_41
LBB56_11:
	cbz	w5, LBB56_17
	mov	x23, x4
	cbz	w20, LBB56_14
	ldrb	w23, [x3, #17]
	add	w23, w22, w23
LBB56_14:
	umull	x23, w5, w23
	lsr	x25, x23, #3
	and	w24, w23, #0x7
	ldr	x26, [x6, x25]
	and	x23, x23, #0x7
	lsr	x23, x26, x23
	add	w26, w24, w5
	cmp	w26, #65
	b.lo	LBB56_16
	add	x25, x25, x6
	ldrb	w25, [x25, #8]
	neg	w24, w24
	lsl	x24, x25, x24
	orr	x23, x24, x23
LBB56_16:
	and	x23, x23, x7
	ldrb	w24, [x3, #19]
	lsl	x23, x23, x24
	b	LBB56_18
LBB56_17:
	mov	x23, #0
LBB56_18:
	sub	w24, w21, #3
	cmp	w20, #0
	cneg	x23, x23, ne
	add	x23, x19, x23
	and	x25, x23, #0x7fffffffffffffff
	cmp	x23, #0
	csinv	x23, x25, x23, lt
	cbz	w5, LBB56_21
	cbz	w20, LBB56_22
	ldrb	w25, [x3, #17]
	eor	w26, w24, #0xfffffffe
	add	w25, w26, w25
	b	LBB56_23
LBB56_21:
	mov	x25, #0
	b	LBB56_26
LBB56_22:
	sub	w25, w21, #2
LBB56_23:
	umull	x25, w5, w25
	lsr	x27, x25, #3
	and	w26, w25, #0x7
	ldr	x28, [x6, x27]
	and	x25, x25, #0x7
	lsr	x25, x28, x25
	add	w28, w26, w5
	cmp	w28, #65
	b.lo	LBB56_25
	add	x27, x27, x6
	ldrb	w27, [x27, #8]
	neg	w26, w26
	lsl	x26, x27, x26
	orr	x25, x26, x25
LBB56_25:
	and	x25, x25, x7
	ldrb	w26, [x3, #19]
	lsl	x25, x25, x26
LBB56_26:
	cmp	w20, #0
	cneg	x25, x25, ne
	add	x25, x25, x19
	and	x26, x25, #0x7fffffffffffffff
	cmp	x25, #0
	csinv	x25, x26, x25, lt
	cbz	w5, LBB56_29
	cbz	w20, LBB56_30
	ldrb	w26, [x3, #17]
	eor	w27, w24, #0xfffffffd
	add	w26, w27, w26
	b	LBB56_31
LBB56_29:
	mov	x26, #0
	b	LBB56_34
LBB56_30:
	sub	w26, w21, #1
LBB56_31:
	umull	x26, w5, w26
	lsr	x28, x26, #3
	and	w27, w26, #0x7
	ldr	x30, [x6, x28]
	and	x26, x26, #0x7
	lsr	x26, x30, x26
	add	w30, w27, w5
	cmp	w30, #65
	b.lo	LBB56_33
	add	x28, x28, x6
	ldrb	w28, [x28, #8]
	neg	w27, w27
	lsl	x27, x28, x27
	orr	x26, x27, x26
LBB56_33:
	and	x26, x26, x7
	ldrb	w27, [x3, #19]
	lsl	x26, x26, x27
LBB56_34:
	cmp	w20, #0
	cneg	x26, x26, ne
	add	x26, x26, x19
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
	cbz	w5, LBB56_39
	mov	x27, x21
	cbz	w20, LBB56_37
	ldrb	w27, [x3, #17]
	eor	w24, w24, #0xfffffffc
	add	w27, w24, w27
LBB56_37:
	umull	x24, w5, w27
	lsr	x28, x24, #3
	and	w27, w24, #0x7
	ldr	x30, [x6, x28]
	and	x24, x24, #0x7
	lsr	x24, x30, x24
	add	w30, w27, w5
	cmp	w30, #65
	b.lo	LBB56_9
	add	x28, x28, x6
	ldrb	w28, [x28, #8]
	neg	w27, w27
	lsl	x27, x28, x27
	orr	x24, x27, x24
	b	LBB56_9
LBB56_39:
	mov	x24, #0
	b	LBB56_10
LBB56_40:
	mov	w4, #0
	subs	w5, w17, w4
	b.ls	LBB56_6
	b	LBB56_42
LBB56_41:
	mov	x4, x2
	subs	w5, w17, w4
	b.ls	LBB56_6
LBB56_42:
	ldrb	w6, [x3, #52]
	lsl	x7, x13, x6
	cmp	w6, #64
	csinv	x19, x13, x7, hs
	ldr	x7, [x3, #40]
	cbz	w6, LBB56_5
	add	x20, x3, #56
	ldrb	w21, [x3, #53]
	ldrb	w22, [x3, #19]
	mvn	w23, w4
	b	LBB56_45
LBB56_44:
	and	x24, x24, x19
	lsl	x24, x24, x22
	cmp	w21, #0
	cneg	x24, x24, ne
	add	x24, x7, x24
	and	x25, x24, #0x7fffffffffffffff
	cmp	x24, #0
	csinv	x24, x25, x24, lt
	add	x8, x24, x8
	add	w4, w4, #1
	sub	w23, w23, #1
	sub	w5, w5, #1
	cbz	w5, LBB56_6
LBB56_45:
	mov	x24, x4
	cbz	w21, LBB56_47
	ldrb	w24, [x3, #17]
	add	w24, w23, w24
LBB56_47:
	umull	x24, w6, w24
	lsr	x26, x24, #3
	and	w25, w24, #0x7
	ldr	x27, [x20, x26]
	and	x24, x24, #0x7
	lsr	x24, x27, x24
	add	w27, w25, w6
	cmp	w27, #65
	b.lo	LBB56_44
	add	x26, x26, x20
	ldrb	w26, [x26, #8]
	neg	w25, w25
	lsl	x25, x26, x25
	orr	x24, x25, x24
	b	LBB56_44
LBB56_49:
	add	x10, x11, x12
	add	x8, x9, x8
	add	x0, x10, x8
	ldp	x29, x30, [sp, #80]
	ldp	x20, x19, [sp, #64]
	ldp	x22, x21, [sp, #48]
	ldp	x24, x23, [sp, #32]
	ldp	x26, x25, [sp, #16]
	ldp	x28, x27, [sp], #96
LBB56_50:
	mov	x0, #0
