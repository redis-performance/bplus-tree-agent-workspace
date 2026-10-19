
scratch/amd-chunk-build/base/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000c6b0 <zbtScoreInsertAt>:
    c6b0:	55                   	push   rbp
    c6b1:	48 89 e5             	mov    rbp,rsp
    c6b4:	41 57                	push   r15
    c6b6:	41 56                	push   r14
    c6b8:	41 55                	push   r13
    c6ba:	41 54                	push   r12
    c6bc:	53                   	push   rbx
    c6bd:	48 81 ec 18 14 00 00 	sub    rsp,0x1418
    c6c4:	4d 89 cb             	mov    r11,r9
    c6c7:	41 89 ca             	mov    r10d,ecx
    c6ca:	49 89 f1             	mov    r9,rsi
    c6cd:	48 89 bd 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdi
    c6d4:	41 0f b6 43 13       	movzx  eax,BYTE PTR [r11+0x13]
    c6d9:	88 45 c8             	mov    BYTE PTR [rbp-0x38],al
    c6dc:	0f b6 5e 11          	movzx  ebx,BYTE PTR [rsi+0x11]
    c6e0:	41 09 c8             	or     r8d,ecx
    c6e3:	74 2f                	je     c714 <zbtScoreInsertAt+0x64>
    c6e5:	80 fb 60             	cmp    bl,0x60
    c6e8:	75 2a                	jne    c714 <zbtScoreInsertAt+0x64>
    c6ea:	0f b6 4d c8          	movzx  ecx,BYTE PTR [rbp-0x38]
    c6ee:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    c6f5:	4c 89 ce             	mov    rsi,r9
    c6f8:	4c 89 da             	mov    rdx,r11
    c6fb:	45 89 d0             	mov    r8d,r10d
    c6fe:	48 81 c4 18 14 00 00 	add    rsp,0x1418
    c705:	5b                   	pop    rbx
    c706:	41 5c                	pop    r12
    c708:	41 5d                	pop    r13
    c70a:	41 5e                	pop    r14
    c70c:	41 5f                	pop    r15
    c70e:	5d                   	pop    rbp
    c70f:	e9 6c 19 00 00       	jmp    e080 <zbtScoreInsertEdgeLeaf>
    c714:	44 0f b6 e3          	movzx  r12d,bl
    c718:	80 fb 5f             	cmp    bl,0x5f
    c71b:	4c 89 c8             	mov    rax,r9
    c71e:	4c 89 4d d0          	mov    QWORD PTR [rbp-0x30],r9
    c722:	4c 89 65 b0          	mov    QWORD PTR [rbp-0x50],r12
    c726:	4c 89 5d 98          	mov    QWORD PTR [rbp-0x68],r11
    c72a:	77 61                	ja     c78d <zbtScoreInsertAt+0xdd>
    c72c:	66 49 0f 7e c7       	movq   r15,xmm0
    c731:	4d 85 ff             	test   r15,r15
    c734:	78 27                	js     c75d <zbtScoreInsertAt+0xad>
    c736:	48 b8 00 00 00 00 00 	movabs rax,0x8000000000000000
    c73d:	00 00 80
    c740:	49 09 c7             	or     r15,rax
    c743:	41 0f b6 41 35       	movzx  eax,BYTE PTR [r9+0x35]
    c748:	49 8b 49 28          	mov    rcx,QWORD PTR [r9+0x28]
    c74c:	84 c0                	test   al,al
    c74e:	74 1d                	je     c76d <zbtScoreInsertAt+0xbd>
    c750:	49 39 cf             	cmp    r15,rcx
    c753:	77 38                	ja     c78d <zbtScoreInsertAt+0xdd>
    c755:	4c 29 f9             	sub    rcx,r15
    c758:	49 89 cf             	mov    r15,rcx
    c75b:	eb 15                	jmp    c772 <zbtScoreInsertAt+0xc2>
    c75d:	49 f7 d7             	not    r15
    c760:	41 0f b6 41 35       	movzx  eax,BYTE PTR [r9+0x35]
    c765:	49 8b 49 28          	mov    rcx,QWORD PTR [r9+0x28]
    c769:	84 c0                	test   al,al
    c76b:	75 e3                	jne    c750 <zbtScoreInsertAt+0xa0>
    c76d:	49 29 cf             	sub    r15,rcx
    c770:	72 1b                	jb     c78d <zbtScoreInsertAt+0xdd>
    c772:	41 0f b6 49 13       	movzx  ecx,BYTE PTR [r9+0x13]
    c777:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
    c77e:	48 d3 e6             	shl    rsi,cl
    c781:	48 f7 d6             	not    rsi
    c784:	49 85 f7             	test   r15,rsi
    c787:	0f 84 6c 06 00 00    	je     cdf9 <zbtScoreInsertAt+0x749>
    c78d:	44 89 85 70 ff ff ff 	mov    DWORD PTR [rbp-0x90],r8d
    c794:	44 89 95 60 ff ff ff 	mov    DWORD PTR [rbp-0xa0],r10d
    c79b:	4d 8d 71 38          	lea    r14,[r9+0x38]
    c79f:	89 95 68 ff ff ff    	mov    DWORD PTR [rbp-0x98],edx
    c7a5:	41 89 d2             	mov    r10d,edx
    c7a8:	49 8d 44 24 01       	lea    rax,[r12+0x1]
    c7ad:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    c7b1:	4b 8d 04 92          	lea    rax,[r10+r10*4]
    c7b5:	48 89 85 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],rax
    c7bc:	48 8d 04 c5 d0 eb ff 	lea    rax,[rax*8-0x1430]
    c7c3:	ff
    c7c4:	48 01 e8             	add    rax,rbp
    c7c7:	48 89 45 88          	mov    QWORD PTR [rbp-0x78],rax
    c7cb:	45 31 e4             	xor    r12d,r12d
    c7ce:	89 d9                	mov    ecx,ebx
    c7d0:	48 8d 9d d0 eb ff ff 	lea    rbx,[rbp-0x1430]
    c7d7:	88 4d a4             	mov    BYTE PTR [rbp-0x5c],cl
    c7da:	45 31 ff             	xor    r15d,r15d
    c7dd:	4c 89 75 a8          	mov    QWORD PTR [rbp-0x58],r14
    c7e1:	4c 89 55 90          	mov    QWORD PTR [rbp-0x70],r10
    c7e5:	66 0f d6 45 80       	movq   QWORD PTR [rbp-0x80],xmm0
    c7ea:	eb 52                	jmp    c83e <zbtScoreInsertAt+0x18e>
    c7ec:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    c7f0:	66 42 0f d6 84 d5 00 	movq   QWORD PTR [rbp+r10*8-0x500],xmm0
    c7f7:	fb ff ff
    c7fa:	49 8b 43 20          	mov    rax,QWORD PTR [r11+0x20]
    c7fe:	48 8b 55 88          	mov    rdx,QWORD PTR [rbp-0x78]
    c802:	48 89 42 20          	mov    QWORD PTR [rdx+0x20],rax
    c806:	41 0f 10 13          	movups xmm2,XMMWORD PTR [r11]
    c80a:	41 0f 10 4b 10       	movups xmm1,XMMWORD PTR [r11+0x10]
    c80f:	0f 11 4a 10          	movups XMMWORD PTR [rdx+0x10],xmm1
    c813:	0f 11 12             	movups XMMWORD PTR [rdx],xmm2
    c816:	0f b6 45 c8          	movzx  eax,BYTE PTR [rbp-0x38]
    c81a:	42 88 84 15 e0 fe ff 	mov    BYTE PTR [rbp+r10*1-0x120],al
    c821:	ff
    c822:	66 42 c7 84 55 10 fe 	mov    WORD PTR [rbp+r10*2-0x1f0],0x0
    c829:	ff ff 00 00
    c82d:	49 ff c4             	inc    r12
    c830:	48 83 c3 28          	add    rbx,0x28
    c834:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    c838:	0f 84 70 02 00 00    	je     caae <zbtScoreInsertAt+0x3fe>
    c83e:	4d 39 e2             	cmp    r10,r12
    c841:	74 ad                	je     c7f0 <zbtScoreInsertAt+0x140>
    c843:	41 0f b6 41 34       	movzx  eax,BYTE PTR [r9+0x34]
    c848:	41 0f b6 71 35       	movzx  esi,BYTE PTR [r9+0x35]
    c84d:	0f b6 d1             	movzx  edx,cl
    c850:	45 89 fd             	mov    r13d,r15d
    c853:	41 f7 d5             	not    r13d
    c856:	85 c0                	test   eax,eax
    c858:	0f 84 7f 00 00 00    	je     c8dd <zbtScoreInsertAt+0x22d>
    c85e:	46 8d 04 2a          	lea    r8d,[rdx+r13*1]
    c862:	40 84 f6             	test   sil,sil
    c865:	45 0f 44 c7          	cmove  r8d,r15d
    c869:	4c 0f af c0          	imul   r8,rax
    c86d:	4d 89 c1             	mov    r9,r8
    c870:	49 c1 e9 03          	shr    r9,0x3
    c874:	4b 8b 3c 0e          	mov    rdi,QWORD PTR [r14+r9*1]
    c878:	44 89 c1             	mov    ecx,r8d
    c87b:	80 e1 07             	and    cl,0x7
    c87e:	48 d3 ef             	shr    rdi,cl
    c881:	41 83 e0 07          	and    r8d,0x7
    c885:	74 29                	je     c8b0 <zbtScoreInsertAt+0x200>
    c887:	b9 40 00 00 00       	mov    ecx,0x40
    c88c:	44 29 c1             	sub    ecx,r8d
    c88f:	39 c1                	cmp    ecx,eax
    c891:	73 1d                	jae    c8b0 <zbtScoreInsertAt+0x200>
    c893:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c897:	47 0f b6 44 11 40    	movzx  r8d,BYTE PTR [r9+r10*1+0x40]
    c89d:	4d 89 d1             	mov    r9,r10
    c8a0:	49 d3 e0             	shl    r8,cl
    c8a3:	4c 09 c7             	or     rdi,r8
    c8a6:	eb 0c                	jmp    c8b4 <zbtScoreInsertAt+0x204>
    c8a8:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    c8af:	00
    c8b0:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    c8b4:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    c8bb:	89 c1                	mov    ecx,eax
    c8bd:	49 d3 e0             	shl    r8,cl
    c8c0:	3c 40                	cmp    al,0x40
    c8c2:	49 f7 d0             	not    r8
    c8c5:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
    c8cc:	4c 0f 43 c1          	cmovae r8,rcx
    c8d0:	49 21 f8             	and    r8,rdi
    c8d3:	41 0f b6 49 13       	movzx  ecx,BYTE PTR [r9+0x13]
    c8d8:	49 d3 e0             	shl    r8,cl
    c8db:	eb 03                	jmp    c8e0 <zbtScoreInsertAt+0x230>
    c8dd:	45 31 c0             	xor    r8d,r8d
    c8e0:	4c 89 c1             	mov    rcx,r8
    c8e3:	48 f7 d9             	neg    rcx
    c8e6:	40 84 f6             	test   sil,sil
    c8e9:	49 0f 44 c8          	cmove  rcx,r8
    c8ed:	49 03 49 28          	add    rcx,QWORD PTR [r9+0x28]
    c8f1:	48 89 cf             	mov    rdi,rcx
    c8f4:	49 b8 ff ff ff ff ff 	movabs r8,0x7fffffffffffffff
    c8fb:	ff ff 7f
    c8fe:	4c 21 c7             	and    rdi,r8
    c901:	48 85 c9             	test   rcx,rcx
    c904:	48 f7 d1             	not    rcx
    c907:	48 0f 48 cf          	cmovs  rcx,rdi
    c90b:	4a 89 8c e5 00 fb ff 	mov    QWORD PTR [rbp+r12*8-0x500],rcx
    c912:	ff
    c913:	48 85 c0             	test   rax,rax
    c916:	74 11                	je     c929 <zbtScoreInsertAt+0x279>
    c918:	0f af c2             	imul   eax,edx
    c91b:	83 c0 07             	add    eax,0x7
    c91e:	c1 e8 03             	shr    eax,0x3
    c921:	83 c0 09             	add    eax,0x9
    c924:	83 e0 fe             	and    eax,0xfffffffe
    c927:	eb 02                	jmp    c92b <zbtScoreInsertAt+0x27b>
    c929:	31 c0                	xor    eax,eax
    c92b:	44 01 ea             	add    edx,r13d
    c92e:	40 84 f6             	test   sil,sil
    c931:	44 89 7d c0          	mov    DWORD PTR [rbp-0x40],r15d
    c935:	41 0f 44 d7          	cmove  edx,r15d
    c939:	4c 01 f0             	add    rax,r14
    c93c:	0f b7 04 50          	movzx  eax,WORD PTR [rax+rdx*2]
    c940:	4d 8d 3c 01          	lea    r15,[r9+rax*1]
    c944:	41 0f b6 04 01       	movzx  eax,BYTE PTR [r9+rax*1]
    c949:	48 3d fd 00 00 00    	cmp    rax,0xfd
    c94f:	77 0f                	ja     c960 <zbtScoreInsertAt+0x2b0>
    c951:	b9 01 00 00 00       	mov    ecx,0x1
    c956:	eb 19                	jmp    c971 <zbtScoreInsertAt+0x2c1>
    c958:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    c95f:	00
    c960:	3d fe 00 00 00       	cmp    eax,0xfe
    c965:	75 1e                	jne    c985 <zbtScoreInsertAt+0x2d5>
    c967:	41 0f b7 47 01       	movzx  eax,WORD PTR [r15+0x1]
    c96c:	b9 03 00 00 00       	mov    ecx,0x3
    c971:	48 89 43 08          	mov    QWORD PTR [rbx+0x8],rax
    c975:	49 01 cf             	add    r15,rcx
    c978:	4c 89 3b             	mov    QWORD PTR [rbx],r15
    c97b:	31 c0                	xor    eax,eax
    c97d:	45 31 f6             	xor    r14d,r14d
    c980:	45 31 ff             	xor    r15d,r15d
    c983:	eb 1c                	jmp    c9a1 <zbtScoreInsertAt+0x2f1>
    c985:	4d 8b 77 0d          	mov    r14,QWORD PTR [r15+0xd]
    c989:	4d 85 f6             	test   r14,r14
    c98c:	0f 84 ac 00 00 00    	je     ca3e <zbtScoreInsertAt+0x38e>
    c992:	49 8b 47 05          	mov    rax,QWORD PTR [r15+0x5]
    c996:	48 89 43 08          	mov    QWORD PTR [rbx+0x8],rax
    c99a:	4c 89 33             	mov    QWORD PTR [rbx],r14
    c99d:	41 8b 47 01          	mov    eax,DWORD PTR [r15+0x1]
    c9a1:	89 43 10             	mov    DWORD PTR [rbx+0x10],eax
    c9a4:	4c 89 73 18          	mov    QWORD PTR [rbx+0x18],r14
    c9a8:	4c 89 7b 20          	mov    QWORD PTR [rbx+0x20],r15
    c9ac:	41 0f b6 41 34       	movzx  eax,BYTE PTR [r9+0x34]
    c9b1:	41 0f b6 49 11       	movzx  ecx,BYTE PTR [r9+0x11]
    c9b6:	0f b6 d1             	movzx  edx,cl
    c9b9:	48 85 c0             	test   rax,rax
    c9bc:	74 13                	je     c9d1 <zbtScoreInsertAt+0x321>
    c9be:	89 d7                	mov    edi,edx
    c9c0:	0f af f8             	imul   edi,eax
    c9c3:	83 c7 07             	add    edi,0x7
    c9c6:	c1 ef 03             	shr    edi,0x3
    c9c9:	83 c7 09             	add    edi,0x9
    c9cc:	83 e7 fe             	and    edi,0xfffffffe
    c9cf:	eb 02                	jmp    c9d3 <zbtScoreInsertAt+0x323>
    c9d1:	31 ff                	xor    edi,edi
    c9d3:	4c 8b 75 a8          	mov    r14,QWORD PTR [rbp-0x58]
    c9d7:	4c 8b 55 90          	mov    r10,QWORD PTR [rbp-0x70]
    c9db:	44 8b 7d c0          	mov    r15d,DWORD PTR [rbp-0x40]
    c9df:	4c 01 f7             	add    rdi,r14
    c9e2:	89 d6                	mov    esi,edx
    c9e4:	44 01 ee             	add    esi,r13d
    c9e7:	41 80 79 35 00       	cmp    BYTE PTR [r9+0x35],0x0
    c9ec:	41 0f 44 f7          	cmove  esi,r15d
    c9f0:	48 8d 3c 57          	lea    rdi,[rdi+rdx*2]
    c9f4:	0f b6 3c 3e          	movzx  edi,BYTE PTR [rsi+rdi*1]
    c9f8:	42 88 bc 25 e0 fe ff 	mov    BYTE PTR [rbp+r12*1-0x120],dil
    c9ff:	ff
    ca00:	48 85 c0             	test   rax,rax
    ca03:	74 11                	je     ca16 <zbtScoreInsertAt+0x366>
    ca05:	0f af c2             	imul   eax,edx
    ca08:	83 c0 07             	add    eax,0x7
    ca0b:	c1 e8 03             	shr    eax,0x3
    ca0e:	83 c0 09             	add    eax,0x9
    ca11:	83 e0 fe             	and    eax,0xfffffffe
    ca14:	eb 02                	jmp    ca18 <zbtScoreInsertAt+0x368>
    ca16:	31 c0                	xor    eax,eax
    ca18:	4c 01 f0             	add    rax,r14
    ca1b:	0f b7 04 70          	movzx  eax,WORD PTR [rax+rsi*2]
    ca1f:	66 42 89 84 65 10 fe 	mov    WORD PTR [rbp+r12*2-0x1f0],ax
    ca26:	ff ff
    ca28:	41 ff c7             	inc    r15d
    ca2b:	49 ff c4             	inc    r12
    ca2e:	48 83 c3 28          	add    rbx,0x28
    ca32:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    ca36:	0f 85 02 fe ff ff    	jne    c83e <zbtScoreInsertAt+0x18e>
    ca3c:	eb 70                	jmp    caae <zbtScoreInsertAt+0x3fe>
    ca3e:	48 8d 3d d9 6b 00 00 	lea    rdi,[rip+0x6bd9]        # 1361e <_IO_stdin_used+0x61e>
    ca45:	be 57 02 00 00       	mov    esi,0x257
    ca4a:	48 8d 15 f9 6c 00 00 	lea    rdx,[rip+0x6cf9]        # 1374a <_IO_stdin_used+0x74a>
    ca51:	e8 4a 4c 00 00       	call   116a0 <standalone_panic>
    ca56:	f3 0f 7e 45 80       	movq   xmm0,QWORD PTR [rbp-0x80]
    ca5b:	4c 8b 5d 98          	mov    r11,QWORD PTR [rbp-0x68]
    ca5f:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    ca63:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    ca67:	0f 84 25 ff ff ff    	je     c992 <zbtScoreInsertAt+0x2e2>
    ca6d:	48 8d 3d aa 6b 00 00 	lea    rdi,[rip+0x6baa]        # 1361e <_IO_stdin_used+0x61e>
    ca74:	be 37 02 00 00       	mov    esi,0x237
    ca79:	48 8d 15 d6 6c 00 00 	lea    rdx,[rip+0x6cd6]        # 13756 <_IO_stdin_used+0x756>
    ca80:	e8 1b 4c 00 00       	call   116a0 <standalone_panic>
    ca85:	f3 0f 7e 45 80       	movq   xmm0,QWORD PTR [rbp-0x80]
    ca8a:	4c 8b 5d 98          	mov    r11,QWORD PTR [rbp-0x68]
    ca8e:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    ca92:	41 0f b6 07          	movzx  eax,BYTE PTR [r15]
    ca96:	49 8b 4f 05          	mov    rcx,QWORD PTR [r15+0x5]
    ca9a:	48 89 4b 08          	mov    QWORD PTR [rbx+0x8],rcx
    ca9e:	4c 89 33             	mov    QWORD PTR [rbx],r14
    caa1:	3c ff                	cmp    al,0xff
    caa3:	0f 85 d2 fe ff ff    	jne    c97b <zbtScoreInsertAt+0x2cb>
    caa9:	e9 ef fe ff ff       	jmp    c99d <zbtScoreInsertAt+0x2ed>
    caae:	f3 0f 7e 8d 00 fb ff 	movq   xmm1,QWORD PTR [rbp-0x500]
    cab5:	ff
    cab6:	66 49 0f 7e cd       	movq   r13,xmm1
    cabb:	4d 85 ed             	test   r13,r13
    cabe:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    cac5:	00 00 80
    cac8:	4c 89 e8             	mov    rax,r13
    cacb:	78 05                	js     cad2 <zbtScoreInsertAt+0x422>
    cacd:	4c 09 f8             	or     rax,r15
    cad0:	eb 03                	jmp    cad5 <zbtScoreInsertAt+0x425>
    cad2:	48 f7 d0             	not    rax
    cad5:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    cad9:	0f b6 5d a4          	movzx  ebx,BYTE PTR [rbp-0x5c]
    cadd:	44 8b b5 70 ff ff ff 	mov    r14d,DWORD PTR [rbp-0x90]
    cae4:	ba 38 00 00 00       	mov    edx,0x38
    cae9:	84 db                	test   bl,bl
    caeb:	0f 84 97 00 00 00    	je     cb88 <zbtScoreInsertAt+0x4d8>
    caf1:	45 31 c0             	xor    r8d,r8d
    caf4:	48 89 c7             	mov    rdi,rax
    caf7:	31 c9                	xor    ecx,ecx
    caf9:	48 89 c6             	mov    rsi,rax
    cafc:	eb 24                	jmp    cb22 <zbtScoreInsertAt+0x472>
    cafe:	66 90                	xchg   ax,ax
    cb00:	49 f7 d1             	not    r9
    cb03:	4d 89 ca             	mov    r10,r9
    cb06:	49 31 c2             	xor    r10,rax
    cb09:	4c 09 d1             	or     rcx,r10
    cb0c:	49 39 f9             	cmp    r9,rdi
    cb0f:	49 0f 42 f9          	cmovb  rdi,r9
    cb13:	49 39 f1             	cmp    r9,rsi
    cb16:	49 0f 47 f1          	cmova  rsi,r9
    cb1a:	49 ff c0             	inc    r8
    cb1d:	4d 39 c4             	cmp    r12,r8
    cb20:	74 19                	je     cb3b <zbtScoreInsertAt+0x48b>
    cb22:	f3 42 0f 7e 8c c5 08 	movq   xmm1,QWORD PTR [rbp+r8*8-0x4f8]
    cb29:	fb ff ff
    cb2c:	66 49 0f 7e c9       	movq   r9,xmm1
    cb31:	4d 85 c9             	test   r9,r9
    cb34:	78 ca                	js     cb00 <zbtScoreInsertAt+0x450>
    cb36:	4d 09 f9             	or     r9,r15
    cb39:	eb c8                	jmp    cb03 <zbtScoreInsertAt+0x453>
    cb3b:	48 85 c9             	test   rcx,rcx
    cb3e:	74 44                	je     cb84 <zbtScoreInsertAt+0x4d4>
    cb40:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    cb45:	48 29 fe             	sub    rsi,rdi
    cb48:	48 d3 ee             	shr    rsi,cl
    cb4b:	48 85 f6             	test   rsi,rsi
    cb4e:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    cb52:	74 34                	je     cb88 <zbtScoreInsertAt+0x4d8>
    cb54:	48 0f bd c6          	bsr    rax,rsi
    cb58:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    cb5c:	48 83 c0 41          	add    rax,0x41
    cb60:	48 0f af 45 b8       	imul   rax,QWORD PTR [rbp-0x48]
    cb65:	48 83 c0 07          	add    rax,0x7
    cb69:	48 c1 e8 03          	shr    rax,0x3
    cb6d:	48 83 c0 09          	add    rax,0x9
    cb71:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    cb78:	ff ff 1f
    cb7b:	48 21 c2             	and    rdx,rax
    cb7e:	48 83 c2 38          	add    rdx,0x38
    cb82:	eb 04                	jmp    cb88 <zbtScoreInsertAt+0x4d8>
    cb84:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    cb88:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    cb8c:	48 8d 04 40          	lea    rax,[rax+rax*2]
    cb90:	48 01 c2             	add    rdx,rax
    cb93:	4b 8d 0c a4          	lea    rcx,[r12+r12*4]
    cb97:	48 8d 0c cd 28 00 00 	lea    rcx,[rcx*8+0x28]
    cb9e:	00
    cb9f:	31 f6                	xor    esi,esi
    cba1:	eb 19                	jmp    cbbc <zbtScoreInsertAt+0x50c>
    cba3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    cbaa:	84 00 00 00 00 00
    cbb0:	48 01 fa             	add    rdx,rdi
    cbb3:	48 83 c6 28          	add    rsi,0x28
    cbb7:	48 39 f1             	cmp    rcx,rsi
    cbba:	74 37                	je     cbf3 <zbtScoreInsertAt+0x543>
    cbbc:	bf 15 00 00 00       	mov    edi,0x15
    cbc1:	48 83 bc 35 e8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1418],0x0
    cbc8:	ff 00
    cbca:	75 e4                	jne    cbb0 <zbtScoreInsertAt+0x500>
    cbcc:	4c 8b 84 35 d8 eb ff 	mov    r8,QWORD PTR [rbp+rsi*1-0x1428]
    cbd3:	ff
    cbd4:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    cbdb:	77 d3                	ja     cbb0 <zbtScoreInsertAt+0x500>
    cbdd:	31 ff                	xor    edi,edi
    cbdf:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    cbe6:	40 0f 93 c7          	setae  dil
    cbea:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    cbee:	48 ff c7             	inc    rdi
    cbf1:	eb bd                	jmp    cbb0 <zbtScoreInsertAt+0x500>
    cbf3:	45 85 f6             	test   r14d,r14d
    cbf6:	74 2b                	je     cc23 <zbtScoreInsertAt+0x573>
    cbf8:	48 81 fa 00 10 00 00 	cmp    rdx,0x1000
    cbff:	72 22                	jb     cc23 <zbtScoreInsertAt+0x573>
    cc01:	0f b6 4d c8          	movzx  ecx,BYTE PTR [rbp-0x38]
    cc05:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    cc0c:	4c 89 ce             	mov    rsi,r9
    cc0f:	4c 89 da             	mov    rdx,r11
    cc12:	44 8b 85 60 ff ff ff 	mov    r8d,DWORD PTR [rbp-0xa0]
    cc19:	e8 62 14 00 00       	call   e080 <zbtScoreInsertEdgeLeaf>
    cc1e:	e9 42 11 00 00       	jmp    dd65 <zbtScoreInsertAt+0x16b5>
    cc23:	80 fb 5f             	cmp    bl,0x5f
    cc26:	77 77                	ja     cc9f <zbtScoreInsertAt+0x5ef>
    cc28:	48 81 fa 00 10 00 00 	cmp    rdx,0x1000
    cc2f:	73 6e                	jae    cc9f <zbtScoreInsertAt+0x5ef>
    cc31:	4d 85 ed             	test   r13,r13
    cc34:	0f 88 6e 03 00 00    	js     cfa8 <zbtScoreInsertAt+0x8f8>
    cc3a:	4d 09 fd             	or     r13,r15
    cc3d:	84 db                	test   bl,bl
    cc3f:	0f 84 6e 03 00 00    	je     cfb3 <zbtScoreInsertAt+0x903>
    cc45:	41 0f b6 79 35       	movzx  edi,BYTE PTR [r9+0x35]
    cc4a:	45 31 c0             	xor    r8d,r8d
    cc4d:	4c 89 e9             	mov    rcx,r13
    cc50:	31 f6                	xor    esi,esi
    cc52:	4c 89 ea             	mov    rdx,r13
    cc55:	48 8b 9d 50 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xb0]
    cc5c:	eb 28                	jmp    cc86 <zbtScoreInsertAt+0x5d6>
    cc5e:	66 90                	xchg   ax,ax
    cc60:	49 f7 d1             	not    r9
    cc63:	4d 89 ca             	mov    r10,r9
    cc66:	4d 31 ea             	xor    r10,r13
    cc69:	4c 09 d6             	or     rsi,r10
    cc6c:	49 39 c9             	cmp    r9,rcx
    cc6f:	49 0f 42 c9          	cmovb  rcx,r9
    cc73:	49 39 d1             	cmp    r9,rdx
    cc76:	49 0f 47 d1          	cmova  rdx,r9
    cc7a:	49 ff c0             	inc    r8
    cc7d:	4d 39 c4             	cmp    r12,r8
    cc80:	0f 84 15 01 00 00    	je     cd9b <zbtScoreInsertAt+0x6eb>
    cc86:	f3 42 0f 7e 84 c5 08 	movq   xmm0,QWORD PTR [rbp+r8*8-0x4f8]
    cc8d:	fb ff ff
    cc90:	66 49 0f 7e c1       	movq   r9,xmm0
    cc95:	4d 85 c9             	test   r9,r9
    cc98:	78 c6                	js     cc60 <zbtScoreInsertAt+0x5b0>
    cc9a:	4d 09 f9             	or     r9,r15
    cc9d:	eb c4                	jmp    cc63 <zbtScoreInsertAt+0x5b3>
    cc9f:	31 d2                	xor    edx,edx
    cca1:	31 c0                	xor    eax,eax
    cca3:	eb 1b                	jmp    ccc0 <zbtScoreInsertAt+0x610>
    cca5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    ccac:	00 00 00 00
    ccb0:	48 01 f0             	add    rax,rsi
    ccb3:	48 83 c0 0b          	add    rax,0xb
    ccb7:	48 83 c2 28          	add    rdx,0x28
    ccbb:	48 39 d1             	cmp    rcx,rdx
    ccbe:	74 37                	je     ccf7 <zbtScoreInsertAt+0x647>
    ccc0:	be 15 00 00 00       	mov    esi,0x15
    ccc5:	48 83 bc 15 e8 eb ff 	cmp    QWORD PTR [rbp+rdx*1-0x1418],0x0
    cccc:	ff 00
    ccce:	75 e0                	jne    ccb0 <zbtScoreInsertAt+0x600>
    ccd0:	48 8b bc 15 d8 eb ff 	mov    rdi,QWORD PTR [rbp+rdx*1-0x1428]
    ccd7:	ff
    ccd8:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    ccdf:	77 cf                	ja     ccb0 <zbtScoreInsertAt+0x600>
    cce1:	31 f6                	xor    esi,esi
    cce3:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    ccea:	40 0f 93 c6          	setae  sil
    ccee:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    ccf2:	48 ff c6             	inc    rsi
    ccf5:	eb b9                	jmp    ccb0 <zbtScoreInsertAt+0x600>
    ccf7:	84 db                	test   bl,bl
    ccf9:	0f 84 48 01 00 00    	je     ce47 <zbtScoreInsertAt+0x797>
    ccff:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cd03:	d1 e9                	shr    ecx,1
    cd05:	42 8d 14 e5 00 00 00 	lea    edx,[r12*8+0x0]
    cd0c:	00
    cd0d:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    cd11:	c7 45 c8 01 00 00 00 	mov    DWORD PTR [rbp-0x38],0x1
    cd18:	31 f6                	xor    esi,esi
    cd1a:	31 ff                	xor    edi,edi
    cd1c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    cd20:	41 b8 15 00 00 00    	mov    r8d,0x15
    cd26:	48 83 bc 35 e8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1418],0x0
    cd2d:	ff 00
    cd2f:	75 2f                	jne    cd60 <zbtScoreInsertAt+0x6b0>
    cd31:	4c 8b 8c 35 d8 eb ff 	mov    r9,QWORD PTR [rbp+rsi*1-0x1428]
    cd38:	ff
    cd39:	49 81 f9 3f 01 00 00 	cmp    r9,0x13f
    cd40:	77 1e                	ja     cd60 <zbtScoreInsertAt+0x6b0>
    cd42:	45 31 c0             	xor    r8d,r8d
    cd45:	49 81 f9 fe 00 00 00 	cmp    r9,0xfe
    cd4c:	41 0f 93 c0          	setae  r8b
    cd50:	4f 8d 04 41          	lea    r8,[r9+r8*2]
    cd54:	49 ff c0             	inc    r8
    cd57:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    cd5e:	00 00
    cd60:	4e 8d 0c 07          	lea    r9,[rdi+r8*1]
    cd64:	4e 8d 0c 4d 16 00 00 	lea    r9,[r9*2+0x16]
    cd6b:	00
    cd6c:	49 39 c1             	cmp    r9,rax
    cd6f:	73 16                	jae    cd87 <zbtScoreInsertAt+0x6d7>
    cd71:	4c 01 c7             	add    rdi,r8
    cd74:	48 83 c7 0b          	add    rdi,0xb
    cd78:	ff 45 c8             	inc    DWORD PTR [rbp-0x38]
    cd7b:	48 83 c6 28          	add    rsi,0x28
    cd7f:	48 39 f2             	cmp    rdx,rsi
    cd82:	75 9c                	jne    cd20 <zbtScoreInsertAt+0x670>
    cd84:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    cd87:	4c 89 e9             	mov    rcx,r13
    cd8a:	4d 85 ed             	test   r13,r13
    cd8d:	0f 88 c7 00 00 00    	js     ce5a <zbtScoreInsertAt+0x7aa>
    cd93:	4c 09 f9             	or     rcx,r15
    cd96:	e9 c2 00 00 00       	jmp    ce5d <zbtScoreInsertAt+0x7ad>
    cd9b:	40 84 ff             	test   dil,dil
    cd9e:	49 89 d5             	mov    r13,rdx
    cda1:	4c 0f 44 e9          	cmove  r13,rcx
    cda5:	48 85 f6             	test   rsi,rsi
    cda8:	0f 84 af 02 00 00    	je     d05d <zbtScoreInsertAt+0x9ad>
    cdae:	f3 48 0f bc fe       	tzcnt  rdi,rsi
    cdb3:	48 29 ca             	sub    rdx,rcx
    cdb6:	89 f9                	mov    ecx,edi
    cdb8:	48 d3 ea             	shr    rdx,cl
    cdbb:	48 85 d2             	test   rdx,rdx
    cdbe:	0f 84 66 03 00 00    	je     d12a <zbtScoreInsertAt+0xa7a>
    cdc4:	48 0f bd ca          	bsr    rcx,rdx
    cdc8:	83 f1 3f             	xor    ecx,0x3f
    cdcb:	41 b0 40             	mov    r8b,0x40
    cdce:	41 28 c8             	sub    r8b,cl
    cdd1:	41 0f b6 d0          	movzx  edx,r8b
    cdd5:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cdd9:	41 89 ca             	mov    r10d,ecx
    cddc:	48 89 55 c8          	mov    QWORD PTR [rbp-0x38],rdx
    cde0:	44 0f af d2          	imul   r10d,edx
    cde4:	41 83 c2 07          	add    r10d,0x7
    cde8:	41 c1 ea 03          	shr    r10d,0x3
    cdec:	41 83 c2 09          	add    r10d,0x9
    cdf0:	41 83 e2 fe          	and    r10d,0xfffffffe
    cdf4:	e9 3d 03 00 00       	jmp    d136 <zbtScoreInsertAt+0xa86>
    cdf9:	49 d3 ef             	shr    r15,cl
    cdfc:	41 0f b6 49 34       	movzx  ecx,BYTE PTR [r9+0x34]
    ce01:	48 85 c9             	test   rcx,rcx
    ce04:	0f 84 2f 04 00 00    	je     d239 <zbtScoreInsertAt+0xb89>
    ce0a:	4c 89 fe             	mov    rsi,r15
    ce0d:	48 d3 ee             	shr    rsi,cl
    ce10:	80 f9 3f             	cmp    cl,0x3f
    ce13:	77 09                	ja     ce1e <zbtScoreInsertAt+0x76e>
    ce15:	48 85 f6             	test   rsi,rsi
    ce18:	0f 85 6f f9 ff ff    	jne    c78d <zbtScoreInsertAt+0xdd>
    ce1e:	45 8d 74 24 01       	lea    r14d,[r12+0x1]
    ce23:	89 ce                	mov    esi,ecx
    ce25:	41 0f af f6          	imul   esi,r14d
    ce29:	83 c6 07             	add    esi,0x7
    ce2c:	c1 ee 03             	shr    esi,0x3
    ce2f:	83 c6 09             	add    esi,0x9
    ce32:	81 e6 fe ff 00 00    	and    esi,0xfffe
    ce38:	48 89 75 a8          	mov    QWORD PTR [rbp-0x58],rsi
    ce3c:	89 ce                	mov    esi,ecx
    ce3e:	48 89 75 88          	mov    QWORD PTR [rbp-0x78],rsi
    ce42:	e9 0c 04 00 00       	jmp    d253 <zbtScoreInsertAt+0xba3>
    ce47:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    ce4e:	4c 89 e9             	mov    rcx,r13
    ce51:	4d 85 ed             	test   r13,r13
    ce54:	0f 89 39 ff ff ff    	jns    cd93 <zbtScoreInsertAt+0x6e3>
    ce5a:	48 f7 d1             	not    rcx
    ce5d:	8b 75 c8             	mov    esi,DWORD PTR [rbp-0x38]
    ce60:	89 f0                	mov    eax,esi
    ce62:	ba 38 00 00 00       	mov    edx,0x38
    ce67:	83 fe 02             	cmp    esi,0x2
    ce6a:	0f 82 8d 00 00 00    	jb     cefd <zbtScoreInsertAt+0x84d>
    ce70:	41 b9 01 00 00 00    	mov    r9d,0x1
    ce76:	31 ff                	xor    edi,edi
    ce78:	49 89 c8             	mov    r8,rcx
    ce7b:	48 89 ce             	mov    rsi,rcx
    ce7e:	eb 22                	jmp    cea2 <zbtScoreInsertAt+0x7f2>
    ce80:	4d 09 fa             	or     r10,r15
    ce83:	4d 89 d3             	mov    r11,r10
    ce86:	49 31 cb             	xor    r11,rcx
    ce89:	4c 09 df             	or     rdi,r11
    ce8c:	4d 39 c2             	cmp    r10,r8
    ce8f:	4d 0f 42 c2          	cmovb  r8,r10
    ce93:	49 39 f2             	cmp    r10,rsi
    ce96:	49 0f 47 f2          	cmova  rsi,r10
    ce9a:	49 ff c1             	inc    r9
    ce9d:	4c 39 c8             	cmp    rax,r9
    cea0:	74 19                	je     cebb <zbtScoreInsertAt+0x80b>
    cea2:	f3 42 0f 7e 84 cd 00 	movq   xmm0,QWORD PTR [rbp+r9*8-0x500]
    cea9:	fb ff ff
    ceac:	66 49 0f 7e c2       	movq   r10,xmm0
    ceb1:	4d 85 d2             	test   r10,r10
    ceb4:	79 ca                	jns    ce80 <zbtScoreInsertAt+0x7d0>
    ceb6:	49 f7 d2             	not    r10
    ceb9:	eb c8                	jmp    ce83 <zbtScoreInsertAt+0x7d3>
    cebb:	48 85 ff             	test   rdi,rdi
    cebe:	74 3d                	je     cefd <zbtScoreInsertAt+0x84d>
    cec0:	f3 48 0f bc cf       	tzcnt  rcx,rdi
    cec5:	4c 29 c6             	sub    rsi,r8
    cec8:	48 d3 ee             	shr    rsi,cl
    cecb:	48 85 f6             	test   rsi,rsi
    cece:	74 2d                	je     cefd <zbtScoreInsertAt+0x84d>
    ced0:	48 0f bd ce          	bsr    rcx,rsi
    ced4:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    ced8:	48 83 c1 41          	add    rcx,0x41
    cedc:	48 0f af c8          	imul   rcx,rax
    cee0:	48 83 c1 07          	add    rcx,0x7
    cee4:	48 c1 e9 03          	shr    rcx,0x3
    cee8:	48 83 c1 09          	add    rcx,0x9
    ceec:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    cef3:	ff ff 1f
    cef6:	48 21 ca             	and    rdx,rcx
    cef9:	48 83 c2 38          	add    rdx,0x38
    cefd:	48 8d 0c 40          	lea    rcx,[rax+rax*2]
    cf01:	48 01 d1             	add    rcx,rdx
    cf04:	83 7d c8 00          	cmp    DWORD PTR [rbp-0x38],0x0
    cf08:	74 59                	je     cf63 <zbtScoreInsertAt+0x8b3>
    cf0a:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
    cf11:	00
    cf12:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    cf16:	31 f6                	xor    esi,esi
    cf18:	eb 12                	jmp    cf2c <zbtScoreInsertAt+0x87c>
    cf1a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    cf20:	48 01 f9             	add    rcx,rdi
    cf23:	48 83 c6 28          	add    rsi,0x28
    cf27:	48 39 f2             	cmp    rdx,rsi
    cf2a:	74 37                	je     cf63 <zbtScoreInsertAt+0x8b3>
    cf2c:	bf 15 00 00 00       	mov    edi,0x15
    cf31:	48 83 bc 35 e8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1418],0x0
    cf38:	ff 00
    cf3a:	75 e4                	jne    cf20 <zbtScoreInsertAt+0x870>
    cf3c:	4c 8b 84 35 d8 eb ff 	mov    r8,QWORD PTR [rbp+rsi*1-0x1428]
    cf43:	ff
    cf44:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    cf4b:	77 d3                	ja     cf20 <zbtScoreInsertAt+0x870>
    cf4d:	31 ff                	xor    edi,edi
    cf4f:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    cf56:	40 0f 93 c7          	setae  dil
    cf5a:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    cf5e:	48 ff c7             	inc    rdi
    cf61:	eb bd                	jmp    cf20 <zbtScoreInsertAt+0x870>
    cf63:	48 81 f9 ff 0f 00 00 	cmp    rcx,0xfff
    cf6a:	0f 87 84 04 00 00    	ja     d3f4 <zbtScoreInsertAt+0xd44>
    cf70:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cf74:	89 cf                	mov    edi,ecx
    cf76:	2b 7d c8             	sub    edi,DWORD PTR [rbp-0x38]
    cf79:	f3 0f 7e 84 c5 00 fb 	movq   xmm0,QWORD PTR [rbp+rax*8-0x500]
    cf80:	ff ff
    cf82:	66 48 0f 7e c1       	movq   rcx,xmm0
    cf87:	48 85 c9             	test   rcx,rcx
    cf8a:	0f 88 da 00 00 00    	js     d06a <zbtScoreInsertAt+0x9ba>
    cf90:	4c 09 f9             	or     rcx,r15
    cf93:	89 fa                	mov    edx,edi
    cf95:	be 38 00 00 00       	mov    esi,0x38
    cf9a:	83 ff 02             	cmp    edi,0x2
    cf9d:	0f 83 da 00 00 00    	jae    d07d <zbtScoreInsertAt+0x9cd>
    cfa3:	e9 2c 04 00 00       	jmp    d3d4 <zbtScoreInsertAt+0xd24>
    cfa8:	49 f7 d5             	not    r13
    cfab:	84 db                	test   bl,bl
    cfad:	0f 85 92 fc ff ff    	jne    cc45 <zbtScoreInsertAt+0x595>
    cfb3:	31 c9                	xor    ecx,ecx
    cfb5:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    cfb9:	31 ff                	xor    edi,edi
    cfbb:	45 31 c0             	xor    r8d,r8d
    cfbe:	45 31 d2             	xor    r10d,r10d
    cfc1:	48 8b 9d 50 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xb0]
    cfc8:	4c 01 d0             	add    rax,r10
    cfcb:	48 83 c0 38          	add    rax,0x38
    cfcf:	48 8b 94 dd e8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1418]
    cfd6:	ff
    cfd7:	48 85 d2             	test   rdx,rdx
    cfda:	0f 85 72 01 00 00    	jne    d152 <zbtScoreInsertAt+0xaa2>
    cfe0:	4c 8b 9c dd d8 eb ff 	mov    r11,QWORD PTR [rbp+rbx*8-0x1428]
    cfe7:	ff
    cfe8:	31 c9                	xor    ecx,ecx
    cfea:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    cff1:	0f 93 c1             	setae  cl
    cff4:	49 81 fb 40 01 00 00 	cmp    r11,0x140
    cffb:	49 8d 54 4b 01       	lea    rdx,[r11+rcx*2+0x1]
    d000:	b9 15 00 00 00       	mov    ecx,0x15
    d005:	48 0f 42 ca          	cmovb  rcx,rdx
    d009:	48 01 c8             	add    rax,rcx
    d00c:	45 0f b7 61 36       	movzx  r12d,WORD PTR [r9+0x36]
    d011:	4c 39 e0             	cmp    rax,r12
    d014:	0f 87 4a 01 00 00    	ja     d164 <zbtScoreInsertAt+0xab4>
    d01a:	41 29 cc             	sub    r12d,ecx
    d01d:	45 0f b7 f4          	movzx  r14d,r12w
    d021:	4d 01 ce             	add    r14,r9
    d024:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    d02b:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    d02f:	4c 89 45 98          	mov    QWORD PTR [rbp-0x68],r8
    d033:	0f 87 15 0a 00 00    	ja     da4e <zbtScoreInsertAt+0x139e>
    d039:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    d03d:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    d040:	4c 89 d3             	mov    rbx,r10
    d043:	49 81 fb fd 00 00 00 	cmp    r11,0xfd
    d04a:	0f 87 27 0d 00 00    	ja     dd77 <zbtScoreInsertAt+0x16c7>
    d050:	bf 01 00 00 00       	mov    edi,0x1
    d055:	44 89 d8             	mov    eax,r11d
    d058:	e9 26 0d 00 00       	jmp    dd83 <zbtScoreInsertAt+0x16d3>
    d05d:	31 c9                	xor    ecx,ecx
    d05f:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    d063:	31 ff                	xor    edi,edi
    d065:	e9 c6 00 00 00       	jmp    d130 <zbtScoreInsertAt+0xa80>
    d06a:	48 f7 d1             	not    rcx
    d06d:	89 fa                	mov    edx,edi
    d06f:	be 38 00 00 00       	mov    esi,0x38
    d074:	83 ff 02             	cmp    edi,0x2
    d077:	0f 82 57 03 00 00    	jb     d3d4 <zbtScoreInsertAt+0xd24>
    d07d:	4c 8d 14 c5 00 fb ff 	lea    r10,[rax*8-0x500]
    d084:	ff
    d085:	49 01 ea             	add    r10,rbp
    d088:	41 bb 01 00 00 00    	mov    r11d,0x1
    d08e:	45 31 c0             	xor    r8d,r8d
    d091:	49 89 c9             	mov    r9,rcx
    d094:	48 89 cf             	mov    rdi,rcx
    d097:	eb 29                	jmp    d0c2 <zbtScoreInsertAt+0xa12>
    d099:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    d0a0:	4c 09 fb             	or     rbx,r15
    d0a3:	49 89 de             	mov    r14,rbx
    d0a6:	49 31 ce             	xor    r14,rcx
    d0a9:	4d 09 f0             	or     r8,r14
    d0ac:	4c 39 cb             	cmp    rbx,r9
    d0af:	4c 0f 42 cb          	cmovb  r9,rbx
    d0b3:	48 39 fb             	cmp    rbx,rdi
    d0b6:	48 0f 47 fb          	cmova  rdi,rbx
    d0ba:	49 ff c3             	inc    r11
    d0bd:	4c 39 da             	cmp    rdx,r11
    d0c0:	74 15                	je     d0d7 <zbtScoreInsertAt+0xa27>
    d0c2:	f3 43 0f 7e 04 da    	movq   xmm0,QWORD PTR [r10+r11*8]
    d0c8:	66 48 0f 7e c3       	movq   rbx,xmm0
    d0cd:	48 85 db             	test   rbx,rbx
    d0d0:	79 ce                	jns    d0a0 <zbtScoreInsertAt+0x9f0>
    d0d2:	48 f7 d3             	not    rbx
    d0d5:	eb cc                	jmp    d0a3 <zbtScoreInsertAt+0x9f3>
    d0d7:	4d 85 c0             	test   r8,r8
    d0da:	0f 84 f0 02 00 00    	je     d3d0 <zbtScoreInsertAt+0xd20>
    d0e0:	f3 49 0f bc c8       	tzcnt  rcx,r8
    d0e5:	4c 29 cf             	sub    rdi,r9
    d0e8:	48 d3 ef             	shr    rdi,cl
    d0eb:	48 85 ff             	test   rdi,rdi
    d0ee:	0f b6 5d a4          	movzx  ebx,BYTE PTR [rbp-0x5c]
    d0f2:	0f 84 dc 02 00 00    	je     d3d4 <zbtScoreInsertAt+0xd24>
    d0f8:	48 0f bd cf          	bsr    rcx,rdi
    d0fc:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    d100:	48 83 c1 41          	add    rcx,0x41
    d104:	48 0f af ca          	imul   rcx,rdx
    d108:	48 83 c1 07          	add    rcx,0x7
    d10c:	48 c1 e9 03          	shr    rcx,0x3
    d110:	48 83 c1 09          	add    rcx,0x9
    d114:	48 be fe ff ff ff ff 	movabs rsi,0x1ffffffffffffffe
    d11b:	ff ff 1f
    d11e:	48 21 ce             	and    rsi,rcx
    d121:	48 83 c6 38          	add    rsi,0x38
    d125:	e9 aa 02 00 00       	jmp    d3d4 <zbtScoreInsertAt+0xd24>
    d12a:	31 c9                	xor    ecx,ecx
    d12c:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    d130:	45 31 c0             	xor    r8d,r8d
    d133:	45 31 d2             	xor    r10d,r10d
    d136:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    d13a:	4c 01 d0             	add    rax,r10
    d13d:	48 83 c0 38          	add    rax,0x38
    d141:	48 8b 94 dd e8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1418]
    d148:	ff
    d149:	48 85 d2             	test   rdx,rdx
    d14c:	0f 84 8e fe ff ff    	je     cfe0 <zbtScoreInsertAt+0x930>
    d152:	48 83 c0 15          	add    rax,0x15
    d156:	45 0f b7 61 36       	movzx  r12d,WORD PTR [r9+0x36]
    d15b:	4c 39 e0             	cmp    rax,r12
    d15e:	0f 86 bd 00 00 00    	jbe    d221 <zbtScoreInsertAt+0xb71>
    d164:	4c 89 cb             	mov    rbx,r9
    d167:	45 8b 49 30          	mov    r9d,DWORD PTR [r9+0x30]
    d16b:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d172:	48 8d 95 00 fb ff ff 	lea    rdx,[rbp-0x500]
    d179:	48 8d 8d d0 eb ff ff 	lea    rcx,[rbp-0x1430]
    d180:	4c 8d 85 e0 fe ff ff 	lea    r8,[rbp-0x120]
    d187:	4c 8b bd 78 ff ff ff 	mov    r15,QWORD PTR [rbp-0x88]
    d18e:	4c 89 ff             	mov    rdi,r15
    d191:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    d195:	e8 e6 ed ff ff       	call   bf80 <zbtScoreLeafBuild>
    d19a:	49 89 c6             	mov    r14,rax
    d19d:	48 8b 03             	mov    rax,QWORD PTR [rbx]
    d1a0:	49 89 06             	mov    QWORD PTR [r14],rax
    d1a3:	0f b6 43 10          	movzx  eax,BYTE PTR [rbx+0x10]
    d1a7:	41 88 46 10          	mov    BYTE PTR [r14+0x10],al
    d1ab:	0f b7 4b 16          	movzx  ecx,WORD PTR [rbx+0x16]
    d1af:	66 41 89 4e 16       	mov    WORD PTR [r14+0x16],cx
    d1b4:	48 8b 4b 18          	mov    rcx,QWORD PTR [rbx+0x18]
    d1b8:	49 89 4e 18          	mov    QWORD PTR [r14+0x18],rcx
    d1bc:	48 8b 53 20          	mov    rdx,QWORD PTR [rbx+0x20]
    d1c0:	49 89 56 20          	mov    QWORD PTR [r14+0x20],rdx
    d1c4:	49 8d 57 08          	lea    rdx,[r15+0x8]
    d1c8:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d1cc:	48 85 c9             	test   rcx,rcx
    d1cf:	48 0f 44 f2          	cmove  rsi,rdx
    d1d3:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d1d6:	49 8b 4e 20          	mov    rcx,QWORD PTR [r14+0x20]
    d1da:	49 8d 57 10          	lea    rdx,[r15+0x10]
    d1de:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d1e2:	48 85 c9             	test   rcx,rcx
    d1e5:	48 0f 44 f2          	cmove  rsi,rdx
    d1e9:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d1ec:	48 8b 0b             	mov    rcx,QWORD PTR [rbx]
    d1ef:	48 85 c9             	test   rcx,rcx
    d1f2:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d1f7:	49 0f 44 c7          	cmove  rax,r15
    d1fb:	4c 89 30             	mov    QWORD PTR [rax],r14
    d1fe:	49 8b 76 08          	mov    rsi,QWORD PTR [r14+0x8]
    d202:	48 2b 73 08          	sub    rsi,QWORD PTR [rbx+0x8]
    d206:	4c 89 f7             	mov    rdi,r14
    d209:	e8 62 1d 00 00       	call   ef70 <zbtScoreUpdatePath>
    d20e:	4c 89 ff             	mov    rdi,r15
    d211:	48 89 de             	mov    rsi,rbx
    d214:	e8 b7 e9 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d219:	4c 89 f0             	mov    rax,r14
    d21c:	e9 44 0b 00 00       	jmp    dd65 <zbtScoreInsertAt+0x16b5>
    d221:	41 83 c4 eb          	add    r12d,0xffffffeb
    d225:	45 0f b7 f4          	movzx  r14d,r12w
    d229:	4d 01 ce             	add    r14,r9
    d22c:	48 8b 8c dd d8 eb ff 	mov    rcx,QWORD PTR [rbp+rbx*8-0x1428]
    d233:	ff
    d234:	e9 73 08 00 00       	jmp    daac <zbtScoreInsertAt+0x13fc>
    d239:	4d 85 ff             	test   r15,r15
    d23c:	0f 85 4b f5 ff ff    	jne    c78d <zbtScoreInsertAt+0xdd>
    d242:	45 8d 74 24 01       	lea    r14d,[r12+0x1]
    d247:	31 f6                	xor    esi,esi
    d249:	48 89 75 88          	mov    QWORD PTR [rbp-0x78],rsi
    d24d:	31 f6                	xor    esi,esi
    d24f:	48 89 75 a8          	mov    QWORD PTR [rbp-0x58],rsi
    d253:	be 15 00 00 00       	mov    esi,0x15
    d258:	48 89 75 c0          	mov    QWORD PTR [rbp-0x40],rsi
    d25c:	49 83 7b 18 00       	cmp    QWORD PTR [r11+0x18],0x0
    d261:	75 25                	jne    d288 <zbtScoreInsertAt+0xbd8>
    d263:	49 8b 7b 08          	mov    rdi,QWORD PTR [r11+0x8]
    d267:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    d26e:	77 18                	ja     d288 <zbtScoreInsertAt+0xbd8>
    d270:	31 f6                	xor    esi,esi
    d272:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    d279:	40 0f 93 c6          	setae  sil
    d27d:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    d281:	48 ff c6             	inc    rsi
    d284:	48 89 75 c0          	mov    QWORD PTR [rbp-0x40],rsi
    d288:	44 89 f6             	mov    esi,r14d
    d28b:	48 89 75 90          	mov    QWORD PTR [rbp-0x70],rsi
    d28f:	48 8d 34 76          	lea    rsi,[rsi+rsi*2]
    d293:	48 03 75 a8          	add    rsi,QWORD PTR [rbp-0x58]
    d297:	48 8b 7d c0          	mov    rdi,QWORD PTR [rbp-0x40]
    d29b:	48 01 f7             	add    rdi,rsi
    d29e:	48 83 c7 38          	add    rdi,0x38
    d2a2:	41 0f b7 71 36       	movzx  esi,WORD PTR [r9+0x36]
    d2a7:	48 39 f7             	cmp    rdi,rsi
    d2aa:	0f 87 dd f4 ff ff    	ja     c78d <zbtScoreInsertAt+0xdd>
    d2b0:	44 89 75 a4          	mov    DWORD PTR [rbp-0x5c],r14d
    d2b4:	49 8d 73 18          	lea    rsi,[r11+0x18]
    d2b8:	48 89 75 80          	mov    QWORD PTR [rbp-0x80],rsi
    d2bc:	45 89 e6             	mov    r14d,r12d
    d2bf:	41 29 d6             	sub    r14d,edx
    d2c2:	84 c0                	test   al,al
    d2c4:	44 0f 44 f2          	cmove  r14d,edx
    d2c8:	48 85 c9             	test   rcx,rcx
    d2cb:	0f 84 d8 0a 00 00    	je     dda9 <zbtScoreInsertAt+0x16f9>
    d2d1:	41 89 cd             	mov    r13d,ecx
    d2d4:	44 89 e0             	mov    eax,r12d
    d2d7:	0f af c1             	imul   eax,ecx
    d2da:	83 c0 07             	add    eax,0x7
    d2dd:	c1 e8 03             	shr    eax,0x3
    d2e0:	83 c0 09             	add    eax,0x9
    d2e3:	25 fe 3f 00 00       	and    eax,0x3ffe
    d2e8:	44 89 f3             	mov    ebx,r14d
    d2eb:	4d 8d 71 38          	lea    r14,[r9+0x38]
    d2ef:	4c 01 c8             	add    rax,r9
    d2f2:	48 83 c0 38          	add    rax,0x38
    d2f6:	48 89 85 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],rax
    d2fd:	4a 8d 34 60          	lea    rsi,[rax+r12*2]
    d301:	48 8d bd d0 eb ff ff 	lea    rdi,[rbp-0x1430]
    d308:	4c 89 e2             	mov    rdx,r12
    d30b:	e8 10 3e ff ff       	call   1120 <memcpy@plt>
    d310:	89 d9                	mov    ecx,ebx
    d312:	4c 89 6d b8          	mov    QWORD PTR [rbp-0x48],r13
    d316:	4c 89 e8             	mov    rax,r13
    d319:	48 89 8d 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rcx
    d320:	48 0f af c1          	imul   rax,rcx
    d324:	45 89 e0             	mov    r8d,r12d
    d327:	89 9d 70 ff ff ff    	mov    DWORD PTR [rbp-0x90],ebx
    d32d:	41 29 d8             	sub    r8d,ebx
    d330:	0f 85 64 0b 00 00    	jne    de9a <zbtScoreInsertAt+0x17ea>
    d336:	48 89 c6             	mov    rsi,rax
    d339:	48 c1 ee 03          	shr    rsi,0x3
    d33d:	83 e0 07             	and    eax,0x7
    d340:	bf 40 00 00 00       	mov    edi,0x40
    d345:	29 c7                	sub    edi,eax
    d347:	4c 8b 55 88          	mov    r10,QWORD PTR [rbp-0x78]
    d34b:	44 39 d7             	cmp    edi,r10d
    d34e:	44 89 d2             	mov    edx,r10d
    d351:	0f 42 d7             	cmovb  edx,edi
    d354:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    d35b:	49 c7 c1 ff ff ff ff 	mov    r9,0xffffffffffffffff
    d362:	89 d1                	mov    ecx,edx
    d364:	49 d3 e1             	shl    r9,cl
    d367:	83 fa 40             	cmp    edx,0x40
    d36a:	49 f7 d1             	not    r9
    d36d:	4d 0f 44 c8          	cmove  r9,r8
    d371:	4d 89 c8             	mov    r8,r9
    d374:	89 c1                	mov    ecx,eax
    d376:	49 d3 e0             	shl    r8,cl
    d379:	49 f7 d0             	not    r8
    d37c:	4d 23 04 36          	and    r8,QWORD PTR [r14+rsi*1]
    d380:	4d 21 f9             	and    r9,r15
    d383:	49 d3 e1             	shl    r9,cl
    d386:	4d 09 c1             	or     r9,r8
    d389:	4d 89 0c 36          	mov    QWORD PTR [r14+rsi*1],r9
    d38d:	44 39 d7             	cmp    edi,r10d
    d390:	73 20                	jae    d3b2 <zbtScoreInsertAt+0xd02>
    d392:	41 29 d2             	sub    r10d,edx
    d395:	41 0f b6 44 36 08    	movzx  eax,BYTE PTR [r14+rsi*1+0x8]
    d39b:	89 d1                	mov    ecx,edx
    d39d:	49 d3 ef             	shr    r15,cl
    d3a0:	44 31 f8             	xor    eax,r15d
    d3a3:	44 89 d1             	mov    ecx,r10d
    d3a6:	d3 e8                	shr    eax,cl
    d3a8:	d3 e0                	shl    eax,cl
    d3aa:	44 31 f8             	xor    eax,r15d
    d3ad:	41 88 44 36 08       	mov    BYTE PTR [r14+rsi*1+0x8],al
    d3b2:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    d3b6:	44 8b b5 70 ff ff ff 	mov    r14d,DWORD PTR [rbp-0x90]
    d3bd:	4c 8b bd 60 ff ff ff 	mov    r15,QWORD PTR [rbp-0xa0]
    d3c4:	48 8b b5 68 ff ff ff 	mov    rsi,QWORD PTR [rbp-0x98]
    d3cb:	e9 fe 09 00 00       	jmp    ddce <zbtScoreInsertAt+0x171e>
    d3d0:	0f b6 5d a4          	movzx  ebx,BYTE PTR [rbp-0x5c]
    d3d4:	48 8d 0c 52          	lea    rcx,[rdx+rdx*2]
    d3d8:	48 01 f1             	add    rcx,rsi
    d3db:	8b 75 c8             	mov    esi,DWORD PTR [rbp-0x38]
    d3de:	39 75 b8             	cmp    DWORD PTR [rbp-0x48],esi
    d3e1:	0f 85 18 06 00 00    	jne    d9ff <zbtScoreInsertAt+0x134f>
    d3e7:	48 81 f9 00 10 00 00 	cmp    rcx,0x1000
    d3ee:	0f 82 73 03 00 00    	jb     d767 <zbtScoreInsertAt+0x10b7>
    d3f4:	84 db                	test   bl,bl
    d3f6:	0f 84 4c 03 00 00    	je     d748 <zbtScoreInsertAt+0x1098>
    d3fc:	4c 89 e8             	mov    rax,r13
    d3ff:	4c 09 f8             	or     rax,r15
    d402:	4d 85 ed             	test   r13,r13
    d405:	49 f7 d5             	not    r13
    d408:	4c 0f 49 e8          	cmovns r13,rax
    d40c:	48 8d 95 10 fb ff ff 	lea    rdx,[rbp-0x4f0]
    d413:	31 f6                	xor    esi,esi
    d415:	48 c7 45 98 ff ff ff 	mov    QWORD PTR [rbp-0x68],0xffffffffffffffff
    d41c:	ff
    d41d:	41 b8 01 00 00 00    	mov    r8d,0x1
    d423:	41 b9 28 00 00 00    	mov    r9d,0x28
    d429:	4c 8d b5 10 ec ff ff 	lea    r14,[rbp-0x13f0]
    d430:	44 89 e1             	mov    ecx,r12d
    d433:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    d43a:	4c 89 6d 88          	mov    QWORD PTR [rbp-0x78],r13
    d43e:	eb 27                	jmp    d467 <zbtScoreInsertAt+0xdb7>
    d440:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d444:	49 ff c0             	inc    r8
    d447:	48 83 c6 08          	add    rsi,0x8
    d44b:	49 83 c1 28          	add    r9,0x28
    d44f:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    d453:	ff c9                	dec    ecx
    d455:	48 83 c2 08          	add    rdx,0x8
    d459:	49 83 c6 28          	add    r14,0x28
    d45d:	4c 3b 45 b8          	cmp    r8,QWORD PTR [rbp-0x48]
    d461:	0f 84 db 02 00 00    	je     d742 <zbtScoreInsertAt+0x1092>
    d467:	4c 89 75 90          	mov    QWORD PTR [rbp-0x70],r14
    d46b:	41 be 38 00 00 00    	mov    r14d,0x38
    d471:	49 83 f8 02          	cmp    r8,0x2
    d475:	4c 89 45 c0          	mov    QWORD PTR [rbp-0x40],r8
    d479:	0f 82 b1 00 00 00    	jb     d530 <zbtScoreInsertAt+0xe80>
    d47f:	49 89 cc             	mov    r12,rcx
    d482:	31 db                	xor    ebx,ebx
    d484:	4c 89 ef             	mov    rdi,r13
    d487:	31 c9                	xor    ecx,ecx
    d489:	4c 89 e8             	mov    rax,r13
    d48c:	eb 25                	jmp    d4b3 <zbtScoreInsertAt+0xe03>
    d48e:	66 90                	xchg   ax,ax
    d490:	4d 09 fa             	or     r10,r15
    d493:	4d 89 d3             	mov    r11,r10
    d496:	4d 31 eb             	xor    r11,r13
    d499:	4c 09 d9             	or     rcx,r11
    d49c:	49 39 fa             	cmp    r10,rdi
    d49f:	49 0f 42 fa          	cmovb  rdi,r10
    d4a3:	49 39 c2             	cmp    r10,rax
    d4a6:	49 0f 47 c2          	cmova  rax,r10
    d4aa:	48 83 c3 08          	add    rbx,0x8
    d4ae:	48 39 de             	cmp    rsi,rbx
    d4b1:	74 1d                	je     d4d0 <zbtScoreInsertAt+0xe20>
    d4b3:	f3 0f 7e 84 1d 08 fb 	movq   xmm0,QWORD PTR [rbp+rbx*1-0x4f8]
    d4ba:	ff ff
    d4bc:	66 49 0f 7e c2       	movq   r10,xmm0
    d4c1:	4d 85 d2             	test   r10,r10
    d4c4:	79 ca                	jns    d490 <zbtScoreInsertAt+0xde0>
    d4c6:	49 f7 d2             	not    r10
    d4c9:	eb c8                	jmp    d493 <zbtScoreInsertAt+0xde3>
    d4cb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    d4d0:	48 85 c9             	test   rcx,rcx
    d4d3:	74 4a                	je     d51f <zbtScoreInsertAt+0xe6f>
    d4d5:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    d4da:	48 29 f8             	sub    rax,rdi
    d4dd:	48 d3 e8             	shr    rax,cl
    d4e0:	48 85 c0             	test   rax,rax
    d4e3:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d4e7:	4c 89 e1             	mov    rcx,r12
    d4ea:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d4ee:	74 40                	je     d530 <zbtScoreInsertAt+0xe80>
    d4f0:	4c 0f bd f0          	bsr    r14,rax
    d4f4:	49 83 f6 c0          	xor    r14,0xffffffffffffffc0
    d4f8:	49 83 c6 41          	add    r14,0x41
    d4fc:	4d 0f af f0          	imul   r14,r8
    d500:	49 83 c6 07          	add    r14,0x7
    d504:	49 c1 ee 03          	shr    r14,0x3
    d508:	49 83 c6 09          	add    r14,0x9
    d50c:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d513:	ff ff 1f
    d516:	49 21 c6             	and    r14,rax
    d519:	49 83 c6 38          	add    r14,0x38
    d51d:	eb 11                	jmp    d530 <zbtScoreInsertAt+0xe80>
    d51f:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d523:	4c 89 e1             	mov    rcx,r12
    d526:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d52a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    d530:	89 c9                	mov    ecx,ecx
    d532:	48 89 4d a8          	mov    QWORD PTR [rbp-0x58],rcx
    d536:	48 ff c9             	dec    rcx
    d539:	4b 8d 1c 40          	lea    rbx,[r8+r8*2]
    d53d:	4c 01 f3             	add    rbx,r14
    d540:	31 c0                	xor    eax,eax
    d542:	eb 18                	jmp    d55c <zbtScoreInsertAt+0xeac>
    d544:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d54b:	00 00 00 00 00
    d550:	48 01 fb             	add    rbx,rdi
    d553:	48 83 c0 28          	add    rax,0x28
    d557:	49 39 c1             	cmp    r9,rax
    d55a:	74 44                	je     d5a0 <zbtScoreInsertAt+0xef0>
    d55c:	bf 15 00 00 00       	mov    edi,0x15
    d561:	48 83 bc 05 e8 eb ff 	cmp    QWORD PTR [rbp+rax*1-0x1418],0x0
    d568:	ff 00
    d56a:	75 e4                	jne    d550 <zbtScoreInsertAt+0xea0>
    d56c:	4c 8b 94 05 d8 eb ff 	mov    r10,QWORD PTR [rbp+rax*1-0x1428]
    d573:	ff
    d574:	49 81 fa 3f 01 00 00 	cmp    r10,0x13f
    d57b:	77 d3                	ja     d550 <zbtScoreInsertAt+0xea0>
    d57d:	31 ff                	xor    edi,edi
    d57f:	49 81 fa fe 00 00 00 	cmp    r10,0xfe
    d586:	40 0f 93 c7          	setae  dil
    d58a:	49 8d 3c 7a          	lea    rdi,[r10+rdi*2]
    d58e:	48 ff c7             	inc    rdi
    d591:	eb bd                	jmp    d550 <zbtScoreInsertAt+0xea0>
    d593:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d59a:	84 00 00 00 00 00
    d5a0:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    d5a4:	f3 0f 7e 84 c5 00 fb 	movq   xmm0,QWORD PTR [rbp+rax*8-0x500]
    d5ab:	ff ff
    d5ad:	66 49 0f 7e c5       	movq   r13,xmm0
    d5b2:	4d 85 ed             	test   r13,r13
    d5b5:	78 09                	js     d5c0 <zbtScoreInsertAt+0xf10>
    d5b7:	4d 09 fd             	or     r13,r15
    d5ba:	eb 07                	jmp    d5c3 <zbtScoreInsertAt+0xf13>
    d5bc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d5c0:	49 f7 d5             	not    r13
    d5c3:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d5c7:	41 29 c6             	sub    r14d,eax
    d5ca:	41 bf 38 00 00 00    	mov    r15d,0x38
    d5d0:	41 83 fe 02          	cmp    r14d,0x2
    d5d4:	72 6a                	jb     d640 <zbtScoreInsertAt+0xf90>
    d5d6:	45 31 d2             	xor    r10d,r10d
    d5d9:	4c 89 ef             	mov    rdi,r13
    d5dc:	45 31 e4             	xor    r12d,r12d
    d5df:	4c 89 e8             	mov    rax,r13
    d5e2:	eb 38                	jmp    d61c <zbtScoreInsertAt+0xf6c>
    d5e4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d5eb:	00 00 00 00 00
    d5f0:	49 bb 00 00 00 00 00 	movabs r11,0x8000000000000000
    d5f7:	00 00 80
    d5fa:	4d 09 d8             	or     r8,r11
    d5fd:	4d 89 c3             	mov    r11,r8
    d600:	4d 31 eb             	xor    r11,r13
    d603:	4d 09 dc             	or     r12,r11
    d606:	49 39 f8             	cmp    r8,rdi
    d609:	49 0f 42 f8          	cmovb  rdi,r8
    d60d:	49 39 c0             	cmp    r8,rax
    d610:	49 0f 47 c0          	cmova  rax,r8
    d614:	49 ff c2             	inc    r10
    d617:	4c 39 d1             	cmp    rcx,r10
    d61a:	74 34                	je     d650 <zbtScoreInsertAt+0xfa0>
    d61c:	f3 42 0f 7e 04 d2    	movq   xmm0,QWORD PTR [rdx+r10*8]
    d622:	66 49 0f 7e c0       	movq   r8,xmm0
    d627:	4d 85 c0             	test   r8,r8
    d62a:	79 c4                	jns    d5f0 <zbtScoreInsertAt+0xf40>
    d62c:	49 f7 d0             	not    r8
    d62f:	eb cc                	jmp    d5fd <zbtScoreInsertAt+0xf4d>
    d631:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d638:	0f 1f 84 00 00 00 00
    d63f:	00
    d640:	4c 8b 6d 88          	mov    r13,QWORD PTR [rbp-0x78]
    d644:	eb 5a                	jmp    d6a0 <zbtScoreInsertAt+0xff0>
    d646:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    d64d:	00 00 00
    d650:	4d 85 e4             	test   r12,r12
    d653:	4c 8b 6d 88          	mov    r13,QWORD PTR [rbp-0x78]
    d657:	74 43                	je     d69c <zbtScoreInsertAt+0xfec>
    d659:	f3 49 0f bc cc       	tzcnt  rcx,r12
    d65e:	48 29 f8             	sub    rax,rdi
    d661:	48 d3 e8             	shr    rax,cl
    d664:	48 85 c0             	test   rax,rax
    d667:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d66b:	74 33                	je     d6a0 <zbtScoreInsertAt+0xff0>
    d66d:	4c 0f bd f8          	bsr    r15,rax
    d671:	49 83 f7 c0          	xor    r15,0xffffffffffffffc0
    d675:	49 83 c7 41          	add    r15,0x41
    d679:	4d 0f af fe          	imul   r15,r14
    d67d:	49 83 c7 07          	add    r15,0x7
    d681:	49 c1 ef 03          	shr    r15,0x3
    d685:	49 83 c7 09          	add    r15,0x9
    d689:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d690:	ff ff 1f
    d693:	49 21 c7             	and    r15,rax
    d696:	49 83 c7 38          	add    r15,0x38
    d69a:	eb 04                	jmp    d6a0 <zbtScoreInsertAt+0xff0>
    d69c:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d6a0:	4b 8d 04 76          	lea    rax,[r14+r14*2]
    d6a4:	4c 01 f8             	add    rax,r15
    d6a7:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    d6ab:	4c 8b 75 90          	mov    r14,QWORD PTR [rbp-0x70]
    d6af:	4c 89 f7             	mov    rdi,r14
    d6b2:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    d6b9:	00 00 80
    d6bc:	eb 0e                	jmp    d6cc <zbtScoreInsertAt+0x101c>
    d6be:	66 90                	xchg   ax,ax
    d6c0:	4c 01 d0             	add    rax,r10
    d6c3:	48 83 c7 28          	add    rdi,0x28
    d6c7:	48 ff c9             	dec    rcx
    d6ca:	74 34                	je     d700 <zbtScoreInsertAt+0x1050>
    d6cc:	41 ba 15 00 00 00    	mov    r10d,0x15
    d6d2:	48 83 3f 00          	cmp    QWORD PTR [rdi],0x0
    d6d6:	75 e8                	jne    d6c0 <zbtScoreInsertAt+0x1010>
    d6d8:	4c 8b 5f f0          	mov    r11,QWORD PTR [rdi-0x10]
    d6dc:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    d6e3:	77 db                	ja     d6c0 <zbtScoreInsertAt+0x1010>
    d6e5:	45 31 c0             	xor    r8d,r8d
    d6e8:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    d6ef:	41 0f 93 c0          	setae  r8b
    d6f3:	4f 8d 14 43          	lea    r10,[r11+r8*2]
    d6f7:	49 ff c2             	inc    r10
    d6fa:	eb c4                	jmp    d6c0 <zbtScoreInsertAt+0x1010>
    d6fc:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d700:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    d707:	0f 87 33 fd ff ff    	ja     d440 <zbtScoreInsertAt+0xd90>
    d70d:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    d713:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d717:	0f 87 27 fd ff ff    	ja     d444 <zbtScoreInsertAt+0xd94>
    d71d:	48 39 c3             	cmp    rbx,rax
    d720:	48 0f 47 c3          	cmova  rax,rbx
    d724:	48 8b 7d 98          	mov    rdi,QWORD PTR [rbp-0x68]
    d728:	48 39 f8             	cmp    rax,rdi
    d72b:	8b 4d c8             	mov    ecx,DWORD PTR [rbp-0x38]
    d72e:	41 0f 42 c8          	cmovb  ecx,r8d
    d732:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    d735:	48 0f 42 f8          	cmovb  rdi,rax
    d739:	48 89 7d 98          	mov    QWORD PTR [rbp-0x68],rdi
    d73d:	e9 02 fd ff ff       	jmp    d444 <zbtScoreInsertAt+0xd94>
    d742:	83 7d c8 00          	cmp    DWORD PTR [rbp-0x38],0x0
    d746:	75 1f                	jne    d767 <zbtScoreInsertAt+0x10b7>
    d748:	48 8d 3d cf 5e 00 00 	lea    rdi,[rip+0x5ecf]        # 1361e <_IO_stdin_used+0x61e>
    d74f:	48 8d 15 79 61 00 00 	lea    rdx,[rip+0x6179]        # 138cf <_IO_stdin_used+0x8cf>
    d756:	be 52 05 00 00       	mov    esi,0x552
    d75b:	e8 40 3f 00 00       	call   116a0 <standalone_panic>
    d760:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    d767:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d76b:	44 8b 7d c8          	mov    r15d,DWORD PTR [rbp-0x38]
    d76f:	45 29 fe             	sub    r14d,r15d
    d772:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    d776:	44 8b 48 30          	mov    r9d,DWORD PTR [rax+0x30]
    d77a:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d781:	48 8d 95 00 fb ff ff 	lea    rdx,[rbp-0x500]
    d788:	48 8d 8d d0 eb ff ff 	lea    rcx,[rbp-0x1430]
    d78f:	4c 8d 85 e0 fe ff ff 	lea    r8,[rbp-0x120]
    d796:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d79d:	48 89 df             	mov    rdi,rbx
    d7a0:	44 89 fe             	mov    esi,r15d
    d7a3:	e8 d8 e7 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d7a8:	49 89 c5             	mov    r13,rax
    d7ab:	44 89 f8             	mov    eax,r15d
    d7ae:	48 8d 14 c5 00 fb ff 	lea    rdx,[rax*8-0x500]
    d7b5:	ff
    d7b6:	48 01 ea             	add    rdx,rbp
    d7b9:	48 8d 0c 80          	lea    rcx,[rax+rax*4]
    d7bd:	48 8d 8c cd d0 eb ff 	lea    rcx,[rbp+rcx*8-0x1430]
    d7c4:	ff
    d7c5:	4c 8d 84 05 e0 fe ff 	lea    r8,[rbp+rax*1-0x120]
    d7cc:	ff
    d7cd:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d7d4:	48 89 df             	mov    rdi,rbx
    d7d7:	44 89 f6             	mov    esi,r14d
    d7da:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    d7e0:	e8 9b e7 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d7e5:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d7e9:	4c 89 e7             	mov    rdi,r12
    d7ec:	49 89 c4             	mov    r12,rax
    d7ef:	41 0f b7 40 16       	movzx  eax,WORD PTR [r8+0x16]
    d7f4:	66 41 89 44 24 16    	mov    WORD PTR [r12+0x16],ax
    d7fa:	66 41 89 45 16       	mov    WORD PTR [r13+0x16],ax
    d7ff:	49 8b 00             	mov    rax,QWORD PTR [r8]
    d802:	49 89 45 00          	mov    QWORD PTR [r13+0x0],rax
    d806:	41 0f b6 40 10       	movzx  eax,BYTE PTR [r8+0x10]
    d80b:	41 88 45 10          	mov    BYTE PTR [r13+0x10],al
    d80f:	49 8b 48 18          	mov    rcx,QWORD PTR [r8+0x18]
    d813:	49 89 4d 18          	mov    QWORD PTR [r13+0x18],rcx
    d817:	4d 89 65 20          	mov    QWORD PTR [r13+0x20],r12
    d81b:	4d 89 6c 24 18       	mov    QWORD PTR [r12+0x18],r13
    d820:	49 8b 48 20          	mov    rcx,QWORD PTR [r8+0x20]
    d824:	49 89 4c 24 20       	mov    QWORD PTR [r12+0x20],rcx
    d829:	49 8b 4d 18          	mov    rcx,QWORD PTR [r13+0x18]
    d82d:	48 8d 53 08          	lea    rdx,[rbx+0x8]
    d831:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d835:	48 85 c9             	test   rcx,rcx
    d838:	48 0f 44 f2          	cmove  rsi,rdx
    d83c:	4c 89 2e             	mov    QWORD PTR [rsi],r13
    d83f:	49 8b 4c 24 20       	mov    rcx,QWORD PTR [r12+0x20]
    d844:	48 8d 53 10          	lea    rdx,[rbx+0x10]
    d848:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d84c:	48 85 c9             	test   rcx,rcx
    d84f:	48 0f 44 f2          	cmove  rsi,rdx
    d853:	4c 89 26             	mov    QWORD PTR [rsi],r12
    d856:	49 8b 08             	mov    rcx,QWORD PTR [r8]
    d859:	48 85 c9             	test   rcx,rcx
    d85c:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d861:	48 0f 44 c3          	cmove  rax,rbx
    d865:	4c 89 6d a8          	mov    QWORD PTR [rbp-0x58],r13
    d869:	4c 89 28             	mov    QWORD PTR [rax],r13
    d86c:	c7 85 58 ff ff ff 00 	mov    DWORD PTR [rbp-0xa8],0x0
    d873:	00 00 00
    d876:	41 39 ff             	cmp    r15d,edi
    d879:	76 5a                	jbe    d8d5 <zbtScoreInsertAt+0x1225>
    d87b:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d882:	48 89 df             	mov    rdi,rbx
    d885:	4c 89 c6             	mov    rsi,r8
    d888:	e8 43 e3 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d88d:	48 89 df             	mov    rdi,rbx
    d890:	4c 8b 75 a8          	mov    r14,QWORD PTR [rbp-0x58]
    d894:	4c 89 f6             	mov    rsi,r14
    d897:	4c 89 e2             	mov    rdx,r12
    d89a:	e8 81 09 00 00       	call   e220 <zbtScoreInsertSibling>
    d89f:	49 8b 1e             	mov    rbx,QWORD PTR [r14]
    d8a2:	48 85 db             	test   rbx,rbx
    d8a5:	74 19                	je     d8c0 <zbtScoreInsertAt+0x1210>
    d8a7:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    d8ae:	00 00
    d8b0:	48 89 df             	mov    rdi,rbx
    d8b3:	e8 d8 0d 00 00       	call   e690 <zbtScoreRefreshNode>
    d8b8:	48 8b 1b             	mov    rbx,QWORD PTR [rbx]
    d8bb:	48 85 db             	test   rbx,rbx
    d8be:	75 f0                	jne    d8b0 <zbtScoreInsertAt+0x1200>
    d8c0:	8b 45 c8             	mov    eax,DWORD PTR [rbp-0x38]
    d8c3:	39 85 68 ff ff ff    	cmp    DWORD PTR [rbp-0x98],eax
    d8c9:	4d 0f 42 e6          	cmovb  r12,r14
    d8cd:	4c 89 e0             	mov    rax,r12
    d8d0:	e9 90 04 00 00       	jmp    dd65 <zbtScoreInsertAt+0x16b5>
    d8d5:	49 8d 44 24 38       	lea    rax,[r12+0x38]
    d8da:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    d8de:	31 c0                	xor    eax,eax
    d8e0:	44 8b bd 68 ff ff ff 	mov    r15d,DWORD PTR [rbp-0x98]
    d8e7:	44 8b 75 c8          	mov    r14d,DWORD PTR [rbp-0x38]
    d8eb:	45 29 f7             	sub    r15d,r14d
    d8ee:	0f 93 c0             	setae  al
    d8f1:	89 45 c0             	mov    DWORD PTR [rbp-0x40],eax
    d8f4:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    d8f8:	45 29 f5             	sub    r13d,r14d
    d8fb:	41 ff c5             	inc    r13d
    d8fe:	31 db                	xor    ebx,ebx
    d900:	eb 1c                	jmp    d91e <zbtScoreInsertAt+0x126e>
    d902:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d909:	1f 84 00 00 00 00 00
    d910:	41 ff c6             	inc    r14d
    d913:	ff c3                	inc    ebx
    d915:	41 39 dd             	cmp    r13d,ebx
    d918:	0f 84 5d ff ff ff    	je     d87b <zbtScoreInsertAt+0x11cb>
    d91e:	41 39 df             	cmp    r15d,ebx
    d921:	74 ed                	je     d910 <zbtScoreInsertAt+0x1260>
    d923:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    d929:	48 85 c0             	test   rax,rax
    d92c:	74 57                	je     d985 <zbtScoreInsertAt+0x12d5>
    d92e:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    d934:	0f af c1             	imul   eax,ecx
    d937:	83 c0 07             	add    eax,0x7
    d93a:	c1 e8 03             	shr    eax,0x3
    d93d:	83 c0 09             	add    eax,0x9
    d940:	83 e0 fe             	and    eax,0xfffffffe
    d943:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    d949:	89 d9                	mov    ecx,ebx
    d94b:	74 10                	je     d95d <zbtScoreInsertAt+0x12ad>
    d94d:	44 89 f1             	mov    ecx,r14d
    d950:	2b 4d c8             	sub    ecx,DWORD PTR [rbp-0x38]
    d953:	41 0f b6 54 24 11    	movzx  edx,BYTE PTR [r12+0x11]
    d959:	f7 d1                	not    ecx
    d95b:	01 d1                	add    ecx,edx
    d95d:	48 03 45 b8          	add    rax,QWORD PTR [rbp-0x48]
    d961:	89 c9                	mov    ecx,ecx
    d963:	0f b7 04 48          	movzx  eax,WORD PTR [rax+rcx*2]
    d967:	49 8d 3c 04          	lea    rdi,[r12+rax*1]
    d96b:	41 0f b6 34 04       	movzx  esi,BYTE PTR [r12+rax*1]
    d970:	81 fe fe 00 00 00    	cmp    esi,0xfe
    d976:	74 1b                	je     d993 <zbtScoreInsertAt+0x12e3>
    d978:	81 fe ff 00 00 00    	cmp    esi,0xff
    d97e:	75 1e                	jne    d99e <zbtScoreInsertAt+0x12ee>
    d980:	8b 77 01             	mov    esi,DWORD PTR [rdi+0x1]
    d983:	eb 2d                	jmp    d9b2 <zbtScoreInsertAt+0x1302>
    d985:	31 c0                	xor    eax,eax
    d987:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    d98d:	89 d9                	mov    ecx,ebx
    d98f:	75 bc                	jne    d94d <zbtScoreInsertAt+0x129d>
    d991:	eb ca                	jmp    d95d <zbtScoreInsertAt+0x12ad>
    d993:	0f b7 77 01          	movzx  esi,WORD PTR [rdi+0x1]
    d997:	b8 03 00 00 00       	mov    eax,0x3
    d99c:	eb 05                	jmp    d9a3 <zbtScoreInsertAt+0x12f3>
    d99e:	b8 01 00 00 00       	mov    eax,0x1
    d9a3:	48 01 c7             	add    rdi,rax
    d9a6:	e8 35 3f 00 00       	call   118e0 <dictGenHashFunction>
    d9ab:	48 89 c6             	mov    rsi,rax
    d9ae:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d9b2:	41 8b 50 30          	mov    edx,DWORD PTR [r8+0x30]
    d9b6:	41 8b 4c 24 30       	mov    ecx,DWORD PTR [r12+0x30]
    d9bb:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    d9c2:	44 8b 45 c0          	mov    r8d,DWORD PTR [rbp-0x40]
    d9c6:	4c 8d 8d 58 ff ff ff 	lea    r9,[rbp-0xa8]
    d9cd:	e8 fe b7 ff ff       	call   91d0 <zbtIndexMove>
    d9d2:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d9d6:	85 c0                	test   eax,eax
    d9d8:	0f 85 32 ff ff ff    	jne    d910 <zbtScoreInsertAt+0x1260>
    d9de:	48 8d 3d 39 5c 00 00 	lea    rdi,[rip+0x5c39]        # 1361e <_IO_stdin_used+0x61e>
    d9e5:	be 7c 06 00 00       	mov    esi,0x67c
    d9ea:	48 8d 15 83 5e 00 00 	lea    rdx,[rip+0x5e83]        # 13874 <_IO_stdin_used+0x874>
    d9f1:	e8 aa 3c 00 00       	call   116a0 <standalone_panic>
    d9f6:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d9fa:	e9 11 ff ff ff       	jmp    d910 <zbtScoreInsertAt+0x1260>
    d9ff:	48 8d 04 80          	lea    rax,[rax+rax*4]
    da03:	48 8d 04 c5 e8 eb ff 	lea    rax,[rax*8-0x1418]
    da0a:	ff
    da0b:	48 01 e8             	add    rax,rbp
    da0e:	eb 10                	jmp    da20 <zbtScoreInsertAt+0x1370>
    da10:	48 01 f1             	add    rcx,rsi
    da13:	48 83 c0 28          	add    rax,0x28
    da17:	48 ff ca             	dec    rdx
    da1a:	0f 84 c7 f9 ff ff    	je     d3e7 <zbtScoreInsertAt+0xd37>
    da20:	be 15 00 00 00       	mov    esi,0x15
    da25:	48 83 38 00          	cmp    QWORD PTR [rax],0x0
    da29:	75 e5                	jne    da10 <zbtScoreInsertAt+0x1360>
    da2b:	48 8b 78 f0          	mov    rdi,QWORD PTR [rax-0x10]
    da2f:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    da36:	77 d8                	ja     da10 <zbtScoreInsertAt+0x1360>
    da38:	31 f6                	xor    esi,esi
    da3a:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    da41:	40 0f 93 c6          	setae  sil
    da45:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    da49:	48 ff c6             	inc    rsi
    da4c:	eb c2                	jmp    da10 <zbtScoreInsertAt+0x1360>
    da4e:	48 8d b5 58 ff ff ff 	lea    rsi,[rbp-0xa8]
    da55:	4c 89 df             	mov    rdi,r11
    da58:	4c 89 55 c0          	mov    QWORD PTR [rbp-0x40],r10
    da5c:	4c 89 5d 80          	mov    QWORD PTR [rbp-0x80],r11
    da60:	e8 3b 3d 00 00       	call   117a0 <zmalloc_usable>
    da65:	48 89 c7             	mov    rdi,rax
    da68:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    da6f:	48 8b 85 58 ff ff ff 	mov    rax,QWORD PTR [rbp-0xa8]
    da76:	48 8b 8d 78 ff ff ff 	mov    rcx,QWORD PTR [rbp-0x88]
    da7d:	48 01 41 68          	add    QWORD PTR [rcx+0x68],rax
    da81:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    da85:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    da88:	48 8b 55 80          	mov    rdx,QWORD PTR [rbp-0x80]
    da8c:	e8 8f 36 ff ff       	call   1120 <memcpy@plt>
    da91:	48 8b 95 70 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x90]
    da98:	48 8b 4d 80          	mov    rcx,QWORD PTR [rbp-0x80]
    da9c:	4c 8b 55 c0          	mov    r10,QWORD PTR [rbp-0x40]
    daa0:	4c 8b 45 98          	mov    r8,QWORD PTR [rbp-0x68]
    daa4:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    daa8:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    daac:	41 c6 06 ff          	mov    BYTE PTR [r14],0xff
    dab0:	8b 84 dd e0 eb ff ff 	mov    eax,DWORD PTR [rbp+rbx*8-0x1420]
    dab7:	41 89 46 01          	mov    DWORD PTR [r14+0x1],eax
    dabb:	49 89 4e 05          	mov    QWORD PTR [r14+0x5],rcx
    dabf:	49 89 56 0d          	mov    QWORD PTR [r14+0xd],rdx
    dac3:	4c 8b b4 dd f0 eb ff 	mov    r14,QWORD PTR [rbp+rbx*8-0x1410]
    daca:	ff
    dacb:	4d 85 f6             	test   r14,r14
    dace:	74 40                	je     db10 <zbtScoreInsertAt+0x1460>
    dad0:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    dad4:	74 32                	je     db08 <zbtScoreInsertAt+0x1458>
    dad6:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    dada:	48 8d 3d 3d 5b 00 00 	lea    rdi,[rip+0x5b3d]        # 1361e <_IO_stdin_used+0x61e>
    dae1:	48 8d 15 6e 5c 00 00 	lea    rdx,[rip+0x5c6e]        # 13756 <_IO_stdin_used+0x756>
    dae8:	be 45 02 00 00       	mov    esi,0x245
    daed:	4c 89 c3             	mov    rbx,r8
    daf0:	4c 89 55 c0          	mov    QWORD PTR [rbp-0x40],r10
    daf4:	e8 a7 3b 00 00       	call   116a0 <standalone_panic>
    daf9:	4c 8b 55 c0          	mov    r10,QWORD PTR [rbp-0x40]
    dafd:	49 89 d8             	mov    r8,rbx
    db00:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    db04:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    db08:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    db0f:	00
    db10:	4c 89 65 c0          	mov    QWORD PTR [rbp-0x40],r12
    db14:	41 c6 41 14 01       	mov    BYTE PTR [r9+0x14],0x1
    db19:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    db1d:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    db21:	45 88 61 11          	mov    BYTE PTR [r9+0x11],r12b
    db25:	4d 89 61 08          	mov    QWORD PTR [r9+0x8],r12
    db29:	41 88 79 13          	mov    BYTE PTR [r9+0x13],dil
    db2d:	4d 89 69 28          	mov    QWORD PTR [r9+0x28],r13
    db31:	45 88 41 34          	mov    BYTE PTR [r9+0x34],r8b
    db35:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    db39:	66 41 89 41 36       	mov    WORD PTR [r9+0x36],ax
    db3e:	48 8b 5d a8          	mov    rbx,QWORD PTR [rbp-0x58]
    db42:	48 89 df             	mov    rdi,rbx
    db45:	31 f6                	xor    esi,esi
    db47:	4c 89 d2             	mov    rdx,r10
    db4a:	4d 89 c6             	mov    r14,r8
    db4d:	e8 5e 35 ff ff       	call   10b0 <memset@plt>
    db52:	41 0f b6 cc          	movzx  ecx,r12b
    db56:	45 84 f6             	test   r14b,r14b
    db59:	0f 84 0d 01 00 00    	je     dc6c <zbtScoreInsertAt+0x15bc>
    db5f:	41 0f b6 d6          	movzx  edx,r14b
    db63:	89 d6                	mov    esi,edx
    db65:	0f af f1             	imul   esi,ecx
    db68:	83 c6 07             	add    esi,0x7
    db6b:	c1 ee 03             	shr    esi,0x3
    db6e:	83 c6 09             	add    esi,0x9
    db71:	83 e6 fe             	and    esi,0xfffffffe
    db74:	48 01 de             	add    rsi,rbx
    db77:	48 8d 3c 4e          	lea    rdi,[rsi+rcx*2]
    db7b:	0f b6 45 b0          	movzx  eax,BYTE PTR [rbp-0x50]
    db7f:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    db83:	45 0f b6 40 35       	movzx  r8d,BYTE PTR [r8+0x35]
    db88:	44 8d 49 ff          	lea    r9d,[rcx-0x1]
    db8c:	45 31 d2             	xor    r10d,r10d
    db8f:	eb 39                	jmp    dbca <zbtScoreInsertAt+0x151a>
    db91:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    db98:	0f 1f 84 00 00 00 00
    db9f:	00
    dba0:	66 89 0c 5e          	mov    WORD PTR [rsi+rbx*2],cx
    dba4:	42 0f b6 8c 15 e0 fe 	movzx  ecx,BYTE PTR [rbp+r10*1-0x120]
    dbab:	ff ff
    dbad:	88 0c 1f             	mov    BYTE PTR [rdi+rbx*1],cl
    dbb0:	49 ff c2             	inc    r10
    dbb3:	41 ff c9             	dec    r9d
    dbb6:	4c 39 55 b8          	cmp    QWORD PTR [rbp-0x48],r10
    dbba:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    dbc1:	00 00 80
    dbc4:	0f 84 87 01 00 00    	je     dd51 <zbtScoreInsertAt+0x16a1>
    dbca:	f3 42 0f 7e 84 d5 00 	movq   xmm0,QWORD PTR [rbp+r10*8-0x500]
    dbd1:	fb ff ff
    dbd4:	66 49 0f 7e c3       	movq   r11,xmm0
    dbd9:	4d 85 db             	test   r11,r11
    dbdc:	78 12                	js     dbf0 <zbtScoreInsertAt+0x1540>
    dbde:	4d 09 fb             	or     r11,r15
    dbe1:	eb 10                	jmp    dbf3 <zbtScoreInsertAt+0x1543>
    dbe3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    dbea:	84 00 00 00 00 00
    dbf0:	49 f7 d3             	not    r11
    dbf3:	4c 89 e9             	mov    rcx,r13
    dbf6:	4c 29 d9             	sub    rcx,r11
    dbf9:	4d 29 eb             	sub    r11,r13
    dbfc:	45 84 c0             	test   r8b,r8b
    dbff:	4c 0f 45 d9          	cmovne r11,rcx
    dc03:	44 89 cb             	mov    ebx,r9d
    dc06:	41 0f 44 da          	cmove  ebx,r10d
    dc0a:	89 c1                	mov    ecx,eax
    dc0c:	49 d3 eb             	shr    r11,cl
    dc0f:	49 89 df             	mov    r15,rbx
    dc12:	4c 0f af fa          	imul   r15,rdx
    dc16:	4d 89 fe             	mov    r14,r15
    dc19:	49 c1 ee 03          	shr    r14,0x3
    dc1d:	44 89 f9             	mov    ecx,r15d
    dc20:	80 e1 07             	and    cl,0x7
    dc23:	4d 89 dc             	mov    r12,r11
    dc26:	49 d3 e4             	shl    r12,cl
    dc29:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    dc2d:	4e 09 24 31          	or     QWORD PTR [rcx+r14*1],r12
    dc31:	41 83 e7 07          	and    r15d,0x7
    dc35:	74 19                	je     dc50 <zbtScoreInsertAt+0x15a0>
    dc37:	b9 40 00 00 00       	mov    ecx,0x40
    dc3c:	44 29 f9             	sub    ecx,r15d
    dc3f:	3b 4d c8             	cmp    ecx,DWORD PTR [rbp-0x38]
    dc42:	73 0c                	jae    dc50 <zbtScoreInsertAt+0x15a0>
    dc44:	49 d3 eb             	shr    r11,cl
    dc47:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    dc4b:	45 08 5c 0e 40       	or     BYTE PTR [r14+rcx*1+0x40],r11b
    dc50:	48 8b 4d c0          	mov    rcx,QWORD PTR [rbp-0x40]
    dc54:	4c 39 55 90          	cmp    QWORD PTR [rbp-0x70],r10
    dc58:	0f 84 42 ff ff ff    	je     dba0 <zbtScoreInsertAt+0x14f0>
    dc5e:	42 0f b7 8c 55 10 fe 	movzx  ecx,WORD PTR [rbp+r10*2-0x1f0]
    dc65:	ff ff
    dc67:	e9 34 ff ff ff       	jmp    dba0 <zbtScoreInsertAt+0x14f0>
    dc6c:	48 8d 04 4b          	lea    rax,[rbx+rcx*2]
    dc70:	48 8b 55 d0          	mov    rdx,QWORD PTR [rbp-0x30]
    dc74:	0f b6 52 35          	movzx  edx,BYTE PTR [rdx+0x35]
    dc78:	80 7d a4 00          	cmp    BYTE PTR [rbp-0x5c],0x0
    dc7c:	0f 84 95 00 00 00    	je     dd17 <zbtScoreInsertAt+0x1667>
    dc82:	48 8b 7d b8          	mov    rdi,QWORD PTR [rbp-0x48]
    dc86:	83 e7 fe             	and    edi,0xfffffffe
    dc89:	44 8d 41 fe          	lea    r8d,[rcx-0x2]
    dc8d:	45 31 c9             	xor    r9d,r9d
    dc90:	48 8b 5d a8          	mov    rbx,QWORD PTR [rbp-0x58]
    dc94:	4c 8b 75 90          	mov    r14,QWORD PTR [rbp-0x70]
    dc98:	4c 8b 7d c0          	mov    r15,QWORD PTR [rbp-0x40]
    dc9c:	eb 29                	jmp    dcc7 <zbtScoreInsertAt+0x1617>
    dc9e:	66 90                	xchg   ax,ax
    dca0:	84 d2                	test   dl,dl
    dca2:	45 89 c3             	mov    r11d,r8d
    dca5:	45 0f 44 d9          	cmove  r11d,r9d
    dca9:	66 46 89 14 5b       	mov    WORD PTR [rbx+r11*2],r10w
    dcae:	44 0f b6 94 35 e1 fe 	movzx  r10d,BYTE PTR [rbp+rsi*1-0x11f]
    dcb5:	ff ff
    dcb7:	46 88 14 18          	mov    BYTE PTR [rax+r11*1],r10b
    dcbb:	41 83 c0 fe          	add    r8d,0xfffffffe
    dcbf:	49 ff c1             	inc    r9
    dcc2:	49 39 f9             	cmp    r9,rdi
    dcc5:	74 4a                	je     dd11 <zbtScoreInsertAt+0x1661>
    dcc7:	4c 89 ce             	mov    rsi,r9
    dcca:	45 89 f9             	mov    r9d,r15d
    dccd:	49 39 f6             	cmp    r14,rsi
    dcd0:	74 09                	je     dcdb <zbtScoreInsertAt+0x162b>
    dcd2:	44 0f b7 8c 75 10 fe 	movzx  r9d,WORD PTR [rbp+rsi*2-0x1f0]
    dcd9:	ff ff
    dcdb:	45 8d 50 01          	lea    r10d,[r8+0x1]
    dcdf:	84 d2                	test   dl,dl
    dce1:	41 89 f3             	mov    r11d,esi
    dce4:	45 0f 45 da          	cmovne r11d,r10d
    dce8:	66 46 89 0c 5b       	mov    WORD PTR [rbx+r11*2],r9w
    dced:	44 0f b6 8c 35 e0 fe 	movzx  r9d,BYTE PTR [rbp+rsi*1-0x120]
    dcf4:	ff ff
    dcf6:	46 88 0c 18          	mov    BYTE PTR [rax+r11*1],r9b
    dcfa:	4c 8d 4e 01          	lea    r9,[rsi+0x1]
    dcfe:	45 89 fa             	mov    r10d,r15d
    dd01:	4d 39 f1             	cmp    r9,r14
    dd04:	74 9a                	je     dca0 <zbtScoreInsertAt+0x15f0>
    dd06:	44 0f b7 94 75 12 fe 	movzx  r10d,WORD PTR [rbp+rsi*2-0x1ee]
    dd0d:	ff ff
    dd0f:	eb 8f                	jmp    dca0 <zbtScoreInsertAt+0x15f0>
    dd11:	48 83 c6 02          	add    rsi,0x2
    dd15:	eb 06                	jmp    dd1d <zbtScoreInsertAt+0x166d>
    dd17:	31 f6                	xor    esi,esi
    dd19:	4c 8b 7d c0          	mov    r15,QWORD PTR [rbp-0x40]
    dd1d:	f6 45 b8 01          	test   BYTE PTR [rbp-0x48],0x1
    dd21:	74 2e                	je     dd51 <zbtScoreInsertAt+0x16a1>
    dd23:	48 3b 75 90          	cmp    rsi,QWORD PTR [rbp-0x70]
    dd27:	74 09                	je     dd32 <zbtScoreInsertAt+0x1682>
    dd29:	44 0f b7 bc 75 10 fe 	movzx  r15d,WORD PTR [rbp+rsi*2-0x1f0]
    dd30:	ff ff
    dd32:	89 f7                	mov    edi,esi
    dd34:	f7 d7                	not    edi
    dd36:	01 cf                	add    edi,ecx
    dd38:	84 d2                	test   dl,dl
    dd3a:	0f 44 fe             	cmove  edi,esi
    dd3d:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    dd41:	66 44 89 3c 79       	mov    WORD PTR [rcx+rdi*2],r15w
    dd46:	0f b6 8c 35 e0 fe ff 	movzx  ecx,BYTE PTR [rbp+rsi*1-0x120]
    dd4d:	ff
    dd4e:	88 0c 38             	mov    BYTE PTR [rax+rdi*1],cl
    dd51:	be 01 00 00 00       	mov    esi,0x1
    dd56:	48 8b 5d d0          	mov    rbx,QWORD PTR [rbp-0x30]
    dd5a:	48 89 df             	mov    rdi,rbx
    dd5d:	e8 0e 12 00 00       	call   ef70 <zbtScoreUpdatePath>
    dd62:	48 89 d8             	mov    rax,rbx
    dd65:	48 81 c4 18 14 00 00 	add    rsp,0x1418
    dd6c:	5b                   	pop    rbx
    dd6d:	41 5c                	pop    r12
    dd6f:	41 5d                	pop    r13
    dd71:	41 5e                	pop    r14
    dd73:	41 5f                	pop    r15
    dd75:	5d                   	pop    rbp
    dd76:	c3                   	ret
    dd77:	66 45 89 5e 01       	mov    WORD PTR [r14+0x1],r11w
    dd7c:	bf 03 00 00 00       	mov    edi,0x3
    dd81:	b0 fe                	mov    al,0xfe
    dd83:	4c 89 65 c0          	mov    QWORD PTR [rbp-0x40],r12
    dd87:	41 88 06             	mov    BYTE PTR [r14],al
    dd8a:	4c 01 f7             	add    rdi,r14
    dd8d:	4c 89 da             	mov    rdx,r11
    dd90:	e8 8b 33 ff ff       	call   1120 <memcpy@plt>
    dd95:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    dd99:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    dd9d:	4c 8b 45 98          	mov    r8,QWORD PTR [rbp-0x68]
    dda1:	49 89 da             	mov    r10,rbx
    dda4:	e9 70 fd ff ff       	jmp    db19 <zbtScoreInsertAt+0x1469>
    dda9:	49 8d 59 38          	lea    rbx,[r9+0x38]
    ddad:	4b 8d 34 61          	lea    rsi,[r9+r12*2]
    ddb1:	48 83 c6 38          	add    rsi,0x38
    ddb5:	48 8d bd d0 eb ff ff 	lea    rdi,[rbp-0x1430]
    ddbc:	4c 89 e2             	mov    rdx,r12
    ddbf:	e8 5c 33 ff ff       	call   1120 <memcpy@plt>
    ddc4:	48 89 de             	mov    rsi,rbx
    ddc7:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    ddcb:	45 89 f7             	mov    r15d,r14d
    ddce:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    ddd2:	48 8d 1c 08          	lea    rbx,[rax+rcx*1]
    ddd6:	48 8d 3c 08          	lea    rdi,[rax+rcx*1]
    ddda:	48 83 c7 38          	add    rdi,0x38
    ddde:	43 8d 14 24          	lea    edx,[r12+r12*1]
    dde2:	e8 79 33 ff ff       	call   1160 <memmove@plt>
    dde7:	4e 8d 2c 7b          	lea    r13,[rbx+r15*2]
    ddeb:	49 83 c5 38          	add    r13,0x38
    ddef:	4a 8d 3c 7b          	lea    rdi,[rbx+r15*2]
    ddf3:	48 83 c7 3a          	add    rdi,0x3a
    ddf7:	45 29 f4             	sub    r12d,r14d
    ddfa:	4b 8d 14 24          	lea    rdx,[r12+r12*1]
    ddfe:	4c 89 ee             	mov    rsi,r13
    de01:	e8 5a 33 ff ff       	call   1160 <memmove@plt>
    de06:	48 8b 45 90          	mov    rax,QWORD PTR [rbp-0x70]
    de0a:	4c 8d 34 43          	lea    r14,[rbx+rax*2]
    de0e:	49 83 c6 38          	add    r14,0x38
    de12:	48 8d b5 d0 eb ff ff 	lea    rsi,[rbp-0x1430]
    de19:	4c 89 f7             	mov    rdi,r14
    de1c:	4c 89 fa             	mov    rdx,r15
    de1f:	e8 fc 32 ff ff       	call   1120 <memcpy@plt>
    de24:	0f b6 45 c8          	movzx  eax,BYTE PTR [rbp-0x38]
    de28:	43 88 04 37          	mov    BYTE PTR [r15+r14*1],al
    de2c:	4b 8d 3c 37          	lea    rdi,[r15+r14*1]
    de30:	48 ff c7             	inc    rdi
    de33:	49 8d 34 2f          	lea    rsi,[r15+rbp*1]
    de37:	48 81 c6 d0 eb ff ff 	add    rsi,0xffffffffffffebd0
    de3e:	4c 89 e2             	mov    rdx,r12
    de41:	e8 da 32 ff ff       	call   1120 <memcpy@plt>
    de46:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    de4a:	0f b7 5f 36          	movzx  ebx,WORD PTR [rdi+0x36]
    de4e:	2b 5d c0             	sub    ebx,DWORD PTR [rbp-0x40]
    de51:	44 0f b7 f3          	movzx  r14d,bx
    de55:	49 01 fe             	add    r14,rdi
    de58:	4c 8b 65 80          	mov    r12,QWORD PTR [rbp-0x80]
    de5c:	4d 8b 3c 24          	mov    r15,QWORD PTR [r12]
    de60:	4d 85 ff             	test   r15,r15
    de63:	0f 85 6c 01 00 00    	jne    dfd5 <zbtScoreInsertAt+0x1925>
    de69:	48 8b 45 98          	mov    rax,QWORD PTR [rbp-0x68]
    de6d:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    de71:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    de78:	0f 87 17 01 00 00    	ja     df95 <zbtScoreInsertAt+0x18e5>
    de7e:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    de81:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    de88:	0f 87 cd 01 00 00    	ja     e05b <zbtScoreInsertAt+0x19ab>
    de8e:	bf 01 00 00 00       	mov    edi,0x1
    de93:	89 d0                	mov    eax,edx
    de95:	e9 cd 01 00 00       	jmp    e067 <zbtScoreInsertAt+0x19b7>
    de9a:	4c 0f af 45 b8       	imul   r8,QWORD PTR [rbp-0x48]
    de9f:	49 c7 c1 ff ff ff ff 	mov    r9,0xffffffffffffffff
    dea6:	eb 0d                	jmp    deb5 <zbtScoreInsertAt+0x1805>
    dea8:	49 29 d0             	sub    r8,rdx
    deab:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    deaf:	0f 84 81 f4 ff ff    	je     d336 <zbtScoreInsertAt+0xc86>
    deb5:	49 83 f8 40          	cmp    r8,0x40
    deb9:	ba 40 00 00 00       	mov    edx,0x40
    debe:	49 0f 42 d0          	cmovb  rdx,r8
    dec2:	49 8d 34 00          	lea    rsi,[r8+rax*1]
    dec6:	48 29 d6             	sub    rsi,rdx
    dec9:	49 89 f2             	mov    r10,rsi
    decc:	49 c1 ea 03          	shr    r10,0x3
    ded0:	89 f1                	mov    ecx,esi
    ded2:	83 e1 07             	and    ecx,0x7
    ded5:	bf 40 00 00 00       	mov    edi,0x40
    deda:	29 cf                	sub    edi,ecx
    dedc:	4f 8b 1c 16          	mov    r11,QWORD PTR [r14+r10*1]
    dee0:	89 f1                	mov    ecx,esi
    dee2:	80 e1 07             	and    cl,0x7
    dee5:	49 d3 eb             	shr    r11,cl
    dee8:	39 d7                	cmp    edi,edx
    deea:	73 0e                	jae    defa <zbtScoreInsertAt+0x184a>
    deec:	47 0f b6 54 16 08    	movzx  r10d,BYTE PTR [r14+r10*1+0x8]
    def2:	89 f9                	mov    ecx,edi
    def4:	49 d3 e2             	shl    r10,cl
    def7:	4d 09 d3             	or     r11,r10
    defa:	49 c7 c5 ff ff ff ff 	mov    r13,0xffffffffffffffff
    df01:	89 d1                	mov    ecx,edx
    df03:	49 d3 e5             	shl    r13,cl
    df06:	83 fa 40             	cmp    edx,0x40
    df09:	49 f7 d5             	not    r13
    df0c:	4d 0f 43 e9          	cmovae r13,r9
    df10:	4d 21 dd             	and    r13,r11
    df13:	48 03 75 b8          	add    rsi,QWORD PTR [rbp-0x48]
    df17:	49 89 f3             	mov    r11,rsi
    df1a:	49 c1 eb 03          	shr    r11,0x3
    df1e:	83 e6 07             	and    esi,0x7
    df21:	41 bc 40 00 00 00    	mov    r12d,0x40
    df27:	41 29 f4             	sub    r12d,esi
    df2a:	41 39 d4             	cmp    r12d,edx
    df2d:	89 d7                	mov    edi,edx
    df2f:	41 0f 42 fc          	cmovb  edi,r12d
    df33:	48 c7 c3 ff ff ff ff 	mov    rbx,0xffffffffffffffff
    df3a:	89 f9                	mov    ecx,edi
    df3c:	48 d3 e3             	shl    rbx,cl
    df3f:	83 ff 40             	cmp    edi,0x40
    df42:	48 f7 d3             	not    rbx
    df45:	49 0f 44 d9          	cmove  rbx,r9
    df49:	4d 89 ea             	mov    r10,r13
    df4c:	49 21 da             	and    r10,rbx
    df4f:	89 f1                	mov    ecx,esi
    df51:	48 d3 e3             	shl    rbx,cl
    df54:	48 f7 d3             	not    rbx
    df57:	4b 23 1c 1e          	and    rbx,QWORD PTR [r14+r11*1]
    df5b:	49 d3 e2             	shl    r10,cl
    df5e:	49 09 da             	or     r10,rbx
    df61:	4f 89 14 1e          	mov    QWORD PTR [r14+r11*1],r10
    df65:	41 39 d4             	cmp    r12d,edx
    df68:	0f 83 3a ff ff ff    	jae    dea8 <zbtScoreInsertAt+0x17f8>
    df6e:	89 d6                	mov    esi,edx
    df70:	29 fe                	sub    esi,edi
    df72:	47 0f b6 54 1e 08    	movzx  r10d,BYTE PTR [r14+r11*1+0x8]
    df78:	89 f9                	mov    ecx,edi
    df7a:	49 d3 ed             	shr    r13,cl
    df7d:	45 31 ea             	xor    r10d,r13d
    df80:	89 f1                	mov    ecx,esi
    df82:	41 d3 ea             	shr    r10d,cl
    df85:	41 d3 e2             	shl    r10d,cl
    df88:	45 31 ea             	xor    r10d,r13d
    df8b:	47 88 54 1e 08       	mov    BYTE PTR [r14+r11*1+0x8],r10b
    df90:	e9 13 ff ff ff       	jmp    dea8 <zbtScoreInsertAt+0x17f8>
    df95:	48 8d b5 00 fb ff ff 	lea    rsi,[rbp-0x500]
    df9c:	48 89 d7             	mov    rdi,rdx
    df9f:	49 89 c4             	mov    r12,rax
    dfa2:	e8 f9 37 00 00       	call   117a0 <zmalloc_usable>
    dfa7:	48 8b 8d 00 fb ff ff 	mov    rcx,QWORD PTR [rbp-0x500]
    dfae:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    dfb5:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    dfb9:	49 89 c7             	mov    r15,rax
    dfbc:	49 8b 34 24          	mov    rsi,QWORD PTR [r12]
    dfc0:	49 8b 54 24 08       	mov    rdx,QWORD PTR [r12+0x8]
    dfc5:	4c 8b 65 80          	mov    r12,QWORD PTR [rbp-0x80]
    dfc9:	48 89 c7             	mov    rdi,rax
    dfcc:	e8 4f 31 ff ff       	call   1120 <memcpy@plt>
    dfd1:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    dfd5:	48 8b 55 98          	mov    rdx,QWORD PTR [rbp-0x68]
    dfd9:	48 8b 42 08          	mov    rax,QWORD PTR [rdx+0x8]
    dfdd:	41 c6 06 ff          	mov    BYTE PTR [r14],0xff
    dfe1:	8b 4a 10             	mov    ecx,DWORD PTR [rdx+0x10]
    dfe4:	41 89 4e 01          	mov    DWORD PTR [r14+0x1],ecx
    dfe8:	49 89 46 05          	mov    QWORD PTR [r14+0x5],rax
    dfec:	4d 89 7e 0d          	mov    QWORD PTR [r14+0xd],r15
    dff0:	4c 8b 72 20          	mov    r14,QWORD PTR [rdx+0x20]
    dff4:	4d 85 f6             	test   r14,r14
    dff7:	74 2a                	je     e023 <zbtScoreInsertAt+0x1973>
    dff9:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    dffd:	74 1c                	je     e01b <zbtScoreInsertAt+0x196b>
    dfff:	48 8d 3d 18 56 00 00 	lea    rdi,[rip+0x5618]        # 1361e <_IO_stdin_used+0x61e>
    e006:	48 8d 15 49 57 00 00 	lea    rdx,[rip+0x5749]        # 13756 <_IO_stdin_used+0x756>
    e00d:	be 45 02 00 00       	mov    esi,0x245
    e012:	e8 89 36 00 00       	call   116a0 <standalone_panic>
    e017:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e01b:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    e022:	00
    e023:	66 0f ef c0          	pxor   xmm0,xmm0
    e027:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    e02d:	c6 47 14 01          	mov    BYTE PTR [rdi+0x14],0x1
    e031:	8b 45 a4             	mov    eax,DWORD PTR [rbp-0x5c]
    e034:	88 47 11             	mov    BYTE PTR [rdi+0x11],al
    e037:	48 8b 45 90          	mov    rax,QWORD PTR [rbp-0x70]
    e03b:	48 89 47 08          	mov    QWORD PTR [rdi+0x8],rax
    e03f:	66 89 5f 36          	mov    WORD PTR [rdi+0x36],bx
    e043:	66 41 89 5d 00       	mov    WORD PTR [r13+0x0],bx
    e048:	be 01 00 00 00       	mov    esi,0x1
    e04d:	e8 1e 0f 00 00       	call   ef70 <zbtScoreUpdatePath>
    e052:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    e056:	e9 0a fd ff ff       	jmp    dd65 <zbtScoreInsertAt+0x16b5>
    e05b:	66 41 89 56 01       	mov    WORD PTR [r14+0x1],dx
    e060:	bf 03 00 00 00       	mov    edi,0x3
    e065:	b0 fe                	mov    al,0xfe
    e067:	41 88 06             	mov    BYTE PTR [r14],al
    e06a:	4c 01 f7             	add    rdi,r14
    e06d:	e8 ae 30 ff ff       	call   1120 <memcpy@plt>
    e072:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e076:	eb b9                	jmp    e031 <zbtScoreInsertAt+0x1981>

Disassembly of section .fini:
