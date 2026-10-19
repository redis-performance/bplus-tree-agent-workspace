
scratch/amd-scan-build/A/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000010da0 <zbtIndexScanSlot>:
   10da0:	55                   	push   %rbp
   10da1:	48 89 e5             	mov    %rsp,%rbp
   10da4:	41 57                	push   %r15
   10da6:	41 56                	push   %r14
   10da8:	41 55                	push   %r13
   10daa:	41 54                	push   %r12
   10dac:	53                   	push   %rbx
   10dad:	48 81 ec d8 01 00 00 	sub    $0x1d8,%rsp
   10db4:	89 c8                	mov    %ecx,%eax
   10db6:	49 89 d3             	mov    %rdx,%r11
   10db9:	49 89 f5             	mov    %rsi,%r13
   10dbc:	4c 8b 22             	mov    (%rdx),%r12
   10dbf:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   10dc6:	49 d3 ec             	shr    %cl,%r12
   10dc9:	49 89 ff             	mov    %rdi,%r15
   10dcc:	8b 56 20             	mov    0x20(%rsi),%edx
   10dcf:	89 c0                	mov    %eax,%eax
   10dd1:	85 d2                	test   %edx,%edx
   10dd3:	74 18                	je     10ded <zbtIndexScanSlot+0x4d>
   10dd5:	45 8b 74 83 10       	mov    0x10(%r11,%rax,4),%r14d
   10dda:	31 c0                	xor    %eax,%eax
   10ddc:	4c 89 e3             	mov    %r12,%rbx
   10ddf:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10de6:	75 2d                	jne    10e15 <zbtIndexScanSlot+0x75>
   10de8:	e9 79 01 00 00       	jmp    10f66 <zbtIndexScanSlot+0x1c6>
   10ded:	41 0f b7 4c 43 10    	movzwl 0x10(%r11,%rax,2),%ecx
   10df3:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   10df9:	41 be ff ff ff ff    	mov    $0xffffffff,%r14d
   10dff:	44 0f 45 f1          	cmovne %ecx,%r14d
   10e03:	31 c0                	xor    %eax,%eax
   10e05:	4c 89 e3             	mov    %r12,%rbx
   10e08:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10e0f:	0f 84 51 01 00 00    	je     10f66 <zbtIndexScanSlot+0x1c6>
   10e15:	41 83 fe ff          	cmp    $0xffffffff,%r14d
   10e19:	0f 84 47 01 00 00    	je     10f66 <zbtIndexScanSlot+0x1c6>
   10e1f:	4d 85 c9             	test   %r9,%r9
   10e22:	0f 84 7c 00 00 00    	je     10ea4 <zbtIndexScanSlot+0x104>
   10e28:	49 ba 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%r10
   10e2f:	79 37 9e
   10e32:	4c 0f af d3          	imul   %rbx,%r10
   10e36:	4c 89 d1             	mov    %r10,%rcx
   10e39:	48 c1 e9 3a          	shr    $0x3a,%rcx
   10e3d:	be 01 00 00 00       	mov    $0x1,%esi
   10e42:	48 d3 e6             	shl    %cl,%rsi
   10e45:	4c 89 c7             	mov    %r8,%rdi
   10e48:	4d 39 c8             	cmp    %r9,%r8
   10e4b:	73 4e                	jae    10e9b <zbtIndexScanSlot+0xfb>
   10e4d:	4c 0f ab e6          	bts    %r12,%rsi
   10e51:	49 c1 ea 24          	shr    $0x24,%r10
   10e55:	4c 0f ab d6          	bts    %r10,%rsi
   10e59:	31 c9                	xor    %ecx,%ecx
   10e5b:	85 d2                	test   %edx,%edx
   10e5d:	0f 95 c1             	setne  %cl
   10e60:	49 8b 55 00          	mov    0x0(%r13),%rdx
   10e64:	c1 e1 04             	shl    $0x4,%ecx
   10e67:	48 83 c9 20          	or     $0x20,%rcx
   10e6b:	48 89 cf             	mov    %rcx,%rdi
   10e6e:	49 0f af f8          	imul   %r8,%rdi
   10e72:	48 01 fa             	add    %rdi,%rdx
   10e75:	48 83 c2 08          	add    $0x8,%rdx
   10e79:	31 c0                	xor    %eax,%eax
   10e7b:	4c 89 c7             	mov    %r8,%rdi
   10e7e:	66 90                	xchg   %ax,%ax
   10e80:	4c 8b 12             	mov    (%rdx),%r10
   10e83:	49 f7 d2             	not    %r10
   10e86:	4c 85 d6             	test   %r10,%rsi
   10e89:	74 10                	je     10e9b <zbtIndexScanSlot+0xfb>
   10e8b:	48 ff c7             	inc    %rdi
   10e8e:	48 01 ca             	add    %rcx,%rdx
   10e91:	49 39 f9             	cmp    %rdi,%r9
   10e94:	75 ea                	jne    10e80 <zbtIndexScanSlot+0xe0>
   10e96:	e9 cb 00 00 00       	jmp    10f66 <zbtIndexScanSlot+0x1c6>
   10e9b:	4c 39 cf             	cmp    %r9,%rdi
   10e9e:	0f 84 c0 00 00 00    	je     10f64 <zbtIndexScanSlot+0x1c4>
   10ea4:	45 3b 77 54          	cmp    0x54(%r15),%r14d
   10ea8:	0f 83 8e 00 00 00    	jae    10f3c <zbtIndexScanSlot+0x19c>
   10eae:	49 8b 4f 48          	mov    0x48(%r15),%rcx
   10eb2:	44 89 f2             	mov    %r14d,%edx
   10eb5:	48 8b 14 d1          	mov    (%rcx,%rdx,8),%rdx
   10eb9:	48 85 d2             	test   %rdx,%rdx
   10ebc:	74 7e                	je     10f3c <zbtIndexScanSlot+0x19c>
   10ebe:	89 d1                	mov    %edx,%ecx
   10ec0:	83 e1 01             	and    $0x1,%ecx
   10ec3:	75 77                	jne    10f3c <zbtIndexScanSlot+0x19c>
   10ec5:	48 89 55 c8          	mov    %rdx,-0x38(%rbp)
   10ec9:	44 39 72 30          	cmp    %r14d,0x30(%rdx)
   10ecd:	4c 89 45 98          	mov    %r8,-0x68(%rbp)
   10ed1:	4c 89 5d 90          	mov    %r11,-0x70(%rbp)
   10ed5:	74 1e                	je     10ef5 <zbtIndexScanSlot+0x155>
   10ed7:	48 8d 3d 40 27 00 00 	lea    0x2740(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10ede:	48 8d 15 92 28 00 00 	lea    0x2892(%rip),%rdx        # 13777 <_IO_stdin_used+0x777>
   10ee5:	be 6d 10 00 00       	mov    $0x106d,%esi
   10eea:	4d 89 ce             	mov    %r9,%r14
   10eed:	e8 3e 08 00 00       	call   11730 <standalone_panic>
   10ef2:	4d 89 f1             	mov    %r14,%r9
   10ef5:	49 8b 47 40          	mov    0x40(%r15),%rax
   10ef9:	48 85 c0             	test   %rax,%rax
   10efc:	74 19                	je     10f17 <zbtIndexScanSlot+0x177>
   10efe:	48 8b 4d c8          	mov    -0x38(%rbp),%rcx
   10f02:	0f b7 49 16          	movzwl 0x16(%rcx),%ecx
   10f06:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   10f0a:	0f 94 c1             	sete   %cl
   10f0d:	4c 39 e8             	cmp    %r13,%rax
   10f10:	0f 95 c0             	setne  %al
   10f13:	38 c8                	cmp    %cl,%al
   10f15:	74 4d                	je     10f64 <zbtIndexScanSlot+0x1c4>
   10f17:	48 8b 55 c8          	mov    -0x38(%rbp),%rdx
   10f1b:	0f b6 4a 34          	movzbl 0x34(%rdx),%ecx
   10f1f:	45 31 f6             	xor    %r14d,%r14d
   10f22:	0f b6 42 11          	movzbl 0x11(%rdx),%eax
   10f26:	48 85 c9             	test   %rcx,%rcx
   10f29:	74 4d                	je     10f78 <zbtIndexScanSlot+0x1d8>
   10f2b:	0f af c8             	imul   %eax,%ecx
   10f2e:	83 c1 07             	add    $0x7,%ecx
   10f31:	c1 e9 03             	shr    $0x3,%ecx
   10f34:	83 c1 09             	add    $0x9,%ecx
   10f37:	83 e1 fe             	and    $0xfffffffe,%ecx
   10f3a:	eb 3e                	jmp    10f7a <zbtIndexScanSlot+0x1da>
   10f3c:	49 83 7f 40 00       	cmpq   $0x0,0x40(%r15)
   10f41:	74 09                	je     10f4c <zbtIndexScanSlot+0x1ac>
   10f43:	49 83 c7 18          	add    $0x18,%r15
   10f47:	4d 39 ef             	cmp    %r13,%r15
   10f4a:	74 18                	je     10f64 <zbtIndexScanSlot+0x1c4>
   10f4c:	48 8d 3d cb 26 00 00 	lea    0x26cb(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10f53:	48 8d 15 3c 28 00 00 	lea    0x283c(%rip),%rdx        # 13796 <_IO_stdin_used+0x796>
   10f5a:	be 6a 10 00 00       	mov    $0x106a,%esi
   10f5f:	e8 cc 07 00 00       	call   11730 <standalone_panic>
   10f64:	31 c0                	xor    %eax,%eax
   10f66:	48 81 c4 d8 01 00 00 	add    $0x1d8,%rsp
   10f6d:	5b                   	pop    %rbx
   10f6e:	41 5c                	pop    %r12
   10f70:	41 5d                	pop    %r13
   10f72:	41 5e                	pop    %r14
   10f74:	41 5f                	pop    %r15
   10f76:	5d                   	pop    %rbp
   10f77:	c3                   	ret
   10f78:	31 c9                	xor    %ecx,%ecx
   10f7a:	48 01 d1             	add    %rdx,%rcx
   10f7d:	48 83 c1 38          	add    $0x38,%rcx
   10f81:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   10f85:	0f b6 52 35          	movzbl 0x35(%rdx),%edx
   10f89:	88 55 d7             	mov    %dl,-0x29(%rbp)
   10f8c:	8d 70 ff             	lea    -0x1(%rax),%esi
   10f8f:	41 bf 00 00 00 00    	mov    $0x0,%r15d
   10f95:	3c 10                	cmp    $0x10,%al
   10f97:	0f 82 19 01 00 00    	jb     110b6 <zbtIndexScanSlot+0x316>
   10f9d:	4d 89 cb             	mov    %r9,%r11
   10fa0:	41 0f b6 d4          	movzbl %r12b,%edx
   10fa4:	66 0f 6e c2          	movd   %edx,%xmm0
   10fa8:	66 0f 60 c0          	punpcklbw %xmm0,%xmm0
   10fac:	f2 0f 70 c0 00       	pshuflw $0x0,%xmm0,%xmm0
   10fb1:	66 0f 70 c0 00       	pshufd $0x0,%xmm0,%xmm0
   10fb6:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   10fba:	74 7d                	je     11039 <zbtIndexScanSlot+0x299>
   10fbc:	31 ff                	xor    %edi,%edi
   10fbe:	41 b9 10 00 00 00    	mov    $0x10,%r9d
   10fc4:	45 31 ff             	xor    %r15d,%r15d
   10fc7:	eb 18                	jmp    10fe1 <zbtIndexScanSlot+0x241>
   10fc9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   10fd0:	4d 8d 4e 10          	lea    0x10(%r14),%r9
   10fd4:	48 83 c7 10          	add    $0x10,%rdi
   10fd8:	49 39 c1             	cmp    %rax,%r9
   10fdb:	0f 87 d2 00 00 00    	ja     110b3 <zbtIndexScanSlot+0x313>
   10fe1:	4d 89 ce             	mov    %r9,%r14
   10fe4:	f3 0f 6f 0c 39       	movdqu (%rcx,%rdi,1),%xmm1
   10fe9:	66 0f ef d2          	pxor   %xmm2,%xmm2
   10fed:	41 80 fc 01          	cmp    $0x1,%r12b
   10ff1:	75 04                	jne    10ff7 <zbtIndexScanSlot+0x257>
   10ff3:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   10ff7:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   10ffb:	66 0f eb ca          	por    %xmm2,%xmm1
   10fff:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   11004:	45 85 c9             	test   %r9d,%r9d
   11007:	74 c7                	je     10fd0 <zbtIndexScanSlot+0x230>
   11009:	45 0f b7 c9          	movzwl %r9w,%r9d
   1100d:	0f 1f 00             	nopl   (%rax)
   11010:	f3 41 0f bc d1       	tzcnt  %r9d,%edx
   11015:	01 fa                	add    %edi,%edx
   11017:	41 89 f2             	mov    %esi,%r10d
   1101a:	41 29 d2             	sub    %edx,%r10d
   1101d:	44 89 fa             	mov    %r15d,%edx
   11020:	41 ff c7             	inc    %r15d
   11023:	44 89 94 95 00 fe ff 	mov    %r10d,-0x200(%rbp,%rdx,4)
   1102a:	ff
   1102b:	41 8d 51 ff          	lea    -0x1(%r9),%edx
   1102f:	44 21 ca             	and    %r9d,%edx
   11032:	41 89 d1             	mov    %edx,%r9d
   11035:	75 d9                	jne    11010 <zbtIndexScanSlot+0x270>
   11037:	eb 97                	jmp    10fd0 <zbtIndexScanSlot+0x230>
   11039:	31 ff                	xor    %edi,%edi
   1103b:	41 b9 10 00 00 00    	mov    $0x10,%r9d
   11041:	45 31 ff             	xor    %r15d,%r15d
   11044:	eb 17                	jmp    1105d <zbtIndexScanSlot+0x2bd>
   11046:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   1104d:	00 00 00
   11050:	4d 8d 4e 10          	lea    0x10(%r14),%r9
   11054:	48 83 c7 10          	add    $0x10,%rdi
   11058:	49 39 c1             	cmp    %rax,%r9
   1105b:	77 56                	ja     110b3 <zbtIndexScanSlot+0x313>
   1105d:	4d 89 ce             	mov    %r9,%r14
   11060:	f3 0f 6f 0c 39       	movdqu (%rcx,%rdi,1),%xmm1
   11065:	66 0f ef d2          	pxor   %xmm2,%xmm2
   11069:	41 80 fc 01          	cmp    $0x1,%r12b
   1106d:	75 04                	jne    11073 <zbtIndexScanSlot+0x2d3>
   1106f:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   11073:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   11077:	66 0f eb ca          	por    %xmm2,%xmm1
   1107b:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   11080:	45 85 c9             	test   %r9d,%r9d
   11083:	74 cb                	je     11050 <zbtIndexScanSlot+0x2b0>
   11085:	45 0f b7 c9          	movzwl %r9w,%r9d
   11089:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   11090:	f3 41 0f bc d1       	tzcnt  %r9d,%edx
   11095:	01 fa                	add    %edi,%edx
   11097:	45 89 fa             	mov    %r15d,%r10d
   1109a:	41 ff c7             	inc    %r15d
   1109d:	42 89 94 95 00 fe ff 	mov    %edx,-0x200(%rbp,%r10,4)
   110a4:	ff
   110a5:	41 8d 51 ff          	lea    -0x1(%r9),%edx
   110a9:	44 21 ca             	and    %r9d,%edx
   110ac:	41 89 d1             	mov    %edx,%r9d
   110af:	75 df                	jne    11090 <zbtIndexScanSlot+0x2f0>
   110b1:	eb 9d                	jmp    11050 <zbtIndexScanSlot+0x2b0>
   110b3:	4d 89 d9             	mov    %r11,%r9
   110b6:	4c 89 4d b0          	mov    %r9,-0x50(%rbp)
   110ba:	89 c2                	mov    %eax,%edx
   110bc:	c1 ea 03             	shr    $0x3,%edx
   110bf:	41 c1 ee 03          	shr    $0x3,%r14d
   110c3:	48 89 55 c0          	mov    %rdx,-0x40(%rbp)
   110c7:	41 39 d6             	cmp    %edx,%r14d
   110ca:	4c 89 6d a0          	mov    %r13,-0x60(%rbp)
   110ce:	0f 83 b8 01 00 00    	jae    1128c <zbtIndexScanSlot+0x4ec>
   110d4:	48 ba 01 01 01 01 01 	movabs $0x101010101010101,%rdx
   110db:	01 01 01
   110de:	48 0f af da          	imul   %rdx,%rbx
   110e2:	45 89 f0             	mov    %r14d,%r8d
   110e5:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   110e9:	0f 84 d6 00 00 00    	je     111c5 <zbtIndexScanSlot+0x425>
   110ef:	45 89 e2             	mov    %r12d,%r10d
   110f2:	41 80 f2 01          	xor    $0x1,%r10b
   110f6:	eb 15                	jmp    1110d <zbtIndexScanSlot+0x36d>
   110f8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   110ff:	00
   11100:	49 ff c0             	inc    %r8
   11103:	4c 3b 45 c0          	cmp    -0x40(%rbp),%r8
   11107:	0f 84 7f 01 00 00    	je     1128c <zbtIndexScanSlot+0x4ec>
   1110d:	48 89 c7             	mov    %rax,%rdi
   11110:	4e 8d 1c c5 00 00 00 	lea    0x0(,%r8,8),%r11
   11117:	00
   11118:	4c 89 da             	mov    %r11,%rdx
   1111b:	48 b8 f8 ff ff ff 07 	movabs $0x7fffffff8,%rax
   11122:	00 00 00
   11125:	48 21 c2             	and    %rax,%rdx
   11128:	4c 8b 34 11          	mov    (%rcx,%rdx,1),%r14
   1112c:	4c 89 f2             	mov    %r14,%rdx
   1112f:	48 31 da             	xor    %rbx,%rdx
   11132:	49 89 d5             	mov    %rdx,%r13
   11135:	49 f7 d5             	not    %r13
   11138:	49 b9 ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r9
   1113f:	fe fe fe
   11142:	4c 01 ca             	add    %r9,%rdx
   11145:	48 b8 80 80 80 80 80 	movabs $0x8080808080808080,%rax
   1114c:	80 80 80
   1114f:	49 21 c5             	and    %rax,%r13
   11152:	49 21 d5             	and    %rdx,%r13
   11155:	41 80 fc 01          	cmp    $0x1,%r12b
   11159:	75 10                	jne    1116b <zbtIndexScanSlot+0x3cb>
   1115b:	4b 8d 14 0e          	lea    (%r14,%r9,1),%rdx
   1115f:	49 f7 d6             	not    %r14
   11162:	49 21 c6             	and    %rax,%r14
   11165:	49 21 d6             	and    %rdx,%r14
   11168:	4d 09 f5             	or     %r14,%r13
   1116b:	4d 85 ed             	test   %r13,%r13
   1116e:	48 89 f8             	mov    %rdi,%rax
   11171:	75 2d                	jne    111a0 <zbtIndexScanSlot+0x400>
   11173:	eb 8b                	jmp    11100 <zbtIndexScanSlot+0x360>
   11175:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   1117c:	00 00 00 00
   11180:	89 f2                	mov    %esi,%edx
   11182:	44 29 f2             	sub    %r14d,%edx
   11185:	45 89 f9             	mov    %r15d,%r9d
   11188:	41 ff c7             	inc    %r15d
   1118b:	42 89 94 8d 00 fe ff 	mov    %edx,-0x200(%rbp,%r9,4)
   11192:	ff
   11193:	49 8d 55 ff          	lea    -0x1(%r13),%rdx
   11197:	49 21 d5             	and    %rdx,%r13
   1119a:	0f 84 60 ff ff ff    	je     11100 <zbtIndexScanSlot+0x360>
   111a0:	f3 4d 0f bc f5       	tzcnt  %r13,%r14
   111a5:	41 c1 ee 03          	shr    $0x3,%r14d
   111a9:	45 09 de             	or     %r11d,%r14d
   111ac:	46 0f b6 0c 31       	movzbl (%rcx,%r14,1),%r9d
   111b1:	44 89 d2             	mov    %r10d,%edx
   111b4:	44 08 ca             	or     %r9b,%dl
   111b7:	0f 94 c2             	sete   %dl
   111ba:	45 38 e1             	cmp    %r12b,%r9b
   111bd:	74 c1                	je     11180 <zbtIndexScanSlot+0x3e0>
   111bf:	84 d2                	test   %dl,%dl
   111c1:	74 d0                	je     11193 <zbtIndexScanSlot+0x3f3>
   111c3:	eb bb                	jmp    11180 <zbtIndexScanSlot+0x3e0>
   111c5:	48 bf f8 ff ff ff 07 	movabs $0x7fffffff8,%rdi
   111cc:	00 00 00
   111cf:	45 89 e1             	mov    %r12d,%r9d
   111d2:	41 80 f1 01          	xor    $0x1,%r9b
   111d6:	48 be 80 80 80 80 80 	movabs $0x8080808080808080,%rsi
   111dd:	80 80 80
   111e0:	eb 1b                	jmp    111fd <zbtIndexScanSlot+0x45d>
   111e2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   111e9:	1f 84 00 00 00 00 00
   111f0:	49 ff c0             	inc    %r8
   111f3:	4c 3b 45 c0          	cmp    -0x40(%rbp),%r8
   111f7:	0f 84 8f 00 00 00    	je     1128c <zbtIndexScanSlot+0x4ec>
   111fd:	4e 8d 14 c5 00 00 00 	lea    0x0(,%r8,8),%r10
   11204:	00
   11205:	4c 89 d2             	mov    %r10,%rdx
   11208:	48 21 fa             	and    %rdi,%rdx
   1120b:	4c 8b 34 11          	mov    (%rcx,%rdx,1),%r14
   1120f:	4c 89 f2             	mov    %r14,%rdx
   11212:	48 31 da             	xor    %rbx,%rdx
   11215:	49 89 d3             	mov    %rdx,%r11
   11218:	49 f7 d3             	not    %r11
   1121b:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   11222:	fe fe fe
   11225:	4c 01 ea             	add    %r13,%rdx
   11228:	49 21 f3             	and    %rsi,%r11
   1122b:	49 21 d3             	and    %rdx,%r11
   1122e:	41 80 fc 01          	cmp    $0x1,%r12b
   11232:	75 10                	jne    11244 <zbtIndexScanSlot+0x4a4>
   11234:	4b 8d 14 2e          	lea    (%r14,%r13,1),%rdx
   11238:	49 f7 d6             	not    %r14
   1123b:	49 21 f6             	and    %rsi,%r14
   1123e:	49 21 d6             	and    %rdx,%r14
   11241:	4d 09 f3             	or     %r14,%r11
   11244:	4d 85 db             	test   %r11,%r11
   11247:	75 1e                	jne    11267 <zbtIndexScanSlot+0x4c7>
   11249:	eb a5                	jmp    111f0 <zbtIndexScanSlot+0x450>
   1124b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   11250:	44 89 fa             	mov    %r15d,%edx
   11253:	41 ff c7             	inc    %r15d
   11256:	44 89 b4 95 00 fe ff 	mov    %r14d,-0x200(%rbp,%rdx,4)
   1125d:	ff
   1125e:	49 8d 53 ff          	lea    -0x1(%r11),%rdx
   11262:	49 21 d3             	and    %rdx,%r11
   11265:	74 89                	je     111f0 <zbtIndexScanSlot+0x450>
   11267:	f3 4d 0f bc f3       	tzcnt  %r11,%r14
   1126c:	41 c1 ee 03          	shr    $0x3,%r14d
   11270:	45 09 d6             	or     %r10d,%r14d
   11273:	46 0f b6 2c 31       	movzbl (%rcx,%r14,1),%r13d
   11278:	44 89 ca             	mov    %r9d,%edx
   1127b:	44 08 ea             	or     %r13b,%dl
   1127e:	0f 94 c2             	sete   %dl
   11281:	45 38 e5             	cmp    %r12b,%r13b
   11284:	74 ca                	je     11250 <zbtIndexScanSlot+0x4b0>
   11286:	84 d2                	test   %dl,%dl
   11288:	74 d4                	je     1125e <zbtIndexScanSlot+0x4be>
   1128a:	eb c4                	jmp    11250 <zbtIndexScanSlot+0x4b0>
   1128c:	a8 07                	test   $0x7,%al
   1128e:	74 6c                	je     112fc <zbtIndexScanSlot+0x55c>
   11290:	89 c6                	mov    %eax,%esi
   11292:	83 e6 f8             	and    $0xfffffff8,%esi
   11295:	41 80 fc 01          	cmp    $0x1,%r12b
   11299:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   1129d:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   112a1:	0f 85 24 04 00 00    	jne    116cb <zbtIndexScanSlot+0x92b>
   112a7:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   112ab:	74 3a                	je     112e7 <zbtIndexScanSlot+0x547>
   112ad:	89 c2                	mov    %eax,%edx
   112af:	f7 d2                	not    %edx
   112b1:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   112b7:	01 c2                	add    %eax,%edx
   112b9:	eb 0f                	jmp    112ca <zbtIndexScanSlot+0x52a>
   112bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   112c0:	48 ff c6             	inc    %rsi
   112c3:	ff ca                	dec    %edx
   112c5:	48 39 c6             	cmp    %rax,%rsi
   112c8:	73 3a                	jae    11304 <zbtIndexScanSlot+0x564>
   112ca:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   112ce:	77 f0                	ja     112c0 <zbtIndexScanSlot+0x520>
   112d0:	44 89 ff             	mov    %r15d,%edi
   112d3:	41 ff c7             	inc    %r15d
   112d6:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   112dd:	eb e1                	jmp    112c0 <zbtIndexScanSlot+0x520>
   112df:	48 ff c6             	inc    %rsi
   112e2:	48 39 c6             	cmp    %rax,%rsi
   112e5:	73 1d                	jae    11304 <zbtIndexScanSlot+0x564>
   112e7:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   112eb:	77 f2                	ja     112df <zbtIndexScanSlot+0x53f>
   112ed:	44 89 fa             	mov    %r15d,%edx
   112f0:	41 ff c7             	inc    %r15d
   112f3:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   112fa:	eb e3                	jmp    112df <zbtIndexScanSlot+0x53f>
   112fc:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   11300:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11304:	45 85 ff             	test   %r15d,%r15d
   11307:	0f 84 79 03 00 00    	je     11686 <zbtIndexScanSlot+0x8e6>
   1130d:	49 8d 43 38          	lea    0x38(%r11),%rax
   11311:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
   11315:	4d 85 f6             	test   %r14,%r14
   11318:	0f 95 c0             	setne  %al
   1131b:	41 83 ff 01          	cmp    $0x1,%r15d
   1131f:	0f 95 c1             	setne  %cl
   11322:	08 c1                	or     %al,%cl
   11324:	88 4d d7             	mov    %cl,-0x29(%rbp)
   11327:	44 89 f8             	mov    %r15d,%eax
   1132a:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   1132e:	31 db                	xor    %ebx,%ebx
   11330:	31 c0                	xor    %eax,%eax
   11332:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   11336:	eb 57                	jmp    1138f <zbtIndexScanSlot+0x5ef>
   11338:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   1133f:	00
   11340:	45 31 d2             	xor    %r10d,%r10d
   11343:	4c 89 d0             	mov    %r10,%rax
   11346:	48 f7 d8             	neg    %rax
   11349:	45 84 c0             	test   %r8b,%r8b
   1134c:	49 0f 44 c2          	cmove  %r10,%rax
   11350:	49 03 43 28          	add    0x28(%r11),%rax
   11354:	48 89 c1             	mov    %rax,%rcx
   11357:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   1135e:	ff ff 7f
   11361:	48 21 f9             	and    %rdi,%rcx
   11364:	48 85 c0             	test   %rax,%rax
   11367:	48 f7 d0             	not    %rax
   1136a:	48 0f 48 c1          	cmovs  %rcx,%rax
   1136e:	66 48 0f 6e c0       	movq   %rax,%xmm0
   11373:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11377:	ff 55 10             	call   *0x10(%rbp)
   1137a:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   1137e:	48 ff 45 b8          	incq   -0x48(%rbp)
   11382:	48 ff c3             	inc    %rbx
   11385:	48 3b 5d 88          	cmp    -0x78(%rbp),%rbx
   11389:	0f 84 15 03 00 00    	je     116a4 <zbtIndexScanSlot+0x904>
   1138f:	44 8b a4 9d 00 fe ff 	mov    -0x200(%rbp,%rbx,4),%r12d
   11396:	ff
   11397:	45 89 e5             	mov    %r12d,%r13d
   1139a:	41 f7 d5             	not    %r13d
   1139d:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   113a1:	0f 84 29 01 00 00    	je     114d0 <zbtIndexScanSlot+0x730>
   113a7:	41 0f b6 43 34       	movzbl 0x34(%r11),%eax
   113ac:	48 85 c0             	test   %rax,%rax
   113af:	74 4e                	je     113ff <zbtIndexScanSlot+0x65f>
   113b1:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   113b6:	0f af c1             	imul   %ecx,%eax
   113b9:	83 c0 07             	add    $0x7,%eax
   113bc:	c1 e8 03             	shr    $0x3,%eax
   113bf:	83 c0 09             	add    $0x9,%eax
   113c2:	83 e0 fe             	and    $0xfffffffe,%eax
   113c5:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   113ca:	44 89 e1             	mov    %r12d,%ecx
   113cd:	74 08                	je     113d7 <zbtIndexScanSlot+0x637>
   113cf:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   113d4:	44 01 e9             	add    %r13d,%ecx
   113d7:	48 03 45 c0          	add    -0x40(%rbp),%rax
   113db:	89 c9                	mov    %ecx,%ecx
   113dd:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   113e1:	49 8d 3c 03          	lea    (%r11,%rax,1),%rdi
   113e5:	41 0f b6 34 03       	movzbl (%r11,%rax,1),%esi
   113ea:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   113f0:	74 1b                	je     1140d <zbtIndexScanSlot+0x66d>
   113f2:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   113f8:	75 1e                	jne    11418 <zbtIndexScanSlot+0x678>
   113fa:	8b 47 01             	mov    0x1(%rdi),%eax
   113fd:	eb 2a                	jmp    11429 <zbtIndexScanSlot+0x689>
   113ff:	31 c0                	xor    %eax,%eax
   11401:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   11406:	44 89 e1             	mov    %r12d,%ecx
   11409:	75 c4                	jne    113cf <zbtIndexScanSlot+0x62f>
   1140b:	eb ca                	jmp    113d7 <zbtIndexScanSlot+0x637>
   1140d:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   11411:	b8 03 00 00 00       	mov    $0x3,%eax
   11416:	eb 05                	jmp    1141d <zbtIndexScanSlot+0x67d>
   11418:	b8 01 00 00 00       	mov    $0x1,%eax
   1141d:	48 01 c7             	add    %rax,%rdi
   11420:	e8 4b 05 00 00       	call   11970 <dictGenHashFunction>
   11425:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11429:	89 c0                	mov    %eax,%eax
   1142b:	48 8b 4d a0          	mov    -0x60(%rbp),%rcx
   1142f:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   11433:	4d 85 f6             	test   %r14,%r14
   11436:	74 1a                	je     11452 <zbtIndexScanSlot+0x6b2>
   11438:	8d 71 ff             	lea    -0x1(%rcx),%esi
   1143b:	89 c2                	mov    %eax,%edx
   1143d:	21 f2                	and    %esi,%edx
   1143f:	48 3b 55 98          	cmp    -0x68(%rbp),%rdx
   11443:	0f 82 39 ff ff ff    	jb     11382 <zbtIndexScanSlot+0x5e2>
   11449:	4c 39 f2             	cmp    %r14,%rdx
   1144c:	0f 83 30 ff ff ff    	jae    11382 <zbtIndexScanSlot+0x5e2>
   11452:	41 83 ff 01          	cmp    $0x1,%r15d
   11456:	74 78                	je     114d0 <zbtIndexScanSlot+0x730>
   11458:	48 89 ca             	mov    %rcx,%rdx
   1145b:	48 83 ea 01          	sub    $0x1,%rdx
   1145f:	0f 82 1d ff ff ff    	jb     11382 <zbtIndexScanSlot+0x5e2>
   11465:	21 d0                	and    %edx,%eax
   11467:	31 f6                	xor    %esi,%esi
   11469:	48 8b 7d a0          	mov    -0x60(%rbp),%rdi
   1146d:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   11471:	48 8b 3f             	mov    (%rdi),%rdi
   11474:	40 0f 95 c6          	setne  %sil
   11478:	c1 e6 04             	shl    $0x4,%esi
   1147b:	48 83 ce 20          	or     $0x20,%rsi
   1147f:	90                   	nop
   11480:	49 89 c0             	mov    %rax,%r8
   11483:	4c 0f af c6          	imul   %rsi,%r8
   11487:	49 01 f8             	add    %rdi,%r8
   1148a:	4c 3b 45 90          	cmp    -0x70(%rbp),%r8
   1148e:	74 40                	je     114d0 <zbtIndexScanSlot+0x730>
   11490:	4d 8b 00             	mov    (%r8),%r8
   11493:	4d 89 c1             	mov    %r8,%r9
   11496:	49 f7 d1             	not    %r9
   11499:	49 ba ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r10
   114a0:	fe fe fe
   114a3:	4d 01 d0             	add    %r10,%r8
   114a6:	49 ba 80 80 80 80 80 	movabs $0x8080808080808080,%r10
   114ad:	80 80 80
   114b0:	4d 21 d1             	and    %r10,%r9
   114b3:	4d 85 c1             	test   %r8,%r9
   114b6:	0f 85 c6 fe ff ff    	jne    11382 <zbtIndexScanSlot+0x5e2>
   114bc:	48 ff c0             	inc    %rax
   114bf:	48 21 d0             	and    %rdx,%rax
   114c2:	48 ff c9             	dec    %rcx
   114c5:	75 b9                	jne    11480 <zbtIndexScanSlot+0x6e0>
   114c7:	e9 b6 fe ff ff       	jmp    11382 <zbtIndexScanSlot+0x5e2>
   114cc:	0f 1f 40 00          	nopl   0x0(%rax)
   114d0:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   114d5:	48 85 ff             	test   %rdi,%rdi
   114d8:	0f 84 92 00 00 00    	je     11570 <zbtIndexScanSlot+0x7d0>
   114de:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   114e3:	89 f8                	mov    %edi,%eax
   114e5:	0f af c1             	imul   %ecx,%eax
   114e8:	83 c0 07             	add    $0x7,%eax
   114eb:	c1 e8 03             	shr    $0x3,%eax
   114ee:	83 c0 09             	add    $0x9,%eax
   114f1:	83 e0 fe             	and    $0xfffffffe,%eax
   114f4:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   114f9:	44 89 e1             	mov    %r12d,%ecx
   114fc:	45 84 c0             	test   %r8b,%r8b
   114ff:	74 08                	je     11509 <zbtIndexScanSlot+0x769>
   11501:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   11506:	44 01 e9             	add    %r13d,%ecx
   11509:	48 03 45 c0          	add    -0x40(%rbp),%rax
   1150d:	89 c9                	mov    %ecx,%ecx
   1150f:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   11513:	4d 8d 34 03          	lea    (%r11,%rax,1),%r14
   11517:	41 0f b6 14 03       	movzbl (%r11,%rax,1),%edx
   1151c:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11523:	77 1b                	ja     11540 <zbtIndexScanSlot+0x7a0>
   11525:	49 ff c6             	inc    %r14
   11528:	4c 89 f6             	mov    %r14,%rsi
   1152b:	40 84 ff             	test   %dil,%dil
   1152e:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   11532:	0f 85 b7 00 00 00    	jne    115ef <zbtIndexScanSlot+0x84f>
   11538:	e9 03 fe ff ff       	jmp    11340 <zbtIndexScanSlot+0x5a0>
   1153d:	0f 1f 00             	nopl   (%rax)
   11540:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11546:	75 39                	jne    11581 <zbtIndexScanSlot+0x7e1>
   11548:	41 0f b7 56 01       	movzwl 0x1(%r14),%edx
   1154d:	49 83 c6 03          	add    $0x3,%r14
   11551:	4c 89 f6             	mov    %r14,%rsi
   11554:	40 84 ff             	test   %dil,%dil
   11557:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   1155b:	0f 85 8e 00 00 00    	jne    115ef <zbtIndexScanSlot+0x84f>
   11561:	e9 da fd ff ff       	jmp    11340 <zbtIndexScanSlot+0x5a0>
   11566:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   1156d:	00 00 00
   11570:	31 c0                	xor    %eax,%eax
   11572:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   11577:	44 89 e1             	mov    %r12d,%ecx
   1157a:	45 84 c0             	test   %r8b,%r8b
   1157d:	75 82                	jne    11501 <zbtIndexScanSlot+0x761>
   1157f:	eb 88                	jmp    11509 <zbtIndexScanSlot+0x769>
   11581:	49 8b 76 0d          	mov    0xd(%r14),%rsi
   11585:	48 85 f6             	test   %rsi,%rsi
   11588:	75 4a                	jne    115d4 <zbtIndexScanSlot+0x834>
   1158a:	48 8d 3d 8d 20 00 00 	lea    0x208d(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11591:	48 89 75 a8          	mov    %rsi,-0x58(%rbp)
   11595:	be 5b 02 00 00       	mov    $0x25b,%esi
   1159a:	48 8d 15 a9 21 00 00 	lea    0x21a9(%rip),%rdx        # 1374a <_IO_stdin_used+0x74a>
   115a1:	e8 8a 01 00 00       	call   11730 <standalone_panic>
   115a6:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   115aa:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   115ae:	41 80 3e ff          	cmpb   $0xff,(%r14)
   115b2:	74 20                	je     115d4 <zbtIndexScanSlot+0x834>
   115b4:	48 8d 3d 63 20 00 00 	lea    0x2063(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   115bb:	be 3b 02 00 00       	mov    $0x23b,%esi
   115c0:	48 8d 15 8f 21 00 00 	lea    0x218f(%rip),%rdx        # 13756 <_IO_stdin_used+0x756>
   115c7:	e8 64 01 00 00       	call   11730 <standalone_panic>
   115cc:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   115d0:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   115d4:	49 8b 56 05          	mov    0x5(%r14),%rdx
   115d8:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   115dd:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   115e2:	40 84 ff             	test   %dil,%dil
   115e5:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   115e9:	0f 84 51 fd ff ff    	je     11340 <zbtIndexScanSlot+0x5a0>
   115ef:	45 84 c0             	test   %r8b,%r8b
   115f2:	74 08                	je     115fc <zbtIndexScanSlot+0x85c>
   115f4:	45 0f b6 63 11       	movzbl 0x11(%r11),%r12d
   115f9:	45 01 ec             	add    %r13d,%r12d
   115fc:	44 0f b6 d7          	movzbl %dil,%r10d
   11600:	45 89 e3             	mov    %r12d,%r11d
   11603:	44 89 d0             	mov    %r10d,%eax
   11606:	4c 0f af d8          	imul   %rax,%r11
   1160a:	4d 89 de             	mov    %r11,%r14
   1160d:	49 c1 ee 03          	shr    $0x3,%r14
   11611:	48 8b 4d c0          	mov    -0x40(%rbp),%rcx
   11615:	4e 8b 0c 31          	mov    (%rcx,%r14,1),%r9
   11619:	44 89 d9             	mov    %r11d,%ecx
   1161c:	80 e1 07             	and    $0x7,%cl
   1161f:	49 d3 e9             	shr    %cl,%r9
   11622:	41 83 e3 07          	and    $0x7,%r11d
   11626:	74 28                	je     11650 <zbtIndexScanSlot+0x8b0>
   11628:	b9 40 00 00 00       	mov    $0x40,%ecx
   1162d:	44 29 d9             	sub    %r11d,%ecx
   11630:	44 39 d1             	cmp    %r10d,%ecx
   11633:	73 1b                	jae    11650 <zbtIndexScanSlot+0x8b0>
   11635:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11639:	47 0f b6 54 1e 40    	movzbl 0x40(%r14,%r11,1),%r10d
   1163f:	49 d3 e2             	shl    %cl,%r10
   11642:	4d 09 d1             	or     %r10,%r9
   11645:	eb 0d                	jmp    11654 <zbtIndexScanSlot+0x8b4>
   11647:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
   1164e:	00 00
   11650:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11654:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   1165b:	89 c1                	mov    %eax,%ecx
   1165d:	49 d3 e2             	shl    %cl,%r10
   11660:	40 80 ff 40          	cmp    $0x40,%dil
   11664:	49 f7 d2             	not    %r10
   11667:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   1166e:	4c 0f 43 d0          	cmovae %rax,%r10
   11672:	4d 21 ca             	and    %r9,%r10
   11675:	41 0f b6 4b 13       	movzbl 0x13(%r11),%ecx
   1167a:	49 d3 e2             	shl    %cl,%r10
   1167d:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   11681:	e9 bd fc ff ff       	jmp    11343 <zbtIndexScanSlot+0x5a3>
   11686:	48 8d 3d 91 1f 00 00 	lea    0x1f91(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   1168d:	48 8d 15 01 25 00 00 	lea    0x2501(%rip),%rdx        # 13b95 <_IO_stdin_used+0xb95>
   11694:	be 7b 10 00 00       	mov    $0x107b,%esi
   11699:	e8 92 00 00 00       	call   11730 <standalone_panic>
   1169e:	31 c0                	xor    %eax,%eax
   116a0:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   116a4:	4c 0b 75 b8          	or     -0x48(%rbp),%r14
   116a8:	75 18                	jne    116c2 <zbtIndexScanSlot+0x922>
   116aa:	48 8d 3d 6d 1f 00 00 	lea    0x1f6d(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   116b1:	48 8d 15 e8 24 00 00 	lea    0x24e8(%rip),%rdx        # 13ba0 <_IO_stdin_used+0xba0>
   116b8:	be 92 10 00 00       	mov    $0x1092,%esi
   116bd:	e8 6e 00 00 00       	call   11730 <standalone_panic>
   116c2:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   116c6:	e9 9b f8 ff ff       	jmp    10f66 <zbtIndexScanSlot+0x1c6>
   116cb:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   116cf:	74 3e                	je     1170f <zbtIndexScanSlot+0x96f>
   116d1:	89 c2                	mov    %eax,%edx
   116d3:	f7 d2                	not    %edx
   116d5:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   116db:	01 c2                	add    %eax,%edx
   116dd:	eb 0f                	jmp    116ee <zbtIndexScanSlot+0x94e>
   116df:	90                   	nop
   116e0:	48 ff c6             	inc    %rsi
   116e3:	ff ca                	dec    %edx
   116e5:	48 39 c6             	cmp    %rax,%rsi
   116e8:	0f 83 16 fc ff ff    	jae    11304 <zbtIndexScanSlot+0x564>
   116ee:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   116f2:	75 ec                	jne    116e0 <zbtIndexScanSlot+0x940>
   116f4:	44 89 ff             	mov    %r15d,%edi
   116f7:	41 ff c7             	inc    %r15d
   116fa:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   11701:	eb dd                	jmp    116e0 <zbtIndexScanSlot+0x940>
   11703:	48 ff c6             	inc    %rsi
   11706:	48 39 c6             	cmp    %rax,%rsi
   11709:	0f 83 f5 fb ff ff    	jae    11304 <zbtIndexScanSlot+0x564>
   1170f:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   11713:	75 ee                	jne    11703 <zbtIndexScanSlot+0x963>
   11715:	44 89 fa             	mov    %r15d,%edx
   11718:	41 ff c7             	inc    %r15d
   1171b:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   11722:	eb df                	jmp    11703 <zbtIndexScanSlot+0x963>

Disassembly of section .fini:
