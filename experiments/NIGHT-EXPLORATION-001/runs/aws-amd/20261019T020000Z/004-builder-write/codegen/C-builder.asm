
scratch/amd-builder-build/C/build/native/btree-bench:     file format elf64-x86-64


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
    bf8d:	48 83 ec 68          	sub    rsp,0x68
    bf91:	4c 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],r8
    bf98:	49 89 c8             	mov    r8,rcx
    bf9b:	49 89 d7             	mov    r15,rdx
    bf9e:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    bfa2:	f3 0f 7e 02          	movq   xmm0,QWORD PTR [rdx]
    bfa6:	66 48 0f 7e c0       	movq   rax,xmm0
    bfab:	49 bc 00 00 00 00 00 	movabs r12,0x8000000000000000
    bfb2:	00 00 80
    bfb5:	48 89 c3             	mov    rbx,rax
    bfb8:	48 85 c0             	test   rax,rax
    bfbb:	0f 88 9d 00 00 00    	js     c05e <zbtScoreLeafBuild+0xde>
    bfc1:	4c 09 e3             	or     rbx,r12
    bfc4:	41 89 f5             	mov    r13d,esi
    bfc7:	83 fe 02             	cmp    esi,0x2
    bfca:	0f 82 9d 00 00 00    	jb     c06d <zbtScoreLeafBuild+0xed>
    bfd0:	4d 89 c3             	mov    r11,r8
    bfd3:	bf 01 00 00 00       	mov    edi,0x1
    bfd8:	31 c9                	xor    ecx,ecx
    bfda:	48 89 da             	mov    rdx,rbx
    bfdd:	49 89 de             	mov    r14,rbx
    bfe0:	eb 30                	jmp    c012 <zbtScoreLeafBuild+0x92>
    bfe2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    bfe9:	1f 84 00 00 00 00 00
    bff0:	4d 09 e0             	or     r8,r12
    bff3:	4d 89 c2             	mov    r10,r8
    bff6:	49 31 da             	xor    r10,rbx
    bff9:	4c 09 d1             	or     rcx,r10
    bffc:	49 39 d0             	cmp    r8,rdx
    bfff:	49 0f 42 d0          	cmovb  rdx,r8
    c003:	4d 39 f0             	cmp    r8,r14
    c006:	4d 0f 47 f0          	cmova  r14,r8
    c00a:	48 ff c7             	inc    rdi
    c00d:	49 39 fd             	cmp    r13,rdi
    c010:	74 15                	je     c027 <zbtScoreLeafBuild+0xa7>
    c012:	f3 41 0f 7e 04 ff    	movq   xmm0,QWORD PTR [r15+rdi*8]
    c018:	66 49 0f 7e c0       	movq   r8,xmm0
    c01d:	4d 85 c0             	test   r8,r8
    c020:	79 ce                	jns    bff0 <zbtScoreLeafBuild+0x70>
    c022:	49 f7 d0             	not    r8
    c025:	eb cc                	jmp    bff3 <zbtScoreLeafBuild+0x73>
    c027:	45 31 c0             	xor    r8d,r8d
    c02a:	48 85 c9             	test   rcx,rcx
    c02d:	74 55                	je     c084 <zbtScoreLeafBuild+0x104>
    c02f:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c034:	49 29 d6             	sub    r14,rdx
    c037:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    c03b:	49 d3 ee             	shr    r14,cl
    c03e:	49 0f bd ce          	bsr    rcx,r14
    c042:	83 f1 3f             	xor    ecx,0x3f
    c045:	40 b7 40             	mov    dil,0x40
    c048:	40 28 cf             	sub    dil,cl
    c04b:	4d 85 f6             	test   r14,r14
    c04e:	40 0f b6 cf          	movzx  ecx,dil
    c052:	41 0f 44 c8          	cmove  ecx,r8d
    c056:	48 89 d3             	mov    rbx,rdx
    c059:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    c05c:	eb 36                	jmp    c094 <zbtScoreLeafBuild+0x114>
    c05e:	48 f7 d3             	not    rbx
    c061:	41 89 f5             	mov    r13d,esi
    c064:	83 fe 02             	cmp    esi,0x2
    c067:	0f 83 63 ff ff ff    	jae    bfd0 <zbtScoreLeafBuild+0x50>
    c06d:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    c074:	31 c9                	xor    ecx,ecx
    c076:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    c07a:	48 85 c0             	test   rax,rax
    c07d:	79 1d                	jns    c09c <zbtScoreLeafBuild+0x11c>
    c07f:	48 f7 d0             	not    rax
    c082:	eb 1b                	jmp    c09f <zbtScoreLeafBuild+0x11f>
    c084:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    c08b:	48 89 d3             	mov    rbx,rdx
    c08e:	31 c9                	xor    ecx,ecx
    c090:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    c094:	4d 89 d8             	mov    r8,r11
    c097:	48 85 c0             	test   rax,rax
    c09a:	78 e3                	js     c07f <zbtScoreLeafBuild+0xff>
    c09c:	4c 09 e0             	or     rax,r12
    c09f:	ba 38 00 00 00       	mov    edx,0x38
    c0a4:	48 89 75 d0          	mov    QWORD PTR [rbp-0x30],rsi
    c0a8:	83 fe 02             	cmp    esi,0x2
    c0ab:	4c 89 4d 80          	mov    QWORD PTR [rbp-0x80],r9
    c0af:	0f 82 a1 00 00 00    	jb     c156 <zbtScoreLeafBuild+0x1d6>
    c0b5:	4d 89 c6             	mov    r14,r8
    c0b8:	41 b8 01 00 00 00    	mov    r8d,0x1
    c0be:	31 c9                	xor    ecx,ecx
    c0c0:	48 89 c7             	mov    rdi,rax
    c0c3:	48 89 c6             	mov    rsi,rax
    c0c6:	eb 34                	jmp    c0fc <zbtScoreLeafBuild+0x17c>
    c0c8:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    c0cf:	00
    c0d0:	49 ba 00 00 00 00 00 	movabs r10,0x8000000000000000
    c0d7:	00 00 80
    c0da:	4d 09 d3             	or     r11,r10
    c0dd:	4d 89 da             	mov    r10,r11
    c0e0:	49 31 c2             	xor    r10,rax
    c0e3:	4c 09 d1             	or     rcx,r10
    c0e6:	49 39 fb             	cmp    r11,rdi
    c0e9:	49 0f 42 fb          	cmovb  rdi,r11
    c0ed:	49 39 f3             	cmp    r11,rsi
    c0f0:	49 0f 47 f3          	cmova  rsi,r11
    c0f4:	49 ff c0             	inc    r8
    c0f7:	4d 39 c5             	cmp    r13,r8
    c0fa:	74 15                	je     c111 <zbtScoreLeafBuild+0x191>
    c0fc:	f3 43 0f 7e 04 c7    	movq   xmm0,QWORD PTR [r15+r8*8]
    c102:	66 49 0f 7e c3       	movq   r11,xmm0
    c107:	4d 85 db             	test   r11,r11
    c10a:	79 c4                	jns    c0d0 <zbtScoreLeafBuild+0x150>
    c10c:	49 f7 d3             	not    r11
    c10f:	eb cc                	jmp    c0dd <zbtScoreLeafBuild+0x15d>
    c111:	48 85 c9             	test   rcx,rcx
    c114:	4d 89 f0             	mov    r8,r14
    c117:	74 3d                	je     c156 <zbtScoreLeafBuild+0x1d6>
    c119:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c11e:	48 29 fe             	sub    rsi,rdi
    c121:	48 d3 ee             	shr    rsi,cl
    c124:	48 85 f6             	test   rsi,rsi
    c127:	74 2d                	je     c156 <zbtScoreLeafBuild+0x1d6>
    c129:	48 0f bd c6          	bsr    rax,rsi
    c12d:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    c131:	48 83 c0 41          	add    rax,0x41
    c135:	49 0f af c5          	imul   rax,r13
    c139:	48 83 c0 07          	add    rax,0x7
    c13d:	48 c1 e8 03          	shr    rax,0x3
    c141:	48 83 c0 09          	add    rax,0x9
    c145:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    c14c:	ff ff 1f
    c14f:	48 21 c2             	and    rdx,rax
    c152:	48 83 c2 38          	add    rdx,0x38
    c156:	8b 45 10             	mov    eax,DWORD PTR [rbp+0x10]
    c159:	4e 8d 34 6d 00 00 00 	lea    r14,[r13*2+0x0]
    c160:	00
    c161:	4d 01 ee             	add    r14,r13
    c164:	49 01 d6             	add    r14,rdx
    c167:	83 7d d0 00          	cmp    DWORD PTR [rbp-0x30],0x0
    c16b:	74 50                	je     c1bd <zbtScoreLeafBuild+0x23d>
    c16d:	4a 8d 0c ed 00 00 00 	lea    rcx,[r13*8+0x0]
    c174:	00
    c175:	48 8d 0c 89          	lea    rcx,[rcx+rcx*4]
    c179:	31 d2                	xor    edx,edx
    c17b:	eb 0f                	jmp    c18c <zbtScoreLeafBuild+0x20c>
    c17d:	0f 1f 00             	nop    DWORD PTR [rax]
    c180:	49 01 f6             	add    r14,rsi
    c183:	48 83 c2 28          	add    rdx,0x28
    c187:	48 39 d1             	cmp    rcx,rdx
    c18a:	74 31                	je     c1bd <zbtScoreLeafBuild+0x23d>
    c18c:	be 15 00 00 00       	mov    esi,0x15
    c191:	49 83 7c 10 18 00    	cmp    QWORD PTR [r8+rdx*1+0x18],0x0
    c197:	75 e7                	jne    c180 <zbtScoreLeafBuild+0x200>
    c199:	49 8b 7c 10 08       	mov    rdi,QWORD PTR [r8+rdx*1+0x8]
    c19e:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    c1a5:	77 d9                	ja     c180 <zbtScoreLeafBuild+0x200>
    c1a7:	31 f6                	xor    esi,esi
    c1a9:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    c1b0:	40 0f 93 c6          	setae  sil
    c1b4:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    c1b8:	48 ff c6             	inc    rsi
    c1bb:	eb c3                	jmp    c180 <zbtScoreLeafBuild+0x200>
    c1bd:	4c 89 45 88          	mov    QWORD PTR [rbp-0x78],r8
    c1c1:	85 c0                	test   eax,eax
    c1c3:	74 0e                	je     c1d3 <zbtScoreLeafBuild+0x253>
    c1c5:	bf ff 0f 00 00       	mov    edi,0xfff
    c1ca:	49 81 fe 00 10 00 00 	cmp    r14,0x1000
    c1d1:	72 29                	jb     c1fc <zbtScoreLeafBuild+0x27c>
    c1d3:	4c 89 f7             	mov    rdi,r14
    c1d6:	83 7d d0 5f          	cmp    DWORD PTR [rbp-0x30],0x5f
    c1da:	77 20                	ja     c1fc <zbtScoreLeafBuild+0x27c>
    c1dc:	4c 89 f7             	mov    rdi,r14
    c1df:	49 81 fe ff 0f 00 00 	cmp    r14,0xfff
    c1e6:	77 14                	ja     c1fc <zbtScoreLeafBuild+0x27c>
    c1e8:	49 81 fe 7f 0f 00 00 	cmp    r14,0xf7f
    c1ef:	bf 7f 0f 00 00       	mov    edi,0xf7f
    c1f4:	49 0f 42 fe          	cmovb  rdi,r14
    c1f8:	48 83 ef 80          	sub    rdi,0xffffffffffffff80
    c1fc:	48 8d 75 b8          	lea    rsi,[rbp-0x48]
    c200:	e8 cb 55 00 00       	call   117d0 <zmalloc_usable>
    c205:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    c209:	48 8b 55 b0          	mov    rdx,QWORD PTR [rbp-0x50]
    c20d:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    c211:	49 89 c4             	mov    r12,rax
    c214:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    c218:	ff c8                	dec    eax
    c21a:	83 f8 60             	cmp    eax,0x60
    c21d:	72 18                	jb     c237 <zbtScoreLeafBuild+0x2b7>
    c21f:	48 8d 3d f8 73 00 00 	lea    rdi,[rip+0x73f8]        # 1361e <_IO_stdin_used+0x61e>
    c226:	48 8d 15 99 75 00 00 	lea    rdx,[rip+0x7599]        # 137c6 <_IO_stdin_used+0x7c6>
    c22d:	be de 03 00 00       	mov    esi,0x3de
    c232:	e8 99 54 00 00       	call   116d0 <standalone_panic>
    c237:	49 81 fe 00 10 00 00 	cmp    r14,0x1000
    c23e:	72 18                	jb     c258 <zbtScoreLeafBuild+0x2d8>
    c240:	48 8d 3d d7 73 00 00 	lea    rdi,[rip+0x73d7]        # 1361e <_IO_stdin_used+0x61e>
    c247:	48 8d 15 a1 75 00 00 	lea    rdx,[rip+0x75a1]        # 137ef <_IO_stdin_used+0x7ef>
    c24e:	be df 03 00 00       	mov    esi,0x3df
    c253:	e8 78 54 00 00       	call   116d0 <standalone_panic>
    c258:	66 0f ef c0          	pxor   xmm0,xmm0
    c25c:	f3 41 0f 7f 44 24 10 	movdqu XMMWORD PTR [r12+0x10],xmm0
    c263:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    c269:	f3 41 0f 7f 44 24 20 	movdqu XMMWORD PTR [r12+0x20],xmm0
    c270:	49 c7 44 24 30 00 00 	mov    QWORD PTR [r12+0x30],0x0
    c277:	00 00
    c279:	41 c6 44 24 12 01    	mov    BYTE PTR [r12+0x12],0x1
    c27f:	4c 8b 75 d0          	mov    r14,QWORD PTR [rbp-0x30]
    c283:	45 88 74 24 11       	mov    BYTE PTR [r12+0x11],r14b
    c288:	4d 89 6c 24 08       	mov    QWORD PTR [r12+0x8],r13
    c28d:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    c291:	41 88 44 24 13       	mov    BYTE PTR [r12+0x13],al
    c296:	49 89 5c 24 28       	mov    QWORD PTR [r12+0x28],rbx
    c29b:	8b 45 c0             	mov    eax,DWORD PTR [rbp-0x40]
    c29e:	41 88 44 24 34       	mov    BYTE PTR [r12+0x34],al
    c2a3:	49 8d 5c 24 38       	lea    rbx,[r12+0x38]
    c2a8:	84 c0                	test   al,al
    c2aa:	4c 89 6d 98          	mov    QWORD PTR [rbp-0x68],r13
    c2ae:	74 62                	je     c312 <zbtScoreLeafBuild+0x392>
    c2b0:	44 0f b6 f0          	movzx  r14d,al
    c2b4:	4c 89 f0             	mov    rax,r14
    c2b7:	49 0f af c5          	imul   rax,r13
    c2bb:	48 83 c0 07          	add    rax,0x7
    c2bf:	48 c1 e8 03          	shr    rax,0x3
    c2c3:	48 83 c0 09          	add    rax,0x9
    c2c7:	48 ba fe ff ff ff 3f 	movabs rdx,0x3ffffffffe
    c2ce:	00 00 00
    c2d1:	48 21 c2             	and    rdx,rax
    c2d4:	48 89 df             	mov    rdi,rbx
    c2d7:	31 f6                	xor    esi,esi
    c2d9:	e8 d2 4d ff ff       	call   10b0 <memset@plt>
    c2de:	0f b6 4d d0          	movzx  ecx,BYTE PTR [rbp-0x30]
    c2e2:	48 89 c8             	mov    rax,rcx
    c2e5:	48 89 4d a0          	mov    QWORD PTR [rbp-0x60],rcx
    c2e9:	44 0f af f1          	imul   r14d,ecx
    c2ed:	41 83 c6 07          	add    r14d,0x7
    c2f1:	41 c1 ee 03          	shr    r14d,0x3
    c2f5:	41 83 c6 09          	add    r14d,0x9
    c2f9:	41 83 e6 fe          	and    r14d,0xfffffffe
    c2fd:	49 89 dd             	mov    r13,rbx
    c300:	4c 89 75 c8          	mov    QWORD PTR [rbp-0x38],r14
    c304:	4a 8d 04 33          	lea    rax,[rbx+r14*1]
    c308:	4c 8b 75 d0          	mov    r14,QWORD PTR [rbp-0x30]
    c30c:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
    c310:	eb 15                	jmp    c327 <zbtScoreLeafBuild+0x3a7>
    c312:	41 0f b6 c6          	movzx  eax,r14b
    c316:	48 89 45 a0          	mov    QWORD PTR [rbp-0x60],rax
    c31a:	31 c0                	xor    eax,eax
    c31c:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    c320:	49 89 dd             	mov    r13,rbx
    c323:	48 89 5d c0          	mov    QWORD PTR [rbp-0x40],rbx
    c327:	4c 89 e7             	mov    rdi,r12
    c32a:	e8 d1 53 00 00       	call   11700 <zmalloc_usable_size>
    c32f:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    c335:	bb ff 0f 00 00       	mov    ebx,0xfff
    c33a:	48 0f 42 d8          	cmovb  rbx,rax
    c33e:	45 85 f6             	test   r14d,r14d
    c341:	0f 84 9e 02 00 00    	je     c5e5 <zbtScoreLeafBuild+0x665>
    c347:	41 0f b6 44 24 34    	movzx  eax,BYTE PTR [r12+0x34]
    c34d:	85 c0                	test   eax,eax
    c34f:	0f 84 c9 00 00 00    	je     c41e <zbtScoreLeafBuild+0x49e>
    c355:	89 c2                	mov    edx,eax
    c357:	31 f6                	xor    esi,esi
    c359:	bf ff ff ff ff       	mov    edi,0xffffffff
    c35e:	eb 0d                	jmp    c36d <zbtScoreLeafBuild+0x3ed>
    c360:	48 ff c6             	inc    rsi
    c363:	48 39 75 98          	cmp    QWORD PTR [rbp-0x68],rsi
    c367:	0f 84 a8 00 00 00    	je     c415 <zbtScoreLeafBuild+0x495>
    c36d:	f3 41 0f 7e 04 f7    	movq   xmm0,QWORD PTR [r15+rsi*8]
    c373:	66 49 0f 7e c0       	movq   r8,xmm0
    c378:	4d 85 c0             	test   r8,r8
    c37b:	78 33                	js     c3b0 <zbtScoreLeafBuild+0x430>
    c37d:	48 b9 00 00 00 00 00 	movabs rcx,0x8000000000000000
    c384:	00 00 80
    c387:	49 09 c8             	or     r8,rcx
    c38a:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    c390:	49 8b 4c 24 28       	mov    rcx,QWORD PTR [r12+0x28]
    c395:	74 29                	je     c3c0 <zbtScoreLeafBuild+0x440>
    c397:	4c 29 c1             	sub    rcx,r8
    c39a:	45 0f b6 44 24 11    	movzx  r8d,BYTE PTR [r12+0x11]
    c3a0:	49 89 f1             	mov    r9,rsi
    c3a3:	49 31 f9             	xor    r9,rdi
    c3a6:	4d 01 c1             	add    r9,r8
    c3a9:	49 89 c8             	mov    r8,rcx
    c3ac:	eb 18                	jmp    c3c6 <zbtScoreLeafBuild+0x446>
    c3ae:	66 90                	xchg   ax,ax
    c3b0:	49 f7 d0             	not    r8
    c3b3:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    c3b9:	49 8b 4c 24 28       	mov    rcx,QWORD PTR [r12+0x28]
    c3be:	75 d7                	jne    c397 <zbtScoreLeafBuild+0x417>
    c3c0:	49 29 c8             	sub    r8,rcx
    c3c3:	49 89 f1             	mov    r9,rsi
    c3c6:	41 0f b6 4c 24 13    	movzx  ecx,BYTE PTR [r12+0x13]
    c3cc:	49 d3 e8             	shr    r8,cl
    c3cf:	45 89 ca             	mov    r10d,r9d
    c3d2:	4c 0f af d2          	imul   r10,rdx
    c3d6:	4d 89 d1             	mov    r9,r10
    c3d9:	49 c1 e9 03          	shr    r9,0x3
    c3dd:	44 89 d1             	mov    ecx,r10d
    c3e0:	80 e1 07             	and    cl,0x7
    c3e3:	4d 89 c3             	mov    r11,r8
    c3e6:	49 d3 e3             	shl    r11,cl
    c3e9:	4f 09 5c 0d 00       	or     QWORD PTR [r13+r9*1+0x0],r11
    c3ee:	41 83 e2 07          	and    r10d,0x7
    c3f2:	0f 84 68 ff ff ff    	je     c360 <zbtScoreLeafBuild+0x3e0>
    c3f8:	b9 40 00 00 00       	mov    ecx,0x40
    c3fd:	44 29 d1             	sub    ecx,r10d
    c400:	39 c1                	cmp    ecx,eax
    c402:	0f 83 58 ff ff ff    	jae    c360 <zbtScoreLeafBuild+0x3e0>
    c408:	49 d3 e8             	shr    r8,cl
    c40b:	47 08 44 21 40       	or     BYTE PTR [r9+r12*1+0x40],r8b
    c410:	e9 4b ff ff ff       	jmp    c360 <zbtScoreLeafBuild+0x3e0>
    c415:	45 85 f6             	test   r14d,r14d
    c418:	0f 84 c7 01 00 00    	je     c5e5 <zbtScoreLeafBuild+0x665>
    c41e:	4c 03 6d c8          	add    r13,QWORD PTR [rbp-0x38]
    c422:	4c 01 e3             	add    rbx,r12
    c425:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    c429:	48 8d 04 45 00 00 00 	lea    rax,[rax*2+0x0]
    c430:	00
    c431:	4c 01 e8             	add    rax,r13
    c434:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    c438:	45 31 ed             	xor    r13d,r13d
    c43b:	48 8b 75 88          	mov    rsi,QWORD PTR [rbp-0x78]
    c43f:	4c 89 65 a8          	mov    QWORD PTR [rbp-0x58],r12
    c443:	eb 3c                	jmp    c481 <zbtScoreLeafBuild+0x501>
    c445:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    c44c:	00 00 00 00
    c450:	49 c7 47 0d 00 00 00 	mov    QWORD PTR [r15+0xd],0x0
    c457:	00
    c458:	66 0f ef c0          	pxor   xmm0,xmm0
    c45c:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    c462:	4c 8b 65 a8          	mov    r12,QWORD PTR [rbp-0x58]
    c466:	41 c6 44 24 14 01    	mov    BYTE PTR [r12+0x14],0x1
    c46c:	4c 8b 7d d0          	mov    r15,QWORD PTR [rbp-0x30]
    c470:	49 ff c5             	inc    r13
    c473:	48 83 c6 28          	add    rsi,0x28
    c477:	4c 39 6d 98          	cmp    QWORD PTR [rbp-0x68],r13
    c47b:	0f 84 67 01 00 00    	je     c5e8 <zbtScoreLeafBuild+0x668>
    c481:	48 c7 c0 eb ff ff ff 	mov    rax,0xffffffffffffffeb
    c488:	48 83 7e 18 00       	cmp    QWORD PTR [rsi+0x18],0x0
    c48d:	75 31                	jne    c4c0 <zbtScoreLeafBuild+0x540>
    c48f:	48 8b 4e 08          	mov    rcx,QWORD PTR [rsi+0x8]
    c493:	48 81 f9 3f 01 00 00 	cmp    rcx,0x13f
    c49a:	77 24                	ja     c4c0 <zbtScoreLeafBuild+0x540>
    c49c:	48 81 f9 fe 00 00 00 	cmp    rcx,0xfe
    c4a3:	b8 00 00 00 00       	mov    eax,0x0
    c4a8:	48 19 c0             	sbb    rax,rax
    c4ab:	48 83 c8 fd          	or     rax,0xfffffffffffffffd
    c4af:	48 29 c8             	sub    rax,rcx
    c4b2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c4b9:	1f 84 00 00 00 00 00
    c4c0:	48 01 c3             	add    rbx,rax
    c4c3:	49 89 df             	mov    r15,rbx
    c4c6:	4d 29 e7             	sub    r15,r12
    c4c9:	49 81 ff 00 10 00 00 	cmp    r15,0x1000
    c4d0:	49 89 f6             	mov    r14,rsi
    c4d3:	7c 1b                	jl     c4f0 <zbtScoreLeafBuild+0x570>
    c4d5:	48 8d 3d 42 71 00 00 	lea    rdi,[rip+0x7142]        # 1361e <_IO_stdin_used+0x61e>
    c4dc:	be fa 03 00 00       	mov    esi,0x3fa
    c4e1:	48 8d 15 27 73 00 00 	lea    rdx,[rip+0x7327]        # 1380f <_IO_stdin_used+0x80f>
    c4e8:	e8 e3 51 00 00       	call   116d0 <standalone_panic>
    c4ed:	4c 89 f6             	mov    rsi,r14
    c4f0:	4c 8d 66 18          	lea    r12,[rsi+0x18]
    c4f4:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c4f8:	4c 89 7d d0          	mov    QWORD PTR [rbp-0x30],r15
    c4fc:	66 46 89 3c 68       	mov    WORD PTR [rax+r13*2],r15w
    c501:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
    c508:	42 0f b6 04 28       	movzx  eax,BYTE PTR [rax+r13*1]
    c50d:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    c511:	42 88 04 29          	mov    BYTE PTR [rcx+r13*1],al
    c515:	4d 8b 3c 24          	mov    r15,QWORD PTR [r12]
    c519:	4d 85 ff             	test   r15,r15
    c51c:	75 56                	jne    c574 <zbtScoreLeafBuild+0x5f4>
    c51e:	48 8b 56 08          	mov    rdx,QWORD PTR [rsi+0x8]
    c522:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    c529:	77 1c                	ja     c547 <zbtScoreLeafBuild+0x5c7>
    c52b:	48 8b 36             	mov    rsi,QWORD PTR [rsi]
    c52e:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    c535:	0f 87 85 00 00 00    	ja     c5c0 <zbtScoreLeafBuild+0x640>
    c53b:	bf 01 00 00 00       	mov    edi,0x1
    c540:	89 d0                	mov    eax,edx
    c542:	e9 84 00 00 00       	jmp    c5cb <zbtScoreLeafBuild+0x64b>
    c547:	48 89 d7             	mov    rdi,rdx
    c54a:	48 8d 75 b8          	lea    rsi,[rbp-0x48]
    c54e:	e8 7d 52 00 00       	call   117d0 <zmalloc_usable>
    c553:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    c557:	48 8b 55 b0          	mov    rdx,QWORD PTR [rbp-0x50]
    c55b:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    c55f:	49 89 c7             	mov    r15,rax
    c562:	49 8b 36             	mov    rsi,QWORD PTR [r14]
    c565:	49 8b 56 08          	mov    rdx,QWORD PTR [r14+0x8]
    c569:	48 89 c7             	mov    rdi,rax
    c56c:	e8 af 4b ff ff       	call   1120 <memcpy@plt>
    c571:	4c 89 f6             	mov    rsi,r14
    c574:	48 8b 46 08          	mov    rax,QWORD PTR [rsi+0x8]
    c578:	c6 03 ff             	mov    BYTE PTR [rbx],0xff
    c57b:	8b 4e 10             	mov    ecx,DWORD PTR [rsi+0x10]
    c57e:	89 4b 01             	mov    DWORD PTR [rbx+0x1],ecx
    c581:	48 89 43 05          	mov    QWORD PTR [rbx+0x5],rax
    c585:	4c 89 7b 0d          	mov    QWORD PTR [rbx+0xd],r15
    c589:	4c 8b 7e 20          	mov    r15,QWORD PTR [rsi+0x20]
    c58d:	4d 85 ff             	test   r15,r15
    c590:	0f 84 c2 fe ff ff    	je     c458 <zbtScoreLeafBuild+0x4d8>
    c596:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    c59a:	0f 84 b0 fe ff ff    	je     c450 <zbtScoreLeafBuild+0x4d0>
    c5a0:	48 8d 3d 77 70 00 00 	lea    rdi,[rip+0x7077]        # 1361e <_IO_stdin_used+0x61e>
    c5a7:	be 45 02 00 00       	mov    esi,0x245
    c5ac:	48 8d 15 a3 71 00 00 	lea    rdx,[rip+0x71a3]        # 13756 <_IO_stdin_used+0x756>
    c5b3:	e8 18 51 00 00       	call   116d0 <standalone_panic>
    c5b8:	4c 89 f6             	mov    rsi,r14
    c5bb:	e9 90 fe ff ff       	jmp    c450 <zbtScoreLeafBuild+0x4d0>
    c5c0:	66 89 53 01          	mov    WORD PTR [rbx+0x1],dx
    c5c4:	bf 03 00 00 00       	mov    edi,0x3
    c5c9:	b0 fe                	mov    al,0xfe
    c5cb:	4c 8b 65 a8          	mov    r12,QWORD PTR [rbp-0x58]
    c5cf:	4c 8b 7d d0          	mov    r15,QWORD PTR [rbp-0x30]
    c5d3:	88 03                	mov    BYTE PTR [rbx],al
    c5d5:	48 01 df             	add    rdi,rbx
    c5d8:	e8 43 4b ff ff       	call   1120 <memcpy@plt>
    c5dd:	4c 89 f6             	mov    rsi,r14
    c5e0:	e9 8b fe ff ff       	jmp    c470 <zbtScoreLeafBuild+0x4f0>
    c5e5:	49 89 df             	mov    r15,rbx
    c5e8:	66 45 89 7c 24 36    	mov    WORD PTR [r12+0x36],r15w
    c5ee:	4c 8b 75 80          	mov    r14,QWORD PTR [rbp-0x80]
    c5f2:	41 83 fe ff          	cmp    r14d,0xffffffff
    c5f6:	4c 8b 7d b0          	mov    r15,QWORD PTR [rbp-0x50]
    c5fa:	74 22                	je     c61e <zbtScoreLeafBuild+0x69e>
    c5fc:	45 89 74 24 30       	mov    DWORD PTR [r12+0x30],r14d
    c601:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c605:	44 89 f1             	mov    ecx,r14d
    c608:	4c 89 24 c8          	mov    QWORD PTR [rax+rcx*8],r12
    c60c:	4c 89 e0             	mov    rax,r12
    c60f:	48 83 c4 68          	add    rsp,0x68
    c613:	5b                   	pop    rbx
    c614:	41 5c                	pop    r12
    c616:	41 5d                	pop    r13
    c618:	41 5e                	pop    r14
    c61a:	41 5f                	pop    r15
    c61c:	5d                   	pop    rbp
    c61d:	c3                   	ret
    c61e:	45 8b 77 58          	mov    r14d,DWORD PTR [r15+0x58]
    c622:	45 85 f6             	test   r14d,r14d
    c625:	74 07                	je     c62e <zbtScoreLeafBuild+0x6ae>
    c627:	49 83 7f 40 00       	cmp    QWORD PTR [r15+0x40],0x0
    c62c:	74 72                	je     c6a0 <zbtScoreLeafBuild+0x720>
    c62e:	45 8b 77 54          	mov    r14d,DWORD PTR [r15+0x54]
    c632:	41 8d 46 01          	lea    eax,[r14+0x1]
    c636:	41 89 47 54          	mov    DWORD PTR [r15+0x54],eax
    c63a:	45 3b 77 50          	cmp    r14d,DWORD PTR [r15+0x50]
    c63e:	75 bc                	jne    c5fc <zbtScoreLeafBuild+0x67c>
    c640:	43 8d 04 36          	lea    eax,[r14+r14*1]
    c644:	45 85 f6             	test   r14d,r14d
    c647:	bb 10 00 00 00       	mov    ebx,0x10
    c64c:	0f 45 d8             	cmovne ebx,eax
    c64f:	48 c7 45 90 00 00 00 	mov    QWORD PTR [rbp-0x70],0x0
    c656:	00
    c657:	49 8b 7f 48          	mov    rdi,QWORD PTR [r15+0x48]
    c65b:	48 8d 34 dd 00 00 00 	lea    rsi,[rbx*8+0x0]
    c662:	00
    c663:	48 8d 55 b8          	lea    rdx,[rbp-0x48]
    c667:	48 8d 4d 90          	lea    rcx,[rbp-0x70]
    c66b:	e8 d0 51 00 00       	call   11840 <zrealloc_usable>
    c670:	49 89 47 48          	mov    QWORD PTR [r15+0x48],rax
    c674:	41 8b 4f 50          	mov    ecx,DWORD PTR [r15+0x50]
    c678:	48 8d 3c c8          	lea    rdi,[rax+rcx*8]
    c67c:	89 da                	mov    edx,ebx
    c67e:	29 ca                	sub    edx,ecx
    c680:	48 c1 e2 03          	shl    rdx,0x3
    c684:	31 f6                	xor    esi,esi
    c686:	e8 25 4a ff ff       	call   10b0 <memset@plt>
    c68b:	41 89 5f 50          	mov    DWORD PTR [r15+0x50],ebx
    c68f:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    c693:	48 2b 45 90          	sub    rax,QWORD PTR [rbp-0x70]
    c697:	49 01 47 68          	add    QWORD PTR [r15+0x68],rax
    c69b:	e9 5c ff ff ff       	jmp    c5fc <zbtScoreLeafBuild+0x67c>
    c6a0:	41 ff ce             	dec    r14d
    c6a3:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c6a7:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c6ab:	a8 01                	test   al,0x1
    c6ad:	75 20                	jne    c6cf <zbtScoreLeafBuild+0x74f>
    c6af:	48 8d 3d 68 6f 00 00 	lea    rdi,[rip+0x6f68]        # 1361e <_IO_stdin_used+0x61e>
    c6b6:	48 8d 15 89 71 00 00 	lea    rdx,[rip+0x7189]        # 13846 <_IO_stdin_used+0x846>
    c6bd:	be 25 03 00 00       	mov    esi,0x325
    c6c2:	e8 09 50 00 00       	call   116d0 <standalone_panic>
    c6c7:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c6cb:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c6cf:	48 d1 e8             	shr    rax,1
    c6d2:	41 89 47 58          	mov    DWORD PTR [r15+0x58],eax
    c6d6:	e9 21 ff ff ff       	jmp    c5fc <zbtScoreLeafBuild+0x67c>

Disassembly of section .fini:
