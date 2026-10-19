
build/size-matrix/btree-bench:     file format elf64-x86-64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .plt.got:

Disassembly of section .text:

0000000000004a70 <zbtreeFindForAdd>:
    4a70:	55                   	push   rbp
    4a71:	48 89 e5             	mov    rbp,rsp
    4a74:	41 57                	push   r15
    4a76:	41 56                	push   r14
    4a78:	41 55                	push   r13
    4a7a:	41 54                	push   r12
    4a7c:	53                   	push   rbx
    4a7d:	48 81 ec 98 00 00 00 	sub    rsp,0x98
    4a84:	48 89 cb             	mov    rbx,rcx
    4a87:	48 89 95 50 ff ff ff 	mov    QWORD PTR [rbp-0xb0],rdx
    4a8e:	49 89 f7             	mov    r15,rsi
    4a91:	48 89 7d c8          	mov    QWORD PTR [rbp-0x38],rdi
    4a95:	0f b6 76 ff          	movzx  esi,BYTE PTR [rsi-0x1]
    4a99:	89 f0                	mov    eax,esi
    4a9b:	83 e0 07             	and    eax,0x7
    4a9e:	83 f8 04             	cmp    eax,0x4
    4aa1:	77 2f                	ja     4ad2 <zbtreeFindForAdd+0x62>
    4aa3:	48 8d 0d ca f1 00 00 	lea    rcx,[rip+0xf1ca]        # 13c74 <_IO_stdin_used+0xc74>
    4aaa:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    4aae:	48 01 c8             	add    rax,rcx
    4ab1:	ff e0                	jmp    rax
    4ab3:	c1 ee 03             	shr    esi,0x3
    4ab6:	eb 1c                	jmp    4ad4 <zbtreeFindForAdd+0x64>
    4ab8:	49 8b 77 ef          	mov    rsi,QWORD PTR [r15-0x11]
    4abc:	eb 16                	jmp    4ad4 <zbtreeFindForAdd+0x64>
    4abe:	41 0f b7 77 fb       	movzx  esi,WORD PTR [r15-0x5]
    4ac3:	eb 0f                	jmp    4ad4 <zbtreeFindForAdd+0x64>
    4ac5:	41 8b 77 f7          	mov    esi,DWORD PTR [r15-0x9]
    4ac9:	eb 09                	jmp    4ad4 <zbtreeFindForAdd+0x64>
    4acb:	41 0f b6 77 fd       	movzx  esi,BYTE PTR [r15-0x3]
    4ad0:	eb 02                	jmp    4ad4 <zbtreeFindForAdd+0x64>
    4ad2:	31 f6                	xor    esi,esi
    4ad4:	4c 89 ff             	mov    rdi,r15
    4ad7:	e8 04 ce 00 00       	call   118e0 <dictGenHashFunction>
    4adc:	48 89 45 88          	mov    QWORD PTR [rbp-0x78],rax
    4ae0:	c7 45 ac 00 00 00 00 	mov    DWORD PTR [rbp-0x54],0x0
    4ae7:	41 0f b6 47 ff       	movzx  eax,BYTE PTR [r15-0x1]
    4aec:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    4af0:	83 e0 07             	and    eax,0x7
    4af3:	45 31 c0             	xor    r8d,r8d
    4af6:	83 f8 04             	cmp    eax,0x4
    4af9:	0f 87 15 01 00 00    	ja     4c14 <zbtreeFindForAdd+0x1a4>
    4aff:	48 8d 0d 82 f1 00 00 	lea    rcx,[rip+0xf182]        # 13c88 <_IO_stdin_used+0xc88>
    4b06:	48 63 04 81          	movsxd rax,DWORD PTR [rcx+rax*4]
    4b0a:	48 01 c8             	add    rax,rcx
    4b0d:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4b11:	ff e0                	jmp    rax
    4b13:	48 8b 45 b8          	mov    rax,QWORD PTR [rbp-0x48]
    4b17:	c1 e8 03             	shr    eax,0x3
    4b1a:	eb 18                	jmp    4b34 <zbtreeFindForAdd+0xc4>
    4b1c:	49 8b 47 ef          	mov    rax,QWORD PTR [r15-0x11]
    4b20:	eb 12                	jmp    4b34 <zbtreeFindForAdd+0xc4>
    4b22:	41 0f b7 47 fb       	movzx  eax,WORD PTR [r15-0x5]
    4b27:	eb 0b                	jmp    4b34 <zbtreeFindForAdd+0xc4>
    4b29:	41 8b 47 f7          	mov    eax,DWORD PTR [r15-0x9]
    4b2d:	eb 05                	jmp    4b34 <zbtreeFindForAdd+0xc4>
    4b2f:	41 0f b6 47 fd       	movzx  eax,BYTE PTR [r15-0x3]
    4b34:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    4b38:	c6 45 98 01          	mov    BYTE PTR [rbp-0x68],0x1
    4b3c:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    4b41:	4c 89 bd 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],r15
    4b48:	0f 84 e6 00 00 00    	je     4c34 <zbtreeFindForAdd+0x1c4>
    4b4e:	48 8b 7d c8          	mov    rdi,QWORD PTR [rbp-0x38]
    4b52:	be 01 00 00 00       	mov    esi,0x1
    4b57:	e8 74 30 00 00       	call   7bd0 <zbtIndexRehashStep>
    4b5c:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4b60:	4c 8b 6e 40          	mov    r13,QWORD PTR [rsi+0x40]
    4b64:	4d 85 ed             	test   r13,r13
    4b67:	0f 84 94 00 00 00    	je     4c01 <zbtreeFindForAdd+0x191>
    4b6d:	49 8b 55 08          	mov    rdx,QWORD PTR [r13+0x8]
    4b71:	48 85 d2             	test   rdx,rdx
    4b74:	0f 84 68 0a 00 00    	je     55e2 <zbtreeFindForAdd+0xb72>
    4b7a:	48 89 5d c0          	mov    QWORD PTR [rbp-0x40],rbx
    4b7e:	48 8b 45 88          	mov    rax,QWORD PTR [rbp-0x78]
    4b82:	89 c3                	mov    ebx,eax
    4b84:	c1 eb 18             	shr    ebx,0x18
    4b87:	3d 00 00 00 01       	cmp    eax,0x1000000
    4b8c:	b9 01 00 00 00       	mov    ecx,0x1
    4b91:	0f 42 d9             	cmovb  ebx,ecx
    4b94:	48 ff ca             	dec    rdx
    4b97:	89 c1                	mov    ecx,eax
    4b99:	48 89 4d 80          	mov    QWORD PTR [rbp-0x80],rcx
    4b9d:	89 d7                	mov    edi,edx
    4b9f:	21 c7                	and    edi,eax
    4ba1:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    4ba8:	79 37 9e
    4bab:	48 0f af c3          	imul   rax,rbx
    4baf:	48 89 c1             	mov    rcx,rax
    4bb2:	48 c1 e9 3a          	shr    rcx,0x3a
    4bb6:	41 b8 01 00 00 00    	mov    r8d,0x1
    4bbc:	49 d3 e0             	shl    r8,cl
    4bbf:	49 0f ab d8          	bts    r8,rbx
    4bc3:	48 c1 e8 24          	shr    rax,0x24
    4bc7:	49 0f ab c0          	bts    r8,rax
    4bcb:	4c 89 45 98          	mov    QWORD PTR [rbp-0x68],r8
    4bcf:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    4bd6:	01 01 01
    4bd9:	48 0f af c3          	imul   rax,rbx
    4bdd:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    4be4:	4c 8d 7e 18          	lea    r15,[rsi+0x18]
    4be8:	45 31 d2             	xor    r10d,r10d
    4beb:	45 31 c9             	xor    r9d,r9d
    4bee:	45 31 c0             	xor    r8d,r8d
    4bf1:	4c 89 7d a0          	mov    QWORD PTR [rbp-0x60],r15
    4bf5:	48 89 95 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rdx
    4bfc:	e9 9d 05 00 00       	jmp    519e <zbtreeFindForAdd+0x72e>
    4c01:	31 ff                	xor    edi,edi
    4c03:	45 31 c0             	xor    r8d,r8d
    4c06:	4c 8b 4e 20          	mov    r9,QWORD PTR [rsi+0x20]
    4c0a:	4d 85 c9             	test   r9,r9
    4c0d:	75 34                	jne    4c43 <zbtreeFindForAdd+0x1d3>
    4c0f:	e9 28 0b 00 00       	jmp    573c <zbtreeFindForAdd+0xccc>
    4c14:	31 c0                	xor    eax,eax
    4c16:	48 89 45 b8          	mov    QWORD PTR [rbp-0x48],rax
    4c1a:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4c1e:	c6 45 98 01          	mov    BYTE PTR [rbp-0x68],0x1
    4c22:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    4c27:	4c 89 bd 58 ff ff ff 	mov    QWORD PTR [rbp-0xa8],r15
    4c2e:	0f 85 1a ff ff ff    	jne    4b4e <zbtreeFindForAdd+0xde>
    4c34:	31 ff                	xor    edi,edi
    4c36:	4c 8b 4e 20          	mov    r9,QWORD PTR [rsi+0x20]
    4c3a:	4d 85 c9             	test   r9,r9
    4c3d:	0f 84 f9 0a 00 00    	je     573c <zbtreeFindForAdd+0xccc>
    4c43:	48 89 5d c0          	mov    QWORD PTR [rbp-0x40],rbx
    4c47:	48 8d 46 18          	lea    rax,[rsi+0x18]
    4c4b:	48 89 85 78 ff ff ff 	mov    QWORD PTR [rbp-0x88],rax
    4c52:	48 8b 55 88          	mov    rdx,QWORD PTR [rbp-0x78]
    4c56:	89 d3                	mov    ebx,edx
    4c58:	c1 eb 18             	shr    ebx,0x18
    4c5b:	81 fa 00 00 00 01    	cmp    edx,0x1000000
    4c61:	b8 01 00 00 00       	mov    eax,0x1
    4c66:	0f 42 d8             	cmovb  ebx,eax
    4c69:	49 ff c9             	dec    r9
    4c6c:	45 89 cb             	mov    r11d,r9d
    4c6f:	41 21 d3             	and    r11d,edx
    4c72:	48 b8 15 7c 4a 7f b9 	movabs rax,0x9e3779b97f4a7c15
    4c79:	79 37 9e
    4c7c:	48 0f af c3          	imul   rax,rbx
    4c80:	48 89 c1             	mov    rcx,rax
    4c83:	48 c1 e9 3a          	shr    rcx,0x3a
    4c87:	41 ba 01 00 00 00    	mov    r10d,0x1
    4c8d:	49 d3 e2             	shl    r10,cl
    4c90:	49 0f ab da          	bts    r10,rbx
    4c94:	48 c1 e8 24          	shr    rax,0x24
    4c98:	49 0f ab c2          	bts    r10,rax
    4c9c:	4c 89 95 40 ff ff ff 	mov    QWORD PTR [rbp-0xc0],r10
    4ca3:	48 b8 01 01 01 01 01 	movabs rax,0x101010101010101
    4caa:	01 01 01
    4cad:	48 0f af c3          	imul   rax,rbx
    4cb1:	48 89 85 70 ff ff ff 	mov    QWORD PTR [rbp-0x90],rax
    4cb8:	89 d0                	mov    eax,edx
    4cba:	48 89 85 48 ff ff ff 	mov    QWORD PTR [rbp-0xb8],rax
    4cc1:	45 31 ff             	xor    r15d,r15d
    4cc4:	45 31 d2             	xor    r10d,r10d
    4cc7:	45 31 f6             	xor    r14d,r14d
    4cca:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    4cce:	4c 89 45 a0          	mov    QWORD PTR [rbp-0x60],r8
    4cd2:	4c 89 4d 80          	mov    QWORD PTR [rbp-0x80],r9
    4cd6:	eb 48                	jmp    4d20 <zbtreeFindForAdd+0x2b0>
    4cd8:	41 0f b7 45 1e       	movzx  eax,WORD PTR [r13+0x1e]
    4cdd:	3d ff ff 00 00       	cmp    eax,0xffff
    4ce2:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    4ce7:	0f 44 c1             	cmove  eax,ecx
    4cea:	83 f8 ff             	cmp    eax,0xffffffff
    4ced:	b8 07 00 00 00       	mov    eax,0x7
    4cf2:	44 0f 44 d0          	cmove  r10d,eax
    4cf6:	b8 00 00 00 00       	mov    eax,0x0
    4cfb:	4c 0f 45 e8          	cmovne r13,rax
    4cff:	4d 89 ef             	mov    r15,r13
    4d02:	4c 8b 9d 68 ff ff ff 	mov    r11,QWORD PTR [rbp-0x98]
    4d09:	49 ff c3             	inc    r11
    4d0c:	4c 8b 4d 80          	mov    r9,QWORD PTR [rbp-0x80]
    4d10:	4d 21 cb             	and    r11,r9
    4d13:	49 ff c6             	inc    r14
    4d16:	4c 3b 76 20          	cmp    r14,QWORD PTR [rsi+0x20]
    4d1a:	0f 83 8e 09 00 00    	jae    56ae <zbtreeFindForAdd+0xc3e>
    4d20:	4c 89 7d 90          	mov    QWORD PTR [rbp-0x70],r15
    4d24:	4c 89 b5 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],r14
    4d2b:	44 89 55 d4          	mov    DWORD PTR [rbp-0x2c],r10d
    4d2f:	48 8b 46 18          	mov    rax,QWORD PTR [rsi+0x18]
    4d33:	31 c9                	xor    ecx,ecx
    4d35:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4d39:	0f 95 c1             	setne  cl
    4d3c:	c1 e1 04             	shl    ecx,0x4
    4d3f:	48 83 c9 20          	or     rcx,0x20
    4d43:	4c 89 9d 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],r11
    4d4a:	49 0f af cb          	imul   rcx,r11
    4d4e:	4c 8d 2c 08          	lea    r13,[rax+rcx*1]
    4d52:	4c 8b 3c 08          	mov    r15,QWORD PTR [rax+rcx*1]
    4d56:	4c 33 bd 70 ff ff ff 	xor    r15,QWORD PTR [rbp-0x90]
    4d5d:	4c 89 f8             	mov    rax,r15
    4d60:	48 f7 d0             	not    rax
    4d63:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    4d6a:	80 80 80
    4d6d:	48 21 c8             	and    rax,rcx
    4d70:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    4d77:	fe fe fe
    4d7a:	49 01 cf             	add    r15,rcx
    4d7d:	49 21 c7             	and    r15,rax
    4d80:	75 2b                	jne    4dad <zbtreeFindForAdd+0x33d>
    4d82:	e9 49 01 00 00       	jmp    4ed0 <zbtreeFindForAdd+0x460>
    4d87:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    4d8e:	00 00
    4d90:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    4d95:	0f 84 f8 00 00 00    	je     4e93 <zbtreeFindForAdd+0x423>
    4d9b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    4da0:	49 8d 47 ff          	lea    rax,[r15-0x1]
    4da4:	49 21 c7             	and    r15,rax
    4da7:	0f 84 23 01 00 00    	je     4ed0 <zbtreeFindForAdd+0x460>
    4dad:	f3 4d 0f bc f7       	tzcnt  r14,r15
    4db2:	49 8b 45 00          	mov    rax,QWORD PTR [r13+0x0]
    4db6:	44 89 f1             	mov    ecx,r14d
    4db9:	80 e1 38             	and    cl,0x38
    4dbc:	48 d3 e8             	shr    rax,cl
    4dbf:	38 c3                	cmp    bl,al
    4dc1:	75 dd                	jne    4da0 <zbtreeFindForAdd+0x330>
    4dc3:	41 c1 ee 03          	shr    r14d,0x3
    4dc7:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4dcb:	44 89 f0             	mov    eax,r14d
    4dce:	74 0c                	je     4ddc <zbtreeFindForAdd+0x36c>
    4dd0:	41 8b 44 85 10       	mov    eax,DWORD PTR [r13+rax*4+0x10]
    4dd5:	83 f8 ff             	cmp    eax,0xffffffff
    4dd8:	75 0f                	jne    4de9 <zbtreeFindForAdd+0x379>
    4dda:	eb c4                	jmp    4da0 <zbtreeFindForAdd+0x330>
    4ddc:	41 0f b7 44 45 10    	movzx  eax,WORD PTR [r13+rax*2+0x10]
    4de2:	3d ff ff 00 00       	cmp    eax,0xffff
    4de7:	74 b7                	je     4da0 <zbtreeFindForAdd+0x330>
    4de9:	3b 46 54             	cmp    eax,DWORD PTR [rsi+0x54]
    4dec:	73 a2                	jae    4d90 <zbtreeFindForAdd+0x320>
    4dee:	48 8b 4e 48          	mov    rcx,QWORD PTR [rsi+0x48]
    4df2:	89 c2                	mov    edx,eax
    4df4:	4c 8b 24 d1          	mov    r12,QWORD PTR [rcx+rdx*8]
    4df8:	4d 85 e4             	test   r12,r12
    4dfb:	74 93                	je     4d90 <zbtreeFindForAdd+0x320>
    4dfd:	44 89 e1             	mov    ecx,r12d
    4e00:	83 e1 01             	and    ecx,0x1
    4e03:	75 8b                	jne    4d90 <zbtreeFindForAdd+0x320>
    4e05:	41 39 44 24 30       	cmp    DWORD PTR [r12+0x30],eax
    4e0a:	74 24                	je     4e30 <zbtreeFindForAdd+0x3c0>
    4e0c:	48 8d 3d 0b e8 00 00 	lea    rdi,[rip+0xe80b]        # 1361e <_IO_stdin_used+0x61e>
    4e13:	be a5 07 00 00       	mov    esi,0x7a5
    4e18:	48 8d 15 58 e9 00 00 	lea    rdx,[rip+0xe958]        # 13777 <_IO_stdin_used+0x777>
    4e1f:	e8 7c c8 00 00       	call   116a0 <standalone_panic>
    4e24:	4c 8b 45 a0          	mov    r8,QWORD PTR [rbp-0x60]
    4e28:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    4e2c:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4e30:	48 8b 46 40          	mov    rax,QWORD PTR [rsi+0x40]
    4e34:	48 85 c0             	test   rax,rax
    4e37:	74 1f                	je     4e58 <zbtreeFindForAdd+0x3e8>
    4e39:	48 3b 85 78 ff ff ff 	cmp    rax,QWORD PTR [rbp-0x88]
    4e40:	0f 94 c1             	sete   cl
    4e43:	41 0f b7 54 24 16    	movzx  edx,WORD PTR [r12+0x16]
    4e49:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    4e4d:	0f 95 c0             	setne  al
    4e50:	38 c1                	cmp    cl,al
    4e52:	0f 84 48 ff ff ff    	je     4da0 <zbtreeFindForAdd+0x330>
    4e58:	4c 89 e7             	mov    rdi,r12
    4e5b:	48 8b 75 88          	mov    rsi,QWORD PTR [rbp-0x78]
    4e5f:	48 8b 95 58 ff ff ff 	mov    rdx,QWORD PTR [rbp-0xa8]
    4e66:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    4e6a:	4c 8b 85 50 ff ff ff 	mov    r8,QWORD PTR [rbp-0xb0]
    4e71:	4c 8d 4d ac          	lea    r9,[rbp-0x54]
    4e75:	e8 36 6e 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    4e7a:	4c 8b 45 a0          	mov    r8,QWORD PTR [rbp-0x60]
    4e7e:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    4e82:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4e86:	85 c0                	test   eax,eax
    4e88:	0f 84 12 ff ff ff    	je     4da0 <zbtreeFindForAdd+0x330>
    4e8e:	e9 5a 07 00 00       	jmp    55ed <zbtreeFindForAdd+0xb7d>
    4e93:	48 8d 3d 84 e7 00 00 	lea    rdi,[rip+0xe784]        # 1361e <_IO_stdin_used+0x61e>
    4e9a:	be a1 07 00 00       	mov    esi,0x7a1
    4e9f:	48 8d 15 f0 e8 00 00 	lea    rdx,[rip+0xe8f0]        # 13796 <_IO_stdin_used+0x796>
    4ea6:	e8 f5 c7 00 00       	call   116a0 <standalone_panic>
    4eab:	4c 8b 45 a0          	mov    r8,QWORD PTR [rbp-0x60]
    4eaf:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    4eb3:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    4eb7:	49 8d 47 ff          	lea    rax,[r15-0x1]
    4ebb:	49 21 c7             	and    r15,rax
    4ebe:	0f 85 e9 fe ff ff    	jne    4dad <zbtreeFindForAdd+0x33d>
    4ec4:	66 66 66 2e 0f 1f 84 	data16 data16 cs nop WORD PTR [rax+rax*1+0x0]
    4ecb:	00 00 00 00 00
    4ed0:	4c 8b b5 60 ff ff ff 	mov    r14,QWORD PTR [rbp-0xa0]
    4ed7:	4d 85 f6             	test   r14,r14
    4eda:	75 3d                	jne    4f19 <zbtreeFindForAdd+0x4a9>
    4edc:	8b 46 20             	mov    eax,DWORD PTR [rsi+0x20]
    4edf:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    4ee4:	01 c8                	add    eax,ecx
    4ee6:	23 85 48 ff ff ff    	and    eax,DWORD PTR [rbp-0xb8]
    4eec:	31 c9                	xor    ecx,ecx
    4eee:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4ef2:	48 8b 56 18          	mov    rdx,QWORD PTR [rsi+0x18]
    4ef6:	0f 95 c1             	setne  cl
    4ef9:	c1 e1 04             	shl    ecx,0x4
    4efc:	48 83 c9 20          	or     rcx,0x20
    4f00:	48 0f af c8          	imul   rcx,rax
    4f04:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    4f09:	48 f7 d0             	not    rax
    4f0c:	48 85 85 40 ff ff ff 	test   QWORD PTR [rbp-0xc0],rax
    4f13:	0f 85 a6 07 00 00    	jne    56bf <zbtreeFindForAdd+0xc4f>
    4f19:	49 8b 4d 00          	mov    rcx,QWORD PTR [r13+0x0]
    4f1d:	31 c0                	xor    eax,eax
    4f1f:	84 c9                	test   cl,cl
    4f21:	0f 84 d6 06 00 00    	je     55fd <zbtreeFindForAdd+0xb8d>
    4f27:	4c 8b 7d 90          	mov    r15,QWORD PTR [rbp-0x70]
    4f2b:	4d 85 ff             	test   r15,r15
    4f2e:	44 8b 55 d4          	mov    r10d,DWORD PTR [rbp-0x2c]
    4f32:	75 37                	jne    4f6b <zbtreeFindForAdd+0x4fb>
    4f34:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4f38:	74 06                	je     4f40 <zbtreeFindForAdd+0x4d0>
    4f3a:	41 8b 55 10          	mov    edx,DWORD PTR [r13+0x10]
    4f3e:	eb 15                	jmp    4f55 <zbtreeFindForAdd+0x4e5>
    4f40:	41 0f b7 55 10       	movzx  edx,WORD PTR [r13+0x10]
    4f45:	81 fa ff ff 00 00    	cmp    edx,0xffff
    4f4b:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    4f51:	41 0f 44 d1          	cmove  edx,r9d
    4f55:	83 fa ff             	cmp    edx,0xffffffff
    4f58:	ba 00 00 00 00       	mov    edx,0x0
    4f5d:	44 0f 44 d2          	cmove  r10d,edx
    4f61:	41 bf 00 00 00 00    	mov    r15d,0x0
    4f67:	4d 0f 44 fd          	cmove  r15,r13
    4f6b:	f7 c1 00 ff 00 00    	test   ecx,0xff00
    4f71:	0f 84 b3 06 00 00    	je     562a <zbtreeFindForAdd+0xbba>
    4f77:	4d 85 ff             	test   r15,r15
    4f7a:	75 37                	jne    4fb3 <zbtreeFindForAdd+0x543>
    4f7c:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4f80:	74 06                	je     4f88 <zbtreeFindForAdd+0x518>
    4f82:	41 8b 55 14          	mov    edx,DWORD PTR [r13+0x14]
    4f86:	eb 15                	jmp    4f9d <zbtreeFindForAdd+0x52d>
    4f88:	41 0f b7 55 12       	movzx  edx,WORD PTR [r13+0x12]
    4f8d:	81 fa ff ff 00 00    	cmp    edx,0xffff
    4f93:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    4f99:	41 0f 44 d1          	cmove  edx,r9d
    4f9d:	83 fa ff             	cmp    edx,0xffffffff
    4fa0:	ba 01 00 00 00       	mov    edx,0x1
    4fa5:	44 0f 44 d2          	cmove  r10d,edx
    4fa9:	41 bf 00 00 00 00    	mov    r15d,0x0
    4faf:	4d 0f 44 fd          	cmove  r15,r13
    4fb3:	f7 c1 00 00 ff 00    	test   ecx,0xff0000
    4fb9:	0f 84 82 06 00 00    	je     5641 <zbtreeFindForAdd+0xbd1>
    4fbf:	4d 85 ff             	test   r15,r15
    4fc2:	75 37                	jne    4ffb <zbtreeFindForAdd+0x58b>
    4fc4:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    4fc8:	74 06                	je     4fd0 <zbtreeFindForAdd+0x560>
    4fca:	41 8b 55 18          	mov    edx,DWORD PTR [r13+0x18]
    4fce:	eb 15                	jmp    4fe5 <zbtreeFindForAdd+0x575>
    4fd0:	41 0f b7 55 14       	movzx  edx,WORD PTR [r13+0x14]
    4fd5:	81 fa ff ff 00 00    	cmp    edx,0xffff
    4fdb:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    4fe1:	41 0f 44 d1          	cmove  edx,r9d
    4fe5:	83 fa ff             	cmp    edx,0xffffffff
    4fe8:	ba 02 00 00 00       	mov    edx,0x2
    4fed:	44 0f 44 d2          	cmove  r10d,edx
    4ff1:	41 bf 00 00 00 00    	mov    r15d,0x0
    4ff7:	4d 0f 44 fd          	cmove  r15,r13
    4ffb:	48 89 ca             	mov    rdx,rcx
    4ffe:	48 c1 ea 18          	shr    rdx,0x18
    5002:	84 d2                	test   dl,dl
    5004:	0f 84 48 06 00 00    	je     5652 <zbtreeFindForAdd+0xbe2>
    500a:	4d 85 ff             	test   r15,r15
    500d:	75 37                	jne    5046 <zbtreeFindForAdd+0x5d6>
    500f:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    5013:	74 06                	je     501b <zbtreeFindForAdd+0x5ab>
    5015:	41 8b 55 1c          	mov    edx,DWORD PTR [r13+0x1c]
    5019:	eb 15                	jmp    5030 <zbtreeFindForAdd+0x5c0>
    501b:	41 0f b7 55 16       	movzx  edx,WORD PTR [r13+0x16]
    5020:	81 fa ff ff 00 00    	cmp    edx,0xffff
    5026:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    502c:	41 0f 44 d1          	cmove  edx,r9d
    5030:	83 fa ff             	cmp    edx,0xffffffff
    5033:	ba 03 00 00 00       	mov    edx,0x3
    5038:	44 0f 44 d2          	cmove  r10d,edx
    503c:	41 bf 00 00 00 00    	mov    r15d,0x0
    5042:	4d 0f 44 fd          	cmove  r15,r13
    5046:	48 ba 00 00 00 00 ff 	movabs rdx,0xff00000000
    504d:	00 00 00
    5050:	48 85 d1             	test   rcx,rdx
    5053:	0f 84 0a 06 00 00    	je     5663 <zbtreeFindForAdd+0xbf3>
    5059:	4d 85 ff             	test   r15,r15
    505c:	75 37                	jne    5095 <zbtreeFindForAdd+0x625>
    505e:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    5062:	74 06                	je     506a <zbtreeFindForAdd+0x5fa>
    5064:	41 8b 55 20          	mov    edx,DWORD PTR [r13+0x20]
    5068:	eb 15                	jmp    507f <zbtreeFindForAdd+0x60f>
    506a:	41 0f b7 55 18       	movzx  edx,WORD PTR [r13+0x18]
    506f:	81 fa ff ff 00 00    	cmp    edx,0xffff
    5075:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    507b:	41 0f 44 d1          	cmove  edx,r9d
    507f:	83 fa ff             	cmp    edx,0xffffffff
    5082:	ba 04 00 00 00       	mov    edx,0x4
    5087:	44 0f 44 d2          	cmove  r10d,edx
    508b:	41 bf 00 00 00 00    	mov    r15d,0x0
    5091:	4d 0f 44 fd          	cmove  r15,r13
    5095:	48 ba 00 00 00 00 00 	movabs rdx,0xff0000000000
    509c:	ff 00 00
    509f:	48 85 d1             	test   rcx,rdx
    50a2:	0f 84 cc 05 00 00    	je     5674 <zbtreeFindForAdd+0xc04>
    50a8:	4d 85 ff             	test   r15,r15
    50ab:	75 37                	jne    50e4 <zbtreeFindForAdd+0x674>
    50ad:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    50b1:	74 06                	je     50b9 <zbtreeFindForAdd+0x649>
    50b3:	41 8b 55 24          	mov    edx,DWORD PTR [r13+0x24]
    50b7:	eb 15                	jmp    50ce <zbtreeFindForAdd+0x65e>
    50b9:	41 0f b7 55 1a       	movzx  edx,WORD PTR [r13+0x1a]
    50be:	81 fa ff ff 00 00    	cmp    edx,0xffff
    50c4:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    50ca:	41 0f 44 d1          	cmove  edx,r9d
    50ce:	83 fa ff             	cmp    edx,0xffffffff
    50d1:	ba 05 00 00 00       	mov    edx,0x5
    50d6:	44 0f 44 d2          	cmove  r10d,edx
    50da:	41 bf 00 00 00 00    	mov    r15d,0x0
    50e0:	4d 0f 44 fd          	cmove  r15,r13
    50e4:	48 ba 00 00 00 00 00 	movabs rdx,0xff000000000000
    50eb:	00 ff 00
    50ee:	48 85 d1             	test   rcx,rdx
    50f1:	0f 84 8e 05 00 00    	je     5685 <zbtreeFindForAdd+0xc15>
    50f7:	4d 85 ff             	test   r15,r15
    50fa:	75 37                	jne    5133 <zbtreeFindForAdd+0x6c3>
    50fc:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    5100:	74 06                	je     5108 <zbtreeFindForAdd+0x698>
    5102:	41 8b 55 28          	mov    edx,DWORD PTR [r13+0x28]
    5106:	eb 15                	jmp    511d <zbtreeFindForAdd+0x6ad>
    5108:	41 0f b7 55 1c       	movzx  edx,WORD PTR [r13+0x1c]
    510d:	81 fa ff ff 00 00    	cmp    edx,0xffff
    5113:	41 b9 ff ff ff ff    	mov    r9d,0xffffffff
    5119:	41 0f 44 d1          	cmove  edx,r9d
    511d:	83 fa ff             	cmp    edx,0xffffffff
    5120:	ba 06 00 00 00       	mov    edx,0x6
    5125:	44 0f 44 d2          	cmove  r10d,edx
    5129:	41 bf 00 00 00 00    	mov    r15d,0x0
    512f:	4d 0f 44 fd          	cmove  r15,r13
    5133:	48 ba 00 00 00 00 00 	movabs rdx,0x100000000000000
    513a:	00 00 01
    513d:	48 39 d1             	cmp    rcx,rdx
    5140:	0f 82 53 05 00 00    	jb     5699 <zbtreeFindForAdd+0xc29>
    5146:	4d 85 ff             	test   r15,r15
    5149:	0f 85 b3 fb ff ff    	jne    4d02 <zbtreeFindForAdd+0x292>
    514f:	83 7e 38 00          	cmp    DWORD PTR [rsi+0x38],0x0
    5153:	0f 84 7f fb ff ff    	je     4cd8 <zbtreeFindForAdd+0x268>
    5159:	41 8b 45 2c          	mov    eax,DWORD PTR [r13+0x2c]
    515d:	e9 88 fb ff ff       	jmp    4cea <zbtreeFindForAdd+0x27a>
    5162:	8b 47 2c             	mov    eax,DWORD PTR [rdi+0x2c]
    5165:	83 f8 ff             	cmp    eax,0xffffffff
    5168:	b8 07 00 00 00       	mov    eax,0x7
    516d:	44 0f 44 c8          	cmove  r9d,eax
    5171:	b8 00 00 00 00       	mov    eax,0x0
    5176:	48 0f 45 f8          	cmovne rdi,rax
    517a:	49 89 fa             	mov    r10,rdi
    517d:	48 8b bd 68 ff ff ff 	mov    rdi,QWORD PTR [rbp-0x98]
    5184:	48 ff c7             	inc    rdi
    5187:	48 8b 95 78 ff ff ff 	mov    rdx,QWORD PTR [rbp-0x88]
    518e:	48 21 d7             	and    rdi,rdx
    5191:	49 ff c0             	inc    r8
    5194:	4d 3b 45 08          	cmp    r8,QWORD PTR [r13+0x8]
    5198:	0f 83 d3 05 00 00    	jae    5771 <zbtreeFindForAdd+0xd01>
    519e:	4c 89 55 90          	mov    QWORD PTR [rbp-0x70],r10
    51a2:	4c 89 85 60 ff ff ff 	mov    QWORD PTR [rbp-0xa0],r8
    51a9:	44 89 4d d4          	mov    DWORD PTR [rbp-0x2c],r9d
    51ad:	49 8b 45 00          	mov    rax,QWORD PTR [r13+0x0]
    51b1:	31 c9                	xor    ecx,ecx
    51b3:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    51b8:	0f 95 c1             	setne  cl
    51bb:	c1 e1 04             	shl    ecx,0x4
    51be:	48 83 c9 20          	or     rcx,0x20
    51c2:	48 89 bd 68 ff ff ff 	mov    QWORD PTR [rbp-0x98],rdi
    51c9:	48 0f af cf          	imul   rcx,rdi
    51cd:	48 8d 3c 08          	lea    rdi,[rax+rcx*1]
    51d1:	4c 8b 34 08          	mov    r14,QWORD PTR [rax+rcx*1]
    51d5:	4c 33 b5 70 ff ff ff 	xor    r14,QWORD PTR [rbp-0x90]
    51dc:	4c 89 f0             	mov    rax,r14
    51df:	48 f7 d0             	not    rax
    51e2:	48 b9 80 80 80 80 80 	movabs rcx,0x8080808080808080
    51e9:	80 80 80
    51ec:	48 21 c8             	and    rax,rcx
    51ef:	48 b9 ff fe fe fe fe 	movabs rcx,0xfefefefefefefeff
    51f6:	fe fe fe
    51f9:	49 01 ce             	add    r14,rcx
    51fc:	49 21 c6             	and    r14,rax
    51ff:	0f 84 5b 01 00 00    	je     5360 <zbtreeFindForAdd+0x8f0>
    5205:	48 89 7d b0          	mov    QWORD PTR [rbp-0x50],rdi
    5209:	eb 32                	jmp    523d <zbtreeFindForAdd+0x7cd>
    520b:	48 8d 3d 0c e4 00 00 	lea    rdi,[rip+0xe40c]        # 1361e <_IO_stdin_used+0x61e>
    5212:	be a1 07 00 00       	mov    esi,0x7a1
    5217:	48 8d 15 78 e5 00 00 	lea    rdx,[rip+0xe578]        # 13796 <_IO_stdin_used+0x796>
    521e:	e8 7d c4 00 00       	call   116a0 <standalone_panic>
    5223:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    5227:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    522b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
    5230:	49 8d 46 ff          	lea    rax,[r14-0x1]
    5234:	49 21 c6             	and    r14,rax
    5237:	0f 84 23 01 00 00    	je     5360 <zbtreeFindForAdd+0x8f0>
    523d:	f3 4d 0f bc c6       	tzcnt  r8,r14
    5242:	48 8b 07             	mov    rax,QWORD PTR [rdi]
    5245:	44 89 c1             	mov    ecx,r8d
    5248:	80 e1 38             	and    cl,0x38
    524b:	48 d3 e8             	shr    rax,cl
    524e:	38 c3                	cmp    bl,al
    5250:	75 de                	jne    5230 <zbtreeFindForAdd+0x7c0>
    5252:	41 c1 e8 03          	shr    r8d,0x3
    5256:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    525b:	44 89 c0             	mov    eax,r8d
    525e:	74 0b                	je     526b <zbtreeFindForAdd+0x7fb>
    5260:	8b 44 87 10          	mov    eax,DWORD PTR [rdi+rax*4+0x10]
    5264:	83 f8 ff             	cmp    eax,0xffffffff
    5267:	75 0e                	jne    5277 <zbtreeFindForAdd+0x807>
    5269:	eb c5                	jmp    5230 <zbtreeFindForAdd+0x7c0>
    526b:	0f b7 44 47 10       	movzx  eax,WORD PTR [rdi+rax*2+0x10]
    5270:	3d ff ff 00 00       	cmp    eax,0xffff
    5275:	74 b9                	je     5230 <zbtreeFindForAdd+0x7c0>
    5277:	3b 46 54             	cmp    eax,DWORD PTR [rsi+0x54]
    527a:	0f 83 c0 00 00 00    	jae    5340 <zbtreeFindForAdd+0x8d0>
    5280:	48 8b 4e 48          	mov    rcx,QWORD PTR [rsi+0x48]
    5284:	89 c2                	mov    edx,eax
    5286:	4c 8b 24 d1          	mov    r12,QWORD PTR [rcx+rdx*8]
    528a:	4d 85 e4             	test   r12,r12
    528d:	0f 84 ad 00 00 00    	je     5340 <zbtreeFindForAdd+0x8d0>
    5293:	44 89 e1             	mov    ecx,r12d
    5296:	83 e1 01             	and    ecx,0x1
    5299:	0f 85 a1 00 00 00    	jne    5340 <zbtreeFindForAdd+0x8d0>
    529f:	41 39 44 24 30       	cmp    DWORD PTR [r12+0x30],eax
    52a4:	74 2a                	je     52d0 <zbtreeFindForAdd+0x860>
    52a6:	48 8d 3d 71 e3 00 00 	lea    rdi,[rip+0xe371]        # 1361e <_IO_stdin_used+0x61e>
    52ad:	be a5 07 00 00       	mov    esi,0x7a5
    52b2:	48 8d 15 be e4 00 00 	lea    rdx,[rip+0xe4be]        # 13777 <_IO_stdin_used+0x777>
    52b9:	4d 89 c7             	mov    r15,r8
    52bc:	e8 df c3 00 00       	call   116a0 <standalone_panic>
    52c1:	4d 89 f8             	mov    r8,r15
    52c4:	4c 8b 7d a0          	mov    r15,QWORD PTR [rbp-0x60]
    52c8:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    52cc:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    52d0:	48 8b 46 40          	mov    rax,QWORD PTR [rsi+0x40]
    52d4:	48 85 c0             	test   rax,rax
    52d7:	74 1b                	je     52f4 <zbtreeFindForAdd+0x884>
    52d9:	4c 39 e8             	cmp    rax,r13
    52dc:	0f 94 c1             	sete   cl
    52df:	41 0f b7 54 24 16    	movzx  edx,WORD PTR [r12+0x16]
    52e5:	66 3b 50 2c          	cmp    dx,WORD PTR [rax+0x2c]
    52e9:	0f 95 c0             	setne  al
    52ec:	38 c1                	cmp    cl,al
    52ee:	0f 84 3c ff ff ff    	je     5230 <zbtreeFindForAdd+0x7c0>
    52f4:	4c 89 e7             	mov    rdi,r12
    52f7:	48 8b 75 88          	mov    rsi,QWORD PTR [rbp-0x78]
    52fb:	48 8b 95 58 ff ff ff 	mov    rdx,QWORD PTR [rbp-0xa8]
    5302:	48 8b 4d b8          	mov    rcx,QWORD PTR [rbp-0x48]
    5306:	4d 89 c7             	mov    r15,r8
    5309:	4c 8b 85 50 ff ff ff 	mov    r8,QWORD PTR [rbp-0xb0]
    5310:	4c 8d 4d ac          	lea    r9,[rbp-0x54]
    5314:	e8 97 69 00 00       	call   bcb0 <zbtScoreLeafFindMember>
    5319:	4d 89 f8             	mov    r8,r15
    531c:	4c 8b 7d a0          	mov    r15,QWORD PTR [rbp-0x60]
    5320:	48 8b 7d b0          	mov    rdi,QWORD PTR [rbp-0x50]
    5324:	48 8b 75 c8          	mov    rsi,QWORD PTR [rbp-0x38]
    5328:	85 c0                	test   eax,eax
    532a:	0f 84 00 ff ff ff    	je     5230 <zbtreeFindForAdd+0x7c0>
    5330:	e9 91 03 00 00       	jmp    56c6 <zbtreeFindForAdd+0xc56>
    5335:	66 66 2e 0f 1f 84 00 	data16 cs nop WORD PTR [rax+rax*1+0x0]
    533c:	00 00 00 00
    5340:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    5345:	0f 84 c0 fe ff ff    	je     520b <zbtreeFindForAdd+0x79b>
    534b:	4d 39 ef             	cmp    r15,r13
    534e:	0f 84 dc fe ff ff    	je     5230 <zbtreeFindForAdd+0x7c0>
    5354:	e9 b2 fe ff ff       	jmp    520b <zbtreeFindForAdd+0x79b>
    5359:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    5360:	4c 8b 85 60 ff ff ff 	mov    r8,QWORD PTR [rbp-0xa0]
    5367:	4d 85 c0             	test   r8,r8
    536a:	75 39                	jne    53a5 <zbtreeFindForAdd+0x935>
    536c:	41 8b 45 08          	mov    eax,DWORD PTR [r13+0x8]
    5370:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    5375:	01 c8                	add    eax,ecx
    5377:	23 45 80             	and    eax,DWORD PTR [rbp-0x80]
    537a:	31 c9                	xor    ecx,ecx
    537c:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    5381:	49 8b 55 00          	mov    rdx,QWORD PTR [r13+0x0]
    5385:	0f 95 c1             	setne  cl
    5388:	c1 e1 04             	shl    ecx,0x4
    538b:	48 83 c9 20          	or     rcx,0x20
    538f:	48 0f af c8          	imul   rcx,rax
    5393:	48 8b 44 0a 08       	mov    rax,QWORD PTR [rdx+rcx*1+0x8]
    5398:	48 f7 d0             	not    rax
    539b:	48 85 45 98          	test   QWORD PTR [rbp-0x68],rax
    539f:	0f 85 da 03 00 00    	jne    577f <zbtreeFindForAdd+0xd0f>
    53a5:	48 8b 07             	mov    rax,QWORD PTR [rdi]
    53a8:	84 c0                	test   al,al
    53aa:	0f 84 21 03 00 00    	je     56d1 <zbtreeFindForAdd+0xc61>
    53b0:	4c 8b 55 90          	mov    r10,QWORD PTR [rbp-0x70]
    53b4:	4d 85 d2             	test   r10,r10
    53b7:	44 8b 4d d4          	mov    r9d,DWORD PTR [rbp-0x2c]
    53bb:	75 34                	jne    53f1 <zbtreeFindForAdd+0x981>
    53bd:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    53c2:	74 05                	je     53c9 <zbtreeFindForAdd+0x959>
    53c4:	8b 4f 10             	mov    ecx,DWORD PTR [rdi+0x10]
    53c7:	eb 12                	jmp    53db <zbtreeFindForAdd+0x96b>
    53c9:	0f b7 4f 10          	movzx  ecx,WORD PTR [rdi+0x10]
    53cd:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    53d3:	ba ff ff ff ff       	mov    edx,0xffffffff
    53d8:	0f 44 ca             	cmove  ecx,edx
    53db:	83 f9 ff             	cmp    ecx,0xffffffff
    53de:	b9 00 00 00 00       	mov    ecx,0x0
    53e3:	44 0f 44 c9          	cmove  r9d,ecx
    53e7:	41 ba 00 00 00 00    	mov    r10d,0x0
    53ed:	4c 0f 44 d7          	cmove  r10,rdi
    53f1:	a9 00 ff 00 00       	test   eax,0xff00
    53f6:	0f 84 e2 02 00 00    	je     56de <zbtreeFindForAdd+0xc6e>
    53fc:	4d 85 d2             	test   r10,r10
    53ff:	75 34                	jne    5435 <zbtreeFindForAdd+0x9c5>
    5401:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    5406:	74 05                	je     540d <zbtreeFindForAdd+0x99d>
    5408:	8b 4f 14             	mov    ecx,DWORD PTR [rdi+0x14]
    540b:	eb 12                	jmp    541f <zbtreeFindForAdd+0x9af>
    540d:	0f b7 4f 12          	movzx  ecx,WORD PTR [rdi+0x12]
    5411:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    5417:	ba ff ff ff ff       	mov    edx,0xffffffff
    541c:	0f 44 ca             	cmove  ecx,edx
    541f:	83 f9 ff             	cmp    ecx,0xffffffff
    5422:	b9 01 00 00 00       	mov    ecx,0x1
    5427:	44 0f 44 c9          	cmove  r9d,ecx
    542b:	41 ba 00 00 00 00    	mov    r10d,0x0
    5431:	4c 0f 44 d7          	cmove  r10,rdi
    5435:	a9 00 00 ff 00       	test   eax,0xff0000
    543a:	0f 84 a6 02 00 00    	je     56e6 <zbtreeFindForAdd+0xc76>
    5440:	4d 85 d2             	test   r10,r10
    5443:	75 34                	jne    5479 <zbtreeFindForAdd+0xa09>
    5445:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    544a:	74 05                	je     5451 <zbtreeFindForAdd+0x9e1>
    544c:	8b 4f 18             	mov    ecx,DWORD PTR [rdi+0x18]
    544f:	eb 12                	jmp    5463 <zbtreeFindForAdd+0x9f3>
    5451:	0f b7 4f 14          	movzx  ecx,WORD PTR [rdi+0x14]
    5455:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    545b:	ba ff ff ff ff       	mov    edx,0xffffffff
    5460:	0f 44 ca             	cmove  ecx,edx
    5463:	83 f9 ff             	cmp    ecx,0xffffffff
    5466:	b9 02 00 00 00       	mov    ecx,0x2
    546b:	44 0f 44 c9          	cmove  r9d,ecx
    546f:	41 ba 00 00 00 00    	mov    r10d,0x0
    5475:	4c 0f 44 d7          	cmove  r10,rdi
    5479:	48 89 c1             	mov    rcx,rax
    547c:	48 c1 e9 18          	shr    rcx,0x18
    5480:	84 c9                	test   cl,cl
    5482:	0f 84 66 02 00 00    	je     56ee <zbtreeFindForAdd+0xc7e>
    5488:	4d 85 d2             	test   r10,r10
    548b:	75 34                	jne    54c1 <zbtreeFindForAdd+0xa51>
    548d:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    5492:	74 05                	je     5499 <zbtreeFindForAdd+0xa29>
    5494:	8b 4f 1c             	mov    ecx,DWORD PTR [rdi+0x1c]
    5497:	eb 12                	jmp    54ab <zbtreeFindForAdd+0xa3b>
    5499:	0f b7 4f 16          	movzx  ecx,WORD PTR [rdi+0x16]
    549d:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    54a3:	ba ff ff ff ff       	mov    edx,0xffffffff
    54a8:	0f 44 ca             	cmove  ecx,edx
    54ab:	83 f9 ff             	cmp    ecx,0xffffffff
    54ae:	b9 03 00 00 00       	mov    ecx,0x3
    54b3:	44 0f 44 c9          	cmove  r9d,ecx
    54b7:	41 ba 00 00 00 00    	mov    r10d,0x0
    54bd:	4c 0f 44 d7          	cmove  r10,rdi
    54c1:	48 b9 00 00 00 00 ff 	movabs rcx,0xff00000000
    54c8:	00 00 00
    54cb:	48 85 c8             	test   rax,rcx
    54ce:	0f 84 22 02 00 00    	je     56f6 <zbtreeFindForAdd+0xc86>
    54d4:	4d 85 d2             	test   r10,r10
    54d7:	75 34                	jne    550d <zbtreeFindForAdd+0xa9d>
    54d9:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    54de:	74 05                	je     54e5 <zbtreeFindForAdd+0xa75>
    54e0:	8b 4f 20             	mov    ecx,DWORD PTR [rdi+0x20]
    54e3:	eb 12                	jmp    54f7 <zbtreeFindForAdd+0xa87>
    54e5:	0f b7 4f 18          	movzx  ecx,WORD PTR [rdi+0x18]
    54e9:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    54ef:	ba ff ff ff ff       	mov    edx,0xffffffff
    54f4:	0f 44 ca             	cmove  ecx,edx
    54f7:	83 f9 ff             	cmp    ecx,0xffffffff
    54fa:	b9 04 00 00 00       	mov    ecx,0x4
    54ff:	44 0f 44 c9          	cmove  r9d,ecx
    5503:	41 ba 00 00 00 00    	mov    r10d,0x0
    5509:	4c 0f 44 d7          	cmove  r10,rdi
    550d:	48 b9 00 00 00 00 00 	movabs rcx,0xff0000000000
    5514:	ff 00 00
    5517:	48 85 c8             	test   rax,rcx
    551a:	0f 84 de 01 00 00    	je     56fe <zbtreeFindForAdd+0xc8e>
    5520:	4d 85 d2             	test   r10,r10
    5523:	75 34                	jne    5559 <zbtreeFindForAdd+0xae9>
    5525:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    552a:	74 05                	je     5531 <zbtreeFindForAdd+0xac1>
    552c:	8b 4f 24             	mov    ecx,DWORD PTR [rdi+0x24]
    552f:	eb 12                	jmp    5543 <zbtreeFindForAdd+0xad3>
    5531:	0f b7 4f 1a          	movzx  ecx,WORD PTR [rdi+0x1a]
    5535:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    553b:	ba ff ff ff ff       	mov    edx,0xffffffff
    5540:	0f 44 ca             	cmove  ecx,edx
    5543:	83 f9 ff             	cmp    ecx,0xffffffff
    5546:	b9 05 00 00 00       	mov    ecx,0x5
    554b:	44 0f 44 c9          	cmove  r9d,ecx
    554f:	41 ba 00 00 00 00    	mov    r10d,0x0
    5555:	4c 0f 44 d7          	cmove  r10,rdi
    5559:	48 b9 00 00 00 00 00 	movabs rcx,0xff000000000000
    5560:	00 ff 00
    5563:	48 85 c8             	test   rax,rcx
    5566:	0f 84 9a 01 00 00    	je     5706 <zbtreeFindForAdd+0xc96>
    556c:	4d 85 d2             	test   r10,r10
    556f:	75 34                	jne    55a5 <zbtreeFindForAdd+0xb35>
    5571:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    5576:	74 05                	je     557d <zbtreeFindForAdd+0xb0d>
    5578:	8b 4f 28             	mov    ecx,DWORD PTR [rdi+0x28]
    557b:	eb 12                	jmp    558f <zbtreeFindForAdd+0xb1f>
    557d:	0f b7 4f 1c          	movzx  ecx,WORD PTR [rdi+0x1c]
    5581:	81 f9 ff ff 00 00    	cmp    ecx,0xffff
    5587:	ba ff ff ff ff       	mov    edx,0xffffffff
    558c:	0f 44 ca             	cmove  ecx,edx
    558f:	83 f9 ff             	cmp    ecx,0xffffffff
    5592:	b9 06 00 00 00       	mov    ecx,0x6
    5597:	44 0f 44 c9          	cmove  r9d,ecx
    559b:	41 ba 00 00 00 00    	mov    r10d,0x0
    55a1:	4c 0f 44 d7          	cmove  r10,rdi
    55a5:	48 b9 00 00 00 00 00 	movabs rcx,0x100000000000000
    55ac:	00 00 01
    55af:	48 39 c8             	cmp    rax,rcx
    55b2:	0f 82 56 01 00 00    	jb     570e <zbtreeFindForAdd+0xc9e>
    55b8:	4d 85 d2             	test   r10,r10
    55bb:	0f 85 bc fb ff ff    	jne    517d <zbtreeFindForAdd+0x70d>
    55c1:	41 83 7d 20 00       	cmp    DWORD PTR [r13+0x20],0x0
    55c6:	0f 85 96 fb ff ff    	jne    5162 <zbtreeFindForAdd+0x6f2>
    55cc:	0f b7 47 1e          	movzx  eax,WORD PTR [rdi+0x1e]
    55d0:	3d ff ff 00 00       	cmp    eax,0xffff
    55d5:	b9 ff ff ff ff       	mov    ecx,0xffffffff
    55da:	0f 44 c1             	cmove  eax,ecx
    55dd:	e9 83 fb ff ff       	jmp    5165 <zbtreeFindForAdd+0x6f5>
    55e2:	45 31 d2             	xor    r10d,r10d
    55e5:	45 31 c0             	xor    r8d,r8d
    55e8:	e9 36 01 00 00       	jmp    5723 <zbtreeFindForAdd+0xcb3>
    55ed:	b8 01 00 00 00       	mov    eax,0x1
    55f2:	4c 89 ef             	mov    rdi,r13
    55f5:	45 89 f0             	mov    r8d,r14d
    55f8:	e9 ce 00 00 00       	jmp    56cb <zbtreeFindForAdd+0xc5b>
    55fd:	31 c9                	xor    ecx,ecx
    55ff:	44 8b 55 d4          	mov    r10d,DWORD PTR [rbp-0x2c]
    5603:	4c 8b 7d 90          	mov    r15,QWORD PTR [rbp-0x70]
    5607:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    560b:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    560f:	74 28                	je     5639 <zbtreeFindForAdd+0xbc9>
    5611:	4d 85 ff             	test   r15,r15
    5614:	4d 0f 45 ef          	cmovne r13,r15
    5618:	44 0f 44 d1          	cmove  r10d,ecx
    561c:	45 31 e4             	xor    r12d,r12d
    561f:	4c 89 ef             	mov    rdi,r13
    5622:	45 89 d0             	mov    r8d,r10d
    5625:	e9 15 01 00 00       	jmp    573f <zbtreeFindForAdd+0xccf>
    562a:	b9 01 00 00 00       	mov    ecx,0x1
    562f:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    5633:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    5637:	75 d8                	jne    5611 <zbtreeFindForAdd+0xba1>
    5639:	45 31 e4             	xor    r12d,r12d
    563c:	e9 00 01 00 00       	jmp    5741 <zbtreeFindForAdd+0xcd1>
    5641:	b9 02 00 00 00       	mov    ecx,0x2
    5646:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    564a:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    564e:	75 c1                	jne    5611 <zbtreeFindForAdd+0xba1>
    5650:	eb e7                	jmp    5639 <zbtreeFindForAdd+0xbc9>
    5652:	b9 03 00 00 00       	mov    ecx,0x3
    5657:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    565b:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    565f:	75 b0                	jne    5611 <zbtreeFindForAdd+0xba1>
    5661:	eb d6                	jmp    5639 <zbtreeFindForAdd+0xbc9>
    5663:	b9 04 00 00 00       	mov    ecx,0x4
    5668:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    566c:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    5670:	75 9f                	jne    5611 <zbtreeFindForAdd+0xba1>
    5672:	eb c5                	jmp    5639 <zbtreeFindForAdd+0xbc9>
    5674:	b9 05 00 00 00       	mov    ecx,0x5
    5679:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    567d:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    5681:	75 8e                	jne    5611 <zbtreeFindForAdd+0xba1>
    5683:	eb b4                	jmp    5639 <zbtreeFindForAdd+0xbc9>
    5685:	b9 06 00 00 00       	mov    ecx,0x6
    568a:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    568e:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    5692:	74 a5                	je     5639 <zbtreeFindForAdd+0xbc9>
    5694:	e9 78 ff ff ff       	jmp    5611 <zbtreeFindForAdd+0xba1>
    5699:	b9 07 00 00 00       	mov    ecx,0x7
    569e:	80 7d 98 00          	cmp    BYTE PTR [rbp-0x68],0x0
    56a2:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    56a6:	0f 85 65 ff ff ff    	jne    5611 <zbtreeFindForAdd+0xba1>
    56ac:	eb 8b                	jmp    5639 <zbtreeFindForAdd+0xbc9>
    56ae:	4d 85 ff             	test   r15,r15
    56b1:	0f 95 c0             	setne  al
    56b4:	84 45 98             	test   BYTE PTR [rbp-0x68],al
    56b7:	49 0f 45 ff          	cmovne rdi,r15
    56bb:	45 0f 45 c2          	cmovne r8d,r10d
    56bf:	45 31 e4             	xor    r12d,r12d
    56c2:	31 c0                	xor    eax,eax
    56c4:	eb 05                	jmp    56cb <zbtreeFindForAdd+0xc5b>
    56c6:	b8 01 00 00 00       	mov    eax,0x1
    56cb:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    56cf:	eb 70                	jmp    5741 <zbtreeFindForAdd+0xcd1>
    56d1:	45 31 c0             	xor    r8d,r8d
    56d4:	44 8b 4d d4          	mov    r9d,DWORD PTR [rbp-0x2c]
    56d8:	4c 8b 55 90          	mov    r10,QWORD PTR [rbp-0x70]
    56dc:	eb 36                	jmp    5714 <zbtreeFindForAdd+0xca4>
    56de:	41 b8 01 00 00 00    	mov    r8d,0x1
    56e4:	eb 2e                	jmp    5714 <zbtreeFindForAdd+0xca4>
    56e6:	41 b8 02 00 00 00    	mov    r8d,0x2
    56ec:	eb 26                	jmp    5714 <zbtreeFindForAdd+0xca4>
    56ee:	41 b8 03 00 00 00    	mov    r8d,0x3
    56f4:	eb 1e                	jmp    5714 <zbtreeFindForAdd+0xca4>
    56f6:	41 b8 04 00 00 00    	mov    r8d,0x4
    56fc:	eb 16                	jmp    5714 <zbtreeFindForAdd+0xca4>
    56fe:	41 b8 05 00 00 00    	mov    r8d,0x5
    5704:	eb 0e                	jmp    5714 <zbtreeFindForAdd+0xca4>
    5706:	41 b8 06 00 00 00    	mov    r8d,0x6
    570c:	eb 06                	jmp    5714 <zbtreeFindForAdd+0xca4>
    570e:	41 b8 07 00 00 00    	mov    r8d,0x7
    5714:	4d 85 d2             	test   r10,r10
    5717:	4c 0f 44 d7          	cmove  r10,rdi
    571b:	45 0f 45 c1          	cmovne r8d,r9d
    571f:	48 8b 5d c0          	mov    rbx,QWORD PTR [rbp-0x40]
    5723:	48 83 7e 40 00       	cmp    QWORD PTR [rsi+0x40],0x0
    5728:	0f 94 45 98          	sete   BYTE PTR [rbp-0x68]
    572c:	4c 89 d7             	mov    rdi,r10
    572f:	4c 8b 4e 20          	mov    r9,QWORD PTR [rsi+0x20]
    5733:	4d 85 c9             	test   r9,r9
    5736:	0f 85 07 f5 ff ff    	jne    4c43 <zbtreeFindForAdd+0x1d3>
    573c:	45 31 e4             	xor    r12d,r12d
    573f:	31 c0                	xor    eax,eax
    5741:	48 89 3b             	mov    QWORD PTR [rbx],rdi
    5744:	44 89 43 08          	mov    DWORD PTR [rbx+0x8],r8d
    5748:	4c 89 63 10          	mov    QWORD PTR [rbx+0x10],r12
    574c:	8b 4d ac             	mov    ecx,DWORD PTR [rbp-0x54]
    574f:	89 4b 18             	mov    DWORD PTR [rbx+0x18],ecx
    5752:	48 8b 4d 88          	mov    rcx,QWORD PTR [rbp-0x78]
    5756:	89 4b 1c             	mov    DWORD PTR [rbx+0x1c],ecx
    5759:	8b 4e 5c             	mov    ecx,DWORD PTR [rsi+0x5c]
    575c:	89 4b 20             	mov    DWORD PTR [rbx+0x20],ecx
    575f:	48 81 c4 98 00 00 00 	add    rsp,0x98
    5766:	5b                   	pop    rbx
    5767:	41 5c                	pop    r12
    5769:	41 5d                	pop    r13
    576b:	41 5e                	pop    r14
    576d:	41 5f                	pop    r15
    576f:	5d                   	pop    rbp
    5770:	c3                   	ret
    5771:	31 c0                	xor    eax,eax
    5773:	4d 85 d2             	test   r10,r10
    5776:	44 0f 44 c8          	cmove  r9d,eax
    577a:	45 89 c8             	mov    r8d,r9d
    577d:	eb a0                	jmp    571f <zbtreeFindForAdd+0xcaf>
    577f:	45 31 d2             	xor    r10d,r10d
    5782:	45 31 c0             	xor    r8d,r8d
    5785:	eb 98                	jmp    571f <zbtreeFindForAdd+0xcaf>

Disassembly of section .fini:
