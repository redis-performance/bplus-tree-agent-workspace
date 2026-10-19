	.text
	.file	"compile-probe.c"
	.globl	compile_probe                   // -- Begin function compile_probe
	.p2align	2
	.type	compile_probe,@function
compile_probe:                          // @compile_probe
// %bb.0:
	sub	sp, sp, #112
	stp	x28, x27, [sp, #32]             // 16-byte Folded Spill
	lsr	w27, w1, #3
	cmp	w1, #16
	stp	x22, x21, [sp, #80]             // 16-byte Folded Spill
	mov	w22, w3
	sub	w28, w1, #1
	stp	x20, x19, [sp, #96]             // 16-byte Folded Spill
	mov	x19, x4
	mov	x20, x0
	stp	x29, x30, [sp, #16]             // 16-byte Folded Spill
	add	x29, sp, #16
	stp	x26, x25, [sp, #48]             // 16-byte Folded Spill
	stp	x24, x23, [sp, #64]             // 16-byte Folded Spill
	b.lo	.LBB0_10
// %bb.1:
	movi	d1, #0x0000ff000000ff
	mov	w9, #1                          // =0x1
	fmov	s3, w22
	fmov	s2, w9
	dup	v0.16b, w22
	mov	x8, xzr
	mov	w21, wzr
	mov	w11, #15                        // =0xf
	and	v2.8b, v2.8b, v1.8b
	and	v1.8b, v3.8b, v1.8b
	cmeq	v1.2s, v1.2s, v2.2s
	dup	v2.2s, v1.s[0]
	fmov	w10, s1
	mov	w9, v2.s[1]
	cbnz	w2, .LBB0_3
	b	.LBB0_7
.LBB0_2:                                //   in Loop: Header=BB0_3 Depth=1
	add	x13, x8, #3
	add	x12, x8, #2
	cmp	x13, x27
	mov	x8, x12
	b.hs	.LBB0_12
.LBB0_3:                                // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_5 Depth 2
	sturb	w10, [x29, #-2]
	sturb	w9, [x29, #-1]
	ldurh	w13, [x29, #-2]
	and	w14, w13, #0x1
	ubfx	w12, w13, #1, #1
	fmov	s1, w14
	mov	v1.b[1], w12
	ubfx	w12, w13, #2, #1
	mov	v1.b[2], w12
	ubfx	w12, w13, #3, #1
	mov	v1.b[3], w12
	ubfx	w12, w13, #4, #1
	mov	v1.b[4], w12
	ubfx	w12, w13, #5, #1
	mov	v1.b[5], w12
	ubfx	w12, w13, #6, #1
	mov	v1.b[6], w12
	ubfx	w12, w13, #7, #1
	mov	v1.b[7], w12
	ubfx	w12, w13, #8, #1
	mov	v1.b[8], w12
	ubfx	w12, w13, #9, #1
	mov	v1.b[9], w12
	ubfx	w12, w13, #10, #1
	mov	v1.b[10], w12
	ubfx	w12, w13, #11, #1
	mov	v1.b[11], w12
	ubfx	w12, w13, #12, #1
	mov	v1.b[12], w12
	ubfx	w12, w13, #13, #1
	mov	v1.b[13], w12
	ubfx	w12, w13, #14, #1
	lsr	w13, w13, #15
	mov	v1.b[14], w12
	lsl	x12, x8, #3
	ldr	q2, [x20, x12]
	mov	v1.b[15], w13
	cmeq	v3.16b, v2.16b, #0
	cmeq	v2.16b, v2.16b, v0.16b
	and	v1.16b, v1.16b, v3.16b
	orr	v1.16b, v1.16b, v2.16b
	shl	v1.16b, v1.16b, #7
	cmlt	v1.16b, v1.16b, #0
	shrn	v1.8b, v1.8h, #4
	fmov	x13, d1
	cbz	x13, .LBB0_2
// %bb.4:                               //   in Loop: Header=BB0_3 Depth=1
	mov	w14, w21
.LBB0_5:                                //   Parent Loop BB0_3 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	rbit	x15, x13
	add	w21, w14, #1
	clz	x15, x15
	and	x16, x15, #0x3c
	orr	w15, w12, w15, lsr #2
	lsl	x16, x11, x16
	sub	w15, w28, w15
	str	w15, [x19, w14, uxtw #2]
	mov	w14, w21
	bics	x13, x13, x16
	b.ne	.LBB0_5
	b	.LBB0_2
.LBB0_6:                                //   in Loop: Header=BB0_7 Depth=1
	add	x13, x8, #3
	add	x12, x8, #2
	cmp	x13, x27
	mov	x8, x12
	b.hs	.LBB0_11
.LBB0_7:                                // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_9 Depth 2
	sturb	w10, [x29, #-4]
	sturb	w9, [x29, #-3]
	ldurh	w13, [x29, #-4]
	and	w14, w13, #0x1
	ubfx	w12, w13, #1, #1
	fmov	s1, w14
	mov	v1.b[1], w12
	ubfx	w12, w13, #2, #1
	mov	v1.b[2], w12
	ubfx	w12, w13, #3, #1
	mov	v1.b[3], w12
	ubfx	w12, w13, #4, #1
	mov	v1.b[4], w12
	ubfx	w12, w13, #5, #1
	mov	v1.b[5], w12
	ubfx	w12, w13, #6, #1
	mov	v1.b[6], w12
	ubfx	w12, w13, #7, #1
	mov	v1.b[7], w12
	ubfx	w12, w13, #8, #1
	mov	v1.b[8], w12
	ubfx	w12, w13, #9, #1
	mov	v1.b[9], w12
	ubfx	w12, w13, #10, #1
	mov	v1.b[10], w12
	ubfx	w12, w13, #11, #1
	mov	v1.b[11], w12
	ubfx	w12, w13, #12, #1
	mov	v1.b[12], w12
	ubfx	w12, w13, #13, #1
	mov	v1.b[13], w12
	ubfx	w12, w13, #14, #1
	lsr	w13, w13, #15
	mov	v1.b[14], w12
	lsl	x12, x8, #3
	ldr	q2, [x20, x12]
	mov	v1.b[15], w13
	cmeq	v3.16b, v2.16b, #0
	cmeq	v2.16b, v2.16b, v0.16b
	and	v1.16b, v1.16b, v3.16b
	orr	v1.16b, v1.16b, v2.16b
	shl	v1.16b, v1.16b, #7
	cmlt	v1.16b, v1.16b, #0
	shrn	v1.8b, v1.8h, #4
	fmov	x13, d1
	cbz	x13, .LBB0_6
// %bb.8:                               //   in Loop: Header=BB0_7 Depth=1
	mov	w14, w21
.LBB0_9:                                //   Parent Loop BB0_7 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	rbit	x15, x13
	add	w21, w14, #1
	clz	x15, x15
	and	x16, x15, #0x3c
	orr	w15, w12, w15, lsr #2
	lsl	x16, x11, x16
	str	w15, [x19, w14, uxtw #2]
	mov	w14, w21
	bics	x13, x13, x16
	b.ne	.LBB0_9
	b	.LBB0_6
.LBB0_10:
	mov	w12, wzr
	mov	w21, wzr
.LBB0_11:
	cmp	w12, w27
	stp	w2, w1, [sp, #4]                // 8-byte Folded Spill
	b.lo	.LBB0_13
	b	.LBB0_28
.LBB0_12:
                                        // kill: def $w12 killed $w12 killed $x12 def $x12
	cmp	w12, w27
	stp	w2, w1, [sp, #4]                // 8-byte Folded Spill
	b.hs	.LBB0_28
.LBB0_13:
	mov	w24, w12
	cbnz	w2, .LBB0_15
	b	.LBB0_22
.LBB0_14:                               //   in Loop: Header=BB0_15 Depth=1
	add	x24, x24, #1
	cmp	x24, x27
	b.eq	.LBB0_28
.LBB0_15:                               // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_19 Depth 2
	lsl	x23, x24, #3
	and	w25, w22, #0xff
	add	x0, x20, x23
	bl	zbtLeafTagWord
	mov	w1, w22
	mov	x26, x0
	bl	zbtIndexTagMask
	cmp	w25, #1
	mov	x25, x0
	b.ne	.LBB0_17
// %bb.16:                              //   in Loop: Header=BB0_15 Depth=1
	mov	x0, x26
	mov	w1, wzr
	bl	zbtIndexTagMask
	orr	x25, x0, x25
.LBB0_17:                               //   in Loop: Header=BB0_15 Depth=1
	cbnz	x25, .LBB0_19
	b	.LBB0_14
.LBB0_18:                               //   in Loop: Header=BB0_19 Depth=2
	sub	x8, x25, #1
	ands	x25, x8, x25
	b.eq	.LBB0_14
.LBB0_19:                               //   Parent Loop BB0_15 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	mov	x0, x25
	and	w26, w22, #0xff
	bl	zbtIndexFirstTag
	add	w8, w0, w23
	cmp	w26, #1
	ldrb	w9, [x20, w8, uxtw]
	ccmp	w9, #0, #0, eq
	cset	w10, eq
	cmp	w9, w26
	ccmp	w10, #0, #0, ne
	b.eq	.LBB0_18
// %bb.20:                              //   in Loop: Header=BB0_19 Depth=2
	add	w9, w21, #1
	sub	w8, w28, w8
	str	w8, [x19, w21, uxtw #2]
	mov	w21, w9
	b	.LBB0_18
.LBB0_21:                               //   in Loop: Header=BB0_22 Depth=1
	add	x24, x24, #1
	cmp	x24, x27
	b.eq	.LBB0_28
.LBB0_22:                               // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_26 Depth 2
	lsl	x23, x24, #3
	and	w25, w22, #0xff
	add	x0, x20, x23
	bl	zbtLeafTagWord
	mov	w1, w22
	mov	x26, x0
	bl	zbtIndexTagMask
	cmp	w25, #1
	mov	x25, x0
	b.ne	.LBB0_24
// %bb.23:                              //   in Loop: Header=BB0_22 Depth=1
	mov	x0, x26
	mov	w1, wzr
	bl	zbtIndexTagMask
	orr	x25, x0, x25
.LBB0_24:                               //   in Loop: Header=BB0_22 Depth=1
	cbnz	x25, .LBB0_26
	b	.LBB0_21
.LBB0_25:                               //   in Loop: Header=BB0_26 Depth=2
	sub	x8, x25, #1
	ands	x25, x8, x25
	b.eq	.LBB0_21
.LBB0_26:                               //   Parent Loop BB0_22 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	mov	x0, x25
	and	w26, w22, #0xff
	bl	zbtIndexFirstTag
	add	w8, w0, w23
	cmp	w26, #1
	ldrb	w9, [x20, w8, uxtw]
	ccmp	w9, #0, #0, eq
	cset	w10, eq
	cmp	w9, w26
	ccmp	w10, #0, #0, ne
	b.eq	.LBB0_25
// %bb.27:                              //   in Loop: Header=BB0_26 Depth=2
	add	w9, w21, #1
	str	w8, [x19, w21, uxtw #2]
	mov	w21, w9
	b	.LBB0_25
.LBB0_28:
	ldr	w11, [sp, #8]                   // 4-byte Folded Reload
	tst	w11, #0x7
	b.eq	.LBB0_46
// %bb.29:
	and	w9, w22, #0xff
	mov	w8, w11
	cmp	w9, #1
	and	x9, x8, #0xfffffff8
	b.ne	.LBB0_38
// %bb.30:
	ldr	w10, [sp, #4]                   // 4-byte Folded Reload
	cbz	w10, .LBB0_36
// %bb.31:
	mvn	w10, w8
	orr	w10, w10, #0x7
	add	w10, w10, w11
	b	.LBB0_33
.LBB0_32:                               //   in Loop: Header=BB0_33 Depth=1
	add	x9, x9, #1
	sub	w10, w10, #1
	cmp	x9, x8
	b.hs	.LBB0_46
.LBB0_33:                               // =>This Inner Loop Header: Depth=1
	ldrb	w11, [x20, x9]
	cmp	w11, #1
	b.hi	.LBB0_32
// %bb.34:                              //   in Loop: Header=BB0_33 Depth=1
	add	w11, w21, #1
	str	w10, [x19, w21, uxtw #2]
	mov	w21, w11
	b	.LBB0_32
.LBB0_35:                               //   in Loop: Header=BB0_36 Depth=1
	add	x9, x9, #1
	cmp	x9, x8
	b.hs	.LBB0_46
.LBB0_36:                               // =>This Inner Loop Header: Depth=1
	ldrb	w10, [x20, x9]
	cmp	w10, #1
	b.hi	.LBB0_35
// %bb.37:                              //   in Loop: Header=BB0_36 Depth=1
	add	w10, w21, #1
	str	w9, [x19, w21, uxtw #2]
	mov	w21, w10
	b	.LBB0_35
.LBB0_38:
	ldr	w10, [sp, #4]                   // 4-byte Folded Reload
	cbz	w10, .LBB0_44
// %bb.39:
	mvn	w10, w8
	orr	w10, w10, #0x7
	add	w10, w10, w11
	b	.LBB0_41
.LBB0_40:                               //   in Loop: Header=BB0_41 Depth=1
	add	x9, x9, #1
	sub	w10, w10, #1
	cmp	x9, x8
	b.hs	.LBB0_46
.LBB0_41:                               // =>This Inner Loop Header: Depth=1
	ldrb	w11, [x20, x9]
	cmp	w11, w22, uxtb
	b.ne	.LBB0_40
// %bb.42:                              //   in Loop: Header=BB0_41 Depth=1
	add	w11, w21, #1
	str	w10, [x19, w21, uxtw #2]
	mov	w21, w11
	b	.LBB0_40
.LBB0_43:                               //   in Loop: Header=BB0_44 Depth=1
	add	x9, x9, #1
	cmp	x9, x8
	b.hs	.LBB0_46
.LBB0_44:                               // =>This Inner Loop Header: Depth=1
	ldrb	w10, [x20, x9]
	cmp	w10, w22, uxtb
	b.ne	.LBB0_43
// %bb.45:                              //   in Loop: Header=BB0_44 Depth=1
	add	w10, w21, #1
	str	w9, [x19, w21, uxtw #2]
	mov	w21, w10
	b	.LBB0_43
.LBB0_46:
	mov	w0, w21
	ldp	x20, x19, [sp, #96]             // 16-byte Folded Reload
	ldp	x22, x21, [sp, #80]             // 16-byte Folded Reload
	ldp	x24, x23, [sp, #64]             // 16-byte Folded Reload
	ldp	x26, x25, [sp, #48]             // 16-byte Folded Reload
	ldp	x28, x27, [sp, #32]             // 16-byte Folded Reload
	ldp	x29, x30, [sp, #16]             // 16-byte Folded Reload
	add	sp, sp, #112
	ret
.Lfunc_end0:
	.size	compile_probe, .Lfunc_end0-compile_probe
                                        // -- End function
	.ident	"Ubuntu clang version 18.1.3 (1ubuntu1)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
