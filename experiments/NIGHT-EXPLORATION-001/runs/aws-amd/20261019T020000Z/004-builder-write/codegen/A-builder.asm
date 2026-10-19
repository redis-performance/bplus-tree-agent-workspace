
scratch/amd-builder-build/A/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000bf80 <zbtScoreLeafBuild>:
    bf80:	55                   	push   rbp
    bf81:	48 89 e5             	mov    rbp,rsp
    bf84:	41 57                	push   r15
    bf86:	41 56                	push   r14
    bf88:	41 55                	push   r13
    bf8a:	41 54                	push   r12
    bf8c:	53                   	push   rbx
    bf8d:	48 81 ec 88 00 00 00 	sub    rsp,0x88
    bf94:	4c 89 8d 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],r9
    bf9b:	4c 89 85 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],r8
    bfa2:	49 89 cb             	mov    r11,rcx
    bfa5:	49 89 fd             	mov    r13,rdi
    bfa8:	f3 0f 7e 02          	movq   xmm0,QWORD PTR [rdx]
    bfac:	66 48 0f 7e c0       	movq   rax,xmm0
    bfb1:	48 bb 00 00 00 00 00 	movabs rbx,0x8000000000000000
    bfb8:	00 00 80
    bfbb:	48 89 c1             	mov    rcx,rax
    bfbe:	48 85 c0             	test   rax,rax
    bfc1:	78 05                	js     bfc8 <zbtScoreLeafBuild+0x48>
    bfc3:	48 09 d9             	or     rcx,rbx
    bfc6:	eb 03                	jmp    bfcb <zbtScoreLeafBuild+0x4b>
    bfc8:	48 f7 d1             	not    rcx
    bfcb:	48 89 4d b8          	mov    QWORD PTR [rbp-0x48],rcx
    bfcf:	41 89 f4             	mov    r12d,esi
    bfd2:	49 89 f6             	mov    r14,rsi
    bfd5:	83 fe 02             	cmp    esi,0x2
    bfd8:	72 4d                	jb     c027 <zbtScoreLeafBuild+0xa7>
    bfda:	bf 01 00 00 00       	mov    edi,0x1
    bfdf:	31 c9                	xor    ecx,ecx
    bfe1:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    bfe5:	49 89 f2             	mov    r10,rsi
    bfe8:	eb 29                	jmp    c013 <zbtScoreLeafBuild+0x93>
    bfea:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    bff0:	49 09 d8             	or     r8,rbx
    bff3:	4d 89 c1             	mov    r9,r8
    bff6:	4c 33 4d b8          	xor    r9,QWORD PTR [rbp-0x48]
    bffa:	4c 09 c9             	or     rcx,r9
    bffd:	4d 39 d0             	cmp    r8,r10
    c000:	4d 0f 42 d0          	cmovb  r10,r8
    c004:	49 39 f0             	cmp    r8,rsi
    c007:	49 0f 47 f0          	cmova  rsi,r8
    c00b:	48 ff c7             	inc    rdi
    c00e:	49 39 fc             	cmp    r12,rdi
    c011:	74 19                	je     c02c <zbtScoreLeafBuild+0xac>
    c013:	f3 0f 7e 04 fa       	movq   xmm0,QWORD PTR [rdx+rdi*8]
    c018:	66 49 0f 7e c0       	movq   r8,xmm0
    c01d:	4d 85 c0             	test   r8,r8
    c020:	79 ce                	jns    bff0 <zbtScoreLeafBuild+0x70>
    c022:	49 f7 d0             	not    r8
    c025:	eb cc                	jmp    bff3 <zbtScoreLeafBuild+0x73>
    c027:	45 31 c0             	xor    r8d,r8d
    c02a:	eb 5e                	jmp    c08a <zbtScoreLeafBuild+0x10a>
    c02c:	45 31 c0             	xor    r8d,r8d
    c02f:	48 85 c9             	test   rcx,rcx
    c032:	74 52                	je     c086 <zbtScoreLeafBuild+0x106>
    c034:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c039:	4c 29 d6             	sub    rsi,r10
    c03c:	48 89 4d d0          	mov    QWORD PTR [rbp-0x30],rcx
    c040:	48 d3 ee             	shr    rsi,cl
    c043:	48 0f bd ce          	bsr    rcx,rsi
    c047:	83 f1 3f             	xor    ecx,0x3f
    c04a:	40 b7 40             	mov    dil,0x40
    c04d:	40 28 cf             	sub    dil,cl
    c050:	48 85 f6             	test   rsi,rsi
    c053:	40 0f b6 cf          	movzx  ecx,dil
    c057:	41 0f 44 c8          	cmove  ecx,r8d
    c05b:	4c 89 55 b8          	mov    QWORD PTR [rbp-0x48],r10
    c05f:	41 89 c8             	mov    r8d,ecx
    c062:	44 89 45 cc          	mov    DWORD PTR [rbp-0x34],r8d
    c066:	48 85 c0             	test   rax,rax
    c069:	79 2e                	jns    c099 <zbtScoreLeafBuild+0x119>
    c06b:	48 f7 d0             	not    rax
    c06e:	41 bf 38 00 00 00    	mov    r15d,0x38
    c074:	41 83 fe 02          	cmp    r14d,0x2
    c078:	48 89 95 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdx
    c07f:	73 32                	jae    c0b3 <zbtScoreLeafBuild+0x133>
    c081:	e9 c3 00 00 00       	jmp    c149 <zbtScoreLeafBuild+0x1c9>
    c086:	4c 89 55 b8          	mov    QWORD PTR [rbp-0x48],r10
    c08a:	31 c9                	xor    ecx,ecx
    c08c:	48 89 4d d0          	mov    QWORD PTR [rbp-0x30],rcx
    c090:	44 89 45 cc          	mov    DWORD PTR [rbp-0x34],r8d
    c094:	48 85 c0             	test   rax,rax
    c097:	78 d2                	js     c06b <zbtScoreLeafBuild+0xeb>
    c099:	48 09 d8             	or     rax,rbx
    c09c:	41 bf 38 00 00 00    	mov    r15d,0x38
    c0a2:	41 83 fe 02          	cmp    r14d,0x2
    c0a6:	48 89 95 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdx
    c0ad:	0f 82 96 00 00 00    	jb     c149 <zbtScoreLeafBuild+0x1c9>
    c0b3:	41 b8 01 00 00 00    	mov    r8d,0x1
    c0b9:	31 c9                	xor    ecx,ecx
    c0bb:	48 89 c7             	mov    rdi,rax
    c0be:	48 89 c6             	mov    rsi,rax
    c0c1:	eb 2f                	jmp    c0f2 <zbtScoreLeafBuild+0x172>
    c0c3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c0ca:	84 00 00 00 00 00
    c0d0:	49 09 d9             	or     r9,rbx
    c0d3:	4d 89 ca             	mov    r10,r9
    c0d6:	49 31 c2             	xor    r10,rax
    c0d9:	4c 09 d1             	or     rcx,r10
    c0dc:	49 39 f9             	cmp    r9,rdi
    c0df:	49 0f 42 f9          	cmovb  rdi,r9
    c0e3:	49 39 f1             	cmp    r9,rsi
    c0e6:	49 0f 47 f1          	cmova  rsi,r9
    c0ea:	49 ff c0             	inc    r8
    c0ed:	4d 39 c4             	cmp    r12,r8
    c0f0:	74 15                	je     c107 <zbtScoreLeafBuild+0x187>
    c0f2:	f3 42 0f 7e 04 c2    	movq   xmm0,QWORD PTR [rdx+r8*8]
    c0f8:	66 49 0f 7e c1       	movq   r9,xmm0
    c0fd:	4d 85 c9             	test   r9,r9
    c100:	79 ce                	jns    c0d0 <zbtScoreLeafBuild+0x150>
    c102:	49 f7 d1             	not    r9
    c105:	eb cc                	jmp    c0d3 <zbtScoreLeafBuild+0x153>
    c107:	48 85 c9             	test   rcx,rcx
    c10a:	74 3d                	je     c149 <zbtScoreLeafBuild+0x1c9>
    c10c:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c111:	48 29 fe             	sub    rsi,rdi
    c114:	48 d3 ee             	shr    rsi,cl
    c117:	48 85 f6             	test   rsi,rsi
    c11a:	74 2d                	je     c149 <zbtScoreLeafBuild+0x1c9>
    c11c:	48 0f bd c6          	bsr    rax,rsi
    c120:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    c124:	48 83 c0 41          	add    rax,0x41
    c128:	49 0f af c4          	imul   rax,r12
    c12c:	48 83 c0 07          	add    rax,0x7
    c130:	48 c1 e8 03          	shr    rax,0x3
    c134:	48 83 c0 09          	add    rax,0x9
    c138:	49 bf fe ff ff ff ff 	movabs r15,0x1ffffffffffffffe
    c13f:	ff ff 1f
    c142:	49 21 c7             	and    r15,rax
    c145:	49 83 c7 38          	add    r15,0x38
    c149:	8b 45 10             	mov    eax,DWORD PTR [rbp+0x10]
    c14c:	4b 8d 1c 64          	lea    rbx,[r12+r12*2]
    c150:	4c 01 fb             	add    rbx,r15
    c153:	45 85 f6             	test   r14d,r14d
    c156:	74 55                	je     c1ad <zbtScoreLeafBuild+0x22d>
    c158:	4a 8d 0c e5 00 00 00 	lea    rcx,[r12*8+0x0]
    c15f:	00
    c160:	48 8d 0c 89          	lea    rcx,[rcx+rcx*4]
    c164:	31 d2                	xor    edx,edx
    c166:	44 8b 7d cc          	mov    r15d,DWORD PTR [rbp-0x34]
    c16a:	eb 10                	jmp    c17c <zbtScoreLeafBuild+0x1fc>
    c16c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    c170:	48 01 f3             	add    rbx,rsi
    c173:	48 83 c2 28          	add    rdx,0x28
    c177:	48 39 d1             	cmp    rcx,rdx
    c17a:	74 35                	je     c1b1 <zbtScoreLeafBuild+0x231>
    c17c:	be 15 00 00 00       	mov    esi,0x15
    c181:	49 83 7c 13 18 00    	cmp    QWORD PTR [r11+rdx*1+0x18],0x0
    c187:	75 e7                	jne    c170 <zbtScoreLeafBuild+0x1f0>
    c189:	49 8b 7c 13 08       	mov    rdi,QWORD PTR [r11+rdx*1+0x8]
    c18e:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    c195:	77 d9                	ja     c170 <zbtScoreLeafBuild+0x1f0>
    c197:	31 f6                	xor    esi,esi
    c199:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    c1a0:	40 0f 93 c6          	setae  sil
    c1a4:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    c1a8:	48 ff c6             	inc    rsi
    c1ab:	eb c3                	jmp    c170 <zbtScoreLeafBuild+0x1f0>
    c1ad:	44 8b 7d cc          	mov    r15d,DWORD PTR [rbp-0x34]
    c1b1:	4c 89 65 98          	mov    QWORD PTR [rbp-0x68],r12
    c1b5:	4c 89 5d c0          	mov    QWORD PTR [rbp-0x40],r11
    c1b9:	85 c0                	test   eax,eax
    c1bb:	4d 89 f4             	mov    r12,r14
    c1be:	74 0e                	je     c1ce <zbtScoreLeafBuild+0x24e>
    c1c0:	bf ff 0f 00 00       	mov    edi,0xfff
    c1c5:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c1cc:	72 29                	jb     c1f7 <zbtScoreLeafBuild+0x277>
    c1ce:	48 89 df             	mov    rdi,rbx
    c1d1:	41 83 fc 5f          	cmp    r12d,0x5f
    c1d5:	77 20                	ja     c1f7 <zbtScoreLeafBuild+0x277>
    c1d7:	48 89 df             	mov    rdi,rbx
    c1da:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    c1e1:	77 14                	ja     c1f7 <zbtScoreLeafBuild+0x277>
    c1e3:	48 81 fb 7f 0f 00 00 	cmp    rbx,0xf7f
    c1ea:	bf 7f 0f 00 00       	mov    edi,0xf7f
    c1ef:	48 0f 42 fb          	cmovb  rdi,rbx
    c1f3:	48 83 ef 80          	sub    rdi,0xffffffffffffff80
    c1f7:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    c1fb:	e8 c0 55 00 00       	call   117c0 <zmalloc_usable>
    c200:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    c204:	49 01 4d 68          	add    QWORD PTR [r13+0x68],rcx
    c208:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    c20c:	41 8d 44 24 ff       	lea    eax,[r12-0x1]
    c211:	83 f8 60             	cmp    eax,0x60
    c214:	72 18                	jb     c22e <zbtScoreLeafBuild+0x2ae>
    c216:	48 8d 3d 01 74 00 00 	lea    rdi,[rip+0x7401]        # 1361e <_IO_stdin_used+0x61e>
    c21d:	48 8d 15 a2 75 00 00 	lea    rdx,[rip+0x75a2]        # 137c6 <_IO_stdin_used+0x7c6>
    c224:	be f0 03 00 00       	mov    esi,0x3f0
    c229:	e8 92 54 00 00       	call   116c0 <standalone_panic>
    c22e:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c235:	72 18                	jb     c24f <zbtScoreLeafBuild+0x2cf>
    c237:	48 8d 3d e0 73 00 00 	lea    rdi,[rip+0x73e0]        # 1361e <_IO_stdin_used+0x61e>
    c23e:	48 8d 15 aa 75 00 00 	lea    rdx,[rip+0x75aa]        # 137ef <_IO_stdin_used+0x7ef>
    c245:	be f1 03 00 00       	mov    esi,0x3f1
    c24a:	e8 71 54 00 00       	call   116c0 <standalone_panic>
    c24f:	4c 89 6d 88          	mov    QWORD PTR [rbp-0x78],r13
    c253:	66 0f ef c0          	pxor   xmm0,xmm0
    c257:	48 8b 55 b0          	mov    rdx,QWORD PTR [rbp-0x50]
    c25b:	f3 0f 7f 42 10       	movdqu XMMWORD PTR [rdx+0x10],xmm0
    c260:	f3 0f 7f 02          	movdqu XMMWORD PTR [rdx],xmm0
    c264:	f3 0f 7f 42 20       	movdqu XMMWORD PTR [rdx+0x20],xmm0
    c269:	48 c7 42 30 00 00 00 	mov    QWORD PTR [rdx+0x30],0x0
    c270:	00
    c271:	c6 42 12 01          	mov    BYTE PTR [rdx+0x12],0x1
    c275:	44 88 62 11          	mov    BYTE PTR [rdx+0x11],r12b
    c279:	48 8b 4d 98          	mov    rcx,QWORD PTR [rbp-0x68]
    c27d:	48 89 4a 08          	mov    QWORD PTR [rdx+0x8],rcx
    c281:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    c285:	88 42 13             	mov    BYTE PTR [rdx+0x13],al
    c288:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    c28c:	48 89 42 28          	mov    QWORD PTR [rdx+0x28],rax
    c290:	44 88 7a 34          	mov    BYTE PTR [rdx+0x34],r15b
    c294:	4c 8d 6a 38          	lea    r13,[rdx+0x38]
    c298:	41 0f b6 df          	movzx  ebx,r15b
    c29c:	84 db                	test   bl,bl
    c29e:	48 89 5d a8          	mov    QWORD PTR [rbp-0x58],rbx
    c2a2:	4c 89 6d 90          	mov    QWORD PTR [rbp-0x70],r13
    c2a6:	74 4f                	je     c2f7 <zbtScoreLeafBuild+0x377>
    c2a8:	48 89 d8             	mov    rax,rbx
    c2ab:	48 0f af c1          	imul   rax,rcx
    c2af:	48 83 c0 07          	add    rax,0x7
    c2b3:	48 c1 e8 03          	shr    rax,0x3
    c2b7:	48 83 c0 09          	add    rax,0x9
    c2bb:	48 ba fe ff ff ff 3f 	movabs rdx,0x3ffffffffe
    c2c2:	00 00 00
    c2c5:	48 21 c2             	and    rdx,rax
    c2c8:	4c 89 ef             	mov    rdi,r13
    c2cb:	31 f6                	xor    esi,esi
    c2cd:	e8 de 4d ff ff       	call   10b0 <memset@plt>
    c2d2:	45 0f b6 f4          	movzx  r14d,r12b
    c2d6:	45 89 f7             	mov    r15d,r14d
    c2d9:	44 0f af fb          	imul   r15d,ebx
    c2dd:	41 83 c7 07          	add    r15d,0x7
    c2e1:	41 c1 ef 03          	shr    r15d,0x3
    c2e5:	41 83 c7 09          	add    r15d,0x9
    c2e9:	41 83 e7 fe          	and    r15d,0xfffffffe
    c2ed:	4b 8d 04 2f          	lea    rax,[r15+r13*1]
    c2f1:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    c2f5:	eb 0b                	jmp    c302 <zbtScoreLeafBuild+0x382>
    c2f7:	45 0f b6 f4          	movzx  r14d,r12b
    c2fb:	45 31 ff             	xor    r15d,r15d
    c2fe:	4c 89 6d 80          	mov    QWORD PTR [rbp-0x80],r13
    c302:	4d 89 e5             	mov    r13,r12
    c305:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c309:	4c 89 e7             	mov    rdi,r12
    c30c:	e8 df 53 00 00       	call   116f0 <zmalloc_usable_size>
    c311:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    c317:	bb ff 0f 00 00       	mov    ebx,0xfff
    c31c:	48 0f 42 d8          	cmovb  rbx,rax
    c320:	45 85 ed             	test   r13d,r13d
    c323:	0f 84 a1 02 00 00    	je     c5ca <zbtScoreLeafBuild+0x64a>
    c329:	4c 03 7d 90          	add    r15,QWORD PTR [rbp-0x70]
    c32d:	4b 8d 04 77          	lea    rax,[r15+r14*2]
    c331:	48 89 85 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],rax
    c338:	4c 01 e3             	add    rbx,r12
    c33b:	0f b6 45 d0          	movzx  eax,BYTE PTR [rbp-0x30]
    c33f:	48 89 85 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rax
    c346:	45 31 f6             	xor    r14d,r14d
    c349:	45 31 ed             	xor    r13d,r13d
    c34c:	49 89 db             	mov    r11,rbx
    c34f:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c353:	4c 8b 55 a8          	mov    r10,QWORD PTR [rbp-0x58]
    c357:	eb 3a                	jmp    c393 <zbtScoreLeafBuild+0x413>
    c359:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    c360:	49 c7 47 0d 00 00 00 	mov    QWORD PTR [r15+0xd],0x0
    c367:	00
    c368:	66 0f ef c0          	pxor   xmm0,xmm0
    c36c:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    c372:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c376:	41 c6 44 24 14 01    	mov    BYTE PTR [r12+0x14],0x1
    c37c:	4c 8b 7d 98          	mov    r15,QWORD PTR [rbp-0x68]
    c380:	49 ff c5             	inc    r13
    c383:	49 83 c0 28          	add    r8,0x28
    c387:	4d 01 d6             	add    r14,r10
    c38a:	4d 39 ef             	cmp    r15,r13
    c38d:	0f 84 37 02 00 00    	je     c5ca <zbtScoreLeafBuild+0x64a>
    c393:	48 c7 c0 eb ff ff ff 	mov    rax,0xffffffffffffffeb
    c39a:	49 83 78 18 00       	cmp    QWORD PTR [r8+0x18],0x0
    c39f:	74 1f                	je     c3c0 <zbtScoreLeafBuild+0x440>
    c3a1:	4c 8b 8d 78 ff ff ff 	mov    r9,QWORD PTR [rbp-0x88]
    c3a8:	48 be 00 00 00 00 00 	movabs rsi,0x8000000000000000
    c3af:	00 00 80
    c3b2:	8b 55 cc             	mov    edx,DWORD PTR [rbp-0x34]
    c3b5:	eb 49                	jmp    c400 <zbtScoreLeafBuild+0x480>
    c3b7:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    c3be:	00 00
    c3c0:	49 8b 48 08          	mov    rcx,QWORD PTR [r8+0x8]
    c3c4:	48 81 f9 3f 01 00 00 	cmp    rcx,0x13f
    c3cb:	4c 8b 8d 78 ff ff ff 	mov    r9,QWORD PTR [rbp-0x88]
    c3d2:	48 be 00 00 00 00 00 	movabs rsi,0x8000000000000000
    c3d9:	00 00 80
    c3dc:	8b 55 cc             	mov    edx,DWORD PTR [rbp-0x34]
    c3df:	77 1f                	ja     c400 <zbtScoreLeafBuild+0x480>
    c3e1:	48 81 f9 fe 00 00 00 	cmp    rcx,0xfe
    c3e8:	b8 00 00 00 00       	mov    eax,0x0
    c3ed:	48 19 c0             	sbb    rax,rax
    c3f0:	48 83 c8 fd          	or     rax,0xfffffffffffffffd
    c3f4:	48 29 c8             	sub    rax,rcx
    c3f7:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    c3fe:	00 00
    c400:	84 d2                	test   dl,dl
    c402:	74 6c                	je     c470 <zbtScoreLeafBuild+0x4f0>
    c404:	f3 43 0f 7e 04 e9    	movq   xmm0,QWORD PTR [r9+r13*8]
    c40a:	66 48 0f 7e c2       	movq   rdx,xmm0
    c40f:	48 85 d2             	test   rdx,rdx
    c412:	78 0c                	js     c420 <zbtScoreLeafBuild+0x4a0>
    c414:	48 09 f2             	or     rdx,rsi
    c417:	eb 0a                	jmp    c423 <zbtScoreLeafBuild+0x4a3>
    c419:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    c420:	48 f7 d2             	not    rdx
    c423:	48 2b 55 b8          	sub    rdx,QWORD PTR [rbp-0x48]
    c427:	48 8b 8d 60 ff ff ff 	mov    rcx,QWORD PTR [rbp-0xa0]
    c42e:	48 d3 ea             	shr    rdx,cl
    c431:	4c 89 f6             	mov    rsi,r14
    c434:	44 89 f1             	mov    ecx,r14d
    c437:	80 e1 07             	and    cl,0x7
    c43a:	48 89 d7             	mov    rdi,rdx
    c43d:	48 d3 e7             	shl    rdi,cl
    c440:	48 c1 ee 03          	shr    rsi,0x3
    c444:	48 8b 4d 90          	mov    rcx,QWORD PTR [rbp-0x70]
    c448:	48 09 3c 31          	or     QWORD PTR [rcx+rsi*1],rdi
    c44c:	44 89 f7             	mov    edi,r14d
    c44f:	83 e7 07             	and    edi,0x7
    c452:	74 1c                	je     c470 <zbtScoreLeafBuild+0x4f0>
    c454:	b9 40 00 00 00       	mov    ecx,0x40
    c459:	29 f9                	sub    ecx,edi
    c45b:	44 39 d1             	cmp    ecx,r10d
    c45e:	73 10                	jae    c470 <zbtScoreLeafBuild+0x4f0>
    c460:	48 d3 ea             	shr    rdx,cl
    c463:	48 8b 4d 90          	mov    rcx,QWORD PTR [rbp-0x70]
    c467:	08 54 31 08          	or     BYTE PTR [rcx+rsi*1+0x8],dl
    c46b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    c470:	49 01 c3             	add    r11,rax
    c473:	4c 89 db             	mov    rbx,r11
    c476:	4c 29 e3             	sub    rbx,r12
    c479:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c480:	4c 89 45 c0          	mov    QWORD PTR [rbp-0x40],r8
    c484:	4c 89 5d d0          	mov    QWORD PTR [rbp-0x30],r11
    c488:	7c 24                	jl     c4ae <zbtScoreLeafBuild+0x52e>
    c48a:	48 8d 3d 8d 71 00 00 	lea    rdi,[rip+0x718d]        # 1361e <_IO_stdin_used+0x61e>
    c491:	be 0a 04 00 00       	mov    esi,0x40a
    c496:	48 8d 15 72 73 00 00 	lea    rdx,[rip+0x7372]        # 1380f <_IO_stdin_used+0x80f>
    c49d:	e8 1e 52 00 00       	call   116c0 <standalone_panic>
    c4a2:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    c4a6:	4c 8b 55 a8          	mov    r10,QWORD PTR [rbp-0x58]
    c4aa:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c4ae:	4d 8d 60 18          	lea    r12,[r8+0x18]
    c4b2:	48 8b 45 80          	mov    rax,QWORD PTR [rbp-0x80]
    c4b6:	66 42 89 1c 68       	mov    WORD PTR [rax+r13*2],bx
    c4bb:	48 8b 85 50 ff ff ff 	mov    rax,QWORD PTR [rbp-0xb0]
    c4c2:	42 0f b6 04 28       	movzx  eax,BYTE PTR [rax+r13*1]
    c4c7:	48 8b 8d 58 ff ff ff 	mov    rcx,QWORD PTR [rbp-0xa8]
    c4ce:	42 88 04 29          	mov    BYTE PTR [rcx+r13*1],al
    c4d2:	4d 8b 3c 24          	mov    r15,QWORD PTR [r12]
    c4d6:	4d 85 ff             	test   r15,r15
    c4d9:	75 67                	jne    c542 <zbtScoreLeafBuild+0x5c2>
    c4db:	49 8b 50 08          	mov    rdx,QWORD PTR [r8+0x8]
    c4df:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    c4e6:	77 1c                	ja     c504 <zbtScoreLeafBuild+0x584>
    c4e8:	49 8b 30             	mov    rsi,QWORD PTR [r8]
    c4eb:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    c4f2:	0f 87 a2 00 00 00    	ja     c59a <zbtScoreLeafBuild+0x61a>
    c4f8:	bf 01 00 00 00       	mov    edi,0x1
    c4fd:	89 d0                	mov    eax,edx
    c4ff:	e9 a2 00 00 00       	jmp    c5a6 <zbtScoreLeafBuild+0x626>
    c504:	48 89 d7             	mov    rdi,rdx
    c507:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    c50b:	e8 b0 52 00 00       	call   117c0 <zmalloc_usable>
    c510:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    c514:	48 8b 55 88          	mov    rdx,QWORD PTR [rbp-0x78]
    c518:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    c51c:	49 89 c7             	mov    r15,rax
    c51f:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c523:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    c526:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c52a:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    c52e:	4c 89 ff             	mov    rdi,r15
    c531:	e8 ea 4b ff ff       	call   1120 <memcpy@plt>
    c536:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    c53a:	4c 8b 55 a8          	mov    r10,QWORD PTR [rbp-0x58]
    c53e:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c542:	49 8b 40 08          	mov    rax,QWORD PTR [r8+0x8]
    c546:	41 c6 03 ff          	mov    BYTE PTR [r11],0xff
    c54a:	41 8b 48 10          	mov    ecx,DWORD PTR [r8+0x10]
    c54e:	41 89 4b 01          	mov    DWORD PTR [r11+0x1],ecx
    c552:	49 89 43 05          	mov    QWORD PTR [r11+0x5],rax
    c556:	4d 89 7b 0d          	mov    QWORD PTR [r11+0xd],r15
    c55a:	4d 8b 78 20          	mov    r15,QWORD PTR [r8+0x20]
    c55e:	4d 85 ff             	test   r15,r15
    c561:	0f 84 01 fe ff ff    	je     c368 <zbtScoreLeafBuild+0x3e8>
    c567:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    c56b:	0f 84 ef fd ff ff    	je     c360 <zbtScoreLeafBuild+0x3e0>
    c571:	48 8d 3d a6 70 00 00 	lea    rdi,[rip+0x70a6]        # 1361e <_IO_stdin_used+0x61e>
    c578:	be 45 02 00 00       	mov    esi,0x245
    c57d:	48 8d 15 d2 71 00 00 	lea    rdx,[rip+0x71d2]        # 13756 <_IO_stdin_used+0x756>
    c584:	e8 37 51 00 00       	call   116c0 <standalone_panic>
    c589:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    c58d:	4c 8b 55 a8          	mov    r10,QWORD PTR [rbp-0x58]
    c591:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c595:	e9 c6 fd ff ff       	jmp    c360 <zbtScoreLeafBuild+0x3e0>
    c59a:	66 41 89 53 01       	mov    WORD PTR [r11+0x1],dx
    c59f:	bf 03 00 00 00       	mov    edi,0x3
    c5a4:	b0 fe                	mov    al,0xfe
    c5a6:	4c 8b 7d 98          	mov    r15,QWORD PTR [rbp-0x68]
    c5aa:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c5ae:	41 88 03             	mov    BYTE PTR [r11],al
    c5b1:	4c 01 df             	add    rdi,r11
    c5b4:	e8 67 4b ff ff       	call   1120 <memcpy@plt>
    c5b9:	4c 8b 5d d0          	mov    r11,QWORD PTR [rbp-0x30]
    c5bd:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c5c1:	4c 8b 55 a8          	mov    r10,QWORD PTR [rbp-0x58]
    c5c5:	e9 b6 fd ff ff       	jmp    c380 <zbtScoreLeafBuild+0x400>
    c5ca:	66 41 89 5c 24 36    	mov    WORD PTR [r12+0x36],bx
    c5d0:	4c 8b b5 68 ff ff ff 	mov    r14,QWORD PTR [rbp-0x98]
    c5d7:	41 83 fe ff          	cmp    r14d,0xffffffff
    c5db:	4c 8b 7d 88          	mov    r15,QWORD PTR [rbp-0x78]
    c5df:	74 25                	je     c606 <zbtScoreLeafBuild+0x686>
    c5e1:	45 89 74 24 30       	mov    DWORD PTR [r12+0x30],r14d
    c5e6:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c5ea:	44 89 f1             	mov    ecx,r14d
    c5ed:	4c 89 24 c8          	mov    QWORD PTR [rax+rcx*8],r12
    c5f1:	4c 89 e0             	mov    rax,r12
    c5f4:	48 81 c4 88 00 00 00 	add    rsp,0x88
    c5fb:	5b                   	pop    rbx
    c5fc:	41 5c                	pop    r12
    c5fe:	41 5d                	pop    r13
    c600:	41 5e                	pop    r14
    c602:	41 5f                	pop    r15
    c604:	5d                   	pop    rbp
    c605:	c3                   	ret
    c606:	45 8b 77 58          	mov    r14d,DWORD PTR [r15+0x58]
    c60a:	45 85 f6             	test   r14d,r14d
    c60d:	74 07                	je     c616 <zbtScoreLeafBuild+0x696>
    c60f:	49 83 7f 40 00       	cmp    QWORD PTR [r15+0x40],0x0
    c614:	74 7b                	je     c691 <zbtScoreLeafBuild+0x711>
    c616:	45 8b 77 54          	mov    r14d,DWORD PTR [r15+0x54]
    c61a:	41 8d 46 01          	lea    eax,[r14+0x1]
    c61e:	41 89 47 54          	mov    DWORD PTR [r15+0x54],eax
    c622:	45 3b 77 50          	cmp    r14d,DWORD PTR [r15+0x50]
    c626:	75 b9                	jne    c5e1 <zbtScoreLeafBuild+0x661>
    c628:	43 8d 04 36          	lea    eax,[r14+r14*1]
    c62c:	45 85 f6             	test   r14d,r14d
    c62f:	bb 10 00 00 00       	mov    ebx,0x10
    c634:	0f 45 d8             	cmovne ebx,eax
    c637:	48 c7 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],0x0
    c63e:	00 00 00 00
    c642:	49 8b 7f 48          	mov    rdi,QWORD PTR [r15+0x48]
    c646:	48 8d 34 dd 00 00 00 	lea    rsi,[rbx*8+0x0]
    c64d:	00
    c64e:	48 8d 55 a0          	lea    rdx,[rbp-0x60]
    c652:	48 8d 8d 70 ff ff ff 	lea    rcx,[rbp-0x90]
    c659:	e8 d2 51 00 00       	call   11830 <zrealloc_usable>
    c65e:	49 89 47 48          	mov    QWORD PTR [r15+0x48],rax
    c662:	41 8b 4f 50          	mov    ecx,DWORD PTR [r15+0x50]
    c666:	48 8d 3c c8          	lea    rdi,[rax+rcx*8]
    c66a:	89 da                	mov    edx,ebx
    c66c:	29 ca                	sub    edx,ecx
    c66e:	48 c1 e2 03          	shl    rdx,0x3
    c672:	31 f6                	xor    esi,esi
    c674:	e8 37 4a ff ff       	call   10b0 <memset@plt>
    c679:	41 89 5f 50          	mov    DWORD PTR [r15+0x50],ebx
    c67d:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    c681:	48 2b 85 70 ff ff ff 	sub    rax,QWORD PTR [rbp-0x90]
    c688:	49 01 47 68          	add    QWORD PTR [r15+0x68],rax
    c68c:	e9 50 ff ff ff       	jmp    c5e1 <zbtScoreLeafBuild+0x661>
    c691:	41 ff ce             	dec    r14d
    c694:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c698:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c69c:	a8 01                	test   al,0x1
    c69e:	75 20                	jne    c6c0 <zbtScoreLeafBuild+0x740>
    c6a0:	48 8d 3d 77 6f 00 00 	lea    rdi,[rip+0x6f77]        # 1361e <_IO_stdin_used+0x61e>
    c6a7:	48 8d 15 98 71 00 00 	lea    rdx,[rip+0x7198]        # 13846 <_IO_stdin_used+0x846>
    c6ae:	be 25 03 00 00       	mov    esi,0x325
    c6b3:	e8 08 50 00 00       	call   116c0 <standalone_panic>
    c6b8:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c6bc:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c6c0:	48 d1 e8             	shr    rax,1
    c6c3:	41 89 47 58          	mov    DWORD PTR [r15+0x58],eax
    c6c7:	e9 15 ff ff ff       	jmp    c5e1 <zbtScoreLeafBuild+0x661>

Disassembly of section .fini:
