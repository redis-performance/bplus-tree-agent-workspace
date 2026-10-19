0000000000010574 <zbtIndexScanSlot>:
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4166
{
   10574:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
   10578:	a9016ffc 	stp	x28, x27, [sp, #16]
   1057c:	a90267fa 	stp	x26, x25, [sp, #32]
   10580:	a9035ff8 	stp	x24, x23, [sp, #48]
   10584:	a90457f6 	stp	x22, x21, [sp, #64]
   10588:	a9054ff4 	stp	x20, x19, [sp, #80]
   1058c:	910003fd 	mov	x29, sp
   10590:	d106c3ff 	sub	sp, sp, #0x1b0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   10594:	f9400048 	ldr	x8, [x2]
   10598:	531d7069 	lsl	w9, w3, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4168
    uint32_t id = zbtIndexGetId(table, bucket, slot_pos);
   1059c:	b940202a 	ldr	w10, [x1, #32]
   105a0:	aa0503f5 	mov	x21, x5
   105a4:	aa0203f7 	mov	x23, x2
   105a8:	a9019fe6 	stp	x6, x7, [sp, #24]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   105ac:	9ac92509 	lsr	x9, x8, x9
   105b0:	2a0303e8 	mov	w8, w3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1775
    if (table->wide_ids) return bucket->wide.id[pos];
   105b4:	340000ea 	cbz	w10, 105d0 <zbtIndexScanSlot+0x5c>
   105b8:	8b080ae8 	add	x8, x23, x8, lsl #2
   105bc:	b9401108 	ldr	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   105c0:	f2401d2c 	ands	x12, x9, #0xff
   105c4:	aa1f03f9 	mov	x25, xzr
   105c8:	54000141 	b.ne	105f0 <zbtIndexScanSlot+0x7c>  // b.any
   105cc:	14000072 	b	10794 <zbtIndexScanSlot+0x220>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1776
    uint16_t id = bucket->narrow.id[pos];
   105d0:	8b0806e8 	add	x8, x23, x8, lsl #1
   105d4:	529fffeb 	mov	w11, #0xffff                	// #65535
   105d8:	79402108 	ldrh	w8, [x8, #16]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1777
    return id == UINT16_MAX ? ZBT_INDEX_DELETED_ID : id;
   105dc:	6b0b011f 	cmp	w8, w11
   105e0:	5a9f1108 	csinv	w8, w8, wzr, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   105e4:	f2401d2c 	ands	x12, x9, #0xff
   105e8:	aa1f03f9 	mov	x25, xzr
   105ec:	54000d40 	b.eq	10794 <zbtIndexScanSlot+0x220>  // b.none
   105f0:	3100051f 	cmn	w8, #0x1
   105f4:	54000d00 	b.eq	10794 <zbtIndexScanSlot+0x220>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   105f8:	b4000475 	cbz	x21, 10684 <zbtIndexScanSlot+0x110>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   105fc:	eb15009f 	cmp	x4, x21
   10600:	aa0403eb 	mov	x11, x4
   10604:	540003c2 	b.cs	1067c <zbtIndexScanSlot+0x108>  // b.hs, b.nlast
   10608:	d28f82ab 	mov	x11, #0x7c15                	// #31765
   1060c:	7100015f 	cmp	w10, #0x0
   10610:	5280060a 	mov	w10, #0x30                  	// #48
   10614:	f2afe94b 	movk	x11, #0x7f4a, lsl #16
   10618:	5280040d 	mov	w13, #0x20                  	// #32
   1061c:	f940002e 	ldr	x14, [x1]
   10620:	f2cf372b 	movk	x11, #0x79b9, lsl #32
   10624:	9a8a01aa 	csel	x10, x13, x10, eq	// eq = none
   10628:	5280002f 	mov	w15, #0x1                   	// #1
   1062c:	f2f3c6eb 	movk	x11, #0x9e37, lsl #48
   10630:	9b04394e 	madd	x14, x10, x4, x14
   10634:	9ac921f0 	lsl	x16, x15, x9
   10638:	9b0b7d8b 	mul	x11, x12, x11
   1063c:	910021ce 	add	x14, x14, #0x8
   10640:	d37afd6d 	lsr	x13, x11, #58
   10644:	d364fd6b 	lsr	x11, x11, #36
   10648:	9acd21ed 	lsl	x13, x15, x13
   1064c:	9acb21eb 	lsl	x11, x15, x11
   10650:	aa1001ad 	orr	x13, x13, x16
   10654:	aa0b01ad 	orr	x13, x13, x11
   10658:	aa0403eb 	mov	x11, x4
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4174
            if ((*zbtIndexHomeTagsAt(table, home) & bits) == bits) break;
   1065c:	f94001cf 	ldr	x15, [x14]
   10660:	ea2f01bf 	bics	xzr, x13, x15
   10664:	540000c0 	b.eq	1067c <zbtIndexScanSlot+0x108>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   10668:	9100056b 	add	x11, x11, #0x1
   1066c:	8b0a01ce 	add	x14, x14, x10
   10670:	eb0b02bf 	cmp	x21, x11
   10674:	54ffff41 	b.ne	1065c <zbtIndexScanSlot+0xe8>  // b.any
   10678:	14000046 	b	10790 <zbtIndexScanSlot+0x21c>
   1067c:	eb15017f 	cmp	x11, x21
   10680:	54000880 	b.eq	10790 <zbtIndexScanSlot+0x21c>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4178
    zbtScoreLeaf *leaf = id < zs->next_score_leaf_id ?
   10684:	b940540a 	ldr	w10, [x0, #84]
   10688:	6b0a011f 	cmp	w8, w10
   1068c:	54000782 	b.cs	1077c <zbtIndexScanSlot+0x208>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4179
        zs->score_leaf_by_id[id] : NULL;
   10690:	f940240a 	ldr	x10, [x0, #72]
   10694:	f868595a 	ldr	x26, [x10, w8, uxtw #3]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4180
    if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {
   10698:	b400073a 	cbz	x26, 1077c <zbtIndexScanSlot+0x208>
   1069c:	3700071a 	tbnz	w26, #0, 1077c <zbtIndexScanSlot+0x208>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4184
    serverAssert(leaf->id == id);
   106a0:	b940334a 	ldr	w10, [x26, #48]
   106a4:	6b08015f 	cmp	w10, w8
   106a8:	54003481 	b.ne	10d38 <zbtIndexScanSlot+0x7c4>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4185
    if (zs->member_rehash) {
   106ac:	f9402008 	ldr	x8, [x0, #64]
   106b0:	b4000128 	cbz	x8, 106d4 <zbtIndexScanSlot+0x160>
zbtIndexLeafMigrated():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:2086
           leaf->n.index_resize == zs->member_rehash->resize_id;
   106b4:	79402f4a 	ldrh	w10, [x26, #22]
   106b8:	7940590b 	ldrh	w11, [x8, #44]
   106bc:	6b0b015f 	cmp	w10, w11
   106c0:	1a9f17ea 	cset	w10, eq	// eq = none
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4187
        if (in_new != zbtIndexLeafMigrated(zs, leaf)) return 0;
   106c4:	eb01011f 	cmp	x8, x1
   106c8:	1a9f07e8 	cset	w8, ne	// ne = any
   106cc:	6b0a011f 	cmp	w8, w10
   106d0:	54000600 	b.eq	10790 <zbtIndexScanSlot+0x21c>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   106d4:	3940d34a 	ldrb	w10, [x26, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:363
    return (uint8_t *)(zbtScoreLeafOffsets(leaf) + leaf->n.count);
   106d8:	39404748 	ldrb	w8, [x26, #17]
   106dc:	528000ef 	mov	w15, #0x7                   	// #7
zbtScoreLeafScoreBytes():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   106e0:	b40000aa 	cbz	x10, 106f4 <zbtIndexScanSlot+0x180>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   106e4:	1b0a3d0a 	madd	w10, w8, w10, w15
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   106e8:	53037d4a 	lsr	w10, w10, #3
   106ec:	1100254a 	add	w10, w10, #0x9
   106f0:	927f354a 	and	x10, x10, #0x7ffe
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   106f4:	3940d74b 	ldrb	w11, [x26, #53]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   106f8:	7100211f 	cmp	w8, #0x8
   106fc:	12001d29 	and	w9, w9, #0xff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10700:	9100e343 	add	x3, x26, #0x38
   10704:	a90007e4 	stp	x4, x1, [sp]
   10708:	b90017ef 	str	w15, [sp, #20]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   1070c:	54000562 	b.cs	107b8 <zbtIndexScanSlot+0x244>  // b.hs, b.nlast
   10710:	2a1f03fc 	mov	w28, wzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10714:	7200091f 	tst	w8, #0x7
   10718:	540019e0 	b.eq	10a54 <zbtIndexScanSlot+0x4e0>  // b.none
   1071c:	7100053f 	cmp	w9, #0x1
   10720:	927d110c 	and	x12, x8, #0xf8
   10724:	540009e1 	b.ne	10860 <zbtIndexScanSlot+0x2ec>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10728:	3400154b 	cbz	w11, 109d0 <zbtIndexScanSlot+0x45c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   1072c:	2a2803e9 	mvn	w9, w8
   10730:	8b08054a 	add	x10, x10, x8, lsl #1
   10734:	9100e18c 	add	x12, x12, #0x38
   10738:	32186929 	orr	w9, w9, #0xffffff07
   1073c:	9100a3eb 	add	x11, sp, #0x28
   10740:	0b080129 	add	w9, w9, w8
   10744:	8b0a034a 	add	x10, x26, x10
   10748:	14000006 	b	10760 <zbtIndexScanSlot+0x1ec>
   1074c:	d100dd8d 	sub	x13, x12, #0x37
   10750:	9100058c 	add	x12, x12, #0x1
   10754:	51000529 	sub	w9, w9, #0x1
   10758:	eb0801bf 	cmp	x13, x8
   1075c:	540017c2 	b.cs	10a54 <zbtIndexScanSlot+0x4e0>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10760:	386c694d 	ldrb	w13, [x10, x12]
   10764:	710005bf 	cmp	w13, #0x1
   10768:	54ffff28 	b.hi	1074c <zbtIndexScanSlot+0x1d8>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   1076c:	1100078d 	add	w13, w28, #0x1
   10770:	b83c5969 	str	w9, [x11, w28, uxtw #2]
   10774:	2a0d03fc 	mov	w28, w13
   10778:	17fffff5 	b	1074c <zbtIndexScanSlot+0x1d8>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   1077c:	f9402008 	ldr	x8, [x0, #64]
   10780:	b4002d08 	cbz	x8, 10d20 <zbtIndexScanSlot+0x7ac>
   10784:	91006008 	add	x8, x0, #0x18
   10788:	eb01011f 	cmp	x8, x1
   1078c:	54002ca1 	b.ne	10d20 <zbtIndexScanSlot+0x7ac>  // b.any
   10790:	aa1f03f9 	mov	x25, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4223
}
   10794:	aa1903e0 	mov	x0, x25
   10798:	9106c3ff 	add	sp, sp, #0x1b0
   1079c:	a9454ff4 	ldp	x20, x19, [sp, #80]
   107a0:	a94457f6 	ldp	x22, x21, [sp, #64]
   107a4:	a9435ff8 	ldp	x24, x23, [sp, #48]
   107a8:	a94267fa 	ldp	x26, x25, [sp, #32]
   107ac:	a9416ffc 	ldp	x28, x27, [sp, #16]
   107b0:	a8c67bfd 	ldp	x29, x30, [sp], #96
   107b4:	d65f03c0 	ret
   107b8:	b200c3ed 	mov	x13, #0x101010101010101     	// #72340172838076673
   107bc:	9b0d7d8e 	mul	x14, x12, x13
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4195
    unsigned int count = zbtLeafTagMatches(zbtScoreLeafHashTags(leaf),
   107c0:	8b0a006c 	add	x12, x3, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4135
    unsigned int words = count / 8;
   107c4:	d343fd0d 	lsr	x13, x8, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4195
    unsigned int count = zbtLeafTagMatches(zbtScoreLeafHashTags(leaf),
   107c8:	8b08058c 	add	x12, x12, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   107cc:	3400074b 	cbz	w11, 108b4 <zbtIndexScanSlot+0x340>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   107d0:	7100053f 	cmp	w9, #0x1
   107d4:	5100050f 	sub	w15, w8, #0x1
   107d8:	54000be1 	b.ne	10954 <zbtIndexScanSlot+0x3e0>  // b.any
   107dc:	aa1f03ee 	mov	x14, xzr
   107e0:	2a1f03fc 	mov	w28, wzr
   107e4:	9100a3f0 	add	x16, sp, #0x28
   107e8:	14000004 	b	107f8 <zbtIndexScanSlot+0x284>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   107ec:	910005ce 	add	x14, x14, #0x1
   107f0:	eb0d01df 	cmp	x14, x13
   107f4:	54fff900 	b.eq	10714 <zbtIndexScanSlot+0x1a0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   107f8:	d37df1d1 	lsl	x17, x14, #3
   107fc:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   10800:	f29fdfe1 	movk	x1, #0xfeff
   10804:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10808:	d200c240 	eor	x0, x18, #0x101010101010101
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   1080c:	8b010000 	add	x0, x0, x1
   10810:	8b010241 	add	x1, x18, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10814:	aa010000 	orr	x0, x0, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10818:	8a320012 	bic	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   1081c:	f201c252 	ands	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10820:	540000a1 	b.ne	10834 <zbtIndexScanSlot+0x2c0>  // b.any
   10824:	17fffff2 	b	107ec <zbtIndexScanSlot+0x278>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10828:	d1000640 	sub	x0, x18, #0x1
   1082c:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10830:	54fffde0 	b.eq	107ec <zbtIndexScanSlot+0x278>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   10834:	dac00240 	rbit	x0, x18
   10838:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   1083c:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10840:	38604981 	ldrb	w1, [x12, w0, uxtw]
   10844:	7100043f 	cmp	w1, #0x1
   10848:	54ffff08 	b.hi	10828 <zbtIndexScanSlot+0x2b4>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   1084c:	11000781 	add	w1, w28, #0x1
   10850:	4b0001e0 	sub	w0, w15, w0
   10854:	b83c5a00 	str	w0, [x16, w28, uxtw #2]
   10858:	2a0103fc 	mov	w28, w1
   1085c:	17fffff3 	b	10828 <zbtIndexScanSlot+0x2b4>
   10860:	8b08054d 	add	x13, x10, x8, lsl #1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10864:	34000d8b 	cbz	w11, 10a14 <zbtIndexScanSlot+0x4a0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10868:	2a2803ea 	mvn	w10, w8
   1086c:	9100e18c 	add	x12, x12, #0x38
   10870:	8b0d034b 	add	x11, x26, x13
   10874:	3218694a 	orr	w10, w10, #0xffffff07
   10878:	9100a3ed 	add	x13, sp, #0x28
   1087c:	0b08014a 	add	w10, w10, w8
   10880:	14000006 	b	10898 <zbtIndexScanSlot+0x324>
   10884:	d100dd8e 	sub	x14, x12, #0x37
   10888:	9100058c 	add	x12, x12, #0x1
   1088c:	5100054a 	sub	w10, w10, #0x1
   10890:	eb0801df 	cmp	x14, x8
   10894:	54000e02 	b.cs	10a54 <zbtIndexScanSlot+0x4e0>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10898:	386c696e 	ldrb	w14, [x11, x12]
   1089c:	6b0901df 	cmp	w14, w9
   108a0:	54ffff21 	b.ne	10884 <zbtIndexScanSlot+0x310>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   108a4:	1100078e 	add	w14, w28, #0x1
   108a8:	b83c59aa 	str	w10, [x13, w28, uxtw #2]
   108ac:	2a0e03fc 	mov	w28, w14
   108b0:	17fffff5 	b	10884 <zbtIndexScanSlot+0x310>
   108b4:	aa1f03ef 	mov	x15, xzr
   108b8:	2a1f03fc 	mov	w28, wzr
   108bc:	9100a3f0 	add	x16, sp, #0x28
   108c0:	14000004 	b	108d0 <zbtIndexScanSlot+0x35c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   108c4:	910005ef 	add	x15, x15, #0x1
   108c8:	eb0d01ff 	cmp	x15, x13
   108cc:	54fff240 	b.eq	10714 <zbtIndexScanSlot+0x1a0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   108d0:	d37df1f1 	lsl	x17, x15, #3
   108d4:	b207dbe2 	mov	x2, #0xfefefefefefefefe    	// #-72340172838076674
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   108d8:	7100053f 	cmp	w9, #0x1
   108dc:	f29fdfe2 	movk	x2, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   108e0:	f8716992 	ldr	x18, [x12, x17]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   108e4:	ca0e0240 	eor	x0, x18, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   108e8:	8b020001 	add	x1, x0, x2
   108ec:	8b020242 	add	x2, x18, x2
   108f0:	8a200020 	bic	x0, x1, x0
   108f4:	8a320052 	bic	x18, x2, x18
   108f8:	9201c000 	and	x0, x0, #0x8080808080808080
   108fc:	9201c252 	and	x18, x18, #0x8080808080808080
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   10900:	aa120012 	orr	x18, x0, x18
   10904:	9a921012 	csel	x18, x0, x18, ne	// ne = any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10908:	b50000b2 	cbnz	x18, 1091c <zbtIndexScanSlot+0x3a8>
   1090c:	17ffffee 	b	108c4 <zbtIndexScanSlot+0x350>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10910:	d1000640 	sub	x0, x18, #0x1
   10914:	ea120012 	ands	x18, x0, x18
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   10918:	54fffd60 	b.eq	108c4 <zbtIndexScanSlot+0x350>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   1091c:	dac00240 	rbit	x0, x18
   10920:	7100053f 	cmp	w9, #0x1
   10924:	dac01000 	clz	x0, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   10928:	2a400e20 	orr	w0, w17, w0, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   1092c:	38604981 	ldrb	w1, [x12, w0, uxtw]
   10930:	7a400820 	ccmp	w1, #0x0, #0x0, eq	// eq = none
   10934:	1a9f17e2 	cset	w2, eq	// eq = none
   10938:	6b09003f 	cmp	w1, w9
   1093c:	7a401840 	ccmp	w2, #0x0, #0x0, ne	// ne = any
   10940:	54fffe80 	b.eq	10910 <zbtIndexScanSlot+0x39c>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   10944:	11000781 	add	w1, w28, #0x1
   10948:	b83c5a00 	str	w0, [x16, w28, uxtw #2]
   1094c:	2a0103fc 	mov	w28, w1
   10950:	17fffff0 	b	10910 <zbtIndexScanSlot+0x39c>
   10954:	aa1f03f0 	mov	x16, xzr
   10958:	2a1f03fc 	mov	w28, wzr
   1095c:	9100a3f1 	add	x17, sp, #0x28
   10960:	14000004 	b	10970 <zbtIndexScanSlot+0x3fc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   10964:	91000610 	add	x16, x16, #0x1
   10968:	eb0d021f 	cmp	x16, x13
   1096c:	54ffed40 	b.eq	10714 <zbtIndexScanSlot+0x1a0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   10970:	d37df212 	lsl	x18, x16, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10974:	b207dbe1 	mov	x1, #0xfefefefefefefefe    	// #-72340172838076674
   10978:	f29fdfe1 	movk	x1, #0xfeff
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   1097c:	f8726980 	ldr	x0, [x12, x18]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   10980:	ca0e0000 	eor	x0, x0, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10984:	8b010001 	add	x1, x0, x1
   10988:	8a200020 	bic	x0, x1, x0
   1098c:	f201c000 	ands	x0, x0, #0x8080808080808080
   10990:	540000a1 	b.ne	109a4 <zbtIndexScanSlot+0x430>  // b.any
   10994:	17fffff4 	b	10964 <zbtIndexScanSlot+0x3f0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4145
            mask &= mask - 1;
   10998:	d1000401 	sub	x1, x0, #0x1
   1099c:	ea000020 	ands	x0, x1, x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4141
        while (mask) {
   109a0:	54fffe20 	b.eq	10964 <zbtIndexScanSlot+0x3f0>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   109a4:	dac00001 	rbit	x1, x0
   109a8:	dac01021 	clz	x1, x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   109ac:	2a410e41 	orr	w1, w18, w1, lsr #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   109b0:	38614982 	ldrb	w2, [x12, w1, uxtw]
   109b4:	6b09005f 	cmp	w2, w9
   109b8:	54ffff01 	b.ne	10998 <zbtIndexScanSlot+0x424>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   109bc:	11000782 	add	w2, w28, #0x1
   109c0:	4b0101e1 	sub	w1, w15, w1
   109c4:	b83c5a21 	str	w1, [x17, w28, uxtw #2]
   109c8:	2a0203fc 	mov	w28, w2
   109cc:	17fffff3 	b	10998 <zbtIndexScanSlot+0x424>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   109d0:	8b080549 	add	x9, x10, x8, lsl #1
   109d4:	9100e18a 	add	x10, x12, #0x38
   109d8:	9100a3eb 	add	x11, sp, #0x28
   109dc:	8b090349 	add	x9, x26, x9
   109e0:	14000005 	b	109f4 <zbtIndexScanSlot+0x480>
   109e4:	d100dd4c 	sub	x12, x10, #0x37
   109e8:	9100054a 	add	x10, x10, #0x1
   109ec:	eb08019f 	cmp	x12, x8
   109f0:	54000322 	b.cs	10a54 <zbtIndexScanSlot+0x4e0>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   109f4:	386a692c 	ldrb	w12, [x9, x10]
   109f8:	7100059f 	cmp	w12, #0x1
   109fc:	54ffff48 	b.hi	109e4 <zbtIndexScanSlot+0x470>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10a00:	1100078c 	add	w12, w28, #0x1
   10a04:	5100e14d 	sub	w13, w10, #0x38
   10a08:	b83c596d 	str	w13, [x11, w28, uxtw #2]
   10a0c:	2a0c03fc 	mov	w28, w12
   10a10:	17fffff5 	b	109e4 <zbtIndexScanSlot+0x470>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   10a14:	9100e18b 	add	x11, x12, #0x38
   10a18:	8b0d034a 	add	x10, x26, x13
   10a1c:	9100a3ec 	add	x12, sp, #0x28
   10a20:	14000005 	b	10a34 <zbtIndexScanSlot+0x4c0>
   10a24:	d100dd6d 	sub	x13, x11, #0x37
   10a28:	9100056b 	add	x11, x11, #0x1
   10a2c:	eb0801bf 	cmp	x13, x8
   10a30:	54000122 	b.cs	10a54 <zbtIndexScanSlot+0x4e0>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   10a34:	386b694d 	ldrb	w13, [x10, x11]
   10a38:	6b0901bf 	cmp	w13, w9
   10a3c:	54ffff41 	b.ne	10a24 <zbtIndexScanSlot+0x4b0>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   10a40:	1100078d 	add	w13, w28, #0x1
   10a44:	5100e16e 	sub	w14, w11, #0x38
   10a48:	b83c598e 	str	w14, [x12, w28, uxtw #2]
   10a4c:	2a0d03fc 	mov	w28, w13
   10a50:	17fffff5 	b	10a24 <zbtIndexScanSlot+0x4b0>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   10a54:	340017fc 	cbz	w28, 10d50 <zbtIndexScanSlot+0x7dc>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   10a58:	f10002bf 	cmp	x21, #0x0
   10a5c:	aa1f03f4 	mov	x20, xzr
   10a60:	aa1f03f9 	mov	x25, xzr
   10a64:	7a410b80 	ccmp	w28, #0x1, #0x0, eq	// eq = none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   10a68:	2a1c03f6 	mov	w22, w28
   10a6c:	aa0303f3 	mov	x19, x3
   10a70:	1a9f07f8 	cset	w24, ne	// ne = any
   10a74:	14000017 	b	10ad0 <zbtIndexScanSlot+0x55c>
   10a78:	9280000c 	mov	x12, #0xffffffffffffffff    	// #-1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   10a7c:	7101011f 	cmp	w8, #0x40
   10a80:	9ac8218b 	lsl	x11, x12, x8
   10a84:	da8b2188 	csinv	x8, x12, x11, cs	// cs = hs, nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10a88:	39404f4b 	ldrb	w11, [x26, #19]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:511
        if (bits < 64)
   10a8c:	8a080148 	and	x8, x10, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   10a90:	9acb2108 	lsl	x8, x8, x11
   10a94:	f940174a 	ldr	x10, [x26, #40]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   10a98:	7100013f 	cmp	w9, #0x0
   10a9c:	da880508 	cneg	x8, x8, ne	// ne = any
   10aa0:	8b080148 	add	x8, x10, x8
zbtOrderedToScore():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:331
    if (ordered & (UINT64_C(1) << 63))
   10aa4:	9240f909 	and	x9, x8, #0x7fffffffffffffff
   10aa8:	f100011f 	cmp	x8, #0x0
   10aac:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:335
    memcpy(&score, &bits, sizeof(score));
   10ab0:	9e670100 	fmov	d0, x8
   10ab4:	a94183e8 	ldp	x8, x0, [sp, #24]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   10ab8:	d63f0100 	blr	x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4219
        emitted++;
   10abc:	91000739 	add	x25, x25, #0x1
   10ac0:	aa1303e3 	mov	x3, x19
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   10ac4:	91000694 	add	x20, x20, #0x1
   10ac8:	eb16029f 	cmp	x20, x22
   10acc:	540010e0 	b.eq	10ce8 <zbtIndexScanSlot+0x774>  // b.none
   10ad0:	9100a3e8 	add	x8, sp, #0x28
   10ad4:	b874791b 	ldr	w27, [x8, x20, lsl #2]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4207
        if (count > 1 || home_end) {
   10ad8:	34000938 	cbz	w24, 10bfc <zbtIndexScanSlot+0x688>
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10adc:	3940d348 	ldrb	w8, [x26, #52]
   10ae0:	b40000e8 	cbz	x8, 10afc <zbtIndexScanSlot+0x588>
   10ae4:	39404749 	ldrb	w9, [x26, #17]
   10ae8:	b94017ea 	ldr	w10, [sp, #20]
zbtScoreLeafScoreBytes():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10aec:	1b082928 	madd	w8, w9, w8, w10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10af0:	53037d08 	lsr	w8, w8, #3
   10af4:	11002508 	add	w8, w8, #0x9
   10af8:	927f3508 	and	x8, x8, #0x7ffe
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10afc:	3940d74a 	ldrb	w10, [x26, #53]
   10b00:	2a1b03e9 	mov	w9, w27
   10b04:	3400008a 	cbz	w10, 10b14 <zbtIndexScanSlot+0x5a0>
   10b08:	39404749 	ldrb	w9, [x26, #17]
   10b0c:	2a3b03ea 	mvn	w10, w27
   10b10:	0b0a0129 	add	w9, w9, w10
zbtScoreLeafOffset():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10b14:	8b080068 	add	x8, x3, x8
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   10b18:	78695908 	ldrh	w8, [x8, w9, uxtw #1]
zbtScoreLeafRecord():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   10b1c:	8b080348 	add	x8, x26, x8
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:625
    if (record[0] == ZBT_PACKED_EXTERNAL)
   10b20:	39400101 	ldrb	w1, [x8]
   10b24:	7103f83f 	cmp	w1, #0xfe
   10b28:	54000100 	b.eq	10b48 <zbtIndexScanSlot+0x5d4>  // b.none
   10b2c:	7103fc3f 	cmp	w1, #0xff
   10b30:	54000121 	b.ne	10b54 <zbtIndexScanSlot+0x5e0>  // b.any
zbtExternalHash():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:561
    memcpy(&hash, record + ZBT_EXTERNAL_HASH_OFFSET, sizeof(hash));
   10b34:	b8401109 	ldur	w9, [x8, #1]
   10b38:	f94007e8 	ldr	x8, [sp, #8]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10b3c:	f9400508 	ldr	x8, [x8, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10b40:	b50001b5 	cbnz	x21, 10b74 <zbtIndexScanSlot+0x600>
   10b44:	14000013 	b	10b90 <zbtIndexScanSlot+0x61c>
zbtPackedData():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   10b48:	78401101 	ldurh	w1, [x8, #1]
   10b4c:	52800069 	mov	w9, #0x3                   	// #3
   10b50:	14000002 	b	10b58 <zbtIndexScanSlot+0x5e4>
   10b54:	52800029 	mov	w9, #0x1                   	// #1
   10b58:	8b090100 	add	x0, x8, x9
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:629
    return (uint32_t)dictGenHashFunction(ele, len);
   10b5c:	94000103 	bl	10f68 <dictGenHashFunction>
   10b60:	92407c09 	and	x9, x0, #0xffffffff
   10b64:	aa1303e3 	mov	x3, x19
   10b68:	f94007e8 	ldr	x8, [sp, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10b6c:	f9400508 	ldr	x8, [x8, #8]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10b70:	b4000115 	cbz	x21, 10b90 <zbtIndexScanSlot+0x61c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   10b74:	5100050a 	sub	w10, w8, #0x1
   10b78:	f94003eb 	ldr	x11, [sp]
   10b7c:	8a09014a 	and	x10, x10, x9
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   10b80:	eb0b015f 	cmp	x10, x11
   10b84:	54fffa03 	b.cc	10ac4 <zbtIndexScanSlot+0x550>  // b.lo, b.ul, b.last
   10b88:	eb15015f 	cmp	x10, x21
   10b8c:	54fff9c2 	b.cs	10ac4 <zbtIndexScanSlot+0x550>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4212
            if (count > 1 && !zbtIndexHashReachesBucket(table, hash, bucket))
   10b90:	7100079f 	cmp	w28, #0x1
   10b94:	54000340 	b.eq	10bfc <zbtIndexScanSlot+0x688>  // b.none
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10b98:	b4fff968 	cbz	x8, 10ac4 <zbtIndexScanSlot+0x550>
   10b9c:	f94007eb 	ldr	x11, [sp, #8]
   10ba0:	d100050a 	sub	x10, x8, #0x1
   10ba4:	5280040d 	mov	w13, #0x20                  	// #32
   10ba8:	b940216c 	ldr	w12, [x11, #32]
   10bac:	f940016b 	ldr	x11, [x11]
   10bb0:	7100019f 	cmp	w12, #0x0
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4102
    unsigned long index = hash & mask;
   10bb4:	8a09014c 	and	x12, x10, x9
   10bb8:	52800609 	mov	w9, #0x30                  	// #48
   10bbc:	9a8901a9 	csel	x9, x13, x9, eq	// eq = none
zbtIndexBucketAt():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1759
    return (zbtIndexBucket *)((unsigned char *)table->buckets +
   10bc0:	9b092d8d 	madd	x13, x12, x9, x11
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4106
        if (bucket == target) return 1;
   10bc4:	eb1701bf 	cmp	x13, x23
   10bc8:	540001a0 	b.eq	10bfc <zbtIndexScanSlot+0x688>  // b.none
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   10bcc:	f94001ad 	ldr	x13, [x13]
zbtIndexTagMask():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   10bd0:	b207dbee 	mov	x14, #0xfefefefefefefefe    	// #-72340172838076674
   10bd4:	f29fdfee 	movk	x14, #0xfeff
   10bd8:	8b0e01ae 	add	x14, x13, x14
   10bdc:	8a2d01cd 	bic	x13, x14, x13
   10be0:	f201c1bf 	tst	x13, #0x8080808080808080
zbtIndexHashReachesBucket():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   10be4:	54fff701 	b.ne	10ac4 <zbtIndexScanSlot+0x550>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10be8:	9100058c 	add	x12, x12, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10bec:	f1000508 	subs	x8, x8, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4108
        index = (index + 1) & mask;
   10bf0:	8a0a018c 	and	x12, x12, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   10bf4:	54fffe61 	b.ne	10bc0 <zbtIndexScanSlot+0x64c>  // b.any
   10bf8:	17ffffb3 	b	10ac4 <zbtIndexScanSlot+0x550>
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10bfc:	3940d348 	ldrb	w8, [x26, #52]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:350
    if (score_bits == 0) return 0;
   10c00:	34000608 	cbz	w8, 10cc0 <zbtIndexScanSlot+0x74c>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   10c04:	39404749 	ldrb	w9, [x26, #17]
   10c08:	b94017ea 	ldr	w10, [sp, #20]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   10c0c:	1b082929 	madd	w9, w9, w8, w10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   10c10:	53037d29 	lsr	w9, w9, #3
   10c14:	11002529 	add	w9, w9, #0x9
   10c18:	927f352a 	and	x10, x9, #0x7ffe
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10c1c:	3940d749 	ldrb	w9, [x26, #53]
   10c20:	2a1b03eb 	mov	w11, w27
   10c24:	34000089 	cbz	w9, 10c34 <zbtIndexScanSlot+0x6c0>
   10c28:	3940474b 	ldrb	w11, [x26, #17]
   10c2c:	2a3b03ec 	mvn	w12, w27
   10c30:	0b0c016b 	add	w11, w11, w12
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   10c34:	8b0a006a 	add	x10, x3, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   10c38:	786b594a 	ldrh	w10, [x10, w11, uxtw #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   10c3c:	8b0a034a 	add	x10, x26, x10
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:589
    if (record[0] < ZBT_PACKED_SHORT) {
   10c40:	39400142 	ldrb	w2, [x10]
   10c44:	7103f45f 	cmp	w2, #0xfd
   10c48:	540002e8 	b.hi	10ca4 <zbtIndexScanSlot+0x730>  // b.pmore
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:591
        return record + 1;
   10c4c:	91000541 	add	x1, x10, #0x1
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10c50:	34000348 	cbz	w8, 10cb8 <zbtIndexScanSlot+0x744>
zbtScoreLeafPhysicalPos():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10c54:	34000089 	cbz	w9, 10c64 <zbtIndexScanSlot+0x6f0>
   10c58:	3940474a 	ldrb	w10, [x26, #17]
   10c5c:	2a3b03eb 	mvn	w11, w27
   10c60:	0b0b015b 	add	w27, w10, w11
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:504
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
   10c64:	9bbb7d0a 	umull	x10, w8, w27
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:505
        size_t byte = bitpos / 8;
   10c68:	d343fd4b 	lsr	x11, x10, #3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10c6c:	9240094e 	and	x14, x10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:506
        unsigned int shift = bitpos & 7;
   10c70:	7200094c 	ands	w12, w10, #0x7
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:507
        memcpy(&delta, leaf->data + byte, sizeof(delta));
   10c74:	f86b686d 	ldr	x13, [x3, x11]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   10c78:	9ace25aa 	lsr	x10, x13, x14
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:509
        if (shift && bits > 64 - shift)
   10c7c:	54ffefe0 	b.eq	10a78 <zbtIndexScanSlot+0x504>  // b.none
   10c80:	5280080d 	mov	w13, #0x40                  	// #64
   10c84:	4b0c01ac 	sub	w12, w13, w12
   10c88:	6b08019f 	cmp	w12, w8
   10c8c:	54ffef62 	b.cs	10a78 <zbtIndexScanSlot+0x504>  // b.hs, b.nlast
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:510
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
   10c90:	8b1a016b 	add	x11, x11, x26
   10c94:	3941016b 	ldrb	w11, [x11, #64]
   10c98:	9acc216b 	lsl	x11, x11, x12
   10c9c:	aa0a016a 	orr	x10, x11, x10
   10ca0:	17ffff76 	b	10a78 <zbtIndexScanSlot+0x504>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:592
    } else if (record[0] == ZBT_PACKED_SHORT) {
   10ca4:	7103f85f 	cmp	w2, #0xfe
   10ca8:	54000161 	b.ne	10cd4 <zbtIndexScanSlot+0x760>  // b.any
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   10cac:	78401142 	ldurh	w2, [x10, #1]
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:596
        return record + 3;
   10cb0:	91000d41 	add	x1, x10, #0x3
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10cb4:	35fffd08 	cbnz	w8, 10c54 <zbtIndexScanSlot+0x6e0>
   10cb8:	aa1f03e8 	mov	x8, xzr
   10cbc:	17ffff76 	b	10a94 <zbtIndexScanSlot+0x520>
   10cc0:	aa1f03ea 	mov	x10, xzr
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   10cc4:	3940d749 	ldrb	w9, [x26, #53]
   10cc8:	2a1b03eb 	mov	w11, w27
   10ccc:	35fffae9 	cbnz	w9, 10c28 <zbtIndexScanSlot+0x6b4>
   10cd0:	17ffffd9 	b	10c34 <zbtIndexScanSlot+0x6c0>
zbtExternalPointer():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:576
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
   10cd4:	f840d141 	ldur	x1, [x10, #13]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:599
        serverAssert(ptr != NULL);
   10cd8:	b4000181 	cbz	x1, 10d08 <zbtIndexScanSlot+0x794>
zbtExternalLength():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:568
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
   10cdc:	f8405142 	ldur	x2, [x10, #5]
zbtIndexScanSlot():
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:503
    if (bits != 0) {
   10ce0:	35fffba8 	cbnz	w8, 10c54 <zbtIndexScanSlot+0x6e0>
   10ce4:	17fffff5 	b	10cb8 <zbtIndexScanSlot+0x744>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4170
    if (home_end) {
   10ce8:	aa1902a8 	orr	x8, x21, x25
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4221
    serverAssert(home_end || emitted != 0);
   10cec:	b5ffd548 	cbnz	x8, 10794 <zbtIndexScanSlot+0x220>
   10cf0:	b0000000 	adrp	x0, 11000 <sdsnewlen+0x88>
   10cf4:	9130b000 	add	x0, x0, #0xc2c
   10cf8:	d0000002 	adrp	x2, 12000 <_IO_stdin_used+0x9d0>
   10cfc:	9106b842 	add	x2, x2, #0x1ae
   10d00:	52820fa1 	mov	w1, #0x107d                	// #4221
   10d04:	94000019 	bl	10d68 <standalone_panic>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:599
        serverAssert(ptr != NULL);
   10d08:	b0000000 	adrp	x0, 11000 <sdsnewlen+0x88>
   10d0c:	9130b000 	add	x0, x0, #0xc2c
   10d10:	b0000002 	adrp	x2, 11000 <sdsnewlen+0x88>
   10d14:	91356042 	add	x2, x2, #0xd58
   10d18:	52804ae1 	mov	w1, #0x257                 	// #599
   10d1c:	94000013 	bl	10d68 <standalone_panic>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   10d20:	b0000000 	adrp	x0, 11000 <sdsnewlen+0x88>
   10d24:	9130b000 	add	x0, x0, #0xc2c
   10d28:	b0000002 	adrp	x2, 11000 <sdsnewlen+0x88>
   10d2c:	91369042 	add	x2, x2, #0xda4
   10d30:	52820aa1 	mov	w1, #0x1055                	// #4181
   10d34:	9400000d 	bl	10d68 <standalone_panic>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4184
    serverAssert(leaf->id == id);
   10d38:	b0000000 	adrp	x0, 11000 <sdsnewlen+0x88>
   10d3c:	9130b000 	add	x0, x0, #0xc2c
   10d40:	b0000002 	adrp	x2, 11000 <sdsnewlen+0x88>
   10d44:	91361442 	add	x2, x2, #0xd85
   10d48:	52820b01 	mov	w1, #0x1058                	// #4184
   10d4c:	94000007 	bl	10d68 <standalone_panic>
<remote_repo>/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/build/src/zset_btree.c:4198
    serverAssert(count != 0);
   10d50:	b0000000 	adrp	x0, 11000 <sdsnewlen+0x88>
   10d54:	9130b000 	add	x0, x0, #0xc2c
   10d58:	d0000002 	adrp	x2, 12000 <_IO_stdin_used+0x9d0>
   10d5c:	91068c42 	add	x2, x2, #0x1a3
   10d60:	52820cc1 	mov	w1, #0x1066                	// #4198
   10d64:	94000001 	bl	10d68 <standalone_panic>

