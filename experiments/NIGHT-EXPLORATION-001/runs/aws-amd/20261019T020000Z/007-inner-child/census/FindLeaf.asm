
build/size-matrix/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000a5c0 <zbtScoreFindLeaf>:
    a5c0:	55                   	push   rbp
    a5c1:	48 89 e5             	mov    rbp,rsp
    a5c4:	41 57                	push   r15
    a5c6:	41 56                	push   r14
    a5c8:	41 55                	push   r13
    a5ca:	41 54                	push   r12
    a5cc:	53                   	push   rbx
    a5cd:	48 83 ec 18          	sub    rsp,0x18
    a5d1:	48 89 55 d0          	mov    QWORD PTR [rbp-0x30],rdx
    a5d5:	48 89 75 c8          	mov    QWORD PTR [rbp-0x38],rsi
    a5d9:	f2 0f 11 45 c0       	movsd  QWORD PTR [rbp-0x40],xmm0
    a5de:	48 85 ff             	test   rdi,rdi
    a5e1:	0f 84 73 01 00 00    	je     a75a <zbtScoreFindLeaf+0x19a>
    a5e7:	48 89 fb             	mov    rbx,rdi
    a5ea:	eb 13                	jmp    a5ff <zbtScoreFindLeaf+0x3f>
    a5ec:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a5f1:	48 01 c1             	add    rcx,rax
    a5f4:	49 89 cc             	mov    r12,rcx
    a5f7:	44 89 e0             	mov    eax,r12d
    a5fa:	48 8b 5c c3 18       	mov    rbx,QWORD PTR [rbx+rax*8+0x18]
    a5ff:	80 7b 12 00          	cmp    BYTE PTR [rbx+0x12],0x0
    a603:	0f 85 53 01 00 00    	jne    a75c <zbtScoreFindLeaf+0x19c>
    a609:	0f b6 43 11          	movzx  eax,BYTE PTR [rbx+0x11]
    a60d:	41 bc ff ff ff ff    	mov    r12d,0xffffffff
    a613:	84 c0                	test   al,al
    a615:	74 e0                	je     a5f7 <zbtScoreFindLeaf+0x37>
    a617:	45 31 e4             	xor    r12d,r12d
    a61a:	eb 0f                	jmp    a62b <zbtScoreFindLeaf+0x6b>
    a61c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    a620:	49 ff c4             	inc    r12
    a623:	0f b6 c8             	movzx  ecx,al
    a626:	49 39 cc             	cmp    r12,rcx
    a629:	73 c1                	jae    a5ec <zbtScoreFindLeaf+0x2c>
    a62b:	f2 42 0f 10 84 e3 18 	movsd  xmm0,QWORD PTR [rbx+r12*8+0x218]
    a632:	02 00 00
    a635:	66 0f 2e 45 c0       	ucomisd xmm0,QWORD PTR [rbp-0x40]
    a63a:	77 bb                	ja     a5f7 <zbtScoreFindLeaf+0x37>
    a63c:	75 e2                	jne    a620 <zbtScoreFindLeaf+0x60>
    a63e:	7a e0                	jp     a620 <zbtScoreFindLeaf+0x60>
    a640:	4a 8b 44 e3 18       	mov    rax,QWORD PTR [rbx+r12*8+0x18]
    a645:	80 78 12 00          	cmp    BYTE PTR [rax+0x12],0x0
    a649:	75 14                	jne    a65f <zbtScoreFindLeaf+0x9f>
    a64b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    a650:	0f b6 48 11          	movzx  ecx,BYTE PTR [rax+0x11]
    a654:	48 8b 44 c8 10       	mov    rax,QWORD PTR [rax+rcx*8+0x10]
    a659:	80 78 12 00          	cmp    BYTE PTR [rax+0x12],0x0
    a65d:	74 f1                	je     a650 <zbtScoreFindLeaf+0x90>
    a65f:	0f b6 50 11          	movzx  edx,BYTE PTR [rax+0x11]
    a663:	0f b6 48 34          	movzx  ecx,BYTE PTR [rax+0x34]
    a667:	48 85 c9             	test   rcx,rcx
    a66a:	74 14                	je     a680 <zbtScoreFindLeaf+0xc0>
    a66c:	0f af ca             	imul   ecx,edx
    a66f:	83 c1 07             	add    ecx,0x7
    a672:	c1 e9 03             	shr    ecx,0x3
    a675:	83 c1 09             	add    ecx,0x9
    a678:	83 e1 fe             	and    ecx,0xfffffffe
    a67b:	eb 05                	jmp    a682 <zbtScoreFindLeaf+0xc2>
    a67d:	0f 1f 00             	nop    DWORD PTR [rax]
    a680:	31 c9                	xor    ecx,ecx
    a682:	be ff ff ff ff       	mov    esi,0xffffffff
    a687:	48 01 f2             	add    rdx,rsi
    a68a:	48 01 c1             	add    rcx,rax
    a68d:	80 78 35 00          	cmp    BYTE PTR [rax+0x35],0x0
    a691:	89 d2                	mov    edx,edx
    a693:	be 00 00 00 00       	mov    esi,0x0
    a698:	48 0f 45 d6          	cmovne rdx,rsi
    a69c:	0f b7 4c 51 38       	movzx  ecx,WORD PTR [rcx+rdx*2+0x38]
    a6a1:	4c 8d 2c 08          	lea    r13,[rax+rcx*1]
    a6a5:	44 0f b6 34 08       	movzx  r14d,BYTE PTR [rax+rcx*1]
    a6aa:	49 81 fe fd 00 00 00 	cmp    r14,0xfd
    a6b1:	77 0d                	ja     a6c0 <zbtScoreFindLeaf+0x100>
    a6b3:	49 ff c5             	inc    r13
    a6b6:	4d 89 ef             	mov    r15,r13
    a6b9:	eb 60                	jmp    a71b <zbtScoreFindLeaf+0x15b>
    a6bb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    a6c0:	41 81 fe fe 00 00 00 	cmp    r14d,0xfe
    a6c7:	75 0e                	jne    a6d7 <zbtScoreFindLeaf+0x117>
    a6c9:	45 0f b7 75 01       	movzx  r14d,WORD PTR [r13+0x1]
    a6ce:	49 83 c5 03          	add    r13,0x3
    a6d2:	4d 89 ef             	mov    r15,r13
    a6d5:	eb 44                	jmp    a71b <zbtScoreFindLeaf+0x15b>
    a6d7:	4d 8b 7d 0d          	mov    r15,QWORD PTR [r13+0xd]
    a6db:	4d 85 ff             	test   r15,r15
    a6de:	75 37                	jne    a717 <zbtScoreFindLeaf+0x157>
    a6e0:	48 8d 3d 37 8f 00 00 	lea    rdi,[rip+0x8f37]        # 1361e <_IO_stdin_used+0x61e>
    a6e7:	be 57 02 00 00       	mov    esi,0x257
    a6ec:	48 8d 15 57 90 00 00 	lea    rdx,[rip+0x9057]        # 1374a <_IO_stdin_used+0x74a>
    a6f3:	e8 a8 6f 00 00       	call   116a0 <standalone_panic>
    a6f8:	41 80 7d 00 ff       	cmp    BYTE PTR [r13+0x0],0xff
    a6fd:	74 18                	je     a717 <zbtScoreFindLeaf+0x157>
    a6ff:	48 8d 3d 18 8f 00 00 	lea    rdi,[rip+0x8f18]        # 1361e <_IO_stdin_used+0x61e>
    a706:	be 37 02 00 00       	mov    esi,0x237
    a70b:	48 8d 15 44 90 00 00 	lea    rdx,[rip+0x9044]        # 13756 <_IO_stdin_used+0x756>
    a712:	e8 89 6f 00 00       	call   116a0 <standalone_panic>
    a717:	4d 8b 75 05          	mov    r14,QWORD PTR [r13+0x5]
    a71b:	48 8b 45 d0          	mov    rax,QWORD PTR [rbp-0x30]
    a71f:	4c 39 f0             	cmp    rax,r14
    a722:	4c 89 f2             	mov    rdx,r14
    a725:	48 0f 42 d0          	cmovb  rdx,rax
    a729:	48 8b 7d c8          	mov    rdi,QWORD PTR [rbp-0x38]
    a72d:	4c 89 fe             	mov    rsi,r15
    a730:	e8 ab 69 ff ff       	call   10e0 <memcmp@plt>
    a735:	85 c0                	test   eax,eax
    a737:	75 10                	jne    a749 <zbtScoreFindLeaf+0x189>
    a739:	4c 3b 75 d0          	cmp    r14,QWORD PTR [rbp-0x30]
    a73d:	0f 87 b4 fe ff ff    	ja     a5f7 <zbtScoreFindLeaf+0x37>
    a743:	0f 92 c0             	setb   al
    a746:	0f b6 c0             	movzx  eax,al
    a749:	85 c0                	test   eax,eax
    a74b:	0f 8e a6 fe ff ff    	jle    a5f7 <zbtScoreFindLeaf+0x37>
    a751:	0f b6 43 11          	movzx  eax,BYTE PTR [rbx+0x11]
    a755:	e9 c6 fe ff ff       	jmp    a620 <zbtScoreFindLeaf+0x60>
    a75a:	31 db                	xor    ebx,ebx
    a75c:	48 89 d8             	mov    rax,rbx
    a75f:	48 83 c4 18          	add    rsp,0x18
    a763:	5b                   	pop    rbx
    a764:	41 5c                	pop    r12
    a766:	41 5d                	pop    r13
    a768:	41 5e                	pop    r14
    a76a:	41 5f                	pop    r15
    a76c:	5d                   	pop    rbp
    a76d:	c3                   	ret

Disassembly of section .fini:
