
experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator/build/A:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

000000000000b7cc <zbtreeIteratorNext>:

/* Return the current member and score, then advance to the next logical
 * position. The output pointers are optional. Return zero at the end. */
int zbtreeIteratorNext(zbtreeIterator *iter, int reverse,
                       const unsigned char **ele, size_t *len, double *score)
{
    b7cc:	a9ba7bfd 	stp	x29, x30, [sp, #-96]!
    b7d0:	f9000bfb 	str	x27, [sp, #16]
    b7d4:	a90267fa 	stp	x26, x25, [sp, #32]
    b7d8:	a9035ff8 	stp	x24, x23, [sp, #48]
    b7dc:	a90457f6 	stp	x22, x21, [sp, #64]
    b7e0:	a9054ff4 	stp	x20, x19, [sp, #80]
    b7e4:	910003fd 	mov	x29, sp
    zbtScoreLeaf *leaf = iter->leaf;
    b7e8:	f9400013 	ldr	x19, [x0]
    if (leaf == NULL) return 0;
    b7ec:	b40003f3 	cbz	x19, b868 <zbtreeIteratorNext+0x9c>

    unsigned int pos = iter->pos;
    b7f0:	b9400814 	ldr	w20, [x0, #8]
    if (ele || len) {
    b7f4:	aa030048 	orr	x8, x2, x3
    b7f8:	b4000968 	cbz	x8, b924 <zbtreeIteratorNext+0x158>
        if (iter->member_offsets == NULL)
    b7fc:	f9400808 	ldr	x8, [x0, #16]
    b800:	b5000188 	cbnz	x8, b830 <zbtreeIteratorNext+0x64>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    b804:	3940d268 	ldrb	w8, [x19, #52]
    if (score_bits == 0) return 0;
    b808:	b40000e8 	cbz	x8, b824 <zbtreeIteratorNext+0x58>
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    b80c:	39404669 	ldrb	w9, [x19, #17]
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
    b810:	528000ea 	mov	w10, #0x7                   	// #7
    b814:	1b082928 	madd	w8, w9, w8, w10
    return (bytes + 8 + 1) & ~(size_t)1;
    b818:	53037d08 	lsr	w8, w8, #3
    b81c:	11002508 	add	w8, w8, #0x9
    b820:	927f3508 	and	x8, x8, #0x7ffe
    return (uint16_t *)(leaf->data +
    b824:	8b080268 	add	x8, x19, x8
    b828:	9100e108 	add	x8, x8, #0x38
            iter->member_offsets = zbtScoreLeafOffsets(leaf);
    b82c:	f9000808 	str	x8, [x0, #16]
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    b830:	3940d66a 	ldrb	w10, [x19, #53]
    b834:	2a1403e9 	mov	w9, w20
    b838:	3400008a 	cbz	w10, b848 <zbtreeIteratorNext+0x7c>
    b83c:	39404669 	ldrb	w9, [x19, #17]
    b840:	2a3403ea 	mvn	w10, w20
    b844:	0b0a0129 	add	w9, w9, w10
        const uint16_t *offsets = iter->member_offsets;
        size_t elelen;
        const unsigned char *element = zbtPackedData(
            (unsigned char *)leaf + offsets[zbtScoreLeafPhysicalPos(leaf, pos)],
    b848:	78695908 	ldrh	w8, [x8, w9, uxtw #1]
    b84c:	8b080276 	add	x22, x19, x8
    if (record[0] < ZBT_PACKED_SHORT) {
    b850:	394002c8 	ldrb	w8, [x22]
    b854:	7103f51f 	cmp	w8, #0xfd
    b858:	540000c8 	b.hi	b870 <zbtreeIteratorNext+0xa4>  // b.pmore
        return record + 1;
    b85c:	910006d5 	add	x21, x22, #0x1
            &elelen);
        if (ele) *ele = element;
    b860:	b50005c2 	cbnz	x2, b918 <zbtreeIteratorNext+0x14c>
    b864:	1400002e 	b	b91c <zbtreeIteratorNext+0x150>
    b868:	2a1f03e0 	mov	w0, wzr
    b86c:	14000071 	b	ba30 <zbtreeIteratorNext+0x264>
    } else if (record[0] == ZBT_PACKED_SHORT) {
    b870:	7103f91f 	cmp	w8, #0xfe
    b874:	540000a1 	b.ne	b888 <zbtreeIteratorNext+0xbc>  // b.any
        memcpy(&shortlen, record + 1, sizeof(shortlen));
    b878:	784012c8 	ldurh	w8, [x22, #1]
        return record + 3;
    b87c:	91000ed5 	add	x21, x22, #0x3
        if (ele) *ele = element;
    b880:	b50004c2 	cbnz	x2, b918 <zbtreeIteratorNext+0x14c>
    b884:	14000026 	b	b91c <zbtreeIteratorNext+0x150>
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
    b888:	f840d2d5 	ldur	x21, [x22, #13]
        serverAssert(ptr != NULL);
    b88c:	b5000435 	cbnz	x21, b910 <zbtreeIteratorNext+0x144>
    b890:	90000048 	adrp	x8, 13000 <_IO_stdin_used+0x2c0>
    b894:	91201d08 	add	x8, x8, #0x807
    b898:	90000049 	adrp	x9, 13000 <_IO_stdin_used+0x2c0>
    b89c:	91263d29 	add	x9, x9, #0x98f
    b8a0:	aa0003f7 	mov	x23, x0
    b8a4:	aa0803e0 	mov	x0, x8
    b8a8:	2a0103f8 	mov	w24, w1
    b8ac:	52804ae1 	mov	w1, #0x257                 	// #599
    b8b0:	aa0203f9 	mov	x25, x2
    b8b4:	aa0903e2 	mov	x2, x9
    b8b8:	aa0403fa 	mov	x26, x4
    b8bc:	aa0303fb 	mov	x27, x3
    b8c0:	94001ab6 	bl	12398 <standalone_panic>
    serverAssert(record[0] == ZBT_PACKED_EXTERNAL);
    b8c4:	394002c8 	ldrb	w8, [x22]
    b8c8:	aa1903e2 	mov	x2, x25
    b8cc:	aa1b03e3 	mov	x3, x27
    b8d0:	2a1803e1 	mov	w1, w24
    b8d4:	aa1a03e4 	mov	x4, x26
    b8d8:	aa1703e0 	mov	x0, x23
    b8dc:	7103fd1f 	cmp	w8, #0xff
    b8e0:	54000180 	b.eq	b910 <zbtreeIteratorNext+0x144>  // b.none
    b8e4:	90000040 	adrp	x0, 13000 <_IO_stdin_used+0x2c0>
    b8e8:	91201c00 	add	x0, x0, #0x807
    b8ec:	90000042 	adrp	x2, 13000 <_IO_stdin_used+0x2c0>
    b8f0:	91266c42 	add	x2, x2, #0x99b
    b8f4:	528046e1 	mov	w1, #0x237                 	// #567
    b8f8:	94001aa8 	bl	12398 <standalone_panic>
    b8fc:	aa1903e2 	mov	x2, x25
    b900:	aa1b03e3 	mov	x3, x27
    b904:	2a1803e1 	mov	w1, w24
    b908:	aa1a03e4 	mov	x4, x26
    b90c:	aa1703e0 	mov	x0, x23
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
    b910:	f84052c8 	ldur	x8, [x22, #5]
        if (ele) *ele = element;
    b914:	b4000042 	cbz	x2, b91c <zbtreeIteratorNext+0x150>
    b918:	f9000055 	str	x21, [x2]
        if (len) *len = elelen;
    b91c:	b4000043 	cbz	x3, b924 <zbtreeIteratorNext+0x158>
    b920:	f9000068 	str	x8, [x3]
    }
    if (score) *score = zbtScoreLeafScore(leaf, pos);
    b924:	b4000544 	cbz	x4, b9cc <zbtreeIteratorNext+0x200>
    unsigned int bits = leaf->score_bits;
    b928:	3940d269 	ldrb	w9, [x19, #52]
    b92c:	3940d668 	ldrb	w8, [x19, #53]
    if (bits != 0) {
    b930:	340003c9 	cbz	w9, b9a8 <zbtreeIteratorNext+0x1dc>
    b934:	2a1403ea 	mov	w10, w20
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
    b938:	34000088 	cbz	w8, b948 <zbtreeIteratorNext+0x17c>
    b93c:	3940466a 	ldrb	w10, [x19, #17]
    b940:	2a3403eb 	mvn	w11, w20
    b944:	0b0b014a 	add	w10, w10, w11
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
    b948:	9baa7d2a 	umull	x10, w9, w10
        size_t byte = bitpos / 8;
    b94c:	d343fd4b 	lsr	x11, x10, #3
        delta = intrev64ifbe(delta) >> shift;
    b950:	9240094e 	and	x14, x10, #0x7
        memcpy(&delta, leaf->data + byte, sizeof(delta));
    b954:	8b0b026c 	add	x12, x19, x11
    b958:	f9401d8d 	ldr	x13, [x12, #56]
        unsigned int shift = bitpos & 7;
    b95c:	7200094c 	ands	w12, w10, #0x7
        delta = intrev64ifbe(delta) >> shift;
    b960:	9ace25aa 	lsr	x10, x13, x14
        if (shift && bits > 64 - shift)
    b964:	54000120 	b.eq	b988 <zbtreeIteratorNext+0x1bc>  // b.none
    b968:	5280080d 	mov	w13, #0x40                  	// #64
    b96c:	4b0c01ac 	sub	w12, w13, w12
    b970:	6b09019f 	cmp	w12, w9
    b974:	540000a2 	b.cs	b988 <zbtreeIteratorNext+0x1bc>  // b.hs, b.nlast
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
    b978:	8b13016b 	add	x11, x11, x19
    b97c:	3941016b 	ldrb	w11, [x11, #64]
    b980:	9acc216b 	lsl	x11, x11, x12
    b984:	aa0a016a 	orr	x10, x11, x10
    b988:	9280000b 	mov	x11, #0xffffffffffffffff    	// #-1
        if (bits < 64)
    b98c:	7101013f 	cmp	w9, #0x40
    b990:	9ac9216c 	lsl	x12, x11, x9
    b994:	da8c2169 	csinv	x9, x11, x12, cs	// cs = hs, nlast
        delta <<= leaf->n.score_shift;
    b998:	39404e6b 	ldrb	w11, [x19, #19]
        if (bits < 64)
    b99c:	8a090149 	and	x9, x10, x9
        delta <<= leaf->n.score_shift;
    b9a0:	9acb2129 	lsl	x9, x9, x11
    b9a4:	14000002 	b	b9ac <zbtreeIteratorNext+0x1e0>
    b9a8:	aa1f03e9 	mov	x9, xzr
    b9ac:	f940166a 	ldr	x10, [x19, #40]
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
    b9b0:	7100011f 	cmp	w8, #0x0
    b9b4:	da890528 	cneg	x8, x9, ne	// ne = any
    b9b8:	8b080148 	add	x8, x10, x8
    if (ordered & (UINT64_C(1) << 63))
    b9bc:	9240f909 	and	x9, x8, #0x7fffffffffffffff
    b9c0:	f100011f 	cmp	x8, #0x0
    b9c4:	da88b128 	csinv	x8, x9, x8, lt	// lt = tstop
    if (score) *score = zbtScoreLeafScore(leaf, pos);
    b9c8:	f9000088 	str	x8, [x4]

    if (reverse) {
    b9cc:	340000a1 	cbz	w1, b9e0 <zbtreeIteratorNext+0x214>
        if (pos != 0) {
    b9d0:	34000174 	cbz	w20, b9fc <zbtreeIteratorNext+0x230>
            iter->pos--;
    b9d4:	b9400808 	ldr	w8, [x0, #8]
    b9d8:	51000508 	sub	w8, w8, #0x1
    b9dc:	14000013 	b	ba28 <zbtreeIteratorNext+0x25c>
            iter->leaf = leaf;
            iter->member_offsets = NULL;
            if (leaf) iter->pos = leaf->n.count - 1;
        }
    } else {
        if (pos + 1 < leaf->n.count) {
    b9e0:	39404668 	ldrb	w8, [x19, #17]
    b9e4:	11000689 	add	w9, w20, #0x1
    b9e8:	6b08013f 	cmp	w9, w8
    b9ec:	54000162 	b.cs	ba18 <zbtreeIteratorNext+0x24c>  // b.hs, b.nlast
            iter->pos++;
    b9f0:	b9400808 	ldr	w8, [x0, #8]
    b9f4:	11000508 	add	w8, w8, #0x1
    b9f8:	1400000c 	b	ba28 <zbtreeIteratorNext+0x25c>
            leaf = leaf->prev;
    b9fc:	f9400e68 	ldr	x8, [x19, #24]
            iter->member_offsets = NULL;
    ba00:	f900081f 	str	xzr, [x0, #16]
            iter->leaf = leaf;
    ba04:	f9000008 	str	x8, [x0]
            if (leaf) iter->pos = leaf->n.count - 1;
    ba08:	b4000128 	cbz	x8, ba2c <zbtreeIteratorNext+0x260>
    ba0c:	39404508 	ldrb	w8, [x8, #17]
    ba10:	51000508 	sub	w8, w8, #0x1
    ba14:	14000005 	b	ba28 <zbtreeIteratorNext+0x25c>
        } else {
            leaf = leaf->next;
    ba18:	f9401269 	ldr	x9, [x19, #32]
    ba1c:	2a1f03e8 	mov	w8, wzr
            iter->leaf = leaf;
            iter->member_offsets = NULL;
    ba20:	f900081f 	str	xzr, [x0, #16]
            iter->leaf = leaf;
    ba24:	f9000009 	str	x9, [x0]
    ba28:	b9000808 	str	w8, [x0, #8]
    ba2c:	52800020 	mov	w0, #0x1                   	// #1
            iter->pos = 0;
        }
    }
    return 1;
}
    ba30:	a9454ff4 	ldp	x20, x19, [sp, #80]
    ba34:	f9400bfb 	ldr	x27, [sp, #16]
    ba38:	a94457f6 	ldp	x22, x21, [sp, #64]
    ba3c:	a9435ff8 	ldp	x24, x23, [sp, #48]
    ba40:	a94267fa 	ldp	x26, x25, [sp, #32]
    ba44:	a8c67bfd 	ldp	x29, x30, [sp], #96
    ba48:	d65f03c0 	ret

Disassembly of section .fini:
