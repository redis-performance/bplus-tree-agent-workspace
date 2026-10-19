_zbtIndexScanSlot:
  +0000  stp	x28, x27, [sp, #-0x60]!
  +0004  stp	x26, x25, [sp, #0x10]
  +0008  stp	x24, x23, [sp, #0x20]
  +0012  stp	x22, x21, [sp, #0x30]
  +0016  stp	x20, x19, [sp, #0x40]
  +0020  stp	x29, x30, [sp, #0x50]
  +0024  add	x29, sp, #0x50
  +0028  sub	sp, sp, #0x1b0
  +0032  stp	x6, x7, [sp, #0x10]
  +0036  mov	x21, x5
  +0040  mov	x24, x2
  +0044  adrp	x8, 3 ; __image+0x14000
  +0048  ldr	x8, [x8, #0x60] ; literal pool symbol address: ___stack_chk_guard
  +0052  ldr	x8, [x8]
  +0056  stur	x8, [x29, #-0x60]
  +0060  mov	x8, x2
  +0064  ldr	x9, [x8], #0x10
  +0068  lsl	w10, w3, #3
  +0072  lsr	x9, x9, x10
  +0076  ldr	w10, [x1, #0x20]
  +0080  cbz	w10, __image+0x1127c
  +0084  ldr	w8, [x8, w3, uxtw #2]
  +0088  and	x14, x9, #0xff
  +0092  cmp	x14, #0x0
  +0096  ccmn	w8, #0x1, #0x4, ne
  +0100  b.ne	__image+0x1129c
  +0104  b	__image+0x11360
  +0108  ldrh	w8, [x8, w3, uxtw #1]
  +0112  mov	w11, #0xffff
  +0116  cmp	w8, w11
  +0120  csinv	w8, w8, wzr, ne
  +0124  and	x14, x9, #0xff
  +0128  cmp	x14, #0x0
  +0132  ccmn	w8, #0x1, #0x4, ne
  +0136  b.eq	__image+0x11360
  +0140  cbz	x21, __image+0x11328
  +0144  mov	x12, x4
  +0148  cmp	x4, x21
  +0152  b.hs	__image+0x11320
  +0156  mov	x11, #0x7c15
  +0160  movk	x11, #0x7f4a, lsl #16
  +0164  movk	x11, #0x79b9, lsl #32
  +0168  movk	x11, #0x9e37, lsl #48
  +0172  mul	x11, x14, x11
  +0176  mov	w12, #0x1
  +0180  lsl	x13, x12, x9
  +0184  lsr	x15, x11, #58
  +0188  lsl	x15, x12, x15
  +0192  orr	x13, x15, x13
  +0196  lsr	x11, x11, #36
  +0200  lsl	x11, x12, x11
  +0204  orr	x11, x13, x11
  +0208  ldr	x12, [x1]
  +0212  cmp	w10, #0x0
  +0216  mov	w10, #0x30
  +0220  mov	w13, #0x20
  +0224  csel	x10, x13, x10, eq
  +0228  madd	x12, x10, x4, x12
  +0232  add	x13, x12, #0x8
  +0236  mov	x12, x4
  +0240  ldr	x15, [x13]
  +0244  bics	xzr, x11, x15
  +0248  b.eq	__image+0x11320
  +0252  add	x13, x13, x10
  +0256  add	x12, x12, #0x1
  +0260  cmp	x21, x12
  +0264  b.ne	__image+0x11300
  +0268  b	__image+0x11360
  +0272  cmp	x12, x21
  +0276  b.eq	__image+0x11360
  +0280  ldr	w10, [x0, #0x54]
  +0284  cmp	w8, w10
  +0288  b.hs	__image+0x1134c
  +0292  ldr	x10, [x0, #0x48]
  +0296  ldr	x26, [x10, w8, uxtw #3]
  +0300  and	x10, x26, #0x1
  +0304  cmp	x26, #0x0
  +0308  ccmp	x10, #0x0, #0x0, ne
  +0312  b.eq	__image+0x113a0
  +0316  ldr	x8, [x0, #0x40]
  +0320  cbz	x8, __image+0x119d0
  +0324  add	x8, x0, #0x18
  +0328  cmp	x1, x8
  +0332  b.ne	__image+0x119d0
  +0336  mov	x25, #0x0
  +0340  ldur	x8, [x29, #-0x60]
  +0344  adrp	x9, 3 ; __image+0x14000
  +0348  ldr	x9, [x9, #0x60] ; literal pool symbol address: ___stack_chk_guard
  +0352  ldr	x9, [x9]
  +0356  cmp	x9, x8
  +0360  b.ne	__image+0x119b4
  +0364  mov	x0, x25
  +0368  add	sp, sp, #0x1b0
  +0372  ldp	x29, x30, [sp, #0x50]
  +0376  ldp	x20, x19, [sp, #0x40]
  +0380  ldp	x22, x21, [sp, #0x30]
  +0384  ldp	x24, x23, [sp, #0x20]
  +0388  ldp	x26, x25, [sp, #0x10]
  +0392  ldp	x28, x27, [sp], #0x60
  +0396  ret
  +0400  ldr	w10, [x26, #0x30]
  +0404  cmp	w10, w8
  +0408  b.ne	__image+0x119e8
  +0412  ldr	x8, [x0, #0x40]
  +0416  cbz	x8, __image+0x113d4
  +0420  ldrh	w10, [x26, #0x16]
  +0424  ldrh	w11, [x8, #0x2c]
  +0428  cmp	w10, w11
  +0432  cset	w10, eq
  +0436  cmp	x1, x8
  +0440  cset	w8, ne
  +0444  cmp	w8, w10
  +0448  b.eq	__image+0x11360
  +0452  ldrb	w10, [x26, #0x34]
  +0456  ldrb	w8, [x26, #0x11]
  +0460  cbz	x10, __image+0x113f4
  +0464  mov	w11, #0x7
  +0468  madd	w10, w8, w10, w11
  +0472  lsr	w10, w10, #3
  +0476  add	w10, w10, #0x9
  +0480  and	x10, x10, #0x7ffe
  +0484  and	w9, w9, #0xff
  +0488  add	x28, x26, #0x38
  +0492  ldrb	w11, [x26, #0x35]
  +0496  cmp	w8, #0x8
  +0500  stp	x4, x1, [sp]
  +0504  b.hs	__image+0x11474
  +0508  mov	w27, #0x0
  +0512  tst	w8, #0x7
  +0516  b.eq	__image+0x116f8
  +0520  and	x12, x8, #0xf8
  +0524  cmp	w9, #0x1
  +0528  b.ne	__image+0x11518
  +0532  cbz	w11, __image+0x1167c
  +0536  mvn	w9, w8
  +0540  orr	w9, w9, #0xffffff07
  +0544  add	w9, w9, w8
  +0548  add	x11, x12, #0x38
  +0552  add	x10, x10, x8, lsl #1
  +0556  add	x10, x26, x10
  +0560  add	x12, sp, #0x20
  +0564  b	__image+0x1145c
  +0568  sub	w9, w9, #0x1
  +0572  sub	x13, x11, #0x37
  +0576  add	x11, x11, #0x1
  +0580  cmp	x13, x8
  +0584  b.hs	__image+0x116f8
  +0588  ldrb	w13, [x10, x11]
  +0592  cmp	w13, #0x1
  +0596  b.hi	__image+0x11448
  +0600  str	w9, [x12, w27, uxtw #2]
  +0604  add	w27, w27, #0x1
  +0608  b	__image+0x11448
  +0612  add	x12, x28, x10
  +0616  add	x12, x12, x8, lsl #1
  +0620  lsr	x13, x8, #3
  +0624  mov	x15, #__image+0x101010001010101
  +0628  mul	x14, x14, x15
  +0632  cbz	w11, __image+0x11568
  +0636  sub	w15, w8, #0x1
  +0640  cmp	w9, #0x1
  +0644  b.ne	__image+0x11604
  +0648  mov	x14, #0x0
  +0652  mov	w27, #0x0
  +0656  add	x16, sp, #0x20
  +0660  b	__image+0x114b4
  +0664  add	x14, x14, #0x1
  +0668  cmp	x14, x13
  +0672  b.eq	__image+0x11410
  +0676  lsl	x17, x14, #3
  +0680  ldr	x0, [x12, x17]
  +0684  eor	x1, x0, #__image+0x101010001010101
  +0688  mov	x2, #-__image+0x101010001010102
  +0692  movk	x2, #0xfeff
  +0696  add	x1, x1, x2
  +0700  add	x2, x0, x2
  +0704  orr	x1, x1, x2
  +0708  bic	x0, x1, x0
  +0712  ands	x0, x0, #__image+0x8080807f80808080
  +0716  b.ne	__image+0x114f0
  +0720  b	__image+0x114a8
  +0724  sub	x1, x0, #0x1
  +0728  ands	x0, x1, x0
  +0732  b.eq	__image+0x114a8
  +0736  rbit	x1, x0
  +0740  clz	x1, x1
  +0744  orr	w1, w17, w1, lsr #3
  +0748  ldrb	w2, [x12, w1, uxtw]
  +0752  cmp	w2, #0x1
  +0756  b.hi	__image+0x114e4
  +0760  sub	w1, w15, w1
  +0764  str	w1, [x16, w27, uxtw #2]
  +0768  add	w27, w27, #0x1
  +0772  b	__image+0x114e4
  +0776  add	x13, x10, x8, lsl #1
  +0780  cbz	w11, __image+0x116bc
  +0784  mvn	w10, w8
  +0788  orr	w10, w10, #0xffffff07
  +0792  add	w10, w10, w8
  +0796  add	x12, x12, #0x38
  +0800  add	x11, x26, x13
  +0804  add	x13, sp, #0x20
  +0808  b	__image+0x11550
  +0812  sub	w10, w10, #0x1
  +0816  sub	x14, x12, #0x37
  +0820  add	x12, x12, #0x1
  +0824  cmp	x14, x8
  +0828  b.hs	__image+0x116f8
  +0832  ldrb	w14, [x11, x12]
  +0836  cmp	w14, w9
  +0840  b.ne	__image+0x1153c
  +0844  str	w10, [x13, w27, uxtw #2]
  +0848  add	w27, w27, #0x1
  +0852  b	__image+0x1153c
  +0856  mov	x15, #0x0
  +0860  mov	w27, #0x0
  +0864  add	x16, sp, #0x20
  +0868  b	__image+0x11584
  +0872  add	x15, x15, #0x1
  +0876  cmp	x15, x13
  +0880  b.eq	__image+0x11410
  +0884  lsl	x17, x15, #3
  +0888  ldr	x0, [x12, x17]
  +0892  eor	x1, x0, x14
  +0896  mov	x3, #-__image+0x101010001010102
  +0900  movk	x3, #0xfeff
  +0904  add	x2, x1, x3
  +0908  bic	x1, x2, x1
  +0912  and	x1, x1, #__image+0x8080807f80808080
  +0916  cmp	w9, #0x1
  +0920  add	x2, x0, x3
  +0924  bic	x0, x2, x0
  +0928  and	x0, x0, #__image+0x8080807f80808080
  +0932  orr	x0, x1, x0
  +0936  csel	x0, x1, x0, ne
  +0940  cbnz	x0, __image+0x115d0
  +0944  b	__image+0x11578
  +0948  sub	x1, x0, #0x1
  +0952  ands	x0, x1, x0
  +0956  b.eq	__image+0x11578
  +0960  cmp	w9, #0x1
  +0964  rbit	x1, x0
  +0968  clz	x1, x1
  +0972  orr	w1, w17, w1, lsr #3
  +0976  ldrb	w2, [x12, w1, uxtw]
  +0980  ccmp	w2, #0x0, #0x0, eq
  +0984  cset	w3, eq
  +0988  cmp	w2, w9
  +0992  ccmp	w3, #0x0, #0x0, ne
  +0996  b.eq	__image+0x115c4
  +1000  str	w1, [x16, w27, uxtw #2]
  +1004  add	w27, w27, #0x1
  +1008  b	__image+0x115c4
  +1012  mov	x16, #0x0
  +1016  mov	w27, #0x0
  +1020  add	x17, sp, #0x20
  +1024  b	__image+0x11620
  +1028  add	x16, x16, #0x1
  +1032  cmp	x16, x13
  +1036  b.eq	__image+0x11410
  +1040  lsl	x0, x16, #3
  +1044  ldr	x1, [x12, x0]
  +1048  eor	x1, x1, x14
  +1052  mov	x2, #-__image+0x101010001010102
  +1056  movk	x2, #0xfeff
  +1060  add	x2, x1, x2
  +1064  bic	x1, x2, x1
  +1068  ands	x1, x1, #__image+0x8080807f80808080
  +1072  b.ne	__image+0x11654
  +1076  b	__image+0x11614
  +1080  sub	x2, x1, #0x1
  +1084  ands	x1, x2, x1
  +1088  b.eq	__image+0x11614
  +1092  rbit	x2, x1
  +1096  clz	x2, x2
  +1100  orr	w2, w0, w2, lsr #3
  +1104  ldrb	w3, [x12, w2, uxtw]
  +1108  cmp	w3, w9
  +1112  b.ne	__image+0x11648
  +1116  sub	w2, w15, w2
  +1120  str	w2, [x17, w27, uxtw #2]
  +1124  add	w27, w27, #0x1
  +1128  b	__image+0x11648
  +1132  add	x9, x12, #0x38
  +1136  add	x10, x10, x8, lsl #1
  +1140  add	x10, x26, x10
  +1144  add	x11, sp, #0x20
  +1148  b	__image+0x116a0
  +1152  sub	x12, x9, #0x37
  +1156  add	x9, x9, #0x1
  +1160  cmp	x12, x8
  +1164  b.hs	__image+0x116f8
  +1168  ldrb	w12, [x10, x9]
  +1172  cmp	w12, #0x1
  +1176  b.hi	__image+0x11690
  +1180  sub	w12, w9, #0x38
  +1184  str	w12, [x11, w27, uxtw #2]
  +1188  add	w27, w27, #0x1
  +1192  b	__image+0x11690
  +1196  add	x11, x12, #0x38
  +1200  add	x10, x26, x13
  +1204  add	x12, sp, #0x20
  +1208  b	__image+0x116dc
  +1212  sub	x13, x11, #0x37
  +1216  add	x11, x11, #0x1
  +1220  cmp	x13, x8
  +1224  b.hs	__image+0x116f8
  +1228  ldrb	w13, [x10, x11]
  +1232  cmp	w13, w9
  +1236  b.ne	__image+0x116cc
  +1240  sub	w13, w11, #0x38
  +1244  str	w13, [x12, w27, uxtw #2]
  +1248  add	w27, w27, #0x1
  +1252  b	__image+0x116cc
  +1256  cbz	w27, __image+0x11a00
  +1260  mov	x20, #0x0
  +1264  mov	x25, #0x0
  +1268  cmp	x21, #0x0
  +1272  ccmp	w27, #0x1, #0x0, eq
  +1276  cset	w22, ne
  +1280  mov	w23, w27
  +1284  b	__image+0x1176c
  +1288  mov	x12, #-0x1
  +1292  lsl	x11, x12, x8
  +1296  cmp	w8, #0x40
  +1300  csinv	x8, x12, x11, hs
  +1304  and	x8, x10, x8
  +1308  ldrb	w10, [x26, #0x13]
  +1312  lsl	x8, x8, x10
  +1316  ldr	x10, [x26, #0x28]
  +1320  cmp	w9, #0x0
  +1324  cneg	x8, x8, ne
  +1328  add	x8, x10, x8
  +1332  and	x9, x8, #__image+0x7ffffffeffffffff
  +1336  cmp	x8, #0x0
  +1340  csinv	x8, x9, x8, lt
  +1344  fmov	d0, x8
  +1348  ldp	x8, x0, [sp, #0x10]
  +1352  blr	x8
  +1356  add	x25, x25, #0x1
  +1360  add	x20, x20, #0x1
  +1364  cmp	x20, x23
  +1368  b.eq	__image+0x11994
  +1372  add	x8, sp, #0x20
  +1376  ldr	w19, [x8, x20, lsl #2]
  +1380  cbz	w22, __image+0x118a8
  +1384  ldrb	w8, [x26, #0x34]
  +1388  cbz	x8, __image+0x11798
  +1392  ldrb	w9, [x26, #0x11]
  +1396  mov	w10, #0x7
  +1400  madd	w8, w9, w8, w10
  +1404  lsr	w8, w8, #3
  +1408  add	w8, w8, #0x9
  +1412  and	x8, x8, #0x7ffe
  +1416  ldrb	w10, [x26, #0x35]
  +1420  mov	x9, x19
  +1424  cbz	w10, __image+0x117b0
  +1428  ldrb	w9, [x26, #0x11]
  +1432  mvn	w10, w19
  +1436  add	w9, w9, w10
  +1440  add	x8, x28, x8
  +1444  ldrh	w8, [x8, w9, uxtw #1]
  +1448  add	x8, x26, x8
  +1452  ldrb	w1, [x8]
  +1456  cmp	w1, #0xfe
  +1460  b.eq	__image+0x117e4
  +1464  cmp	w1, #0xff
  +1468  b.ne	__image+0x11808
  +1472  ldur	w10, [x8, #0x1]
  +1476  ldr	x8, [sp, #0x8]
  +1480  ldr	x8, [x8, #0x8]
  +1484  cbnz	x21, __image+0x11824
  +1488  b	__image+0x1183c
  +1492  ldurh	w1, [x8, #0x1]
  +1496  mov	w9, #0x3
  +1500  add	x0, x8, x9
  +1504  bl	_dictGenHashFunction
  +1508  mov	w10, w0
  +1512  ldr	x8, [sp, #0x8]
  +1516  ldr	x8, [x8, #0x8]
  +1520  cbnz	x21, __image+0x11824
  +1524  b	__image+0x1183c
  +1528  mov	w9, #0x1
  +1532  add	x0, x8, x9
  +1536  bl	_dictGenHashFunction
  +1540  mov	w10, w0
  +1544  ldr	x8, [sp, #0x8]
  +1548  ldr	x8, [x8, #0x8]
  +1552  cbz	x21, __image+0x1183c
  +1556  sub	w9, w8, #0x1
  +1560  and	x9, x9, x10
  +1564  ldr	x11, [sp]
  +1568  cmp	x9, x11
  +1572  ccmp	x9, x21, #0x2, hs
  +1576  b.hs	__image+0x11760
  +1580  cmp	w27, #0x1
  +1584  b.eq	__image+0x118a8
  +1588  cbz	x8, __image+0x11760
  +1592  sub	x9, x8, #0x1
  +1596  and	x10, x9, x10
  +1600  ldr	x12, [sp, #0x8]
  +1604  ldr	x11, [x12]
  +1608  ldr	w12, [x12, #0x20]
  +1612  cmp	w12, #0x0
  +1616  mov	w12, #0x30
  +1620  mov	w13, #0x20
  +1624  csel	x12, x13, x12, eq
  +1628  madd	x13, x10, x12, x11
  +1632  cmp	x13, x24
  +1636  b.eq	__image+0x118a8
  +1640  ldr	x13, [x13]
  +1644  mov	x14, #-__image+0x101010001010102
  +1648  movk	x14, #0xfeff
  +1652  add	x14, x13, x14
  +1656  bic	x13, x14, x13
  +1660  tst	x13, #__image+0x8080807f80808080
  +1664  b.ne	__image+0x11760
  +1668  add	x10, x10, #0x1
  +1672  and	x10, x10, x9
  +1676  subs	x8, x8, #0x1
  +1680  b.ne	__image+0x1186c
  +1684  b	__image+0x11760
  +1688  ldrb	w8, [x26, #0x34]
  +1692  cbz	w8, __image+0x1196c
  +1696  ldrb	w9, [x26, #0x11]
  +1700  mov	w10, #0x7
  +1704  madd	w9, w9, w8, w10
  +1708  lsr	w9, w9, #3
  +1712  add	w9, w9, #0x9
  +1716  and	x10, x9, #0x7ffe
  +1720  ldrb	w9, [x26, #0x35]
  +1724  mov	x11, x19
  +1728  cbz	w9, __image+0x118e0
  +1732  ldrb	w11, [x26, #0x11]
  +1736  mvn	w12, w19
  +1740  add	w11, w11, w12
  +1744  add	x10, x28, x10
  +1748  ldrh	w10, [x10, w11, uxtw #1]
  +1752  add	x10, x26, x10
  +1756  ldrb	w2, [x10]
  +1760  cmp	w2, #0xfd
  +1764  b.hi	__image+0x11950
  +1768  add	x1, x10, #0x1
  +1772  cbz	w8, __image+0x11964
  +1776  cbz	w9, __image+0x11910
  +1780  ldrb	w10, [x26, #0x11]
  +1784  mvn	w11, w19
  +1788  add	w19, w10, w11
  +1792  umull	x12, w8, w19
  +1796  lsr	x11, x12, #3
  +1800  ldr	x10, [x28, x11]
  +1804  and	x13, x12, #0x7
  +1808  lsr	x10, x10, x13
  +1812  ands	w12, w12, #0x7
  +1816  b.eq	__image+0x11718
  +1820  mov	w13, #0x40
  +1824  sub	w12, w13, w12
  +1828  cmp	w12, w8
  +1832  b.hs	__image+0x11718
  +1836  add	x11, x11, x28
  +1840  ldrb	w11, [x11, #0x8]
  +1844  lsl	x11, x11, x12
  +1848  orr	x10, x11, x10
  +1852  b	__image+0x11718
  +1856  cmp	w2, #0xfe
  +1860  b.ne	__image+0x11980
  +1864  ldurh	w2, [x10, #0x1]
  +1868  add	x1, x10, #0x3
  +1872  cbnz	w8, __image+0x11900
  +1876  mov	x8, #0x0
  +1880  b	__image+0x11734
  +1884  mov	x10, #0x0
  +1888  ldrb	w9, [x26, #0x35]
  +1892  mov	x11, x19
  +1896  cbnz	w9, __image+0x118d4
  +1900  b	__image+0x118e0
  +1904  ldur	x1, [x10, #0xd]
  +1908  cbz	x1, __image+0x119b8
  +1912  ldur	x2, [x10, #0x5]
  +1916  cbnz	w8, __image+0x11900
  +1920  b	__image+0x11964
  +1924  orr	x8, x21, x25
  +1928  cbnz	x8, __image+0x11364
  +1932  adrp	x0, 1 ; __image+0x12000
  +1936  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +1940  adrp	x2, 2 ; __image+0x13000
  +1944  add	x2, x2, #0x2ad ; literal pool for: "home_end || emitted != 0"
  +1948  mov	w1, #0x107d
  +1952  bl	_standalone_panic
  +1956  bl	__image+0x122c0 ; symbol stub for: ___stack_chk_fail
  +1960  adrp	x0, 1 ; __image+0x12000
  +1964  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +1968  adrp	x2, 1 ; __image+0x12000
  +1972  add	x2, x2, #0xe54 ; literal pool for: "ptr != NULL"
  +1976  mov	w1, #0x257
  +1980  bl	_standalone_panic
  +1984  adrp	x0, 1 ; __image+0x12000
  +1988  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +1992  adrp	x2, 1 ; __image+0x12000
  +1996  add	x2, x2, #0xe24 ; literal pool for: "zs->member_rehash && table == &zs->member_index"
  +2000  mov	w1, #0x1055
  +2004  bl	_standalone_panic
  +2008  adrp	x0, 1 ; __image+0x12000
  +2012  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +2016  adrp	x2, 1 ; __image+0x12000
  +2020  add	x2, x2, #0xe05 ; literal pool for: "leaf->id == id"
  +2024  mov	w1, #0x1058
  +2028  bl	_standalone_panic
  +2032  adrp	x0, 1 ; __image+0x12000
  +2036  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +2040  adrp	x2, 2 ; __image+0x13000
  +2044  add	x2, x2, #0x2a2 ; literal pool for: "count != 0"
  +2048  mov	w1, #0x1066
  +2052  bl	_standalone_panic

_zbtIndexScanGroup:
  +0000  sub	sp, sp, #0x80
  +0004  stp	x28, x27, [sp, #0x20]
  +0008  stp	x26, x25, [sp, #0x30]
  +0012  stp	x24, x23, [sp, #0x40]
  +0016  stp	x22, x21, [sp, #0x50]
  +0020  stp	x20, x19, [sp, #0x60]
  +0024  stp	x29, x30, [sp, #0x70]
  +0028  add	x29, sp, #0x70
  +0032  mov	x19, x4
  +0036  mov	x20, x3
  +0040  mov	x21, x1
  +0044  mov	x22, x0
  +0048  lsl	x8, x2, #2
  +0052  add	x24, x8, #0x4
  +0056  str	x8, [sp, #0x10]
  +0060  cmn	x8, #0x4
  +0064  b.ne	__image+0xa9a8
  +0068  mov	x25, #0x0
  +0072  b	__image+0xaf44
  +0076  ldr	x9, [x21]
  +0080  ldr	w11, [x21, #0x20]
  +0084  cmp	w11, #0x0
  +0088  mov	w8, #0x30
  +0092  mov	w10, #0x20
  +0096  csel	x8, x10, x8, eq
  +0100  mul	x10, x8, x2
  +0104  add	x9, x9, x10, lsl #2
  +0108  cbz	w11, __image+0xaba0
  +0112  add	x9, x9, #0x18
  +0116  ldr	x10, [sp, #0x10]
  +0120  b	__image+0xa9e8
  +0124  add	x10, x10, #0x1
  +0128  add	x9, x9, x8
  +0132  cmp	x10, x24
  +0136  b.hs	__image+0xadc8
  +0140  ldur	x11, [x9, #-0x18]
  +0144  tst	x11, #0xff
  +0148  b.eq	__image+0xaa24
  +0152  ldur	w12, [x9, #-0x8]
  +0156  ldr	w13, [x22, #0x54]
  +0160  cmp	w12, w13
  +0164  b.hs	__image+0xaa24
  +0168  ldr	x13, [x22, #0x48]
  +0172  ldr	x12, [x13, x12, lsl #3]
  +0176  and	x13, x12, #0x1
  +0180  cmp	x12, #0x0
  +0184  ccmp	x13, #0x0, #0x0, ne
  +0188  b.ne	__image+0xaa24
  +0192  prfm	pldl1keep, [x12]
  +0196  prfm	pldl1keep, [x12, #0x40]
  +0200  tst	x11, #0xff00
  +0204  b.eq	__image+0xaa5c
  +0208  ldur	w12, [x9, #-0x4]
  +0212  ldr	w13, [x22, #0x54]
  +0216  cmp	w12, w13
  +0220  b.hs	__image+0xaa5c
  +0224  ldr	x13, [x22, #0x48]
  +0228  ldr	x12, [x13, x12, lsl #3]
  +0232  and	x13, x12, #0x1
  +0236  cmp	x12, #0x0
  +0240  ccmp	x13, #0x0, #0x0, ne
  +0244  b.ne	__image+0xaa5c
  +0248  prfm	pldl1keep, [x12]
  +0252  prfm	pldl1keep, [x12, #0x40]
  +0256  tst	x11, #0xff0000
  +0260  b.eq	__image+0xaa94
  +0264  ldr	w12, [x9]
  +0268  ldr	w13, [x22, #0x54]
  +0272  cmp	w12, w13
  +0276  b.hs	__image+0xaa94
  +0280  ldr	x13, [x22, #0x48]
  +0284  ldr	x12, [x13, x12, lsl #3]
  +0288  and	x13, x12, #0x1
  +0292  cmp	x12, #0x0
  +0296  ccmp	x13, #0x0, #0x0, ne
  +0300  b.ne	__image+0xaa94
  +0304  prfm	pldl1keep, [x12]
  +0308  prfm	pldl1keep, [x12, #0x40]
  +0312  tst	x11, #0xff000000
  +0316  b.eq	__image+0xaacc
  +0320  ldr	w12, [x9, #0x4]
  +0324  ldr	w13, [x22, #0x54]
  +0328  cmp	w12, w13
  +0332  b.hs	__image+0xaacc
  +0336  ldr	x13, [x22, #0x48]
  +0340  ldr	x12, [x13, x12, lsl #3]
  +0344  and	x13, x12, #0x1
  +0348  cmp	x12, #0x0
  +0352  ccmp	x13, #0x0, #0x0, ne
  +0356  b.ne	__image+0xaacc
  +0360  prfm	pldl1keep, [x12]
  +0364  prfm	pldl1keep, [x12, #0x40]
  +0368  tst	x11, #__image+0xfe00000000
  +0372  b.eq	__image+0xab04
  +0376  ldr	w12, [x9, #0x8]
  +0380  ldr	w13, [x22, #0x54]
  +0384  cmp	w12, w13
  +0388  b.hs	__image+0xab04
  +0392  ldr	x13, [x22, #0x48]
  +0396  ldr	x12, [x13, x12, lsl #3]
  +0400  and	x13, x12, #0x1
  +0404  cmp	x12, #0x0
  +0408  ccmp	x13, #0x0, #0x0, ne
  +0412  b.ne	__image+0xab04
  +0416  prfm	pldl1keep, [x12]
  +0420  prfm	pldl1keep, [x12, #0x40]
  +0424  tst	x11, #__image+0xfeff00000000
  +0428  b.eq	__image+0xab3c
  +0432  ldr	w12, [x9, #0xc]
  +0436  ldr	w13, [x22, #0x54]
  +0440  cmp	w12, w13
  +0444  b.hs	__image+0xab3c
  +0448  ldr	x13, [x22, #0x48]
  +0452  ldr	x12, [x13, x12, lsl #3]
  +0456  and	x13, x12, #0x1
  +0460  cmp	x12, #0x0
  +0464  ccmp	x13, #0x0, #0x0, ne
  +0468  b.ne	__image+0xab3c
  +0472  prfm	pldl1keep, [x12]
  +0476  prfm	pldl1keep, [x12, #0x40]
  +0480  tst	x11, #__image+0xfeffff00000000
  +0484  b.eq	__image+0xab6c
  +0488  ldr	w12, [x9, #0x10]
  +0492  ldr	w13, [x22, #0x54]
  +0496  cmp	w12, w13
  +0500  b.hs	__image+0xab6c
  +0504  ldr	x13, [x22, #0x48]
  +0508  ldr	x12, [x13, x12, lsl #3]
  +0512  cbz	x12, __image+0xab6c
  +0516  tbnz	w12, #0x0, __image+0xab6c
  +0520  prfm	pldl1keep, [x12]
  +0524  prfm	pldl1keep, [x12, #0x40]
  +0528  lsr	x11, x11, #56
  +0532  cbz	x11, __image+0xa9d8
  +0536  ldr	w11, [x9, #0x14]
  +0540  ldr	w12, [x22, #0x54]
  +0544  cmp	w11, w12
  +0548  b.hs	__image+0xa9d8
  +0552  ldr	x12, [x22, #0x48]
  +0556  ldr	x11, [x12, x11, lsl #3]
  +0560  cbz	x11, __image+0xa9d8
  +0564  tbnz	w11, #0x0, __image+0xa9d8
  +0568  prfm	pldl1keep, [x11]
  +0572  prfm	pldl1keep, [x11, #0x40]
  +0576  b	__image+0xa9d8
  +0580  add	x9, x9, #0x1e
  +0584  mov	w10, #0xffff
  +0588  ldr	x11, [sp, #0x10]
  +0592  b	__image+0xabc0
  +0596  add	x11, x11, #0x1
  +0600  add	x9, x9, x8
  +0604  cmp	x11, x24
  +0608  b.hs	__image+0xadc8
  +0612  ldur	x12, [x9, #-0x1e]
  +0616  tst	x12, #0xff
  +0620  b.eq	__image+0xac04
  +0624  ldurh	w13, [x9, #-0xe]
  +0628  cmp	w13, w10
  +0632  csinv	w13, w13, wzr, ne
  +0636  ldr	w14, [x22, #0x54]
  +0640  cmp	w13, w14
  +0644  b.hs	__image+0xac04
  +0648  ldr	x14, [x22, #0x48]
  +0652  ldr	x13, [x14, w13, uxtw #3]
  +0656  and	x14, x13, #0x1
  +0660  cmp	x13, #0x0
  +0664  ccmp	x14, #0x0, #0x0, ne
  +0668  b.ne	__image+0xac04
  +0672  prfm	pldl1keep, [x13]
  +0676  prfm	pldl1keep, [x13, #0x40]
  +0680  tst	x12, #0xff00
  +0684  b.eq	__image+0xac44
  +0688  ldurh	w13, [x9, #-0xc]
  +0692  cmp	w13, w10
  +0696  csinv	w13, w13, wzr, ne
  +0700  ldr	w14, [x22, #0x54]
  +0704  cmp	w13, w14
  +0708  b.hs	__image+0xac44
  +0712  ldr	x14, [x22, #0x48]
  +0716  ldr	x13, [x14, w13, uxtw #3]
  +0720  and	x14, x13, #0x1
  +0724  cmp	x13, #0x0
  +0728  ccmp	x14, #0x0, #0x0, ne
  +0732  b.ne	__image+0xac44
  +0736  prfm	pldl1keep, [x13]
  +0740  prfm	pldl1keep, [x13, #0x40]
  +0744  tst	x12, #0xff0000
  +0748  b.eq	__image+0xac84
  +0752  ldurh	w13, [x9, #-0xa]
  +0756  cmp	w13, w10
  +0760  csinv	w13, w13, wzr, ne
  +0764  ldr	w14, [x22, #0x54]
  +0768  cmp	w13, w14
  +0772  b.hs	__image+0xac84
  +0776  ldr	x14, [x22, #0x48]
  +0780  ldr	x13, [x14, w13, uxtw #3]
  +0784  and	x14, x13, #0x1
  +0788  cmp	x13, #0x0
  +0792  ccmp	x14, #0x0, #0x0, ne
  +0796  b.ne	__image+0xac84
  +0800  prfm	pldl1keep, [x13]
  +0804  prfm	pldl1keep, [x13, #0x40]
  +0808  tst	x12, #0xff000000
  +0812  b.eq	__image+0xacc4
  +0816  ldurh	w13, [x9, #-0x8]
  +0820  cmp	w13, w10
  +0824  csinv	w13, w13, wzr, ne
  +0828  ldr	w14, [x22, #0x54]
  +0832  cmp	w13, w14
  +0836  b.hs	__image+0xacc4
  +0840  ldr	x14, [x22, #0x48]
  +0844  ldr	x13, [x14, w13, uxtw #3]
  +0848  and	x14, x13, #0x1
  +0852  cmp	x13, #0x0
  +0856  ccmp	x14, #0x0, #0x0, ne
  +0860  b.ne	__image+0xacc4
  +0864  prfm	pldl1keep, [x13]
  +0868  prfm	pldl1keep, [x13, #0x40]
  +0872  tst	x12, #__image+0xfe00000000
  +0876  b.eq	__image+0xad04
  +0880  ldurh	w13, [x9, #-0x6]
  +0884  cmp	w13, w10
  +0888  csinv	w13, w13, wzr, ne
  +0892  ldr	w14, [x22, #0x54]
  +0896  cmp	w13, w14
  +0900  b.hs	__image+0xad04
  +0904  ldr	x14, [x22, #0x48]
  +0908  ldr	x13, [x14, w13, uxtw #3]
  +0912  and	x14, x13, #0x1
  +0916  cmp	x13, #0x0
  +0920  ccmp	x14, #0x0, #0x0, ne
  +0924  b.ne	__image+0xad04
  +0928  prfm	pldl1keep, [x13]
  +0932  prfm	pldl1keep, [x13, #0x40]
  +0936  tst	x12, #__image+0xfeff00000000
  +0940  b.eq	__image+0xad44
  +0944  ldurh	w13, [x9, #-0x4]
  +0948  cmp	w13, w10
  +0952  csinv	w13, w13, wzr, ne
  +0956  ldr	w14, [x22, #0x54]
  +0960  cmp	w13, w14
  +0964  b.hs	__image+0xad44
  +0968  ldr	x14, [x22, #0x48]
  +0972  ldr	x13, [x14, w13, uxtw #3]
  +0976  and	x14, x13, #0x1
  +0980  cmp	x13, #0x0
  +0984  ccmp	x14, #0x0, #0x0, ne
  +0988  b.ne	__image+0xad44
  +0992  prfm	pldl1keep, [x13]
  +0996  prfm	pldl1keep, [x13, #0x40]
  +1000  tst	x12, #__image+0xfeffff00000000
  +1004  b.eq	__image+0xad84
  +1008  ldurh	w13, [x9, #-0x2]
  +1012  cmp	w13, w10
  +1016  csinv	w13, w13, wzr, ne
  +1020  ldr	w14, [x22, #0x54]
  +1024  cmp	w13, w14
  +1028  b.hs	__image+0xad84
  +1032  ldr	x14, [x22, #0x48]
  +1036  ldr	x13, [x14, w13, uxtw #3]
  +1040  and	x14, x13, #0x1
  +1044  cmp	x13, #0x0
  +1048  ccmp	x14, #0x0, #0x0, ne
  +1052  b.ne	__image+0xad84
  +1056  prfm	pldl1keep, [x13]
  +1060  prfm	pldl1keep, [x13, #0x40]
  +1064  lsr	x12, x12, #56
  +1068  cbz	x12, __image+0xabb0
  +1072  ldrh	w12, [x9]
  +1076  cmp	w12, w10
  +1080  csinv	w12, w12, wzr, ne
  +1084  ldr	w13, [x22, #0x54]
  +1088  cmp	w12, w13
  +1092  b.hs	__image+0xabb0
  +1096  ldr	x13, [x22, #0x48]
  +1100  ldr	x12, [x13, w12, uxtw #3]
  +1104  and	x13, x12, #0x1
  +1108  cmp	x12, #0x0
  +1112  ccmp	x13, #0x0, #0x0, ne
  +1116  b.ne	__image+0xabb0
  +1120  prfm	pldl1keep, [x12]
  +1124  prfm	pldl1keep, [x12, #0x40]
  +1128  b	__image+0xabb0
  +1132  mov	x25, #0x0
  +1136  mov	w28, #0x20
  +1140  ldr	x23, [sp, #0x10]
  +1144  ldr	x8, [x21]
  +1148  ldr	w9, [x21, #0x20]
  +1152  cmp	w9, #0x0
  +1156  mov	w9, #0x30
  +1160  csel	x9, x28, x9, eq
  +1164  madd	x26, x9, x23, x8
  +1168  mov	x0, x22
  +1172  mov	x1, x21
  +1176  mov	x2, x26
  +1180  mov	w3, #0x0
  +1184  mov	x4, #0x0
  +1188  mov	x5, #0x0
  +1192  mov	x6, x20
  +1196  mov	x7, x19
  +1200  bl	_zbtIndexScanSlot
  +1204  add	x27, x0, x25
  +1208  mov	x0, x22
  +1212  mov	x1, x21
  +1216  mov	x2, x26
  +1220  mov	w3, #0x1
  +1224  mov	x4, #0x0
  +1228  mov	x5, #0x0
  +1232  mov	x6, x20
  +1236  mov	x7, x19
  +1240  bl	_zbtIndexScanSlot
  +1244  mov	x25, x0
  +1248  mov	x0, x22
  +1252  mov	x1, x21
  +1256  mov	x2, x26
  +1260  mov	w3, #0x2
  +1264  mov	x4, #0x0
  +1268  mov	x5, #0x0
  +1272  mov	x6, x20
  +1276  mov	x7, x19
  +1280  bl	_zbtIndexScanSlot
  +1284  add	x8, x0, x25
  +1288  add	x27, x8, x27
  +1292  mov	x0, x22
  +1296  mov	x1, x21
  +1300  mov	x2, x26
  +1304  mov	w3, #0x3
  +1308  mov	x4, #0x0
  +1312  mov	x5, #0x0
  +1316  mov	x6, x20
  +1320  mov	x7, x19
  +1324  bl	_zbtIndexScanSlot
  +1328  mov	x25, x0
  +1332  mov	x0, x22
  +1336  mov	x1, x21
  +1340  mov	x2, x26
  +1344  mov	w3, #0x4
  +1348  mov	x4, #0x0
  +1352  mov	x5, #0x0
  +1356  mov	x6, x20
  +1360  mov	x7, x19
  +1364  bl	_zbtIndexScanSlot
  +1368  add	x25, x0, x25
  +1372  mov	x0, x22
  +1376  mov	x1, x21
  +1380  mov	x2, x26
  +1384  mov	w3, #0x5
  +1388  mov	x4, #0x0
  +1392  mov	x5, #0x0
  +1396  mov	x6, x20
  +1400  mov	x7, x19
  +1404  bl	_zbtIndexScanSlot
  +1408  add	x8, x0, x25
  +1412  add	x27, x8, x27
  +1416  mov	x0, x22
  +1420  mov	x1, x21
  +1424  mov	x2, x26
  +1428  mov	w3, #0x6
  +1432  mov	x4, #0x0
  +1436  mov	x5, #0x0
  +1440  mov	x6, x20
  +1444  mov	x7, x19
  +1448  bl	_zbtIndexScanSlot
  +1452  mov	x25, x0
  +1456  mov	x0, x22
  +1460  mov	x1, x21
  +1464  mov	x2, x26
  +1468  mov	w3, #0x7
  +1472  mov	x4, #0x0
  +1476  mov	x5, #0x0
  +1480  mov	x6, x20
  +1484  mov	x7, x19
  +1488  bl	_zbtIndexScanSlot
  +1492  add	x8, x0, x25
  +1496  add	x25, x8, x27
  +1500  add	x23, x23, #0x1
  +1504  cmp	x23, x24
  +1508  b.lo	__image+0xadd4
  +1512  ldr	x8, [x21, #0x8]
  +1516  subs	x12, x8, #0x4
  +1520  b.eq	__image+0xb120
  +1524  sub	x8, x8, #0x1
  +1528  str	x8, [sp, #0x8]
  +1532  ldr	x8, [sp, #0x10]
  +1536  orr	x28, x8, #0x3
  +1540  ldr	x8, [x21]
  +1544  ldr	w9, [x21, #0x20]
  +1548  cmp	w9, #0x0
  +1552  mov	w9, #0x30
  +1556  mov	w10, #0x20
  +1560  csel	x9, x10, x9, eq
  +1564  mul	x10, x9, x28
  +1568  ldr	x10, [x8, x10]
  +1572  mov	x11, #-__image+0x101010001010102
  +1576  movk	x11, #0xfeff
  +1580  add	x11, x10, x11
  +1584  bic	x10, x11, x10
  +1588  tst	x10, #__image+0x8080807f80808080
  +1592  b.ne	__image+0xb120
  +1596  add	x10, x28, #0x1
  +1600  ldr	x11, [sp, #0x8]
  +1604  and	x28, x10, x11
  +1608  madd	x26, x9, x28, x8
  +1612  mov	x0, x22
  +1616  mov	x1, x21
  +1620  mov	x2, x26
  +1624  mov	w3, #0x0
  +1628  mov	x27, x20
  +1632  mov	x20, x19
  +1636  mov	x19, x24
  +1640  ldr	x24, [sp, #0x10]
  +1644  mov	x4, x24
  +1648  mov	x5, x19
  +1652  mov	x6, x27
  +1656  mov	x7, x20
  +1660  str	x12, [sp, #0x18]
  +1664  bl	_zbtIndexScanSlot
  +1668  add	x23, x0, x25
  +1672  mov	x0, x22
  +1676  mov	x1, x21
  +1680  mov	x2, x26
  +1684  mov	w3, #0x1
  +1688  mov	x4, x24
  +1692  mov	x5, x19
  +1696  mov	x6, x27
  +1700  mov	x7, x20
  +1704  bl	_zbtIndexScanSlot
  +1708  mov	x25, x0
  +1712  mov	x0, x22
  +1716  mov	x1, x21
  +1720  mov	x2, x26
  +1724  mov	w3, #0x2
  +1728  mov	x4, x24
  +1732  mov	x5, x19
  +1736  mov	x6, x27
  +1740  mov	x7, x20
  +1744  bl	_zbtIndexScanSlot
  +1748  add	x8, x0, x25
  +1752  add	x23, x8, x23
  +1756  mov	x0, x22
  +1760  mov	x1, x21
  +1764  mov	x2, x26
  +1768  mov	w3, #0x3
  +1772  mov	x4, x24
  +1776  mov	x5, x19
  +1780  mov	x6, x27
  +1784  mov	x7, x20
  +1788  bl	_zbtIndexScanSlot
  +1792  mov	x25, x0
  +1796  mov	x0, x22
  +1800  mov	x1, x21
  +1804  mov	x2, x26
  +1808  mov	w3, #0x4
  +1812  mov	x4, x24
  +1816  mov	x5, x19
  +1820  mov	x6, x27
  +1824  mov	x7, x20
  +1828  bl	_zbtIndexScanSlot
  +1832  add	x25, x0, x25
  +1836  mov	x0, x22
  +1840  mov	x1, x21
  +1844  mov	x2, x26
  +1848  mov	w3, #0x5
  +1852  mov	x4, x24
  +1856  mov	x5, x19
  +1860  mov	x6, x27
  +1864  mov	x7, x20
  +1868  bl	_zbtIndexScanSlot
  +1872  add	x8, x0, x25
  +1876  add	x23, x8, x23
  +1880  mov	x0, x22
  +1884  mov	x1, x21
  +1888  mov	x2, x26
  +1892  mov	w3, #0x6
  +1896  mov	x4, x24
  +1900  mov	x5, x19
  +1904  mov	x6, x27
  +1908  mov	x7, x20
  +1912  bl	_zbtIndexScanSlot
  +1916  mov	x25, x0
  +1920  mov	x0, x22
  +1924  mov	x1, x21
  +1928  mov	x2, x26
  +1932  mov	w3, #0x7
  +1936  mov	x4, x24
  +1940  mov	x24, x19
  +1944  mov	x19, x20
  +1948  mov	x20, x27
  +1952  mov	x5, x24
  +1956  mov	x6, x27
  +1960  mov	x7, x19
  +1964  bl	_zbtIndexScanSlot
  +1968  ldr	x12, [sp, #0x18]
  +1972  add	x8, x0, x25
  +1976  add	x25, x8, x23
  +1980  subs	x12, x12, #0x1
  +1984  b.ne	__image+0xaf60
  +1988  mov	x0, x25
  +1992  ldp	x29, x30, [sp, #0x70]
  +1996  ldp	x20, x19, [sp, #0x60]
  +2000  ldp	x22, x21, [sp, #0x50]
  +2004  ldp	x24, x23, [sp, #0x40]
  +2008  ldp	x26, x25, [sp, #0x30]
  +2012  ldp	x28, x27, [sp, #0x20]
  +2016  add	sp, sp, #0x80
  +2020  ret

_zbtreeScoreRaw:
  +0000  sub	sp, sp, #0xa0
  +0004  stp	x28, x27, [sp, #0x40]
  +0008  stp	x26, x25, [sp, #0x50]
  +0012  stp	x24, x23, [sp, #0x60]
  +0016  stp	x22, x21, [sp, #0x70]
  +0020  stp	x20, x19, [sp, #0x80]
  +0024  stp	x29, x30, [sp, #0x90]
  +0028  add	x29, sp, #0x90
  +0032  stp	x2, x3, [sp, #0x28]
  +0036  mov	x22, x0
  +0040  str	x1, [sp, #0x20]
  +0044  mov	x0, x1
  +0048  mov	x1, x2
  +0052  bl	_dictGenHashFunction
  +0056  str	x0, [sp, #0x38]
  +0060  ldr	x8, [x22, #0x40]
  +0064  cbz	x8, __image+0x33e4
  +0068  mov	x0, x22
  +0072  mov	w1, #0x1
  +0076  bl	_zbtIndexRehashStep
  +0080  ldr	x24, [x22, #0x40]
  +0084  cbz	x24, __image+0x33e4
  +0088  ldr	x8, [x24, #0x8]
  +0092  cbz	x8, __image+0x33e4
  +0096  mov	x21, #0x0
  +0100  mov	x25, #0x0
  +0104  mov	w9, #0x1000000
  +0108  ldr	x10, [sp, #0x38]
  +0112  cmp	w10, w9
  +0116  csel	w9, w10, w9, hi
  +0120  lsr	w27, w9, #24
  +0124  sub	x8, x8, #0x1
  +0128  mov	w9, w10
  +0132  stp	x9, x8, [sp, #0x8]
  +0136  and	x26, x8, x9
  +0140  mov	x8, #__image+0x101010001010101
  +0144  mul	x8, x27, x8
  +0148  str	x8, [sp, #0x18]
  +0152  add	x28, x22, #0x18
  +0156  mov	x8, #0x7c15
  +0160  movk	x8, #0x7f4a, lsl #16
  +0164  movk	x8, #0x79b9, lsl #32
  +0168  movk	x8, #0x9e37, lsl #48
  +0172  mul	x8, x27, x8
  +0176  mov	w9, #0x1
  +0180  lsl	x10, x9, x27
  +0184  lsr	x11, x8, #58
  +0188  lsl	x11, x9, x11
  +0192  orr	x10, x11, x10
  +0196  lsr	x8, x8, #36
  +0200  lsl	x8, x9, x8
  +0204  orr	x8, x10, x8
  +0208  str	x8, [sp]
  +0212  mov	w12, #0xffff
  +0216  b	__image+0x3114
  +0220  ldr	w8, [x20, #0x2c]
  +0224  cmn	w8, #0x1
  +0228  cset	w8, eq
  +0232  cmp	w8, #0x0
  +0236  csel	x21, x20, xzr, ne
  +0240  add	x8, x26, #0x1
  +0244  ldr	x9, [sp, #0x10]
  +0248  and	x26, x8, x9
  +0252  add	x25, x25, #0x1
  +0256  ldr	x8, [x24, #0x8]
  +0260  cmp	x25, x8
  +0264  b.hs	__image+0x33e4
  +0268  ldr	x8, [x24]
  +0272  ldr	w9, [x24, #0x20]
  +0276  cmp	w9, #0x0
  +0280  mov	w9, #0x30
  +0284  mov	w10, #0x20
  +0288  csel	x9, x10, x9, eq
  +0292  madd	x20, x9, x26, x8
  +0296  ldr	x8, [x20]
  +0300  ldr	x9, [sp, #0x18]
  +0304  eor	x8, x8, x9
  +0308  mov	x9, #-__image+0x101010001010102
  +0312  movk	x9, #0xfeff
  +0316  add	x9, x8, x9
  +0320  bic	x8, x9, x8
  +0324  ands	x19, x8, #__image+0x8080807f80808080
  +0328  b.eq	__image+0x3234
  +0332  add	x23, x20, #0x10
  +0336  b	__image+0x3180
  +0340  ldp	x4, x1, [sp, #0x30]
  +0344  ldp	x2, x3, [sp, #0x20]
  +0348  mov	x5, #0x0
  +0352  bl	_zbtScoreLeafFindMember
  +0356  mov	w12, #0xffff
  +0360  cbnz	w0, __image+0x377c
  +0364  sub	x8, x19, #0x1
  +0368  ands	x19, x8, x19
  +0372  b.eq	__image+0x3234
  +0376  rbit	x8, x19
  +0380  clz	x8, x8
  +0384  ldr	x9, [x20]
  +0388  and	x10, x8, #0x38
  +0392  lsr	x9, x9, x10
  +0396  cmp	w27, w9, uxtb
  +0400  b.ne	__image+0x3174
  +0404  lsr	x8, x8, #3
  +0408  ldr	w9, [x24, #0x20]
  +0412  cbz	w9, __image+0x31b8
  +0416  ldr	w8, [x23, x8, lsl #2]
  +0420  cmn	w8, #0x1
  +0424  b.ne	__image+0x31c4
  +0428  b	__image+0x3174
  +0432  ldrh	w8, [x23, x8, lsl #1]
  +0436  cmp	w8, w12
  +0440  b.eq	__image+0x3174
  +0444  ldr	w9, [x22, #0x54]
  +0448  cmp	w8, w9
  +0452  b.hs	__image+0x31e8
  +0456  ldr	x9, [x22, #0x48]
  +0460  ldr	x0, [x9, w8, uxtw #3]
  +0464  and	x9, x0, #0x1
  +0468  cmp	x0, #0x0
  +0472  ccmp	x9, #0x0, #0x0, ne
  +0476  b.eq	__image+0x31fc
  +0480  ldr	x8, [x22, #0x40]
  +0484  cbz	x8, __image+0x3784
  +0488  cmp	x24, x28
  +0492  b.eq	__image+0x3174
  +0496  b	__image+0x3784
  +0500  ldr	w9, [x0, #0x30]
  +0504  cmp	w9, w8
  +0508  b.ne	__image+0x379c
  +0512  ldr	x8, [x22, #0x40]
  +0516  cbz	x8, __image+0x315c
  +0520  cmp	x24, x8
  +0524  cset	w9, eq
  +0528  ldrh	w10, [x0, #0x16]
  +0532  ldrh	w8, [x8, #0x2c]
  +0536  cmp	w10, w8
  +0540  cset	w8, ne
  +0544  cmp	w9, w8
  +0548  b.ne	__image+0x315c
  +0552  b	__image+0x3174
  +0556  cbnz	x25, __image+0x3274
  +0560  ldr	w8, [x24, #0x8]
  +0564  sub	w8, w8, #0x1
  +0568  ldr	x9, [sp, #0x8]
  +0572  and	x8, x8, x9
  +0576  ldr	x9, [x24]
  +0580  ldr	w10, [x24, #0x20]
  +0584  cmp	w10, #0x0
  +0588  mov	w10, #0x30
  +0592  mov	w11, #0x20
  +0596  csel	x10, x11, x10, eq
  +0600  umaddl	x8, w10, w8, x9
  +0604  ldr	x8, [x8, #0x8]
  +0608  ldr	x9, [sp]
  +0612  bics	xzr, x9, x8
  +0616  b.ne	__image+0x33e4
  +0620  ldr	x8, [x20]
  +0624  tst	x8, #0xff
  +0628  b.eq	__image+0x33e4
  +0632  cbnz	x21, __image+0x32a8
  +0636  ldr	w9, [x24, #0x20]
  +0640  cbz	w9, __image+0x3294
  +0644  ldr	w9, [x20, #0x10]
  +0648  b	__image+0x3298
  +0652  ldrsh	w9, [x20, #0x10]
  +0656  cmn	w9, #0x1
  +0660  cset	w9, eq
  +0664  cmp	w9, #0x0
  +0668  csel	x21, x20, xzr, ne
  +0672  tst	x8, #0xff00
  +0676  b.eq	__image+0x33e4
  +0680  cbnz	x21, __image+0x32d8
  +0684  ldr	w9, [x24, #0x20]
  +0688  cbz	w9, __image+0x32c4
  +0692  ldr	w9, [x20, #0x14]
  +0696  b	__image+0x32c8
  +0700  ldrsh	w9, [x20, #0x12]
  +0704  cmn	w9, #0x1
  +0708  cset	w9, eq
  +0712  cmp	w9, #0x0
  +0716  csel	x21, x20, xzr, ne
  +0720  tst	x8, #0xff0000
  +0724  b.eq	__image+0x33e4
  +0728  cbnz	x21, __image+0x3308
  +0732  ldr	w9, [x24, #0x20]
  +0736  cbz	w9, __image+0x32f4
  +0740  ldr	w9, [x20, #0x18]
  +0744  b	__image+0x32f8
  +0748  ldrsh	w9, [x20, #0x14]
  +0752  cmn	w9, #0x1
  +0756  cset	w9, eq
  +0760  cmp	w9, #0x0
  +0764  csel	x21, x20, xzr, ne
  +0768  tst	x8, #0xff000000
  +0772  b.eq	__image+0x33e4
  +0776  cbnz	x21, __image+0x3338
  +0780  ldr	w9, [x24, #0x20]
  +0784  cbz	w9, __image+0x3324
  +0788  ldr	w9, [x20, #0x1c]
  +0792  b	__image+0x3328
  +0796  ldrsh	w9, [x20, #0x16]
  +0800  cmn	w9, #0x1
  +0804  cset	w9, eq
  +0808  cmp	w9, #0x0
  +0812  csel	x21, x20, xzr, ne
  +0816  tst	x8, #__image+0xfe00000000
  +0820  b.eq	__image+0x33e4
  +0824  cbnz	x21, __image+0x3368
  +0828  ldr	w9, [x24, #0x20]
  +0832  cbz	w9, __image+0x3354
  +0836  ldr	w9, [x20, #0x20]
  +0840  b	__image+0x3358
  +0844  ldrsh	w9, [x20, #0x18]
  +0848  cmn	w9, #0x1
  +0852  cset	w9, eq
  +0856  cmp	w9, #0x0
  +0860  csel	x21, x20, xzr, ne
  +0864  tst	x8, #__image+0xfeff00000000
  +0868  b.eq	__image+0x33e4
  +0872  cbnz	x21, __image+0x3398
  +0876  ldr	w9, [x24, #0x20]
  +0880  cbz	w9, __image+0x3384
  +0884  ldr	w9, [x20, #0x24]
  +0888  b	__image+0x3388
  +0892  ldrsh	w9, [x20, #0x1a]
  +0896  cmn	w9, #0x1
  +0900  cset	w9, eq
  +0904  cmp	w9, #0x0
  +0908  csel	x21, x20, xzr, ne
  +0912  tst	x8, #__image+0xfeffff00000000
  +0916  b.eq	__image+0x33e4
  +0920  cbnz	x21, __image+0x33c8
  +0924  ldr	w9, [x24, #0x20]
  +0928  cbz	w9, __image+0x33b4
  +0932  ldr	w9, [x20, #0x28]
  +0936  b	__image+0x33b8
  +0940  ldrsh	w9, [x20, #0x1c]
  +0944  cmn	w9, #0x1
  +0948  cset	w9, eq
  +0952  cmp	w9, #0x0
  +0956  csel	x21, x20, xzr, ne
  +0960  lsr	x8, x8, #56
  +0964  cbz	x8, __image+0x33e4
  +0968  cbnz	x21, __image+0x30f8
  +0972  ldr	w8, [x24, #0x20]
  +0976  cbnz	w8, __image+0x30e4
  +0980  ldrsh	w8, [x20, #0x1e]
  +0984  b	__image+0x30e8
  +0988  ldr	x8, [x22, #0x20]
  +0992  cbz	x8, __image+0x3758
  +0996  mov	x25, #0x0
  +1000  mov	x24, #0x0
  +1004  add	x11, x22, #0x18
  +1008  mov	w9, #0x1000000
  +1012  ldr	x10, [sp, #0x38]
  +1016  cmp	w10, w9
  +1020  csel	w9, w10, w9, hi
  +1024  lsr	w27, w9, #24
  +1028  sub	x28, x8, #0x1
  +1032  mov	w8, w10
  +1036  stp	x8, x11, [sp, #0x8]
  +1040  and	x19, x28, x8
  +1044  mov	x8, #__image+0x101010001010101
  +1048  mul	x8, x27, x8
  +1052  str	x8, [sp, #0x18]
  +1056  mov	x8, #0x7c15
  +1060  movk	x8, #0x7f4a, lsl #16
  +1064  movk	x8, #0x79b9, lsl #32
  +1068  movk	x8, #0x9e37, lsl #48
  +1072  mul	x8, x27, x8
  +1076  mov	w9, #0x1
  +1080  lsl	x10, x9, x27
  +1084  lsr	x11, x8, #58
  +1088  lsl	x11, x9, x11
  +1092  orr	x10, x11, x10
  +1096  lsr	x8, x8, #36
  +1100  lsl	x8, x9, x8
  +1104  orr	x8, x10, x8
  +1108  str	x8, [sp]
  +1112  mov	w20, #0xffff
  +1116  b	__image+0x3494
  +1120  ldrsh	w8, [x21, #0x1e]
  +1124  cmn	w8, #0x1
  +1128  cset	w8, eq
  +1132  cmp	w8, #0x0
  +1136  csel	x25, x21, xzr, ne
  +1140  add	x8, x19, #0x1
  +1144  and	x19, x8, x28
  +1148  add	x24, x24, #0x1
  +1152  ldr	x8, [x22, #0x20]
  +1156  cmp	x24, x8
  +1160  b.hs	__image+0x3758
  +1164  ldr	x8, [x22, #0x18]
  +1168  ldr	w9, [x22, #0x38]
  +1172  cmp	w9, #0x0
  +1176  mov	w9, #0x30
  +1180  mov	w10, #0x20
  +1184  csel	x9, x10, x9, eq
  +1188  madd	x21, x9, x19, x8
  +1192  ldr	x8, [x21]
  +1196  ldr	x9, [sp, #0x18]
  +1200  eor	x8, x8, x9
  +1204  mov	x9, #-__image+0x101010001010102
  +1208  movk	x9, #0xfeff
  +1212  add	x9, x8, x9
  +1216  bic	x8, x9, x8
  +1220  ands	x26, x8, #__image+0x8080807f80808080
  +1224  b.eq	__image+0x35a8
  +1228  add	x23, x21, #0x10
  +1232  b	__image+0x34f0
  +1236  ldr	x8, [x22, #0x40]
  +1240  cbz	x8, __image+0x3784
  +1244  sub	x8, x26, #0x1
  +1248  ands	x26, x8, x26
  +1252  b.eq	__image+0x35a8
  +1256  rbit	x8, x26
  +1260  clz	x8, x8
  +1264  ldr	x9, [x21]
  +1268  and	x10, x8, #0x38
  +1272  lsr	x9, x9, x10
  +1276  cmp	w27, w9, uxtb
  +1280  b.ne	__image+0x34e4
  +1284  lsr	x8, x8, #3
  +1288  ldr	w9, [x22, #0x38]
  +1292  cbz	w9, __image+0x3528
  +1296  ldr	w8, [x23, x8, lsl #2]
  +1300  cmn	w8, #0x1
  +1304  b.ne	__image+0x3534
  +1308  b	__image+0x34e4
  +1312  ldrh	w8, [x23, x8, lsl #1]
  +1316  cmp	w8, w20
  +1320  b.eq	__image+0x34e4
  +1324  ldr	w9, [x22, #0x54]
  +1328  cmp	w8, w9
  +1332  b.hs	__image+0x34dc
  +1336  ldr	x9, [x22, #0x48]
  +1340  ldr	x0, [x9, w8, uxtw #3]
  +1344  and	x9, x0, #0x1
  +1348  cmp	x0, #0x0
  +1352  ccmp	x9, #0x0, #0x0, ne
  +1356  b.ne	__image+0x34dc
  +1360  ldr	w9, [x0, #0x30]
  +1364  cmp	w9, w8
  +1368  b.ne	__image+0x379c
  +1372  ldr	x8, [x22, #0x40]
  +1376  cbz	x8, __image+0x3590
  +1380  ldr	x9, [sp, #0x10]
  +1384  cmp	x9, x8
  +1388  cset	w9, eq
  +1392  ldrh	w10, [x0, #0x16]
  +1396  ldrh	w8, [x8, #0x2c]
  +1400  cmp	w10, w8
  +1404  cset	w8, ne
  +1408  cmp	w9, w8
  +1412  b.eq	__image+0x34e4
  +1416  ldp	x4, x1, [sp, #0x30]
  +1420  ldp	x2, x3, [sp, #0x20]
  +1424  mov	x5, #0x0
  +1428  bl	_zbtScoreLeafFindMember
  +1432  cbz	w0, __image+0x34e4
  +1436  b	__image+0x377c
  +1440  cbnz	x24, __image+0x35e8
  +1444  ldr	w8, [x22, #0x20]
  +1448  sub	w8, w8, #0x1
  +1452  ldr	x9, [sp, #0x8]
  +1456  and	x8, x8, x9
  +1460  ldr	x9, [x22, #0x18]
  +1464  ldr	w10, [x22, #0x38]
  +1468  cmp	w10, #0x0
  +1472  mov	w10, #0x30
  +1476  mov	w11, #0x20
  +1480  csel	x10, x11, x10, eq
  +1484  umaddl	x8, w10, w8, x9
  +1488  ldr	x8, [x8, #0x8]
  +1492  ldr	x9, [sp]
  +1496  bics	xzr, x9, x8
  +1500  b.ne	__image+0x3758
  +1504  ldr	x8, [x21]
  +1508  tst	x8, #0xff
  +1512  b.eq	__image+0x3758
  +1516  cbnz	x25, __image+0x361c
  +1520  ldr	w9, [x22, #0x38]
  +1524  cbz	w9, __image+0x3608
  +1528  ldr	w9, [x21, #0x10]
  +1532  b	__image+0x360c
  +1536  ldrsh	w9, [x21, #0x10]
  +1540  cmn	w9, #0x1
  +1544  cset	w9, eq
  +1548  cmp	w9, #0x0
  +1552  csel	x25, x21, xzr, ne
  +1556  tst	x8, #0xff00
  +1560  b.eq	__image+0x3758
  +1564  cbnz	x25, __image+0x364c
  +1568  ldr	w9, [x22, #0x38]
  +1572  cbz	w9, __image+0x3638
  +1576  ldr	w9, [x21, #0x14]
  +1580  b	__image+0x363c
  +1584  ldrsh	w9, [x21, #0x12]
  +1588  cmn	w9, #0x1
  +1592  cset	w9, eq
  +1596  cmp	w9, #0x0
  +1600  csel	x25, x21, xzr, ne
  +1604  tst	x8, #0xff0000
  +1608  b.eq	__image+0x3758
  +1612  cbnz	x25, __image+0x367c
  +1616  ldr	w9, [x22, #0x38]
  +1620  cbz	w9, __image+0x3668
  +1624  ldr	w9, [x21, #0x18]
  +1628  b	__image+0x366c
  +1632  ldrsh	w9, [x21, #0x14]
  +1636  cmn	w9, #0x1
  +1640  cset	w9, eq
  +1644  cmp	w9, #0x0
  +1648  csel	x25, x21, xzr, ne
  +1652  tst	x8, #0xff000000
  +1656  b.eq	__image+0x3758
  +1660  cbnz	x25, __image+0x36ac
  +1664  ldr	w9, [x22, #0x38]
  +1668  cbz	w9, __image+0x3698
  +1672  ldr	w9, [x21, #0x1c]
  +1676  b	__image+0x369c
  +1680  ldrsh	w9, [x21, #0x16]
  +1684  cmn	w9, #0x1
  +1688  cset	w9, eq
  +1692  cmp	w9, #0x0
  +1696  csel	x25, x21, xzr, ne
  +1700  tst	x8, #__image+0xfe00000000
  +1704  b.eq	__image+0x3758
  +1708  cbnz	x25, __image+0x36dc
  +1712  ldr	w9, [x22, #0x38]
  +1716  cbz	w9, __image+0x36c8
  +1720  ldr	w9, [x21, #0x20]
  +1724  b	__image+0x36cc
  +1728  ldrsh	w9, [x21, #0x18]
  +1732  cmn	w9, #0x1
  +1736  cset	w9, eq
  +1740  cmp	w9, #0x0
  +1744  csel	x25, x21, xzr, ne
  +1748  tst	x8, #__image+0xfeff00000000
  +1752  b.eq	__image+0x3758
  +1756  cbnz	x25, __image+0x370c
  +1760  ldr	w9, [x22, #0x38]
  +1764  cbz	w9, __image+0x36f8
  +1768  ldr	w9, [x21, #0x24]
  +1772  b	__image+0x36fc
  +1776  ldrsh	w9, [x21, #0x1a]
  +1780  cmn	w9, #0x1
  +1784  cset	w9, eq
  +1788  cmp	w9, #0x0
  +1792  csel	x25, x21, xzr, ne
  +1796  tst	x8, #__image+0xfeffff00000000
  +1800  b.eq	__image+0x3758
  +1804  cbnz	x25, __image+0x373c
  +1808  ldr	w9, [x22, #0x38]
  +1812  cbz	w9, __image+0x3728
  +1816  ldr	w9, [x21, #0x28]
  +1820  b	__image+0x372c
  +1824  ldrsh	w9, [x21, #0x1c]
  +1828  cmn	w9, #0x1
  +1832  cset	w9, eq
  +1836  cmp	w9, #0x0
  +1840  csel	x25, x21, xzr, ne
  +1844  lsr	x8, x8, #56
  +1848  cbz	x8, __image+0x3758
  +1852  cbnz	x25, __image+0x347c
  +1856  ldr	w8, [x22, #0x38]
  +1860  cbz	w8, __image+0x3468
  +1864  ldr	w8, [x21, #0x2c]
  +1868  b	__image+0x346c
  +1872  mov	w0, #0x0
  +1876  ldp	x29, x30, [sp, #0x90]
  +1880  ldp	x20, x19, [sp, #0x80]
  +1884  ldp	x22, x21, [sp, #0x70]
  +1888  ldp	x24, x23, [sp, #0x60]
  +1892  ldp	x26, x25, [sp, #0x50]
  +1896  ldp	x28, x27, [sp, #0x40]
  +1900  add	sp, sp, #0xa0
  +1904  ret
  +1908  mov	w0, #0x1
  +1912  b	__image+0x375c
  +1916  adrp	x0, 15 ; __image+0x12000
  +1920  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +1924  adrp	x2, 15 ; __image+0x12000
  +1928  add	x2, x2, #0xe24 ; literal pool for: "zs->member_rehash && table == &zs->member_index"
  +1932  mov	w1, #0x7a1
  +1936  bl	_standalone_panic
  +1940  adrp	x0, 15 ; __image+0x12000
  +1944  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +1948  adrp	x2, 15 ; __image+0x12000
  +1952  add	x2, x2, #0xe05 ; literal pool for: "leaf->id == id"
  +1956  mov	w1, #0x7a5
  +1960  bl	_standalone_panic

_zbtScoreLeafFindMember:
  +0000  sub	sp, sp, #0x90
  +0004  stp	x28, x27, [sp, #0x30]
  +0008  stp	x26, x25, [sp, #0x40]
  +0012  stp	x24, x23, [sp, #0x50]
  +0016  stp	x22, x21, [sp, #0x60]
  +0020  stp	x20, x19, [sp, #0x70]
  +0024  stp	x29, x30, [sp, #0x80]
  +0028  add	x29, sp, #0x80
  +0032  mov	x21, x3
  +0036  mov	x22, x2
  +0040  mov	x23, x1
  +0044  mov	x20, x0
  +0048  ldrb	w10, [x0, #0x34]
  +0052  cbz	w10, __image+0xb420
  +0056  ldrb	w11, [x20, #0x11]
  +0060  mov	w8, #0x7
  +0064  madd	w8, w11, w10, w8
  +0068  lsr	w8, w8, #3
  +0072  add	w8, w8, #0x9
  +0076  and	x8, x8, #0x7ffe
  +0080  add	x9, x20, x8
  +0084  add	x19, x9, #0x38
  +0088  cbnz	x11, __image+0xb430
  +0092  b	__image+0xb4f0
  +0096  mov	x8, #0x0
  +0100  add	x19, x20, #0x38
  +0104  ldrb	w11, [x20, #0x11]
  +0108  cbz	x11, __image+0xb4f0
  +0112  stp	x5, x4, [sp, #0x20]
  +0116  lsr	w24, w23, #24
  +0120  add	x9, x20, #0x38
  +0124  stp	x9, x10, [sp, #0x8]
  +0128  add	x8, x9, x8
  +0132  add	x28, x8, x11, lsl #1
  +0136  str	x11, [sp, #0x18]
  +0140  add	x26, x28, x11
  +0144  mov	x0, x28
  +0148  b	__image+0xb474
  +0152  mov	x1, x22
  +0156  mov	x2, x21
  +0160  bl	__image+0x12374 ; symbol stub for: _memcmp
  +0164  cbz	w0, __image+0xb514
  +0168  add	x0, x25, #0x1
  +0172  cmp	x0, x26
  +0176  b.hs	__image+0xb4f0
  +0180  sub	x2, x26, x0
  +0184  mov	x1, x24
  +0188  bl	__image+0x12368 ; symbol stub for: _memchr
  +0192  cbz	x0, __image+0xb4f4
  +0196  mov	x25, x0
  +0200  sub	x27, x0, x28
  +0204  ldrh	w8, [x19, w27, uxtw #1]
  +0208  add	x9, x20, x8
  +0212  ldrb	w8, [x9]
  +0216  cmp	w8, #0xfe
  +0220  b.eq	__image+0xb4cc
  +0224  cmp	w8, #0xff
  +0228  b.ne	__image+0xb4e0
  +0232  ldur	w8, [x9, #0x1]
  +0236  cmp	w8, w23
  +0240  b.ne	__image+0xb468
  +0244  ldur	x0, [x9, #0xd]
  +0248  cbz	x0, __image+0xb5e0
  +0252  ldur	x8, [x9, #0x5]
  +0256  cmp	x8, x21
  +0260  b.ne	__image+0xb468
  +0264  b	__image+0xb458
  +0268  ldurh	w8, [x9, #0x1]
  +0272  add	x0, x9, #0x3
  +0276  cmp	x8, x21
  +0280  b.eq	__image+0xb458
  +0284  b	__image+0xb468
  +0288  add	x0, x9, #0x1
  +0292  cmp	x8, x21
  +0296  b.ne	__image+0xb468
  +0300  b	__image+0xb458
  +0304  mov	w0, #0x0
  +0308  ldp	x29, x30, [sp, #0x80]
  +0312  ldp	x20, x19, [sp, #0x70]
  +0316  ldp	x22, x21, [sp, #0x60]
  +0320  ldp	x24, x23, [sp, #0x50]
  +0324  ldp	x26, x25, [sp, #0x40]
  +0328  ldp	x28, x27, [sp, #0x30]
  +0332  add	sp, sp, #0x90
  +0336  ret
  +0340  ldrb	w10, [x20, #0x35]
  +0344  mvn	w8, w27
  +0348  ldp	x12, x15, [sp, #0x18]
  +0352  add	w8, w8, w12
  +0356  cmp	w10, #0x0
  +0360  csel	w8, w27, w8, eq
  +0364  ldr	x9, [sp, #0x28]
  +0368  cbz	x9, __image+0xb5d0
  +0372  ldr	x16, [sp, #0x10]
  +0376  cbz	w16, __image+0xb5ac
  +0380  mvn	w11, w8
  +0384  add	w11, w11, w12
  +0388  cmp	w10, #0x0
  +0392  csel	w11, w27, w11, eq
  +0396  umull	x13, w16, w11
  +0400  lsr	x12, x13, #3
  +0404  ldr	x17, [sp, #0x8]
  +0408  ldr	x11, [x17, x12]
  +0412  and	x14, x13, #0x7
  +0416  lsr	x11, x11, x14
  +0420  ands	w13, w13, #0x7
  +0424  b.eq	__image+0xb58c
  +0428  mov	w14, #0x40
  +0432  sub	w13, w14, w13
  +0436  cmp	w13, w16
  +0440  b.hs	__image+0xb58c
  +0444  add	x12, x12, x17
  +0448  ldrb	w12, [x12, #0x8]
  +0452  lsl	x12, x12, x13
  +0456  orr	x11, x12, x11
  +0460  mov	x12, #-0x1
  +0464  lsl	x13, x12, x16
  +0468  cmp	w16, #0x40
  +0472  csinv	x12, x12, x13, hs
  +0476  and	x11, x11, x12
  +0480  ldrb	w12, [x20, #0x13]
  +0484  lsl	x11, x11, x12
  +0488  b	__image+0xb5b0
  +0492  mov	x11, #0x0
  +0496  ldr	x12, [x20, #0x28]
  +0500  cmp	w10, #0x0
  +0504  cneg	x10, x11, ne
  +0508  add	x10, x12, x10
  +0512  and	x11, x10, #__image+0x7ffffffeffffffff
  +0516  cmp	x10, #0x0
  +0520  csinv	x10, x11, x10, lt
  +0524  str	x10, [x9]
  +0528  cbz	x15, __image+0xb5d8
  +0532  str	w8, [x15]
  +0536  mov	w0, #0x1
  +0540  b	__image+0xb4f4
  +0544  adrp	x0, 7 ; __image+0x12000
  +0548  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +0552  adrp	x2, 7 ; __image+0x12000
  +0556  add	x2, x2, #0xe54 ; literal pool for: "ptr != NULL"
  +0560  mov	w1, #0x257
  +0564  bl	_standalone_panic

_zbtreeRank:
  +0000  sub	sp, sp, #0xc0
  +0004  stp	x28, x27, [sp, #0x60]
  +0008  stp	x26, x25, [sp, #0x70]
  +0012  stp	x24, x23, [sp, #0x80]
  +0016  stp	x22, x21, [sp, #0x90]
  +0020  stp	x20, x19, [sp, #0xa0]
  +0024  stp	x29, x30, [sp, #0xb0]
  +0028  add	x29, sp, #0xb0
  +0032  str	x3, [sp, #0x40]
  +0036  mov	x20, x2
  +0040  mov	x21, x1
  +0044  mov	x19, x0
  +0048  mov	x1, #0x0
  +0052  ldurb	w9, [x21, #-0x1]
  +0056  and	w8, w9, #0x7
  +0060  cmp	w8, #0x1
  +0064  b.le	__image+0x50cc
  +0068  cmp	w8, #0x2
  +0072  b.eq	__image+0x50e0
  +0076  cmp	w8, #0x3
  +0080  b.eq	__image+0x50e8
  +0084  cmp	w8, #0x4
  +0088  b.ne	__image+0x50f4
  +0092  ldur	x1, [x21, #-0x11]
  +0096  b	__image+0x50f4
  +0100  cbz	w8, __image+0x50f0
  +0104  cmp	w8, #0x1
  +0108  b.ne	__image+0x50f4
  +0112  ldurb	w1, [x21, #-0x3]
  +0116  b	__image+0x50f4
  +0120  ldurh	w1, [x21, #-0x5]
  +0124  b	__image+0x50f4
  +0128  ldur	w1, [x21, #-0x9]
  +0132  b	__image+0x50f4
  +0136  lsr	x1, x9, #3
  +0140  mov	x0, x21
  +0144  bl	_dictGenHashFunction
  +0148  stp	xzr, x0, [sp, #0x48]
  +0152  ldurb	w9, [x21, #-0x1]
  +0156  and	w8, w9, #0x7
  +0160  cmp	w8, #0x1
  +0164  str	w20, [sp, #0xc]
  +0168  b.le	__image+0x5134
  +0172  cmp	w8, #0x2
  +0176  b.eq	__image+0x5148
  +0180  cmp	w8, #0x3
  +0184  b.eq	__image+0x5150
  +0188  cmp	w8, #0x4
  +0192  b.ne	__image+0x5160
  +0196  ldur	x8, [x21, #-0x11]
  +0200  b	__image+0x515c
  +0204  cbz	w8, __image+0x5158
  +0208  cmp	w8, #0x1
  +0212  b.ne	__image+0x5160
  +0216  ldurb	w8, [x21, #-0x3]
  +0220  b	__image+0x515c
  +0224  ldurh	w8, [x21, #-0x5]
  +0228  b	__image+0x515c
  +0232  ldur	w8, [x21, #-0x9]
  +0236  b	__image+0x515c
  +0240  lsr	x8, x9, #3
  +0244  str	x8, [sp, #0x48]
  +0248  str	x21, [sp, #0x38]
  +0252  ldr	x8, [x19, #0x40]
  +0256  cbz	x8, __image+0x5514
  +0260  mov	x0, x19
  +0264  mov	w1, #0x1
  +0268  bl	_zbtIndexRehashStep
  +0272  ldr	x26, [x19, #0x40]
  +0276  cbz	x26, __image+0x5514
  +0280  ldr	x8, [x26, #0x8]
  +0284  cbz	x8, __image+0x5514
  +0288  mov	x23, #0x0
  +0292  mov	x14, #0x0
  +0296  mov	w9, #0x1000000
  +0300  ldr	x10, [sp, #0x50]
  +0304  cmp	w10, w9
  +0308  csel	w9, w10, w9, hi
  +0312  lsr	w20, w9, #24
  +0316  sub	x8, x8, #0x1
  +0320  mov	w9, w10
  +0324  stp	x9, x8, [sp, #0x18]
  +0328  and	x12, x8, x9
  +0332  mov	x8, #__image+0x101010001010101
  +0336  mul	x8, x20, x8
  +0340  str	x8, [sp, #0x28]
  +0344  add	x27, x19, #0x18
  +0348  mov	x8, #0x7c15
  +0352  movk	x8, #0x7f4a, lsl #16
  +0356  movk	x8, #0x79b9, lsl #32
  +0360  movk	x8, #0x9e37, lsl #48
  +0364  mul	x8, x20, x8
  +0368  mov	w9, #0x1
  +0372  lsl	x10, x9, x20
  +0376  lsr	x11, x8, #58
  +0380  lsl	x11, x9, x11
  +0384  orr	x10, x11, x10
  +0388  lsr	x8, x8, #36
  +0392  lsl	x8, x9, x8
  +0396  orr	x8, x10, x8
  +0400  str	x8, [sp, #0x10]
  +0404  mov	w15, #0xffff
  +0408  b	__image+0x5234
  +0412  ldr	w8, [x24, #0x2c]
  +0416  cmn	w8, #0x1
  +0420  cset	w8, eq
  +0424  cmp	w8, #0x0
  +0428  csel	x23, x24, xzr, ne
  +0432  add	x8, x21, #0x1
  +0436  ldr	x9, [sp, #0x20]
  +0440  and	x12, x8, x9
  +0444  add	x14, x14, #0x1
  +0448  ldr	x8, [x26, #0x8]
  +0452  cmp	x14, x8
  +0456  b.hs	__image+0x5514
  +0460  str	x14, [sp, #0x30]
  +0464  ldr	x8, [x26]
  +0468  ldr	w9, [x26, #0x20]
  +0472  cmp	w9, #0x0
  +0476  mov	w9, #0x30
  +0480  mov	w10, #0x20
  +0484  csel	x9, x10, x9, eq
  +0488  mov	x21, x12
  +0492  madd	x24, x9, x12, x8
  +0496  ldr	x8, [x24]
  +0500  ldr	x9, [sp, #0x28]
  +0504  eor	x8, x8, x9
  +0508  mov	x9, #-__image+0x101010001010102
  +0512  movk	x9, #0xfeff
  +0516  add	x9, x8, x9
  +0520  bic	x8, x9, x8
  +0524  ands	x28, x8, #__image+0x8080807f80808080
  +0528  b.eq	__image+0x5360
  +0532  add	x22, x24, #0x10
  +0536  b	__image+0x52ac
  +0540  sub	x5, x29, #0x54
  +0544  mov	x0, x25
  +0548  ldp	x3, x1, [sp, #0x48]
  +0552  ldp	x2, x4, [sp, #0x38]
  +0556  bl	_zbtScoreLeafFindMember
  +0560  mov	w15, #0xffff
  +0564  cbnz	w0, __image+0x58b8
  +0568  sub	x8, x28, #0x1
  +0572  ands	x28, x8, x28
  +0576  b.eq	__image+0x5360
  +0580  rbit	x8, x28
  +0584  clz	x8, x8
  +0588  ldr	x9, [x24]
  +0592  and	x10, x8, #0x38
  +0596  lsr	x9, x9, x10
  +0600  cmp	w20, w9, uxtb
  +0604  b.ne	__image+0x52a0
  +0608  lsr	x8, x8, #3
  +0612  ldr	w9, [x26, #0x20]
  +0616  cbz	w9, __image+0x52e4
  +0620  ldr	w8, [x22, x8, lsl #2]
  +0624  cmn	w8, #0x1
  +0628  b.ne	__image+0x52f0
  +0632  b	__image+0x52a0
  +0636  ldrh	w8, [x22, x8, lsl #1]
  +0640  cmp	w8, w15
  +0644  b.eq	__image+0x52a0
  +0648  ldr	w9, [x19, #0x54]
  +0652  cmp	w8, w9
  +0656  b.hs	__image+0x5314
  +0660  ldr	x9, [x19, #0x48]
  +0664  ldr	x25, [x9, w8, uxtw #3]
  +0668  and	x9, x25, #0x1
  +0672  cmp	x25, #0x0
  +0676  ccmp	x9, #0x0, #0x0, ne
  +0680  b.eq	__image+0x5328
  +0684  ldr	x8, [x19, #0x40]
  +0688  cbz	x8, __image+0x5988
  +0692  cmp	x26, x27
  +0696  b.eq	__image+0x52a0
  +0700  b	__image+0x5988
  +0704  ldr	w9, [x25, #0x30]
  +0708  cmp	w9, w8
  +0712  b.ne	__image+0x59a0
  +0716  ldr	x8, [x19, #0x40]
  +0720  cbz	x8, __image+0x5284
  +0724  cmp	x26, x8
  +0728  cset	w9, eq
  +0732  ldrh	w10, [x25, #0x16]
  +0736  ldrh	w8, [x8, #0x2c]
  +0740  cmp	w10, w8
  +0744  cset	w8, ne
  +0748  cmp	w9, w8
  +0752  b.ne	__image+0x5284
  +0756  b	__image+0x52a0
  +0760  ldr	x14, [sp, #0x30]
  +0764  cbnz	x14, __image+0x53a4
  +0768  ldr	w8, [x26, #0x8]
  +0772  sub	w8, w8, #0x1
  +0776  ldr	x9, [sp, #0x18]
  +0780  and	x8, x8, x9
  +0784  ldr	x9, [x26]
  +0788  ldr	w10, [x26, #0x20]
  +0792  cmp	w10, #0x0
  +0796  mov	w10, #0x30
  +0800  mov	w12, #0x20
  +0804  csel	x10, x12, x10, eq
  +0808  umaddl	x8, w10, w8, x9
  +0812  ldr	x8, [x8, #0x8]
  +0816  ldr	x9, [sp, #0x10]
  +0820  bics	xzr, x9, x8
  +0824  b.ne	__image+0x5514
  +0828  ldr	x8, [x24]
  +0832  tst	x8, #0xff
  +0836  b.eq	__image+0x5514
  +0840  cbnz	x23, __image+0x53d8
  +0844  ldr	w9, [x26, #0x20]
  +0848  cbz	w9, __image+0x53c4
  +0852  ldr	w9, [x24, #0x10]
  +0856  b	__image+0x53c8
  +0860  ldrsh	w9, [x24, #0x10]
  +0864  cmn	w9, #0x1
  +0868  cset	w9, eq
  +0872  cmp	w9, #0x0
  +0876  csel	x23, x24, xzr, ne
  +0880  tst	x8, #0xff00
  +0884  b.eq	__image+0x5514
  +0888  cbnz	x23, __image+0x5408
  +0892  ldr	w9, [x26, #0x20]
  +0896  cbz	w9, __image+0x53f4
  +0900  ldr	w9, [x24, #0x14]
  +0904  b	__image+0x53f8
  +0908  ldrsh	w9, [x24, #0x12]
  +0912  cmn	w9, #0x1
  +0916  cset	w9, eq
  +0920  cmp	w9, #0x0
  +0924  csel	x23, x24, xzr, ne
  +0928  tst	x8, #0xff0000
  +0932  b.eq	__image+0x5514
  +0936  cbnz	x23, __image+0x5438
  +0940  ldr	w9, [x26, #0x20]
  +0944  cbz	w9, __image+0x5424
  +0948  ldr	w9, [x24, #0x18]
  +0952  b	__image+0x5428
  +0956  ldrsh	w9, [x24, #0x14]
  +0960  cmn	w9, #0x1
  +0964  cset	w9, eq
  +0968  cmp	w9, #0x0
  +0972  csel	x23, x24, xzr, ne
  +0976  tst	x8, #0xff000000
  +0980  b.eq	__image+0x5514
  +0984  cbnz	x23, __image+0x5468
  +0988  ldr	w9, [x26, #0x20]
  +0992  cbz	w9, __image+0x5454
  +0996  ldr	w9, [x24, #0x1c]
  +1000  b	__image+0x5458
  +1004  ldrsh	w9, [x24, #0x16]
  +1008  cmn	w9, #0x1
  +1012  cset	w9, eq
  +1016  cmp	w9, #0x0
  +1020  csel	x23, x24, xzr, ne
  +1024  tst	x8, #__image+0xfe00000000
  +1028  b.eq	__image+0x5514
  +1032  cbnz	x23, __image+0x5498
  +1036  ldr	w9, [x26, #0x20]
  +1040  cbz	w9, __image+0x5484
  +1044  ldr	w9, [x24, #0x20]
  +1048  b	__image+0x5488
  +1052  ldrsh	w9, [x24, #0x18]
  +1056  cmn	w9, #0x1
  +1060  cset	w9, eq
  +1064  cmp	w9, #0x0
  +1068  csel	x23, x24, xzr, ne
  +1072  tst	x8, #__image+0xfeff00000000
  +1076  b.eq	__image+0x5514
  +1080  cbnz	x23, __image+0x54c8
  +1084  ldr	w9, [x26, #0x20]
  +1088  cbz	w9, __image+0x54b4
  +1092  ldr	w9, [x24, #0x24]
  +1096  b	__image+0x54b8
  +1100  ldrsh	w9, [x24, #0x1a]
  +1104  cmn	w9, #0x1
  +1108  cset	w9, eq
  +1112  cmp	w9, #0x0
  +1116  csel	x23, x24, xzr, ne
  +1120  tst	x8, #__image+0xfeffff00000000
  +1124  b.eq	__image+0x5514
  +1128  cbnz	x23, __image+0x54f8
  +1132  ldr	w9, [x26, #0x20]
  +1136  cbz	w9, __image+0x54e4
  +1140  ldr	w9, [x24, #0x28]
  +1144  b	__image+0x54e8
  +1148  ldrsh	w9, [x24, #0x1c]
  +1152  cmn	w9, #0x1
  +1156  cset	w9, eq
  +1160  cmp	w9, #0x0
  +1164  csel	x23, x24, xzr, ne
  +1168  lsr	x8, x8, #56
  +1172  cbz	x8, __image+0x5514
  +1176  cbnz	x23, __image+0x5218
  +1180  ldr	w8, [x26, #0x20]
  +1184  cbnz	w8, __image+0x5204
  +1188  ldrsh	w8, [x24, #0x1e]
  +1192  b	__image+0x5208
  +1196  ldr	x8, [x19, #0x20]
  +1200  cbz	x8, __image+0x5894
  +1204  mov	x23, #0x0
  +1208  mov	x20, #0x0
  +1212  add	x11, x19, #0x18
  +1216  mov	w9, #0x1000000
  +1220  ldr	x10, [sp, #0x50]
  +1224  cmp	w10, w9
  +1228  csel	w9, w10, w9, hi
  +1232  lsr	w27, w9, #24
  +1236  sub	x8, x8, #0x1
  +1240  mov	w9, w10
  +1244  stp	x8, x11, [sp, #0x20]
  +1248  str	x9, [sp, #0x18]
  +1252  and	x21, x8, x9
  +1256  mov	x8, #__image+0x101010001010101
  +1260  mul	x8, x27, x8
  +1264  str	x8, [sp, #0x30]
  +1268  mov	x8, #0x7c15
  +1272  movk	x8, #0x7f4a, lsl #16
  +1276  movk	x8, #0x79b9, lsl #32
  +1280  movk	x8, #0x9e37, lsl #48
  +1284  mul	x8, x27, x8
  +1288  mov	w9, #0x1
  +1292  lsl	x10, x9, x27
  +1296  lsr	x11, x8, #58
  +1300  lsl	x11, x9, x11
  +1304  orr	x10, x11, x10
  +1308  lsr	x8, x8, #36
  +1312  lsl	x8, x9, x8
  +1316  orr	x8, x10, x8
  +1320  str	x8, [sp, #0x10]
  +1324  mov	w26, #0xffff
  +1328  b	__image+0x55cc
  +1332  ldrsh	w8, [x24, #0x1e]
  +1336  cmn	w8, #0x1
  +1340  cset	w8, eq
  +1344  cmp	w8, #0x0
  +1348  csel	x23, x24, xzr, ne
  +1352  add	x8, x21, #0x1
  +1356  ldr	x9, [sp, #0x20]
  +1360  and	x21, x8, x9
  +1364  add	x20, x20, #0x1
  +1368  ldr	x8, [x19, #0x20]
  +1372  cmp	x20, x8
  +1376  b.hs	__image+0x5894
  +1380  ldr	x8, [x19, #0x18]
  +1384  ldr	w9, [x19, #0x38]
  +1388  cmp	w9, #0x0
  +1392  mov	w9, #0x30
  +1396  mov	w10, #0x20
  +1400  csel	x9, x10, x9, eq
  +1404  madd	x24, x9, x21, x8
  +1408  ldr	x8, [x24]
  +1412  ldr	x9, [sp, #0x30]
  +1416  eor	x8, x8, x9
  +1420  mov	x9, #-__image+0x101010001010102
  +1424  movk	x9, #0xfeff
  +1428  add	x9, x8, x9
  +1432  bic	x8, x9, x8
  +1436  ands	x28, x8, #__image+0x8080807f80808080
  +1440  b.eq	__image+0x56e4
  +1444  add	x22, x24, #0x10
  +1448  b	__image+0x5628
  +1452  ldr	x8, [x19, #0x40]
  +1456  cbz	x8, __image+0x5988
  +1460  sub	x8, x28, #0x1
  +1464  ands	x28, x8, x28
  +1468  b.eq	__image+0x56e4
  +1472  rbit	x8, x28
  +1476  clz	x8, x8
  +1480  ldr	x9, [x24]
  +1484  and	x10, x8, #0x38
  +1488  lsr	x9, x9, x10
  +1492  cmp	w27, w9, uxtb
  +1496  b.ne	__image+0x561c
  +1500  lsr	x8, x8, #3
  +1504  ldr	w9, [x19, #0x38]
  +1508  cbz	w9, __image+0x5660
  +1512  ldr	w8, [x22, x8, lsl #2]
  +1516  cmn	w8, #0x1
  +1520  b.ne	__image+0x566c
  +1524  b	__image+0x561c
  +1528  ldrh	w8, [x22, x8, lsl #1]
  +1532  cmp	w8, w26
  +1536  b.eq	__image+0x561c
  +1540  ldr	w9, [x19, #0x54]
  +1544  cmp	w8, w9
  +1548  b.hs	__image+0x5614
  +1552  ldr	x9, [x19, #0x48]
  +1556  ldr	x25, [x9, w8, uxtw #3]
  +1560  and	x9, x25, #0x1
  +1564  cmp	x25, #0x0
  +1568  ccmp	x9, #0x0, #0x0, ne
  +1572  b.ne	__image+0x5614
  +1576  ldr	w9, [x25, #0x30]
  +1580  cmp	w9, w8
  +1584  b.ne	__image+0x59a0
  +1588  ldr	x8, [x19, #0x40]
  +1592  cbz	x8, __image+0x56c8
  +1596  ldr	x9, [sp, #0x28]
  +1600  cmp	x9, x8
  +1604  cset	w9, eq
  +1608  ldrh	w10, [x25, #0x16]
  +1612  ldrh	w8, [x8, #0x2c]
  +1616  cmp	w10, w8
  +1620  cset	w8, ne
  +1624  cmp	w9, w8
  +1628  b.eq	__image+0x561c
  +1632  sub	x5, x29, #0x54
  +1636  mov	x0, x25
  +1640  ldp	x3, x1, [sp, #0x48]
  +1644  ldp	x2, x4, [sp, #0x38]
  +1648  bl	_zbtScoreLeafFindMember
  +1652  cbz	w0, __image+0x561c
  +1656  b	__image+0x58b8
  +1660  cbnz	x20, __image+0x5724
  +1664  ldr	w8, [x19, #0x20]
  +1668  sub	w8, w8, #0x1
  +1672  ldr	x9, [sp, #0x18]
  +1676  and	x8, x8, x9
  +1680  ldr	x9, [x19, #0x18]
  +1684  ldr	w10, [x19, #0x38]
  +1688  cmp	w10, #0x0
  +1692  mov	w10, #0x30
  +1696  mov	w11, #0x20
  +1700  csel	x10, x11, x10, eq
  +1704  umaddl	x8, w10, w8, x9
  +1708  ldr	x8, [x8, #0x8]
  +1712  ldr	x9, [sp, #0x10]
  +1716  bics	xzr, x9, x8
  +1720  b.ne	__image+0x5894
  +1724  ldr	x8, [x24]
  +1728  tst	x8, #0xff
  +1732  b.eq	__image+0x5894
  +1736  cbnz	x23, __image+0x5758
  +1740  ldr	w9, [x19, #0x38]
  +1744  cbz	w9, __image+0x5744
  +1748  ldr	w9, [x24, #0x10]
  +1752  b	__image+0x5748
  +1756  ldrsh	w9, [x24, #0x10]
  +1760  cmn	w9, #0x1
  +1764  cset	w9, eq
  +1768  cmp	w9, #0x0
  +1772  csel	x23, x24, xzr, ne
  +1776  tst	x8, #0xff00
  +1780  b.eq	__image+0x5894
  +1784  cbnz	x23, __image+0x5788
  +1788  ldr	w9, [x19, #0x38]
  +1792  cbz	w9, __image+0x5774
  +1796  ldr	w9, [x24, #0x14]
  +1800  b	__image+0x5778
  +1804  ldrsh	w9, [x24, #0x12]
  +1808  cmn	w9, #0x1
  +1812  cset	w9, eq
  +1816  cmp	w9, #0x0
  +1820  csel	x23, x24, xzr, ne
  +1824  tst	x8, #0xff0000
  +1828  b.eq	__image+0x5894
  +1832  cbnz	x23, __image+0x57b8
  +1836  ldr	w9, [x19, #0x38]
  +1840  cbz	w9, __image+0x57a4
  +1844  ldr	w9, [x24, #0x18]
  +1848  b	__image+0x57a8
  +1852  ldrsh	w9, [x24, #0x14]
  +1856  cmn	w9, #0x1
  +1860  cset	w9, eq
  +1864  cmp	w9, #0x0
  +1868  csel	x23, x24, xzr, ne
  +1872  tst	x8, #0xff000000
  +1876  b.eq	__image+0x5894
  +1880  cbnz	x23, __image+0x57e8
  +1884  ldr	w9, [x19, #0x38]
  +1888  cbz	w9, __image+0x57d4
  +1892  ldr	w9, [x24, #0x1c]
  +1896  b	__image+0x57d8
  +1900  ldrsh	w9, [x24, #0x16]
  +1904  cmn	w9, #0x1
  +1908  cset	w9, eq
  +1912  cmp	w9, #0x0
  +1916  csel	x23, x24, xzr, ne
  +1920  tst	x8, #__image+0xfe00000000
  +1924  b.eq	__image+0x5894
  +1928  cbnz	x23, __image+0x5818
  +1932  ldr	w9, [x19, #0x38]
  +1936  cbz	w9, __image+0x5804
  +1940  ldr	w9, [x24, #0x20]
  +1944  b	__image+0x5808
  +1948  ldrsh	w9, [x24, #0x18]
  +1952  cmn	w9, #0x1
  +1956  cset	w9, eq
  +1960  cmp	w9, #0x0
  +1964  csel	x23, x24, xzr, ne
  +1968  tst	x8, #__image+0xfeff00000000
  +1972  b.eq	__image+0x5894
  +1976  cbnz	x23, __image+0x5848
  +1980  ldr	w9, [x19, #0x38]
  +1984  cbz	w9, __image+0x5834
  +1988  ldr	w9, [x24, #0x24]
  +1992  b	__image+0x5838
  +1996  ldrsh	w9, [x24, #0x1a]
  +2000  cmn	w9, #0x1
  +2004  cset	w9, eq
  +2008  cmp	w9, #0x0
  +2012  csel	x23, x24, xzr, ne
  +2016  tst	x8, #__image+0xfeffff00000000
  +2020  b.eq	__image+0x5894
  +2024  cbnz	x23, __image+0x5878
  +2028  ldr	w9, [x19, #0x38]
  +2032  cbz	w9, __image+0x5864
  +2036  ldr	w9, [x24, #0x28]
  +2040  b	__image+0x5868
  +2044  ldrsh	w9, [x24, #0x1c]
  +2048  cmn	w9, #0x1
  +2052  cset	w9, eq
  +2056  cmp	w9, #0x0
  +2060  csel	x23, x24, xzr, ne
  +2064  lsr	x8, x8, #56
  +2068  cbz	x8, __image+0x5894
  +2072  cbnz	x23, __image+0x55b0
  +2076  ldr	w8, [x19, #0x38]
  +2080  cbz	w8, __image+0x559c
  +2084  ldr	w8, [x24, #0x2c]
  +2088  b	__image+0x55a0
  +2092  mov	x0, #-0x1
  +2096  ldp	x29, x30, [sp, #0xb0]
  +2100  ldp	x20, x19, [sp, #0xa0]
  +2104  ldp	x22, x21, [sp, #0x90]
  +2108  ldp	x24, x23, [sp, #0x80]
  +2112  ldp	x26, x25, [sp, #0x70]
  +2116  ldp	x28, x27, [sp, #0x60]
  +2120  add	sp, sp, #0xc0
  +2124  ret
  +2128  ldur	w0, [x29, #-0x54]
  +2132  ldr	x9, [x25]
  +2136  cbz	x9, __image+0x5970
  +2140  ldr	w12, [sp, #0xc]
  +2144  b	__image+0x58d4
  +2148  ldr	x9, [x25]
  +2152  cbz	x9, __image+0x5974
  +2156  ldrb	w8, [x25, #0x10]
  +2160  mov	x25, x9
  +2164  cbz	w8, __image+0x58cc
  +2168  cmp	w8, #0x8
  +2172  b.hs	__image+0x58f0
  +2176  mov	x9, #0x0
  +2180  b	__image+0x5950
  +2184  and	x9, x8, #0xf8
  +2188  movi.2d	v0, #0000000000000000
  +2192  movi.2d	v1, #0000000000000000
  +2196  mov.d	v1[0], x0
  +2200  add	x10, x25, #0x148
  +2204  mov	x11, x9
  +2208  movi.2d	v2, #0000000000000000
  +2212  movi.2d	v3, #0000000000000000
  +2216  ldp	q4, q5, [x10, #-0x30]
  +2220  ldp	q6, q7, [x10, #-0x10]
  +2224  add.2d	v1, v4, v1
  +2228  add.2d	v0, v5, v0
  +2232  add.2d	v2, v6, v2
  +2236  add.2d	v3, v7, v3
  +2240  add	x10, x10, #0x40
  +2244  subs	x11, x11, #0x8
  +2248  b.ne	__image+0x5910
  +2252  add.2d	v0, v0, v1
  +2256  add.2d	v0, v2, v0
  +2260  add.2d	v0, v3, v0
  +2264  addp.2d	d0, v0
  +2268  fmov	x0, d0
  +2272  cmp	x9, x8
  +2276  b.eq	__image+0x58cc
  +2280  sub	x8, x8, x9
  +2284  add	x9, x25, x9, lsl #3
  +2288  add	x9, x9, #0x118
  +2292  ldr	x10, [x9], #0x8
  +2296  add	x0, x10, x0
  +2300  subs	x8, x8, #0x1
  +2304  b.ne	__image+0x595c
  +2308  b	__image+0x58cc
  +2312  ldr	w12, [sp, #0xc]
  +2316  cbz	w12, __image+0x5898
  +2320  ldr	x8, [x19, #0x60]
  +2324  mvn	x9, x0
  +2328  add	x0, x8, x9
  +2332  b	__image+0x5898
  +2336  adrp	x0, 13 ; __image+0x12000
  +2340  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +2344  adrp	x2, 13 ; __image+0x12000
  +2348  add	x2, x2, #0xe24 ; literal pool for: "zs->member_rehash && table == &zs->member_index"
  +2352  mov	w1, #0x7a1
  +2356  bl	_standalone_panic
  +2360  adrp	x0, 13 ; __image+0x12000
  +2364  add	x0, x0, #0xcac ; literal pool for: "src/zset_btree.c"
  +2368  adrp	x2, 13 ; __image+0x12000
  +2372  add	x2, x2, #0xe05 ; literal pool for: "leaf->id == id"
  +2376  mov	w1, #0x7a5
  +2380  bl	_standalone_panic
