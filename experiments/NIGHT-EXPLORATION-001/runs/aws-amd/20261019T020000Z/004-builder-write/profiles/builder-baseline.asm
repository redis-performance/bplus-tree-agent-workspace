
build/size-matrix/btree-bench:     file format elf64-x86-64


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
    bf91:	4c 89 4d 88          	mov    QWORD PTR [rbp-0x78],r9
    bf95:	4c 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],r8
    bf9c:	49 89 cb             	mov    r11,rcx
    bf9f:	f3 0f 7e 02          	movq   xmm0,QWORD PTR [rdx]
    bfa3:	66 48 0f 7e c0       	movq   rax,xmm0
    bfa8:	48 bb 00 00 00 00 00 	movabs rbx,0x8000000000000000
    bfaf:	00 00 80
    bfb2:	49 89 fd             	mov    r13,rdi
    bfb5:	49 89 c7             	mov    r15,rax
    bfb8:	48 85 c0             	test   rax,rax
    bfbb:	0f 88 bb 00 00 00    	js     c07c <zbtScoreLeafBuild+0xfc>
    bfc1:	49 09 df             	or     r15,rbx
    bfc4:	41 89 f4             	mov    r12d,esi
    bfc7:	49 89 f6             	mov    r14,rsi
    bfca:	83 fe 02             	cmp    esi,0x2
    bfcd:	0f 82 bb 00 00 00    	jb     c08e <zbtScoreLeafBuild+0x10e>
    bfd3:	bf 01 00 00 00       	mov    edi,0x1
    bfd8:	31 c9                	xor    ecx,ecx
    bfda:	4d 89 fa             	mov    r10,r15
    bfdd:	4c 89 fe             	mov    rsi,r15
    bfe0:	eb 30                	jmp    c012 <zbtScoreLeafBuild+0x92>
    bfe2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    bfe9:	1f 84 00 00 00 00 00
    bff0:	49 09 d8             	or     r8,rbx
    bff3:	4d 89 c1             	mov    r9,r8
    bff6:	4d 31 f9             	xor    r9,r15
    bff9:	4c 09 c9             	or     rcx,r9
    bffc:	4d 39 d0             	cmp    r8,r10
    bfff:	4d 0f 42 d0          	cmovb  r10,r8
    c003:	49 39 f0             	cmp    r8,rsi
    c006:	49 0f 47 f0          	cmova  rsi,r8
    c00a:	48 ff c7             	inc    rdi
    c00d:	49 39 fc             	cmp    r12,rdi
    c010:	74 14                	je     c026 <zbtScoreLeafBuild+0xa6>
    c012:	f3 0f 7e 04 fa       	movq   xmm0,QWORD PTR [rdx+rdi*8]
    c017:	66 49 0f 7e c0       	movq   r8,xmm0
    c01c:	4d 85 c0             	test   r8,r8
    c01f:	79 cf                	jns    bff0 <zbtScoreLeafBuild+0x70>
    c021:	49 f7 d0             	not    r8
    c024:	eb cd                	jmp    bff3 <zbtScoreLeafBuild+0x73>
    c026:	45 31 c0             	xor    r8d,r8d
    c029:	48 85 c9             	test   rcx,rcx
    c02c:	74 69                	je     c097 <zbtScoreLeafBuild+0x117>
    c02e:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c033:	4c 29 d6             	sub    rsi,r10
    c036:	48 89 4d b8          	mov    QWORD PTR [rbp-0x48],rcx
    c03a:	48 d3 ee             	shr    rsi,cl
    c03d:	48 0f bd ce          	bsr    rcx,rsi
    c041:	83 f1 3f             	xor    ecx,0x3f
    c044:	40 b7 40             	mov    dil,0x40
    c047:	40 28 cf             	sub    dil,cl
    c04a:	48 85 f6             	test   rsi,rsi
    c04d:	40 0f b6 cf          	movzx  ecx,dil
    c051:	41 0f 44 c8          	cmove  ecx,r8d
    c055:	4d 89 d7             	mov    r15,r10
    c058:	89 4d c0             	mov    DWORD PTR [rbp-0x40],ecx
    c05b:	48 85 c0             	test   rax,rax
    c05e:	4c 89 65 c8          	mov    QWORD PTR [rbp-0x38],r12
    c062:	79 4c                	jns    c0b0 <zbtScoreLeafBuild+0x130>
    c064:	48 f7 d0             	not    rax
    c067:	41 bc 38 00 00 00    	mov    r12d,0x38
    c06d:	41 83 fe 02          	cmp    r14d,0x2
    c071:	48 89 55 80          	mov    QWORD PTR [rbp-0x80],rdx
    c075:	73 50                	jae    c0c7 <zbtScoreLeafBuild+0x147>
    c077:	e9 df 00 00 00       	jmp    c15b <zbtScoreLeafBuild+0x1db>
    c07c:	49 f7 d7             	not    r15
    c07f:	41 89 f4             	mov    r12d,esi
    c082:	49 89 f6             	mov    r14,rsi
    c085:	83 fe 02             	cmp    esi,0x2
    c088:	0f 83 45 ff ff ff    	jae    bfd3 <zbtScoreLeafBuild+0x53>
    c08e:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    c095:	eb 0a                	jmp    c0a1 <zbtScoreLeafBuild+0x121>
    c097:	c7 45 c0 00 00 00 00 	mov    DWORD PTR [rbp-0x40],0x0
    c09e:	4d 89 d7             	mov    r15,r10
    c0a1:	31 c9                	xor    ecx,ecx
    c0a3:	48 89 4d b8          	mov    QWORD PTR [rbp-0x48],rcx
    c0a7:	48 85 c0             	test   rax,rax
    c0aa:	4c 89 65 c8          	mov    QWORD PTR [rbp-0x38],r12
    c0ae:	78 b4                	js     c064 <zbtScoreLeafBuild+0xe4>
    c0b0:	48 09 d8             	or     rax,rbx
    c0b3:	41 bc 38 00 00 00    	mov    r12d,0x38
    c0b9:	41 83 fe 02          	cmp    r14d,0x2
    c0bd:	48 89 55 80          	mov    QWORD PTR [rbp-0x80],rdx
    c0c1:	0f 82 94 00 00 00    	jb     c15b <zbtScoreLeafBuild+0x1db>
    c0c7:	41 b8 01 00 00 00    	mov    r8d,0x1
    c0cd:	31 c9                	xor    ecx,ecx
    c0cf:	48 89 c7             	mov    rdi,rax
    c0d2:	48 89 c6             	mov    rsi,rax
    c0d5:	eb 2c                	jmp    c103 <zbtScoreLeafBuild+0x183>
    c0d7:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    c0de:	00 00
    c0e0:	49 09 d9             	or     r9,rbx
    c0e3:	4d 89 ca             	mov    r10,r9
    c0e6:	49 31 c2             	xor    r10,rax
    c0e9:	4c 09 d1             	or     rcx,r10
    c0ec:	49 39 f9             	cmp    r9,rdi
    c0ef:	49 0f 42 f9          	cmovb  rdi,r9
    c0f3:	49 39 f1             	cmp    r9,rsi
    c0f6:	49 0f 47 f1          	cmova  rsi,r9
    c0fa:	49 ff c0             	inc    r8
    c0fd:	4c 39 45 c8          	cmp    QWORD PTR [rbp-0x38],r8
    c101:	74 15                	je     c118 <zbtScoreLeafBuild+0x198>
    c103:	f3 42 0f 7e 04 c2    	movq   xmm0,QWORD PTR [rdx+r8*8]
    c109:	66 49 0f 7e c1       	movq   r9,xmm0
    c10e:	4d 85 c9             	test   r9,r9
    c111:	79 cd                	jns    c0e0 <zbtScoreLeafBuild+0x160>
    c113:	49 f7 d1             	not    r9
    c116:	eb cb                	jmp    c0e3 <zbtScoreLeafBuild+0x163>
    c118:	48 85 c9             	test   rcx,rcx
    c11b:	74 3e                	je     c15b <zbtScoreLeafBuild+0x1db>
    c11d:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c122:	48 29 fe             	sub    rsi,rdi
    c125:	48 d3 ee             	shr    rsi,cl
    c128:	48 85 f6             	test   rsi,rsi
    c12b:	74 2e                	je     c15b <zbtScoreLeafBuild+0x1db>
    c12d:	48 0f bd c6          	bsr    rax,rsi
    c131:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    c135:	48 83 c0 41          	add    rax,0x41
    c139:	48 0f af 45 c8       	imul   rax,QWORD PTR [rbp-0x38]
    c13e:	48 83 c0 07          	add    rax,0x7
    c142:	48 c1 e8 03          	shr    rax,0x3
    c146:	48 83 c0 09          	add    rax,0x9
    c14a:	49 bc fe ff ff ff ff 	movabs r12,0x1ffffffffffffffe
    c151:	ff ff 1f
    c154:	49 21 c4             	and    r12,rax
    c157:	49 83 c4 38          	add    r12,0x38
    c15b:	8b 45 10             	mov    eax,DWORD PTR [rbp+0x10]
    c15e:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    c162:	48 8d 1c 49          	lea    rbx,[rcx+rcx*2]
    c166:	4c 01 e3             	add    rbx,r12
    c169:	45 85 f6             	test   r14d,r14d
    c16c:	74 5f                	je     c1cd <zbtScoreLeafBuild+0x24d>
    c16e:	48 8d 0c cd 00 00 00 	lea    rcx,[rcx*8+0x0]
    c175:	00
    c176:	48 8d 0c 89          	lea    rcx,[rcx+rcx*4]
    c17a:	31 d2                	xor    edx,edx
    c17c:	4d 89 ec             	mov    r12,r13
    c17f:	eb 1b                	jmp    c19c <zbtScoreLeafBuild+0x21c>
    c181:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c188:	0f 1f 84 00 00 00 00
    c18f:	00
    c190:	48 01 f3             	add    rbx,rsi
    c193:	48 83 c2 28          	add    rdx,0x28
    c197:	48 39 d1             	cmp    rcx,rdx
    c19a:	74 34                	je     c1d0 <zbtScoreLeafBuild+0x250>
    c19c:	be 15 00 00 00       	mov    esi,0x15
    c1a1:	49 83 7c 13 18 00    	cmp    QWORD PTR [r11+rdx*1+0x18],0x0
    c1a7:	75 e7                	jne    c190 <zbtScoreLeafBuild+0x210>
    c1a9:	49 8b 7c 13 08       	mov    rdi,QWORD PTR [r11+rdx*1+0x8]
    c1ae:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    c1b5:	77 d9                	ja     c190 <zbtScoreLeafBuild+0x210>
    c1b7:	31 f6                	xor    esi,esi
    c1b9:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    c1c0:	40 0f 93 c6          	setae  sil
    c1c4:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    c1c8:	48 ff c6             	inc    rsi
    c1cb:	eb c3                	jmp    c190 <zbtScoreLeafBuild+0x210>
    c1cd:	4d 89 ec             	mov    r12,r13
    c1d0:	4c 89 5d d0          	mov    QWORD PTR [rbp-0x30],r11
    c1d4:	85 c0                	test   eax,eax
    c1d6:	74 0e                	je     c1e6 <zbtScoreLeafBuild+0x266>
    c1d8:	bf ff 0f 00 00       	mov    edi,0xfff
    c1dd:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c1e4:	72 29                	jb     c20f <zbtScoreLeafBuild+0x28f>
    c1e6:	48 89 df             	mov    rdi,rbx
    c1e9:	41 83 fe 5f          	cmp    r14d,0x5f
    c1ed:	77 20                	ja     c20f <zbtScoreLeafBuild+0x28f>
    c1ef:	48 89 df             	mov    rdi,rbx
    c1f2:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    c1f9:	77 14                	ja     c20f <zbtScoreLeafBuild+0x28f>
    c1fb:	48 81 fb 7f 0f 00 00 	cmp    rbx,0xf7f
    c202:	bf 7f 0f 00 00       	mov    edi,0xf7f
    c207:	48 0f 42 fb          	cmovb  rdi,rbx
    c20b:	48 83 ef 80          	sub    rdi,0xffffffffffffff80
    c20f:	48 8d 75 a8          	lea    rsi,[rbp-0x58]
    c213:	e8 88 55 00 00       	call   117a0 <zmalloc_usable>
    c218:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    c21c:	49 01 4c 24 68       	add    QWORD PTR [r12+0x68],rcx
    c221:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    c225:	41 8d 46 ff          	lea    eax,[r14-0x1]
    c229:	83 f8 60             	cmp    eax,0x60
    c22c:	72 18                	jb     c246 <zbtScoreLeafBuild+0x2c6>
    c22e:	48 8d 3d e9 73 00 00 	lea    rdi,[rip+0x73e9]        # 1361e <_IO_stdin_used+0x61e>
    c235:	48 8d 15 8a 75 00 00 	lea    rdx,[rip+0x758a]        # 137c6 <_IO_stdin_used+0x7c6>
    c23c:	be de 03 00 00       	mov    esi,0x3de
    c241:	e8 5a 54 00 00       	call   116a0 <standalone_panic>
    c246:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c24d:	72 18                	jb     c267 <zbtScoreLeafBuild+0x2e7>
    c24f:	48 8d 3d c8 73 00 00 	lea    rdi,[rip+0x73c8]        # 1361e <_IO_stdin_used+0x61e>
    c256:	48 8d 15 92 75 00 00 	lea    rdx,[rip+0x7592]        # 137ef <_IO_stdin_used+0x7ef>
    c25d:	be df 03 00 00       	mov    esi,0x3df
    c262:	e8 39 54 00 00       	call   116a0 <standalone_panic>
    c267:	66 0f ef c0          	pxor   xmm0,xmm0
    c26b:	48 8b 45 b0          	mov    rax,QWORD PTR [rbp-0x50]
    c26f:	f3 0f 7f 40 10       	movdqu XMMWORD PTR [rax+0x10],xmm0
    c274:	f3 0f 7f 00          	movdqu XMMWORD PTR [rax],xmm0
    c278:	f3 0f 7f 40 20       	movdqu XMMWORD PTR [rax+0x20],xmm0
    c27d:	48 c7 40 30 00 00 00 	mov    QWORD PTR [rax+0x30],0x0
    c284:	00
    c285:	c6 40 12 01          	mov    BYTE PTR [rax+0x12],0x1
    c289:	44 88 70 11          	mov    BYTE PTR [rax+0x11],r14b
    c28d:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    c291:	48 89 48 08          	mov    QWORD PTR [rax+0x8],rcx
    c295:	48 8b 55 b8          	mov    rdx,QWORD PTR [rbp-0x48]
    c299:	88 50 13             	mov    BYTE PTR [rax+0x13],dl
    c29c:	4c 89 78 28          	mov    QWORD PTR [rax+0x28],r15
    c2a0:	8b 55 c0             	mov    edx,DWORD PTR [rbp-0x40]
    c2a3:	88 50 34             	mov    BYTE PTR [rax+0x34],dl
    c2a6:	4c 8d 68 38          	lea    r13,[rax+0x38]
    c2aa:	84 d2                	test   dl,dl
    c2ac:	4c 89 6d 98          	mov    QWORD PTR [rbp-0x68],r13
    c2b0:	74 4b                	je     c2fd <zbtScoreLeafBuild+0x37d>
    c2b2:	0f b6 da             	movzx  ebx,dl
    c2b5:	48 89 d8             	mov    rax,rbx
    c2b8:	48 0f af c1          	imul   rax,rcx
    c2bc:	48 83 c0 07          	add    rax,0x7
    c2c0:	48 c1 e8 03          	shr    rax,0x3
    c2c4:	48 83 c0 09          	add    rax,0x9
    c2c8:	48 ba fe ff ff ff 3f 	movabs rdx,0x3ffffffffe
    c2cf:	00 00 00
    c2d2:	48 21 c2             	and    rdx,rax
    c2d5:	4c 89 ef             	mov    rdi,r13
    c2d8:	31 f6                	xor    esi,esi
    c2da:	e8 d1 4d ff ff       	call   10b0 <memset@plt>
    c2df:	45 0f b6 fe          	movzx  r15d,r14b
    c2e3:	41 0f af df          	imul   ebx,r15d
    c2e7:	83 c3 07             	add    ebx,0x7
    c2ea:	c1 eb 03             	shr    ebx,0x3
    c2ed:	83 c3 09             	add    ebx,0x9
    c2f0:	83 e3 fe             	and    ebx,0xfffffffe
    c2f3:	4a 8d 04 2b          	lea    rax,[rbx+r13*1]
    c2f7:	48 89 45 c0          	mov    QWORD PTR [rbp-0x40],rax
    c2fb:	eb 0a                	jmp    c307 <zbtScoreLeafBuild+0x387>
    c2fd:	45 0f b6 fe          	movzx  r15d,r14b
    c301:	31 db                	xor    ebx,ebx
    c303:	4c 89 6d c0          	mov    QWORD PTR [rbp-0x40],r13
    c307:	4d 89 f5             	mov    r13,r14
    c30a:	4c 89 65 a0          	mov    QWORD PTR [rbp-0x60],r12
    c30e:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c312:	4c 89 e7             	mov    rdi,r12
    c315:	e8 b6 53 00 00       	call   116d0 <zmalloc_usable_size>
    c31a:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    c320:	41 be ff 0f 00 00    	mov    r14d,0xfff
    c326:	4c 0f 42 f0          	cmovb  r14,rax
    c32a:	45 85 ed             	test   r13d,r13d
    c32d:	0f 84 7c 02 00 00    	je     c5af <zbtScoreLeafBuild+0x62f>
    c333:	48 03 5d 98          	add    rbx,QWORD PTR [rbp-0x68]
    c337:	4a 8d 04 7b          	lea    rax,[rbx+r15*2]
    c33b:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    c33f:	4d 01 e6             	add    r14,r12
    c342:	45 31 ed             	xor    r13d,r13d
    c345:	4c 89 f3             	mov    rbx,r14
    c348:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c34c:	eb 32                	jmp    c380 <zbtScoreLeafBuild+0x400>
    c34e:	66 90                	xchg   ax,ax
    c350:	49 c7 47 0d 00 00 00 	mov    QWORD PTR [r15+0xd],0x0
    c357:	00
    c358:	66 0f ef c0          	pxor   xmm0,xmm0
    c35c:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    c362:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c366:	41 c6 44 24 14 01    	mov    BYTE PTR [r12+0x14],0x1
    c36c:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    c370:	49 ff c5             	inc    r13
    c373:	49 83 c2 28          	add    r10,0x28
    c377:	4d 39 ef             	cmp    r15,r13
    c37a:	0f 84 2f 02 00 00    	je     c5af <zbtScoreLeafBuild+0x62f>
    c380:	48 c7 c0 eb ff ff ff 	mov    rax,0xffffffffffffffeb
    c387:	49 83 7a 18 00       	cmp    QWORD PTR [r10+0x18],0x0
    c38c:	75 32                	jne    c3c0 <zbtScoreLeafBuild+0x440>
    c38e:	49 8b 4a 08          	mov    rcx,QWORD PTR [r10+0x8]
    c392:	48 81 f9 3f 01 00 00 	cmp    rcx,0x13f
    c399:	77 25                	ja     c3c0 <zbtScoreLeafBuild+0x440>
    c39b:	48 81 f9 fe 00 00 00 	cmp    rcx,0xfe
    c3a2:	b8 00 00 00 00       	mov    eax,0x0
    c3a7:	48 19 c0             	sbb    rax,rax
    c3aa:	48 83 c8 fd          	or     rax,0xfffffffffffffffd
    c3ae:	48 29 c8             	sub    rax,rcx
    c3b1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c3b8:	0f 1f 84 00 00 00 00
    c3bf:	00
    c3c0:	41 0f b6 54 24 34    	movzx  edx,BYTE PTR [r12+0x34]
    c3c6:	85 d2                	test   edx,edx
    c3c8:	0f 84 b2 00 00 00    	je     c480 <zbtScoreLeafBuild+0x500>
    c3ce:	48 8b 4d 80          	mov    rcx,QWORD PTR [rbp-0x80]
    c3d2:	f3 42 0f 7e 04 e9    	movq   xmm0,QWORD PTR [rcx+r13*8]
    c3d8:	66 48 0f 7e c6       	movq   rsi,xmm0
    c3dd:	48 85 f6             	test   rsi,rsi
    c3e0:	78 3e                	js     c420 <zbtScoreLeafBuild+0x4a0>
    c3e2:	48 b9 00 00 00 00 00 	movabs rcx,0x8000000000000000
    c3e9:	00 00 80
    c3ec:	48 09 ce             	or     rsi,rcx
    c3ef:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    c3f5:	49 8b 4c 24 28       	mov    rcx,QWORD PTR [r12+0x28]
    c3fa:	74 34                	je     c430 <zbtScoreLeafBuild+0x4b0>
    c3fc:	48 29 f1             	sub    rcx,rsi
    c3ff:	41 0f b6 74 24 11    	movzx  esi,BYTE PTR [r12+0x11]
    c405:	4c 89 ef             	mov    rdi,r13
    c408:	41 b8 ff ff ff ff    	mov    r8d,0xffffffff
    c40e:	4c 31 c7             	xor    rdi,r8
    c411:	48 01 f7             	add    rdi,rsi
    c414:	48 89 ce             	mov    rsi,rcx
    c417:	eb 1d                	jmp    c436 <zbtScoreLeafBuild+0x4b6>
    c419:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    c420:	48 f7 d6             	not    rsi
    c423:	41 80 7c 24 35 00    	cmp    BYTE PTR [r12+0x35],0x0
    c429:	49 8b 4c 24 28       	mov    rcx,QWORD PTR [r12+0x28]
    c42e:	75 cc                	jne    c3fc <zbtScoreLeafBuild+0x47c>
    c430:	48 29 ce             	sub    rsi,rcx
    c433:	4c 89 ef             	mov    rdi,r13
    c436:	41 0f b6 4c 24 13    	movzx  ecx,BYTE PTR [r12+0x13]
    c43c:	48 d3 ee             	shr    rsi,cl
    c43f:	89 f9                	mov    ecx,edi
    c441:	41 89 d0             	mov    r8d,edx
    c444:	4c 0f af c1          	imul   r8,rcx
    c448:	4c 89 c7             	mov    rdi,r8
    c44b:	48 c1 ef 03          	shr    rdi,0x3
    c44f:	44 89 c1             	mov    ecx,r8d
    c452:	80 e1 07             	and    cl,0x7
    c455:	49 89 f1             	mov    r9,rsi
    c458:	49 d3 e1             	shl    r9,cl
    c45b:	48 8b 4d 98          	mov    rcx,QWORD PTR [rbp-0x68]
    c45f:	4c 09 0c 39          	or     QWORD PTR [rcx+rdi*1],r9
    c463:	41 83 e0 07          	and    r8d,0x7
    c467:	74 17                	je     c480 <zbtScoreLeafBuild+0x500>
    c469:	b9 40 00 00 00       	mov    ecx,0x40
    c46e:	44 29 c1             	sub    ecx,r8d
    c471:	39 d1                	cmp    ecx,edx
    c473:	73 0b                	jae    c480 <zbtScoreLeafBuild+0x500>
    c475:	48 d3 ee             	shr    rsi,cl
    c478:	42 08 74 27 40       	or     BYTE PTR [rdi+r12*1+0x40],sil
    c47d:	0f 1f 00             	nop    DWORD PTR [rax]
    c480:	48 01 c3             	add    rbx,rax
    c483:	49 89 de             	mov    r14,rbx
    c486:	4d 29 e6             	sub    r14,r12
    c489:	49 81 fe 00 10 00 00 	cmp    r14,0x1000
    c490:	4c 89 55 d0          	mov    QWORD PTR [rbp-0x30],r10
    c494:	7c 1c                	jl     c4b2 <zbtScoreLeafBuild+0x532>
    c496:	48 8d 3d 81 71 00 00 	lea    rdi,[rip+0x7181]        # 1361e <_IO_stdin_used+0x61e>
    c49d:	be f7 03 00 00       	mov    esi,0x3f7
    c4a2:	48 8d 15 66 73 00 00 	lea    rdx,[rip+0x7366]        # 1380f <_IO_stdin_used+0x80f>
    c4a9:	e8 f2 51 00 00       	call   116a0 <standalone_panic>
    c4ae:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c4b2:	4d 8d 62 18          	lea    r12,[r10+0x18]
    c4b6:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c4ba:	66 46 89 34 68       	mov    WORD PTR [rax+r13*2],r14w
    c4bf:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
    c4c6:	42 0f b6 04 28       	movzx  eax,BYTE PTR [rax+r13*1]
    c4cb:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    c4cf:	42 88 04 29          	mov    BYTE PTR [rcx+r13*1],al
    c4d3:	4d 8b 3c 24          	mov    r15,QWORD PTR [r12]
    c4d7:	4d 85 ff             	test   r15,r15
    c4da:	75 5f                	jne    c53b <zbtScoreLeafBuild+0x5bb>
    c4dc:	49 8b 52 08          	mov    rdx,QWORD PTR [r10+0x8]
    c4e0:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    c4e7:	77 1c                	ja     c505 <zbtScoreLeafBuild+0x585>
    c4e9:	49 8b 32             	mov    rsi,QWORD PTR [r10]
    c4ec:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    c4f3:	0f 87 90 00 00 00    	ja     c589 <zbtScoreLeafBuild+0x609>
    c4f9:	bf 01 00 00 00       	mov    edi,0x1
    c4fe:	89 d0                	mov    eax,edx
    c500:	e9 8f 00 00 00       	jmp    c594 <zbtScoreLeafBuild+0x614>
    c505:	48 89 d7             	mov    rdi,rdx
    c508:	48 8d 75 a8          	lea    rsi,[rbp-0x58]
    c50c:	e8 8f 52 00 00       	call   117a0 <zmalloc_usable>
    c511:	48 8b 4d a8          	mov    rcx,QWORD PTR [rbp-0x58]
    c515:	48 8b 55 a0          	mov    rdx,QWORD PTR [rbp-0x60]
    c519:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    c51d:	49 89 c7             	mov    r15,rax
    c520:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    c524:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    c527:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    c52b:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    c52f:	4c 89 ff             	mov    rdi,r15
    c532:	e8 e9 4b ff ff       	call   1120 <memcpy@plt>
    c537:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c53b:	49 8b 42 08          	mov    rax,QWORD PTR [r10+0x8]
    c53f:	c6 03 ff             	mov    BYTE PTR [rbx],0xff
    c542:	41 8b 4a 10          	mov    ecx,DWORD PTR [r10+0x10]
    c546:	89 4b 01             	mov    DWORD PTR [rbx+0x1],ecx
    c549:	48 89 43 05          	mov    QWORD PTR [rbx+0x5],rax
    c54d:	4c 89 7b 0d          	mov    QWORD PTR [rbx+0xd],r15
    c551:	4d 8b 7a 20          	mov    r15,QWORD PTR [r10+0x20]
    c555:	4d 85 ff             	test   r15,r15
    c558:	0f 84 fa fd ff ff    	je     c358 <zbtScoreLeafBuild+0x3d8>
    c55e:	41 80 3f ff          	cmp    BYTE PTR [r15],0xff
    c562:	0f 84 e8 fd ff ff    	je     c350 <zbtScoreLeafBuild+0x3d0>
    c568:	48 8d 3d af 70 00 00 	lea    rdi,[rip+0x70af]        # 1361e <_IO_stdin_used+0x61e>
    c56f:	be 45 02 00 00       	mov    esi,0x245
    c574:	48 8d 15 db 71 00 00 	lea    rdx,[rip+0x71db]        # 13756 <_IO_stdin_used+0x756>
    c57b:	e8 20 51 00 00       	call   116a0 <standalone_panic>
    c580:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c584:	e9 c7 fd ff ff       	jmp    c350 <zbtScoreLeafBuild+0x3d0>
    c589:	66 89 53 01          	mov    WORD PTR [rbx+0x1],dx
    c58d:	bf 03 00 00 00       	mov    edi,0x3
    c592:	b0 fe                	mov    al,0xfe
    c594:	4c 8b 7d c8          	mov    r15,QWORD PTR [rbp-0x38]
    c598:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c59c:	88 03                	mov    BYTE PTR [rbx],al
    c59e:	48 01 df             	add    rdi,rbx
    c5a1:	e8 7a 4b ff ff       	call   1120 <memcpy@plt>
    c5a6:	4c 8b 55 d0          	mov    r10,QWORD PTR [rbp-0x30]
    c5aa:	e9 c1 fd ff ff       	jmp    c370 <zbtScoreLeafBuild+0x3f0>
    c5af:	66 45 89 74 24 36    	mov    WORD PTR [r12+0x36],r14w
    c5b5:	4c 8b 75 88          	mov    r14,QWORD PTR [rbp-0x78]
    c5b9:	41 83 fe ff          	cmp    r14d,0xffffffff
    c5bd:	4c 8b 7d a0          	mov    r15,QWORD PTR [rbp-0x60]
    c5c1:	74 22                	je     c5e5 <zbtScoreLeafBuild+0x665>
    c5c3:	45 89 74 24 30       	mov    DWORD PTR [r12+0x30],r14d
    c5c8:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c5cc:	44 89 f1             	mov    ecx,r14d
    c5cf:	4c 89 24 c8          	mov    QWORD PTR [rax+rcx*8],r12
    c5d3:	4c 89 e0             	mov    rax,r12
    c5d6:	48 83 c4 68          	add    rsp,0x68
    c5da:	5b                   	pop    rbx
    c5db:	41 5c                	pop    r12
    c5dd:	41 5d                	pop    r13
    c5df:	41 5e                	pop    r14
    c5e1:	41 5f                	pop    r15
    c5e3:	5d                   	pop    rbp
    c5e4:	c3                   	ret
    c5e5:	45 8b 77 58          	mov    r14d,DWORD PTR [r15+0x58]
    c5e9:	45 85 f6             	test   r14d,r14d
    c5ec:	74 07                	je     c5f5 <zbtScoreLeafBuild+0x675>
    c5ee:	49 83 7f 40 00       	cmp    QWORD PTR [r15+0x40],0x0
    c5f3:	74 72                	je     c667 <zbtScoreLeafBuild+0x6e7>
    c5f5:	45 8b 77 54          	mov    r14d,DWORD PTR [r15+0x54]
    c5f9:	41 8d 46 01          	lea    eax,[r14+0x1]
    c5fd:	41 89 47 54          	mov    DWORD PTR [r15+0x54],eax
    c601:	45 3b 77 50          	cmp    r14d,DWORD PTR [r15+0x50]
    c605:	75 bc                	jne    c5c3 <zbtScoreLeafBuild+0x643>
    c607:	43 8d 04 36          	lea    eax,[r14+r14*1]
    c60b:	45 85 f6             	test   r14d,r14d
    c60e:	bb 10 00 00 00       	mov    ebx,0x10
    c613:	0f 45 d8             	cmovne ebx,eax
    c616:	48 c7 45 90 00 00 00 	mov    QWORD PTR [rbp-0x70],0x0
    c61d:	00
    c61e:	49 8b 7f 48          	mov    rdi,QWORD PTR [r15+0x48]
    c622:	48 8d 34 dd 00 00 00 	lea    rsi,[rbx*8+0x0]
    c629:	00
    c62a:	48 8d 55 a8          	lea    rdx,[rbp-0x58]
    c62e:	48 8d 4d 90          	lea    rcx,[rbp-0x70]
    c632:	e8 d9 51 00 00       	call   11810 <zrealloc_usable>
    c637:	49 89 47 48          	mov    QWORD PTR [r15+0x48],rax
    c63b:	41 8b 4f 50          	mov    ecx,DWORD PTR [r15+0x50]
    c63f:	48 8d 3c c8          	lea    rdi,[rax+rcx*8]
    c643:	89 da                	mov    edx,ebx
    c645:	29 ca                	sub    edx,ecx
    c647:	48 c1 e2 03          	shl    rdx,0x3
    c64b:	31 f6                	xor    esi,esi
    c64d:	e8 5e 4a ff ff       	call   10b0 <memset@plt>
    c652:	41 89 5f 50          	mov    DWORD PTR [r15+0x50],ebx
    c656:	48 8b 45 a8          	mov    rax,QWORD PTR [rbp-0x58]
    c65a:	48 2b 45 90          	sub    rax,QWORD PTR [rbp-0x70]
    c65e:	49 01 47 68          	add    QWORD PTR [r15+0x68],rax
    c662:	e9 5c ff ff ff       	jmp    c5c3 <zbtScoreLeafBuild+0x643>
    c667:	41 ff ce             	dec    r14d
    c66a:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c66e:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c672:	a8 01                	test   al,0x1
    c674:	75 20                	jne    c696 <zbtScoreLeafBuild+0x716>
    c676:	48 8d 3d a1 6f 00 00 	lea    rdi,[rip+0x6fa1]        # 1361e <_IO_stdin_used+0x61e>
    c67d:	48 8d 15 c2 71 00 00 	lea    rdx,[rip+0x71c2]        # 13846 <_IO_stdin_used+0x846>
    c684:	be 25 03 00 00       	mov    esi,0x325
    c689:	e8 12 50 00 00       	call   116a0 <standalone_panic>
    c68e:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c692:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c696:	48 d1 e8             	shr    rax,1
    c699:	41 89 47 58          	mov    DWORD PTR [r15+0x58],eax
    c69d:	e9 21 ff ff ff       	jmp    c5c3 <zbtScoreLeafBuild+0x643>

Disassembly of section .fini:
