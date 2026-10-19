
scratch/amd-scan-mechanism/A-profile:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000010f80 <zbtIndexScanSlot>:
   10f80:	55                   	push   %rbp
   10f81:	48 89 e5             	mov    %rsp,%rbp
   10f84:	41 57                	push   %r15
   10f86:	41 56                	push   %r14
   10f88:	41 55                	push   %r13
   10f8a:	41 54                	push   %r12
   10f8c:	53                   	push   %rbx
   10f8d:	48 81 ec d8 01 00 00 	sub    $0x1d8,%rsp
   10f94:	89 c8                	mov    %ecx,%eax
   10f96:	49 89 d3             	mov    %rdx,%r11
   10f99:	49 89 f5             	mov    %rsi,%r13
   10f9c:	4c 8b 22             	mov    (%rdx),%r12
   10f9f:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   10fa6:	49 d3 ec             	shr    %cl,%r12
   10fa9:	49 89 ff             	mov    %rdi,%r15
   10fac:	8b 56 20             	mov    0x20(%rsi),%edx
   10faf:	89 c0                	mov    %eax,%eax
   10fb1:	85 d2                	test   %edx,%edx
   10fb3:	74 18                	je     10fcd <zbtIndexScanSlot+0x4d>
   10fb5:	45 8b 74 83 10       	mov    0x10(%r11,%rax,4),%r14d
   10fba:	31 c0                	xor    %eax,%eax
   10fbc:	4c 89 e3             	mov    %r12,%rbx
   10fbf:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10fc6:	75 2d                	jne    10ff5 <zbtIndexScanSlot+0x75>
   10fc8:	e9 79 01 00 00       	jmp    11146 <zbtIndexScanSlot+0x1c6>
   10fcd:	41 0f b7 4c 43 10    	movzwl 0x10(%r11,%rax,2),%ecx
   10fd3:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   10fd9:	41 be ff ff ff ff    	mov    $0xffffffff,%r14d
   10fdf:	44 0f 45 f1          	cmovne %ecx,%r14d
   10fe3:	31 c0                	xor    %eax,%eax
   10fe5:	4c 89 e3             	mov    %r12,%rbx
   10fe8:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10fef:	0f 84 51 01 00 00    	je     11146 <zbtIndexScanSlot+0x1c6>
   10ff5:	41 83 fe ff          	cmp    $0xffffffff,%r14d
   10ff9:	0f 84 47 01 00 00    	je     11146 <zbtIndexScanSlot+0x1c6>
   10fff:	4d 85 c9             	test   %r9,%r9
   11002:	0f 84 7c 00 00 00    	je     11084 <zbtIndexScanSlot+0x104>
   11008:	49 ba 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%r10
   1100f:	79 37 9e
   11012:	4c 0f af d3          	imul   %rbx,%r10
   11016:	4c 89 d1             	mov    %r10,%rcx
   11019:	48 c1 e9 3a          	shr    $0x3a,%rcx
   1101d:	be 01 00 00 00       	mov    $0x1,%esi
   11022:	48 d3 e6             	shl    %cl,%rsi
   11025:	4c 89 c7             	mov    %r8,%rdi
   11028:	4d 39 c8             	cmp    %r9,%r8
   1102b:	73 4e                	jae    1107b <zbtIndexScanSlot+0xfb>
   1102d:	4c 0f ab e6          	bts    %r12,%rsi
   11031:	49 c1 ea 24          	shr    $0x24,%r10
   11035:	4c 0f ab d6          	bts    %r10,%rsi
   11039:	31 c9                	xor    %ecx,%ecx
   1103b:	85 d2                	test   %edx,%edx
   1103d:	0f 95 c1             	setne  %cl
   11040:	49 8b 55 00          	mov    0x0(%r13),%rdx
   11044:	c1 e1 04             	shl    $0x4,%ecx
   11047:	48 83 c9 20          	or     $0x20,%rcx
   1104b:	48 89 cf             	mov    %rcx,%rdi
   1104e:	49 0f af f8          	imul   %r8,%rdi
   11052:	48 01 fa             	add    %rdi,%rdx
   11055:	48 83 c2 08          	add    $0x8,%rdx
   11059:	31 c0                	xor    %eax,%eax
   1105b:	4c 89 c7             	mov    %r8,%rdi
   1105e:	66 90                	xchg   %ax,%ax
   11060:	4c 8b 12             	mov    (%rdx),%r10
   11063:	49 f7 d2             	not    %r10
   11066:	4c 85 d6             	test   %r10,%rsi
   11069:	74 10                	je     1107b <zbtIndexScanSlot+0xfb>
   1106b:	48 ff c7             	inc    %rdi
   1106e:	48 01 ca             	add    %rcx,%rdx
   11071:	49 39 f9             	cmp    %rdi,%r9
   11074:	75 ea                	jne    11060 <zbtIndexScanSlot+0xe0>
   11076:	e9 cb 00 00 00       	jmp    11146 <zbtIndexScanSlot+0x1c6>
   1107b:	4c 39 cf             	cmp    %r9,%rdi
   1107e:	0f 84 c0 00 00 00    	je     11144 <zbtIndexScanSlot+0x1c4>
   11084:	45 3b 77 54          	cmp    0x54(%r15),%r14d
   11088:	0f 83 8e 00 00 00    	jae    1111c <zbtIndexScanSlot+0x19c>
   1108e:	49 8b 4f 48          	mov    0x48(%r15),%rcx
   11092:	44 89 f2             	mov    %r14d,%edx
   11095:	48 8b 14 d1          	mov    (%rcx,%rdx,8),%rdx
   11099:	48 85 d2             	test   %rdx,%rdx
   1109c:	74 7e                	je     1111c <zbtIndexScanSlot+0x19c>
   1109e:	89 d1                	mov    %edx,%ecx
   110a0:	83 e1 01             	and    $0x1,%ecx
   110a3:	75 77                	jne    1111c <zbtIndexScanSlot+0x19c>
   110a5:	48 89 55 c8          	mov    %rdx,-0x38(%rbp)
   110a9:	44 39 72 30          	cmp    %r14d,0x30(%rdx)
   110ad:	4c 89 45 98          	mov    %r8,-0x68(%rbp)
   110b1:	4c 89 5d 90          	mov    %r11,-0x70(%rbp)
   110b5:	74 1e                	je     110d5 <zbtIndexScanSlot+0x155>
   110b7:	48 8d 3d 21 26 00 00 	lea    0x2621(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   110be:	48 8d 15 8c 27 00 00 	lea    0x278c(%rip),%rdx        # 13851 <_IO_stdin_used+0x851>
   110c5:	be 6d 10 00 00       	mov    $0x106d,%esi
   110ca:	4d 89 ce             	mov    %r9,%r14
   110cd:	e8 3e 08 00 00       	call   11910 <standalone_panic>
   110d2:	4d 89 f1             	mov    %r14,%r9
   110d5:	49 8b 47 40          	mov    0x40(%r15),%rax
   110d9:	48 85 c0             	test   %rax,%rax
   110dc:	74 19                	je     110f7 <zbtIndexScanSlot+0x177>
   110de:	48 8b 4d c8          	mov    -0x38(%rbp),%rcx
   110e2:	0f b7 49 16          	movzwl 0x16(%rcx),%ecx
   110e6:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   110ea:	0f 94 c1             	sete   %cl
   110ed:	4c 39 e8             	cmp    %r13,%rax
   110f0:	0f 95 c0             	setne  %al
   110f3:	38 c8                	cmp    %cl,%al
   110f5:	74 4d                	je     11144 <zbtIndexScanSlot+0x1c4>
   110f7:	48 8b 55 c8          	mov    -0x38(%rbp),%rdx
   110fb:	0f b6 4a 34          	movzbl 0x34(%rdx),%ecx
   110ff:	45 31 f6             	xor    %r14d,%r14d
   11102:	0f b6 42 11          	movzbl 0x11(%rdx),%eax
   11106:	48 85 c9             	test   %rcx,%rcx
   11109:	74 4d                	je     11158 <zbtIndexScanSlot+0x1d8>
   1110b:	0f af c8             	imul   %eax,%ecx
   1110e:	83 c1 07             	add    $0x7,%ecx
   11111:	c1 e9 03             	shr    $0x3,%ecx
   11114:	83 c1 09             	add    $0x9,%ecx
   11117:	83 e1 fe             	and    $0xfffffffe,%ecx
   1111a:	eb 3e                	jmp    1115a <zbtIndexScanSlot+0x1da>
   1111c:	49 83 7f 40 00       	cmpq   $0x0,0x40(%r15)
   11121:	74 09                	je     1112c <zbtIndexScanSlot+0x1ac>
   11123:	49 83 c7 18          	add    $0x18,%r15
   11127:	4d 39 ef             	cmp    %r13,%r15
   1112a:	74 18                	je     11144 <zbtIndexScanSlot+0x1c4>
   1112c:	48 8d 3d ac 25 00 00 	lea    0x25ac(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11133:	48 8d 15 36 27 00 00 	lea    0x2736(%rip),%rdx        # 13870 <_IO_stdin_used+0x870>
   1113a:	be 6a 10 00 00       	mov    $0x106a,%esi
   1113f:	e8 cc 07 00 00       	call   11910 <standalone_panic>
   11144:	31 c0                	xor    %eax,%eax
   11146:	48 81 c4 d8 01 00 00 	add    $0x1d8,%rsp
   1114d:	5b                   	pop    %rbx
   1114e:	41 5c                	pop    %r12
   11150:	41 5d                	pop    %r13
   11152:	41 5e                	pop    %r14
   11154:	41 5f                	pop    %r15
   11156:	5d                   	pop    %rbp
   11157:	c3                   	ret
   11158:	31 c9                	xor    %ecx,%ecx
   1115a:	48 01 d1             	add    %rdx,%rcx
   1115d:	48 83 c1 38          	add    $0x38,%rcx
   11161:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   11165:	0f b6 52 35          	movzbl 0x35(%rdx),%edx
   11169:	88 55 d7             	mov    %dl,-0x29(%rbp)
   1116c:	8d 70 ff             	lea    -0x1(%rax),%esi
   1116f:	41 bf 00 00 00 00    	mov    $0x0,%r15d
   11175:	3c 10                	cmp    $0x10,%al
   11177:	0f 82 19 01 00 00    	jb     11296 <zbtIndexScanSlot+0x316>
   1117d:	4d 89 cb             	mov    %r9,%r11
   11180:	41 0f b6 d4          	movzbl %r12b,%edx
   11184:	66 0f 6e c2          	movd   %edx,%xmm0
   11188:	66 0f 60 c0          	punpcklbw %xmm0,%xmm0
   1118c:	f2 0f 70 c0 00       	pshuflw $0x0,%xmm0,%xmm0
   11191:	66 0f 70 c0 00       	pshufd $0x0,%xmm0,%xmm0
   11196:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   1119a:	74 7d                	je     11219 <zbtIndexScanSlot+0x299>
   1119c:	31 ff                	xor    %edi,%edi
   1119e:	41 b9 10 00 00 00    	mov    $0x10,%r9d
   111a4:	45 31 ff             	xor    %r15d,%r15d
   111a7:	eb 18                	jmp    111c1 <zbtIndexScanSlot+0x241>
   111a9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   111b0:	4d 8d 4e 10          	lea    0x10(%r14),%r9
   111b4:	48 83 c7 10          	add    $0x10,%rdi
   111b8:	49 39 c1             	cmp    %rax,%r9
   111bb:	0f 87 d2 00 00 00    	ja     11293 <zbtIndexScanSlot+0x313>
   111c1:	4d 89 ce             	mov    %r9,%r14
   111c4:	f3 0f 6f 0c 39       	movdqu (%rcx,%rdi,1),%xmm1
   111c9:	66 0f ef d2          	pxor   %xmm2,%xmm2
   111cd:	41 80 fc 01          	cmp    $0x1,%r12b
   111d1:	75 04                	jne    111d7 <zbtIndexScanSlot+0x257>
   111d3:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   111d7:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   111db:	66 0f eb ca          	por    %xmm2,%xmm1
   111df:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   111e4:	45 85 c9             	test   %r9d,%r9d
   111e7:	74 c7                	je     111b0 <zbtIndexScanSlot+0x230>
   111e9:	45 0f b7 c9          	movzwl %r9w,%r9d
   111ed:	0f 1f 00             	nopl   (%rax)
   111f0:	f3 41 0f bc d1       	tzcnt  %r9d,%edx
   111f5:	01 fa                	add    %edi,%edx
   111f7:	41 89 f2             	mov    %esi,%r10d
   111fa:	41 29 d2             	sub    %edx,%r10d
   111fd:	44 89 fa             	mov    %r15d,%edx
   11200:	41 ff c7             	inc    %r15d
   11203:	44 89 94 95 00 fe ff 	mov    %r10d,-0x200(%rbp,%rdx,4)
   1120a:	ff
   1120b:	41 8d 51 ff          	lea    -0x1(%r9),%edx
   1120f:	44 21 ca             	and    %r9d,%edx
   11212:	41 89 d1             	mov    %edx,%r9d
   11215:	75 d9                	jne    111f0 <zbtIndexScanSlot+0x270>
   11217:	eb 97                	jmp    111b0 <zbtIndexScanSlot+0x230>
   11219:	31 ff                	xor    %edi,%edi
   1121b:	41 b9 10 00 00 00    	mov    $0x10,%r9d
   11221:	45 31 ff             	xor    %r15d,%r15d
   11224:	eb 17                	jmp    1123d <zbtIndexScanSlot+0x2bd>
   11226:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   1122d:	00 00 00
   11230:	4d 8d 4e 10          	lea    0x10(%r14),%r9
   11234:	48 83 c7 10          	add    $0x10,%rdi
   11238:	49 39 c1             	cmp    %rax,%r9
   1123b:	77 56                	ja     11293 <zbtIndexScanSlot+0x313>
   1123d:	4d 89 ce             	mov    %r9,%r14
   11240:	f3 0f 6f 0c 39       	movdqu (%rcx,%rdi,1),%xmm1
   11245:	66 0f ef d2          	pxor   %xmm2,%xmm2
   11249:	41 80 fc 01          	cmp    $0x1,%r12b
   1124d:	75 04                	jne    11253 <zbtIndexScanSlot+0x2d3>
   1124f:	66 0f 74 d1          	pcmpeqb %xmm1,%xmm2
   11253:	66 0f 74 c8          	pcmpeqb %xmm0,%xmm1
   11257:	66 0f eb ca          	por    %xmm2,%xmm1
   1125b:	66 44 0f d7 c9       	pmovmskb %xmm1,%r9d
   11260:	45 85 c9             	test   %r9d,%r9d
   11263:	74 cb                	je     11230 <zbtIndexScanSlot+0x2b0>
   11265:	45 0f b7 c9          	movzwl %r9w,%r9d
   11269:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
   11270:	f3 41 0f bc d1       	tzcnt  %r9d,%edx
   11275:	01 fa                	add    %edi,%edx
   11277:	45 89 fa             	mov    %r15d,%r10d
   1127a:	41 ff c7             	inc    %r15d
   1127d:	42 89 94 95 00 fe ff 	mov    %edx,-0x200(%rbp,%r10,4)
   11284:	ff
   11285:	41 8d 51 ff          	lea    -0x1(%r9),%edx
   11289:	44 21 ca             	and    %r9d,%edx
   1128c:	41 89 d1             	mov    %edx,%r9d
   1128f:	75 df                	jne    11270 <zbtIndexScanSlot+0x2f0>
   11291:	eb 9d                	jmp    11230 <zbtIndexScanSlot+0x2b0>
   11293:	4d 89 d9             	mov    %r11,%r9
   11296:	4c 89 4d b0          	mov    %r9,-0x50(%rbp)
   1129a:	89 c2                	mov    %eax,%edx
   1129c:	c1 ea 03             	shr    $0x3,%edx
   1129f:	41 c1 ee 03          	shr    $0x3,%r14d
   112a3:	48 89 55 c0          	mov    %rdx,-0x40(%rbp)
   112a7:	41 39 d6             	cmp    %edx,%r14d
   112aa:	4c 89 6d a0          	mov    %r13,-0x60(%rbp)
   112ae:	0f 83 b8 01 00 00    	jae    1146c <zbtIndexScanSlot+0x4ec>
   112b4:	48 ba 01 01 01 01 01 	movabs $0x101010101010101,%rdx
   112bb:	01 01 01
   112be:	48 0f af da          	imul   %rdx,%rbx
   112c2:	45 89 f0             	mov    %r14d,%r8d
   112c5:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   112c9:	0f 84 d6 00 00 00    	je     113a5 <zbtIndexScanSlot+0x425>
   112cf:	45 89 e2             	mov    %r12d,%r10d
   112d2:	41 80 f2 01          	xor    $0x1,%r10b
   112d6:	eb 15                	jmp    112ed <zbtIndexScanSlot+0x36d>
   112d8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   112df:	00
   112e0:	49 ff c0             	inc    %r8
   112e3:	4c 3b 45 c0          	cmp    -0x40(%rbp),%r8
   112e7:	0f 84 7f 01 00 00    	je     1146c <zbtIndexScanSlot+0x4ec>
   112ed:	48 89 c7             	mov    %rax,%rdi
   112f0:	4e 8d 1c c5 00 00 00 	lea    0x0(,%r8,8),%r11
   112f7:	00
   112f8:	4c 89 da             	mov    %r11,%rdx
   112fb:	48 b8 f8 ff ff ff 07 	movabs $0x7fffffff8,%rax
   11302:	00 00 00
   11305:	48 21 c2             	and    %rax,%rdx
   11308:	4c 8b 34 11          	mov    (%rcx,%rdx,1),%r14
   1130c:	4c 89 f2             	mov    %r14,%rdx
   1130f:	48 31 da             	xor    %rbx,%rdx
   11312:	49 89 d5             	mov    %rdx,%r13
   11315:	49 f7 d5             	not    %r13
   11318:	49 b9 ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r9
   1131f:	fe fe fe
   11322:	4c 01 ca             	add    %r9,%rdx
   11325:	48 b8 80 80 80 80 80 	movabs $0x8080808080808080,%rax
   1132c:	80 80 80
   1132f:	49 21 c5             	and    %rax,%r13
   11332:	49 21 d5             	and    %rdx,%r13
   11335:	41 80 fc 01          	cmp    $0x1,%r12b
   11339:	75 10                	jne    1134b <zbtIndexScanSlot+0x3cb>
   1133b:	4b 8d 14 0e          	lea    (%r14,%r9,1),%rdx
   1133f:	49 f7 d6             	not    %r14
   11342:	49 21 c6             	and    %rax,%r14
   11345:	49 21 d6             	and    %rdx,%r14
   11348:	4d 09 f5             	or     %r14,%r13
   1134b:	4d 85 ed             	test   %r13,%r13
   1134e:	48 89 f8             	mov    %rdi,%rax
   11351:	75 2d                	jne    11380 <zbtIndexScanSlot+0x400>
   11353:	eb 8b                	jmp    112e0 <zbtIndexScanSlot+0x360>
   11355:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   1135c:	00 00 00 00
   11360:	89 f2                	mov    %esi,%edx
   11362:	44 29 f2             	sub    %r14d,%edx
   11365:	45 89 f9             	mov    %r15d,%r9d
   11368:	41 ff c7             	inc    %r15d
   1136b:	42 89 94 8d 00 fe ff 	mov    %edx,-0x200(%rbp,%r9,4)
   11372:	ff
   11373:	49 8d 55 ff          	lea    -0x1(%r13),%rdx
   11377:	49 21 d5             	and    %rdx,%r13
   1137a:	0f 84 60 ff ff ff    	je     112e0 <zbtIndexScanSlot+0x360>
   11380:	f3 4d 0f bc f5       	tzcnt  %r13,%r14
   11385:	41 c1 ee 03          	shr    $0x3,%r14d
   11389:	45 09 de             	or     %r11d,%r14d
   1138c:	46 0f b6 0c 31       	movzbl (%rcx,%r14,1),%r9d
   11391:	44 89 d2             	mov    %r10d,%edx
   11394:	44 08 ca             	or     %r9b,%dl
   11397:	0f 94 c2             	sete   %dl
   1139a:	45 38 e1             	cmp    %r12b,%r9b
   1139d:	74 c1                	je     11360 <zbtIndexScanSlot+0x3e0>
   1139f:	84 d2                	test   %dl,%dl
   113a1:	74 d0                	je     11373 <zbtIndexScanSlot+0x3f3>
   113a3:	eb bb                	jmp    11360 <zbtIndexScanSlot+0x3e0>
   113a5:	48 bf f8 ff ff ff 07 	movabs $0x7fffffff8,%rdi
   113ac:	00 00 00
   113af:	45 89 e1             	mov    %r12d,%r9d
   113b2:	41 80 f1 01          	xor    $0x1,%r9b
   113b6:	48 be 80 80 80 80 80 	movabs $0x8080808080808080,%rsi
   113bd:	80 80 80
   113c0:	eb 1b                	jmp    113dd <zbtIndexScanSlot+0x45d>
   113c2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   113c9:	1f 84 00 00 00 00 00
   113d0:	49 ff c0             	inc    %r8
   113d3:	4c 3b 45 c0          	cmp    -0x40(%rbp),%r8
   113d7:	0f 84 8f 00 00 00    	je     1146c <zbtIndexScanSlot+0x4ec>
   113dd:	4e 8d 14 c5 00 00 00 	lea    0x0(,%r8,8),%r10
   113e4:	00
   113e5:	4c 89 d2             	mov    %r10,%rdx
   113e8:	48 21 fa             	and    %rdi,%rdx
   113eb:	4c 8b 34 11          	mov    (%rcx,%rdx,1),%r14
   113ef:	4c 89 f2             	mov    %r14,%rdx
   113f2:	48 31 da             	xor    %rbx,%rdx
   113f5:	49 89 d3             	mov    %rdx,%r11
   113f8:	49 f7 d3             	not    %r11
   113fb:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   11402:	fe fe fe
   11405:	4c 01 ea             	add    %r13,%rdx
   11408:	49 21 f3             	and    %rsi,%r11
   1140b:	49 21 d3             	and    %rdx,%r11
   1140e:	41 80 fc 01          	cmp    $0x1,%r12b
   11412:	75 10                	jne    11424 <zbtIndexScanSlot+0x4a4>
   11414:	4b 8d 14 2e          	lea    (%r14,%r13,1),%rdx
   11418:	49 f7 d6             	not    %r14
   1141b:	49 21 f6             	and    %rsi,%r14
   1141e:	49 21 d6             	and    %rdx,%r14
   11421:	4d 09 f3             	or     %r14,%r11
   11424:	4d 85 db             	test   %r11,%r11
   11427:	75 1e                	jne    11447 <zbtIndexScanSlot+0x4c7>
   11429:	eb a5                	jmp    113d0 <zbtIndexScanSlot+0x450>
   1142b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   11430:	44 89 fa             	mov    %r15d,%edx
   11433:	41 ff c7             	inc    %r15d
   11436:	44 89 b4 95 00 fe ff 	mov    %r14d,-0x200(%rbp,%rdx,4)
   1143d:	ff
   1143e:	49 8d 53 ff          	lea    -0x1(%r11),%rdx
   11442:	49 21 d3             	and    %rdx,%r11
   11445:	74 89                	je     113d0 <zbtIndexScanSlot+0x450>
   11447:	f3 4d 0f bc f3       	tzcnt  %r11,%r14
   1144c:	41 c1 ee 03          	shr    $0x3,%r14d
   11450:	45 09 d6             	or     %r10d,%r14d
   11453:	46 0f b6 2c 31       	movzbl (%rcx,%r14,1),%r13d
   11458:	44 89 ca             	mov    %r9d,%edx
   1145b:	44 08 ea             	or     %r13b,%dl
   1145e:	0f 94 c2             	sete   %dl
   11461:	45 38 e5             	cmp    %r12b,%r13b
   11464:	74 ca                	je     11430 <zbtIndexScanSlot+0x4b0>
   11466:	84 d2                	test   %dl,%dl
   11468:	74 d4                	je     1143e <zbtIndexScanSlot+0x4be>
   1146a:	eb c4                	jmp    11430 <zbtIndexScanSlot+0x4b0>
   1146c:	a8 07                	test   $0x7,%al
   1146e:	74 6c                	je     114dc <zbtIndexScanSlot+0x55c>
   11470:	89 c6                	mov    %eax,%esi
   11472:	83 e6 f8             	and    $0xfffffff8,%esi
   11475:	41 80 fc 01          	cmp    $0x1,%r12b
   11479:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   1147d:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11481:	0f 85 24 04 00 00    	jne    118ab <zbtIndexScanSlot+0x92b>
   11487:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   1148b:	74 3a                	je     114c7 <zbtIndexScanSlot+0x547>
   1148d:	89 c2                	mov    %eax,%edx
   1148f:	f7 d2                	not    %edx
   11491:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   11497:	01 c2                	add    %eax,%edx
   11499:	eb 0f                	jmp    114aa <zbtIndexScanSlot+0x52a>
   1149b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   114a0:	48 ff c6             	inc    %rsi
   114a3:	ff ca                	dec    %edx
   114a5:	48 39 c6             	cmp    %rax,%rsi
   114a8:	73 3a                	jae    114e4 <zbtIndexScanSlot+0x564>
   114aa:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   114ae:	77 f0                	ja     114a0 <zbtIndexScanSlot+0x520>
   114b0:	44 89 ff             	mov    %r15d,%edi
   114b3:	41 ff c7             	inc    %r15d
   114b6:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   114bd:	eb e1                	jmp    114a0 <zbtIndexScanSlot+0x520>
   114bf:	48 ff c6             	inc    %rsi
   114c2:	48 39 c6             	cmp    %rax,%rsi
   114c5:	73 1d                	jae    114e4 <zbtIndexScanSlot+0x564>
   114c7:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   114cb:	77 f2                	ja     114bf <zbtIndexScanSlot+0x53f>
   114cd:	44 89 fa             	mov    %r15d,%edx
   114d0:	41 ff c7             	inc    %r15d
   114d3:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   114da:	eb e3                	jmp    114bf <zbtIndexScanSlot+0x53f>
   114dc:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   114e0:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   114e4:	45 85 ff             	test   %r15d,%r15d
   114e7:	0f 84 79 03 00 00    	je     11866 <zbtIndexScanSlot+0x8e6>
   114ed:	49 8d 43 38          	lea    0x38(%r11),%rax
   114f1:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
   114f5:	4d 85 f6             	test   %r14,%r14
   114f8:	0f 95 c0             	setne  %al
   114fb:	41 83 ff 01          	cmp    $0x1,%r15d
   114ff:	0f 95 c1             	setne  %cl
   11502:	08 c1                	or     %al,%cl
   11504:	88 4d d7             	mov    %cl,-0x29(%rbp)
   11507:	44 89 f8             	mov    %r15d,%eax
   1150a:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   1150e:	31 db                	xor    %ebx,%ebx
   11510:	31 c0                	xor    %eax,%eax
   11512:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   11516:	eb 57                	jmp    1156f <zbtIndexScanSlot+0x5ef>
   11518:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   1151f:	00
   11520:	45 31 d2             	xor    %r10d,%r10d
   11523:	4c 89 d0             	mov    %r10,%rax
   11526:	48 f7 d8             	neg    %rax
   11529:	45 84 c0             	test   %r8b,%r8b
   1152c:	49 0f 44 c2          	cmove  %r10,%rax
   11530:	49 03 43 28          	add    0x28(%r11),%rax
   11534:	48 89 c1             	mov    %rax,%rcx
   11537:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   1153e:	ff ff 7f
   11541:	48 21 f9             	and    %rdi,%rcx
   11544:	48 85 c0             	test   %rax,%rax
   11547:	48 f7 d0             	not    %rax
   1154a:	48 0f 48 c1          	cmovs  %rcx,%rax
   1154e:	66 48 0f 6e c0       	movq   %rax,%xmm0
   11553:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11557:	ff 55 10             	call   *0x10(%rbp)
   1155a:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   1155e:	48 ff 45 b8          	incq   -0x48(%rbp)
   11562:	48 ff c3             	inc    %rbx
   11565:	48 3b 5d 88          	cmp    -0x78(%rbp),%rbx
   11569:	0f 84 15 03 00 00    	je     11884 <zbtIndexScanSlot+0x904>
   1156f:	44 8b a4 9d 00 fe ff 	mov    -0x200(%rbp,%rbx,4),%r12d
   11576:	ff
   11577:	45 89 e5             	mov    %r12d,%r13d
   1157a:	41 f7 d5             	not    %r13d
   1157d:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   11581:	0f 84 29 01 00 00    	je     116b0 <zbtIndexScanSlot+0x730>
   11587:	41 0f b6 43 34       	movzbl 0x34(%r11),%eax
   1158c:	48 85 c0             	test   %rax,%rax
   1158f:	74 4e                	je     115df <zbtIndexScanSlot+0x65f>
   11591:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   11596:	0f af c1             	imul   %ecx,%eax
   11599:	83 c0 07             	add    $0x7,%eax
   1159c:	c1 e8 03             	shr    $0x3,%eax
   1159f:	83 c0 09             	add    $0x9,%eax
   115a2:	83 e0 fe             	and    $0xfffffffe,%eax
   115a5:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   115aa:	44 89 e1             	mov    %r12d,%ecx
   115ad:	74 08                	je     115b7 <zbtIndexScanSlot+0x637>
   115af:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   115b4:	44 01 e9             	add    %r13d,%ecx
   115b7:	48 03 45 c0          	add    -0x40(%rbp),%rax
   115bb:	89 c9                	mov    %ecx,%ecx
   115bd:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   115c1:	49 8d 3c 03          	lea    (%r11,%rax,1),%rdi
   115c5:	41 0f b6 34 03       	movzbl (%r11,%rax,1),%esi
   115ca:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   115d0:	74 1b                	je     115ed <zbtIndexScanSlot+0x66d>
   115d2:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   115d8:	75 1e                	jne    115f8 <zbtIndexScanSlot+0x678>
   115da:	8b 47 01             	mov    0x1(%rdi),%eax
   115dd:	eb 2a                	jmp    11609 <zbtIndexScanSlot+0x689>
   115df:	31 c0                	xor    %eax,%eax
   115e1:	41 80 7b 35 00       	cmpb   $0x0,0x35(%r11)
   115e6:	44 89 e1             	mov    %r12d,%ecx
   115e9:	75 c4                	jne    115af <zbtIndexScanSlot+0x62f>
   115eb:	eb ca                	jmp    115b7 <zbtIndexScanSlot+0x637>
   115ed:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   115f1:	b8 03 00 00 00       	mov    $0x3,%eax
   115f6:	eb 05                	jmp    115fd <zbtIndexScanSlot+0x67d>
   115f8:	b8 01 00 00 00       	mov    $0x1,%eax
   115fd:	48 01 c7             	add    %rax,%rdi
   11600:	e8 4b 05 00 00       	call   11b50 <dictGenHashFunction>
   11605:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11609:	89 c0                	mov    %eax,%eax
   1160b:	48 8b 4d a0          	mov    -0x60(%rbp),%rcx
   1160f:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   11613:	4d 85 f6             	test   %r14,%r14
   11616:	74 1a                	je     11632 <zbtIndexScanSlot+0x6b2>
   11618:	8d 71 ff             	lea    -0x1(%rcx),%esi
   1161b:	89 c2                	mov    %eax,%edx
   1161d:	21 f2                	and    %esi,%edx
   1161f:	48 3b 55 98          	cmp    -0x68(%rbp),%rdx
   11623:	0f 82 39 ff ff ff    	jb     11562 <zbtIndexScanSlot+0x5e2>
   11629:	4c 39 f2             	cmp    %r14,%rdx
   1162c:	0f 83 30 ff ff ff    	jae    11562 <zbtIndexScanSlot+0x5e2>
   11632:	41 83 ff 01          	cmp    $0x1,%r15d
   11636:	74 78                	je     116b0 <zbtIndexScanSlot+0x730>
   11638:	48 89 ca             	mov    %rcx,%rdx
   1163b:	48 83 ea 01          	sub    $0x1,%rdx
   1163f:	0f 82 1d ff ff ff    	jb     11562 <zbtIndexScanSlot+0x5e2>
   11645:	21 d0                	and    %edx,%eax
   11647:	31 f6                	xor    %esi,%esi
   11649:	48 8b 7d a0          	mov    -0x60(%rbp),%rdi
   1164d:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   11651:	48 8b 3f             	mov    (%rdi),%rdi
   11654:	40 0f 95 c6          	setne  %sil
   11658:	c1 e6 04             	shl    $0x4,%esi
   1165b:	48 83 ce 20          	or     $0x20,%rsi
   1165f:	90                   	nop
   11660:	49 89 c0             	mov    %rax,%r8
   11663:	4c 0f af c6          	imul   %rsi,%r8
   11667:	49 01 f8             	add    %rdi,%r8
   1166a:	4c 3b 45 90          	cmp    -0x70(%rbp),%r8
   1166e:	74 40                	je     116b0 <zbtIndexScanSlot+0x730>
   11670:	4d 8b 00             	mov    (%r8),%r8
   11673:	4d 89 c1             	mov    %r8,%r9
   11676:	49 f7 d1             	not    %r9
   11679:	49 ba ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r10
   11680:	fe fe fe
   11683:	4d 01 d0             	add    %r10,%r8
   11686:	49 ba 80 80 80 80 80 	movabs $0x8080808080808080,%r10
   1168d:	80 80 80
   11690:	4d 21 d1             	and    %r10,%r9
   11693:	4d 85 c1             	test   %r8,%r9
   11696:	0f 85 c6 fe ff ff    	jne    11562 <zbtIndexScanSlot+0x5e2>
   1169c:	48 ff c0             	inc    %rax
   1169f:	48 21 d0             	and    %rdx,%rax
   116a2:	48 ff c9             	dec    %rcx
   116a5:	75 b9                	jne    11660 <zbtIndexScanSlot+0x6e0>
   116a7:	e9 b6 fe ff ff       	jmp    11562 <zbtIndexScanSlot+0x5e2>
   116ac:	0f 1f 40 00          	nopl   0x0(%rax)
   116b0:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   116b5:	48 85 ff             	test   %rdi,%rdi
   116b8:	0f 84 92 00 00 00    	je     11750 <zbtIndexScanSlot+0x7d0>
   116be:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   116c3:	89 f8                	mov    %edi,%eax
   116c5:	0f af c1             	imul   %ecx,%eax
   116c8:	83 c0 07             	add    $0x7,%eax
   116cb:	c1 e8 03             	shr    $0x3,%eax
   116ce:	83 c0 09             	add    $0x9,%eax
   116d1:	83 e0 fe             	and    $0xfffffffe,%eax
   116d4:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   116d9:	44 89 e1             	mov    %r12d,%ecx
   116dc:	45 84 c0             	test   %r8b,%r8b
   116df:	74 08                	je     116e9 <zbtIndexScanSlot+0x769>
   116e1:	41 0f b6 4b 11       	movzbl 0x11(%r11),%ecx
   116e6:	44 01 e9             	add    %r13d,%ecx
   116e9:	48 03 45 c0          	add    -0x40(%rbp),%rax
   116ed:	89 c9                	mov    %ecx,%ecx
   116ef:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   116f3:	4d 8d 34 03          	lea    (%r11,%rax,1),%r14
   116f7:	41 0f b6 14 03       	movzbl (%r11,%rax,1),%edx
   116fc:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11703:	77 1b                	ja     11720 <zbtIndexScanSlot+0x7a0>
   11705:	49 ff c6             	inc    %r14
   11708:	4c 89 f6             	mov    %r14,%rsi
   1170b:	40 84 ff             	test   %dil,%dil
   1170e:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   11712:	0f 85 b7 00 00 00    	jne    117cf <zbtIndexScanSlot+0x84f>
   11718:	e9 03 fe ff ff       	jmp    11520 <zbtIndexScanSlot+0x5a0>
   1171d:	0f 1f 00             	nopl   (%rax)
   11720:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11726:	75 39                	jne    11761 <zbtIndexScanSlot+0x7e1>
   11728:	41 0f b7 56 01       	movzwl 0x1(%r14),%edx
   1172d:	49 83 c6 03          	add    $0x3,%r14
   11731:	4c 89 f6             	mov    %r14,%rsi
   11734:	40 84 ff             	test   %dil,%dil
   11737:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   1173b:	0f 85 8e 00 00 00    	jne    117cf <zbtIndexScanSlot+0x84f>
   11741:	e9 da fd ff ff       	jmp    11520 <zbtIndexScanSlot+0x5a0>
   11746:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   1174d:	00 00 00
   11750:	31 c0                	xor    %eax,%eax
   11752:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   11757:	44 89 e1             	mov    %r12d,%ecx
   1175a:	45 84 c0             	test   %r8b,%r8b
   1175d:	75 82                	jne    116e1 <zbtIndexScanSlot+0x761>
   1175f:	eb 88                	jmp    116e9 <zbtIndexScanSlot+0x769>
   11761:	49 8b 76 0d          	mov    0xd(%r14),%rsi
   11765:	48 85 f6             	test   %rsi,%rsi
   11768:	75 4a                	jne    117b4 <zbtIndexScanSlot+0x834>
   1176a:	48 8d 3d 6e 1f 00 00 	lea    0x1f6e(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11771:	48 89 75 a8          	mov    %rsi,-0x58(%rbp)
   11775:	be 5b 02 00 00       	mov    $0x25b,%esi
   1177a:	48 8d 15 a3 20 00 00 	lea    0x20a3(%rip),%rdx        # 13824 <_IO_stdin_used+0x824>
   11781:	e8 8a 01 00 00       	call   11910 <standalone_panic>
   11786:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   1178a:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   1178e:	41 80 3e ff          	cmpb   $0xff,(%r14)
   11792:	74 20                	je     117b4 <zbtIndexScanSlot+0x834>
   11794:	48 8d 3d 44 1f 00 00 	lea    0x1f44(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   1179b:	be 3b 02 00 00       	mov    $0x23b,%esi
   117a0:	48 8d 15 89 20 00 00 	lea    0x2089(%rip),%rdx        # 13830 <_IO_stdin_used+0x830>
   117a7:	e8 64 01 00 00       	call   11910 <standalone_panic>
   117ac:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   117b0:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   117b4:	49 8b 56 05          	mov    0x5(%r14),%rdx
   117b8:	41 0f b6 7b 34       	movzbl 0x34(%r11),%edi
   117bd:	45 0f b6 43 35       	movzbl 0x35(%r11),%r8d
   117c2:	40 84 ff             	test   %dil,%dil
   117c5:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   117c9:	0f 84 51 fd ff ff    	je     11520 <zbtIndexScanSlot+0x5a0>
   117cf:	45 84 c0             	test   %r8b,%r8b
   117d2:	74 08                	je     117dc <zbtIndexScanSlot+0x85c>
   117d4:	45 0f b6 63 11       	movzbl 0x11(%r11),%r12d
   117d9:	45 01 ec             	add    %r13d,%r12d
   117dc:	44 0f b6 d7          	movzbl %dil,%r10d
   117e0:	45 89 e3             	mov    %r12d,%r11d
   117e3:	44 89 d0             	mov    %r10d,%eax
   117e6:	4c 0f af d8          	imul   %rax,%r11
   117ea:	4d 89 de             	mov    %r11,%r14
   117ed:	49 c1 ee 03          	shr    $0x3,%r14
   117f1:	48 8b 4d c0          	mov    -0x40(%rbp),%rcx
   117f5:	4e 8b 0c 31          	mov    (%rcx,%r14,1),%r9
   117f9:	44 89 d9             	mov    %r11d,%ecx
   117fc:	80 e1 07             	and    $0x7,%cl
   117ff:	49 d3 e9             	shr    %cl,%r9
   11802:	41 83 e3 07          	and    $0x7,%r11d
   11806:	74 28                	je     11830 <zbtIndexScanSlot+0x8b0>
   11808:	b9 40 00 00 00       	mov    $0x40,%ecx
   1180d:	44 29 d9             	sub    %r11d,%ecx
   11810:	44 39 d1             	cmp    %r10d,%ecx
   11813:	73 1b                	jae    11830 <zbtIndexScanSlot+0x8b0>
   11815:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11819:	47 0f b6 54 1e 40    	movzbl 0x40(%r14,%r11,1),%r10d
   1181f:	49 d3 e2             	shl    %cl,%r10
   11822:	4d 09 d1             	or     %r10,%r9
   11825:	eb 0d                	jmp    11834 <zbtIndexScanSlot+0x8b4>
   11827:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
   1182e:	00 00
   11830:	4c 8b 5d c8          	mov    -0x38(%rbp),%r11
   11834:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   1183b:	89 c1                	mov    %eax,%ecx
   1183d:	49 d3 e2             	shl    %cl,%r10
   11840:	40 80 ff 40          	cmp    $0x40,%dil
   11844:	49 f7 d2             	not    %r10
   11847:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   1184e:	4c 0f 43 d0          	cmovae %rax,%r10
   11852:	4d 21 ca             	and    %r9,%r10
   11855:	41 0f b6 4b 13       	movzbl 0x13(%r11),%ecx
   1185a:	49 d3 e2             	shl    %cl,%r10
   1185d:	4c 8b 75 b0          	mov    -0x50(%rbp),%r14
   11861:	e9 bd fc ff ff       	jmp    11523 <zbtIndexScanSlot+0x5a3>
   11866:	48 8d 3d 72 1e 00 00 	lea    0x1e72(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   1186d:	48 8d 15 fb 23 00 00 	lea    0x23fb(%rip),%rdx        # 13c6f <_IO_stdin_used+0xc6f>
   11874:	be 7b 10 00 00       	mov    $0x107b,%esi
   11879:	e8 92 00 00 00       	call   11910 <standalone_panic>
   1187e:	31 c0                	xor    %eax,%eax
   11880:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   11884:	4c 0b 75 b8          	or     -0x48(%rbp),%r14
   11888:	75 18                	jne    118a2 <zbtIndexScanSlot+0x922>
   1188a:	48 8d 3d 4e 1e 00 00 	lea    0x1e4e(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11891:	48 8d 15 e2 23 00 00 	lea    0x23e2(%rip),%rdx        # 13c7a <_IO_stdin_used+0xc7a>
   11898:	be 92 10 00 00       	mov    $0x1092,%esi
   1189d:	e8 6e 00 00 00       	call   11910 <standalone_panic>
   118a2:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   118a6:	e9 9b f8 ff ff       	jmp    11146 <zbtIndexScanSlot+0x1c6>
   118ab:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   118af:	74 3e                	je     118ef <zbtIndexScanSlot+0x96f>
   118b1:	89 c2                	mov    %eax,%edx
   118b3:	f7 d2                	not    %edx
   118b5:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   118bb:	01 c2                	add    %eax,%edx
   118bd:	eb 0f                	jmp    118ce <zbtIndexScanSlot+0x94e>
   118bf:	90                   	nop
   118c0:	48 ff c6             	inc    %rsi
   118c3:	ff ca                	dec    %edx
   118c5:	48 39 c6             	cmp    %rax,%rsi
   118c8:	0f 83 16 fc ff ff    	jae    114e4 <zbtIndexScanSlot+0x564>
   118ce:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   118d2:	75 ec                	jne    118c0 <zbtIndexScanSlot+0x940>
   118d4:	44 89 ff             	mov    %r15d,%edi
   118d7:	41 ff c7             	inc    %r15d
   118da:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   118e1:	eb dd                	jmp    118c0 <zbtIndexScanSlot+0x940>
   118e3:	48 ff c6             	inc    %rsi
   118e6:	48 39 c6             	cmp    %rax,%rsi
   118e9:	0f 83 f5 fb ff ff    	jae    114e4 <zbtIndexScanSlot+0x564>
   118ef:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   118f3:	75 ee                	jne    118e3 <zbtIndexScanSlot+0x963>
   118f5:	44 89 fa             	mov    %r15d,%edx
   118f8:	41 ff c7             	inc    %r15d
   118fb:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   11902:	eb df                	jmp    118e3 <zbtIndexScanSlot+0x963>

Disassembly of section .fini:
