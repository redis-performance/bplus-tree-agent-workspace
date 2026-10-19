
scratch/amd-builder-build/B/build/native/btree-bench:     file format elf64-x86-64


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
    bfa5:	49 89 d5             	mov    r13,rdx
    bfa8:	49 89 ff             	mov    r15,rdi
    bfab:	f3 0f 7e 02          	movq   xmm0,QWORD PTR [rdx]
    bfaf:	66 48 0f 7e c0       	movq   rax,xmm0
    bfb4:	48 bb 00 00 00 00 00 	movabs rbx,0x8000000000000000
    bfbb:	00 00 80
    bfbe:	48 89 c1             	mov    rcx,rax
    bfc1:	48 85 c0             	test   rax,rax
    bfc4:	78 05                	js     bfcb <zbtScoreLeafBuild+0x4b>
    bfc6:	48 09 d9             	or     rcx,rbx
    bfc9:	eb 03                	jmp    bfce <zbtScoreLeafBuild+0x4e>
    bfcb:	48 f7 d1             	not    rcx
    bfce:	48 89 4d b8          	mov    QWORD PTR [rbp-0x48],rcx
    bfd2:	41 89 f4             	mov    r12d,esi
    bfd5:	49 89 f6             	mov    r14,rsi
    bfd8:	83 fe 02             	cmp    esi,0x2
    bfdb:	72 4c                	jb     c029 <zbtScoreLeafBuild+0xa9>
    bfdd:	bf 01 00 00 00       	mov    edi,0x1
    bfe2:	31 c9                	xor    ecx,ecx
    bfe4:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    bfe8:	48 89 f2             	mov    rdx,rsi
    bfeb:	eb 26                	jmp    c013 <zbtScoreLeafBuild+0x93>
    bfed:	0f 1f 00             	nop    DWORD PTR [rax]
    bff0:	49 09 d8             	or     r8,rbx
    bff3:	4d 89 c1             	mov    r9,r8
    bff6:	4c 33 4d b8          	xor    r9,QWORD PTR [rbp-0x48]
    bffa:	4c 09 c9             	or     rcx,r9
    bffd:	49 39 d0             	cmp    r8,rdx
    c000:	49 0f 42 d0          	cmovb  rdx,r8
    c004:	49 39 f0             	cmp    r8,rsi
    c007:	49 0f 47 f0          	cmova  rsi,r8
    c00b:	48 ff c7             	inc    rdi
    c00e:	49 39 fc             	cmp    r12,rdi
    c011:	74 1f                	je     c032 <zbtScoreLeafBuild+0xb2>
    c013:	f3 41 0f 7e 44 fd 00 	movq   xmm0,QWORD PTR [r13+rdi*8+0x0]
    c01a:	66 49 0f 7e c0       	movq   r8,xmm0
    c01f:	4d 85 c0             	test   r8,r8
    c022:	79 cc                	jns    bff0 <zbtScoreLeafBuild+0x70>
    c024:	49 f7 d0             	not    r8
    c027:	eb ca                	jmp    bff3 <zbtScoreLeafBuild+0x73>
    c029:	c7 45 d4 00 00 00 00 	mov    DWORD PTR [rbp-0x2c],0x0
    c030:	eb 59                	jmp    c08b <zbtScoreLeafBuild+0x10b>
    c032:	45 31 c0             	xor    r8d,r8d
    c035:	48 85 c9             	test   rcx,rcx
    c038:	74 46                	je     c080 <zbtScoreLeafBuild+0x100>
    c03a:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c03f:	48 29 d6             	sub    rsi,rdx
    c042:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    c046:	48 d3 ee             	shr    rsi,cl
    c049:	48 0f bd ce          	bsr    rcx,rsi
    c04d:	83 f1 3f             	xor    ecx,0x3f
    c050:	40 b7 40             	mov    dil,0x40
    c053:	40 28 cf             	sub    dil,cl
    c056:	48 85 f6             	test   rsi,rsi
    c059:	40 0f b6 cf          	movzx  ecx,dil
    c05d:	41 0f 44 c8          	cmove  ecx,r8d
    c061:	48 89 55 b8          	mov    QWORD PTR [rbp-0x48],rdx
    c065:	89 4d d4             	mov    DWORD PTR [rbp-0x2c],ecx
    c068:	48 85 c0             	test   rax,rax
    c06b:	79 29                	jns    c096 <zbtScoreLeafBuild+0x116>
    c06d:	48 f7 d0             	not    rax
    c070:	ba 38 00 00 00       	mov    edx,0x38
    c075:	41 83 fe 02          	cmp    r14d,0x2
    c079:	73 2d                	jae    c0a8 <zbtScoreLeafBuild+0x128>
    c07b:	e9 ba 00 00 00       	jmp    c13a <zbtScoreLeafBuild+0x1ba>
    c080:	c7 45 d4 00 00 00 00 	mov    DWORD PTR [rbp-0x2c],0x0
    c087:	48 89 55 b8          	mov    QWORD PTR [rbp-0x48],rdx
    c08b:	31 c9                	xor    ecx,ecx
    c08d:	48 89 4d c8          	mov    QWORD PTR [rbp-0x38],rcx
    c091:	48 85 c0             	test   rax,rax
    c094:	78 d7                	js     c06d <zbtScoreLeafBuild+0xed>
    c096:	48 09 d8             	or     rax,rbx
    c099:	ba 38 00 00 00       	mov    edx,0x38
    c09e:	41 83 fe 02          	cmp    r14d,0x2
    c0a2:	0f 82 92 00 00 00    	jb     c13a <zbtScoreLeafBuild+0x1ba>
    c0a8:	41 b8 01 00 00 00    	mov    r8d,0x1
    c0ae:	31 c9                	xor    ecx,ecx
    c0b0:	48 89 c7             	mov    rdi,rax
    c0b3:	48 89 c6             	mov    rsi,rax
    c0b6:	eb 2a                	jmp    c0e2 <zbtScoreLeafBuild+0x162>
    c0b8:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    c0bf:	00
    c0c0:	49 09 d9             	or     r9,rbx
    c0c3:	4d 89 ca             	mov    r10,r9
    c0c6:	49 31 c2             	xor    r10,rax
    c0c9:	4c 09 d1             	or     rcx,r10
    c0cc:	49 39 f9             	cmp    r9,rdi
    c0cf:	49 0f 42 f9          	cmovb  rdi,r9
    c0d3:	49 39 f1             	cmp    r9,rsi
    c0d6:	49 0f 47 f1          	cmova  rsi,r9
    c0da:	49 ff c0             	inc    r8
    c0dd:	4d 39 c4             	cmp    r12,r8
    c0e0:	74 16                	je     c0f8 <zbtScoreLeafBuild+0x178>
    c0e2:	f3 43 0f 7e 44 c5 00 	movq   xmm0,QWORD PTR [r13+r8*8+0x0]
    c0e9:	66 49 0f 7e c1       	movq   r9,xmm0
    c0ee:	4d 85 c9             	test   r9,r9
    c0f1:	79 cd                	jns    c0c0 <zbtScoreLeafBuild+0x140>
    c0f3:	49 f7 d1             	not    r9
    c0f6:	eb cb                	jmp    c0c3 <zbtScoreLeafBuild+0x143>
    c0f8:	48 85 c9             	test   rcx,rcx
    c0fb:	74 3d                	je     c13a <zbtScoreLeafBuild+0x1ba>
    c0fd:	f3 48 0f bc c9       	tzcnt  rcx,rcx
    c102:	48 29 fe             	sub    rsi,rdi
    c105:	48 d3 ee             	shr    rsi,cl
    c108:	48 85 f6             	test   rsi,rsi
    c10b:	74 2d                	je     c13a <zbtScoreLeafBuild+0x1ba>
    c10d:	48 0f bd c6          	bsr    rax,rsi
    c111:	48 83 f0 c0          	xor    rax,0xffffffffffffffc0
    c115:	48 83 c0 41          	add    rax,0x41
    c119:	49 0f af c4          	imul   rax,r12
    c11d:	48 83 c0 07          	add    rax,0x7
    c121:	48 c1 e8 03          	shr    rax,0x3
    c125:	48 83 c0 09          	add    rax,0x9
    c129:	48 ba fe ff ff ff ff 	movabs rdx,0x1ffffffffffffffe
    c130:	ff ff 1f
    c133:	48 21 c2             	and    rdx,rax
    c136:	48 83 c2 38          	add    rdx,0x38
    c13a:	8b 45 10             	mov    eax,DWORD PTR [rbp+0x10]
    c13d:	4b 8d 1c 64          	lea    rbx,[r12+r12*2]
    c141:	48 01 d3             	add    rbx,rdx
    c144:	45 85 f6             	test   r14d,r14d
    c147:	74 54                	je     c19d <zbtScoreLeafBuild+0x21d>
    c149:	4a 8d 0c e5 00 00 00 	lea    rcx,[r12*8+0x0]
    c150:	00
    c151:	48 8d 0c 89          	lea    rcx,[rcx+rcx*4]
    c155:	31 d2                	xor    edx,edx
    c157:	eb 13                	jmp    c16c <zbtScoreLeafBuild+0x1ec>
    c159:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    c160:	48 01 f3             	add    rbx,rsi
    c163:	48 83 c2 28          	add    rdx,0x28
    c167:	48 39 d1             	cmp    rcx,rdx
    c16a:	74 31                	je     c19d <zbtScoreLeafBuild+0x21d>
    c16c:	be 15 00 00 00       	mov    esi,0x15
    c171:	49 83 7c 13 18 00    	cmp    QWORD PTR [r11+rdx*1+0x18],0x0
    c177:	75 e7                	jne    c160 <zbtScoreLeafBuild+0x1e0>
    c179:	49 8b 7c 13 08       	mov    rdi,QWORD PTR [r11+rdx*1+0x8]
    c17e:	48 81 ff 3f 01 00 00 	cmp    rdi,0x13f
    c185:	77 d9                	ja     c160 <zbtScoreLeafBuild+0x1e0>
    c187:	31 f6                	xor    esi,esi
    c189:	48 81 ff fe 00 00 00 	cmp    rdi,0xfe
    c190:	40 0f 93 c6          	setae  sil
    c194:	48 8d 34 77          	lea    rsi,[rdi+rsi*2]
    c198:	48 ff c6             	inc    rsi
    c19b:	eb c3                	jmp    c160 <zbtScoreLeafBuild+0x1e0>
    c19d:	4c 89 65 90          	mov    QWORD PTR [rbp-0x70],r12
    c1a1:	4c 89 5d c0          	mov    QWORD PTR [rbp-0x40],r11
    c1a5:	85 c0                	test   eax,eax
    c1a7:	4d 89 f4             	mov    r12,r14
    c1aa:	74 0e                	je     c1ba <zbtScoreLeafBuild+0x23a>
    c1ac:	bf ff 0f 00 00       	mov    edi,0xfff
    c1b1:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c1b8:	72 29                	jb     c1e3 <zbtScoreLeafBuild+0x263>
    c1ba:	48 89 df             	mov    rdi,rbx
    c1bd:	41 83 fc 5f          	cmp    r12d,0x5f
    c1c1:	77 20                	ja     c1e3 <zbtScoreLeafBuild+0x263>
    c1c3:	48 89 df             	mov    rdi,rbx
    c1c6:	48 81 fb ff 0f 00 00 	cmp    rbx,0xfff
    c1cd:	77 14                	ja     c1e3 <zbtScoreLeafBuild+0x263>
    c1cf:	48 81 fb 7f 0f 00 00 	cmp    rbx,0xf7f
    c1d6:	bf 7f 0f 00 00       	mov    edi,0xf7f
    c1db:	48 0f 42 fb          	cmovb  rdi,rbx
    c1df:	48 83 ef 80          	sub    rdi,0xffffffffffffff80
    c1e3:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    c1e7:	e8 c4 55 00 00       	call   117b0 <zmalloc_usable>
    c1ec:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    c1f0:	49 01 4f 68          	add    QWORD PTR [r15+0x68],rcx
    c1f4:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    c1f8:	41 8d 44 24 ff       	lea    eax,[r12-0x1]
    c1fd:	83 f8 60             	cmp    eax,0x60
    c200:	72 18                	jb     c21a <zbtScoreLeafBuild+0x29a>
    c202:	48 8d 3d 15 74 00 00 	lea    rdi,[rip+0x7415]        # 1361e <_IO_stdin_used+0x61e>
    c209:	48 8d 15 b6 75 00 00 	lea    rdx,[rip+0x75b6]        # 137c6 <_IO_stdin_used+0x7c6>
    c210:	be de 03 00 00       	mov    esi,0x3de
    c215:	e8 96 54 00 00       	call   116b0 <standalone_panic>
    c21a:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c221:	72 18                	jb     c23b <zbtScoreLeafBuild+0x2bb>
    c223:	48 8d 3d f4 73 00 00 	lea    rdi,[rip+0x73f4]        # 1361e <_IO_stdin_used+0x61e>
    c22a:	48 8d 15 be 75 00 00 	lea    rdx,[rip+0x75be]        # 137ef <_IO_stdin_used+0x7ef>
    c231:	be df 03 00 00       	mov    esi,0x3df
    c236:	e8 75 54 00 00       	call   116b0 <standalone_panic>
    c23b:	4c 89 7d 88          	mov    QWORD PTR [rbp-0x78],r15
    c23f:	66 0f ef c0          	pxor   xmm0,xmm0
    c243:	48 8b 55 b0          	mov    rdx,QWORD PTR [rbp-0x50]
    c247:	f3 0f 7f 42 10       	movdqu XMMWORD PTR [rdx+0x10],xmm0
    c24c:	f3 0f 7f 02          	movdqu XMMWORD PTR [rdx],xmm0
    c250:	f3 0f 7f 42 20       	movdqu XMMWORD PTR [rdx+0x20],xmm0
    c255:	48 c7 42 30 00 00 00 	mov    QWORD PTR [rdx+0x30],0x0
    c25c:	00
    c25d:	c6 42 12 01          	mov    BYTE PTR [rdx+0x12],0x1
    c261:	44 88 62 11          	mov    BYTE PTR [rdx+0x11],r12b
    c265:	48 8b 4d 90          	mov    rcx,QWORD PTR [rbp-0x70]
    c269:	48 89 4a 08          	mov    QWORD PTR [rdx+0x8],rcx
    c26d:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    c271:	88 42 13             	mov    BYTE PTR [rdx+0x13],al
    c274:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    c278:	48 89 42 28          	mov    QWORD PTR [rdx+0x28],rax
    c27c:	8b 45 d4             	mov    eax,DWORD PTR [rbp-0x2c]
    c27f:	88 42 34             	mov    BYTE PTR [rdx+0x34],al
    c282:	48 8d 7a 38          	lea    rdi,[rdx+0x38]
    c286:	44 0f b6 c0          	movzx  r8d,al
    c28a:	45 84 c0             	test   r8b,r8b
    c28d:	4c 89 45 a8          	mov    QWORD PTR [rbp-0x58],r8
    c291:	48 89 7d 80          	mov    QWORD PTR [rbp-0x80],rdi
    c295:	74 59                	je     c2f0 <zbtScoreLeafBuild+0x370>
    c297:	4c 89 c0             	mov    rax,r8
    c29a:	48 0f af c1          	imul   rax,rcx
    c29e:	48 83 c0 07          	add    rax,0x7
    c2a2:	48 c1 e8 03          	shr    rax,0x3
    c2a6:	48 83 c0 09          	add    rax,0x9
    c2aa:	48 ba fe ff ff ff 3f 	movabs rdx,0x3ffffffffe
    c2b1:	00 00 00
    c2b4:	48 21 c2             	and    rdx,rax
    c2b7:	31 f6                	xor    esi,esi
    c2b9:	48 89 fb             	mov    rbx,rdi
    c2bc:	4d 89 c6             	mov    r14,r8
    c2bf:	e8 ec 4d ff ff       	call   10b0 <memset@plt>
    c2c4:	45 0f b6 fc          	movzx  r15d,r12b
    c2c8:	4c 89 f8             	mov    rax,r15
    c2cb:	4c 89 7d 98          	mov    QWORD PTR [rbp-0x68],r15
    c2cf:	45 0f af fe          	imul   r15d,r14d
    c2d3:	41 83 c7 07          	add    r15d,0x7
    c2d7:	41 c1 ef 03          	shr    r15d,0x3
    c2db:	41 83 c7 09          	add    r15d,0x9
    c2df:	41 83 e7 fe          	and    r15d,0xfffffffe
    c2e3:	4a 8d 04 3b          	lea    rax,[rbx+r15*1]
    c2e7:	48 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rax
    c2ee:	eb 12                	jmp    c302 <zbtScoreLeafBuild+0x382>
    c2f0:	41 0f b6 c4          	movzx  eax,r12b
    c2f4:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
    c2f8:	45 31 ff             	xor    r15d,r15d
    c2fb:	48 89 bd 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdi
    c302:	4d 89 e6             	mov    r14,r12
    c305:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c309:	4c 89 e7             	mov    rdi,r12
    c30c:	e8 cf 53 00 00       	call   116e0 <zmalloc_usable_size>
    c311:	48 3d ff 0f 00 00    	cmp    rax,0xfff
    c317:	bb ff 0f 00 00       	mov    ebx,0xfff
    c31c:	48 0f 42 d8          	cmovb  rbx,rax
    c320:	45 85 f6             	test   r14d,r14d
    c323:	0f 84 91 02 00 00    	je     c5ba <zbtScoreLeafBuild+0x63a>
    c329:	4c 89 ad 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],r13
    c330:	4c 03 7d 80          	add    r15,QWORD PTR [rbp-0x80]
    c334:	48 8b 45 98          	mov    rax,QWORD PTR [rbp-0x68]
    c338:	49 8d 04 47          	lea    rax,[r15+rax*2]
    c33c:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
    c340:	4c 01 e3             	add    rbx,r12
    c343:	0f b6 45 c8          	movzx  eax,BYTE PTR [rbp-0x38]
    c347:	48 89 85 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],rax
    c34e:	45 31 ff             	xor    r15d,r15d
    c351:	45 31 ed             	xor    r13d,r13d
    c354:	49 89 da             	mov    r10,rbx
    c357:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c35b:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    c35f:	eb 42                	jmp    c3a3 <zbtScoreLeafBuild+0x423>
    c361:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    c368:	0f 1f 84 00 00 00 00
    c36f:	00
    c370:	49 c7 46 0d 00 00 00 	mov    QWORD PTR [r14+0xd],0x0
    c377:	00
    c378:	66 0f ef c0          	pxor   xmm0,xmm0
    c37c:	f3 41 0f 7f 04 24    	movdqu XMMWORD PTR [r12],xmm0
    c382:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c386:	41 c6 44 24 14 01    	mov    BYTE PTR [r12+0x14],0x1
    c38c:	4c 8b 75 90          	mov    r14,QWORD PTR [rbp-0x70]
    c390:	49 ff c5             	inc    r13
    c393:	49 83 c0 28          	add    r8,0x28
    c397:	4d 01 cf             	add    r15,r9
    c39a:	4d 39 ee             	cmp    r14,r13
    c39d:	0f 84 17 02 00 00    	je     c5ba <zbtScoreLeafBuild+0x63a>
    c3a3:	48 c7 c0 eb ff ff ff 	mov    rax,0xffffffffffffffeb
    c3aa:	49 83 78 18 00       	cmp    QWORD PTR [r8+0x18],0x0
    c3af:	74 0f                	je     c3c0 <zbtScoreLeafBuild+0x440>
    c3b1:	48 be 00 00 00 00 00 	movabs rsi,0x8000000000000000
    c3b8:	00 00 80
    c3bb:	8b 55 d4             	mov    edx,DWORD PTR [rbp-0x2c]
    c3be:	eb 30                	jmp    c3f0 <zbtScoreLeafBuild+0x470>
    c3c0:	49 8b 48 08          	mov    rcx,QWORD PTR [r8+0x8]
    c3c4:	48 81 f9 3f 01 00 00 	cmp    rcx,0x13f
    c3cb:	48 be 00 00 00 00 00 	movabs rsi,0x8000000000000000
    c3d2:	00 00 80
    c3d5:	8b 55 d4             	mov    edx,DWORD PTR [rbp-0x2c]
    c3d8:	77 16                	ja     c3f0 <zbtScoreLeafBuild+0x470>
    c3da:	48 81 f9 fe 00 00 00 	cmp    rcx,0xfe
    c3e1:	b8 00 00 00 00       	mov    eax,0x0
    c3e6:	48 19 c0             	sbb    rax,rax
    c3e9:	48 83 c8 fd          	or     rax,0xfffffffffffffffd
    c3ed:	48 29 c8             	sub    rax,rcx
    c3f0:	84 d2                	test   dl,dl
    c3f2:	74 6c                	je     c460 <zbtScoreLeafBuild+0x4e0>
    c3f4:	48 8b 8d 58 ff ff ff 	mov    rcx,QWORD PTR [rbp-0xa8]
    c3fb:	f3 42 0f 7e 04 e9    	movq   xmm0,QWORD PTR [rcx+r13*8]
    c401:	66 48 0f 7e c2       	movq   rdx,xmm0
    c406:	48 85 d2             	test   rdx,rdx
    c409:	78 05                	js     c410 <zbtScoreLeafBuild+0x490>
    c40b:	48 09 f2             	or     rdx,rsi
    c40e:	eb 03                	jmp    c413 <zbtScoreLeafBuild+0x493>
    c410:	48 f7 d2             	not    rdx
    c413:	48 2b 55 b8          	sub    rdx,QWORD PTR [rbp-0x48]
    c417:	48 8b 8d 60 ff ff ff 	mov    rcx,QWORD PTR [rbp-0xa0]
    c41e:	48 d3 ea             	shr    rdx,cl
    c421:	4c 89 fe             	mov    rsi,r15
    c424:	44 89 f9             	mov    ecx,r15d
    c427:	80 e1 07             	and    cl,0x7
    c42a:	48 89 d7             	mov    rdi,rdx
    c42d:	48 d3 e7             	shl    rdi,cl
    c430:	48 c1 ee 03          	shr    rsi,0x3
    c434:	48 8b 4d 80          	mov    rcx,QWORD PTR [rbp-0x80]
    c438:	48 09 3c 31          	or     QWORD PTR [rcx+rsi*1],rdi
    c43c:	44 89 ff             	mov    edi,r15d
    c43f:	83 e7 07             	and    edi,0x7
    c442:	74 1c                	je     c460 <zbtScoreLeafBuild+0x4e0>
    c444:	b9 40 00 00 00       	mov    ecx,0x40
    c449:	29 f9                	sub    ecx,edi
    c44b:	44 39 c9             	cmp    ecx,r9d
    c44e:	73 10                	jae    c460 <zbtScoreLeafBuild+0x4e0>
    c450:	48 d3 ea             	shr    rdx,cl
    c453:	42 08 54 26 40       	or     BYTE PTR [rsi+r12*1+0x40],dl
    c458:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
    c45f:	00
    c460:	49 01 c2             	add    r10,rax
    c463:	4c 89 d3             	mov    rbx,r10
    c466:	4c 29 e3             	sub    rbx,r12
    c469:	48 81 fb 00 10 00 00 	cmp    rbx,0x1000
    c470:	4c 89 45 c0          	mov    QWORD PTR [rbp-0x40],r8
    c474:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    c478:	7c 24                	jl     c49e <zbtScoreLeafBuild+0x51e>
    c47a:	48 8d 3d 9d 71 00 00 	lea    rdi,[rip+0x719d]        # 1361e <_IO_stdin_used+0x61e>
    c481:	be 03 04 00 00       	mov    esi,0x403
    c486:	48 8d 15 82 73 00 00 	lea    rdx,[rip+0x7382]        # 1380f <_IO_stdin_used+0x80f>
    c48d:	e8 1e 52 00 00       	call   116b0 <standalone_panic>
    c492:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    c496:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    c49a:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c49e:	4d 8d 60 18          	lea    r12,[r8+0x18]
    c4a2:	48 8b 85 78 ff ff ff 	mov    rax,QWORD PTR [rbp-0x88]
    c4a9:	66 42 89 1c 68       	mov    WORD PTR [rax+r13*2],bx
    c4ae:	48 8b 85 50 ff ff ff 	mov    rax,QWORD PTR [rbp-0xb0]
    c4b5:	42 0f b6 04 28       	movzx  eax,BYTE PTR [rax+r13*1]
    c4ba:	48 8b 4d 98          	mov    rcx,QWORD PTR [rbp-0x68]
    c4be:	42 88 04 29          	mov    BYTE PTR [rcx+r13*1],al
    c4c2:	4d 8b 34 24          	mov    r14,QWORD PTR [r12]
    c4c6:	4d 85 f6             	test   r14,r14
    c4c9:	75 67                	jne    c532 <zbtScoreLeafBuild+0x5b2>
    c4cb:	49 8b 50 08          	mov    rdx,QWORD PTR [r8+0x8]
    c4cf:	48 81 fa 3f 01 00 00 	cmp    rdx,0x13f
    c4d6:	77 1c                	ja     c4f4 <zbtScoreLeafBuild+0x574>
    c4d8:	49 8b 30             	mov    rsi,QWORD PTR [r8]
    c4db:	48 81 fa fd 00 00 00 	cmp    rdx,0xfd
    c4e2:	0f 87 a2 00 00 00    	ja     c58a <zbtScoreLeafBuild+0x60a>
    c4e8:	bf 01 00 00 00       	mov    edi,0x1
    c4ed:	89 d0                	mov    eax,edx
    c4ef:	e9 a2 00 00 00       	jmp    c596 <zbtScoreLeafBuild+0x616>
    c4f4:	48 89 d7             	mov    rdi,rdx
    c4f7:	48 8d 75 a0          	lea    rsi,[rbp-0x60]
    c4fb:	e8 b0 52 00 00       	call   117b0 <zmalloc_usable>
    c500:	48 8b 4d a0          	mov    rcx,QWORD PTR [rbp-0x60]
    c504:	48 8b 55 88          	mov    rdx,QWORD PTR [rbp-0x78]
    c508:	48 01 4a 68          	add    QWORD PTR [rdx+0x68],rcx
    c50c:	49 89 c6             	mov    r14,rax
    c50f:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c513:	48 8b 30             	mov    rsi,QWORD PTR [rax]
    c516:	48 8b 45 c0          	mov    rax,QWORD PTR [rbp-0x40]
    c51a:	48 8b 50 08          	mov    rdx,QWORD PTR [rax+0x8]
    c51e:	4c 89 f7             	mov    rdi,r14
    c521:	e8 fa 4b ff ff       	call   1120 <memcpy@plt>
    c526:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    c52a:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    c52e:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c532:	49 8b 40 08          	mov    rax,QWORD PTR [r8+0x8]
    c536:	41 c6 02 ff          	mov    BYTE PTR [r10],0xff
    c53a:	41 8b 48 10          	mov    ecx,DWORD PTR [r8+0x10]
    c53e:	41 89 4a 01          	mov    DWORD PTR [r10+0x1],ecx
    c542:	49 89 42 05          	mov    QWORD PTR [r10+0x5],rax
    c546:	4d 89 72 0d          	mov    QWORD PTR [r10+0xd],r14
    c54a:	4d 8b 70 20          	mov    r14,QWORD PTR [r8+0x20]
    c54e:	4d 85 f6             	test   r14,r14
    c551:	0f 84 21 fe ff ff    	je     c378 <zbtScoreLeafBuild+0x3f8>
    c557:	41 80 3e ff          	cmp    BYTE PTR [r14],0xff
    c55b:	0f 84 0f fe ff ff    	je     c370 <zbtScoreLeafBuild+0x3f0>
    c561:	48 8d 3d b6 70 00 00 	lea    rdi,[rip+0x70b6]        # 1361e <_IO_stdin_used+0x61e>
    c568:	be 45 02 00 00       	mov    esi,0x245
    c56d:	48 8d 15 e2 71 00 00 	lea    rdx,[rip+0x71e2]        # 13756 <_IO_stdin_used+0x756>
    c574:	e8 37 51 00 00       	call   116b0 <standalone_panic>
    c579:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    c57d:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    c581:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c585:	e9 e6 fd ff ff       	jmp    c370 <zbtScoreLeafBuild+0x3f0>
    c58a:	66 41 89 52 01       	mov    WORD PTR [r10+0x1],dx
    c58f:	bf 03 00 00 00       	mov    edi,0x3
    c594:	b0 fe                	mov    al,0xfe
    c596:	4c 8b 75 90          	mov    r14,QWORD PTR [rbp-0x70]
    c59a:	4c 8b 65 b0          	mov    r12,QWORD PTR [rbp-0x50]
    c59e:	41 88 02             	mov    BYTE PTR [r10],al
    c5a1:	4c 01 d7             	add    rdi,r10
    c5a4:	e8 77 4b ff ff       	call   1120 <memcpy@plt>
    c5a9:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    c5ad:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    c5b1:	4c 8b 4d a8          	mov    r9,QWORD PTR [rbp-0x58]
    c5b5:	e9 d6 fd ff ff       	jmp    c390 <zbtScoreLeafBuild+0x410>
    c5ba:	66 41 89 5c 24 36    	mov    WORD PTR [r12+0x36],bx
    c5c0:	4c 8b b5 68 ff ff ff 	mov    r14,QWORD PTR [rbp-0x98]
    c5c7:	41 83 fe ff          	cmp    r14d,0xffffffff
    c5cb:	4c 8b 7d 88          	mov    r15,QWORD PTR [rbp-0x78]
    c5cf:	74 25                	je     c5f6 <zbtScoreLeafBuild+0x676>
    c5d1:	45 89 74 24 30       	mov    DWORD PTR [r12+0x30],r14d
    c5d6:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c5da:	44 89 f1             	mov    ecx,r14d
    c5dd:	4c 89 24 c8          	mov    QWORD PTR [rax+rcx*8],r12
    c5e1:	4c 89 e0             	mov    rax,r12
    c5e4:	48 81 c4 88 00 00 00 	add    rsp,0x88
    c5eb:	5b                   	pop    rbx
    c5ec:	41 5c                	pop    r12
    c5ee:	41 5d                	pop    r13
    c5f0:	41 5e                	pop    r14
    c5f2:	41 5f                	pop    r15
    c5f4:	5d                   	pop    rbp
    c5f5:	c3                   	ret
    c5f6:	45 8b 77 58          	mov    r14d,DWORD PTR [r15+0x58]
    c5fa:	45 85 f6             	test   r14d,r14d
    c5fd:	74 07                	je     c606 <zbtScoreLeafBuild+0x686>
    c5ff:	49 83 7f 40 00       	cmp    QWORD PTR [r15+0x40],0x0
    c604:	74 7b                	je     c681 <zbtScoreLeafBuild+0x701>
    c606:	45 8b 77 54          	mov    r14d,DWORD PTR [r15+0x54]
    c60a:	41 8d 46 01          	lea    eax,[r14+0x1]
    c60e:	41 89 47 54          	mov    DWORD PTR [r15+0x54],eax
    c612:	45 3b 77 50          	cmp    r14d,DWORD PTR [r15+0x50]
    c616:	75 b9                	jne    c5d1 <zbtScoreLeafBuild+0x651>
    c618:	43 8d 04 36          	lea    eax,[r14+r14*1]
    c61c:	45 85 f6             	test   r14d,r14d
    c61f:	bb 10 00 00 00       	mov    ebx,0x10
    c624:	0f 45 d8             	cmovne ebx,eax
    c627:	48 c7 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],0x0
    c62e:	00 00 00 00
    c632:	49 8b 7f 48          	mov    rdi,QWORD PTR [r15+0x48]
    c636:	48 8d 34 dd 00 00 00 	lea    rsi,[rbx*8+0x0]
    c63d:	00
    c63e:	48 8d 55 a0          	lea    rdx,[rbp-0x60]
    c642:	48 8d 8d 70 ff ff ff 	lea    rcx,[rbp-0x90]
    c649:	e8 d2 51 00 00       	call   11820 <zrealloc_usable>
    c64e:	49 89 47 48          	mov    QWORD PTR [r15+0x48],rax
    c652:	41 8b 4f 50          	mov    ecx,DWORD PTR [r15+0x50]
    c656:	48 8d 3c c8          	lea    rdi,[rax+rcx*8]
    c65a:	89 da                	mov    edx,ebx
    c65c:	29 ca                	sub    edx,ecx
    c65e:	48 c1 e2 03          	shl    rdx,0x3
    c662:	31 f6                	xor    esi,esi
    c664:	e8 47 4a ff ff       	call   10b0 <memset@plt>
    c669:	41 89 5f 50          	mov    DWORD PTR [r15+0x50],ebx
    c66d:	48 8b 45 a0          	mov    rax,QWORD PTR [rbp-0x60]
    c671:	48 2b 85 70 ff ff ff 	sub    rax,QWORD PTR [rbp-0x90]
    c678:	49 01 47 68          	add    QWORD PTR [r15+0x68],rax
    c67c:	e9 50 ff ff ff       	jmp    c5d1 <zbtScoreLeafBuild+0x651>
    c681:	41 ff ce             	dec    r14d
    c684:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c688:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c68c:	a8 01                	test   al,0x1
    c68e:	75 20                	jne    c6b0 <zbtScoreLeafBuild+0x730>
    c690:	48 8d 3d 87 6f 00 00 	lea    rdi,[rip+0x6f87]        # 1361e <_IO_stdin_used+0x61e>
    c697:	48 8d 15 a8 71 00 00 	lea    rdx,[rip+0x71a8]        # 13846 <_IO_stdin_used+0x846>
    c69e:	be 25 03 00 00       	mov    esi,0x325
    c6a3:	e8 08 50 00 00       	call   116b0 <standalone_panic>
    c6a8:	49 8b 47 48          	mov    rax,QWORD PTR [r15+0x48]
    c6ac:	4a 8b 04 f0          	mov    rax,QWORD PTR [rax+r14*8]
    c6b0:	48 d1 e8             	shr    rax,1
    c6b3:	41 89 47 58          	mov    DWORD PTR [r15+0x58],eax
    c6b7:	e9 15 ff ff ff       	jmp    c5d1 <zbtScoreLeafBuild+0x651>

Disassembly of section .fini:
