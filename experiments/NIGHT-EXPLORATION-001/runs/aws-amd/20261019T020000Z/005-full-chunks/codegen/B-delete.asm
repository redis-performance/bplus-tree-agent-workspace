
scratch/amd-chunk-build/B/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000f8b0 <zbtScoreDeleteInPlace>:
    f8b0:	55                   	push   rbp
    f8b1:	48 89 e5             	mov    rbp,rsp
    f8b4:	41 57                	push   r15
    f8b6:	41 56                	push   r14
    f8b8:	41 55                	push   r13
    f8ba:	41 54                	push   r12
    f8bc:	53                   	push   rbx
    f8bd:	48 81 ec 08 01 00 00 	sub    rsp,0x108
    f8c4:	89 4d c8             	mov    DWORD PTR [rbp-0x38],ecx
    f8c7:	41 89 d5             	mov    r13d,edx
    f8ca:	49 89 f4             	mov    r12,rsi
    f8cd:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    f8d1:	44 0f b6 76 11       	movzx  r14d,BYTE PTR [rsi+0x11]
    f8d6:	41 8d 5e ff          	lea    ebx,[r14-0x1]
    f8da:	41 39 d6             	cmp    r14d,edx
    f8dd:	76 04                	jbe    f8e3 <zbtScoreDeleteInPlace+0x33>
    f8df:	85 db                	test   ebx,ebx
    f8e1:	75 18                	jne    f8fb <zbtScoreDeleteInPlace+0x4b>
    f8e3:	48 8d 3d 34 3d 00 00 	lea    rdi,[rip+0x3d34]        # 1361e <_IO_stdin_used+0x61e>
    f8ea:	48 8d 15 0a 41 00 00 	lea    rdx,[rip+0x410a]        # 139fb <_IO_stdin_used+0x9fb>
    f8f1:	be 04 0a 00 00       	mov    esi,0xa04
    f8f6:	e8 15 25 00 00       	call   11e10 <standalone_panic>
    f8fb:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    f901:	74 0c                	je     f90f <zbtScoreDeleteInPlace+0x5f>
    f903:	41 0f b6 44 24 11    	movzx  eax,BYTE PTR [r12+0x11]
    f909:	41 f7 d5             	not    r13d
    f90c:	41 01 c5             	add    r13d,eax
    f90f:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    f915:	48 85 c0             	test   rax,rax
    f918:	74 1f                	je     f939 <zbtScoreDeleteInPlace+0x89>
    f91a:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    f920:	0f af c1             	imul   eax,ecx
    f923:	83 c0 07             	add    eax,0x7
    f926:	c1 e8 03             	shr    eax,0x3
    f929:	83 c0 09             	add    eax,0x9
    f92c:	83 e0 fe             	and    eax,0xfffffffe
    f92f:	4d 8d 3c 04          	lea    r15,[r12+rax*1]
    f933:	49 83 c7 38          	add    r15,0x38
    f937:	eb 0d                	jmp    f946 <zbtScoreDeleteInPlace+0x96>
    f939:	4d 8d 7c 24 38       	lea    r15,[r12+0x38]
    f93e:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    f944:	31 c0                	xor    eax,eax
    f946:	4c 01 e0             	add    rax,r12
    f949:	48 83 c0 38          	add    rax,0x38
    f94d:	48 8d 34 48          	lea    rsi,[rax+rcx*2]
    f951:	48 8d bd d0 fe ff ff 	lea    rdi,[rbp-0x130]
    f958:	4c 89 f2             	mov    rdx,r14
    f95b:	e8 c0 17 ff ff       	call   1120 <memcpy@plt>
    f960:	44 89 6d 90          	mov    DWORD PTR [rbp-0x70],r13d
    f964:	44 89 e8             	mov    eax,r13d
    f967:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    f96e:	41 0f b7 34 47       	movzx  esi,WORD PTR [r15+rax*2]
    f973:	44 0f b7 ee          	movzx  r13d,si
    f977:	43 0f b6 04 2c       	movzx  eax,BYTE PTR [r12+r13*1]
    f97c:	3d fe 00 00 00       	cmp    eax,0xfe
    f981:	89 75 b4             	mov    DWORD PTR [rbp-0x4c],esi
    f984:	89 5d 8c             	mov    DWORD PTR [rbp-0x74],ebx
    f987:	74 21                	je     f9aa <zbtScoreDeleteInPlace+0xfa>
    f989:	3d ff 00 00 00       	cmp    eax,0xff
    f98e:	8b 55 c8             	mov    edx,DWORD PTR [rbp-0x38]
    f991:	75 20                	jne    f9b3 <zbtScoreDeleteInPlace+0x103>
    f993:	85 d2                	test   edx,edx
    f995:	74 46                	je     f9dd <zbtScoreDeleteInPlace+0x12d>
    f997:	4b 8b 7c 2c 0d       	mov    rdi,QWORD PTR [r12+r13*1+0xd]
    f99c:	48 85 ff             	test   rdi,rdi
    f99f:	74 43                	je     f9e4 <zbtScoreDeleteInPlace+0x134>
    f9a1:	48 8d b5 68 ff ff ff 	lea    rsi,[rbp-0x98]
    f9a8:	eb 5b                	jmp    fa05 <zbtScoreDeleteInPlace+0x155>
    f9aa:	43 0f b7 44 2c 01    	movzx  eax,WORD PTR [r12+r13*1+0x1]
    f9b0:	8b 55 c8             	mov    edx,DWORD PTR [rbp-0x38]
    f9b3:	31 c9                	xor    ecx,ecx
    f9b5:	48 3d fe 00 00 00    	cmp    rax,0xfe
    f9bb:	0f 93 c1             	setae  cl
    f9be:	48 8d 1c 48          	lea    rbx,[rax+rcx*2]
    f9c2:	48 ff c3             	inc    rbx
    f9c5:	85 d2                	test   edx,edx
    f9c7:	0f 84 8b 00 00 00    	je     fa58 <zbtScoreDeleteInPlace+0x1a8>
    f9cd:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    f9d3:	66 39 c6             	cmp    si,ax
    f9d6:	75 54                	jne    fa2c <zbtScoreDeleteInPlace+0x17c>
    f9d8:	e9 8e 00 00 00       	jmp    fa6b <zbtScoreDeleteInPlace+0x1bb>
    f9dd:	bb 15 00 00 00       	mov    ebx,0x15
    f9e2:	eb 74                	jmp    fa58 <zbtScoreDeleteInPlace+0x1a8>
    f9e4:	48 8d 3d 33 3c 00 00 	lea    rdi,[rip+0x3c33]        # 1361e <_IO_stdin_used+0x61e>
    f9eb:	48 8d 15 26 40 00 00 	lea    rdx,[rip+0x4026]        # 13a18 <_IO_stdin_used+0xa18>
    f9f2:	be 10 0a 00 00       	mov    esi,0xa10
    f9f7:	e8 14 24 00 00       	call   11e10 <standalone_panic>
    f9fc:	48 8d b5 68 ff ff ff 	lea    rsi,[rbp-0x98]
    fa03:	31 ff                	xor    edi,edi
    fa05:	e8 06 26 00 00       	call   12010 <zfree_usable>
    fa0a:	48 8b 85 68 ff ff ff 	mov    rax,QWORD PTR [rbp-0x98]
    fa11:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fa15:	48 29 41 68          	sub    QWORD PTR [rcx+0x68],rax
    fa19:	bb 15 00 00 00       	mov    ebx,0x15
    fa1e:	8b 75 b4             	mov    esi,DWORD PTR [rbp-0x4c]
    fa21:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa27:	66 39 c6             	cmp    si,ax
    fa2a:	74 3f                	je     fa6b <zbtScoreDeleteInPlace+0x1bb>
    fa2c:	4d 85 f6             	test   r14,r14
    fa2f:	74 27                	je     fa58 <zbtScoreDeleteInPlace+0x1a8>
    fa31:	b9 01 00 00 00       	mov    ecx,0x1
    fa36:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    fa3d:	00 00 00
    fa40:	41 0f b7 54 4f fe    	movzx  edx,WORD PTR [r15+rcx*2-0x2]
    fa46:	4c 39 f1             	cmp    rcx,r14
    fa49:	73 08                	jae    fa53 <zbtScoreDeleteInPlace+0x1a3>
    fa4b:	48 ff c1             	inc    rcx
    fa4e:	66 39 f2             	cmp    dx,si
    fa51:	76 ed                	jbe    fa40 <zbtScoreDeleteInPlace+0x190>
    fa53:	66 39 f2             	cmp    dx,si
    fa56:	77 13                	ja     fa6b <zbtScoreDeleteInPlace+0x1bb>
    fa58:	31 c9                	xor    ecx,ecx
    fa5a:	66 41 3b 74 24 36    	cmp    si,WORD PTR [r12+0x36]
    fa60:	75 34                	jne    fa96 <zbtScoreDeleteInPlace+0x1e6>
    fa62:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa67:	89 f0                	mov    eax,esi
    fa69:	eb 20                	jmp    fa8b <zbtScoreDeleteInPlace+0x1db>
    fa6b:	4d 8d 74 24 36       	lea    r14,[r12+0x36]
    fa70:	49 8d 34 04          	lea    rsi,[r12+rax*1]
    fa74:	48 8d 3c 1e          	lea    rdi,[rsi+rbx*1]
    fa78:	49 29 c5             	sub    r13,rax
    fa7b:	4c 89 ea             	mov    rdx,r13
    fa7e:	e8 dd 16 ff ff       	call   1160 <memmove@plt>
    fa83:	41 0f b7 44 24 36    	movzx  eax,WORD PTR [r12+0x36]
    fa89:	b1 01                	mov    cl,0x1
    fa8b:	89 4d 94             	mov    DWORD PTR [rbp-0x6c],ecx
    fa8e:	01 d8                	add    eax,ebx
    fa90:	66 41 89 06          	mov    WORD PTR [r14],ax
    fa94:	eb 07                	jmp    fa9d <zbtScoreDeleteInPlace+0x1ed>
    fa96:	c7 45 94 00 00 00 00 	mov    DWORD PTR [rbp-0x6c],0x0
    fa9d:	4d 8d 74 24 38       	lea    r14,[r12+0x38]
    faa2:	4c 89 bd 30 ff ff ff 	mov    QWORD PTR [rbp-0xd0],r15
    faa9:	48 8b 85 70 ff ff ff 	mov    rax,QWORD PTR [rbp-0x90]
    fab0:	49 8d 3c 47          	lea    rdi,[r15+rax*2]
    fab4:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    faba:	85 c0                	test   eax,eax
    fabc:	4c 89 65 c0          	mov    QWORD PTR [rbp-0x40],r12
    fac0:	0f 84 14 07 00 00    	je     101da <zbtScoreDeleteInPlace+0x92a>
    fac6:	48 89 bd 38 ff ff ff 	mov    QWORD PTR [rbp-0xc8],rdi
    facd:	89 85 64 ff ff ff    	mov    DWORD PTR [rbp-0x9c],eax
    fad3:	89 c2                	mov    edx,eax
    fad5:	48 89 d0             	mov    rax,rdx
    fad8:	48 0f af 85 70 ff ff 	imul   rax,QWORD PTR [rbp-0x90]
    fadf:	ff
    fae0:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    fae4:	41 0f b6 4c 24 11    	movzx  ecx,BYTE PTR [r12+0x11]
    faea:	8b 45 90             	mov    eax,DWORD PTR [rbp-0x70]
    faed:	f7 d0                	not    eax
    faef:	48 89 8d 40 ff ff ff 	mov    QWORD PTR [rbp-0xc0],rcx
    faf6:	01 c8                	add    eax,ecx
    faf8:	48 89 95 48 ff ff ff 	mov    QWORD PTR [rbp-0xb8],rdx
    faff:	48 0f af c2          	imul   rax,rdx
    fb03:	48 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rax
    fb0a:	48 83 f8 40          	cmp    rax,0x40
    fb0e:	0f 82 65 05 00 00    	jb     10079 <zbtScoreDeleteInPlace+0x7c9>
    fb14:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
    fb1b:	48 c1 e8 06          	shr    rax,0x6
    fb1f:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    fb23:	48 8b 85 48 ff ff ff 	mov    rax,QWORD PTR [rbp-0xb8]
    fb2a:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    fb2e:	4d 8d 1c 01          	lea    r11,[r9+rax*1]
    fb32:	44 89 df             	mov    edi,r11d
    fb35:	83 e7 07             	and    edi,0x7
    fb38:	be 40 00 00 00       	mov    esi,0x40
    fb3d:	29 fe                	sub    esi,edi
    fb3f:	45 89 ca             	mov    r10d,r9d
    fb42:	41 83 e2 07          	and    r10d,0x7
    fb46:	44 89 d1             	mov    ecx,r10d
    fb49:	f7 d9                	neg    ecx
    fb4b:	48 c7 c0 ff ff ff ff 	mov    rax,0xffffffffffffffff
    fb52:	48 d3 e0             	shl    rax,cl
    fb55:	45 31 ff             	xor    r15d,r15d
    fb58:	41 83 fa 01          	cmp    r10d,0x1
    fb5c:	4d 19 ff             	sbb    r15,r15
    fb5f:	48 f7 d0             	not    rax
    fb62:	49 09 c7             	or     r15,rax
    fb65:	4d 89 fd             	mov    r13,r15
    fb68:	44 89 d1             	mov    ecx,r10d
    fb6b:	49 d3 e5             	shl    r13,cl
    fb6e:	b8 7e 00 00 00       	mov    eax,0x7e
    fb73:	d3 e8                	shr    eax,cl
    fb75:	d3 e0                	shl    eax,cl
    fb77:	b9 40 00 00 00       	mov    ecx,0x40
    fb7c:	49 f7 d5             	not    r13
    fb7f:	45 85 d2             	test   r10d,r10d
    fb82:	0f 84 d4 00 00 00    	je     fc5c <zbtScoreDeleteInPlace+0x3ac>
    fb88:	4c 89 6d b8          	mov    QWORD PTR [rbp-0x48],r13
    fb8c:	4c 89 7d 98          	mov    QWORD PTR [rbp-0x68],r15
    fb90:	4d 89 d5             	mov    r13,r10
    fb93:	44 29 d1             	sub    ecx,r10d
    fb96:	48 89 8d 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],rcx
    fb9d:	89 c1                	mov    ecx,eax
    fb9f:	83 f1 7f             	xor    ecx,0x7f
    fba2:	48 89 8d 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],rcx
    fba9:	48 83 f0 80          	xor    rax,0xffffffffffffff80
    fbad:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    fbb1:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    fbb5:	85 ff                	test   edi,edi
    fbb7:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    fbbb:	4c 89 c9             	mov    rcx,r9
    fbbe:	0f 84 cf 00 00 00    	je     fc93 <zbtScoreDeleteInPlace+0x3e3>
    fbc4:	48 c1 e9 03          	shr    rcx,0x3
    fbc8:	4c 8d 24 01          	lea    r12,[rcx+rax*1]
    fbcc:	49 83 c4 40          	add    r12,0x40
    fbd0:	49 c1 eb 03          	shr    r11,0x3
    fbd4:	4d 8d 3c 03          	lea    r15,[r11+rax*1]
    fbd8:	49 83 c7 40          	add    r15,0x40
    fbdc:	45 31 c0             	xor    r8d,r8d
    fbdf:	4c 8b 55 98          	mov    r10,QWORD PTR [rbp-0x68]
    fbe3:	48 89 75 a0          	mov    QWORD PTR [rbp-0x60],rsi
    fbe7:	48 8b 75 80          	mov    rsi,QWORD PTR [rbp-0x80]
    fbeb:	48 8b bd 50 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xb0]
    fbf2:	48 8b 95 58 ff ff ff 	mov    rdx,QWORD PTR [rbp-0xa8]
    fbf9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    fc00:	4b 8b 44 c7 f8       	mov    rax,QWORD PTR [r15+r8*8-0x8]
    fc05:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fc09:	48 d3 e8             	shr    rax,cl
    fc0c:	47 0f b6 1c c7       	movzx  r11d,BYTE PTR [r15+r8*8]
    fc11:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    fc15:	49 d3 e3             	shl    r11,cl
    fc18:	49 09 c3             	or     r11,rax
    fc1b:	4b 8b 44 c4 f8       	mov    rax,QWORD PTR [r12+r8*8-0x8]
    fc20:	48 23 45 b8          	and    rax,QWORD PTR [rbp-0x48]
    fc24:	4d 89 d9             	mov    r9,r11
    fc27:	4d 21 d1             	and    r9,r10
    fc2a:	44 89 e9             	mov    ecx,r13d
    fc2d:	49 d3 e1             	shl    r9,cl
    fc30:	49 09 c1             	or     r9,rax
    fc33:	4f 89 4c c4 f8       	mov    QWORD PTR [r12+r8*8-0x8],r9
    fc38:	43 0f b6 04 c4       	movzx  eax,BYTE PTR [r12+r8*8]
    fc3d:	21 f0                	and    eax,esi
    fc3f:	89 f9                	mov    ecx,edi
    fc41:	49 d3 eb             	shr    r11,cl
    fc44:	41 21 d3             	and    r11d,edx
    fc47:	41 09 c3             	or     r11d,eax
    fc4a:	47 88 1c c4          	mov    BYTE PTR [r12+r8*8],r11b
    fc4e:	49 ff c0             	inc    r8
    fc51:	4c 39 45 c8          	cmp    QWORD PTR [rbp-0x38],r8
    fc55:	75 a9                	jne    fc00 <zbtScoreDeleteInPlace+0x350>
    fc57:	e9 1d 04 00 00       	jmp    10079 <zbtScoreDeleteInPlace+0x7c9>
    fc5c:	85 ff                	test   edi,edi
    fc5e:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    fc62:	0f 84 b8 00 00 00    	je     fd20 <zbtScoreDeleteInPlace+0x470>
    fc68:	48 89 75 a0          	mov    QWORD PTR [rbp-0x60],rsi
    fc6c:	4c 89 7d 98          	mov    QWORD PTR [rbp-0x68],r15
    fc70:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    fc74:	48 81 bd 78 ff ff ff 	cmp    QWORD PTR [rbp-0x88],0x43f
    fc7b:	3f 04 00 00
    fc7f:	4c 89 6d b8          	mov    QWORD PTR [rbp-0x48],r13
    fc83:	0f 87 b9 00 00 00    	ja     fd42 <zbtScoreDeleteInPlace+0x492>
    fc89:	4c 89 df             	mov    rdi,r11
    fc8c:	31 d2                	xor    edx,edx
    fc8e:	e9 0e 02 00 00       	jmp    fea1 <zbtScoreDeleteInPlace+0x5f1>
    fc93:	48 c1 e9 03          	shr    rcx,0x3
    fc97:	4c 8d 04 01          	lea    r8,[rcx+rax*1]
    fc9b:	49 83 c0 40          	add    r8,0x40
    fc9f:	49 c1 eb 03          	shr    r11,0x3
    fca3:	4c 01 d8             	add    rax,r11
    fca6:	48 83 c0 38          	add    rax,0x38
    fcaa:	48 89 45 a0          	mov    QWORD PTR [rbp-0x60],rax
    fcae:	45 31 ff             	xor    r15d,r15d
    fcb1:	4c 8b 55 98          	mov    r10,QWORD PTR [rbp-0x68]
    fcb5:	48 8b 55 b8          	mov    rdx,QWORD PTR [rbp-0x48]
    fcb9:	48 8b 75 80          	mov    rsi,QWORD PTR [rbp-0x80]
    fcbd:	4c 8b 9d 50 ff ff ff 	mov    r11,QWORD PTR [rbp-0xb0]
    fcc4:	48 8b bd 58 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xa8]
    fccb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    fcd0:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    fcd4:	4a 8b 04 f8          	mov    rax,QWORD PTR [rax+r15*8]
    fcd8:	48 8b 4d d0          	mov    rcx,QWORD PTR [rbp-0x30]
    fcdc:	48 d3 e8             	shr    rax,cl
    fcdf:	4f 8b 4c f8 f8       	mov    r9,QWORD PTR [r8+r15*8-0x8]
    fce4:	49 21 d1             	and    r9,rdx
    fce7:	49 89 c4             	mov    r12,rax
    fcea:	4d 21 d4             	and    r12,r10
    fced:	44 89 e9             	mov    ecx,r13d
    fcf0:	49 d3 e4             	shl    r12,cl
    fcf3:	4d 09 cc             	or     r12,r9
    fcf6:	4f 89 64 f8 f8       	mov    QWORD PTR [r8+r15*8-0x8],r12
    fcfb:	47 0f b6 0c f8       	movzx  r9d,BYTE PTR [r8+r15*8]
    fd00:	41 21 f1             	and    r9d,esi
    fd03:	44 89 d9             	mov    ecx,r11d
    fd06:	48 d3 e8             	shr    rax,cl
    fd09:	21 f8                	and    eax,edi
    fd0b:	44 09 c8             	or     eax,r9d
    fd0e:	43 88 04 f8          	mov    BYTE PTR [r8+r15*8],al
    fd12:	49 ff c7             	inc    r15
    fd15:	4c 39 7d c8          	cmp    QWORD PTR [rbp-0x38],r15
    fd19:	75 b5                	jne    fcd0 <zbtScoreDeleteInPlace+0x420>
    fd1b:	e9 59 03 00 00       	jmp    10079 <zbtScoreDeleteInPlace+0x7c9>
    fd20:	48 81 bd 78 ff ff ff 	cmp    QWORD PTR [rbp-0x88],0x200
    fd27:	00 02 00 00
    fd2b:	0f 83 fb 01 00 00    	jae    ff2c <zbtScoreDeleteInPlace+0x67c>
    fd31:	31 c9                	xor    ecx,ecx
    fd33:	4c 8b 4d c8          	mov    r9,QWORD PTR [rbp-0x38]
    fd37:	49 89 fc             	mov    r12,rdi
    fd3a:	4c 89 ff             	mov    rdi,r15
    fd3d:	e9 d6 02 00 00       	jmp    10018 <zbtScoreDeleteInPlace+0x768>
    fd42:	4c 89 df             	mov    rdi,r11
    fd45:	49 c1 eb 03          	shr    r11,0x3
    fd49:	4e 8d 04 18          	lea    r8,[rax+r11*1]
    fd4d:	4a 8d 0c 18          	lea    rcx,[rax+r11*1]
    fd51:	48 83 c1 40          	add    rcx,0x40
    fd55:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    fd59:	4b 8d 34 f8          	lea    rsi,[r8+r15*8]
    fd5d:	48 83 c6 38          	add    rsi,0x38
    fd61:	31 d2                	xor    edx,edx
    fd63:	48 39 ce             	cmp    rsi,rcx
    fd66:	0f 82 35 01 00 00    	jb     fea1 <zbtScoreDeleteInPlace+0x5f1>
    fd6c:	49 8d 77 ff          	lea    rsi,[r15-0x1]
    fd70:	48 c1 ee 3d          	shr    rsi,0x3d
    fd74:	0f 85 27 01 00 00    	jne    fea1 <zbtScoreDeleteInPlace+0x5f1>
    fd7a:	4c 89 ce             	mov    rsi,r9
    fd7d:	48 c1 ee 03          	shr    rsi,0x3
    fd81:	48 8d 14 30          	lea    rdx,[rax+rsi*1]
    fd85:	4c 8d 0c 30          	lea    r9,[rax+rsi*1]
    fd89:	49 83 c1 38          	add    r9,0x38
    fd8d:	4c 89 4d 80          	mov    QWORD PTR [rbp-0x80],r9
    fd91:	4c 8b 4d c8          	mov    r9,QWORD PTR [rbp-0x38]
    fd95:	4e 8d 24 ca          	lea    r12,[rdx+r9*8]
    fd99:	4e 8d 6c ca 38       	lea    r13,[rdx+r9*8+0x38]
    fd9e:	4f 8d 1c cb          	lea    r11,[r11+r9*8]
    fda2:	4e 8d 3c 18          	lea    r15,[rax+r11*1]
    fda6:	49 01 c3             	add    r11,rax
    fda9:	49 83 c3 39          	add    r11,0x39
    fdad:	4c 39 fa             	cmp    rdx,r15
    fdb0:	41 0f 92 c7          	setb   r15b
    fdb4:	4d 39 e0             	cmp    r8,r12
    fdb7:	41 0f 92 c4          	setb   r12b
    fdbb:	4c 39 5d 80          	cmp    QWORD PTR [rbp-0x80],r11
    fdbf:	41 0f 92 c0          	setb   r8b
    fdc3:	4c 39 e9             	cmp    rcx,r13
    fdc6:	41 0f 92 c3          	setb   r11b
    fdca:	31 d2                	xor    edx,edx
    fdcc:	45 84 e7             	test   r15b,r12b
    fdcf:	0f 85 c4 00 00 00    	jne    fe99 <zbtScoreDeleteInPlace+0x5e9>
    fdd5:	45 20 d8             	and    r8b,r11b
    fdd8:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    fddc:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    fde0:	0f 85 bb 00 00 00    	jne    fea1 <zbtScoreDeleteInPlace+0x5f1>
    fde6:	4c 8b 4d c8          	mov    r9,QWORD PTR [rbp-0x38]
    fdea:	44 89 ca             	mov    edx,r9d
    fded:	83 e2 01             	and    edx,0x1
    fdf0:	41 b8 02 00 00 00    	mov    r8d,0x2
    fdf6:	4c 0f 45 c2          	cmovne r8,rdx
    fdfa:	4c 89 ca             	mov    rdx,r9
    fdfd:	4c 29 c2             	sub    rdx,r8
    fe00:	66 0f 6e 45 d0       	movd   xmm0,DWORD PTR [rbp-0x30]
    fe05:	66 0f 6e 4d a0       	movd   xmm1,DWORD PTR [rbp-0x60]
    fe0a:	f3 0f 7e 55 b8       	movq   xmm2,QWORD PTR [rbp-0x48]
    fe0f:	66 0f 70 d2 44       	pshufd xmm2,xmm2,0x44
    fe14:	f3 0f 7e 5d 98       	movq   xmm3,QWORD PTR [rbp-0x68]
    fe19:	66 0f 70 db 44       	pshufd xmm3,xmm3,0x44
    fe1e:	66 41 0f 6e e2       	movd   xmm4,r10d
    fe23:	4c 8d 47 40          	lea    r8,[rdi+0x40]
    fe27:	48 01 c6             	add    rsi,rax
    fe2a:	48 83 c6 38          	add    rsi,0x38
    fe2e:	45 31 ff             	xor    r15d,r15d
    fe31:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    fe38:	0f 1f 84 00 00 00 00
    fe3f:	00
    fe40:	4d 89 c3             	mov    r11,r8
    fe43:	f3 42 0f 6f 6c f9 f8 	movdqu xmm5,XMMWORD PTR [rcx+r15*8-0x8]
    fe4a:	66 0f d3 e8          	psrlq  xmm5,xmm0
    fe4e:	49 c1 eb 03          	shr    r11,0x3
    fe52:	46 0f b6 24 f9       	movzx  r12d,BYTE PTR [rcx+r15*8]
    fe57:	47 0f b6 5c 1e 08    	movzx  r11d,BYTE PTR [r14+r11*1+0x8]
    fe5d:	66 41 0f 6e f4       	movd   xmm6,r12d
    fe62:	66 41 0f c4 f3 04    	pinsrw xmm6,r11d,0x4
    fe68:	66 0f f3 f1          	psllq  xmm6,xmm1
    fe6c:	66 0f eb f5          	por    xmm6,xmm5
    fe70:	66 0f db f3          	pand   xmm6,xmm3
    fe74:	66 0f f3 f4          	psllq  xmm6,xmm4
    fe78:	f3 42 0f 6f 2c fe    	movdqu xmm5,XMMWORD PTR [rsi+r15*8]
    fe7e:	66 0f db ea          	pand   xmm5,xmm2
    fe82:	66 0f eb ee          	por    xmm5,xmm6
    fe86:	f3 42 0f 7f 2c fe    	movdqu XMMWORD PTR [rsi+r15*8],xmm5
    fe8c:	49 83 c7 02          	add    r15,0x2
    fe90:	49 83 e8 80          	sub    r8,0xffffffffffffff80
    fe94:	4c 39 fa             	cmp    rdx,r15
    fe97:	75 a7                	jne    fe40 <zbtScoreDeleteInPlace+0x590>
    fe99:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    fe9d:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    fea1:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    fea5:	48 29 d6             	sub    rsi,rdx
    fea8:	48 c1 e2 06          	shl    rdx,0x6
    feac:	49 8d 0c 11          	lea    rcx,[r9+rdx*1]
    feb0:	49 89 f1             	mov    r9,rsi
    feb3:	48 c1 e9 03          	shr    rcx,0x3
    feb7:	48 8d 34 01          	lea    rsi,[rcx+rax*1]
    febb:	48 83 c6 38          	add    rsi,0x38
    febf:	48 01 d7             	add    rdi,rdx
    fec2:	48 c1 ef 03          	shr    rdi,0x3
    fec6:	48 8d 14 07          	lea    rdx,[rdi+rax*1]
    feca:	48 83 c2 40          	add    rdx,0x40
    fece:	45 31 c0             	xor    r8d,r8d
    fed1:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    fed5:	48 8b 7d 98          	mov    rdi,QWORD PTR [rbp-0x68]
    fed9:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    fedd:	4c 8b 6d a0          	mov    r13,QWORD PTR [rbp-0x60]
    fee1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    fee8:	0f 1f 84 00 00 00 00
    feef:	00
    fef0:	4e 8b 5c c2 f8       	mov    r11,QWORD PTR [rdx+r8*8-0x8]
    fef5:	89 c1                	mov    ecx,eax
    fef7:	49 d3 eb             	shr    r11,cl
    fefa:	46 0f b6 3c c2       	movzx  r15d,BYTE PTR [rdx+r8*8]
    feff:	44 89 e9             	mov    ecx,r13d
    ff02:	49 d3 e7             	shl    r15,cl
    ff05:	4d 09 df             	or     r15,r11
    ff08:	4e 8b 1c c6          	mov    r11,QWORD PTR [rsi+r8*8]
    ff0c:	4d 21 e3             	and    r11,r12
    ff0f:	49 21 ff             	and    r15,rdi
    ff12:	44 89 d1             	mov    ecx,r10d
    ff15:	49 d3 e7             	shl    r15,cl
    ff18:	4d 09 df             	or     r15,r11
    ff1b:	4e 89 3c c6          	mov    QWORD PTR [rsi+r8*8],r15
    ff1f:	49 ff c0             	inc    r8
    ff22:	4d 39 c1             	cmp    r9,r8
    ff25:	75 c9                	jne    fef0 <zbtScoreDeleteInPlace+0x640>
    ff27:	e9 4d 01 00 00       	jmp    10079 <zbtScoreDeleteInPlace+0x7c9>
    ff2c:	4c 89 ca             	mov    rdx,r9
    ff2f:	48 c1 ea 03          	shr    rdx,0x3
    ff33:	48 8d 0c 10          	lea    rcx,[rax+rdx*1]
    ff37:	4c 89 5d d0          	mov    QWORD PTR [rbp-0x30],r11
    ff3b:	4c 89 de             	mov    rsi,r11
    ff3e:	48 c1 ee 03          	shr    rsi,0x3
    ff42:	4c 8d 04 30          	lea    r8,[rax+rsi*1]
    ff46:	4c 8b 4d c8          	mov    r9,QWORD PTR [rbp-0x38]
    ff4a:	4f 8d 1c c8          	lea    r11,[r8+r9*8]
    ff4e:	4c 39 d9             	cmp    rcx,r11
    ff51:	73 1a                	jae    ff6d <zbtScoreDeleteInPlace+0x6bd>
    ff53:	4a 8d 0c c9          	lea    rcx,[rcx+r9*8]
    ff57:	49 39 c8             	cmp    r8,rcx
    ff5a:	73 11                	jae    ff6d <zbtScoreDeleteInPlace+0x6bd>
    ff5c:	31 c9                	xor    ecx,ecx
    ff5e:	49 89 fc             	mov    r12,rdi
    ff61:	4c 89 ff             	mov    rdi,r15
    ff64:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    ff68:	e9 ab 00 00 00       	jmp    10018 <zbtScoreDeleteInPlace+0x768>
    ff6d:	4c 89 c9             	mov    rcx,r9
    ff70:	48 83 e1 fc          	and    rcx,0xfffffffffffffffc
    ff74:	49 89 fc             	mov    r12,rdi
    ff77:	66 0f 6e c7          	movd   xmm0,edi
    ff7b:	4c 89 6d b8          	mov    QWORD PTR [rbp-0x48],r13
    ff7f:	66 49 0f 6e cd       	movq   xmm1,r13
    ff84:	66 0f 70 c9 44       	pshufd xmm1,xmm1,0x44
    ff89:	4c 89 ff             	mov    rdi,r15
    ff8c:	66 49 0f 6e d7       	movq   xmm2,r15
    ff91:	66 0f 70 d2 44       	pshufd xmm2,xmm2,0x44
    ff96:	4d 89 d3             	mov    r11,r10
    ff99:	66 41 0f 6e da       	movd   xmm3,r10d
    ff9e:	48 01 c2             	add    rdx,rax
    ffa1:	48 83 c2 48          	add    rdx,0x48
    ffa5:	48 01 c6             	add    rsi,rax
    ffa8:	48 83 c6 48          	add    rsi,0x48
    ffac:	45 31 c0             	xor    r8d,r8d
    ffaf:	90                   	nop
    ffb0:	f3 42 0f 6f 64 c6 f0 	movdqu xmm4,XMMWORD PTR [rsi+r8*8-0x10]
    ffb7:	f3 42 0f 6f 2c c6    	movdqu xmm5,XMMWORD PTR [rsi+r8*8]
    ffbd:	66 0f d3 e0          	psrlq  xmm4,xmm0
    ffc1:	66 0f d3 e8          	psrlq  xmm5,xmm0
    ffc5:	f3 42 0f 6f 74 c2 f0 	movdqu xmm6,XMMWORD PTR [rdx+r8*8-0x10]
    ffcc:	f3 42 0f 6f 3c c2    	movdqu xmm7,XMMWORD PTR [rdx+r8*8]
    ffd2:	66 0f db f1          	pand   xmm6,xmm1
    ffd6:	66 0f db f9          	pand   xmm7,xmm1
    ffda:	66 0f db e2          	pand   xmm4,xmm2
    ffde:	66 0f db ea          	pand   xmm5,xmm2
    ffe2:	66 0f f3 e3          	psllq  xmm4,xmm3
    ffe6:	66 0f eb e6          	por    xmm4,xmm6
    ffea:	66 0f f3 eb          	psllq  xmm5,xmm3
    ffee:	66 0f eb ef          	por    xmm5,xmm7
    fff2:	f3 42 0f 7f 64 c2 f0 	movdqu XMMWORD PTR [rdx+r8*8-0x10],xmm4
    fff9:	f3 42 0f 7f 2c c2    	movdqu XMMWORD PTR [rdx+r8*8],xmm5
    ffff:	49 83 c0 04          	add    r8,0x4
   10003:	4c 39 c1             	cmp    rcx,r8
   10006:	75 a8                	jne    ffb0 <zbtScoreDeleteInPlace+0x700>
   10008:	49 39 c9             	cmp    r9,rcx
   1000b:	4d 89 da             	mov    r10,r11
   1000e:	4c 8b 6d b8          	mov    r13,QWORD PTR [rbp-0x48]
   10012:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
   10016:	74 61                	je     10079 <zbtScoreDeleteInPlace+0x7c9>
   10018:	49 29 c9             	sub    r9,rcx
   1001b:	48 c1 e1 06          	shl    rcx,0x6
   1001f:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
   10023:	48 8d 14 08          	lea    rdx,[rax+rcx*1]
   10027:	48 c1 ea 03          	shr    rdx,0x3
   1002b:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
   1002f:	48 01 c2             	add    rdx,rax
   10032:	48 83 c2 38          	add    rdx,0x38
   10036:	49 01 cb             	add    r11,rcx
   10039:	49 c1 eb 03          	shr    r11,0x3
   1003d:	49 8d 34 03          	lea    rsi,[r11+rax*1]
   10041:	48 83 c6 38          	add    rsi,0x38
   10045:	45 31 c0             	xor    r8d,r8d
   10048:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
   1004f:	00
   10050:	4e 8b 1c c6          	mov    r11,QWORD PTR [rsi+r8*8]
   10054:	44 89 e1             	mov    ecx,r12d
   10057:	49 d3 eb             	shr    r11,cl
   1005a:	4e 8b 3c c2          	mov    r15,QWORD PTR [rdx+r8*8]
   1005e:	4d 21 ef             	and    r15,r13
   10061:	49 21 fb             	and    r11,rdi
   10064:	44 89 d1             	mov    ecx,r10d
   10067:	49 d3 e3             	shl    r11,cl
   1006a:	4d 09 fb             	or     r11,r15
   1006d:	4e 89 1c c2          	mov    QWORD PTR [rdx+r8*8],r11
   10071:	49 ff c0             	inc    r8
   10074:	4d 39 c1             	cmp    r9,r8
   10077:	75 d7                	jne    10050 <zbtScoreDeleteInPlace+0x7a0>
   10079:	4c 8b ad 78 ff ff ff 	mov    r13,QWORD PTR [rbp-0x88]
   10080:	45 89 e9             	mov    r9d,r13d
   10083:	41 83 e1 3f          	and    r9d,0x3f
   10087:	4c 8b 65 c0          	mov    r12,QWORD PTR [rbp-0x40]
   1008b:	4c 8b 9d 48 ff ff ff 	mov    r11,QWORD PTR [rbp-0xb8]
   10092:	0f 84 c4 00 00 00    	je     1015c <zbtScoreDeleteInPlace+0x8ac>
   10098:	4c 89 e8             	mov    rax,r13
   1009b:	48 83 e0 c0          	and    rax,0xffffffffffffffc0
   1009f:	4c 8b 7d a8          	mov    r15,QWORD PTR [rbp-0x58]
   100a3:	4b 8d 0c 1f          	lea    rcx,[r15+r11*1]
   100a7:	48 8d 34 08          	lea    rsi,[rax+rcx*1]
   100ab:	48 c1 ee 03          	shr    rsi,0x3
   100af:	89 cf                	mov    edi,ecx
   100b1:	83 e7 07             	and    edi,0x7
   100b4:	ba 40 00 00 00       	mov    edx,0x40
   100b9:	41 ba 40 00 00 00    	mov    r10d,0x40
   100bf:	41 29 fa             	sub    r10d,edi
   100c2:	4d 8b 04 36          	mov    r8,QWORD PTR [r14+rsi*1]
   100c6:	80 e1 07             	and    cl,0x7
   100c9:	49 d3 e8             	shr    r8,cl
   100cc:	45 39 ca             	cmp    r10d,r9d
   100cf:	73 0f                	jae    100e0 <zbtScoreDeleteInPlace+0x830>
   100d1:	41 0f b6 74 36 08    	movzx  esi,BYTE PTR [r14+rsi*1+0x8]
   100d7:	44 89 d1             	mov    ecx,r10d
   100da:	48 d3 e6             	shl    rsi,cl
   100dd:	49 09 f0             	or     r8,rsi
   100e0:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
   100e7:	44 89 e9             	mov    ecx,r13d
   100ea:	48 d3 e6             	shl    rsi,cl
   100ed:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
   100f4:	48 f7 d6             	not    rsi
   100f7:	4c 21 c6             	and    rsi,r8
   100fa:	4c 01 f8             	add    rax,r15
   100fd:	48 c1 e8 03          	shr    rax,0x3
   10101:	41 83 e7 07          	and    r15d,0x7
   10105:	44 29 fa             	sub    edx,r15d
   10108:	44 39 ca             	cmp    edx,r9d
   1010b:	45 89 c8             	mov    r8d,r9d
   1010e:	44 0f 42 c2          	cmovb  r8d,edx
   10112:	44 89 c1             	mov    ecx,r8d
   10115:	48 d3 e7             	shl    rdi,cl
   10118:	48 f7 d7             	not    rdi
   1011b:	49 89 f2             	mov    r10,rsi
   1011e:	49 21 fa             	and    r10,rdi
   10121:	44 89 f9             	mov    ecx,r15d
   10124:	48 d3 e7             	shl    rdi,cl
   10127:	48 f7 d7             	not    rdi
   1012a:	49 23 3c 06          	and    rdi,QWORD PTR [r14+rax*1]
   1012e:	49 d3 e2             	shl    r10,cl
   10131:	49 09 fa             	or     r10,rdi
   10134:	4d 89 14 06          	mov    QWORD PTR [r14+rax*1],r10
   10138:	44 39 ca             	cmp    edx,r9d
   1013b:	73 1f                	jae    1015c <zbtScoreDeleteInPlace+0x8ac>
   1013d:	45 29 c1             	sub    r9d,r8d
   10140:	41 0f b6 54 06 08    	movzx  edx,BYTE PTR [r14+rax*1+0x8]
   10146:	44 89 c1             	mov    ecx,r8d
   10149:	48 d3 ee             	shr    rsi,cl
   1014c:	31 f2                	xor    edx,esi
   1014e:	44 89 c9             	mov    ecx,r9d
   10151:	d3 ea                	shr    edx,cl
   10153:	d3 e2                	shl    edx,cl
   10155:	31 f2                	xor    edx,esi
   10157:	41 88 54 06 08       	mov    BYTE PTR [r14+rax*1+0x8],dl
   1015c:	4c 8b 8d 40 ff ff ff 	mov    r9,QWORD PTR [rbp-0xc0]
   10163:	49 ff c9             	dec    r9
   10166:	4d 0f af cb          	imul   r9,r11
   1016a:	4c 89 c8             	mov    rax,r9
   1016d:	48 c1 e8 03          	shr    rax,0x3
   10171:	44 89 c9             	mov    ecx,r9d
   10174:	83 e1 07             	and    ecx,0x7
   10177:	ba 40 00 00 00       	mov    edx,0x40
   1017c:	29 ca                	sub    edx,ecx
   1017e:	44 8b 85 64 ff ff ff 	mov    r8d,DWORD PTR [rbp-0x9c]
   10185:	44 39 c2             	cmp    edx,r8d
   10188:	44 89 c6             	mov    esi,r8d
   1018b:	0f 42 f2             	cmovb  esi,edx
   1018e:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
   10195:	89 f1                	mov    ecx,esi
   10197:	48 d3 e7             	shl    rdi,cl
   1019a:	48 c7 c1 ff ff ff ff 	mov    rcx,0xffffffffffffffff
   101a1:	83 fe 40             	cmp    esi,0x40
   101a4:	48 f7 d7             	not    rdi
   101a7:	48 0f 44 f9          	cmove  rdi,rcx
   101ab:	41 80 e1 07          	and    r9b,0x7
   101af:	44 89 c9             	mov    ecx,r9d
   101b2:	48 d3 e7             	shl    rdi,cl
   101b5:	48 f7 d7             	not    rdi
   101b8:	49 21 3c 06          	and    QWORD PTR [r14+rax*1],rdi
   101bc:	44 39 c2             	cmp    edx,r8d
   101bf:	48 8b bd 38 ff ff ff 	mov    rdi,QWORD PTR [rbp-0xc8]
   101c6:	73 12                	jae    101da <zbtScoreDeleteInPlace+0x92a>
   101c8:	41 29 f0             	sub    r8d,esi
   101cb:	ba ff ff ff ff       	mov    edx,0xffffffff
   101d0:	44 89 c1             	mov    ecx,r8d
   101d3:	d3 e2                	shl    edx,cl
   101d5:	41 20 54 06 08       	and    BYTE PTR [r14+rax*1+0x8],dl
   101da:	48 8d 77 02          	lea    rsi,[rdi+0x2]
   101de:	44 8b 6d 8c          	mov    r13d,DWORD PTR [rbp-0x74]
   101e2:	44 89 e8             	mov    eax,r13d
   101e5:	2b 45 90             	sub    eax,DWORD PTR [rbp-0x70]
   101e8:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
   101ec:	48 8d 14 00          	lea    rdx,[rax+rax*1]
   101f0:	e8 6b 0f ff ff       	call   1160 <memmove@plt>
   101f5:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
   101fb:	44 89 e9             	mov    ecx,r13d
   101fe:	45 89 ef             	mov    r15d,r13d
   10201:	48 85 c0             	test   rax,rax
   10204:	74 16                	je     1021c <zbtScoreDeleteInPlace+0x96c>
   10206:	49 0f af c7          	imul   rax,r15
   1020a:	48 83 c0 07          	add    rax,0x7
   1020e:	48 c1 e8 03          	shr    rax,0x3
   10212:	48 83 c0 09          	add    rax,0x9
   10216:	48 83 e0 fe          	and    rax,0xfffffffffffffffe
   1021a:	eb 02                	jmp    1021e <zbtScoreDeleteInPlace+0x96e>
   1021c:	31 c0                	xor    eax,eax
   1021e:	85 c9                	test   ecx,ecx
   10220:	0f 94 45 d0          	sete   BYTE PTR [rbp-0x30]
   10224:	49 01 c6             	add    r14,rax
   10227:	4b 8d 14 3f          	lea    rdx,[r15+r15*1]
   1022b:	4c 89 f7             	mov    rdi,r14
   1022e:	48 8b b5 30 ff ff ff 	mov    rsi,QWORD PTR [rbp-0xd0]
   10235:	e8 26 0f ff ff       	call   1160 <memmove@plt>
   1023a:	4f 8d 24 7e          	lea    r12,[r14+r15*2]
   1023e:	48 8d b5 d0 fe ff ff 	lea    rsi,[rbp-0x130]
   10245:	4c 89 e7             	mov    rdi,r12
   10248:	4c 8b ad 70 ff ff ff 	mov    r13,QWORD PTR [rbp-0x90]
   1024f:	4c 89 ea             	mov    rdx,r13
   10252:	e8 c9 0e ff ff       	call   1120 <memcpy@plt>
   10257:	4d 01 ec             	add    r12,r13
   1025a:	4a 8d 34 2d d1 fe ff 	lea    rsi,[r13*1-0x12f]
   10261:	ff
   10262:	48 01 ee             	add    rsi,rbp
   10265:	4c 89 e7             	mov    rdi,r12
   10268:	48 8b 55 c8          	mov    rdx,QWORD PTR [rbp-0x38]
   1026c:	e8 af 0e ff ff       	call   1120 <memcpy@plt>
   10271:	8b 4d 8c             	mov    ecx,DWORD PTR [rbp-0x74]
   10274:	48 8b 7d c0          	mov    rdi,QWORD PTR [rbp-0x40]
   10278:	88 4f 11             	mov    BYTE PTR [rdi+0x11],cl
   1027b:	4c 89 7f 08          	mov    QWORD PTR [rdi+0x8],r15
   1027f:	8b 45 94             	mov    eax,DWORD PTR [rbp-0x6c]
   10282:	34 01                	xor    al,0x1
   10284:	0a 45 d0             	or     al,BYTE PTR [rbp-0x30]
   10287:	44 8b 45 b4          	mov    r8d,DWORD PTR [rbp-0x4c]
   1028b:	0f 85 00 03 00 00    	jne    10591 <zbtScoreDeleteInPlace+0xce1>
   10291:	83 f9 10             	cmp    ecx,0x10
   10294:	73 07                	jae    1029d <zbtScoreDeleteInPlace+0x9ed>
   10296:	31 c0                	xor    eax,eax
   10298:	e9 1b 03 00 00       	jmp    105b8 <zbtScoreDeleteInPlace+0xd08>
   1029d:	44 89 f8             	mov    eax,r15d
   102a0:	83 e0 f0             	and    eax,0xfffffff0
   102a3:	66 41 0f 6e c0       	movd   xmm0,r8d
   102a8:	f2 0f 70 c0 00       	pshuflw xmm0,xmm0,0x0
   102ad:	66 0f 70 c0 00       	pshufd xmm0,xmm0,0x0
   102b2:	31 c9                	xor    ecx,ecx
   102b4:	66 0f 6f 0d 94 2d 00 	movdqa xmm1,XMMWORD PTR [rip+0x2d94]        # 13050 <_IO_stdin_used+0x50>
   102bb:	00
   102bc:	66 0f ef c1          	pxor   xmm0,xmm1
   102c0:	eb 1b                	jmp    102dd <zbtScoreDeleteInPlace+0xa2d>
   102c2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
   102c9:	1f 84 00 00 00 00 00
   102d0:	48 83 c1 10          	add    rcx,0x10
   102d4:	48 39 c8             	cmp    rax,rcx
   102d7:	0f 84 af 02 00 00    	je     1058c <zbtScoreDeleteInPlace+0xcdc>
   102dd:	f3 41 0f 6f 14 4e    	movdqu xmm2,XMMWORD PTR [r14+rcx*2]
   102e3:	66 0f 6f e2          	movdqa xmm4,xmm2
   102e7:	66 0f ef e1          	pxor   xmm4,xmm1
   102eb:	66 0f 6f d8          	movdqa xmm3,xmm0
   102ef:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
   102f3:	66 0f 7e da          	movd   edx,xmm3
   102f7:	f6 c2 01             	test   dl,0x1
   102fa:	0f 85 00 01 00 00    	jne    10400 <zbtScoreDeleteInPlace+0xb50>
   10300:	c1 ea 10             	shr    edx,0x10
   10303:	f6 c2 01             	test   dl,0x1
   10306:	0f 85 0b 01 00 00    	jne    10417 <zbtScoreDeleteInPlace+0xb67>
   1030c:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
   10311:	f6 c2 01             	test   dl,0x1
   10314:	0f 85 18 01 00 00    	jne    10432 <zbtScoreDeleteInPlace+0xb82>
   1031a:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
   1031f:	f6 c2 01             	test   dl,0x1
   10322:	0f 85 25 01 00 00    	jne    1044d <zbtScoreDeleteInPlace+0xb9d>
   10328:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
   1032d:	f6 c2 01             	test   dl,0x1
   10330:	0f 85 32 01 00 00    	jne    10468 <zbtScoreDeleteInPlace+0xbb8>
   10336:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   1033b:	f6 c2 01             	test   dl,0x1
   1033e:	0f 85 3f 01 00 00    	jne    10483 <zbtScoreDeleteInPlace+0xbd3>
   10344:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   10349:	f6 c2 01             	test   dl,0x1
   1034c:	0f 85 4c 01 00 00    	jne    1049e <zbtScoreDeleteInPlace+0xbee>
   10352:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   10357:	f6 c2 01             	test   dl,0x1
   1035a:	74 0d                	je     10369 <zbtScoreDeleteInPlace+0xab9>
   1035c:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
   10361:	01 da                	add    edx,ebx
   10363:	66 41 89 54 4e 0e    	mov    WORD PTR [r14+rcx*2+0xe],dx
   10369:	f3 41 0f 6f 54 4e 10 	movdqu xmm2,XMMWORD PTR [r14+rcx*2+0x10]
   10370:	66 0f 6f e2          	movdqa xmm4,xmm2
   10374:	66 0f ef e1          	pxor   xmm4,xmm1
   10378:	66 0f 6f d8          	movdqa xmm3,xmm0
   1037c:	66 0f 65 dc          	pcmpgtw xmm3,xmm4
   10380:	66 0f 7e da          	movd   edx,xmm3
   10384:	f6 c2 01             	test   dl,0x1
   10387:	0f 85 33 01 00 00    	jne    104c0 <zbtScoreDeleteInPlace+0xc10>
   1038d:	c1 ea 10             	shr    edx,0x10
   10390:	f6 c2 01             	test   dl,0x1
   10393:	0f 85 3f 01 00 00    	jne    104d8 <zbtScoreDeleteInPlace+0xc28>
   10399:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
   1039e:	f6 c2 01             	test   dl,0x1
   103a1:	0f 85 4c 01 00 00    	jne    104f3 <zbtScoreDeleteInPlace+0xc43>
   103a7:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
   103ac:	f6 c2 01             	test   dl,0x1
   103af:	0f 85 59 01 00 00    	jne    1050e <zbtScoreDeleteInPlace+0xc5e>
   103b5:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
   103ba:	f6 c2 01             	test   dl,0x1
   103bd:	0f 85 66 01 00 00    	jne    10529 <zbtScoreDeleteInPlace+0xc79>
   103c3:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   103c8:	f6 c2 01             	test   dl,0x1
   103cb:	0f 85 73 01 00 00    	jne    10544 <zbtScoreDeleteInPlace+0xc94>
   103d1:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   103d6:	f6 c2 01             	test   dl,0x1
   103d9:	0f 85 80 01 00 00    	jne    1055f <zbtScoreDeleteInPlace+0xcaf>
   103df:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   103e4:	f6 c2 01             	test   dl,0x1
   103e7:	0f 84 e3 fe ff ff    	je     102d0 <zbtScoreDeleteInPlace+0xa20>
   103ed:	e9 88 01 00 00       	jmp    1057a <zbtScoreDeleteInPlace+0xcca>
   103f2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
   103f9:	1f 84 00 00 00 00 00
   10400:	66 0f 7e d6          	movd   esi,xmm2
   10404:	01 de                	add    esi,ebx
   10406:	66 41 89 34 4e       	mov    WORD PTR [r14+rcx*2],si
   1040b:	c1 ea 10             	shr    edx,0x10
   1040e:	f6 c2 01             	test   dl,0x1
   10411:	0f 84 f5 fe ff ff    	je     1030c <zbtScoreDeleteInPlace+0xa5c>
   10417:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
   1041c:	01 da                	add    edx,ebx
   1041e:	66 41 89 54 4e 02    	mov    WORD PTR [r14+rcx*2+0x2],dx
   10424:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
   10429:	f6 c2 01             	test   dl,0x1
   1042c:	0f 84 e8 fe ff ff    	je     1031a <zbtScoreDeleteInPlace+0xa6a>
   10432:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
   10437:	01 da                	add    edx,ebx
   10439:	66 41 89 54 4e 04    	mov    WORD PTR [r14+rcx*2+0x4],dx
   1043f:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
   10444:	f6 c2 01             	test   dl,0x1
   10447:	0f 84 db fe ff ff    	je     10328 <zbtScoreDeleteInPlace+0xa78>
   1044d:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
   10452:	01 da                	add    edx,ebx
   10454:	66 41 89 54 4e 06    	mov    WORD PTR [r14+rcx*2+0x6],dx
   1045a:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
   1045f:	f6 c2 01             	test   dl,0x1
   10462:	0f 84 ce fe ff ff    	je     10336 <zbtScoreDeleteInPlace+0xa86>
   10468:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
   1046d:	01 da                	add    edx,ebx
   1046f:	66 41 89 54 4e 08    	mov    WORD PTR [r14+rcx*2+0x8],dx
   10475:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   1047a:	f6 c2 01             	test   dl,0x1
   1047d:	0f 84 c1 fe ff ff    	je     10344 <zbtScoreDeleteInPlace+0xa94>
   10483:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
   10488:	01 da                	add    edx,ebx
   1048a:	66 41 89 54 4e 0a    	mov    WORD PTR [r14+rcx*2+0xa],dx
   10490:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   10495:	f6 c2 01             	test   dl,0x1
   10498:	0f 84 b4 fe ff ff    	je     10352 <zbtScoreDeleteInPlace+0xaa2>
   1049e:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
   104a3:	01 da                	add    edx,ebx
   104a5:	66 41 89 54 4e 0c    	mov    WORD PTR [r14+rcx*2+0xc],dx
   104ab:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   104b0:	f6 c2 01             	test   dl,0x1
   104b3:	0f 85 a3 fe ff ff    	jne    1035c <zbtScoreDeleteInPlace+0xaac>
   104b9:	e9 ab fe ff ff       	jmp    10369 <zbtScoreDeleteInPlace+0xab9>
   104be:	66 90                	xchg   ax,ax
   104c0:	66 0f 7e d6          	movd   esi,xmm2
   104c4:	01 de                	add    esi,ebx
   104c6:	66 41 89 74 4e 10    	mov    WORD PTR [r14+rcx*2+0x10],si
   104cc:	c1 ea 10             	shr    edx,0x10
   104cf:	f6 c2 01             	test   dl,0x1
   104d2:	0f 84 c1 fe ff ff    	je     10399 <zbtScoreDeleteInPlace+0xae9>
   104d8:	66 0f c5 d2 01       	pextrw edx,xmm2,0x1
   104dd:	01 da                	add    edx,ebx
   104df:	66 41 89 54 4e 12    	mov    WORD PTR [r14+rcx*2+0x12],dx
   104e5:	66 0f c5 d3 02       	pextrw edx,xmm3,0x2
   104ea:	f6 c2 01             	test   dl,0x1
   104ed:	0f 84 b4 fe ff ff    	je     103a7 <zbtScoreDeleteInPlace+0xaf7>
   104f3:	66 0f c5 d2 02       	pextrw edx,xmm2,0x2
   104f8:	01 da                	add    edx,ebx
   104fa:	66 41 89 54 4e 14    	mov    WORD PTR [r14+rcx*2+0x14],dx
   10500:	66 0f c5 d3 03       	pextrw edx,xmm3,0x3
   10505:	f6 c2 01             	test   dl,0x1
   10508:	0f 84 a7 fe ff ff    	je     103b5 <zbtScoreDeleteInPlace+0xb05>
   1050e:	66 0f c5 d2 03       	pextrw edx,xmm2,0x3
   10513:	01 da                	add    edx,ebx
   10515:	66 41 89 54 4e 16    	mov    WORD PTR [r14+rcx*2+0x16],dx
   1051b:	66 0f c5 d3 04       	pextrw edx,xmm3,0x4
   10520:	f6 c2 01             	test   dl,0x1
   10523:	0f 84 9a fe ff ff    	je     103c3 <zbtScoreDeleteInPlace+0xb13>
   10529:	66 0f c5 d2 04       	pextrw edx,xmm2,0x4
   1052e:	01 da                	add    edx,ebx
   10530:	66 41 89 54 4e 18    	mov    WORD PTR [r14+rcx*2+0x18],dx
   10536:	66 0f c5 d3 05       	pextrw edx,xmm3,0x5
   1053b:	f6 c2 01             	test   dl,0x1
   1053e:	0f 84 8d fe ff ff    	je     103d1 <zbtScoreDeleteInPlace+0xb21>
   10544:	66 0f c5 d2 05       	pextrw edx,xmm2,0x5
   10549:	01 da                	add    edx,ebx
   1054b:	66 41 89 54 4e 1a    	mov    WORD PTR [r14+rcx*2+0x1a],dx
   10551:	66 0f c5 d3 06       	pextrw edx,xmm3,0x6
   10556:	f6 c2 01             	test   dl,0x1
   10559:	0f 84 80 fe ff ff    	je     103df <zbtScoreDeleteInPlace+0xb2f>
   1055f:	66 0f c5 d2 06       	pextrw edx,xmm2,0x6
   10564:	01 da                	add    edx,ebx
   10566:	66 41 89 54 4e 1c    	mov    WORD PTR [r14+rcx*2+0x1c],dx
   1056c:	66 0f c5 d3 07       	pextrw edx,xmm3,0x7
   10571:	f6 c2 01             	test   dl,0x1
   10574:	0f 84 56 fd ff ff    	je     102d0 <zbtScoreDeleteInPlace+0xa20>
   1057a:	66 0f c5 d2 07       	pextrw edx,xmm2,0x7
   1057f:	01 da                	add    edx,ebx
   10581:	66 41 89 54 4e 1e    	mov    WORD PTR [r14+rcx*2+0x1e],dx
   10587:	e9 44 fd ff ff       	jmp    102d0 <zbtScoreDeleteInPlace+0xa20>
   1058c:	4c 39 f8             	cmp    rax,r15
   1058f:	75 27                	jne    105b8 <zbtScoreDeleteInPlace+0xd08>
   10591:	48 c7 c6 ff ff ff ff 	mov    rsi,0xffffffffffffffff
   10598:	e8 e3 eb ff ff       	call   f180 <zbtScoreUpdatePath>
   1059d:	48 81 c4 08 01 00 00 	add    rsp,0x108
   105a4:	5b                   	pop    rbx
   105a5:	41 5c                	pop    r12
   105a7:	41 5d                	pop    r13
   105a9:	41 5e                	pop    r14
   105ab:	41 5f                	pop    r15
   105ad:	5d                   	pop    rbp
   105ae:	c3                   	ret
   105af:	90                   	nop
   105b0:	48 ff c0             	inc    rax
   105b3:	49 39 c7             	cmp    r15,rax
   105b6:	74 d9                	je     10591 <zbtScoreDeleteInPlace+0xce1>
   105b8:	41 0f b7 0c 46       	movzx  ecx,WORD PTR [r14+rax*2]
   105bd:	66 44 39 c1          	cmp    cx,r8w
   105c1:	73 ed                	jae    105b0 <zbtScoreDeleteInPlace+0xd00>
   105c3:	01 d9                	add    ecx,ebx
   105c5:	66 41 89 0c 46       	mov    WORD PTR [r14+rax*2],cx
   105ca:	eb e4                	jmp    105b0 <zbtScoreDeleteInPlace+0xd00>

Disassembly of section .fini:
