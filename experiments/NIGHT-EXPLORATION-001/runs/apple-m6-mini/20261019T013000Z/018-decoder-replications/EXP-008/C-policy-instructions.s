cbz	w2, LBB56_34
cmp	w2, #16
b.hi	LBB56_12
mov	x8, #0
ldr	x9, [x0, #40]
add	x10, x0, #56
mov	x11, #-1
mov	w12, #64
mov	x13, x1
mov	w14, w2
b	LBB56_5
lsl	x2, x11, x16
cmp	w16, #64
csinv	x16, x11, x2, hs
and	x16, x17, x16
ldrb	w17, [x0, #19]
lsl	x16, x16, x17
cmp	w15, #0
cneg	x15, x16, ne
add	x15, x9, x15
and	x16, x15, #0x7fffffffffffffff
cmp	x15, #0
csinv	x15, x16, x15, lt
str	x15, [x3], #8
add	x8, x8, #1
add	w13, w13, #1
subs	x14, x14, #1
b.eq	LBB56_34
ldrb	w16, [x0, #52]
ldrb	w15, [x0, #53]
cbz	w16, LBB56_11
mov	x17, x13
cbz	w15, LBB56_8
ldrb	w17, [x0, #17]
add	w2, w1, w8
mvn	w2, w2
add	w17, w17, w2
umull	x4, w16, w17
lsr	x2, x4, #3
ldr	x17, [x10, x2]
and	x5, x4, #0x7
lsr	x17, x17, x5
ands	w4, w4, #0x7
b.eq	LBB56_3
sub	w4, w12, w4
cmp	w4, w16
b.hs	LBB56_3
add	x2, x2, x10
ldrb	w2, [x2, #8]
lsl	x2, x2, x4
orr	x17, x2, x17
b	LBB56_3
mov	x16, #0
b	LBB56_4
ldrb	w10, [x0, #52]
ldr	x8, [x0, #40]
cbz	w10, LBB56_21
ldrb	w9, [x0, #19]
ldrb	w14, [x0, #53]
ldrb	w15, [x0, #17]
mov	x11, #-1
lsl	x16, x11, x10
cmp	w10, #64
csinv	x11, x11, x16, eq
tst	w10, #0x7
b.eq	LBB56_26
add	x12, x0, #56
mov	w13, w2
cmp	w10, #59
b.lo	LBB56_30
cmp	w10, #60
b.eq	LBB56_30
mvn	w16, w1
add	w15, w16, w15
mov	w16, #64
b	LBB56_18
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
cbz	x13, LBB56_34
tst	w14, #0xff
csel	w17, w1, w15, eq
umull	x2, w10, w17
lsr	x0, x2, #3
ldr	x17, [x12, x0]
and	x4, x2, #0x7
lsr	x17, x17, x4
ands	w2, w2, #0x7
b.eq	LBB56_17
sub	w2, w16, w2
cmp	w2, w10
b.hs	LBB56_17
add	x0, x0, x12
ldrb	w0, [x0, #8]
lsl	x0, x0, x2
orr	x17, x0, x17
b	LBB56_17
and	x9, x8, #0x7fffffffffffffff
cmp	x8, #0
csinv	x8, x9, x8, lt
mov	w9, w2
and	x10, x9, #0xfffffff8
dup.2d	v0, x8
add	x11, x3, #32
mov	x12, x10
stp	q0, q0, [x11, #-32]
stp	q0, q0, [x11], #64
subs	x12, x12, #8
b.ne	LBB56_22
subs	x10, x9, x10
b.eq	LBB56_34
lsl	x9, x9, #3
and	x9, x9, #0x7ffffffc0
add	x9, x3, x9
str	x8, [x9], #8
subs	x10, x10, #1
b.ne	LBB56_25
b	LBB56_34
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
cbnz	x13, LBB56_28
b	LBB56_34
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
b	LBB56_34
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
b	LBB56_34
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
