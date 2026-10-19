
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/004-update/build/update-native:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

00000000000071e0 <zbtreeUpdateScore>:

/* Update an existing member's score. Its hash entry remains in place unless
 * the member lands in a different score leaf. */
void zbtreeUpdateScore(zbtreeSet *zs, sds ele, double score,
                       const zbtreeInsertPosition *position)
{
    71e0:	d10243ff 	sub	sp, sp, #0x90
    71e4:	fd001be8 	str	d8, [sp, #48]
    71e8:	a9047bfd 	stp	x29, x30, [sp, #64]
    71ec:	a90567fa 	stp	x26, x25, [sp, #80]
    71f0:	a9065ff8 	stp	x24, x23, [sp, #96]
    71f4:	a90757f6 	stp	x22, x21, [sp, #112]
    71f8:	a9084ff4 	stp	x20, x19, [sp, #128]
    71fc:	910103fd 	add	x29, sp, #0x40
    7200:	1e604008 	fmov	d8, d0
    uint32_t hash = position->hash;
    zbtScoreLeaf *oldleaf = position->score_leaf;
    unsigned int oldpos = position->score_pos;

    serverAssert(position->revision == zs->member_revision);
    7204:	b9405c09 	ldr	w9, [x0, #92]
    zbtScoreLeaf *oldleaf = position->score_leaf;
    7208:	f9400855 	ldr	x21, [x2, #16]
    serverAssert(position->revision == zs->member_revision);
    720c:	2943a054 	ldp	w20, w8, [x2, #28]
    unsigned int oldpos = position->score_pos;
    7210:	b9401856 	ldr	w22, [x2, #24]
    7214:	aa0003f3 	mov	x19, x0
    7218:	aa0103f7 	mov	x23, x1
    serverAssert(position->revision == zs->member_revision);
    721c:	6b09011f 	cmp	w8, w9
    7220:	540000e0 	b.eq	723c <zbtreeUpdateScore+0x5c>  // b.none
    7224:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    7228:	913e7c00 	add	x0, x0, #0xf9f
    722c:	b0000042 	adrp	x2, 10000 <zbtIndexScanSlot+0x614>
    7230:	913f6c42 	add	x2, x2, #0xfdb
    7234:	5281c841 	mov	w1, #0xe42                 	// #3650
    7238:	94002411 	bl	1027c <standalone_panic>
    serverAssert(oldleaf != NULL && oldpos < oldleaf->n.count);
    723c:	b40002b5 	cbz	x21, 7290 <zbtreeUpdateScore+0xb0>
    7240:	394046a8 	ldrb	w8, [x21, #17]
    7244:	6b0802df 	cmp	w22, w8
    7248:	54000242 	b.cs	7290 <zbtreeUpdateScore+0xb0>  // b.hs, b.nlast
    724c:	385ff2e9 	ldurb	w9, [x23, #-1]
    7250:	aa1f03e3 	mov	x3, xzr
#define SDS_HDR(T,s) ((struct sdshdr##T *)((s)-(sizeof(struct sdshdr##T))))
#define SDS_TYPE_5_LEN(s) (((unsigned char)(s[-1])) >> SDS_TYPE_BITS)

static inline unsigned char sdsType(sds s) {
    unsigned char flags = s[-1];
    return flags & SDS_TYPE_MASK;
    7254:	12000928 	and	w8, w9, #0x7
    }
    s[-1] = (char)flags;
}

static inline size_t sdslen(const sds s) {
    switch (sdsType(s)) {
    7258:	7100051f 	cmp	w8, #0x1
    725c:	540004cd 	b.le	72f4 <zbtreeUpdateScore+0x114>
    7260:	7100091f 	cmp	w8, #0x2
    7264:	540007e0 	b.eq	7360 <zbtreeUpdateScore+0x180>  // b.none
    7268:	71000d1f 	cmp	w8, #0x3
    726c:	54000301 	b.ne	72cc <zbtreeUpdateScore+0xec>  // b.any
        case SDS_TYPE_8:
            return SDS_HDR(8,s)->len;
        case SDS_TYPE_16:
            return SDS_HDR(16,s)->len;
        case SDS_TYPE_32:
            return SDS_HDR(32,s)->len;
    7270:	b85f72e3 	ldur	w3, [x23, #-9]

    /* Most small score changes preserve the member's position. In that case
     * only its packed score bits and the maxima on the path are changed. */
    if (zbtScoreUpdateInPlace(oldleaf, oldpos, score,
    7274:	1e604100 	fmov	d0, d8
    7278:	aa1503e0 	mov	x0, x21
    727c:	2a1603e1 	mov	w1, w22
    7280:	aa1703e2 	mov	x2, x23
    7284:	94000198 	bl	78e4 <zbtScoreUpdateInPlace>
    7288:	350031e0 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    728c:	1400003c 	b	737c <zbtreeUpdateScore+0x19c>
    serverAssert(oldleaf != NULL && oldpos < oldleaf->n.count);
    7290:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    7294:	913e7c00 	add	x0, x0, #0xf9f
    7298:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    729c:	91001442 	add	x2, x2, #0x5
    72a0:	5281c861 	mov	w1, #0xe43                 	// #3651
    72a4:	940023f6 	bl	1027c <standalone_panic>
    72a8:	385ff2e9 	ldurb	w9, [x23, #-1]
    72ac:	aa1f03e3 	mov	x3, xzr
    return flags & SDS_TYPE_MASK;
    72b0:	12000928 	and	w8, w9, #0x7
    switch (sdsType(s)) {
    72b4:	7100051f 	cmp	w8, #0x1
    72b8:	540001ed 	b.le	72f4 <zbtreeUpdateScore+0x114>
    72bc:	7100091f 	cmp	w8, #0x2
    72c0:	54000400 	b.eq	7340 <zbtreeUpdateScore+0x160>  // b.none
    72c4:	71000d1f 	cmp	w8, #0x3
    72c8:	54fffd40 	b.eq	7270 <zbtreeUpdateScore+0x90>  // b.none
    72cc:	7100111f 	cmp	w8, #0x4
    72d0:	540004a1 	b.ne	7364 <zbtreeUpdateScore+0x184>  // b.any
        case SDS_TYPE_64:
            return SDS_HDR(64,s)->len;
    72d4:	f85ef2e3 	ldur	x3, [x23, #-17]
    if (zbtScoreUpdateInPlace(oldleaf, oldpos, score,
    72d8:	1e604100 	fmov	d0, d8
    72dc:	aa1503e0 	mov	x0, x21
    72e0:	2a1603e1 	mov	w1, w22
    72e4:	aa1703e2 	mov	x2, x23
    72e8:	9400017f 	bl	78e4 <zbtScoreUpdateInPlace>
    72ec:	35002ec0 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    72f0:	14000023 	b	737c <zbtreeUpdateScore+0x19c>
    switch (sdsType(s)) {
    72f4:	34000168 	cbz	w8, 7320 <zbtreeUpdateScore+0x140>
    72f8:	7100051f 	cmp	w8, #0x1
    72fc:	54000341 	b.ne	7364 <zbtreeUpdateScore+0x184>  // b.any
            return SDS_HDR(8,s)->len;
    7300:	385fd2e3 	ldurb	w3, [x23, #-3]
    7304:	1e604100 	fmov	d0, d8
    7308:	aa1503e0 	mov	x0, x21
    730c:	2a1603e1 	mov	w1, w22
    7310:	aa1703e2 	mov	x2, x23
    7314:	94000174 	bl	78e4 <zbtScoreUpdateInPlace>
    7318:	35002d60 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    731c:	14000018 	b	737c <zbtreeUpdateScore+0x19c>
    7320:	d343fd23 	lsr	x3, x9, #3
    7324:	1e604100 	fmov	d0, d8
    7328:	aa1503e0 	mov	x0, x21
    732c:	2a1603e1 	mov	w1, w22
    7330:	aa1703e2 	mov	x2, x23
    7334:	9400016c 	bl	78e4 <zbtScoreUpdateInPlace>
    7338:	35002c60 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    733c:	14000010 	b	737c <zbtreeUpdateScore+0x19c>
            return SDS_HDR(16,s)->len;
    7340:	785fb2e3 	ldurh	w3, [x23, #-5]
    7344:	1e604100 	fmov	d0, d8
    7348:	aa1503e0 	mov	x0, x21
    734c:	2a1603e1 	mov	w1, w22
    7350:	aa1703e2 	mov	x2, x23
    7354:	94000164 	bl	78e4 <zbtScoreUpdateInPlace>
    7358:	35002b60 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    735c:	14000008 	b	737c <zbtreeUpdateScore+0x19c>
    7360:	785fb2e3 	ldurh	w3, [x23, #-5]
    7364:	1e604100 	fmov	d0, d8
    7368:	aa1503e0 	mov	x0, x21
    736c:	2a1603e1 	mov	w1, w22
    7370:	aa1703e2 	mov	x2, x23
    7374:	9400015c 	bl	78e4 <zbtScoreUpdateInPlace>
    7378:	35002a60 	cbnz	w0, 78c4 <zbtreeUpdateScore+0x6e4>
    if (zs->next_score_leaf_id < ZBT_INDEX_WIDE_ID_AT) return;
    737c:	b9405668 	ldr	w8, [x19, #84]
    7380:	528fffe9 	mov	w9, #0x7fff                	// #32767
    7384:	6b09011f 	cmp	w8, w9
    7388:	54000363 	b.cc	73f4 <zbtreeUpdateScore+0x214>  // b.lo, b.ul, b.last
    if (zs->member_rehash && !zs->member_rehash->table.wide_ids) {
    738c:	f9402269 	ldr	x9, [x19, #64]
    7390:	b4000229 	cbz	x9, 73d4 <zbtreeUpdateScore+0x1f4>
    7394:	b9402129 	ldr	w9, [x9, #32]
    7398:	350002e9 	cbnz	w9, 73f4 <zbtreeUpdateScore+0x214>
    739c:	529ffde9 	mov	w9, #0xffef                	// #65519
        if (zs->next_score_leaf_id < ZBT_INDEX_NARROW_ID_LIMIT)
    73a0:	6b09011f 	cmp	w8, w9
    73a4:	540000e2 	b.cs	73c0 <zbtreeUpdateScore+0x1e0>  // b.hs, b.nlast
            zbtIndexRehashStep(zs, ZBT_INDEX_WIDEN_STEPS);
    73a8:	aa1303e0 	mov	x0, x19
    73ac:	52800081 	mov	w1, #0x4                   	// #4
    73b0:	97fffd95 	bl	6a04 <zbtIndexRehashStep>
    if (zs->member_rehash == NULL && zs->member_index.size &&
    73b4:	f9402268 	ldr	x8, [x19, #64]
    73b8:	b50001e8 	cbnz	x8, 73f4 <zbtreeUpdateScore+0x214>
    73bc:	14000006 	b	73d4 <zbtreeUpdateScore+0x1f4>
            while (zs->member_rehash) zbtIndexRehashStep(zs, 64);
    73c0:	aa1303e0 	mov	x0, x19
    73c4:	52800801 	mov	w1, #0x40                  	// #64
    73c8:	97fffd8f 	bl	6a04 <zbtIndexRehashStep>
    73cc:	f9402268 	ldr	x8, [x19, #64]
    73d0:	b5ffff88 	cbnz	x8, 73c0 <zbtreeUpdateScore+0x1e0>
    if (zs->member_rehash == NULL && zs->member_index.size &&
    73d4:	f9401268 	ldr	x8, [x19, #32]
    73d8:	b40000e8 	cbz	x8, 73f4 <zbtreeUpdateScore+0x214>
        !zs->member_index.wide_ids)
    73dc:	b9403a68 	ldr	w8, [x19, #56]
    if (zs->member_rehash == NULL && zs->member_index.size &&
    73e0:	350000a8 	cbnz	w8, 73f4 <zbtreeUpdateScore+0x214>
        zbtIndexStartResize(zs, zs->member_index.used + add, 1);
    73e4:	f9401661 	ldr	x1, [x19, #40]
    73e8:	aa1303e0 	mov	x0, x19
    73ec:	52800022 	mov	w2, #0x1                   	// #1
    73f0:	94000c25 	bl	a484 <zbtIndexStartResize>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    73f4:	3940d2a8 	ldrb	w8, [x21, #52]
    if (score_bits == 0) return 0;
    73f8:	b40000e8 	cbz	x8, 7414 <zbtreeUpdateScore+0x234>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    73fc:	394046a9 	ldrb	w9, [x21, #17]
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
    7400:	528000ea 	mov	w10, #0x7                   	// #7
    7404:	1b082928 	madd	w8, w9, w8, w10
    return (bytes + 8 + 1) & ~(size_t)1;
    7408:	53037d08 	lsr	w8, w8, #3
    740c:	11002508 	add	w8, w8, #0x9
    7410:	927f3508 	and	x8, x8, #0x7ffe
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    7414:	3940d6aa 	ldrb	w10, [x21, #53]
    7418:	2a1603e9 	mov	w9, w22
    741c:	3400008a 	cbz	w10, 742c <zbtreeUpdateScore+0x24c>
    7420:	394046a9 	ldrb	w9, [x21, #17]
    7424:	2a3603ea 	mvn	w10, w22
    7428:	0b0a0129 	add	w9, w9, w10
    return (uint16_t *)(leaf->data +
    742c:	9100e2b8 	add	x24, x21, #0x38
    7430:	8b080308 	add	x8, x24, x8
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
    7434:	78695908 	ldrh	w8, [x8, w9, uxtw #1]
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
    7438:	8b0802b9 	add	x25, x21, x8
    if (record[0] < ZBT_PACKED_SHORT) {
    743c:	39400328 	ldrb	w8, [x25]
    7440:	7103f51f 	cmp	w8, #0xfd
    7444:	54000089 	b.ls	7454 <zbtreeUpdateScore+0x274>  // b.plast
    } else if (record[0] == ZBT_PACKED_SHORT) {
    7448:	7103f91f 	cmp	w8, #0xfe
    744c:	540002e1 	b.ne	74a8 <zbtreeUpdateScore+0x2c8>  // b.any
        memcpy(&shortlen, record + 1, sizeof(shortlen));
    7450:	78401328 	ldurh	w8, [x25, #1]
    7454:	f9000be8 	str	x8, [sp, #16]
    7458:	385ff2eb 	ldurb	w11, [x23, #-1]
    745c:	910023e8 	add	x8, sp, #0x8
    7460:	aa1f03e9 	mov	x9, xzr
    7464:	91006108 	add	x8, x8, #0x18
    return flags & SDS_TYPE_MASK;
    7468:	1200096a 	and	w10, w11, #0x7
    switch (sdsType(s)) {
    746c:	7100055f 	cmp	w10, #0x1
    7470:	5400012d 	b.le	7494 <zbtreeUpdateScore+0x2b4>
    7474:	7100095f 	cmp	w10, #0x2
    7478:	54000620 	b.eq	753c <zbtreeUpdateScore+0x35c>  // b.none
    747c:	71000d5f 	cmp	w10, #0x3
    7480:	54000620 	b.eq	7544 <zbtreeUpdateScore+0x364>  // b.none
    7484:	7100115f 	cmp	w10, #0x4
    7488:	54000641 	b.ne	7550 <zbtreeUpdateScore+0x370>  // b.any
            return SDS_HDR(64,s)->len;
    748c:	f85ef2e9 	ldur	x9, [x23, #-17]
    7490:	14000030 	b	7550 <zbtreeUpdateScore+0x370>
    switch (sdsType(s)) {
    7494:	340005ca 	cbz	w10, 754c <zbtreeUpdateScore+0x36c>
    7498:	7100055f 	cmp	w10, #0x1
    749c:	540005a1 	b.ne	7550 <zbtreeUpdateScore+0x370>  // b.any
            return SDS_HDR(8,s)->len;
    74a0:	385fd2e9 	ldurb	w9, [x23, #-3]
    74a4:	1400002b 	b	7550 <zbtreeUpdateScore+0x370>
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
    74a8:	f840d33a 	ldur	x26, [x25, #13]
        serverAssert(ptr != NULL);
    74ac:	b400123a 	cbz	x26, 76f0 <zbtreeUpdateScore+0x510>
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
    74b0:	f8405329 	ldur	x9, [x25, #5]
    memcpy(&hash, record + ZBT_EXTERNAL_HASH_OFFSET, sizeof(hash));
    74b4:	b8401328 	ldur	w8, [x25, #1]
    74b8:	f90013fa 	str	x26, [sp, #32]
        *len = zbtExternalLength(record);
    74bc:	a900a7fa 	stp	x26, x9, [sp, #8]
    74c0:	b9001be8 	str	w8, [sp, #24]
     * no score leaf.
     */
    zbtIndexReserveLeafId(zs, 0);
    zbtBuildElement moved;
    zbtBuildElementFromLeaf(&moved, oldleaf, oldpos);
    if (moved.external) {
    74c4:	b4fffcba 	cbz	x26, 7458 <zbtreeUpdateScore+0x278>
        serverAssert(moved.hash == hash);
    74c8:	6b14011f 	cmp	w8, w20
    74cc:	54000200 	b.eq	750c <zbtreeUpdateScore+0x32c>  // b.none
    74d0:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    74d4:	913e7c00 	add	x0, x0, #0xf9f
    74d8:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    74dc:	9100c842 	add	x2, x2, #0x32
    74e0:	5281caa1 	mov	w1, #0xe55                 	// #3669
    74e4:	94002366 	bl	1027c <standalone_panic>
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
    74e8:	39400328 	ldrb	w8, [x25]
    74ec:	7103fd1f 	cmp	w8, #0xff
    74f0:	540000e0 	b.eq	750c <zbtreeUpdateScore+0x32c>  // b.none
    74f4:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    74f8:	913e7c00 	add	x0, x0, #0xf9f
    74fc:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    7500:	91035c42 	add	x2, x2, #0xd7
    7504:	528048a1 	mov	w1, #0x245                 	// #581
    7508:	9400235d 	bl	1027c <standalone_panic>
    memcpy(record + ZBT_EXTERNAL_POINTER_OFFSET, &ptr, sizeof(ptr));
    750c:	f800d33f 	stur	xzr, [x25, #13]
    ele->owner_record = NULL;
    7510:	f90017ff 	str	xzr, [sp, #40]
         * command argument until the member has its new record. */
        zbtBuildElementFromBytes(&moved, (unsigned char *)ele,
                                 sdslen(ele), hash);
    }
    uint32_t oldid = oldleaf->id;
    if (oldleaf->n.count > 1) zbtScoreLeafNoteMove(oldleaf, oldpos);
    7514:	394046a8 	ldrb	w8, [x21, #17]
    uint32_t oldid = oldleaf->id;
    7518:	b94032b7 	ldr	w23, [x21, #48]
    if (oldleaf->n.count > 1) zbtScoreLeafNoteMove(oldleaf, oldpos);
    751c:	7100091f 	cmp	w8, #0x2
    7520:	54000262 	b.cs	756c <zbtreeUpdateScore+0x38c>  // b.hs, b.nlast
    if (leaf->n.count == 1) {
    7524:	7100051f 	cmp	w8, #0x1
    7528:	54000741 	b.ne	7610 <zbtreeUpdateScore+0x430>  // b.any
        zbtScoreRemoveLeaf(zs, leaf);
    752c:	aa1303e0 	mov	x0, x19
    7530:	aa1503e1 	mov	x1, x21
    7534:	94001c54 	bl	e684 <zbtScoreRemoveLeaf>
    7538:	1400003b 	b	7624 <zbtreeUpdateScore+0x444>
            return SDS_HDR(16,s)->len;
    753c:	785fb2e9 	ldurh	w9, [x23, #-5]
    7540:	14000004 	b	7550 <zbtreeUpdateScore+0x370>
            return SDS_HDR(32,s)->len;
    7544:	b85f72e9 	ldur	w9, [x23, #-9]
    7548:	14000002 	b	7550 <zbtreeUpdateScore+0x370>
    754c:	d343fd69 	lsr	x9, x11, #3
    ele->ptr = ptr;
    7550:	a900a7f7 	stp	x23, x9, [sp, #8]
    ele->hash = hash;
    7554:	b9001bf4 	str	w20, [sp, #24]
    ele->owner_record = NULL;
    7558:	a9007d1f 	stp	xzr, xzr, [x8]
    if (oldleaf->n.count > 1) zbtScoreLeafNoteMove(oldleaf, oldpos);
    755c:	394046a8 	ldrb	w8, [x21, #17]
    uint32_t oldid = oldleaf->id;
    7560:	b94032b7 	ldr	w23, [x21, #48]
    if (oldleaf->n.count > 1) zbtScoreLeafNoteMove(oldleaf, oldpos);
    7564:	7100091f 	cmp	w8, #0x2
    7568:	54fffde3 	b.cc	7524 <zbtreeUpdateScore+0x344>  // b.lo, b.ul, b.last
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    756c:	3940d2a9 	ldrb	w9, [x21, #52]
    if (score_bits == 0) return 0;
    7570:	b40000c9 	cbz	x9, 7588 <zbtreeUpdateScore+0x3a8>
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
    7574:	528000ea 	mov	w10, #0x7                   	// #7
    7578:	1b082929 	madd	w9, w9, w8, w10
    return (bytes + 8 + 1) & ~(size_t)1;
    757c:	53037d29 	lsr	w9, w9, #3
    7580:	11002529 	add	w9, w9, #0x9
    7584:	927f3529 	and	x9, x9, #0x7ffe
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    7588:	3940d6aa 	ldrb	w10, [x21, #53]
    758c:	2a3603eb 	mvn	w11, w22
    return (uint16_t *)(leaf->data +
    7590:	8b090309 	add	x9, x24, x9
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    7594:	0b0b0108 	add	w8, w8, w11
    7598:	7100015f 	cmp	w10, #0x0
    759c:	1a8802c8 	csel	w8, w22, w8, eq	// eq = none
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
    75a0:	78685928 	ldrh	w8, [x9, w8, uxtw #1]
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
    75a4:	8b0802a9 	add	x9, x21, x8
    if (record[0] == ZBT_PACKED_EXTERNAL)
    75a8:	39400128 	ldrb	w8, [x9]
    75ac:	7103f91f 	cmp	w8, #0xfe
    75b0:	540000a0 	b.eq	75c4 <zbtreeUpdateScore+0x3e4>  // b.none
    75b4:	7103fd1f 	cmp	w8, #0xff
    75b8:	54000081 	b.ne	75c8 <zbtreeUpdateScore+0x3e8>  // b.any
    75bc:	2a1f03e8 	mov	w8, wzr
    75c0:	1400000c 	b	75f0 <zbtreeUpdateScore+0x410>
        memcpy(&shortlen, record + 1, sizeof(shortlen));
    75c4:	78401128 	ldurh	w8, [x9, #1]
    return zbtPackedLengthBytes(len) + len;
    75c8:	11000d09 	add	w9, w8, #0x3
    75cc:	f103f91f 	cmp	x8, #0xfe
    unsigned int share = bytes * ZBT_SCORE_LEAF_MAX / ZBT_SCORE_LEAF_BYTES;
    75d0:	5280240a 	mov	w10, #0x120                 	// #288
    return zbtPackedLengthBytes(len) + len;
    75d4:	1a882528 	csinc	w8, w9, w8, cs	// cs = hs, nlast
    75d8:	52800c09 	mov	w9, #0x60                  	// #96
    unsigned int share = bytes * ZBT_SCORE_LEAF_MAX / ZBT_SCORE_LEAF_BYTES;
    75dc:	1b092908 	madd	w8, w8, w9, w10
    75e0:	52840069 	mov	w9, #0x2003                	// #8195
    75e4:	72a04009 	movk	w9, #0x200, lsl #16
    75e8:	9ba97d08 	umull	x8, w8, w9
    75ec:	d365fd08 	lsr	x8, x8, #37
    if (share == 0) share = 1;
    75f0:	7100051f 	cmp	w8, #0x1
    share += leaf->n.moved_out;
    75f4:	394056a9 	ldrb	w9, [x21, #21]
    if (share == 0) share = 1;
    75f8:	1a9f8508 	csinc	w8, w8, wzr, hi	// hi = pmore
    share += leaf->n.moved_out;
    75fc:	0b090108 	add	w8, w8, w9
    7600:	52801fe9 	mov	w9, #0xff                  	// #255
    leaf->n.moved_out = share > UINT8_MAX ? UINT8_MAX : share;
    7604:	7103fd1f 	cmp	w8, #0xff
    7608:	1a893108 	csel	w8, w8, w9, cc	// cc = lo, ul, last
    760c:	390056a8 	strb	w8, [x21, #21]
    zbtScoreDeleteInPlace(zs, leaf, pos, allow_merge);
    7610:	aa1303e0 	mov	x0, x19
    7614:	aa1503e1 	mov	x1, x21
    7618:	2a1603e2 	mov	w2, w22
    761c:	2a1f03e3 	mov	w3, wzr
    7620:	94001c81 	bl	e824 <zbtScoreDeleteInPlace>
    zbtScoreDeleteAt(zs, oldleaf, oldpos, 0);
    zbtScoreLeaf *newleaf = zbtScoreInsert(zs, score, &moved);
    7624:	1e604100 	fmov	d0, d8
    7628:	910023e1 	add	x1, sp, #0x8
    762c:	aa1303e0 	mov	x0, x19
    7630:	97fff5b4 	bl	4d00 <zbtScoreInsert>
    if (oldid != newleaf->id) {
    7634:	b9403003 	ldr	w3, [x0, #48]
    7638:	6b0302ff 	cmp	w23, w3
    763c:	540001e0 	b.eq	7678 <zbtreeUpdateScore+0x498>  // b.none
        int target_was_copied = 0;
        serverAssert(zbtIndexMove(zs, hash, oldid, newleaf->id, 0,
    7640:	d10013a5 	sub	x5, x29, #0x4
    7644:	aa1303e0 	mov	x0, x19
    7648:	2a1403e1 	mov	w1, w20
    764c:	2a1703e2 	mov	w2, w23
    7650:	2a1f03e4 	mov	w4, wzr
        int target_was_copied = 0;
    7654:	b81fc3bf 	stur	wzr, [x29, #-4]
        serverAssert(zbtIndexMove(zs, hash, oldid, newleaf->id, 0,
    7658:	94000200 	bl	7e58 <zbtIndexMove>
    765c:	350000e0 	cbnz	w0, 7678 <zbtreeUpdateScore+0x498>
    7660:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    7664:	913e7c00 	add	x0, x0, #0xf9f
    7668:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    766c:	91011442 	add	x2, x2, #0x45
    7670:	5281cc81 	mov	w1, #0xe64                 	// #3684
    7674:	94002302 	bl	1027c <standalone_panic>
    if (id >= zs->next_score_leaf_id) return NULL;
    7678:	b9405668 	ldr	w8, [x19, #84]
    767c:	6b17011f 	cmp	w8, w23
    7680:	54001229 	b.ls	78c4 <zbtreeUpdateScore+0x6e4>  // b.plast
    zbtScoreLeaf *leaf = zs->score_leaf_by_id[id];
    7684:	f9402668 	ldr	x8, [x19, #72]
    7688:	f8777914 	ldr	x20, [x8, x23, lsl #3]
    if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) return NULL;
    768c:	b40011d4 	cbz	x20, 78c4 <zbtreeUpdateScore+0x6e4>
    7690:	370011b4 	tbnz	w20, #0, 78c4 <zbtreeUpdateScore+0x6e4>
    serverAssert(leaf->id == id);
    7694:	b9403288 	ldr	w8, [x20, #48]
    7698:	6b17011f 	cmp	w8, w23
    769c:	540000e0 	b.eq	76b8 <zbtreeUpdateScore+0x4d8>  // b.none
    76a0:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    76a4:	913e7c00 	add	x0, x0, #0xf9f
    76a8:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    76ac:	9103e042 	add	x2, x2, #0xf8
    76b0:	528185e1 	mov	w1, #0xc2f                 	// #3119
    76b4:	940022f2 	bl	1027c <standalone_panic>
    if (leaf == NULL || leaf->n.moved_out < ZBT_SCORE_MOVED_CHECK) return;
    76b8:	39405688 	ldrb	w8, [x20, #21]
    76bc:	7100611f 	cmp	w8, #0x18
    76c0:	54001023 	b.cc	78c4 <zbtreeUpdateScore+0x6e4>  // b.lo, b.ul, b.last
           zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits) +
    76c4:	3940d289 	ldrb	w9, [x20, #52]
    76c8:	39404688 	ldrb	w8, [x20, #17]
    leaf->n.moved_out = 0;
    76cc:	3900569f 	strb	wzr, [x20, #21]
    if (score_bits == 0) return 0;
    76d0:	b4000349 	cbz	x9, 7738 <zbtreeUpdateScore+0x558>
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
    76d4:	528000ea 	mov	w10, #0x7                   	// #7
    76d8:	1b082929 	madd	w9, w9, w8, w10
    return (bytes + 8 + 1) & ~(size_t)1;
    76dc:	53037d29 	lsr	w9, w9, #3
    76e0:	11002529 	add	w9, w9, #0x9
    76e4:	927f352b 	and	x11, x9, #0x7ffe
    return offsetof(zbtScoreLeaf, data) +
    76e8:	9100e169 	add	x9, x11, #0x38
    76ec:	14000015 	b	7740 <zbtreeUpdateScore+0x560>
        serverAssert(ptr != NULL);
    76f0:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    76f4:	913e7c00 	add	x0, x0, #0xf9f
    76f8:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    76fc:	91032c42 	add	x2, x2, #0xcb
    7700:	52804ae1 	mov	w1, #0x257                 	// #599
    7704:	940022de 	bl	1027c <standalone_panic>
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
    7708:	39400328 	ldrb	w8, [x25]
    770c:	7103fd1f 	cmp	w8, #0xff
    7710:	54ffed00 	b.eq	74b0 <zbtreeUpdateScore+0x2d0>  // b.none
    7714:	b0000040 	adrp	x0, 10000 <zbtIndexScanSlot+0x614>
    7718:	913e7c00 	add	x0, x0, #0xf9f
    771c:	d0000042 	adrp	x2, 11000 <_IO_stdin_used+0x3e0>
    7720:	91035c42 	add	x2, x2, #0xd7
    7724:	528046e1 	mov	w1, #0x237                 	// #567
    7728:	940022d5 	bl	1027c <standalone_panic>
    if (record[0] == ZBT_PACKED_EXTERNAL) {
    772c:	39400328 	ldrb	w8, [x25]
    7730:	7103fd1f 	cmp	w8, #0xff
    7734:	17ffff49 	b	7458 <zbtreeUpdateScore+0x278>
    7738:	aa1f03eb 	mov	x11, xzr
    773c:	52800709 	mov	w9, #0x38                  	// #56
    7740:	aa1f03ea 	mov	x10, xzr
    for (unsigned int i = 0; i < leaf->n.count; i++)
    7744:	340003c8 	cbz	w8, 77bc <zbtreeUpdateScore+0x5dc>
    7748:	8b0b028b 	add	x11, x20, x11
    774c:	aa0803ec 	mov	x12, x8
    7750:	9100e16b 	add	x11, x11, #0x38
    7754:	14000005 	b	7768 <zbtreeUpdateScore+0x588>
    7758:	528002ad 	mov	w13, #0x15                  	// #21
    775c:	f100058c 	subs	x12, x12, #0x1
        bytes += zbtRecordStorageBytes((unsigned char *)leaf + offsets[i]);
    7760:	8b0a01aa 	add	x10, x13, x10
    for (unsigned int i = 0; i < leaf->n.count; i++)
    7764:	540002c0 	b.eq	77bc <zbtreeUpdateScore+0x5dc>  // b.none
        bytes += zbtRecordStorageBytes((unsigned char *)leaf + offsets[i]);
    7768:	7840256d 	ldrh	w13, [x11], #2
    776c:	8b0d028e 	add	x14, x20, x13
    if (record[0] == ZBT_PACKED_EXTERNAL)
    7770:	394001cd 	ldrb	w13, [x14]
    7774:	7103f9bf 	cmp	w13, #0xfe
    7778:	54000140 	b.eq	77a0 <zbtreeUpdateScore+0x5c0>  // b.none
    777c:	7103fdbf 	cmp	w13, #0xff
    7780:	54fffec0 	b.eq	7758 <zbtreeUpdateScore+0x578>  // b.none
    return len < ZBT_PACKED_SHORT ? 1 : 3;
    7784:	f103f9bf 	cmp	x13, #0xfe
    return zbtPackedLengthBytes(len) + len;
    7788:	91000dae 	add	x14, x13, #0x3
    778c:	9a8d25cd 	csinc	x13, x14, x13, cs	// cs = hs, nlast
    for (unsigned int i = 0; i < leaf->n.count; i++)
    7790:	f100058c 	subs	x12, x12, #0x1
        bytes += zbtRecordStorageBytes((unsigned char *)leaf + offsets[i]);
    7794:	8b0a01aa 	add	x10, x13, x10
    7798:	54fffe81 	b.ne	7768 <zbtreeUpdateScore+0x588>  // b.any
    779c:	14000008 	b	77bc <zbtreeUpdateScore+0x5dc>
        memcpy(&shortlen, record + 1, sizeof(shortlen));
    77a0:	784011cd 	ldurh	w13, [x14, #1]
    return len < ZBT_PACKED_SHORT ? 1 : 3;
    77a4:	f103f9bf 	cmp	x13, #0xfe
    return zbtPackedLengthBytes(len) + len;
    77a8:	91000dae 	add	x14, x13, #0x3
    77ac:	9a8d25cd 	csinc	x13, x14, x13, cs	// cs = hs, nlast
    for (unsigned int i = 0; i < leaf->n.count; i++)
    77b0:	f100058c 	subs	x12, x12, #0x1
        bytes += zbtRecordStorageBytes((unsigned char *)leaf + offsets[i]);
    77b4:	8b0a01aa 	add	x10, x13, x10
    for (unsigned int i = 0; i < leaf->n.count; i++)
    77b8:	54fffd81 	b.ne	7768 <zbtreeUpdateScore+0x588>  // b.any
           leaf->n.count * (sizeof(uint16_t) + sizeof(uint8_t)) +
    77bc:	8b08050b 	add	x11, x8, x8, lsl #1
           zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits) +
    77c0:	8b0a0129 	add	x9, x9, x10
        zbtScoreLeaf *other = side == 0 ? leaf->prev : leaf->next;
    77c4:	f9400e81 	ldr	x1, [x20, #24]
           leaf->n.count * (sizeof(uint16_t) + sizeof(uint8_t)) +
    77c8:	8b0b0135 	add	x21, x9, x11
            (estimate && live + other->n.count * member_bytes > max_bytes))
    77cc:	f117febf 	cmp	x21, #0x5ff
    77d0:	54000389 	b.ls	7840 <zbtreeUpdateScore+0x660>  // b.plast
    77d4:	d100e2a9 	sub	x9, x21, #0x38
    77d8:	9ac80936 	udiv	x22, x9, x8
        if (other == NULL || leaf->n.count + other->n.count > max_count ||
    77dc:	b40001c1 	cbz	x1, 7814 <zbtreeUpdateScore+0x634>
    77e0:	39404429 	ldrb	w9, [x1, #17]
    77e4:	0b080128 	add	w8, w9, w8
    77e8:	7101211f 	cmp	w8, #0x48
    77ec:	54000148 	b.hi	7814 <zbtreeUpdateScore+0x634>  // b.pmore
            (estimate && live + other->n.count * member_bytes > max_bytes))
    77f0:	9b0956c8 	madd	x8, x22, x9, x21
        if (other == NULL || leaf->n.count + other->n.count > max_count ||
    77f4:	f12ffd1f 	cmp	x8, #0xbff
    77f8:	540000e8 	b.hi	7814 <zbtreeUpdateScore+0x634>  // b.pmore
        if (zbtScoreMergePair(zs, side == 0 ? other : leaf,
    77fc:	aa1303e0 	mov	x0, x19
    7800:	aa1403e2 	mov	x2, x20
    7804:	52800903 	mov	w3, #0x48                  	// #72
    7808:	52817fe4 	mov	w4, #0xbff                 	// #3071
    780c:	94001da2 	bl	ee94 <zbtScoreMergePair>
    7810:	b50005a0 	cbnz	x0, 78c4 <zbtreeUpdateScore+0x6e4>
        zbtScoreLeaf *other = side == 0 ? leaf->prev : leaf->next;
    7814:	f9401282 	ldr	x2, [x20, #32]
        if (other == NULL || leaf->n.count + other->n.count > max_count ||
    7818:	b4000442 	cbz	x2, 78a0 <zbtreeUpdateScore+0x6c0>
    781c:	39404689 	ldrb	w9, [x20, #17]
    7820:	39404448 	ldrb	w8, [x2, #17]
    7824:	0b090109 	add	w9, w8, w9
    7828:	7101213f 	cmp	w9, #0x48
    782c:	540003a8 	b.hi	78a0 <zbtreeUpdateScore+0x6c0>  // b.pmore
            (estimate && live + other->n.count * member_bytes > max_bytes))
    7830:	9b0856c8 	madd	x8, x22, x8, x21
        if (other == NULL || leaf->n.count + other->n.count > max_count ||
    7834:	f12ffd1f 	cmp	x8, #0xbff
    7838:	54000289 	b.ls	7888 <zbtreeUpdateScore+0x6a8>  // b.plast
    783c:	14000019 	b	78a0 <zbtreeUpdateScore+0x6c0>
    7840:	b4000161 	cbz	x1, 786c <zbtreeUpdateScore+0x68c>
    7844:	39404429 	ldrb	w9, [x1, #17]
    7848:	0b080128 	add	w8, w9, w8
    784c:	7101211f 	cmp	w8, #0x48
    7850:	540000e8 	b.hi	786c <zbtreeUpdateScore+0x68c>  // b.pmore
        if (zbtScoreMergePair(zs, side == 0 ? other : leaf,
    7854:	aa1303e0 	mov	x0, x19
    7858:	aa1403e2 	mov	x2, x20
    785c:	52800903 	mov	w3, #0x48                  	// #72
    7860:	52817fe4 	mov	w4, #0xbff                 	// #3071
    7864:	94001d8c 	bl	ee94 <zbtScoreMergePair>
    7868:	b50002e0 	cbnz	x0, 78c4 <zbtreeUpdateScore+0x6e4>
        zbtScoreLeaf *other = side == 0 ? leaf->prev : leaf->next;
    786c:	f9401282 	ldr	x2, [x20, #32]
        if (other == NULL || leaf->n.count + other->n.count > max_count ||
    7870:	b4000182 	cbz	x2, 78a0 <zbtreeUpdateScore+0x6c0>
    7874:	39404688 	ldrb	w8, [x20, #17]
    7878:	39404449 	ldrb	w9, [x2, #17]
    787c:	0b080128 	add	w8, w9, w8
    7880:	7101211f 	cmp	w8, #0x48
    7884:	540000e8 	b.hi	78a0 <zbtreeUpdateScore+0x6c0>  // b.pmore
        if (zbtScoreMergePair(zs, side == 0 ? other : leaf,
    7888:	aa1303e0 	mov	x0, x19
    788c:	aa1403e1 	mov	x1, x20
    7890:	52800903 	mov	w3, #0x48                  	// #72
    7894:	52817fe4 	mov	w4, #0xbff                 	// #3071
    7898:	94001d7f 	bl	ee94 <zbtScoreMergePair>
    789c:	b5000140 	cbnz	x0, 78c4 <zbtreeUpdateScore+0x6e4>
    if (zmalloc_usable_size(leaf) >= 2 * live + ZBT_SCORE_LEAF_RESERVE)
    78a0:	aa1403e0 	mov	x0, x20
    78a4:	94002283 	bl	102b0 <zmalloc_usable_size>
    78a8:	d37ffaa8 	lsl	x8, x21, #1
    78ac:	91020108 	add	x8, x8, #0x80
    78b0:	eb08001f 	cmp	x0, x8
    78b4:	54000083 	b.cc	78c4 <zbtreeUpdateScore+0x6e4>  // b.lo, b.ul, b.last
        zbtScoreCompactLeaf(zs, leaf);
    78b8:	aa1303e0 	mov	x0, x19
    78bc:	aa1403e1 	mov	x1, x20
    78c0:	94001788 	bl	d6e0 <zbtScoreCompactLeaf>
                                  &target_was_copied));
    }
    zbtScoreMovedOut(zs, oldid);
}
    78c4:	a9484ff4 	ldp	x20, x19, [sp, #128]
    78c8:	fd401be8 	ldr	d8, [sp, #48]
    78cc:	a94757f6 	ldp	x22, x21, [sp, #112]
    78d0:	a9465ff8 	ldp	x24, x23, [sp, #96]
    78d4:	a94567fa 	ldp	x26, x25, [sp, #80]
    78d8:	a9447bfd 	ldp	x29, x30, [sp, #64]
    78dc:	910243ff 	add	sp, sp, #0x90
    78e0:	d65f03c0 	ret

Disassembly of section .fini:
