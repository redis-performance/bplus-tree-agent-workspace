
scratch/amd-chunk-build/C/build/native/btree-bench:     file format elf64-x86-64


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
    f8b4:	89 4d d0             	mov    DWORD PTR [rbp-0x30],ecx
    f8b7:	41 89 d7             	mov    r15d,edx
    f8ba:	49 89 f4             	mov    r12,rsi
    f8bd:	48 89 7d c8          	mov    QWORD PTR [rbp-0x38],rdi
    f8c1:	44 0f b6 76 11       	movzx  r14d,BYTE PTR [rsi+0x11]
    f8c6:	41 8d 5e ff          	lea    ebx,[r14-0x1]
    f8ca:	41 39 d6             	cmp    r14d,edx
    f8cd:	76 04                	jbe    f8d3 <zbtScoreDeleteInPlace+0x33>
    f8cf:	85 db                	test   ebx,ebx
    f8d1:	75 18                	jne    f8eb <zbtScoreDeleteInPlace+0x4b>
    f8d3:	48 8d 3d 44 3d 00 00 	lea    rdi,[rip+0x3d44]        # 1361e <_IO_stdin_used+0x61e>
    f8da:	48 8d 15 1a 41 00 00 	lea    rdx,[rip+0x411a]        # 139fb <_IO_stdin_used+0x9fb>
    f8e1:	be 08 0a 00 00       	mov    esi,0xa08
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
    f950:	44 89 7d bc          	mov    DWORD PTR [rbp-0x44],r15d
    f954:	44 89 f8             	mov    eax,r15d
    f957:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    f95b:	41 0f b7 74 45 00    	movzx  esi,WORD PTR [r13+rax*2+0x0]
    f961:	44 0f b7 fe          	movzx  r15d,si
    f965:	43 0f b6 04 3c       	movzx  eax,BYTE PTR [r12+r15*1]
    f96a:	3d fe 00 00 00       	cmp    eax,0xfe
    f96f:	89 75 c4             	mov    DWORD PTR [rbp-0x3c],esi
    f972:	89 5d b8             	mov    DWORD PTR [rbp-0x48],ebx
    f975:	74 1e                	je     f995 <zbtScoreDeleteInPlace+0xf5>
    f977:	3d ff 00 00 00       	cmp    eax,0xff
    f97c:	8b 55 d0             	mov    edx,DWORD PTR [rbp-0x30]
    f97f:	75 1d                	jne    f99e <zbtScoreDeleteInPlace+0xfe>
    f981:	85 d2                	test   edx,edx
    f983:	74 43                	je     f9c8 <zbtScoreDeleteInPlace+0x128>
    f985:	4b 8b 7c 3c 0d       	mov    rdi,QWORD PTR [r12+r15*1+0xd]
    f98a:	48 85 ff             	test   rdi,rdi
    f98d:	74 40                	je     f9cf <zbtScoreDeleteInPlace+0x12f>
    f98f:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    f993:	eb 58                	jmp    f9ed <zbtScoreDeleteInPlace+0x14d>
    f995:	43 0f b7 44 3c 01    	movzx  eax,WORD PTR [r12+r15*1+0x1]
    f99b:	8b 55 d0             	mov    edx,DWORD PTR [rbp-0x30]
    f99e:	31 c9                	xor    ecx,ecx
    f9a0:	48 3d fe 00 00 00    	cmp    rax,0xfe
    f9a6:	0f 93 c1             	setae  cl
    f9a9:	48 8d 1c 48          	lea    rbx,[rax+rcx*2]
    f9ad:	48 ff c3             	inc    rbx
    f9b0:	85 d2                	test   edx,edx
    f9b2:	0f 84 80 00 00 00    	je     fa38 <zbtScoreDeleteInPlace+0x198>
    f9b8:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    f9be:	66 39 c6             	cmp    si,ax
    f9c1:	75 4e                	jne    fa11 <zbtScoreDeleteInPlace+0x171>
    f9c3:	e9 83 00 00 00       	jmp    fa4b <zbtScoreDeleteInPlace+0x1ab>
    f9c8:	bb 15 00 00 00       	mov    ebx,0x15
    f9cd:	eb 69                	jmp    fa38 <zbtScoreDeleteInPlace+0x198>
    f9cf:	48 8d 3d 48 3c 00 00 	lea    rdi,[rip+0x3c48]        # 1361e <_IO_stdin_used+0x61e>
    f9d6:	48 8d 15 3b 40 00 00 	lea    rdx,[rip+0x403b]        # 13a18 <_IO_stdin_used+0xa18>
    f9dd:	be 14 0a 00 00       	mov    esi,0xa14
    f9e2:	e8 29 21 00 00       	call   11b10 <standalone_panic>
    f9e7:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    f9eb:	31 ff                	xor    edi,edi
    f9ed:	e8 1e 23 00 00       	call   11d10 <zfree_usable>
    f9f2:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    f9f6:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    f9fa:	48 29 41 68          	sub    QWORD PTR [rcx+0x68],rax
    f9fe:	bb 15 00 00 00       	mov    ebx,0x15
    fa03:	8b 75 c4             	mov    esi,DWORD PTR [rbp-0x3c]
    fa06:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa0c:	66 39 c6             	cmp    si,ax
    fa0f:	74 3a                	je     fa4b <zbtScoreDeleteInPlace+0x1ab>
    fa11:	4d 85 f6             	test   r14,r14
    fa14:	74 22                	je     fa38 <zbtScoreDeleteInPlace+0x198>
    fa16:	b9 01 00 00 00       	mov    ecx,0x1
    fa1b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    fa20:	41 0f b7 54 4d fe    	movzx  edx,WORD PTR [r13+rcx*2-0x2]
    fa26:	4c 39 f1             	cmp    rcx,r14
    fa29:	73 08                	jae    fa33 <zbtScoreDeleteInPlace+0x193>
    fa2b:	48 ff c1             	inc    rcx
    fa2e:	66 39 f2             	cmp    dx,si
    fa31:	76 ed                	jbe    fa20 <zbtScoreDeleteInPlace+0x180>
    fa33:	66 39 f2             	cmp    dx,si
    fa36:	77 13                	ja     fa4b <zbtScoreDeleteInPlace+0x1ab>
    fa38:	31 c9                	xor    ecx,ecx
    fa3a:	66 41 3b 74 24 36    	cmp    si,WORD PTR [r12+0x36]
    fa40:	75 34                	jne    fa76 <zbtScoreDeleteInPlace+0x1d6>
    fa42:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa47:	89 f0                	mov    eax,esi
    fa49:	eb 20                	jmp    fa6b <zbtScoreDeleteInPlace+0x1cb>
    fa4b:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa50:	49 8d 34 04          	lea    rsi,[r12+rax*1]
    fa54:	48 8d 3c 1e          	lea    rdi,[rsi+rbx*1]
    fa58:	49 29 c7             	sub    r15,rax
    fa5b:	4c 89 fa             	mov    rdx,r15
    fa5e:	e8 fd 16 ff ff       	call   1160 <memmove@plt>
    fa63:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa69:	b1 01                	mov    cl,0x1
    fa6b:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    fa6e:	01 d8                	add    eax,ebx
    fa70:	66 41 89 06          	mov    WORD PTR [r14],ax
    fa74:	eb 07                	jmp    fa7d <zbtScoreDeleteInPlace+0x1dd>
    fa76:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    fa7d:	4d 8d 74 24 38       	lea    r14,[r12+0x38]
    fa82:	4c 89 ad 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],r13
    fa89:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
    fa8d:	48 8d 3c 45 00 00 00 	lea    rdi,[rax*2+0x0]
    fa94:	00
    fa95:	4c 01 ef             	add    rdi,r13
    fa98:	41 0f b6 74 24 34    	movzx  esi,BYTE PTR [r12+0x34]
    fa9e:	85 f6                	test   esi,esi
    faa0:	4c 89 65 80          	mov    QWORD PTR [rbp-0x80],r12
    faa4:	0f 84 cd 02 00 00    	je     fd77 <zbtScoreDeleteInPlace+0x4d7>
    faaa:	89 f1                	mov    ecx,esi
    faac:	49 89 cb             	mov    r11,rcx
    faaf:	4c 0f af 5d b0       	imul   r11,QWORD PTR [rbp-0x50]
    fab4:	45 0f b6 44 24 11    	movzx  r8d,BYTE PTR [r12+0x11]
    faba:	8b 45 bc             	mov    eax,DWORD PTR [rbp-0x44]
    fabd:	41 89 c1             	mov    r9d,eax
    fac0:	41 f7 d1             	not    r9d
    fac3:	45 01 c1             	add    r9d,r8d
    fac6:	4c 0f af c9          	imul   r9,rcx
    faca:	49 83 f9 40          	cmp    r9,0x40
    face:	48 89 bd 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],rdi
    fad5:	89 75 9c             	mov    DWORD PTR [rbp-0x64],esi
    fad8:	4c 89 85 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],r8
    fadf:	48 89 8d 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],rcx
    fae6:	4c 89 8d 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],r9
    faed:	0f 82 32 01 00 00    	jb     fc25 <zbtScoreDeleteInPlace+0x385>
    faf3:	49 8d 04 0b          	lea    rax,[r11+rcx*1]
    faf7:	48 89 45 d0          	mov    QWORD PTR [rbp-0x30],rax
    fafb:	41 89 c7             	mov    r15d,eax
    fafe:	41 83 e7 07          	and    r15d,0x7
    fb02:	41 ba 40 00 00 00    	mov    r10d,0x40
    fb08:	45 29 fa             	sub    r10d,r15d
    fb0b:	45 89 dd             	mov    r13d,r11d
    fb0e:	41 83 e5 07          	and    r13d,0x7
    fb12:	44 89 e9             	mov    ecx,r13d
    fb15:	f7 d9                	neg    ecx
    fb17:	48 c7 c0 ff ff ff ff 	mov    rax,0xffffffffffffffff
    fb1e:	48 d3 e0             	shl    rax,cl
    fb21:	31 d2                	xor    edx,edx
    fb23:	41 83 fd 01          	cmp    r13d,0x1
    fb27:	48 19 d2             	sbb    rdx,rdx
    fb2a:	48 f7 d0             	not    rax
    fb2d:	48 09 c2             	or     rdx,rax
    fb30:	49 89 d4             	mov    r12,rdx
    fb33:	44 89 e9             	mov    ecx,r13d
    fb36:	49 d3 e4             	shl    r12,cl
    fb39:	b8 7e 00 00 00       	mov    eax,0x7e
    fb3e:	d3 e8                	shr    eax,cl
    fb40:	d3 e0                	shl    eax,cl
    fb42:	49 f7 d4             	not    r12
    fb45:	45 85 ed             	test   r13d,r13d
    fb48:	0f 84 0e 06 00 00    	je     1015c <zbtScoreDeleteInPlace+0x8bc>
    fb4e:	48 89 c1             	mov    rcx,rax
    fb51:	4c 89 65 88          	mov    QWORD PTR [rbp-0x78],r12
    fb55:	49 89 d4             	mov    r12,rdx
    fb58:	ba 40 00 00 00       	mov    edx,0x40
    fb5d:	4c 89 e8             	mov    rax,r13
    fb60:	44 29 ea             	sub    edx,r13d
    fb63:	48 89 55 90          	mov    QWORD PTR [rbp-0x70],rdx
    fb67:	89 ca                	mov    edx,ecx
    fb69:	83 f2 7f             	xor    edx,0x7f
    fb6c:	48 89 95 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdx
    fb73:	48 83 f1 80          	xor    rcx,0xffffffffffffff80
    fb77:	48 89 ce             	mov    rsi,rcx
    fb7a:	4c 89 fa             	mov    rdx,r15
    fb7d:	45 85 ff             	test   r15d,r15d
    fb80:	4d 89 dd             	mov    r13,r11
    fb83:	4c 89 7d c8          	mov    QWORD PTR [rbp-0x38],r15
    fb87:	0f 84 48 06 00 00    	je     101d5 <zbtScoreDeleteInPlace+0x935>
    fb8d:	45 31 ff             	xor    r15d,r15d
    fb90:	4d 89 c8             	mov    r8,r9
    fb93:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    fb97:	48 8b 7d 88          	mov    rdi,QWORD PTR [rbp-0x78]
    fb9b:	48 89 75 a8          	mov    QWORD PTR [rbp-0x58],rsi
    fb9f:	48 8b 55 90          	mov    rdx,QWORD PTR [rbp-0x70]
    fba3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    fbaa:	84 00 00 00 00 00
    fbb0:	4b 8d 34 39          	lea    rsi,[r9+r15*1]
    fbb4:	4f 8d 1c 2f          	lea    r11,[r15+r13*1]
    fbb8:	48 c1 ee 03          	shr    rsi,0x3
    fbbc:	4d 8b 0c 36          	mov    r9,QWORD PTR [r14+rsi*1]
    fbc0:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    fbc4:	49 d3 e9             	shr    r9,cl
    fbc7:	41 0f b6 74 36 08    	movzx  esi,BYTE PTR [r14+rsi*1+0x8]
    fbcd:	44 89 d1             	mov    ecx,r10d
    fbd0:	48 d3 e6             	shl    rsi,cl
    fbd3:	4c 09 ce             	or     rsi,r9
    fbd6:	49 c1 eb 03          	shr    r11,0x3
    fbda:	49 89 f1             	mov    r9,rsi
    fbdd:	4d 21 e1             	and    r9,r12
    fbe0:	89 c1                	mov    ecx,eax
    fbe2:	49 d3 e1             	shl    r9,cl
    fbe5:	4b 8b 0c 1e          	mov    rcx,QWORD PTR [r14+r11*1]
    fbe9:	48 21 f9             	and    rcx,rdi
    fbec:	49 09 c9             	or     r9,rcx
    fbef:	4f 89 0c 1e          	mov    QWORD PTR [r14+r11*1],r9
    fbf3:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
    fbf7:	89 d1                	mov    ecx,edx
    fbf9:	48 d3 ee             	shr    rsi,cl
    fbfc:	43 0f b6 4c 1e 08    	movzx  ecx,BYTE PTR [r14+r11*1+0x8]
    fc02:	23 4d a8             	and    ecx,DWORD PTR [rbp-0x58]
    fc05:	23 b5 78 ff ff ff    	and    esi,DWORD PTR [rbp-0x88]
    fc0b:	09 ce                	or     esi,ecx
    fc0d:	43 88 74 1e 08       	mov    BYTE PTR [r14+r11*1+0x8],sil
    fc12:	4d 89 eb             	mov    r11,r13
    fc15:	49 83 c7 40          	add    r15,0x40
    fc19:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
    fc1d:	49 83 f8 3f          	cmp    r8,0x3f
    fc21:	77 8d                	ja     fbb0 <zbtScoreDeleteInPlace+0x310>
    fc23:	eb 06                	jmp    fc2b <zbtScoreDeleteInPlace+0x38b>
    fc25:	45 31 ff             	xor    r15d,r15d
    fc28:	4d 89 c8             	mov    r8,r9
    fc2b:	4c 3b bd 70 ff ff ff 	cmp    r15,QWORD PTR [rbp-0x90]
    fc32:	4c 8b 65 80          	mov    r12,QWORD PTR [rbp-0x80]
    fc36:	4c 8b 95 68 ff ff ff 	mov    r10,QWORD PTR [rbp-0x98]
    fc3d:	0f 83 b9 00 00 00    	jae    fcfc <zbtScoreDeleteInPlace+0x45c>
    fc43:	4b 8d 0c 13          	lea    rcx,[r11+r10*1]
    fc47:	49 8d 14 0f          	lea    rdx,[r15+rcx*1]
    fc4b:	48 c1 ea 03          	shr    rdx,0x3
    fc4f:	89 ce                	mov    esi,ecx
    fc51:	83 e6 07             	and    esi,0x7
    fc54:	b8 40 00 00 00       	mov    eax,0x40
    fc59:	41 b9 40 00 00 00    	mov    r9d,0x40
    fc5f:	41 29 f1             	sub    r9d,esi
    fc62:	49 8b 34 16          	mov    rsi,QWORD PTR [r14+rdx*1]
    fc66:	80 e1 07             	and    cl,0x7
    fc69:	48 d3 ee             	shr    rsi,cl
    fc6c:	45 39 c1             	cmp    r9d,r8d
    fc6f:	73 0f                	jae    fc80 <zbtScoreDeleteInPlace+0x3e0>
    fc71:	41 0f b6 54 16 08    	movzx  edx,BYTE PTR [r14+rdx*1+0x8]
    fc77:	44 89 c9             	mov    ecx,r9d
    fc7a:	48 d3 e2             	shl    rdx,cl
    fc7d:	48 09 d6             	or     rsi,rdx
    fc80:	48 c7 c2 ff ff ff ff 	mov    rdx,0xffffffffffffffff
    fc87:	44 89 c1             	mov    ecx,r8d
    fc8a:	48 d3 e2             	shl    rdx,cl
    fc8d:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    fc94:	48 f7 d2             	not    rdx
    fc97:	48 21 f2             	and    rdx,rsi
    fc9a:	4d 01 df             	add    r15,r11
    fc9d:	49 c1 ef 03          	shr    r15,0x3
    fca1:	41 83 e3 07          	and    r11d,0x7
    fca5:	44 29 d8             	sub    eax,r11d
    fca8:	44 39 c0             	cmp    eax,r8d
    fcab:	45 89 c1             	mov    r9d,r8d
    fcae:	44 0f 42 c8          	cmovb  r9d,eax
    fcb2:	44 89 c9             	mov    ecx,r9d
    fcb5:	48 d3 e7             	shl    rdi,cl
    fcb8:	48 f7 d7             	not    rdi
    fcbb:	48 89 d6             	mov    rsi,rdx
    fcbe:	48 21 fe             	and    rsi,rdi
    fcc1:	44 89 d9             	mov    ecx,r11d
    fcc4:	48 d3 e7             	shl    rdi,cl
    fcc7:	48 f7 d7             	not    rdi
    fcca:	4b 23 3c 3e          	and    rdi,QWORD PTR [r14+r15*1]
    fcce:	48 d3 e6             	shl    rsi,cl
    fcd1:	48 09 fe             	or     rsi,rdi
    fcd4:	4b 89 34 3e          	mov    QWORD PTR [r14+r15*1],rsi
    fcd8:	44 39 c0             	cmp    eax,r8d
    fcdb:	73 1f                	jae    fcfc <zbtScoreDeleteInPlace+0x45c>
    fcdd:	45 29 c8             	sub    r8d,r9d
    fce0:	43 0f b6 44 3e 08    	movzx  eax,BYTE PTR [r14+r15*1+0x8]
    fce6:	44 89 c9             	mov    ecx,r9d
    fce9:	48 d3 ea             	shr    rdx,cl
    fcec:	31 d0                	xor    eax,edx
    fcee:	44 89 c1             	mov    ecx,r8d
    fcf1:	d3 e8                	shr    eax,cl
    fcf3:	d3 e0                	shl    eax,cl
    fcf5:	31 d0                	xor    eax,edx
    fcf7:	43 88 44 3e 08       	mov    BYTE PTR [r14+r15*1+0x8],al
    fcfc:	4c 8b 8d 60 ff ff ff 	mov    r9,QWORD PTR [rbp-0xa0]
    fd03:	49 ff c9             	dec    r9
    fd06:	4d 0f af ca          	imul   r9,r10
    fd0a:	4c 89 c8             	mov    rax,r9
    fd0d:	48 c1 e8 03          	shr    rax,0x3
    fd11:	44 89 c9             	mov    ecx,r9d
    fd14:	83 e1 07             	and    ecx,0x7
    fd17:	ba 40 00 00 00       	mov    edx,0x40
    fd1c:	29 ca                	sub    edx,ecx
    fd1e:	44 8b 45 9c          	mov    r8d,DWORD PTR [rbp-0x64]
    fd22:	44 39 c2             	cmp    edx,r8d
    fd25:	44 89 c6             	mov    esi,r8d
    fd28:	0f 42 f2             	cmovb  esi,edx
    fd2b:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    fd32:	89 f1                	mov    ecx,esi
    fd34:	48 d3 e7             	shl    rdi,cl
    fd37:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
    fd3e:	83 fe 40             	cmp    esi,0x40
    fd41:	48 f7 d7             	not    rdi
    fd44:	48 0f 44 f9          	cmove  rdi,rcx
    fd48:	41 80 e1 07          	and    r9b,0x7
    fd4c:	44 89 c9             	mov    ecx,r9d
    fd4f:	48 d3 e7             	shl    rdi,cl
    fd52:	48 f7 d7             	not    rdi
    fd55:	49 21 3c 06          	and    QWORD PTR [r14+rax*1],rdi
    fd59:	44 39 c2             	cmp    edx,r8d
    fd5c:	48 8b bd 58 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xa8]
    fd63:	73 12                	jae    fd77 <zbtScoreDeleteInPlace+0x4d7>
    fd65:	41 29 f0             	sub    r8d,esi
    fd68:	ba ff ff ff ff       	mov    edx,0xffffffff
    fd6d:	44 89 c1             	mov    ecx,r8d
    fd70:	d3 e2                	shl    edx,cl
    fd72:	41 20 54 06 08       	and    BYTE PTR [r14+rax*1+0x8],dl
    fd77:	48 8d 77 02          	lea    rsi,[rdi+0x2]
    fd7b:	44 8b 6d b8          	mov    r13d,DWORD PTR [rbp-0x48]
    fd7f:	44 89 e8             	mov    eax,r13d
    fd82:	2b 45 bc             	sub    eax,DWORD PTR [rbp-0x44]
    fd85:	48 89 45 d0          	mov    QWORD PTR [rbp-0x30],rax
    fd89:	48 8d 14 00          	lea    rdx,[rax+rax*1]
    fd8d:	e8 ce 13 ff ff       	call   1160 <memmove@plt>
    fd92:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    fd98:	44 89 e9             	mov    ecx,r13d
    fd9b:	45 89 ef             	mov    r15d,r13d
    fd9e:	48 85 c0             	test   rax,rax
    fda1:	74 16                	je     fdb9 <zbtScoreDeleteInPlace+0x519>
    fda3:	49 0f af c7          	imul   rax,r15
    fda7:	48 83 c0 07          	add    rax,0x7
    fdab:	48 c1 e8 03          	shr    rax,0x3
    fdaf:	48 83 c0 09          	add    rax,0x9
    fdb3:	48 83 e0 fe          	and    rax,0xfffffffffffffffe
    fdb7:	eb 02                	jmp    fdbb <zbtScoreDeleteInPlace+0x51b>
    fdb9:	31 c0                	xor    eax,eax
    fdbb:	85 c9                	test   ecx,ecx
    fdbd:	0f 94 45 c8          	sete   BYTE PTR [rbp-0x38]
    fdc1:	49 01 c6             	add    r14,rax
    fdc4:	4b 8d 14 3f          	lea    rdx,[r15+r15*1]
    fdc8:	4c 89 f7             	mov    rdi,r14
    fdcb:	48 8b b5 50 ff ff ff 	mov    rsi,QWORD PTR [rbp-0xb0]
    fdd2:	e8 89 13 ff ff       	call   1160 <memmove@plt>
    fdd7:	4f 8d 24 7e          	lea    r12,[r14+r15*2]
    fddb:	48 8d b5 f0 fe ff ff 	lea    rsi,[rbp-0x110]
    fde2:	4c 89 e7             	mov    rdi,r12
    fde5:	4c 8b 6d b0          	mov    r13,QWORD PTR [rbp-0x50]
    fde9:	4c 89 ea             	mov    rdx,r13
    fdec:	e8 2f 13 ff ff       	call   1120 <memcpy@plt>
    fdf1:	4d 01 ec             	add    r12,r13
    fdf4:	4a 8d 34 2d f1 fe ff 	lea    rsi,[r13*1-0x10f]
    fdfb:	ff
    fdfc:	48 01 ee             	add    rsi,rbp
    fdff:	4c 89 e7             	mov    rdi,r12
    fe02:	48 8b 55 d0          	mov    rdx,QWORD PTR [rbp-0x30]
    fe06:	e8 15 13 ff ff       	call   1120 <memcpy@plt>
    fe0b:	8b 4d b8             	mov    ecx,DWORD PTR [rbp-0x48]
    fe0e:	48 8b 7d 80          	mov    rdi,QWORD PTR [rbp-0x80]
    fe12:	88 4f 11             	mov    BYTE PTR [rdi+0x11],cl
    fe15:	4c 89 7f 08          	mov    QWORD PTR [rdi+0x8],r15
    fe19:	8b 45 c0             	mov    eax,DWORD PTR [rbp-0x40]
    fe1c:	34 01                	xor    al,0x1
    fe1e:	0a 45 c8             	or     al,BYTE PTR [rbp-0x38]
    fe21:	44 8b 45 c4          	mov    r8d,DWORD PTR [rbp-0x3c]
    fe25:	0f 85 f6 02 00 00    	jne    10121 <zbtScoreDeleteInPlace+0x881>
    fe2b:	83 f9 10             	cmp    ecx,0x10
    fe2e:	73 07                	jae    fe37 <zbtScoreDeleteInPlace+0x597>
    fe30:	31 c0                	xor    eax,eax
    fe32:	e9 11 03 00 00       	jmp    10148 <zbtScoreDeleteInPlace+0x8a8>
    fe37:	44 89 f8             	mov    eax,r15d
    fe3a:	83 e0 f0             	and    eax,0xfffffff0
    fe3d:	66 41 0f 6e c0       	movd   xmm0,r8d
    fe42:	f2 0f 70 c0 00       	pshuflw xmm0,xmm0,0x0
    fe47:	66 0f 70 c0 00       	pshufd xmm0,xmm0,0x0
    fe4c:	31 c9                	xor    ecx,ecx
    fe4e:	66 0f 6f 0d fa 31 00 	movdqa xmm1,XMMWORD PTR [rip+0x31fa]        # 13050 <_IO_stdin_used+0x50>
    fe55:	00
    fe56:	66 0f ef c1          	pxor   xmm0,xmm1
    fe5a:	eb 11                	jmp    fe6d <zbtScoreDeleteInPlace+0x5cd>
    fe5c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
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
   1015c:	4c 89 e8             	mov    rax,r13
   1015f:	4d 89 e5             	mov    r13,r12
   10162:	49 89 d4             	mov    r12,rdx
   10165:	4c 89 fa             	mov    rdx,r15
   10168:	45 85 ff             	test   r15d,r15d
   1016b:	0f 84 f6 00 00 00    	je     10267 <zbtScoreDeleteInPlace+0x9c7>
   10171:	45 31 ff             	xor    r15d,r15d
   10174:	4d 89 c8             	mov    r8,r9
   10177:	49 89 c1             	mov    r9,rax
   1017a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
   10180:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
   10184:	4c 01 f8             	add    rax,r15
   10187:	48 c1 e8 03          	shr    rax,0x3
   1018b:	49 8b 34 06          	mov    rsi,QWORD PTR [r14+rax*1]
   1018f:	89 d1                	mov    ecx,edx
   10191:	48 d3 ee             	shr    rsi,cl
   10194:	41 0f b6 44 06 08    	movzx  eax,BYTE PTR [r14+rax*1+0x8]
   1019a:	44 89 d1             	mov    ecx,r10d
   1019d:	48 d3 e0             	shl    rax,cl
   101a0:	4b 8d 3c 3b          	lea    rdi,[r11+r15*1]
   101a4:	48 09 f0             	or     rax,rsi
   101a7:	48 c1 ef 03          	shr    rdi,0x3
   101ab:	49 8b 34 3e          	mov    rsi,QWORD PTR [r14+rdi*1]
   101af:	4c 21 ee             	and    rsi,r13
   101b2:	4c 21 e0             	and    rax,r12
   101b5:	44 89 c9             	mov    ecx,r9d
   101b8:	48 d3 e0             	shl    rax,cl
   101bb:	48 09 f0             	or     rax,rsi
   101be:	49 89 04 3e          	mov    QWORD PTR [r14+rdi*1],rax
   101c2:	49 83 c7 40          	add    r15,0x40
   101c6:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
   101ca:	49 83 f8 3f          	cmp    r8,0x3f
   101ce:	77 b0                	ja     10180 <zbtScoreDeleteInPlace+0x8e0>
   101d0:	e9 56 fa ff ff       	jmp    fc2b <zbtScoreDeleteInPlace+0x38b>
   101d5:	45 31 ff             	xor    r15d,r15d
   101d8:	4d 89 c8             	mov    r8,r9
   101db:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
   101df:	4c 89 65 a8          	mov    QWORD PTR [rbp-0x58],r12
   101e3:	4c 8b 65 88          	mov    r12,QWORD PTR [rbp-0x78]
   101e7:	49 89 f2             	mov    r10,rsi
   101ea:	48 8b 55 90          	mov    rdx,QWORD PTR [rbp-0x70]
   101ee:	48 8b bd 78 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x88]
   101f5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
   101fc:	00 00 00 00
   10200:	4c 01 f9             	add    rcx,r15
   10203:	48 c1 e9 03          	shr    rcx,0x3
   10207:	4d 8b 0c 0e          	mov    r9,QWORD PTR [r14+rcx*1]
   1020b:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
   1020f:	49 d3 e9             	shr    r9,cl
   10212:	4f 8d 1c 2f          	lea    r11,[r15+r13*1]
   10216:	49 c1 eb 03          	shr    r11,0x3
   1021a:	4c 89 ce             	mov    rsi,r9
   1021d:	48 23 75 a8          	and    rsi,QWORD PTR [rbp-0x58]
   10221:	89 c1                	mov    ecx,eax
   10223:	48 d3 e6             	shl    rsi,cl
   10226:	4b 8b 0c 1e          	mov    rcx,QWORD PTR [r14+r11*1]
   1022a:	4c 21 e1             	and    rcx,r12
   1022d:	48 09 ce             	or     rsi,rcx
   10230:	4b 89 34 1e          	mov    QWORD PTR [r14+r11*1],rsi
   10234:	89 d1                	mov    ecx,edx
   10236:	49 d3 e9             	shr    r9,cl
   10239:	43 0f b6 4c 1e 08    	movzx  ecx,BYTE PTR [r14+r11*1+0x8]
   1023f:	44 21 d1             	and    ecx,r10d
   10242:	41 21 f9             	and    r9d,edi
   10245:	41 09 c9             	or     r9d,ecx
   10248:	47 88 4c 1e 08       	mov    BYTE PTR [r14+r11*1+0x8],r9b
   1024d:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
   10251:	4d 89 eb             	mov    r11,r13
   10254:	49 83 c7 40          	add    r15,0x40
   10258:	49 83 c0 c0          	add    r8,0xffffffffffffffc0
   1025c:	49 83 f8 3f          	cmp    r8,0x3f
   10260:	77 9e                	ja     10200 <zbtScoreDeleteInPlace+0x960>
   10262:	e9 c4 f9 ff ff       	jmp    fc2b <zbtScoreDeleteInPlace+0x38b>
   10267:	45 31 ff             	xor    r15d,r15d
   1026a:	4d 89 c8             	mov    r8,r9
   1026d:	4c 8b 4d d0          	mov    r9,QWORD PTR [rbp-0x30]
   10271:	49 89 c2             	mov    r10,rax
   10274:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
   1027b:	00 00 00 00 00
   10280:	4b 8d 04 39          	lea    rax,[r9+r15*1]
   10284:	4b 8d 34 3b          	lea    rsi,[r11+r15*1]
   10288:	48 c1 e8 03          	shr    rax,0x3
   1028c:	49 8b 04 06          	mov    rax,QWORD PTR [r14+rax*1]
   10290:	89 d1                	mov    ecx,edx
   10292:	48 d3 e8             	shr    rax,cl
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
   102be:	e9 68 f9 ff ff       	jmp    fc2b <zbtScoreDeleteInPlace+0x38b>

Disassembly of section .fini:
