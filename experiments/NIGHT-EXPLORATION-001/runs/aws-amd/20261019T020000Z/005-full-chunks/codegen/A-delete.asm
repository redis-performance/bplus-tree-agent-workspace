
scratch/amd-chunk-build/A/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000f8a0 <zbtScoreDeleteInPlace>:
    f8a0:	55                   	push   rbp
    f8a1:	48 89 e5             	mov    rbp,rsp
    f8a4:	41 57                	push   r15
    f8a6:	41 56                	push   r14
    f8a8:	41 55                	push   r13
    f8aa:	41 54                	push   r12
    f8ac:	53                   	push   rbx
    f8ad:	48 81 ec e8 00 00 00 	sub    rsp,0xe8
    f8b4:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    f8b7:	41 89 d7             	mov    r15d,edx
    f8ba:	49 89 f4             	mov    r12,rsi
    f8bd:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    f8c1:	44 0f b6 76 11       	movzx  r14d,BYTE PTR [rsi+0x11]
    f8c6:	41 8d 5e ff          	lea    ebx,[r14-0x1]
    f8ca:	41 39 d6             	cmp    r14d,edx
    f8cd:	76 04                	jbe    f8d3 <zbtScoreDeleteInPlace+0x33>
    f8cf:	85 db                	test   ebx,ebx
    f8d1:	75 18                	jne    f8eb <zbtScoreDeleteInPlace+0x4b>
    f8d3:	48 8d 3d 44 3d 00 00 	lea    rdi,[rip+0x3d44]        # 1361e <_IO_stdin_used+0x61e>
    f8da:	48 8d 15 1a 41 00 00 	lea    rdx,[rip+0x411a]        # 139fb <_IO_stdin_used+0x9fb>
    f8e1:	be 02 0a 00 00       	mov    esi,0xa02
    f8e6:	e8 25 22 00 00       	call   11b10 <standalone_panic>
    f8eb:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    f8f1:	74 0c                	je     f8ff <zbtScoreDeleteInPlace+0x5f>
    f8f3:	41 0f b6 44 24 11    	movzx  eax,BYTE PTR [r12+0x11]
    f8f9:	41 f7 d7             	not    r15d
    f8fc:	41 01 c7             	add    r15d,eax
    f8ff:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    f905:	48 85 c0             	test   rax,rax
    f908:	74 1f                	je     f929 <zbtScoreDeleteInPlace+0x89>
    f90a:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    f910:	0f af c1             	imul   eax,ecx
    f913:	83 c0 07             	add    eax,0x7
    f916:	c1 e8 03             	shr    eax,0x3
    f919:	83 c0 09             	add    eax,0x9
    f91c:	83 e0 fe             	and    eax,0xfffffffe
    f91f:	4d 8d 2c 04          	lea    r13,[r12+rax*1]
    f923:	49 83 c5 38          	add    r13,0x38
    f927:	eb 0d                	jmp    f936 <zbtScoreDeleteInPlace+0x96>
    f929:	4d 8d 6c 24 38       	lea    r13,[r12+0x38]
    f92e:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    f934:	31 c0                	xor    eax,eax
    f936:	4c 01 e0             	add    rax,r12
    f939:	48 83 c0 38          	add    rax,0x38
    f93d:	48 8d 34 48          	lea    rsi,[rax+rcx*2]
    f941:	48 8d bd f0 fe ff ff 	lea    rdi,[rbp-0x110]
    f948:	4c 89 f2             	mov    rdx,r14
    f94b:	e8 d0 17 ff ff       	call   1120 <memcpy@plt>
    f950:	44 89 7d c0          	mov    DWORD PTR [rbp-0x40],r15d
    f954:	44 89 f8             	mov    eax,r15d
    f957:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    f95b:	41 0f b7 74 45 00    	movzx  esi,WORD PTR [r13+rax*2+0x0]
    f961:	44 0f b7 fe          	movzx  r15d,si
    f965:	43 0f b6 04 3c       	movzx  eax,BYTE PTR [r12+r15*1]
    f96a:	3d fe 00 00 00       	cmp    eax,0xfe
    f96f:	89 75 90             	mov    DWORD PTR [rbp-0x70],esi
    f972:	89 5d bc             	mov    DWORD PTR [rbp-0x44],ebx
    f975:	4c 89 6d b0          	mov    QWORD PTR [rbp-0x50],r13
    f979:	74 21                	je     f99c <zbtScoreDeleteInPlace+0xfc>
    f97b:	3d ff 00 00 00       	cmp    eax,0xff
    f980:	8b 55 c8             	mov    edx,DWORD PTR [rbp-0x38]
    f983:	75 20                	jne    f9a5 <zbtScoreDeleteInPlace+0x105>
    f985:	85 d2                	test   edx,edx
    f987:	74 46                	je     f9cf <zbtScoreDeleteInPlace+0x12f>
    f989:	41 89 f5             	mov    r13d,esi
    f98c:	4b 8b 7c 3c 0d       	mov    rdi,QWORD PTR [r12+r15*1+0xd]
    f991:	48 85 ff             	test   rdi,rdi
    f994:	74 40                	je     f9d6 <zbtScoreDeleteInPlace+0x136>
    f996:	48 8d 75 98          	lea    rsi,[rbp-0x68]
    f99a:	eb 58                	jmp    f9f4 <zbtScoreDeleteInPlace+0x154>
    f99c:	43 0f b7 44 3c 01    	movzx  eax,WORD PTR [r12+r15*1+0x1]
    f9a2:	8b 55 c8             	mov    edx,DWORD PTR [rbp-0x38]
    f9a5:	31 c9                	xor    ecx,ecx
    f9a7:	48 3d fe 00 00 00    	cmp    rax,0xfe
    f9ad:	0f 93 c1             	setae  cl
    f9b0:	48 8d 1c 48          	lea    rbx,[rax+rcx*2]
    f9b4:	48 ff c3             	inc    rbx
    f9b7:	85 d2                	test   edx,edx
    f9b9:	0f 84 89 00 00 00    	je     fa48 <zbtScoreDeleteInPlace+0x1a8>
    f9bf:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    f9c5:	66 39 c6             	cmp    si,ax
    f9c8:	75 52                	jne    fa1c <zbtScoreDeleteInPlace+0x17c>
    f9ca:	e9 8c 00 00 00       	jmp    fa5b <zbtScoreDeleteInPlace+0x1bb>
    f9cf:	bb 15 00 00 00       	mov    ebx,0x15
    f9d4:	eb 72                	jmp    fa48 <zbtScoreDeleteInPlace+0x1a8>
    f9d6:	48 8d 3d 41 3c 00 00 	lea    rdi,[rip+0x3c41]        # 1361e <_IO_stdin_used+0x61e>
    f9dd:	48 8d 15 34 40 00 00 	lea    rdx,[rip+0x4034]        # 13a18 <_IO_stdin_used+0xa18>
    f9e4:	be 0e 0a 00 00       	mov    esi,0xa0e
    f9e9:	e8 22 21 00 00       	call   11b10 <standalone_panic>
    f9ee:	48 8d 75 98          	lea    rsi,[rbp-0x68]
    f9f2:	31 ff                	xor    edi,edi
    f9f4:	e8 17 23 00 00       	call   11d10 <zfree_usable>
    f9f9:	48 8b 45 98          	mov    rax,QWORD PTR [rbp-0x68]
    f9fd:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fa01:	48 29 41 68          	sub    QWORD PTR [rcx+0x68],rax
    fa05:	bb 15 00 00 00       	mov    ebx,0x15
    fa0a:	44 89 ee             	mov    esi,r13d
    fa0d:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    fa11:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa17:	66 39 c6             	cmp    si,ax
    fa1a:	74 3f                	je     fa5b <zbtScoreDeleteInPlace+0x1bb>
    fa1c:	4d 85 f6             	test   r14,r14
    fa1f:	74 27                	je     fa48 <zbtScoreDeleteInPlace+0x1a8>
    fa21:	b9 01 00 00 00       	mov    ecx,0x1
    fa26:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    fa2d:	00 00 00
    fa30:	41 0f b7 54 4d fe    	movzx  edx,WORD PTR [r13+rcx*2-0x2]
    fa36:	4c 39 f1             	cmp    rcx,r14
    fa39:	73 08                	jae    fa43 <zbtScoreDeleteInPlace+0x1a3>
    fa3b:	48 ff c1             	inc    rcx
    fa3e:	66 39 f2             	cmp    dx,si
    fa41:	76 ed                	jbe    fa30 <zbtScoreDeleteInPlace+0x190>
    fa43:	66 39 f2             	cmp    dx,si
    fa46:	77 13                	ja     fa5b <zbtScoreDeleteInPlace+0x1bb>
    fa48:	31 c9                	xor    ecx,ecx
    fa4a:	66 41 3b 74 24 36    	cmp    si,WORD PTR [r12+0x36]
    fa50:	75 34                	jne    fa86 <zbtScoreDeleteInPlace+0x1e6>
    fa52:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa57:	89 f0                	mov    eax,esi
    fa59:	eb 20                	jmp    fa7b <zbtScoreDeleteInPlace+0x1db>
    fa5b:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa60:	49 8d 34 04          	lea    rsi,[r12+rax*1]
    fa64:	48 8d 3c 1e          	lea    rdi,[rsi+rbx*1]
    fa68:	49 29 c7             	sub    r15,rax
    fa6b:	4c 89 fa             	mov    rdx,r15
    fa6e:	e8 ed 16 ff ff       	call   1160 <memmove@plt>
    fa73:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa79:	b1 01                	mov    cl,0x1
    fa7b:	89 4d c4             	mov    DWORD PTR [rbp-0x3c],ecx
    fa7e:	01 d8                	add    eax,ebx
    fa80:	66 41 89 06          	mov    WORD PTR [r14],ax
    fa84:	eb 07                	jmp    fa8d <zbtScoreDeleteInPlace+0x1ed>
    fa86:	c7 45 c4 00 00 00 00 	mov    DWORD PTR [rbp-0x3c],0x0
    fa8d:	4d 8d 74 24 38       	lea    r14,[r12+0x38]
    fa92:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    fa96:	48 8d 3c 45 00 00 00 	lea    rdi,[rax*2+0x0]
    fa9d:	00
    fa9e:	4c 01 ef             	add    rdi,r13
    faa1:	41 0f b6 74 24 34    	movzx  esi,BYTE PTR [r12+0x34]
    faa7:	85 f6                	test   esi,esi
    faa9:	4c 89 65 80          	mov    QWORD PTR [rbp-0x80],r12
    faad:	0f 84 cb 02 00 00    	je     fd7e <zbtScoreDeleteInPlace+0x4de>
    fab3:	41 89 f1             	mov    r9d,esi
    fab6:	4d 89 ca             	mov    r10,r9
    fab9:	4c 0f af 55 a8       	imul   r10,QWORD PTR [rbp-0x58]
    fabe:	45 0f b6 44 24 11    	movzx  r8d,BYTE PTR [r12+0x11]
    fac4:	8b 45 c0             	mov    eax,DWORD PTR [rbp-0x40]
    fac7:	41 89 c3             	mov    r11d,eax
    faca:	41 f7 d3             	not    r11d
    facd:	45 01 c3             	add    r11d,r8d
    fad0:	4d 0f af d9          	imul   r11,r9
    fad4:	49 83 fb 40          	cmp    r11,0x40
    fad8:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    fadc:	48 89 bd 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rdi
    fae3:	89 75 94             	mov    DWORD PTR [rbp-0x6c],esi
    fae6:	4c 89 85 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],r8
    faed:	4c 89 8d 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],r9
    faf4:	4c 89 9d 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],r11
    fafb:	0f 82 27 01 00 00    	jb     fc28 <zbtScoreDeleteInPlace+0x388>
    fb01:	4b 8d 04 0a          	lea    rax,[r10+r9*1]
    fb05:	48 89 45 d0          	mov    QWORD PTR [rbp-0x30],rax
    fb09:	41 89 c7             	mov    r15d,eax
    fb0c:	41 83 e7 07          	and    r15d,0x7
    fb10:	41 bd 40 00 00 00    	mov    r13d,0x40
    fb16:	45 29 fd             	sub    r13d,r15d
    fb19:	41 83 e2 07          	and    r10d,0x7
    fb1d:	44 89 d1             	mov    ecx,r10d
    fb20:	f7 d9                	neg    ecx
    fb22:	48 c7 c0 ff ff ff ff 	mov    rax,0xffffffffffffffff
    fb29:	48 d3 e0             	shl    rax,cl
    fb2c:	31 d2                	xor    edx,edx
    fb2e:	41 83 fa 01          	cmp    r10d,0x1
    fb32:	48 19 d2             	sbb    rdx,rdx
    fb35:	48 f7 d0             	not    rax
    fb38:	48 09 c2             	or     rdx,rax
    fb3b:	49 89 d4             	mov    r12,rdx
    fb3e:	44 89 d1             	mov    ecx,r10d
    fb41:	49 d3 e4             	shl    r12,cl
    fb44:	b8 7e 00 00 00       	mov    eax,0x7e
    fb49:	d3 e8                	shr    eax,cl
    fb4b:	d3 e0                	shl    eax,cl
    fb4d:	49 f7 d4             	not    r12
    fb50:	45 85 d2             	test   r10d,r10d
    fb53:	0f 84 03 06 00 00    	je     1015c <zbtScoreDeleteInPlace+0x8bc>
    fb59:	48 89 c1             	mov    rcx,rax
    fb5c:	4c 89 65 88          	mov    QWORD PTR [rbp-0x78],r12
    fb60:	49 89 d4             	mov    r12,rdx
    fb63:	be 40 00 00 00       	mov    esi,0x40
    fb68:	4c 89 d0             	mov    rax,r10
    fb6b:	44 29 d6             	sub    esi,r10d
    fb6e:	89 ca                	mov    edx,ecx
    fb70:	83 f2 7f             	xor    edx,0x7f
    fb73:	49 89 d1             	mov    r9,rdx
    fb76:	48 83 f1 80          	xor    rcx,0xffffffffffffff80
    fb7a:	49 89 ca             	mov    r10,rcx
    fb7d:	4c 89 fa             	mov    rdx,r15
    fb80:	45 85 ff             	test   r15d,r15d
    fb83:	0f 84 5d 06 00 00    	je     101e6 <zbtScoreDeleteInPlace+0x946>
    fb89:	45 31 ff             	xor    r15d,r15d
    fb8c:	4d 89 d8             	mov    r8,r11
    fb8f:	4c 89 6d a0          	mov    QWORD PTR [rbp-0x60],r13
    fb93:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fb97:	48 8b 7d 88          	mov    rdi,QWORD PTR [rbp-0x78]
    fb9b:	49 89 f5             	mov    r13,rsi
    fb9e:	4c 89 8d 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],r9
    fba5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    fbac:	00 00 00 00
    fbb0:	4a 8d 34 39          	lea    rsi,[rcx+r15*1]
    fbb4:	48 c1 ee 03          	shr    rsi,0x3
    fbb8:	4d 8b 0c 36          	mov    r9,QWORD PTR [r14+rsi*1]
    fbbc:	89 d1                	mov    ecx,edx
    fbbe:	49 d3 e9             	shr    r9,cl
    fbc1:	45 0f b6 5c 36 08    	movzx  r11d,BYTE PTR [r14+rsi*1+0x8]
    fbc7:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    fbcb:	49 d3 e3             	shl    r11,cl
    fbce:	4d 09 cb             	or     r11,r9
    fbd1:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    fbd5:	4a 8d 34 39          	lea    rsi,[rcx+r15*1]
    fbd9:	48 c1 ee 03          	shr    rsi,0x3
    fbdd:	4d 89 d9             	mov    r9,r11
    fbe0:	4d 21 e1             	and    r9,r12
    fbe3:	89 c1                	mov    ecx,eax
    fbe5:	49 d3 e1             	shl    r9,cl
    fbe8:	49 8b 0c 36          	mov    rcx,QWORD PTR [r14+rsi*1]
    fbec:	48 21 f9             	and    rcx,rdi
    fbef:	49 09 c9             	or     r9,rcx
    fbf2:	4d 89 0c 36          	mov    QWORD PTR [r14+rsi*1],r9
    fbf6:	44 89 e9             	mov    ecx,r13d
    fbf9:	49 d3 eb             	shr    r11,cl
    fbfc:	41 0f b6 4c 36 08    	movzx  ecx,BYTE PTR [r14+rsi*1+0x8]
    fc02:	44 21 d1             	and    ecx,r10d
    fc05:	44 23 9d 58 ff ff ff 	and    r11d,DWORD PTR [rbp-0xa8]
    fc0c:	41 09 cb             	or     r11d,ecx
    fc0f:	45 88 5c 36 08       	mov    BYTE PTR [r14+rsi*1+0x8],r11b
    fc14:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fc18:	49 83 c7 40          	add    r15,0x40
    fc1c:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    fc20:	49 83 f8 3f          	cmp    r8,0x3f
    fc24:	77 8a                	ja     fbb0 <zbtScoreDeleteInPlace+0x310>
    fc26:	eb 06                	jmp    fc2e <zbtScoreDeleteInPlace+0x38e>
    fc28:	45 31 ff             	xor    r15d,r15d
    fc2b:	4d 89 d8             	mov    r8,r11
    fc2e:	4c 3b bd 78 ff ff ff 	cmp    r15,QWORD PTR [rbp-0x88]
    fc35:	4c 8b 65 80          	mov    r12,QWORD PTR [rbp-0x80]
    fc39:	4c 8b 9d 70 ff ff ff 	mov    r11,QWORD PTR [rbp-0x90]
    fc40:	0f 83 bd 00 00 00    	jae    fd03 <zbtScoreDeleteInPlace+0x463>
    fc46:	4c 8b 6d c8          	mov    r13,QWORD PTR [rbp-0x38]
    fc4a:	4b 8d 0c 2b          	lea    rcx,[r11+r13*1]
    fc4e:	49 8d 14 0f          	lea    rdx,[r15+rcx*1]
    fc52:	48 c1 ea 03          	shr    rdx,0x3
    fc56:	89 ce                	mov    esi,ecx
    fc58:	83 e6 07             	and    esi,0x7
    fc5b:	b8 40 00 00 00       	mov    eax,0x40
    fc60:	41 b9 40 00 00 00    	mov    r9d,0x40
    fc66:	41 29 f1             	sub    r9d,esi
    fc69:	4d 8b 14 16          	mov    r10,QWORD PTR [r14+rdx*1]
    fc6d:	80 e1 07             	and    cl,0x7
    fc70:	49 d3 ea             	shr    r10,cl
    fc73:	45 39 c1             	cmp    r9d,r8d
    fc76:	73 0f                	jae    fc87 <zbtScoreDeleteInPlace+0x3e7>
    fc78:	41 0f b6 54 16 08    	movzx  edx,BYTE PTR [r14+rdx*1+0x8]
    fc7e:	44 89 c9             	mov    ecx,r9d
    fc81:	48 d3 e2             	shl    rdx,cl
    fc84:	49 09 d2             	or     r10,rdx
    fc87:	48 c7 c2 ff ff ff ff 	mov    rdx,0xffffffffffffffff
    fc8e:	44 89 c1             	mov    ecx,r8d
    fc91:	48 d3 e2             	shl    rdx,cl
    fc94:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    fc9b:	48 f7 d2             	not    rdx
    fc9e:	4c 21 d2             	and    rdx,r10
    fca1:	4d 01 ef             	add    r15,r13
    fca4:	49 c1 ef 03          	shr    r15,0x3
    fca8:	41 83 e5 07          	and    r13d,0x7
    fcac:	44 29 e8             	sub    eax,r13d
    fcaf:	44 39 c0             	cmp    eax,r8d
    fcb2:	45 89 c1             	mov    r9d,r8d
    fcb5:	44 0f 42 c8          	cmovb  r9d,eax
    fcb9:	44 89 c9             	mov    ecx,r9d
    fcbc:	48 d3 e7             	shl    rdi,cl
    fcbf:	48 f7 d7             	not    rdi
    fcc2:	48 89 d6             	mov    rsi,rdx
    fcc5:	48 21 fe             	and    rsi,rdi
    fcc8:	44 89 e9             	mov    ecx,r13d
    fccb:	48 d3 e7             	shl    rdi,cl
    fcce:	48 f7 d7             	not    rdi
    fcd1:	4b 23 3c 3e          	and    rdi,QWORD PTR [r14+r15*1]
    fcd5:	48 d3 e6             	shl    rsi,cl
    fcd8:	48 09 fe             	or     rsi,rdi
    fcdb:	4b 89 34 3e          	mov    QWORD PTR [r14+r15*1],rsi
    fcdf:	44 39 c0             	cmp    eax,r8d
    fce2:	73 1f                	jae    fd03 <zbtScoreDeleteInPlace+0x463>
    fce4:	45 29 c8             	sub    r8d,r9d
    fce7:	43 0f b6 44 3e 08    	movzx  eax,BYTE PTR [r14+r15*1+0x8]
    fced:	44 89 c9             	mov    ecx,r9d
    fcf0:	48 d3 ea             	shr    rdx,cl
    fcf3:	31 d0                	xor    eax,edx
    fcf5:	44 89 c1             	mov    ecx,r8d
    fcf8:	d3 e8                	shr    eax,cl
    fcfa:	d3 e0                	shl    eax,cl
    fcfc:	31 d0                	xor    eax,edx
    fcfe:	43 88 44 3e 08       	mov    BYTE PTR [r14+r15*1+0x8],al
    fd03:	4c 8b 8d 68 ff ff ff 	mov    r9,QWORD PTR [rbp-0x98]
    fd0a:	49 ff c9             	dec    r9
    fd0d:	4d 0f af cb          	imul   r9,r11
    fd11:	4c 89 c8             	mov    rax,r9
    fd14:	48 c1 e8 03          	shr    rax,0x3
    fd18:	44 89 c9             	mov    ecx,r9d
    fd1b:	83 e1 07             	and    ecx,0x7
    fd1e:	ba 40 00 00 00       	mov    edx,0x40
    fd23:	29 ca                	sub    edx,ecx
    fd25:	44 8b 45 94          	mov    r8d,DWORD PTR [rbp-0x6c]
    fd29:	44 39 c2             	cmp    edx,r8d
    fd2c:	44 89 c6             	mov    esi,r8d
    fd2f:	0f 42 f2             	cmovb  esi,edx
    fd32:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    fd39:	89 f1                	mov    ecx,esi
    fd3b:	48 d3 e7             	shl    rdi,cl
    fd3e:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
    fd45:	83 fe 40             	cmp    esi,0x40
    fd48:	48 f7 d7             	not    rdi
    fd4b:	48 0f 44 f9          	cmove  rdi,rcx
    fd4f:	41 80 e1 07          	and    r9b,0x7
    fd53:	44 89 c9             	mov    ecx,r9d
    fd56:	48 d3 e7             	shl    rdi,cl
    fd59:	48 f7 d7             	not    rdi
    fd5c:	49 21 3c 06          	and    QWORD PTR [r14+rax*1],rdi
    fd60:	44 39 c2             	cmp    edx,r8d
    fd63:	48 8b bd 60 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xa0]
    fd6a:	73 12                	jae    fd7e <zbtScoreDeleteInPlace+0x4de>
    fd6c:	41 29 f0             	sub    r8d,esi
    fd6f:	ba ff ff ff ff       	mov    edx,0xffffffff
    fd74:	44 89 c1             	mov    ecx,r8d
    fd77:	d3 e2                	shl    edx,cl
    fd79:	41 20 54 06 08       	and    BYTE PTR [r14+rax*1+0x8],dl
    fd7e:	48 8d 77 02          	lea    rsi,[rdi+0x2]
    fd82:	44 8b 6d bc          	mov    r13d,DWORD PTR [rbp-0x44]
    fd86:	44 89 e8             	mov    eax,r13d
    fd89:	2b 45 c0             	sub    eax,DWORD PTR [rbp-0x40]
    fd8c:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    fd90:	48 8d 14 00          	lea    rdx,[rax+rax*1]
    fd94:	e8 c7 13 ff ff       	call   1160 <memmove@plt>
    fd99:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    fd9f:	44 89 e9             	mov    ecx,r13d
    fda2:	45 89 ef             	mov    r15d,r13d
    fda5:	48 85 c0             	test   rax,rax
    fda8:	74 16                	je     fdc0 <zbtScoreDeleteInPlace+0x520>
    fdaa:	49 0f af c7          	imul   rax,r15
    fdae:	48 83 c0 07          	add    rax,0x7
    fdb2:	48 c1 e8 03          	shr    rax,0x3
    fdb6:	48 83 c0 09          	add    rax,0x9
    fdba:	48 83 e0 fe          	and    rax,0xfffffffffffffffe
    fdbe:	eb 02                	jmp    fdc2 <zbtScoreDeleteInPlace+0x522>
    fdc0:	31 c0                	xor    eax,eax
    fdc2:	85 c9                	test   ecx,ecx
    fdc4:	0f 94 45 d0          	sete   BYTE PTR [rbp-0x30]
    fdc8:	49 01 c6             	add    r14,rax
    fdcb:	4b 8d 14 3f          	lea    rdx,[r15+r15*1]
    fdcf:	4c 89 f7             	mov    rdi,r14
    fdd2:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    fdd6:	e8 85 13 ff ff       	call   1160 <memmove@plt>
    fddb:	4f 8d 24 7e          	lea    r12,[r14+r15*2]
    fddf:	48 8d b5 f0 fe ff ff 	lea    rsi,[rbp-0x110]
    fde6:	4c 89 e7             	mov    rdi,r12
    fde9:	4c 8b 6d a8          	mov    r13,QWORD PTR [rbp-0x58]
    fded:	4c 89 ea             	mov    rdx,r13
    fdf0:	e8 2b 13 ff ff       	call   1120 <memcpy@plt>
    fdf5:	4d 01 ec             	add    r12,r13
    fdf8:	4a 8d 34 2d f1 fe ff 	lea    rsi,[r13*1-0x10f]
    fdff:	ff
    fe00:	48 01 ee             	add    rsi,rbp
    fe03:	4c 89 e7             	mov    rdi,r12
    fe06:	48 8b 55 c8          	mov    rdx,QWORD PTR [rbp-0x38]
    fe0a:	e8 11 13 ff ff       	call   1120 <memcpy@plt>
    fe0f:	8b 4d bc             	mov    ecx,DWORD PTR [rbp-0x44]
    fe12:	48 8b 7d 80          	mov    rdi,QWORD PTR [rbp-0x80]
    fe16:	88 4f 11             	mov    BYTE PTR [rdi+0x11],cl
    fe19:	4c 89 7f 08          	mov    QWORD PTR [rdi+0x8],r15
    fe1d:	8b 45 c4             	mov    eax,DWORD PTR [rbp-0x3c]
    fe20:	34 01                	xor    al,0x1
    fe22:	0a 45 d0             	or     al,BYTE PTR [rbp-0x30]
    fe25:	44 8b 45 90          	mov    r8d,DWORD PTR [rbp-0x70]
    fe29:	0f 85 f2 02 00 00    	jne    10121 <zbtScoreDeleteInPlace+0x881>
    fe2f:	83 f9 10             	cmp    ecx,0x10
    fe32:	73 07                	jae    fe3b <zbtScoreDeleteInPlace+0x59b>
    fe34:	31 c0                	xor    eax,eax
    fe36:	e9 0d 03 00 00       	jmp    10148 <zbtScoreDeleteInPlace+0x8a8>
    fe3b:	44 89 f8             	mov    eax,r15d
    fe3e:	83 e0 f0             	and    eax,0xfffffff0
    fe41:	66 41 0f 6e c0       	movd   xmm0,r8d
    fe46:	f2 0f 70 c0 00       	pshuflw xmm0,xmm0,0x0
    fe4b:	66 0f 70 c0 00       	pshufd xmm0,xmm0,0x0
    fe50:	31 c9                	xor    ecx,ecx
    fe52:	66 0f 6f 0d f6 31 00 	movdqa xmm1,XMMWORD PTR [rip+0x31f6]        # 13050 <_IO_stdin_used+0x50>
    fe59:	00
    fe5a:	66 0f ef c1          	pxor   xmm0,xmm1
    fe5e:	eb 0d                	jmp    fe6d <zbtScoreDeleteInPlace+0x5cd>
    fe60:	48 83 c1 10          	add    rcx,0x10
    fe64:	48 39 c8             	cmp    rax,rcx
    fe67:	0f 84 af 02 00 00    	je     1011c <zbtScoreDeleteInPlace+0x87c>
    fe6d:	f3 41 0f 6f 14 4e    	movdqu xmm2,XMMWORD PTR [r14+rcx*2]
    fe73:	66 0f 6f e2          	movdqa xmm4,xmm2
    fe77:	66 0f ef e1          	pxor   xmm4,xmm1
    fe7b:	66 0f 6f d8          	movdqa xmm3,xmm0
    fe7f:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
    fe83:	66 0f 7e da          	movd   edx,xmm3
    fe87:	f6 c2 01             	test   dl,0x1
    fe8a:	0f 85 00 01 00 00    	jne    ff90 <zbtScoreDeleteInPlace+0x6f0>
    fe90:	c1 ea 10             	shr    edx,0x10
    fe93:	f6 c2 01             	test   dl,0x1
    fe96:	0f 85 0b 01 00 00    	jne    ffa7 <zbtScoreDeleteInPlace+0x707>
    fe9c:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    fea1:	f6 c2 01             	test   dl,0x1
    fea4:	0f 85 18 01 00 00    	jne    ffc2 <zbtScoreDeleteInPlace+0x722>
    feaa:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    feaf:	f6 c2 01             	test   dl,0x1
    feb2:	0f 85 25 01 00 00    	jne    ffdd <zbtScoreDeleteInPlace+0x73d>
    feb8:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    febd:	f6 c2 01             	test   dl,0x1
    fec0:	0f 85 32 01 00 00    	jne    fff8 <zbtScoreDeleteInPlace+0x758>
    fec6:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    fecb:	f6 c2 01             	test   dl,0x1
    fece:	0f 85 3f 01 00 00    	jne    10013 <zbtScoreDeleteInPlace+0x773>
    fed4:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    fed9:	f6 c2 01             	test   dl,0x1
    fedc:	0f 85 4c 01 00 00    	jne    1002e <zbtScoreDeleteInPlace+0x78e>
    fee2:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    fee7:	f6 c2 01             	test   dl,0x1
    feea:	74 0d                	je     fef9 <zbtScoreDeleteInPlace+0x659>
    feec:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
    fef1:	01 da                	add    edx,ebx
    fef3:	66 41 89 54 4e 0e    	mov    WORD PTR [r14+rcx*2+0xe],dx
    fef9:	f3 41 0f 6f 54 4e 10 	movdqu xmm2,XMMWORD PTR [r14+rcx*2+0x10]
    ff00:	66 0f 6f e2          	movdqa xmm4,xmm2
    ff04:	66 0f ef e1          	pxor   xmm4,xmm1
    ff08:	66 0f 6f d8          	movdqa xmm3,xmm0
    ff0c:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
    ff10:	66 0f 7e da          	movd   edx,xmm3
    ff14:	f6 c2 01             	test   dl,0x1
    ff17:	0f 85 33 01 00 00    	jne    10050 <zbtScoreDeleteInPlace+0x7b0>
    ff1d:	c1 ea 10             	shr    edx,0x10
    ff20:	f6 c2 01             	test   dl,0x1
    ff23:	0f 85 3f 01 00 00    	jne    10068 <zbtScoreDeleteInPlace+0x7c8>
    ff29:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    ff2e:	f6 c2 01             	test   dl,0x1
    ff31:	0f 85 4c 01 00 00    	jne    10083 <zbtScoreDeleteInPlace+0x7e3>
    ff37:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    ff3c:	f6 c2 01             	test   dl,0x1
    ff3f:	0f 85 59 01 00 00    	jne    1009e <zbtScoreDeleteInPlace+0x7fe>
    ff45:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    ff4a:	f6 c2 01             	test   dl,0x1
    ff4d:	0f 85 66 01 00 00    	jne    100b9 <zbtScoreDeleteInPlace+0x819>
    ff53:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
    ff58:	f6 c2 01             	test   dl,0x1
    ff5b:	0f 85 73 01 00 00    	jne    100d4 <zbtScoreDeleteInPlace+0x834>
    ff61:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
    ff66:	f6 c2 01             	test   dl,0x1
    ff69:	0f 85 80 01 00 00    	jne    100ef <zbtScoreDeleteInPlace+0x84f>
    ff6f:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
    ff74:	f6 c2 01             	test   dl,0x1
    ff77:	0f 84 e3 fe ff ff    	je     fe60 <zbtScoreDeleteInPlace+0x5c0>
    ff7d:	e9 88 01 00 00       	jmp    1010a <zbtScoreDeleteInPlace+0x86a>
    ff82:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    ff89:	1f 84 00 00 00 00 00
    ff90:	66 0f 7e d6          	movd   esi,xmm2
    ff94:	01 de                	add    esi,ebx
    ff96:	66 41 89 34 4e       	mov    WORD PTR [r14+rcx*2],si
    ff9b:	c1 ea 10             	shr    edx,0x10
    ff9e:	f6 c2 01             	test   dl,0x1
    ffa1:	0f 84 f5 fe ff ff    	je     fe9c <zbtScoreDeleteInPlace+0x5fc>
    ffa7:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
    ffac:	01 da                	add    edx,ebx
    ffae:	66 41 89 54 4e 02    	mov    WORD PTR [r14+rcx*2+0x2],dx
    ffb4:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
    ffb9:	f6 c2 01             	test   dl,0x1
    ffbc:	0f 84 e8 fe ff ff    	je     feaa <zbtScoreDeleteInPlace+0x60a>
    ffc2:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
    ffc7:	01 da                	add    edx,ebx
    ffc9:	66 41 89 54 4e 04    	mov    WORD PTR [r14+rcx*2+0x4],dx
    ffcf:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
    ffd4:	f6 c2 01             	test   dl,0x1
    ffd7:	0f 84 db fe ff ff    	je     feb8 <zbtScoreDeleteInPlace+0x618>
    ffdd:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
    ffe2:	01 da                	add    edx,ebx
    ffe4:	66 41 89 54 4e 06    	mov    WORD PTR [r14+rcx*2+0x6],dx
    ffea:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
    ffef:	f6 c2 01             	test   dl,0x1
    fff2:	0f 84 ce fe ff ff    	je     fec6 <zbtScoreDeleteInPlace+0x626>
    fff8:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
    fffd:	01 da                	add    edx,ebx
    ffff:	66 41 89 54 4e 08    	mov    WORD PTR [r14+rcx*2+0x8],dx
   10005:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   1000a:	f6 c2 01             	test   dl,0x1
   1000d:	0f 84 c1 fe ff ff    	je     fed4 <zbtScoreDeleteInPlace+0x634>
   10013:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
   10018:	01 da                	add    edx,ebx
   1001a:	66 41 89 54 4e 0a    	mov    WORD PTR [r14+rcx*2+0xa],dx
   10020:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   10025:	f6 c2 01             	test   dl,0x1
   10028:	0f 84 b4 fe ff ff    	je     fee2 <zbtScoreDeleteInPlace+0x642>
   1002e:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
   10033:	01 da                	add    edx,ebx
   10035:	66 41 89 54 4e 0c    	mov    WORD PTR [r14+rcx*2+0xc],dx
   1003b:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   10040:	f6 c2 01             	test   dl,0x1
   10043:	0f 85 a3 fe ff ff    	jne    feec <zbtScoreDeleteInPlace+0x64c>
   10049:	e9 ab fe ff ff       	jmp    fef9 <zbtScoreDeleteInPlace+0x659>
   1004e:	66 90                	xchg   ax,ax
   10050:	66 0f 7e d6          	movd   esi,xmm2
   10054:	01 de                	add    esi,ebx
   10056:	66 41 89 74 4e 10    	mov    WORD PTR [r14+rcx*2+0x10],si
   1005c:	c1 ea 10             	shr    edx,0x10
   1005f:	f6 c2 01             	test   dl,0x1
   10062:	0f 84 c1 fe ff ff    	je     ff29 <zbtScoreDeleteInPlace+0x689>
   10068:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
   1006d:	01 da                	add    edx,ebx
   1006f:	66 41 89 54 4e 12    	mov    WORD PTR [r14+rcx*2+0x12],dx
   10075:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
   1007a:	f6 c2 01             	test   dl,0x1
   1007d:	0f 84 b4 fe ff ff    	je     ff37 <zbtScoreDeleteInPlace+0x697>
   10083:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
   10088:	01 da                	add    edx,ebx
   1008a:	66 41 89 54 4e 14    	mov    WORD PTR [r14+rcx*2+0x14],dx
   10090:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
   10095:	f6 c2 01             	test   dl,0x1
   10098:	0f 84 a7 fe ff ff    	je     ff45 <zbtScoreDeleteInPlace+0x6a5>
   1009e:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
   100a3:	01 da                	add    edx,ebx
   100a5:	66 41 89 54 4e 16    	mov    WORD PTR [r14+rcx*2+0x16],dx
   100ab:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
   100b0:	f6 c2 01             	test   dl,0x1
   100b3:	0f 84 9a fe ff ff    	je     ff53 <zbtScoreDeleteInPlace+0x6b3>
   100b9:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
   100be:	01 da                	add    edx,ebx
   100c0:	66 41 89 54 4e 18    	mov    WORD PTR [r14+rcx*2+0x18],dx
   100c6:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   100cb:	f6 c2 01             	test   dl,0x1
   100ce:	0f 84 8d fe ff ff    	je     ff61 <zbtScoreDeleteInPlace+0x6c1>
   100d4:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
   100d9:	01 da                	add    edx,ebx
   100db:	66 41 89 54 4e 1a    	mov    WORD PTR [r14+rcx*2+0x1a],dx
   100e1:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   100e6:	f6 c2 01             	test   dl,0x1
   100e9:	0f 84 80 fe ff ff    	je     ff6f <zbtScoreDeleteInPlace+0x6cf>
   100ef:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
   100f4:	01 da                	add    edx,ebx
   100f6:	66 41 89 54 4e 1c    	mov    WORD PTR [r14+rcx*2+0x1c],dx
   100fc:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   10101:	f6 c2 01             	test   dl,0x1
   10104:	0f 84 56 fd ff ff    	je     fe60 <zbtScoreDeleteInPlace+0x5c0>
   1010a:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
   1010f:	01 da                	add    edx,ebx
   10111:	66 41 89 54 4e 1e    	mov    WORD PTR [r14+rcx*2+0x1e],dx
   10117:	e9 44 fd ff ff       	jmp    fe60 <zbtScoreDeleteInPlace+0x5c0>
   1011c:	4c 39 f8             	cmp    rax,r15
   1011f:	75 27                	jne    10148 <zbtScoreDeleteInPlace+0x8a8>
   10121:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
   10128:	e8 43 f0 ff ff       	call   f170 <zbtScoreUpdatePath>
   1012d:	48 81 c4 e8 00 00 00 	add    rsp,0xe8
   10134:	5b                   	pop    rbx
   10135:	41 5c                	pop    r12
   10137:	41 5d                	pop    r13
   10139:	41 5e                	pop    r14
   1013b:	41 5f                	pop    r15
   1013d:	5d                   	pop    rbp
   1013e:	c3                   	ret
   1013f:	90                   	nop
   10140:	48 ff c0             	inc    rax
   10143:	49 39 c7             	cmp    r15,rax
   10146:	74 d9                	je     10121 <zbtScoreDeleteInPlace+0x881>
   10148:	41 0f b7 0c 46       	movzx  ecx,WORD PTR [r14+rax*2]
   1014d:	66 44 39 c1          	cmp    cx,r8w
   10151:	73 ed                	jae    10140 <zbtScoreDeleteInPlace+0x8a0>
   10153:	01 d9                	add    ecx,ebx
   10155:	66 41 89 0c 46       	mov    WORD PTR [r14+rax*2],cx
   1015a:	eb e4                	jmp    10140 <zbtScoreDeleteInPlace+0x8a0>
   1015c:	4c 89 d0             	mov    rax,r10
   1015f:	4d 89 ea             	mov    r10,r13
   10162:	4d 89 e5             	mov    r13,r12
   10165:	49 89 d4             	mov    r12,rdx
   10168:	4c 89 fa             	mov    rdx,r15
   1016b:	45 85 ff             	test   r15d,r15d
   1016e:	0f 84 f5 00 00 00    	je     10269 <zbtScoreDeleteInPlace+0x9c9>
   10174:	45 31 ff             	xor    r15d,r15d
   10177:	4d 89 d8             	mov    r8,r11
   1017a:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
   1017e:	49 89 c1             	mov    r9,rax
   10181:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
   10188:	0f 1f 84 00 00 00 00
   1018f:	00
   10190:	4b 8d 04 3b          	lea    rax,[r11+r15*1]
   10194:	48 c1 e8 03          	shr    rax,0x3
   10198:	49 8b 34 06          	mov    rsi,QWORD PTR [r14+rax*1]
   1019c:	89 d1                	mov    ecx,edx
   1019e:	48 d3 ee             	shr    rsi,cl
   101a1:	41 0f b6 44 06 08    	movzx  eax,BYTE PTR [r14+rax*1+0x8]
   101a7:	44 89 d1             	mov    ecx,r10d
   101aa:	48 d3 e0             	shl    rax,cl
   101ad:	48 09 f0             	or     rax,rsi
   101b0:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
   101b4:	4a 8d 34 39          	lea    rsi,[rcx+r15*1]
   101b8:	48 c1 ee 03          	shr    rsi,0x3
   101bc:	49 8b 3c 36          	mov    rdi,QWORD PTR [r14+rsi*1]
   101c0:	4c 21 ef             	and    rdi,r13
   101c3:	4c 21 e0             	and    rax,r12
   101c6:	44 89 c9             	mov    ecx,r9d
   101c9:	48 d3 e0             	shl    rax,cl
   101cc:	48 09 f8             	or     rax,rdi
   101cf:	49 89 04 36          	mov    QWORD PTR [r14+rsi*1],rax
   101d3:	49 83 c7 40          	add    r15,0x40
   101d7:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
   101db:	49 83 f8 3f          	cmp    r8,0x3f
   101df:	77 af                	ja     10190 <zbtScoreDeleteInPlace+0x8f0>
   101e1:	e9 48 fa ff ff       	jmp    fc2e <zbtScoreDeleteInPlace+0x38e>
   101e6:	45 31 ff             	xor    r15d,r15d
   101e9:	4d 89 d8             	mov    r8,r11
   101ec:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
   101f0:	48 89 55 a0          	mov    QWORD PTR [rbp-0x60],rdx
   101f4:	48 8b 7d 88          	mov    rdi,QWORD PTR [rbp-0x78]
   101f8:	49 89 f5             	mov    r13,rsi
   101fb:	4c 89 ca             	mov    rdx,r9
   101fe:	66 90                	xchg   ax,ax
   10200:	4b 8d 0c 3b          	lea    rcx,[r11+r15*1]
   10204:	48 c1 e9 03          	shr    rcx,0x3
   10208:	4d 8b 0c 0e          	mov    r9,QWORD PTR [r14+rcx*1]
   1020c:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
   10210:	49 d3 e9             	shr    r9,cl
   10213:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
   10217:	4a 8d 34 39          	lea    rsi,[rcx+r15*1]
   1021b:	48 c1 ee 03          	shr    rsi,0x3
   1021f:	4d 89 cb             	mov    r11,r9
   10222:	4d 21 e3             	and    r11,r12
   10225:	89 c1                	mov    ecx,eax
   10227:	49 d3 e3             	shl    r11,cl
   1022a:	49 8b 0c 36          	mov    rcx,QWORD PTR [r14+rsi*1]
   1022e:	48 21 f9             	and    rcx,rdi
   10231:	49 09 cb             	or     r11,rcx
   10234:	4d 89 1c 36          	mov    QWORD PTR [r14+rsi*1],r11
   10238:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
   1023c:	44 89 e9             	mov    ecx,r13d
   1023f:	49 d3 e9             	shr    r9,cl
   10242:	41 0f b6 4c 36 08    	movzx  ecx,BYTE PTR [r14+rsi*1+0x8]
   10248:	44 21 d1             	and    ecx,r10d
   1024b:	41 21 d1             	and    r9d,edx
   1024e:	41 09 c9             	or     r9d,ecx
   10251:	45 88 4c 36 08       	mov    BYTE PTR [r14+rsi*1+0x8],r9b
   10256:	49 83 c7 40          	add    r15,0x40
   1025a:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
   1025e:	49 83 f8 3f          	cmp    r8,0x3f
   10262:	77 9c                	ja     10200 <zbtScoreDeleteInPlace+0x960>
   10264:	e9 c5 f9 ff ff       	jmp    fc2e <zbtScoreDeleteInPlace+0x38e>
   10269:	45 31 ff             	xor    r15d,r15d
   1026c:	4d 89 d8             	mov    r8,r11
   1026f:	4c 8b 4d c8          	mov    r9,QWORD PTR [rbp-0x38]
   10273:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
   10277:	49 89 c2             	mov    r10,rax
   1027a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
   10280:	4b 8d 04 3b          	lea    rax,[r11+r15*1]
   10284:	48 c1 e8 03          	shr    rax,0x3
   10288:	49 8b 04 06          	mov    rax,QWORD PTR [r14+rax*1]
   1028c:	89 d1                	mov    ecx,edx
   1028e:	48 d3 e8             	shr    rax,cl
   10291:	4b 8d 34 39          	lea    rsi,[r9+r15*1]
   10295:	48 c1 ee 03          	shr    rsi,0x3
   10299:	49 8b 3c 36          	mov    rdi,QWORD PTR [r14+rsi*1]
   1029d:	4c 21 ef             	and    rdi,r13
   102a0:	4c 21 e0             	and    rax,r12
   102a3:	44 89 d1             	mov    ecx,r10d
   102a6:	48 d3 e0             	shl    rax,cl
   102a9:	48 09 f8             	or     rax,rdi
   102ac:	49 89 04 36          	mov    QWORD PTR [r14+rsi*1],rax
   102b0:	49 83 c7 40          	add    r15,0x40
   102b4:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
   102b8:	49 83 f8 3f          	cmp    r8,0x3f
   102bc:	77 c2                	ja     10280 <zbtScoreDeleteInPlace+0x9e0>
   102be:	e9 6b f9 ff ff       	jmp    fc2e <zbtScoreDeleteInPlace+0x38e>

Disassembly of section .fini:
