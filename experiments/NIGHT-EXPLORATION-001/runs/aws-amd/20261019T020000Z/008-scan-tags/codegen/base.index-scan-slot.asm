
scratch/amd-scan-build/base/build/native/btree-bench:     file format elf64-x86-64


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
   10db4:	4c 89 45 98          	mov    %r8,-0x68(%rbp)
   10db8:	89 c8                	mov    %ecx,%eax
   10dba:	4c 8b 22             	mov    (%rdx),%r12
   10dbd:	8d 0c c5 00 00 00 00 	lea    0x0(,%rax,8),%ecx
   10dc4:	49 d3 ec             	shr    %cl,%r12
   10dc7:	49 89 ff             	mov    %rdi,%r15
   10dca:	44 8b 5e 20          	mov    0x20(%rsi),%r11d
   10dce:	89 c0                	mov    %eax,%eax
   10dd0:	45 85 db             	test   %r11d,%r11d
   10dd3:	74 18                	je     10ded <zbtIndexScanSlot+0x4d>
   10dd5:	44 8b 74 82 10       	mov    0x10(%rdx,%rax,4),%r14d
   10dda:	31 c0                	xor    %eax,%eax
   10ddc:	4c 89 e3             	mov    %r12,%rbx
   10ddf:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10de6:	75 2c                	jne    10e14 <zbtIndexScanSlot+0x74>
   10de8:	e9 8a 01 00 00       	jmp    10f77 <zbtIndexScanSlot+0x1d7>
   10ded:	0f b7 4c 42 10       	movzwl 0x10(%rdx,%rax,2),%ecx
   10df2:	81 f9 ff ff 00 00    	cmp    $0xffff,%ecx
   10df8:	41 be ff ff ff ff    	mov    $0xffffffff,%r14d
   10dfe:	44 0f 45 f1          	cmovne %ecx,%r14d
   10e02:	31 c0                	xor    %eax,%eax
   10e04:	4c 89 e3             	mov    %r12,%rbx
   10e07:	48 81 e3 ff 00 00 00 	and    $0xff,%rbx
   10e0e:	0f 84 63 01 00 00    	je     10f77 <zbtIndexScanSlot+0x1d7>
   10e14:	41 83 fe ff          	cmp    $0xffffffff,%r14d
   10e18:	0f 84 59 01 00 00    	je     10f77 <zbtIndexScanSlot+0x1d7>
   10e1e:	4d 85 c9             	test   %r9,%r9
   10e21:	0f 84 8d 00 00 00    	je     10eb4 <zbtIndexScanSlot+0x114>
   10e27:	49 b8 15 7c 4a 7f b9 	movabs $0x9e3779b97f4a7c15,%r8
   10e2e:	79 37 9e
   10e31:	4c 0f af c3          	imul   %rbx,%r8
   10e35:	4c 89 c1             	mov    %r8,%rcx
   10e38:	48 c1 e9 3a          	shr    $0x3a,%rcx
   10e3c:	41 ba 01 00 00 00    	mov    $0x1,%r10d
   10e42:	49 d3 e2             	shl    %cl,%r10
   10e45:	48 8b 4d 98          	mov    -0x68(%rbp),%rcx
   10e49:	48 89 cf             	mov    %rcx,%rdi
   10e4c:	4c 39 c9             	cmp    %r9,%rcx
   10e4f:	73 5a                	jae    10eab <zbtIndexScanSlot+0x10b>
   10e51:	4d 0f ab e2          	bts    %r12,%r10
   10e55:	49 c1 e8 24          	shr    $0x24,%r8
   10e59:	4d 0f ab c2          	bts    %r8,%r10
   10e5d:	31 c9                	xor    %ecx,%ecx
   10e5f:	45 85 db             	test   %r11d,%r11d
   10e62:	0f 95 c1             	setne  %cl
   10e65:	4c 8b 1e             	mov    (%rsi),%r11
   10e68:	c1 e1 04             	shl    $0x4,%ecx
   10e6b:	48 83 c9 20          	or     $0x20,%rcx
   10e6f:	48 89 cf             	mov    %rcx,%rdi
   10e72:	4c 8b 45 98          	mov    -0x68(%rbp),%r8
   10e76:	49 0f af f8          	imul   %r8,%rdi
   10e7a:	49 01 fb             	add    %rdi,%r11
   10e7d:	49 83 c3 08          	add    $0x8,%r11
   10e81:	4c 89 c7             	mov    %r8,%rdi
   10e84:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   10e8b:	00 00 00 00 00
   10e90:	4d 8b 03             	mov    (%r11),%r8
   10e93:	49 f7 d0             	not    %r8
   10e96:	4d 85 c2             	test   %r8,%r10
   10e99:	74 10                	je     10eab <zbtIndexScanSlot+0x10b>
   10e9b:	48 ff c7             	inc    %rdi
   10e9e:	49 01 cb             	add    %rcx,%r11
   10ea1:	49 39 f9             	cmp    %rdi,%r9
   10ea4:	75 ea                	jne    10e90 <zbtIndexScanSlot+0xf0>
   10ea6:	e9 ca 00 00 00       	jmp    10f75 <zbtIndexScanSlot+0x1d5>
   10eab:	4c 39 cf             	cmp    %r9,%rdi
   10eae:	0f 84 c1 00 00 00    	je     10f75 <zbtIndexScanSlot+0x1d5>
   10eb4:	45 3b 77 54          	cmp    0x54(%r15),%r14d
   10eb8:	0f 83 8f 00 00 00    	jae    10f4d <zbtIndexScanSlot+0x1ad>
   10ebe:	49 8b 4f 48          	mov    0x48(%r15),%rcx
   10ec2:	44 89 f7             	mov    %r14d,%edi
   10ec5:	48 8b 3c f9          	mov    (%rcx,%rdi,8),%rdi
   10ec9:	48 85 ff             	test   %rdi,%rdi
   10ecc:	74 7f                	je     10f4d <zbtIndexScanSlot+0x1ad>
   10ece:	89 f9                	mov    %edi,%ecx
   10ed0:	83 e1 01             	and    $0x1,%ecx
   10ed3:	75 78                	jne    10f4d <zbtIndexScanSlot+0x1ad>
   10ed5:	48 89 f9             	mov    %rdi,%rcx
   10ed8:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
   10edc:	44 39 77 30          	cmp    %r14d,0x30(%rdi)
   10ee0:	4c 89 4d c0          	mov    %r9,-0x40(%rbp)
   10ee4:	48 89 75 a8          	mov    %rsi,-0x58(%rbp)
   10ee8:	48 89 55 b0          	mov    %rdx,-0x50(%rbp)
   10eec:	74 1c                	je     10f0a <zbtIndexScanSlot+0x16a>
   10eee:	48 8d 3d 29 27 00 00 	lea    0x2729(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10ef5:	48 8d 15 7b 28 00 00 	lea    0x287b(%rip),%rdx        # 13777 <_IO_stdin_used+0x777>
   10efc:	be 58 10 00 00       	mov    $0x1058,%esi
   10f01:	e8 9a 07 00 00       	call   116a0 <standalone_panic>
   10f06:	48 8b 75 a8          	mov    -0x58(%rbp),%rsi
   10f0a:	49 8b 47 40          	mov    0x40(%r15),%rax
   10f0e:	48 85 c0             	test   %rax,%rax
   10f11:	48 8b 55 c8          	mov    -0x38(%rbp),%rdx
   10f15:	74 15                	je     10f2c <zbtIndexScanSlot+0x18c>
   10f17:	0f b7 4a 16          	movzwl 0x16(%rdx),%ecx
   10f1b:	66 3b 48 2c          	cmp    0x2c(%rax),%cx
   10f1f:	0f 94 c1             	sete   %cl
   10f22:	48 39 f0             	cmp    %rsi,%rax
   10f25:	0f 95 c0             	setne  %al
   10f28:	38 c8                	cmp    %cl,%al
   10f2a:	74 49                	je     10f75 <zbtIndexScanSlot+0x1d5>
   10f2c:	0f b6 4a 34          	movzbl 0x34(%rdx),%ecx
   10f30:	45 31 ff             	xor    %r15d,%r15d
   10f33:	0f b6 42 11          	movzbl 0x11(%rdx),%eax
   10f37:	48 85 c9             	test   %rcx,%rcx
   10f3a:	74 4d                	je     10f89 <zbtIndexScanSlot+0x1e9>
   10f3c:	0f af c8             	imul   %eax,%ecx
   10f3f:	83 c1 07             	add    $0x7,%ecx
   10f42:	c1 e9 03             	shr    $0x3,%ecx
   10f45:	83 c1 09             	add    $0x9,%ecx
   10f48:	83 e1 fe             	and    $0xfffffffe,%ecx
   10f4b:	eb 3e                	jmp    10f8b <zbtIndexScanSlot+0x1eb>
   10f4d:	49 83 7f 40 00       	cmpq   $0x0,0x40(%r15)
   10f52:	74 09                	je     10f5d <zbtIndexScanSlot+0x1bd>
   10f54:	49 83 c7 18          	add    $0x18,%r15
   10f58:	49 39 f7             	cmp    %rsi,%r15
   10f5b:	74 18                	je     10f75 <zbtIndexScanSlot+0x1d5>
   10f5d:	48 8d 3d ba 26 00 00 	lea    0x26ba(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   10f64:	48 8d 15 2b 28 00 00 	lea    0x282b(%rip),%rdx        # 13796 <_IO_stdin_used+0x796>
   10f6b:	be 55 10 00 00       	mov    $0x1055,%esi
   10f70:	e8 2b 07 00 00       	call   116a0 <standalone_panic>
   10f75:	31 c0                	xor    %eax,%eax
   10f77:	48 81 c4 d8 01 00 00 	add    $0x1d8,%rsp
   10f7e:	5b                   	pop    %rbx
   10f7f:	41 5c                	pop    %r12
   10f81:	41 5d                	pop    %r13
   10f83:	41 5e                	pop    %r14
   10f85:	41 5f                	pop    %r15
   10f87:	5d                   	pop    %rbp
   10f88:	c3                   	ret
   10f89:	31 c9                	xor    %ecx,%ecx
   10f8b:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   10f92:	fe fe fe
   10f95:	48 01 d1             	add    %rdx,%rcx
   10f98:	48 83 c1 38          	add    $0x38,%rcx
   10f9c:	48 8d 0c 41          	lea    (%rcx,%rax,2),%rcx
   10fa0:	0f b6 52 35          	movzbl 0x35(%rdx),%edx
   10fa4:	3c 08                	cmp    $0x8,%al
   10fa6:	73 6b                	jae    11013 <zbtIndexScanSlot+0x273>
   10fa8:	a8 07                	test   $0x7,%al
   10faa:	0f 84 20 01 00 00    	je     110d0 <zbtIndexScanSlot+0x330>
   10fb0:	89 c6                	mov    %eax,%esi
   10fb2:	83 e6 f8             	and    $0xfffffff8,%esi
   10fb5:	41 80 fc 01          	cmp    $0x1,%r12b
   10fb9:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   10fbd:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   10fc1:	0f 85 04 05 00 00    	jne    114cb <zbtIndexScanSlot+0x72b>
   10fc7:	84 d2                	test   %dl,%dl
   10fc9:	0f 84 82 06 00 00    	je     11651 <zbtIndexScanSlot+0x8b1>
   10fcf:	89 c2                	mov    %eax,%edx
   10fd1:	f7 d2                	not    %edx
   10fd3:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   10fd9:	01 c2                	add    %eax,%edx
   10fdb:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   10fdf:	eb 1d                	jmp    10ffe <zbtIndexScanSlot+0x25e>
   10fe1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   10fe8:	0f 1f 84 00 00 00 00
   10fef:	00
   10ff0:	48 ff c6             	inc    %rsi
   10ff3:	ff ca                	dec    %edx
   10ff5:	48 39 c6             	cmp    %rax,%rsi
   10ff8:	0f 83 de 00 00 00    	jae    110dc <zbtIndexScanSlot+0x33c>
   10ffe:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   11002:	77 ec                	ja     10ff0 <zbtIndexScanSlot+0x250>
   11004:	44 89 ff             	mov    %r15d,%edi
   11007:	41 ff c7             	inc    %r15d
   1100a:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   11011:	eb dd                	jmp    10ff0 <zbtIndexScanSlot+0x250>
   11013:	89 c6                	mov    %eax,%esi
   11015:	c1 ee 03             	shr    $0x3,%esi
   11018:	49 b8 01 01 01 01 01 	movabs $0x101010101010101,%r8
   1101f:	01 01 01
   11022:	49 0f af d8          	imul   %r8,%rbx
   11026:	84 d2                	test   %dl,%dl
   11028:	0f 84 e5 04 00 00    	je     11513 <zbtIndexScanSlot+0x773>
   1102e:	8d 78 ff             	lea    -0x1(%rax),%edi
   11031:	41 80 fc 01          	cmp    $0x1,%r12b
   11035:	0f 85 93 05 00 00    	jne    115ce <zbtIndexScanSlot+0x82e>
   1103b:	45 31 c9             	xor    %r9d,%r9d
   1103e:	45 31 ff             	xor    %r15d,%r15d
   11041:	eb 19                	jmp    1105c <zbtIndexScanSlot+0x2bc>
   11043:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   1104a:	84 00 00 00 00 00
   11050:	49 ff c1             	inc    %r9
   11053:	49 39 f1             	cmp    %rsi,%r9
   11056:	0f 84 4c ff ff ff    	je     10fa8 <zbtIndexScanSlot+0x208>
   1105c:	4e 8b 14 c9          	mov    (%rcx,%r9,8),%r10
   11060:	4d 89 d3             	mov    %r10,%r11
   11063:	49 f7 d3             	not    %r11
   11066:	4c 89 d3             	mov    %r10,%rbx
   11069:	4c 31 c3             	xor    %r8,%rbx
   1106c:	4c 01 eb             	add    %r13,%rbx
   1106f:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   11076:	80 80 80
   11079:	4d 21 f3             	and    %r14,%r11
   1107c:	4d 01 ea             	add    %r13,%r10
   1107f:	49 09 da             	or     %rbx,%r10
   11082:	4d 21 da             	and    %r11,%r10
   11085:	74 c9                	je     11050 <zbtIndexScanSlot+0x2b0>
   11087:	4e 8d 1c cd 00 00 00 	lea    0x0(,%r9,8),%r11
   1108e:	00
   1108f:	eb 18                	jmp    110a9 <zbtIndexScanSlot+0x309>
   11091:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11098:	0f 1f 84 00 00 00 00
   1109f:	00
   110a0:	49 8d 5a ff          	lea    -0x1(%r10),%rbx
   110a4:	49 21 da             	and    %rbx,%r10
   110a7:	74 a7                	je     11050 <zbtIndexScanSlot+0x2b0>
   110a9:	f3 49 0f bc da       	tzcnt  %r10,%rbx
   110ae:	c1 eb 03             	shr    $0x3,%ebx
   110b1:	44 09 db             	or     %r11d,%ebx
   110b4:	80 3c 19 01          	cmpb   $0x1,(%rcx,%rbx,1)
   110b8:	77 e6                	ja     110a0 <zbtIndexScanSlot+0x300>
   110ba:	41 89 fe             	mov    %edi,%r14d
   110bd:	41 29 de             	sub    %ebx,%r14d
   110c0:	44 89 fb             	mov    %r15d,%ebx
   110c3:	41 ff c7             	inc    %r15d
   110c6:	44 89 b4 9d 00 fe ff 	mov    %r14d,-0x200(%rbp,%rbx,4)
   110cd:	ff
   110ce:	eb d0                	jmp    110a0 <zbtIndexScanSlot+0x300>
   110d0:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   110d4:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   110d8:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   110dc:	45 85 ff             	test   %r15d,%r15d
   110df:	0f 84 9d 03 00 00    	je     11482 <zbtIndexScanSlot+0x6e2>
   110e5:	49 8d 41 38          	lea    0x38(%r9),%rax
   110e9:	48 89 45 a0          	mov    %rax,-0x60(%rbp)
   110ed:	4d 85 d2             	test   %r10,%r10
   110f0:	0f 95 c0             	setne  %al
   110f3:	41 83 ff 01          	cmp    $0x1,%r15d
   110f7:	0f 95 c1             	setne  %cl
   110fa:	08 c1                	or     %al,%cl
   110fc:	88 4d d7             	mov    %cl,-0x29(%rbp)
   110ff:	44 89 f8             	mov    %r15d,%eax
   11102:	48 89 45 88          	mov    %rax,-0x78(%rbp)
   11106:	45 31 e4             	xor    %r12d,%r12d
   11109:	31 c0                	xor    %eax,%eax
   1110b:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   1110f:	e9 8d 00 00 00       	jmp    111a1 <zbtIndexScanSlot+0x401>
   11114:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   1111b:	00 00 00 00 00
   11120:	49 c7 c2 ff ff ff ff 	mov    $0xffffffffffffffff,%r10
   11127:	89 c1                	mov    %eax,%ecx
   11129:	49 d3 e2             	shl    %cl,%r10
   1112c:	40 80 ff 40          	cmp    $0x40,%dil
   11130:	49 f7 d2             	not    %r10
   11133:	48 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%rax
   1113a:	4c 0f 43 d0          	cmovae %rax,%r10
   1113e:	4d 21 ca             	and    %r9,%r10
   11141:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11145:	41 0f b6 49 13       	movzbl 0x13(%r9),%ecx
   1114a:	49 d3 e2             	shl    %cl,%r10
   1114d:	4c 89 d0             	mov    %r10,%rax
   11150:	48 f7 d8             	neg    %rax
   11153:	45 84 c0             	test   %r8b,%r8b
   11156:	49 0f 44 c2          	cmove  %r10,%rax
   1115a:	49 03 41 28          	add    0x28(%r9),%rax
   1115e:	48 89 c1             	mov    %rax,%rcx
   11161:	48 bf ff ff ff ff ff 	movabs $0x7fffffffffffffff,%rdi
   11168:	ff ff 7f
   1116b:	48 21 f9             	and    %rdi,%rcx
   1116e:	48 85 c0             	test   %rax,%rax
   11171:	48 f7 d0             	not    %rax
   11174:	48 0f 48 c1          	cmovs  %rcx,%rax
   11178:	66 48 0f 6e c0       	movq   %rax,%xmm0
   1117d:	48 8b 7d 18          	mov    0x18(%rbp),%rdi
   11181:	ff 55 10             	call   *0x10(%rbp)
   11184:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11188:	48 ff 45 b8          	incq   -0x48(%rbp)
   1118c:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   11190:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   11194:	49 ff c4             	inc    %r12
   11197:	4c 3b 65 88          	cmp    -0x78(%rbp),%r12
   1119b:	0f 84 03 03 00 00    	je     114a4 <zbtIndexScanSlot+0x704>
   111a1:	42 8b 9c a5 00 fe ff 	mov    -0x200(%rbp,%r12,4),%ebx
   111a8:	ff
   111a9:	41 89 dd             	mov    %ebx,%r13d
   111ac:	41 f7 d5             	not    %r13d
   111af:	80 7d d7 00          	cmpb   $0x0,-0x29(%rbp)
   111b3:	0f 84 37 01 00 00    	je     112f0 <zbtIndexScanSlot+0x550>
   111b9:	41 0f b6 41 34       	movzbl 0x34(%r9),%eax
   111be:	48 85 c0             	test   %rax,%rax
   111c1:	74 4d                	je     11210 <zbtIndexScanSlot+0x470>
   111c3:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   111c8:	0f af c1             	imul   %ecx,%eax
   111cb:	83 c0 07             	add    $0x7,%eax
   111ce:	c1 e8 03             	shr    $0x3,%eax
   111d1:	83 c0 09             	add    $0x9,%eax
   111d4:	83 e0 fe             	and    $0xfffffffe,%eax
   111d7:	41 80 79 35 00       	cmpb   $0x0,0x35(%r9)
   111dc:	89 d9                	mov    %ebx,%ecx
   111de:	74 08                	je     111e8 <zbtIndexScanSlot+0x448>
   111e0:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   111e5:	44 01 e9             	add    %r13d,%ecx
   111e8:	48 03 45 a0          	add    -0x60(%rbp),%rax
   111ec:	89 c9                	mov    %ecx,%ecx
   111ee:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   111f2:	49 8d 3c 01          	lea    (%r9,%rax,1),%rdi
   111f6:	41 0f b6 34 01       	movzbl (%r9,%rax,1),%esi
   111fb:	81 fe fe 00 00 00    	cmp    $0xfe,%esi
   11201:	74 1a                	je     1121d <zbtIndexScanSlot+0x47d>
   11203:	81 fe ff 00 00 00    	cmp    $0xff,%esi
   11209:	75 1d                	jne    11228 <zbtIndexScanSlot+0x488>
   1120b:	8b 47 01             	mov    0x1(%rdi),%eax
   1120e:	eb 31                	jmp    11241 <zbtIndexScanSlot+0x4a1>
   11210:	31 c0                	xor    %eax,%eax
   11212:	41 80 79 35 00       	cmpb   $0x0,0x35(%r9)
   11217:	89 d9                	mov    %ebx,%ecx
   11219:	75 c5                	jne    111e0 <zbtIndexScanSlot+0x440>
   1121b:	eb cb                	jmp    111e8 <zbtIndexScanSlot+0x448>
   1121d:	0f b7 77 01          	movzwl 0x1(%rdi),%esi
   11221:	b8 03 00 00 00       	mov    $0x3,%eax
   11226:	eb 05                	jmp    1122d <zbtIndexScanSlot+0x48d>
   11228:	b8 01 00 00 00       	mov    $0x1,%eax
   1122d:	48 01 c7             	add    %rax,%rdi
   11230:	e8 ab 06 00 00       	call   118e0 <dictGenHashFunction>
   11235:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   11239:	4c 8b 5d b0          	mov    -0x50(%rbp),%r11
   1123d:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11241:	89 c0                	mov    %eax,%eax
   11243:	48 8b 4d a8          	mov    -0x58(%rbp),%rcx
   11247:	48 8b 49 08          	mov    0x8(%rcx),%rcx
   1124b:	4d 85 d2             	test   %r10,%r10
   1124e:	74 1a                	je     1126a <zbtIndexScanSlot+0x4ca>
   11250:	8d 71 ff             	lea    -0x1(%rcx),%esi
   11253:	89 c2                	mov    %eax,%edx
   11255:	21 f2                	and    %esi,%edx
   11257:	48 3b 55 98          	cmp    -0x68(%rbp),%rdx
   1125b:	0f 82 33 ff ff ff    	jb     11194 <zbtIndexScanSlot+0x3f4>
   11261:	4c 39 d2             	cmp    %r10,%rdx
   11264:	0f 83 2a ff ff ff    	jae    11194 <zbtIndexScanSlot+0x3f4>
   1126a:	41 83 ff 01          	cmp    $0x1,%r15d
   1126e:	0f 84 7c 00 00 00    	je     112f0 <zbtIndexScanSlot+0x550>
   11274:	48 89 ca             	mov    %rcx,%rdx
   11277:	48 83 ea 01          	sub    $0x1,%rdx
   1127b:	0f 82 13 ff ff ff    	jb     11194 <zbtIndexScanSlot+0x3f4>
   11281:	21 d0                	and    %edx,%eax
   11283:	31 f6                	xor    %esi,%esi
   11285:	48 8b 7d a8          	mov    -0x58(%rbp),%rdi
   11289:	83 7f 20 00          	cmpl   $0x0,0x20(%rdi)
   1128d:	48 8b 3f             	mov    (%rdi),%rdi
   11290:	40 0f 95 c6          	setne  %sil
   11294:	c1 e6 04             	shl    $0x4,%esi
   11297:	48 83 ce 20          	or     $0x20,%rsi
   1129b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
   112a0:	49 89 c0             	mov    %rax,%r8
   112a3:	4c 0f af c6          	imul   %rsi,%r8
   112a7:	49 01 f8             	add    %rdi,%r8
   112aa:	4d 39 d8             	cmp    %r11,%r8
   112ad:	74 41                	je     112f0 <zbtIndexScanSlot+0x550>
   112af:	4d 8b 00             	mov    (%r8),%r8
   112b2:	4d 89 c1             	mov    %r8,%r9
   112b5:	49 f7 d1             	not    %r9
   112b8:	49 be ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r14
   112bf:	fe fe fe
   112c2:	4d 01 f0             	add    %r14,%r8
   112c5:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   112cc:	80 80 80
   112cf:	4d 21 f1             	and    %r14,%r9
   112d2:	4d 85 c1             	test   %r8,%r9
   112d5:	0f 85 9e 01 00 00    	jne    11479 <zbtIndexScanSlot+0x6d9>
   112db:	48 ff c0             	inc    %rax
   112de:	48 21 d0             	and    %rdx,%rax
   112e1:	48 ff c9             	dec    %rcx
   112e4:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   112e8:	75 b6                	jne    112a0 <zbtIndexScanSlot+0x500>
   112ea:	e9 a5 fe ff ff       	jmp    11194 <zbtIndexScanSlot+0x3f4>
   112ef:	90                   	nop
   112f0:	41 0f b6 79 34       	movzbl 0x34(%r9),%edi
   112f5:	48 85 ff             	test   %rdi,%rdi
   112f8:	0f 84 f2 00 00 00    	je     113f0 <zbtIndexScanSlot+0x650>
   112fe:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   11303:	89 f8                	mov    %edi,%eax
   11305:	0f af c1             	imul   %ecx,%eax
   11308:	83 c0 07             	add    $0x7,%eax
   1130b:	c1 e8 03             	shr    $0x3,%eax
   1130e:	83 c0 09             	add    $0x9,%eax
   11311:	83 e0 fe             	and    $0xfffffffe,%eax
   11314:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   11319:	89 d9                	mov    %ebx,%ecx
   1131b:	45 84 c0             	test   %r8b,%r8b
   1131e:	74 08                	je     11328 <zbtIndexScanSlot+0x588>
   11320:	41 0f b6 49 11       	movzbl 0x11(%r9),%ecx
   11325:	44 01 e9             	add    %r13d,%ecx
   11328:	48 03 45 a0          	add    -0x60(%rbp),%rax
   1132c:	89 c9                	mov    %ecx,%ecx
   1132e:	0f b7 04 48          	movzwl (%rax,%rcx,2),%eax
   11332:	4d 8d 34 01          	lea    (%r9,%rax,1),%r14
   11336:	41 0f b6 14 01       	movzbl (%r9,%rax,1),%edx
   1133b:	48 81 fa fd 00 00 00 	cmp    $0xfd,%rdx
   11342:	77 1c                	ja     11360 <zbtIndexScanSlot+0x5c0>
   11344:	49 ff c6             	inc    %r14
   11347:	4c 89 f6             	mov    %r14,%rsi
   1134a:	40 84 ff             	test   %dil,%dil
   1134d:	75 32                	jne    11381 <zbtIndexScanSlot+0x5e1>
   1134f:	e9 1d 01 00 00       	jmp    11471 <zbtIndexScanSlot+0x6d1>
   11354:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   1135b:	00 00 00 00 00
   11360:	81 fa fe 00 00 00    	cmp    $0xfe,%edx
   11366:	0f 85 9b 00 00 00    	jne    11407 <zbtIndexScanSlot+0x667>
   1136c:	41 0f b7 56 01       	movzwl 0x1(%r14),%edx
   11371:	49 83 c6 03          	add    $0x3,%r14
   11375:	4c 89 f6             	mov    %r14,%rsi
   11378:	40 84 ff             	test   %dil,%dil
   1137b:	0f 84 f0 00 00 00    	je     11471 <zbtIndexScanSlot+0x6d1>
   11381:	45 84 c0             	test   %r8b,%r8b
   11384:	74 08                	je     1138e <zbtIndexScanSlot+0x5ee>
   11386:	41 0f b6 59 11       	movzbl 0x11(%r9),%ebx
   1138b:	44 01 eb             	add    %r13d,%ebx
   1138e:	44 0f b6 d7          	movzbl %dil,%r10d
   11392:	41 89 db             	mov    %ebx,%r11d
   11395:	44 89 d0             	mov    %r10d,%eax
   11398:	4c 0f af d8          	imul   %rax,%r11
   1139c:	4c 89 db             	mov    %r11,%rbx
   1139f:	48 c1 eb 03          	shr    $0x3,%rbx
   113a3:	48 8b 4d a0          	mov    -0x60(%rbp),%rcx
   113a7:	4c 8b 0c 19          	mov    (%rcx,%rbx,1),%r9
   113ab:	44 89 d9             	mov    %r11d,%ecx
   113ae:	80 e1 07             	and    $0x7,%cl
   113b1:	49 d3 e9             	shr    %cl,%r9
   113b4:	41 83 e3 07          	and    $0x7,%r11d
   113b8:	0f 84 62 fd ff ff    	je     11120 <zbtIndexScanSlot+0x380>
   113be:	b9 40 00 00 00       	mov    $0x40,%ecx
   113c3:	44 29 d9             	sub    %r11d,%ecx
   113c6:	44 39 d1             	cmp    %r10d,%ecx
   113c9:	0f 83 51 fd ff ff    	jae    11120 <zbtIndexScanSlot+0x380>
   113cf:	4c 8b 55 c8          	mov    -0x38(%rbp),%r10
   113d3:	46 0f b6 54 13 40    	movzbl 0x40(%rbx,%r10,1),%r10d
   113d9:	49 d3 e2             	shl    %cl,%r10
   113dc:	4d 09 d1             	or     %r10,%r9
   113df:	e9 3c fd ff ff       	jmp    11120 <zbtIndexScanSlot+0x380>
   113e4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nopw 0x0(%rax,%rax,1)
   113eb:	00 00 00 00 00
   113f0:	31 c0                	xor    %eax,%eax
   113f2:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   113f7:	89 d9                	mov    %ebx,%ecx
   113f9:	45 84 c0             	test   %r8b,%r8b
   113fc:	0f 85 1e ff ff ff    	jne    11320 <zbtIndexScanSlot+0x580>
   11402:	e9 21 ff ff ff       	jmp    11328 <zbtIndexScanSlot+0x588>
   11407:	49 8b 76 0d          	mov    0xd(%r14),%rsi
   1140b:	48 85 f6             	test   %rsi,%rsi
   1140e:	75 4a                	jne    1145a <zbtIndexScanSlot+0x6ba>
   11410:	48 8d 3d 07 22 00 00 	lea    0x2207(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11417:	48 89 75 90          	mov    %rsi,-0x70(%rbp)
   1141b:	be 57 02 00 00       	mov    $0x257,%esi
   11420:	48 8d 15 23 23 00 00 	lea    0x2323(%rip),%rdx        # 1374a <_IO_stdin_used+0x74a>
   11427:	e8 74 02 00 00       	call   116a0 <standalone_panic>
   1142c:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11430:	48 8b 75 90          	mov    -0x70(%rbp),%rsi
   11434:	41 80 3e ff          	cmpb   $0xff,(%r14)
   11438:	74 20                	je     1145a <zbtIndexScanSlot+0x6ba>
   1143a:	48 8d 3d dd 21 00 00 	lea    0x21dd(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11441:	be 37 02 00 00       	mov    $0x237,%esi
   11446:	48 8d 15 09 23 00 00 	lea    0x2309(%rip),%rdx        # 13756 <_IO_stdin_used+0x756>
   1144d:	e8 4e 02 00 00       	call   116a0 <standalone_panic>
   11452:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11456:	48 8b 75 90          	mov    -0x70(%rbp),%rsi
   1145a:	49 8b 56 05          	mov    0x5(%r14),%rdx
   1145e:	41 0f b6 79 34       	movzbl 0x34(%r9),%edi
   11463:	45 0f b6 41 35       	movzbl 0x35(%r9),%r8d
   11468:	40 84 ff             	test   %dil,%dil
   1146b:	0f 85 10 ff ff ff    	jne    11381 <zbtIndexScanSlot+0x5e1>
   11471:	45 31 d2             	xor    %r10d,%r10d
   11474:	e9 d4 fc ff ff       	jmp    1114d <zbtIndexScanSlot+0x3ad>
   11479:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   1147d:	e9 12 fd ff ff       	jmp    11194 <zbtIndexScanSlot+0x3f4>
   11482:	48 8d 3d 95 21 00 00 	lea    0x2195(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   11489:	48 8d 15 05 27 00 00 	lea    0x2705(%rip),%rdx        # 13b95 <_IO_stdin_used+0xb95>
   11490:	be 66 10 00 00       	mov    $0x1066,%esi
   11495:	e8 06 02 00 00       	call   116a0 <standalone_panic>
   1149a:	4c 8b 55 c0          	mov    -0x40(%rbp),%r10
   1149e:	31 c0                	xor    %eax,%eax
   114a0:	48 89 45 b8          	mov    %rax,-0x48(%rbp)
   114a4:	4c 0b 55 b8          	or     -0x48(%rbp),%r10
   114a8:	75 18                	jne    114c2 <zbtIndexScanSlot+0x722>
   114aa:	48 8d 3d 6d 21 00 00 	lea    0x216d(%rip),%rdi        # 1361e <_IO_stdin_used+0x61e>
   114b1:	48 8d 15 e8 26 00 00 	lea    0x26e8(%rip),%rdx        # 13ba0 <_IO_stdin_used+0xba0>
   114b8:	be 7d 10 00 00       	mov    $0x107d,%esi
   114bd:	e8 de 01 00 00       	call   116a0 <standalone_panic>
   114c2:	48 8b 45 b8          	mov    -0x48(%rbp),%rax
   114c6:	e9 ac fa ff ff       	jmp    10f77 <zbtIndexScanSlot+0x1d7>
   114cb:	84 d2                	test   %dl,%dl
   114cd:	0f 84 a5 01 00 00    	je     11678 <zbtIndexScanSlot+0x8d8>
   114d3:	89 c2                	mov    %eax,%edx
   114d5:	f7 d2                	not    %edx
   114d7:	81 ca 07 ff ff ff    	or     $0xffffff07,%edx
   114dd:	01 c2                	add    %eax,%edx
   114df:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   114e3:	eb 19                	jmp    114fe <zbtIndexScanSlot+0x75e>
   114e5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
   114ec:	00 00 00 00
   114f0:	48 ff c6             	inc    %rsi
   114f3:	ff ca                	dec    %edx
   114f5:	48 39 c6             	cmp    %rax,%rsi
   114f8:	0f 83 de fb ff ff    	jae    110dc <zbtIndexScanSlot+0x33c>
   114fe:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   11502:	75 ec                	jne    114f0 <zbtIndexScanSlot+0x750>
   11504:	44 89 ff             	mov    %r15d,%edi
   11507:	41 ff c7             	inc    %r15d
   1150a:	89 94 bd 00 fe ff ff 	mov    %edx,-0x200(%rbp,%rdi,4)
   11511:	eb dd                	jmp    114f0 <zbtIndexScanSlot+0x750>
   11513:	31 ff                	xor    %edi,%edi
   11515:	45 89 e0             	mov    %r12d,%r8d
   11518:	41 80 f0 01          	xor    $0x1,%r8b
   1151c:	45 31 ff             	xor    %r15d,%r15d
   1151f:	eb 25                	jmp    11546 <zbtIndexScanSlot+0x7a6>
   11521:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   11528:	0f 1f 84 00 00 00 00
   1152f:	00
   11530:	48 ff c7             	inc    %rdi
   11533:	48 39 f7             	cmp    %rsi,%rdi
   11536:	49 bd ff fe fe fe fe 	movabs $0xfefefefefefefeff,%r13
   1153d:	fe fe fe
   11540:	0f 84 62 fa ff ff    	je     10fa8 <zbtIndexScanSlot+0x208>
   11546:	4c 8b 14 f9          	mov    (%rcx,%rdi,8),%r10
   1154a:	4d 89 d3             	mov    %r10,%r11
   1154d:	49 31 db             	xor    %rbx,%r11
   11550:	4d 89 d9             	mov    %r11,%r9
   11553:	49 f7 d1             	not    %r9
   11556:	4d 01 eb             	add    %r13,%r11
   11559:	49 be 80 80 80 80 80 	movabs $0x8080808080808080,%r14
   11560:	80 80 80
   11563:	4d 21 f1             	and    %r14,%r9
   11566:	4d 21 d9             	and    %r11,%r9
   11569:	41 80 fc 01          	cmp    $0x1,%r12b
   1156d:	75 10                	jne    1157f <zbtIndexScanSlot+0x7df>
   1156f:	4f 8d 1c 2a          	lea    (%r10,%r13,1),%r11
   11573:	49 f7 d2             	not    %r10
   11576:	4d 21 f2             	and    %r14,%r10
   11579:	4d 21 da             	and    %r11,%r10
   1157c:	4d 09 d1             	or     %r10,%r9
   1157f:	4d 85 c9             	test   %r9,%r9
   11582:	74 ac                	je     11530 <zbtIndexScanSlot+0x790>
   11584:	4c 8d 14 fd 00 00 00 	lea    0x0(,%rdi,8),%r10
   1158b:	00
   1158c:	eb 19                	jmp    115a7 <zbtIndexScanSlot+0x807>
   1158e:	66 90                	xchg   %ax,%ax
   11590:	45 89 fe             	mov    %r15d,%r14d
   11593:	41 ff c7             	inc    %r15d
   11596:	46 89 9c b5 00 fe ff 	mov    %r11d,-0x200(%rbp,%r14,4)
   1159d:	ff
   1159e:	4d 8d 59 ff          	lea    -0x1(%r9),%r11
   115a2:	4d 21 d9             	and    %r11,%r9
   115a5:	74 89                	je     11530 <zbtIndexScanSlot+0x790>
   115a7:	f3 4d 0f bc d9       	tzcnt  %r9,%r11
   115ac:	41 c1 eb 03          	shr    $0x3,%r11d
   115b0:	45 09 d3             	or     %r10d,%r11d
   115b3:	46 0f b6 2c 19       	movzbl (%rcx,%r11,1),%r13d
   115b8:	45 89 c6             	mov    %r8d,%r14d
   115bb:	45 08 ee             	or     %r13b,%r14b
   115be:	41 0f 94 c6          	sete   %r14b
   115c2:	45 38 e5             	cmp    %r12b,%r13b
   115c5:	74 c9                	je     11590 <zbtIndexScanSlot+0x7f0>
   115c7:	45 84 f6             	test   %r14b,%r14b
   115ca:	74 d2                	je     1159e <zbtIndexScanSlot+0x7fe>
   115cc:	eb c2                	jmp    11590 <zbtIndexScanSlot+0x7f0>
   115ce:	45 31 c0             	xor    %r8d,%r8d
   115d1:	45 31 ff             	xor    %r15d,%r15d
   115d4:	eb 16                	jmp    115ec <zbtIndexScanSlot+0x84c>
   115d6:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
   115dd:	00 00 00
   115e0:	49 ff c0             	inc    %r8
   115e3:	49 39 f0             	cmp    %rsi,%r8
   115e6:	0f 84 bc f9 ff ff    	je     10fa8 <zbtIndexScanSlot+0x208>
   115ec:	4e 8b 14 c1          	mov    (%rcx,%r8,8),%r10
   115f0:	49 31 da             	xor    %rbx,%r10
   115f3:	4d 89 d1             	mov    %r10,%r9
   115f6:	49 f7 d1             	not    %r9
   115f9:	4d 01 ea             	add    %r13,%r10
   115fc:	49 bb 80 80 80 80 80 	movabs $0x8080808080808080,%r11
   11603:	80 80 80
   11606:	4d 21 d9             	and    %r11,%r9
   11609:	4d 21 d1             	and    %r10,%r9
   1160c:	74 d2                	je     115e0 <zbtIndexScanSlot+0x840>
   1160e:	4e 8d 14 c5 00 00 00 	lea    0x0(,%r8,8),%r10
   11615:	00
   11616:	eb 11                	jmp    11629 <zbtIndexScanSlot+0x889>
   11618:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
   1161f:	00
   11620:	4d 8d 59 ff          	lea    -0x1(%r9),%r11
   11624:	4d 21 d9             	and    %r11,%r9
   11627:	74 b7                	je     115e0 <zbtIndexScanSlot+0x840>
   11629:	f3 4d 0f bc d9       	tzcnt  %r9,%r11
   1162e:	41 c1 eb 03          	shr    $0x3,%r11d
   11632:	45 09 d3             	or     %r10d,%r11d
   11635:	46 38 24 19          	cmp    %r12b,(%rcx,%r11,1)
   11639:	75 e5                	jne    11620 <zbtIndexScanSlot+0x880>
   1163b:	41 89 fe             	mov    %edi,%r14d
   1163e:	45 29 de             	sub    %r11d,%r14d
   11641:	45 89 fb             	mov    %r15d,%r11d
   11644:	41 ff c7             	inc    %r15d
   11647:	46 89 b4 9d 00 fe ff 	mov    %r14d,-0x200(%rbp,%r11,4)
   1164e:	ff
   1164f:	eb cf                	jmp    11620 <zbtIndexScanSlot+0x880>
   11651:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   11655:	eb 0c                	jmp    11663 <zbtIndexScanSlot+0x8c3>
   11657:	48 ff c6             	inc    %rsi
   1165a:	48 39 c6             	cmp    %rax,%rsi
   1165d:	0f 83 79 fa ff ff    	jae    110dc <zbtIndexScanSlot+0x33c>
   11663:	80 3c 31 01          	cmpb   $0x1,(%rcx,%rsi,1)
   11667:	77 ee                	ja     11657 <zbtIndexScanSlot+0x8b7>
   11669:	44 89 fa             	mov    %r15d,%edx
   1166c:	41 ff c7             	inc    %r15d
   1166f:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   11676:	eb df                	jmp    11657 <zbtIndexScanSlot+0x8b7>
   11678:	4c 8b 4d c8          	mov    -0x38(%rbp),%r9
   1167c:	eb 0c                	jmp    1168a <zbtIndexScanSlot+0x8ea>
   1167e:	48 ff c6             	inc    %rsi
   11681:	48 39 c6             	cmp    %rax,%rsi
   11684:	0f 83 52 fa ff ff    	jae    110dc <zbtIndexScanSlot+0x33c>
   1168a:	44 38 24 31          	cmp    %r12b,(%rcx,%rsi,1)
   1168e:	75 ee                	jne    1167e <zbtIndexScanSlot+0x8de>
   11690:	44 89 fa             	mov    %r15d,%edx
   11693:	41 ff c7             	inc    %r15d
   11696:	89 b4 95 00 fe ff ff 	mov    %esi,-0x200(%rbp,%rdx,4)
   1169d:	eb df                	jmp    1167e <zbtIndexScanSlot+0x8de>

Disassembly of section .fini:
