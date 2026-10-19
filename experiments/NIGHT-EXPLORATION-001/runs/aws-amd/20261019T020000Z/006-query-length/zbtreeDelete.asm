
build/size-matrix/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000006940 <zbtreeDelete>:
    6940:	55                   	push   rbp
    6941:	48 89 e5             	mov    rbp,rsp
    6944:	41 57                	push   r15
    6946:	41 56                	push   r14
    6948:	41 55                	push   r13
    694a:	41 54                	push   r12
    694c:	53                   	push   rbx
    694d:	48 83 ec 68          	sub    rsp,0x68
    6951:	48 89 f3             	mov    rbx,rsi
    6954:	48 89 7d d0          	mov    QWORD PTR [rbp-0x30],rdi
    6958:	0f b6 76 ff          	movzx  esi,BYTE PTR [rsi-0x1]
    695c:	89 f0                	mov    eax,esi
    695e:	83 e0 07             	and    eax,0x7
    6961:	83 f8 04             	cmp    eax,0x4
    6964:	77 2c                	ja     6992 <zbtreeDelete+0x52>
    6966:	48 8d 0d 6b d3 00 00 	lea    rcx,[rip+0xd36b]        # 13cd8 <_IO_stdin_used+0xcd8>
    696d:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    6971:	48 01 c8             	add    rax,rcx
    6974:	ff e0                	jmp    rax
    6976:	c1 ee 03             	shr    esi,0x3
    6979:	eb 19                	jmp    6994 <zbtreeDelete+0x54>
    697b:	48 8b 73 ef          	mov    rsi,QWORD PTR [rbx-0x11]
    697f:	eb 13                	jmp    6994 <zbtreeDelete+0x54>
    6981:	0f b7 73 fb          	movzx  esi,WORD PTR [rbx-0x5]
    6985:	eb 0d                	jmp    6994 <zbtreeDelete+0x54>
    6987:	8b 73 f7             	mov    esi,DWORD PTR [rbx-0x9]
    698a:	eb 08                	jmp    6994 <zbtreeDelete+0x54>
    698c:	0f b6 73 fd          	movzx  esi,BYTE PTR [rbx-0x3]
    6990:	eb 02                	jmp    6994 <zbtreeDelete+0x54>
    6992:	31 f6                	xor    esi,esi
    6994:	48 89 df             	mov    rdi,rbx
    6997:	e8 44 af 00 00       	call   118e0 <dictGenHashFunction>
    699c:	48 89 45 b0          	mov    QWORD PTR [rbp-0x50],rax
    69a0:	0f b6 43 ff          	movzx  eax,BYTE PTR [rbx-0x1]
    69a4:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    69a8:	83 e0 07             	and    eax,0x7
    69ab:	83 f8 04             	cmp    eax,0x4
    69ae:	48 89 9d 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rbx
    69b5:	77 7a                	ja     6a31 <zbtreeDelete+0xf1>
    69b7:	48 8d 0d 2e d3 00 00 	lea    rcx,[rip+0xd32e]        # 13cec <_IO_stdin_used+0xcec>
    69be:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    69c2:	48 01 c8             	add    rax,rcx
    69c5:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    69c9:	ff e0                	jmp    rax
    69cb:	48 8b 45 c8          	mov    rax,QWORD PTR [rbp-0x38]
    69cf:	c1 e8 03             	shr    eax,0x3
    69d2:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    69d6:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    69db:	75 69                	jne    6a46 <zbtreeDelete+0x106>
    69dd:	e9 7f 03 00 00       	jmp    6d61 <zbtreeDelete+0x421>
    69e2:	48 8b 43 ef          	mov    rax,QWORD PTR [rbx-0x11]
    69e6:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    69ea:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    69ef:	75 55                	jne    6a46 <zbtreeDelete+0x106>
    69f1:	e9 6b 03 00 00       	jmp    6d61 <zbtreeDelete+0x421>
    69f6:	0f b7 43 fb          	movzx  eax,WORD PTR [rbx-0x5]
    69fa:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    69fe:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6a03:	75 41                	jne    6a46 <zbtreeDelete+0x106>
    6a05:	e9 57 03 00 00       	jmp    6d61 <zbtreeDelete+0x421>
    6a0a:	8b 43 f7             	mov    eax,DWORD PTR [rbx-0x9]
    6a0d:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    6a11:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6a16:	75 2e                	jne    6a46 <zbtreeDelete+0x106>
    6a18:	e9 44 03 00 00       	jmp    6d61 <zbtreeDelete+0x421>
    6a1d:	0f b6 43 fd          	movzx  eax,BYTE PTR [rbx-0x3]
    6a21:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    6a25:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6a2a:	75 1a                	jne    6a46 <zbtreeDelete+0x106>
    6a2c:	e9 30 03 00 00       	jmp    6d61 <zbtreeDelete+0x421>
    6a31:	31 c0                	xor    eax,eax
    6a33:	48 89 45 c8          	mov    QWORD PTR [rbp-0x38],rax
    6a37:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6a3b:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6a40:	0f 84 1b 03 00 00    	je     6d61 <zbtreeDelete+0x421>
    6a46:	48 8b 7d d0          	mov    rdi,QWORD PTR [rbp-0x30]
    6a4a:	be 01 00 00 00       	mov    esi,0x1
    6a4f:	e8 7c 11 00 00       	call   7bd0 <zbtIndexRehashStep>
    6a54:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6a58:	48 8b 7e 40          	mov    rdi,QWORD PTR [rsi+0x40]
    6a5c:	48 85 ff             	test   rdi,rdi
    6a5f:	0f 84 fc 02 00 00    	je     6d61 <zbtreeDelete+0x421>
    6a65:	48 8b 47 08          	mov    rax,QWORD PTR [rdi+0x8]
    6a69:	48 85 c0             	test   rax,rax
    6a6c:	0f 84 ef 02 00 00    	je     6d61 <zbtreeDelete+0x421>
    6a72:	48 89 c2             	mov    rdx,rax
    6a75:	48 8b 4d b0          	mov    rcx,QWORD PTR [rbp-0x50]
    6a79:	89 c8                	mov    eax,ecx
    6a7b:	c1 e8 18             	shr    eax,0x18
    6a7e:	81 f9 00 00 00 01    	cmp    ecx,0x1000000
    6a84:	41 b8 01 00 00 00    	mov    r8d,0x1
    6a8a:	44 0f 43 c0          	cmovae r8d,eax
    6a8e:	48 ff ca             	dec    rdx
    6a91:	89 c8                	mov    eax,ecx
    6a93:	48 89 45 a8          	mov    QWORD PTR [rbp-0x58],rax
    6a97:	48 89 55 a0          	mov    QWORD PTR [rbp-0x60],rdx
    6a9b:	41 89 d1             	mov    r9d,edx
    6a9e:	41 21 c9             	and    r9d,ecx
    6aa1:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    6aa8:	01 01 01
    6aab:	49 0f af c0          	imul   rax,r8
    6aaf:	48 89 45 98          	mov    QWORD PTR [rbp-0x68],rax
    6ab3:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    6aba:	79 37 9e
    6abd:	49 0f af c0          	imul   rax,r8
    6ac1:	48 89 c1             	mov    rcx,rax
    6ac4:	48 c1 e9 3a          	shr    rcx,0x3a
    6ac8:	ba 01 00 00 00       	mov    edx,0x1
    6acd:	48 d3 e2             	shl    rdx,cl
    6ad0:	4c 0f ab c2          	bts    rdx,r8
    6ad4:	48 c1 e8 24          	shr    rax,0x24
    6ad8:	48 0f ab c2          	bts    rdx,rax
    6adc:	48 89 95 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rdx
    6ae3:	48 8d 46 18          	lea    rax,[rsi+0x18]
    6ae7:	48 89 45 80          	mov    QWORD PTR [rbp-0x80],rax
    6aeb:	45 31 d2             	xor    r10d,r10d
    6aee:	48 89 7d c0          	mov    QWORD PTR [rbp-0x40],rdi
    6af2:	4c 89 c3             	mov    rbx,r8
    6af5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    6afc:	00 00 00 00
    6b00:	4c 89 55 90          	mov    QWORD PTR [rbp-0x70],r10
    6b04:	48 8b 07             	mov    rax,QWORD PTR [rdi]
    6b07:	31 c9                	xor    ecx,ecx
    6b09:	83 7f 20 00          	cmp    DWORD PTR [rdi+0x20],0x0
    6b0d:	0f 95 c1             	setne  cl
    6b10:	c1 e1 04             	shl    ecx,0x4
    6b13:	48 83 c9 20          	or     rcx,0x20
    6b17:	4c 89 4d 88          	mov    QWORD PTR [rbp-0x78],r9
    6b1b:	49 0f af c9          	imul   rcx,r9
    6b1f:	4c 8d 2c 08          	lea    r13,[rax+rcx*1]
    6b23:	4c 8b 24 08          	mov    r12,QWORD PTR [rax+rcx*1]
    6b27:	4c 33 65 98          	xor    r12,QWORD PTR [rbp-0x68]
    6b2b:	4c 89 e0             	mov    rax,r12
    6b2e:	48 f7 d0             	not    rax
    6b31:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    6b38:	80 80 80
    6b3b:	48 21 c8             	and    rax,rcx
    6b3e:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    6b45:	fe fe fe
    6b48:	49 01 cc             	add    r12,rcx
    6b4b:	49 21 c4             	and    r12,rax
    6b4e:	75 4e                	jne    6b9e <zbtreeDelete+0x25e>
    6b50:	e9 4b 01 00 00       	jmp    6ca0 <zbtreeDelete+0x360>
    6b55:	4c 89 ff             	mov    rdi,r15
    6b58:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    6b5c:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    6b63:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    6b67:	45 31 c0             	xor    r8d,r8d
    6b6a:	4c 8d 4d bc          	lea    r9,[rbp-0x44]
    6b6e:	e8 3d 51 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    6b73:	49 89 d8             	mov    r8,rbx
    6b76:	48 8b 7d c0          	mov    rdi,QWORD PTR [rbp-0x40]
    6b7a:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6b7e:	85 c0                	test   eax,eax
    6b80:	0f 85 cc 04 00 00    	jne    7052 <zbtreeDelete+0x712>
    6b86:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    6b8d:	00 00 00
    6b90:	49 8d 44 24 ff       	lea    rax,[r12-0x1]
    6b95:	49 21 c4             	and    r12,rax
    6b98:	0f 84 02 01 00 00    	je     6ca0 <zbtreeDelete+0x360>
    6b9e:	f3 4d 0f bc f4       	tzcnt  r14,r12
    6ba3:	49 8b 45 00          	mov    rax,QWORD PTR [r13+0x0]
    6ba7:	44 89 f1             	mov    ecx,r14d
    6baa:	80 e1 38             	and    cl,0x38
    6bad:	48 d3 e8             	shr    rax,cl
    6bb0:	41 38 c0             	cmp    r8b,al
    6bb3:	75 db                	jne    6b90 <zbtreeDelete+0x250>
    6bb5:	41 c1 ee 03          	shr    r14d,0x3
    6bb9:	83 7f 20 00          	cmp    DWORD PTR [rdi+0x20],0x0
    6bbd:	44 89 f0             	mov    eax,r14d
    6bc0:	74 0c                	je     6bce <zbtreeDelete+0x28e>
    6bc2:	41 8b 44 85 10       	mov    eax,DWORD PTR [r13+rax*4+0x10]
    6bc7:	83 f8 ff             	cmp    eax,0xffffffff
    6bca:	75 0f                	jne    6bdb <zbtreeDelete+0x29b>
    6bcc:	eb c2                	jmp    6b90 <zbtreeDelete+0x250>
    6bce:	41 0f b7 44 45 10    	movzx  eax,WORD PTR [r13+rax*2+0x10]
    6bd4:	3d ff ff 00 00       	cmp    eax,0xffff
    6bd9:	74 b5                	je     6b90 <zbtreeDelete+0x250>
    6bdb:	3b 46 54             	cmp    eax,DWORD PTR [rsi+0x54]
    6bde:	73 70                	jae    6c50 <zbtreeDelete+0x310>
    6be0:	48 8b 4e 48          	mov    rcx,QWORD PTR [rsi+0x48]
    6be4:	89 c2                	mov    edx,eax
    6be6:	4c 8b 3c d1          	mov    r15,QWORD PTR [rcx+rdx*8]
    6bea:	4d 85 ff             	test   r15,r15
    6bed:	74 61                	je     6c50 <zbtreeDelete+0x310>
    6bef:	44 89 f9             	mov    ecx,r15d
    6bf2:	83 e1 01             	and    ecx,0x1
    6bf5:	75 59                	jne    6c50 <zbtreeDelete+0x310>
    6bf7:	41 39 47 30          	cmp    DWORD PTR [r15+0x30],eax
    6bfb:	74 23                	je     6c20 <zbtreeDelete+0x2e0>
    6bfd:	48 8d 3d 1a ca 00 00 	lea    rdi,[rip+0xca1a]        # 1361e <_IO_stdin_used+0x61e>
    6c04:	be a5 07 00 00       	mov    esi,0x7a5
    6c09:	48 8d 15 67 cb 00 00 	lea    rdx,[rip+0xcb67]        # 13777 <_IO_stdin_used+0x777>
    6c10:	e8 8b aa 00 00       	call   116a0 <standalone_panic>
    6c15:	49 89 d8             	mov    r8,rbx
    6c18:	48 8b 7d c0          	mov    rdi,QWORD PTR [rbp-0x40]
    6c1c:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6c20:	48 8b 46 40          	mov    rax,QWORD PTR [rsi+0x40]
    6c24:	48 85 c0             	test   rax,rax
    6c27:	0f 84 28 ff ff ff    	je     6b55 <zbtreeDelete+0x215>
    6c2d:	48 39 f8             	cmp    rax,rdi
    6c30:	0f 94 c1             	sete   cl
    6c33:	41 0f b7 57 16       	movzx  edx,WORD PTR [r15+0x16]
    6c38:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    6c3c:	0f 95 c0             	setne  al
    6c3f:	38 c1                	cmp    cl,al
    6c41:	0f 85 0e ff ff ff    	jne    6b55 <zbtreeDelete+0x215>
    6c47:	e9 44 ff ff ff       	jmp    6b90 <zbtreeDelete+0x250>
    6c4c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
    6c50:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6c55:	74 0a                	je     6c61 <zbtreeDelete+0x321>
    6c57:	48 39 7d 80          	cmp    QWORD PTR [rbp-0x80],rdi
    6c5b:	0f 84 2f ff ff ff    	je     6b90 <zbtreeDelete+0x250>
    6c61:	48 8d 3d b6 c9 00 00 	lea    rdi,[rip+0xc9b6]        # 1361e <_IO_stdin_used+0x61e>
    6c68:	be a1 07 00 00       	mov    esi,0x7a1
    6c6d:	48 8d 15 22 cb 00 00 	lea    rdx,[rip+0xcb22]        # 13796 <_IO_stdin_used+0x796>
    6c74:	e8 27 aa 00 00       	call   116a0 <standalone_panic>
    6c79:	49 89 d8             	mov    r8,rbx
    6c7c:	48 8b 7d c0          	mov    rdi,QWORD PTR [rbp-0x40]
    6c80:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6c84:	49 8d 44 24 ff       	lea    rax,[r12-0x1]
    6c89:	49 21 c4             	and    r12,rax
    6c8c:	0f 85 0c ff ff ff    	jne    6b9e <zbtreeDelete+0x25e>
    6c92:	66 66 66 66 66 2e 0f 	data16 data16 data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    6c99:	1f 84 00 00 00 00 00
    6ca0:	4c 8b 55 90          	mov    r10,QWORD PTR [rbp-0x70]
    6ca4:	4d 85 d2             	test   r10,r10
    6ca7:	4c 8b 4d 88          	mov    r9,QWORD PTR [rbp-0x78]
    6cab:	75 35                	jne    6ce2 <zbtreeDelete+0x3a2>
    6cad:	8b 47 08             	mov    eax,DWORD PTR [rdi+0x8]
    6cb0:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    6cb5:	01 c8                	add    eax,ecx
    6cb7:	23 45 a8             	and    eax,DWORD PTR [rbp-0x58]
    6cba:	31 c9                	xor    ecx,ecx
    6cbc:	83 7f 20 00          	cmp    DWORD PTR [rdi+0x20],0x0
    6cc0:	48 8b 17             	mov    rdx,QWORD PTR [rdi]
    6cc3:	0f 95 c1             	setne  cl
    6cc6:	c1 e1 04             	shl    ecx,0x4
    6cc9:	48 83 c9 20          	or     rcx,0x20
    6ccd:	48 0f af c8          	imul   rcx,rax
    6cd1:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    6cd6:	48 f7 d0             	not    rax
    6cd9:	48 85 85 70 ff ff ff 	test   QWORD PTR [rbp-0x90],rax
    6ce0:	75 7f                	jne    6d61 <zbtreeDelete+0x421>
    6ce2:	49 8b 45 00          	mov    rax,QWORD PTR [r13+0x0]
    6ce6:	84 c0                	test   al,al
    6ce8:	74 77                	je     6d61 <zbtreeDelete+0x421>
    6cea:	89 c1                	mov    ecx,eax
    6cec:	81 e1 00 ff 00 00    	and    ecx,0xff00
    6cf2:	74 6d                	je     6d61 <zbtreeDelete+0x421>
    6cf4:	89 c1                	mov    ecx,eax
    6cf6:	81 e1 00 00 ff 00    	and    ecx,0xff0000
    6cfc:	74 63                	je     6d61 <zbtreeDelete+0x421>
    6cfe:	89 c1                	mov    ecx,eax
    6d00:	81 e1 00 00 00 ff    	and    ecx,0xff000000
    6d06:	74 59                	je     6d61 <zbtreeDelete+0x421>
    6d08:	48 89 c1             	mov    rcx,rax
    6d0b:	48 ba 00 00 00 00 ff 	movabs rdx,0xff00000000
    6d12:	00 00 00
    6d15:	48 21 d1             	and    rcx,rdx
    6d18:	74 47                	je     6d61 <zbtreeDelete+0x421>
    6d1a:	48 89 c1             	mov    rcx,rax
    6d1d:	48 ba 00 00 00 00 00 	movabs rdx,0xff0000000000
    6d24:	ff 00 00
    6d27:	48 21 d1             	and    rcx,rdx
    6d2a:	74 35                	je     6d61 <zbtreeDelete+0x421>
    6d2c:	48 89 c1             	mov    rcx,rax
    6d2f:	48 ba 00 00 00 00 00 	movabs rdx,0xff000000000000
    6d36:	00 ff 00
    6d39:	48 21 d1             	and    rcx,rdx
    6d3c:	74 23                	je     6d61 <zbtreeDelete+0x421>
    6d3e:	48 b9 00 00 00 00 00 	movabs rcx,0x100000000000000
    6d45:	00 00 01
    6d48:	48 39 c8             	cmp    rax,rcx
    6d4b:	72 14                	jb     6d61 <zbtreeDelete+0x421>
    6d4d:	49 ff c1             	inc    r9
    6d50:	4c 23 4d a0          	and    r9,QWORD PTR [rbp-0x60]
    6d54:	49 ff c2             	inc    r10
    6d57:	4c 3b 57 08          	cmp    r10,QWORD PTR [rdi+0x8]
    6d5b:	0f 82 9f fd ff ff    	jb     6b00 <zbtreeDelete+0x1c0>
    6d61:	48 8b 7e 20          	mov    rdi,QWORD PTR [rsi+0x20]
    6d65:	48 85 ff             	test   rdi,rdi
    6d68:	0f 84 e0 02 00 00    	je     704e <zbtreeDelete+0x70e>
    6d6e:	48 8d 46 18          	lea    rax,[rsi+0x18]
    6d72:	48 89 45 90          	mov    QWORD PTR [rbp-0x70],rax
    6d76:	48 8b 55 b0          	mov    rdx,QWORD PTR [rbp-0x50]
    6d7a:	89 d0                	mov    eax,edx
    6d7c:	c1 e8 18             	shr    eax,0x18
    6d7f:	81 fa 00 00 00 01    	cmp    edx,0x1000000
    6d85:	41 bc 01 00 00 00    	mov    r12d,0x1
    6d8b:	44 0f 43 e0          	cmovae r12d,eax
    6d8f:	48 ff cf             	dec    rdi
    6d92:	89 d0                	mov    eax,edx
    6d94:	48 89 45 a0          	mov    QWORD PTR [rbp-0x60],rax
    6d98:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    6d9f:	79 37 9e
    6da2:	49 0f af c4          	imul   rax,r12
    6da6:	48 89 c1             	mov    rcx,rax
    6da9:	48 c1 e9 3a          	shr    rcx,0x3a
    6dad:	41 b8 01 00 00 00    	mov    r8d,0x1
    6db3:	49 d3 e0             	shl    r8,cl
    6db6:	41 89 f9             	mov    r9d,edi
    6db9:	41 21 d1             	and    r9d,edx
    6dbc:	4d 0f ab e0          	bts    r8,r12
    6dc0:	48 c1 e8 24          	shr    rax,0x24
    6dc4:	49 0f ab c0          	bts    r8,rax
    6dc8:	4c 89 45 a8          	mov    QWORD PTR [rbp-0x58],r8
    6dcc:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    6dd3:	01 01 01
    6dd6:	49 0f af c4          	imul   rax,r12
    6dda:	48 89 45 88          	mov    QWORD PTR [rbp-0x78],rax
    6dde:	45 31 c0             	xor    r8d,r8d
    6de1:	48 89 7d 98          	mov    QWORD PTR [rbp-0x68],rdi
    6de5:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    6dec:	00 00 00 00
    6df0:	4c 89 45 c0          	mov    QWORD PTR [rbp-0x40],r8
    6df4:	48 8b 46 18          	mov    rax,QWORD PTR [rsi+0x18]
    6df8:	31 c9                	xor    ecx,ecx
    6dfa:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    6dfe:	0f 95 c1             	setne  cl
    6e01:	c1 e1 04             	shl    ecx,0x4
    6e04:	48 83 c9 20          	or     rcx,0x20
    6e08:	4c 89 4d 80          	mov    QWORD PTR [rbp-0x80],r9
    6e0c:	49 0f af c9          	imul   rcx,r9
    6e10:	4c 8d 2c 08          	lea    r13,[rax+rcx*1]
    6e14:	48 8b 1c 08          	mov    rbx,QWORD PTR [rax+rcx*1]
    6e18:	48 33 5d 88          	xor    rbx,QWORD PTR [rbp-0x78]
    6e1c:	48 89 d8             	mov    rax,rbx
    6e1f:	48 f7 d0             	not    rax
    6e22:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    6e29:	80 80 80
    6e2c:	48 21 c8             	and    rax,rcx
    6e2f:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    6e36:	fe fe fe
    6e39:	48 01 cb             	add    rbx,rcx
    6e3c:	48 21 c3             	and    rbx,rax
    6e3f:	75 2c                	jne    6e6d <zbtreeDelete+0x52d>
    6e41:	e9 2a 01 00 00       	jmp    6f70 <zbtreeDelete+0x630>
    6e46:	66 2e 0f 1f 84 00 00 	cs nop WORD PTR [rax+rax*1+0x0]
    6e4d:	00 00 00
    6e50:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    6e55:	0f 84 e0 00 00 00    	je     6f3b <zbtreeDelete+0x5fb>
    6e5b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    6e60:	48 8d 43 ff          	lea    rax,[rbx-0x1]
    6e64:	48 21 c3             	and    rbx,rax
    6e67:	0f 84 03 01 00 00    	je     6f70 <zbtreeDelete+0x630>
    6e6d:	f3 4c 0f bc f3       	tzcnt  r14,rbx
    6e72:	49 8b 45 00          	mov    rax,QWORD PTR [r13+0x0]
    6e76:	44 89 f1             	mov    ecx,r14d
    6e79:	80 e1 38             	and    cl,0x38
    6e7c:	48 d3 e8             	shr    rax,cl
    6e7f:	41 38 c4             	cmp    r12b,al
    6e82:	75 dc                	jne    6e60 <zbtreeDelete+0x520>
    6e84:	41 c1 ee 03          	shr    r14d,0x3
    6e88:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    6e8c:	44 89 f0             	mov    eax,r14d
    6e8f:	74 0c                	je     6e9d <zbtreeDelete+0x55d>
    6e91:	41 8b 44 85 10       	mov    eax,DWORD PTR [r13+rax*4+0x10]
    6e96:	83 f8 ff             	cmp    eax,0xffffffff
    6e99:	75 0f                	jne    6eaa <zbtreeDelete+0x56a>
    6e9b:	eb c3                	jmp    6e60 <zbtreeDelete+0x520>
    6e9d:	41 0f b7 44 45 10    	movzx  eax,WORD PTR [r13+rax*2+0x10]
    6ea3:	3d ff ff 00 00       	cmp    eax,0xffff
    6ea8:	74 b6                	je     6e60 <zbtreeDelete+0x520>
    6eaa:	3b 46 54             	cmp    eax,DWORD PTR [rsi+0x54]
    6ead:	73 a1                	jae    6e50 <zbtreeDelete+0x510>
    6eaf:	48 8b 4e 48          	mov    rcx,QWORD PTR [rsi+0x48]
    6eb3:	89 c2                	mov    edx,eax
    6eb5:	4c 8b 3c d1          	mov    r15,QWORD PTR [rcx+rdx*8]
    6eb9:	4d 85 ff             	test   r15,r15
    6ebc:	74 92                	je     6e50 <zbtreeDelete+0x510>
    6ebe:	44 89 f9             	mov    ecx,r15d
    6ec1:	83 e1 01             	and    ecx,0x1
    6ec4:	75 8a                	jne    6e50 <zbtreeDelete+0x510>
    6ec6:	41 39 47 30          	cmp    DWORD PTR [r15+0x30],eax
    6eca:	74 1c                	je     6ee8 <zbtreeDelete+0x5a8>
    6ecc:	48 8d 3d 4b c7 00 00 	lea    rdi,[rip+0xc74b]        # 1361e <_IO_stdin_used+0x61e>
    6ed3:	be a5 07 00 00       	mov    esi,0x7a5
    6ed8:	48 8d 15 98 c8 00 00 	lea    rdx,[rip+0xc898]        # 13777 <_IO_stdin_used+0x777>
    6edf:	e8 bc a7 00 00       	call   116a0 <standalone_panic>
    6ee4:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6ee8:	48 8b 46 40          	mov    rax,QWORD PTR [rsi+0x40]
    6eec:	48 85 c0             	test   rax,rax
    6eef:	74 1b                	je     6f0c <zbtreeDelete+0x5cc>
    6ef1:	48 3b 45 90          	cmp    rax,QWORD PTR [rbp-0x70]
    6ef5:	0f 94 c1             	sete   cl
    6ef8:	41 0f b7 57 16       	movzx  edx,WORD PTR [r15+0x16]
    6efd:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    6f01:	0f 95 c0             	setne  al
    6f04:	38 c1                	cmp    cl,al
    6f06:	0f 84 54 ff ff ff    	je     6e60 <zbtreeDelete+0x520>
    6f0c:	4c 89 ff             	mov    rdi,r15
    6f0f:	48 8b 75 b0          	mov    rsi,QWORD PTR [rbp-0x50]
    6f13:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    6f1a:	48 8b 4d c8          	mov    rcx,QWORD PTR [rbp-0x38]
    6f1e:	45 31 c0             	xor    r8d,r8d
    6f21:	4c 8d 4d bc          	lea    r9,[rbp-0x44]
    6f25:	e8 86 4d 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    6f2a:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6f2e:	85 c0                	test   eax,eax
    6f30:	0f 84 2a ff ff ff    	je     6e60 <zbtreeDelete+0x520>
    6f36:	e9 17 01 00 00       	jmp    7052 <zbtreeDelete+0x712>
    6f3b:	48 8d 3d dc c6 00 00 	lea    rdi,[rip+0xc6dc]        # 1361e <_IO_stdin_used+0x61e>
    6f42:	be a1 07 00 00       	mov    esi,0x7a1
    6f47:	48 8d 15 48 c8 00 00 	lea    rdx,[rip+0xc848]        # 13796 <_IO_stdin_used+0x796>
    6f4e:	e8 4d a7 00 00       	call   116a0 <standalone_panic>
    6f53:	48 8b 75 d0          	mov    rsi,QWORD PTR [rbp-0x30]
    6f57:	48 8d 43 ff          	lea    rax,[rbx-0x1]
    6f5b:	48 21 c3             	and    rbx,rax
    6f5e:	0f 85 09 ff ff ff    	jne    6e6d <zbtreeDelete+0x52d>
    6f64:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    6f6b:	00 00 00 00 00
    6f70:	4c 8b 45 c0          	mov    r8,QWORD PTR [rbp-0x40]
    6f74:	4d 85 c0             	test   r8,r8
    6f77:	75 37                	jne    6fb0 <zbtreeDelete+0x670>
    6f79:	8b 46 20             	mov    eax,DWORD PTR [rsi+0x20]
    6f7c:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    6f81:	01 c8                	add    eax,ecx
    6f83:	23 45 a0             	and    eax,DWORD PTR [rbp-0x60]
    6f86:	31 c9                	xor    ecx,ecx
    6f88:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    6f8c:	48 8b 56 18          	mov    rdx,QWORD PTR [rsi+0x18]
    6f90:	0f 95 c1             	setne  cl
    6f93:	c1 e1 04             	shl    ecx,0x4
    6f96:	48 83 c9 20          	or     rcx,0x20
    6f9a:	48 0f af c8          	imul   rcx,rax
    6f9e:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    6fa3:	48 f7 d0             	not    rax
    6fa6:	48 85 45 a8          	test   QWORD PTR [rbp-0x58],rax
    6faa:	0f 85 9e 00 00 00    	jne    704e <zbtreeDelete+0x70e>
    6fb0:	49 8b 4d 00          	mov    rcx,QWORD PTR [r13+0x0]
    6fb4:	31 c0                	xor    eax,eax
    6fb6:	84 c9                	test   cl,cl
    6fb8:	0f 84 c9 00 00 00    	je     7087 <zbtreeDelete+0x747>
    6fbe:	89 ca                	mov    edx,ecx
    6fc0:	81 e2 00 ff 00 00    	and    edx,0xff00
    6fc6:	0f 84 bb 00 00 00    	je     7087 <zbtreeDelete+0x747>
    6fcc:	89 ca                	mov    edx,ecx
    6fce:	81 e2 00 00 ff 00    	and    edx,0xff0000
    6fd4:	0f 84 ad 00 00 00    	je     7087 <zbtreeDelete+0x747>
    6fda:	89 ca                	mov    edx,ecx
    6fdc:	81 e2 00 00 00 ff    	and    edx,0xff000000
    6fe2:	0f 84 9f 00 00 00    	je     7087 <zbtreeDelete+0x747>
    6fe8:	48 89 ca             	mov    rdx,rcx
    6feb:	48 bf 00 00 00 00 ff 	movabs rdi,0xff00000000
    6ff2:	00 00 00
    6ff5:	48 21 fa             	and    rdx,rdi
    6ff8:	0f 84 89 00 00 00    	je     7087 <zbtreeDelete+0x747>
    6ffe:	48 89 ca             	mov    rdx,rcx
    7001:	48 bf 00 00 00 00 00 	movabs rdi,0xff0000000000
    7008:	ff 00 00
    700b:	48 21 fa             	and    rdx,rdi
    700e:	74 77                	je     7087 <zbtreeDelete+0x747>
    7010:	48 89 ca             	mov    rdx,rcx
    7013:	48 bf 00 00 00 00 00 	movabs rdi,0xff000000000000
    701a:	00 ff 00
    701d:	48 21 fa             	and    rdx,rdi
    7020:	74 65                	je     7087 <zbtreeDelete+0x747>
    7022:	48 ba 00 00 00 00 00 	movabs rdx,0x100000000000000
    7029:	00 00 01
    702c:	48 39 d1             	cmp    rcx,rdx
    702f:	72 56                	jb     7087 <zbtreeDelete+0x747>
    7031:	4c 8b 4d 80          	mov    r9,QWORD PTR [rbp-0x80]
    7035:	49 ff c1             	inc    r9
    7038:	48 8b 7d 98          	mov    rdi,QWORD PTR [rbp-0x68]
    703c:	49 21 f9             	and    r9,rdi
    703f:	49 ff c0             	inc    r8
    7042:	4c 3b 46 20          	cmp    r8,QWORD PTR [rsi+0x20]
    7046:	0f 82 a4 fd ff ff    	jb     6df0 <zbtreeDelete+0x4b0>
    704c:	eb 39                	jmp    7087 <zbtreeDelete+0x747>
    704e:	31 c0                	xor    eax,eax
    7050:	eb 35                	jmp    7087 <zbtreeDelete+0x747>
    7052:	48 89 f3             	mov    rbx,rsi
    7055:	48 89 f7             	mov    rdi,rsi
    7058:	4c 89 ee             	mov    rsi,r13
    705b:	44 89 f2             	mov    edx,r14d
    705e:	e8 3d 00 00 00       	call   70a0 <zbtIndexDeleteAt>
    7063:	8b 55 bc             	mov    edx,DWORD PTR [rbp-0x44]
    7066:	48 89 df             	mov    rdi,rbx
    7069:	4c 89 fe             	mov    rsi,r15
    706c:	b9 01 00 00 00       	mov    ecx,0x1
    7071:	e8 2a 01 00 00       	call   71a0 <zbtScoreDeleteAt>
    7076:	48 ff 4b 60          	dec    QWORD PTR [rbx+0x60]
    707a:	48 89 df             	mov    rdi,rbx
    707d:	e8 ae 09 00 00       	call   7a30 <zbtIndexShrinkIfNeeded>
    7082:	b8 01 00 00 00       	mov    eax,0x1
    7087:	48 83 c4 68          	add    rsp,0x68
    708b:	5b                   	pop    rbx
    708c:	41 5c                	pop    r12
    708e:	41 5d                	pop    r13
    7090:	41 5e                	pop    r14
    7092:	41 5f                	pop    r15
    7094:	5d                   	pop    rbp
    7095:	c3                   	ret

Disassembly of section .fini:
