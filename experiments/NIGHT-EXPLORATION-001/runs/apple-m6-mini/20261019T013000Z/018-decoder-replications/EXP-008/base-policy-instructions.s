cbz	w2, LBB56_25
ldrb	w10, [x0, #52]
ldr	x8, [x0, #40]
cbz	w10, LBB56_10
ldrb	w9, [x0, #19]
ldrb	w14, [x0, #53]
ldrb	w15, [x0, #17]
mov	x11, #-1
lsl	x16, x11, x10
cmp	w10, #64
csinv	x11, x11, x16, eq
tst	w10, #0x7
b.eq	LBB56_12
add	x12, x0, #56
mov	w13, w2
cmp	w10, #59
b.lo	LBB56_16
cmp	w10, #60
b.eq	LBB56_16
mvn	w16, w1
add	w15, w16, w15
mov	w16, #64
b	LBB56_7
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
cbz	x13, LBB56_25
tst	w14, #0xff
csel	w17, w1, w15, eq
umull	x2, w10, w17
lsr	x0, x2, #3
ldr	x17, [x12, x0]
and	x4, x2, #0x7
lsr	x17, x17, x4
ands	w2, w2, #0x7
b.eq	LBB56_6
sub	w2, w16, w2
cmp	w2, w10
b.hs	LBB56_6
add	x0, x0, x12
ldrb	w0, [x0, #8]
lsl	x0, x0, x2
orr	x17, x0, x17
b	LBB56_6
and	x9, x8, #0x7fffffffffffffff
cmp	x8, #0
csinv	x8, x9, x8, lt
mov	w9, w2
cmp	w2, #8
b.hs	LBB56_20
mov	x10, #0
b	LBB56_23
lsr	x10, x10, #3
add	x12, x0, #56
mov	w13, w2
tst	w14, #0xff
b.eq	LBB56_15
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
cbnz	x13, LBB56_14
b	LBB56_25
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
b.ne	LBB56_15
b	LBB56_25
mvn	x11, x16
tst	w14, #0xff
b.eq	LBB56_19
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
cbnz	x13, LBB56_18
b	LBB56_25
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
b.ne	LBB56_19
b	LBB56_25
and	x10, x9, #0xfffffff8
dup.2d	v0, x8
add	x11, x3, #32
mov	x12, x10
stp	q0, q0, [x11, #-32]
stp	q0, q0, [x11], #64
subs	x12, x12, #8
b.ne	LBB56_21
cmp	x10, x9
b.eq	LBB56_25
sub	x9, x9, x10
add	x10, x3, x10, lsl #3
str	x8, [x10], #8
subs	x9, x9, #1
b.ne	LBB56_24
