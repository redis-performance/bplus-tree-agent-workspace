
scratch/amd-lowerbound-build/A/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000a770 <zbtScoreLeafLowerBound>:
    a770:	55                   	push   rbp
    a771:	48 89 e5             	mov    rbp,rsp
    a774:	41 57                	push   r15
    a776:	41 56                	push   r14
    a778:	41 55                	push   r13
    a77a:	41 54                	push   r12
    a77c:	53                   	push   rbx
    a77d:	48 83 ec 28          	sub    rsp,0x28
    a781:	48 89 75 b0          	mov    QWORD PTR [rbp-0x50],rsi
    a785:	44 0f b6 4f 11       	movzx  r9d,BYTE PTR [rdi+0x11]
    a78a:	45 85 c9             	test   r9d,r9d
    a78d:	0f 84 46 02 00 00    	je     a9d9 <zbtScoreLeafLowerBound+0x269>
    a793:	49 89 ff             	mov    r15,rdi
    a796:	48 89 55 c8          	mov    QWORD PTR [rbp-0x38],rdx
    a79a:	4c 8d 57 38          	lea    r10,[rdi+0x38]
    a79e:	45 31 e4             	xor    r12d,r12d
    a7a1:	49 bb ff ff ff ff ff 	movabs r11,0x7fffffffffffffff
    a7a8:	ff ff 7f 
    a7ab:	49 c7 c5 ff ff ff ff 	mov    r13,0xffffffffffffffff
    a7b2:	f2 0f 11 45 b8       	movsd  QWORD PTR [rbp-0x48],xmm0
    a7b7:	4c 89 55 c0          	mov    QWORD PTR [rbp-0x40],r10
    a7bb:	eb 0f                	jmp    a7cc <zbtScoreLeafLowerBound+0x5c>
    a7bd:	0f 1f 00             	nop    DWORD PTR [rax]
    a7c0:	45 89 f1             	mov    r9d,r14d
    a7c3:	45 39 cc             	cmp    r12d,r9d
    a7c6:	0f 83 10 02 00 00    	jae    a9dc <zbtScoreLeafLowerBound+0x26c>
    a7cc:	45 89 ce             	mov    r14d,r9d
    a7cf:	45 29 e6             	sub    r14d,r12d
    a7d2:	41 d1 ee             	shr    r14d,1
    a7d5:	45 01 e6             	add    r14d,r12d
    a7d8:	41 0f b6 57 34       	movzx  edx,BYTE PTR [r15+0x34]
    a7dd:	41 0f b6 77 35       	movzx  esi,BYTE PTR [r15+0x35]
    a7e2:	85 d2                	test   edx,edx
    a7e4:	74 7a                	je     a860 <zbtScoreLeafLowerBound+0xf0>
    a7e6:	44 89 f0             	mov    eax,r14d
    a7e9:	40 84 f6             	test   sil,sil
    a7ec:	74 0c                	je     a7fa <zbtScoreLeafLowerBound+0x8a>
    a7ee:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    a7f3:	44 89 f0             	mov    eax,r14d
    a7f6:	f7 d0                	not    eax
    a7f8:	01 c8                	add    eax,ecx
    a7fa:	41 89 c0             	mov    r8d,eax
    a7fd:	4c 0f af c2          	imul   r8,rdx
    a801:	4c 89 c7             	mov    rdi,r8
    a804:	48 c1 ef 03          	shr    rdi,0x3
    a808:	49 8b 04 3a          	mov    rax,QWORD PTR [r10+rdi*1]
    a80c:	44 89 c1             	mov    ecx,r8d
    a80f:	80 e1 07             	and    cl,0x7
    a812:	48 d3 e8             	shr    rax,cl
    a815:	41 83 e0 07          	and    r8d,0x7
    a819:	74 18                	je     a833 <zbtScoreLeafLowerBound+0xc3>
    a81b:	b9 40 00 00 00       	mov    ecx,0x40
    a820:	44 29 c1             	sub    ecx,r8d
    a823:	39 d1                	cmp    ecx,edx
    a825:	73 0c                	jae    a833 <zbtScoreLeafLowerBound+0xc3>
    a827:	42 0f b6 7c 3f 40    	movzx  edi,BYTE PTR [rdi+r15*1+0x40]
    a82d:	48 d3 e7             	shl    rdi,cl
    a830:	48 09 f8             	or     rax,rdi
    a833:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    a83a:	89 d1                	mov    ecx,edx
    a83c:	48 d3 e7             	shl    rdi,cl
    a83f:	80 fa 40             	cmp    dl,0x40
    a842:	48 f7 d7             	not    rdi
    a845:	49 0f 43 fd          	cmovae rdi,r13
    a849:	48 21 c7             	and    rdi,rax
    a84c:	41 0f b6 4f 13       	movzx  ecx,BYTE PTR [r15+0x13]
    a851:	48 d3 e7             	shl    rdi,cl
    a854:	eb 0c                	jmp    a862 <zbtScoreLeafLowerBound+0xf2>
    a856:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    a85d:	00 00 00 
    a860:	31 ff                	xor    edi,edi
    a862:	48 89 f8             	mov    rax,rdi
    a865:	48 f7 d8             	neg    rax
    a868:	40 84 f6             	test   sil,sil
    a86b:	48 0f 44 c7          	cmove  rax,rdi
    a86f:	49 03 47 28          	add    rax,QWORD PTR [r15+0x28]
    a873:	48 89 c1             	mov    rcx,rax
    a876:	4c 21 d9             	and    rcx,r11
    a879:	48 85 c0             	test   rax,rax
    a87c:	48 f7 d0             	not    rax
    a87f:	48 0f 48 c1          	cmovs  rax,rcx
    a883:	66 48 0f 6e c8       	movq   xmm1,rax
    a888:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a88d:	66 0f 2e c1          	ucomisd xmm0,xmm1
    a891:	0f 87 29 01 00 00    	ja     a9c0 <zbtScoreLeafLowerBound+0x250>
    a897:	b8 01 00 00 00       	mov    eax,0x1
    a89c:	66 0f 2e c8          	ucomisd xmm1,xmm0
    a8a0:	0f 87 1a 01 00 00    	ja     a9c0 <zbtScoreLeafLowerBound+0x250>
    a8a6:	48 85 d2             	test   rdx,rdx
    a8a9:	74 61                	je     a90c <zbtScoreLeafLowerBound+0x19c>
    a8ab:	41 0f b6 47 11       	movzx  eax,BYTE PTR [r15+0x11]
    a8b0:	0f af c2             	imul   eax,edx
    a8b3:	83 c0 07             	add    eax,0x7
    a8b6:	c1 e8 03             	shr    eax,0x3
    a8b9:	83 c0 09             	add    eax,0x9
    a8bc:	83 e0 fe             	and    eax,0xfffffffe
    a8bf:	44 89 f1             	mov    ecx,r14d
    a8c2:	40 84 f6             	test   sil,sil
    a8c5:	74 0c                	je     a8d3 <zbtScoreLeafLowerBound+0x163>
    a8c7:	41 0f b6 57 11       	movzx  edx,BYTE PTR [r15+0x11]
    a8cc:	44 89 f1             	mov    ecx,r14d
    a8cf:	f7 d1                	not    ecx
    a8d1:	01 d1                	add    ecx,edx
    a8d3:	4c 01 d0             	add    rax,r10
    a8d6:	89 c9                	mov    ecx,ecx
    a8d8:	0f b7 04 48          	movzx  eax,WORD PTR [rax+rcx*2]
    a8dc:	4d 8d 2c 07          	lea    r13,[r15+rax*1]
    a8e0:	41 0f b6 1c 07       	movzx  ebx,BYTE PTR [r15+rax*1]
    a8e5:	48 81 fb fd 00 00 00 	cmp    rbx,0xfd
    a8ec:	77 08                	ja     a8f6 <zbtScoreLeafLowerBound+0x186>
    a8ee:	49 ff c5             	inc    r13
    a8f1:	4c 89 ef             	mov    rdi,r13
    a8f4:	eb 7b                	jmp    a971 <zbtScoreLeafLowerBound+0x201>
    a8f6:	81 fb fe 00 00 00    	cmp    ebx,0xfe
    a8fc:	75 1a                	jne    a918 <zbtScoreLeafLowerBound+0x1a8>
    a8fe:	41 0f b7 5d 01       	movzx  ebx,WORD PTR [r13+0x1]
    a903:	49 83 c5 03          	add    r13,0x3
    a907:	4c 89 ef             	mov    rdi,r13
    a90a:	eb 65                	jmp    a971 <zbtScoreLeafLowerBound+0x201>
    a90c:	31 c0                	xor    eax,eax
    a90e:	44 89 f1             	mov    ecx,r14d
    a911:	40 84 f6             	test   sil,sil
    a914:	75 b1                	jne    a8c7 <zbtScoreLeafLowerBound+0x157>
    a916:	eb bb                	jmp    a8d3 <zbtScoreLeafLowerBound+0x163>
    a918:	49 8b 7d 0d          	mov    rdi,QWORD PTR [r13+0xd]
    a91c:	48 85 ff             	test   rdi,rdi
    a91f:	75 4c                	jne    a96d <zbtScoreLeafLowerBound+0x1fd>
    a921:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    a925:	48 8d 3d f2 8c 00 00 	lea    rdi,[rip+0x8cf2]        # 1361e <_IO_stdin_used+0x61e>
    a92c:	be 57 02 00 00       	mov    esi,0x257
    a931:	48 8d 15 12 8e 00 00 	lea    rdx,[rip+0x8e12]        # 1374a <_IO_stdin_used+0x74a>
    a938:	44 89 cb             	mov    ebx,r9d
    a93b:	e8 10 6d 00 00       	call   11650 <standalone_panic>
    a940:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    a944:	41 89 d9             	mov    r9d,ebx
    a947:	41 80 7d 00 ff       	cmp    BYTE PTR [r13+0x0],0xff
    a94c:	74 1f                	je     a96d <zbtScoreLeafLowerBound+0x1fd>
    a94e:	48 8d 3d c9 8c 00 00 	lea    rdi,[rip+0x8cc9]        # 1361e <_IO_stdin_used+0x61e>
    a955:	be 37 02 00 00       	mov    esi,0x237
    a95a:	48 8d 15 f5 8d 00 00 	lea    rdx,[rip+0x8df5]        # 13756 <_IO_stdin_used+0x756>
    a961:	e8 ea 6c 00 00       	call   11650 <standalone_panic>
    a966:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    a96a:	41 89 d9             	mov    r9d,ebx
    a96d:	49 8b 5d 05          	mov    rbx,QWORD PTR [r13+0x5]
    a971:	45 89 cd             	mov    r13d,r9d
    a974:	48 89 da             	mov    rdx,rbx
    a977:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    a97b:	48 39 c3             	cmp    rbx,rax
    a97e:	72 03                	jb     a983 <zbtScoreLeafLowerBound+0x213>
    a980:	48 89 c2             	mov    rdx,rax
    a983:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    a987:	e8 54 67 ff ff       	call   10e0 <memcmp@plt>
    a98c:	85 c0                	test   eax,eax
    a98e:	f2 0f 10 45 b8       	movsd  xmm0,QWORD PTR [rbp-0x48]
    a993:	45 89 e9             	mov    r9d,r13d
    a996:	4c 8b 55 c0          	mov    r10,QWORD PTR [rbp-0x40]
    a99a:	49 bb ff ff ff ff ff 	movabs r11,0x7fffffffffffffff
    a9a1:	ff ff 7f 
    a9a4:	49 c7 c5 ff ff ff ff 	mov    r13,0xffffffffffffffff
    a9ab:	75 13                	jne    a9c0 <zbtScoreLeafLowerBound+0x250>
    a9ad:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a9b2:	48 3b 5d c8          	cmp    rbx,QWORD PTR [rbp-0x38]
    a9b6:	72 08                	jb     a9c0 <zbtScoreLeafLowerBound+0x250>
    a9b8:	0f 97 c0             	seta   al
    a9bb:	0f b6 c0             	movzx  eax,al
    a9be:	66 90                	xchg   ax,ax
    a9c0:	85 c0                	test   eax,eax
    a9c2:	0f 89 f8 fd ff ff    	jns    a7c0 <zbtScoreLeafLowerBound+0x50>
    a9c8:	41 ff c6             	inc    r14d
    a9cb:	45 89 f4             	mov    r12d,r14d
    a9ce:	45 39 cc             	cmp    r12d,r9d
    a9d1:	0f 82 f5 fd ff ff    	jb     a7cc <zbtScoreLeafLowerBound+0x5c>
    a9d7:	eb 03                	jmp    a9dc <zbtScoreLeafLowerBound+0x26c>
    a9d9:	45 31 e4             	xor    r12d,r12d
    a9dc:	44 89 e0             	mov    eax,r12d
    a9df:	48 83 c4 28          	add    rsp,0x28
    a9e3:	5b                   	pop    rbx
    a9e4:	41 5c                	pop    r12
    a9e6:	41 5d                	pop    r13
    a9e8:	41 5e                	pop    r14
    a9ea:	41 5f                	pop    r15
    a9ec:	5d                   	pop    rbp
    a9ed:	c3                   	ret

Disassembly of section .fini:
