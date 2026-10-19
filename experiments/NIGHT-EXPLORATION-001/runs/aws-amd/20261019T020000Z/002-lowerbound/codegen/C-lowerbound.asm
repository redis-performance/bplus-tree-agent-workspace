
scratch/amd-lowerbound-build/C/build/native/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

000000000000a770 <zbtScoreLeafLowerBound>:
    a770:	55                   	push   rbp
    a771:	48 89 e5             	mov    rbp,rsp
    a774:	41 57                	push   r15
    a776:	41 56                	push   r14
    a778:	41 55                	push   r13
    a77a:	41 54                	push   r12
    a77c:	53                   	push   rbx
    a77d:	48 83 ec 28          	sub    rsp,0x28
    a781:	48 89 75 b0          	mov    QWORD PTR [rbp-0x50],rsi
    a785:	44 0f b6 4f 11       	movzx  r9d,BYTE PTR [rdi+0x11]
    a78a:	45 85 c9             	test   r9d,r9d
    a78d:	0f 84 59 02 00 00    	je     a9ec <zbtScoreLeafLowerBound+0x27c>
    a793:	49 89 d4             	mov    r12,rdx
    a796:	49 89 ff             	mov    r15,rdi
    a799:	4c 8d 57 38          	lea    r10,[rdi+0x38]
    a79d:	45 31 ed             	xor    r13d,r13d
    a7a0:	49 bb ff ff ff ff ff 	movabs r11,0x7fffffffffffffff
    a7a7:	ff ff 7f 
    a7aa:	48 c7 c3 ff ff ff ff 	mov    rbx,0xffffffffffffffff
    a7b1:	f2 0f 11 45 c0       	movsd  QWORD PTR [rbp-0x40],xmm0
    a7b6:	48 89 55 b8          	mov    QWORD PTR [rbp-0x48],rdx
    a7ba:	4c 89 55 c8          	mov    QWORD PTR [rbp-0x38],r10
    a7be:	eb 0f                	jmp    a7cf <zbtScoreLeafLowerBound+0x5f>
    a7c0:	41 ff c6             	inc    r14d
    a7c3:	45 89 f5             	mov    r13d,r14d
    a7c6:	45 39 cd             	cmp    r13d,r9d
    a7c9:	0f 83 20 02 00 00    	jae    a9ef <zbtScoreLeafLowerBound+0x27f>
    a7cf:	45 89 ce             	mov    r14d,r9d
    a7d2:	45 29 ee             	sub    r14d,r13d
    a7d5:	41 d1 ee             	shr    r14d,1
    a7d8:	45 01 ee             	add    r14d,r13d
    a7db:	41 0f b6 47 34       	movzx  eax,BYTE PTR [r15+0x34]
    a7e0:	41 0f b6 57 35       	movzx  edx,BYTE PTR [r15+0x35]
    a7e5:	85 c0                	test   eax,eax
    a7e7:	74 77                	je     a860 <zbtScoreLeafLowerBound+0xf0>
    a7e9:	44 89 f1             	mov    ecx,r14d
    a7ec:	84 d2                	test   dl,dl
    a7ee:	74 0c                	je     a7fc <zbtScoreLeafLowerBound+0x8c>
    a7f0:	41 0f b6 77 11       	movzx  esi,BYTE PTR [r15+0x11]
    a7f5:	44 89 f1             	mov    ecx,r14d
    a7f8:	f7 d1                	not    ecx
    a7fa:	01 f1                	add    ecx,esi
    a7fc:	41 89 c8             	mov    r8d,ecx
    a7ff:	4c 0f af c0          	imul   r8,rax
    a803:	4c 89 c7             	mov    rdi,r8
    a806:	48 c1 ef 03          	shr    rdi,0x3
    a80a:	49 8b 34 3a          	mov    rsi,QWORD PTR [r10+rdi*1]
    a80e:	44 89 c1             	mov    ecx,r8d
    a811:	80 e1 07             	and    cl,0x7
    a814:	48 d3 ee             	shr    rsi,cl
    a817:	41 83 e0 07          	and    r8d,0x7
    a81b:	74 18                	je     a835 <zbtScoreLeafLowerBound+0xc5>
    a81d:	b9 40 00 00 00       	mov    ecx,0x40
    a822:	44 29 c1             	sub    ecx,r8d
    a825:	39 c1                	cmp    ecx,eax
    a827:	73 0c                	jae    a835 <zbtScoreLeafLowerBound+0xc5>
    a829:	42 0f b6 7c 3f 40    	movzx  edi,BYTE PTR [rdi+r15*1+0x40]
    a82f:	48 d3 e7             	shl    rdi,cl
    a832:	48 09 fe             	or     rsi,rdi
    a835:	48 c7 c7 ff ff ff ff 	mov    rdi,0xffffffffffffffff
    a83c:	89 c1                	mov    ecx,eax
    a83e:	48 d3 e7             	shl    rdi,cl
    a841:	3c 40                	cmp    al,0x40
    a843:	48 f7 d7             	not    rdi
    a846:	48 0f 43 fb          	cmovae rdi,rbx
    a84a:	48 21 f7             	and    rdi,rsi
    a84d:	41 0f b6 4f 13       	movzx  ecx,BYTE PTR [r15+0x13]
    a852:	48 d3 e7             	shl    rdi,cl
    a855:	eb 0b                	jmp    a862 <zbtScoreLeafLowerBound+0xf2>
    a857:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    a85e:	00 00 
    a860:	31 ff                	xor    edi,edi
    a862:	48 89 f9             	mov    rcx,rdi
    a865:	48 f7 d9             	neg    rcx
    a868:	84 d2                	test   dl,dl
    a86a:	48 0f 44 cf          	cmove  rcx,rdi
    a86e:	49 03 4f 28          	add    rcx,QWORD PTR [r15+0x28]
    a872:	48 89 ce             	mov    rsi,rcx
    a875:	4c 21 de             	and    rsi,r11
    a878:	48 85 c9             	test   rcx,rcx
    a87b:	48 f7 d1             	not    rcx
    a87e:	48 0f 48 ce          	cmovs  rcx,rsi
    a882:	66 48 0f 6e c9       	movq   xmm1,rcx
    a887:	66 0f 2e c1          	ucomisd xmm0,xmm1
    a88b:	0f 87 2f ff ff ff    	ja     a7c0 <zbtScoreLeafLowerBound+0x50>
    a891:	66 0f 2e c8          	ucomisd xmm1,xmm0
    a895:	76 09                	jbe    a8a0 <zbtScoreLeafLowerBound+0x130>
    a897:	45 89 f1             	mov    r9d,r14d
    a89a:	e9 27 ff ff ff       	jmp    a7c6 <zbtScoreLeafLowerBound+0x56>
    a89f:	90                   	nop
    a8a0:	48 85 c0             	test   rax,rax
    a8a3:	0f 84 c9 00 00 00    	je     a972 <zbtScoreLeafLowerBound+0x202>
    a8a9:	41 0f b6 4f 11       	movzx  ecx,BYTE PTR [r15+0x11]
    a8ae:	0f af c8             	imul   ecx,eax
    a8b1:	83 c1 07             	add    ecx,0x7
    a8b4:	c1 e9 03             	shr    ecx,0x3
    a8b7:	83 c1 09             	add    ecx,0x9
    a8ba:	83 e1 fe             	and    ecx,0xfffffffe
    a8bd:	44 89 4d d4          	mov    DWORD PTR [rbp-0x2c],r9d
    a8c1:	44 89 f0             	mov    eax,r14d
    a8c4:	84 d2                	test   dl,dl
    a8c6:	74 0c                	je     a8d4 <zbtScoreLeafLowerBound+0x164>
    a8c8:	41 0f b6 57 11       	movzx  edx,BYTE PTR [r15+0x11]
    a8cd:	44 89 f0             	mov    eax,r14d
    a8d0:	f7 d0                	not    eax
    a8d2:	01 d0                	add    eax,edx
    a8d4:	4c 01 d1             	add    rcx,r10
    a8d7:	89 c0                	mov    eax,eax
    a8d9:	0f b7 04 41          	movzx  eax,WORD PTR [rcx+rax*2]
    a8dd:	4d 8d 24 07          	lea    r12,[r15+rax*1]
    a8e1:	41 0f b6 1c 07       	movzx  ebx,BYTE PTR [r15+rax*1]
    a8e6:	48 81 fb fd 00 00 00 	cmp    rbx,0xfd
    a8ed:	77 05                	ja     a8f4 <zbtScoreLeafLowerBound+0x184>
    a8ef:	49 ff c4             	inc    r12
    a8f2:	eb 16                	jmp    a90a <zbtScoreLeafLowerBound+0x19a>
    a8f4:	81 fb fe 00 00 00    	cmp    ebx,0xfe
    a8fa:	0f 85 88 00 00 00    	jne    a988 <zbtScoreLeafLowerBound+0x218>
    a900:	41 0f b7 5c 24 01    	movzx  ebx,WORD PTR [r12+0x1]
    a906:	49 83 c4 03          	add    r12,0x3
    a90a:	4c 89 e7             	mov    rdi,r12
    a90d:	48 89 da             	mov    rdx,rbx
    a910:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    a914:	4c 39 e3             	cmp    rbx,r12
    a917:	72 03                	jb     a91c <zbtScoreLeafLowerBound+0x1ac>
    a919:	4c 89 e2             	mov    rdx,r12
    a91c:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    a920:	e8 bb 67 ff ff       	call   10e0 <memcmp@plt>
    a925:	85 c0                	test   eax,eax
    a927:	75 17                	jne    a940 <zbtScoreLeafLowerBound+0x1d0>
    a929:	b8 ff ff ff ff       	mov    eax,0xffffffff
    a92e:	4c 39 e3             	cmp    rbx,r12
    a931:	72 0d                	jb     a940 <zbtScoreLeafLowerBound+0x1d0>
    a933:	0f 97 c0             	seta   al
    a936:	0f b6 c0             	movzx  eax,al
    a939:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    a940:	85 c0                	test   eax,eax
    a942:	f2 0f 10 45 c0       	movsd  xmm0,QWORD PTR [rbp-0x40]
    a947:	78 05                	js     a94e <zbtScoreLeafLowerBound+0x1de>
    a949:	45 89 f1             	mov    r9d,r14d
    a94c:	eb 0a                	jmp    a958 <zbtScoreLeafLowerBound+0x1e8>
    a94e:	41 ff c6             	inc    r14d
    a951:	45 89 f5             	mov    r13d,r14d
    a954:	44 8b 4d d4          	mov    r9d,DWORD PTR [rbp-0x2c]
    a958:	4c 8b 55 c8          	mov    r10,QWORD PTR [rbp-0x38]
    a95c:	49 bb ff ff ff ff ff 	movabs r11,0x7fffffffffffffff
    a963:	ff ff 7f 
    a966:	48 c7 c3 ff ff ff ff 	mov    rbx,0xffffffffffffffff
    a96d:	e9 54 fe ff ff       	jmp    a7c6 <zbtScoreLeafLowerBound+0x56>
    a972:	31 c9                	xor    ecx,ecx
    a974:	44 89 4d d4          	mov    DWORD PTR [rbp-0x2c],r9d
    a978:	44 89 f0             	mov    eax,r14d
    a97b:	84 d2                	test   dl,dl
    a97d:	0f 85 45 ff ff ff    	jne    a8c8 <zbtScoreLeafLowerBound+0x158>
    a983:	e9 4c ff ff ff       	jmp    a8d4 <zbtScoreLeafLowerBound+0x164>
    a988:	49 8b 7c 24 0d       	mov    rdi,QWORD PTR [r12+0xd]
    a98d:	48 85 ff             	test   rdi,rdi
    a990:	75 40                	jne    a9d2 <zbtScoreLeafLowerBound+0x262>
    a992:	48 89 fb             	mov    rbx,rdi
    a995:	48 8d 3d 82 8c 00 00 	lea    rdi,[rip+0x8c82]        # 1361e <_IO_stdin_used+0x61e>
    a99c:	be 57 02 00 00       	mov    esi,0x257
    a9a1:	48 8d 15 a2 8d 00 00 	lea    rdx,[rip+0x8da2]        # 1374a <_IO_stdin_used+0x74a>
    a9a8:	e8 c3 6c 00 00       	call   11670 <standalone_panic>
    a9ad:	48 89 df             	mov    rdi,rbx
    a9b0:	41 80 3c 24 ff       	cmp    BYTE PTR [r12],0xff
    a9b5:	74 1b                	je     a9d2 <zbtScoreLeafLowerBound+0x262>
    a9b7:	48 8d 3d 60 8c 00 00 	lea    rdi,[rip+0x8c60]        # 1361e <_IO_stdin_used+0x61e>
    a9be:	be 37 02 00 00       	mov    esi,0x237
    a9c3:	48 8d 15 8c 8d 00 00 	lea    rdx,[rip+0x8d8c]        # 13756 <_IO_stdin_used+0x756>
    a9ca:	e8 a1 6c 00 00       	call   11670 <standalone_panic>
    a9cf:	48 89 df             	mov    rdi,rbx
    a9d2:	49 8b 5c 24 05       	mov    rbx,QWORD PTR [r12+0x5]
    a9d7:	48 89 da             	mov    rdx,rbx
    a9da:	4c 8b 65 b8          	mov    r12,QWORD PTR [rbp-0x48]
    a9de:	4c 39 e3             	cmp    rbx,r12
    a9e1:	0f 83 32 ff ff ff    	jae    a919 <zbtScoreLeafLowerBound+0x1a9>
    a9e7:	e9 30 ff ff ff       	jmp    a91c <zbtScoreLeafLowerBound+0x1ac>
    a9ec:	45 31 ed             	xor    r13d,r13d
    a9ef:	44 89 e8             	mov    eax,r13d
    a9f2:	48 83 c4 28          	add    rsp,0x28
    a9f6:	5b                   	pop    rbx
    a9f7:	41 5c                	pop    r12
    a9f9:	41 5d                	pop    r13
    a9fb:	41 5e                	pop    r14
    a9fd:	41 5f                	pop    r15
    a9ff:	5d                   	pop    rbp
    aa00:	c3                   	ret

Disassembly of section .fini:
