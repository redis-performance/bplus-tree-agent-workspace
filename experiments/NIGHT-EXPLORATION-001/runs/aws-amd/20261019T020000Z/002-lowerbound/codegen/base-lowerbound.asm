
scratch/amd-lowerbound-build/base/build/native/btree-bench:     file format elf64-x86-64


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
    a77d:	48 83 ec 38          	sub    rsp,0x38
    a781:	48 89 55 b8          	mov    QWORD PTR [rbp-0x48],rdx
    a785:	48 89 75 a8          	mov    QWORD PTR [rbp-0x58],rsi
    a789:	44 0f b6 4f 11       	movzx  r9d,BYTE PTR [rdi+0x11]
    a78e:	45 85 c9             	test   r9d,r9d
    a791:	0f 84 92 02 00 00    	je     aa29 <zbtScoreLeafLowerBound+0x2b9>
    a797:	49 89 ff             	mov    r15,rdi
    a79a:	4c 8d 57 38          	lea    r10,[rdi+0x38]
    a79e:	44 0f b6 47 34       	movzx  r8d,BYTE PTR [rdi+0x34]
    a7a3:	45 31 db             	xor    r11d,r11d
    a7a6:	f2 0f 11 45 c0       	movsd  QWORD PTR [rbp-0x40],xmm0
    a7ab:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    a7af:	eb 1b                	jmp    a7cc <zbtScoreLeafLowerBound+0x5c>
    a7b1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    a7b8:	0f 1f 84 00 00 00 00 
    a7bf:	00 
    a7c0:	45 89 f1             	mov    r9d,r14d
    a7c3:	45 39 cb             	cmp    r11d,r9d
    a7c6:	0f 83 60 02 00 00    	jae    aa2c <zbtScoreLeafLowerBound+0x2bc>
    a7cc:	45 84 c0             	test   r8b,r8b
    a7cf:	74 1f                	je     a7f0 <zbtScoreLeafLowerBound+0x80>
    a7d1:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    a7d6:	41 0f b6 c0          	movzx  eax,r8b
    a7da:	0f af c1             	imul   eax,ecx
    a7dd:	83 c0 07             	add    eax,0x7
    a7e0:	c1 e8 03             	shr    eax,0x3
    a7e3:	83 c0 09             	add    eax,0x9
    a7e6:	83 e0 fe             	and    eax,0xfffffffe
    a7e9:	eb 07                	jmp    a7f2 <zbtScoreLeafLowerBound+0x82>
    a7eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    a7f0:	31 c0                	xor    eax,eax
    a7f2:	45 89 ce             	mov    r14d,r9d
    a7f5:	45 29 de             	sub    r14d,r11d
    a7f8:	41 d1 ee             	shr    r14d,1
    a7fb:	45 01 de             	add    r14d,r11d
    a7fe:	41 0f b6 57 35       	movzx  edx,BYTE PTR [r15+0x35]
    a803:	45 89 f4             	mov    r12d,r14d
    a806:	41 f7 d4             	not    r12d
    a809:	44 89 f1             	mov    ecx,r14d
    a80c:	84 d2                	test   dl,dl
    a80e:	74 08                	je     a818 <zbtScoreLeafLowerBound+0xa8>
    a810:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    a815:	44 01 e1             	add    ecx,r12d
    a818:	4c 01 d0             	add    rax,r10
    a81b:	89 c9                	mov    ecx,ecx
    a81d:	0f b7 04 48          	movzx  eax,WORD PTR [rax+rcx*2]
    a821:	49 8d 1c 07          	lea    rbx,[r15+rax*1]
    a825:	45 0f b6 2c 07       	movzx  r13d,BYTE PTR [r15+rax*1]
    a82a:	49 81 fd fd 00 00 00 	cmp    r13,0xfd
    a831:	77 1d                	ja     a850 <zbtScoreLeafLowerBound+0xe0>
    a833:	48 ff c3             	inc    rbx
    a836:	48 89 5d b0          	mov    QWORD PTR [rbp-0x50],rbx
    a83a:	45 84 c0             	test   r8b,r8b
    a83d:	0f 85 bd 00 00 00    	jne    a900 <zbtScoreLeafLowerBound+0x190>
    a843:	eb 2a                	jmp    a86f <zbtScoreLeafLowerBound+0xff>
    a845:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    a84c:	00 00 00 00 
    a850:	41 81 fd fe 00 00 00 	cmp    r13d,0xfe
    a857:	75 27                	jne    a880 <zbtScoreLeafLowerBound+0x110>
    a859:	44 0f b7 6b 01       	movzx  r13d,WORD PTR [rbx+0x1]
    a85e:	48 83 c3 03          	add    rbx,0x3
    a862:	48 89 5d b0          	mov    QWORD PTR [rbp-0x50],rbx
    a866:	45 84 c0             	test   r8b,r8b
    a869:	0f 85 91 00 00 00    	jne    a900 <zbtScoreLeafLowerBound+0x190>
    a86f:	31 ff                	xor    edi,edi
    a871:	e9 00 01 00 00       	jmp    a976 <zbtScoreLeafLowerBound+0x206>
    a876:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    a87d:	00 00 00 
    a880:	48 8b 43 0d          	mov    rax,QWORD PTR [rbx+0xd]
    a884:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    a888:	48 85 c0             	test   rax,rax
    a88b:	75 5c                	jne    a8e9 <zbtScoreLeafLowerBound+0x179>
    a88d:	48 8d 3d 8a 8d 00 00 	lea    rdi,[rip+0x8d8a]        # 1361e <_IO_stdin_used+0x61e>
    a894:	be 57 02 00 00       	mov    esi,0x257
    a899:	48 8d 15 aa 8e 00 00 	lea    rdx,[rip+0x8eaa]        # 1374a <_IO_stdin_used+0x74a>
    a8a0:	45 89 cd             	mov    r13d,r9d
    a8a3:	4c 89 5d d0          	mov    QWORD PTR [rbp-0x30],r11
    a8a7:	e8 f4 6d 00 00       	call   116a0 <standalone_panic>
    a8ac:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    a8b0:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    a8b4:	45 89 e9             	mov    r9d,r13d
    a8b7:	f2 0f 10 45 c0       	movsd  xmm0,QWORD PTR [rbp-0x40]
    a8bc:	80 3b ff             	cmp    BYTE PTR [rbx],0xff
    a8bf:	74 28                	je     a8e9 <zbtScoreLeafLowerBound+0x179>
    a8c1:	48 8d 3d 56 8d 00 00 	lea    rdi,[rip+0x8d56]        # 1361e <_IO_stdin_used+0x61e>
    a8c8:	be 37 02 00 00       	mov    esi,0x237
    a8cd:	48 8d 15 82 8e 00 00 	lea    rdx,[rip+0x8e82]        # 13756 <_IO_stdin_used+0x756>
    a8d4:	e8 c7 6d 00 00       	call   116a0 <standalone_panic>
    a8d9:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    a8dd:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    a8e1:	45 89 e9             	mov    r9d,r13d
    a8e4:	f2 0f 10 45 c0       	movsd  xmm0,QWORD PTR [rbp-0x40]
    a8e9:	4c 8b 6b 05          	mov    r13,QWORD PTR [rbx+0x5]
    a8ed:	45 0f b6 47 34       	movzx  r8d,BYTE PTR [r15+0x34]
    a8f2:	41 0f b6 57 35       	movzx  edx,BYTE PTR [r15+0x35]
    a8f7:	45 84 c0             	test   r8b,r8b
    a8fa:	0f 84 6f ff ff ff    	je     a86f <zbtScoreLeafLowerBound+0xff>
    a900:	44 89 f1             	mov    ecx,r14d
    a903:	84 d2                	test   dl,dl
    a905:	74 08                	je     a90f <zbtScoreLeafLowerBound+0x19f>
    a907:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    a90c:	44 01 e1             	add    ecx,r12d
    a90f:	44 89 c3             	mov    ebx,r8d
    a912:	41 0f b6 c0          	movzx  eax,r8b
    a916:	89 cf                	mov    edi,ecx
    a918:	48 0f af f8          	imul   rdi,rax
    a91c:	49 89 f8             	mov    r8,rdi
    a91f:	49 c1 e8 03          	shr    r8,0x3
    a923:	4b 8b 34 02          	mov    rsi,QWORD PTR [r10+r8*1]
    a927:	89 f9                	mov    ecx,edi
    a929:	80 e1 07             	and    cl,0x7
    a92c:	48 d3 ee             	shr    rsi,cl
    a92f:	83 e7 07             	and    edi,0x7
    a932:	74 17                	je     a94b <zbtScoreLeafLowerBound+0x1db>
    a934:	b9 40 00 00 00       	mov    ecx,0x40
    a939:	29 f9                	sub    ecx,edi
    a93b:	39 c1                	cmp    ecx,eax
    a93d:	73 0c                	jae    a94b <zbtScoreLeafLowerBound+0x1db>
    a93f:	43 0f b6 7c 38 40    	movzx  edi,BYTE PTR [r8+r15*1+0x40]
    a945:	48 d3 e7             	shl    rdi,cl
    a948:	48 09 fe             	or     rsi,rdi
    a94b:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    a952:	89 c1                	mov    ecx,eax
    a954:	48 d3 e7             	shl    rdi,cl
    a957:	41 89 d8             	mov    r8d,ebx
    a95a:	80 fb 40             	cmp    bl,0x40
    a95d:	48 f7 d7             	not    rdi
    a960:	48 c7 c0 ff ff ff ff 	mov    rax,0xffffffffffffffff
    a967:	48 0f 43 f8          	cmovae rdi,rax
    a96b:	48 21 f7             	and    rdi,rsi
    a96e:	41 0f b6 4f 13       	movzx  ecx,BYTE PTR [r15+0x13]
    a973:	48 d3 e7             	shl    rdi,cl
    a976:	48 89 f8             	mov    rax,rdi
    a979:	48 f7 d8             	neg    rax
    a97c:	84 d2                	test   dl,dl
    a97e:	48 0f 44 c7          	cmove  rax,rdi
    a982:	49 03 47 28          	add    rax,QWORD PTR [r15+0x28]
    a986:	48 89 c1             	mov    rcx,rax
    a989:	48 ba ff ff ff ff ff 	movabs rdx,0x7fffffffffffffff
    a990:	ff ff 7f 
    a993:	48 21 d1             	and    rcx,rdx
    a996:	48 85 c0             	test   rax,rax
    a999:	48 f7 d0             	not    rax
    a99c:	48 0f 48 c1          	cmovs  rax,rcx
    a9a0:	66 48 0f 6e c8       	movq   xmm1,rax
    a9a5:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a9aa:	66 0f 2e c1          	ucomisd xmm0,xmm1
    a9ae:	77 60                	ja     aa10 <zbtScoreLeafLowerBound+0x2a0>
    a9b0:	b8 01 00 00 00       	mov    eax,0x1
    a9b5:	66 0f 2e c8          	ucomisd xmm1,xmm0
    a9b9:	77 55                	ja     aa10 <zbtScoreLeafLowerBound+0x2a0>
    a9bb:	44 88 45 d0          	mov    BYTE PTR [rbp-0x30],r8b
    a9bf:	4d 89 dc             	mov    r12,r11
    a9c2:	44 89 cb             	mov    ebx,r9d
    a9c5:	4c 89 ea             	mov    rdx,r13
    a9c8:	4c 3b 6d b8          	cmp    r13,QWORD PTR [rbp-0x48]
    a9cc:	72 04                	jb     a9d2 <zbtScoreLeafLowerBound+0x262>
    a9ce:	48 8b 55 b8          	mov    rdx,QWORD PTR [rbp-0x48]
    a9d2:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    a9d6:	48 8b 75 a8          	mov    rsi,QWORD PTR [rbp-0x58]
    a9da:	e8 01 67 ff ff       	call   10e0 <memcmp@plt>
    a9df:	85 c0                	test   eax,eax
    a9e1:	f2 0f 10 45 c0       	movsd  xmm0,QWORD PTR [rbp-0x40]
    a9e6:	41 89 d9             	mov    r9d,ebx
    a9e9:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    a9ed:	4d 89 e3             	mov    r11,r12
    a9f0:	44 0f b6 45 d0       	movzx  r8d,BYTE PTR [rbp-0x30]
    a9f5:	75 19                	jne    aa10 <zbtScoreLeafLowerBound+0x2a0>
    a9f7:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a9fc:	4c 3b 6d b8          	cmp    r13,QWORD PTR [rbp-0x48]
    aa00:	72 0e                	jb     aa10 <zbtScoreLeafLowerBound+0x2a0>
    aa02:	0f 97 c0             	seta   al
    aa05:	0f b6 c0             	movzx  eax,al
    aa08:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    aa0f:	00 
    aa10:	85 c0                	test   eax,eax
    aa12:	0f 89 a8 fd ff ff    	jns    a7c0 <zbtScoreLeafLowerBound+0x50>
    aa18:	41 ff c6             	inc    r14d
    aa1b:	45 89 f3             	mov    r11d,r14d
    aa1e:	45 39 cb             	cmp    r11d,r9d
    aa21:	0f 82 a5 fd ff ff    	jb     a7cc <zbtScoreLeafLowerBound+0x5c>
    aa27:	eb 03                	jmp    aa2c <zbtScoreLeafLowerBound+0x2bc>
    aa29:	45 31 db             	xor    r11d,r11d
    aa2c:	44 89 d8             	mov    eax,r11d
    aa2f:	48 83 c4 38          	add    rsp,0x38
    aa33:	5b                   	pop    rbx
    aa34:	41 5c                	pop    r12
    aa36:	41 5d                	pop    r13
    aa38:	41 5e                	pop    r14
    aa3a:	41 5f                	pop    r15
    aa3c:	5d                   	pop    rbp
    aa3d:	c3                   	ret

Disassembly of section .fini:
