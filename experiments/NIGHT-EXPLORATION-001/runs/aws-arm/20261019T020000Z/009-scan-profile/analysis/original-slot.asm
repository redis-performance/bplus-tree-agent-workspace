0000000000010094 <zbtIndexScanSlot>:
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4166
{
   10094:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
   10098:	a9016ffc 	stp	x28, x27, [sp, #16]
   1009c:	a90267fa 	stp	x26, x25, [sp, #32]
   100a0:	a9035ff8 	stp	x24, x23, [sp, #48]
   100a4:	a90457f6 	stp	x22, x21, [sp, #64]
   100a8:	a9054ff4 	stp	x20, x19, [sp, #80]
   100ac:	910003fd 	mov	x29, sp
   100b0:	d10703ff 	sub	sp, sp, #0x1c0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   100b4:	f9400048 	ldr	x8, [x2]
   100b8:	531d706a 	lsl	w10, w3, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4168
    uint32_t id = zbtIndexGetId(table, bucket, slot_pos);
   100bc:	b9402029 	ldr	w9, [x1, #32]
   100c0:	aa0703f8 	mov	x24, x7
   100c4:	aa0503f3 	mov	x19, x5
   100c8:	aa0203f7 	mov	x23, x2
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   100cc:	9aca2515 	lsr	x21, x8, x10
   100d0:	aa0103fc 	mov	x28, x1
   100d4:	2a0303e8 	mov	w8, w3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1775
    if (table->wide_ids) return bucket->wide.id[pos];
   100d8:	340000e9 	cbz	w9, 100f4 <zbtIndexScanSlot+0x60>
   100dc:	8b080ae8 	add	x8, x23, x8, lsl #2
   100e0:	b9401108 	ldr	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   100e4:	f2401eb6 	ands	x22, x21, #0xff
   100e8:	aa1f03f9 	mov	x25, xzr
   100ec:	54000141 	b.ne	10114 <zbtIndexScanSlot+0x80>  // b.any
   100f0:	14000083 	b	102fc <zbtIndexScanSlot+0x268>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1776
    uint16_t id = bucket->narrow.id[pos];
   100f4:	8b0806e8 	add	x8, x23, x8, lsl #1
   100f8:	529fffea 	mov	w10, #0xffff                	// #65535
   100fc:	79402108 	ldrh	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1777
    return id == UINT16_MAX ? ZBT_INDEX_DELETED_ID : id;
   10100:	6b0a011f 	cmp	w8, w10
   10104:	5a9f1108 	csinv	w8, w8, wzr, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   10108:	f2401eb6 	ands	x22, x21, #0xff
   1010c:	aa1f03f9 	mov	x25, xzr
   10110:	54000f60 	b.eq	102fc <zbtIndexScanSlot+0x268>  // b.none
   10114:	3100051f 	cmn	w8, #0x1
   10118:	54000f20 	b.eq	102fc <zbtIndexScanSlot+0x268>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   1011c:	b4000473 	cbz	x19, 101a8 <zbtIndexScanSlot+0x114>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   10120:	eb13009f 	cmp	x4, x19
   10124:	aa0403ea 	mov	x10, x4
   10128:	540003c2 	b.cs	101a0 <zbtIndexScanSlot+0x10c>  // b.hs, b.nlast
   1012c:	d28f82aa 	mov	x10, #0x7c15                	// #31765
   10130:	7100013f 	cmp	w9, #0x0
   10134:	52800609 	mov	w9, #0x30                  	// #48
   10138:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
   1013c:	5280040b 	mov	w11, #0x20                  	// #32
   10140:	f940038c 	ldr	x12, [x28]
   10144:	f2cf372a 	movk	x10, #0x79b9, lsl #32
   10148:	9a890169 	csel	x9, x11, x9, eq	// eq = none
   1014c:	5280002d 	mov	w13, #0x1                   	// #1
   10150:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
   10154:	9b04312c 	madd	x12, x9, x4, x12
   10158:	9ad521ae 	lsl	x14, x13, x21
   1015c:	9b0a7eca 	mul	x10, x22, x10
   10160:	9100218c 	add	x12, x12, #0x8
   10164:	d37afd4b 	lsr	x11, x10, #58
   10168:	d364fd4a 	lsr	x10, x10, #36
   1016c:	9acb21ab 	lsl	x11, x13, x11
   10170:	9aca21aa 	lsl	x10, x13, x10
   10174:	aa0e016b 	orr	x11, x11, x14
   10178:	aa0a016b 	orr	x11, x11, x10
   1017c:	aa0403ea 	mov	x10, x4
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4174
            if ((*zbtIndexHomeTagsAt(table, home) & bits) == bits) break;
   10180:	f940018d 	ldr	x13, [x12]
   10184:	ea2d017f 	bics	xzr, x11, x13
   10188:	540000c0 	b.eq	101a0 <zbtIndexScanSlot+0x10c>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   1018c:	9100054a 	add	x10, x10, #0x1
   10190:	8b09018c 	add	x12, x12, x9
   10194:	eb0a027f 	cmp	x19, x10
   10198:	54ffff41 	b.ne	10180 <zbtIndexScanSlot+0xec>  // b.any
   1019c:	14000057 	b	102f8 <zbtIndexScanSlot+0x264>
   101a0:	eb13015f 	cmp	x10, x19
   101a4:	54000aa0 	b.eq	102f8 <zbtIndexScanSlot+0x264>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4178
    zbtScoreLeaf *leaf = id < zs->next_score_leaf_id ?
   101a8:	b9405409 	ldr	w9, [x0, #84]
   101ac:	f90003e4 	str	x4, [sp]
   101b0:	6b09011f 	cmp	w8, w9
   101b4:	540008c2 	b.cs	102cc <zbtIndexScanSlot+0x238>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4179
        zs->score_leaf_by_id[id] : NULL;
   101b8:	f9402409 	ldr	x9, [x0, #72]
   101bc:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4180
    if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {
   101c0:	b400087b 	cbz	x27, 102cc <zbtIndexScanSlot+0x238>
   101c4:	3700085b 	tbnz	w27, #0, 102cc <zbtIndexScanSlot+0x238>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4184
    serverAssert(leaf->id == id);
   101c8:	b9403369 	ldr	w9, [x27, #48]
   101cc:	f9000fe6 	str	x6, [sp, #24]
   101d0:	6b08013f 	cmp	w9, w8
   101d4:	54000180 	b.eq	10204 <zbtIndexScanSlot+0x170>  // b.none
   101d8:	b0000008 	adrp	x8, 11000 <siphash_nocase+0x4c>
   101dc:	91207908 	add	x8, x8, #0x81e
   101e0:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   101e4:	9125dc42 	add	x2, x2, #0x977
   101e8:	aa1803f4 	mov	x20, x24
   101ec:	aa0003f8 	mov	x24, x0
   101f0:	aa0803e0 	mov	x0, x8
   101f4:	52820b01 	mov	w1, #0x1058                	// #4184
   101f8:	940001cb 	bl	10924 <standalone_panic>
   101fc:	aa1803e0 	mov	x0, x24
   10200:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4185
    if (zs->member_rehash) {
   10204:	f9402008 	ldr	x8, [x0, #64]
   10208:	b4000128 	cbz	x8, 1022c <zbtIndexScanSlot+0x198>
zbtIndexLeafMigrated():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:2086
           leaf->n.index_resize == zs->member_rehash->resize_id;
   1020c:	79402f69 	ldrh	w9, [x27, #22]
   10210:	7940590a 	ldrh	w10, [x8, #44]
   10214:	6b0a013f 	cmp	w9, w10
   10218:	1a9f17e9 	cset	w9, eq	// eq = none
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4187
        if (in_new != zbtIndexLeafMigrated(zs, leaf)) return 0;
   1021c:	eb1c011f 	cmp	x8, x28
   10220:	1a9f07e8 	cset	w8, ne	// ne = any
   10224:	6b09011f 	cmp	w8, w9
   10228:	54000680 	b.eq	102f8 <zbtIndexScanSlot+0x264>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   1022c:	3940d369 	ldrb	w9, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:363
    return (uint8_t *)(zbtScoreLeafOffsets(leaf) + leaf->n.count);
   10230:	39404768 	ldrb	w8, [x27, #17]
   10234:	528000f4 	mov	w20, #0x7                   	// #7
zbtScoreLeafScoreBytes():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10238:	b4000749 	cbz	x9, 10320 <zbtIndexScanSlot+0x28c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   1023c:	1b095109 	madd	w9, w8, w9, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10240:	53037d29 	lsr	w9, w9, #3
   10244:	11002529 	add	w9, w9, #0x9
   10248:	927f352a 	and	x10, x9, #0x7ffe
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   1024c:	3940d76b 	ldrb	w11, [x27, #53]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10250:	7100211f 	cmp	w8, #0x8
   10254:	12001ea9 	and	w9, w21, #0xff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10258:	9100e363 	add	x3, x27, #0x38
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   1025c:	540006e2 	b.cs	10338 <zbtIndexScanSlot+0x2a4>  // b.hs, b.nlast
   10260:	2a1f03f5 	mov	w21, wzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10264:	7200091f 	tst	w8, #0x7
   10268:	54001b60 	b.eq	105d4 <zbtIndexScanSlot+0x540>  // b.none
   1026c:	7100053f 	cmp	w9, #0x1
   10270:	927d110c 	and	x12, x8, #0xf8
   10274:	54000b61 	b.ne	103e0 <zbtIndexScanSlot+0x34c>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10278:	340016cb 	cbz	w11, 10550 <zbtIndexScanSlot+0x4bc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   1027c:	2a2803e9 	mvn	w9, w8
   10280:	8b08054a 	add	x10, x10, x8, lsl #1
   10284:	9100e18c 	add	x12, x12, #0x38
   10288:	32186929 	orr	w9, w9, #0xffffff07
   1028c:	9100e3eb 	add	x11, sp, #0x38
   10290:	0b080129 	add	w9, w9, w8
   10294:	8b0a036a 	add	x10, x27, x10
   10298:	14000006 	b	102b0 <zbtIndexScanSlot+0x21c>
   1029c:	d100dd8d 	sub	x13, x12, #0x37
   102a0:	9100058c 	add	x12, x12, #0x1
   102a4:	51000529 	sub	w9, w9, #0x1
   102a8:	eb0801bf 	cmp	x13, x8
   102ac:	54001942 	b.cs	105d4 <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   102b0:	386c694d 	ldrb	w13, [x10, x12]
   102b4:	710005bf 	cmp	w13, #0x1
   102b8:	54ffff28 	b.hi	1029c <zbtIndexScanSlot+0x208>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   102bc:	110006ad 	add	w13, w21, #0x1
   102c0:	b8355969 	str	w9, [x11, w21, uxtw #2]
   102c4:	2a0d03f5 	mov	w21, w13
   102c8:	17fffff5 	b	1029c <zbtIndexScanSlot+0x208>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   102cc:	f9402008 	ldr	x8, [x0, #64]
   102d0:	b4000088 	cbz	x8, 102e0 <zbtIndexScanSlot+0x24c>
   102d4:	91006008 	add	x8, x0, #0x18
   102d8:	eb1c011f 	cmp	x8, x28
   102dc:	540000e0 	b.eq	102f8 <zbtIndexScanSlot+0x264>  // b.none
   102e0:	b0000000 	adrp	x0, 11000 <siphash_nocase+0x4c>
   102e4:	91207800 	add	x0, x0, #0x81e
   102e8:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   102ec:	91265842 	add	x2, x2, #0x996
   102f0:	52820aa1 	mov	w1, #0x1055                	// #4181
   102f4:	9400018c 	bl	10924 <standalone_panic>
   102f8:	aa1f03f9 	mov	x25, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4223
}
   102fc:	aa1903e0 	mov	x0, x25
   10300:	910703ff 	add	sp, sp, #0x1c0
   10304:	a9454ff4 	ldp	x20, x19, [sp, #80]
   10308:	a94457f6 	ldp	x22, x21, [sp, #64]
   1030c:	a9435ff8 	ldp	x24, x23, [sp, #48]
   10310:	a94267fa 	ldp	x26, x25, [sp, #32]
   10314:	a9416ffc 	ldp	x28, x27, [sp, #16]
   10318:	a8c67bfd 	ldp	x29, x30, [sp], #96
   1031c:	d65f03c0 	ret
   10320:	aa1f03ea 	mov	x10, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   10324:	3940d76b 	ldrb	w11, [x27, #53]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10328:	7100211f 	cmp	w8, #0x8
   1032c:	12001ea9 	and	w9, w21, #0xff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10330:	9100e363 	add	x3, x27, #0x38
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10334:	54fff963 	b.cc	10260 <zbtIndexScanSlot+0x1cc>  // b.lo, b.ul, b.last
   10338:	b200c3ec 	mov	x12, #0x101010101010101     	// #72340172838076673
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4135
    unsigned int words = count / 8;
   1033c:	d343fd0d 	lsr	x13, x8, #3
   10340:	9b0c7ece 	mul	x14, x22, x12
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4195
    unsigned int count = zbtLeafTagMatches(zbtScoreLeafHashTags(leaf),
   10344:	8b0a006c 	add	x12, x3, x10
   10348:	8b08058c 	add	x12, x12, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   1034c:	3400074b 	cbz	w11, 10434 <zbtIndexScanSlot+0x3a0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10350:	7100053f 	cmp	w9, #0x1
   10354:	5100050f 	sub	w15, w8, #0x1
   10358:	54000be1 	b.ne	104d4 <zbtIndexScanSlot+0x440>  // b.any
   1035c:	aa1f03ee 	mov	x14, xzr
   10360:	2a1f03f5 	mov	w21, wzr
   10364:	9100e3f0 	add	x16, sp, #0x38
   10368:	14000004 	b	10378 <zbtIndexScanSlot+0x2e4>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   1036c:	910005ce 	add	x14, x14, #0x1
   10370:	eb0d01df 	cmp	x14, x13
   10374:	54fff780 	b.eq	10264 <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10378:	d37df1d1 	lsl	x17, x14, #3
   1037c:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   10380:	f29fdfe1 	movk	x1, #0xfeff
   10384:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10388:	d200c240 	eor	x0, x18, #0x101010101010101
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   1038c:	8b010000 	add	x0, x0, x1
   10390:	8b010241 	add	x1, x18, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10394:	aa010000 	orr	x0, x0, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10398:	8a320012 	bic	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   1039c:	f201c252 	ands	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   103a0:	540000a1 	b.ne	103b4 <zbtIndexScanSlot+0x320>  // b.any
   103a4:	17fffff2 	b	1036c <zbtIndexScanSlot+0x2d8>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   103a8:	d1000640 	sub	x0, x18, #0x1
   103ac:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   103b0:	54fffde0 	b.eq	1036c <zbtIndexScanSlot+0x2d8>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   103b4:	dac00240 	rbit	x0, x18
   103b8:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   103bc:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   103c0:	38604981 	ldrb	w1, [x12, w0, uxtw]
   103c4:	7100043f 	cmp	w1, #0x1
   103c8:	54ffff08 	b.hi	103a8 <zbtIndexScanSlot+0x314>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   103cc:	110006a1 	add	w1, w21, #0x1
   103d0:	4b0001e0 	sub	w0, w15, w0
   103d4:	b8355a00 	str	w0, [x16, w21, uxtw #2]
   103d8:	2a0103f5 	mov	w21, w1
   103dc:	17fffff3 	b	103a8 <zbtIndexScanSlot+0x314>
   103e0:	8b08054d 	add	x13, x10, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   103e4:	34000d8b 	cbz	w11, 10594 <zbtIndexScanSlot+0x500>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   103e8:	2a2803ea 	mvn	w10, w8
   103ec:	9100e18c 	add	x12, x12, #0x38
   103f0:	8b0d036b 	add	x11, x27, x13
   103f4:	3218694a 	orr	w10, w10, #0xffffff07
   103f8:	9100e3ed 	add	x13, sp, #0x38
   103fc:	0b08014a 	add	w10, w10, w8
   10400:	14000006 	b	10418 <zbtIndexScanSlot+0x384>
   10404:	d100dd8e 	sub	x14, x12, #0x37
   10408:	9100058c 	add	x12, x12, #0x1
   1040c:	5100054a 	sub	w10, w10, #0x1
   10410:	eb0801df 	cmp	x14, x8
   10414:	54000e02 	b.cs	105d4 <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10418:	386c696e 	ldrb	w14, [x11, x12]
   1041c:	6b0901df 	cmp	w14, w9
   10420:	54ffff21 	b.ne	10404 <zbtIndexScanSlot+0x370>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10424:	110006ae 	add	w14, w21, #0x1
   10428:	b83559aa 	str	w10, [x13, w21, uxtw #2]
   1042c:	2a0e03f5 	mov	w21, w14
   10430:	17fffff5 	b	10404 <zbtIndexScanSlot+0x370>
   10434:	aa1f03ef 	mov	x15, xzr
   10438:	2a1f03f5 	mov	w21, wzr
   1043c:	9100e3f0 	add	x16, sp, #0x38
   10440:	14000004 	b	10450 <zbtIndexScanSlot+0x3bc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10444:	910005ef 	add	x15, x15, #0x1
   10448:	eb0d01ff 	cmp	x15, x13
   1044c:	54fff0c0 	b.eq	10264 <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10450:	d37df1f1 	lsl	x17, x15, #3
   10454:	b207dbe2 	mov	x2, #0xfefefefefefefefe    	// #-72340172838076674
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10458:	7100053f 	cmp	w9, #0x1
   1045c:	f29fdfe2 	movk	x2, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10460:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10464:	ca0e0240 	eor	x0, x18, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10468:	8b020001 	add	x1, x0, x2
   1046c:	8b020242 	add	x2, x18, x2
   10470:	8a200020 	bic	x0, x1, x0
   10474:	8a320052 	bic	x18, x2, x18
   10478:	9201c000 	and	x0, x0, #0x8080808080808080
   1047c:	9201c252 	and	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10480:	aa120012 	orr	x18, x0, x18
   10484:	9a921012 	csel	x18, x0, x18, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10488:	b50000b2 	cbnz	x18, 1049c <zbtIndexScanSlot+0x408>
   1048c:	17ffffee 	b	10444 <zbtIndexScanSlot+0x3b0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10490:	d1000640 	sub	x0, x18, #0x1
   10494:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10498:	54fffd60 	b.eq	10444 <zbtIndexScanSlot+0x3b0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   1049c:	dac00240 	rbit	x0, x18
   104a0:	7100053f 	cmp	w9, #0x1
   104a4:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   104a8:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   104ac:	38604981 	ldrb	w1, [x12, w0, uxtw]
   104b0:	7a400820 	ccmp	w1, #0x0, #0x0, eq	// eq = none
   104b4:	1a9f17e2 	cset	w2, eq	// eq = none
   104b8:	6b09003f 	cmp	w1, w9
   104bc:	7a401840 	ccmp	w2, #0x0, #0x0, ne	// ne = any
   104c0:	54fffe80 	b.eq	10490 <zbtIndexScanSlot+0x3fc>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   104c4:	110006a1 	add	w1, w21, #0x1
   104c8:	b8355a00 	str	w0, [x16, w21, uxtw #2]
   104cc:	2a0103f5 	mov	w21, w1
   104d0:	17fffff0 	b	10490 <zbtIndexScanSlot+0x3fc>
   104d4:	aa1f03f0 	mov	x16, xzr
   104d8:	2a1f03f5 	mov	w21, wzr
   104dc:	9100e3f1 	add	x17, sp, #0x38
   104e0:	14000004 	b	104f0 <zbtIndexScanSlot+0x45c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   104e4:	91000610 	add	x16, x16, #0x1
   104e8:	eb0d021f 	cmp	x16, x13
   104ec:	54ffebc0 	b.eq	10264 <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   104f0:	d37df212 	lsl	x18, x16, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   104f4:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   104f8:	f29fdfe1 	movk	x1, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   104fc:	f8726980 	ldr	x0, [x12, x18]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10500:	ca0e0000 	eor	x0, x0, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10504:	8b010001 	add	x1, x0, x1
   10508:	8a200020 	bic	x0, x1, x0
   1050c:	f201c000 	ands	x0, x0, #0x8080808080808080
   10510:	540000a1 	b.ne	10524 <zbtIndexScanSlot+0x490>  // b.any
   10514:	17fffff4 	b	104e4 <zbtIndexScanSlot+0x450>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10518:	d1000401 	sub	x1, x0, #0x1
   1051c:	ea000020 	ands	x0, x1, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10520:	54fffe20 	b.eq	104e4 <zbtIndexScanSlot+0x450>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   10524:	dac00001 	rbit	x1, x0
   10528:	dac01021 	clz	x1, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   1052c:	2a410e41 	orr	w1, w18, w1, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10530:	38614982 	ldrb	w2, [x12, w1, uxtw]
   10534:	6b09005f 	cmp	w2, w9
   10538:	54ffff01 	b.ne	10518 <zbtIndexScanSlot+0x484>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   1053c:	110006a2 	add	w2, w21, #0x1
   10540:	4b0101e1 	sub	w1, w15, w1
   10544:	b8355a21 	str	w1, [x17, w21, uxtw #2]
   10548:	2a0203f5 	mov	w21, w2
   1054c:	17fffff3 	b	10518 <zbtIndexScanSlot+0x484>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10550:	8b080549 	add	x9, x10, x8, lsl #1
   10554:	9100e18a 	add	x10, x12, #0x38
   10558:	9100e3eb 	add	x11, sp, #0x38
   1055c:	8b090369 	add	x9, x27, x9
   10560:	14000005 	b	10574 <zbtIndexScanSlot+0x4e0>
   10564:	d100dd4c 	sub	x12, x10, #0x37
   10568:	9100054a 	add	x10, x10, #0x1
   1056c:	eb08019f 	cmp	x12, x8
   10570:	54000322 	b.cs	105d4 <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10574:	386a692c 	ldrb	w12, [x9, x10]
   10578:	7100059f 	cmp	w12, #0x1
   1057c:	54ffff48 	b.hi	10564 <zbtIndexScanSlot+0x4d0>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10580:	110006ac 	add	w12, w21, #0x1
   10584:	5100e14d 	sub	w13, w10, #0x38
   10588:	b835596d 	str	w13, [x11, w21, uxtw #2]
   1058c:	2a0c03f5 	mov	w21, w12
   10590:	17fffff5 	b	10564 <zbtIndexScanSlot+0x4d0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10594:	9100e18b 	add	x11, x12, #0x38
   10598:	8b0d036a 	add	x10, x27, x13
   1059c:	9100e3ec 	add	x12, sp, #0x38
   105a0:	14000005 	b	105b4 <zbtIndexScanSlot+0x520>
   105a4:	d100dd6d 	sub	x13, x11, #0x37
   105a8:	9100056b 	add	x11, x11, #0x1
   105ac:	eb0801bf 	cmp	x13, x8
   105b0:	54000122 	b.cs	105d4 <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   105b4:	386b694d 	ldrb	w13, [x10, x11]
   105b8:	6b0901bf 	cmp	w13, w9
   105bc:	54ffff41 	b.ne	105a4 <zbtIndexScanSlot+0x510>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   105c0:	110006ad 	add	w13, w21, #0x1
   105c4:	5100e16e 	sub	w14, w11, #0x38
   105c8:	b835598e 	str	w14, [x12, w21, uxtw #2]
   105cc:	2a0d03f5 	mov	w21, w13
   105d0:	17fffff5 	b	105a4 <zbtIndexScanSlot+0x510>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   105d4:	34001895 	cbz	w21, 108e4 <zbtIndexScanSlot+0x850>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   105d8:	f100027f 	cmp	x19, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   105dc:	2a1503e8 	mov	w8, w21
   105e0:	aa1f03f6 	mov	x22, xzr
   105e4:	7a410aa0 	ccmp	w21, #0x1, #0x0, eq	// eq = none
   105e8:	aa1f03f9 	mov	x25, xzr
   105ec:	a9028fe8 	stp	x8, x3, [sp, #40]
   105f0:	1a9f07e8 	cset	w8, ne	// ne = any
   105f4:	f90007fc 	str	x28, [sp, #8]
   105f8:	b90027e8 	str	w8, [sp, #36]
   105fc:	b90017f4 	str	w20, [sp, #20]
   10600:	1400001b 	b	1066c <zbtIndexScanSlot+0x5d8>
   10604:	2a0803eb 	mov	w11, w8
   10608:	9280000c 	mov	x12, #0xffffffffffffffff    	// #-1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   1060c:	7101011f 	cmp	w8, #0x40
   10610:	9acb218b 	lsl	x11, x12, x11
   10614:	da8b2188 	csinv	x8, x12, x11, cs	// cs = hs, nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10618:	39404f6b 	ldrb	w11, [x27, #19]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   1061c:	8a080148 	and	x8, x10, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10620:	9acb2108 	lsl	x8, x8, x11
   10624:	f940176a 	ldr	x10, [x27, #40]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10628:	7100013f 	cmp	w9, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   1062c:	aa1803e0 	mov	x0, x24
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10630:	da880508 	cneg	x8, x8, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   10634:	aa1c03e1 	mov	x1, x28
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10638:	8b080148 	add	x8, x10, x8
zbtOrderedToScore():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:331
    if (ordered & (UINT64_C(1) << 63))
   1063c:	9240f909 	and	x9, x8, #0x7fffffffffffffff
   10640:	f100011f 	cmp	x8, #0x0
   10644:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:335
    memcpy(&score, &bits, sizeof(score));
   10648:	9e670100 	fmov	d0, x8
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   1064c:	d63f01e0 	blr	x15
   10650:	f94007fc 	ldr	x28, [sp, #8]
   10654:	f9401be3 	ldr	x3, [sp, #48]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4219
        emitted++;
   10658:	91000739 	add	x25, x25, #0x1
   1065c:	f94017e8 	ldr	x8, [sp, #40]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   10660:	910006d6 	add	x22, x22, #0x1
   10664:	eb0802df 	cmp	x22, x8
   10668:	540014c0 	b.eq	10900 <zbtIndexScanSlot+0x86c>  // b.none
   1066c:	9100e3e8 	add	x8, sp, #0x38
   10670:	b876791a 	ldr	w26, [x8, x22, lsl #2]
   10674:	b94027e8 	ldr	w8, [sp, #36]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4207
        if (count > 1 || home_end) {
   10678:	340008a8 	cbz	w8, 1078c <zbtIndexScanSlot+0x6f8>
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   1067c:	3940d368 	ldrb	w8, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10680:	b40000c8 	cbz	x8, 10698 <zbtIndexScanSlot+0x604>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10684:	39404769 	ldrb	w9, [x27, #17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10688:	1b085128 	madd	w8, w9, w8, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   1068c:	53037d08 	lsr	w8, w8, #3
   10690:	11002508 	add	w8, w8, #0x9
   10694:	927f3508 	and	x8, x8, #0x7ffe
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10698:	3940d76a 	ldrb	w10, [x27, #53]
   1069c:	2a1a03e9 	mov	w9, w26
   106a0:	3400008a 	cbz	w10, 106b0 <zbtIndexScanSlot+0x61c>
   106a4:	39404769 	ldrb	w9, [x27, #17]
   106a8:	2a3a03ea 	mvn	w10, w26
   106ac:	0b0a0129 	add	w9, w9, w10
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   106b0:	8b080068 	add	x8, x3, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   106b4:	78695908 	ldrh	w8, [x8, w9, uxtw #1]
zbtScoreLeafRecord():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   106b8:	8b080368 	add	x8, x27, x8
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:625
    if (record[0] == ZBT_PACKED_EXTERNAL)
   106bc:	39400101 	ldrb	w1, [x8]
   106c0:	7103f83f 	cmp	w1, #0xfe
   106c4:	540000e0 	b.eq	106e0 <zbtIndexScanSlot+0x64c>  // b.none
   106c8:	7103fc3f 	cmp	w1, #0xff
   106cc:	54000101 	b.ne	106ec <zbtIndexScanSlot+0x658>  // b.any
zbtExternalHash():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:561
    memcpy(&hash, record + ZBT_EXTERNAL_HASH_OFFSET, sizeof(hash));
   106d0:	b8401109 	ldur	w9, [x8, #1]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   106d4:	f9400788 	ldr	x8, [x28, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   106d8:	b5000193 	cbnz	x19, 10708 <zbtIndexScanSlot+0x674>
   106dc:	14000012 	b	10724 <zbtIndexScanSlot+0x690>
zbtPackedData():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   106e0:	78401101 	ldurh	w1, [x8, #1]
   106e4:	52800069 	mov	w9, #0x3                   	// #3
   106e8:	14000002 	b	106f0 <zbtIndexScanSlot+0x65c>
   106ec:	52800029 	mov	w9, #0x1                   	// #1
   106f0:	8b090100 	add	x0, x8, x9
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:629
    return (uint32_t)dictGenHashFunction(ele, len);
   106f4:	94000124 	bl	10b84 <dictGenHashFunction>
   106f8:	f9401be3 	ldr	x3, [sp, #48]
   106fc:	92407c09 	and	x9, x0, #0xffffffff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10700:	f9400788 	ldr	x8, [x28, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10704:	b4000113 	cbz	x19, 10724 <zbtIndexScanSlot+0x690>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10708:	5100050a 	sub	w10, w8, #0x1
   1070c:	f94003eb 	ldr	x11, [sp]
   10710:	8a09014a 	and	x10, x10, x9
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10714:	eb0b015f 	cmp	x10, x11
   10718:	54fffa23 	b.cc	1065c <zbtIndexScanSlot+0x5c8>  // b.lo, b.ul, b.last
   1071c:	eb13015f 	cmp	x10, x19
   10720:	54fff9e2 	b.cs	1065c <zbtIndexScanSlot+0x5c8>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4212
            if (count > 1 && !zbtIndexHashReachesBucket(table, hash, bucket))
   10724:	710006bf 	cmp	w21, #0x1
   10728:	54000320 	b.eq	1078c <zbtIndexScanSlot+0x6f8>  // b.none
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   1072c:	b4fff988 	cbz	x8, 1065c <zbtIndexScanSlot+0x5c8>
   10730:	b940238c 	ldr	w12, [x28, #32]
   10734:	d100050a 	sub	x10, x8, #0x1
   10738:	f940038b 	ldr	x11, [x28]
   1073c:	5280040d 	mov	w13, #0x20                  	// #32
   10740:	7100019f 	cmp	w12, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4102
    unsigned long index = hash & mask;
   10744:	8a09014c 	and	x12, x10, x9
   10748:	52800609 	mov	w9, #0x30                  	// #48
   1074c:	9a8901a9 	csel	x9, x13, x9, eq	// eq = none
zbtIndexBucketAt():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1759
    return (zbtIndexBucket *)((unsigned char *)table->buckets +
   10750:	9b092d8d 	madd	x13, x12, x9, x11
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4106
        if (bucket == target) return 1;
   10754:	eb1701bf 	cmp	x13, x23
   10758:	540001a0 	b.eq	1078c <zbtIndexScanSlot+0x6f8>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   1075c:	f94001ad 	ldr	x13, [x13]
zbtIndexTagMask():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10760:	b207dbee 	mov	x14, #0xfefefefefefefefe    	// #-72340172838076674
   10764:	f29fdfee 	movk	x14, #0xfeff
   10768:	8b0e01ae 	add	x14, x13, x14
   1076c:	8a2d01cd 	bic	x13, x14, x13
   10770:	f201c1bf 	tst	x13, #0x8080808080808080
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   10774:	54fff741 	b.ne	1065c <zbtIndexScanSlot+0x5c8>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10778:	9100058c 	add	x12, x12, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   1077c:	f1000508 	subs	x8, x8, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10780:	8a0a018c 	and	x12, x12, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10784:	54fffe61 	b.ne	10750 <zbtIndexScanSlot+0x6bc>  // b.any
   10788:	17ffffb5 	b	1065c <zbtIndexScanSlot+0x5c8>
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   1078c:	3940d368 	ldrb	w8, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10790:	34000668 	cbz	w8, 1085c <zbtIndexScanSlot+0x7c8>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10794:	39404769 	ldrb	w9, [x27, #17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10798:	1b085129 	madd	w9, w9, w8, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   1079c:	53037d29 	lsr	w9, w9, #3
   107a0:	11002529 	add	w9, w9, #0x9
   107a4:	927f352a 	and	x10, x9, #0x7ffe
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   107a8:	3940d769 	ldrb	w9, [x27, #53]
   107ac:	aa1803f4 	mov	x20, x24
   107b0:	2a1a03eb 	mov	w11, w26
   107b4:	34000089 	cbz	w9, 107c4 <zbtIndexScanSlot+0x730>
   107b8:	3940476b 	ldrb	w11, [x27, #17]
   107bc:	2a3a03ec 	mvn	w12, w26
   107c0:	0b0c016b 	add	w11, w11, w12
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   107c4:	8b0a006a 	add	x10, x3, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   107c8:	786b594a 	ldrh	w10, [x10, w11, uxtw #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   107cc:	8b0a0378 	add	x24, x27, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:589
    if (record[0] < ZBT_PACKED_SHORT) {
   107d0:	39400302 	ldrb	w2, [x24]
   107d4:	7103f45f 	cmp	w2, #0xfd
   107d8:	540000a8 	b.hi	107ec <zbtIndexScanSlot+0x758>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:591
        return record + 1;
   107dc:	9100071c 	add	x28, x24, #0x1
   107e0:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   107e4:	35000108 	cbnz	w8, 10804 <zbtIndexScanSlot+0x770>
   107e8:	1400003b 	b	108d4 <zbtIndexScanSlot+0x840>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:592
    } else if (record[0] == ZBT_PACKED_SHORT) {
   107ec:	7103f85f 	cmp	w2, #0xfe
   107f0:	54000421 	b.ne	10874 <zbtIndexScanSlot+0x7e0>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   107f4:	78401302 	ldurh	w2, [x24, #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:596
        return record + 3;
   107f8:	91000f1c 	add	x28, x24, #0x3
   107fc:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10800:	340006a8 	cbz	w8, 108d4 <zbtIndexScanSlot+0x840>
   10804:	f9400fef 	ldr	x15, [sp, #24]
   10808:	b94017f4 	ldr	w20, [sp, #20]
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   1080c:	34000089 	cbz	w9, 1081c <zbtIndexScanSlot+0x788>
   10810:	3940476a 	ldrb	w10, [x27, #17]
   10814:	2a3a03eb 	mvn	w11, w26
   10818:	0b0b015a 	add	w26, w10, w11
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:504
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
   1081c:	9ba87f4a 	umull	x10, w26, w8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:505
        size_t byte = bitpos / 8;
   10820:	d343fd4b 	lsr	x11, x10, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10824:	9240094e 	and	x14, x10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:506
        unsigned int shift = bitpos & 7;
   10828:	7200094c 	ands	w12, w10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:507
        memcpy(&delta, leaf->data + byte, sizeof(delta));
   1082c:	f86b686d 	ldr	x13, [x3, x11]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10830:	9ace25aa 	lsr	x10, x13, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:509
        if (shift && bits > 64 - shift)
   10834:	54ffee80 	b.eq	10604 <zbtIndexScanSlot+0x570>  // b.none
   10838:	5280080d 	mov	w13, #0x40                  	// #64
   1083c:	4b0c01ac 	sub	w12, w13, w12
   10840:	6b08019f 	cmp	w12, w8
   10844:	54ffee02 	b.cs	10604 <zbtIndexScanSlot+0x570>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:510
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
   10848:	8b1b016b 	add	x11, x11, x27
   1084c:	3941016b 	ldrb	w11, [x11, #64]
   10850:	9acc216b 	lsl	x11, x11, x12
   10854:	aa0a016a 	orr	x10, x11, x10
   10858:	17ffff6b 	b	10604 <zbtIndexScanSlot+0x570>
   1085c:	aa1f03ea 	mov	x10, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10860:	3940d769 	ldrb	w9, [x27, #53]
   10864:	aa1803f4 	mov	x20, x24
   10868:	2a1a03eb 	mov	w11, w26
   1086c:	35fffa69 	cbnz	w9, 107b8 <zbtIndexScanSlot+0x724>
   10870:	17ffffd5 	b	107c4 <zbtIndexScanSlot+0x730>
zbtExternalPointer():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:576
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
   10874:	f840d31c 	ldur	x28, [x24, #13]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:599
        serverAssert(ptr != NULL);
   10878:	b500025c 	cbnz	x28, 108c0 <zbtIndexScanSlot+0x82c>
   1087c:	b0000000 	adrp	x0, 11000 <siphash_nocase+0x4c>
   10880:	91207800 	add	x0, x0, #0x81e
   10884:	52804ae1 	mov	w1, #0x257                 	// #599
   10888:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   1088c:	91252842 	add	x2, x2, #0x94a
   10890:	94000025 	bl	10924 <standalone_panic>
zbtExternalLength():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:567
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
   10894:	39400308 	ldrb	w8, [x24]
   10898:	f9401be3 	ldr	x3, [sp, #48]
   1089c:	7103fd1f 	cmp	w8, #0xff
   108a0:	54000100 	b.eq	108c0 <zbtIndexScanSlot+0x82c>  // b.none
   108a4:	b0000000 	adrp	x0, 11000 <siphash_nocase+0x4c>
   108a8:	91207800 	add	x0, x0, #0x81e
   108ac:	528046e1 	mov	w1, #0x237                 	// #567
   108b0:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   108b4:	91255842 	add	x2, x2, #0x956
   108b8:	9400001b 	bl	10924 <standalone_panic>
   108bc:	f9401be3 	ldr	x3, [sp, #48]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:568
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
   108c0:	f8405302 	ldur	x2, [x24, #5]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:500
    unsigned int bits = leaf->score_bits;
   108c4:	3940d368 	ldrb	w8, [x27, #52]
   108c8:	3940d769 	ldrb	w9, [x27, #53]
   108cc:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   108d0:	35fff9a8 	cbnz	w8, 10804 <zbtIndexScanSlot+0x770>
   108d4:	f9400fef 	ldr	x15, [sp, #24]
   108d8:	b94017f4 	ldr	w20, [sp, #20]
   108dc:	aa1f03e8 	mov	x8, xzr
   108e0:	17ffff51 	b	10624 <zbtIndexScanSlot+0x590>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   108e4:	b0000000 	adrp	x0, 11000 <siphash_nocase+0x4c>
   108e8:	91207800 	add	x0, x0, #0x81e
   108ec:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   108f0:	91365442 	add	x2, x2, #0xd95
   108f4:	52820cc1 	mov	w1, #0x1066                	// #4198
   108f8:	9400000b 	bl	10924 <standalone_panic>
   108fc:	aa1f03f9 	mov	x25, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   10900:	aa190268 	orr	x8, x19, x25
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4221
    serverAssert(home_end || emitted != 0);
   10904:	b5ffcfc8 	cbnz	x8, 102fc <zbtIndexScanSlot+0x268>
   10908:	b0000000 	adrp	x0, 11000 <siphash_nocase+0x4c>
   1090c:	91207800 	add	x0, x0, #0x81e
   10910:	b0000002 	adrp	x2, 11000 <siphash_nocase+0x4c>
   10914:	91368042 	add	x2, x2, #0xda0
   10918:	52820fa1 	mov	w1, #0x107d                	// #4221
   1091c:	94000002 	bl	10924 <standalone_panic>
   10920:	17fffe77 	b	102fc <zbtIndexScanSlot+0x268>

