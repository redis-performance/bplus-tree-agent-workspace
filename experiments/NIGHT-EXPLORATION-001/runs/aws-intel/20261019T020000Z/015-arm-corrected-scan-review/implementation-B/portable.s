	.text
	.file	"compile-probe.c"
	.globl	compile_probe                   // -- Begin function compile_probe
	.p2align	2
	.type	compile_probe,@function
compile_probe:                          // @compile_probe
// %bb.0:
	sub	sp, sp, #112
	stp	x29, x30, [sp, #16]             // 16-byte Folded Spill
	add	x29, sp, #16
	cmp	w1, #8
	stp	x22, x21, [sp, #80]             // 16-byte Folded Spill
	mov	w22, w3
	stp	x20, x19, [sp, #96]             // 16-byte Folded Spill
	mov	x19, x4
	mov	x20, x0
	stp	x28, x27, [sp, #32]             // 16-byte Folded Spill
	stp	x26, x25, [sp, #48]             // 16-byte Folded Spill
	stp	x24, x23, [sp, #64]             // 16-byte Folded Spill
	stur	w1, [x29, #-4]                  // 4-byte Folded Spill
	str	w2, [sp, #8]                    // 4-byte Folded Spill
	b.hs	.LBB0_12
// %bb.1:
	mov	w21, wzr
.LBB0_2:
	ldur	w11, [x29, #-4]                 // 4-byte Folded Reload
	tst	w11, #0x7
	b.eq	.LBB0_33
// %bb.3:
	and	w9, w22, #0xff
	mov	w8, w11
	cmp	w9, #1
	and	x9, x8, #0xfffffff8
	b.ne	.LBB0_25
// %bb.4:
	ldr	w10, [sp, #8]                   // 4-byte Folded Reload
	cbz	w10, .LBB0_10
// %bb.5:
	mvn	w10, w8
	orr	w10, w10, #0x7
	add	w10, w10, w11
	b	.LBB0_7
.LBB0_6:                                //   in Loop: Header=BB0_7 Depth=1
	add	x9, x9, #1
	sub	w10, w10, #1
	cmp	x9, x8
	b.hs	.LBB0_33
.LBB0_7:                                // =>This Inner Loop Header: Depth=1
	ldrb	w11, [x20, x9]
	cmp	w11, #1
	b.hi	.LBB0_6
// %bb.8:                               //   in Loop: Header=BB0_7 Depth=1
	add	w11, w21, #1
	str	w10, [x19, w21, uxtw #2]
	mov	w21, w11
	b	.LBB0_6
.LBB0_9:                                //   in Loop: Header=BB0_10 Depth=1
	add	x9, x9, #1
	cmp	x9, x8
	b.hs	.LBB0_33
.LBB0_10:                               // =>This Inner Loop Header: Depth=1
	ldrb	w10, [x20, x9]
	cmp	w10, #1
	b.hi	.LBB0_9
// %bb.11:                              //   in Loop: Header=BB0_10 Depth=1
	add	w10, w21, #1
	str	w9, [x19, w21, uxtw #2]
	mov	w21, w10
	b	.LBB0_9
.LBB0_12:
	lsr	w27, w1, #3
	cbz	w2, .LBB0_34
// %bb.13:
	and	w8, w22, #0xff
	sub	w28, w1, #1
	mov	x24, xzr
	cmp	w8, #1
	mov	w21, wzr
	b.eq	.LBB0_15
	b	.LBB0_20
.LBB0_14:                               //   in Loop: Header=BB0_15 Depth=1
	add	x24, x24, #1
	cmp	x24, x27
	b.eq	.LBB0_2
.LBB0_15:                               // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_17 Depth 2
	lsl	x23, x24, #3
	add	x0, x20, x23
	bl	zbtLeafTagWord
	mov	w1, #1                          // =0x1
	mov	x25, x0
	bl	zbtIndexTagMask
	mov	x26, x0
	mov	x0, x25
	mov	w1, wzr
	bl	zbtIndexTagMask
	orr	x25, x0, x26
	cbnz	x25, .LBB0_17
	b	.LBB0_14
.LBB0_16:                               //   in Loop: Header=BB0_17 Depth=2
	sub	x8, x25, #1
	ands	x25, x8, x25
	b.eq	.LBB0_14
.LBB0_17:                               //   Parent Loop BB0_15 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	mov	x0, x25
	bl	zbtIndexFirstTag
	add	w8, w0, w23
	ldrb	w9, [x20, w8, uxtw]
	cmp	w9, #1
	b.hi	.LBB0_16
// %bb.18:                              //   in Loop: Header=BB0_17 Depth=2
	add	w9, w21, #1
	sub	w8, w28, w8
	str	w8, [x19, w21, uxtw #2]
	mov	w21, w9
	b	.LBB0_16
.LBB0_19:                               //   in Loop: Header=BB0_20 Depth=1
	add	x24, x24, #1
	cmp	x24, x27
	b.eq	.LBB0_2
.LBB0_20:                               // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_23 Depth 2
	lsl	x23, x24, #3
	add	x0, x20, x23
	bl	zbtLeafTagWord
	mov	w1, w22
	bl	zbtIndexTagMask
	cbz	x0, .LBB0_19
// %bb.21:                              //   in Loop: Header=BB0_20 Depth=1
	mov	x25, x0
	b	.LBB0_23
.LBB0_22:                               //   in Loop: Header=BB0_23 Depth=2
	sub	x8, x25, #1
	ands	x25, x8, x25
	b.eq	.LBB0_19
.LBB0_23:                               //   Parent Loop BB0_20 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	mov	x0, x25
	bl	zbtIndexFirstTag
	add	w8, w0, w23
	ldrb	w9, [x20, w8, uxtw]
	cmp	w9, w22, uxtb
	b.ne	.LBB0_22
// %bb.24:                              //   in Loop: Header=BB0_23 Depth=2
	add	w9, w21, #1
	sub	w8, w28, w8
	str	w8, [x19, w21, uxtw #2]
	mov	w21, w9
	b	.LBB0_22
.LBB0_25:
	ldr	w10, [sp, #8]                   // 4-byte Folded Reload
	cbz	w10, .LBB0_31
// %bb.26:
	mvn	w10, w8
	orr	w10, w10, #0x7
	add	w10, w10, w11
	b	.LBB0_28
.LBB0_27:                               //   in Loop: Header=BB0_28 Depth=1
	add	x9, x9, #1
	sub	w10, w10, #1
	cmp	x9, x8
	b.hs	.LBB0_33
.LBB0_28:                               // =>This Inner Loop Header: Depth=1
	ldrb	w11, [x20, x9]
	cmp	w11, w22, uxtb
	b.ne	.LBB0_27
// %bb.29:                              //   in Loop: Header=BB0_28 Depth=1
	add	w11, w21, #1
	str	w10, [x19, w21, uxtw #2]
	mov	w21, w11
	b	.LBB0_27
.LBB0_30:                               //   in Loop: Header=BB0_31 Depth=1
	add	x9, x9, #1
	cmp	x9, x8
	b.hs	.LBB0_33
.LBB0_31:                               // =>This Inner Loop Header: Depth=1
	ldrb	w10, [x20, x9]
	cmp	w10, w22, uxtb
	b.ne	.LBB0_30
// %bb.32:                              //   in Loop: Header=BB0_31 Depth=1
	add	w10, w21, #1
	str	w9, [x19, w21, uxtw #2]
	mov	w21, w10
	b	.LBB0_30
.LBB0_33:
	mov	w0, w21
	ldp	x20, x19, [sp, #96]             // 16-byte Folded Reload
	ldp	x22, x21, [sp, #80]             // 16-byte Folded Reload
	ldp	x24, x23, [sp, #64]             // 16-byte Folded Reload
	ldp	x26, x25, [sp, #48]             // 16-byte Folded Reload
	ldp	x28, x27, [sp, #32]             // 16-byte Folded Reload
	ldp	x29, x30, [sp, #16]             // 16-byte Folded Reload
	add	sp, sp, #112
	ret
.LBB0_34:
	mov	x28, xzr
	mov	w21, wzr
	b	.LBB0_36
.LBB0_35:                               //   in Loop: Header=BB0_36 Depth=1
	add	x28, x28, #1
	cmp	x28, x27
	b.eq	.LBB0_2
.LBB0_36:                               // =>This Loop Header: Depth=1
                                        //     Child Loop BB0_40 Depth 2
	lsl	x24, x28, #3
	and	w23, w22, #0xff
	add	x0, x20, x24
	bl	zbtLeafTagWord
	mov	w1, w22
	mov	x26, x0
	bl	zbtIndexTagMask
	cmp	w23, #1
	mov	x25, x0
	b.ne	.LBB0_38
// %bb.37:                              //   in Loop: Header=BB0_36 Depth=1
	mov	x0, x26
	mov	w1, wzr
	bl	zbtIndexTagMask
	orr	x25, x0, x25
.LBB0_38:                               //   in Loop: Header=BB0_36 Depth=1
	cbnz	x25, .LBB0_40
	b	.LBB0_35
.LBB0_39:                               //   in Loop: Header=BB0_40 Depth=2
	sub	x8, x25, #1
	ands	x25, x8, x25
	b.eq	.LBB0_35
.LBB0_40:                               //   Parent Loop BB0_36 Depth=1
                                        // =>  This Inner Loop Header: Depth=2
	mov	x0, x25
	and	w23, w22, #0xff
	bl	zbtIndexFirstTag
	add	w8, w0, w24
	cmp	w23, #1
	ldrb	w9, [x20, w8, uxtw]
	ccmp	w9, #0, #0, eq
	cset	w10, eq
	cmp	w9, w23
	ccmp	w10, #0, #0, ne
	b.eq	.LBB0_39
// %bb.41:                              //   in Loop: Header=BB0_40 Depth=2
	add	w9, w21, #1
	str	w8, [x19, w21, uxtw #2]
	mov	w21, w9
	b	.LBB0_39
.Lfunc_end0:
	.size	compile_probe, .Lfunc_end0-compile_probe
                                        // -- End function
	.ident	"Ubuntu clang version 18.1.3 (1ubuntu1)"
	.section	".note.GNU-stack","",@progbits
	.addrsig
