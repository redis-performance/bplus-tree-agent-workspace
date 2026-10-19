
build/size-matrix/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000005790 <zbtreeRank>:
    5790:	55                   	push   rbp
    5791:	48 89 e5             	mov    rbp,rsp
    5794:	41 57                	push   r15
    5796:	41 56                	push   r14
    5798:	41 55                	push   r13
    579a:	41 54                	push   r12
    579c:	53                   	push   rbx
    579d:	48 83 ec 68          	sub    rsp,0x68
    57a1:	48 89 8d 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rcx
    57a8:	89 d3                	mov    ebx,edx
    57aa:	49 89 f6             	mov    r14,rsi
    57ad:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    57b1:	0f b6 76 ff          	movzx  esi,BYTE PTR [rsi-0x1]
    57b5:	89 f0                	mov    eax,esi
    57b7:	83 e0 07             	and    eax,0x7
    57ba:	83 f8 04             	cmp    eax,0x4
    57bd:	77 2f                	ja     57ee <zbtreeRank+0x5e>
    57bf:	48 8d 0d d6 e4 00 00 	lea    rcx,[rip+0xe4d6]        # 13c9c <_IO_stdin_used+0xc9c>
    57c6:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    57ca:	48 01 c8             	add    rax,rcx
    57cd:	ff e0                	jmp    rax
    57cf:	c1 ee 03             	shr    esi,0x3
    57d2:	eb 1c                	jmp    57f0 <zbtreeRank+0x60>
    57d4:	49 8b 76 ef          	mov    rsi,QWORD PTR [r14-0x11]
    57d8:	eb 16                	jmp    57f0 <zbtreeRank+0x60>
    57da:	41 0f b7 76 fb       	movzx  esi,WORD PTR [r14-0x5]
    57df:	eb 0f                	jmp    57f0 <zbtreeRank+0x60>
    57e1:	41 8b 76 f7          	mov    esi,DWORD PTR [r14-0x9]
    57e5:	eb 09                	jmp    57f0 <zbtreeRank+0x60>
    57e7:	41 0f b6 76 fd       	movzx  esi,BYTE PTR [r14-0x3]
    57ec:	eb 02                	jmp    57f0 <zbtreeRank+0x60>
    57ee:	31 f6                	xor    esi,esi
    57f0:	4c 89 f7             	mov    rdi,r14
    57f3:	e8 e8 c0 00 00       	call   118e0 <dictGenHashFunction>
    57f8:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    57fc:	41 0f b6 46 ff       	movzx  eax,BYTE PTR [r14-0x1]
    5801:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    5805:	83 e0 07             	and    eax,0x7
    5808:	83 f8 04             	cmp    eax,0x4
    580b:	89 5d c4             	mov    DWORD PTR [rbp-0x3c],ebx
    580e:	4c 89 b5 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],r14
    5815:	77 7d                	ja     5894 <zbtreeRank+0x104>
    5817:	48 8d 0d 92 e4 00 00 	lea    rcx,[rip+0xe492]        # 13cb0 <_IO_stdin_used+0xcb0>
    581e:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    5822:	48 01 c8             	add    rax,rcx
    5825:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5829:	ff e0                	jmp    rax
    582b:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    582f:	c1 e8 03             	shr    eax,0x3
    5832:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    5836:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    583b:	75 6c                	jne    58a9 <zbtreeRank+0x119>
    583d:	e9 5d 03 00 00       	jmp    5b9f <zbtreeRank+0x40f>
    5842:	49 8b 46 ef          	mov    rax,QWORD PTR [r14-0x11]
    5846:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    584a:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    584f:	75 58                	jne    58a9 <zbtreeRank+0x119>
    5851:	e9 49 03 00 00       	jmp    5b9f <zbtreeRank+0x40f>
    5856:	41 0f b7 46 fb       	movzx  eax,WORD PTR [r14-0x5]
    585b:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    585f:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    5864:	75 43                	jne    58a9 <zbtreeRank+0x119>
    5866:	e9 34 03 00 00       	jmp    5b9f <zbtreeRank+0x40f>
    586b:	41 8b 46 f7          	mov    eax,DWORD PTR [r14-0x9]
    586f:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    5873:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    5878:	75 2f                	jne    58a9 <zbtreeRank+0x119>
    587a:	e9 20 03 00 00       	jmp    5b9f <zbtreeRank+0x40f>
    587f:	41 0f b6 46 fd       	movzx  eax,BYTE PTR [r14-0x3]
    5884:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    5888:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    588d:	75 1a                	jne    58a9 <zbtreeRank+0x119>
    588f:	e9 0b 03 00 00       	jmp    5b9f <zbtreeRank+0x40f>
    5894:	31 c0                	xor    eax,eax
    5896:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    589a:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    589e:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    58a3:	0f 84 f6 02 00 00    	je     5b9f <zbtreeRank+0x40f>
    58a9:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    58ad:	be 01 00 00 00       	mov    esi,0x1
    58b2:	e8 19 23 00 00       	call   7bd0 <zbtIndexRehashStep>
    58b7:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    58bb:	4c 8b 77 40          	mov    r14,QWORD PTR [rdi+0x40]
    58bf:	4d 85 f6             	test   r14,r14
    58c2:	0f 84 d7 02 00 00    	je     5b9f <zbtreeRank+0x40f>
    58c8:	49 8b 46 08          	mov    rax,QWORD PTR [r14+0x8]
    58cc:	48 85 c0             	test   rax,rax
    58cf:	0f 84 ca 02 00 00    	je     5b9f <zbtreeRank+0x40f>
    58d5:	48 89 c2             	mov    rdx,rax
    58d8:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    58dc:	89 c8                	mov    eax,ecx
    58de:	c1 e8 18             	shr    eax,0x18
    58e1:	81 f9 00 00 00 01    	cmp    ecx,0x1000000
    58e7:	41 bd 01 00 00 00    	mov    r13d,0x1
    58ed:	44 0f 43 e8          	cmovae r13d,eax
    58f1:	48 ff ca             	dec    rdx
    58f4:	89 c8                	mov    eax,ecx
    58f6:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    58fa:	48 89 55 a0          	mov    QWORD PTR [rbp-0x60],rdx
    58fe:	89 d6                	mov    esi,edx
    5900:	21 ce                	and    esi,ecx
    5902:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    5909:	01 01 01
    590c:	49 0f af c5          	imul   rax,r13
    5910:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
    5914:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    591b:	79 37 9e
    591e:	49 0f af c5          	imul   rax,r13
    5922:	48 89 c1             	mov    rcx,rax
    5925:	48 c1 e9 3a          	shr    rcx,0x3a
    5929:	ba 01 00 00 00       	mov    edx,0x1
    592e:	48 d3 e2             	shl    rdx,cl
    5931:	4c 0f ab ea          	bts    rdx,r13
    5935:	48 c1 e8 24          	shr    rax,0x24
    5939:	48 0f ab c2          	bts    rdx,rax
    593d:	48 89 55 b0          	mov    QWORD PTR [rbp-0x50],rdx
    5941:	48 8d 47 18          	lea    rax,[rdi+0x18]
    5945:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    5949:	45 31 c0             	xor    r8d,r8d
    594c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    5950:	4c 89 45 90          	mov    QWORD PTR [rbp-0x70],r8
    5954:	49 8b 06             	mov    rax,QWORD PTR [r14]
    5957:	31 c9                	xor    ecx,ecx
    5959:	41 83 7e 20 00       	cmp    DWORD PTR [r14+0x20],0x0
    595e:	0f 95 c1             	setne  cl
    5961:	c1 e1 04             	shl    ecx,0x4
    5964:	48 83 c9 20          	or     rcx,0x20
    5968:	48 89 75 88          	mov    QWORD PTR [rbp-0x78],rsi
    596c:	48 0f af ce          	imul   rcx,rsi
    5970:	4c 8d 3c 08          	lea    r15,[rax+rcx*1]
    5974:	48 8b 1c 08          	mov    rbx,QWORD PTR [rax+rcx*1]
    5978:	48 33 5d 98          	xor    rbx,QWORD PTR [rbp-0x68]
    597c:	48 89 d8             	mov    rax,rbx
    597f:	48 f7 d0             	not    rax
    5982:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    5989:	80 80 80
    598c:	48 21 c8             	and    rax,rcx
    598f:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    5996:	fe fe fe
    5999:	48 01 cb             	add    rbx,rcx
    599c:	48 21 c3             	and    rbx,rax
    599f:	75 4c                	jne    59ed <zbtreeRank+0x25d>
    59a1:	e9 3a 01 00 00       	jmp    5ae0 <zbtreeRank+0x350>
    59a6:	4c 89 e7             	mov    rdi,r12
    59a9:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    59ad:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    59b4:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    59b8:	4c 8b 85 70 ff ff ff 	mov    r8,QWORD PTR [rbp-0x90]
    59bf:	4c 8d 4d c0          	lea    r9,[rbp-0x40]
    59c3:	e8 e8 62 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    59c8:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    59cc:	85 c0                	test   eax,eax
    59ce:	0f 85 c6 04 00 00    	jne    5e9a <zbtreeRank+0x70a>
    59d4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    59db:	00 00 00 00 00
    59e0:	48 8d 43 ff          	lea    rax,[rbx-0x1]
    59e4:	48 21 c3             	and    rbx,rax
    59e7:	0f 84 f3 00 00 00    	je     5ae0 <zbtreeRank+0x350>
    59ed:	f3 48 0f bc c3       	tzcnt  rax,rbx
    59f2:	49 8b 17             	mov    rdx,QWORD PTR [r15]
    59f5:	89 c1                	mov    ecx,eax
    59f7:	80 e1 38             	and    cl,0x38
    59fa:	48 d3 ea             	shr    rdx,cl
    59fd:	41 38 d5             	cmp    r13b,dl
    5a00:	75 de                	jne    59e0 <zbtreeRank+0x250>
    5a02:	c1 e8 03             	shr    eax,0x3
    5a05:	41 83 7e 20 00       	cmp    DWORD PTR [r14+0x20],0x0
    5a0a:	74 0c                	je     5a18 <zbtreeRank+0x288>
    5a0c:	41 8b 44 87 10       	mov    eax,DWORD PTR [r15+rax*4+0x10]
    5a11:	83 f8 ff             	cmp    eax,0xffffffff
    5a14:	75 0f                	jne    5a25 <zbtreeRank+0x295>
    5a16:	eb c8                	jmp    59e0 <zbtreeRank+0x250>
    5a18:	41 0f b7 44 47 10    	movzx  eax,WORD PTR [r15+rax*2+0x10]
    5a1e:	3d ff ff 00 00       	cmp    eax,0xffff
    5a23:	74 bb                	je     59e0 <zbtreeRank+0x250>
    5a25:	3b 47 54             	cmp    eax,DWORD PTR [rdi+0x54]
    5a28:	73 76                	jae    5aa0 <zbtreeRank+0x310>
    5a2a:	48 8b 4f 48          	mov    rcx,QWORD PTR [rdi+0x48]
    5a2e:	89 c2                	mov    edx,eax
    5a30:	4c 8b 24 d1          	mov    r12,QWORD PTR [rcx+rdx*8]
    5a34:	4d 85 e4             	test   r12,r12
    5a37:	74 67                	je     5aa0 <zbtreeRank+0x310>
    5a39:	44 89 e1             	mov    ecx,r12d
    5a3c:	83 e1 01             	and    ecx,0x1
    5a3f:	75 5f                	jne    5aa0 <zbtreeRank+0x310>
    5a41:	41 39 44 24 30       	cmp    DWORD PTR [r12+0x30],eax
    5a46:	74 1c                	je     5a64 <zbtreeRank+0x2d4>
    5a48:	48 8d 3d cf db 00 00 	lea    rdi,[rip+0xdbcf]        # 1361e <_IO_stdin_used+0x61e>
    5a4f:	be a5 07 00 00       	mov    esi,0x7a5
    5a54:	48 8d 15 1c dd 00 00 	lea    rdx,[rip+0xdd1c]        # 13777 <_IO_stdin_used+0x777>
    5a5b:	e8 40 bc 00 00       	call   116a0 <standalone_panic>
    5a60:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5a64:	48 8b 47 40          	mov    rax,QWORD PTR [rdi+0x40]
    5a68:	48 85 c0             	test   rax,rax
    5a6b:	0f 84 35 ff ff ff    	je     59a6 <zbtreeRank+0x216>
    5a71:	4c 39 f0             	cmp    rax,r14
    5a74:	0f 94 c1             	sete   cl
    5a77:	41 0f b7 54 24 16    	movzx  edx,WORD PTR [r12+0x16]
    5a7d:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    5a81:	0f 95 c0             	setne  al
    5a84:	38 c1                	cmp    cl,al
    5a86:	0f 85 1a ff ff ff    	jne    59a6 <zbtreeRank+0x216>
    5a8c:	e9 4f ff ff ff       	jmp    59e0 <zbtreeRank+0x250>
    5a91:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    5a98:	0f 1f 84 00 00 00 00
    5a9f:	00
    5aa0:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    5aa5:	74 0a                	je     5ab1 <zbtreeRank+0x321>
    5aa7:	4c 39 75 80          	cmp    QWORD PTR [rbp-0x80],r14
    5aab:	0f 84 2f ff ff ff    	je     59e0 <zbtreeRank+0x250>
    5ab1:	48 8d 3d 66 db 00 00 	lea    rdi,[rip+0xdb66]        # 1361e <_IO_stdin_used+0x61e>
    5ab8:	be a1 07 00 00       	mov    esi,0x7a1
    5abd:	48 8d 15 d2 dc 00 00 	lea    rdx,[rip+0xdcd2]        # 13796 <_IO_stdin_used+0x796>
    5ac4:	e8 d7 bb 00 00       	call   116a0 <standalone_panic>
    5ac9:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5acd:	48 8d 43 ff          	lea    rax,[rbx-0x1]
    5ad1:	48 21 c3             	and    rbx,rax
    5ad4:	0f 85 13 ff ff ff    	jne    59ed <zbtreeRank+0x25d>
    5ada:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    5ae0:	4c 8b 45 90          	mov    r8,QWORD PTR [rbp-0x70]
    5ae4:	4d 85 c0             	test   r8,r8
    5ae7:	48 8b 75 88          	mov    rsi,QWORD PTR [rbp-0x78]
    5aeb:	75 34                	jne    5b21 <zbtreeRank+0x391>
    5aed:	41 8b 46 08          	mov    eax,DWORD PTR [r14+0x8]
    5af1:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    5af6:	01 c8                	add    eax,ecx
    5af8:	23 45 a8             	and    eax,DWORD PTR [rbp-0x58]
    5afb:	31 c9                	xor    ecx,ecx
    5afd:	41 83 7e 20 00       	cmp    DWORD PTR [r14+0x20],0x0
    5b02:	49 8b 16             	mov    rdx,QWORD PTR [r14]
    5b05:	0f 95 c1             	setne  cl
    5b08:	c1 e1 04             	shl    ecx,0x4
    5b0b:	48 83 c9 20          	or     rcx,0x20
    5b0f:	48 0f af c8          	imul   rcx,rax
    5b13:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    5b18:	48 f7 d0             	not    rax
    5b1b:	48 85 45 b0          	test   QWORD PTR [rbp-0x50],rax
    5b1f:	75 7e                	jne    5b9f <zbtreeRank+0x40f>
    5b21:	49 8b 07             	mov    rax,QWORD PTR [r15]
    5b24:	84 c0                	test   al,al
    5b26:	74 77                	je     5b9f <zbtreeRank+0x40f>
    5b28:	89 c1                	mov    ecx,eax
    5b2a:	81 e1 00 ff 00 00    	and    ecx,0xff00
    5b30:	74 6d                	je     5b9f <zbtreeRank+0x40f>
    5b32:	89 c1                	mov    ecx,eax
    5b34:	81 e1 00 00 ff 00    	and    ecx,0xff0000
    5b3a:	74 63                	je     5b9f <zbtreeRank+0x40f>
    5b3c:	89 c1                	mov    ecx,eax
    5b3e:	81 e1 00 00 00 ff    	and    ecx,0xff000000
    5b44:	74 59                	je     5b9f <zbtreeRank+0x40f>
    5b46:	48 89 c1             	mov    rcx,rax
    5b49:	48 ba 00 00 00 00 ff 	movabs rdx,0xff00000000
    5b50:	00 00 00
    5b53:	48 21 d1             	and    rcx,rdx
    5b56:	74 47                	je     5b9f <zbtreeRank+0x40f>
    5b58:	48 89 c1             	mov    rcx,rax
    5b5b:	48 ba 00 00 00 00 00 	movabs rdx,0xff0000000000
    5b62:	ff 00 00
    5b65:	48 21 d1             	and    rcx,rdx
    5b68:	74 35                	je     5b9f <zbtreeRank+0x40f>
    5b6a:	48 89 c1             	mov    rcx,rax
    5b6d:	48 ba 00 00 00 00 00 	movabs rdx,0xff000000000000
    5b74:	00 ff 00
    5b77:	48 21 d1             	and    rcx,rdx
    5b7a:	74 23                	je     5b9f <zbtreeRank+0x40f>
    5b7c:	48 b9 00 00 00 00 00 	movabs rcx,0x100000000000000
    5b83:	00 00 01
    5b86:	48 39 c8             	cmp    rax,rcx
    5b89:	72 14                	jb     5b9f <zbtreeRank+0x40f>
    5b8b:	48 ff c6             	inc    rsi
    5b8e:	48 23 75 a0          	and    rsi,QWORD PTR [rbp-0x60]
    5b92:	49 ff c0             	inc    r8
    5b95:	4d 3b 46 08          	cmp    r8,QWORD PTR [r14+0x8]
    5b99:	0f 82 b1 fd ff ff    	jb     5950 <zbtreeRank+0x1c0>
    5b9f:	48 8b 77 20          	mov    rsi,QWORD PTR [rdi+0x20]
    5ba3:	49 c7 c7 ff ff ff ff 	mov    r15,0xffffffffffffffff
    5baa:	48 85 f6             	test   rsi,rsi
    5bad:	0f 84 c2 03 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5bb3:	48 8d 47 18          	lea    rax,[rdi+0x18]
    5bb7:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
    5bbb:	48 8b 55 b8          	mov    rdx,QWORD PTR [rbp-0x48]
    5bbf:	89 d0                	mov    eax,edx
    5bc1:	c1 e8 18             	shr    eax,0x18
    5bc4:	81 fa 00 00 00 01    	cmp    edx,0x1000000
    5bca:	41 bd 01 00 00 00    	mov    r13d,0x1
    5bd0:	44 0f 43 e8          	cmovae r13d,eax
    5bd4:	48 ff ce             	dec    rsi
    5bd7:	89 d0                	mov    eax,edx
    5bd9:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    5bdd:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    5be4:	79 37 9e
    5be7:	49 0f af c5          	imul   rax,r13
    5beb:	48 89 c1             	mov    rcx,rax
    5bee:	48 c1 e9 3a          	shr    rcx,0x3a
    5bf2:	41 b8 01 00 00 00    	mov    r8d,0x1
    5bf8:	49 d3 e0             	shl    r8,cl
    5bfb:	41 89 f1             	mov    r9d,esi
    5bfe:	41 21 d1             	and    r9d,edx
    5c01:	4d 0f ab e8          	bts    r8,r13
    5c05:	48 c1 e8 24          	shr    rax,0x24
    5c09:	49 0f ab c0          	bts    r8,rax
    5c0d:	4c 89 45 b0          	mov    QWORD PTR [rbp-0x50],r8
    5c11:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    5c18:	01 01 01
    5c1b:	49 0f af c5          	imul   rax,r13
    5c1f:	48 89 45 90          	mov    QWORD PTR [rbp-0x70],rax
    5c23:	45 31 c0             	xor    r8d,r8d
    5c26:	48 89 75 a0          	mov    QWORD PTR [rbp-0x60],rsi
    5c2a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    5c30:	4c 89 45 80          	mov    QWORD PTR [rbp-0x80],r8
    5c34:	48 8b 47 18          	mov    rax,QWORD PTR [rdi+0x18]
    5c38:	31 c9                	xor    ecx,ecx
    5c3a:	83 7f 38 00          	cmp    DWORD PTR [rdi+0x38],0x0
    5c3e:	0f 95 c1             	setne  cl
    5c41:	c1 e1 04             	shl    ecx,0x4
    5c44:	48 83 c9 20          	or     rcx,0x20
    5c48:	4c 89 4d 88          	mov    QWORD PTR [rbp-0x78],r9
    5c4c:	49 0f af c9          	imul   rcx,r9
    5c50:	48 8d 1c 08          	lea    rbx,[rax+rcx*1]
    5c54:	4c 8b 34 08          	mov    r14,QWORD PTR [rax+rcx*1]
    5c58:	4c 33 75 90          	xor    r14,QWORD PTR [rbp-0x70]
    5c5c:	4c 89 f0             	mov    rax,r14
    5c5f:	48 f7 d0             	not    rax
    5c62:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    5c69:	80 80 80
    5c6c:	48 21 c8             	and    rax,rcx
    5c6f:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    5c76:	fe fe fe
    5c79:	49 01 ce             	add    r14,rcx
    5c7c:	49 21 c6             	and    r14,rax
    5c7f:	75 2c                	jne    5cad <zbtreeRank+0x51d>
    5c81:	e9 2a 01 00 00       	jmp    5db0 <zbtreeRank+0x620>
    5c86:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    5c8d:	00 00 00
    5c90:	48 83 7f 40 00       	cmp    QWORD PTR [rdi+0x40],0x0
    5c95:	0f 84 de 00 00 00    	je     5d79 <zbtreeRank+0x5e9>
    5c9b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    5ca0:	49 8d 46 ff          	lea    rax,[r14-0x1]
    5ca4:	49 21 c6             	and    r14,rax
    5ca7:	0f 84 03 01 00 00    	je     5db0 <zbtreeRank+0x620>
    5cad:	f3 49 0f bc c6       	tzcnt  rax,r14
    5cb2:	48 8b 13             	mov    rdx,QWORD PTR [rbx]
    5cb5:	89 c1                	mov    ecx,eax
    5cb7:	80 e1 38             	and    cl,0x38
    5cba:	48 d3 ea             	shr    rdx,cl
    5cbd:	41 38 d5             	cmp    r13b,dl
    5cc0:	75 de                	jne    5ca0 <zbtreeRank+0x510>
    5cc2:	c1 e8 03             	shr    eax,0x3
    5cc5:	83 7f 38 00          	cmp    DWORD PTR [rdi+0x38],0x0
    5cc9:	74 0b                	je     5cd6 <zbtreeRank+0x546>
    5ccb:	8b 44 83 10          	mov    eax,DWORD PTR [rbx+rax*4+0x10]
    5ccf:	83 f8 ff             	cmp    eax,0xffffffff
    5cd2:	75 0e                	jne    5ce2 <zbtreeRank+0x552>
    5cd4:	eb ca                	jmp    5ca0 <zbtreeRank+0x510>
    5cd6:	0f b7 44 43 10       	movzx  eax,WORD PTR [rbx+rax*2+0x10]
    5cdb:	3d ff ff 00 00       	cmp    eax,0xffff
    5ce0:	74 be                	je     5ca0 <zbtreeRank+0x510>
    5ce2:	3b 47 54             	cmp    eax,DWORD PTR [rdi+0x54]
    5ce5:	73 a9                	jae    5c90 <zbtreeRank+0x500>
    5ce7:	48 8b 4f 48          	mov    rcx,QWORD PTR [rdi+0x48]
    5ceb:	89 c2                	mov    edx,eax
    5ced:	4c 8b 24 d1          	mov    r12,QWORD PTR [rcx+rdx*8]
    5cf1:	4d 85 e4             	test   r12,r12
    5cf4:	74 9a                	je     5c90 <zbtreeRank+0x500>
    5cf6:	44 89 e1             	mov    ecx,r12d
    5cf9:	83 e1 01             	and    ecx,0x1
    5cfc:	75 92                	jne    5c90 <zbtreeRank+0x500>
    5cfe:	41 39 44 24 30       	cmp    DWORD PTR [r12+0x30],eax
    5d03:	74 1c                	je     5d21 <zbtreeRank+0x591>
    5d05:	48 8d 3d 12 d9 00 00 	lea    rdi,[rip+0xd912]        # 1361e <_IO_stdin_used+0x61e>
    5d0c:	be a5 07 00 00       	mov    esi,0x7a5
    5d11:	48 8d 15 5f da 00 00 	lea    rdx,[rip+0xda5f]        # 13777 <_IO_stdin_used+0x777>
    5d18:	e8 83 b9 00 00       	call   116a0 <standalone_panic>
    5d1d:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5d21:	48 8b 47 40          	mov    rax,QWORD PTR [rdi+0x40]
    5d25:	48 85 c0             	test   rax,rax
    5d28:	74 1c                	je     5d46 <zbtreeRank+0x5b6>
    5d2a:	48 3b 45 98          	cmp    rax,QWORD PTR [rbp-0x68]
    5d2e:	0f 94 c1             	sete   cl
    5d31:	41 0f b7 54 24 16    	movzx  edx,WORD PTR [r12+0x16]
    5d37:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    5d3b:	0f 95 c0             	setne  al
    5d3e:	38 c1                	cmp    cl,al
    5d40:	0f 84 5a ff ff ff    	je     5ca0 <zbtreeRank+0x510>
    5d46:	4c 89 e7             	mov    rdi,r12
    5d49:	48 8b 75 b8          	mov    rsi,QWORD PTR [rbp-0x48]
    5d4d:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    5d54:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    5d58:	4c 8b 85 70 ff ff ff 	mov    r8,QWORD PTR [rbp-0x90]
    5d5f:	4c 8d 4d c0          	lea    r9,[rbp-0x40]
    5d63:	e8 48 5f 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    5d68:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5d6c:	85 c0                	test   eax,eax
    5d6e:	0f 84 2c ff ff ff    	je     5ca0 <zbtreeRank+0x510>
    5d74:	e9 21 01 00 00       	jmp    5e9a <zbtreeRank+0x70a>
    5d79:	48 8d 3d 9e d8 00 00 	lea    rdi,[rip+0xd89e]        # 1361e <_IO_stdin_used+0x61e>
    5d80:	be a1 07 00 00       	mov    esi,0x7a1
    5d85:	48 8d 15 0a da 00 00 	lea    rdx,[rip+0xda0a]        # 13796 <_IO_stdin_used+0x796>
    5d8c:	e8 0f b9 00 00       	call   116a0 <standalone_panic>
    5d91:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    5d95:	49 8d 46 ff          	lea    rax,[r14-0x1]
    5d99:	49 21 c6             	and    r14,rax
    5d9c:	0f 85 0b ff ff ff    	jne    5cad <zbtreeRank+0x51d>
    5da2:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    5da9:	1f 84 00 00 00 00 00
    5db0:	4c 8b 45 80          	mov    r8,QWORD PTR [rbp-0x80]
    5db4:	4d 85 c0             	test   r8,r8
    5db7:	75 37                	jne    5df0 <zbtreeRank+0x660>
    5db9:	8b 47 20             	mov    eax,DWORD PTR [rdi+0x20]
    5dbc:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    5dc1:	01 c8                	add    eax,ecx
    5dc3:	23 45 a8             	and    eax,DWORD PTR [rbp-0x58]
    5dc6:	31 c9                	xor    ecx,ecx
    5dc8:	83 7f 38 00          	cmp    DWORD PTR [rdi+0x38],0x0
    5dcc:	48 8b 57 18          	mov    rdx,QWORD PTR [rdi+0x18]
    5dd0:	0f 95 c1             	setne  cl
    5dd3:	c1 e1 04             	shl    ecx,0x4
    5dd6:	48 83 c9 20          	or     rcx,0x20
    5dda:	48 0f af c8          	imul   rcx,rax
    5dde:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    5de3:	48 f7 d0             	not    rax
    5de6:	48 85 45 b0          	test   QWORD PTR [rbp-0x50],rax
    5dea:	0f 85 85 01 00 00    	jne    5f75 <zbtreeRank+0x7e5>
    5df0:	48 8b 03             	mov    rax,QWORD PTR [rbx]
    5df3:	84 c0                	test   al,al
    5df5:	0f 84 7a 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5dfb:	89 c1                	mov    ecx,eax
    5dfd:	81 e1 00 ff 00 00    	and    ecx,0xff00
    5e03:	0f 84 6c 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e09:	89 c1                	mov    ecx,eax
    5e0b:	81 e1 00 00 ff 00    	and    ecx,0xff0000
    5e11:	0f 84 5e 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e17:	89 c1                	mov    ecx,eax
    5e19:	81 e1 00 00 00 ff    	and    ecx,0xff000000
    5e1f:	0f 84 50 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e25:	48 89 c1             	mov    rcx,rax
    5e28:	48 ba 00 00 00 00 ff 	movabs rdx,0xff00000000
    5e2f:	00 00 00
    5e32:	48 21 d1             	and    rcx,rdx
    5e35:	0f 84 3a 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e3b:	48 89 c1             	mov    rcx,rax
    5e3e:	48 ba 00 00 00 00 00 	movabs rdx,0xff0000000000
    5e45:	ff 00 00
    5e48:	48 21 d1             	and    rcx,rdx
    5e4b:	0f 84 24 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e51:	48 89 c1             	mov    rcx,rax
    5e54:	48 ba 00 00 00 00 00 	movabs rdx,0xff000000000000
    5e5b:	00 ff 00
    5e5e:	48 21 d1             	and    rcx,rdx
    5e61:	0f 84 0e 01 00 00    	je     5f75 <zbtreeRank+0x7e5>
    5e67:	48 b9 00 00 00 00 00 	movabs rcx,0x100000000000000
    5e6e:	00 00 01
    5e71:	48 39 c8             	cmp    rax,rcx
    5e74:	0f 82 fb 00 00 00    	jb     5f75 <zbtreeRank+0x7e5>
    5e7a:	4c 8b 4d 88          	mov    r9,QWORD PTR [rbp-0x78]
    5e7e:	49 ff c1             	inc    r9
    5e81:	48 8b 75 a0          	mov    rsi,QWORD PTR [rbp-0x60]
    5e85:	49 21 f1             	and    r9,rsi
    5e88:	49 ff c0             	inc    r8
    5e8b:	4c 3b 47 20          	cmp    r8,QWORD PTR [rdi+0x20]
    5e8f:	0f 82 9b fd ff ff    	jb     5c30 <zbtreeRank+0x4a0>
    5e95:	e9 db 00 00 00       	jmp    5f75 <zbtreeRank+0x7e5>
    5e9a:	44 8b 7d c0          	mov    r15d,DWORD PTR [rbp-0x40]
    5e9e:	49 8b 0c 24          	mov    rcx,QWORD PTR [r12]
    5ea2:	48 85 c9             	test   rcx,rcx
    5ea5:	0f 84 ba 00 00 00    	je     5f65 <zbtreeRank+0x7d5>
    5eab:	44 8b 45 c4          	mov    r8d,DWORD PTR [rbp-0x3c]
    5eaf:	eb 1c                	jmp    5ecd <zbtreeRank+0x73d>
    5eb1:	66 66 66 66 66 66 2e 	data16 data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    5eb8:	0f 1f 84 00 00 00 00
    5ebf:	00
    5ec0:	49 8b 0c 24          	mov    rcx,QWORD PTR [r12]
    5ec4:	48 85 c9             	test   rcx,rcx
    5ec7:	0f 84 9c 00 00 00    	je     5f69 <zbtreeRank+0x7d9>
    5ecd:	41 0f b6 44 24 10    	movzx  eax,BYTE PTR [r12+0x10]
    5ed3:	49 89 cc             	mov    r12,rcx
    5ed6:	48 85 c0             	test   rax,rax
    5ed9:	74 e5                	je     5ec0 <zbtreeRank+0x730>
    5edb:	3c 04                	cmp    al,0x4
    5edd:	73 11                	jae    5ef0 <zbtreeRank+0x760>
    5edf:	31 c9                	xor    ecx,ecx
    5ee1:	eb 6d                	jmp    5f50 <zbtreeRank+0x7c0>
    5ee3:	66 66 66 66 2e 0f 1f 	data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    5eea:	84 00 00 00 00 00
    5ef0:	89 c1                	mov    ecx,eax
    5ef2:	83 e1 fc             	and    ecx,0xfffffffc
    5ef5:	66 49 0f 6e c7       	movq   xmm0,r15
    5efa:	8d 14 c5 00 00 00 00 	lea    edx,[rax*8+0x0]
    5f01:	83 e2 e0             	and    edx,0xffffffe0
    5f04:	66 0f ef c9          	pxor   xmm1,xmm1
    5f08:	31 f6                	xor    esi,esi
    5f0a:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    5f10:	f3 41 0f 6f 94 34 18 	movdqu xmm2,XMMWORD PTR [r12+rsi*1+0x118]
    5f17:	01 00 00
    5f1a:	66 0f d4 c2          	paddq  xmm0,xmm2
    5f1e:	f3 41 0f 6f 94 34 28 	movdqu xmm2,XMMWORD PTR [r12+rsi*1+0x128]
    5f25:	01 00 00
    5f28:	66 0f d4 ca          	paddq  xmm1,xmm2
    5f2c:	48 83 c6 20          	add    rsi,0x20
    5f30:	48 39 f2             	cmp    rdx,rsi
    5f33:	75 db                	jne    5f10 <zbtreeRank+0x780>
    5f35:	66 0f d4 c8          	paddq  xmm1,xmm0
    5f39:	66 0f 70 c1 ee       	pshufd xmm0,xmm1,0xee
    5f3e:	66 0f d4 c1          	paddq  xmm0,xmm1
    5f42:	66 49 0f 7e c7       	movq   r15,xmm0
    5f47:	48 39 c1             	cmp    rcx,rax
    5f4a:	0f 84 70 ff ff ff    	je     5ec0 <zbtreeRank+0x730>
    5f50:	4d 03 bc cc 18 01 00 	add    r15,QWORD PTR [r12+rcx*8+0x118]
    5f57:	00
    5f58:	48 ff c1             	inc    rcx
    5f5b:	48 39 c8             	cmp    rax,rcx
    5f5e:	75 f0                	jne    5f50 <zbtreeRank+0x7c0>
    5f60:	e9 5b ff ff ff       	jmp    5ec0 <zbtreeRank+0x730>
    5f65:	44 8b 45 c4          	mov    r8d,DWORD PTR [rbp-0x3c]
    5f69:	45 85 c0             	test   r8d,r8d
    5f6c:	74 07                	je     5f75 <zbtreeRank+0x7e5>
    5f6e:	49 f7 d7             	not    r15
    5f71:	4c 03 7f 60          	add    r15,QWORD PTR [rdi+0x60]
    5f75:	4c 89 f8             	mov    rax,r15
    5f78:	48 83 c4 68          	add    rsp,0x68
    5f7c:	5b                   	pop    rbx
    5f7d:	41 5c                	pop    r12
    5f7f:	41 5d                	pop    r13
    5f81:	41 5e                	pop    r14
    5f83:	41 5f                	pop    r15
    5f85:	5d                   	pop    rbp
    5f86:	c3                   	ret

Disassembly of section .fini:
