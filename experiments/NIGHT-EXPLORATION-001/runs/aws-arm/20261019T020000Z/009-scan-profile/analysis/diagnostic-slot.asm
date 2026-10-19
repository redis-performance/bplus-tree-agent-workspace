000000000001038c <zbtIndexScanSlot>:
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4166
{
   1038c:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
   10390:	a9016ffc 	stp	x28, x27, [sp, #16]
   10394:	a90267fa 	stp	x26, x25, [sp, #32]
   10398:	a9035ff8 	stp	x24, x23, [sp, #48]
   1039c:	a90457f6 	stp	x22, x21, [sp, #64]
   103a0:	a9054ff4 	stp	x20, x19, [sp, #80]
   103a4:	910003fd 	mov	x29, sp
   103a8:	d10703ff 	sub	sp, sp, #0x1c0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   103ac:	f9400048 	ldr	x8, [x2]
   103b0:	531d706a 	lsl	w10, w3, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4168
    uint32_t id = zbtIndexGetId(table, bucket, slot_pos);
   103b4:	b9402029 	ldr	w9, [x1, #32]
   103b8:	aa0703f8 	mov	x24, x7
   103bc:	aa0503f3 	mov	x19, x5
   103c0:	aa0203f7 	mov	x23, x2
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   103c4:	9aca2515 	lsr	x21, x8, x10
   103c8:	aa0103fc 	mov	x28, x1
   103cc:	2a0303e8 	mov	w8, w3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1775
    if (table->wide_ids) return bucket->wide.id[pos];
   103d0:	340000e9 	cbz	w9, 103ec <zbtIndexScanSlot+0x60>
   103d4:	8b080ae8 	add	x8, x23, x8, lsl #2
   103d8:	b9401108 	ldr	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   103dc:	f2401eb6 	ands	x22, x21, #0xff
   103e0:	aa1f03f9 	mov	x25, xzr
   103e4:	54000141 	b.ne	1040c <zbtIndexScanSlot+0x80>  // b.any
   103e8:	14000083 	b	105f4 <zbtIndexScanSlot+0x268>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1776
    uint16_t id = bucket->narrow.id[pos];
   103ec:	8b0806e8 	add	x8, x23, x8, lsl #1
   103f0:	529fffea 	mov	w10, #0xffff                	// #65535
   103f4:	79402108 	ldrh	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1777
    return id == UINT16_MAX ? ZBT_INDEX_DELETED_ID : id;
   103f8:	6b0a011f 	cmp	w8, w10
   103fc:	5a9f1108 	csinv	w8, w8, wzr, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   10400:	f2401eb6 	ands	x22, x21, #0xff
   10404:	aa1f03f9 	mov	x25, xzr
   10408:	54000f60 	b.eq	105f4 <zbtIndexScanSlot+0x268>  // b.none
   1040c:	3100051f 	cmn	w8, #0x1
   10410:	54000f20 	b.eq	105f4 <zbtIndexScanSlot+0x268>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   10414:	b4000473 	cbz	x19, 104a0 <zbtIndexScanSlot+0x114>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   10418:	eb13009f 	cmp	x4, x19
   1041c:	aa0403ea 	mov	x10, x4
   10420:	540003c2 	b.cs	10498 <zbtIndexScanSlot+0x10c>  // b.hs, b.nlast
   10424:	d28f82aa 	mov	x10, #0x7c15                	// #31765
   10428:	7100013f 	cmp	w9, #0x0
   1042c:	52800609 	mov	w9, #0x30                  	// #48
   10430:	f2afe94a 	movk	x10, #0x7f4a, lsl #16
   10434:	5280040b 	mov	w11, #0x20                  	// #32
   10438:	f940038c 	ldr	x12, [x28]
   1043c:	f2cf372a 	movk	x10, #0x79b9, lsl #32
   10440:	9a890169 	csel	x9, x11, x9, eq	// eq = none
   10444:	5280002d 	mov	w13, #0x1                   	// #1
   10448:	f2f3c6ea 	movk	x10, #0x9e37, lsl #48
   1044c:	9b04312c 	madd	x12, x9, x4, x12
   10450:	9ad521ae 	lsl	x14, x13, x21
   10454:	9b0a7eca 	mul	x10, x22, x10
   10458:	9100218c 	add	x12, x12, #0x8
   1045c:	d37afd4b 	lsr	x11, x10, #58
   10460:	d364fd4a 	lsr	x10, x10, #36
   10464:	9acb21ab 	lsl	x11, x13, x11
   10468:	9aca21aa 	lsl	x10, x13, x10
   1046c:	aa0e016b 	orr	x11, x11, x14
   10470:	aa0a016b 	orr	x11, x11, x10
   10474:	aa0403ea 	mov	x10, x4
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4174
            if ((*zbtIndexHomeTagsAt(table, home) & bits) == bits) break;
   10478:	f940018d 	ldr	x13, [x12]
   1047c:	ea2d017f 	bics	xzr, x11, x13
   10480:	540000c0 	b.eq	10498 <zbtIndexScanSlot+0x10c>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   10484:	9100054a 	add	x10, x10, #0x1
   10488:	8b09018c 	add	x12, x12, x9
   1048c:	eb0a027f 	cmp	x19, x10
   10490:	54ffff41 	b.ne	10478 <zbtIndexScanSlot+0xec>  // b.any
   10494:	14000057 	b	105f0 <zbtIndexScanSlot+0x264>
   10498:	eb13015f 	cmp	x10, x19
   1049c:	54000aa0 	b.eq	105f0 <zbtIndexScanSlot+0x264>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4178
    zbtScoreLeaf *leaf = id < zs->next_score_leaf_id ?
   104a0:	b9405409 	ldr	w9, [x0, #84]
   104a4:	f90003e4 	str	x4, [sp]
   104a8:	6b09011f 	cmp	w8, w9
   104ac:	540008c2 	b.cs	105c4 <zbtIndexScanSlot+0x238>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4179
        zs->score_leaf_by_id[id] : NULL;
   104b0:	f9402409 	ldr	x9, [x0, #72]
   104b4:	f868593b 	ldr	x27, [x9, w8, uxtw #3]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4180
    if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {
   104b8:	b400087b 	cbz	x27, 105c4 <zbtIndexScanSlot+0x238>
   104bc:	3700085b 	tbnz	w27, #0, 105c4 <zbtIndexScanSlot+0x238>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4184
    serverAssert(leaf->id == id);
   104c0:	b9403369 	ldr	w9, [x27, #48]
   104c4:	f9000fe6 	str	x6, [sp, #24]
   104c8:	6b08013f 	cmp	w9, w8
   104cc:	54000180 	b.eq	104fc <zbtIndexScanSlot+0x170>  // b.none
   104d0:	b0000008 	adrp	x8, 11000 <sdsnew+0x88>
   104d4:	912ef108 	add	x8, x8, #0xbbc
   104d8:	b0000002 	adrp	x2, 11000 <sdsnew+0x88>
   104dc:	91345442 	add	x2, x2, #0xd15
   104e0:	aa1803f4 	mov	x20, x24
   104e4:	aa0003f8 	mov	x24, x0
   104e8:	aa0803e0 	mov	x0, x8
   104ec:	52820b01 	mov	w1, #0x1058                	// #4184
   104f0:	940001cb 	bl	10c1c <standalone_panic>
   104f4:	aa1803e0 	mov	x0, x24
   104f8:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4185
    if (zs->member_rehash) {
   104fc:	f9402008 	ldr	x8, [x0, #64]
   10500:	b4000128 	cbz	x8, 10524 <zbtIndexScanSlot+0x198>
zbtIndexLeafMigrated():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:2086
           leaf->n.index_resize == zs->member_rehash->resize_id;
   10504:	79402f69 	ldrh	w9, [x27, #22]
   10508:	7940590a 	ldrh	w10, [x8, #44]
   1050c:	6b0a013f 	cmp	w9, w10
   10510:	1a9f17e9 	cset	w9, eq	// eq = none
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4187
        if (in_new != zbtIndexLeafMigrated(zs, leaf)) return 0;
   10514:	eb1c011f 	cmp	x8, x28
   10518:	1a9f07e8 	cset	w8, ne	// ne = any
   1051c:	6b09011f 	cmp	w8, w9
   10520:	54000680 	b.eq	105f0 <zbtIndexScanSlot+0x264>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10524:	3940d369 	ldrb	w9, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:363
    return (uint8_t *)(zbtScoreLeafOffsets(leaf) + leaf->n.count);
   10528:	39404768 	ldrb	w8, [x27, #17]
   1052c:	528000f4 	mov	w20, #0x7                   	// #7
zbtScoreLeafScoreBytes():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10530:	b4000749 	cbz	x9, 10618 <zbtIndexScanSlot+0x28c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10534:	1b095109 	madd	w9, w8, w9, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10538:	53037d29 	lsr	w9, w9, #3
   1053c:	11002529 	add	w9, w9, #0x9
   10540:	927f352a 	and	x10, x9, #0x7ffe
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   10544:	3940d76b 	ldrb	w11, [x27, #53]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10548:	7100211f 	cmp	w8, #0x8
   1054c:	12001ea9 	and	w9, w21, #0xff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10550:	9100e363 	add	x3, x27, #0x38
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10554:	540006e2 	b.cs	10630 <zbtIndexScanSlot+0x2a4>  // b.hs, b.nlast
   10558:	2a1f03f5 	mov	w21, wzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   1055c:	7200091f 	tst	w8, #0x7
   10560:	54001b60 	b.eq	108cc <zbtIndexScanSlot+0x540>  // b.none
   10564:	7100053f 	cmp	w9, #0x1
   10568:	927d110c 	and	x12, x8, #0xf8
   1056c:	54000b61 	b.ne	106d8 <zbtIndexScanSlot+0x34c>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10570:	340016cb 	cbz	w11, 10848 <zbtIndexScanSlot+0x4bc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10574:	2a2803e9 	mvn	w9, w8
   10578:	8b08054a 	add	x10, x10, x8, lsl #1
   1057c:	9100e18c 	add	x12, x12, #0x38
   10580:	32186929 	orr	w9, w9, #0xffffff07
   10584:	9100e3eb 	add	x11, sp, #0x38
   10588:	0b080129 	add	w9, w9, w8
   1058c:	8b0a036a 	add	x10, x27, x10
   10590:	14000006 	b	105a8 <zbtIndexScanSlot+0x21c>
   10594:	d100dd8d 	sub	x13, x12, #0x37
   10598:	9100058c 	add	x12, x12, #0x1
   1059c:	51000529 	sub	w9, w9, #0x1
   105a0:	eb0801bf 	cmp	x13, x8
   105a4:	54001942 	b.cs	108cc <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   105a8:	386c694d 	ldrb	w13, [x10, x12]
   105ac:	710005bf 	cmp	w13, #0x1
   105b0:	54ffff28 	b.hi	10594 <zbtIndexScanSlot+0x208>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   105b4:	110006ad 	add	w13, w21, #0x1
   105b8:	b8355969 	str	w9, [x11, w21, uxtw #2]
   105bc:	2a0d03f5 	mov	w21, w13
   105c0:	17fffff5 	b	10594 <zbtIndexScanSlot+0x208>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   105c4:	f9402008 	ldr	x8, [x0, #64]
   105c8:	b4000088 	cbz	x8, 105d8 <zbtIndexScanSlot+0x24c>
   105cc:	91006008 	add	x8, x0, #0x18
   105d0:	eb1c011f 	cmp	x8, x28
   105d4:	540000e0 	b.eq	105f0 <zbtIndexScanSlot+0x264>  // b.none
   105d8:	b0000000 	adrp	x0, 11000 <sdsnew+0x88>
   105dc:	912ef000 	add	x0, x0, #0xbbc
   105e0:	b0000002 	adrp	x2, 11000 <sdsnew+0x88>
   105e4:	9134d042 	add	x2, x2, #0xd34
   105e8:	52820aa1 	mov	w1, #0x1055                	// #4181
   105ec:	9400018c 	bl	10c1c <standalone_panic>
   105f0:	aa1f03f9 	mov	x25, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4223
}
   105f4:	aa1903e0 	mov	x0, x25
   105f8:	910703ff 	add	sp, sp, #0x1c0
   105fc:	a9454ff4 	ldp	x20, x19, [sp, #80]
   10600:	a94457f6 	ldp	x22, x21, [sp, #64]
   10604:	a9435ff8 	ldp	x24, x23, [sp, #48]
   10608:	a94267fa 	ldp	x26, x25, [sp, #32]
   1060c:	a9416ffc 	ldp	x28, x27, [sp, #16]
   10610:	a8c67bfd 	ldp	x29, x30, [sp], #96
   10614:	d65f03c0 	ret
   10618:	aa1f03ea 	mov	x10, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   1061c:	3940d76b 	ldrb	w11, [x27, #53]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10620:	7100211f 	cmp	w8, #0x8
   10624:	12001ea9 	and	w9, w21, #0xff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10628:	9100e363 	add	x3, x27, #0x38
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   1062c:	54fff963 	b.cc	10558 <zbtIndexScanSlot+0x1cc>  // b.lo, b.ul, b.last
   10630:	b200c3ec 	mov	x12, #0x101010101010101     	// #72340172838076673
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4135
    unsigned int words = count / 8;
   10634:	d343fd0d 	lsr	x13, x8, #3
   10638:	9b0c7ece 	mul	x14, x22, x12
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4195
    unsigned int count = zbtLeafTagMatches(zbtScoreLeafHashTags(leaf),
   1063c:	8b0a006c 	add	x12, x3, x10
   10640:	8b08058c 	add	x12, x12, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   10644:	3400074b 	cbz	w11, 1072c <zbtIndexScanSlot+0x3a0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10648:	7100053f 	cmp	w9, #0x1
   1064c:	5100050f 	sub	w15, w8, #0x1
   10650:	54000be1 	b.ne	107cc <zbtIndexScanSlot+0x440>  // b.any
   10654:	aa1f03ee 	mov	x14, xzr
   10658:	2a1f03f5 	mov	w21, wzr
   1065c:	9100e3f0 	add	x16, sp, #0x38
   10660:	14000004 	b	10670 <zbtIndexScanSlot+0x2e4>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10664:	910005ce 	add	x14, x14, #0x1
   10668:	eb0d01df 	cmp	x14, x13
   1066c:	54fff780 	b.eq	1055c <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10670:	d37df1d1 	lsl	x17, x14, #3
   10674:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   10678:	f29fdfe1 	movk	x1, #0xfeff
   1067c:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10680:	d200c240 	eor	x0, x18, #0x101010101010101
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10684:	8b010000 	add	x0, x0, x1
   10688:	8b010241 	add	x1, x18, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   1068c:	aa010000 	orr	x0, x0, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10690:	8a320012 	bic	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10694:	f201c252 	ands	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10698:	540000a1 	b.ne	106ac <zbtIndexScanSlot+0x320>  // b.any
   1069c:	17fffff2 	b	10664 <zbtIndexScanSlot+0x2d8>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   106a0:	d1000640 	sub	x0, x18, #0x1
   106a4:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   106a8:	54fffde0 	b.eq	10664 <zbtIndexScanSlot+0x2d8>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   106ac:	dac00240 	rbit	x0, x18
   106b0:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   106b4:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   106b8:	38604981 	ldrb	w1, [x12, w0, uxtw]
   106bc:	7100043f 	cmp	w1, #0x1
   106c0:	54ffff08 	b.hi	106a0 <zbtIndexScanSlot+0x314>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   106c4:	110006a1 	add	w1, w21, #0x1
   106c8:	4b0001e0 	sub	w0, w15, w0
   106cc:	b8355a00 	str	w0, [x16, w21, uxtw #2]
   106d0:	2a0103f5 	mov	w21, w1
   106d4:	17fffff3 	b	106a0 <zbtIndexScanSlot+0x314>
   106d8:	8b08054d 	add	x13, x10, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   106dc:	34000d8b 	cbz	w11, 1088c <zbtIndexScanSlot+0x500>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   106e0:	2a2803ea 	mvn	w10, w8
   106e4:	9100e18c 	add	x12, x12, #0x38
   106e8:	8b0d036b 	add	x11, x27, x13
   106ec:	3218694a 	orr	w10, w10, #0xffffff07
   106f0:	9100e3ed 	add	x13, sp, #0x38
   106f4:	0b08014a 	add	w10, w10, w8
   106f8:	14000006 	b	10710 <zbtIndexScanSlot+0x384>
   106fc:	d100dd8e 	sub	x14, x12, #0x37
   10700:	9100058c 	add	x12, x12, #0x1
   10704:	5100054a 	sub	w10, w10, #0x1
   10708:	eb0801df 	cmp	x14, x8
   1070c:	54000e02 	b.cs	108cc <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10710:	386c696e 	ldrb	w14, [x11, x12]
   10714:	6b0901df 	cmp	w14, w9
   10718:	54ffff21 	b.ne	106fc <zbtIndexScanSlot+0x370>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   1071c:	110006ae 	add	w14, w21, #0x1
   10720:	b83559aa 	str	w10, [x13, w21, uxtw #2]
   10724:	2a0e03f5 	mov	w21, w14
   10728:	17fffff5 	b	106fc <zbtIndexScanSlot+0x370>
   1072c:	aa1f03ef 	mov	x15, xzr
   10730:	2a1f03f5 	mov	w21, wzr
   10734:	9100e3f0 	add	x16, sp, #0x38
   10738:	14000004 	b	10748 <zbtIndexScanSlot+0x3bc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   1073c:	910005ef 	add	x15, x15, #0x1
   10740:	eb0d01ff 	cmp	x15, x13
   10744:	54fff0c0 	b.eq	1055c <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10748:	d37df1f1 	lsl	x17, x15, #3
   1074c:	b207dbe2 	mov	x2, #0xfefefefefefefefe    	// #-72340172838076674
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10750:	7100053f 	cmp	w9, #0x1
   10754:	f29fdfe2 	movk	x2, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10758:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   1075c:	ca0e0240 	eor	x0, x18, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10760:	8b020001 	add	x1, x0, x2
   10764:	8b020242 	add	x2, x18, x2
   10768:	8a200020 	bic	x0, x1, x0
   1076c:	8a320052 	bic	x18, x2, x18
   10770:	9201c000 	and	x0, x0, #0x8080808080808080
   10774:	9201c252 	and	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10778:	aa120012 	orr	x18, x0, x18
   1077c:	9a921012 	csel	x18, x0, x18, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10780:	b50000b2 	cbnz	x18, 10794 <zbtIndexScanSlot+0x408>
   10784:	17ffffee 	b	1073c <zbtIndexScanSlot+0x3b0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10788:	d1000640 	sub	x0, x18, #0x1
   1078c:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10790:	54fffd60 	b.eq	1073c <zbtIndexScanSlot+0x3b0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   10794:	dac00240 	rbit	x0, x18
   10798:	7100053f 	cmp	w9, #0x1
   1079c:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   107a0:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   107a4:	38604981 	ldrb	w1, [x12, w0, uxtw]
   107a8:	7a400820 	ccmp	w1, #0x0, #0x0, eq	// eq = none
   107ac:	1a9f17e2 	cset	w2, eq	// eq = none
   107b0:	6b09003f 	cmp	w1, w9
   107b4:	7a401840 	ccmp	w2, #0x0, #0x0, ne	// ne = any
   107b8:	54fffe80 	b.eq	10788 <zbtIndexScanSlot+0x3fc>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   107bc:	110006a1 	add	w1, w21, #0x1
   107c0:	b8355a00 	str	w0, [x16, w21, uxtw #2]
   107c4:	2a0103f5 	mov	w21, w1
   107c8:	17fffff0 	b	10788 <zbtIndexScanSlot+0x3fc>
   107cc:	aa1f03f0 	mov	x16, xzr
   107d0:	2a1f03f5 	mov	w21, wzr
   107d4:	9100e3f1 	add	x17, sp, #0x38
   107d8:	14000004 	b	107e8 <zbtIndexScanSlot+0x45c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   107dc:	91000610 	add	x16, x16, #0x1
   107e0:	eb0d021f 	cmp	x16, x13
   107e4:	54ffebc0 	b.eq	1055c <zbtIndexScanSlot+0x1d0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   107e8:	d37df212 	lsl	x18, x16, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   107ec:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   107f0:	f29fdfe1 	movk	x1, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   107f4:	f8726980 	ldr	x0, [x12, x18]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   107f8:	ca0e0000 	eor	x0, x0, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   107fc:	8b010001 	add	x1, x0, x1
   10800:	8a200020 	bic	x0, x1, x0
   10804:	f201c000 	ands	x0, x0, #0x8080808080808080
   10808:	540000a1 	b.ne	1081c <zbtIndexScanSlot+0x490>  // b.any
   1080c:	17fffff4 	b	107dc <zbtIndexScanSlot+0x450>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10810:	d1000401 	sub	x1, x0, #0x1
   10814:	ea000020 	ands	x0, x1, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10818:	54fffe20 	b.eq	107dc <zbtIndexScanSlot+0x450>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   1081c:	dac00001 	rbit	x1, x0
   10820:	dac01021 	clz	x1, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   10824:	2a410e41 	orr	w1, w18, w1, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10828:	38614982 	ldrb	w2, [x12, w1, uxtw]
   1082c:	6b09005f 	cmp	w2, w9
   10830:	54ffff01 	b.ne	10810 <zbtIndexScanSlot+0x484>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   10834:	110006a2 	add	w2, w21, #0x1
   10838:	4b0101e1 	sub	w1, w15, w1
   1083c:	b8355a21 	str	w1, [x17, w21, uxtw #2]
   10840:	2a0203f5 	mov	w21, w2
   10844:	17fffff3 	b	10810 <zbtIndexScanSlot+0x484>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10848:	8b080549 	add	x9, x10, x8, lsl #1
   1084c:	9100e18a 	add	x10, x12, #0x38
   10850:	9100e3eb 	add	x11, sp, #0x38
   10854:	8b090369 	add	x9, x27, x9
   10858:	14000005 	b	1086c <zbtIndexScanSlot+0x4e0>
   1085c:	d100dd4c 	sub	x12, x10, #0x37
   10860:	9100054a 	add	x10, x10, #0x1
   10864:	eb08019f 	cmp	x12, x8
   10868:	54000322 	b.cs	108cc <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   1086c:	386a692c 	ldrb	w12, [x9, x10]
   10870:	7100059f 	cmp	w12, #0x1
   10874:	54ffff48 	b.hi	1085c <zbtIndexScanSlot+0x4d0>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10878:	110006ac 	add	w12, w21, #0x1
   1087c:	5100e14d 	sub	w13, w10, #0x38
   10880:	b835596d 	str	w13, [x11, w21, uxtw #2]
   10884:	2a0c03f5 	mov	w21, w12
   10888:	17fffff5 	b	1085c <zbtIndexScanSlot+0x4d0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   1088c:	9100e18b 	add	x11, x12, #0x38
   10890:	8b0d036a 	add	x10, x27, x13
   10894:	9100e3ec 	add	x12, sp, #0x38
   10898:	14000005 	b	108ac <zbtIndexScanSlot+0x520>
   1089c:	d100dd6d 	sub	x13, x11, #0x37
   108a0:	9100056b 	add	x11, x11, #0x1
   108a4:	eb0801bf 	cmp	x13, x8
   108a8:	54000122 	b.cs	108cc <zbtIndexScanSlot+0x540>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   108ac:	386b694d 	ldrb	w13, [x10, x11]
   108b0:	6b0901bf 	cmp	w13, w9
   108b4:	54ffff41 	b.ne	1089c <zbtIndexScanSlot+0x510>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   108b8:	110006ad 	add	w13, w21, #0x1
   108bc:	5100e16e 	sub	w14, w11, #0x38
   108c0:	b835598e 	str	w14, [x12, w21, uxtw #2]
   108c4:	2a0d03f5 	mov	w21, w13
   108c8:	17fffff5 	b	1089c <zbtIndexScanSlot+0x510>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   108cc:	34001895 	cbz	w21, 10bdc <zbtIndexScanSlot+0x850>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   108d0:	f100027f 	cmp	x19, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   108d4:	2a1503e8 	mov	w8, w21
   108d8:	aa1f03f6 	mov	x22, xzr
   108dc:	7a410aa0 	ccmp	w21, #0x1, #0x0, eq	// eq = none
   108e0:	aa1f03f9 	mov	x25, xzr
   108e4:	a9028fe8 	stp	x8, x3, [sp, #40]
   108e8:	1a9f07e8 	cset	w8, ne	// ne = any
   108ec:	f90007fc 	str	x28, [sp, #8]
   108f0:	b90027e8 	str	w8, [sp, #36]
   108f4:	b90017f4 	str	w20, [sp, #20]
   108f8:	1400001b 	b	10964 <zbtIndexScanSlot+0x5d8>
   108fc:	2a0803eb 	mov	w11, w8
   10900:	9280000c 	mov	x12, #0xffffffffffffffff    	// #-1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   10904:	7101011f 	cmp	w8, #0x40
   10908:	9acb218b 	lsl	x11, x12, x11
   1090c:	da8b2188 	csinv	x8, x12, x11, cs	// cs = hs, nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10910:	39404f6b 	ldrb	w11, [x27, #19]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   10914:	8a080148 	and	x8, x10, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10918:	9acb2108 	lsl	x8, x8, x11
   1091c:	f940176a 	ldr	x10, [x27, #40]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10920:	7100013f 	cmp	w9, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   10924:	aa1803e0 	mov	x0, x24
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10928:	da880508 	cneg	x8, x8, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   1092c:	aa1c03e1 	mov	x1, x28
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10930:	8b080148 	add	x8, x10, x8
zbtOrderedToScore():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:331
    if (ordered & (UINT64_C(1) << 63))
   10934:	9240f909 	and	x9, x8, #0x7fffffffffffffff
   10938:	f100011f 	cmp	x8, #0x0
   1093c:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:335
    memcpy(&score, &bits, sizeof(score));
   10940:	9e670100 	fmov	d0, x8
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   10944:	d63f01e0 	blr	x15
   10948:	f94007fc 	ldr	x28, [sp, #8]
   1094c:	f9401be3 	ldr	x3, [sp, #48]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4219
        emitted++;
   10950:	91000739 	add	x25, x25, #0x1
   10954:	f94017e8 	ldr	x8, [sp, #40]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   10958:	910006d6 	add	x22, x22, #0x1
   1095c:	eb0802df 	cmp	x22, x8
   10960:	540014c0 	b.eq	10bf8 <zbtIndexScanSlot+0x86c>  // b.none
   10964:	9100e3e8 	add	x8, sp, #0x38
   10968:	b876791a 	ldr	w26, [x8, x22, lsl #2]
   1096c:	b94027e8 	ldr	w8, [sp, #36]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4207
        if (count > 1 || home_end) {
   10970:	340008a8 	cbz	w8, 10a84 <zbtIndexScanSlot+0x6f8>
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10974:	3940d368 	ldrb	w8, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10978:	b40000c8 	cbz	x8, 10990 <zbtIndexScanSlot+0x604>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   1097c:	39404769 	ldrb	w9, [x27, #17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10980:	1b085128 	madd	w8, w9, w8, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10984:	53037d08 	lsr	w8, w8, #3
   10988:	11002508 	add	w8, w8, #0x9
   1098c:	927f3508 	and	x8, x8, #0x7ffe
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10990:	3940d76a 	ldrb	w10, [x27, #53]
   10994:	2a1a03e9 	mov	w9, w26
   10998:	3400008a 	cbz	w10, 109a8 <zbtIndexScanSlot+0x61c>
   1099c:	39404769 	ldrb	w9, [x27, #17]
   109a0:	2a3a03ea 	mvn	w10, w26
   109a4:	0b0a0129 	add	w9, w9, w10
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   109a8:	8b080068 	add	x8, x3, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   109ac:	78695908 	ldrh	w8, [x8, w9, uxtw #1]
zbtScoreLeafRecord():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   109b0:	8b080368 	add	x8, x27, x8
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:625
    if (record[0] == ZBT_PACKED_EXTERNAL)
   109b4:	39400101 	ldrb	w1, [x8]
   109b8:	7103f83f 	cmp	w1, #0xfe
   109bc:	540000e0 	b.eq	109d8 <zbtIndexScanSlot+0x64c>  // b.none
   109c0:	7103fc3f 	cmp	w1, #0xff
   109c4:	54000101 	b.ne	109e4 <zbtIndexScanSlot+0x658>  // b.any
zbtExternalHash():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:561
    memcpy(&hash, record + ZBT_EXTERNAL_HASH_OFFSET, sizeof(hash));
   109c8:	b8401109 	ldur	w9, [x8, #1]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   109cc:	f9400788 	ldr	x8, [x28, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   109d0:	b5000193 	cbnz	x19, 10a00 <zbtIndexScanSlot+0x674>
   109d4:	14000012 	b	10a1c <zbtIndexScanSlot+0x690>
zbtPackedData():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   109d8:	78401101 	ldurh	w1, [x8, #1]
   109dc:	52800069 	mov	w9, #0x3                   	// #3
   109e0:	14000002 	b	109e8 <zbtIndexScanSlot+0x65c>
   109e4:	52800029 	mov	w9, #0x1                   	// #1
   109e8:	8b090100 	add	x0, x8, x9
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:629
    return (uint32_t)dictGenHashFunction(ele, len);
   109ec:	94000124 	bl	10e7c <dictGenHashFunction>
   109f0:	f9401be3 	ldr	x3, [sp, #48]
   109f4:	92407c09 	and	x9, x0, #0xffffffff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   109f8:	f9400788 	ldr	x8, [x28, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   109fc:	b4000113 	cbz	x19, 10a1c <zbtIndexScanSlot+0x690>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10a00:	5100050a 	sub	w10, w8, #0x1
   10a04:	f94003eb 	ldr	x11, [sp]
   10a08:	8a09014a 	and	x10, x10, x9
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10a0c:	eb0b015f 	cmp	x10, x11
   10a10:	54fffa23 	b.cc	10954 <zbtIndexScanSlot+0x5c8>  // b.lo, b.ul, b.last
   10a14:	eb13015f 	cmp	x10, x19
   10a18:	54fff9e2 	b.cs	10954 <zbtIndexScanSlot+0x5c8>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4212
            if (count > 1 && !zbtIndexHashReachesBucket(table, hash, bucket))
   10a1c:	710006bf 	cmp	w21, #0x1
   10a20:	54000320 	b.eq	10a84 <zbtIndexScanSlot+0x6f8>  // b.none
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10a24:	b4fff988 	cbz	x8, 10954 <zbtIndexScanSlot+0x5c8>
   10a28:	b940238c 	ldr	w12, [x28, #32]
   10a2c:	d100050a 	sub	x10, x8, #0x1
   10a30:	f940038b 	ldr	x11, [x28]
   10a34:	5280040d 	mov	w13, #0x20                  	// #32
   10a38:	7100019f 	cmp	w12, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4102
    unsigned long index = hash & mask;
   10a3c:	8a09014c 	and	x12, x10, x9
   10a40:	52800609 	mov	w9, #0x30                  	// #48
   10a44:	9a8901a9 	csel	x9, x13, x9, eq	// eq = none
zbtIndexBucketAt():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1759
    return (zbtIndexBucket *)((unsigned char *)table->buckets +
   10a48:	9b092d8d 	madd	x13, x12, x9, x11
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4106
        if (bucket == target) return 1;
   10a4c:	eb1701bf 	cmp	x13, x23
   10a50:	540001a0 	b.eq	10a84 <zbtIndexScanSlot+0x6f8>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   10a54:	f94001ad 	ldr	x13, [x13]
zbtIndexTagMask():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10a58:	b207dbee 	mov	x14, #0xfefefefefefefefe    	// #-72340172838076674
   10a5c:	f29fdfee 	movk	x14, #0xfeff
   10a60:	8b0e01ae 	add	x14, x13, x14
   10a64:	8a2d01cd 	bic	x13, x14, x13
   10a68:	f201c1bf 	tst	x13, #0x8080808080808080
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   10a6c:	54fff741 	b.ne	10954 <zbtIndexScanSlot+0x5c8>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10a70:	9100058c 	add	x12, x12, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10a74:	f1000508 	subs	x8, x8, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10a78:	8a0a018c 	and	x12, x12, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10a7c:	54fffe61 	b.ne	10a48 <zbtIndexScanSlot+0x6bc>  // b.any
   10a80:	17ffffb5 	b	10954 <zbtIndexScanSlot+0x5c8>
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10a84:	3940d368 	ldrb	w8, [x27, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10a88:	34000668 	cbz	w8, 10b54 <zbtIndexScanSlot+0x7c8>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10a8c:	39404769 	ldrb	w9, [x27, #17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10a90:	1b085129 	madd	w9, w9, w8, w20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10a94:	53037d29 	lsr	w9, w9, #3
   10a98:	11002529 	add	w9, w9, #0x9
   10a9c:	927f352a 	and	x10, x9, #0x7ffe
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10aa0:	3940d769 	ldrb	w9, [x27, #53]
   10aa4:	aa1803f4 	mov	x20, x24
   10aa8:	2a1a03eb 	mov	w11, w26
   10aac:	34000089 	cbz	w9, 10abc <zbtIndexScanSlot+0x730>
   10ab0:	3940476b 	ldrb	w11, [x27, #17]
   10ab4:	2a3a03ec 	mvn	w12, w26
   10ab8:	0b0c016b 	add	w11, w11, w12
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10abc:	8b0a006a 	add	x10, x3, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   10ac0:	786b594a 	ldrh	w10, [x10, w11, uxtw #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   10ac4:	8b0a0378 	add	x24, x27, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:589
    if (record[0] < ZBT_PACKED_SHORT) {
   10ac8:	39400302 	ldrb	w2, [x24]
   10acc:	7103f45f 	cmp	w2, #0xfd
   10ad0:	540000a8 	b.hi	10ae4 <zbtIndexScanSlot+0x758>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:591
        return record + 1;
   10ad4:	9100071c 	add	x28, x24, #0x1
   10ad8:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10adc:	35000108 	cbnz	w8, 10afc <zbtIndexScanSlot+0x770>
   10ae0:	1400003b 	b	10bcc <zbtIndexScanSlot+0x840>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:592
    } else if (record[0] == ZBT_PACKED_SHORT) {
   10ae4:	7103f85f 	cmp	w2, #0xfe
   10ae8:	54000421 	b.ne	10b6c <zbtIndexScanSlot+0x7e0>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   10aec:	78401302 	ldurh	w2, [x24, #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:596
        return record + 3;
   10af0:	91000f1c 	add	x28, x24, #0x3
   10af4:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10af8:	340006a8 	cbz	w8, 10bcc <zbtIndexScanSlot+0x840>
   10afc:	f9400fef 	ldr	x15, [sp, #24]
   10b00:	b94017f4 	ldr	w20, [sp, #20]
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10b04:	34000089 	cbz	w9, 10b14 <zbtIndexScanSlot+0x788>
   10b08:	3940476a 	ldrb	w10, [x27, #17]
   10b0c:	2a3a03eb 	mvn	w11, w26
   10b10:	0b0b015a 	add	w26, w10, w11
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:504
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
   10b14:	9ba87f4a 	umull	x10, w26, w8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:505
        size_t byte = bitpos / 8;
   10b18:	d343fd4b 	lsr	x11, x10, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10b1c:	9240094e 	and	x14, x10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:506
        unsigned int shift = bitpos & 7;
   10b20:	7200094c 	ands	w12, w10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:507
        memcpy(&delta, leaf->data + byte, sizeof(delta));
   10b24:	f86b686d 	ldr	x13, [x3, x11]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10b28:	9ace25aa 	lsr	x10, x13, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:509
        if (shift && bits > 64 - shift)
   10b2c:	54ffee80 	b.eq	108fc <zbtIndexScanSlot+0x570>  // b.none
   10b30:	5280080d 	mov	w13, #0x40                  	// #64
   10b34:	4b0c01ac 	sub	w12, w13, w12
   10b38:	6b08019f 	cmp	w12, w8
   10b3c:	54ffee02 	b.cs	108fc <zbtIndexScanSlot+0x570>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:510
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
   10b40:	8b1b016b 	add	x11, x11, x27
   10b44:	3941016b 	ldrb	w11, [x11, #64]
   10b48:	9acc216b 	lsl	x11, x11, x12
   10b4c:	aa0a016a 	orr	x10, x11, x10
   10b50:	17ffff6b 	b	108fc <zbtIndexScanSlot+0x570>
   10b54:	aa1f03ea 	mov	x10, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10b58:	3940d769 	ldrb	w9, [x27, #53]
   10b5c:	aa1803f4 	mov	x20, x24
   10b60:	2a1a03eb 	mov	w11, w26
   10b64:	35fffa69 	cbnz	w9, 10ab0 <zbtIndexScanSlot+0x724>
   10b68:	17ffffd5 	b	10abc <zbtIndexScanSlot+0x730>
zbtExternalPointer():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:576
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
   10b6c:	f840d31c 	ldur	x28, [x24, #13]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:599
        serverAssert(ptr != NULL);
   10b70:	b500025c 	cbnz	x28, 10bb8 <zbtIndexScanSlot+0x82c>
   10b74:	b0000000 	adrp	x0, 11000 <sdsnew+0x88>
   10b78:	912ef000 	add	x0, x0, #0xbbc
   10b7c:	52804ae1 	mov	w1, #0x257                 	// #599
   10b80:	b0000002 	adrp	x2, 11000 <sdsnew+0x88>
   10b84:	9133a042 	add	x2, x2, #0xce8
   10b88:	94000025 	bl	10c1c <standalone_panic>
zbtExternalLength():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:567
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
   10b8c:	39400308 	ldrb	w8, [x24]
   10b90:	f9401be3 	ldr	x3, [sp, #48]
   10b94:	7103fd1f 	cmp	w8, #0xff
   10b98:	54000100 	b.eq	10bb8 <zbtIndexScanSlot+0x82c>  // b.none
   10b9c:	b0000000 	adrp	x0, 11000 <sdsnew+0x88>
   10ba0:	912ef000 	add	x0, x0, #0xbbc
   10ba4:	528046e1 	mov	w1, #0x237                 	// #567
   10ba8:	b0000002 	adrp	x2, 11000 <sdsnew+0x88>
   10bac:	9133d042 	add	x2, x2, #0xcf4
   10bb0:	9400001b 	bl	10c1c <standalone_panic>
   10bb4:	f9401be3 	ldr	x3, [sp, #48]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:568
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
   10bb8:	f8405302 	ldur	x2, [x24, #5]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:500
    unsigned int bits = leaf->score_bits;
   10bbc:	3940d368 	ldrb	w8, [x27, #52]
   10bc0:	3940d769 	ldrb	w9, [x27, #53]
   10bc4:	aa1403f8 	mov	x24, x20
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10bc8:	35fff9a8 	cbnz	w8, 10afc <zbtIndexScanSlot+0x770>
   10bcc:	f9400fef 	ldr	x15, [sp, #24]
   10bd0:	b94017f4 	ldr	w20, [sp, #20]
   10bd4:	aa1f03e8 	mov	x8, xzr
   10bd8:	17ffff51 	b	1091c <zbtIndexScanSlot+0x590>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   10bdc:	b0000000 	adrp	x0, 11000 <sdsnew+0x88>
   10be0:	912ef000 	add	x0, x0, #0xbbc
   10be4:	d0000002 	adrp	x2, 12000 <_IO_stdin_used+0xa40>
   10be8:	9104cc42 	add	x2, x2, #0x133
   10bec:	52820cc1 	mov	w1, #0x1066                	// #4198
   10bf0:	9400000b 	bl	10c1c <standalone_panic>
   10bf4:	aa1f03f9 	mov	x25, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   10bf8:	aa190268 	orr	x8, x19, x25
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/009-scan-profile/build/src/zset_btree.c:4221
    serverAssert(home_end || emitted != 0);
   10bfc:	b5ffcfc8 	cbnz	x8, 105f4 <zbtIndexScanSlot+0x268>
   10c00:	b0000000 	adrp	x0, 11000 <sdsnew+0x88>
   10c04:	912ef000 	add	x0, x0, #0xbbc
   10c08:	d0000002 	adrp	x2, 12000 <_IO_stdin_used+0xa40>
   10c0c:	9104f842 	add	x2, x2, #0x13e
   10c10:	52820fa1 	mov	w1, #0x107d                	// #4221
   10c14:	94000002 	bl	10c1c <standalone_panic>
   10c18:	17fffe77 	b	105f4 <zbtIndexScanSlot+0x268>

