
scratch/amd-scoped-profile/base-fifo2-profile:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000f880 <zbtScoreDeleteInPlace>:
    f880:	55                   	push   %rbp
    f881:	48 89 e5             	mov    %rsp,%rbp
    f884:	41 57                	push   %r15
    f886:	41 56                	push   %r14
    f888:	41 55                	push   %r13
    f88a:	41 54                	push   %r12
    f88c:	53                   	push   %rbx
    f88d:	48 81 ec b8 00 00 00 	sub    $0xb8,%rsp
    f894:	89 4d c0             	mov    %ecx,-0x40(%rbp)
    f897:	89 d3                	mov    %edx,%ebx
    f899:	49 89 f7             	mov    %rsi,%r15
    f89c:	48 89 7d c8          	mov    %rdi,-0x38(%rbp)
    f8a0:	44 0f b6 76 11       	movzbl 0x11(%rsi),%r14d
    f8a5:	45 8d 66 ff          	lea    -0x1(%r14),%r12d
    f8a9:	41 39 d6             	cmp    %edx,%r14d
    f8ac:	76 05                	jbe    f8b3 <zbtScoreDeleteInPlace+0x33>
    f8ae:	45 85 e4             	test   %r12d,%r12d
    f8b1:	75 18                	jne    f8cb <zbtScoreDeleteInPlace+0x4b>
    f8b3:	48 8d 3d 27 3e 00 00 	lea    0x3e27(%rip),%rdi        # 136e1 <_IO_stdin_used+0x6e1>
    f8ba:	48 8d 15 1f 42 00 00 	lea    0x421f(%rip),%rdx        # 13ae0 <_IO_stdin_used+0xae0>
    f8c1:	be fb 09 00 00       	mov    $0x9fb,%esi
    f8c6:	e8 b5 1f 00 00       	call   11880 <standalone_panic>
    f8cb:	41 80 7f 35 00       	cmpb   $0x0,0x35(%r15)
    f8d0:	74 09                	je     f8db <zbtScoreDeleteInPlace+0x5b>
    f8d2:	41 0f b6 47 11       	movzbl 0x11(%r15),%eax
    f8d7:	f7 d3                	not    %ebx
    f8d9:	01 c3                	add    %eax,%ebx
    f8db:	41 0f b6 47 34       	movzbl 0x34(%r15),%eax
    f8e0:	48 85 c0             	test   %rax,%rax
    f8e3:	44 89 65 d4          	mov    %r12d,-0x2c(%rbp)
    f8e7:	74 1e                	je     f907 <zbtScoreDeleteInPlace+0x87>
    f8e9:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
    f8ee:	0f af c1             	imul   %ecx,%eax
    f8f1:	83 c0 07             	add    $0x7,%eax
    f8f4:	c1 e8 03             	shr    $0x3,%eax
    f8f7:	83 c0 09             	add    $0x9,%eax
    f8fa:	83 e0 fe             	and    $0xfffffffe,%eax
    f8fd:	4d 8d 24 07          	lea    (%r15,%rax,1),%r12
    f901:	49 83 c4 38          	add    $0x38,%r12
    f905:	eb 0b                	jmp    f912 <zbtScoreDeleteInPlace+0x92>
    f907:	4d 8d 67 38          	lea    0x38(%r15),%r12
    f90b:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
    f910:	31 c0                	xor    %eax,%eax
    f912:	4c 01 f8             	add    %r15,%rax
    f915:	48 83 c0 38          	add    $0x38,%rax
    f919:	48 8d 34 48          	lea    (%rax,%rcx,2),%rsi
    f91d:	48 8d bd 20 ff ff ff 	lea    -0xe0(%rbp),%rdi
    f924:	4c 89 f2             	mov    %r14,%rdx
    f927:	e8 34 18 ff ff       	call   1160 <memcpy@plt>
    f92c:	89 d8                	mov    %ebx,%eax
    f92e:	48 89 45 a8          	mov    %rax,-0x58(%rbp)
    f932:	41 0f b7 34 44       	movzwl (%r12,%rax,2),%esi
    f937:	44 0f b7 ee          	movzwl %si,%r13d
    f93b:	43 0f b6 04 2f       	movzbl (%r15,%r13,1),%eax
    f940:	3d fe 00 00 00       	cmp    $0xfe,%eax
    f945:	4c 89 e7             	mov    %r12,%rdi
    f948:	89 75 98             	mov    %esi,-0x68(%rbp)
    f94b:	89 5d d0             	mov    %ebx,-0x30(%rbp)
    f94e:	4c 89 65 b0          	mov    %r12,-0x50(%rbp)
    f952:	74 20                	je     f974 <zbtScoreDeleteInPlace+0xf4>
    f954:	3d ff 00 00 00       	cmp    $0xff,%eax
    f959:	75 1f                	jne    f97a <zbtScoreDeleteInPlace+0xfa>
    f95b:	83 7d c0 00          	cmpl   $0x0,-0x40(%rbp)
    f95f:	74 44                	je     f9a5 <zbtScoreDeleteInPlace+0x125>
    f961:	41 89 f4             	mov    %esi,%r12d
    f964:	4b 8b 7c 2f 0d       	mov    0xd(%r15,%r13,1),%rdi
    f969:	48 85 ff             	test   %rdi,%rdi
    f96c:	74 3e                	je     f9ac <zbtScoreDeleteInPlace+0x12c>
    f96e:	48 8d 75 a0          	lea    -0x60(%rbp),%rsi
    f972:	eb 56                	jmp    f9ca <zbtScoreDeleteInPlace+0x14a>
    f974:	43 0f b7 44 2f 01    	movzwl 0x1(%r15,%r13,1),%eax
    f97a:	31 c9                	xor    %ecx,%ecx
    f97c:	48 3d fe 00 00 00    	cmp    $0xfe,%rax
    f982:	0f 93 c1             	setae  %cl
    f985:	48 8d 1c 48          	lea    (%rax,%rcx,2),%rbx
    f989:	48 ff c3             	inc    %rbx
    f98c:	83 7d c0 00          	cmpl   $0x0,-0x40(%rbp)
    f990:	0f 84 81 00 00 00    	je     fa17 <zbtScoreDeleteInPlace+0x197>
    f996:	41 0f b7 47 36       	movzwl 0x36(%r15),%eax
    f99b:	66 39 c6             	cmp    %ax,%si
    f99e:	75 51                	jne    f9f1 <zbtScoreDeleteInPlace+0x171>
    f9a0:	e9 88 00 00 00       	jmp    fa2d <zbtScoreDeleteInPlace+0x1ad>
    f9a5:	bb 15 00 00 00       	mov    $0x15,%ebx
    f9aa:	eb 6b                	jmp    fa17 <zbtScoreDeleteInPlace+0x197>
    f9ac:	48 8d 3d 2e 3d 00 00 	lea    0x3d2e(%rip),%rdi        # 136e1 <_IO_stdin_used+0x6e1>
    f9b3:	48 8d 15 43 41 00 00 	lea    0x4143(%rip),%rdx        # 13afd <_IO_stdin_used+0xafd>
    f9ba:	be 07 0a 00 00       	mov    $0xa07,%esi
    f9bf:	e8 bc 1e 00 00       	call   11880 <standalone_panic>
    f9c4:	48 8d 75 a0          	lea    -0x60(%rbp),%rsi
    f9c8:	31 ff                	xor    %edi,%edi
    f9ca:	e8 b1 20 00 00       	call   11a80 <zfree_usable>
    f9cf:	48 8b 45 a0          	mov    -0x60(%rbp),%rax
    f9d3:	48 8b 4d c8          	mov    -0x38(%rbp),%rcx
    f9d7:	48 29 41 68          	sub    %rax,0x68(%rcx)
    f9db:	bb 15 00 00 00       	mov    $0x15,%ebx
    f9e0:	44 89 e6             	mov    %r12d,%esi
    f9e3:	48 8b 7d b0          	mov    -0x50(%rbp),%rdi
    f9e7:	41 0f b7 47 36       	movzwl 0x36(%r15),%eax
    f9ec:	66 39 c6             	cmp    %ax,%si
    f9ef:	74 3c                	je     fa2d <zbtScoreDeleteInPlace+0x1ad>
    f9f1:	4d 85 f6             	test   %r14,%r14
    f9f4:	74 21                	je     fa17 <zbtScoreDeleteInPlace+0x197>
    f9f6:	b9 01 00 00 00       	mov    $0x1,%ecx
    f9fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
    fa00:	0f b7 54 4f fe       	movzwl -0x2(%rdi,%rcx,2),%edx
    fa05:	4c 39 f1             	cmp    %r14,%rcx
    fa08:	73 08                	jae    fa12 <zbtScoreDeleteInPlace+0x192>
    fa0a:	48 ff c1             	inc    %rcx
    fa0d:	66 39 f2             	cmp    %si,%dx
    fa10:	76 ee                	jbe    fa00 <zbtScoreDeleteInPlace+0x180>
    fa12:	66 39 f2             	cmp    %si,%dx
    fa15:	77 16                	ja     fa2d <zbtScoreDeleteInPlace+0x1ad>
    fa17:	c7 45 bc 00 00 00 00 	movl   $0x0,-0x44(%rbp)
    fa1e:	66 41 3b 77 36       	cmp    0x36(%r15),%si
    fa23:	75 3b                	jne    fa60 <zbtScoreDeleteInPlace+0x1e0>
    fa25:	4d 8d 77 36          	lea    0x36(%r15),%r14
    fa29:	89 f0                	mov    %esi,%eax
    fa2b:	eb 27                	jmp    fa54 <zbtScoreDeleteInPlace+0x1d4>
    fa2d:	4d 8d 77 36          	lea    0x36(%r15),%r14
    fa31:	49 8d 34 07          	lea    (%r15,%rax,1),%rsi
    fa35:	49 89 fc             	mov    %rdi,%r12
    fa38:	48 8d 3c 1e          	lea    (%rsi,%rbx,1),%rdi
    fa3c:	49 29 c5             	sub    %rax,%r13
    fa3f:	4c 89 ea             	mov    %r13,%rdx
    fa42:	e8 59 17 ff ff       	call   11a0 <memmove@plt>
    fa47:	4c 89 e7             	mov    %r12,%rdi
    fa4a:	41 0f b7 47 36       	movzwl 0x36(%r15),%eax
    fa4f:	b1 01                	mov    $0x1,%cl
    fa51:	89 4d bc             	mov    %ecx,-0x44(%rbp)
    fa54:	44 8b 65 d4          	mov    -0x2c(%rbp),%r12d
    fa58:	01 d8                	add    %ebx,%eax
    fa5a:	66 41 89 06          	mov    %ax,(%r14)
    fa5e:	eb 04                	jmp    fa64 <zbtScoreDeleteInPlace+0x1e4>
    fa60:	44 8b 65 d4          	mov    -0x2c(%rbp),%r12d
    fa64:	4d 8d 77 38          	lea    0x38(%r15),%r14
    fa68:	48 8b 45 a8          	mov    -0x58(%rbp),%rax
    fa6c:	48 8d 3c 47          	lea    (%rdi,%rax,2),%rdi
    fa70:	41 0f b6 47 34       	movzbl 0x34(%r15),%eax
    fa75:	85 c0                	test   %eax,%eax
    fa77:	4c 89 7d c8          	mov    %r15,-0x38(%rbp)
    fa7b:	0f 84 c8 01 00 00    	je     fc49 <zbtScoreDeleteInPlace+0x3c9>
    fa81:	48 89 7d 80          	mov    %rdi,-0x80(%rbp)
    fa85:	89 45 9c             	mov    %eax,-0x64(%rbp)
    fa88:	89 c0                	mov    %eax,%eax
    fa8a:	48 89 45 90          	mov    %rax,-0x70(%rbp)
    fa8e:	41 0f b6 4f 11       	movzbl 0x11(%r15),%ecx
    fa93:	8b 45 d0             	mov    -0x30(%rbp),%eax
    fa96:	41 89 c3             	mov    %eax,%r11d
    fa99:	41 f7 d3             	not    %r11d
    fa9c:	48 89 4d 88          	mov    %rcx,-0x78(%rbp)
    faa0:	41 01 cb             	add    %ecx,%r11d
    faa3:	0f 84 24 01 00 00    	je     fbcd <zbtScoreDeleteInPlace+0x34d>
    faa9:	48 8b 45 90          	mov    -0x70(%rbp),%rax
    faad:	49 89 c4             	mov    %rax,%r12
    fab0:	4c 0f af 65 a8       	imul   -0x58(%rbp),%r12
    fab5:	4c 0f af d8          	imul   %rax,%r11
    fab9:	4c 01 e0             	add    %r12,%rax
    fabc:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
    fac0:	45 31 d2             	xor    %r10d,%r10d
    fac3:	eb 17                	jmp    fadc <zbtScoreDeleteInPlace+0x25c>
    fac5:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
    facc:	00 00 00 00
    fad0:	49 01 d2             	add    %rdx,%r10
    fad3:	4d 39 da             	cmp    %r11,%r10
    fad6:	0f 83 f1 00 00 00    	jae    fbcd <zbtScoreDeleteInPlace+0x34d>
    fadc:	4c 89 da             	mov    %r11,%rdx
    fadf:	4c 29 d2             	sub    %r10,%rdx
    fae2:	48 83 fa 40          	cmp    $0x40,%rdx
    fae6:	b8 40 00 00 00       	mov    $0x40,%eax
    faeb:	48 0f 43 d0          	cmovae %rax,%rdx
    faef:	48 8b 45 c0          	mov    -0x40(%rbp),%rax
    faf3:	4a 8d 0c 10          	lea    (%rax,%r10,1),%rcx
    faf7:	49 89 c8             	mov    %rcx,%r8
    fafa:	49 c1 e8 03          	shr    $0x3,%r8
    fafe:	89 c8                	mov    %ecx,%eax
    fb00:	83 e0 07             	and    $0x7,%eax
    fb03:	be 40 00 00 00       	mov    $0x40,%esi
    fb08:	29 c6                	sub    %eax,%esi
    fb0a:	4b 8b 04 06          	mov    (%r14,%r8,1),%rax
    fb0e:	80 e1 07             	and    $0x7,%cl
    fb11:	48 d3 e8             	shr    %cl,%rax
    fb14:	39 d6                	cmp    %edx,%esi
    fb16:	73 0e                	jae    fb26 <zbtScoreDeleteInPlace+0x2a6>
    fb18:	47 0f b6 44 06 08    	movzbl 0x8(%r14,%r8,1),%r8d
    fb1e:	89 f1                	mov    %esi,%ecx
    fb20:	49 d3 e0             	shl    %cl,%r8
    fb23:	4c 09 c0             	or     %r8,%rax
    fb26:	48 c7 c7 ff ff ff ff 	mov    $0xffffffffffffffff,%rdi
    fb2d:	89 d1                	mov    %edx,%ecx
    fb2f:	48 d3 e7             	shl    %cl,%rdi
    fb32:	83 fa 40             	cmp    $0x40,%edx
    fb35:	48 f7 d7             	not    %rdi
    fb38:	49 c7 c7 ff ff ff ff 	mov    $0xffffffffffffffff,%r15
    fb3f:	49 0f 43 ff          	cmovae %r15,%rdi
    fb43:	48 21 c7             	and    %rax,%rdi
    fb46:	4f 8d 04 22          	lea    (%r10,%r12,1),%r8
    fb4a:	4c 89 c0             	mov    %r8,%rax
    fb4d:	48 c1 e8 03          	shr    $0x3,%rax
    fb51:	41 83 e0 07          	and    $0x7,%r8d
    fb55:	41 b9 40 00 00 00    	mov    $0x40,%r9d
    fb5b:	45 29 c1             	sub    %r8d,%r9d
    fb5e:	41 39 d1             	cmp    %edx,%r9d
    fb61:	89 d6                	mov    %edx,%esi
    fb63:	41 0f 42 f1          	cmovb  %r9d,%esi
    fb67:	49 c7 c5 ff ff ff ff 	mov    $0xffffffffffffffff,%r13
    fb6e:	89 f1                	mov    %esi,%ecx
    fb70:	49 d3 e5             	shl    %cl,%r13
    fb73:	83 fe 40             	cmp    $0x40,%esi
    fb76:	49 f7 d5             	not    %r13
    fb79:	4d 0f 44 ef          	cmove  %r15,%r13
    fb7d:	49 89 ff             	mov    %rdi,%r15
    fb80:	4d 21 ef             	and    %r13,%r15
    fb83:	44 89 c1             	mov    %r8d,%ecx
    fb86:	49 d3 e5             	shl    %cl,%r13
    fb89:	49 f7 d5             	not    %r13
    fb8c:	4d 23 2c 06          	and    (%r14,%rax,1),%r13
    fb90:	49 d3 e7             	shl    %cl,%r15
    fb93:	4d 09 ef             	or     %r13,%r15
    fb96:	4d 89 3c 06          	mov    %r15,(%r14,%rax,1)
    fb9a:	41 39 d1             	cmp    %edx,%r9d
    fb9d:	0f 83 2d ff ff ff    	jae    fad0 <zbtScoreDeleteInPlace+0x250>
    fba3:	41 89 d0             	mov    %edx,%r8d
    fba6:	41 29 f0             	sub    %esi,%r8d
    fba9:	45 0f b6 4c 06 08    	movzbl 0x8(%r14,%rax,1),%r9d
    fbaf:	89 f1                	mov    %esi,%ecx
    fbb1:	48 d3 ef             	shr    %cl,%rdi
    fbb4:	41 31 f9             	xor    %edi,%r9d
    fbb7:	44 89 c1             	mov    %r8d,%ecx
    fbba:	41 d3 e9             	shr    %cl,%r9d
    fbbd:	41 d3 e1             	shl    %cl,%r9d
    fbc0:	41 31 f9             	xor    %edi,%r9d
    fbc3:	45 88 4c 06 08       	mov    %r9b,0x8(%r14,%rax,1)
    fbc8:	e9 03 ff ff ff       	jmp    fad0 <zbtScoreDeleteInPlace+0x250>
    fbcd:	48 8b 45 88          	mov    -0x78(%rbp),%rax
    fbd1:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
    fbd5:	48 0f af 55 90       	imul   -0x70(%rbp),%rdx
    fbda:	48 89 d0             	mov    %rdx,%rax
    fbdd:	48 c1 e8 03          	shr    $0x3,%rax
    fbe1:	89 d1                	mov    %edx,%ecx
    fbe3:	83 e1 07             	and    $0x7,%ecx
    fbe6:	bf 40 00 00 00       	mov    $0x40,%edi
    fbeb:	29 cf                	sub    %ecx,%edi
    fbed:	44 8b 4d 9c          	mov    -0x64(%rbp),%r9d
    fbf1:	44 39 cf             	cmp    %r9d,%edi
    fbf4:	44 89 ce             	mov    %r9d,%esi
    fbf7:	0f 42 f7             	cmovb  %edi,%esi
    fbfa:	49 c7 c0 ff ff ff ff 	mov    $0xffffffffffffffff,%r8
    fc01:	89 f1                	mov    %esi,%ecx
    fc03:	49 d3 e0             	shl    %cl,%r8
    fc06:	48 c7 c1 ff ff ff ff 	mov    $0xffffffffffffffff,%rcx
    fc0d:	83 fe 40             	cmp    $0x40,%esi
    fc10:	49 f7 d0             	not    %r8
    fc13:	4c 0f 44 c1          	cmove  %rcx,%r8
    fc17:	80 e2 07             	and    $0x7,%dl
    fc1a:	89 d1                	mov    %edx,%ecx
    fc1c:	49 d3 e0             	shl    %cl,%r8
    fc1f:	49 f7 d0             	not    %r8
    fc22:	4d 21 04 06          	and    %r8,(%r14,%rax,1)
    fc26:	44 39 cf             	cmp    %r9d,%edi
    fc29:	4c 8b 7d c8          	mov    -0x38(%rbp),%r15
    fc2d:	44 8b 65 d4          	mov    -0x2c(%rbp),%r12d
    fc31:	48 8b 7d 80          	mov    -0x80(%rbp),%rdi
    fc35:	73 12                	jae    fc49 <zbtScoreDeleteInPlace+0x3c9>
    fc37:	41 29 f1             	sub    %esi,%r9d
    fc3a:	ba ff ff ff ff       	mov    $0xffffffff,%edx
    fc3f:	44 89 c9             	mov    %r9d,%ecx
    fc42:	d3 e2                	shl    %cl,%edx
    fc44:	41 20 54 06 08       	and    %dl,0x8(%r14,%rax,1)
    fc49:	48 8d 77 02          	lea    0x2(%rdi),%rsi
    fc4d:	44 89 e0             	mov    %r12d,%eax
    fc50:	2b 45 d0             	sub    -0x30(%rbp),%eax
    fc53:	48 89 45 c0          	mov    %rax,-0x40(%rbp)
    fc57:	48 8d 14 00          	lea    (%rax,%rax,1),%rdx
    fc5b:	e8 40 15 ff ff       	call   11a0 <memmove@plt>
    fc60:	41 0f b6 47 34       	movzbl 0x34(%r15),%eax
    fc65:	44 89 e1             	mov    %r12d,%ecx
    fc68:	45 89 e5             	mov    %r12d,%r13d
    fc6b:	48 85 c0             	test   %rax,%rax
    fc6e:	74 16                	je     fc86 <zbtScoreDeleteInPlace+0x406>
    fc70:	49 0f af c5          	imul   %r13,%rax
    fc74:	48 83 c0 07          	add    $0x7,%rax
    fc78:	48 c1 e8 03          	shr    $0x3,%rax
    fc7c:	48 83 c0 09          	add    $0x9,%rax
    fc80:	48 83 e0 fe          	and    $0xfffffffffffffffe,%rax
    fc84:	eb 02                	jmp    fc88 <zbtScoreDeleteInPlace+0x408>
    fc86:	31 c0                	xor    %eax,%eax
    fc88:	85 c9                	test   %ecx,%ecx
    fc8a:	0f 94 45 d0          	sete   -0x30(%rbp)
    fc8e:	49 01 c6             	add    %rax,%r14
    fc91:	4a 8d 14 6d 00 00 00 	lea    0x0(,%r13,2),%rdx
    fc98:	00
    fc99:	4c 89 f7             	mov    %r14,%rdi
    fc9c:	48 8b 75 b0          	mov    -0x50(%rbp),%rsi
    fca0:	e8 fb 14 ff ff       	call   11a0 <memmove@plt>
    fca5:	4f 8d 3c 6e          	lea    (%r14,%r13,2),%r15
    fca9:	48 8d b5 20 ff ff ff 	lea    -0xe0(%rbp),%rsi
    fcb0:	4c 89 ff             	mov    %r15,%rdi
    fcb3:	4c 8b 65 a8          	mov    -0x58(%rbp),%r12
    fcb7:	4c 89 e2             	mov    %r12,%rdx
    fcba:	e8 a1 14 ff ff       	call   1160 <memcpy@plt>
    fcbf:	4d 01 e7             	add    %r12,%r15
    fcc2:	49 8d 34 2c          	lea    (%r12,%rbp,1),%rsi
    fcc6:	48 81 c6 21 ff ff ff 	add    $0xffffffffffffff21,%rsi
    fccd:	4c 89 ff             	mov    %r15,%rdi
    fcd0:	48 8b 55 c0          	mov    -0x40(%rbp),%rdx
    fcd4:	e8 87 14 ff ff       	call   1160 <memcpy@plt>
    fcd9:	8b 4d d4             	mov    -0x2c(%rbp),%ecx
    fcdc:	48 8b 45 c8          	mov    -0x38(%rbp),%rax
    fce0:	88 48 11             	mov    %cl,0x11(%rax)
    fce3:	4c 89 68 08          	mov    %r13,0x8(%rax)
    fce7:	8b 45 bc             	mov    -0x44(%rbp),%eax
    fcea:	34 01                	xor    $0x1,%al
    fcec:	0a 45 d0             	or     -0x30(%rbp),%al
    fcef:	8b 7d 98             	mov    -0x68(%rbp),%edi
    fcf2:	0f 85 f9 02 00 00    	jne    fff1 <zbtScoreDeleteInPlace+0x771>
    fcf8:	83 f9 10             	cmp    $0x10,%ecx
    fcfb:	73 07                	jae    fd04 <zbtScoreDeleteInPlace+0x484>
    fcfd:	31 c0                	xor    %eax,%eax
    fcff:	e9 24 03 00 00       	jmp    10028 <zbtScoreDeleteInPlace+0x7a8>
    fd04:	44 89 e8             	mov    %r13d,%eax
    fd07:	83 e0 f0             	and    $0xfffffff0,%eax
    fd0a:	66 0f 6e c7          	movd   %edi,%xmm0
    fd0e:	f2 0f 70 c0 00       	pshuflw $0x0,%xmm0,%xmm0
    fd13:	66 0f 70 c0 00       	pshufd $0x0,%xmm0,%xmm0
    fd18:	31 c9                	xor    %ecx,%ecx
    fd1a:	66 0f 6f 0d 2e 33 00 	movdqa 0x332e(%rip),%xmm1        # 13050 <_IO_stdin_used+0x50>
    fd21:	00
    fd22:	66 0f ef c1          	pxor   %xmm1,%xmm0
    fd26:	eb 15                	jmp    fd3d <zbtScoreDeleteInPlace+0x4bd>
    fd28:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
    fd2f:	00
    fd30:	48 83 c1 10          	add    $0x10,%rcx
    fd34:	48 39 c8             	cmp    %rcx,%rax
    fd37:	0f 84 af 02 00 00    	je     ffec <zbtScoreDeleteInPlace+0x76c>
    fd3d:	f3 41 0f 6f 14 4e    	movdqu (%r14,%rcx,2),%xmm2
    fd43:	66 0f 6f e2          	movdqa %xmm2,%xmm4
    fd47:	66 0f ef e1          	pxor   %xmm1,%xmm4
    fd4b:	66 0f 6f d8          	movdqa %xmm0,%xmm3
    fd4f:	66 0f 65 dc          	pcmpgtw %xmm4,%xmm3
    fd53:	66 0f 7e da          	movd   %xmm3,%edx
    fd57:	f6 c2 01             	test   $0x1,%dl
    fd5a:	0f 85 00 01 00 00    	jne    fe60 <zbtScoreDeleteInPlace+0x5e0>
    fd60:	c1 ea 10             	shr    $0x10,%edx
    fd63:	f6 c2 01             	test   $0x1,%dl
    fd66:	0f 85 0b 01 00 00    	jne    fe77 <zbtScoreDeleteInPlace+0x5f7>
    fd6c:	66 0f c5 d3 02       	pextrw $0x2,%xmm3,%edx
    fd71:	f6 c2 01             	test   $0x1,%dl
    fd74:	0f 85 18 01 00 00    	jne    fe92 <zbtScoreDeleteInPlace+0x612>
    fd7a:	66 0f c5 d3 03       	pextrw $0x3,%xmm3,%edx
    fd7f:	f6 c2 01             	test   $0x1,%dl
    fd82:	0f 85 25 01 00 00    	jne    fead <zbtScoreDeleteInPlace+0x62d>
    fd88:	66 0f c5 d3 04       	pextrw $0x4,%xmm3,%edx
    fd8d:	f6 c2 01             	test   $0x1,%dl
    fd90:	0f 85 32 01 00 00    	jne    fec8 <zbtScoreDeleteInPlace+0x648>
    fd96:	66 0f c5 d3 05       	pextrw $0x5,%xmm3,%edx
    fd9b:	f6 c2 01             	test   $0x1,%dl
    fd9e:	0f 85 3f 01 00 00    	jne    fee3 <zbtScoreDeleteInPlace+0x663>
    fda4:	66 0f c5 d3 06       	pextrw $0x6,%xmm3,%edx
    fda9:	f6 c2 01             	test   $0x1,%dl
    fdac:	0f 85 4c 01 00 00    	jne    fefe <zbtScoreDeleteInPlace+0x67e>
    fdb2:	66 0f c5 d3 07       	pextrw $0x7,%xmm3,%edx
    fdb7:	f6 c2 01             	test   $0x1,%dl
    fdba:	74 0d                	je     fdc9 <zbtScoreDeleteInPlace+0x549>
    fdbc:	66 0f c5 d2 07       	pextrw $0x7,%xmm2,%edx
    fdc1:	01 da                	add    %ebx,%edx
    fdc3:	66 41 89 54 4e 0e    	mov    %dx,0xe(%r14,%rcx,2)
    fdc9:	f3 41 0f 6f 54 4e 10 	movdqu 0x10(%r14,%rcx,2),%xmm2
    fdd0:	66 0f 6f e2          	movdqa %xmm2,%xmm4
    fdd4:	66 0f ef e1          	pxor   %xmm1,%xmm4
    fdd8:	66 0f 6f d8          	movdqa %xmm0,%xmm3
    fddc:	66 0f 65 dc          	pcmpgtw %xmm4,%xmm3
    fde0:	66 0f 7e da          	movd   %xmm3,%edx
    fde4:	f6 c2 01             	test   $0x1,%dl
    fde7:	0f 85 33 01 00 00    	jne    ff20 <zbtScoreDeleteInPlace+0x6a0>
    fded:	c1 ea 10             	shr    $0x10,%edx
    fdf0:	f6 c2 01             	test   $0x1,%dl
    fdf3:	0f 85 3f 01 00 00    	jne    ff38 <zbtScoreDeleteInPlace+0x6b8>
    fdf9:	66 0f c5 d3 02       	pextrw $0x2,%xmm3,%edx
    fdfe:	f6 c2 01             	test   $0x1,%dl
    fe01:	0f 85 4c 01 00 00    	jne    ff53 <zbtScoreDeleteInPlace+0x6d3>
    fe07:	66 0f c5 d3 03       	pextrw $0x3,%xmm3,%edx
    fe0c:	f6 c2 01             	test   $0x1,%dl
    fe0f:	0f 85 59 01 00 00    	jne    ff6e <zbtScoreDeleteInPlace+0x6ee>
    fe15:	66 0f c5 d3 04       	pextrw $0x4,%xmm3,%edx
    fe1a:	f6 c2 01             	test   $0x1,%dl
    fe1d:	0f 85 66 01 00 00    	jne    ff89 <zbtScoreDeleteInPlace+0x709>
    fe23:	66 0f c5 d3 05       	pextrw $0x5,%xmm3,%edx
    fe28:	f6 c2 01             	test   $0x1,%dl
    fe2b:	0f 85 73 01 00 00    	jne    ffa4 <zbtScoreDeleteInPlace+0x724>
    fe31:	66 0f c5 d3 06       	pextrw $0x6,%xmm3,%edx
    fe36:	f6 c2 01             	test   $0x1,%dl
    fe39:	0f 85 80 01 00 00    	jne    ffbf <zbtScoreDeleteInPlace+0x73f>
    fe3f:	66 0f c5 d3 07       	pextrw $0x7,%xmm3,%edx
    fe44:	f6 c2 01             	test   $0x1,%dl
    fe47:	0f 84 e3 fe ff ff    	je     fd30 <zbtScoreDeleteInPlace+0x4b0>
    fe4d:	e9 88 01 00 00       	jmp    ffda <zbtScoreDeleteInPlace+0x75a>
    fe52:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
    fe59:	1f 84 00 00 00 00 00
    fe60:	66 0f 7e d6          	movd   %xmm2,%esi
    fe64:	01 de                	add    %ebx,%esi
    fe66:	66 41 89 34 4e       	mov    %si,(%r14,%rcx,2)
    fe6b:	c1 ea 10             	shr    $0x10,%edx
    fe6e:	f6 c2 01             	test   $0x1,%dl
    fe71:	0f 84 f5 fe ff ff    	je     fd6c <zbtScoreDeleteInPlace+0x4ec>
    fe77:	66 0f c5 d2 01       	pextrw $0x1,%xmm2,%edx
    fe7c:	01 da                	add    %ebx,%edx
    fe7e:	66 41 89 54 4e 02    	mov    %dx,0x2(%r14,%rcx,2)
    fe84:	66 0f c5 d3 02       	pextrw $0x2,%xmm3,%edx
    fe89:	f6 c2 01             	test   $0x1,%dl
    fe8c:	0f 84 e8 fe ff ff    	je     fd7a <zbtScoreDeleteInPlace+0x4fa>
    fe92:	66 0f c5 d2 02       	pextrw $0x2,%xmm2,%edx
    fe97:	01 da                	add    %ebx,%edx
    fe99:	66 41 89 54 4e 04    	mov    %dx,0x4(%r14,%rcx,2)
    fe9f:	66 0f c5 d3 03       	pextrw $0x3,%xmm3,%edx
    fea4:	f6 c2 01             	test   $0x1,%dl
    fea7:	0f 84 db fe ff ff    	je     fd88 <zbtScoreDeleteInPlace+0x508>
    fead:	66 0f c5 d2 03       	pextrw $0x3,%xmm2,%edx
    feb2:	01 da                	add    %ebx,%edx
    feb4:	66 41 89 54 4e 06    	mov    %dx,0x6(%r14,%rcx,2)
    feba:	66 0f c5 d3 04       	pextrw $0x4,%xmm3,%edx
    febf:	f6 c2 01             	test   $0x1,%dl
    fec2:	0f 84 ce fe ff ff    	je     fd96 <zbtScoreDeleteInPlace+0x516>
    fec8:	66 0f c5 d2 04       	pextrw $0x4,%xmm2,%edx
    fecd:	01 da                	add    %ebx,%edx
    fecf:	66 41 89 54 4e 08    	mov    %dx,0x8(%r14,%rcx,2)
    fed5:	66 0f c5 d3 05       	pextrw $0x5,%xmm3,%edx
    feda:	f6 c2 01             	test   $0x1,%dl
    fedd:	0f 84 c1 fe ff ff    	je     fda4 <zbtScoreDeleteInPlace+0x524>
    fee3:	66 0f c5 d2 05       	pextrw $0x5,%xmm2,%edx
    fee8:	01 da                	add    %ebx,%edx
    feea:	66 41 89 54 4e 0a    	mov    %dx,0xa(%r14,%rcx,2)
    fef0:	66 0f c5 d3 06       	pextrw $0x6,%xmm3,%edx
    fef5:	f6 c2 01             	test   $0x1,%dl
    fef8:	0f 84 b4 fe ff ff    	je     fdb2 <zbtScoreDeleteInPlace+0x532>
    fefe:	66 0f c5 d2 06       	pextrw $0x6,%xmm2,%edx
    ff03:	01 da                	add    %ebx,%edx
    ff05:	66 41 89 54 4e 0c    	mov    %dx,0xc(%r14,%rcx,2)
    ff0b:	66 0f c5 d3 07       	pextrw $0x7,%xmm3,%edx
    ff10:	f6 c2 01             	test   $0x1,%dl
    ff13:	0f 85 a3 fe ff ff    	jne    fdbc <zbtScoreDeleteInPlace+0x53c>
    ff19:	e9 ab fe ff ff       	jmp    fdc9 <zbtScoreDeleteInPlace+0x549>
    ff1e:	66 90                	xchg   %ax,%ax
    ff20:	66 0f 7e d6          	movd   %xmm2,%esi
    ff24:	01 de                	add    %ebx,%esi
    ff26:	66 41 89 74 4e 10    	mov    %si,0x10(%r14,%rcx,2)
    ff2c:	c1 ea 10             	shr    $0x10,%edx
    ff2f:	f6 c2 01             	test   $0x1,%dl
    ff32:	0f 84 c1 fe ff ff    	je     fdf9 <zbtScoreDeleteInPlace+0x579>
    ff38:	66 0f c5 d2 01       	pextrw $0x1,%xmm2,%edx
    ff3d:	01 da                	add    %ebx,%edx
    ff3f:	66 41 89 54 4e 12    	mov    %dx,0x12(%r14,%rcx,2)
    ff45:	66 0f c5 d3 02       	pextrw $0x2,%xmm3,%edx
    ff4a:	f6 c2 01             	test   $0x1,%dl
    ff4d:	0f 84 b4 fe ff ff    	je     fe07 <zbtScoreDeleteInPlace+0x587>
    ff53:	66 0f c5 d2 02       	pextrw $0x2,%xmm2,%edx
    ff58:	01 da                	add    %ebx,%edx
    ff5a:	66 41 89 54 4e 14    	mov    %dx,0x14(%r14,%rcx,2)
    ff60:	66 0f c5 d3 03       	pextrw $0x3,%xmm3,%edx
    ff65:	f6 c2 01             	test   $0x1,%dl
    ff68:	0f 84 a7 fe ff ff    	je     fe15 <zbtScoreDeleteInPlace+0x595>
    ff6e:	66 0f c5 d2 03       	pextrw $0x3,%xmm2,%edx
    ff73:	01 da                	add    %ebx,%edx
    ff75:	66 41 89 54 4e 16    	mov    %dx,0x16(%r14,%rcx,2)
    ff7b:	66 0f c5 d3 04       	pextrw $0x4,%xmm3,%edx
    ff80:	f6 c2 01             	test   $0x1,%dl
    ff83:	0f 84 9a fe ff ff    	je     fe23 <zbtScoreDeleteInPlace+0x5a3>
    ff89:	66 0f c5 d2 04       	pextrw $0x4,%xmm2,%edx
    ff8e:	01 da                	add    %ebx,%edx
    ff90:	66 41 89 54 4e 18    	mov    %dx,0x18(%r14,%rcx,2)
    ff96:	66 0f c5 d3 05       	pextrw $0x5,%xmm3,%edx
    ff9b:	f6 c2 01             	test   $0x1,%dl
    ff9e:	0f 84 8d fe ff ff    	je     fe31 <zbtScoreDeleteInPlace+0x5b1>
    ffa4:	66 0f c5 d2 05       	pextrw $0x5,%xmm2,%edx
    ffa9:	01 da                	add    %ebx,%edx
    ffab:	66 41 89 54 4e 1a    	mov    %dx,0x1a(%r14,%rcx,2)
    ffb1:	66 0f c5 d3 06       	pextrw $0x6,%xmm3,%edx
    ffb6:	f6 c2 01             	test   $0x1,%dl
    ffb9:	0f 84 80 fe ff ff    	je     fe3f <zbtScoreDeleteInPlace+0x5bf>
    ffbf:	66 0f c5 d2 06       	pextrw $0x6,%xmm2,%edx
    ffc4:	01 da                	add    %ebx,%edx
    ffc6:	66 41 89 54 4e 1c    	mov    %dx,0x1c(%r14,%rcx,2)
    ffcc:	66 0f c5 d3 07       	pextrw $0x7,%xmm3,%edx
    ffd1:	f6 c2 01             	test   $0x1,%dl
    ffd4:	0f 84 56 fd ff ff    	je     fd30 <zbtScoreDeleteInPlace+0x4b0>
    ffda:	66 0f c5 d2 07       	pextrw $0x7,%xmm2,%edx
    ffdf:	01 da                	add    %ebx,%edx
    ffe1:	66 41 89 54 4e 1e    	mov    %dx,0x1e(%r14,%rcx,2)
    ffe7:	e9 44 fd ff ff       	jmp    fd30 <zbtScoreDeleteInPlace+0x4b0>
    ffec:	4c 39 e8             	cmp    %r13,%rax
    ffef:	75 37                	jne    10028 <zbtScoreDeleteInPlace+0x7a8>
    fff1:	48 8b 7d c8          	mov    -0x38(%rbp),%rdi
    fff5:	48 c7 c6 ff ff ff ff 	mov    $0xffffffffffffffff,%rsi
    fffc:	e8 4f f1 ff ff       	call   f150 <zbtScoreUpdatePath>
   10001:	48 81 c4 b8 00 00 00 	add    $0xb8,%rsp
   10008:	5b                   	pop    %rbx
   10009:	41 5c                	pop    %r12
   1000b:	41 5d                	pop    %r13
   1000d:	41 5e                	pop    %r14
   1000f:	41 5f                	pop    %r15
   10011:	5d                   	pop    %rbp
   10012:	c3                   	ret
   10013:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nopw 0x0(%rax,%rax,1)
   1001a:	84 00 00 00 00 00
   10020:	48 ff c0             	inc    %rax
   10023:	49 39 c5             	cmp    %rax,%r13
   10026:	74 c9                	je     fff1 <zbtScoreDeleteInPlace+0x771>
   10028:	41 0f b7 0c 46       	movzwl (%r14,%rax,2),%ecx
   1002d:	66 39 f9             	cmp    %di,%cx
   10030:	73 ee                	jae    10020 <zbtScoreDeleteInPlace+0x7a0>
   10032:	01 d9                	add    %ebx,%ecx
   10034:	66 41 89 0c 46       	mov    %cx,(%r14,%rax,2)
   10039:	eb e5                	jmp    10020 <zbtScoreDeleteInPlace+0x7a0>

Disassembly of section .fini:
