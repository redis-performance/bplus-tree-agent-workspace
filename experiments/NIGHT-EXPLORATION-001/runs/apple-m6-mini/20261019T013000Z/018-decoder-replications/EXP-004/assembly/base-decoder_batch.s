_decoder_batch:
	sub	sp, sp, #112
	stp	x28, x27, [sp, #16]
	stp	x26, x25, [sp, #32]
	stp	x24, x23, [sp, #48]
	stp	x22, x21, [sp, #64]
	stp	x20, x19, [sp, #80]
	stp	x29, x30, [sp, #96]
	str	w1, [sp, #12]
	cbz	w1, LBB56_55
	mov	x8, #0
	mov	w1, #0
	mov	x9, #0
	mov	x11, #0
	mov	x12, #0
	mov	x13, #-1
	mov	w14, #64
	b	LBB56_3
LBB56_2:
	add	w1, w1, #1
	ldr	w10, [sp, #12]
	cmp	w1, w10
	b.eq	LBB56_54
LBB56_3:
	ldr	w15, [x0, #4]
	cbz	w15, LBB56_2
	mov	x16, #0
	ldr	x17, [x0, #8]
	ldr	w2, [x0]
	and	w3, w2, #0xfffffffc
	b	LBB56_7
LBB56_5:
	and	x4, x19, #0x7fffffffffffffff
	cmp	x19, #0
	csinv	x4, x4, x19, lt
	mvn	w5, w5
	add	w5, w2, w5
	madd	x4, x4, x5, x4
	add	x8, x8, x4
LBB56_6:
	add	x16, x16, #1
	cmp	x16, x15
	b.eq	LBB56_2
LBB56_7:
	ldr	x4, [x17, x16, lsl #3]
	cmp	w2, #4
	b.lo	LBB56_44
	mov	w5, #0
	ldrb	w6, [x4, #52]
	ldrb	w7, [x4, #53]
	add	x19, x4, #56
	lsl	x20, x13, x6
	cmp	w6, #64
	csinv	x20, x13, x20, hs
	ldr	x21, [x4, #40]
	mov	w22, #3
	mov	w23, #-1
	b	LBB56_11
LBB56_9:
	and	x10, x25, x20
	ldrb	w25, [x4, #19]
	lsl	x25, x10, x25
LBB56_10:
	add	x8, x24, x8
	add	x12, x26, x12
	add	x11, x27, x11
	cmp	w7, #0
	cneg	x10, x25, ne
	add	x10, x10, x21
	and	x24, x10, #0x7fffffffffffffff
	cmp	x10, #0
	csinv	x10, x24, x10, lt
	add	x9, x10, x9
	add	w5, w5, #4
	add	w22, w22, #4
	sub	w23, w23, #4
	cmp	w22, w2
	b.hs	LBB56_45
LBB56_11:
	cbz	w6, LBB56_18
	mov	x24, x5
	cbz	w7, LBB56_14
	ldrb	w24, [x4, #17]
	add	w24, w23, w24
LBB56_14:
	umull	x26, w6, w24
	lsr	x25, x26, #3
	ldr	x24, [x19, x25]
	and	x27, x26, #0x7
	lsr	x24, x24, x27
	ands	w26, w26, #0x7
	b.eq	LBB56_17
	sub	w26, w14, w26
	cmp	w26, w6
	b.hs	LBB56_17
	add	x25, x25, x19
	ldrb	w25, [x25, #8]
	lsl	x25, x25, x26
	orr	x24, x25, x24
LBB56_17:
	and	x24, x24, x20
	ldrb	w25, [x4, #19]
	lsl	x24, x24, x25
	b	LBB56_19
LBB56_18:
	mov	x24, #0
LBB56_19:
	sub	w25, w22, #3
	cmp	w7, #0
	cneg	x24, x24, ne
	add	x24, x21, x24
	and	x26, x24, #0x7fffffffffffffff
	cmp	x24, #0
	csinv	x24, x26, x24, lt
	cbz	w6, LBB56_22
	cbz	w7, LBB56_23
	ldrb	w26, [x4, #17]
	eor	w27, w25, #0xfffffffe
	add	w26, w27, w26
	b	LBB56_24
LBB56_22:
	mov	x26, #0
	b	LBB56_28
LBB56_23:
	sub	w26, w22, #2
LBB56_24:
	umull	x28, w6, w26
	lsr	x27, x28, #3
	ldr	x26, [x19, x27]
	and	x30, x28, #0x7
	lsr	x26, x26, x30
	ands	w28, w28, #0x7
	b.eq	LBB56_27
	sub	w28, w14, w28
	cmp	w28, w6
	b.hs	LBB56_27
	add	x27, x27, x19
	ldrb	w27, [x27, #8]
	lsl	x27, x27, x28
	orr	x26, x27, x26
LBB56_27:
	and	x26, x26, x20
	ldrb	w27, [x4, #19]
	lsl	x26, x26, x27
LBB56_28:
	cmp	w7, #0
	cneg	x26, x26, ne
	add	x26, x26, x21
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
	cbz	w6, LBB56_31
	cbz	w7, LBB56_32
	ldrb	w27, [x4, #17]
	eor	w28, w25, #0xfffffffd
	add	w27, w28, w27
	b	LBB56_33
LBB56_31:
	mov	x27, #0
	b	LBB56_37
LBB56_32:
	sub	w27, w22, #1
LBB56_33:
	umull	x30, w6, w27
	lsr	x28, x30, #3
	ldr	x27, [x19, x28]
	and	x10, x30, #0x7
	lsr	x27, x27, x10
	ands	w30, w30, #0x7
	b.eq	LBB56_36
	sub	w30, w14, w30
	cmp	w30, w6
	b.hs	LBB56_36
	add	x10, x28, x19
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x30
	orr	x27, x10, x27
LBB56_36:
	and	x10, x27, x20
	ldrb	w27, [x4, #19]
	lsl	x27, x10, x27
LBB56_37:
	cmp	w7, #0
	cneg	x10, x27, ne
	add	x10, x10, x21
	and	x27, x10, #0x7fffffffffffffff
	cmp	x10, #0
	csinv	x27, x27, x10, lt
	cbz	w6, LBB56_43
	mov	x28, x22
	cbz	w7, LBB56_40
	ldrb	w10, [x4, #17]
	eor	w25, w25, #0xfffffffc
	add	w28, w25, w10
LBB56_40:
	umull	x10, w6, w28
	lsr	x28, x10, #3
	ldr	x25, [x19, x28]
	and	x30, x10, #0x7
	lsr	x25, x25, x30
	ands	w30, w10, #0x7
	b.eq	LBB56_9
	sub	w30, w14, w30
	cmp	w30, w6
	b.hs	LBB56_9
	add	x10, x28, x19
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x30
	orr	x25, x10, x25
	b	LBB56_9
LBB56_43:
	mov	x25, #0
	b	LBB56_10
LBB56_44:
	mov	w5, #0
	subs	w6, w2, w5
	b.ls	LBB56_6
	b	LBB56_46
LBB56_45:
	mov	x5, x3
	subs	w6, w2, w5
	b.ls	LBB56_6
LBB56_46:
	ldrb	w7, [x4, #52]
	lsl	x19, x13, x7
	cmp	w7, #64
	csinv	x20, x13, x19, hs
	ldr	x19, [x4, #40]
	cbz	w7, LBB56_5
	ldrb	w21, [x4, #53]
	add	x22, x4, #56
	ldrb	w23, [x4, #19]
	mvn	w24, w5
	b	LBB56_49
LBB56_48:
	and	x10, x25, x20
	lsl	x10, x10, x23
	cmp	w21, #0
	cneg	x10, x10, ne
	add	x10, x19, x10
	and	x25, x10, #0x7fffffffffffffff
	cmp	x10, #0
	csinv	x10, x25, x10, lt
	add	x8, x10, x8
	add	w5, w5, #1
	sub	w24, w24, #1
	sub	w6, w6, #1
	cbz	w6, LBB56_6
LBB56_49:
	mov	x25, x5
	cbz	w21, LBB56_51
	ldrb	w10, [x4, #17]
	add	w25, w24, w10
LBB56_51:
	umull	x10, w7, w25
	lsr	x26, x10, #3
	ldr	x25, [x22, x26]
	and	x27, x10, #0x7
	lsr	x25, x25, x27
	ands	w27, w10, #0x7
	b.eq	LBB56_48
	sub	w27, w14, w27
	cmp	w27, w7
	b.hs	LBB56_48
	add	x10, x26, x22
	ldrb	w10, [x10, #8]
	lsl	x10, x10, x27
	orr	x25, x10, x25
	b	LBB56_48
LBB56_54:
	add	x10, x11, x12
	add	x8, x9, x8
	add	x0, x10, x8
	b	LBB56_56
LBB56_55:
	mov	x0, #0
LBB56_56:
	ldp	x29, x30, [sp, #96]
	ldp	x20, x19, [sp, #80]
	ldp	x22, x21, [sp, #64]
	ldp	x24, x23, [sp, #48]
	ldp	x26, x25, [sp, #32]
	ldp	x28, x27, [sp, #16]
	add	sp, sp, #112
