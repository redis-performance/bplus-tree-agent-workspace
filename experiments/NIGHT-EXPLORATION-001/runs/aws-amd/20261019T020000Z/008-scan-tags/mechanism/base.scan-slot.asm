
scratch/amd-scan-mechanism/base-profile:     file format elf64-x86-64


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
   10f94:	4c 89 45 98          	mov    %r8,-0x68(%rbp)
   10f98:	89 c8                	mov    %ecx,%eax
   10f9a:	4c 8b 22             	mov    (%rdx),%r12
   10f9d:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   10fa4:	49 d3 ec             	shr    %cl,%r12
   10fa7:	49 89 ff             	mov    %rdi,%r15
   10faa:	44 8b 5e 20          	mov    0x20(%rsi),%r11d
   10fae:	89 c0                	mov    %eax,%eax
   10fb0:	45 85 db             	test   %r11d,%r11d
   10fb3:	74 18                	je     10fcd <zbtIndexScanSlot+0x4d>
   10fb5:	44 8b 74 82 10       	mov    0x10(%rdx,%rax,4),%r14d
   10fba:	31 c0                	xor    %eax,%eax
   10fbc:	4c 89 e3             	mov    %r12,%rbx
   10fbf:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10fc6:	75 2c                	jne    10ff4 <zbtIndexScanSlot+0x74>
   10fc8:	e9 8a 01 00 00       	jmp    11157 <zbtIndexScanSlot+0x1d7>
   10fcd:	0f b7 4c 42 10       	movzwl 0x10(%rdx,%rax,2),%ecx
   10fd2:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   10fd8:	41 be ff ff ff ff    	mov    $0xffffffff,%r14d
   10fde:	44 0f 45 f1          	cmovne %ecx,%r14d
   10fe2:	31 c0                	xor    %eax,%eax
   10fe4:	4c 89 e3             	mov    %r12,%rbx
   10fe7:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10fee:	0f 84 63 01 00 00    	je     11157 <zbtIndexScanSlot+0x1d7>
   10ff4:	41 83 fe ff          	cmp    $0xffffffff,%r14d
   10ff8:	0f 84 59 01 00 00    	je     11157 <zbtIndexScanSlot+0x1d7>
   10ffe:	4d 85 c9             	test   %r9,%r9
   11001:	0f 84 8d 00 00 00    	je     11094 <zbtIndexScanSlot+0x114>
   11007:	49 b8 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%r8
   1100e:	79 37 9e
   11011:	4c 0f af c3          	imul   %rbx,%r8
   11015:	4c 89 c1             	mov    %r8,%rcx
   11018:	48 c1 e9 3a          	shr    $0x3a,%rcx
   1101c:	41 ba 01 00 00 00    	mov    $0x1,%r10d
   11022:	49 d3 e2             	shl    %cl,%r10
   11025:	48 8b 4d 98          	mov    -0x68(%rbp),%rcx
   11029:	48 89 cf             	mov    %rcx,%rdi
   1102c:	4c 39 c9             	cmp    %r9,%rcx
   1102f:	73 5a                	jae    1108b <zbtIndexScanSlot+0x10b>
   11031:	4d 0f ab e2          	bts    %r12,%r10
   11035:	49 c1 e8 24          	shr    $0x24,%r8
   11039:	4d 0f ab c2          	bts    %r8,%r10
   1103d:	31 c9                	xor    %ecx,%ecx
   1103f:	45 85 db             	test   %r11d,%r11d
   11042:	0f 95 c1             	setne  %cl
   11045:	4c 8b 1e             	mov    (%rsi),%r11
   11048:	c1 e1 04             	shl    $0x4,%ecx
   1104b:	48 83 c9 20          	or     $0x20,%rcx
   1104f:	48 89 cf             	mov    %rcx,%rdi
   11052:	4c 8b 45 98          	mov    -0x68(%rbp),%r8
   11056:	49 0f af f8          	imul   %r8,%rdi
   1105a:	49 01 fb             	add    %rdi,%r11
   1105d:	49 83 c3 08          	add    $0x8,%r11
   11061:	4c 89 c7             	mov    %r8,%rdi
   11064:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   1106b:	00 00 00 00 00
   11070:	4d 8b 03             	mov    (%r11),%r8
   11073:	49 f7 d0             	not    %r8
   11076:	4d 85 c2             	test   %r8,%r10
   11079:	74 10                	je     1108b <zbtIndexScanSlot+0x10b>
   1107b:	48 ff c7             	inc    %rdi
   1107e:	49 01 cb             	add    %rcx,%r11
   11081:	49 39 f9             	cmp    %rdi,%r9
   11084:	75 ea                	jne    11070 <zbtIndexScanSlot+0xf0>
   11086:	e9 ca 00 00 00       	jmp    11155 <zbtIndexScanSlot+0x1d5>
   1108b:	4c 39 cf             	cmp    %r9,%rdi
   1108e:	0f 84 c1 00 00 00    	je     11155 <zbtIndexScanSlot+0x1d5>
   11094:	45 3b 77 54          	cmp    0x54(%r15),%r14d
   11098:	0f 83 8f 00 00 00    	jae    1112d <zbtIndexScanSlot+0x1ad>
   1109e:	49 8b 4f 48          	mov    0x48(%r15),%rcx
   110a2:	44 89 f7             	mov    %r14d,%edi
   110a5:	48 8b 3c f9          	mov    (%rcx,%rdi,8),%rdi
   110a9:	48 85 ff             	test   %rdi,%rdi
   110ac:	74 7f                	je     1112d <zbtIndexScanSlot+0x1ad>
   110ae:	89 f9                	mov    %edi,%ecx
   110b0:	83 e1 01             	and    $0x1,%ecx
   110b3:	75 78                	jne    1112d <zbtIndexScanSlot+0x1ad>
   110b5:	48 89 f9             	mov    %rdi,%rcx
   110b8:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
   110bc:	44 39 77 30          	cmp    %r14d,0x30(%rdi)
   110c0:	4c 89 4d c0          	mov    %r9,-0x40(%rbp)
   110c4:	48 89 75 a8          	mov    %rsi,-0x58(%rbp)
   110c8:	48 89 55 b0          	mov    %rdx,-0x50(%rbp)
   110cc:	74 1c                	je     110ea <zbtIndexScanSlot+0x16a>
   110ce:	48 8d 3d 0a 26 00 00 	lea    0x260a(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   110d5:	48 8d 15 78 27 00 00 	lea    0x2778(%rip),%rdx        # 13854 <_IO_stdin_used+0x854>
   110dc:	be 58 10 00 00       	mov    $0x1058,%esi
   110e1:	e8 9a 07 00 00       	call   11880 <standalone_panic>
   110e6:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   110ea:	49 8b 47 40          	mov    0x40(%r15),%rax
   110ee:	48 85 c0             	test   %rax,%rax
   110f1:	48 8b 55 c8          	mov    -0x38(%rbp),%rdx
   110f5:	74 15                	je     1110c <zbtIndexScanSlot+0x18c>
   110f7:	0f b7 4a 16          	movzwl 0x16(%rdx),%ecx
   110fb:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   110ff:	0f 94 c1             	sete   %cl
   11102:	48 39 f0             	cmp    %rsi,%rax
   11105:	0f 95 c0             	setne  %al
   11108:	38 c8                	cmp    %cl,%al
   1110a:	74 49                	je     11155 <zbtIndexScanSlot+0x1d5>
   1110c:	0f b6 4a 34          	movzbl 0x34(%rdx),%ecx
   11110:	45 31 ff             	xor    %r15d,%r15d
   11113:	0f b6 42 11          	movzbl 0x11(%rdx),%eax
   11117:	48 85 c9             	test   %rcx,%rcx
   1111a:	74 4d                	je     11169 <zbtIndexScanSlot+0x1e9>
   1111c:	0f af c8             	imul   %eax,%ecx
   1111f:	83 c1 07             	add    $0x7,%ecx
   11122:	c1 e9 03             	shr    $0x3,%ecx
   11125:	83 c1 09             	add    $0x9,%ecx
   11128:	83 e1 fe             	and    $0xfffffffe,%ecx
   1112b:	eb 3e                	jmp    1116b <zbtIndexScanSlot+0x1eb>
   1112d:	49 83 7f 40 00       	cmpq   $0x0,0x40(%r15)
   11132:	74 09                	je     1113d <zbtIndexScanSlot+0x1bd>
   11134:	49 83 c7 18          	add    $0x18,%r15
   11138:	49 39 f7             	cmp    %rsi,%r15
   1113b:	74 18                	je     11155 <zbtIndexScanSlot+0x1d5>
   1113d:	48 8d 3d 9b 25 00 00 	lea    0x259b(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11144:	48 8d 15 28 27 00 00 	lea    0x2728(%rip),%rdx        # 13873 <_IO_stdin_used+0x873>
   1114b:	be 55 10 00 00       	mov    $0x1055,%esi
   11150:	e8 2b 07 00 00       	call   11880 <standalone_panic>
   11155:	31 c0                	xor    %eax,%eax
   11157:	48 81 c4 d8 01 00 00 	add    $0x1d8,%rsp
   1115e:	5b                   	pop    %rbx
   1115f:	41 5c                	pop    %r12
   11161:	41 5d                	pop    %r13
   11163:	41 5e                	pop    %r14
   11165:	41 5f                	pop    %r15
   11167:	5d                   	pop    %rbp
   11168:	c3                   	ret
   11169:	31 c9                	xor    %ecx,%ecx
   1116b:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   11172:	fe fe fe
   11175:	48 01 d1             	add    %rdx,%rcx
   11178:	48 83 c1 38          	add    $0x38,%rcx
   1117c:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   11180:	0f b6 52 35          	movzbl 0x35(%rdx),%edx
   11184:	3c 08                	cmp    $0x8,%al
   11186:	73 6b                	jae    111f3 <zbtIndexScanSlot+0x273>
   11188:	a8 07                	test   $0x7,%al
   1118a:	0f 84 20 01 00 00    	je     112b0 <zbtIndexScanSlot+0x330>
   11190:	89 c6                	mov    %eax,%esi
   11192:	83 e6 f8             	and    $0xfffffff8,%esi
   11195:	41 80 fc 01          	cmp    $0x1,%r12b
   11199:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   1119d:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   111a1:	0f 85 04 05 00 00    	jne    116ab <zbtIndexScanSlot+0x72b>
   111a7:	84 d2                	test   %dl,%dl
   111a9:	0f 84 82 06 00 00    	je     11831 <zbtIndexScanSlot+0x8b1>
   111af:	89 c2                	mov    %eax,%edx
   111b1:	f7 d2                	not    %edx
   111b3:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   111b9:	01 c2                	add    %eax,%edx
   111bb:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   111bf:	eb 1d                	jmp    111de <zbtIndexScanSlot+0x25e>
   111c1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   111c8:	0f 1f 84 00 00 00 00
   111cf:	00
   111d0:	48 ff c6             	inc    %rsi
   111d3:	ff ca                	dec    %edx
   111d5:	48 39 c6             	cmp    %rax,%rsi
   111d8:	0f 83 de 00 00 00    	jae    112bc <zbtIndexScanSlot+0x33c>
   111de:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   111e2:	77 ec                	ja     111d0 <zbtIndexScanSlot+0x250>
   111e4:	44 89 ff             	mov    %r15d,%edi
   111e7:	41 ff c7             	inc    %r15d
   111ea:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   111f1:	eb dd                	jmp    111d0 <zbtIndexScanSlot+0x250>
   111f3:	89 c6                	mov    %eax,%esi
   111f5:	c1 ee 03             	shr    $0x3,%esi
   111f8:	49 b8 01 01 01 01 01 	movabs $0x101010101010101,%r8
   111ff:	01 01 01
   11202:	49 0f af d8          	imul   %r8,%rbx
   11206:	84 d2                	test   %dl,%dl
   11208:	0f 84 e5 04 00 00    	je     116f3 <zbtIndexScanSlot+0x773>
   1120e:	8d 78 ff             	lea    -0x1(%rax),%edi
   11211:	41 80 fc 01          	cmp    $0x1,%r12b
   11215:	0f 85 93 05 00 00    	jne    117ae <zbtIndexScanSlot+0x82e>
   1121b:	45 31 c9             	xor    %r9d,%r9d
   1121e:	45 31 ff             	xor    %r15d,%r15d
   11221:	eb 19                	jmp    1123c <zbtIndexScanSlot+0x2bc>
   11223:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   1122a:	84 00 00 00 00 00
   11230:	49 ff c1             	inc    %r9
   11233:	49 39 f1             	cmp    %rsi,%r9
   11236:	0f 84 4c ff ff ff    	je     11188 <zbtIndexScanSlot+0x208>
   1123c:	4e 8b 14 c9          	mov    (%rcx,%r9,8),%r10
   11240:	4d 89 d3             	mov    %r10,%r11
   11243:	49 f7 d3             	not    %r11
   11246:	4c 89 d3             	mov    %r10,%rbx
   11249:	4c 31 c3             	xor    %r8,%rbx
   1124c:	4c 01 eb             	add    %r13,%rbx
   1124f:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   11256:	80 80 80
   11259:	4d 21 f3             	and    %r14,%r11
   1125c:	4d 01 ea             	add    %r13,%r10
   1125f:	49 09 da             	or     %rbx,%r10
   11262:	4d 21 da             	and    %r11,%r10
   11265:	74 c9                	je     11230 <zbtIndexScanSlot+0x2b0>
   11267:	4e 8d 1c cd 00 00 00 	lea    0x0(,%r9,8),%r11
   1126e:	00
   1126f:	eb 18                	jmp    11289 <zbtIndexScanSlot+0x309>
   11271:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11278:	0f 1f 84 00 00 00 00
   1127f:	00
   11280:	49 8d 5a ff          	lea    -0x1(%r10),%rbx
   11284:	49 21 da             	and    %rbx,%r10
   11287:	74 a7                	je     11230 <zbtIndexScanSlot+0x2b0>
   11289:	f3 49 0f bc da       	tzcnt  %r10,%rbx
   1128e:	c1 eb 03             	shr    $0x3,%ebx
   11291:	44 09 db             	or     %r11d,%ebx
   11294:	80 3c 19 01          	cmpb   $0x1,(%rcx,%rbx,1)
   11298:	77 e6                	ja     11280 <zbtIndexScanSlot+0x300>
   1129a:	41 89 fe             	mov    %edi,%r14d
   1129d:	41 29 de             	sub    %ebx,%r14d
   112a0:	44 89 fb             	mov    %r15d,%ebx
   112a3:	41 ff c7             	inc    %r15d
   112a6:	44 89 b4 9d 00 fe ff 	mov    %r14d,-0x200(%rbp,%rbx,4)
   112ad:	ff
   112ae:	eb d0                	jmp    11280 <zbtIndexScanSlot+0x300>
   112b0:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   112b4:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   112b8:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   112bc:	45 85 ff             	test   %r15d,%r15d
   112bf:	0f 84 9d 03 00 00    	je     11662 <zbtIndexScanSlot+0x6e2>
   112c5:	49 8d 41 38          	lea    0x38(%r9),%rax
   112c9:	48 89 45 a0          	mov    %rax,-0x60(%rbp)
   112cd:	4d 85 d2             	test   %r10,%r10
   112d0:	0f 95 c0             	setne  %al
   112d3:	41 83 ff 01          	cmp    $0x1,%r15d
   112d7:	0f 95 c1             	setne  %cl
   112da:	08 c1                	or     %al,%cl
   112dc:	88 4d d7             	mov    %cl,-0x29(%rbp)
   112df:	44 89 f8             	mov    %r15d,%eax
   112e2:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   112e6:	45 31 e4             	xor    %r12d,%r12d
   112e9:	31 c0                	xor    %eax,%eax
   112eb:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   112ef:	e9 8d 00 00 00       	jmp    11381 <zbtIndexScanSlot+0x401>
   112f4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   112fb:	00 00 00 00 00
   11300:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   11307:	89 c1                	mov    %eax,%ecx
   11309:	49 d3 e2             	shl    %cl,%r10
   1130c:	40 80 ff 40          	cmp    $0x40,%dil
   11310:	49 f7 d2             	not    %r10
   11313:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   1131a:	4c 0f 43 d0          	cmovae %rax,%r10
   1131e:	4d 21 ca             	and    %r9,%r10
   11321:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11325:	41 0f b6 49 13       	movzbl 0x13(%r9),%ecx
   1132a:	49 d3 e2             	shl    %cl,%r10
   1132d:	4c 89 d0             	mov    %r10,%rax
   11330:	48 f7 d8             	neg    %rax
   11333:	45 84 c0             	test   %r8b,%r8b
   11336:	49 0f 44 c2          	cmove  %r10,%rax
   1133a:	49 03 41 28          	add    0x28(%r9),%rax
   1133e:	48 89 c1             	mov    %rax,%rcx
   11341:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   11348:	ff ff 7f
   1134b:	48 21 f9             	and    %rdi,%rcx
   1134e:	48 85 c0             	test   %rax,%rax
   11351:	48 f7 d0             	not    %rax
   11354:	48 0f 48 c1          	cmovs  %rcx,%rax
   11358:	66 48 0f 6e c0       	movq   %rax,%xmm0
   1135d:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11361:	ff 55 10             	call   *0x10(%rbp)
   11364:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11368:	48 ff 45 b8          	incq   -0x48(%rbp)
   1136c:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   11370:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   11374:	49 ff c4             	inc    %r12
   11377:	4c 3b 65 88          	cmp    -0x78(%rbp),%r12
   1137b:	0f 84 03 03 00 00    	je     11684 <zbtIndexScanSlot+0x704>
   11381:	42 8b 9c a5 00 fe ff 	mov    -0x200(%rbp,%r12,4),%ebx
   11388:	ff
   11389:	41 89 dd             	mov    %ebx,%r13d
   1138c:	41 f7 d5             	not    %r13d
   1138f:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   11393:	0f 84 37 01 00 00    	je     114d0 <zbtIndexScanSlot+0x550>
   11399:	41 0f b6 41 34       	movzbl 0x34(%r9),%eax
   1139e:	48 85 c0             	test   %rax,%rax
   113a1:	74 4d                	je     113f0 <zbtIndexScanSlot+0x470>
   113a3:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   113a8:	0f af c1             	imul   %ecx,%eax
   113ab:	83 c0 07             	add    $0x7,%eax
   113ae:	c1 e8 03             	shr    $0x3,%eax
   113b1:	83 c0 09             	add    $0x9,%eax
   113b4:	83 e0 fe             	and    $0xfffffffe,%eax
   113b7:	41 80 79 35 00       	cmpb   $0x0,0x35(%r9)
   113bc:	89 d9                	mov    %ebx,%ecx
   113be:	74 08                	je     113c8 <zbtIndexScanSlot+0x448>
   113c0:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   113c5:	44 01 e9             	add    %r13d,%ecx
   113c8:	48 03 45 a0          	add    -0x60(%rbp),%rax
   113cc:	89 c9                	mov    %ecx,%ecx
   113ce:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   113d2:	49 8d 3c 01          	lea    (%r9,%rax,1),%rdi
   113d6:	41 0f b6 34 01       	movzbl (%r9,%rax,1),%esi
   113db:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   113e1:	74 1a                	je     113fd <zbtIndexScanSlot+0x47d>
   113e3:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   113e9:	75 1d                	jne    11408 <zbtIndexScanSlot+0x488>
   113eb:	8b 47 01             	mov    0x1(%rdi),%eax
   113ee:	eb 31                	jmp    11421 <zbtIndexScanSlot+0x4a1>
   113f0:	31 c0                	xor    %eax,%eax
   113f2:	41 80 79 35 00       	cmpb   $0x0,0x35(%r9)
   113f7:	89 d9                	mov    %ebx,%ecx
   113f9:	75 c5                	jne    113c0 <zbtIndexScanSlot+0x440>
   113fb:	eb cb                	jmp    113c8 <zbtIndexScanSlot+0x448>
   113fd:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   11401:	b8 03 00 00 00       	mov    $0x3,%eax
   11406:	eb 05                	jmp    1140d <zbtIndexScanSlot+0x48d>
   11408:	b8 01 00 00 00       	mov    $0x1,%eax
   1140d:	48 01 c7             	add    %rax,%rdi
   11410:	e8 ab 06 00 00       	call   11ac0 <dictGenHashFunction>
   11415:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   11419:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   1141d:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11421:	89 c0                	mov    %eax,%eax
   11423:	48 8b 4d a8          	mov    -0x58(%rbp),%rcx
   11427:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   1142b:	4d 85 d2             	test   %r10,%r10
   1142e:	74 1a                	je     1144a <zbtIndexScanSlot+0x4ca>
   11430:	8d 71 ff             	lea    -0x1(%rcx),%esi
   11433:	89 c2                	mov    %eax,%edx
   11435:	21 f2                	and    %esi,%edx
   11437:	48 3b 55 98          	cmp    -0x68(%rbp),%rdx
   1143b:	0f 82 33 ff ff ff    	jb     11374 <zbtIndexScanSlot+0x3f4>
   11441:	4c 39 d2             	cmp    %r10,%rdx
   11444:	0f 83 2a ff ff ff    	jae    11374 <zbtIndexScanSlot+0x3f4>
   1144a:	41 83 ff 01          	cmp    $0x1,%r15d
   1144e:	0f 84 7c 00 00 00    	je     114d0 <zbtIndexScanSlot+0x550>
   11454:	48 89 ca             	mov    %rcx,%rdx
   11457:	48 83 ea 01          	sub    $0x1,%rdx
   1145b:	0f 82 13 ff ff ff    	jb     11374 <zbtIndexScanSlot+0x3f4>
   11461:	21 d0                	and    %edx,%eax
   11463:	31 f6                	xor    %esi,%esi
   11465:	48 8b 7d a8          	mov    -0x58(%rbp),%rdi
   11469:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   1146d:	48 8b 3f             	mov    (%rdi),%rdi
   11470:	40 0f 95 c6          	setne  %sil
   11474:	c1 e6 04             	shl    $0x4,%esi
   11477:	48 83 ce 20          	or     $0x20,%rsi
   1147b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   11480:	49 89 c0             	mov    %rax,%r8
   11483:	4c 0f af c6          	imul   %rsi,%r8
   11487:	49 01 f8             	add    %rdi,%r8
   1148a:	4d 39 d8             	cmp    %r11,%r8
   1148d:	74 41                	je     114d0 <zbtIndexScanSlot+0x550>
   1148f:	4d 8b 00             	mov    (%r8),%r8
   11492:	4d 89 c1             	mov    %r8,%r9
   11495:	49 f7 d1             	not    %r9
   11498:	49 be ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r14
   1149f:	fe fe fe
   114a2:	4d 01 f0             	add    %r14,%r8
   114a5:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   114ac:	80 80 80
   114af:	4d 21 f1             	and    %r14,%r9
   114b2:	4d 85 c1             	test   %r8,%r9
   114b5:	0f 85 9e 01 00 00    	jne    11659 <zbtIndexScanSlot+0x6d9>
   114bb:	48 ff c0             	inc    %rax
   114be:	48 21 d0             	and    %rdx,%rax
   114c1:	48 ff c9             	dec    %rcx
   114c4:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   114c8:	75 b6                	jne    11480 <zbtIndexScanSlot+0x500>
   114ca:	e9 a5 fe ff ff       	jmp    11374 <zbtIndexScanSlot+0x3f4>
   114cf:	90                   	nop
   114d0:	41 0f b6 79 34       	movzbl 0x34(%r9),%edi
   114d5:	48 85 ff             	test   %rdi,%rdi
   114d8:	0f 84 f2 00 00 00    	je     115d0 <zbtIndexScanSlot+0x650>
   114de:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   114e3:	89 f8                	mov    %edi,%eax
   114e5:	0f af c1             	imul   %ecx,%eax
   114e8:	83 c0 07             	add    $0x7,%eax
   114eb:	c1 e8 03             	shr    $0x3,%eax
   114ee:	83 c0 09             	add    $0x9,%eax
   114f1:	83 e0 fe             	and    $0xfffffffe,%eax
   114f4:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   114f9:	89 d9                	mov    %ebx,%ecx
   114fb:	45 84 c0             	test   %r8b,%r8b
   114fe:	74 08                	je     11508 <zbtIndexScanSlot+0x588>
   11500:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   11505:	44 01 e9             	add    %r13d,%ecx
   11508:	48 03 45 a0          	add    -0x60(%rbp),%rax
   1150c:	89 c9                	mov    %ecx,%ecx
   1150e:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   11512:	4d 8d 34 01          	lea    (%r9,%rax,1),%r14
   11516:	41 0f b6 14 01       	movzbl (%r9,%rax,1),%edx
   1151b:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11522:	77 1c                	ja     11540 <zbtIndexScanSlot+0x5c0>
   11524:	49 ff c6             	inc    %r14
   11527:	4c 89 f6             	mov    %r14,%rsi
   1152a:	40 84 ff             	test   %dil,%dil
   1152d:	75 32                	jne    11561 <zbtIndexScanSlot+0x5e1>
   1152f:	e9 1d 01 00 00       	jmp    11651 <zbtIndexScanSlot+0x6d1>
   11534:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   1153b:	00 00 00 00 00
   11540:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11546:	0f 85 9b 00 00 00    	jne    115e7 <zbtIndexScanSlot+0x667>
   1154c:	41 0f b7 56 01       	movzwl 0x1(%r14),%edx
   11551:	49 83 c6 03          	add    $0x3,%r14
   11555:	4c 89 f6             	mov    %r14,%rsi
   11558:	40 84 ff             	test   %dil,%dil
   1155b:	0f 84 f0 00 00 00    	je     11651 <zbtIndexScanSlot+0x6d1>
   11561:	45 84 c0             	test   %r8b,%r8b
   11564:	74 08                	je     1156e <zbtIndexScanSlot+0x5ee>
   11566:	41 0f b6 59 11       	movzbl 0x11(%r9),%ebx
   1156b:	44 01 eb             	add    %r13d,%ebx
   1156e:	44 0f b6 d7          	movzbl %dil,%r10d
   11572:	41 89 db             	mov    %ebx,%r11d
   11575:	44 89 d0             	mov    %r10d,%eax
   11578:	4c 0f af d8          	imul   %rax,%r11
   1157c:	4c 89 db             	mov    %r11,%rbx
   1157f:	48 c1 eb 03          	shr    $0x3,%rbx
   11583:	48 8b 4d a0          	mov    -0x60(%rbp),%rcx
   11587:	4c 8b 0c 19          	mov    (%rcx,%rbx,1),%r9
   1158b:	44 89 d9             	mov    %r11d,%ecx
   1158e:	80 e1 07             	and    $0x7,%cl
   11591:	49 d3 e9             	shr    %cl,%r9
   11594:	41 83 e3 07          	and    $0x7,%r11d
   11598:	0f 84 62 fd ff ff    	je     11300 <zbtIndexScanSlot+0x380>
   1159e:	b9 40 00 00 00       	mov    $0x40,%ecx
   115a3:	44 29 d9             	sub    %r11d,%ecx
   115a6:	44 39 d1             	cmp    %r10d,%ecx
   115a9:	0f 83 51 fd ff ff    	jae    11300 <zbtIndexScanSlot+0x380>
   115af:	4c 8b 55 c8          	mov    -0x38(%rbp),%r10
   115b3:	46 0f b6 54 13 40    	movzbl 0x40(%rbx,%r10,1),%r10d
   115b9:	49 d3 e2             	shl    %cl,%r10
   115bc:	4d 09 d1             	or     %r10,%r9
   115bf:	e9 3c fd ff ff       	jmp    11300 <zbtIndexScanSlot+0x380>
   115c4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   115cb:	00 00 00 00 00
   115d0:	31 c0                	xor    %eax,%eax
   115d2:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   115d7:	89 d9                	mov    %ebx,%ecx
   115d9:	45 84 c0             	test   %r8b,%r8b
   115dc:	0f 85 1e ff ff ff    	jne    11500 <zbtIndexScanSlot+0x580>
   115e2:	e9 21 ff ff ff       	jmp    11508 <zbtIndexScanSlot+0x588>
   115e7:	49 8b 76 0d          	mov    0xd(%r14),%rsi
   115eb:	48 85 f6             	test   %rsi,%rsi
   115ee:	75 4a                	jne    1163a <zbtIndexScanSlot+0x6ba>
   115f0:	48 8d 3d e8 20 00 00 	lea    0x20e8(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   115f7:	48 89 75 90          	mov    %rsi,-0x70(%rbp)
   115fb:	be 57 02 00 00       	mov    $0x257,%esi
   11600:	48 8d 15 20 22 00 00 	lea    0x2220(%rip),%rdx        # 13827 <_IO_stdin_used+0x827>
   11607:	e8 74 02 00 00       	call   11880 <standalone_panic>
   1160c:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11610:	48 8b 75 90          	mov    -0x70(%rbp),%rsi
   11614:	41 80 3e ff          	cmpb   $0xff,(%r14)
   11618:	74 20                	je     1163a <zbtIndexScanSlot+0x6ba>
   1161a:	48 8d 3d be 20 00 00 	lea    0x20be(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11621:	be 37 02 00 00       	mov    $0x237,%esi
   11626:	48 8d 15 06 22 00 00 	lea    0x2206(%rip),%rdx        # 13833 <_IO_stdin_used+0x833>
   1162d:	e8 4e 02 00 00       	call   11880 <standalone_panic>
   11632:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11636:	48 8b 75 90          	mov    -0x70(%rbp),%rsi
   1163a:	49 8b 56 05          	mov    0x5(%r14),%rdx
   1163e:	41 0f b6 79 34       	movzbl 0x34(%r9),%edi
   11643:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   11648:	40 84 ff             	test   %dil,%dil
   1164b:	0f 85 10 ff ff ff    	jne    11561 <zbtIndexScanSlot+0x5e1>
   11651:	45 31 d2             	xor    %r10d,%r10d
   11654:	e9 d4 fc ff ff       	jmp    1132d <zbtIndexScanSlot+0x3ad>
   11659:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   1165d:	e9 12 fd ff ff       	jmp    11374 <zbtIndexScanSlot+0x3f4>
   11662:	48 8d 3d 76 20 00 00 	lea    0x2076(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11669:	48 8d 15 02 26 00 00 	lea    0x2602(%rip),%rdx        # 13c72 <_IO_stdin_used+0xc72>
   11670:	be 66 10 00 00       	mov    $0x1066,%esi
   11675:	e8 06 02 00 00       	call   11880 <standalone_panic>
   1167a:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   1167e:	31 c0                	xor    %eax,%eax
   11680:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   11684:	4c 0b 55 b8          	or     -0x48(%rbp),%r10
   11688:	75 18                	jne    116a2 <zbtIndexScanSlot+0x722>
   1168a:	48 8d 3d 4e 20 00 00 	lea    0x204e(%rip),%rdi        # 136df <_IO_stdin_used+0x6df>
   11691:	48 8d 15 e5 25 00 00 	lea    0x25e5(%rip),%rdx        # 13c7d <_IO_stdin_used+0xc7d>
   11698:	be 7d 10 00 00       	mov    $0x107d,%esi
   1169d:	e8 de 01 00 00       	call   11880 <standalone_panic>
   116a2:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   116a6:	e9 ac fa ff ff       	jmp    11157 <zbtIndexScanSlot+0x1d7>
   116ab:	84 d2                	test   %dl,%dl
   116ad:	0f 84 a5 01 00 00    	je     11858 <zbtIndexScanSlot+0x8d8>
   116b3:	89 c2                	mov    %eax,%edx
   116b5:	f7 d2                	not    %edx
   116b7:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   116bd:	01 c2                	add    %eax,%edx
   116bf:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   116c3:	eb 19                	jmp    116de <zbtIndexScanSlot+0x75e>
   116c5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   116cc:	00 00 00 00
   116d0:	48 ff c6             	inc    %rsi
   116d3:	ff ca                	dec    %edx
   116d5:	48 39 c6             	cmp    %rax,%rsi
   116d8:	0f 83 de fb ff ff    	jae    112bc <zbtIndexScanSlot+0x33c>
   116de:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   116e2:	75 ec                	jne    116d0 <zbtIndexScanSlot+0x750>
   116e4:	44 89 ff             	mov    %r15d,%edi
   116e7:	41 ff c7             	inc    %r15d
   116ea:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   116f1:	eb dd                	jmp    116d0 <zbtIndexScanSlot+0x750>
   116f3:	31 ff                	xor    %edi,%edi
   116f5:	45 89 e0             	mov    %r12d,%r8d
   116f8:	41 80 f0 01          	xor    $0x1,%r8b
   116fc:	45 31 ff             	xor    %r15d,%r15d
   116ff:	eb 25                	jmp    11726 <zbtIndexScanSlot+0x7a6>
   11701:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11708:	0f 1f 84 00 00 00 00
   1170f:	00
   11710:	48 ff c7             	inc    %rdi
   11713:	48 39 f7             	cmp    %rsi,%rdi
   11716:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   1171d:	fe fe fe
   11720:	0f 84 62 fa ff ff    	je     11188 <zbtIndexScanSlot+0x208>
   11726:	4c 8b 14 f9          	mov    (%rcx,%rdi,8),%r10
   1172a:	4d 89 d3             	mov    %r10,%r11
   1172d:	49 31 db             	xor    %rbx,%r11
   11730:	4d 89 d9             	mov    %r11,%r9
   11733:	49 f7 d1             	not    %r9
   11736:	4d 01 eb             	add    %r13,%r11
   11739:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   11740:	80 80 80
   11743:	4d 21 f1             	and    %r14,%r9
   11746:	4d 21 d9             	and    %r11,%r9
   11749:	41 80 fc 01          	cmp    $0x1,%r12b
   1174d:	75 10                	jne    1175f <zbtIndexScanSlot+0x7df>
   1174f:	4f 8d 1c 2a          	lea    (%r10,%r13,1),%r11
   11753:	49 f7 d2             	not    %r10
   11756:	4d 21 f2             	and    %r14,%r10
   11759:	4d 21 da             	and    %r11,%r10
   1175c:	4d 09 d1             	or     %r10,%r9
   1175f:	4d 85 c9             	test   %r9,%r9
   11762:	74 ac                	je     11710 <zbtIndexScanSlot+0x790>
   11764:	4c 8d 14 fd 00 00 00 	lea    0x0(,%rdi,8),%r10
   1176b:	00
   1176c:	eb 19                	jmp    11787 <zbtIndexScanSlot+0x807>
   1176e:	66 90                	xchg   %ax,%ax
   11770:	45 89 fe             	mov    %r15d,%r14d
   11773:	41 ff c7             	inc    %r15d
   11776:	46 89 9c b5 00 fe ff 	mov    %r11d,-0x200(%rbp,%r14,4)
   1177d:	ff
   1177e:	4d 8d 59 ff          	lea    -0x1(%r9),%r11
   11782:	4d 21 d9             	and    %r11,%r9
   11785:	74 89                	je     11710 <zbtIndexScanSlot+0x790>
   11787:	f3 4d 0f bc d9       	tzcnt  %r9,%r11
   1178c:	41 c1 eb 03          	shr    $0x3,%r11d
   11790:	45 09 d3             	or     %r10d,%r11d
   11793:	46 0f b6 2c 19       	movzbl (%rcx,%r11,1),%r13d
   11798:	45 89 c6             	mov    %r8d,%r14d
   1179b:	45 08 ee             	or     %r13b,%r14b
   1179e:	41 0f 94 c6          	sete   %r14b
   117a2:	45 38 e5             	cmp    %r12b,%r13b
   117a5:	74 c9                	je     11770 <zbtIndexScanSlot+0x7f0>
   117a7:	45 84 f6             	test   %r14b,%r14b
   117aa:	74 d2                	je     1177e <zbtIndexScanSlot+0x7fe>
   117ac:	eb c2                	jmp    11770 <zbtIndexScanSlot+0x7f0>
   117ae:	45 31 c0             	xor    %r8d,%r8d
   117b1:	45 31 ff             	xor    %r15d,%r15d
   117b4:	eb 16                	jmp    117cc <zbtIndexScanSlot+0x84c>
   117b6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   117bd:	00 00 00
   117c0:	49 ff c0             	inc    %r8
   117c3:	49 39 f0             	cmp    %rsi,%r8
   117c6:	0f 84 bc f9 ff ff    	je     11188 <zbtIndexScanSlot+0x208>
   117cc:	4e 8b 14 c1          	mov    (%rcx,%r8,8),%r10
   117d0:	49 31 da             	xor    %rbx,%r10
   117d3:	4d 89 d1             	mov    %r10,%r9
   117d6:	49 f7 d1             	not    %r9
   117d9:	4d 01 ea             	add    %r13,%r10
   117dc:	49 bb 80 80 80 80 80 	movabs $0x8080808080808080,%r11
   117e3:	80 80 80
   117e6:	4d 21 d9             	and    %r11,%r9
   117e9:	4d 21 d1             	and    %r10,%r9
   117ec:	74 d2                	je     117c0 <zbtIndexScanSlot+0x840>
   117ee:	4e 8d 14 c5 00 00 00 	lea    0x0(,%r8,8),%r10
   117f5:	00
   117f6:	eb 11                	jmp    11809 <zbtIndexScanSlot+0x889>
   117f8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   117ff:	00
   11800:	4d 8d 59 ff          	lea    -0x1(%r9),%r11
   11804:	4d 21 d9             	and    %r11,%r9
   11807:	74 b7                	je     117c0 <zbtIndexScanSlot+0x840>
   11809:	f3 4d 0f bc d9       	tzcnt  %r9,%r11
   1180e:	41 c1 eb 03          	shr    $0x3,%r11d
   11812:	45 09 d3             	or     %r10d,%r11d
   11815:	46 38 24 19          	cmp    %r12b,(%rcx,%r11,1)
   11819:	75 e5                	jne    11800 <zbtIndexScanSlot+0x880>
   1181b:	41 89 fe             	mov    %edi,%r14d
   1181e:	45 29 de             	sub    %r11d,%r14d
   11821:	45 89 fb             	mov    %r15d,%r11d
   11824:	41 ff c7             	inc    %r15d
   11827:	46 89 b4 9d 00 fe ff 	mov    %r14d,-0x200(%rbp,%r11,4)
   1182e:	ff
   1182f:	eb cf                	jmp    11800 <zbtIndexScanSlot+0x880>
   11831:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11835:	eb 0c                	jmp    11843 <zbtIndexScanSlot+0x8c3>
   11837:	48 ff c6             	inc    %rsi
   1183a:	48 39 c6             	cmp    %rax,%rsi
   1183d:	0f 83 79 fa ff ff    	jae    112bc <zbtIndexScanSlot+0x33c>
   11843:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   11847:	77 ee                	ja     11837 <zbtIndexScanSlot+0x8b7>
   11849:	44 89 fa             	mov    %r15d,%edx
   1184c:	41 ff c7             	inc    %r15d
   1184f:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   11856:	eb df                	jmp    11837 <zbtIndexScanSlot+0x8b7>
   11858:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   1185c:	eb 0c                	jmp    1186a <zbtIndexScanSlot+0x8ea>
   1185e:	48 ff c6             	inc    %rsi
   11861:	48 39 c6             	cmp    %rax,%rsi
   11864:	0f 83 52 fa ff ff    	jae    112bc <zbtIndexScanSlot+0x33c>
   1186a:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   1186e:	75 ee                	jne    1185e <zbtIndexScanSlot+0x8de>
   11870:	44 89 fa             	mov    %r15d,%edx
   11873:	41 ff c7             	inc    %r15d
   11876:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   1187d:	eb df                	jmp    1185e <zbtIndexScanSlot+0x8de>

Disassembly of section .fini:
