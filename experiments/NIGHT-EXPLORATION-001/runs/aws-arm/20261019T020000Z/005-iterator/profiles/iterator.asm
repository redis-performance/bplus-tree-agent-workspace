
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator/build/base:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b7a0 <zbtreeIteratorNext>:

/* Return the current member and score, then advance to the next logical
 * position. The output pointers are optional. Return zero at the end. */
int zbtreeIteratorNext(zbtreeIterator *iter, int reverse,
                       const unsigned char **ele, size_t *len, double *score)
{
    b7a0:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
    b7a4:	f9000bfb 	str	x27, [sp, #16]
    b7a8:	a90267fa 	stp	x26, x25, [sp, #32]
    b7ac:	a9035ff8 	stp	x24, x23, [sp, #48]
    b7b0:	a90457f6 	stp	x22, x21, [sp, #64]
    b7b4:	a9054ff4 	stp	x20, x19, [sp, #80]
    b7b8:	910003fd 	mov	x29, sp
    zbtScoreLeaf *leaf = iter->leaf;
    b7bc:	f9400013 	ldr	x19, [x0]
    if (leaf == NULL) return 0;
    b7c0:	b4000393 	cbz	x19, b830 <zbtreeIteratorNext+0x90>

    unsigned int pos = iter->pos;
    b7c4:	b9400814 	ldr	w20, [x0, #8]
    if (ele || len) {
    b7c8:	aa030048 	orr	x8, x2, x3
    b7cc:	b4000908 	cbz	x8, b8ec <zbtreeIteratorNext+0x14c>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    b7d0:	3940d268 	ldrb	w8, [x19, #52]
    if (score_bits == 0) return 0;
    b7d4:	b40000e8 	cbz	x8, b7f0 <zbtreeIteratorNext+0x50>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    b7d8:	39404669 	ldrb	w9, [x19, #17]
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
    b7dc:	528000ea 	mov	w10, #0x7                   	// #7
    b7e0:	1b082928 	madd	w8, w9, w8, w10
    return (bytes + 8 + 1) & ~(size_t)1;
    b7e4:	53037d08 	lsr	w8, w8, #3
    b7e8:	11002508 	add	w8, w8, #0x9
    b7ec:	927f3508 	and	x8, x8, #0x7ffe
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    b7f0:	3940d66a 	ldrb	w10, [x19, #53]
    b7f4:	2a1403e9 	mov	w9, w20
    b7f8:	3400008a 	cbz	w10, b808 <zbtreeIteratorNext+0x68>
    b7fc:	39404669 	ldrb	w9, [x19, #17]
    b800:	2a3403ea 	mvn	w10, w20
    b804:	0b0a0129 	add	w9, w9, w10
    return (uint16_t *)(leaf->data +
    b808:	8b080268 	add	x8, x19, x8
    b80c:	8b294508 	add	x8, x8, w9, uxtw #1
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
    b810:	79407108 	ldrh	w8, [x8, #56]
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
    b814:	8b080276 	add	x22, x19, x8
    if (record[0] < ZBT_PACKED_SHORT) {
    b818:	394002c8 	ldrb	w8, [x22]
    b81c:	7103f51f 	cmp	w8, #0xfd
    b820:	540000c8 	b.hi	b838 <zbtreeIteratorNext+0x98>  // b.pmore
        return record + 1;
    b824:	910006d5 	add	x21, x22, #0x1
        size_t elelen;
        const unsigned char *element =
            zbtScoreLeafElement(leaf, pos, &elelen);
        if (ele) *ele = element;
    b828:	b50005c2 	cbnz	x2, b8e0 <zbtreeIteratorNext+0x140>
    b82c:	1400002e 	b	b8e4 <zbtreeIteratorNext+0x144>
    b830:	2a1f03e0 	mov	w0, wzr
    b834:	1400006f 	b	b9f0 <zbtreeIteratorNext+0x250>
    } else if (record[0] == ZBT_PACKED_SHORT) {
    b838:	7103f91f 	cmp	w8, #0xfe
    b83c:	540000a1 	b.ne	b850 <zbtreeIteratorNext+0xb0>  // b.any
        memcpy(&shortlen, record + 1, sizeof(shortlen));
    b840:	784012c8 	ldurh	w8, [x22, #1]
        return record + 3;
    b844:	91000ed5 	add	x21, x22, #0x3
        if (ele) *ele = element;
    b848:	b50004c2 	cbnz	x2, b8e0 <zbtreeIteratorNext+0x140>
    b84c:	14000026 	b	b8e4 <zbtreeIteratorNext+0x144>
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
    b850:	f840d2d5 	ldur	x21, [x22, #13]
        serverAssert(ptr != NULL);
    b854:	b5000435 	cbnz	x21, b8d8 <zbtreeIteratorNext+0x138>
    b858:	90000048 	adrp	x8, 13000 <_IO_stdin_used+0x300>
    b85c:	911f1d08 	add	x8, x8, #0x7c7
    b860:	90000049 	adrp	x9, 13000 <_IO_stdin_used+0x300>
    b864:	9123cd29 	add	x9, x9, #0x8f3
    b868:	aa0003f7 	mov	x23, x0
    b86c:	aa0803e0 	mov	x0, x8
    b870:	2a0103f8 	mov	w24, w1
    b874:	52804ae1 	mov	w1, #0x257                 	// #599
    b878:	aa0203f9 	mov	x25, x2
    b87c:	aa0903e2 	mov	x2, x9
    b880:	aa0403fa 	mov	x26, x4
    b884:	aa0303fb 	mov	x27, x3
    b888:	94001ab4 	bl	12358 <standalone_panic>
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
    b88c:	394002c8 	ldrb	w8, [x22]
    b890:	aa1903e2 	mov	x2, x25
    b894:	aa1b03e3 	mov	x3, x27
    b898:	2a1803e1 	mov	w1, w24
    b89c:	aa1a03e4 	mov	x4, x26
    b8a0:	aa1703e0 	mov	x0, x23
    b8a4:	7103fd1f 	cmp	w8, #0xff
    b8a8:	54000180 	b.eq	b8d8 <zbtreeIteratorNext+0x138>  // b.none
    b8ac:	90000040 	adrp	x0, 13000 <_IO_stdin_used+0x300>
    b8b0:	911f1c00 	add	x0, x0, #0x7c7
    b8b4:	90000042 	adrp	x2, 13000 <_IO_stdin_used+0x300>
    b8b8:	9123fc42 	add	x2, x2, #0x8ff
    b8bc:	528046e1 	mov	w1, #0x237                 	// #567
    b8c0:	94001aa6 	bl	12358 <standalone_panic>
    b8c4:	aa1903e2 	mov	x2, x25
    b8c8:	aa1b03e3 	mov	x3, x27
    b8cc:	2a1803e1 	mov	w1, w24
    b8d0:	aa1a03e4 	mov	x4, x26
    b8d4:	aa1703e0 	mov	x0, x23
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
    b8d8:	f84052c8 	ldur	x8, [x22, #5]
        if (ele) *ele = element;
    b8dc:	b4000042 	cbz	x2, b8e4 <zbtreeIteratorNext+0x144>
    b8e0:	f9000055 	str	x21, [x2]
        if (len) *len = elelen;
    b8e4:	b4000043 	cbz	x3, b8ec <zbtreeIteratorNext+0x14c>
    b8e8:	f9000068 	str	x8, [x3]
    }
    if (score) *score = zbtScoreLeafScore(leaf, pos);
    b8ec:	b4000544 	cbz	x4, b994 <zbtreeIteratorNext+0x1f4>
    unsigned int bits = leaf->score_bits;
    b8f0:	3940d269 	ldrb	w9, [x19, #52]
    b8f4:	3940d668 	ldrb	w8, [x19, #53]
    if (bits != 0) {
    b8f8:	340003c9 	cbz	w9, b970 <zbtreeIteratorNext+0x1d0>
    b8fc:	2a1403ea 	mov	w10, w20
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    b900:	34000088 	cbz	w8, b910 <zbtreeIteratorNext+0x170>
    b904:	3940466a 	ldrb	w10, [x19, #17]
    b908:	2a3403eb 	mvn	w11, w20
    b90c:	0b0b014a 	add	w10, w10, w11
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
    b910:	9baa7d2a 	umull	x10, w9, w10
        size_t byte = bitpos / 8;
    b914:	d343fd4b 	lsr	x11, x10, #3
        delta = intrev64ifbe(delta) >> shift;
    b918:	9240094e 	and	x14, x10, #0x7
        memcpy(&delta, leaf->data + byte, sizeof(delta));
    b91c:	8b0b026c 	add	x12, x19, x11
    b920:	f9401d8d 	ldr	x13, [x12, #56]
        unsigned int shift = bitpos & 7;
    b924:	7200094c 	ands	w12, w10, #0x7
        delta = intrev64ifbe(delta) >> shift;
    b928:	9ace25aa 	lsr	x10, x13, x14
        if (shift && bits > 64 - shift)
    b92c:	54000120 	b.eq	b950 <zbtreeIteratorNext+0x1b0>  // b.none
    b930:	5280080d 	mov	w13, #0x40                  	// #64
    b934:	4b0c01ac 	sub	w12, w13, w12
    b938:	6b09019f 	cmp	w12, w9
    b93c:	540000a2 	b.cs	b950 <zbtreeIteratorNext+0x1b0>  // b.hs, b.nlast
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
    b940:	8b13016b 	add	x11, x11, x19
    b944:	3941016b 	ldrb	w11, [x11, #64]
    b948:	9acc216b 	lsl	x11, x11, x12
    b94c:	aa0a016a 	orr	x10, x11, x10
    b950:	9280000b 	mov	x11, #0xffffffffffffffff    	// #-1
        if (bits < 64)
    b954:	7101013f 	cmp	w9, #0x40
    b958:	9ac9216c 	lsl	x12, x11, x9
    b95c:	da8c2169 	csinv	x9, x11, x12, cs	// cs = hs, nlast
        delta <<= leaf->n.score_shift;
    b960:	39404e6b 	ldrb	w11, [x19, #19]
        if (bits < 64)
    b964:	8a090149 	and	x9, x10, x9
        delta <<= leaf->n.score_shift;
    b968:	9acb2129 	lsl	x9, x9, x11
    b96c:	14000002 	b	b974 <zbtreeIteratorNext+0x1d4>
    b970:	aa1f03e9 	mov	x9, xzr
    b974:	f940166a 	ldr	x10, [x19, #40]
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
    b978:	7100011f 	cmp	w8, #0x0
    b97c:	da890528 	cneg	x8, x9, ne	// ne = any
    b980:	8b080148 	add	x8, x10, x8
    if (ordered & (UINT64_C(1) << 63))
    b984:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    b988:	f100011f 	cmp	x8, #0x0
    b98c:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
    if (score) *score = zbtScoreLeafScore(leaf, pos);
    b990:	f9000088 	str	x8, [x4]

    if (reverse) {
    b994:	340000a1 	cbz	w1, b9a8 <zbtreeIteratorNext+0x208>
        if (pos != 0) {
    b998:	34000174 	cbz	w20, b9c4 <zbtreeIteratorNext+0x224>
            iter->pos--;
    b99c:	b9400808 	ldr	w8, [x0, #8]
    b9a0:	51000508 	sub	w8, w8, #0x1
    b9a4:	14000011 	b	b9e8 <zbtreeIteratorNext+0x248>
            leaf = leaf->prev;
            iter->leaf = leaf;
            if (leaf) iter->pos = leaf->n.count - 1;
        }
    } else {
        if (pos + 1 < leaf->n.count) {
    b9a8:	39404668 	ldrb	w8, [x19, #17]
    b9ac:	11000689 	add	w9, w20, #0x1
    b9b0:	6b08013f 	cmp	w9, w8
    b9b4:	54000142 	b.cs	b9dc <zbtreeIteratorNext+0x23c>  // b.hs, b.nlast
            iter->pos++;
    b9b8:	b9400808 	ldr	w8, [x0, #8]
    b9bc:	11000508 	add	w8, w8, #0x1
    b9c0:	1400000a 	b	b9e8 <zbtreeIteratorNext+0x248>
            leaf = leaf->prev;
    b9c4:	f9400e68 	ldr	x8, [x19, #24]
            iter->leaf = leaf;
    b9c8:	f9000008 	str	x8, [x0]
            if (leaf) iter->pos = leaf->n.count - 1;
    b9cc:	b4000108 	cbz	x8, b9ec <zbtreeIteratorNext+0x24c>
    b9d0:	39404508 	ldrb	w8, [x8, #17]
    b9d4:	51000508 	sub	w8, w8, #0x1
    b9d8:	14000004 	b	b9e8 <zbtreeIteratorNext+0x248>
        } else {
            leaf = leaf->next;
    b9dc:	f9401269 	ldr	x9, [x19, #32]
    b9e0:	2a1f03e8 	mov	w8, wzr
            iter->leaf = leaf;
    b9e4:	f9000009 	str	x9, [x0]
    b9e8:	b9000808 	str	w8, [x0, #8]
    b9ec:	52800020 	mov	w0, #0x1                   	// #1
            iter->pos = 0;
        }
    }
    return 1;
}
    b9f0:	a9454ff4 	ldp	x20, x19, [sp, #80]
    b9f4:	f9400bfb 	ldr	x27, [sp, #16]
    b9f8:	a94457f6 	ldp	x22, x21, [sp, #64]
    b9fc:	a9435ff8 	ldp	x24, x23, [sp, #48]
    ba00:	a94267fa 	ldp	x26, x25, [sp, #32]
    ba04:	a8c67bfd 	ldp	x29, x30, [sp], #96
    ba08:	d65f03c0 	ret

Disassembly of section .fini:
