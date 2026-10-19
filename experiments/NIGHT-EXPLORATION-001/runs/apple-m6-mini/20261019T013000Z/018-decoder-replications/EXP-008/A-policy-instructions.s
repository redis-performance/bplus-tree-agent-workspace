cbz	w2, LBB56_28
cmp	w2, #4
b.hi	LBB56_9
ldr	x8, [x0, #40]
add	x9, x0, #56
ldrb	w11, [x0, #52]
ldrb	w10, [x0, #53]
cbz	w11, LBB56_18
mov	x12, x1
cbz	w10, LBB56_5
ldrb	w12, [x0, #17]
mvn	w13, w1
add	w12, w12, w13
umull	x14, w11, w12
lsr	x13, x14, #3
ldr	x12, [x9, x13]
and	x15, x14, #0x7
lsr	x12, x12, x15
ands	w14, w14, #0x7
b.eq	LBB56_8
mov	w15, #64
sub	w14, w15, w14
cmp	w14, w11
b.hs	LBB56_8
add	x13, x13, x9
ldrb	w13, [x13, #8]
lsl	x13, x13, x14
orr	x12, x13, x12
mov	x13, #-1
lsl	x14, x13, x11
cmp	w11, #64
csinv	x11, x13, x14, hs
and	x11, x12, x11
ldrb	w12, [x0, #19]
lsl	x11, x11, x12
b	LBB56_19
ldrb	w10, [x0, #52]
ldr	x8, [x0, #40]
cbz	w10, LBB56_23
ldrb	w9, [x0, #19]
ldrb	w14, [x0, #53]
ldrb	w15, [x0, #17]
mov	x11, #-1
lsl	x16, x11, x10
cmp	w10, #64
csinv	x11, x11, x16, eq
tst	w10, #0x7
b.eq	LBB56_25
add	x12, x0, #56
mov	w13, w2
cmp	w10, #59
b.lo	LBB56_30
cmp	w10, #60
b.eq	LBB56_30
mvn	w16, w1
add	w15, w16, w15
mov	w16, #64
b	LBB56_15
and	x17, x17, x11
lsl	x17, x17, x9
tst	w14, #0xff
cneg	x17, x17, ne
add	x17, x17, x8
and	x0, x17, #0x7fffffffffffffff
cmp	x17, #0
csinv	x17, x0, x17, lt
str	x17, [x3], #8
add	w1, w1, #1
sub	w15, w15, #1
sub	x13, x13, #1
cbz	x13, LBB56_28
tst	w14, #0xff
csel	w17, w1, w15, eq
umull	x2, w10, w17
lsr	x0, x2, #3
ldr	x17, [x12, x0]
and	x4, x2, #0x7
lsr	x17, x17, x4
ands	w2, w2, #0x7
b.eq	LBB56_14
sub	w2, w16, w2
cmp	w2, w10
b.hs	LBB56_14
add	x0, x0, x12
ldrb	w0, [x0, #8]
lsl	x0, x0, x2
orr	x17, x0, x17
b	LBB56_14
mov	x11, #0
cmp	w10, #0
cneg	x10, x11, ne
add	x10, x8, x10
and	x11, x10, #0x7fffffffffffffff
cmp	x10, #0
csinv	x10, x11, x10, lt
str	x10, [x3]
cmp	w2, #1
b.eq	LBB56_28
ldrb	w11, [x0, #52]
ldrb	w10, [x0, #53]
cbz	w11, LBB56_34
cbz	w10, LBB56_40
ldrb	w12, [x0, #17]
sub	w12, w12, w1
sub	w12, w12, #2
b	LBB56_41
and	x9, x8, #0x7fffffffffffffff
cmp	x8, #0
csinv	x8, x9, x8, lt
mov	w9, w2
cmp	w2, #8
b.hs	LBB56_35
mov	x10, #0
b	LBB56_38
lsr	x10, x10, #3
add	x12, x0, #56
mov	w13, w2
tst	w14, #0xff
b.eq	LBB56_29
mvn	w14, w1
add	w14, w14, w15
umull	x15, w10, w14
ldr	x15, [x12, x15]
and	x15, x15, x11
lsl	x15, x15, x9
sub	x15, x8, x15
and	x16, x15, #0x7fffffffffffffff
cmp	x15, #0
csinv	x15, x16, x15, lt
str	x15, [x3], #8
sub	w14, w14, #1
sub	x13, x13, #1
cbnz	x13, LBB56_27
umull	x14, w10, w1
ldr	x14, [x12, x14]
and	x14, x14, x11
lsl	x14, x14, x9
add	x14, x14, x8
and	x15, x14, #0x7fffffffffffffff
cmp	x14, #0
csinv	x14, x15, x14, lt
str	x14, [x3], #8
add	w1, w1, #1
subs	x13, x13, #1
b.ne	LBB56_29
b	LBB56_28
mvn	x11, x16
tst	w14, #0xff
b.eq	LBB56_33
mvn	w14, w1
add	w14, w14, w15
umull	x15, w10, w14
lsr	x16, x15, #3
ldr	x16, [x12, x16]
and	x15, x15, #0x7
lsr	x15, x16, x15
and	x15, x15, x11
lsl	x15, x15, x9
sub	x15, x8, x15
and	x16, x15, #0x7fffffffffffffff
cmp	x15, #0
csinv	x15, x16, x15, lt
str	x15, [x3], #8
sub	w14, w14, #1
sub	x13, x13, #1
cbnz	x13, LBB56_32
b	LBB56_28
umull	x14, w10, w1
lsr	x15, x14, #3
ldr	x15, [x12, x15]
and	x14, x14, #0x7
lsr	x14, x15, x14
and	x14, x14, x11
lsl	x14, x14, x9
add	x14, x14, x8
and	x15, x14, #0x7fffffffffffffff
cmp	x14, #0
csinv	x14, x15, x14, lt
str	x14, [x3], #8
add	w1, w1, #1
subs	x13, x13, #1
b.ne	LBB56_33
b	LBB56_28
mov	x11, #0
b	LBB56_45
and	x10, x9, #0xfffffff8
dup.2d	v0, x8
add	x11, x3, #32
mov	x12, x10
stp	q0, q0, [x11, #-32]
stp	q0, q0, [x11], #64
subs	x12, x12, #8
b.ne	LBB56_36
cmp	x10, x9
b.eq	LBB56_28
sub	x9, x9, x10
add	x10, x3, x10, lsl #3
str	x8, [x10], #8
subs	x9, x9, #1
b.ne	LBB56_39
b	LBB56_28
add	w12, w1, #1
umull	x14, w11, w12
lsr	x13, x14, #3
ldr	x12, [x9, x13]
and	x15, x14, #0x7
lsr	x12, x12, x15
ands	w14, w14, #0x7
b.eq	LBB56_44
mov	w15, #64
sub	w14, w15, w14
cmp	w14, w11
b.hs	LBB56_44
add	x13, x13, x9
ldrb	w13, [x13, #8]
lsl	x13, x13, x14
orr	x12, x13, x12
mov	x13, #-1
lsl	x14, x13, x11
cmp	w11, #64
csinv	x11, x13, x14, hs
and	x11, x12, x11
ldrb	w12, [x0, #19]
lsl	x11, x11, x12
cmp	w10, #0
cneg	x10, x11, ne
add	x10, x8, x10
and	x11, x10, #0x7fffffffffffffff
cmp	x10, #0
csinv	x10, x11, x10, lt
str	x10, [x3, #8]
cmp	w2, #2
b.eq	LBB56_28
ldrb	w11, [x0, #52]
ldrb	w10, [x0, #53]
cbz	w11, LBB56_49
cbz	w10, LBB56_50
ldrb	w12, [x0, #17]
sub	w12, w12, w1
sub	w12, w12, #3
b	LBB56_51
mov	x11, #0
b	LBB56_55
add	w12, w1, #2
umull	x14, w11, w12
lsr	x13, x14, #3
ldr	x12, [x9, x13]
and	x15, x14, #0x7
lsr	x12, x12, x15
ands	w14, w14, #0x7
b.eq	LBB56_54
mov	w15, #64
sub	w14, w15, w14
cmp	w14, w11
b.hs	LBB56_54
add	x13, x13, x9
ldrb	w13, [x13, #8]
lsl	x13, x13, x14
orr	x12, x13, x12
mov	x13, #-1
lsl	x14, x13, x11
cmp	w11, #64
csinv	x11, x13, x14, hs
and	x11, x12, x11
ldrb	w12, [x0, #19]
lsl	x11, x11, x12
cmp	w10, #0
cneg	x10, x11, ne
add	x10, x8, x10
and	x11, x10, #0x7fffffffffffffff
cmp	x10, #0
csinv	x10, x11, x10, lt
str	x10, [x3, #16]
cmp	w2, #3
b.eq	LBB56_28
ldrb	w11, [x0, #52]
ldrb	w10, [x0, #53]
cbz	w11, LBB56_59
cbz	w10, LBB56_60
ldrb	w12, [x0, #17]
sub	w12, w12, w1
sub	w12, w12, #4
b	LBB56_61
mov	x9, #0
b	LBB56_65
add	w12, w1, #3
umull	x14, w11, w12
lsr	x13, x14, #3
ldr	x12, [x9, x13]
and	x15, x14, #0x7
lsr	x12, x12, x15
ands	w14, w14, #0x7
b.eq	LBB56_64
mov	w15, #64
sub	w14, w15, w14
cmp	w14, w11
b.hs	LBB56_64
add	x9, x13, x9
ldrb	w9, [x9, #8]
lsl	x9, x9, x14
orr	x12, x9, x12
mov	x9, #-1
lsl	x13, x9, x11
cmp	w11, #64
csinv	x9, x9, x13, hs
and	x9, x12, x9
ldrb	w11, [x0, #19]
lsl	x9, x9, x11
cmp	w10, #0
cneg	x9, x9, ne
add	x8, x8, x9
and	x9, x8, #0x7fffffffffffffff
cmp	x8, #0
csinv	x8, x9, x8, lt
str	x8, [x3, #24]
