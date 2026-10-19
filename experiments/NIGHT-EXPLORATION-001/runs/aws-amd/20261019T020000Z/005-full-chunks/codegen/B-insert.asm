
scratch/amd-chunk-build/B/build/native/btree-bench:     file format elf64-x86-64


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
    c6bd:	48 81 ec 28 14 00 00 	sub    rsp,0x1428
    c6c4:	4d 89 cb             	mov    r11,r9
    c6c7:	89 cb                	mov    ebx,ecx
    c6c9:	49 89 f1             	mov    r9,rsi
    c6cc:	48 89 bd 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdi
    c6d3:	41 0f b6 43 13       	movzx  eax,BYTE PTR [r11+0x13]
    c6d8:	88 45 c0             	mov    BYTE PTR [rbp-0x40],al
    c6db:	44 0f b6 6e 11       	movzx  r13d,BYTE PTR [rsi+0x11]
    c6e0:	41 09 c8             	or     r8d,ecx
    c6e3:	74 30                	je     c715 <zbtScoreInsertAt+0x65>
    c6e5:	41 80 fd 60          	cmp    r13b,0x60
    c6e9:	75 2a                	jne    c715 <zbtScoreInsertAt+0x65>
    c6eb:	0f b6 4d c0          	movzx  ecx,BYTE PTR [rbp-0x40]
    c6ef:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    c6f6:	4c 89 ce             	mov    rsi,r9
    c6f9:	4c 89 da             	mov    rdx,r11
    c6fc:	41 89 d8             	mov    r8d,ebx
    c6ff:	48 81 c4 28 14 00 00 	add    rsp,0x1428
    c706:	5b                   	pop    rbx
    c707:	41 5c                	pop    r12
    c709:	41 5d                	pop    r13
    c70b:	41 5e                	pop    r14
    c70d:	41 5f                	pop    r15
    c70f:	5d                   	pop    rbp
    c710:	e9 7b 1b 00 00       	jmp    e290 <zbtScoreInsertEdgeLeaf>
    c715:	45 0f b6 e5          	movzx  r12d,r13b
    c719:	41 80 fd 5f          	cmp    r13b,0x5f
    c71d:	4c 89 c8             	mov    rax,r9
    c720:	4c 89 4d d0          	mov    QWORD PTR [rbp-0x30],r9
    c724:	4c 89 65 b0          	mov    QWORD PTR [rbp-0x50],r12
    c728:	4c 89 5d 98          	mov    QWORD PTR [rbp-0x68],r11
    c72c:	77 61                	ja     c78f <zbtScoreInsertAt+0xdf>
    c72e:	66 49 0f 7e c7       	movq   r15,xmm0
    c733:	4d 85 ff             	test   r15,r15
    c736:	78 27                	js     c75f <zbtScoreInsertAt+0xaf>
    c738:	48 b8 00 00 00 00 00 	movabs rax,0x8000000000000000
    c73f:	00 00 80
    c742:	49 09 c7             	or     r15,rax
    c745:	41 0f b6 41 35       	movzx  eax,BYTE PTR [r9+0x35]
    c74a:	49 8b 49 28          	mov    rcx,QWORD PTR [r9+0x28]
    c74e:	84 c0                	test   al,al
    c750:	74 1d                	je     c76f <zbtScoreInsertAt+0xbf>
    c752:	49 39 cf             	cmp    r15,rcx
    c755:	77 38                	ja     c78f <zbtScoreInsertAt+0xdf>
    c757:	4c 29 f9             	sub    rcx,r15
    c75a:	49 89 cf             	mov    r15,rcx
    c75d:	eb 15                	jmp    c774 <zbtScoreInsertAt+0xc4>
    c75f:	49 f7 d7             	not    r15
    c762:	41 0f b6 41 35       	movzx  eax,BYTE PTR [r9+0x35]
    c767:	49 8b 49 28          	mov    rcx,QWORD PTR [r9+0x28]
    c76b:	84 c0                	test   al,al
    c76d:	75 e3                	jne    c752 <zbtScoreInsertAt+0xa2>
    c76f:	49 29 cf             	sub    r15,rcx
    c772:	72 1b                	jb     c78f <zbtScoreInsertAt+0xdf>
    c774:	41 0f b6 49 13       	movzx  ecx,BYTE PTR [r9+0x13]
    c779:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
    c780:	48 d3 e6             	shl    rsi,cl
    c783:	48 f7 d6             	not    rsi
    c786:	49 85 f7             	test   r15,rsi
    c789:	0f 84 7a 06 00 00    	je     ce09 <zbtScoreInsertAt+0x759>
    c78f:	44 89 45 80          	mov    DWORD PTR [rbp-0x80],r8d
    c793:	89 9d 70 ff ff ff    	mov    DWORD PTR [rbp-0x90],ebx
    c799:	4d 8d 71 38          	lea    r14,[r9+0x38]
    c79d:	89 95 58 ff ff ff    	mov    DWORD PTR [rbp-0xa8],edx
    c7a3:	41 89 d2             	mov    r10d,edx
    c7a6:	49 8d 44 24 01       	lea    rax,[r12+0x1]
    c7ab:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    c7af:	4b 8d 04 92          	lea    rax,[r10+r10*4]
    c7b3:	48 89 85 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rax
    c7ba:	48 8d 04 c5 c0 eb ff 	lea    rax,[rax*8-0x1440]
    c7c1:	ff
    c7c2:	48 01 e8             	add    rax,rbp
    c7c5:	48 89 45 90          	mov    QWORD PTR [rbp-0x70],rax
    c7c9:	45 31 e4             	xor    r12d,r12d
    c7cc:	44 89 e9             	mov    ecx,r13d
    c7cf:	48 8d 9d c0 eb ff ff 	lea    rbx,[rbp-0x1440]
    c7d6:	44 88 6d a0          	mov    BYTE PTR [rbp-0x60],r13b
    c7da:	45 31 ff             	xor    r15d,r15d
    c7dd:	4c 89 75 a8          	mov    QWORD PTR [rbp-0x58],r14
    c7e1:	4c 89 55 88          	mov    QWORD PTR [rbp-0x78],r10
    c7e5:	66 0f d6 85 68 ff ff 	movq   QWORD PTR [rbp-0x98],xmm0
    c7ec:	ff
    c7ed:	eb 4f                	jmp    c83e <zbtScoreInsertAt+0x18e>
    c7ef:	90                   	nop
    c7f0:	66 42 0f d6 84 d5 f0 	movq   QWORD PTR [rbp+r10*8-0x510],xmm0
    c7f7:	fa ff ff
    c7fa:	49 8b 43 20          	mov    rax,QWORD PTR [r11+0x20]
    c7fe:	48 8b 55 90          	mov    rdx,QWORD PTR [rbp-0x70]
    c802:	48 89 42 20          	mov    QWORD PTR [rdx+0x20],rax
    c806:	41 0f 10 13          	movups xmm2,XMMWORD PTR [r11]
    c80a:	41 0f 10 4b 10       	movups xmm1,XMMWORD PTR [r11+0x10]
    c80f:	0f 11 4a 10          	movups XMMWORD PTR [rdx+0x10],xmm1
    c813:	0f 11 12             	movups XMMWORD PTR [rdx],xmm2
    c816:	0f b6 45 c0          	movzx  eax,BYTE PTR [rbp-0x40]
    c81a:	42 88 84 15 d0 fe ff 	mov    BYTE PTR [rbp+r10*1-0x130],al
    c821:	ff
    c822:	66 42 c7 84 55 00 fe 	mov    WORD PTR [rbp+r10*2-0x200],0x0
    c829:	ff ff 00 00
    c82d:	49 ff c4             	inc    r12
    c830:	48 83 c3 28          	add    rbx,0x28
    c834:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    c838:	0f 84 76 02 00 00    	je     cab4 <zbtScoreInsertAt+0x404>
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
    c90b:	4a 89 8c e5 f0 fa ff 	mov    QWORD PTR [rbp+r12*8-0x510],rcx
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
    c931:	44 89 7d c8          	mov    DWORD PTR [rbp-0x38],r15d
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
    c9d7:	4c 8b 55 88          	mov    r10,QWORD PTR [rbp-0x78]
    c9db:	44 8b 7d c8          	mov    r15d,DWORD PTR [rbp-0x38]
    c9df:	4c 01 f7             	add    rdi,r14
    c9e2:	89 d6                	mov    esi,edx
    c9e4:	44 01 ee             	add    esi,r13d
    c9e7:	41 80 79 35 00       	cmp    BYTE PTR [r9+0x35],0x0
    c9ec:	41 0f 44 f7          	cmove  esi,r15d
    c9f0:	48 8d 3c 57          	lea    rdi,[rdi+rdx*2]
    c9f4:	0f b6 3c 3e          	movzx  edi,BYTE PTR [rsi+rdi*1]
    c9f8:	42 88 bc 25 d0 fe ff 	mov    BYTE PTR [rbp+r12*1-0x130],dil
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
    ca1f:	66 42 89 84 65 00 fe 	mov    WORD PTR [rbp+r12*2-0x200],ax
    ca26:	ff ff
    ca28:	41 ff c7             	inc    r15d
    ca2b:	49 ff c4             	inc    r12
    ca2e:	48 83 c3 28          	add    rbx,0x28
    ca32:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    ca36:	0f 85 02 fe ff ff    	jne    c83e <zbtScoreInsertAt+0x18e>
    ca3c:	eb 76                	jmp    cab4 <zbtScoreInsertAt+0x404>
    ca3e:	48 8d 3d d9 6b 00 00 	lea    rdi,[rip+0x6bd9]        # 1361e <_IO_stdin_used+0x61e>
    ca45:	be 60 02 00 00       	mov    esi,0x260
    ca4a:	48 8d 15 f9 6c 00 00 	lea    rdx,[rip+0x6cf9]        # 1374a <_IO_stdin_used+0x74a>
    ca51:	e8 ba 53 00 00       	call   11e10 <standalone_panic>
    ca56:	f3 0f 7e 85 68 ff ff 	movq   xmm0,QWORD PTR [rbp-0x98]
    ca5d:	ff
    ca5e:	4c 8b 5d 98          	mov    r11,QWORD PTR [rbp-0x68]
    ca62:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    ca66:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    ca6a:	0f 84 22 ff ff ff    	je     c992 <zbtScoreInsertAt+0x2e2>
    ca70:	48 8d 3d a7 6b 00 00 	lea    rdi,[rip+0x6ba7]        # 1361e <_IO_stdin_used+0x61e>
    ca77:	be 40 02 00 00       	mov    esi,0x240
    ca7c:	48 8d 15 d3 6c 00 00 	lea    rdx,[rip+0x6cd3]        # 13756 <_IO_stdin_used+0x756>
    ca83:	e8 88 53 00 00       	call   11e10 <standalone_panic>
    ca88:	f3 0f 7e 85 68 ff ff 	movq   xmm0,QWORD PTR [rbp-0x98]
    ca8f:	ff
    ca90:	4c 8b 5d 98          	mov    r11,QWORD PTR [rbp-0x68]
    ca94:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    ca98:	41 0f b6 07          	movzx  eax,BYTE PTR [r15]
    ca9c:	49 8b 4f 05          	mov    rcx,QWORD PTR [r15+0x5]
    caa0:	48 89 4b 08          	mov    QWORD PTR [rbx+0x8],rcx
    caa4:	4c 89 33             	mov    QWORD PTR [rbx],r14
    caa7:	3c ff                	cmp    al,0xff
    caa9:	0f 85 cc fe ff ff    	jne    c97b <zbtScoreInsertAt+0x2cb>
    caaf:	e9 e9 fe ff ff       	jmp    c99d <zbtScoreInsertAt+0x2ed>
    cab4:	f3 0f 7e 8d f0 fa ff 	movq   xmm1,QWORD PTR [rbp-0x510]
    cabb:	ff
    cabc:	66 49 0f 7e cd       	movq   r13,xmm1
    cac1:	4d 85 ed             	test   r13,r13
    cac4:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    cacb:	00 00 80
    cace:	4c 89 e8             	mov    rax,r13
    cad1:	78 05                	js     cad8 <zbtScoreInsertAt+0x428>
    cad3:	4c 09 f8             	or     rax,r15
    cad6:	eb 03                	jmp    cadb <zbtScoreInsertAt+0x42b>
    cad8:	48 f7 d0             	not    rax
    cadb:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    cadf:	0f b6 5d a0          	movzx  ebx,BYTE PTR [rbp-0x60]
    cae3:	44 8b 75 80          	mov    r14d,DWORD PTR [rbp-0x80]
    cae7:	ba 38 00 00 00       	mov    edx,0x38
    caec:	84 db                	test   bl,bl
    caee:	0f 84 a4 00 00 00    	je     cb98 <zbtScoreInsertAt+0x4e8>
    caf4:	45 31 c0             	xor    r8d,r8d
    caf7:	48 89 c7             	mov    rdi,rax
    cafa:	31 c9                	xor    ecx,ecx
    cafc:	48 89 c6             	mov    rsi,rax
    caff:	eb 31                	jmp    cb32 <zbtScoreInsertAt+0x482>
    cb01:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    cb08:	0f 1f 84 00 00 00 00
    cb0f:	00
    cb10:	49 f7 d1             	not    r9
    cb13:	4d 89 ca             	mov    r10,r9
    cb16:	49 31 c2             	xor    r10,rax
    cb19:	4c 09 d1             	or     rcx,r10
    cb1c:	49 39 f9             	cmp    r9,rdi
    cb1f:	49 0f 42 f9          	cmovb  rdi,r9
    cb23:	49 39 f1             	cmp    r9,rsi
    cb26:	49 0f 47 f1          	cmova  rsi,r9
    cb2a:	49 ff c0             	inc    r8
    cb2d:	4d 39 c4             	cmp    r12,r8
    cb30:	74 19                	je     cb4b <zbtScoreInsertAt+0x49b>
    cb32:	f3 42 0f 7e 8c c5 f8 	movq   xmm1,QWORD PTR [rbp+r8*8-0x508]
    cb39:	fa ff ff
    cb3c:	66 49 0f 7e c9       	movq   r9,xmm1
    cb41:	4d 85 c9             	test   r9,r9
    cb44:	78 ca                	js     cb10 <zbtScoreInsertAt+0x460>
    cb46:	4d 09 f9             	or     r9,r15
    cb49:	eb c8                	jmp    cb13 <zbtScoreInsertAt+0x463>
    cb4b:	48 85 c9             	test   rcx,rcx
    cb4e:	74 44                	je     cb94 <zbtScoreInsertAt+0x4e4>
    cb50:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    cb55:	48 29 fe             	sub    rsi,rdi
    cb58:	48 d3 ee             	shr    rsi,cl
    cb5b:	48 85 f6             	test   rsi,rsi
    cb5e:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    cb62:	74 34                	je     cb98 <zbtScoreInsertAt+0x4e8>
    cb64:	48 0f bd c6          	bsr    rax,rsi
    cb68:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    cb6c:	48 83 c0 41          	add    rax,0x41
    cb70:	48 0f af 45 b8       	imul   rax,QWORD PTR [rbp-0x48]
    cb75:	48 83 c0 07          	add    rax,0x7
    cb79:	48 c1 e8 03          	shr    rax,0x3
    cb7d:	48 83 c0 09          	add    rax,0x9
    cb81:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    cb88:	ff ff 1f
    cb8b:	48 21 c2             	and    rdx,rax
    cb8e:	48 83 c2 38          	add    rdx,0x38
    cb92:	eb 04                	jmp    cb98 <zbtScoreInsertAt+0x4e8>
    cb94:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    cb98:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    cb9c:	48 8d 04 40          	lea    rax,[rax+rax*2]
    cba0:	48 01 c2             	add    rdx,rax
    cba3:	4b 8d 0c a4          	lea    rcx,[r12+r12*4]
    cba7:	48 8d 0c cd 28 00 00 	lea    rcx,[rcx*8+0x28]
    cbae:	00
    cbaf:	31 f6                	xor    esi,esi
    cbb1:	eb 19                	jmp    cbcc <zbtScoreInsertAt+0x51c>
    cbb3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    cbba:	84 00 00 00 00 00
    cbc0:	48 01 fa             	add    rdx,rdi
    cbc3:	48 83 c6 28          	add    rsi,0x28
    cbc7:	48 39 f1             	cmp    rcx,rsi
    cbca:	74 37                	je     cc03 <zbtScoreInsertAt+0x553>
    cbcc:	bf 15 00 00 00       	mov    edi,0x15
    cbd1:	48 83 bc 35 d8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1428],0x0
    cbd8:	ff 00
    cbda:	75 e4                	jne    cbc0 <zbtScoreInsertAt+0x510>
    cbdc:	4c 8b 84 35 c8 eb ff 	mov    r8,QWORD PTR [rbp+rsi*1-0x1438]
    cbe3:	ff
    cbe4:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    cbeb:	77 d3                	ja     cbc0 <zbtScoreInsertAt+0x510>
    cbed:	31 ff                	xor    edi,edi
    cbef:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    cbf6:	40 0f 93 c7          	setae  dil
    cbfa:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    cbfe:	48 ff c7             	inc    rdi
    cc01:	eb bd                	jmp    cbc0 <zbtScoreInsertAt+0x510>
    cc03:	45 85 f6             	test   r14d,r14d
    cc06:	74 2b                	je     cc33 <zbtScoreInsertAt+0x583>
    cc08:	48 81 fa 00 10 00 00 	cmp    rdx,0x1000
    cc0f:	72 22                	jb     cc33 <zbtScoreInsertAt+0x583>
    cc11:	0f b6 4d c0          	movzx  ecx,BYTE PTR [rbp-0x40]
    cc15:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    cc1c:	4c 89 ce             	mov    rsi,r9
    cc1f:	4c 89 da             	mov    rdx,r11
    cc22:	44 8b 85 70 ff ff ff 	mov    r8d,DWORD PTR [rbp-0x90]
    cc29:	e8 62 16 00 00       	call   e290 <zbtScoreInsertEdgeLeaf>
    cc2e:	e9 c2 11 00 00       	jmp    ddf5 <zbtScoreInsertAt+0x1745>
    cc33:	80 fb 5f             	cmp    bl,0x5f
    cc36:	77 77                	ja     ccaf <zbtScoreInsertAt+0x5ff>
    cc38:	48 81 fa 00 10 00 00 	cmp    rdx,0x1000
    cc3f:	73 6e                	jae    ccaf <zbtScoreInsertAt+0x5ff>
    cc41:	4d 85 ed             	test   r13,r13
    cc44:	0f 88 6e 03 00 00    	js     cfb8 <zbtScoreInsertAt+0x908>
    cc4a:	4d 09 fd             	or     r13,r15
    cc4d:	84 db                	test   bl,bl
    cc4f:	0f 84 6e 03 00 00    	je     cfc3 <zbtScoreInsertAt+0x913>
    cc55:	41 0f b6 79 35       	movzx  edi,BYTE PTR [r9+0x35]
    cc5a:	45 31 c0             	xor    r8d,r8d
    cc5d:	4c 89 e9             	mov    rcx,r13
    cc60:	31 f6                	xor    esi,esi
    cc62:	4c 89 ea             	mov    rdx,r13
    cc65:	48 8b 9d 60 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xa0]
    cc6c:	eb 28                	jmp    cc96 <zbtScoreInsertAt+0x5e6>
    cc6e:	66 90                	xchg   ax,ax
    cc70:	49 f7 d1             	not    r9
    cc73:	4d 89 ca             	mov    r10,r9
    cc76:	4d 31 ea             	xor    r10,r13
    cc79:	4c 09 d6             	or     rsi,r10
    cc7c:	49 39 c9             	cmp    r9,rcx
    cc7f:	49 0f 42 c9          	cmovb  rcx,r9
    cc83:	49 39 d1             	cmp    r9,rdx
    cc86:	49 0f 47 d1          	cmova  rdx,r9
    cc8a:	49 ff c0             	inc    r8
    cc8d:	4d 39 c4             	cmp    r12,r8
    cc90:	0f 84 15 01 00 00    	je     cdab <zbtScoreInsertAt+0x6fb>
    cc96:	f3 42 0f 7e 84 c5 f8 	movq   xmm0,QWORD PTR [rbp+r8*8-0x508]
    cc9d:	fa ff ff
    cca0:	66 49 0f 7e c1       	movq   r9,xmm0
    cca5:	4d 85 c9             	test   r9,r9
    cca8:	78 c6                	js     cc70 <zbtScoreInsertAt+0x5c0>
    ccaa:	4d 09 f9             	or     r9,r15
    ccad:	eb c4                	jmp    cc73 <zbtScoreInsertAt+0x5c3>
    ccaf:	31 d2                	xor    edx,edx
    ccb1:	31 c0                	xor    eax,eax
    ccb3:	eb 1b                	jmp    ccd0 <zbtScoreInsertAt+0x620>
    ccb5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    ccbc:	00 00 00 00
    ccc0:	48 01 f0             	add    rax,rsi
    ccc3:	48 83 c0 0b          	add    rax,0xb
    ccc7:	48 83 c2 28          	add    rdx,0x28
    cccb:	48 39 d1             	cmp    rcx,rdx
    ccce:	74 37                	je     cd07 <zbtScoreInsertAt+0x657>
    ccd0:	be 15 00 00 00       	mov    esi,0x15
    ccd5:	48 83 bc 15 d8 eb ff 	cmp    QWORD PTR [rbp+rdx*1-0x1428],0x0
    ccdc:	ff 00
    ccde:	75 e0                	jne    ccc0 <zbtScoreInsertAt+0x610>
    cce0:	48 8b bc 15 c8 eb ff 	mov    rdi,QWORD PTR [rbp+rdx*1-0x1438]
    cce7:	ff
    cce8:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    ccef:	77 cf                	ja     ccc0 <zbtScoreInsertAt+0x610>
    ccf1:	31 f6                	xor    esi,esi
    ccf3:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    ccfa:	40 0f 93 c6          	setae  sil
    ccfe:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    cd02:	48 ff c6             	inc    rsi
    cd05:	eb b9                	jmp    ccc0 <zbtScoreInsertAt+0x610>
    cd07:	84 db                	test   bl,bl
    cd09:	0f 84 45 01 00 00    	je     ce54 <zbtScoreInsertAt+0x7a4>
    cd0f:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cd13:	d1 e9                	shr    ecx,1
    cd15:	42 8d 14 e5 00 00 00 	lea    edx,[r12*8+0x0]
    cd1c:	00
    cd1d:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    cd21:	c7 45 c0 01 00 00 00 	mov    DWORD PTR [rbp-0x40],0x1
    cd28:	31 f6                	xor    esi,esi
    cd2a:	31 ff                	xor    edi,edi
    cd2c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    cd30:	41 b8 15 00 00 00    	mov    r8d,0x15
    cd36:	48 83 bc 35 d8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1428],0x0
    cd3d:	ff 00
    cd3f:	75 2f                	jne    cd70 <zbtScoreInsertAt+0x6c0>
    cd41:	4c 8b 8c 35 c8 eb ff 	mov    r9,QWORD PTR [rbp+rsi*1-0x1438]
    cd48:	ff
    cd49:	49 81 f9 3f 01 00 00 	cmp    r9,0x13f
    cd50:	77 1e                	ja     cd70 <zbtScoreInsertAt+0x6c0>
    cd52:	45 31 c0             	xor    r8d,r8d
    cd55:	49 81 f9 fe 00 00 00 	cmp    r9,0xfe
    cd5c:	41 0f 93 c0          	setae  r8b
    cd60:	4f 8d 04 41          	lea    r8,[r9+r8*2]
    cd64:	49 ff c0             	inc    r8
    cd67:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    cd6e:	00 00
    cd70:	4e 8d 0c 07          	lea    r9,[rdi+r8*1]
    cd74:	4e 8d 0c 4d 16 00 00 	lea    r9,[r9*2+0x16]
    cd7b:	00
    cd7c:	49 39 c1             	cmp    r9,rax
    cd7f:	73 16                	jae    cd97 <zbtScoreInsertAt+0x6e7>
    cd81:	4c 01 c7             	add    rdi,r8
    cd84:	48 83 c7 0b          	add    rdi,0xb
    cd88:	ff 45 c0             	inc    DWORD PTR [rbp-0x40]
    cd8b:	48 83 c6 28          	add    rsi,0x28
    cd8f:	48 39 f2             	cmp    rdx,rsi
    cd92:	75 9c                	jne    cd30 <zbtScoreInsertAt+0x680>
    cd94:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    cd97:	4c 89 e9             	mov    rcx,r13
    cd9a:	4d 85 ed             	test   r13,r13
    cd9d:	0f 88 c4 00 00 00    	js     ce67 <zbtScoreInsertAt+0x7b7>
    cda3:	4c 09 f9             	or     rcx,r15
    cda6:	e9 bf 00 00 00       	jmp    ce6a <zbtScoreInsertAt+0x7ba>
    cdab:	40 84 ff             	test   dil,dil
    cdae:	49 89 d5             	mov    r13,rdx
    cdb1:	4c 0f 44 e9          	cmove  r13,rcx
    cdb5:	48 85 f6             	test   rsi,rsi
    cdb8:	0f 84 af 02 00 00    	je     d06d <zbtScoreInsertAt+0x9bd>
    cdbe:	f3 48 0f bc fe       	tzcnt  rdi,rsi
    cdc3:	48 29 ca             	sub    rdx,rcx
    cdc6:	89 f9                	mov    ecx,edi
    cdc8:	48 d3 ea             	shr    rdx,cl
    cdcb:	48 85 d2             	test   rdx,rdx
    cdce:	0f 84 66 03 00 00    	je     d13a <zbtScoreInsertAt+0xa8a>
    cdd4:	48 0f bd ca          	bsr    rcx,rdx
    cdd8:	83 f1 3f             	xor    ecx,0x3f
    cddb:	41 b0 40             	mov    r8b,0x40
    cdde:	41 28 c8             	sub    r8b,cl
    cde1:	41 0f b6 d0          	movzx  edx,r8b
    cde5:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cde9:	41 89 ca             	mov    r10d,ecx
    cdec:	48 89 55 c0          	mov    QWORD PTR [rbp-0x40],rdx
    cdf0:	44 0f af d2          	imul   r10d,edx
    cdf4:	41 83 c2 07          	add    r10d,0x7
    cdf8:	41 c1 ea 03          	shr    r10d,0x3
    cdfc:	41 83 c2 09          	add    r10d,0x9
    ce00:	41 83 e2 fe          	and    r10d,0xfffffffe
    ce04:	e9 3d 03 00 00       	jmp    d146 <zbtScoreInsertAt+0xa96>
    ce09:	49 d3 ef             	shr    r15,cl
    ce0c:	41 0f b6 49 34       	movzx  ecx,BYTE PTR [r9+0x34]
    ce11:	48 85 c9             	test   rcx,rcx
    ce14:	0f 84 2f 04 00 00    	je     d249 <zbtScoreInsertAt+0xb99>
    ce1a:	4c 89 fe             	mov    rsi,r15
    ce1d:	48 d3 ee             	shr    rsi,cl
    ce20:	80 f9 3f             	cmp    cl,0x3f
    ce23:	77 09                	ja     ce2e <zbtScoreInsertAt+0x77e>
    ce25:	48 85 f6             	test   rsi,rsi
    ce28:	0f 85 61 f9 ff ff    	jne    c78f <zbtScoreInsertAt+0xdf>
    ce2e:	45 8d 54 24 01       	lea    r10d,[r12+0x1]
    ce33:	89 ce                	mov    esi,ecx
    ce35:	41 0f af f2          	imul   esi,r10d
    ce39:	83 c6 07             	add    esi,0x7
    ce3c:	c1 ee 03             	shr    esi,0x3
    ce3f:	83 c6 09             	add    esi,0x9
    ce42:	81 e6 fe ff 00 00    	and    esi,0xfffe
    ce48:	48 89 75 c8          	mov    QWORD PTR [rbp-0x38],rsi
    ce4c:	41 89 ce             	mov    r14d,ecx
    ce4f:	e9 0c 04 00 00       	jmp    d260 <zbtScoreInsertAt+0xbb0>
    ce54:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    ce5b:	4c 89 e9             	mov    rcx,r13
    ce5e:	4d 85 ed             	test   r13,r13
    ce61:	0f 89 3c ff ff ff    	jns    cda3 <zbtScoreInsertAt+0x6f3>
    ce67:	48 f7 d1             	not    rcx
    ce6a:	8b 75 c0             	mov    esi,DWORD PTR [rbp-0x40]
    ce6d:	89 f0                	mov    eax,esi
    ce6f:	ba 38 00 00 00       	mov    edx,0x38
    ce74:	83 fe 02             	cmp    esi,0x2
    ce77:	0f 82 90 00 00 00    	jb     cf0d <zbtScoreInsertAt+0x85d>
    ce7d:	41 b9 01 00 00 00    	mov    r9d,0x1
    ce83:	31 ff                	xor    edi,edi
    ce85:	49 89 c8             	mov    r8,rcx
    ce88:	48 89 ce             	mov    rsi,rcx
    ce8b:	eb 25                	jmp    ceb2 <zbtScoreInsertAt+0x802>
    ce8d:	0f 1f 00             	nop    DWORD PTR [rax]
    ce90:	4d 09 fa             	or     r10,r15
    ce93:	4d 89 d3             	mov    r11,r10
    ce96:	49 31 cb             	xor    r11,rcx
    ce99:	4c 09 df             	or     rdi,r11
    ce9c:	4d 39 c2             	cmp    r10,r8
    ce9f:	4d 0f 42 c2          	cmovb  r8,r10
    cea3:	49 39 f2             	cmp    r10,rsi
    cea6:	49 0f 47 f2          	cmova  rsi,r10
    ceaa:	49 ff c1             	inc    r9
    cead:	4c 39 c8             	cmp    rax,r9
    ceb0:	74 19                	je     cecb <zbtScoreInsertAt+0x81b>
    ceb2:	f3 42 0f 7e 84 cd f0 	movq   xmm0,QWORD PTR [rbp+r9*8-0x510]
    ceb9:	fa ff ff
    cebc:	66 49 0f 7e c2       	movq   r10,xmm0
    cec1:	4d 85 d2             	test   r10,r10
    cec4:	79 ca                	jns    ce90 <zbtScoreInsertAt+0x7e0>
    cec6:	49 f7 d2             	not    r10
    cec9:	eb c8                	jmp    ce93 <zbtScoreInsertAt+0x7e3>
    cecb:	48 85 ff             	test   rdi,rdi
    cece:	74 3d                	je     cf0d <zbtScoreInsertAt+0x85d>
    ced0:	f3 48 0f bc cf       	tzcnt  rcx,rdi
    ced5:	4c 29 c6             	sub    rsi,r8
    ced8:	48 d3 ee             	shr    rsi,cl
    cedb:	48 85 f6             	test   rsi,rsi
    cede:	74 2d                	je     cf0d <zbtScoreInsertAt+0x85d>
    cee0:	48 0f bd ce          	bsr    rcx,rsi
    cee4:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    cee8:	48 83 c1 41          	add    rcx,0x41
    ceec:	48 0f af c8          	imul   rcx,rax
    cef0:	48 83 c1 07          	add    rcx,0x7
    cef4:	48 c1 e9 03          	shr    rcx,0x3
    cef8:	48 83 c1 09          	add    rcx,0x9
    cefc:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    cf03:	ff ff 1f
    cf06:	48 21 ca             	and    rdx,rcx
    cf09:	48 83 c2 38          	add    rdx,0x38
    cf0d:	48 8d 0c 40          	lea    rcx,[rax+rax*2]
    cf11:	48 01 d1             	add    rcx,rdx
    cf14:	83 7d c0 00          	cmp    DWORD PTR [rbp-0x40],0x0
    cf18:	74 59                	je     cf73 <zbtScoreInsertAt+0x8c3>
    cf1a:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
    cf21:	00
    cf22:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    cf26:	31 f6                	xor    esi,esi
    cf28:	eb 12                	jmp    cf3c <zbtScoreInsertAt+0x88c>
    cf2a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    cf30:	48 01 f9             	add    rcx,rdi
    cf33:	48 83 c6 28          	add    rsi,0x28
    cf37:	48 39 f2             	cmp    rdx,rsi
    cf3a:	74 37                	je     cf73 <zbtScoreInsertAt+0x8c3>
    cf3c:	bf 15 00 00 00       	mov    edi,0x15
    cf41:	48 83 bc 35 d8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1428],0x0
    cf48:	ff 00
    cf4a:	75 e4                	jne    cf30 <zbtScoreInsertAt+0x880>
    cf4c:	4c 8b 84 35 c8 eb ff 	mov    r8,QWORD PTR [rbp+rsi*1-0x1438]
    cf53:	ff
    cf54:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    cf5b:	77 d3                	ja     cf30 <zbtScoreInsertAt+0x880>
    cf5d:	31 ff                	xor    edi,edi
    cf5f:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    cf66:	40 0f 93 c7          	setae  dil
    cf6a:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    cf6e:	48 ff c7             	inc    rdi
    cf71:	eb bd                	jmp    cf30 <zbtScoreInsertAt+0x880>
    cf73:	48 81 f9 ff 0f 00 00 	cmp    rcx,0xfff
    cf7a:	0f 87 f8 04 00 00    	ja     d478 <zbtScoreInsertAt+0xdc8>
    cf80:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cf84:	89 cf                	mov    edi,ecx
    cf86:	2b 7d c0             	sub    edi,DWORD PTR [rbp-0x40]
    cf89:	f3 0f 7e 84 c5 f0 fa 	movq   xmm0,QWORD PTR [rbp+rax*8-0x510]
    cf90:	ff ff
    cf92:	66 48 0f 7e c1       	movq   rcx,xmm0
    cf97:	48 85 c9             	test   rcx,rcx
    cf9a:	0f 88 da 00 00 00    	js     d07a <zbtScoreInsertAt+0x9ca>
    cfa0:	4c 09 f9             	or     rcx,r15
    cfa3:	89 fa                	mov    edx,edi
    cfa5:	be 38 00 00 00       	mov    esi,0x38
    cfaa:	83 ff 02             	cmp    edi,0x2
    cfad:	0f 83 da 00 00 00    	jae    d08d <zbtScoreInsertAt+0x9dd>
    cfb3:	e9 a0 04 00 00       	jmp    d458 <zbtScoreInsertAt+0xda8>
    cfb8:	49 f7 d5             	not    r13
    cfbb:	84 db                	test   bl,bl
    cfbd:	0f 85 92 fc ff ff    	jne    cc55 <zbtScoreInsertAt+0x5a5>
    cfc3:	31 c9                	xor    ecx,ecx
    cfc5:	48 89 4d c0          	mov    QWORD PTR [rbp-0x40],rcx
    cfc9:	31 ff                	xor    edi,edi
    cfcb:	45 31 c0             	xor    r8d,r8d
    cfce:	45 31 d2             	xor    r10d,r10d
    cfd1:	48 8b 9d 60 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xa0]
    cfd8:	4c 01 d0             	add    rax,r10
    cfdb:	48 83 c0 38          	add    rax,0x38
    cfdf:	48 8b 94 dd d8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1428]
    cfe6:	ff
    cfe7:	48 85 d2             	test   rdx,rdx
    cfea:	0f 85 72 01 00 00    	jne    d162 <zbtScoreInsertAt+0xab2>
    cff0:	4c 8b 9c dd c8 eb ff 	mov    r11,QWORD PTR [rbp+rbx*8-0x1438]
    cff7:	ff
    cff8:	31 c9                	xor    ecx,ecx
    cffa:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    d001:	0f 93 c1             	setae  cl
    d004:	49 81 fb 40 01 00 00 	cmp    r11,0x140
    d00b:	49 8d 54 4b 01       	lea    rdx,[r11+rcx*2+0x1]
    d010:	b9 15 00 00 00       	mov    ecx,0x15
    d015:	48 0f 42 ca          	cmovb  rcx,rdx
    d019:	48 01 c8             	add    rax,rcx
    d01c:	45 0f b7 61 36       	movzx  r12d,WORD PTR [r9+0x36]
    d021:	4c 39 e0             	cmp    rax,r12
    d024:	0f 87 4a 01 00 00    	ja     d174 <zbtScoreInsertAt+0xac4>
    d02a:	41 29 cc             	sub    r12d,ecx
    d02d:	45 0f b7 f4          	movzx  r14d,r12w
    d031:	4d 01 ce             	add    r14,r9
    d034:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    d03b:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    d03f:	4c 89 45 98          	mov    QWORD PTR [rbp-0x68],r8
    d043:	0f 87 95 0a 00 00    	ja     dade <zbtScoreInsertAt+0x142e>
    d049:	48 8b 45 90          	mov    rax,QWORD PTR [rbp-0x70]
    d04d:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    d050:	4c 89 d3             	mov    rbx,r10
    d053:	49 81 fb fd 00 00 00 	cmp    r11,0xfd
    d05a:	0f 87 a7 0d 00 00    	ja     de07 <zbtScoreInsertAt+0x1757>
    d060:	bf 01 00 00 00       	mov    edi,0x1
    d065:	44 89 d8             	mov    eax,r11d
    d068:	e9 a6 0d 00 00       	jmp    de13 <zbtScoreInsertAt+0x1763>
    d06d:	31 c9                	xor    ecx,ecx
    d06f:	48 89 4d c0          	mov    QWORD PTR [rbp-0x40],rcx
    d073:	31 ff                	xor    edi,edi
    d075:	e9 c6 00 00 00       	jmp    d140 <zbtScoreInsertAt+0xa90>
    d07a:	48 f7 d1             	not    rcx
    d07d:	89 fa                	mov    edx,edi
    d07f:	be 38 00 00 00       	mov    esi,0x38
    d084:	83 ff 02             	cmp    edi,0x2
    d087:	0f 82 cb 03 00 00    	jb     d458 <zbtScoreInsertAt+0xda8>
    d08d:	4c 8d 14 c5 f0 fa ff 	lea    r10,[rax*8-0x510]
    d094:	ff
    d095:	49 01 ea             	add    r10,rbp
    d098:	41 bb 01 00 00 00    	mov    r11d,0x1
    d09e:	45 31 c0             	xor    r8d,r8d
    d0a1:	49 89 c9             	mov    r9,rcx
    d0a4:	48 89 cf             	mov    rdi,rcx
    d0a7:	eb 29                	jmp    d0d2 <zbtScoreInsertAt+0xa22>
    d0a9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    d0b0:	4c 09 fb             	or     rbx,r15
    d0b3:	49 89 de             	mov    r14,rbx
    d0b6:	49 31 ce             	xor    r14,rcx
    d0b9:	4d 09 f0             	or     r8,r14
    d0bc:	4c 39 cb             	cmp    rbx,r9
    d0bf:	4c 0f 42 cb          	cmovb  r9,rbx
    d0c3:	48 39 fb             	cmp    rbx,rdi
    d0c6:	48 0f 47 fb          	cmova  rdi,rbx
    d0ca:	49 ff c3             	inc    r11
    d0cd:	4c 39 da             	cmp    rdx,r11
    d0d0:	74 15                	je     d0e7 <zbtScoreInsertAt+0xa37>
    d0d2:	f3 43 0f 7e 04 da    	movq   xmm0,QWORD PTR [r10+r11*8]
    d0d8:	66 48 0f 7e c3       	movq   rbx,xmm0
    d0dd:	48 85 db             	test   rbx,rbx
    d0e0:	79 ce                	jns    d0b0 <zbtScoreInsertAt+0xa00>
    d0e2:	48 f7 d3             	not    rbx
    d0e5:	eb cc                	jmp    d0b3 <zbtScoreInsertAt+0xa03>
    d0e7:	4d 85 c0             	test   r8,r8
    d0ea:	0f 84 64 03 00 00    	je     d454 <zbtScoreInsertAt+0xda4>
    d0f0:	f3 49 0f bc c8       	tzcnt  rcx,r8
    d0f5:	4c 29 cf             	sub    rdi,r9
    d0f8:	48 d3 ef             	shr    rdi,cl
    d0fb:	48 85 ff             	test   rdi,rdi
    d0fe:	0f b6 5d a0          	movzx  ebx,BYTE PTR [rbp-0x60]
    d102:	0f 84 50 03 00 00    	je     d458 <zbtScoreInsertAt+0xda8>
    d108:	48 0f bd cf          	bsr    rcx,rdi
    d10c:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    d110:	48 83 c1 41          	add    rcx,0x41
    d114:	48 0f af ca          	imul   rcx,rdx
    d118:	48 83 c1 07          	add    rcx,0x7
    d11c:	48 c1 e9 03          	shr    rcx,0x3
    d120:	48 83 c1 09          	add    rcx,0x9
    d124:	48 be fe ff ff ff ff 	movabs rsi,0x1ffffffffffffffe
    d12b:	ff ff 1f
    d12e:	48 21 ce             	and    rsi,rcx
    d131:	48 83 c6 38          	add    rsi,0x38
    d135:	e9 1e 03 00 00       	jmp    d458 <zbtScoreInsertAt+0xda8>
    d13a:	31 c9                	xor    ecx,ecx
    d13c:	48 89 4d c0          	mov    QWORD PTR [rbp-0x40],rcx
    d140:	45 31 c0             	xor    r8d,r8d
    d143:	45 31 d2             	xor    r10d,r10d
    d146:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    d14a:	4c 01 d0             	add    rax,r10
    d14d:	48 83 c0 38          	add    rax,0x38
    d151:	48 8b 94 dd d8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1428]
    d158:	ff
    d159:	48 85 d2             	test   rdx,rdx
    d15c:	0f 84 8e fe ff ff    	je     cff0 <zbtScoreInsertAt+0x940>
    d162:	48 83 c0 15          	add    rax,0x15
    d166:	45 0f b7 61 36       	movzx  r12d,WORD PTR [r9+0x36]
    d16b:	4c 39 e0             	cmp    rax,r12
    d16e:	0f 86 bd 00 00 00    	jbe    d231 <zbtScoreInsertAt+0xb81>
    d174:	4c 89 cb             	mov    rbx,r9
    d177:	45 8b 49 30          	mov    r9d,DWORD PTR [r9+0x30]
    d17b:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d182:	48 8d 95 f0 fa ff ff 	lea    rdx,[rbp-0x510]
    d189:	48 8d 8d c0 eb ff ff 	lea    rcx,[rbp-0x1440]
    d190:	4c 8d 85 d0 fe ff ff 	lea    r8,[rbp-0x130]
    d197:	4c 8b bd 78 ff ff ff 	mov    r15,QWORD PTR [rbp-0x88]
    d19e:	4c 89 ff             	mov    rdi,r15
    d1a1:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    d1a5:	e8 d6 ed ff ff       	call   bf80 <zbtScoreLeafBuild>
    d1aa:	49 89 c6             	mov    r14,rax
    d1ad:	48 8b 03             	mov    rax,QWORD PTR [rbx]
    d1b0:	49 89 06             	mov    QWORD PTR [r14],rax
    d1b3:	0f b6 43 10          	movzx  eax,BYTE PTR [rbx+0x10]
    d1b7:	41 88 46 10          	mov    BYTE PTR [r14+0x10],al
    d1bb:	0f b7 4b 16          	movzx  ecx,WORD PTR [rbx+0x16]
    d1bf:	66 41 89 4e 16       	mov    WORD PTR [r14+0x16],cx
    d1c4:	48 8b 4b 18          	mov    rcx,QWORD PTR [rbx+0x18]
    d1c8:	49 89 4e 18          	mov    QWORD PTR [r14+0x18],rcx
    d1cc:	48 8b 53 20          	mov    rdx,QWORD PTR [rbx+0x20]
    d1d0:	49 89 56 20          	mov    QWORD PTR [r14+0x20],rdx
    d1d4:	49 8d 57 08          	lea    rdx,[r15+0x8]
    d1d8:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d1dc:	48 85 c9             	test   rcx,rcx
    d1df:	48 0f 44 f2          	cmove  rsi,rdx
    d1e3:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d1e6:	49 8b 4e 20          	mov    rcx,QWORD PTR [r14+0x20]
    d1ea:	49 8d 57 10          	lea    rdx,[r15+0x10]
    d1ee:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d1f2:	48 85 c9             	test   rcx,rcx
    d1f5:	48 0f 44 f2          	cmove  rsi,rdx
    d1f9:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d1fc:	48 8b 0b             	mov    rcx,QWORD PTR [rbx]
    d1ff:	48 85 c9             	test   rcx,rcx
    d202:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d207:	49 0f 44 c7          	cmove  rax,r15
    d20b:	4c 89 30             	mov    QWORD PTR [rax],r14
    d20e:	49 8b 76 08          	mov    rsi,QWORD PTR [r14+0x8]
    d212:	48 2b 73 08          	sub    rsi,QWORD PTR [rbx+0x8]
    d216:	4c 89 f7             	mov    rdi,r14
    d219:	e8 62 1f 00 00       	call   f180 <zbtScoreUpdatePath>
    d21e:	4c 89 ff             	mov    rdi,r15
    d221:	48 89 de             	mov    rsi,rbx
    d224:	e8 a7 e9 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d229:	4c 89 f0             	mov    rax,r14
    d22c:	e9 c4 0b 00 00       	jmp    ddf5 <zbtScoreInsertAt+0x1745>
    d231:	41 83 c4 eb          	add    r12d,0xffffffeb
    d235:	45 0f b7 f4          	movzx  r14d,r12w
    d239:	4d 01 ce             	add    r14,r9
    d23c:	48 8b 8c dd c8 eb ff 	mov    rcx,QWORD PTR [rbp+rbx*8-0x1438]
    d243:	ff
    d244:	e9 f6 08 00 00       	jmp    db3f <zbtScoreInsertAt+0x148f>
    d249:	4d 85 ff             	test   r15,r15
    d24c:	0f 85 3d f5 ff ff    	jne    c78f <zbtScoreInsertAt+0xdf>
    d252:	45 8d 54 24 01       	lea    r10d,[r12+0x1]
    d257:	45 31 f6             	xor    r14d,r14d
    d25a:	31 f6                	xor    esi,esi
    d25c:	48 89 75 c8          	mov    QWORD PTR [rbp-0x38],rsi
    d260:	be 15 00 00 00       	mov    esi,0x15
    d265:	48 89 75 b8          	mov    QWORD PTR [rbp-0x48],rsi
    d269:	49 83 7b 18 00       	cmp    QWORD PTR [r11+0x18],0x0
    d26e:	75 25                	jne    d295 <zbtScoreInsertAt+0xbe5>
    d270:	49 8b 7b 08          	mov    rdi,QWORD PTR [r11+0x8]
    d274:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    d27b:	77 18                	ja     d295 <zbtScoreInsertAt+0xbe5>
    d27d:	31 f6                	xor    esi,esi
    d27f:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    d286:	40 0f 93 c6          	setae  sil
    d28a:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    d28e:	48 ff c6             	inc    rsi
    d291:	48 89 75 b8          	mov    QWORD PTR [rbp-0x48],rsi
    d295:	44 89 d6             	mov    esi,r10d
    d298:	48 89 75 a8          	mov    QWORD PTR [rbp-0x58],rsi
    d29c:	48 8d 34 76          	lea    rsi,[rsi+rsi*2]
    d2a0:	48 03 75 c8          	add    rsi,QWORD PTR [rbp-0x38]
    d2a4:	48 8b 7d b8          	mov    rdi,QWORD PTR [rbp-0x48]
    d2a8:	48 01 f7             	add    rdi,rsi
    d2ab:	48 83 c7 38          	add    rdi,0x38
    d2af:	41 0f b7 71 36       	movzx  esi,WORD PTR [r9+0x36]
    d2b4:	48 39 f7             	cmp    rdi,rsi
    d2b7:	0f 87 d2 f4 ff ff    	ja     c78f <zbtScoreInsertAt+0xdf>
    d2bd:	4c 89 75 80          	mov    QWORD PTR [rbp-0x80],r14
    d2c1:	49 8d 73 18          	lea    rsi,[r11+0x18]
    d2c5:	48 89 75 88          	mov    QWORD PTR [rbp-0x78],rsi
    d2c9:	44 89 e3             	mov    ebx,r12d
    d2cc:	29 d3                	sub    ebx,edx
    d2ce:	84 c0                	test   al,al
    d2d0:	0f 44 da             	cmove  ebx,edx
    d2d3:	41 89 de             	mov    r14d,ebx
    d2d6:	48 85 c9             	test   rcx,rcx
    d2d9:	4c 89 b5 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],r14
    d2e0:	44 89 55 90          	mov    DWORD PTR [rbp-0x70],r10d
    d2e4:	0f 84 4f 0b 00 00    	je     de39 <zbtScoreInsertAt+0x1789>
    d2ea:	89 c8                	mov    eax,ecx
    d2ec:	48 89 45 a0          	mov    QWORD PTR [rbp-0x60],rax
    d2f0:	44 89 e0             	mov    eax,r12d
    d2f3:	0f af c1             	imul   eax,ecx
    d2f6:	83 c0 07             	add    eax,0x7
    d2f9:	c1 e8 03             	shr    eax,0x3
    d2fc:	83 c0 09             	add    eax,0x9
    d2ff:	25 fe 3f 00 00       	and    eax,0x3ffe
    d304:	4d 8d 69 38          	lea    r13,[r9+0x38]
    d308:	4c 01 c8             	add    rax,r9
    d30b:	48 83 c0 38          	add    rax,0x38
    d30f:	48 89 85 40 ff ff ff 	mov    QWORD PTR [rbp-0xc0],rax
    d316:	4a 8d 34 60          	lea    rsi,[rax+r12*2]
    d31a:	48 8d bd c0 eb ff ff 	lea    rdi,[rbp-0x1440]
    d321:	4c 89 e2             	mov    rdx,r12
    d324:	e8 f7 3d ff ff       	call   1120 <memcpy@plt>
    d329:	48 8b 55 a0          	mov    rdx,QWORD PTR [rbp-0x60]
    d32d:	48 89 d0             	mov    rax,rdx
    d330:	49 0f af c6          	imul   rax,r14
    d334:	48 89 85 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],rax
    d33b:	44 89 e0             	mov    eax,r12d
    d33e:	29 d8                	sub    eax,ebx
    d340:	48 89 c1             	mov    rcx,rax
    d343:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    d34a:	48 0f af d0          	imul   rdx,rax
    d34e:	48 89 95 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rdx
    d355:	48 83 fa 40          	cmp    rdx,0x40
    d359:	0f 83 03 0b 00 00    	jae    de62 <zbtScoreInsertAt+0x17b2>
    d35f:	4c 8b 9d 58 ff ff ff 	mov    r11,QWORD PTR [rbp-0xa8]
    d366:	4d 89 d9             	mov    r9,r11
    d369:	49 c1 e9 03          	shr    r9,0x3
    d36d:	44 89 d8             	mov    eax,r11d
    d370:	83 e0 07             	and    eax,0x7
    d373:	be 40 00 00 00       	mov    esi,0x40
    d378:	29 c6                	sub    esi,eax
    d37a:	48 8b bd 60 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xa0]
    d381:	41 89 f8             	mov    r8d,edi
    d384:	41 83 e0 3f          	and    r8d,0x3f
    d388:	0f 84 e7 0b 00 00    	je     df75 <zbtScoreInsertAt+0x18c5>
    d38e:	4b 8b 54 0d 00       	mov    rdx,QWORD PTR [r13+r9*1+0x0]
    d393:	44 89 d9             	mov    ecx,r11d
    d396:	83 e1 07             	and    ecx,0x7
    d399:	48 89 8d 48 ff ff ff 	mov    QWORD PTR [rbp-0xb8],rcx
    d3a0:	48 d3 ea             	shr    rdx,cl
    d3a3:	44 39 c6             	cmp    esi,r8d
    d3a6:	73 0e                	jae    d3b6 <zbtScoreInsertAt+0xd06>
    d3a8:	43 0f b6 44 0d 08    	movzx  eax,BYTE PTR [r13+r9*1+0x8]
    d3ae:	89 f1                	mov    ecx,esi
    d3b0:	48 d3 e0             	shl    rax,cl
    d3b3:	48 09 c2             	or     rdx,rax
    d3b6:	48 c7 c3 ff ff ff ff 	mov    rbx,0xffffffffffffffff
    d3bd:	49 c7 c2 ff ff ff ff 	mov    r10,0xffffffffffffffff
    d3c4:	89 f9                	mov    ecx,edi
    d3c6:	49 d3 e2             	shl    r10,cl
    d3c9:	49 f7 d2             	not    r10
    d3cc:	49 21 d2             	and    r10,rdx
    d3cf:	4c 03 5d a0          	add    r11,QWORD PTR [rbp-0x60]
    d3d3:	4c 89 df             	mov    rdi,r11
    d3d6:	48 c1 ef 03          	shr    rdi,0x3
    d3da:	41 83 e3 07          	and    r11d,0x7
    d3de:	41 be 40 00 00 00    	mov    r14d,0x40
    d3e4:	45 29 de             	sub    r14d,r11d
    d3e7:	45 39 c6             	cmp    r14d,r8d
    d3ea:	44 89 c2             	mov    edx,r8d
    d3ed:	41 0f 42 d6          	cmovb  edx,r14d
    d3f1:	89 d1                	mov    ecx,edx
    d3f3:	48 d3 e3             	shl    rbx,cl
    d3f6:	48 f7 d3             	not    rbx
    d3f9:	4c 89 d0             	mov    rax,r10
    d3fc:	48 21 d8             	and    rax,rbx
    d3ff:	44 89 d9             	mov    ecx,r11d
    d402:	48 d3 e3             	shl    rbx,cl
    d405:	48 f7 d3             	not    rbx
    d408:	49 23 5c 3d 00       	and    rbx,QWORD PTR [r13+rdi*1+0x0]
    d40d:	48 d3 e0             	shl    rax,cl
    d410:	48 09 d8             	or     rax,rbx
    d413:	49 89 44 3d 00       	mov    QWORD PTR [r13+rdi*1+0x0],rax
    d418:	45 39 c6             	cmp    r14d,r8d
    d41b:	73 20                	jae    d43d <zbtScoreInsertAt+0xd8d>
    d41d:	41 29 d0             	sub    r8d,edx
    d420:	41 0f b6 44 3d 08    	movzx  eax,BYTE PTR [r13+rdi*1+0x8]
    d426:	89 d1                	mov    ecx,edx
    d428:	49 d3 ea             	shr    r10,cl
    d42b:	44 31 d0             	xor    eax,r10d
    d42e:	44 89 c1             	mov    ecx,r8d
    d431:	d3 e8                	shr    eax,cl
    d433:	d3 e0                	shl    eax,cl
    d435:	44 31 d0             	xor    eax,r10d
    d438:	41 88 44 3d 08       	mov    BYTE PTR [r13+rdi*1+0x8],al
    d43d:	4c 8b 55 80          	mov    r10,QWORD PTR [rbp-0x80]
    d441:	4c 8b b5 70 ff ff ff 	mov    r14,QWORD PTR [rbp-0x90]
    d448:	4c 8b 9d 48 ff ff ff 	mov    r11,QWORD PTR [rbp-0xb8]
    d44f:	e9 30 0b 00 00       	jmp    df84 <zbtScoreInsertAt+0x18d4>
    d454:	0f b6 5d a0          	movzx  ebx,BYTE PTR [rbp-0x60]
    d458:	48 8d 0c 52          	lea    rcx,[rdx+rdx*2]
    d45c:	48 01 f1             	add    rcx,rsi
    d45f:	8b 75 c0             	mov    esi,DWORD PTR [rbp-0x40]
    d462:	39 75 b8             	cmp    DWORD PTR [rbp-0x48],esi
    d465:	0f 85 24 06 00 00    	jne    da8f <zbtScoreInsertAt+0x13df>
    d46b:	48 81 f9 00 10 00 00 	cmp    rcx,0x1000
    d472:	0f 82 7f 03 00 00    	jb     d7f7 <zbtScoreInsertAt+0x1147>
    d478:	84 db                	test   bl,bl
    d47a:	0f 84 58 03 00 00    	je     d7d8 <zbtScoreInsertAt+0x1128>
    d480:	4c 89 e8             	mov    rax,r13
    d483:	4c 09 f8             	or     rax,r15
    d486:	4d 85 ed             	test   r13,r13
    d489:	49 f7 d5             	not    r13
    d48c:	4c 0f 49 e8          	cmovns r13,rax
    d490:	48 8d 95 00 fb ff ff 	lea    rdx,[rbp-0x500]
    d497:	31 f6                	xor    esi,esi
    d499:	48 c7 45 98 ff ff ff 	mov    QWORD PTR [rbp-0x68],0xffffffffffffffff
    d4a0:	ff
    d4a1:	41 b8 01 00 00 00    	mov    r8d,0x1
    d4a7:	41 b9 28 00 00 00    	mov    r9d,0x28
    d4ad:	4c 8d b5 00 ec ff ff 	lea    r14,[rbp-0x1400]
    d4b4:	44 89 e1             	mov    ecx,r12d
    d4b7:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    d4be:	4c 89 6d 90          	mov    QWORD PTR [rbp-0x70],r13
    d4c2:	eb 33                	jmp    d4f7 <zbtScoreInsertAt+0xe47>
    d4c4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d4cb:	00 00 00 00 00
    d4d0:	4c 8b 45 c8          	mov    r8,QWORD PTR [rbp-0x38]
    d4d4:	49 ff c0             	inc    r8
    d4d7:	48 83 c6 08          	add    rsi,0x8
    d4db:	49 83 c1 28          	add    r9,0x28
    d4df:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    d4e3:	ff c9                	dec    ecx
    d4e5:	48 83 c2 08          	add    rdx,0x8
    d4e9:	49 83 c6 28          	add    r14,0x28
    d4ed:	4c 3b 45 b8          	cmp    r8,QWORD PTR [rbp-0x48]
    d4f1:	0f 84 db 02 00 00    	je     d7d2 <zbtScoreInsertAt+0x1122>
    d4f7:	4c 89 75 88          	mov    QWORD PTR [rbp-0x78],r14
    d4fb:	41 be 38 00 00 00    	mov    r14d,0x38
    d501:	49 83 f8 02          	cmp    r8,0x2
    d505:	4c 89 45 c8          	mov    QWORD PTR [rbp-0x38],r8
    d509:	0f 82 b1 00 00 00    	jb     d5c0 <zbtScoreInsertAt+0xf10>
    d50f:	49 89 cc             	mov    r12,rcx
    d512:	31 db                	xor    ebx,ebx
    d514:	4c 89 ef             	mov    rdi,r13
    d517:	31 c9                	xor    ecx,ecx
    d519:	4c 89 e8             	mov    rax,r13
    d51c:	eb 25                	jmp    d543 <zbtScoreInsertAt+0xe93>
    d51e:	66 90                	xchg   ax,ax
    d520:	4d 09 fa             	or     r10,r15
    d523:	4d 89 d3             	mov    r11,r10
    d526:	4d 31 eb             	xor    r11,r13
    d529:	4c 09 d9             	or     rcx,r11
    d52c:	49 39 fa             	cmp    r10,rdi
    d52f:	49 0f 42 fa          	cmovb  rdi,r10
    d533:	49 39 c2             	cmp    r10,rax
    d536:	49 0f 47 c2          	cmova  rax,r10
    d53a:	48 83 c3 08          	add    rbx,0x8
    d53e:	48 39 de             	cmp    rsi,rbx
    d541:	74 1d                	je     d560 <zbtScoreInsertAt+0xeb0>
    d543:	f3 0f 7e 84 1d f8 fa 	movq   xmm0,QWORD PTR [rbp+rbx*1-0x508]
    d54a:	ff ff
    d54c:	66 49 0f 7e c2       	movq   r10,xmm0
    d551:	4d 85 d2             	test   r10,r10
    d554:	79 ca                	jns    d520 <zbtScoreInsertAt+0xe70>
    d556:	49 f7 d2             	not    r10
    d559:	eb c8                	jmp    d523 <zbtScoreInsertAt+0xe73>
    d55b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    d560:	48 85 c9             	test   rcx,rcx
    d563:	74 4a                	je     d5af <zbtScoreInsertAt+0xeff>
    d565:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    d56a:	48 29 f8             	sub    rax,rdi
    d56d:	48 d3 e8             	shr    rax,cl
    d570:	48 85 c0             	test   rax,rax
    d573:	4c 8b 45 c8          	mov    r8,QWORD PTR [rbp-0x38]
    d577:	4c 89 e1             	mov    rcx,r12
    d57a:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d57e:	74 40                	je     d5c0 <zbtScoreInsertAt+0xf10>
    d580:	4c 0f bd f0          	bsr    r14,rax
    d584:	49 83 f6 c0          	xor    r14,0xffffffffffffffc0
    d588:	49 83 c6 41          	add    r14,0x41
    d58c:	4d 0f af f0          	imul   r14,r8
    d590:	49 83 c6 07          	add    r14,0x7
    d594:	49 c1 ee 03          	shr    r14,0x3
    d598:	49 83 c6 09          	add    r14,0x9
    d59c:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d5a3:	ff ff 1f
    d5a6:	49 21 c6             	and    r14,rax
    d5a9:	49 83 c6 38          	add    r14,0x38
    d5ad:	eb 11                	jmp    d5c0 <zbtScoreInsertAt+0xf10>
    d5af:	4c 8b 45 c8          	mov    r8,QWORD PTR [rbp-0x38]
    d5b3:	4c 89 e1             	mov    rcx,r12
    d5b6:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d5ba:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    d5c0:	89 c9                	mov    ecx,ecx
    d5c2:	48 89 4d a8          	mov    QWORD PTR [rbp-0x58],rcx
    d5c6:	48 ff c9             	dec    rcx
    d5c9:	4b 8d 1c 40          	lea    rbx,[r8+r8*2]
    d5cd:	4c 01 f3             	add    rbx,r14
    d5d0:	31 c0                	xor    eax,eax
    d5d2:	eb 18                	jmp    d5ec <zbtScoreInsertAt+0xf3c>
    d5d4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d5db:	00 00 00 00 00
    d5e0:	48 01 fb             	add    rbx,rdi
    d5e3:	48 83 c0 28          	add    rax,0x28
    d5e7:	49 39 c1             	cmp    r9,rax
    d5ea:	74 44                	je     d630 <zbtScoreInsertAt+0xf80>
    d5ec:	bf 15 00 00 00       	mov    edi,0x15
    d5f1:	48 83 bc 05 d8 eb ff 	cmp    QWORD PTR [rbp+rax*1-0x1428],0x0
    d5f8:	ff 00
    d5fa:	75 e4                	jne    d5e0 <zbtScoreInsertAt+0xf30>
    d5fc:	4c 8b 94 05 c8 eb ff 	mov    r10,QWORD PTR [rbp+rax*1-0x1438]
    d603:	ff
    d604:	49 81 fa 3f 01 00 00 	cmp    r10,0x13f
    d60b:	77 d3                	ja     d5e0 <zbtScoreInsertAt+0xf30>
    d60d:	31 ff                	xor    edi,edi
    d60f:	49 81 fa fe 00 00 00 	cmp    r10,0xfe
    d616:	40 0f 93 c7          	setae  dil
    d61a:	49 8d 3c 7a          	lea    rdi,[r10+rdi*2]
    d61e:	48 ff c7             	inc    rdi
    d621:	eb bd                	jmp    d5e0 <zbtScoreInsertAt+0xf30>
    d623:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d62a:	84 00 00 00 00 00
    d630:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    d634:	f3 0f 7e 84 c5 f0 fa 	movq   xmm0,QWORD PTR [rbp+rax*8-0x510]
    d63b:	ff ff
    d63d:	66 49 0f 7e c5       	movq   r13,xmm0
    d642:	4d 85 ed             	test   r13,r13
    d645:	78 09                	js     d650 <zbtScoreInsertAt+0xfa0>
    d647:	4d 09 fd             	or     r13,r15
    d64a:	eb 07                	jmp    d653 <zbtScoreInsertAt+0xfa3>
    d64c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d650:	49 f7 d5             	not    r13
    d653:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d657:	41 29 c6             	sub    r14d,eax
    d65a:	41 bf 38 00 00 00    	mov    r15d,0x38
    d660:	41 83 fe 02          	cmp    r14d,0x2
    d664:	72 6a                	jb     d6d0 <zbtScoreInsertAt+0x1020>
    d666:	45 31 d2             	xor    r10d,r10d
    d669:	4c 89 ef             	mov    rdi,r13
    d66c:	45 31 e4             	xor    r12d,r12d
    d66f:	4c 89 e8             	mov    rax,r13
    d672:	eb 38                	jmp    d6ac <zbtScoreInsertAt+0xffc>
    d674:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d67b:	00 00 00 00 00
    d680:	49 bb 00 00 00 00 00 	movabs r11,0x8000000000000000
    d687:	00 00 80
    d68a:	4d 09 d8             	or     r8,r11
    d68d:	4d 89 c3             	mov    r11,r8
    d690:	4d 31 eb             	xor    r11,r13
    d693:	4d 09 dc             	or     r12,r11
    d696:	49 39 f8             	cmp    r8,rdi
    d699:	49 0f 42 f8          	cmovb  rdi,r8
    d69d:	49 39 c0             	cmp    r8,rax
    d6a0:	49 0f 47 c0          	cmova  rax,r8
    d6a4:	49 ff c2             	inc    r10
    d6a7:	4c 39 d1             	cmp    rcx,r10
    d6aa:	74 34                	je     d6e0 <zbtScoreInsertAt+0x1030>
    d6ac:	f3 42 0f 7e 04 d2    	movq   xmm0,QWORD PTR [rdx+r10*8]
    d6b2:	66 49 0f 7e c0       	movq   r8,xmm0
    d6b7:	4d 85 c0             	test   r8,r8
    d6ba:	79 c4                	jns    d680 <zbtScoreInsertAt+0xfd0>
    d6bc:	49 f7 d0             	not    r8
    d6bf:	eb cc                	jmp    d68d <zbtScoreInsertAt+0xfdd>
    d6c1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d6c8:	0f 1f 84 00 00 00 00
    d6cf:	00
    d6d0:	4c 8b 6d 90          	mov    r13,QWORD PTR [rbp-0x70]
    d6d4:	eb 5a                	jmp    d730 <zbtScoreInsertAt+0x1080>
    d6d6:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    d6dd:	00 00 00
    d6e0:	4d 85 e4             	test   r12,r12
    d6e3:	4c 8b 6d 90          	mov    r13,QWORD PTR [rbp-0x70]
    d6e7:	74 43                	je     d72c <zbtScoreInsertAt+0x107c>
    d6e9:	f3 49 0f bc cc       	tzcnt  rcx,r12
    d6ee:	48 29 f8             	sub    rax,rdi
    d6f1:	48 d3 e8             	shr    rax,cl
    d6f4:	48 85 c0             	test   rax,rax
    d6f7:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d6fb:	74 33                	je     d730 <zbtScoreInsertAt+0x1080>
    d6fd:	4c 0f bd f8          	bsr    r15,rax
    d701:	49 83 f7 c0          	xor    r15,0xffffffffffffffc0
    d705:	49 83 c7 41          	add    r15,0x41
    d709:	4d 0f af fe          	imul   r15,r14
    d70d:	49 83 c7 07          	add    r15,0x7
    d711:	49 c1 ef 03          	shr    r15,0x3
    d715:	49 83 c7 09          	add    r15,0x9
    d719:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d720:	ff ff 1f
    d723:	49 21 c7             	and    r15,rax
    d726:	49 83 c7 38          	add    r15,0x38
    d72a:	eb 04                	jmp    d730 <zbtScoreInsertAt+0x1080>
    d72c:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d730:	4b 8d 04 76          	lea    rax,[r14+r14*2]
    d734:	4c 01 f8             	add    rax,r15
    d737:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    d73b:	4c 8b 75 88          	mov    r14,QWORD PTR [rbp-0x78]
    d73f:	4c 89 f7             	mov    rdi,r14
    d742:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    d749:	00 00 80
    d74c:	eb 0e                	jmp    d75c <zbtScoreInsertAt+0x10ac>
    d74e:	66 90                	xchg   ax,ax
    d750:	4c 01 d0             	add    rax,r10
    d753:	48 83 c7 28          	add    rdi,0x28
    d757:	48 ff c9             	dec    rcx
    d75a:	74 34                	je     d790 <zbtScoreInsertAt+0x10e0>
    d75c:	41 ba 15 00 00 00    	mov    r10d,0x15
    d762:	48 83 3f 00          	cmp    QWORD PTR [rdi],0x0
    d766:	75 e8                	jne    d750 <zbtScoreInsertAt+0x10a0>
    d768:	4c 8b 5f f0          	mov    r11,QWORD PTR [rdi-0x10]
    d76c:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    d773:	77 db                	ja     d750 <zbtScoreInsertAt+0x10a0>
    d775:	45 31 c0             	xor    r8d,r8d
    d778:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    d77f:	41 0f 93 c0          	setae  r8b
    d783:	4f 8d 14 43          	lea    r10,[r11+r8*2]
    d787:	49 ff c2             	inc    r10
    d78a:	eb c4                	jmp    d750 <zbtScoreInsertAt+0x10a0>
    d78c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d790:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    d797:	0f 87 33 fd ff ff    	ja     d4d0 <zbtScoreInsertAt+0xe20>
    d79d:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    d7a3:	4c 8b 45 c8          	mov    r8,QWORD PTR [rbp-0x38]
    d7a7:	0f 87 27 fd ff ff    	ja     d4d4 <zbtScoreInsertAt+0xe24>
    d7ad:	48 39 c3             	cmp    rbx,rax
    d7b0:	48 0f 47 c3          	cmova  rax,rbx
    d7b4:	48 8b 7d 98          	mov    rdi,QWORD PTR [rbp-0x68]
    d7b8:	48 39 f8             	cmp    rax,rdi
    d7bb:	8b 4d c0             	mov    ecx,DWORD PTR [rbp-0x40]
    d7be:	41 0f 42 c8          	cmovb  ecx,r8d
    d7c2:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    d7c5:	48 0f 42 f8          	cmovb  rdi,rax
    d7c9:	48 89 7d 98          	mov    QWORD PTR [rbp-0x68],rdi
    d7cd:	e9 02 fd ff ff       	jmp    d4d4 <zbtScoreInsertAt+0xe24>
    d7d2:	83 7d c0 00          	cmp    DWORD PTR [rbp-0x40],0x0
    d7d6:	75 1f                	jne    d7f7 <zbtScoreInsertAt+0x1147>
    d7d8:	48 8d 3d 3f 5e 00 00 	lea    rdi,[rip+0x5e3f]        # 1361e <_IO_stdin_used+0x61e>
    d7df:	48 8d 15 e9 60 00 00 	lea    rdx,[rip+0x60e9]        # 138cf <_IO_stdin_used+0x8cf>
    d7e6:	be 5b 05 00 00       	mov    esi,0x55b
    d7eb:	e8 20 46 00 00       	call   11e10 <standalone_panic>
    d7f0:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    d7f7:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d7fb:	44 8b 7d c0          	mov    r15d,DWORD PTR [rbp-0x40]
    d7ff:	45 29 fe             	sub    r14d,r15d
    d802:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    d806:	44 8b 48 30          	mov    r9d,DWORD PTR [rax+0x30]
    d80a:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d811:	48 8d 95 f0 fa ff ff 	lea    rdx,[rbp-0x510]
    d818:	48 8d 8d c0 eb ff ff 	lea    rcx,[rbp-0x1440]
    d81f:	4c 8d 85 d0 fe ff ff 	lea    r8,[rbp-0x130]
    d826:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d82d:	48 89 df             	mov    rdi,rbx
    d830:	44 89 fe             	mov    esi,r15d
    d833:	e8 48 e7 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d838:	49 89 c5             	mov    r13,rax
    d83b:	44 89 f8             	mov    eax,r15d
    d83e:	48 8d 14 c5 f0 fa ff 	lea    rdx,[rax*8-0x510]
    d845:	ff
    d846:	48 01 ea             	add    rdx,rbp
    d849:	48 8d 0c 80          	lea    rcx,[rax+rax*4]
    d84d:	48 8d 8c cd c0 eb ff 	lea    rcx,[rbp+rcx*8-0x1440]
    d854:	ff
    d855:	4c 8d 84 05 d0 fe ff 	lea    r8,[rbp+rax*1-0x130]
    d85c:	ff
    d85d:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d864:	48 89 df             	mov    rdi,rbx
    d867:	44 89 f6             	mov    esi,r14d
    d86a:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    d870:	e8 0b e7 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d875:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d879:	4c 89 e7             	mov    rdi,r12
    d87c:	49 89 c4             	mov    r12,rax
    d87f:	41 0f b7 40 16       	movzx  eax,WORD PTR [r8+0x16]
    d884:	66 41 89 44 24 16    	mov    WORD PTR [r12+0x16],ax
    d88a:	66 41 89 45 16       	mov    WORD PTR [r13+0x16],ax
    d88f:	49 8b 00             	mov    rax,QWORD PTR [r8]
    d892:	49 89 45 00          	mov    QWORD PTR [r13+0x0],rax
    d896:	41 0f b6 40 10       	movzx  eax,BYTE PTR [r8+0x10]
    d89b:	41 88 45 10          	mov    BYTE PTR [r13+0x10],al
    d89f:	49 8b 48 18          	mov    rcx,QWORD PTR [r8+0x18]
    d8a3:	49 89 4d 18          	mov    QWORD PTR [r13+0x18],rcx
    d8a7:	4d 89 65 20          	mov    QWORD PTR [r13+0x20],r12
    d8ab:	4d 89 6c 24 18       	mov    QWORD PTR [r12+0x18],r13
    d8b0:	49 8b 48 20          	mov    rcx,QWORD PTR [r8+0x20]
    d8b4:	49 89 4c 24 20       	mov    QWORD PTR [r12+0x20],rcx
    d8b9:	49 8b 4d 18          	mov    rcx,QWORD PTR [r13+0x18]
    d8bd:	48 8d 53 08          	lea    rdx,[rbx+0x8]
    d8c1:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d8c5:	48 85 c9             	test   rcx,rcx
    d8c8:	48 0f 44 f2          	cmove  rsi,rdx
    d8cc:	4c 89 2e             	mov    QWORD PTR [rsi],r13
    d8cf:	49 8b 4c 24 20       	mov    rcx,QWORD PTR [r12+0x20]
    d8d4:	48 8d 53 10          	lea    rdx,[rbx+0x10]
    d8d8:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d8dc:	48 85 c9             	test   rcx,rcx
    d8df:	48 0f 44 f2          	cmove  rsi,rdx
    d8e3:	4c 89 26             	mov    QWORD PTR [rsi],r12
    d8e6:	49 8b 08             	mov    rcx,QWORD PTR [r8]
    d8e9:	48 85 c9             	test   rcx,rcx
    d8ec:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d8f1:	48 0f 44 c3          	cmove  rax,rbx
    d8f5:	4c 89 6d a8          	mov    QWORD PTR [rbp-0x58],r13
    d8f9:	4c 89 28             	mov    QWORD PTR [rax],r13
    d8fc:	c7 85 50 ff ff ff 00 	mov    DWORD PTR [rbp-0xb0],0x0
    d903:	00 00 00
    d906:	41 39 ff             	cmp    r15d,edi
    d909:	76 5a                	jbe    d965 <zbtScoreInsertAt+0x12b5>
    d90b:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d912:	48 89 df             	mov    rdi,rbx
    d915:	4c 89 c6             	mov    rsi,r8
    d918:	e8 b3 e2 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d91d:	48 89 df             	mov    rdi,rbx
    d920:	4c 8b 75 a8          	mov    r14,QWORD PTR [rbp-0x58]
    d924:	4c 89 f6             	mov    rsi,r14
    d927:	4c 89 e2             	mov    rdx,r12
    d92a:	e8 01 0b 00 00       	call   e430 <zbtScoreInsertSibling>
    d92f:	49 8b 1e             	mov    rbx,QWORD PTR [r14]
    d932:	48 85 db             	test   rbx,rbx
    d935:	74 19                	je     d950 <zbtScoreInsertAt+0x12a0>
    d937:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    d93e:	00 00
    d940:	48 89 df             	mov    rdi,rbx
    d943:	e8 58 0f 00 00       	call   e8a0 <zbtScoreRefreshNode>
    d948:	48 8b 1b             	mov    rbx,QWORD PTR [rbx]
    d94b:	48 85 db             	test   rbx,rbx
    d94e:	75 f0                	jne    d940 <zbtScoreInsertAt+0x1290>
    d950:	8b 45 c0             	mov    eax,DWORD PTR [rbp-0x40]
    d953:	39 85 58 ff ff ff    	cmp    DWORD PTR [rbp-0xa8],eax
    d959:	4d 0f 42 e6          	cmovb  r12,r14
    d95d:	4c 89 e0             	mov    rax,r12
    d960:	e9 90 04 00 00       	jmp    ddf5 <zbtScoreInsertAt+0x1745>
    d965:	49 8d 44 24 38       	lea    rax,[r12+0x38]
    d96a:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    d96e:	31 c0                	xor    eax,eax
    d970:	44 8b bd 58 ff ff ff 	mov    r15d,DWORD PTR [rbp-0xa8]
    d977:	44 8b 75 c0          	mov    r14d,DWORD PTR [rbp-0x40]
    d97b:	45 29 f7             	sub    r15d,r14d
    d97e:	0f 93 c0             	setae  al
    d981:	89 45 c8             	mov    DWORD PTR [rbp-0x38],eax
    d984:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    d988:	45 29 f5             	sub    r13d,r14d
    d98b:	41 ff c5             	inc    r13d
    d98e:	31 db                	xor    ebx,ebx
    d990:	eb 1c                	jmp    d9ae <zbtScoreInsertAt+0x12fe>
    d992:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d999:	1f 84 00 00 00 00 00
    d9a0:	41 ff c6             	inc    r14d
    d9a3:	ff c3                	inc    ebx
    d9a5:	41 39 dd             	cmp    r13d,ebx
    d9a8:	0f 84 5d ff ff ff    	je     d90b <zbtScoreInsertAt+0x125b>
    d9ae:	41 39 df             	cmp    r15d,ebx
    d9b1:	74 ed                	je     d9a0 <zbtScoreInsertAt+0x12f0>
    d9b3:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    d9b9:	48 85 c0             	test   rax,rax
    d9bc:	74 57                	je     da15 <zbtScoreInsertAt+0x1365>
    d9be:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    d9c4:	0f af c1             	imul   eax,ecx
    d9c7:	83 c0 07             	add    eax,0x7
    d9ca:	c1 e8 03             	shr    eax,0x3
    d9cd:	83 c0 09             	add    eax,0x9
    d9d0:	83 e0 fe             	and    eax,0xfffffffe
    d9d3:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    d9d9:	89 d9                	mov    ecx,ebx
    d9db:	74 10                	je     d9ed <zbtScoreInsertAt+0x133d>
    d9dd:	44 89 f1             	mov    ecx,r14d
    d9e0:	2b 4d c0             	sub    ecx,DWORD PTR [rbp-0x40]
    d9e3:	41 0f b6 54 24 11    	movzx  edx,BYTE PTR [r12+0x11]
    d9e9:	f7 d1                	not    ecx
    d9eb:	01 d1                	add    ecx,edx
    d9ed:	48 03 45 b8          	add    rax,QWORD PTR [rbp-0x48]
    d9f1:	89 c9                	mov    ecx,ecx
    d9f3:	0f b7 04 48          	movzx  eax,WORD PTR [rax+rcx*2]
    d9f7:	49 8d 3c 04          	lea    rdi,[r12+rax*1]
    d9fb:	41 0f b6 34 04       	movzx  esi,BYTE PTR [r12+rax*1]
    da00:	81 fe fe 00 00 00    	cmp    esi,0xfe
    da06:	74 1b                	je     da23 <zbtScoreInsertAt+0x1373>
    da08:	81 fe ff 00 00 00    	cmp    esi,0xff
    da0e:	75 1e                	jne    da2e <zbtScoreInsertAt+0x137e>
    da10:	8b 77 01             	mov    esi,DWORD PTR [rdi+0x1]
    da13:	eb 2d                	jmp    da42 <zbtScoreInsertAt+0x1392>
    da15:	31 c0                	xor    eax,eax
    da17:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    da1d:	89 d9                	mov    ecx,ebx
    da1f:	75 bc                	jne    d9dd <zbtScoreInsertAt+0x132d>
    da21:	eb ca                	jmp    d9ed <zbtScoreInsertAt+0x133d>
    da23:	0f b7 77 01          	movzx  esi,WORD PTR [rdi+0x1]
    da27:	b8 03 00 00 00       	mov    eax,0x3
    da2c:	eb 05                	jmp    da33 <zbtScoreInsertAt+0x1383>
    da2e:	b8 01 00 00 00       	mov    eax,0x1
    da33:	48 01 c7             	add    rdi,rax
    da36:	e8 15 46 00 00       	call   12050 <dictGenHashFunction>
    da3b:	48 89 c6             	mov    rsi,rax
    da3e:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    da42:	41 8b 50 30          	mov    edx,DWORD PTR [r8+0x30]
    da46:	41 8b 4c 24 30       	mov    ecx,DWORD PTR [r12+0x30]
    da4b:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    da52:	44 8b 45 c8          	mov    r8d,DWORD PTR [rbp-0x38]
    da56:	4c 8d 8d 50 ff ff ff 	lea    r9,[rbp-0xb0]
    da5d:	e8 6e b7 ff ff       	call   91d0 <zbtIndexMove>
    da62:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    da66:	85 c0                	test   eax,eax
    da68:	0f 85 32 ff ff ff    	jne    d9a0 <zbtScoreInsertAt+0x12f0>
    da6e:	48 8d 3d a9 5b 00 00 	lea    rdi,[rip+0x5ba9]        # 1361e <_IO_stdin_used+0x61e>
    da75:	be 85 06 00 00       	mov    esi,0x685
    da7a:	48 8d 15 f3 5d 00 00 	lea    rdx,[rip+0x5df3]        # 13874 <_IO_stdin_used+0x874>
    da81:	e8 8a 43 00 00       	call   11e10 <standalone_panic>
    da86:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    da8a:	e9 11 ff ff ff       	jmp    d9a0 <zbtScoreInsertAt+0x12f0>
    da8f:	48 8d 04 80          	lea    rax,[rax+rax*4]
    da93:	48 8d 04 c5 d8 eb ff 	lea    rax,[rax*8-0x1428]
    da9a:	ff
    da9b:	48 01 e8             	add    rax,rbp
    da9e:	eb 10                	jmp    dab0 <zbtScoreInsertAt+0x1400>
    daa0:	48 01 f1             	add    rcx,rsi
    daa3:	48 83 c0 28          	add    rax,0x28
    daa7:	48 ff ca             	dec    rdx
    daaa:	0f 84 bb f9 ff ff    	je     d46b <zbtScoreInsertAt+0xdbb>
    dab0:	be 15 00 00 00       	mov    esi,0x15
    dab5:	48 83 38 00          	cmp    QWORD PTR [rax],0x0
    dab9:	75 e5                	jne    daa0 <zbtScoreInsertAt+0x13f0>
    dabb:	48 8b 78 f0          	mov    rdi,QWORD PTR [rax-0x10]
    dabf:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    dac6:	77 d8                	ja     daa0 <zbtScoreInsertAt+0x13f0>
    dac8:	31 f6                	xor    esi,esi
    daca:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    dad1:	40 0f 93 c6          	setae  sil
    dad5:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    dad9:	48 ff c6             	inc    rsi
    dadc:	eb c2                	jmp    daa0 <zbtScoreInsertAt+0x13f0>
    dade:	48 8d b5 50 ff ff ff 	lea    rsi,[rbp-0xb0]
    dae5:	4c 89 df             	mov    rdi,r11
    dae8:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    daec:	4c 89 9d 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],r11
    daf3:	e8 18 44 00 00       	call   11f10 <zmalloc_usable>
    daf8:	48 89 c7             	mov    rdi,rax
    dafb:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    daff:	48 8b 85 50 ff ff ff 	mov    rax,QWORD PTR [rbp-0xb0]
    db06:	48 8b 8d 78 ff ff ff 	mov    rcx,QWORD PTR [rbp-0x88]
    db0d:	48 01 41 68          	add    QWORD PTR [rcx+0x68],rax
    db11:	48 8b 45 90          	mov    rax,QWORD PTR [rbp-0x70]
    db15:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    db18:	48 8b 95 68 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x98]
    db1f:	e8 fc 35 ff ff       	call   1120 <memcpy@plt>
    db24:	48 8b 55 80          	mov    rdx,QWORD PTR [rbp-0x80]
    db28:	48 8b 8d 68 ff ff ff 	mov    rcx,QWORD PTR [rbp-0x98]
    db2f:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    db33:	4c 8b 45 98          	mov    r8,QWORD PTR [rbp-0x68]
    db37:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    db3b:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    db3f:	41 c6 06 ff          	mov    BYTE PTR [r14],0xff
    db43:	8b 84 dd d0 eb ff ff 	mov    eax,DWORD PTR [rbp+rbx*8-0x1430]
    db4a:	41 89 46 01          	mov    DWORD PTR [r14+0x1],eax
    db4e:	49 89 4e 05          	mov    QWORD PTR [r14+0x5],rcx
    db52:	49 89 56 0d          	mov    QWORD PTR [r14+0xd],rdx
    db56:	4c 8b b4 dd e0 eb ff 	mov    r14,QWORD PTR [rbp+rbx*8-0x1420]
    db5d:	ff
    db5e:	4d 85 f6             	test   r14,r14
    db61:	74 40                	je     dba3 <zbtScoreInsertAt+0x14f3>
    db63:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    db67:	74 32                	je     db9b <zbtScoreInsertAt+0x14eb>
    db69:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    db6d:	48 8d 3d aa 5a 00 00 	lea    rdi,[rip+0x5aaa]        # 1361e <_IO_stdin_used+0x61e>
    db74:	48 8d 15 db 5b 00 00 	lea    rdx,[rip+0x5bdb]        # 13756 <_IO_stdin_used+0x756>
    db7b:	be 4e 02 00 00       	mov    esi,0x24e
    db80:	4c 89 c3             	mov    rbx,r8
    db83:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    db87:	e8 84 42 00 00       	call   11e10 <standalone_panic>
    db8c:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    db90:	49 89 d8             	mov    r8,rbx
    db93:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    db97:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    db9b:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    dba2:	00
    dba3:	4c 89 65 c8          	mov    QWORD PTR [rbp-0x38],r12
    dba7:	41 c6 41 14 01       	mov    BYTE PTR [r9+0x14],0x1
    dbac:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    dbb0:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    dbb4:	45 88 61 11          	mov    BYTE PTR [r9+0x11],r12b
    dbb8:	4d 89 61 08          	mov    QWORD PTR [r9+0x8],r12
    dbbc:	41 88 79 13          	mov    BYTE PTR [r9+0x13],dil
    dbc0:	4d 89 69 28          	mov    QWORD PTR [r9+0x28],r13
    dbc4:	45 88 41 34          	mov    BYTE PTR [r9+0x34],r8b
    dbc8:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    dbcc:	66 41 89 41 36       	mov    WORD PTR [r9+0x36],ax
    dbd1:	48 8b 5d a8          	mov    rbx,QWORD PTR [rbp-0x58]
    dbd5:	48 89 df             	mov    rdi,rbx
    dbd8:	31 f6                	xor    esi,esi
    dbda:	4c 89 d2             	mov    rdx,r10
    dbdd:	4d 89 c6             	mov    r14,r8
    dbe0:	e8 cb 34 ff ff       	call   10b0 <memset@plt>
    dbe5:	41 0f b6 cc          	movzx  ecx,r12b
    dbe9:	45 84 f6             	test   r14b,r14b
    dbec:	0f 84 0a 01 00 00    	je     dcfc <zbtScoreInsertAt+0x164c>
    dbf2:	41 0f b6 d6          	movzx  edx,r14b
    dbf6:	89 d6                	mov    esi,edx
    dbf8:	0f af f1             	imul   esi,ecx
    dbfb:	83 c6 07             	add    esi,0x7
    dbfe:	c1 ee 03             	shr    esi,0x3
    dc01:	83 c6 09             	add    esi,0x9
    dc04:	83 e6 fe             	and    esi,0xfffffffe
    dc07:	48 01 de             	add    rsi,rbx
    dc0a:	48 8d 3c 4e          	lea    rdi,[rsi+rcx*2]
    dc0e:	0f b6 45 b0          	movzx  eax,BYTE PTR [rbp-0x50]
    dc12:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    dc16:	45 0f b6 40 35       	movzx  r8d,BYTE PTR [r8+0x35]
    dc1b:	44 8d 49 ff          	lea    r9d,[rcx-0x1]
    dc1f:	45 31 d2             	xor    r10d,r10d
    dc22:	eb 36                	jmp    dc5a <zbtScoreInsertAt+0x15aa>
    dc24:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    dc2b:	00 00 00 00 00
    dc30:	66 89 0c 5e          	mov    WORD PTR [rsi+rbx*2],cx
    dc34:	42 0f b6 8c 15 d0 fe 	movzx  ecx,BYTE PTR [rbp+r10*1-0x130]
    dc3b:	ff ff
    dc3d:	88 0c 1f             	mov    BYTE PTR [rdi+rbx*1],cl
    dc40:	49 ff c2             	inc    r10
    dc43:	41 ff c9             	dec    r9d
    dc46:	4c 39 55 b8          	cmp    QWORD PTR [rbp-0x48],r10
    dc4a:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    dc51:	00 00 80
    dc54:	0f 84 87 01 00 00    	je     dde1 <zbtScoreInsertAt+0x1731>
    dc5a:	f3 42 0f 7e 84 d5 f0 	movq   xmm0,QWORD PTR [rbp+r10*8-0x510]
    dc61:	fa ff ff
    dc64:	66 49 0f 7e c3       	movq   r11,xmm0
    dc69:	4d 85 db             	test   r11,r11
    dc6c:	78 12                	js     dc80 <zbtScoreInsertAt+0x15d0>
    dc6e:	4d 09 fb             	or     r11,r15
    dc71:	eb 10                	jmp    dc83 <zbtScoreInsertAt+0x15d3>
    dc73:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    dc7a:	84 00 00 00 00 00
    dc80:	49 f7 d3             	not    r11
    dc83:	4c 89 e9             	mov    rcx,r13
    dc86:	4c 29 d9             	sub    rcx,r11
    dc89:	4d 29 eb             	sub    r11,r13
    dc8c:	45 84 c0             	test   r8b,r8b
    dc8f:	4c 0f 45 d9          	cmovne r11,rcx
    dc93:	44 89 cb             	mov    ebx,r9d
    dc96:	41 0f 44 da          	cmove  ebx,r10d
    dc9a:	89 c1                	mov    ecx,eax
    dc9c:	49 d3 eb             	shr    r11,cl
    dc9f:	49 89 df             	mov    r15,rbx
    dca2:	4c 0f af fa          	imul   r15,rdx
    dca6:	4d 89 fe             	mov    r14,r15
    dca9:	49 c1 ee 03          	shr    r14,0x3
    dcad:	44 89 f9             	mov    ecx,r15d
    dcb0:	80 e1 07             	and    cl,0x7
    dcb3:	4d 89 dc             	mov    r12,r11
    dcb6:	49 d3 e4             	shl    r12,cl
    dcb9:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    dcbd:	4e 09 24 31          	or     QWORD PTR [rcx+r14*1],r12
    dcc1:	41 83 e7 07          	and    r15d,0x7
    dcc5:	74 19                	je     dce0 <zbtScoreInsertAt+0x1630>
    dcc7:	b9 40 00 00 00       	mov    ecx,0x40
    dccc:	44 29 f9             	sub    ecx,r15d
    dccf:	3b 4d c0             	cmp    ecx,DWORD PTR [rbp-0x40]
    dcd2:	73 0c                	jae    dce0 <zbtScoreInsertAt+0x1630>
    dcd4:	49 d3 eb             	shr    r11,cl
    dcd7:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    dcdb:	45 08 5c 0e 40       	or     BYTE PTR [r14+rcx*1+0x40],r11b
    dce0:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    dce4:	4c 39 55 88          	cmp    QWORD PTR [rbp-0x78],r10
    dce8:	0f 84 42 ff ff ff    	je     dc30 <zbtScoreInsertAt+0x1580>
    dcee:	42 0f b7 8c 55 00 fe 	movzx  ecx,WORD PTR [rbp+r10*2-0x200]
    dcf5:	ff ff
    dcf7:	e9 34 ff ff ff       	jmp    dc30 <zbtScoreInsertAt+0x1580>
    dcfc:	48 8d 04 4b          	lea    rax,[rbx+rcx*2]
    dd00:	48 8b 55 d0          	mov    rdx,QWORD PTR [rbp-0x30]
    dd04:	0f b6 52 35          	movzx  edx,BYTE PTR [rdx+0x35]
    dd08:	80 7d a0 00          	cmp    BYTE PTR [rbp-0x60],0x0
    dd0c:	0f 84 95 00 00 00    	je     dda7 <zbtScoreInsertAt+0x16f7>
    dd12:	48 8b 7d b8          	mov    rdi,QWORD PTR [rbp-0x48]
    dd16:	83 e7 fe             	and    edi,0xfffffffe
    dd19:	44 8d 41 fe          	lea    r8d,[rcx-0x2]
    dd1d:	45 31 c9             	xor    r9d,r9d
    dd20:	48 8b 5d a8          	mov    rbx,QWORD PTR [rbp-0x58]
    dd24:	4c 8b 75 88          	mov    r14,QWORD PTR [rbp-0x78]
    dd28:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    dd2c:	eb 29                	jmp    dd57 <zbtScoreInsertAt+0x16a7>
    dd2e:	66 90                	xchg   ax,ax
    dd30:	84 d2                	test   dl,dl
    dd32:	45 89 c3             	mov    r11d,r8d
    dd35:	45 0f 44 d9          	cmove  r11d,r9d
    dd39:	66 46 89 14 5b       	mov    WORD PTR [rbx+r11*2],r10w
    dd3e:	44 0f b6 94 35 d1 fe 	movzx  r10d,BYTE PTR [rbp+rsi*1-0x12f]
    dd45:	ff ff
    dd47:	46 88 14 18          	mov    BYTE PTR [rax+r11*1],r10b
    dd4b:	41 83 c0 fe          	add    r8d,0xfffffffe
    dd4f:	49 ff c1             	inc    r9
    dd52:	49 39 f9             	cmp    r9,rdi
    dd55:	74 4a                	je     dda1 <zbtScoreInsertAt+0x16f1>
    dd57:	4c 89 ce             	mov    rsi,r9
    dd5a:	45 89 f9             	mov    r9d,r15d
    dd5d:	49 39 f6             	cmp    r14,rsi
    dd60:	74 09                	je     dd6b <zbtScoreInsertAt+0x16bb>
    dd62:	44 0f b7 8c 75 00 fe 	movzx  r9d,WORD PTR [rbp+rsi*2-0x200]
    dd69:	ff ff
    dd6b:	45 8d 50 01          	lea    r10d,[r8+0x1]
    dd6f:	84 d2                	test   dl,dl
    dd71:	41 89 f3             	mov    r11d,esi
    dd74:	45 0f 45 da          	cmovne r11d,r10d
    dd78:	66 46 89 0c 5b       	mov    WORD PTR [rbx+r11*2],r9w
    dd7d:	44 0f b6 8c 35 d0 fe 	movzx  r9d,BYTE PTR [rbp+rsi*1-0x130]
    dd84:	ff ff
    dd86:	46 88 0c 18          	mov    BYTE PTR [rax+r11*1],r9b
    dd8a:	4c 8d 4e 01          	lea    r9,[rsi+0x1]
    dd8e:	45 89 fa             	mov    r10d,r15d
    dd91:	4d 39 f1             	cmp    r9,r14
    dd94:	74 9a                	je     dd30 <zbtScoreInsertAt+0x1680>
    dd96:	44 0f b7 94 75 02 fe 	movzx  r10d,WORD PTR [rbp+rsi*2-0x1fe]
    dd9d:	ff ff
    dd9f:	eb 8f                	jmp    dd30 <zbtScoreInsertAt+0x1680>
    dda1:	48 83 c6 02          	add    rsi,0x2
    dda5:	eb 06                	jmp    ddad <zbtScoreInsertAt+0x16fd>
    dda7:	31 f6                	xor    esi,esi
    dda9:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    ddad:	f6 45 b8 01          	test   BYTE PTR [rbp-0x48],0x1
    ddb1:	74 2e                	je     dde1 <zbtScoreInsertAt+0x1731>
    ddb3:	48 3b 75 88          	cmp    rsi,QWORD PTR [rbp-0x78]
    ddb7:	74 09                	je     ddc2 <zbtScoreInsertAt+0x1712>
    ddb9:	44 0f b7 bc 75 00 fe 	movzx  r15d,WORD PTR [rbp+rsi*2-0x200]
    ddc0:	ff ff
    ddc2:	89 f7                	mov    edi,esi
    ddc4:	f7 d7                	not    edi
    ddc6:	01 cf                	add    edi,ecx
    ddc8:	84 d2                	test   dl,dl
    ddca:	0f 44 fe             	cmove  edi,esi
    ddcd:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    ddd1:	66 44 89 3c 79       	mov    WORD PTR [rcx+rdi*2],r15w
    ddd6:	0f b6 8c 35 d0 fe ff 	movzx  ecx,BYTE PTR [rbp+rsi*1-0x130]
    dddd:	ff
    ddde:	88 0c 38             	mov    BYTE PTR [rax+rdi*1],cl
    dde1:	be 01 00 00 00       	mov    esi,0x1
    dde6:	48 8b 5d d0          	mov    rbx,QWORD PTR [rbp-0x30]
    ddea:	48 89 df             	mov    rdi,rbx
    dded:	e8 8e 13 00 00       	call   f180 <zbtScoreUpdatePath>
    ddf2:	48 89 d8             	mov    rax,rbx
    ddf5:	48 81 c4 28 14 00 00 	add    rsp,0x1428
    ddfc:	5b                   	pop    rbx
    ddfd:	41 5c                	pop    r12
    ddff:	41 5d                	pop    r13
    de01:	41 5e                	pop    r14
    de03:	41 5f                	pop    r15
    de05:	5d                   	pop    rbp
    de06:	c3                   	ret
    de07:	66 45 89 5e 01       	mov    WORD PTR [r14+0x1],r11w
    de0c:	bf 03 00 00 00       	mov    edi,0x3
    de11:	b0 fe                	mov    al,0xfe
    de13:	4c 89 65 c8          	mov    QWORD PTR [rbp-0x38],r12
    de17:	41 88 06             	mov    BYTE PTR [r14],al
    de1a:	4c 01 f7             	add    rdi,r14
    de1d:	4c 89 da             	mov    rdx,r11
    de20:	e8 fb 32 ff ff       	call   1120 <memcpy@plt>
    de25:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    de29:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    de2d:	4c 8b 45 98          	mov    r8,QWORD PTR [rbp-0x68]
    de31:	49 89 da             	mov    r10,rbx
    de34:	e9 73 fd ff ff       	jmp    dbac <zbtScoreInsertAt+0x14fc>
    de39:	4d 8d 79 38          	lea    r15,[r9+0x38]
    de3d:	4b 8d 34 61          	lea    rsi,[r9+r12*2]
    de41:	48 83 c6 38          	add    rsi,0x38
    de45:	48 8d bd c0 eb ff ff 	lea    rdi,[rbp-0x1440]
    de4c:	4c 89 e2             	mov    rdx,r12
    de4f:	4d 89 cd             	mov    r13,r9
    de52:	e8 c9 32 ff ff       	call   1120 <memcpy@plt>
    de57:	45 89 e6             	mov    r14d,r12d
    de5a:	41 29 de             	sub    r14d,ebx
    de5d:	e9 97 01 00 00       	jmp    dff9 <zbtScoreInsertAt+0x1949>
    de62:	48 8b 8d 60 ff ff ff 	mov    rcx,QWORD PTR [rbp-0xa0]
    de69:	49 89 ca             	mov    r10,rcx
    de6c:	49 c1 ea 06          	shr    r10,0x6
    de70:	48 8b 85 58 ff ff ff 	mov    rax,QWORD PTR [rbp-0xa8]
    de77:	4c 8d 1c 01          	lea    r11,[rcx+rax*1]
    de7b:	44 89 de             	mov    esi,r11d
    de7e:	bf 40 00 00 00       	mov    edi,0x40
    de83:	83 e6 07             	and    esi,0x7
    de86:	0f 84 04 03 00 00    	je     e190 <zbtScoreInsertAt+0x1ae0>
    de8c:	29 f7                	sub    edi,esi
    de8e:	48 8b 85 70 ff ff ff 	mov    rax,QWORD PTR [rbp-0x90]
    de95:	49 01 c6             	add    r14,rax
    de98:	49 ff c6             	inc    r14
    de9b:	4c 0f af 75 a0       	imul   r14,QWORD PTR [rbp-0x60]
    dea0:	49 83 c6 c0          	add    r14,0xffffffffffffffc0
    dea4:	49 83 c3 c0          	add    r11,0xffffffffffffffc0
    dea8:	eb 11                	jmp    debb <zbtScoreInsertAt+0x180b>
    deaa:	49 83 c6 c0          	add    r14,0xffffffffffffffc0
    deae:	49 83 c3 c0          	add    r11,0xffffffffffffffc0
    deb2:	49 ff ca             	dec    r10
    deb5:	0f 84 a4 f4 ff ff    	je     d35f <zbtScoreInsertAt+0xcaf>
    debb:	4c 89 d8             	mov    rax,r11
    debe:	48 c1 e8 03          	shr    rax,0x3
    dec2:	4d 8b 44 05 00       	mov    r8,QWORD PTR [r13+rax*1+0x0]
    dec7:	89 f1                	mov    ecx,esi
    dec9:	49 d3 e8             	shr    r8,cl
    decc:	41 0f b6 54 05 08    	movzx  edx,BYTE PTR [r13+rax*1+0x8]
    ded2:	89 f9                	mov    ecx,edi
    ded4:	48 d3 e2             	shl    rdx,cl
    ded7:	4c 09 c2             	or     rdx,r8
    deda:	4c 89 f3             	mov    rbx,r14
    dedd:	45 89 f0             	mov    r8d,r14d
    dee0:	41 83 e0 07          	and    r8d,0x7
    dee4:	44 89 c1             	mov    ecx,r8d
    dee7:	f7 d9                	neg    ecx
    dee9:	48 c7 c0 ff ff ff ff 	mov    rax,0xffffffffffffffff
    def0:	48 d3 e0             	shl    rax,cl
    def3:	48 c1 eb 03          	shr    rbx,0x3
    def7:	48 f7 d0             	not    rax
    defa:	41 83 f8 01          	cmp    r8d,0x1
    defe:	41 b9 00 00 00 00    	mov    r9d,0x0
    df04:	4d 19 c9             	sbb    r9,r9
    df07:	49 09 c1             	or     r9,rax
    df0a:	4c 89 c8             	mov    rax,r9
    df0d:	44 89 c1             	mov    ecx,r8d
    df10:	48 d3 e0             	shl    rax,cl
    df13:	48 f7 d0             	not    rax
    df16:	49 23 44 1d 00       	and    rax,QWORD PTR [r13+rbx*1+0x0]
    df1b:	49 21 d1             	and    r9,rdx
    df1e:	49 d3 e1             	shl    r9,cl
    df21:	49 09 c1             	or     r9,rax
    df24:	4d 89 4c 1d 00       	mov    QWORD PTR [r13+rbx*1+0x0],r9
    df29:	45 85 c0             	test   r8d,r8d
    df2c:	0f 84 78 ff ff ff    	je     deaa <zbtScoreInsertAt+0x17fa>
    df32:	41 b9 40 00 00 00    	mov    r9d,0x40
    df38:	45 29 c1             	sub    r9d,r8d
    df3b:	b8 7e 00 00 00       	mov    eax,0x7e
    df40:	44 89 c1             	mov    ecx,r8d
    df43:	d3 e8                	shr    eax,cl
    df45:	d3 e0                	shl    eax,cl
    df47:	45 0f b6 44 1d 08    	movzx  r8d,BYTE PTR [r13+rbx*1+0x8]
    df4d:	41 89 c4             	mov    r12d,eax
    df50:	41 83 f4 7f          	xor    r12d,0x7f
    df54:	0d 80 00 00 00       	or     eax,0x80
    df59:	44 89 c9             	mov    ecx,r9d
    df5c:	48 d3 ea             	shr    rdx,cl
    df5f:	44 21 c0             	and    eax,r8d
    df62:	44 21 e2             	and    edx,r12d
    df65:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    df69:	09 c2                	or     edx,eax
    df6b:	41 88 54 1d 08       	mov    BYTE PTR [r13+rbx*1+0x8],dl
    df70:	e9 35 ff ff ff       	jmp    deaa <zbtScoreInsertAt+0x17fa>
    df75:	41 83 e3 07          	and    r11d,0x7
    df79:	4c 8b 55 80          	mov    r10,QWORD PTR [rbp-0x80]
    df7d:	4c 8b b5 70 ff ff ff 	mov    r14,QWORD PTR [rbp-0x90]
    df84:	44 39 d6             	cmp    esi,r10d
    df87:	44 89 d0             	mov    eax,r10d
    df8a:	0f 42 c6             	cmovb  eax,esi
    df8d:	48 c7 c2 ff ff ff ff 	mov    rdx,0xffffffffffffffff
    df94:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    df9b:	89 c1                	mov    ecx,eax
    df9d:	49 d3 e0             	shl    r8,cl
    dfa0:	83 f8 40             	cmp    eax,0x40
    dfa3:	49 f7 d0             	not    r8
    dfa6:	4c 0f 44 c2          	cmove  r8,rdx
    dfaa:	4c 89 c2             	mov    rdx,r8
    dfad:	44 89 d9             	mov    ecx,r11d
    dfb0:	48 d3 e2             	shl    rdx,cl
    dfb3:	48 f7 d2             	not    rdx
    dfb6:	4b 23 54 0d 00       	and    rdx,QWORD PTR [r13+r9*1+0x0]
    dfbb:	4d 21 f8             	and    r8,r15
    dfbe:	49 d3 e0             	shl    r8,cl
    dfc1:	49 09 d0             	or     r8,rdx
    dfc4:	4f 89 44 0d 00       	mov    QWORD PTR [r13+r9*1+0x0],r8
    dfc9:	44 39 d6             	cmp    esi,r10d
    dfcc:	73 20                	jae    dfee <zbtScoreInsertAt+0x193e>
    dfce:	41 29 c2             	sub    r10d,eax
    dfd1:	43 0f b6 54 0d 08    	movzx  edx,BYTE PTR [r13+r9*1+0x8]
    dfd7:	89 c1                	mov    ecx,eax
    dfd9:	49 d3 ef             	shr    r15,cl
    dfdc:	44 31 fa             	xor    edx,r15d
    dfdf:	44 89 d1             	mov    ecx,r10d
    dfe2:	d3 ea                	shr    edx,cl
    dfe4:	d3 e2                	shl    edx,cl
    dfe6:	44 31 fa             	xor    edx,r15d
    dfe9:	43 88 54 0d 08       	mov    BYTE PTR [r13+r9*1+0x8],dl
    dfee:	4c 8b 6d d0          	mov    r13,QWORD PTR [rbp-0x30]
    dff2:	4c 8b bd 40 ff ff ff 	mov    r15,QWORD PTR [rbp-0xc0]
    dff9:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    dffd:	4a 8d 1c 28          	lea    rbx,[rax+r13*1]
    e001:	4a 8d 3c 28          	lea    rdi,[rax+r13*1]
    e005:	48 83 c7 38          	add    rdi,0x38
    e009:	43 8d 14 24          	lea    edx,[r12+r12*1]
    e00d:	4c 89 fe             	mov    rsi,r15
    e010:	e8 4b 31 ff ff       	call   1160 <memmove@plt>
    e015:	4c 8b bd 68 ff ff ff 	mov    r15,QWORD PTR [rbp-0x98]
    e01c:	4a 8d 34 7b          	lea    rsi,[rbx+r15*2]
    e020:	48 83 c6 38          	add    rsi,0x38
    e024:	4a 8d 3c 7b          	lea    rdi,[rbx+r15*2]
    e028:	48 83 c7 3a          	add    rdi,0x3a
    e02c:	4b 8d 14 36          	lea    rdx,[r14+r14*1]
    e030:	48 89 75 c8          	mov    QWORD PTR [rbp-0x38],rsi
    e034:	e8 27 31 ff ff       	call   1160 <memmove@plt>
    e039:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    e03d:	4c 8d 24 43          	lea    r12,[rbx+rax*2]
    e041:	49 83 c4 38          	add    r12,0x38
    e045:	48 8d b5 c0 eb ff ff 	lea    rsi,[rbp-0x1440]
    e04c:	4c 89 e7             	mov    rdi,r12
    e04f:	4c 89 fa             	mov    rdx,r15
    e052:	e8 c9 30 ff ff       	call   1120 <memcpy@plt>
    e057:	0f b6 45 c0          	movzx  eax,BYTE PTR [rbp-0x40]
    e05b:	43 88 04 27          	mov    BYTE PTR [r15+r12*1],al
    e05f:	4b 8d 3c 27          	lea    rdi,[r15+r12*1]
    e063:	48 ff c7             	inc    rdi
    e066:	49 8d 34 2f          	lea    rsi,[r15+rbp*1]
    e06a:	48 81 c6 c0 eb ff ff 	add    rsi,0xffffffffffffebc0
    e071:	4c 89 f2             	mov    rdx,r14
    e074:	e8 a7 30 ff ff       	call   1120 <memcpy@plt>
    e079:	41 0f b7 5d 36       	movzx  ebx,WORD PTR [r13+0x36]
    e07e:	2b 5d b8             	sub    ebx,DWORD PTR [rbp-0x48]
    e081:	44 0f b7 e3          	movzx  r12d,bx
    e085:	4d 01 ec             	add    r12,r13
    e088:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    e08c:	4c 8b 30             	mov    r14,QWORD PTR [rax]
    e08f:	4d 85 f6             	test   r14,r14
    e092:	4c 89 ef             	mov    rdi,r13
    e095:	75 68                	jne    e0ff <zbtScoreInsertAt+0x1a4f>
    e097:	48 8b 45 98          	mov    rax,QWORD PTR [rbp-0x68]
    e09b:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    e09f:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    e0a6:	77 1c                	ja     e0c4 <zbtScoreInsertAt+0x1a14>
    e0a8:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    e0ab:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    e0b2:	0f 87 a8 01 00 00    	ja     e260 <zbtScoreInsertAt+0x1bb0>
    e0b8:	bf 01 00 00 00       	mov    edi,0x1
    e0bd:	89 d0                	mov    eax,edx
    e0bf:	e9 a9 01 00 00       	jmp    e26d <zbtScoreInsertAt+0x1bbd>
    e0c4:	48 8d b5 f0 fa ff ff 	lea    rsi,[rbp-0x510]
    e0cb:	48 89 d7             	mov    rdi,rdx
    e0ce:	49 89 c5             	mov    r13,rax
    e0d1:	e8 3a 3e 00 00       	call   11f10 <zmalloc_usable>
    e0d6:	48 8b 8d f0 fa ff ff 	mov    rcx,QWORD PTR [rbp-0x510]
    e0dd:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    e0e4:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    e0e8:	49 89 c6             	mov    r14,rax
    e0eb:	49 8b 75 00          	mov    rsi,QWORD PTR [r13+0x0]
    e0ef:	49 8b 55 08          	mov    rdx,QWORD PTR [r13+0x8]
    e0f3:	48 89 c7             	mov    rdi,rax
    e0f6:	e8 25 30 ff ff       	call   1120 <memcpy@plt>
    e0fb:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e0ff:	48 8b 55 98          	mov    rdx,QWORD PTR [rbp-0x68]
    e103:	48 8b 42 08          	mov    rax,QWORD PTR [rdx+0x8]
    e107:	41 c6 04 24 ff       	mov    BYTE PTR [r12],0xff
    e10c:	8b 4a 10             	mov    ecx,DWORD PTR [rdx+0x10]
    e10f:	41 89 4c 24 01       	mov    DWORD PTR [r12+0x1],ecx
    e114:	49 89 44 24 05       	mov    QWORD PTR [r12+0x5],rax
    e119:	4d 89 74 24 0d       	mov    QWORD PTR [r12+0xd],r14
    e11e:	4c 8b 72 20          	mov    r14,QWORD PTR [rdx+0x20]
    e122:	4d 85 f6             	test   r14,r14
    e125:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    e129:	74 2a                	je     e155 <zbtScoreInsertAt+0x1aa5>
    e12b:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    e12f:	74 1c                	je     e14d <zbtScoreInsertAt+0x1a9d>
    e131:	48 8d 3d e6 54 00 00 	lea    rdi,[rip+0x54e6]        # 1361e <_IO_stdin_used+0x61e>
    e138:	48 8d 15 17 56 00 00 	lea    rdx,[rip+0x5617]        # 13756 <_IO_stdin_used+0x756>
    e13f:	be 4e 02 00 00       	mov    esi,0x24e
    e144:	e8 c7 3c 00 00       	call   11e10 <standalone_panic>
    e149:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e14d:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    e154:	00
    e155:	66 0f ef c0          	pxor   xmm0,xmm0
    e159:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    e15d:	f3 0f 7f 00          	movdqu XMMWORD PTR [rax],xmm0
    e161:	c6 47 14 01          	mov    BYTE PTR [rdi+0x14],0x1
    e165:	44 8b 75 90          	mov    r14d,DWORD PTR [rbp-0x70]
    e169:	44 88 77 11          	mov    BYTE PTR [rdi+0x11],r14b
    e16d:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    e171:	48 89 47 08          	mov    QWORD PTR [rdi+0x8],rax
    e175:	66 89 5f 36          	mov    WORD PTR [rdi+0x36],bx
    e179:	66 41 89 1f          	mov    WORD PTR [r15],bx
    e17d:	be 01 00 00 00       	mov    esi,0x1
    e182:	e8 f9 0f 00 00       	call   f180 <zbtScoreUpdatePath>
    e187:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    e18b:	e9 65 fc ff ff       	jmp    ddf5 <zbtScoreInsertAt+0x1745>
    e190:	48 8b 85 70 ff ff ff 	mov    rax,QWORD PTR [rbp-0x90]
    e197:	4d 8d 0c 06          	lea    r9,[r14+rax*1]
    e19b:	49 ff c1             	inc    r9
    e19e:	4c 0f af 4d a0       	imul   r9,QWORD PTR [rbp-0x60]
    e1a3:	49 83 c1 c0          	add    r9,0xffffffffffffffc0
    e1a7:	49 83 c3 c0          	add    r11,0xffffffffffffffc0
    e1ab:	eb 11                	jmp    e1be <zbtScoreInsertAt+0x1b0e>
    e1ad:	49 83 c1 c0          	add    r9,0xffffffffffffffc0
    e1b1:	49 83 c3 c0          	add    r11,0xffffffffffffffc0
    e1b5:	49 ff ca             	dec    r10
    e1b8:	0f 84 a1 f1 ff ff    	je     d35f <zbtScoreInsertAt+0xcaf>
    e1be:	4c 89 d9             	mov    rcx,r11
    e1c1:	48 c1 e9 03          	shr    rcx,0x3
    e1c5:	49 8b 54 0d 00       	mov    rdx,QWORD PTR [r13+rcx*1+0x0]
    e1ca:	89 f1                	mov    ecx,esi
    e1cc:	48 d3 ea             	shr    rdx,cl
    e1cf:	4c 89 cb             	mov    rbx,r9
    e1d2:	44 89 cf             	mov    edi,r9d
    e1d5:	83 e7 07             	and    edi,0x7
    e1d8:	89 f9                	mov    ecx,edi
    e1da:	f7 d9                	neg    ecx
    e1dc:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    e1e3:	49 d3 e0             	shl    r8,cl
    e1e6:	48 c1 eb 03          	shr    rbx,0x3
    e1ea:	49 f7 d0             	not    r8
    e1ed:	83 ff 01             	cmp    edi,0x1
    e1f0:	41 be 00 00 00 00    	mov    r14d,0x0
    e1f6:	4d 19 f6             	sbb    r14,r14
    e1f9:	4d 09 c6             	or     r14,r8
    e1fc:	4d 89 f0             	mov    r8,r14
    e1ff:	89 f9                	mov    ecx,edi
    e201:	49 d3 e0             	shl    r8,cl
    e204:	49 f7 d0             	not    r8
    e207:	4d 23 44 1d 00       	and    r8,QWORD PTR [r13+rbx*1+0x0]
    e20c:	49 21 d6             	and    r14,rdx
    e20f:	49 d3 e6             	shl    r14,cl
    e212:	4d 09 c6             	or     r14,r8
    e215:	4d 89 74 1d 00       	mov    QWORD PTR [r13+rbx*1+0x0],r14
    e21a:	85 ff                	test   edi,edi
    e21c:	74 8f                	je     e1ad <zbtScoreInsertAt+0x1afd>
    e21e:	41 b8 40 00 00 00    	mov    r8d,0x40
    e224:	41 29 f8             	sub    r8d,edi
    e227:	41 be 7e 00 00 00    	mov    r14d,0x7e
    e22d:	89 f9                	mov    ecx,edi
    e22f:	41 d3 ee             	shr    r14d,cl
    e232:	41 d3 e6             	shl    r14d,cl
    e235:	41 0f b6 7c 1d 08    	movzx  edi,BYTE PTR [r13+rbx*1+0x8]
    e23b:	44 89 f0             	mov    eax,r14d
    e23e:	83 f0 7f             	xor    eax,0x7f
    e241:	41 81 ce 80 00 00 00 	or     r14d,0x80
    e248:	44 89 c1             	mov    ecx,r8d
    e24b:	48 d3 ea             	shr    rdx,cl
    e24e:	41 21 fe             	and    r14d,edi
    e251:	21 c2                	and    edx,eax
    e253:	44 09 f2             	or     edx,r14d
    e256:	41 88 54 1d 08       	mov    BYTE PTR [r13+rbx*1+0x8],dl
    e25b:	e9 4d ff ff ff       	jmp    e1ad <zbtScoreInsertAt+0x1afd>
    e260:	66 41 89 54 24 01    	mov    WORD PTR [r12+0x1],dx
    e266:	bf 03 00 00 00       	mov    edi,0x3
    e26b:	b0 fe                	mov    al,0xfe
    e26d:	44 8b 75 90          	mov    r14d,DWORD PTR [rbp-0x70]
    e271:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    e275:	41 88 04 24          	mov    BYTE PTR [r12],al
    e279:	4c 01 e7             	add    rdi,r12
    e27c:	e8 9f 2e ff ff       	call   1120 <memcpy@plt>
    e281:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e285:	e9 df fe ff ff       	jmp    e169 <zbtScoreInsertAt+0x1ab9>

Disassembly of section .fini:
