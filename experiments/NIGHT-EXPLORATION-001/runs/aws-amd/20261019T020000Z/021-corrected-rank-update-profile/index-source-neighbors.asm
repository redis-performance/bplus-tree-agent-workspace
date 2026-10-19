zbtIndexMove+0x2b0
    a47e:	74 3e                	je     a4be <zbtIndexMove+0x2ce>
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1791
        bucket->wide.id[pos] = id;
    a480:	c7 44 90 10 ff ff ff 	movl   $0xffffffff,0x10(%rax,%rdx,4)
    a487:	ff
    a488:	eb 3b                	jmp    a4c5 <zbtIndexMove+0x2d5>
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1793
        serverAssert(id == ZBT_INDEX_DELETED_ID || id < UINT16_MAX);
    a48a:	41 8d 56 01          	lea    0x1(%r14),%edx
    a48e:	81 fa 00 00 01 00    	cmp    $0x10000,%edx
    a494:	0f 83 c3 00 00 00    	jae    a55d <zbtIndexMove+0x36d>
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1794
        bucket->narrow.id[pos] = id == ZBT_INDEX_DELETED_ID ?
    a49a:	66 44 89 74 48 10    	mov    %r14w,0x10(%rax,%rcx,2)
    a4a0:	eb 36                	jmp    a4d8 <zbtIndexMove+0x2e8>
    a4a2:	66 c7 44 50 10 ff ff 	movw   $0xffff,0x10(%rax,%rdx,2)
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:2381
        source->used--;
    a4a9:	48 ff 49 10          	decq   0x10(%rcx)

zbtreeRank+0x68b
    6b04:	c1 e1 04             	shl    $0x4,%ecx
    6b07:	48 83 c9 20          	or     $0x20,%rcx
    6b0b:	4c 89 55 88          	mov    %r10,-0x78(%rbp)
zbtIndexBucketAt():
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1760
           index * zbtIndexBucketBytes(table));
    6b0f:	49 0f af ca          	imul   %r10,%rcx
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1759
    return (zbtIndexBucket *)((unsigned char *)table->buckets +
    6b13:	4c 8d 2c 08          	lea    (%rax,%rcx,1),%r13
    6b17:	4c 8b 24 08          	mov    (%rax,%rcx,1),%r12
zbtIndexTagMask():
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1832
    uint64_t x = tags ^ (UINT64_C(0x0101010101010101) * tag);
    6b1b:	4c 33 65 90          	xor    -0x70(%rbp),%r12
    6b1f:	4c 89 e0             	mov    %r12,%rax
    6b22:	48 f7 d0             	not    %rax
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/src/zset_btree.c:1833
    return (x - UINT64_C(0x0101010101010101)) & ~x &

zbtreeFindForAdd+0x29
    5774:	41 57                	push   %r15
    5776:	41 56                	push   %r14
    5778:	41 55                	push   %r13
    577a:	41 54                	push   %r12
    577c:	53                   	push   %rbx
    577d:	48 81 ec 98 00 00 00 	sub    $0x98,%rsp
    5784:	49 89 ce             	mov    %rcx,%r14
    5787:	48 89 95 50 ff ff ff 	mov    %rdx,-0xb0(%rbp)
    578e:	49 89 f7             	mov    %rsi,%r15
    5791:	48 89 7d a0          	mov    %rdi,-0x60(%rbp)
    5795:	0f b6 76 ff          	movzbl -0x1(%rsi),%esi
sdsType():
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/vendor/redis/sds.h:70
    return flags & SDS_TYPE_MASK;
    5799:	89 f0                	mov    %esi,%eax
    579b:	83 e0 07             	and    $0x7,%eax
sdslen():
<remote_root>/repo/scratch/amd-corrected-rank-update-13e459ff8/source/vendor/redis/sds.h:99
    switch (sdsType(s)) {
