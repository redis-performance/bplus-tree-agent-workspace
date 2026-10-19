
<isolated-path>/original:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000011760 <zbtIndexScanSlot>:
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4166
                                      unsigned int slot_pos,
                                      unsigned long home_start,
                                      unsigned long home_end,
                                      zbtreeScanFunction *fn,
                                      void *privdata)
{
   11760:	55                   	push   %rbp
   11761:	48 89 e5             	mov    %rsp,%rbp
   11764:	41 57                	push   %r15
   11766:	41 56                	push   %r14
   11768:	41 55                	push   %r13
   1176a:	41 54                	push   %r12
   1176c:	53                   	push   %rbx
   1176d:	48 81 ec c8 01 00 00 	sub    $0x1c8,%rsp
   11774:	89 c8                	mov    %ecx,%eax
<isolated-path>/zset_btree.c:4167
    uint8_t tag = zbtIndexTags(bucket) >> (slot_pos * 8);
   11776:	4c 8b 3a             	mov    (%rdx),%r15
   11779:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   11780:	49 d3 ef             	shr    %cl,%r15
<isolated-path>/zset_btree.c:4168
    uint32_t id = zbtIndexGetId(table, bucket, slot_pos);
   11783:	44 8b 76 20          	mov    0x20(%rsi),%r14d
   11787:	89 c0                	mov    %eax,%eax
<isolated-path>/zset_btree.c:1775
    if (table->wide_ids) return bucket->wide.id[pos];
   11789:	45 85 f6             	test   %r14d,%r14d
   1178c:	74 18                	je     117a6 <zbtIndexScanSlot+0x46>
   1178e:	44 8b 64 82 10       	mov    0x10(%rdx,%rax,4),%r12d
   11793:	31 c0                	xor    %eax,%eax
<isolated-path>/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   11795:	4d 89 fd             	mov    %r15,%r13
   11798:	49 81 e5 ff 00 00 00 	and    $0xff,%r13
   1179f:	75 2c                	jne    117cd <zbtIndexScanSlot+0x6d>
   117a1:	e9 59 01 00 00       	jmp    118ff <zbtIndexScanSlot+0x19f>
<isolated-path>/zset_btree.c:1776
    uint16_t id = bucket->narrow.id[pos];
   117a6:	0f b7 4c 42 10       	movzwl 0x10(%rdx,%rax,2),%ecx
   117ab:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   117b1:	41 bc ff ff ff ff    	mov    $0xffffffff,%r12d
<isolated-path>/zset_btree.c:1777
    return id == UINT16_MAX ? ZBT_INDEX_DELETED_ID : id;
   117b7:	44 0f 45 e1          	cmovne %ecx,%r12d
   117bb:	31 c0                	xor    %eax,%eax
<isolated-path>/zset_btree.c:4169
    if (tag == 0 || id == ZBT_INDEX_DELETED_ID) return 0;
   117bd:	4d 89 fd             	mov    %r15,%r13
   117c0:	49 81 e5 ff 00 00 00 	and    $0xff,%r13
   117c7:	0f 84 32 01 00 00    	je     118ff <zbtIndexScanSlot+0x19f>
   117cd:	41 83 fc ff          	cmp    $0xffffffff,%r12d
   117d1:	0f 84 28 01 00 00    	je     118ff <zbtIndexScanSlot+0x19f>
<isolated-path>/zset_btree.c:4170
    if (home_end) {
   117d7:	4d 85 c9             	test   %r9,%r9
   117da:	0f 84 84 00 00 00    	je     11864 <zbtIndexScanSlot+0x104>
   117e0:	49 bb 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%r11
   117e7:	79 37 9e
zbtIndexTagBits():
<isolated-path>/zset_btree.c:1807
    uint64_t mixed = (uint64_t)tag * UINT64_C(0x9e3779b97f4a7c15);
   117ea:	4d 0f af dd          	imul   %r13,%r11
<isolated-path>/zset_btree.c:1809
           (UINT64_C(1) << (mixed >> 58)) |
   117ee:	4c 89 d9             	mov    %r11,%rcx
   117f1:	48 c1 e9 3a          	shr    $0x3a,%rcx
   117f5:	bb 01 00 00 00       	mov    $0x1,%ebx
   117fa:	48 d3 e3             	shl    %cl,%rbx
   117fd:	4d 89 c2             	mov    %r8,%r10
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4173
        uint64_t bits = zbtIndexTagBits(tag);
        unsigned long home;
        for (home = home_start; home < home_end; home++) {
   11800:	4d 39 c8             	cmp    %r9,%r8
   11803:	73 56                	jae    1185b <zbtIndexScanSlot+0xfb>
   11805:	4c 0f ab fb          	bts    %r15,%rbx
   11809:	49 c1 eb 24          	shr    $0x24,%r11
   1180d:	4c 0f ab db          	bts    %r11,%rbx
<isolated-path>/zset_btree.c:1775
    if (table->wide_ids) return bucket->wide.id[pos];
   11811:	31 c9                	xor    %ecx,%ecx
   11813:	45 85 f6             	test   %r14d,%r14d
   11816:	0f 95 c1             	setne  %cl
   11819:	4c 8b 1e             	mov    (%rsi),%r11
   1181c:	c1 e1 04             	shl    $0x4,%ecx
   1181f:	48 83 c9 20          	or     $0x20,%rcx
<isolated-path>/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   11823:	49 89 ca             	mov    %rcx,%r10
   11826:	4d 0f af d0          	imul   %r8,%r10
   1182a:	4f 8d 34 1a          	lea    (%r10,%r11,1),%r14
   1182e:	49 83 c6 08          	add    $0x8,%r14
   11832:	4d 89 c2             	mov    %r8,%r10
   11835:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   1183c:	00 00 00 00
<isolated-path>/zset_btree.c:4174
            if ((*zbtIndexHomeTagsAt(table, home) & bits) == bits) break;
   11840:	4d 8b 1e             	mov    (%r14),%r11
   11843:	49 f7 d3             	not    %r11
   11846:	4c 85 db             	test   %r11,%rbx
   11849:	74 10                	je     1185b <zbtIndexScanSlot+0xfb>
<isolated-path>/zset_btree.c:4173
        for (home = home_start; home < home_end; home++) {
   1184b:	49 ff c2             	inc    %r10
   1184e:	49 01 ce             	add    %rcx,%r14
   11851:	4d 39 d1             	cmp    %r10,%r9
   11854:	75 ea                	jne    11840 <zbtIndexScanSlot+0xe0>
   11856:	e9 a2 00 00 00       	jmp    118fd <zbtIndexScanSlot+0x19d>
<isolated-path>/zset_btree.c:4176
        }
        if (home == home_end) return 0;
   1185b:	4d 39 ca             	cmp    %r9,%r10
   1185e:	0f 84 99 00 00 00    	je     118fd <zbtIndexScanSlot+0x19d>
   11864:	48 89 55 90          	mov    %rdx,-0x70(%rbp)
<isolated-path>/zset_btree.c:4178
    }
    zbtScoreLeaf *leaf = id < zs->next_score_leaf_id ?
   11868:	44 3b 67 54          	cmp    0x54(%rdi),%r12d
   1186c:	73 77                	jae    118e5 <zbtIndexScanSlot+0x185>
<isolated-path>/zset_btree.c:4179
        zs->score_leaf_by_id[id] : NULL;
   1186e:	48 8b 4f 48          	mov    0x48(%rdi),%rcx
   11872:	45 89 e2             	mov    %r12d,%r10d
   11875:	4a 8b 14 d1          	mov    (%rcx,%r10,8),%rdx
<isolated-path>/zset_btree.c:4180
    if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {
   11879:	48 85 d2             	test   %rdx,%rdx
   1187c:	74 67                	je     118e5 <zbtIndexScanSlot+0x185>
   1187e:	89 d1                	mov    %edx,%ecx
   11880:	83 e1 01             	and    $0x1,%ecx
   11883:	75 60                	jne    118e5 <zbtIndexScanSlot+0x185>
   11885:	48 89 55 c0          	mov    %rdx,-0x40(%rbp)
<isolated-path>/zset_btree.c:4184
        serverAssert(zs->member_rehash && table == &zs->member_index);
        return 0;
    }
    serverAssert(leaf->id == id);
   11889:	44 39 62 30          	cmp    %r12d,0x30(%rdx)
   1188d:	0f 85 bd 06 00 00    	jne    11f50 <zbtIndexScanSlot+0x7f0>
<isolated-path>/zset_btree.c:4185
    if (zs->member_rehash) {
   11893:	48 8b 47 40          	mov    0x40(%rdi),%rax
   11897:	48 85 c0             	test   %rax,%rax
   1189a:	74 19                	je     118b5 <zbtIndexScanSlot+0x155>
   1189c:	48 8b 4d c0          	mov    -0x40(%rbp),%rcx
zbtIndexLeafMigrated():
<isolated-path>/zset_btree.c:2086
           leaf->n.index_resize == zs->member_rehash->resize_id;
   118a0:	0f b7 49 16          	movzwl 0x16(%rcx),%ecx
   118a4:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   118a8:	0f 94 c1             	sete   %cl
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4187
        int in_new = table == &zs->member_rehash->table;
        if (in_new != zbtIndexLeafMigrated(zs, leaf)) return 0;
   118ab:	48 39 f0             	cmp    %rsi,%rax
   118ae:	0f 95 c0             	setne  %al
   118b1:	38 c8                	cmp    %cl,%al
   118b3:	74 48                	je     118fd <zbtIndexScanSlot+0x19d>
   118b5:	4c 89 4d b8          	mov    %r9,-0x48(%rbp)
   118b9:	48 89 75 b0          	mov    %rsi,-0x50(%rbp)
   118bd:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   118c1:	0f b6 48 34          	movzbl 0x34(%rax),%ecx
   118c5:	31 db                	xor    %ebx,%ebx
<isolated-path>/zset_btree.c:363
    return (uint8_t *)(zbtScoreLeafOffsets(leaf) + leaf->n.count);
   118c7:	0f b6 40 11          	movzbl 0x11(%rax),%eax
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   118cb:	48 85 c9             	test   %rcx,%rcx
   118ce:	4c 89 45 a0          	mov    %r8,-0x60(%rbp)
zbtScoreLeafScoreBytes():
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   118d2:	74 3d                	je     11911 <zbtIndexScanSlot+0x1b1>
<isolated-path>/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   118d4:	0f af c8             	imul   %eax,%ecx
   118d7:	83 c1 07             	add    $0x7,%ecx
   118da:	c1 e9 03             	shr    $0x3,%ecx
<isolated-path>/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   118dd:	83 c1 09             	add    $0x9,%ecx
   118e0:	83 e1 fe             	and    $0xfffffffe,%ecx
   118e3:	eb 2e                	jmp    11913 <zbtIndexScanSlot+0x1b3>
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   118e5:	48 83 7f 40 00       	cmpq   $0x0,0x40(%rdi)
   118ea:	0f 84 48 06 00 00    	je     11f38 <zbtIndexScanSlot+0x7d8>
   118f0:	48 83 c7 18          	add    $0x18,%rdi
   118f4:	48 39 f7             	cmp    %rsi,%rdi
   118f7:	0f 85 3b 06 00 00    	jne    11f38 <zbtIndexScanSlot+0x7d8>
   118fd:	31 c0                	xor    %eax,%eax
<isolated-path>/zset_btree.c:4223
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
        emitted++;
    }
    serverAssert(home_end || emitted != 0);
    return emitted;
}
   118ff:	48 81 c4 c8 01 00 00 	add    $0x1c8,%rsp
   11906:	5b                   	pop    %rbx
   11907:	41 5c                	pop    %r12
   11909:	41 5d                	pop    %r13
   1190b:	41 5e                	pop    %r14
   1190d:	41 5f                	pop    %r15
   1190f:	5d                   	pop    %rbp
   11910:	c3                   	ret
   11911:	31 c9                	xor    %ecx,%ecx
   11913:	48 be ff fe fe fe fe 	movabs $0xfefefefefefefeff,%rsi
   1191a:	fe fe fe
   1191d:	48 8b 55 c0          	mov    -0x40(%rbp),%rdx
<isolated-path>/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   11921:	48 01 d1             	add    %rdx,%rcx
   11924:	48 83 c1 38          	add    $0x38,%rcx
<isolated-path>/zset_btree.c:363
    return (uint8_t *)(zbtScoreLeafOffsets(leaf) + leaf->n.count);
   11928:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
<isolated-path>/zset_btree.c:4196
                                           leaf->n.count, leaf->reversed,
   1192c:	0f b6 52 35          	movzbl 0x35(%rdx),%edx
   11930:	88 55 c8             	mov    %dl,-0x38(%rbp)
<isolated-path>/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   11933:	3c 08                	cmp    $0x8,%al
   11935:	73 79                	jae    119b0 <zbtIndexScanSlot+0x250>
<isolated-path>/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   11937:	a8 07                	test   $0x7,%al
   11939:	0f 84 8b 01 00 00    	je     11aca <zbtIndexScanSlot+0x36a>
   1193f:	89 c6                	mov    %eax,%esi
   11941:	83 e6 f8             	and    $0xfffffff8,%esi
   11944:	41 80 ff 01          	cmp    $0x1,%r15b
   11948:	0f 85 23 01 00 00    	jne    11a71 <zbtIndexScanSlot+0x311>
<isolated-path>/zset_btree.c:4136
    unsigned int last = reversed ? count - 1 : 0;
   1194e:	80 7d c8 00          	cmpb   $0x0,-0x38(%rbp)
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   11952:	74 49                	je     1199d <zbtIndexScanSlot+0x23d>
<isolated-path>/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   11954:	89 c2                	mov    %eax,%edx
   11956:	f7 d2                	not    %edx
   11958:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   1195e:	01 c2                	add    %eax,%edx
   11960:	eb 1c                	jmp    1197e <zbtIndexScanSlot+0x21e>
   11962:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11969:	1f 84 00 00 00 00 00
   11970:	48 ff c6             	inc    %rsi
   11973:	ff ca                	dec    %edx
   11975:	48 39 c6             	cmp    %rax,%rsi
   11978:	0f 83 4c 01 00 00    	jae    11aca <zbtIndexScanSlot+0x36a>
<isolated-path>/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   1197e:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   11982:	77 ec                	ja     11970 <zbtIndexScanSlot+0x210>
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   11984:	89 df                	mov    %ebx,%edi
   11986:	ff c3                	inc    %ebx
   11988:	89 94 bd 10 fe ff ff 	mov    %edx,-0x1f0(%rbp,%rdi,4)
   1198f:	eb df                	jmp    11970 <zbtIndexScanSlot+0x210>
<isolated-path>/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   11991:	48 ff c6             	inc    %rsi
   11994:	48 39 c6             	cmp    %rax,%rsi
   11997:	0f 83 2d 01 00 00    	jae    11aca <zbtIndexScanSlot+0x36a>
<isolated-path>/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   1199d:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   119a1:	77 ee                	ja     11991 <zbtIndexScanSlot+0x231>
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   119a3:	89 da                	mov    %ebx,%edx
   119a5:	ff c3                	inc    %ebx
   119a7:	89 b4 95 10 fe ff ff 	mov    %esi,-0x1f0(%rbp,%rdx,4)
   119ae:	eb e1                	jmp    11991 <zbtIndexScanSlot+0x231>
   119b0:	48 89 f2             	mov    %rsi,%rdx
<isolated-path>/zset_btree.c:4135
    unsigned int words = count / 8;
   119b3:	41 89 c0             	mov    %eax,%r8d
   119b6:	41 c1 e8 03          	shr    $0x3,%r8d
   119ba:	49 ba 01 01 01 01 01 	movabs $0x101010101010101,%r10
   119c1:	01 01 01
   119c4:	4d 0f af ea          	imul   %r10,%r13
<isolated-path>/zset_btree.c:4136
    unsigned int last = reversed ? count - 1 : 0;
   119c8:	80 7d c8 00          	cmpb   $0x0,-0x38(%rbp)
<isolated-path>/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   119cc:	0f 84 28 04 00 00    	je     11dfa <zbtIndexScanSlot+0x69a>
   119d2:	44 8d 48 ff          	lea    -0x1(%rax),%r9d
   119d6:	41 80 ff 01          	cmp    $0x1,%r15b
<isolated-path>/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   119da:	0f 85 cc 04 00 00    	jne    11eac <zbtIndexScanSlot+0x74c>
   119e0:	31 f6                	xor    %esi,%esi
   119e2:	31 db                	xor    %ebx,%ebx
   119e4:	eb 16                	jmp    119fc <zbtIndexScanSlot+0x29c>
   119e6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   119ed:	00 00 00
<isolated-path>/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   119f0:	48 ff c6             	inc    %rsi
   119f3:	4c 39 c6             	cmp    %r8,%rsi
   119f6:	0f 84 3b ff ff ff    	je     11937 <zbtIndexScanSlot+0x1d7>
<isolated-path>/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   119fc:	4c 8b 1c f1          	mov    (%rcx,%rsi,8),%r11
   11a00:	4c 89 df             	mov    %r11,%rdi
   11a03:	48 f7 d7             	not    %rdi
<isolated-path>/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   11a06:	4d 89 de             	mov    %r11,%r14
   11a09:	4d 31 d6             	xor    %r10,%r14
<isolated-path>/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   11a0c:	49 01 d6             	add    %rdx,%r14
   11a0f:	49 bc 80 80 80 80 80 	movabs $0x8080808080808080,%r12
   11a16:	80 80 80
   11a19:	4c 21 e7             	and    %r12,%rdi
   11a1c:	49 01 d3             	add    %rdx,%r11
<isolated-path>/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   11a1f:	4d 09 f3             	or     %r14,%r11
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11a22:	49 21 fb             	and    %rdi,%r11
   11a25:	74 c9                	je     119f0 <zbtIndexScanSlot+0x290>
   11a27:	4c 8d 34 f5 00 00 00 	lea    0x0(,%rsi,8),%r14
   11a2e:	00
   11a2f:	eb 18                	jmp    11a49 <zbtIndexScanSlot+0x2e9>
   11a31:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11a38:	0f 1f 84 00 00 00 00
   11a3f:	00
<isolated-path>/zset_btree.c:4145
            mask &= mask - 1;
   11a40:	49 8d 7b ff          	lea    -0x1(%r11),%rdi
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11a44:	49 21 fb             	and    %rdi,%r11
   11a47:	74 a7                	je     119f0 <zbtIndexScanSlot+0x290>
<isolated-path>/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   11a49:	f3 4d 0f bc e3       	tzcnt  %r11,%r12
   11a4e:	41 c1 ec 03          	shr    $0x3,%r12d
<isolated-path>/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   11a52:	45 09 f4             	or     %r14d,%r12d
<isolated-path>/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   11a55:	42 80 3c 21 01       	cmpb   $0x1,(%rcx,%r12,1)
   11a5a:	77 e4                	ja     11a40 <zbtIndexScanSlot+0x2e0>
<isolated-path>/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   11a5c:	44 89 cf             	mov    %r9d,%edi
   11a5f:	44 29 e7             	sub    %r12d,%edi
   11a62:	41 89 dc             	mov    %ebx,%r12d
   11a65:	ff c3                	inc    %ebx
   11a67:	42 89 bc a5 10 fe ff 	mov    %edi,-0x1f0(%rbp,%r12,4)
   11a6e:	ff
   11a6f:	eb cf                	jmp    11a40 <zbtIndexScanSlot+0x2e0>
<isolated-path>/zset_btree.c:4136
    unsigned int last = reversed ? count - 1 : 0;
   11a71:	80 7d c8 00          	cmpb   $0x0,-0x38(%rbp)
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   11a75:	74 40                	je     11ab7 <zbtIndexScanSlot+0x357>
<isolated-path>/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   11a77:	89 c7                	mov    %eax,%edi
   11a79:	f7 d7                	not    %edi
   11a7b:	81 cf 07 ff ff ff    	or     $0xffffff07,%edi
   11a81:	01 c7                	add    %eax,%edi
   11a83:	eb 15                	jmp    11a9a <zbtIndexScanSlot+0x33a>
   11a85:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   11a8c:	00 00 00 00
   11a90:	48 ff c6             	inc    %rsi
   11a93:	ff cf                	dec    %edi
   11a95:	48 39 c6             	cmp    %rax,%rsi
   11a98:	73 30                	jae    11aca <zbtIndexScanSlot+0x36a>
<isolated-path>/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   11a9a:	44 38 3c 31          	cmp    %r15b,(%rcx,%rsi,1)
   11a9e:	75 f0                	jne    11a90 <zbtIndexScanSlot+0x330>
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   11aa0:	41 89 d8             	mov    %ebx,%r8d
   11aa3:	ff c3                	inc    %ebx
   11aa5:	42 89 bc 85 10 fe ff 	mov    %edi,-0x1f0(%rbp,%r8,4)
   11aac:	ff
   11aad:	eb e1                	jmp    11a90 <zbtIndexScanSlot+0x330>
<isolated-path>/zset_btree.c:4148
    for (unsigned int pos = words * 8; pos < count; pos++) {
   11aaf:	48 ff c6             	inc    %rsi
   11ab2:	48 39 c6             	cmp    %rax,%rsi
   11ab5:	73 13                	jae    11aca <zbtIndexScanSlot+0x36a>
<isolated-path>/zset_btree.c:4149
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   11ab7:	44 38 3c 31          	cmp    %r15b,(%rcx,%rsi,1)
   11abb:	75 f2                	jne    11aaf <zbtIndexScanSlot+0x34f>
<isolated-path>/zset_btree.c:4150
            positions[found++] = reversed ? last - pos : pos;
   11abd:	89 df                	mov    %ebx,%edi
   11abf:	ff c3                	inc    %ebx
   11ac1:	89 b4 bd 10 fe ff ff 	mov    %esi,-0x1f0(%rbp,%rdi,4)
   11ac8:	eb e5                	jmp    11aaf <zbtIndexScanSlot+0x34f>
<isolated-path>/zset_btree.c:4198
    serverAssert(count != 0);
   11aca:	85 db                	test   %ebx,%ebx
   11acc:	0f 84 96 04 00 00    	je     11f68 <zbtIndexScanSlot+0x808>
   11ad2:	4c 8b 7d c0          	mov    -0x40(%rbp),%r15
   11ad6:	49 8d 47 38          	lea    0x38(%r15),%rax
   11ada:	48 89 45 c8          	mov    %rax,-0x38(%rbp)
<isolated-path>/zset_btree.c:4170
    if (home_end) {
   11ade:	48 83 7d b8 00       	cmpq   $0x0,-0x48(%rbp)
   11ae3:	0f 95 c0             	setne  %al
   11ae6:	83 fb 01             	cmp    $0x1,%ebx
   11ae9:	0f 95 c1             	setne  %cl
   11aec:	08 c1                	or     %al,%cl
   11aee:	88 4d d7             	mov    %cl,-0x29(%rbp)
<isolated-path>/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   11af1:	89 d8                	mov    %ebx,%eax
   11af3:	48 89 45 98          	mov    %rax,-0x68(%rbp)
   11af7:	45 31 f6             	xor    %r14d,%r14d
   11afa:	31 c0                	xor    %eax,%eax
   11afc:	48 89 45 a8          	mov    %rax,-0x58(%rbp)
   11b00:	eb 7f                	jmp    11b81 <zbtIndexScanSlot+0x421>
   11b02:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11b09:	1f 84 00 00 00 00 00
<isolated-path>/zset_btree.c:511
        if (bits < 64)
   11b10:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   11b17:	89 c1                	mov    %eax,%ecx
   11b19:	49 d3 e2             	shl    %cl,%r10
   11b1c:	40 80 ff 40          	cmp    $0x40,%dil
   11b20:	49 f7 d2             	not    %r10
   11b23:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   11b2a:	4c 0f 43 d0          	cmovae %rax,%r10
   11b2e:	4d 21 ca             	and    %r9,%r10
<isolated-path>/zset_btree.c:513
        delta <<= leaf->n.score_shift;
   11b31:	41 0f b6 4f 13       	movzbl 0x13(%r15),%ecx
   11b36:	49 d3 e2             	shl    %cl,%r10
<isolated-path>/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   11b39:	4c 89 d0             	mov    %r10,%rax
   11b3c:	48 f7 d8             	neg    %rax
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11b3f:	45 84 c0             	test   %r8b,%r8b
<isolated-path>/zset_btree.c:515
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
   11b42:	49 0f 44 c2          	cmove  %r10,%rax
   11b46:	49 03 47 28          	add    0x28(%r15),%rax
zbtOrderedToScore():
<isolated-path>/zset_btree.c:331
    if (ordered & (UINT64_C(1) << 63))
   11b4a:	48 89 c1             	mov    %rax,%rcx
   11b4d:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   11b54:	ff ff 7f
   11b57:	48 21 f9             	and    %rdi,%rcx
   11b5a:	48 85 c0             	test   %rax,%rax
   11b5d:	48 f7 d0             	not    %rax
   11b60:	48 0f 48 c1          	cmovs  %rcx,%rax
<isolated-path>/zset_btree.c:335
    memcpy(&score, &bits, sizeof(score));
   11b64:	66 48 0f 6e c0       	movq   %rax,%xmm0
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4218
        fn(privdata, ele, len, zbtScoreLeafScore(leaf, positions[i]));
   11b69:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11b6d:	ff 55 10             	call   *0x10(%rbp)
<isolated-path>/zset_btree.c:4219
        emitted++;
   11b70:	48 ff 45 a8          	incq   -0x58(%rbp)
<isolated-path>/zset_btree.c:4201
    for (unsigned int i = 0; i < count; i++) {
   11b74:	49 ff c6             	inc    %r14
   11b77:	4c 3b 75 98          	cmp    -0x68(%rbp),%r14
   11b7b:	0f 84 53 02 00 00    	je     11dd4 <zbtIndexScanSlot+0x674>
   11b81:	46 8b a4 b5 10 fe ff 	mov    -0x1f0(%rbp,%r14,4),%r12d
   11b88:	ff
   11b89:	45 89 e5             	mov    %r12d,%r13d
   11b8c:	41 f7 d5             	not    %r13d
<isolated-path>/zset_btree.c:4207
        if (count > 1 || home_end) {
   11b8f:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   11b93:	0f 84 27 01 00 00    	je     11cc0 <zbtIndexScanSlot+0x560>
zbtScoreLeafHash():
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   11b99:	41 0f b6 47 34       	movzbl 0x34(%r15),%eax
   11b9e:	48 85 c0             	test   %rax,%rax
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   11ba1:	74 4e                	je     11bf1 <zbtIndexScanSlot+0x491>
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   11ba3:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
<isolated-path>/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   11ba8:	0f af c1             	imul   %ecx,%eax
   11bab:	83 c0 07             	add    $0x7,%eax
   11bae:	c1 e8 03             	shr    $0x3,%eax
<isolated-path>/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   11bb1:	83 c0 09             	add    $0x9,%eax
   11bb4:	83 e0 fe             	and    $0xfffffffe,%eax
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11bb7:	41 80 7f 35 00       	cmpb   $0x0,0x35(%r15)
   11bbc:	44 89 e1             	mov    %r12d,%ecx
   11bbf:	74 08                	je     11bc9 <zbtIndexScanSlot+0x469>
   11bc1:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
   11bc6:	44 01 e9             	add    %r13d,%ecx
<isolated-path>/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   11bc9:	48 03 45 c8          	add    -0x38(%rbp),%rax
<isolated-path>/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   11bcd:	89 c9                	mov    %ecx,%ecx
   11bcf:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
<isolated-path>/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   11bd3:	49 8d 3c 07          	lea    (%r15,%rax,1),%rdi
<isolated-path>/zset_btree.c:625
    if (record[0] == ZBT_PACKED_EXTERNAL)
   11bd7:	41 0f b6 34 07       	movzbl (%r15,%rax,1),%esi
   11bdc:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   11be2:	74 1b                	je     11bff <zbtIndexScanSlot+0x49f>
   11be4:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   11bea:	75 1e                	jne    11c0a <zbtIndexScanSlot+0x4aa>
zbtExternalHash():
<isolated-path>/zset_btree.c:561
    memcpy(&hash, record + ZBT_EXTERNAL_HASH_OFFSET, sizeof(hash));
   11bec:	8b 47 01             	mov    0x1(%rdi),%eax
   11bef:	eb 26                	jmp    11c17 <zbtIndexScanSlot+0x4b7>
zbtScoreLeafHash():
   11bf1:	31 c0                	xor    %eax,%eax
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11bf3:	41 80 7f 35 00       	cmpb   $0x0,0x35(%r15)
   11bf8:	44 89 e1             	mov    %r12d,%ecx
   11bfb:	75 c4                	jne    11bc1 <zbtIndexScanSlot+0x461>
   11bfd:	eb ca                	jmp    11bc9 <zbtIndexScanSlot+0x469>
zbtPackedData():
<isolated-path>/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   11bff:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   11c03:	b8 03 00 00 00       	mov    $0x3,%eax
   11c08:	eb 05                	jmp    11c0f <zbtIndexScanSlot+0x4af>
   11c0a:	b8 01 00 00 00       	mov    $0x1,%eax
   11c0f:	48 01 c7             	add    %rax,%rdi
zbtScoreLeafHash():
<isolated-path>/zset_btree.c:629
    return (uint32_t)dictGenHashFunction(ele, len);
   11c12:	e8 49 05 00 00       	call   12160 <dictGenHashFunction>
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   11c17:	89 c0                	mov    %eax,%eax
   11c19:	48 8b 4d b0          	mov    -0x50(%rbp),%rcx
   11c1d:	48 8b 49 08          	mov    0x8(%rcx),%rcx
<isolated-path>/zset_btree.c:4170
    if (home_end) {
   11c21:	48 83 7d b8 00       	cmpq   $0x0,-0x48(%rbp)
<isolated-path>/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   11c26:	74 1b                	je     11c43 <zbtIndexScanSlot+0x4e3>
<isolated-path>/zset_btree.c:4209
            unsigned long home = hash & (table->size - 1);
   11c28:	8d 71 ff             	lea    -0x1(%rcx),%esi
   11c2b:	89 c2                	mov    %eax,%edx
   11c2d:	21 f2                	and    %esi,%edx
<isolated-path>/zset_btree.c:4210
            if (home_end && (home < home_start || home >= home_end))
   11c2f:	48 3b 55 a0          	cmp    -0x60(%rbp),%rdx
   11c33:	0f 82 3b ff ff ff    	jb     11b74 <zbtIndexScanSlot+0x414>
   11c39:	48 3b 55 b8          	cmp    -0x48(%rbp),%rdx
   11c3d:	0f 83 31 ff ff ff    	jae    11b74 <zbtIndexScanSlot+0x414>
   11c43:	83 fb 01             	cmp    $0x1,%ebx
<isolated-path>/zset_btree.c:4212
            if (count > 1 && !zbtIndexHashReachesBucket(table, hash, bucket))
   11c46:	74 78                	je     11cc0 <zbtIndexScanSlot+0x560>
zbtIndexHashReachesBucket():
<isolated-path>/zset_btree.c:4101
    unsigned long mask = table->size - 1;
   11c48:	48 89 ca             	mov    %rcx,%rdx
   11c4b:	48 83 ea 01          	sub    $0x1,%rdx
<isolated-path>/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   11c4f:	0f 82 1f ff ff ff    	jb     11b74 <zbtIndexScanSlot+0x414>
<isolated-path>/zset_btree.c:4102
    unsigned long index = hash & mask;
   11c55:	21 d0                	and    %edx,%eax
   11c57:	31 f6                	xor    %esi,%esi
   11c59:	48 8b 7d b0          	mov    -0x50(%rbp),%rdi
   11c5d:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   11c61:	48 8b 3f             	mov    (%rdi),%rdi
   11c64:	40 0f 95 c6          	setne  %sil
   11c68:	c1 e6 04             	shl    $0x4,%esi
   11c6b:	48 83 ce 20          	or     $0x20,%rsi
zbtIndexBucketAt():
   11c6f:	90                   	nop
<isolated-path>/zset_btree.c:1760
           index * zbtIndexBucketBytes(table));
   11c70:	49 89 c0             	mov    %rax,%r8
   11c73:	4c 0f af c6          	imul   %rsi,%r8
<isolated-path>/zset_btree.c:1759
    return (zbtIndexBucket *)((unsigned char *)table->buckets +
   11c77:	49 01 f8             	add    %rdi,%r8
zbtIndexHashReachesBucket():
<isolated-path>/zset_btree.c:4106
        if (bucket == target) return 1;
   11c7a:	4c 3b 45 90          	cmp    -0x70(%rbp),%r8
   11c7e:	74 40                	je     11cc0 <zbtIndexScanSlot+0x560>
<isolated-path>/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   11c80:	4d 8b 00             	mov    (%r8),%r8
   11c83:	4d 89 c1             	mov    %r8,%r9
   11c86:	49 f7 d1             	not    %r9
zbtIndexTagMask():
<isolated-path>/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   11c89:	49 ba ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r10
   11c90:	fe fe fe
   11c93:	4d 01 d0             	add    %r10,%r8
   11c96:	49 ba 80 80 80 80 80 	movabs $0x8080808080808080,%r10
   11c9d:	80 80 80
   11ca0:	4d 21 d1             	and    %r10,%r9
zbtIndexHashReachesBucket():
<isolated-path>/zset_btree.c:4107
        if (zbtIndexTagMask(zbtIndexTags(bucket), 0)) return 0;
   11ca3:	4d 85 c1             	test   %r8,%r9
   11ca6:	0f 85 c8 fe ff ff    	jne    11b74 <zbtIndexScanSlot+0x414>
<isolated-path>/zset_btree.c:4108
        index = (index + 1) & mask;
   11cac:	48 ff c0             	inc    %rax
   11caf:	48 21 d0             	and    %rdx,%rax
<isolated-path>/zset_btree.c:4104
    for (unsigned long probes = 0; probes < table->size; probes++) {
   11cb2:	48 ff c9             	dec    %rcx
   11cb5:	75 b9                	jne    11c70 <zbtIndexScanSlot+0x510>
   11cb7:	e9 b8 fe ff ff       	jmp    11b74 <zbtIndexScanSlot+0x414>
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:4104
   11cbc:	0f 1f 40 00          	nopl   0x0(%rax)
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   11cc0:	41 0f b6 7f 34       	movzbl 0x34(%r15),%edi
   11cc5:	48 85 ff             	test   %rdi,%rdi
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   11cc8:	0f 84 d2 00 00 00    	je     11da0 <zbtIndexScanSlot+0x640>
<isolated-path>/zset_btree.c:358
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
   11cce:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
<isolated-path>/zset_btree.c:351
    size_t bytes = ((size_t)count * score_bits + 7) / 8;
   11cd3:	89 f8                	mov    %edi,%eax
   11cd5:	0f af c1             	imul   %ecx,%eax
   11cd8:	83 c0 07             	add    $0x7,%eax
   11cdb:	c1 e8 03             	shr    $0x3,%eax
<isolated-path>/zset_btree.c:352
    return (bytes + 8 + 1) & ~(size_t)1;
   11cde:	83 c0 09             	add    $0x9,%eax
   11ce1:	83 e0 fe             	and    $0xfffffffe,%eax
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11ce4:	45 0f b6 47 35       	movzbl 0x35(%r15),%r8d
   11ce9:	44 89 e1             	mov    %r12d,%ecx
   11cec:	45 84 c0             	test   %r8b,%r8b
   11cef:	74 08                	je     11cf9 <zbtIndexScanSlot+0x599>
   11cf1:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
   11cf6:	44 01 e9             	add    %r13d,%ecx
<isolated-path>/zset_btree.c:357
    return (uint16_t *)(leaf->data +
   11cf9:	48 03 45 c8          	add    -0x38(%rbp),%rax
<isolated-path>/zset_btree.c:379
    return zbtScoreLeafOffsets(leaf)[zbtScoreLeafPhysicalPos(leaf, pos)];
   11cfd:	89 c9                	mov    %ecx,%ecx
   11cff:	0f b7 0c 48          	movzwl (%rax,%rcx,2),%ecx
<isolated-path>/zset_btree.c:609
    return (unsigned char *)leaf + zbtScoreLeafOffset(leaf, pos);
   11d03:	49 8d 04 0f          	lea    (%r15,%rcx,1),%rax
<isolated-path>/zset_btree.c:589
    if (record[0] < ZBT_PACKED_SHORT) {
   11d07:	41 0f b6 14 0f       	movzbl (%r15,%rcx,1),%edx
   11d0c:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11d13:	77 6b                	ja     11d80 <zbtIndexScanSlot+0x620>
<isolated-path>/zset_btree.c:591
        return record + 1;
   11d15:	48 ff c0             	inc    %rax
   11d18:	48 89 c6             	mov    %rax,%rsi
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   11d1b:	48 85 ff             	test   %rdi,%rdi
<isolated-path>/zset_btree.c:503
    if (bits != 0) {
   11d1e:	74 78                	je     11d98 <zbtIndexScanSlot+0x638>
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11d20:	45 84 c0             	test   %r8b,%r8b
zbtScoreLeafPhysicalPos():
<isolated-path>/zset_btree.c:372
   11d23:	74 08                	je     11d2d <zbtIndexScanSlot+0x5cd>
   11d25:	45 0f b6 67 11       	movzbl 0x11(%r15),%r12d
   11d2a:	45 01 ec             	add    %r13d,%r12d
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:504
        size_t bitpos = (size_t)zbtScoreLeafPhysicalPos(leaf, pos) * bits;
   11d2d:	45 89 e2             	mov    %r12d,%r10d
   11d30:	89 f8                	mov    %edi,%eax
   11d32:	4c 0f af d0          	imul   %rax,%r10
<isolated-path>/zset_btree.c:505
        size_t byte = bitpos / 8;
   11d36:	4d 89 d3             	mov    %r10,%r11
   11d39:	49 c1 eb 03          	shr    $0x3,%r11
   11d3d:	48 8b 4d c8          	mov    -0x38(%rbp),%rcx
<isolated-path>/zset_btree.c:507
        memcpy(&delta, leaf->data + byte, sizeof(delta));
   11d41:	4e 8b 0c 19          	mov    (%rcx,%r11,1),%r9
<isolated-path>/zset_btree.c:508
        delta = intrev64ifbe(delta) >> shift;
   11d45:	44 89 d1             	mov    %r10d,%ecx
   11d48:	80 e1 07             	and    $0x7,%cl
   11d4b:	49 d3 e9             	shr    %cl,%r9
<isolated-path>/zset_btree.c:509
        if (shift && bits > 64 - shift)
   11d4e:	41 83 e2 07          	and    $0x7,%r10d
   11d52:	0f 84 b8 fd ff ff    	je     11b10 <zbtIndexScanSlot+0x3b0>
   11d58:	b9 40 00 00 00       	mov    $0x40,%ecx
   11d5d:	44 29 d1             	sub    %r10d,%ecx
   11d60:	39 f9                	cmp    %edi,%ecx
   11d62:	0f 83 a8 fd ff ff    	jae    11b10 <zbtIndexScanSlot+0x3b0>
<isolated-path>/zset_btree.c:510
            delta |= (uint64_t)leaf->data[byte + 8] << (64 - shift);
   11d68:	47 0f b6 54 3b 40    	movzbl 0x40(%r11,%r15,1),%r10d
   11d6e:	49 d3 e2             	shl    %cl,%r10
   11d71:	4d 09 d1             	or     %r10,%r9
   11d74:	e9 97 fd ff ff       	jmp    11b10 <zbtIndexScanSlot+0x3b0>
   11d79:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
<isolated-path>/zset_btree.c:592
    } else if (record[0] == ZBT_PACKED_SHORT) {
   11d80:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11d86:	75 30                	jne    11db8 <zbtIndexScanSlot+0x658>
<isolated-path>/zset_btree.c:594
        memcpy(&shortlen, record + 1, sizeof(shortlen));
   11d88:	0f b7 50 01          	movzwl 0x1(%rax),%edx
<isolated-path>/zset_btree.c:596
        return record + 3;
   11d8c:	48 83 c0 03          	add    $0x3,%rax
   11d90:	48 89 c6             	mov    %rax,%rsi
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   11d93:	48 85 ff             	test   %rdi,%rdi
<isolated-path>/zset_btree.c:503
    if (bits != 0) {
   11d96:	75 88                	jne    11d20 <zbtIndexScanSlot+0x5c0>
   11d98:	45 31 d2             	xor    %r10d,%r10d
   11d9b:	e9 99 fd ff ff       	jmp    11b39 <zbtIndexScanSlot+0x3d9>
   11da0:	31 c0                	xor    %eax,%eax
<isolated-path>/zset_btree.c:372
    return leaf->reversed ? leaf->n.count - pos - 1 : pos;
   11da2:	45 0f b6 47 35       	movzbl 0x35(%r15),%r8d
   11da7:	44 89 e1             	mov    %r12d,%ecx
   11daa:	45 84 c0             	test   %r8b,%r8b
   11dad:	0f 85 3e ff ff ff    	jne    11cf1 <zbtIndexScanSlot+0x591>
   11db3:	e9 41 ff ff ff       	jmp    11cf9 <zbtIndexScanSlot+0x599>
zbtExternalPointer():
<isolated-path>/zset_btree.c:576
    memcpy(&ptr, record + ZBT_EXTERNAL_POINTER_OFFSET, sizeof(ptr));
   11db8:	48 8b 70 0d          	mov    0xd(%rax),%rsi
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:599
        serverAssert(ptr != NULL);
   11dbc:	48 85 f6             	test   %rsi,%rsi
   11dbf:	0f 84 5b 01 00 00    	je     11f20 <zbtIndexScanSlot+0x7c0>
zbtExternalLength():
<isolated-path>/zset_btree.c:568
    memcpy(&len, record + ZBT_EXTERNAL_LENGTH_OFFSET, sizeof(len));
   11dc5:	48 8b 50 05          	mov    0x5(%rax),%rdx
zbtIndexScanSlot():
<isolated-path>/zset_btree.c:350
    if (score_bits == 0) return 0;
   11dc9:	48 85 ff             	test   %rdi,%rdi
<isolated-path>/zset_btree.c:503
    if (bits != 0) {
   11dcc:	0f 85 4e ff ff ff    	jne    11d20 <zbtIndexScanSlot+0x5c0>
   11dd2:	eb c4                	jmp    11d98 <zbtIndexScanSlot+0x638>
   11dd4:	48 8b 45 a8          	mov    -0x58(%rbp),%rax
<isolated-path>/zset_btree.c:4221
    serverAssert(home_end || emitted != 0);
   11dd8:	48 09 45 b8          	or     %rax,-0x48(%rbp)
   11ddc:	0f 85 1d fb ff ff    	jne    118ff <zbtIndexScanSlot+0x19f>
   11de2:	48 8d 3d 35 18 00 00 	lea    0x1835(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11de9:	48 8d 15 b0 1d 00 00 	lea    0x1db0(%rip),%rdx        # 13ba0 <_IO_stdin_used+0xba0>
   11df0:	be 7d 10 00 00       	mov    $0x107d,%esi
   11df5:	e8 86 01 00 00       	call   11f80 <standalone_panic>
   11dfa:	45 31 c9             	xor    %r9d,%r9d
   11dfd:	45 89 fa             	mov    %r15d,%r10d
   11e00:	41 80 f2 01          	xor    $0x1,%r10b
   11e04:	31 db                	xor    %ebx,%ebx
   11e06:	eb 17                	jmp    11e1f <zbtIndexScanSlot+0x6bf>
   11e08:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   11e0f:	00
<isolated-path>/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   11e10:	49 ff c1             	inc    %r9
   11e13:	4d 39 c1             	cmp    %r8,%r9
   11e16:	49 89 f5             	mov    %rsi,%r13
   11e19:	0f 84 18 fb ff ff    	je     11937 <zbtIndexScanSlot+0x1d7>
<isolated-path>/zset_btree.c:4138
        uint64_t word = zbtLeafTagWord(tags + w * 8);
   11e1f:	4e 8b 34 c9          	mov    (%rcx,%r9,8),%r14
<isolated-path>/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   11e23:	4d 89 f4             	mov    %r14,%r12
   11e26:	4d 31 ec             	xor    %r13,%r12
   11e29:	4d 89 e3             	mov    %r12,%r11
   11e2c:	49 f7 d3             	not    %r11
<isolated-path>/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   11e2f:	49 01 d4             	add    %rdx,%r12
   11e32:	48 be 80 80 80 80 80 	movabs $0x8080808080808080,%rsi
   11e39:	80 80 80
   11e3c:	49 21 f3             	and    %rsi,%r11
   11e3f:	4d 21 e3             	and    %r12,%r11
   11e42:	41 80 ff 01          	cmp    $0x1,%r15b
<isolated-path>/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   11e46:	75 10                	jne    11e58 <zbtIndexScanSlot+0x6f8>
<isolated-path>/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   11e48:	4d 8d 24 16          	lea    (%r14,%rdx,1),%r12
   11e4c:	49 f7 d6             	not    %r14
   11e4f:	49 21 f6             	and    %rsi,%r14
   11e52:	4d 21 e6             	and    %r12,%r14
<isolated-path>/zset_btree.c:4140
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
   11e55:	4d 09 f3             	or     %r14,%r11
   11e58:	4c 89 ee             	mov    %r13,%rsi
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11e5b:	4d 85 db             	test   %r11,%r11
   11e5e:	74 b0                	je     11e10 <zbtIndexScanSlot+0x6b0>
   11e60:	4e 8d 34 cd 00 00 00 	lea    0x0(,%r9,8),%r14
   11e67:	00
   11e68:	eb 1b                	jmp    11e85 <zbtIndexScanSlot+0x725>
   11e6a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
<isolated-path>/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   11e70:	89 df                	mov    %ebx,%edi
   11e72:	ff c3                	inc    %ebx
   11e74:	44 89 a4 bd 10 fe ff 	mov    %r12d,-0x1f0(%rbp,%rdi,4)
   11e7b:	ff
<isolated-path>/zset_btree.c:4145
            mask &= mask - 1;
   11e7c:	49 8d 7b ff          	lea    -0x1(%r11),%rdi
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11e80:	49 21 fb             	and    %rdi,%r11
   11e83:	74 8b                	je     11e10 <zbtIndexScanSlot+0x6b0>
<isolated-path>/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   11e85:	f3 4d 0f bc e3       	tzcnt  %r11,%r12
   11e8a:	41 c1 ec 03          	shr    $0x3,%r12d
<isolated-path>/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   11e8e:	45 09 f4             	or     %r14d,%r12d
<isolated-path>/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   11e91:	42 0f b6 3c 21       	movzbl (%rcx,%r12,1),%edi
   11e96:	45 89 d5             	mov    %r10d,%r13d
   11e99:	41 08 fd             	or     %dil,%r13b
   11e9c:	41 0f 94 c5          	sete   %r13b
   11ea0:	44 38 ff             	cmp    %r15b,%dil
   11ea3:	74 cb                	je     11e70 <zbtIndexScanSlot+0x710>
   11ea5:	45 84 ed             	test   %r13b,%r13b
   11ea8:	74 d2                	je     11e7c <zbtIndexScanSlot+0x71c>
   11eaa:	eb c4                	jmp    11e70 <zbtIndexScanSlot+0x710>
   11eac:	45 31 d2             	xor    %r10d,%r10d
   11eaf:	31 db                	xor    %ebx,%ebx
   11eb1:	48 be 80 80 80 80 80 	movabs $0x8080808080808080,%rsi
   11eb8:	80 80 80
   11ebb:	eb 0f                	jmp    11ecc <zbtIndexScanSlot+0x76c>
   11ebd:	0f 1f 00             	nopl   (%rax)
<isolated-path>/zset_btree.c:4137
    for (unsigned int w = 0; w < words; w++) {
   11ec0:	49 ff c2             	inc    %r10
   11ec3:	4d 39 c2             	cmp    %r8,%r10
   11ec6:	0f 84 6b fa ff ff    	je     11937 <zbtIndexScanSlot+0x1d7>
   11ecc:	4a 8b 3c d1          	mov    (%rcx,%r10,8),%rdi
<isolated-path>/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
   11ed0:	4c 31 ef             	xor    %r13,%rdi
   11ed3:	49 89 fb             	mov    %rdi,%r11
   11ed6:	49 f7 d3             	not    %r11
<isolated-path>/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &
   11ed9:	48 01 d7             	add    %rdx,%rdi
   11edc:	49 21 f3             	and    %rsi,%r11
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11edf:	49 21 fb             	and    %rdi,%r11
   11ee2:	74 dc                	je     11ec0 <zbtIndexScanSlot+0x760>
   11ee4:	4e 8d 34 d5 00 00 00 	lea    0x0(,%r10,8),%r14
   11eeb:	00
   11eec:	eb 0b                	jmp    11ef9 <zbtIndexScanSlot+0x799>
   11eee:	66 90                	xchg   %ax,%ax
<isolated-path>/zset_btree.c:4145
            mask &= mask - 1;
   11ef0:	49 8d 7b ff          	lea    -0x1(%r11),%rdi
<isolated-path>/zset_btree.c:4141
        while (mask) {
   11ef4:	49 21 fb             	and    %rdi,%r11
   11ef7:	74 c7                	je     11ec0 <zbtIndexScanSlot+0x760>
<isolated-path>/zset_btree.c:1839
    return __builtin_ctzll(mask) >> 3;
   11ef9:	f3 4d 0f bc e3       	tzcnt  %r11,%r12
   11efe:	41 c1 ec 03          	shr    $0x3,%r12d
<isolated-path>/zset_btree.c:4142
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
   11f02:	45 09 f4             	or     %r14d,%r12d
<isolated-path>/zset_btree.c:4143
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
   11f05:	46 38 3c 21          	cmp    %r15b,(%rcx,%r12,1)
   11f09:	75 e5                	jne    11ef0 <zbtIndexScanSlot+0x790>
<isolated-path>/zset_btree.c:4144
                positions[found++] = reversed ? last - pos : pos;
   11f0b:	44 89 cf             	mov    %r9d,%edi
   11f0e:	44 29 e7             	sub    %r12d,%edi
   11f11:	41 89 dc             	mov    %ebx,%r12d
   11f14:	ff c3                	inc    %ebx
   11f16:	42 89 bc a5 10 fe ff 	mov    %edi,-0x1f0(%rbp,%r12,4)
   11f1d:	ff
   11f1e:	eb d0                	jmp    11ef0 <zbtIndexScanSlot+0x790>
<isolated-path>/zset_btree.c:599
        serverAssert(ptr != NULL);
   11f20:	48 8d 3d f7 16 00 00 	lea    0x16f7(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11f27:	48 8d 15 1c 18 00 00 	lea    0x181c(%rip),%rdx        # 1374a <_IO_stdin_used+0x74a>
   11f2e:	be 57 02 00 00       	mov    $0x257,%esi
   11f33:	e8 48 00 00 00       	call   11f80 <standalone_panic>
<isolated-path>/zset_btree.c:4181
        serverAssert(zs->member_rehash && table == &zs->member_index);
   11f38:	48 8d 3d df 16 00 00 	lea    0x16df(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11f3f:	48 8d 15 50 18 00 00 	lea    0x1850(%rip),%rdx        # 13796 <_IO_stdin_used+0x796>
   11f46:	be 55 10 00 00       	mov    $0x1055,%esi
   11f4b:	e8 30 00 00 00       	call   11f80 <standalone_panic>
<isolated-path>/zset_btree.c:4184
    serverAssert(leaf->id == id);
   11f50:	48 8d 3d c7 16 00 00 	lea    0x16c7(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11f57:	48 8d 15 19 18 00 00 	lea    0x1819(%rip),%rdx        # 13777 <_IO_stdin_used+0x777>
   11f5e:	be 58 10 00 00       	mov    $0x1058,%esi
   11f63:	e8 18 00 00 00       	call   11f80 <standalone_panic>
<isolated-path>/zset_btree.c:4198
    serverAssert(count != 0);
   11f68:	48 8d 3d af 16 00 00 	lea    0x16af(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11f6f:	48 8d 15 1f 1c 00 00 	lea    0x1c1f(%rip),%rdx        # 13b95 <_IO_stdin_used+0xb95>
   11f76:	be 66 10 00 00       	mov    $0x1066,%esi
   11f7b:	e8 00 00 00 00       	call   11f80 <standalone_panic>

Disassembly of section .fini:
