
build/size-matrix/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000f6a0 <zbtScoreDeleteInPlace>:
    f6a0:	55                   	push   rbp
    f6a1:	48 89 e5             	mov    rbp,rsp
    f6a4:	41 57                	push   r15
    f6a6:	41 56                	push   r14
    f6a8:	41 55                	push   r13
    f6aa:	41 54                	push   r12
    f6ac:	53                   	push   rbx
    f6ad:	48 81 ec b8 00 00 00 	sub    rsp,0xb8
    f6b4:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    f6b7:	89 d3                	mov    ebx,edx
    f6b9:	49 89 f7             	mov    r15,rsi
    f6bc:	48 89 7d c8          	mov    QWORD PTR [rbp-0x38],rdi
    f6c0:	44 0f b6 76 11       	movzx  r14d,BYTE PTR [rsi+0x11]
    f6c5:	45 8d 66 ff          	lea    r12d,[r14-0x1]
    f6c9:	41 39 d6             	cmp    r14d,edx
    f6cc:	76 05                	jbe    f6d3 <zbtScoreDeleteInPlace+0x33>
    f6ce:	45 85 e4             	test   r12d,r12d
    f6d1:	75 18                	jne    f6eb <zbtScoreDeleteInPlace+0x4b>
    f6d3:	48 8d 3d 44 3f 00 00 	lea    rdi,[rip+0x3f44]        # 1361e <_IO_stdin_used+0x61e>
    f6da:	48 8d 15 1a 43 00 00 	lea    rdx,[rip+0x431a]        # 139fb <_IO_stdin_used+0x9fb>
    f6e1:	be fb 09 00 00       	mov    esi,0x9fb
    f6e6:	e8 b5 1f 00 00       	call   116a0 <standalone_panic>
    f6eb:	41 80 7f 35 00       	cmp    BYTE PTR [r15+0x35],0x0
    f6f0:	74 09                	je     f6fb <zbtScoreDeleteInPlace+0x5b>
    f6f2:	41 0f b6 47 11       	movzx  eax,BYTE PTR [r15+0x11]
    f6f7:	f7 d3                	not    ebx
    f6f9:	01 c3                	add    ebx,eax
    f6fb:	41 0f b6 47 34       	movzx  eax,BYTE PTR [r15+0x34]
    f700:	48 85 c0             	test   rax,rax
    f703:	44 89 65 d4          	mov    DWORD PTR [rbp-0x2c],r12d
    f707:	74 1e                	je     f727 <zbtScoreDeleteInPlace+0x87>
    f709:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    f70e:	0f af c1             	imul   eax,ecx
    f711:	83 c0 07             	add    eax,0x7
    f714:	c1 e8 03             	shr    eax,0x3
    f717:	83 c0 09             	add    eax,0x9
    f71a:	83 e0 fe             	and    eax,0xfffffffe
    f71d:	4d 8d 24 07          	lea    r12,[r15+rax*1]
    f721:	49 83 c4 38          	add    r12,0x38
    f725:	eb 0b                	jmp    f732 <zbtScoreDeleteInPlace+0x92>
    f727:	4d 8d 67 38          	lea    r12,[r15+0x38]
    f72b:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    f730:	31 c0                	xor    eax,eax
    f732:	4c 01 f8             	add    rax,r15
    f735:	48 83 c0 38          	add    rax,0x38
    f739:	48 8d 34 48          	lea    rsi,[rax+rcx*2]
    f73d:	48 8d bd 20 ff ff ff 	lea    rdi,[rbp-0xe0]
    f744:	4c 89 f2             	mov    rdx,r14
    f747:	e8 d4 19 ff ff       	call   1120 <memcpy@plt>
    f74c:	89 d8                	mov    eax,ebx
    f74e:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    f752:	41 0f b7 34 44       	movzx  esi,WORD PTR [r12+rax*2]
    f757:	44 0f b7 ee          	movzx  r13d,si
    f75b:	43 0f b6 04 2f       	movzx  eax,BYTE PTR [r15+r13*1]
    f760:	3d fe 00 00 00       	cmp    eax,0xfe
    f765:	4c 89 e7             	mov    rdi,r12
    f768:	89 75 98             	mov    DWORD PTR [rbp-0x68],esi
    f76b:	89 5d d0             	mov    DWORD PTR [rbp-0x30],ebx
    f76e:	4c 89 65 b0          	mov    QWORD PTR [rbp-0x50],r12
    f772:	74 20                	je     f794 <zbtScoreDeleteInPlace+0xf4>
    f774:	3d ff 00 00 00       	cmp    eax,0xff
    f779:	75 1f                	jne    f79a <zbtScoreDeleteInPlace+0xfa>
    f77b:	83 7d c0 00          	cmp    DWORD PTR [rbp-0x40],0x0
    f77f:	74 44                	je     f7c5 <zbtScoreDeleteInPlace+0x125>
    f781:	41 89 f4             	mov    r12d,esi
    f784:	4b 8b 7c 2f 0d       	mov    rdi,QWORD PTR [r15+r13*1+0xd]
    f789:	48 85 ff             	test   rdi,rdi
    f78c:	74 3e                	je     f7cc <zbtScoreDeleteInPlace+0x12c>
    f78e:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    f792:	eb 56                	jmp    f7ea <zbtScoreDeleteInPlace+0x14a>
    f794:	43 0f b7 44 2f 01    	movzx  eax,WORD PTR [r15+r13*1+0x1]
    f79a:	31 c9                	xor    ecx,ecx
    f79c:	48 3d fe 00 00 00    	cmp    rax,0xfe
    f7a2:	0f 93 c1             	setae  cl
    f7a5:	48 8d 1c 48          	lea    rbx,[rax+rcx*2]
    f7a9:	48 ff c3             	inc    rbx
    f7ac:	83 7d c0 00          	cmp    DWORD PTR [rbp-0x40],0x0
    f7b0:	0f 84 81 00 00 00    	je     f837 <zbtScoreDeleteInPlace+0x197>
    f7b6:	41 0f b7 47 36       	movzx  eax,WORD PTR [r15+0x36]
    f7bb:	66 39 c6             	cmp    si,ax
    f7be:	75 51                	jne    f811 <zbtScoreDeleteInPlace+0x171>
    f7c0:	e9 88 00 00 00       	jmp    f84d <zbtScoreDeleteInPlace+0x1ad>
    f7c5:	bb 15 00 00 00       	mov    ebx,0x15
    f7ca:	eb 6b                	jmp    f837 <zbtScoreDeleteInPlace+0x197>
    f7cc:	48 8d 3d 4b 3e 00 00 	lea    rdi,[rip+0x3e4b]        # 1361e <_IO_stdin_used+0x61e>
    f7d3:	48 8d 15 3e 42 00 00 	lea    rdx,[rip+0x423e]        # 13a18 <_IO_stdin_used+0xa18>
    f7da:	be 07 0a 00 00       	mov    esi,0xa07
    f7df:	e8 bc 1e 00 00       	call   116a0 <standalone_panic>
    f7e4:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    f7e8:	31 ff                	xor    edi,edi
    f7ea:	e8 b1 20 00 00       	call   118a0 <zfree_usable>
    f7ef:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    f7f3:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    f7f7:	48 29 41 68          	sub    QWORD PTR [rcx+0x68],rax
    f7fb:	bb 15 00 00 00       	mov    ebx,0x15
    f800:	44 89 e6             	mov    esi,r12d
    f803:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    f807:	41 0f b7 47 36       	movzx  eax,WORD PTR [r15+0x36]
    f80c:	66 39 c6             	cmp    si,ax
    f80f:	74 3c                	je     f84d <zbtScoreDeleteInPlace+0x1ad>
    f811:	4d 85 f6             	test   r14,r14
    f814:	74 21                	je     f837 <zbtScoreDeleteInPlace+0x197>
    f816:	b9 01 00 00 00       	mov    ecx,0x1
    f81b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    f820:	0f b7 54 4f fe       	movzx  edx,WORD PTR [rdi+rcx*2-0x2]
    f825:	4c 39 f1             	cmp    rcx,r14
    f828:	73 08                	jae    f832 <zbtScoreDeleteInPlace+0x192>
    f82a:	48 ff c1             	inc    rcx
    f82d:	66 39 f2             	cmp    dx,si
    f830:	76 ee                	jbe    f820 <zbtScoreDeleteInPlace+0x180>
    f832:	66 39 f2             	cmp    dx,si
    f835:	77 16                	ja     f84d <zbtScoreDeleteInPlace+0x1ad>
    f837:	c7 45 bc 00 00 00 00 	mov    DWORD PTR [rbp-0x44],0x0
    f83e:	66 41 3b 77 36       	cmp    si,WORD PTR [r15+0x36]
    f843:	75 3b                	jne    f880 <zbtScoreDeleteInPlace+0x1e0>
    f845:	4d 8d 77 36          	lea    r14,[r15+0x36]
    f849:	89 f0                	mov    eax,esi
    f84b:	eb 27                	jmp    f874 <zbtScoreDeleteInPlace+0x1d4>
    f84d:	4d 8d 77 36          	lea    r14,[r15+0x36]
    f851:	49 8d 34 07          	lea    rsi,[r15+rax*1]
    f855:	49 89 fc             	mov    r12,rdi
    f858:	48 8d 3c 1e          	lea    rdi,[rsi+rbx*1]
    f85c:	49 29 c5             	sub    r13,rax
    f85f:	4c 89 ea             	mov    rdx,r13
    f862:	e8 f9 18 ff ff       	call   1160 <memmove@plt>
    f867:	4c 89 e7             	mov    rdi,r12
    f86a:	41 0f b7 47 36       	movzx  eax,WORD PTR [r15+0x36]
    f86f:	b1 01                	mov    cl,0x1
    f871:	89 4d bc             	mov    DWORD PTR [rbp-0x44],ecx
    f874:	44 8b 65 d4          	mov    r12d,DWORD PTR [rbp-0x2c]
    f878:	01 d8                	add    eax,ebx
    f87a:	66 41 89 06          	mov    WORD PTR [r14],ax
    f87e:	eb 04                	jmp    f884 <zbtScoreDeleteInPlace+0x1e4>
    f880:	44 8b 65 d4          	mov    r12d,DWORD PTR [rbp-0x2c]
    f884:	4d 8d 77 38          	lea    r14,[r15+0x38]
    f888:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    f88c:	48 8d 3c 47          	lea    rdi,[rdi+rax*2]
    f890:	41 0f b6 47 34       	movzx  eax,BYTE PTR [r15+0x34]
    f895:	85 c0                	test   eax,eax
    f897:	4c 89 7d c8          	mov    QWORD PTR [rbp-0x38],r15
    f89b:	0f 84 c8 01 00 00    	je     fa69 <zbtScoreDeleteInPlace+0x3c9>
    f8a1:	48 89 7d 80          	mov    QWORD PTR [rbp-0x80],rdi
    f8a5:	89 45 9c             	mov    DWORD PTR [rbp-0x64],eax
    f8a8:	89 c0                	mov    eax,eax
    f8aa:	48 89 45 90          	mov    QWORD PTR [rbp-0x70],rax
    f8ae:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    f8b3:	8b 45 d0             	mov    eax,DWORD PTR [rbp-0x30]
    f8b6:	41 89 c3             	mov    r11d,eax
    f8b9:	41 f7 d3             	not    r11d
    f8bc:	48 89 4d 88          	mov    QWORD PTR [rbp-0x78],rcx
    f8c0:	41 01 cb             	add    r11d,ecx
    f8c3:	0f 84 24 01 00 00    	je     f9ed <zbtScoreDeleteInPlace+0x34d>
    f8c9:	48 8b 45 90          	mov    rax,QWORD PTR [rbp-0x70]
    f8cd:	49 89 c4             	mov    r12,rax
    f8d0:	4c 0f af 65 a8       	imul   r12,QWORD PTR [rbp-0x58]
    f8d5:	4c 0f af d8          	imul   r11,rax
    f8d9:	4c 01 e0             	add    rax,r12
    f8dc:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
    f8e0:	45 31 d2             	xor    r10d,r10d
    f8e3:	eb 17                	jmp    f8fc <zbtScoreDeleteInPlace+0x25c>
    f8e5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    f8ec:	00 00 00 00
    f8f0:	49 01 d2             	add    r10,rdx
    f8f3:	4d 39 da             	cmp    r10,r11
    f8f6:	0f 83 f1 00 00 00    	jae    f9ed <zbtScoreDeleteInPlace+0x34d>
    f8fc:	4c 89 da             	mov    rdx,r11
    f8ff:	4c 29 d2             	sub    rdx,r10
    f902:	48 83 fa 40          	cmp    rdx,0x40
    f906:	b8 40 00 00 00       	mov    eax,0x40
    f90b:	48 0f 43 d0          	cmovae rdx,rax
    f90f:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    f913:	4a 8d 0c 10          	lea    rcx,[rax+r10*1]
    f917:	49 89 c8             	mov    r8,rcx
    f91a:	49 c1 e8 03          	shr    r8,0x3
    f91e:	89 c8                	mov    eax,ecx
    f920:	83 e0 07             	and    eax,0x7
    f923:	be 40 00 00 00       	mov    esi,0x40
    f928:	29 c6                	sub    esi,eax
    f92a:	4b 8b 04 06          	mov    rax,QWORD PTR [r14+r8*1]
    f92e:	80 e1 07             	and    cl,0x7
    f931:	48 d3 e8             	shr    rax,cl
    f934:	39 d6                	cmp    esi,edx
    f936:	73 0e                	jae    f946 <zbtScoreDeleteInPlace+0x2a6>
    f938:	47 0f b6 44 06 08    	movzx  r8d,BYTE PTR [r14+r8*1+0x8]
    f93e:	89 f1                	mov    ecx,esi
    f940:	49 d3 e0             	shl    r8,cl
    f943:	4c 09 c0             	or     rax,r8
    f946:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    f94d:	89 d1                	mov    ecx,edx
    f94f:	48 d3 e7             	shl    rdi,cl
    f952:	83 fa 40             	cmp    edx,0x40
    f955:	48 f7 d7             	not    rdi
    f958:	49 c7 c7 ff ff ff ff 	mov    r15,0xffffffffffffffff
    f95f:	49 0f 43 ff          	cmovae rdi,r15
    f963:	48 21 c7             	and    rdi,rax
    f966:	4f 8d 04 22          	lea    r8,[r10+r12*1]
    f96a:	4c 89 c0             	mov    rax,r8
    f96d:	48 c1 e8 03          	shr    rax,0x3
    f971:	41 83 e0 07          	and    r8d,0x7
    f975:	41 b9 40 00 00 00    	mov    r9d,0x40
    f97b:	45 29 c1             	sub    r9d,r8d
    f97e:	41 39 d1             	cmp    r9d,edx
    f981:	89 d6                	mov    esi,edx
    f983:	41 0f 42 f1          	cmovb  esi,r9d
    f987:	49 c7 c5 ff ff ff ff 	mov    r13,0xffffffffffffffff
    f98e:	89 f1                	mov    ecx,esi
    f990:	49 d3 e5             	shl    r13,cl
    f993:	83 fe 40             	cmp    esi,0x40
    f996:	49 f7 d5             	not    r13
    f999:	4d 0f 44 ef          	cmove  r13,r15
    f99d:	49 89 ff             	mov    r15,rdi
    f9a0:	4d 21 ef             	and    r15,r13
    f9a3:	44 89 c1             	mov    ecx,r8d
    f9a6:	49 d3 e5             	shl    r13,cl
    f9a9:	49 f7 d5             	not    r13
    f9ac:	4d 23 2c 06          	and    r13,QWORD PTR [r14+rax*1]
    f9b0:	49 d3 e7             	shl    r15,cl
    f9b3:	4d 09 ef             	or     r15,r13
    f9b6:	4d 89 3c 06          	mov    QWORD PTR [r14+rax*1],r15
    f9ba:	41 39 d1             	cmp    r9d,edx
    f9bd:	0f 83 2d ff ff ff    	jae    f8f0 <zbtScoreDeleteInPlace+0x250>
    f9c3:	41 89 d0             	mov    r8d,edx
    f9c6:	41 29 f0             	sub    r8d,esi
    f9c9:	45 0f b6 4c 06 08    	movzx  r9d,BYTE PTR [r14+rax*1+0x8]
    f9cf:	89 f1                	mov    ecx,esi
    f9d1:	48 d3 ef             	shr    rdi,cl
    f9d4:	41 31 f9             	xor    r9d,edi
    f9d7:	44 89 c1             	mov    ecx,r8d
    f9da:	41 d3 e9             	shr    r9d,cl
    f9dd:	41 d3 e1             	shl    r9d,cl
    f9e0:	41 31 f9             	xor    r9d,edi
    f9e3:	45 88 4c 06 08       	mov    BYTE PTR [r14+rax*1+0x8],r9b
    f9e8:	e9 03 ff ff ff       	jmp    f8f0 <zbtScoreDeleteInPlace+0x250>
    f9ed:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    f9f1:	48 8d 50 ff          	lea    rdx,[rax-0x1]
    f9f5:	48 0f af 55 90       	imul   rdx,QWORD PTR [rbp-0x70]
    f9fa:	48 89 d0             	mov    rax,rdx
    f9fd:	48 c1 e8 03          	shr    rax,0x3
    fa01:	89 d1                	mov    ecx,edx
    fa03:	83 e1 07             	and    ecx,0x7
    fa06:	bf 40 00 00 00       	mov    edi,0x40
    fa0b:	29 cf                	sub    edi,ecx
    fa0d:	44 8b 4d 9c          	mov    r9d,DWORD PTR [rbp-0x64]
    fa11:	44 39 cf             	cmp    edi,r9d
    fa14:	44 89 ce             	mov    esi,r9d
    fa17:	0f 42 f7             	cmovb  esi,edi
    fa1a:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    fa21:	89 f1                	mov    ecx,esi
    fa23:	49 d3 e0             	shl    r8,cl
    fa26:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
    fa2d:	83 fe 40             	cmp    esi,0x40
    fa30:	49 f7 d0             	not    r8
    fa33:	4c 0f 44 c1          	cmove  r8,rcx
    fa37:	80 e2 07             	and    dl,0x7
    fa3a:	89 d1                	mov    ecx,edx
    fa3c:	49 d3 e0             	shl    r8,cl
    fa3f:	49 f7 d0             	not    r8
    fa42:	4d 21 04 06          	and    QWORD PTR [r14+rax*1],r8
    fa46:	44 39 cf             	cmp    edi,r9d
    fa49:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    fa4d:	44 8b 65 d4          	mov    r12d,DWORD PTR [rbp-0x2c]
    fa51:	48 8b 7d 80          	mov    rdi,QWORD PTR [rbp-0x80]
    fa55:	73 12                	jae    fa69 <zbtScoreDeleteInPlace+0x3c9>
    fa57:	41 29 f1             	sub    r9d,esi
    fa5a:	ba ff ff ff ff       	mov    edx,0xffffffff
    fa5f:	44 89 c9             	mov    ecx,r9d
    fa62:	d3 e2                	shl    edx,cl
    fa64:	41 20 54 06 08       	and    BYTE PTR [r14+rax*1+0x8],dl
    fa69:	48 8d 77 02          	lea    rsi,[rdi+0x2]
    fa6d:	44 89 e0             	mov    eax,r12d
    fa70:	2b 45 d0             	sub    eax,DWORD PTR [rbp-0x30]
    fa73:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
    fa77:	48 8d 14 00          	lea    rdx,[rax+rax*1]
    fa7b:	e8 e0 16 ff ff       	call   1160 <memmove@plt>
    fa80:	41 0f b6 47 34       	movzx  eax,BYTE PTR [r15+0x34]
    fa85:	44 89 e1             	mov    ecx,r12d
    fa88:	45 89 e5             	mov    r13d,r12d
    fa8b:	48 85 c0             	test   rax,rax
    fa8e:	74 16                	je     faa6 <zbtScoreDeleteInPlace+0x406>
    fa90:	49 0f af c5          	imul   rax,r13
    fa94:	48 83 c0 07          	add    rax,0x7
    fa98:	48 c1 e8 03          	shr    rax,0x3
    fa9c:	48 83 c0 09          	add    rax,0x9
    faa0:	48 83 e0 fe          	and    rax,0xfffffffffffffffe
    faa4:	eb 02                	jmp    faa8 <zbtScoreDeleteInPlace+0x408>
    faa6:	31 c0                	xor    eax,eax
    faa8:	85 c9                	test   ecx,ecx
    faaa:	0f 94 45 d0          	sete   BYTE PTR [rbp-0x30]
    faae:	49 01 c6             	add    r14,rax
    fab1:	4a 8d 14 6d 00 00 00 	lea    rdx,[r13*2+0x0]
    fab8:	00
    fab9:	4c 89 f7             	mov    rdi,r14
    fabc:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    fac0:	e8 9b 16 ff ff       	call   1160 <memmove@plt>
    fac5:	4f 8d 3c 6e          	lea    r15,[r14+r13*2]
    fac9:	48 8d b5 20 ff ff ff 	lea    rsi,[rbp-0xe0]
    fad0:	4c 89 ff             	mov    rdi,r15
    fad3:	4c 8b 65 a8          	mov    r12,QWORD PTR [rbp-0x58]
    fad7:	4c 89 e2             	mov    rdx,r12
    fada:	e8 41 16 ff ff       	call   1120 <memcpy@plt>
    fadf:	4d 01 e7             	add    r15,r12
    fae2:	49 8d 34 2c          	lea    rsi,[r12+rbp*1]
    fae6:	48 81 c6 21 ff ff ff 	add    rsi,0xffffffffffffff21
    faed:	4c 89 ff             	mov    rdi,r15
    faf0:	48 8b 55 c0          	mov    rdx,QWORD PTR [rbp-0x40]
    faf4:	e8 27 16 ff ff       	call   1120 <memcpy@plt>
    faf9:	8b 4d d4             	mov    ecx,DWORD PTR [rbp-0x2c]
    fafc:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    fb00:	88 48 11             	mov    BYTE PTR [rax+0x11],cl
    fb03:	4c 89 68 08          	mov    QWORD PTR [rax+0x8],r13
    fb07:	8b 45 bc             	mov    eax,DWORD PTR [rbp-0x44]
    fb0a:	34 01                	xor    al,0x1
    fb0c:	0a 45 d0             	or     al,BYTE PTR [rbp-0x30]
    fb0f:	8b 7d 98             	mov    edi,DWORD PTR [rbp-0x68]
    fb12:	0f 85 f9 02 00 00    	jne    fe11 <zbtScoreDeleteInPlace+0x771>
    fb18:	83 f9 10             	cmp    ecx,0x10
    fb1b:	73 07                	jae    fb24 <zbtScoreDeleteInPlace+0x484>
    fb1d:	31 c0                	xor    eax,eax
    fb1f:	e9 24 03 00 00       	jmp    fe48 <zbtScoreDeleteInPlace+0x7a8>
    fb24:	44 89 e8             	mov    eax,r13d
    fb27:	83 e0 f0             	and    eax,0xfffffff0
    fb2a:	66 0f 6e c7          	movd   xmm0,edi
    fb2e:	f2 0f 70 c0 00       	pshuflw xmm0,xmm0,0x0
    fb33:	66 0f 70 c0 00       	pshufd xmm0,xmm0,0x0
    fb38:	31 c9                	xor    ecx,ecx
    fb3a:	66 0f 6f 0d 0e 35 00 	movdqa xmm1,XMMWORD PTR [rip+0x350e]        # 13050 <_IO_stdin_used+0x50>
    fb41:	00
    fb42:	66 0f ef c1          	pxor   xmm0,xmm1
    fb46:	eb 15                	jmp    fb5d <zbtScoreDeleteInPlace+0x4bd>
    fb48:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    fb4f:	00
    fb50:	48 83 c1 10          	add    rcx,0x10
    fb54:	48 39 c8             	cmp    rax,rcx
    fb57:	0f 84 af 02 00 00    	je     fe0c <zbtScoreDeleteInPlace+0x76c>
    fb5d:	f3 41 0f 6f 14 4e    	movdqu xmm2,XMMWORD PTR [r14+rcx*2]
    fb63:	66 0f 6f e2          	movdqa xmm4,xmm2
    fb67:	66 0f ef e1          	pxor   xmm4,xmm1
    fb6b:	66 0f 6f d8          	movdqa xmm3,xmm0
    fb6f:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
    fb73:	66 0f 7e da          	movd   edx,xmm3
    fb77:	f6 c2 01             	test   dl,0x1
    fb7a:	0f 85 00 01 00 00    	jne    fc80 <zbtScoreDeleteInPlace+0x5e0>
    fb80:	c1 ea 10             	shr    edx,0x10
    fb83:	f6 c2 01             	test   dl,0x1
    fb86:	0f 85 0b 01 00 00    	jne    fc97 <zbtScoreDeleteInPlace+0x5f7>
    fb8c:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    fb91:	f6 c2 01             	test   dl,0x1
    fb94:	0f 85 18 01 00 00    	jne    fcb2 <zbtScoreDeleteInPlace+0x612>
    fb9a:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    fb9f:	f6 c2 01             	test   dl,0x1
    fba2:	0f 85 25 01 00 00    	jne    fccd <zbtScoreDeleteInPlace+0x62d>
    fba8:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    fbad:	f6 c2 01             	test   dl,0x1
    fbb0:	0f 85 32 01 00 00    	jne    fce8 <zbtScoreDeleteInPlace+0x648>
    fbb6:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    fbbb:	f6 c2 01             	test   dl,0x1
    fbbe:	0f 85 3f 01 00 00    	jne    fd03 <zbtScoreDeleteInPlace+0x663>
    fbc4:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    fbc9:	f6 c2 01             	test   dl,0x1
    fbcc:	0f 85 4c 01 00 00    	jne    fd1e <zbtScoreDeleteInPlace+0x67e>
    fbd2:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    fbd7:	f6 c2 01             	test   dl,0x1
    fbda:	74 0d                	je     fbe9 <zbtScoreDeleteInPlace+0x549>
    fbdc:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
    fbe1:	01 da                	add    edx,ebx
    fbe3:	66 41 89 54 4e 0e    	mov    WORD PTR [r14+rcx*2+0xe],dx
    fbe9:	f3 41 0f 6f 54 4e 10 	movdqu xmm2,XMMWORD PTR [r14+rcx*2+0x10]
    fbf0:	66 0f 6f e2          	movdqa xmm4,xmm2
    fbf4:	66 0f ef e1          	pxor   xmm4,xmm1
    fbf8:	66 0f 6f d8          	movdqa xmm3,xmm0
    fbfc:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
    fc00:	66 0f 7e da          	movd   edx,xmm3
    fc04:	f6 c2 01             	test   dl,0x1
    fc07:	0f 85 33 01 00 00    	jne    fd40 <zbtScoreDeleteInPlace+0x6a0>
    fc0d:	c1 ea 10             	shr    edx,0x10
    fc10:	f6 c2 01             	test   dl,0x1
    fc13:	0f 85 3f 01 00 00    	jne    fd58 <zbtScoreDeleteInPlace+0x6b8>
    fc19:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    fc1e:	f6 c2 01             	test   dl,0x1
    fc21:	0f 85 4c 01 00 00    	jne    fd73 <zbtScoreDeleteInPlace+0x6d3>
    fc27:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    fc2c:	f6 c2 01             	test   dl,0x1
    fc2f:	0f 85 59 01 00 00    	jne    fd8e <zbtScoreDeleteInPlace+0x6ee>
    fc35:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    fc3a:	f6 c2 01             	test   dl,0x1
    fc3d:	0f 85 66 01 00 00    	jne    fda9 <zbtScoreDeleteInPlace+0x709>
    fc43:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    fc48:	f6 c2 01             	test   dl,0x1
    fc4b:	0f 85 73 01 00 00    	jne    fdc4 <zbtScoreDeleteInPlace+0x724>
    fc51:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    fc56:	f6 c2 01             	test   dl,0x1
    fc59:	0f 85 80 01 00 00    	jne    fddf <zbtScoreDeleteInPlace+0x73f>
    fc5f:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    fc64:	f6 c2 01             	test   dl,0x1
    fc67:	0f 84 e3 fe ff ff    	je     fb50 <zbtScoreDeleteInPlace+0x4b0>
    fc6d:	e9 88 01 00 00       	jmp    fdfa <zbtScoreDeleteInPlace+0x75a>
    fc72:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    fc79:	1f 84 00 00 00 00 00
    fc80:	66 0f 7e d6          	movd   esi,xmm2
    fc84:	01 de                	add    esi,ebx
    fc86:	66 41 89 34 4e       	mov    WORD PTR [r14+rcx*2],si
    fc8b:	c1 ea 10             	shr    edx,0x10
    fc8e:	f6 c2 01             	test   dl,0x1
    fc91:	0f 84 f5 fe ff ff    	je     fb8c <zbtScoreDeleteInPlace+0x4ec>
    fc97:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
    fc9c:	01 da                	add    edx,ebx
    fc9e:	66 41 89 54 4e 02    	mov    WORD PTR [r14+rcx*2+0x2],dx
    fca4:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    fca9:	f6 c2 01             	test   dl,0x1
    fcac:	0f 84 e8 fe ff ff    	je     fb9a <zbtScoreDeleteInPlace+0x4fa>
    fcb2:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
    fcb7:	01 da                	add    edx,ebx
    fcb9:	66 41 89 54 4e 04    	mov    WORD PTR [r14+rcx*2+0x4],dx
    fcbf:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    fcc4:	f6 c2 01             	test   dl,0x1
    fcc7:	0f 84 db fe ff ff    	je     fba8 <zbtScoreDeleteInPlace+0x508>
    fccd:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
    fcd2:	01 da                	add    edx,ebx
    fcd4:	66 41 89 54 4e 06    	mov    WORD PTR [r14+rcx*2+0x6],dx
    fcda:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    fcdf:	f6 c2 01             	test   dl,0x1
    fce2:	0f 84 ce fe ff ff    	je     fbb6 <zbtScoreDeleteInPlace+0x516>
    fce8:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
    fced:	01 da                	add    edx,ebx
    fcef:	66 41 89 54 4e 08    	mov    WORD PTR [r14+rcx*2+0x8],dx
    fcf5:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    fcfa:	f6 c2 01             	test   dl,0x1
    fcfd:	0f 84 c1 fe ff ff    	je     fbc4 <zbtScoreDeleteInPlace+0x524>
    fd03:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
    fd08:	01 da                	add    edx,ebx
    fd0a:	66 41 89 54 4e 0a    	mov    WORD PTR [r14+rcx*2+0xa],dx
    fd10:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    fd15:	f6 c2 01             	test   dl,0x1
    fd18:	0f 84 b4 fe ff ff    	je     fbd2 <zbtScoreDeleteInPlace+0x532>
    fd1e:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
    fd23:	01 da                	add    edx,ebx
    fd25:	66 41 89 54 4e 0c    	mov    WORD PTR [r14+rcx*2+0xc],dx
    fd2b:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    fd30:	f6 c2 01             	test   dl,0x1
    fd33:	0f 85 a3 fe ff ff    	jne    fbdc <zbtScoreDeleteInPlace+0x53c>
    fd39:	e9 ab fe ff ff       	jmp    fbe9 <zbtScoreDeleteInPlace+0x549>
    fd3e:	66 90                	xchg   ax,ax
    fd40:	66 0f 7e d6          	movd   esi,xmm2
    fd44:	01 de                	add    esi,ebx
    fd46:	66 41 89 74 4e 10    	mov    WORD PTR [r14+rcx*2+0x10],si
    fd4c:	c1 ea 10             	shr    edx,0x10
    fd4f:	f6 c2 01             	test   dl,0x1
    fd52:	0f 84 c1 fe ff ff    	je     fc19 <zbtScoreDeleteInPlace+0x579>
    fd58:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
    fd5d:	01 da                	add    edx,ebx
    fd5f:	66 41 89 54 4e 12    	mov    WORD PTR [r14+rcx*2+0x12],dx
    fd65:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    fd6a:	f6 c2 01             	test   dl,0x1
    fd6d:	0f 84 b4 fe ff ff    	je     fc27 <zbtScoreDeleteInPlace+0x587>
    fd73:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
    fd78:	01 da                	add    edx,ebx
    fd7a:	66 41 89 54 4e 14    	mov    WORD PTR [r14+rcx*2+0x14],dx
    fd80:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    fd85:	f6 c2 01             	test   dl,0x1
    fd88:	0f 84 a7 fe ff ff    	je     fc35 <zbtScoreDeleteInPlace+0x595>
    fd8e:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
    fd93:	01 da                	add    edx,ebx
    fd95:	66 41 89 54 4e 16    	mov    WORD PTR [r14+rcx*2+0x16],dx
    fd9b:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    fda0:	f6 c2 01             	test   dl,0x1
    fda3:	0f 84 9a fe ff ff    	je     fc43 <zbtScoreDeleteInPlace+0x5a3>
    fda9:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
    fdae:	01 da                	add    edx,ebx
    fdb0:	66 41 89 54 4e 18    	mov    WORD PTR [r14+rcx*2+0x18],dx
    fdb6:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    fdbb:	f6 c2 01             	test   dl,0x1
    fdbe:	0f 84 8d fe ff ff    	je     fc51 <zbtScoreDeleteInPlace+0x5b1>
    fdc4:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
    fdc9:	01 da                	add    edx,ebx
    fdcb:	66 41 89 54 4e 1a    	mov    WORD PTR [r14+rcx*2+0x1a],dx
    fdd1:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    fdd6:	f6 c2 01             	test   dl,0x1
    fdd9:	0f 84 80 fe ff ff    	je     fc5f <zbtScoreDeleteInPlace+0x5bf>
    fddf:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
    fde4:	01 da                	add    edx,ebx
    fde6:	66 41 89 54 4e 1c    	mov    WORD PTR [r14+rcx*2+0x1c],dx
    fdec:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    fdf1:	f6 c2 01             	test   dl,0x1
    fdf4:	0f 84 56 fd ff ff    	je     fb50 <zbtScoreDeleteInPlace+0x4b0>
    fdfa:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
    fdff:	01 da                	add    edx,ebx
    fe01:	66 41 89 54 4e 1e    	mov    WORD PTR [r14+rcx*2+0x1e],dx
    fe07:	e9 44 fd ff ff       	jmp    fb50 <zbtScoreDeleteInPlace+0x4b0>
    fe0c:	4c 39 e8             	cmp    rax,r13
    fe0f:	75 37                	jne    fe48 <zbtScoreDeleteInPlace+0x7a8>
    fe11:	48 8b 7d c8          	mov    rdi,QWORD PTR [rbp-0x38]
    fe15:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
    fe1c:	e8 4f f1 ff ff       	call   ef70 <zbtScoreUpdatePath>
    fe21:	48 81 c4 b8 00 00 00 	add    rsp,0xb8
    fe28:	5b                   	pop    rbx
    fe29:	41 5c                	pop    r12
    fe2b:	41 5d                	pop    r13
    fe2d:	41 5e                	pop    r14
    fe2f:	41 5f                	pop    r15
    fe31:	5d                   	pop    rbp
    fe32:	c3                   	ret
    fe33:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    fe3a:	84 00 00 00 00 00
    fe40:	48 ff c0             	inc    rax
    fe43:	49 39 c5             	cmp    r13,rax
    fe46:	74 c9                	je     fe11 <zbtScoreDeleteInPlace+0x771>
    fe48:	41 0f b7 0c 46       	movzx  ecx,WORD PTR [r14+rax*2]
    fe4d:	66 39 f9             	cmp    cx,di
    fe50:	73 ee                	jae    fe40 <zbtScoreDeleteInPlace+0x7a0>
    fe52:	01 d9                	add    ecx,ebx
    fe54:	66 41 89 0c 46       	mov    WORD PTR [r14+rax*2],cx
    fe59:	eb e5                	jmp    fe40 <zbtScoreDeleteInPlace+0x7a0>

Disassembly of section .fini:
