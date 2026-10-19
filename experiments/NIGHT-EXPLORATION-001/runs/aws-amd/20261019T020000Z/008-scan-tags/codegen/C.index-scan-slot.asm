
scratch/amd-scan-build/C/build/native/btree-bench:     file format elf64-x86-64


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
   10db4:	4d 89 cd             	mov    %r9,%r13
   10db7:	4d 89 c6             	mov    %r8,%r14
   10dba:	89 c8                	mov    %ecx,%eax
   10dbc:	49 89 d2             	mov    %rdx,%r10
   10dbf:	48 89 f3             	mov    %rsi,%rbx
   10dc2:	4c 8b 22             	mov    (%rdx),%r12
   10dc5:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   10dcc:	49 d3 ec             	shr    %cl,%r12
   10dcf:	49 89 ff             	mov    %rdi,%r15
   10dd2:	8b 56 20             	mov    0x20(%rsi),%edx
   10dd5:	89 c0                	mov    %eax,%eax
   10dd7:	85 d2                	test   %edx,%edx
   10dd9:	74 18                	je     10df3 <zbtIndexScanSlot+0x53>
   10ddb:	45 8b 4c 82 10       	mov    0x10(%r10,%rax,4),%r9d
   10de0:	31 c0                	xor    %eax,%eax
   10de2:	4c 89 e7             	mov    %r12,%rdi
   10de5:	48 81 e7 ff 00 00 00 	and    $0xff,%rdi
   10dec:	75 2d                	jne    10e1b <zbtIndexScanSlot+0x7b>
   10dee:	e9 6c 01 00 00       	jmp    10f5f <zbtIndexScanSlot+0x1bf>
   10df3:	41 0f b7 4c 42 10    	movzwl 0x10(%r10,%rax,2),%ecx
   10df9:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   10dff:	41 b9 ff ff ff ff    	mov    $0xffffffff,%r9d
   10e05:	44 0f 45 c9          	cmovne %ecx,%r9d
   10e09:	31 c0                	xor    %eax,%eax
   10e0b:	4c 89 e7             	mov    %r12,%rdi
   10e0e:	48 81 e7 ff 00 00 00 	and    $0xff,%rdi
   10e15:	0f 84 44 01 00 00    	je     10f5f <zbtIndexScanSlot+0x1bf>
   10e1b:	41 83 f9 ff          	cmp    $0xffffffff,%r9d
   10e1f:	0f 84 3a 01 00 00    	je     10f5f <zbtIndexScanSlot+0x1bf>
   10e25:	4d 85 ed             	test   %r13,%r13
   10e28:	74 7a                	je     10ea4 <zbtIndexScanSlot+0x104>
   10e2a:	48 b9 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%rcx
   10e31:	79 37 9e
   10e34:	48 0f af f9          	imul   %rcx,%rdi
   10e38:	48 89 f9             	mov    %rdi,%rcx
   10e3b:	48 c1 e9 3a          	shr    $0x3a,%rcx
   10e3f:	be 01 00 00 00       	mov    $0x1,%esi
   10e44:	48 d3 e6             	shl    %cl,%rsi
   10e47:	4d 89 f0             	mov    %r14,%r8
   10e4a:	4d 39 ee             	cmp    %r13,%r14
   10e4d:	73 4c                	jae    10e9b <zbtIndexScanSlot+0xfb>
   10e4f:	4c 0f ab e6          	bts    %r12,%rsi
   10e53:	48 c1 ef 24          	shr    $0x24,%rdi
   10e57:	48 0f ab fe          	bts    %rdi,%rsi
   10e5b:	31 c9                	xor    %ecx,%ecx
   10e5d:	85 d2                	test   %edx,%edx
   10e5f:	0f 95 c1             	setne  %cl
   10e62:	48 8b 13             	mov    (%rbx),%rdx
   10e65:	c1 e1 04             	shl    $0x4,%ecx
   10e68:	48 83 c9 20          	or     $0x20,%rcx
   10e6c:	48 89 cf             	mov    %rcx,%rdi
   10e6f:	49 0f af fe          	imul   %r14,%rdi
   10e73:	48 01 fa             	add    %rdi,%rdx
   10e76:	48 83 c2 08          	add    $0x8,%rdx
   10e7a:	31 c0                	xor    %eax,%eax
   10e7c:	4d 89 f0             	mov    %r14,%r8
   10e7f:	90                   	nop
   10e80:	48 8b 3a             	mov    (%rdx),%rdi
   10e83:	48 f7 d7             	not    %rdi
   10e86:	48 85 fe             	test   %rdi,%rsi
   10e89:	74 10                	je     10e9b <zbtIndexScanSlot+0xfb>
   10e8b:	49 ff c0             	inc    %r8
   10e8e:	48 01 ca             	add    %rcx,%rdx
   10e91:	4d 39 c5             	cmp    %r8,%r13
   10e94:	75 ea                	jne    10e80 <zbtIndexScanSlot+0xe0>
   10e96:	e9 c4 00 00 00       	jmp    10f5f <zbtIndexScanSlot+0x1bf>
   10e9b:	4d 39 e8             	cmp    %r13,%r8
   10e9e:	0f 84 b9 00 00 00    	je     10f5d <zbtIndexScanSlot+0x1bd>
   10ea4:	45 3b 4f 54          	cmp    0x54(%r15),%r9d
   10ea8:	0f 83 87 00 00 00    	jae    10f35 <zbtIndexScanSlot+0x195>
   10eae:	49 8b 4f 48          	mov    0x48(%r15),%rcx
   10eb2:	44 89 ca             	mov    %r9d,%edx
   10eb5:	4c 8b 1c d1          	mov    (%rcx,%rdx,8),%r11
   10eb9:	4d 85 db             	test   %r11,%r11
   10ebc:	74 77                	je     10f35 <zbtIndexScanSlot+0x195>
   10ebe:	44 89 d9             	mov    %r11d,%ecx
   10ec1:	83 e1 01             	and    $0x1,%ecx
   10ec4:	75 6f                	jne    10f35 <zbtIndexScanSlot+0x195>
   10ec6:	45 39 4b 30          	cmp    %r9d,0x30(%r11)
   10eca:	4c 89 55 c0          	mov    %r10,-0x40(%rbp)
   10ece:	4c 89 5d c8          	mov    %r11,-0x38(%rbp)
   10ed2:	74 20                	je     10ef4 <zbtIndexScanSlot+0x154>
   10ed4:	48 8d 3d 43 27 00 00 	lea    0x2743(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10edb:	48 8d 15 95 28 00 00 	lea    0x2895(%rip),%rdx        # 13777 <_IO_stdin_used+0x777>
   10ee2:	be 75 10 00 00       	mov    $0x1075,%esi
   10ee7:	e8 84 08 00 00       	call   11770 <standalone_panic>
   10eec:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   10ef0:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   10ef4:	49 8b 47 40          	mov    0x40(%r15),%rax
   10ef8:	48 85 c0             	test   %rax,%rax
   10efb:	74 16                	je     10f13 <zbtIndexScanSlot+0x173>
   10efd:	41 0f b7 4b 16       	movzwl 0x16(%r11),%ecx
   10f02:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   10f06:	0f 94 c1             	sete   %cl
   10f09:	48 39 d8             	cmp    %rbx,%rax
   10f0c:	0f 95 c0             	setne  %al
   10f0f:	38 c8                	cmp    %cl,%al
   10f11:	74 4a                	je     10f5d <zbtIndexScanSlot+0x1bd>
   10f13:	41 0f b6 4b 34       	movzbl 0x34(%r11),%ecx
   10f18:	31 d2                	xor    %edx,%edx
   10f1a:	41 0f b6 43 11       	movzbl 0x11(%r11),%eax
   10f1f:	48 85 c9             	test   %rcx,%rcx
   10f22:	74 4d                	je     10f71 <zbtIndexScanSlot+0x1d1>
   10f24:	0f af c8             	imul   %eax,%ecx
   10f27:	83 c1 07             	add    $0x7,%ecx
   10f2a:	c1 e9 03             	shr    $0x3,%ecx
   10f2d:	83 c1 09             	add    $0x9,%ecx
   10f30:	83 e1 fe             	and    $0xfffffffe,%ecx
   10f33:	eb 3e                	jmp    10f73 <zbtIndexScanSlot+0x1d3>
   10f35:	49 83 7f 40 00       	cmpq   $0x0,0x40(%r15)
   10f3a:	74 09                	je     10f45 <zbtIndexScanSlot+0x1a5>
   10f3c:	49 83 c7 18          	add    $0x18,%r15
   10f40:	49 39 df             	cmp    %rbx,%r15
   10f43:	74 18                	je     10f5d <zbtIndexScanSlot+0x1bd>
   10f45:	48 8d 3d d2 26 00 00 	lea    0x26d2(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10f4c:	48 8d 15 43 28 00 00 	lea    0x2843(%rip),%rdx        # 13796 <_IO_stdin_used+0x796>
   10f53:	be 72 10 00 00       	mov    $0x1072,%esi
   10f58:	e8 13 08 00 00       	call   11770 <standalone_panic>
   10f5d:	31 c0                	xor    %eax,%eax
   10f5f:	48 81 c4 d8 01 00 00 	add    $0x1d8,%rsp
   10f66:	5b                   	pop    %rbx
   10f67:	41 5c                	pop    %r12
   10f69:	41 5d                	pop    %r13
   10f6b:	41 5e                	pop    %r14
   10f6d:	41 5f                	pop    %r15
   10f6f:	5d                   	pop    %rbp
   10f70:	c3                   	ret
   10f71:	31 c9                	xor    %ecx,%ecx
   10f73:	49 8d 34 0b          	lea    (%r11,%rcx,1),%rsi
   10f77:	48 83 c6 38          	add    $0x38,%rsi
   10f7b:	48 8d 34 46          	lea    (%rsi,%rax,2),%rsi
   10f7f:	41 0f b6 7b 35       	movzbl 0x35(%r11),%edi
   10f84:	41 bf 00 00 00 00    	mov    $0x0,%r15d
   10f8a:	3c 10                	cmp    $0x10,%al
   10f8c:	0f 82 90 01 00 00    	jb     11122 <zbtIndexScanSlot+0x382>
   10f92:	41 0f b6 d4          	movzbl %r12b,%edx
   10f96:	66 0f 6e c2          	movd   %edx,%xmm0
   10f9a:	66 0f 60 c0          	punpcklbw %xmm0,%xmm0
   10f9e:	f2 0f 70 c0 00       	pshuflw $0x0,%xmm0,%xmm0
   10fa3:	66 0f 70 c0 00       	pshufd $0x0,%xmm0,%xmm0
   10fa8:	89 c2                	mov    %eax,%edx
   10faa:	83 e2 f0             	and    $0xfffffff0,%edx
   10fad:	45 31 c0             	xor    %r8d,%r8d
   10fb0:	40 84 ff             	test   %dil,%dil
   10fb3:	0f 84 81 00 00 00    	je     1103a <zbtIndexScanSlot+0x29a>
   10fb9:	41 80 fc 01          	cmp    $0x1,%r12b
   10fbd:	0f 85 f1 00 00 00    	jne    110b4 <zbtIndexScanSlot+0x314>
   10fc3:	66 0f ef c9          	pxor   %xmm1,%xmm1
   10fc7:	45 31 ff             	xor    %r15d,%r15d
   10fca:	eb 18                	jmp    10fe4 <zbtIndexScanSlot+0x244>
   10fcc:	0f 1f 40 00          	nopl   0x0(%rax)
   10fd0:	49 83 c0 10          	add    $0x10,%r8
   10fd4:	41 89 c1             	mov    %eax,%r9d
   10fd7:	45 29 c1             	sub    %r8d,%r9d
   10fda:	41 83 f9 0f          	cmp    $0xf,%r9d
   10fde:	0f 86 36 01 00 00    	jbe    1111a <zbtIndexScanSlot+0x37a>
   10fe4:	f3 42 0f 6f 14 06    	movdqu (%rsi,%r8,1),%xmm2
   10fea:	66 0f 6f da          	movdqa %xmm2,%xmm3
   10fee:	66 0f 74 d8          	pcmpeqb %xmm0,%xmm3
   10ff2:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   10ff6:	66 0f eb d3          	por    %xmm3,%xmm2
   10ffa:	66 44 0f d7 ca       	pmovmskb %xmm2,%r9d
   10fff:	45 85 c9             	test   %r9d,%r9d
   11002:	74 cc                	je     10fd0 <zbtIndexScanSlot+0x230>
   11004:	45 0f b7 c9          	movzwl %r9w,%r9d
   11008:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   1100f:	00
   11010:	f3 45 0f bc d1       	tzcnt  %r9d,%r10d
   11015:	45 01 c2             	add    %r8d,%r10d
   11018:	41 f7 d2             	not    %r10d
   1101b:	41 01 c2             	add    %eax,%r10d
   1101e:	45 89 fb             	mov    %r15d,%r11d
   11021:	41 ff c7             	inc    %r15d
   11024:	46 89 94 9d 00 fe ff 	mov    %r10d,-0x200(%rbp,%r11,4)
   1102b:	ff
   1102c:	45 8d 51 ff          	lea    -0x1(%r9),%r10d
   11030:	45 21 ca             	and    %r9d,%r10d
   11033:	45 89 d1             	mov    %r10d,%r9d
   11036:	75 d8                	jne    11010 <zbtIndexScanSlot+0x270>
   11038:	eb 96                	jmp    10fd0 <zbtIndexScanSlot+0x230>
   1103a:	45 31 ff             	xor    %r15d,%r15d
   1103d:	eb 1d                	jmp    1105c <zbtIndexScanSlot+0x2bc>
   1103f:	90                   	nop
   11040:	49 83 c0 10          	add    $0x10,%r8
   11044:	41 89 c1             	mov    %eax,%r9d
   11047:	45 29 c1             	sub    %r8d,%r9d
   1104a:	41 83 f9 0f          	cmp    $0xf,%r9d
   1104e:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   11052:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11056:	0f 86 c6 00 00 00    	jbe    11122 <zbtIndexScanSlot+0x382>
   1105c:	f3 42 0f 6f 0c 06    	movdqu (%rsi,%r8,1),%xmm1
   11062:	66 0f ef d2          	pxor   %xmm2,%xmm2
   11066:	41 80 fc 01          	cmp    $0x1,%r12b
   1106a:	75 04                	jne    11070 <zbtIndexScanSlot+0x2d0>
   1106c:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   11070:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   11074:	66 0f eb ca          	por    %xmm2,%xmm1
   11078:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   1107d:	45 85 c9             	test   %r9d,%r9d
   11080:	74 be                	je     11040 <zbtIndexScanSlot+0x2a0>
   11082:	45 0f b7 c9          	movzwl %r9w,%r9d
   11086:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   1108d:	00 00 00
   11090:	f3 45 0f bc d1       	tzcnt  %r9d,%r10d
   11095:	45 01 c2             	add    %r8d,%r10d
   11098:	45 89 fb             	mov    %r15d,%r11d
   1109b:	41 ff c7             	inc    %r15d
   1109e:	46 89 94 9d 00 fe ff 	mov    %r10d,-0x200(%rbp,%r11,4)
   110a5:	ff
   110a6:	45 8d 51 ff          	lea    -0x1(%r9),%r10d
   110aa:	45 21 ca             	and    %r9d,%r10d
   110ad:	45 89 d1             	mov    %r10d,%r9d
   110b0:	75 de                	jne    11090 <zbtIndexScanSlot+0x2f0>
   110b2:	eb 8c                	jmp    11040 <zbtIndexScanSlot+0x2a0>
   110b4:	45 31 ff             	xor    %r15d,%r15d
   110b7:	eb 17                	jmp    110d0 <zbtIndexScanSlot+0x330>
   110b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   110c0:	49 83 c0 10          	add    $0x10,%r8
   110c4:	41 89 c1             	mov    %eax,%r9d
   110c7:	45 29 c1             	sub    %r8d,%r9d
   110ca:	41 83 f9 0f          	cmp    $0xf,%r9d
   110ce:	76 4a                	jbe    1111a <zbtIndexScanSlot+0x37a>
   110d0:	f3 42 0f 6f 0c 06    	movdqu (%rsi,%r8,1),%xmm1
   110d6:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   110da:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   110df:	45 85 c9             	test   %r9d,%r9d
   110e2:	74 dc                	je     110c0 <zbtIndexScanSlot+0x320>
   110e4:	45 0f b7 c9          	movzwl %r9w,%r9d
   110e8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   110ef:	00
   110f0:	f3 45 0f bc d1       	tzcnt  %r9d,%r10d
   110f5:	45 01 c2             	add    %r8d,%r10d
   110f8:	41 f7 d2             	not    %r10d
   110fb:	41 01 c2             	add    %eax,%r10d
   110fe:	45 89 fb             	mov    %r15d,%r11d
   11101:	41 ff c7             	inc    %r15d
   11104:	46 89 94 9d 00 fe ff 	mov    %r10d,-0x200(%rbp,%r11,4)
   1110b:	ff
   1110c:	45 8d 51 ff          	lea    -0x1(%r9),%r10d
   11110:	45 21 ca             	and    %r9d,%r10d
   11113:	45 89 d1             	mov    %r10d,%r9d
   11116:	75 d8                	jne    110f0 <zbtIndexScanSlot+0x350>
   11118:	eb a6                	jmp    110c0 <zbtIndexScanSlot+0x320>
   1111a:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   1111e:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11122:	39 c2                	cmp    %eax,%edx
   11124:	0f 83 ee 01 00 00    	jae    11318 <zbtIndexScanSlot+0x578>
   1112a:	41 89 d0             	mov    %edx,%r8d
   1112d:	41 80 fc 01          	cmp    $0x1,%r12b
   11131:	75 0e                	jne    11141 <zbtIndexScanSlot+0x3a1>
   11133:	40 84 ff             	test   %dil,%dil
   11136:	74 1e                	je     11156 <zbtIndexScanSlot+0x3b6>
   11138:	a8 01                	test   $0x1,%al
   1113a:	75 3a                	jne    11176 <zbtIndexScanSlot+0x3d6>
   1113c:	4c 89 c7             	mov    %r8,%rdi
   1113f:	eb 54                	jmp    11195 <zbtIndexScanSlot+0x3f5>
   11141:	40 84 ff             	test   %dil,%dil
   11144:	74 20                	je     11166 <zbtIndexScanSlot+0x3c6>
   11146:	a8 01                	test   $0x1,%al
   11148:	0f 85 af 00 00 00    	jne    111fd <zbtIndexScanSlot+0x45d>
   1114e:	4c 89 c7             	mov    %r8,%rdi
   11151:	e9 c5 00 00 00       	jmp    1121b <zbtIndexScanSlot+0x47b>
   11156:	a8 01                	test   $0x1,%al
   11158:	0f 85 25 01 00 00    	jne    11283 <zbtIndexScanSlot+0x4e3>
   1115e:	4c 89 c2             	mov    %r8,%rdx
   11161:	e9 38 01 00 00       	jmp    1129e <zbtIndexScanSlot+0x4fe>
   11166:	a8 01                	test   $0x1,%al
   11168:	0f 85 83 01 00 00    	jne    112f1 <zbtIndexScanSlot+0x551>
   1116e:	4c 89 c2             	mov    %r8,%rdx
   11171:	e9 95 01 00 00       	jmp    1130b <zbtIndexScanSlot+0x56b>
   11176:	42 80 3c 06 01       	cmpb   $0x1,(%rsi,%r8,1)
   1117b:	77 11                	ja     1118e <zbtIndexScanSlot+0x3ee>
   1117d:	f7 d2                	not    %edx
   1117f:	01 c2                	add    %eax,%edx
   11181:	44 89 fe             	mov    %r15d,%esi
   11184:	41 ff c7             	inc    %r15d
   11187:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   1118e:	4c 89 c7             	mov    %r8,%rdi
   11191:	48 83 cf 01          	or     $0x1,%rdi
   11195:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
   11199:	4c 39 c2             	cmp    %r8,%rdx
   1119c:	0f 84 76 01 00 00    	je     11318 <zbtIndexScanSlot+0x578>
   111a2:	48 89 c2             	mov    %rax,%rdx
   111a5:	48 29 fa             	sub    %rdi,%rdx
   111a8:	89 fe                	mov    %edi,%esi
   111aa:	f7 d6                	not    %esi
   111ac:	01 c6                	add    %eax,%esi
   111ae:	48 01 f9             	add    %rdi,%rcx
   111b1:	48 8d 04 41          	lea    (%rcx,%rax,2),%rax
   111b5:	4c 01 d8             	add    %r11,%rax
   111b8:	48 83 c0 39          	add    $0x39,%rax
   111bc:	31 c9                	xor    %ecx,%ecx
   111be:	eb 10                	jmp    111d0 <zbtIndexScanSlot+0x430>
   111c0:	48 83 c1 02          	add    $0x2,%rcx
   111c4:	83 c6 fe             	add    $0xfffffffe,%esi
   111c7:	48 39 ca             	cmp    %rcx,%rdx
   111ca:	0f 84 48 01 00 00    	je     11318 <zbtIndexScanSlot+0x578>
   111d0:	80 7c 08 ff 01       	cmpb   $0x1,-0x1(%rax,%rcx,1)
   111d5:	77 0d                	ja     111e4 <zbtIndexScanSlot+0x444>
   111d7:	44 89 ff             	mov    %r15d,%edi
   111da:	41 ff c7             	inc    %r15d
   111dd:	89 b4 bd 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdi,4)
   111e4:	80 3c 08 01          	cmpb   $0x1,(%rax,%rcx,1)
   111e8:	77 d6                	ja     111c0 <zbtIndexScanSlot+0x420>
   111ea:	8d 7e ff             	lea    -0x1(%rsi),%edi
   111ed:	45 89 f8             	mov    %r15d,%r8d
   111f0:	41 ff c7             	inc    %r15d
   111f3:	42 89 bc 85 00 fe ff 	mov    %edi,-0x200(%rbp,%r8,4)
   111fa:	ff
   111fb:	eb c3                	jmp    111c0 <zbtIndexScanSlot+0x420>
   111fd:	46 38 24 06          	cmp    %r12b,(%rsi,%r8,1)
   11201:	75 11                	jne    11214 <zbtIndexScanSlot+0x474>
   11203:	f7 d2                	not    %edx
   11205:	01 c2                	add    %eax,%edx
   11207:	44 89 fe             	mov    %r15d,%esi
   1120a:	41 ff c7             	inc    %r15d
   1120d:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   11214:	4c 89 c7             	mov    %r8,%rdi
   11217:	48 83 cf 01          	or     $0x1,%rdi
   1121b:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
   1121f:	4c 39 c2             	cmp    %r8,%rdx
   11222:	0f 84 f0 00 00 00    	je     11318 <zbtIndexScanSlot+0x578>
   11228:	48 89 c2             	mov    %rax,%rdx
   1122b:	48 29 fa             	sub    %rdi,%rdx
   1122e:	89 fe                	mov    %edi,%esi
   11230:	f7 d6                	not    %esi
   11232:	01 c6                	add    %eax,%esi
   11234:	48 01 f9             	add    %rdi,%rcx
   11237:	48 8d 04 41          	lea    (%rcx,%rax,2),%rax
   1123b:	4c 01 d8             	add    %r11,%rax
   1123e:	48 83 c0 39          	add    $0x39,%rax
   11242:	31 c9                	xor    %ecx,%ecx
   11244:	eb 10                	jmp    11256 <zbtIndexScanSlot+0x4b6>
   11246:	48 83 c1 02          	add    $0x2,%rcx
   1124a:	83 c6 fe             	add    $0xfffffffe,%esi
   1124d:	48 39 ca             	cmp    %rcx,%rdx
   11250:	0f 84 c2 00 00 00    	je     11318 <zbtIndexScanSlot+0x578>
   11256:	44 38 64 08 ff       	cmp    %r12b,-0x1(%rax,%rcx,1)
   1125b:	75 0d                	jne    1126a <zbtIndexScanSlot+0x4ca>
   1125d:	44 89 ff             	mov    %r15d,%edi
   11260:	41 ff c7             	inc    %r15d
   11263:	89 b4 bd 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdi,4)
   1126a:	44 38 24 08          	cmp    %r12b,(%rax,%rcx,1)
   1126e:	75 d6                	jne    11246 <zbtIndexScanSlot+0x4a6>
   11270:	8d 7e ff             	lea    -0x1(%rsi),%edi
   11273:	45 89 f8             	mov    %r15d,%r8d
   11276:	41 ff c7             	inc    %r15d
   11279:	42 89 bc 85 00 fe ff 	mov    %edi,-0x200(%rbp,%r8,4)
   11280:	ff
   11281:	eb c3                	jmp    11246 <zbtIndexScanSlot+0x4a6>
   11283:	42 80 3c 06 01       	cmpb   $0x1,(%rsi,%r8,1)
   11288:	77 0d                	ja     11297 <zbtIndexScanSlot+0x4f7>
   1128a:	44 89 fe             	mov    %r15d,%esi
   1128d:	41 ff c7             	inc    %r15d
   11290:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   11297:	4c 89 c2             	mov    %r8,%rdx
   1129a:	48 83 ca 01          	or     $0x1,%rdx
   1129e:	48 8d 70 ff          	lea    -0x1(%rax),%rsi
   112a2:	4c 39 c6             	cmp    %r8,%rsi
   112a5:	74 71                	je     11318 <zbtIndexScanSlot+0x578>
   112a7:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   112ab:	4c 01 d9             	add    %r11,%rcx
   112ae:	48 83 c1 39          	add    $0x39,%rcx
   112b2:	eb 09                	jmp    112bd <zbtIndexScanSlot+0x51d>
   112b4:	48 83 c2 02          	add    $0x2,%rdx
   112b8:	48 39 d0             	cmp    %rdx,%rax
   112bb:	74 5b                	je     11318 <zbtIndexScanSlot+0x578>
   112bd:	80 7c 11 ff 01       	cmpb   $0x1,-0x1(%rcx,%rdx,1)
   112c2:	77 15                	ja     112d9 <zbtIndexScanSlot+0x539>
   112c4:	44 89 fe             	mov    %r15d,%esi
   112c7:	41 ff c7             	inc    %r15d
   112ca:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   112d1:	80 3c 11 01          	cmpb   $0x1,(%rcx,%rdx,1)
   112d5:	77 dd                	ja     112b4 <zbtIndexScanSlot+0x514>
   112d7:	eb 06                	jmp    112df <zbtIndexScanSlot+0x53f>
   112d9:	80 3c 11 01          	cmpb   $0x1,(%rcx,%rdx,1)
   112dd:	77 d5                	ja     112b4 <zbtIndexScanSlot+0x514>
   112df:	44 89 fe             	mov    %r15d,%esi
   112e2:	41 ff c7             	inc    %r15d
   112e5:	8d 7a 01             	lea    0x1(%rdx),%edi
   112e8:	89 bc b5 00 fe ff ff 	mov    %edi,-0x200(%rbp,%rsi,4)
   112ef:	eb c3                	jmp    112b4 <zbtIndexScanSlot+0x514>
   112f1:	46 38 24 06          	cmp    %r12b,(%rsi,%r8,1)
   112f5:	75 0d                	jne    11304 <zbtIndexScanSlot+0x564>
   112f7:	44 89 fe             	mov    %r15d,%esi
   112fa:	41 ff c7             	inc    %r15d
   112fd:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   11304:	4c 89 c2             	mov    %r8,%rdx
   11307:	48 83 ca 01          	or     $0x1,%rdx
   1130b:	48 8d 70 ff          	lea    -0x1(%rax),%rsi
   1130f:	4c 39 c6             	cmp    %r8,%rsi
   11312:	0f 85 04 04 00 00    	jne    1171c <zbtIndexScanSlot+0x97c>
   11318:	45 85 ff             	test   %r15d,%r15d
   1131b:	0f 84 af 03 00 00    	je     116d0 <zbtIndexScanSlot+0x930>
   11321:	4c 89 75 98          	mov    %r14,-0x68(%rbp)
   11325:	48 89 5d a0          	mov    %rbx,-0x60(%rbp)
   11329:	49 8d 43 38          	lea    0x38(%r11),%rax
   1132d:	48 89 45 a8          	mov    %rax,-0x58(%rbp)
   11331:	4d 85 ed             	test   %r13,%r13
   11334:	0f 95 c0             	setne  %al
   11337:	41 83 ff 01          	cmp    $0x1,%r15d
   1133b:	0f 95 c1             	setne  %cl
   1133e:	08 c1                	or     %al,%cl
   11340:	88 4d d7             	mov    %cl,-0x29(%rbp)
   11343:	44 89 f8             	mov    %r15d,%eax
   11346:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   1134a:	45 31 e4             	xor    %r12d,%r12d
   1134d:	31 c0                	xor    %eax,%eax
   1134f:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   11353:	4c 89 6d 90          	mov    %r13,-0x70(%rbp)
   11357:	eb 5a                	jmp    113b3 <zbtIndexScanSlot+0x613>
   11359:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   11360:	45 31 d2             	xor    %r10d,%r10d
   11363:	4c 89 d0             	mov    %r10,%rax
   11366:	48 f7 d8             	neg    %rax
   11369:	45 84 c0             	test   %r8b,%r8b
   1136c:	49 0f 44 c2          	cmove  %r10,%rax
   11370:	49 03 43 28          	add    0x28(%r11),%rax
   11374:	48 89 c1             	mov    %rax,%rcx
   11377:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   1137e:	ff ff 7f
   11381:	48 21 f9             	and    %rdi,%rcx
   11384:	48 85 c0             	test   %rax,%rax
   11387:	48 f7 d0             	not    %rax
   1138a:	48 0f 48 c1          	cmovs  %rcx,%rax
   1138e:	66 48 0f 6e c0       	movq   %rax,%xmm0
   11393:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11397:	ff 55 10             	call   *0x10(%rbp)
   1139a:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   1139e:	48 ff 45 b8          	incq   -0x48(%rbp)
   113a2:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   113a6:	49 ff c4             	inc    %r12
   113a9:	4c 3b 65 88          	cmp    -0x78(%rbp),%r12
   113ad:	0f 84 3b 03 00 00    	je     116ee <zbtIndexScanSlot+0x94e>
   113b3:	42 8b 9c a5 00 fe ff 	mov    -0x200(%rbp,%r12,4),%ebx
   113ba:	ff
   113bb:	41 89 de             	mov    %ebx,%r14d
   113be:	41 f7 d6             	not    %r14d
   113c1:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   113c5:	0f 84 45 01 00 00    	je     11510 <zbtIndexScanSlot+0x770>
   113cb:	41 0f b6 43 34       	movzbl 0x34(%r11),%eax
   113d0:	48 85 c0             	test   %rax,%rax
   113d3:	74 4d                	je     11422 <zbtIndexScanSlot+0x682>
   113d5:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   113da:	0f af c1             	imul   %ecx,%eax
   113dd:	83 c0 07             	add    $0x7,%eax
   113e0:	c1 e8 03             	shr    $0x3,%eax
   113e3:	83 c0 09             	add    $0x9,%eax
   113e6:	83 e0 fe             	and    $0xfffffffe,%eax
   113e9:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   113ee:	89 d9                	mov    %ebx,%ecx
   113f0:	74 08                	je     113fa <zbtIndexScanSlot+0x65a>
   113f2:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   113f7:	44 01 f1             	add    %r14d,%ecx
   113fa:	48 03 45 a8          	add    -0x58(%rbp),%rax
   113fe:	89 c9                	mov    %ecx,%ecx
   11400:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   11404:	49 8d 3c 03          	lea    (%r11,%rax,1),%rdi
   11408:	41 0f b6 34 03       	movzbl (%r11,%rax,1),%esi
   1140d:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   11413:	74 1a                	je     1142f <zbtIndexScanSlot+0x68f>
   11415:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   1141b:	75 1d                	jne    1143a <zbtIndexScanSlot+0x69a>
   1141d:	8b 47 01             	mov    0x1(%rdi),%eax
   11420:	eb 2d                	jmp    1144f <zbtIndexScanSlot+0x6af>
   11422:	31 c0                	xor    %eax,%eax
   11424:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   11429:	89 d9                	mov    %ebx,%ecx
   1142b:	75 c5                	jne    113f2 <zbtIndexScanSlot+0x652>
   1142d:	eb cb                	jmp    113fa <zbtIndexScanSlot+0x65a>
   1142f:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   11433:	b8 03 00 00 00       	mov    $0x3,%eax
   11438:	eb 05                	jmp    1143f <zbtIndexScanSlot+0x69f>
   1143a:	b8 01 00 00 00       	mov    $0x1,%eax
   1143f:	48 01 c7             	add    %rax,%rdi
   11442:	e8 69 05 00 00       	call   119b0 <dictGenHashFunction>
   11447:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   1144b:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   1144f:	89 c0                	mov    %eax,%eax
   11451:	48 8b 4d a0          	mov    -0x60(%rbp),%rcx
   11455:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   11459:	4d 85 ed             	test   %r13,%r13
   1145c:	74 1a                	je     11478 <zbtIndexScanSlot+0x6d8>
   1145e:	8d 71 ff             	lea    -0x1(%rcx),%esi
   11461:	89 c2                	mov    %eax,%edx
   11463:	21 f2                	and    %esi,%edx
   11465:	48 3b 55 98          	cmp    -0x68(%rbp),%rdx
   11469:	0f 82 37 ff ff ff    	jb     113a6 <zbtIndexScanSlot+0x606>
   1146f:	4c 39 ea             	cmp    %r13,%rdx
   11472:	0f 83 2e ff ff ff    	jae    113a6 <zbtIndexScanSlot+0x606>
   11478:	41 83 ff 01          	cmp    $0x1,%r15d
   1147c:	0f 84 8e 00 00 00    	je     11510 <zbtIndexScanSlot+0x770>
   11482:	48 89 ca             	mov    %rcx,%rdx
   11485:	48 83 ea 01          	sub    $0x1,%rdx
   11489:	0f 82 17 ff ff ff    	jb     113a6 <zbtIndexScanSlot+0x606>
   1148f:	21 d0                	and    %edx,%eax
   11491:	31 f6                	xor    %esi,%esi
   11493:	48 8b 7d a0          	mov    -0x60(%rbp),%rdi
   11497:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   1149b:	48 8b 3f             	mov    (%rdi),%rdi
   1149e:	48 89 7d b0          	mov    %rdi,-0x50(%rbp)
   114a2:	40 0f 95 c6          	setne  %sil
   114a6:	c1 e6 04             	shl    $0x4,%esi
   114a9:	48 83 ce 20          	or     $0x20,%rsi
   114ad:	0f 1f 00             	nopl   (%rax)
   114b0:	49 89 c0             	mov    %rax,%r8
   114b3:	4c 0f af c6          	imul   %rsi,%r8
   114b7:	4c 03 45 b0          	add    -0x50(%rbp),%r8
   114bb:	4d 39 d0             	cmp    %r10,%r8
   114be:	74 50                	je     11510 <zbtIndexScanSlot+0x770>
   114c0:	4c 89 df             	mov    %r11,%rdi
   114c3:	4d 89 d3             	mov    %r10,%r11
   114c6:	4d 89 ea             	mov    %r13,%r10
   114c9:	4d 8b 00             	mov    (%r8),%r8
   114cc:	4d 89 c1             	mov    %r8,%r9
   114cf:	49 f7 d1             	not    %r9
   114d2:	49 bd 80 80 80 80 80 	movabs $0x8080808080808080,%r13
   114d9:	80 80 80
   114dc:	4d 21 e9             	and    %r13,%r9
   114df:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   114e6:	fe fe fe
   114e9:	4d 01 e8             	add    %r13,%r8
   114ec:	4d 85 c1             	test   %r8,%r9
   114ef:	0f 85 cd 01 00 00    	jne    116c2 <zbtIndexScanSlot+0x922>
   114f5:	48 ff c0             	inc    %rax
   114f8:	48 21 d0             	and    %rdx,%rax
   114fb:	48 ff c9             	dec    %rcx
   114fe:	4d 89 d5             	mov    %r10,%r13
   11501:	4d 89 da             	mov    %r11,%r10
   11504:	49 89 fb             	mov    %rdi,%r11
   11507:	75 a7                	jne    114b0 <zbtIndexScanSlot+0x710>
   11509:	e9 98 fe ff ff       	jmp    113a6 <zbtIndexScanSlot+0x606>
   1150e:	66 90                	xchg   %ax,%ax
   11510:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   11515:	48 85 ff             	test   %rdi,%rdi
   11518:	0f 84 92 00 00 00    	je     115b0 <zbtIndexScanSlot+0x810>
   1151e:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   11523:	89 f8                	mov    %edi,%eax
   11525:	0f af c1             	imul   %ecx,%eax
   11528:	83 c0 07             	add    $0x7,%eax
   1152b:	c1 e8 03             	shr    $0x3,%eax
   1152e:	83 c0 09             	add    $0x9,%eax
   11531:	83 e0 fe             	and    $0xfffffffe,%eax
   11534:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   11539:	89 d9                	mov    %ebx,%ecx
   1153b:	45 84 c0             	test   %r8b,%r8b
   1153e:	74 08                	je     11548 <zbtIndexScanSlot+0x7a8>
   11540:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   11545:	44 01 f1             	add    %r14d,%ecx
   11548:	48 03 45 a8          	add    -0x58(%rbp),%rax
   1154c:	89 c9                	mov    %ecx,%ecx
   1154e:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   11552:	4d 8d 2c 03          	lea    (%r11,%rax,1),%r13
   11556:	41 0f b6 14 03       	movzbl (%r11,%rax,1),%edx
   1155b:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11562:	77 1c                	ja     11580 <zbtIndexScanSlot+0x7e0>
   11564:	49 ff c5             	inc    %r13
   11567:	4c 89 ee             	mov    %r13,%rsi
   1156a:	40 84 ff             	test   %dil,%dil
   1156d:	4c 8b 6d 90          	mov    -0x70(%rbp),%r13
   11571:	0f 85 b8 00 00 00    	jne    1162f <zbtIndexScanSlot+0x88f>
   11577:	e9 e4 fd ff ff       	jmp    11360 <zbtIndexScanSlot+0x5c0>
   1157c:	0f 1f 40 00          	nopl   0x0(%rax)
   11580:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11586:	75 38                	jne    115c0 <zbtIndexScanSlot+0x820>
   11588:	41 0f b7 55 01       	movzwl 0x1(%r13),%edx
   1158d:	49 83 c5 03          	add    $0x3,%r13
   11591:	4c 89 ee             	mov    %r13,%rsi
   11594:	40 84 ff             	test   %dil,%dil
   11597:	4c 8b 6d 90          	mov    -0x70(%rbp),%r13
   1159b:	0f 85 8e 00 00 00    	jne    1162f <zbtIndexScanSlot+0x88f>
   115a1:	e9 ba fd ff ff       	jmp    11360 <zbtIndexScanSlot+0x5c0>
   115a6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   115ad:	00 00 00
   115b0:	31 c0                	xor    %eax,%eax
   115b2:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   115b7:	89 d9                	mov    %ebx,%ecx
   115b9:	45 84 c0             	test   %r8b,%r8b
   115bc:	75 82                	jne    11540 <zbtIndexScanSlot+0x7a0>
   115be:	eb 88                	jmp    11548 <zbtIndexScanSlot+0x7a8>
   115c0:	49 8b 75 0d          	mov    0xd(%r13),%rsi
   115c4:	48 85 f6             	test   %rsi,%rsi
   115c7:	75 4b                	jne    11614 <zbtIndexScanSlot+0x874>
   115c9:	48 8d 3d 4e 20 00 00 	lea    0x204e(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   115d0:	48 89 75 b0          	mov    %rsi,-0x50(%rbp)
   115d4:	be 5b 02 00 00       	mov    $0x25b,%esi
   115d9:	48 8d 15 6a 21 00 00 	lea    0x216a(%rip),%rdx        # 1374a <_IO_stdin_used+0x74a>
   115e0:	e8 8b 01 00 00       	call   11770 <standalone_panic>
   115e5:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   115e9:	48 8b 75 b0          	mov    -0x50(%rbp),%rsi
   115ed:	41 80 7d 00 ff       	cmpb   $0xff,0x0(%r13)
   115f2:	74 20                	je     11614 <zbtIndexScanSlot+0x874>
   115f4:	48 8d 3d 23 20 00 00 	lea    0x2023(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   115fb:	be 3b 02 00 00       	mov    $0x23b,%esi
   11600:	48 8d 15 4f 21 00 00 	lea    0x214f(%rip),%rdx        # 13756 <_IO_stdin_used+0x756>
   11607:	e8 64 01 00 00       	call   11770 <standalone_panic>
   1160c:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11610:	48 8b 75 b0          	mov    -0x50(%rbp),%rsi
   11614:	49 8b 55 05          	mov    0x5(%r13),%rdx
   11618:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   1161d:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   11622:	40 84 ff             	test   %dil,%dil
   11625:	4c 8b 6d 90          	mov    -0x70(%rbp),%r13
   11629:	0f 84 31 fd ff ff    	je     11360 <zbtIndexScanSlot+0x5c0>
   1162f:	45 84 c0             	test   %r8b,%r8b
   11632:	74 08                	je     1163c <zbtIndexScanSlot+0x89c>
   11634:	41 0f b6 5b 11       	movzbl 0x11(%r11),%ebx
   11639:	44 01 f3             	add    %r14d,%ebx
   1163c:	44 0f b6 d7          	movzbl %dil,%r10d
   11640:	41 89 db             	mov    %ebx,%r11d
   11643:	44 89 d0             	mov    %r10d,%eax
   11646:	4c 0f af d8          	imul   %rax,%r11
   1164a:	4c 89 db             	mov    %r11,%rbx
   1164d:	48 c1 eb 03          	shr    $0x3,%rbx
   11651:	48 8b 4d a8          	mov    -0x58(%rbp),%rcx
   11655:	4c 8b 0c 19          	mov    (%rcx,%rbx,1),%r9
   11659:	44 89 d9             	mov    %r11d,%ecx
   1165c:	80 e1 07             	and    $0x7,%cl
   1165f:	49 d3 e9             	shr    %cl,%r9
   11662:	41 83 e3 07          	and    $0x7,%r11d
   11666:	74 28                	je     11690 <zbtIndexScanSlot+0x8f0>
   11668:	b9 40 00 00 00       	mov    $0x40,%ecx
   1166d:	44 29 d9             	sub    %r11d,%ecx
   11670:	44 39 d1             	cmp    %r10d,%ecx
   11673:	73 1b                	jae    11690 <zbtIndexScanSlot+0x8f0>
   11675:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11679:	46 0f b6 54 1b 40    	movzbl 0x40(%rbx,%r11,1),%r10d
   1167f:	49 d3 e2             	shl    %cl,%r10
   11682:	4d 09 d1             	or     %r10,%r9
   11685:	eb 0d                	jmp    11694 <zbtIndexScanSlot+0x8f4>
   11687:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
   1168e:	00 00
   11690:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11694:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   1169b:	89 c1                	mov    %eax,%ecx
   1169d:	49 d3 e2             	shl    %cl,%r10
   116a0:	40 80 ff 40          	cmp    $0x40,%dil
   116a4:	49 f7 d2             	not    %r10
   116a7:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   116ae:	4c 0f 43 d0          	cmovae %rax,%r10
   116b2:	4d 21 ca             	and    %r9,%r10
   116b5:	41 0f b6 4b 13       	movzbl 0x13(%r11),%ecx
   116ba:	49 d3 e2             	shl    %cl,%r10
   116bd:	e9 a1 fc ff ff       	jmp    11363 <zbtIndexScanSlot+0x5c3>
   116c2:	4d 89 d5             	mov    %r10,%r13
   116c5:	4d 89 da             	mov    %r11,%r10
   116c8:	49 89 fb             	mov    %rdi,%r11
   116cb:	e9 d6 fc ff ff       	jmp    113a6 <zbtIndexScanSlot+0x606>
   116d0:	48 8d 3d 47 1f 00 00 	lea    0x1f47(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   116d7:	48 8d 15 b7 24 00 00 	lea    0x24b7(%rip),%rdx        # 13b95 <_IO_stdin_used+0xb95>
   116de:	be 83 10 00 00       	mov    $0x1083,%esi
   116e3:	e8 88 00 00 00       	call   11770 <standalone_panic>
   116e8:	31 c0                	xor    %eax,%eax
   116ea:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   116ee:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   116f2:	49 09 c5             	or     %rax,%r13
   116f5:	0f 85 64 f8 ff ff    	jne    10f5f <zbtIndexScanSlot+0x1bf>
   116fb:	48 8d 3d 1c 1f 00 00 	lea    0x1f1c(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11702:	48 8d 15 97 24 00 00 	lea    0x2497(%rip),%rdx        # 13ba0 <_IO_stdin_used+0xba0>
   11709:	be 9a 10 00 00       	mov    $0x109a,%esi
   1170e:	e8 5d 00 00 00       	call   11770 <standalone_panic>
   11713:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   11717:	e9 43 f8 ff ff       	jmp    10f5f <zbtIndexScanSlot+0x1bf>
   1171c:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   11720:	4c 01 d9             	add    %r11,%rcx
   11723:	48 83 c1 39          	add    $0x39,%rcx
   11727:	eb 0d                	jmp    11736 <zbtIndexScanSlot+0x996>
   11729:	48 83 c2 02          	add    $0x2,%rdx
   1172d:	48 39 d0             	cmp    %rdx,%rax
   11730:	0f 84 e2 fb ff ff    	je     11318 <zbtIndexScanSlot+0x578>
   11736:	44 38 64 11 ff       	cmp    %r12b,-0x1(%rcx,%rdx,1)
   1173b:	75 15                	jne    11752 <zbtIndexScanSlot+0x9b2>
   1173d:	44 89 fe             	mov    %r15d,%esi
   11740:	41 ff c7             	inc    %r15d
   11743:	89 94 b5 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rsi,4)
   1174a:	44 38 24 11          	cmp    %r12b,(%rcx,%rdx,1)
   1174e:	75 d9                	jne    11729 <zbtIndexScanSlot+0x989>
   11750:	eb 06                	jmp    11758 <zbtIndexScanSlot+0x9b8>
   11752:	44 38 24 11          	cmp    %r12b,(%rcx,%rdx,1)
   11756:	75 d1                	jne    11729 <zbtIndexScanSlot+0x989>
   11758:	44 89 fe             	mov    %r15d,%esi
   1175b:	41 ff c7             	inc    %r15d
   1175e:	8d 7a 01             	lea    0x1(%rdx),%edi
   11761:	89 bc b5 00 fe ff ff 	mov    %edi,-0x200(%rbp,%rsi,4)
   11768:	eb bf                	jmp    11729 <zbtIndexScanSlot+0x989>

Disassembly of section .fini:
