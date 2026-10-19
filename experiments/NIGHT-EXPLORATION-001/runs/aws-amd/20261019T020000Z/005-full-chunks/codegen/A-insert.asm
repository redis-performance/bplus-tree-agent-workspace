
scratch/amd-chunk-build/A/build/native/btree-bench:     file format elf64-x86-64


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
    c6ca:	48 89 bd 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdi
    c6d1:	41 0f b6 41 13       	movzx  eax,BYTE PTR [r9+0x13]
    c6d6:	88 45 c8             	mov    BYTE PTR [rbp-0x38],al
    c6d9:	0f b6 7e 11          	movzx  edi,BYTE PTR [rsi+0x11]
    c6dd:	41 09 c8             	or     r8d,ecx
    c6e0:	74 2d                	je     c70f <zbtScoreInsertAt+0x5f>
    c6e2:	40 80 ff 60          	cmp    dil,0x60
    c6e6:	75 27                	jne    c70f <zbtScoreInsertAt+0x5f>
    c6e8:	0f b6 4d c8          	movzx  ecx,BYTE PTR [rbp-0x38]
    c6ec:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    c6f3:	4c 89 da             	mov    rdx,r11
    c6f6:	45 89 d0             	mov    r8d,r10d
    c6f9:	48 81 c4 18 14 00 00 	add    rsp,0x1418
    c700:	5b                   	pop    rbx
    c701:	41 5c                	pop    r12
    c703:	41 5d                	pop    r13
    c705:	41 5e                	pop    r14
    c707:	41 5f                	pop    r15
    c709:	5d                   	pop    rbp
    c70a:	e9 71 1b 00 00       	jmp    e280 <zbtScoreInsertEdgeLeaf>
    c70f:	40 0f b6 c7          	movzx  eax,dil
    c713:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    c717:	40 80 ff 5f          	cmp    dil,0x5f
    c71b:	48 89 f0             	mov    rax,rsi
    c71e:	48 89 75 d0          	mov    QWORD PTR [rbp-0x30],rsi
    c722:	4c 89 5d a8          	mov    QWORD PTR [rbp-0x58],r11
    c726:	40 88 7d 90          	mov    BYTE PTR [rbp-0x70],dil
    c72a:	77 5e                	ja     c78a <zbtScoreInsertAt+0xda>
    c72c:	66 49 0f 7e c7       	movq   r15,xmm0
    c731:	4d 85 ff             	test   r15,r15
    c734:	78 26                	js     c75c <zbtScoreInsertAt+0xac>
    c736:	48 b8 00 00 00 00 00 	movabs rax,0x8000000000000000
    c73d:	00 00 80
    c740:	49 09 c7             	or     r15,rax
    c743:	0f b6 46 35          	movzx  eax,BYTE PTR [rsi+0x35]
    c747:	48 8b 4e 28          	mov    rcx,QWORD PTR [rsi+0x28]
    c74b:	84 c0                	test   al,al
    c74d:	74 1c                	je     c76b <zbtScoreInsertAt+0xbb>
    c74f:	49 39 cf             	cmp    r15,rcx
    c752:	77 36                	ja     c78a <zbtScoreInsertAt+0xda>
    c754:	4c 29 f9             	sub    rcx,r15
    c757:	49 89 cf             	mov    r15,rcx
    c75a:	eb 14                	jmp    c770 <zbtScoreInsertAt+0xc0>
    c75c:	49 f7 d7             	not    r15
    c75f:	0f b6 46 35          	movzx  eax,BYTE PTR [rsi+0x35]
    c763:	48 8b 4e 28          	mov    rcx,QWORD PTR [rsi+0x28]
    c767:	84 c0                	test   al,al
    c769:	75 e4                	jne    c74f <zbtScoreInsertAt+0x9f>
    c76b:	49 29 cf             	sub    r15,rcx
    c76e:	72 1a                	jb     c78a <zbtScoreInsertAt+0xda>
    c770:	0f b6 4e 13          	movzx  ecx,BYTE PTR [rsi+0x13]
    c774:	49 c7 c1 ff ff ff ff 	mov    r9,0xffffffffffffffff
    c77b:	49 d3 e1             	shl    r9,cl
    c77e:	49 f7 d1             	not    r9
    c781:	4d 85 cf             	test   r15,r9
    c784:	0f 84 92 06 00 00    	je     ce1c <zbtScoreInsertAt+0x76c>
    c78a:	44 89 85 70 ff ff ff 	mov    DWORD PTR [rbp-0x90],r8d
    c791:	44 89 95 60 ff ff ff 	mov    DWORD PTR [rbp-0xa0],r10d
    c798:	4c 8d 76 38          	lea    r14,[rsi+0x38]
    c79c:	89 95 68 ff ff ff    	mov    DWORD PTR [rbp-0x98],edx
    c7a2:	41 89 d0             	mov    r8d,edx
    c7a5:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
    c7a9:	48 ff c0             	inc    rax
    c7ac:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    c7b0:	4b 8d 04 80          	lea    rax,[r8+r8*4]
    c7b4:	48 89 85 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],rax
    c7bb:	48 8d 04 c5 d0 eb ff 	lea    rax,[rax*8-0x1430]
    c7c2:	ff
    c7c3:	48 01 e8             	add    rax,rbp
    c7c6:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    c7ca:	45 31 e4             	xor    r12d,r12d
    c7cd:	89 f9                	mov    ecx,edi
    c7cf:	48 8d 9d d0 eb ff ff 	lea    rbx,[rbp-0x1430]
    c7d6:	49 ba ff ff ff ff ff 	movabs r10,0x7fffffffffffffff
    c7dd:	ff ff 7f
    c7e0:	45 31 ff             	xor    r15d,r15d
    c7e3:	4c 89 75 a0          	mov    QWORD PTR [rbp-0x60],r14
    c7e7:	4c 89 45 98          	mov    QWORD PTR [rbp-0x68],r8
    c7eb:	66 0f d6 45 88       	movq   QWORD PTR [rbp-0x78],xmm0
    c7f0:	eb 5c                	jmp    c84e <zbtScoreInsertAt+0x19e>
    c7f2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c7f9:	1f 84 00 00 00 00 00
    c800:	66 42 0f d6 84 c5 00 	movq   QWORD PTR [rbp+r8*8-0x500],xmm0
    c807:	fb ff ff
    c80a:	49 8b 43 20          	mov    rax,QWORD PTR [r11+0x20]
    c80e:	48 8b 55 80          	mov    rdx,QWORD PTR [rbp-0x80]
    c812:	48 89 42 20          	mov    QWORD PTR [rdx+0x20],rax
    c816:	41 0f 10 13          	movups xmm2,XMMWORD PTR [r11]
    c81a:	41 0f 10 4b 10       	movups xmm1,XMMWORD PTR [r11+0x10]
    c81f:	0f 11 4a 10          	movups XMMWORD PTR [rdx+0x10],xmm1
    c823:	0f 11 12             	movups XMMWORD PTR [rdx],xmm2
    c826:	0f b6 45 c8          	movzx  eax,BYTE PTR [rbp-0x38]
    c82a:	42 88 84 05 e0 fe ff 	mov    BYTE PTR [rbp+r8*1-0x120],al
    c831:	ff
    c832:	66 42 c7 84 45 10 fe 	mov    WORD PTR [rbp+r8*2-0x1f0],0x0
    c839:	ff ff 00 00
    c83d:	49 ff c4             	inc    r12
    c840:	48 83 c3 28          	add    rbx,0x28
    c844:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    c848:	0f 84 7b 02 00 00    	je     cac9 <zbtScoreInsertAt+0x419>
    c84e:	4d 39 e0             	cmp    r8,r12
    c851:	74 ad                	je     c800 <zbtScoreInsertAt+0x150>
    c853:	0f b6 46 34          	movzx  eax,BYTE PTR [rsi+0x34]
    c857:	44 0f b6 5e 35       	movzx  r11d,BYTE PTR [rsi+0x35]
    c85c:	0f b6 d1             	movzx  edx,cl
    c85f:	45 89 fd             	mov    r13d,r15d
    c862:	41 f7 d5             	not    r13d
    c865:	85 c0                	test   eax,eax
    c867:	0f 84 7f 00 00 00    	je     c8ec <zbtScoreInsertAt+0x23c>
    c86d:	46 8d 04 2a          	lea    r8d,[rdx+r13*1]
    c871:	45 84 db             	test   r11b,r11b
    c874:	45 0f 44 c7          	cmove  r8d,r15d
    c878:	4c 0f af c0          	imul   r8,rax
    c87c:	4d 89 c1             	mov    r9,r8
    c87f:	49 c1 e9 03          	shr    r9,0x3
    c883:	4b 8b 3c 0e          	mov    rdi,QWORD PTR [r14+r9*1]
    c887:	44 89 c1             	mov    ecx,r8d
    c88a:	80 e1 07             	and    cl,0x7
    c88d:	48 d3 ef             	shr    rdi,cl
    c890:	41 83 e0 07          	and    r8d,0x7
    c894:	74 2a                	je     c8c0 <zbtScoreInsertAt+0x210>
    c896:	b9 40 00 00 00       	mov    ecx,0x40
    c89b:	44 29 c1             	sub    ecx,r8d
    c89e:	39 c1                	cmp    ecx,eax
    c8a0:	73 1e                	jae    c8c0 <zbtScoreInsertAt+0x210>
    c8a2:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    c8a6:	45 0f b6 44 31 40    	movzx  r8d,BYTE PTR [r9+rsi*1+0x40]
    c8ac:	49 ba ff ff ff ff ff 	movabs r10,0x7fffffffffffffff
    c8b3:	ff ff 7f
    c8b6:	49 d3 e0             	shl    r8,cl
    c8b9:	4c 09 c7             	or     rdi,r8
    c8bc:	eb 06                	jmp    c8c4 <zbtScoreInsertAt+0x214>
    c8be:	66 90                	xchg   ax,ax
    c8c0:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    c8c4:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    c8cb:	89 c1                	mov    ecx,eax
    c8cd:	49 d3 e0             	shl    r8,cl
    c8d0:	3c 40                	cmp    al,0x40
    c8d2:	49 f7 d0             	not    r8
    c8d5:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
    c8dc:	4c 0f 43 c1          	cmovae r8,rcx
    c8e0:	49 21 f8             	and    r8,rdi
    c8e3:	0f b6 4e 13          	movzx  ecx,BYTE PTR [rsi+0x13]
    c8e7:	49 d3 e0             	shl    r8,cl
    c8ea:	eb 03                	jmp    c8ef <zbtScoreInsertAt+0x23f>
    c8ec:	45 31 c0             	xor    r8d,r8d
    c8ef:	4c 89 c1             	mov    rcx,r8
    c8f2:	48 f7 d9             	neg    rcx
    c8f5:	45 84 db             	test   r11b,r11b
    c8f8:	49 0f 44 c8          	cmove  rcx,r8
    c8fc:	48 03 4e 28          	add    rcx,QWORD PTR [rsi+0x28]
    c900:	48 89 cf             	mov    rdi,rcx
    c903:	4c 21 d7             	and    rdi,r10
    c906:	48 85 c9             	test   rcx,rcx
    c909:	48 f7 d1             	not    rcx
    c90c:	48 0f 48 cf          	cmovs  rcx,rdi
    c910:	4a 89 8c e5 00 fb ff 	mov    QWORD PTR [rbp+r12*8-0x500],rcx
    c917:	ff
    c918:	48 85 c0             	test   rax,rax
    c91b:	74 11                	je     c92e <zbtScoreInsertAt+0x27e>
    c91d:	0f af c2             	imul   eax,edx
    c920:	83 c0 07             	add    eax,0x7
    c923:	c1 e8 03             	shr    eax,0x3
    c926:	83 c0 09             	add    eax,0x9
    c929:	83 e0 fe             	and    eax,0xfffffffe
    c92c:	eb 02                	jmp    c930 <zbtScoreInsertAt+0x280>
    c92e:	31 c0                	xor    eax,eax
    c930:	44 01 ea             	add    edx,r13d
    c933:	45 84 db             	test   r11b,r11b
    c936:	44 89 7d c0          	mov    DWORD PTR [rbp-0x40],r15d
    c93a:	41 0f 44 d7          	cmove  edx,r15d
    c93e:	4c 01 f0             	add    rax,r14
    c941:	0f b7 04 50          	movzx  eax,WORD PTR [rax+rdx*2]
    c945:	4c 8d 3c 06          	lea    r15,[rsi+rax*1]
    c949:	0f b6 04 06          	movzx  eax,BYTE PTR [rsi+rax*1]
    c94d:	48 3d fd 00 00 00    	cmp    rax,0xfd
    c953:	77 0b                	ja     c960 <zbtScoreInsertAt+0x2b0>
    c955:	b9 01 00 00 00       	mov    ecx,0x1
    c95a:	4c 8b 5d a8          	mov    r11,QWORD PTR [rbp-0x58]
    c95e:	eb 15                	jmp    c975 <zbtScoreInsertAt+0x2c5>
    c960:	3d fe 00 00 00       	cmp    eax,0xfe
    c965:	4c 8b 5d a8          	mov    r11,QWORD PTR [rbp-0x58]
    c969:	75 1e                	jne    c989 <zbtScoreInsertAt+0x2d9>
    c96b:	41 0f b7 47 01       	movzx  eax,WORD PTR [r15+0x1]
    c970:	b9 03 00 00 00       	mov    ecx,0x3
    c975:	48 89 43 08          	mov    QWORD PTR [rbx+0x8],rax
    c979:	49 01 cf             	add    r15,rcx
    c97c:	4c 89 3b             	mov    QWORD PTR [rbx],r15
    c97f:	31 c0                	xor    eax,eax
    c981:	45 31 f6             	xor    r14d,r14d
    c984:	45 31 ff             	xor    r15d,r15d
    c987:	eb 1c                	jmp    c9a5 <zbtScoreInsertAt+0x2f5>
    c989:	4d 8b 77 0d          	mov    r14,QWORD PTR [r15+0xd]
    c98d:	4d 85 f6             	test   r14,r14
    c990:	0f 84 af 00 00 00    	je     ca45 <zbtScoreInsertAt+0x395>
    c996:	49 8b 47 05          	mov    rax,QWORD PTR [r15+0x5]
    c99a:	48 89 43 08          	mov    QWORD PTR [rbx+0x8],rax
    c99e:	4c 89 33             	mov    QWORD PTR [rbx],r14
    c9a1:	41 8b 47 01          	mov    eax,DWORD PTR [r15+0x1]
    c9a5:	89 43 10             	mov    DWORD PTR [rbx+0x10],eax
    c9a8:	4c 89 73 18          	mov    QWORD PTR [rbx+0x18],r14
    c9ac:	4c 89 7b 20          	mov    QWORD PTR [rbx+0x20],r15
    c9b0:	0f b6 46 34          	movzx  eax,BYTE PTR [rsi+0x34]
    c9b4:	0f b6 4e 11          	movzx  ecx,BYTE PTR [rsi+0x11]
    c9b8:	0f b6 d1             	movzx  edx,cl
    c9bb:	48 85 c0             	test   rax,rax
    c9be:	74 13                	je     c9d3 <zbtScoreInsertAt+0x323>
    c9c0:	89 d7                	mov    edi,edx
    c9c2:	0f af f8             	imul   edi,eax
    c9c5:	83 c7 07             	add    edi,0x7
    c9c8:	c1 ef 03             	shr    edi,0x3
    c9cb:	83 c7 09             	add    edi,0x9
    c9ce:	83 e7 fe             	and    edi,0xfffffffe
    c9d1:	eb 02                	jmp    c9d5 <zbtScoreInsertAt+0x325>
    c9d3:	31 ff                	xor    edi,edi
    c9d5:	4c 8b 75 a0          	mov    r14,QWORD PTR [rbp-0x60]
    c9d9:	4c 8b 45 98          	mov    r8,QWORD PTR [rbp-0x68]
    c9dd:	44 8b 7d c0          	mov    r15d,DWORD PTR [rbp-0x40]
    c9e1:	4c 01 f7             	add    rdi,r14
    c9e4:	41 89 d1             	mov    r9d,edx
    c9e7:	45 01 e9             	add    r9d,r13d
    c9ea:	80 7e 35 00          	cmp    BYTE PTR [rsi+0x35],0x0
    c9ee:	45 0f 44 cf          	cmove  r9d,r15d
    c9f2:	48 8d 3c 57          	lea    rdi,[rdi+rdx*2]
    c9f6:	41 0f b6 3c 39       	movzx  edi,BYTE PTR [r9+rdi*1]
    c9fb:	42 88 bc 25 e0 fe ff 	mov    BYTE PTR [rbp+r12*1-0x120],dil
    ca02:	ff
    ca03:	48 85 c0             	test   rax,rax
    ca06:	74 11                	je     ca19 <zbtScoreInsertAt+0x369>
    ca08:	0f af c2             	imul   eax,edx
    ca0b:	83 c0 07             	add    eax,0x7
    ca0e:	c1 e8 03             	shr    eax,0x3
    ca11:	83 c0 09             	add    eax,0x9
    ca14:	83 e0 fe             	and    eax,0xfffffffe
    ca17:	eb 02                	jmp    ca1b <zbtScoreInsertAt+0x36b>
    ca19:	31 c0                	xor    eax,eax
    ca1b:	4c 01 f0             	add    rax,r14
    ca1e:	42 0f b7 04 48       	movzx  eax,WORD PTR [rax+r9*2]
    ca23:	66 42 89 84 65 10 fe 	mov    WORD PTR [rbp+r12*2-0x1f0],ax
    ca2a:	ff ff
    ca2c:	41 ff c7             	inc    r15d
    ca2f:	49 ff c4             	inc    r12
    ca32:	48 83 c3 28          	add    rbx,0x28
    ca36:	4c 39 65 b8          	cmp    QWORD PTR [rbp-0x48],r12
    ca3a:	0f 85 0e fe ff ff    	jne    c84e <zbtScoreInsertAt+0x19e>
    ca40:	e9 84 00 00 00       	jmp    cac9 <zbtScoreInsertAt+0x419>
    ca45:	48 8d 3d d2 6b 00 00 	lea    rdi,[rip+0x6bd2]        # 1361e <_IO_stdin_used+0x61e>
    ca4c:	be 5e 02 00 00       	mov    esi,0x25e
    ca51:	48 8d 15 f2 6c 00 00 	lea    rdx,[rip+0x6cf2]        # 1374a <_IO_stdin_used+0x74a>
    ca58:	e8 b3 50 00 00       	call   11b10 <standalone_panic>
    ca5d:	49 ba ff ff ff ff ff 	movabs r10,0x7fffffffffffffff
    ca64:	ff ff 7f
    ca67:	f3 0f 7e 45 88       	movq   xmm0,QWORD PTR [rbp-0x78]
    ca6c:	4c 8b 5d a8          	mov    r11,QWORD PTR [rbp-0x58]
    ca70:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    ca74:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    ca78:	0f 84 18 ff ff ff    	je     c996 <zbtScoreInsertAt+0x2e6>
    ca7e:	48 8d 3d 99 6b 00 00 	lea    rdi,[rip+0x6b99]        # 1361e <_IO_stdin_used+0x61e>
    ca85:	be 3e 02 00 00       	mov    esi,0x23e
    ca8a:	48 8d 15 c5 6c 00 00 	lea    rdx,[rip+0x6cc5]        # 13756 <_IO_stdin_used+0x756>
    ca91:	e8 7a 50 00 00       	call   11b10 <standalone_panic>
    ca96:	49 ba ff ff ff ff ff 	movabs r10,0x7fffffffffffffff
    ca9d:	ff ff 7f
    caa0:	f3 0f 7e 45 88       	movq   xmm0,QWORD PTR [rbp-0x78]
    caa5:	4c 8b 5d a8          	mov    r11,QWORD PTR [rbp-0x58]
    caa9:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    caad:	41 0f b6 07          	movzx  eax,BYTE PTR [r15]
    cab1:	49 8b 4f 05          	mov    rcx,QWORD PTR [r15+0x5]
    cab5:	48 89 4b 08          	mov    QWORD PTR [rbx+0x8],rcx
    cab9:	4c 89 33             	mov    QWORD PTR [rbx],r14
    cabc:	3c ff                	cmp    al,0xff
    cabe:	0f 85 bb fe ff ff    	jne    c97f <zbtScoreInsertAt+0x2cf>
    cac4:	e9 d8 fe ff ff       	jmp    c9a1 <zbtScoreInsertAt+0x2f1>
    cac9:	4c 89 da             	mov    rdx,r11
    cacc:	f3 0f 7e 8d 00 fb ff 	movq   xmm1,QWORD PTR [rbp-0x500]
    cad3:	ff
    cad4:	66 49 0f 7e cd       	movq   r13,xmm1
    cad9:	4d 85 ed             	test   r13,r13
    cadc:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    cae3:	00 00 80
    cae6:	4d 89 eb             	mov    r11,r13
    cae9:	78 05                	js     caf0 <zbtScoreInsertAt+0x440>
    caeb:	4d 09 fb             	or     r11,r15
    caee:	eb 03                	jmp    caf3 <zbtScoreInsertAt+0x443>
    caf0:	49 f7 d3             	not    r11
    caf3:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    caf7:	0f b6 45 90          	movzx  eax,BYTE PTR [rbp-0x70]
    cafb:	44 8b b5 70 ff ff ff 	mov    r14d,DWORD PTR [rbp-0x90]
    cb02:	bb 38 00 00 00       	mov    ebx,0x38
    cb07:	84 c0                	test   al,al
    cb09:	0f 84 99 00 00 00    	je     cba8 <zbtScoreInsertAt+0x4f8>
    cb0f:	45 31 c0             	xor    r8d,r8d
    cb12:	4c 89 df             	mov    rdi,r11
    cb15:	31 c9                	xor    ecx,ecx
    cb17:	4c 89 d8             	mov    rax,r11
    cb1a:	eb 26                	jmp    cb42 <zbtScoreInsertAt+0x492>
    cb1c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    cb20:	49 f7 d1             	not    r9
    cb23:	4d 89 ca             	mov    r10,r9
    cb26:	4d 31 da             	xor    r10,r11
    cb29:	4c 09 d1             	or     rcx,r10
    cb2c:	49 39 f9             	cmp    r9,rdi
    cb2f:	49 0f 42 f9          	cmovb  rdi,r9
    cb33:	49 39 c1             	cmp    r9,rax
    cb36:	49 0f 47 c1          	cmova  rax,r9
    cb3a:	49 ff c0             	inc    r8
    cb3d:	4d 39 c4             	cmp    r12,r8
    cb40:	74 19                	je     cb5b <zbtScoreInsertAt+0x4ab>
    cb42:	f3 42 0f 7e 8c c5 08 	movq   xmm1,QWORD PTR [rbp+r8*8-0x4f8]
    cb49:	fb ff ff
    cb4c:	66 49 0f 7e c9       	movq   r9,xmm1
    cb51:	4d 85 c9             	test   r9,r9
    cb54:	78 ca                	js     cb20 <zbtScoreInsertAt+0x470>
    cb56:	4d 09 f9             	or     r9,r15
    cb59:	eb c8                	jmp    cb23 <zbtScoreInsertAt+0x473>
    cb5b:	48 85 c9             	test   rcx,rcx
    cb5e:	74 44                	je     cba4 <zbtScoreInsertAt+0x4f4>
    cb60:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    cb65:	48 29 f8             	sub    rax,rdi
    cb68:	48 d3 e8             	shr    rax,cl
    cb6b:	48 85 c0             	test   rax,rax
    cb6e:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    cb72:	74 34                	je     cba8 <zbtScoreInsertAt+0x4f8>
    cb74:	48 0f bd c0          	bsr    rax,rax
    cb78:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    cb7c:	48 83 c0 41          	add    rax,0x41
    cb80:	48 0f af 45 b8       	imul   rax,QWORD PTR [rbp-0x48]
    cb85:	48 83 c0 07          	add    rax,0x7
    cb89:	48 c1 e8 03          	shr    rax,0x3
    cb8d:	48 83 c0 09          	add    rax,0x9
    cb91:	48 bb fe ff ff ff ff 	movabs rbx,0x1ffffffffffffffe
    cb98:	ff ff 1f
    cb9b:	48 21 c3             	and    rbx,rax
    cb9e:	48 83 c3 38          	add    rbx,0x38
    cba2:	eb 04                	jmp    cba8 <zbtScoreInsertAt+0x4f8>
    cba4:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    cba8:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    cbac:	48 8d 04 40          	lea    rax,[rax+rax*2]
    cbb0:	48 01 c3             	add    rbx,rax
    cbb3:	4b 8d 0c a4          	lea    rcx,[r12+r12*4]
    cbb7:	48 8d 0c cd 28 00 00 	lea    rcx,[rcx*8+0x28]
    cbbe:	00
    cbbf:	45 31 c9             	xor    r9d,r9d
    cbc2:	eb 18                	jmp    cbdc <zbtScoreInsertAt+0x52c>
    cbc4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    cbcb:	00 00 00 00 00
    cbd0:	48 01 fb             	add    rbx,rdi
    cbd3:	49 83 c1 28          	add    r9,0x28
    cbd7:	4c 39 c9             	cmp    rcx,r9
    cbda:	74 37                	je     cc13 <zbtScoreInsertAt+0x563>
    cbdc:	bf 15 00 00 00       	mov    edi,0x15
    cbe1:	4a 83 bc 0d e8 eb ff 	cmp    QWORD PTR [rbp+r9*1-0x1418],0x0
    cbe8:	ff 00
    cbea:	75 e4                	jne    cbd0 <zbtScoreInsertAt+0x520>
    cbec:	4e 8b 84 0d d8 eb ff 	mov    r8,QWORD PTR [rbp+r9*1-0x1428]
    cbf3:	ff
    cbf4:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    cbfb:	77 d3                	ja     cbd0 <zbtScoreInsertAt+0x520>
    cbfd:	31 ff                	xor    edi,edi
    cbff:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    cc06:	40 0f 93 c7          	setae  dil
    cc0a:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    cc0e:	48 ff c7             	inc    rdi
    cc11:	eb bd                	jmp    cbd0 <zbtScoreInsertAt+0x520>
    cc13:	45 85 f6             	test   r14d,r14d
    cc16:	74 25                	je     cc3d <zbtScoreInsertAt+0x58d>
    cc18:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    cc1f:	72 1c                	jb     cc3d <zbtScoreInsertAt+0x58d>
    cc21:	0f b6 4d c8          	movzx  ecx,BYTE PTR [rbp-0x38]
    cc25:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    cc2c:	44 8b 85 60 ff ff ff 	mov    r8d,DWORD PTR [rbp-0xa0]
    cc33:	e8 48 16 00 00       	call   e280 <zbtScoreInsertEdgeLeaf>
    cc38:	e9 c8 11 00 00       	jmp    de05 <zbtScoreInsertAt+0x1755>
    cc3d:	44 0f b6 45 90       	movzx  r8d,BYTE PTR [rbp-0x70]
    cc42:	41 80 f8 5f          	cmp    r8b,0x5f
    cc46:	77 77                	ja     ccbf <zbtScoreInsertAt+0x60f>
    cc48:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    cc4f:	73 6e                	jae    ccbf <zbtScoreInsertAt+0x60f>
    cc51:	4d 85 ed             	test   r13,r13
    cc54:	0f 88 e3 02 00 00    	js     cf3d <zbtScoreInsertAt+0x88d>
    cc5a:	4d 09 fd             	or     r13,r15
    cc5d:	45 84 c0             	test   r8b,r8b
    cc60:	0f 84 e3 02 00 00    	je     cf49 <zbtScoreInsertAt+0x899>
    cc66:	0f b6 7e 35          	movzx  edi,BYTE PTR [rsi+0x35]
    cc6a:	45 31 c0             	xor    r8d,r8d
    cc6d:	4c 89 e9             	mov    rcx,r13
    cc70:	31 f6                	xor    esi,esi
    cc72:	4c 89 ea             	mov    rdx,r13
    cc75:	48 8b 9d 50 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xb0]
    cc7c:	eb 28                	jmp    cca6 <zbtScoreInsertAt+0x5f6>
    cc7e:	66 90                	xchg   ax,ax
    cc80:	49 f7 d1             	not    r9
    cc83:	4d 89 ca             	mov    r10,r9
    cc86:	4d 31 ea             	xor    r10,r13
    cc89:	4c 09 d6             	or     rsi,r10
    cc8c:	49 39 c9             	cmp    r9,rcx
    cc8f:	49 0f 42 c9          	cmovb  rcx,r9
    cc93:	49 39 d1             	cmp    r9,rdx
    cc96:	49 0f 47 d1          	cmova  rdx,r9
    cc9a:	49 ff c0             	inc    r8
    cc9d:	4d 39 c4             	cmp    r12,r8
    cca0:	0f 84 18 01 00 00    	je     cdbe <zbtScoreInsertAt+0x70e>
    cca6:	f3 42 0f 7e 84 c5 08 	movq   xmm0,QWORD PTR [rbp+r8*8-0x4f8]
    ccad:	fb ff ff
    ccb0:	66 49 0f 7e c1       	movq   r9,xmm0
    ccb5:	4d 85 c9             	test   r9,r9
    ccb8:	78 c6                	js     cc80 <zbtScoreInsertAt+0x5d0>
    ccba:	4d 09 f9             	or     r9,r15
    ccbd:	eb c4                	jmp    cc83 <zbtScoreInsertAt+0x5d3>
    ccbf:	31 d2                	xor    edx,edx
    ccc1:	31 c0                	xor    eax,eax
    ccc3:	eb 1b                	jmp    cce0 <zbtScoreInsertAt+0x630>
    ccc5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    cccc:	00 00 00 00
    ccd0:	48 01 f0             	add    rax,rsi
    ccd3:	48 83 c0 0b          	add    rax,0xb
    ccd7:	48 83 c2 28          	add    rdx,0x28
    ccdb:	48 39 d1             	cmp    rcx,rdx
    ccde:	74 37                	je     cd17 <zbtScoreInsertAt+0x667>
    cce0:	be 15 00 00 00       	mov    esi,0x15
    cce5:	48 83 bc 15 e8 eb ff 	cmp    QWORD PTR [rbp+rdx*1-0x1418],0x0
    ccec:	ff 00
    ccee:	75 e0                	jne    ccd0 <zbtScoreInsertAt+0x620>
    ccf0:	48 8b bc 15 d8 eb ff 	mov    rdi,QWORD PTR [rbp+rdx*1-0x1428]
    ccf7:	ff
    ccf8:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    ccff:	77 cf                	ja     ccd0 <zbtScoreInsertAt+0x620>
    cd01:	31 f6                	xor    esi,esi
    cd03:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    cd0a:	40 0f 93 c6          	setae  sil
    cd0e:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    cd12:	48 ff c6             	inc    rsi
    cd15:	eb b9                	jmp    ccd0 <zbtScoreInsertAt+0x620>
    cd17:	45 84 c0             	test   r8b,r8b
    cd1a:	0f 84 53 01 00 00    	je     ce73 <zbtScoreInsertAt+0x7c3>
    cd20:	45 89 c2             	mov    r10d,r8d
    cd23:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cd27:	d1 e9                	shr    ecx,1
    cd29:	42 8d 14 e5 00 00 00 	lea    edx,[r12*8+0x0]
    cd30:	00
    cd31:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    cd35:	c7 45 c8 01 00 00 00 	mov    DWORD PTR [rbp-0x38],0x1
    cd3c:	31 f6                	xor    esi,esi
    cd3e:	31 ff                	xor    edi,edi
    cd40:	41 b8 15 00 00 00    	mov    r8d,0x15
    cd46:	48 83 bc 35 e8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1418],0x0
    cd4d:	ff 00
    cd4f:	75 2f                	jne    cd80 <zbtScoreInsertAt+0x6d0>
    cd51:	4c 8b 8c 35 d8 eb ff 	mov    r9,QWORD PTR [rbp+rsi*1-0x1428]
    cd58:	ff
    cd59:	49 81 f9 3f 01 00 00 	cmp    r9,0x13f
    cd60:	77 1e                	ja     cd80 <zbtScoreInsertAt+0x6d0>
    cd62:	45 31 c0             	xor    r8d,r8d
    cd65:	49 81 f9 fe 00 00 00 	cmp    r9,0xfe
    cd6c:	41 0f 93 c0          	setae  r8b
    cd70:	4f 8d 04 41          	lea    r8,[r9+r8*2]
    cd74:	49 ff c0             	inc    r8
    cd77:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    cd7e:	00 00
    cd80:	4e 8d 0c 07          	lea    r9,[rdi+r8*1]
    cd84:	4e 8d 0c 4d 16 00 00 	lea    r9,[r9*2+0x16]
    cd8b:	00
    cd8c:	49 39 c1             	cmp    r9,rax
    cd8f:	73 16                	jae    cda7 <zbtScoreInsertAt+0x6f7>
    cd91:	4c 01 c7             	add    rdi,r8
    cd94:	48 83 c7 0b          	add    rdi,0xb
    cd98:	ff 45 c8             	inc    DWORD PTR [rbp-0x38]
    cd9b:	48 83 c6 28          	add    rsi,0x28
    cd9f:	48 39 f2             	cmp    rdx,rsi
    cda2:	75 9c                	jne    cd40 <zbtScoreInsertAt+0x690>
    cda4:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    cda7:	45 89 d0             	mov    r8d,r10d
    cdaa:	4c 89 e9             	mov    rcx,r13
    cdad:	4d 85 ed             	test   r13,r13
    cdb0:	0f 88 d0 00 00 00    	js     ce86 <zbtScoreInsertAt+0x7d6>
    cdb6:	4c 09 f9             	or     rcx,r15
    cdb9:	e9 cb 00 00 00       	jmp    ce89 <zbtScoreInsertAt+0x7d9>
    cdbe:	40 84 ff             	test   dil,dil
    cdc1:	49 89 d5             	mov    r13,rdx
    cdc4:	4c 0f 44 e9          	cmove  r13,rcx
    cdc8:	48 85 f6             	test   rsi,rsi
    cdcb:	0f 84 22 02 00 00    	je     cff3 <zbtScoreInsertAt+0x943>
    cdd1:	f3 48 0f bc fe       	tzcnt  rdi,rsi
    cdd6:	48 29 ca             	sub    rdx,rcx
    cdd9:	89 f9                	mov    ecx,edi
    cddb:	48 d3 ea             	shr    rdx,cl
    cdde:	48 85 d2             	test   rdx,rdx
    cde1:	0f 84 94 03 00 00    	je     d17b <zbtScoreInsertAt+0xacb>
    cde7:	48 0f bd ca          	bsr    rcx,rdx
    cdeb:	83 f1 3f             	xor    ecx,0x3f
    cdee:	41 b0 40             	mov    r8b,0x40
    cdf1:	41 28 c8             	sub    r8b,cl
    cdf4:	41 0f b6 d0          	movzx  edx,r8b
    cdf8:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    cdfc:	41 89 ca             	mov    r10d,ecx
    cdff:	48 89 55 c8          	mov    QWORD PTR [rbp-0x38],rdx
    ce03:	44 0f af d2          	imul   r10d,edx
    ce07:	41 83 c2 07          	add    r10d,0x7
    ce0b:	41 c1 ea 03          	shr    r10d,0x3
    ce0f:	41 83 c2 09          	add    r10d,0x9
    ce13:	41 83 e2 fe          	and    r10d,0xfffffffe
    ce17:	e9 6b 03 00 00       	jmp    d187 <zbtScoreInsertAt+0xad7>
    ce1c:	49 d3 ef             	shr    r15,cl
    ce1f:	44 0f b6 66 34       	movzx  r12d,BYTE PTR [rsi+0x34]
    ce24:	45 85 e4             	test   r12d,r12d
    ce27:	0f 84 5d 04 00 00    	je     d28a <zbtScoreInsertAt+0xbda>
    ce2d:	4d 89 f9             	mov    r9,r15
    ce30:	44 89 e1             	mov    ecx,r12d
    ce33:	49 d3 e9             	shr    r9,cl
    ce36:	41 80 fc 3f          	cmp    r12b,0x3f
    ce3a:	77 09                	ja     ce45 <zbtScoreInsertAt+0x795>
    ce3c:	4d 85 c9             	test   r9,r9
    ce3f:	0f 85 45 f9 ff ff    	jne    c78a <zbtScoreInsertAt+0xda>
    ce45:	48 8b 4d b0          	mov    rcx,QWORD PTR [rbp-0x50]
    ce49:	44 8d 71 01          	lea    r14d,[rcx+0x1]
    ce4d:	45 89 e1             	mov    r9d,r12d
    ce50:	45 0f af ce          	imul   r9d,r14d
    ce54:	41 83 c1 07          	add    r9d,0x7
    ce58:	41 c1 e9 03          	shr    r9d,0x3
    ce5c:	41 83 c1 09          	add    r9d,0x9
    ce60:	41 81 e1 fe ff 00 00 	and    r9d,0xfffe
    ce67:	44 89 e1             	mov    ecx,r12d
    ce6a:	48 89 4d 98          	mov    QWORD PTR [rbp-0x68],rcx
    ce6e:	e9 31 04 00 00       	jmp    d2a4 <zbtScoreInsertAt+0xbf4>
    ce73:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    ce7a:	4c 89 e9             	mov    rcx,r13
    ce7d:	4d 85 ed             	test   r13,r13
    ce80:	0f 89 30 ff ff ff    	jns    cdb6 <zbtScoreInsertAt+0x706>
    ce86:	48 f7 d1             	not    rcx
    ce89:	8b 75 c8             	mov    esi,DWORD PTR [rbp-0x38]
    ce8c:	89 f0                	mov    eax,esi
    ce8e:	ba 38 00 00 00       	mov    edx,0x38
    ce93:	83 fe 02             	cmp    esi,0x2
    ce96:	0f 82 67 01 00 00    	jb     d003 <zbtScoreInsertAt+0x953>
    ce9c:	44 89 c3             	mov    ebx,r8d
    ce9f:	41 b9 01 00 00 00    	mov    r9d,0x1
    cea5:	31 ff                	xor    edi,edi
    cea7:	49 89 c8             	mov    r8,rcx
    ceaa:	48 89 ce             	mov    rsi,rcx
    cead:	eb 23                	jmp    ced2 <zbtScoreInsertAt+0x822>
    ceaf:	90                   	nop
    ceb0:	4d 09 fa             	or     r10,r15
    ceb3:	4d 89 d3             	mov    r11,r10
    ceb6:	49 31 cb             	xor    r11,rcx
    ceb9:	4c 09 df             	or     rdi,r11
    cebc:	4d 39 c2             	cmp    r10,r8
    cebf:	4d 0f 42 c2          	cmovb  r8,r10
    cec3:	49 39 f2             	cmp    r10,rsi
    cec6:	49 0f 47 f2          	cmova  rsi,r10
    ceca:	49 ff c1             	inc    r9
    cecd:	4c 39 c8             	cmp    rax,r9
    ced0:	74 19                	je     ceeb <zbtScoreInsertAt+0x83b>
    ced2:	f3 42 0f 7e 84 cd 00 	movq   xmm0,QWORD PTR [rbp+r9*8-0x500]
    ced9:	fb ff ff
    cedc:	66 49 0f 7e c2       	movq   r10,xmm0
    cee1:	4d 85 d2             	test   r10,r10
    cee4:	79 ca                	jns    ceb0 <zbtScoreInsertAt+0x800>
    cee6:	49 f7 d2             	not    r10
    cee9:	eb c8                	jmp    ceb3 <zbtScoreInsertAt+0x803>
    ceeb:	48 85 ff             	test   rdi,rdi
    ceee:	0f 84 0c 01 00 00    	je     d000 <zbtScoreInsertAt+0x950>
    cef4:	f3 48 0f bc cf       	tzcnt  rcx,rdi
    cef9:	4c 29 c6             	sub    rsi,r8
    cefc:	48 d3 ee             	shr    rsi,cl
    ceff:	48 85 f6             	test   rsi,rsi
    cf02:	41 89 d8             	mov    r8d,ebx
    cf05:	0f 84 f8 00 00 00    	je     d003 <zbtScoreInsertAt+0x953>
    cf0b:	48 0f bd ce          	bsr    rcx,rsi
    cf0f:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    cf13:	48 83 c1 41          	add    rcx,0x41
    cf17:	48 0f af c8          	imul   rcx,rax
    cf1b:	48 83 c1 07          	add    rcx,0x7
    cf1f:	48 c1 e9 03          	shr    rcx,0x3
    cf23:	48 83 c1 09          	add    rcx,0x9
    cf27:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    cf2e:	ff ff 1f
    cf31:	48 21 ca             	and    rdx,rcx
    cf34:	48 83 c2 38          	add    rdx,0x38
    cf38:	e9 c6 00 00 00       	jmp    d003 <zbtScoreInsertAt+0x953>
    cf3d:	49 f7 d5             	not    r13
    cf40:	45 84 c0             	test   r8b,r8b
    cf43:	0f 85 1d fd ff ff    	jne    cc66 <zbtScoreInsertAt+0x5b6>
    cf49:	31 c9                	xor    ecx,ecx
    cf4b:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    cf4f:	31 ff                	xor    edi,edi
    cf51:	45 31 c0             	xor    r8d,r8d
    cf54:	45 31 d2             	xor    r10d,r10d
    cf57:	48 8b 9d 50 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xb0]
    cf5e:	4c 01 d0             	add    rax,r10
    cf61:	48 83 c0 38          	add    rax,0x38
    cf65:	48 8b 94 dd e8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1418]
    cf6c:	ff
    cf6d:	48 85 d2             	test   rdx,rdx
    cf70:	0f 85 2d 02 00 00    	jne    d1a3 <zbtScoreInsertAt+0xaf3>
    cf76:	4c 8b 9c dd d8 eb ff 	mov    r11,QWORD PTR [rbp+rbx*8-0x1428]
    cf7d:	ff
    cf7e:	31 c9                	xor    ecx,ecx
    cf80:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    cf87:	0f 93 c1             	setae  cl
    cf8a:	49 81 fb 40 01 00 00 	cmp    r11,0x140
    cf91:	49 8d 54 4b 01       	lea    rdx,[r11+rcx*2+0x1]
    cf96:	b9 15 00 00 00       	mov    ecx,0x15
    cf9b:	48 0f 42 ca          	cmovb  rcx,rdx
    cf9f:	48 01 c8             	add    rax,rcx
    cfa2:	44 0f b7 66 36       	movzx  r12d,WORD PTR [rsi+0x36]
    cfa7:	4c 39 e0             	cmp    rax,r12
    cfaa:	0f 87 05 02 00 00    	ja     d1b5 <zbtScoreInsertAt+0xb05>
    cfb0:	41 29 cc             	sub    r12d,ecx
    cfb3:	45 0f b7 f4          	movzx  r14d,r12w
    cfb7:	49 01 f6             	add    r14,rsi
    cfba:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    cfc1:	48 89 7d a8          	mov    QWORD PTR [rbp-0x58],rdi
    cfc5:	4c 89 45 b0          	mov    QWORD PTR [rbp-0x50],r8
    cfc9:	0f 87 2f 0b 00 00    	ja     dafe <zbtScoreInsertAt+0x144e>
    cfcf:	48 8b 45 80          	mov    rax,QWORD PTR [rbp-0x80]
    cfd3:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    cfd6:	4c 89 d3             	mov    rbx,r10
    cfd9:	49 81 fb fd 00 00 00 	cmp    r11,0xfd
    cfe0:	0f 87 31 0e 00 00    	ja     de17 <zbtScoreInsertAt+0x1767>
    cfe6:	bf 01 00 00 00       	mov    edi,0x1
    cfeb:	44 89 d8             	mov    eax,r11d
    cfee:	e9 30 0e 00 00       	jmp    de23 <zbtScoreInsertAt+0x1773>
    cff3:	31 c9                	xor    ecx,ecx
    cff5:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    cff9:	31 ff                	xor    edi,edi
    cffb:	e9 81 01 00 00       	jmp    d181 <zbtScoreInsertAt+0xad1>
    d000:	41 89 d8             	mov    r8d,ebx
    d003:	45 89 c1             	mov    r9d,r8d
    d006:	48 8d 0c 40          	lea    rcx,[rax+rax*2]
    d00a:	48 01 d1             	add    rcx,rdx
    d00d:	83 7d c8 00          	cmp    DWORD PTR [rbp-0x38],0x0
    d011:	74 60                	je     d073 <zbtScoreInsertAt+0x9c3>
    d013:	48 8d 14 c5 00 00 00 	lea    rdx,[rax*8+0x0]
    d01a:	00
    d01b:	48 8d 14 92          	lea    rdx,[rdx+rdx*4]
    d01f:	31 f6                	xor    esi,esi
    d021:	eb 19                	jmp    d03c <zbtScoreInsertAt+0x98c>
    d023:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d02a:	84 00 00 00 00 00
    d030:	48 01 f9             	add    rcx,rdi
    d033:	48 83 c6 28          	add    rsi,0x28
    d037:	48 39 f2             	cmp    rdx,rsi
    d03a:	74 37                	je     d073 <zbtScoreInsertAt+0x9c3>
    d03c:	bf 15 00 00 00       	mov    edi,0x15
    d041:	48 83 bc 35 e8 eb ff 	cmp    QWORD PTR [rbp+rsi*1-0x1418],0x0
    d048:	ff 00
    d04a:	75 e4                	jne    d030 <zbtScoreInsertAt+0x980>
    d04c:	4c 8b 84 35 d8 eb ff 	mov    r8,QWORD PTR [rbp+rsi*1-0x1428]
    d053:	ff
    d054:	49 81 f8 3f 01 00 00 	cmp    r8,0x13f
    d05b:	77 d3                	ja     d030 <zbtScoreInsertAt+0x980>
    d05d:	31 ff                	xor    edi,edi
    d05f:	49 81 f8 fe 00 00 00 	cmp    r8,0xfe
    d066:	40 0f 93 c7          	setae  dil
    d06a:	49 8d 3c 78          	lea    rdi,[r8+rdi*2]
    d06e:	48 ff c7             	inc    rdi
    d071:	eb bd                	jmp    d030 <zbtScoreInsertAt+0x980>
    d073:	48 81 f9 ff 0f 00 00 	cmp    rcx,0xfff
    d07a:	45 89 c8             	mov    r8d,r9d
    d07d:	0f 87 11 04 00 00    	ja     d494 <zbtScoreInsertAt+0xde4>
    d083:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    d087:	89 cf                	mov    edi,ecx
    d089:	2b 7d c8             	sub    edi,DWORD PTR [rbp-0x38]
    d08c:	f3 0f 7e 84 c5 00 fb 	movq   xmm0,QWORD PTR [rbp+rax*8-0x500]
    d093:	ff ff
    d095:	66 48 0f 7e c1       	movq   rcx,xmm0
    d09a:	48 85 c9             	test   rcx,rcx
    d09d:	78 14                	js     d0b3 <zbtScoreInsertAt+0xa03>
    d09f:	4c 09 f9             	or     rcx,r15
    d0a2:	89 fa                	mov    edx,edi
    d0a4:	be 38 00 00 00       	mov    esi,0x38
    d0a9:	83 ff 02             	cmp    edi,0x2
    d0ac:	73 18                	jae    d0c6 <zbtScoreInsertAt+0xa16>
    d0ae:	e9 c1 03 00 00       	jmp    d474 <zbtScoreInsertAt+0xdc4>
    d0b3:	48 f7 d1             	not    rcx
    d0b6:	89 fa                	mov    edx,edi
    d0b8:	be 38 00 00 00       	mov    esi,0x38
    d0bd:	83 ff 02             	cmp    edi,0x2
    d0c0:	0f 82 ae 03 00 00    	jb     d474 <zbtScoreInsertAt+0xdc4>
    d0c6:	4c 8d 14 c5 00 fb ff 	lea    r10,[rax*8-0x500]
    d0cd:	ff
    d0ce:	49 01 ea             	add    r10,rbp
    d0d1:	41 bb 01 00 00 00    	mov    r11d,0x1
    d0d7:	45 31 c0             	xor    r8d,r8d
    d0da:	49 89 c9             	mov    r9,rcx
    d0dd:	48 89 cf             	mov    rdi,rcx
    d0e0:	eb 30                	jmp    d112 <zbtScoreInsertAt+0xa62>
    d0e2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d0e9:	1f 84 00 00 00 00 00
    d0f0:	4c 09 fb             	or     rbx,r15
    d0f3:	49 89 de             	mov    r14,rbx
    d0f6:	49 31 ce             	xor    r14,rcx
    d0f9:	4d 09 f0             	or     r8,r14
    d0fc:	4c 39 cb             	cmp    rbx,r9
    d0ff:	4c 0f 42 cb          	cmovb  r9,rbx
    d103:	48 39 fb             	cmp    rbx,rdi
    d106:	48 0f 47 fb          	cmova  rdi,rbx
    d10a:	49 ff c3             	inc    r11
    d10d:	4c 39 da             	cmp    rdx,r11
    d110:	74 15                	je     d127 <zbtScoreInsertAt+0xa77>
    d112:	f3 43 0f 7e 04 da    	movq   xmm0,QWORD PTR [r10+r11*8]
    d118:	66 48 0f 7e c3       	movq   rbx,xmm0
    d11d:	48 85 db             	test   rbx,rbx
    d120:	79 ce                	jns    d0f0 <zbtScoreInsertAt+0xa40>
    d122:	48 f7 d3             	not    rbx
    d125:	eb cc                	jmp    d0f3 <zbtScoreInsertAt+0xa43>
    d127:	4d 85 c0             	test   r8,r8
    d12a:	0f 84 3f 03 00 00    	je     d46f <zbtScoreInsertAt+0xdbf>
    d130:	f3 49 0f bc c8       	tzcnt  rcx,r8
    d135:	4c 29 cf             	sub    rdi,r9
    d138:	48 d3 ef             	shr    rdi,cl
    d13b:	48 85 ff             	test   rdi,rdi
    d13e:	44 0f b6 45 90       	movzx  r8d,BYTE PTR [rbp-0x70]
    d143:	0f 84 2b 03 00 00    	je     d474 <zbtScoreInsertAt+0xdc4>
    d149:	48 0f bd cf          	bsr    rcx,rdi
    d14d:	48 83 f1 c0          	xor    rcx,0xffffffffffffffc0
    d151:	48 83 c1 41          	add    rcx,0x41
    d155:	48 0f af ca          	imul   rcx,rdx
    d159:	48 83 c1 07          	add    rcx,0x7
    d15d:	48 c1 e9 03          	shr    rcx,0x3
    d161:	48 83 c1 09          	add    rcx,0x9
    d165:	48 be fe ff ff ff ff 	movabs rsi,0x1ffffffffffffffe
    d16c:	ff ff 1f
    d16f:	48 21 ce             	and    rsi,rcx
    d172:	48 83 c6 38          	add    rsi,0x38
    d176:	e9 f9 02 00 00       	jmp    d474 <zbtScoreInsertAt+0xdc4>
    d17b:	31 c9                	xor    ecx,ecx
    d17d:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    d181:	45 31 c0             	xor    r8d,r8d
    d184:	45 31 d2             	xor    r10d,r10d
    d187:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    d18b:	4c 01 d0             	add    rax,r10
    d18e:	48 83 c0 38          	add    rax,0x38
    d192:	48 8b 94 dd e8 eb ff 	mov    rdx,QWORD PTR [rbp+rbx*8-0x1418]
    d199:	ff
    d19a:	48 85 d2             	test   rdx,rdx
    d19d:	0f 84 d3 fd ff ff    	je     cf76 <zbtScoreInsertAt+0x8c6>
    d1a3:	48 83 c0 15          	add    rax,0x15
    d1a7:	44 0f b7 66 36       	movzx  r12d,WORD PTR [rsi+0x36]
    d1ac:	4c 39 e0             	cmp    rax,r12
    d1af:	0f 86 bd 00 00 00    	jbe    d272 <zbtScoreInsertAt+0xbc2>
    d1b5:	48 89 f3             	mov    rbx,rsi
    d1b8:	44 8b 4e 30          	mov    r9d,DWORD PTR [rsi+0x30]
    d1bc:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d1c3:	48 8d 95 00 fb ff ff 	lea    rdx,[rbp-0x500]
    d1ca:	48 8d 8d d0 eb ff ff 	lea    rcx,[rbp-0x1430]
    d1d1:	4c 8d 85 e0 fe ff ff 	lea    r8,[rbp-0x120]
    d1d8:	4c 8b bd 78 ff ff ff 	mov    r15,QWORD PTR [rbp-0x88]
    d1df:	4c 89 ff             	mov    rdi,r15
    d1e2:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    d1e6:	e8 95 ed ff ff       	call   bf80 <zbtScoreLeafBuild>
    d1eb:	49 89 c6             	mov    r14,rax
    d1ee:	48 8b 03             	mov    rax,QWORD PTR [rbx]
    d1f1:	49 89 06             	mov    QWORD PTR [r14],rax
    d1f4:	0f b6 43 10          	movzx  eax,BYTE PTR [rbx+0x10]
    d1f8:	41 88 46 10          	mov    BYTE PTR [r14+0x10],al
    d1fc:	0f b7 4b 16          	movzx  ecx,WORD PTR [rbx+0x16]
    d200:	66 41 89 4e 16       	mov    WORD PTR [r14+0x16],cx
    d205:	48 8b 4b 18          	mov    rcx,QWORD PTR [rbx+0x18]
    d209:	49 89 4e 18          	mov    QWORD PTR [r14+0x18],rcx
    d20d:	48 8b 53 20          	mov    rdx,QWORD PTR [rbx+0x20]
    d211:	49 89 56 20          	mov    QWORD PTR [r14+0x20],rdx
    d215:	49 8d 57 08          	lea    rdx,[r15+0x8]
    d219:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d21d:	48 85 c9             	test   rcx,rcx
    d220:	48 0f 44 f2          	cmove  rsi,rdx
    d224:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d227:	49 8b 4e 20          	mov    rcx,QWORD PTR [r14+0x20]
    d22b:	49 8d 57 10          	lea    rdx,[r15+0x10]
    d22f:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d233:	48 85 c9             	test   rcx,rcx
    d236:	48 0f 44 f2          	cmove  rsi,rdx
    d23a:	4c 89 36             	mov    QWORD PTR [rsi],r14
    d23d:	48 8b 0b             	mov    rcx,QWORD PTR [rbx]
    d240:	48 85 c9             	test   rcx,rcx
    d243:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d248:	49 0f 44 c7          	cmove  rax,r15
    d24c:	4c 89 30             	mov    QWORD PTR [rax],r14
    d24f:	49 8b 76 08          	mov    rsi,QWORD PTR [r14+0x8]
    d253:	48 2b 73 08          	sub    rsi,QWORD PTR [rbx+0x8]
    d257:	4c 89 f7             	mov    rdi,r14
    d25a:	e8 11 1f 00 00       	call   f170 <zbtScoreUpdatePath>
    d25f:	4c 89 ff             	mov    rdi,r15
    d262:	48 89 de             	mov    rsi,rbx
    d265:	e8 66 e9 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d26a:	4c 89 f0             	mov    rax,r14
    d26d:	e9 93 0b 00 00       	jmp    de05 <zbtScoreInsertAt+0x1755>
    d272:	41 83 c4 eb          	add    r12d,0xffffffeb
    d276:	45 0f b7 f4          	movzx  r14d,r12w
    d27a:	49 01 f6             	add    r14,rsi
    d27d:	48 8b 8c dd d8 eb ff 	mov    rcx,QWORD PTR [rbp+rbx*8-0x1428]
    d284:	ff
    d285:	e9 d2 08 00 00       	jmp    db5c <zbtScoreInsertAt+0x14ac>
    d28a:	4d 85 ff             	test   r15,r15
    d28d:	0f 85 f7 f4 ff ff    	jne    c78a <zbtScoreInsertAt+0xda>
    d293:	48 8b 4d b0          	mov    rcx,QWORD PTR [rbp-0x50]
    d297:	44 8d 71 01          	lea    r14d,[rcx+0x1]
    d29b:	31 c9                	xor    ecx,ecx
    d29d:	48 89 4d 98          	mov    QWORD PTR [rbp-0x68],rcx
    d2a1:	45 31 c9             	xor    r9d,r9d
    d2a4:	41 bd 15 00 00 00    	mov    r13d,0x15
    d2aa:	49 83 7b 18 00       	cmp    QWORD PTR [r11+0x18],0x0
    d2af:	75 28                	jne    d2d9 <zbtScoreInsertAt+0xc29>
    d2b1:	49 8b 4b 08          	mov    rcx,QWORD PTR [r11+0x8]
    d2b5:	48 81 f9 3f 01 00 00 	cmp    rcx,0x13f
    d2bc:	77 1b                	ja     d2d9 <zbtScoreInsertAt+0xc29>
    d2be:	4c 89 cb             	mov    rbx,r9
    d2c1:	45 31 c9             	xor    r9d,r9d
    d2c4:	48 81 f9 fe 00 00 00 	cmp    rcx,0xfe
    d2cb:	41 0f 93 c1          	setae  r9b
    d2cf:	4e 8d 2c 49          	lea    r13,[rcx+r9*2]
    d2d3:	49 ff c5             	inc    r13
    d2d6:	49 89 d9             	mov    r9,rbx
    d2d9:	44 89 f3             	mov    ebx,r14d
    d2dc:	48 8d 0c 5b          	lea    rcx,[rbx+rbx*2]
    d2e0:	4c 89 4d b8          	mov    QWORD PTR [rbp-0x48],r9
    d2e4:	4c 01 c9             	add    rcx,r9
    d2e7:	4c 01 e9             	add    rcx,r13
    d2ea:	48 83 c1 38          	add    rcx,0x38
    d2ee:	44 0f b7 4e 36       	movzx  r9d,WORD PTR [rsi+0x36]
    d2f3:	4c 39 c9             	cmp    rcx,r9
    d2f6:	0f 87 8e f4 ff ff    	ja     c78a <zbtScoreInsertAt+0xda>
    d2fc:	4c 89 ad 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],r13
    d303:	48 89 5d 80          	mov    QWORD PTR [rbp-0x80],rbx
    d307:	44 89 75 88          	mov    DWORD PTR [rbp-0x78],r14d
    d30b:	49 8d 4b 18          	lea    rcx,[r11+0x18]
    d30f:	48 89 4d a0          	mov    QWORD PTR [rbp-0x60],rcx
    d313:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    d317:	44 89 eb             	mov    ebx,r13d
    d31a:	29 d3                	sub    ebx,edx
    d31c:	84 c0                	test   al,al
    d31e:	0f 44 da             	cmove  ebx,edx
    d321:	89 d8                	mov    eax,ebx
    d323:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
    d327:	4d 85 e4             	test   r12,r12
    d32a:	0f 84 19 0b 00 00    	je     de49 <zbtScoreInsertAt+0x1799>
    d330:	44 89 e0             	mov    eax,r12d
    d333:	41 0f af c5          	imul   eax,r13d
    d337:	83 c0 07             	add    eax,0x7
    d33a:	c1 e8 03             	shr    eax,0x3
    d33d:	83 c0 09             	add    eax,0x9
    d340:	25 fe 3f 00 00       	and    eax,0x3ffe
    d345:	4c 8d 76 38          	lea    r14,[rsi+0x38]
    d349:	48 01 f0             	add    rax,rsi
    d34c:	48 83 c0 38          	add    rax,0x38
    d350:	48 89 85 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],rax
    d357:	4a 8d 34 68          	lea    rsi,[rax+r13*2]
    d35b:	48 8d bd d0 eb ff ff 	lea    rdi,[rbp-0x1430]
    d362:	4c 89 ea             	mov    rdx,r13
    d365:	e8 b6 3d ff ff       	call   1120 <memcpy@plt>
    d36a:	41 29 dd             	sub    r13d,ebx
    d36d:	4c 89 e2             	mov    rdx,r12
    d370:	49 0f af d5          	imul   rdx,r13
    d374:	48 83 fa 40          	cmp    rdx,0x40
    d378:	4c 89 ad 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],r13
    d37f:	0f 82 c1 0b 00 00    	jb     df46 <zbtScoreInsertAt+0x1896>
    d385:	44 89 e0             	mov    eax,r12d
    d388:	f6 65 90             	mul    BYTE PTR [rbp-0x70]
    d38b:	a8 07                	test   al,0x7
    d38d:	0f 84 e4 0a 00 00    	je     de77 <zbtScoreInsertAt+0x17c7>
    d393:	0f b6 c0             	movzx  eax,al
    d396:	83 e0 07             	and    eax,0x7
    d399:	48 8b 4d c0          	mov    rcx,QWORD PTR [rbp-0x40]
    d39d:	4e 8d 04 29          	lea    r8,[rcx+r13*1]
    d3a1:	4e 8d 0c 29          	lea    r9,[rcx+r13*1]
    d3a5:	49 ff c1             	inc    r9
    d3a8:	4d 0f af cc          	imul   r9,r12
    d3ac:	49 83 c1 c0          	add    r9,0xffffffffffffffc0
    d3b0:	4d 0f af c4          	imul   r8,r12
    d3b4:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    d3b8:	eb 16                	jmp    d3d0 <zbtScoreInsertAt+0xd20>
    d3ba:	48 83 c2 c0          	add    rdx,0xffffffffffffffc0
    d3be:	49 83 c1 c0          	add    r9,0xffffffffffffffc0
    d3c2:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    d3c6:	48 83 fa 3f          	cmp    rdx,0x3f
    d3ca:	0f 86 76 0b 00 00    	jbe    df46 <zbtScoreInsertAt+0x1896>
    d3d0:	4c 89 c1             	mov    rcx,r8
    d3d3:	48 c1 e9 03          	shr    rcx,0x3
    d3d7:	4d 8b 14 0e          	mov    r10,QWORD PTR [r14+rcx*1]
    d3db:	41 0f b6 74 0e 08    	movzx  esi,BYTE PTR [r14+rcx*1+0x8]
    d3e1:	89 c1                	mov    ecx,eax
    d3e3:	49 0f ad f2          	shrd   r10,rsi,cl
    d3e7:	4d 89 cb             	mov    r11,r9
    d3ea:	44 89 ce             	mov    esi,r9d
    d3ed:	83 e6 07             	and    esi,0x7
    d3f0:	89 f1                	mov    ecx,esi
    d3f2:	f7 d9                	neg    ecx
    d3f4:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    d3fb:	48 d3 e7             	shl    rdi,cl
    d3fe:	49 c1 eb 03          	shr    r11,0x3
    d402:	48 f7 d7             	not    rdi
    d405:	83 fe 01             	cmp    esi,0x1
    d408:	bb 00 00 00 00       	mov    ebx,0x0
    d40d:	48 19 db             	sbb    rbx,rbx
    d410:	48 09 fb             	or     rbx,rdi
    d413:	48 89 df             	mov    rdi,rbx
    d416:	89 f1                	mov    ecx,esi
    d418:	48 d3 e7             	shl    rdi,cl
    d41b:	48 f7 d7             	not    rdi
    d41e:	4b 23 3c 1e          	and    rdi,QWORD PTR [r14+r11*1]
    d422:	4c 21 d3             	and    rbx,r10
    d425:	48 d3 e3             	shl    rbx,cl
    d428:	48 09 fb             	or     rbx,rdi
    d42b:	4b 89 1c 1e          	mov    QWORD PTR [r14+r11*1],rbx
    d42f:	85 f6                	test   esi,esi
    d431:	74 87                	je     d3ba <zbtScoreInsertAt+0xd0a>
    d433:	bf 40 00 00 00       	mov    edi,0x40
    d438:	29 f7                	sub    edi,esi
    d43a:	bb 7e 00 00 00       	mov    ebx,0x7e
    d43f:	89 f1                	mov    ecx,esi
    d441:	d3 eb                	shr    ebx,cl
    d443:	d3 e3                	shl    ebx,cl
    d445:	43 0f b6 74 1e 08    	movzx  esi,BYTE PTR [r14+r11*1+0x8]
    d44b:	41 89 dd             	mov    r13d,ebx
    d44e:	41 83 f5 7f          	xor    r13d,0x7f
    d452:	81 cb 80 00 00 00    	or     ebx,0x80
    d458:	89 f9                	mov    ecx,edi
    d45a:	49 d3 ea             	shr    r10,cl
    d45d:	21 f3                	and    ebx,esi
    d45f:	45 21 ea             	and    r10d,r13d
    d462:	41 09 da             	or     r10d,ebx
    d465:	47 88 54 1e 08       	mov    BYTE PTR [r14+r11*1+0x8],r10b
    d46a:	e9 4b ff ff ff       	jmp    d3ba <zbtScoreInsertAt+0xd0a>
    d46f:	44 0f b6 45 90       	movzx  r8d,BYTE PTR [rbp-0x70]
    d474:	48 8d 0c 52          	lea    rcx,[rdx+rdx*2]
    d478:	48 01 f1             	add    rcx,rsi
    d47b:	8b 75 c8             	mov    esi,DWORD PTR [rbp-0x38]
    d47e:	39 75 b8             	cmp    DWORD PTR [rbp-0x48],esi
    d481:	0f 85 28 06 00 00    	jne    daaf <zbtScoreInsertAt+0x13ff>
    d487:	48 81 f9 00 10 00 00 	cmp    rcx,0x1000
    d48e:	0f 82 83 03 00 00    	jb     d817 <zbtScoreInsertAt+0x1167>
    d494:	45 84 c0             	test   r8b,r8b
    d497:	0f 84 5b 03 00 00    	je     d7f8 <zbtScoreInsertAt+0x1148>
    d49d:	4c 89 e8             	mov    rax,r13
    d4a0:	4c 09 f8             	or     rax,r15
    d4a3:	4d 85 ed             	test   r13,r13
    d4a6:	49 f7 d5             	not    r13
    d4a9:	4c 0f 49 e8          	cmovns r13,rax
    d4ad:	48 8d 95 10 fb ff ff 	lea    rdx,[rbp-0x4f0]
    d4b4:	31 f6                	xor    esi,esi
    d4b6:	48 c7 45 80 ff ff ff 	mov    QWORD PTR [rbp-0x80],0xffffffffffffffff
    d4bd:	ff
    d4be:	41 b8 01 00 00 00    	mov    r8d,0x1
    d4c4:	41 b9 28 00 00 00    	mov    r9d,0x28
    d4ca:	4c 8d b5 10 ec ff ff 	lea    r14,[rbp-0x13f0]
    d4d1:	44 89 e1             	mov    ecx,r12d
    d4d4:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    d4db:	4c 89 6d a8          	mov    QWORD PTR [rbp-0x58],r13
    d4df:	eb 36                	jmp    d517 <zbtScoreInsertAt+0xe67>
    d4e1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d4e8:	0f 1f 84 00 00 00 00
    d4ef:	00
    d4f0:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d4f4:	49 ff c0             	inc    r8
    d4f7:	48 83 c6 08          	add    rsi,0x8
    d4fb:	49 83 c1 28          	add    r9,0x28
    d4ff:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    d503:	ff c9                	dec    ecx
    d505:	48 83 c2 08          	add    rdx,0x8
    d509:	49 83 c6 28          	add    r14,0x28
    d50d:	4c 3b 45 b8          	cmp    r8,QWORD PTR [rbp-0x48]
    d511:	0f 84 db 02 00 00    	je     d7f2 <zbtScoreInsertAt+0x1142>
    d517:	4c 89 75 98          	mov    QWORD PTR [rbp-0x68],r14
    d51b:	41 be 38 00 00 00    	mov    r14d,0x38
    d521:	49 83 f8 02          	cmp    r8,0x2
    d525:	4c 89 45 c0          	mov    QWORD PTR [rbp-0x40],r8
    d529:	0f 82 b1 00 00 00    	jb     d5e0 <zbtScoreInsertAt+0xf30>
    d52f:	49 89 cc             	mov    r12,rcx
    d532:	31 db                	xor    ebx,ebx
    d534:	4c 89 ef             	mov    rdi,r13
    d537:	31 c9                	xor    ecx,ecx
    d539:	4c 89 e8             	mov    rax,r13
    d53c:	eb 25                	jmp    d563 <zbtScoreInsertAt+0xeb3>
    d53e:	66 90                	xchg   ax,ax
    d540:	4d 09 fa             	or     r10,r15
    d543:	4d 89 d3             	mov    r11,r10
    d546:	4d 31 eb             	xor    r11,r13
    d549:	4c 09 d9             	or     rcx,r11
    d54c:	49 39 fa             	cmp    r10,rdi
    d54f:	49 0f 42 fa          	cmovb  rdi,r10
    d553:	49 39 c2             	cmp    r10,rax
    d556:	49 0f 47 c2          	cmova  rax,r10
    d55a:	48 83 c3 08          	add    rbx,0x8
    d55e:	48 39 de             	cmp    rsi,rbx
    d561:	74 1d                	je     d580 <zbtScoreInsertAt+0xed0>
    d563:	f3 0f 7e 84 1d 08 fb 	movq   xmm0,QWORD PTR [rbp+rbx*1-0x4f8]
    d56a:	ff ff
    d56c:	66 49 0f 7e c2       	movq   r10,xmm0
    d571:	4d 85 d2             	test   r10,r10
    d574:	79 ca                	jns    d540 <zbtScoreInsertAt+0xe90>
    d576:	49 f7 d2             	not    r10
    d579:	eb c8                	jmp    d543 <zbtScoreInsertAt+0xe93>
    d57b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    d580:	48 85 c9             	test   rcx,rcx
    d583:	74 4a                	je     d5cf <zbtScoreInsertAt+0xf1f>
    d585:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    d58a:	48 29 f8             	sub    rax,rdi
    d58d:	48 d3 e8             	shr    rax,cl
    d590:	48 85 c0             	test   rax,rax
    d593:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d597:	4c 89 e1             	mov    rcx,r12
    d59a:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d59e:	74 40                	je     d5e0 <zbtScoreInsertAt+0xf30>
    d5a0:	4c 0f bd f0          	bsr    r14,rax
    d5a4:	49 83 f6 c0          	xor    r14,0xffffffffffffffc0
    d5a8:	49 83 c6 41          	add    r14,0x41
    d5ac:	4d 0f af f0          	imul   r14,r8
    d5b0:	49 83 c6 07          	add    r14,0x7
    d5b4:	49 c1 ee 03          	shr    r14,0x3
    d5b8:	49 83 c6 09          	add    r14,0x9
    d5bc:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d5c3:	ff ff 1f
    d5c6:	49 21 c6             	and    r14,rax
    d5c9:	49 83 c6 38          	add    r14,0x38
    d5cd:	eb 11                	jmp    d5e0 <zbtScoreInsertAt+0xf30>
    d5cf:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d5d3:	4c 89 e1             	mov    rcx,r12
    d5d6:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d5da:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    d5e0:	89 c9                	mov    ecx,ecx
    d5e2:	48 89 4d a0          	mov    QWORD PTR [rbp-0x60],rcx
    d5e6:	48 ff c9             	dec    rcx
    d5e9:	4b 8d 1c 40          	lea    rbx,[r8+r8*2]
    d5ed:	4c 01 f3             	add    rbx,r14
    d5f0:	31 c0                	xor    eax,eax
    d5f2:	eb 18                	jmp    d60c <zbtScoreInsertAt+0xf5c>
    d5f4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d5fb:	00 00 00 00 00
    d600:	48 01 fb             	add    rbx,rdi
    d603:	48 83 c0 28          	add    rax,0x28
    d607:	49 39 c1             	cmp    r9,rax
    d60a:	74 44                	je     d650 <zbtScoreInsertAt+0xfa0>
    d60c:	bf 15 00 00 00       	mov    edi,0x15
    d611:	48 83 bc 05 e8 eb ff 	cmp    QWORD PTR [rbp+rax*1-0x1418],0x0
    d618:	ff 00
    d61a:	75 e4                	jne    d600 <zbtScoreInsertAt+0xf50>
    d61c:	4c 8b 94 05 d8 eb ff 	mov    r10,QWORD PTR [rbp+rax*1-0x1428]
    d623:	ff
    d624:	49 81 fa 3f 01 00 00 	cmp    r10,0x13f
    d62b:	77 d3                	ja     d600 <zbtScoreInsertAt+0xf50>
    d62d:	31 ff                	xor    edi,edi
    d62f:	49 81 fa fe 00 00 00 	cmp    r10,0xfe
    d636:	40 0f 93 c7          	setae  dil
    d63a:	49 8d 3c 7a          	lea    rdi,[r10+rdi*2]
    d63e:	48 ff c7             	inc    rdi
    d641:	eb bd                	jmp    d600 <zbtScoreInsertAt+0xf50>
    d643:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d64a:	84 00 00 00 00 00
    d650:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    d654:	f3 0f 7e 84 c5 00 fb 	movq   xmm0,QWORD PTR [rbp+rax*8-0x500]
    d65b:	ff ff
    d65d:	66 49 0f 7e c5       	movq   r13,xmm0
    d662:	4d 85 ed             	test   r13,r13
    d665:	78 09                	js     d670 <zbtScoreInsertAt+0xfc0>
    d667:	4d 09 fd             	or     r13,r15
    d66a:	eb 07                	jmp    d673 <zbtScoreInsertAt+0xfc3>
    d66c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d670:	49 f7 d5             	not    r13
    d673:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d677:	41 29 c6             	sub    r14d,eax
    d67a:	41 bf 38 00 00 00    	mov    r15d,0x38
    d680:	41 83 fe 02          	cmp    r14d,0x2
    d684:	72 6a                	jb     d6f0 <zbtScoreInsertAt+0x1040>
    d686:	45 31 d2             	xor    r10d,r10d
    d689:	4c 89 ef             	mov    rdi,r13
    d68c:	45 31 e4             	xor    r12d,r12d
    d68f:	4c 89 e8             	mov    rax,r13
    d692:	eb 38                	jmp    d6cc <zbtScoreInsertAt+0x101c>
    d694:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d69b:	00 00 00 00 00
    d6a0:	49 bb 00 00 00 00 00 	movabs r11,0x8000000000000000
    d6a7:	00 00 80
    d6aa:	4d 09 d8             	or     r8,r11
    d6ad:	4d 89 c3             	mov    r11,r8
    d6b0:	4d 31 eb             	xor    r11,r13
    d6b3:	4d 09 dc             	or     r12,r11
    d6b6:	49 39 f8             	cmp    r8,rdi
    d6b9:	49 0f 42 f8          	cmovb  rdi,r8
    d6bd:	49 39 c0             	cmp    r8,rax
    d6c0:	49 0f 47 c0          	cmova  rax,r8
    d6c4:	49 ff c2             	inc    r10
    d6c7:	4c 39 d1             	cmp    rcx,r10
    d6ca:	74 34                	je     d700 <zbtScoreInsertAt+0x1050>
    d6cc:	f3 42 0f 7e 04 d2    	movq   xmm0,QWORD PTR [rdx+r10*8]
    d6d2:	66 49 0f 7e c0       	movq   r8,xmm0
    d6d7:	4d 85 c0             	test   r8,r8
    d6da:	79 c4                	jns    d6a0 <zbtScoreInsertAt+0xff0>
    d6dc:	49 f7 d0             	not    r8
    d6df:	eb cc                	jmp    d6ad <zbtScoreInsertAt+0xffd>
    d6e1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d6e8:	0f 1f 84 00 00 00 00
    d6ef:	00
    d6f0:	4c 8b 6d a8          	mov    r13,QWORD PTR [rbp-0x58]
    d6f4:	eb 5a                	jmp    d750 <zbtScoreInsertAt+0x10a0>
    d6f6:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    d6fd:	00 00 00
    d700:	4d 85 e4             	test   r12,r12
    d703:	4c 8b 6d a8          	mov    r13,QWORD PTR [rbp-0x58]
    d707:	74 43                	je     d74c <zbtScoreInsertAt+0x109c>
    d709:	f3 49 0f bc cc       	tzcnt  rcx,r12
    d70e:	48 29 f8             	sub    rax,rdi
    d711:	48 d3 e8             	shr    rax,cl
    d714:	48 85 c0             	test   rax,rax
    d717:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d71b:	74 33                	je     d750 <zbtScoreInsertAt+0x10a0>
    d71d:	4c 0f bd f8          	bsr    r15,rax
    d721:	49 83 f7 c0          	xor    r15,0xffffffffffffffc0
    d725:	49 83 c7 41          	add    r15,0x41
    d729:	4d 0f af fe          	imul   r15,r14
    d72d:	49 83 c7 07          	add    r15,0x7
    d731:	49 c1 ef 03          	shr    r15,0x3
    d735:	49 83 c7 09          	add    r15,0x9
    d739:	48 b8 fe ff ff ff ff 	movabs rax,0x1ffffffffffffffe
    d740:	ff ff 1f
    d743:	49 21 c7             	and    r15,rax
    d746:	49 83 c7 38          	add    r15,0x38
    d74a:	eb 04                	jmp    d750 <zbtScoreInsertAt+0x10a0>
    d74c:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    d750:	4b 8d 04 76          	lea    rax,[r14+r14*2]
    d754:	4c 01 f8             	add    rax,r15
    d757:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    d75b:	4c 8b 75 98          	mov    r14,QWORD PTR [rbp-0x68]
    d75f:	4c 89 f7             	mov    rdi,r14
    d762:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    d769:	00 00 80
    d76c:	eb 0e                	jmp    d77c <zbtScoreInsertAt+0x10cc>
    d76e:	66 90                	xchg   ax,ax
    d770:	4c 01 d0             	add    rax,r10
    d773:	48 83 c7 28          	add    rdi,0x28
    d777:	48 ff c9             	dec    rcx
    d77a:	74 34                	je     d7b0 <zbtScoreInsertAt+0x1100>
    d77c:	41 ba 15 00 00 00    	mov    r10d,0x15
    d782:	48 83 3f 00          	cmp    QWORD PTR [rdi],0x0
    d786:	75 e8                	jne    d770 <zbtScoreInsertAt+0x10c0>
    d788:	4c 8b 5f f0          	mov    r11,QWORD PTR [rdi-0x10]
    d78c:	49 81 fb 3f 01 00 00 	cmp    r11,0x13f
    d793:	77 db                	ja     d770 <zbtScoreInsertAt+0x10c0>
    d795:	45 31 c0             	xor    r8d,r8d
    d798:	49 81 fb fe 00 00 00 	cmp    r11,0xfe
    d79f:	41 0f 93 c0          	setae  r8b
    d7a3:	4f 8d 14 43          	lea    r10,[r11+r8*2]
    d7a7:	49 ff c2             	inc    r10
    d7aa:	eb c4                	jmp    d770 <zbtScoreInsertAt+0x10c0>
    d7ac:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    d7b0:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    d7b7:	0f 87 33 fd ff ff    	ja     d4f0 <zbtScoreInsertAt+0xe40>
    d7bd:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    d7c3:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    d7c7:	0f 87 27 fd ff ff    	ja     d4f4 <zbtScoreInsertAt+0xe44>
    d7cd:	48 39 c3             	cmp    rbx,rax
    d7d0:	48 0f 47 c3          	cmova  rax,rbx
    d7d4:	48 8b 7d 80          	mov    rdi,QWORD PTR [rbp-0x80]
    d7d8:	48 39 f8             	cmp    rax,rdi
    d7db:	8b 4d c8             	mov    ecx,DWORD PTR [rbp-0x38]
    d7de:	41 0f 42 c8          	cmovb  ecx,r8d
    d7e2:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    d7e5:	48 0f 42 f8          	cmovb  rdi,rax
    d7e9:	48 89 7d 80          	mov    QWORD PTR [rbp-0x80],rdi
    d7ed:	e9 02 fd ff ff       	jmp    d4f4 <zbtScoreInsertAt+0xe44>
    d7f2:	83 7d c8 00          	cmp    DWORD PTR [rbp-0x38],0x0
    d7f6:	75 1f                	jne    d817 <zbtScoreInsertAt+0x1167>
    d7f8:	48 8d 3d 1f 5e 00 00 	lea    rdi,[rip+0x5e1f]        # 1361e <_IO_stdin_used+0x61e>
    d7ff:	48 8d 15 c9 60 00 00 	lea    rdx,[rip+0x60c9]        # 138cf <_IO_stdin_used+0x8cf>
    d806:	be 59 05 00 00       	mov    esi,0x559
    d80b:	e8 00 43 00 00       	call   11b10 <standalone_panic>
    d810:	c7 45 c8 00 00 00 00 	mov    DWORD PTR [rbp-0x38],0x0
    d817:	4c 8b 75 b8          	mov    r14,QWORD PTR [rbp-0x48]
    d81b:	44 8b 7d c8          	mov    r15d,DWORD PTR [rbp-0x38]
    d81f:	45 29 fe             	sub    r14d,r15d
    d822:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    d826:	44 8b 48 30          	mov    r9d,DWORD PTR [rax+0x30]
    d82a:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d831:	48 8d 95 00 fb ff ff 	lea    rdx,[rbp-0x500]
    d838:	48 8d 8d d0 eb ff ff 	lea    rcx,[rbp-0x1430]
    d83f:	4c 8d 85 e0 fe ff ff 	lea    r8,[rbp-0x120]
    d846:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d84d:	48 89 df             	mov    rdi,rbx
    d850:	44 89 fe             	mov    esi,r15d
    d853:	e8 28 e7 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d858:	49 89 c5             	mov    r13,rax
    d85b:	44 89 f8             	mov    eax,r15d
    d85e:	48 8d 14 c5 00 fb ff 	lea    rdx,[rax*8-0x500]
    d865:	ff
    d866:	48 01 ea             	add    rdx,rbp
    d869:	48 8d 0c 80          	lea    rcx,[rax+rax*4]
    d86d:	48 8d 8c cd d0 eb ff 	lea    rcx,[rbp+rcx*8-0x1430]
    d874:	ff
    d875:	4c 8d 84 05 e0 fe ff 	lea    r8,[rbp+rax*1-0x120]
    d87c:	ff
    d87d:	c7 04 24 00 00 00 00 	mov    DWORD PTR [rsp],0x0
    d884:	48 89 df             	mov    rdi,rbx
    d887:	44 89 f6             	mov    esi,r14d
    d88a:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    d890:	e8 eb e6 ff ff       	call   bf80 <zbtScoreLeafBuild>
    d895:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    d899:	4c 89 e7             	mov    rdi,r12
    d89c:	49 89 c4             	mov    r12,rax
    d89f:	41 0f b7 40 16       	movzx  eax,WORD PTR [r8+0x16]
    d8a4:	66 41 89 44 24 16    	mov    WORD PTR [r12+0x16],ax
    d8aa:	66 41 89 45 16       	mov    WORD PTR [r13+0x16],ax
    d8af:	49 8b 00             	mov    rax,QWORD PTR [r8]
    d8b2:	49 89 45 00          	mov    QWORD PTR [r13+0x0],rax
    d8b6:	41 0f b6 40 10       	movzx  eax,BYTE PTR [r8+0x10]
    d8bb:	41 88 45 10          	mov    BYTE PTR [r13+0x10],al
    d8bf:	49 8b 48 18          	mov    rcx,QWORD PTR [r8+0x18]
    d8c3:	49 89 4d 18          	mov    QWORD PTR [r13+0x18],rcx
    d8c7:	4d 89 65 20          	mov    QWORD PTR [r13+0x20],r12
    d8cb:	4d 89 6c 24 18       	mov    QWORD PTR [r12+0x18],r13
    d8d0:	49 8b 48 20          	mov    rcx,QWORD PTR [r8+0x20]
    d8d4:	49 89 4c 24 20       	mov    QWORD PTR [r12+0x20],rcx
    d8d9:	49 8b 4d 18          	mov    rcx,QWORD PTR [r13+0x18]
    d8dd:	48 8d 53 08          	lea    rdx,[rbx+0x8]
    d8e1:	48 8d 71 20          	lea    rsi,[rcx+0x20]
    d8e5:	48 85 c9             	test   rcx,rcx
    d8e8:	48 0f 44 f2          	cmove  rsi,rdx
    d8ec:	4c 89 2e             	mov    QWORD PTR [rsi],r13
    d8ef:	49 8b 4c 24 20       	mov    rcx,QWORD PTR [r12+0x20]
    d8f4:	48 8d 53 10          	lea    rdx,[rbx+0x10]
    d8f8:	48 8d 71 18          	lea    rsi,[rcx+0x18]
    d8fc:	48 85 c9             	test   rcx,rcx
    d8ff:	48 0f 44 f2          	cmove  rsi,rdx
    d903:	4c 89 26             	mov    QWORD PTR [rsi],r12
    d906:	49 8b 08             	mov    rcx,QWORD PTR [r8]
    d909:	48 85 c9             	test   rcx,rcx
    d90c:	48 8d 44 c1 18       	lea    rax,[rcx+rax*8+0x18]
    d911:	48 0f 44 c3          	cmove  rax,rbx
    d915:	4c 89 6d a0          	mov    QWORD PTR [rbp-0x60],r13
    d919:	4c 89 28             	mov    QWORD PTR [rax],r13
    d91c:	c7 85 58 ff ff ff 00 	mov    DWORD PTR [rbp-0xa8],0x0
    d923:	00 00 00
    d926:	41 39 ff             	cmp    r15d,edi
    d929:	76 5a                	jbe    d985 <zbtScoreInsertAt+0x12d5>
    d92b:	48 8b 9d 78 ff ff ff 	mov    rbx,QWORD PTR [rbp-0x88]
    d932:	48 89 df             	mov    rdi,rbx
    d935:	4c 89 c6             	mov    rsi,r8
    d938:	e8 93 e2 ff ff       	call   bbd0 <zbtScoreLeafFreeOwned>
    d93d:	48 89 df             	mov    rdi,rbx
    d940:	4c 8b 75 a0          	mov    r14,QWORD PTR [rbp-0x60]
    d944:	4c 89 f6             	mov    rsi,r14
    d947:	4c 89 e2             	mov    rdx,r12
    d94a:	e8 d1 0a 00 00       	call   e420 <zbtScoreInsertSibling>
    d94f:	49 8b 1e             	mov    rbx,QWORD PTR [r14]
    d952:	48 85 db             	test   rbx,rbx
    d955:	74 19                	je     d970 <zbtScoreInsertAt+0x12c0>
    d957:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    d95e:	00 00
    d960:	48 89 df             	mov    rdi,rbx
    d963:	e8 28 0f 00 00       	call   e890 <zbtScoreRefreshNode>
    d968:	48 8b 1b             	mov    rbx,QWORD PTR [rbx]
    d96b:	48 85 db             	test   rbx,rbx
    d96e:	75 f0                	jne    d960 <zbtScoreInsertAt+0x12b0>
    d970:	8b 45 c8             	mov    eax,DWORD PTR [rbp-0x38]
    d973:	39 85 68 ff ff ff    	cmp    DWORD PTR [rbp-0x98],eax
    d979:	4d 0f 42 e6          	cmovb  r12,r14
    d97d:	4c 89 e0             	mov    rax,r12
    d980:	e9 80 04 00 00       	jmp    de05 <zbtScoreInsertAt+0x1755>
    d985:	49 8d 44 24 38       	lea    rax,[r12+0x38]
    d98a:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    d98e:	31 c0                	xor    eax,eax
    d990:	44 8b bd 68 ff ff ff 	mov    r15d,DWORD PTR [rbp-0x98]
    d997:	44 8b 75 c8          	mov    r14d,DWORD PTR [rbp-0x38]
    d99b:	45 29 f7             	sub    r15d,r14d
    d99e:	0f 93 c0             	setae  al
    d9a1:	89 45 c0             	mov    DWORD PTR [rbp-0x40],eax
    d9a4:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    d9a8:	45 29 f5             	sub    r13d,r14d
    d9ab:	41 ff c5             	inc    r13d
    d9ae:	31 db                	xor    ebx,ebx
    d9b0:	eb 1c                	jmp    d9ce <zbtScoreInsertAt+0x131e>
    d9b2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    d9b9:	1f 84 00 00 00 00 00
    d9c0:	41 ff c6             	inc    r14d
    d9c3:	ff c3                	inc    ebx
    d9c5:	41 39 dd             	cmp    r13d,ebx
    d9c8:	0f 84 5d ff ff ff    	je     d92b <zbtScoreInsertAt+0x127b>
    d9ce:	41 39 df             	cmp    r15d,ebx
    d9d1:	74 ed                	je     d9c0 <zbtScoreInsertAt+0x1310>
    d9d3:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    d9d9:	48 85 c0             	test   rax,rax
    d9dc:	74 57                	je     da35 <zbtScoreInsertAt+0x1385>
    d9de:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    d9e4:	0f af c1             	imul   eax,ecx
    d9e7:	83 c0 07             	add    eax,0x7
    d9ea:	c1 e8 03             	shr    eax,0x3
    d9ed:	83 c0 09             	add    eax,0x9
    d9f0:	83 e0 fe             	and    eax,0xfffffffe
    d9f3:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    d9f9:	89 d9                	mov    ecx,ebx
    d9fb:	74 10                	je     da0d <zbtScoreInsertAt+0x135d>
    d9fd:	44 89 f1             	mov    ecx,r14d
    da00:	2b 4d c8             	sub    ecx,DWORD PTR [rbp-0x38]
    da03:	41 0f b6 54 24 11    	movzx  edx,BYTE PTR [r12+0x11]
    da09:	f7 d1                	not    ecx
    da0b:	01 d1                	add    ecx,edx
    da0d:	48 03 45 b8          	add    rax,QWORD PTR [rbp-0x48]
    da11:	89 c9                	mov    ecx,ecx
    da13:	0f b7 04 48          	movzx  eax,WORD PTR [rax+rcx*2]
    da17:	49 8d 3c 04          	lea    rdi,[r12+rax*1]
    da1b:	41 0f b6 34 04       	movzx  esi,BYTE PTR [r12+rax*1]
    da20:	81 fe fe 00 00 00    	cmp    esi,0xfe
    da26:	74 1b                	je     da43 <zbtScoreInsertAt+0x1393>
    da28:	81 fe ff 00 00 00    	cmp    esi,0xff
    da2e:	75 1e                	jne    da4e <zbtScoreInsertAt+0x139e>
    da30:	8b 77 01             	mov    esi,DWORD PTR [rdi+0x1]
    da33:	eb 2d                	jmp    da62 <zbtScoreInsertAt+0x13b2>
    da35:	31 c0                	xor    eax,eax
    da37:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    da3d:	89 d9                	mov    ecx,ebx
    da3f:	75 bc                	jne    d9fd <zbtScoreInsertAt+0x134d>
    da41:	eb ca                	jmp    da0d <zbtScoreInsertAt+0x135d>
    da43:	0f b7 77 01          	movzx  esi,WORD PTR [rdi+0x1]
    da47:	b8 03 00 00 00       	mov    eax,0x3
    da4c:	eb 05                	jmp    da53 <zbtScoreInsertAt+0x13a3>
    da4e:	b8 01 00 00 00       	mov    eax,0x1
    da53:	48 01 c7             	add    rdi,rax
    da56:	e8 f5 42 00 00       	call   11d50 <dictGenHashFunction>
    da5b:	48 89 c6             	mov    rsi,rax
    da5e:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    da62:	41 8b 50 30          	mov    edx,DWORD PTR [r8+0x30]
    da66:	41 8b 4c 24 30       	mov    ecx,DWORD PTR [r12+0x30]
    da6b:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
    da72:	44 8b 45 c0          	mov    r8d,DWORD PTR [rbp-0x40]
    da76:	4c 8d 8d 58 ff ff ff 	lea    r9,[rbp-0xa8]
    da7d:	e8 4e b7 ff ff       	call   91d0 <zbtIndexMove>
    da82:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    da86:	85 c0                	test   eax,eax
    da88:	0f 85 32 ff ff ff    	jne    d9c0 <zbtScoreInsertAt+0x1310>
    da8e:	48 8d 3d 89 5b 00 00 	lea    rdi,[rip+0x5b89]        # 1361e <_IO_stdin_used+0x61e>
    da95:	be 83 06 00 00       	mov    esi,0x683
    da9a:	48 8d 15 d3 5d 00 00 	lea    rdx,[rip+0x5dd3]        # 13874 <_IO_stdin_used+0x874>
    daa1:	e8 6a 40 00 00       	call   11b10 <standalone_panic>
    daa6:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    daaa:	e9 11 ff ff ff       	jmp    d9c0 <zbtScoreInsertAt+0x1310>
    daaf:	48 8d 04 80          	lea    rax,[rax+rax*4]
    dab3:	48 8d 04 c5 e8 eb ff 	lea    rax,[rax*8-0x1418]
    daba:	ff
    dabb:	48 01 e8             	add    rax,rbp
    dabe:	eb 10                	jmp    dad0 <zbtScoreInsertAt+0x1420>
    dac0:	48 01 f1             	add    rcx,rsi
    dac3:	48 83 c0 28          	add    rax,0x28
    dac7:	48 ff ca             	dec    rdx
    daca:	0f 84 b7 f9 ff ff    	je     d487 <zbtScoreInsertAt+0xdd7>
    dad0:	be 15 00 00 00       	mov    esi,0x15
    dad5:	48 83 38 00          	cmp    QWORD PTR [rax],0x0
    dad9:	75 e5                	jne    dac0 <zbtScoreInsertAt+0x1410>
    dadb:	48 8b 78 f0          	mov    rdi,QWORD PTR [rax-0x10]
    dadf:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    dae6:	77 d8                	ja     dac0 <zbtScoreInsertAt+0x1410>
    dae8:	31 f6                	xor    esi,esi
    daea:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    daf1:	40 0f 93 c6          	setae  sil
    daf5:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    daf9:	48 ff c6             	inc    rsi
    dafc:	eb c2                	jmp    dac0 <zbtScoreInsertAt+0x1410>
    dafe:	48 8d b5 58 ff ff ff 	lea    rsi,[rbp-0xa8]
    db05:	4c 89 df             	mov    rdi,r11
    db08:	4c 89 55 c0          	mov    QWORD PTR [rbp-0x40],r10
    db0c:	4c 89 5d 88          	mov    QWORD PTR [rbp-0x78],r11
    db10:	e8 fb 40 00 00       	call   11c10 <zmalloc_usable>
    db15:	48 89 c7             	mov    rdi,rax
    db18:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    db1f:	48 8b 85 58 ff ff ff 	mov    rax,QWORD PTR [rbp-0xa8]
    db26:	48 8b 8d 78 ff ff ff 	mov    rcx,QWORD PTR [rbp-0x88]
    db2d:	48 01 41 68          	add    QWORD PTR [rcx+0x68],rax
    db31:	48 8b 45 80          	mov    rax,QWORD PTR [rbp-0x80]
    db35:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    db38:	48 8b 55 88          	mov    rdx,QWORD PTR [rbp-0x78]
    db3c:	e8 df 35 ff ff       	call   1120 <memcpy@plt>
    db41:	48 8b 95 70 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x90]
    db48:	48 8b 4d 88          	mov    rcx,QWORD PTR [rbp-0x78]
    db4c:	4c 8b 55 c0          	mov    r10,QWORD PTR [rbp-0x40]
    db50:	4c 8b 45 b0          	mov    r8,QWORD PTR [rbp-0x50]
    db54:	48 8b 7d a8          	mov    rdi,QWORD PTR [rbp-0x58]
    db58:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    db5c:	41 c6 06 ff          	mov    BYTE PTR [r14],0xff
    db60:	8b 84 dd e0 eb ff ff 	mov    eax,DWORD PTR [rbp+rbx*8-0x1420]
    db67:	41 89 46 01          	mov    DWORD PTR [r14+0x1],eax
    db6b:	49 89 4e 05          	mov    QWORD PTR [r14+0x5],rcx
    db6f:	49 89 56 0d          	mov    QWORD PTR [r14+0xd],rdx
    db73:	4c 8b b4 dd f0 eb ff 	mov    r14,QWORD PTR [rbp+rbx*8-0x1410]
    db7a:	ff
    db7b:	4d 85 f6             	test   r14,r14
    db7e:	74 40                	je     dbc0 <zbtScoreInsertAt+0x1510>
    db80:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    db84:	74 32                	je     dbb8 <zbtScoreInsertAt+0x1508>
    db86:	48 89 7d a8          	mov    QWORD PTR [rbp-0x58],rdi
    db8a:	48 8d 3d 8d 5a 00 00 	lea    rdi,[rip+0x5a8d]        # 1361e <_IO_stdin_used+0x61e>
    db91:	48 8d 15 be 5b 00 00 	lea    rdx,[rip+0x5bbe]        # 13756 <_IO_stdin_used+0x756>
    db98:	be 4c 02 00 00       	mov    esi,0x24c
    db9d:	4c 89 c3             	mov    rbx,r8
    dba0:	4c 89 55 c0          	mov    QWORD PTR [rbp-0x40],r10
    dba4:	e8 67 3f 00 00       	call   11b10 <standalone_panic>
    dba9:	4c 8b 55 c0          	mov    r10,QWORD PTR [rbp-0x40]
    dbad:	49 89 d8             	mov    r8,rbx
    dbb0:	48 8b 7d a8          	mov    rdi,QWORD PTR [rbp-0x58]
    dbb4:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    dbb8:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    dbbf:	00
    dbc0:	4c 89 65 c0          	mov    QWORD PTR [rbp-0x40],r12
    dbc4:	c6 46 14 01          	mov    BYTE PTR [rsi+0x14],0x1
    dbc8:	48 89 7d a8          	mov    QWORD PTR [rbp-0x58],rdi
    dbcc:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    dbd0:	44 88 66 11          	mov    BYTE PTR [rsi+0x11],r12b
    dbd4:	4c 89 66 08          	mov    QWORD PTR [rsi+0x8],r12
    dbd8:	40 88 7e 13          	mov    BYTE PTR [rsi+0x13],dil
    dbdc:	4c 89 6e 28          	mov    QWORD PTR [rsi+0x28],r13
    dbe0:	44 88 46 34          	mov    BYTE PTR [rsi+0x34],r8b
    dbe4:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    dbe8:	66 89 46 36          	mov    WORD PTR [rsi+0x36],ax
    dbec:	48 8b 5d a0          	mov    rbx,QWORD PTR [rbp-0x60]
    dbf0:	48 89 df             	mov    rdi,rbx
    dbf3:	31 f6                	xor    esi,esi
    dbf5:	4c 89 d2             	mov    rdx,r10
    dbf8:	4d 89 c6             	mov    r14,r8
    dbfb:	e8 b0 34 ff ff       	call   10b0 <memset@plt>
    dc00:	41 0f b6 cc          	movzx  ecx,r12b
    dc04:	45 84 f6             	test   r14b,r14b
    dc07:	0f 84 ff 00 00 00    	je     dd0c <zbtScoreInsertAt+0x165c>
    dc0d:	41 0f b6 d6          	movzx  edx,r14b
    dc11:	89 d6                	mov    esi,edx
    dc13:	0f af f1             	imul   esi,ecx
    dc16:	83 c6 07             	add    esi,0x7
    dc19:	c1 ee 03             	shr    esi,0x3
    dc1c:	83 c6 09             	add    esi,0x9
    dc1f:	83 e6 fe             	and    esi,0xfffffffe
    dc22:	48 01 de             	add    rsi,rbx
    dc25:	48 8d 3c 4e          	lea    rdi,[rsi+rcx*2]
    dc29:	0f b6 45 a8          	movzx  eax,BYTE PTR [rbp-0x58]
    dc2d:	4c 8b 45 d0          	mov    r8,QWORD PTR [rbp-0x30]
    dc31:	45 0f b6 40 35       	movzx  r8d,BYTE PTR [r8+0x35]
    dc36:	44 8d 49 ff          	lea    r9d,[rcx-0x1]
    dc3a:	45 31 d2             	xor    r10d,r10d
    dc3d:	eb 2b                	jmp    dc6a <zbtScoreInsertAt+0x15ba>
    dc3f:	90                   	nop
    dc40:	66 89 0c 5e          	mov    WORD PTR [rsi+rbx*2],cx
    dc44:	42 0f b6 8c 15 e0 fe 	movzx  ecx,BYTE PTR [rbp+r10*1-0x120]
    dc4b:	ff ff
    dc4d:	88 0c 1f             	mov    BYTE PTR [rdi+rbx*1],cl
    dc50:	49 ff c2             	inc    r10
    dc53:	41 ff c9             	dec    r9d
    dc56:	4c 39 55 b8          	cmp    QWORD PTR [rbp-0x48],r10
    dc5a:	49 bf 00 00 00 00 00 	movabs r15,0x8000000000000000
    dc61:	00 00 80
    dc64:	0f 84 87 01 00 00    	je     ddf1 <zbtScoreInsertAt+0x1741>
    dc6a:	f3 42 0f 7e 84 d5 00 	movq   xmm0,QWORD PTR [rbp+r10*8-0x500]
    dc71:	fb ff ff
    dc74:	66 49 0f 7e c3       	movq   r11,xmm0
    dc79:	4d 85 db             	test   r11,r11
    dc7c:	78 12                	js     dc90 <zbtScoreInsertAt+0x15e0>
    dc7e:	4d 09 fb             	or     r11,r15
    dc81:	eb 10                	jmp    dc93 <zbtScoreInsertAt+0x15e3>
    dc83:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    dc8a:	84 00 00 00 00 00
    dc90:	49 f7 d3             	not    r11
    dc93:	4c 89 e9             	mov    rcx,r13
    dc96:	4c 29 d9             	sub    rcx,r11
    dc99:	4d 29 eb             	sub    r11,r13
    dc9c:	45 84 c0             	test   r8b,r8b
    dc9f:	4c 0f 45 d9          	cmovne r11,rcx
    dca3:	44 89 cb             	mov    ebx,r9d
    dca6:	41 0f 44 da          	cmove  ebx,r10d
    dcaa:	89 c1                	mov    ecx,eax
    dcac:	49 d3 eb             	shr    r11,cl
    dcaf:	49 89 df             	mov    r15,rbx
    dcb2:	4c 0f af fa          	imul   r15,rdx
    dcb6:	4d 89 fe             	mov    r14,r15
    dcb9:	49 c1 ee 03          	shr    r14,0x3
    dcbd:	44 89 f9             	mov    ecx,r15d
    dcc0:	80 e1 07             	and    cl,0x7
    dcc3:	4d 89 dc             	mov    r12,r11
    dcc6:	49 d3 e4             	shl    r12,cl
    dcc9:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    dccd:	4e 09 24 31          	or     QWORD PTR [rcx+r14*1],r12
    dcd1:	41 83 e7 07          	and    r15d,0x7
    dcd5:	74 19                	je     dcf0 <zbtScoreInsertAt+0x1640>
    dcd7:	b9 40 00 00 00       	mov    ecx,0x40
    dcdc:	44 29 f9             	sub    ecx,r15d
    dcdf:	3b 4d c8             	cmp    ecx,DWORD PTR [rbp-0x38]
    dce2:	73 0c                	jae    dcf0 <zbtScoreInsertAt+0x1640>
    dce4:	49 d3 eb             	shr    r11,cl
    dce7:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    dceb:	45 08 5c 0e 40       	or     BYTE PTR [r14+rcx*1+0x40],r11b
    dcf0:	48 8b 4d c0          	mov    rcx,QWORD PTR [rbp-0x40]
    dcf4:	4c 39 55 98          	cmp    QWORD PTR [rbp-0x68],r10
    dcf8:	0f 84 42 ff ff ff    	je     dc40 <zbtScoreInsertAt+0x1590>
    dcfe:	42 0f b7 8c 55 10 fe 	movzx  ecx,WORD PTR [rbp+r10*2-0x1f0]
    dd05:	ff ff
    dd07:	e9 34 ff ff ff       	jmp    dc40 <zbtScoreInsertAt+0x1590>
    dd0c:	48 8d 04 4b          	lea    rax,[rbx+rcx*2]
    dd10:	48 8b 55 d0          	mov    rdx,QWORD PTR [rbp-0x30]
    dd14:	0f b6 52 35          	movzx  edx,BYTE PTR [rdx+0x35]
    dd18:	80 7d 90 00          	cmp    BYTE PTR [rbp-0x70],0x0
    dd1c:	0f 84 95 00 00 00    	je     ddb7 <zbtScoreInsertAt+0x1707>
    dd22:	48 8b 7d b8          	mov    rdi,QWORD PTR [rbp-0x48]
    dd26:	83 e7 fe             	and    edi,0xfffffffe
    dd29:	44 8d 41 fe          	lea    r8d,[rcx-0x2]
    dd2d:	45 31 c9             	xor    r9d,r9d
    dd30:	48 8b 5d a0          	mov    rbx,QWORD PTR [rbp-0x60]
    dd34:	4c 8b 75 98          	mov    r14,QWORD PTR [rbp-0x68]
    dd38:	4c 8b 7d c0          	mov    r15,QWORD PTR [rbp-0x40]
    dd3c:	eb 29                	jmp    dd67 <zbtScoreInsertAt+0x16b7>
    dd3e:	66 90                	xchg   ax,ax
    dd40:	84 d2                	test   dl,dl
    dd42:	45 89 c3             	mov    r11d,r8d
    dd45:	45 0f 44 d9          	cmove  r11d,r9d
    dd49:	66 46 89 14 5b       	mov    WORD PTR [rbx+r11*2],r10w
    dd4e:	44 0f b6 94 35 e1 fe 	movzx  r10d,BYTE PTR [rbp+rsi*1-0x11f]
    dd55:	ff ff
    dd57:	46 88 14 18          	mov    BYTE PTR [rax+r11*1],r10b
    dd5b:	41 83 c0 fe          	add    r8d,0xfffffffe
    dd5f:	49 ff c1             	inc    r9
    dd62:	49 39 f9             	cmp    r9,rdi
    dd65:	74 4a                	je     ddb1 <zbtScoreInsertAt+0x1701>
    dd67:	4c 89 ce             	mov    rsi,r9
    dd6a:	45 89 f9             	mov    r9d,r15d
    dd6d:	49 39 f6             	cmp    r14,rsi
    dd70:	74 09                	je     dd7b <zbtScoreInsertAt+0x16cb>
    dd72:	44 0f b7 8c 75 10 fe 	movzx  r9d,WORD PTR [rbp+rsi*2-0x1f0]
    dd79:	ff ff
    dd7b:	45 8d 50 01          	lea    r10d,[r8+0x1]
    dd7f:	84 d2                	test   dl,dl
    dd81:	41 89 f3             	mov    r11d,esi
    dd84:	45 0f 45 da          	cmovne r11d,r10d
    dd88:	66 46 89 0c 5b       	mov    WORD PTR [rbx+r11*2],r9w
    dd8d:	44 0f b6 8c 35 e0 fe 	movzx  r9d,BYTE PTR [rbp+rsi*1-0x120]
    dd94:	ff ff
    dd96:	46 88 0c 18          	mov    BYTE PTR [rax+r11*1],r9b
    dd9a:	4c 8d 4e 01          	lea    r9,[rsi+0x1]
    dd9e:	45 89 fa             	mov    r10d,r15d
    dda1:	4d 39 f1             	cmp    r9,r14
    dda4:	74 9a                	je     dd40 <zbtScoreInsertAt+0x1690>
    dda6:	44 0f b7 94 75 12 fe 	movzx  r10d,WORD PTR [rbp+rsi*2-0x1ee]
    ddad:	ff ff
    ddaf:	eb 8f                	jmp    dd40 <zbtScoreInsertAt+0x1690>
    ddb1:	48 83 c6 02          	add    rsi,0x2
    ddb5:	eb 06                	jmp    ddbd <zbtScoreInsertAt+0x170d>
    ddb7:	31 f6                	xor    esi,esi
    ddb9:	4c 8b 7d c0          	mov    r15,QWORD PTR [rbp-0x40]
    ddbd:	f6 45 b8 01          	test   BYTE PTR [rbp-0x48],0x1
    ddc1:	74 2e                	je     ddf1 <zbtScoreInsertAt+0x1741>
    ddc3:	48 3b 75 98          	cmp    rsi,QWORD PTR [rbp-0x68]
    ddc7:	74 09                	je     ddd2 <zbtScoreInsertAt+0x1722>
    ddc9:	44 0f b7 bc 75 10 fe 	movzx  r15d,WORD PTR [rbp+rsi*2-0x1f0]
    ddd0:	ff ff
    ddd2:	89 f7                	mov    edi,esi
    ddd4:	f7 d7                	not    edi
    ddd6:	01 cf                	add    edi,ecx
    ddd8:	84 d2                	test   dl,dl
    ddda:	0f 44 fe             	cmove  edi,esi
    dddd:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    dde1:	66 44 89 3c 79       	mov    WORD PTR [rcx+rdi*2],r15w
    dde6:	0f b6 8c 35 e0 fe ff 	movzx  ecx,BYTE PTR [rbp+rsi*1-0x120]
    dded:	ff
    ddee:	88 0c 38             	mov    BYTE PTR [rax+rdi*1],cl
    ddf1:	be 01 00 00 00       	mov    esi,0x1
    ddf6:	48 8b 5d d0          	mov    rbx,QWORD PTR [rbp-0x30]
    ddfa:	48 89 df             	mov    rdi,rbx
    ddfd:	e8 6e 13 00 00       	call   f170 <zbtScoreUpdatePath>
    de02:	48 89 d8             	mov    rax,rbx
    de05:	48 81 c4 18 14 00 00 	add    rsp,0x1418
    de0c:	5b                   	pop    rbx
    de0d:	41 5c                	pop    r12
    de0f:	41 5d                	pop    r13
    de11:	41 5e                	pop    r14
    de13:	41 5f                	pop    r15
    de15:	5d                   	pop    rbp
    de16:	c3                   	ret
    de17:	66 45 89 5e 01       	mov    WORD PTR [r14+0x1],r11w
    de1c:	bf 03 00 00 00       	mov    edi,0x3
    de21:	b0 fe                	mov    al,0xfe
    de23:	4c 89 65 c0          	mov    QWORD PTR [rbp-0x40],r12
    de27:	41 88 06             	mov    BYTE PTR [r14],al
    de2a:	4c 01 f7             	add    rdi,r14
    de2d:	4c 89 da             	mov    rdx,r11
    de30:	e8 eb 32 ff ff       	call   1120 <memcpy@plt>
    de35:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    de39:	48 8b 7d a8          	mov    rdi,QWORD PTR [rbp-0x58]
    de3d:	4c 8b 45 b0          	mov    r8,QWORD PTR [rbp-0x50]
    de41:	49 89 da             	mov    r10,rbx
    de44:	e9 7f fd ff ff       	jmp    dbc8 <zbtScoreInsertAt+0x1518>
    de49:	4c 8d 76 38          	lea    r14,[rsi+0x38]
    de4d:	4a 8d 34 6e          	lea    rsi,[rsi+r13*2]
    de51:	48 83 c6 38          	add    rsi,0x38
    de55:	48 8d bd d0 eb ff ff 	lea    rdi,[rbp-0x1430]
    de5c:	4c 89 ea             	mov    rdx,r13
    de5f:	e8 bc 32 ff ff       	call   1120 <memcpy@plt>
    de64:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    de68:	45 89 ef             	mov    r15d,r13d
    de6b:	41 29 df             	sub    r15d,ebx
    de6e:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    de72:	e9 40 02 00 00       	jmp    e0b7 <zbtScoreInsertAt+0x1a07>
    de77:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    de7b:	4a 8d 3c 28          	lea    rdi,[rax+r13*1]
    de7f:	4e 8d 04 28          	lea    r8,[rax+r13*1]
    de83:	49 ff c0             	inc    r8
    de86:	4d 0f af c4          	imul   r8,r12
    de8a:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    de8e:	49 0f af fc          	imul   rdi,r12
    de92:	48 83 c7 c0          	add    rdi,0xffffffffffffffc0
    de96:	eb 16                	jmp    deae <zbtScoreInsertAt+0x17fe>
    de98:	48 83 c2 c0          	add    rdx,0xffffffffffffffc0
    de9c:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    dea0:	48 83 c7 c0          	add    rdi,0xffffffffffffffc0
    dea4:	48 83 fa 3f          	cmp    rdx,0x3f
    dea8:	0f 86 98 00 00 00    	jbe    df46 <zbtScoreInsertAt+0x1896>
    deae:	48 89 f8             	mov    rax,rdi
    deb1:	48 c1 e8 03          	shr    rax,0x3
    deb5:	4d 8b 0c 06          	mov    r9,QWORD PTR [r14+rax*1]
    deb9:	4d 89 c2             	mov    r10,r8
    debc:	44 89 c0             	mov    eax,r8d
    debf:	83 e0 07             	and    eax,0x7
    dec2:	89 c1                	mov    ecx,eax
    dec4:	f7 d9                	neg    ecx
    dec6:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
    decd:	48 d3 e6             	shl    rsi,cl
    ded0:	49 c1 ea 03          	shr    r10,0x3
    ded4:	48 f7 d6             	not    rsi
    ded7:	83 f8 01             	cmp    eax,0x1
    deda:	41 bb 00 00 00 00    	mov    r11d,0x0
    dee0:	4d 19 db             	sbb    r11,r11
    dee3:	49 09 f3             	or     r11,rsi
    dee6:	4c 89 de             	mov    rsi,r11
    dee9:	89 c1                	mov    ecx,eax
    deeb:	48 d3 e6             	shl    rsi,cl
    deee:	48 f7 d6             	not    rsi
    def1:	4b 23 34 16          	and    rsi,QWORD PTR [r14+r10*1]
    def5:	4d 21 cb             	and    r11,r9
    def8:	49 d3 e3             	shl    r11,cl
    defb:	49 09 f3             	or     r11,rsi
    defe:	4f 89 1c 16          	mov    QWORD PTR [r14+r10*1],r11
    df02:	85 c0                	test   eax,eax
    df04:	74 92                	je     de98 <zbtScoreInsertAt+0x17e8>
    df06:	be 40 00 00 00       	mov    esi,0x40
    df0b:	29 c6                	sub    esi,eax
    df0d:	41 bb 7e 00 00 00    	mov    r11d,0x7e
    df13:	89 c1                	mov    ecx,eax
    df15:	41 d3 eb             	shr    r11d,cl
    df18:	41 d3 e3             	shl    r11d,cl
    df1b:	43 0f b6 44 16 08    	movzx  eax,BYTE PTR [r14+r10*1+0x8]
    df21:	44 89 db             	mov    ebx,r11d
    df24:	83 f3 7f             	xor    ebx,0x7f
    df27:	41 81 cb 80 00 00 00 	or     r11d,0x80
    df2e:	89 f1                	mov    ecx,esi
    df30:	49 d3 e9             	shr    r9,cl
    df33:	41 21 c3             	and    r11d,eax
    df36:	41 21 d9             	and    r9d,ebx
    df39:	45 09 d9             	or     r9d,r11d
    df3c:	47 88 4c 16 08       	mov    BYTE PTR [r14+r10*1+0x8],r9b
    df41:	e9 52 ff ff ff       	jmp    de98 <zbtScoreInsertAt+0x17e8>
    df46:	4c 89 e7             	mov    rdi,r12
    df49:	48 0f af 7d c0       	imul   rdi,QWORD PTR [rbp-0x40]
    df4e:	48 85 d2             	test   rdx,rdx
    df51:	0f 84 c7 00 00 00    	je     e01e <zbtScoreInsertAt+0x196e>
    df57:	49 89 f9             	mov    r9,rdi
    df5a:	49 c1 e9 03          	shr    r9,0x3
    df5e:	89 fe                	mov    esi,edi
    df60:	83 e6 07             	and    esi,0x7
    df63:	41 ba 40 00 00 00    	mov    r10d,0x40
    df69:	b8 40 00 00 00       	mov    eax,0x40
    df6e:	29 f0                	sub    eax,esi
    df70:	4f 8b 04 0e          	mov    r8,QWORD PTR [r14+r9*1]
    df74:	89 f1                	mov    ecx,esi
    df76:	49 d3 e8             	shr    r8,cl
    df79:	39 d0                	cmp    eax,edx
    df7b:	4c 89 4d 90          	mov    QWORD PTR [rbp-0x70],r9
    df7f:	73 0e                	jae    df8f <zbtScoreInsertAt+0x18df>
    df81:	47 0f b6 4c 0e 08    	movzx  r9d,BYTE PTR [r14+r9*1+0x8]
    df87:	89 c1                	mov    ecx,eax
    df89:	49 d3 e1             	shl    r9,cl
    df8c:	4d 09 c8             	or     r8,r9
    df8f:	49 c7 c3 ff ff ff ff 	mov    r11,0xffffffffffffffff
    df96:	89 d1                	mov    ecx,edx
    df98:	49 d3 e3             	shl    r11,cl
    df9b:	49 c7 c1 ff ff ff ff 	mov    r9,0xffffffffffffffff
    dfa2:	49 f7 d3             	not    r11
    dfa5:	4d 21 c3             	and    r11,r8
    dfa8:	4c 01 e7             	add    rdi,r12
    dfab:	48 89 fb             	mov    rbx,rdi
    dfae:	48 c1 eb 03          	shr    rbx,0x3
    dfb2:	83 e7 07             	and    edi,0x7
    dfb5:	41 29 fa             	sub    r10d,edi
    dfb8:	41 39 d2             	cmp    r10d,edx
    dfbb:	41 89 d0             	mov    r8d,edx
    dfbe:	45 0f 42 c2          	cmovb  r8d,r10d
    dfc2:	44 89 c1             	mov    ecx,r8d
    dfc5:	49 d3 e1             	shl    r9,cl
    dfc8:	49 f7 d1             	not    r9
    dfcb:	4d 89 dc             	mov    r12,r11
    dfce:	4d 21 cc             	and    r12,r9
    dfd1:	89 f9                	mov    ecx,edi
    dfd3:	49 d3 e1             	shl    r9,cl
    dfd6:	49 f7 d1             	not    r9
    dfd9:	4d 23 0c 1e          	and    r9,QWORD PTR [r14+rbx*1]
    dfdd:	49 d3 e4             	shl    r12,cl
    dfe0:	4d 09 cc             	or     r12,r9
    dfe3:	4d 89 24 1e          	mov    QWORD PTR [r14+rbx*1],r12
    dfe7:	41 39 d2             	cmp    r10d,edx
    dfea:	73 20                	jae    e00c <zbtScoreInsertAt+0x195c>
    dfec:	44 29 c2             	sub    edx,r8d
    dfef:	41 0f b6 7c 1e 08    	movzx  edi,BYTE PTR [r14+rbx*1+0x8]
    dff5:	44 89 c1             	mov    ecx,r8d
    dff8:	49 d3 eb             	shr    r11,cl
    dffb:	44 31 df             	xor    edi,r11d
    dffe:	89 d1                	mov    ecx,edx
    e000:	d3 ef                	shr    edi,cl
    e002:	d3 e7                	shl    edi,cl
    e004:	44 31 df             	xor    edi,r11d
    e007:	41 88 7c 1e 08       	mov    BYTE PTR [r14+rbx*1+0x8],dil
    e00c:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    e010:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    e014:	4c 8b 55 98          	mov    r10,QWORD PTR [rbp-0x68]
    e018:	4c 8b 5d 90          	mov    r11,QWORD PTR [rbp-0x70]
    e01c:	eb 20                	jmp    e03e <zbtScoreInsertAt+0x198e>
    e01e:	49 89 fb             	mov    r11,rdi
    e021:	49 c1 eb 03          	shr    r11,0x3
    e025:	83 e7 07             	and    edi,0x7
    e028:	b8 40 00 00 00       	mov    eax,0x40
    e02d:	29 f8                	sub    eax,edi
    e02f:	48 89 fe             	mov    rsi,rdi
    e032:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    e036:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    e03a:	4c 8b 55 98          	mov    r10,QWORD PTR [rbp-0x68]
    e03e:	44 39 d0             	cmp    eax,r10d
    e041:	44 89 d2             	mov    edx,r10d
    e044:	0f 42 d0             	cmovb  edx,eax
    e047:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    e04e:	49 c7 c0 ff ff ff ff 	mov    r8,0xffffffffffffffff
    e055:	89 d1                	mov    ecx,edx
    e057:	49 d3 e0             	shl    r8,cl
    e05a:	83 fa 40             	cmp    edx,0x40
    e05d:	49 f7 d0             	not    r8
    e060:	4c 0f 44 c7          	cmove  r8,rdi
    e064:	4c 89 c7             	mov    rdi,r8
    e067:	89 f1                	mov    ecx,esi
    e069:	48 d3 e7             	shl    rdi,cl
    e06c:	48 f7 d7             	not    rdi
    e06f:	4b 23 3c 1e          	and    rdi,QWORD PTR [r14+r11*1]
    e073:	4d 21 f8             	and    r8,r15
    e076:	49 d3 e0             	shl    r8,cl
    e079:	49 09 f8             	or     r8,rdi
    e07c:	4f 89 04 1e          	mov    QWORD PTR [r14+r11*1],r8
    e080:	44 39 d0             	cmp    eax,r10d
    e083:	73 20                	jae    e0a5 <zbtScoreInsertAt+0x19f5>
    e085:	41 29 d2             	sub    r10d,edx
    e088:	43 0f b6 44 1e 08    	movzx  eax,BYTE PTR [r14+r11*1+0x8]
    e08e:	89 d1                	mov    ecx,edx
    e090:	49 d3 ef             	shr    r15,cl
    e093:	44 31 f8             	xor    eax,r15d
    e096:	44 89 d1             	mov    ecx,r10d
    e099:	d3 e8                	shr    eax,cl
    e09b:	d3 e0                	shl    eax,cl
    e09d:	44 31 f8             	xor    eax,r15d
    e0a0:	43 88 44 1e 08       	mov    BYTE PTR [r14+r11*1+0x8],al
    e0a5:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    e0a9:	4c 8b bd 60 ff ff ff 	mov    r15,QWORD PTR [rbp-0xa0]
    e0b0:	4c 8b b5 68 ff ff ff 	mov    r14,QWORD PTR [rbp-0x98]
    e0b7:	49 8d 1c 01          	lea    rbx,[r9+rax*1]
    e0bb:	49 8d 3c 01          	lea    rdi,[r9+rax*1]
    e0bf:	48 83 c7 38          	add    rdi,0x38
    e0c3:	42 8d 14 6d 00 00 00 	lea    edx,[r13*2+0x0]
    e0ca:	00
    e0cb:	4c 89 f6             	mov    rsi,r14
    e0ce:	e8 8d 30 ff ff       	call   1160 <memmove@plt>
    e0d3:	4c 8b 75 c0          	mov    r14,QWORD PTR [rbp-0x40]
    e0d7:	4a 8d 34 73          	lea    rsi,[rbx+r14*2]
    e0db:	48 83 c6 38          	add    rsi,0x38
    e0df:	4a 8d 3c 73          	lea    rdi,[rbx+r14*2]
    e0e3:	48 83 c7 3a          	add    rdi,0x3a
    e0e7:	4b 8d 14 3f          	lea    rdx,[r15+r15*1]
    e0eb:	48 89 75 b8          	mov    QWORD PTR [rbp-0x48],rsi
    e0ef:	e8 6c 30 ff ff       	call   1160 <memmove@plt>
    e0f4:	4c 8b 6d 80          	mov    r13,QWORD PTR [rbp-0x80]
    e0f8:	4e 8d 24 6b          	lea    r12,[rbx+r13*2]
    e0fc:	49 83 c4 38          	add    r12,0x38
    e100:	48 8d b5 d0 eb ff ff 	lea    rsi,[rbp-0x1430]
    e107:	4c 89 e7             	mov    rdi,r12
    e10a:	4c 89 f2             	mov    rdx,r14
    e10d:	e8 0e 30 ff ff       	call   1120 <memcpy@plt>
    e112:	0f b6 45 c8          	movzx  eax,BYTE PTR [rbp-0x38]
    e116:	43 88 04 26          	mov    BYTE PTR [r14+r12*1],al
    e11a:	4b 8d 3c 26          	lea    rdi,[r14+r12*1]
    e11e:	48 ff c7             	inc    rdi
    e121:	49 8d 34 2e          	lea    rsi,[r14+rbp*1]
    e125:	48 81 c6 d0 eb ff ff 	add    rsi,0xffffffffffffebd0
    e12c:	4c 89 fa             	mov    rdx,r15
    e12f:	e8 ec 2f ff ff       	call   1120 <memcpy@plt>
    e134:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e138:	0f b7 5f 36          	movzx  ebx,WORD PTR [rdi+0x36]
    e13c:	2b 9d 70 ff ff ff    	sub    ebx,DWORD PTR [rbp-0x90]
    e142:	44 0f b7 e3          	movzx  r12d,bx
    e146:	49 01 fc             	add    r12,rdi
    e149:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    e14d:	4c 8b 30             	mov    r14,QWORD PTR [rax]
    e150:	4d 85 f6             	test   r14,r14
    e153:	75 6c                	jne    e1c1 <zbtScoreInsertAt+0x1b11>
    e155:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    e159:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    e15d:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    e164:	77 1c                	ja     e182 <zbtScoreInsertAt+0x1ad2>
    e166:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    e169:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    e170:	0f 87 d8 00 00 00    	ja     e24e <zbtScoreInsertAt+0x1b9e>
    e176:	bf 01 00 00 00       	mov    edi,0x1
    e17b:	89 d0                	mov    eax,edx
    e17d:	e9 d9 00 00 00       	jmp    e25b <zbtScoreInsertAt+0x1bab>
    e182:	48 8d b5 00 fb ff ff 	lea    rsi,[rbp-0x500]
    e189:	48 89 d7             	mov    rdi,rdx
    e18c:	49 89 c5             	mov    r13,rax
    e18f:	e8 7c 3a 00 00       	call   11c10 <zmalloc_usable>
    e194:	48 8b 8d 00 fb ff ff 	mov    rcx,QWORD PTR [rbp-0x500]
    e19b:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    e1a2:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    e1a6:	49 89 c6             	mov    r14,rax
    e1a9:	49 8b 75 00          	mov    rsi,QWORD PTR [r13+0x0]
    e1ad:	49 8b 55 08          	mov    rdx,QWORD PTR [r13+0x8]
    e1b1:	4c 8b 6d 80          	mov    r13,QWORD PTR [rbp-0x80]
    e1b5:	48 89 c7             	mov    rdi,rax
    e1b8:	e8 63 2f ff ff       	call   1120 <memcpy@plt>
    e1bd:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e1c1:	48 8b 55 a8          	mov    rdx,QWORD PTR [rbp-0x58]
    e1c5:	48 8b 42 08          	mov    rax,QWORD PTR [rdx+0x8]
    e1c9:	41 c6 04 24 ff       	mov    BYTE PTR [r12],0xff
    e1ce:	8b 4a 10             	mov    ecx,DWORD PTR [rdx+0x10]
    e1d1:	41 89 4c 24 01       	mov    DWORD PTR [r12+0x1],ecx
    e1d6:	49 89 44 24 05       	mov    QWORD PTR [r12+0x5],rax
    e1db:	4d 89 74 24 0d       	mov    QWORD PTR [r12+0xd],r14
    e1e0:	4c 8b 72 20          	mov    r14,QWORD PTR [rdx+0x20]
    e1e4:	4d 85 f6             	test   r14,r14
    e1e7:	4c 8b 7d b8          	mov    r15,QWORD PTR [rbp-0x48]
    e1eb:	74 2a                	je     e217 <zbtScoreInsertAt+0x1b67>
    e1ed:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    e1f1:	74 1c                	je     e20f <zbtScoreInsertAt+0x1b5f>
    e1f3:	48 8d 3d 24 54 00 00 	lea    rdi,[rip+0x5424]        # 1361e <_IO_stdin_used+0x61e>
    e1fa:	48 8d 15 55 55 00 00 	lea    rdx,[rip+0x5555]        # 13756 <_IO_stdin_used+0x756>
    e201:	be 4c 02 00 00       	mov    esi,0x24c
    e206:	e8 05 39 00 00       	call   11b10 <standalone_panic>
    e20b:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e20f:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    e216:	00
    e217:	66 0f ef c0          	pxor   xmm0,xmm0
    e21b:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    e21f:	f3 0f 7f 00          	movdqu XMMWORD PTR [rax],xmm0
    e223:	c6 47 14 01          	mov    BYTE PTR [rdi+0x14],0x1
    e227:	44 8b 75 88          	mov    r14d,DWORD PTR [rbp-0x78]
    e22b:	44 88 77 11          	mov    BYTE PTR [rdi+0x11],r14b
    e22f:	4c 89 6f 08          	mov    QWORD PTR [rdi+0x8],r13
    e233:	66 89 5f 36          	mov    WORD PTR [rdi+0x36],bx
    e237:	66 41 89 1f          	mov    WORD PTR [r15],bx
    e23b:	be 01 00 00 00       	mov    esi,0x1
    e240:	e8 2b 0f 00 00       	call   f170 <zbtScoreUpdatePath>
    e245:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    e249:	e9 b7 fb ff ff       	jmp    de05 <zbtScoreInsertAt+0x1755>
    e24e:	66 41 89 54 24 01    	mov    WORD PTR [r12+0x1],dx
    e254:	bf 03 00 00 00       	mov    edi,0x3
    e259:	b0 fe                	mov    al,0xfe
    e25b:	44 8b 75 88          	mov    r14d,DWORD PTR [rbp-0x78]
    e25f:	4c 8b 7d b8          	mov    r15,QWORD PTR [rbp-0x48]
    e263:	41 88 04 24          	mov    BYTE PTR [r12],al
    e267:	4c 01 e7             	add    rdi,r12
    e26a:	e8 b1 2e ff ff       	call   1120 <memcpy@plt>
    e26f:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    e273:	eb b6                	jmp    e22b <zbtScoreInsertAt+0x1b7b>

Disassembly of section .fini:
