_decoder_batch:                         ; @decoder_batch
Lfunc_begin57:
; %bb.0:
	stp	d15, d14, [sp, #-160]!          ; 16-byte Folded Spill
	stp	d13, d12, [sp, #16]             ; 16-byte Folded Spill
	stp	d11, d10, [sp, #32]             ; 16-byte Folded Spill
	stp	d9, d8, [sp, #48]               ; 16-byte Folded Spill
	stp	x28, x27, [sp, #64]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #80]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #96]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #112]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #128]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #144]            ; 16-byte Folded Spill
	add	x29, sp, #144
	sub	sp, sp, #784
Lloh357:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh358:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh359:
	ldr	x8, [x8]
	stur	x8, [x29, #-160]
Ltmp4825:
	cbz	w1, LBB57_146
Ltmp4826:
; %bb.1:
	mov	x4, #0                          ; =0x0
	mov	w8, #0                          ; =0x0
	mov	x17, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	x3, #0                          ; =0x0
	mov	w9, #-3                         ; =0xfffffffd
	mov	x10, sp
	add	x11, x10, #32
	add	x12, x10, #16
	add	x13, x10, #128
	mov	x14, #-1                        ; =0xffffffffffffffff
	mov	w15, #64                        ; =0x40
	b	LBB57_3
Ltmp4827:
LBB57_2:                                ;   in Loop: Header=BB57_3 Depth=1
	add	w8, w8, #1
Ltmp4828:
	cmp	w8, w1
	b.eq	LBB57_144
Ltmp4829:
LBB57_3:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB57_6 Depth 2
                                        ;       Child Loop BB57_97 Depth 3
                                        ;       Child Loop BB57_65 Depth 3
                                        ;       Child Loop BB57_122 Depth 3
                                        ;       Child Loop BB57_92 Depth 3
                                        ;       Child Loop BB57_68 Depth 3
                                        ;       Child Loop BB57_71 Depth 3
                                        ;       Child Loop BB57_25 Depth 3
                                        ;       Child Loop BB57_15 Depth 3
                                        ;       Child Loop BB57_77 Depth 3
                                        ;       Child Loop BB57_80 Depth 3
                                        ;       Child Loop BB57_85 Depth 3
                                        ;       Child Loop BB57_88 Depth 3
	; InlineAsm Start
	; InlineAsm End
Ltmp4830:
	ldr	w16, [x0, #4]
Ltmp4831:
	cbz	w16, LBB57_2
Ltmp4832:
; %bb.4:                                ;   in Loop: Header=BB57_3 Depth=1
	mov	x16, #0                         ; =0x0
Ltmp4833:
	ldr	w6, [x0]
	b	LBB57_6
Ltmp4834:
LBB57_5:                                ;   in Loop: Header=BB57_6 Depth=2
	add	x16, x16, #1
Ltmp4835:
	ldr	w5, [x0, #4]
Ltmp4836:
	cmp	x16, x5
	b.hs	LBB57_2
Ltmp4837:
LBB57_6:                                ;   Parent Loop BB57_3 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB57_97 Depth 3
                                        ;       Child Loop BB57_65 Depth 3
                                        ;       Child Loop BB57_122 Depth 3
                                        ;       Child Loop BB57_92 Depth 3
                                        ;       Child Loop BB57_68 Depth 3
                                        ;       Child Loop BB57_71 Depth 3
                                        ;       Child Loop BB57_25 Depth 3
                                        ;       Child Loop BB57_15 Depth 3
                                        ;       Child Loop BB57_77 Depth 3
                                        ;       Child Loop BB57_80 Depth 3
                                        ;       Child Loop BB57_85 Depth 3
                                        ;       Child Loop BB57_88 Depth 3
	cbz	x6, LBB57_72
Ltmp4838:
; %bb.7:                                ;   in Loop: Header=BB57_6 Depth=2
	ldr	x5, [x0, #8]
	ldr	x5, [x5, x16, lsl #3]
Ltmp4839:
	ldrb	w7, [x5, #52]
Ltmp4840:
	sub	w19, w7, #61
	cmp	w19, #3
	b.lo	LBB57_10
Ltmp4841:
; %bb.8:                                ;   in Loop: Header=BB57_6 Depth=2
	cbz	w7, LBB57_59
Ltmp4842:
; %bb.9:                                ;   in Loop: Header=BB57_6 Depth=2
	cmp	w7, #59
	b.ne	LBB57_61
Ltmp4843:
LBB57_10:                               ;   in Loop: Header=BB57_6 Depth=2
	ldr	x7, [x5, #40]
Ltmp4844:
	add	x19, x5, #56
Ltmp4845:
	cmp	x6, #4
	b.hs	LBB57_22
Ltmp4846:
; %bb.11:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x20, #0                         ; =0x0
Ltmp4847:
LBB57_12:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x6, x6, #0x3
Ltmp4848:
	cbnz	x6, LBB57_15
	b	LBB57_72
Ltmp4849:
LBB57_13:                               ;   in Loop: Header=BB57_15 Depth=3
	lsl	x24, x14, x22
	cmp	w22, #64
	csinv	x22, x14, x24, hs
Ltmp4850:
	and	x22, x23, x22
Ltmp4851:
	ldrb	w23, [x5, #19]
	lsl	x22, x22, x23
Ltmp4852:
LBB57_14:                               ;   in Loop: Header=BB57_15 Depth=3
	cmp	w21, #0
	cneg	x21, x22, ne
	add	x21, x21, x7
Ltmp4853:
	and	x22, x21, #0x7fffffffffffffff
Ltmp4854:
	cmp	x21, #0
	csinv	x21, x22, x21, lt
Ltmp4855:
	str	x21, [x10, x20, lsl #3]
	add	x20, x20, #1
Ltmp4856:
	subs	x6, x6, #1
	b.eq	LBB57_72
Ltmp4857:
LBB57_15:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w22, [x5, #52]
Ltmp4858:
	ldrb	w21, [x5, #53]
	cbz	w22, LBB57_21
Ltmp4859:
; %bb.16:                               ;   in Loop: Header=BB57_15 Depth=3
	mov	x23, x20
Ltmp4860:
	cbz	w21, LBB57_18
Ltmp4861:
; %bb.17:                               ;   in Loop: Header=BB57_15 Depth=3
	ldrb	w23, [x5, #17]
	eor	x24, x20, #0xffffffff
	add	x23, x24, x23
Ltmp4862:
LBB57_18:                               ;   in Loop: Header=BB57_15 Depth=3
	mov	w23, w23
	umull	x25, w23, w22
Ltmp4863:
	lsr	x24, x25, #3
Ltmp4864:
	ldr	x23, [x19, x24]
Ltmp4865:
	and	x26, x25, #0x7
	lsr	x23, x23, x26
Ltmp4866:
	ands	w25, w25, #0x7
Ltmp4867:
	b.eq	LBB57_13
Ltmp4868:
; %bb.19:                               ;   in Loop: Header=BB57_15 Depth=3
	sub	w25, w15, w25
Ltmp4869:
	cmp	w25, w22
	b.hs	LBB57_13
Ltmp4870:
; %bb.20:                               ;   in Loop: Header=BB57_15 Depth=3
	add	x24, x24, x19
Ltmp4871:
	ldrb	w24, [x24, #8]
	lsl	x24, x24, x25
	orr	x23, x24, x23
Ltmp4872:
	b	LBB57_13
Ltmp4873:
LBB57_21:                               ;   in Loop: Header=BB57_15 Depth=3
	mov	x22, #0                         ; =0x0
Ltmp4874:
	b	LBB57_14
Ltmp4875:
LBB57_22:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x20, #0                         ; =0x0
	and	x21, x6, #0xfffffffc
	mov	x22, x12
	b	LBB57_25
Ltmp4876:
LBB57_23:                               ;   in Loop: Header=BB57_25 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4877:
	and	x24, x25, x24
Ltmp4878:
	ldrb	w25, [x5, #19]
	lsl	x24, x24, x25
Ltmp4879:
LBB57_24:                               ;   in Loop: Header=BB57_25 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x7
Ltmp4880:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4881:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4882:
	str	x23, [x22, #8]
	add	x20, x20, #4
Ltmp4883:
	add	x22, x22, #32
	cmp	x21, x20
	b.eq	LBB57_12
Ltmp4884:
LBB57_25:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w24, [x5, #52]
Ltmp4885:
	ldrb	w23, [x5, #53]
	cbz	w24, LBB57_32
Ltmp4886:
; %bb.26:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	x25, x20
Ltmp4887:
	cbz	w23, LBB57_28
Ltmp4888:
; %bb.27:                               ;   in Loop: Header=BB57_25 Depth=3
	ldrb	w25, [x5, #17]
	eor	x26, x20, #0xffffffff
	add	x25, x26, x25
Ltmp4889:
LBB57_28:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4890:
	lsr	x26, x27, #3
Ltmp4891:
	ldr	x25, [x19, x26]
Ltmp4892:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4893:
	ands	w27, w27, #0x7
Ltmp4894:
	b.eq	LBB57_31
Ltmp4895:
; %bb.29:                               ;   in Loop: Header=BB57_25 Depth=3
	sub	w27, w15, w27
Ltmp4896:
	cmp	w27, w24
	b.hs	LBB57_31
Ltmp4897:
; %bb.30:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x26, x26, x19
Ltmp4898:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4899:
LBB57_31:                               ;   in Loop: Header=BB57_25 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4900:
	and	x24, x25, x24
Ltmp4901:
	ldrb	w25, [x5, #19]
	lsl	x24, x24, x25
Ltmp4902:
	b	LBB57_33
Ltmp4903:
LBB57_32:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4904:
LBB57_33:                               ;   in Loop: Header=BB57_25 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x7
Ltmp4905:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4906:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4907:
	stur	x23, [x22, #-16]
Ltmp4908:
	ldrb	w24, [x5, #52]
Ltmp4909:
	ldrb	w23, [x5, #53]
	cbz	w24, LBB57_36
Ltmp4910:
; %bb.34:                               ;   in Loop: Header=BB57_25 Depth=3
	cbz	w23, LBB57_37
Ltmp4911:
; %bb.35:                               ;   in Loop: Header=BB57_25 Depth=3
	ldrb	w25, [x5, #17]
	eor	x26, x20, #0xfffffffe
	add	x25, x26, x25
	b	LBB57_38
Ltmp4912:
LBB57_36:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4913:
	b	LBB57_42
Ltmp4914:
LBB57_37:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x25, x20, #1
Ltmp4915:
LBB57_38:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4916:
	lsr	x26, x27, #3
Ltmp4917:
	ldr	x25, [x19, x26]
Ltmp4918:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4919:
	ands	w27, w27, #0x7
Ltmp4920:
	b.eq	LBB57_41
Ltmp4921:
; %bb.39:                               ;   in Loop: Header=BB57_25 Depth=3
	sub	w27, w15, w27
Ltmp4922:
	cmp	w27, w24
	b.hs	LBB57_41
Ltmp4923:
; %bb.40:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x26, x26, x19
Ltmp4924:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4925:
LBB57_41:                               ;   in Loop: Header=BB57_25 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4926:
	and	x24, x25, x24
Ltmp4927:
	ldrb	w25, [x5, #19]
	lsl	x24, x24, x25
Ltmp4928:
LBB57_42:                               ;   in Loop: Header=BB57_25 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x7
Ltmp4929:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4930:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4931:
	stur	x23, [x22, #-8]
Ltmp4932:
	ldrb	w24, [x5, #52]
Ltmp4933:
	ldrb	w23, [x5, #53]
	cbz	w24, LBB57_45
Ltmp4934:
; %bb.43:                               ;   in Loop: Header=BB57_25 Depth=3
	cbz	w23, LBB57_46
Ltmp4935:
; %bb.44:                               ;   in Loop: Header=BB57_25 Depth=3
	ldrb	w25, [x5, #17]
	eor	x26, x20, x9
	add	x25, x26, x25
	b	LBB57_47
Ltmp4936:
LBB57_45:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4937:
	b	LBB57_51
Ltmp4938:
LBB57_46:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x25, x20, #2
Ltmp4939:
LBB57_47:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4940:
	lsr	x26, x27, #3
Ltmp4941:
	ldr	x25, [x19, x26]
Ltmp4942:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4943:
	ands	w27, w27, #0x7
Ltmp4944:
	b.eq	LBB57_50
Ltmp4945:
; %bb.48:                               ;   in Loop: Header=BB57_25 Depth=3
	sub	w27, w15, w27
Ltmp4946:
	cmp	w27, w24
	b.hs	LBB57_50
Ltmp4947:
; %bb.49:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x26, x26, x19
Ltmp4948:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4949:
LBB57_50:                               ;   in Loop: Header=BB57_25 Depth=3
	lsl	x26, x14, x24
	cmp	w24, #64
	csinv	x24, x14, x26, hs
Ltmp4950:
	and	x24, x25, x24
Ltmp4951:
	ldrb	w25, [x5, #19]
	lsl	x24, x24, x25
Ltmp4952:
LBB57_51:                               ;   in Loop: Header=BB57_25 Depth=3
	cmp	w23, #0
	cneg	x23, x24, ne
	add	x23, x23, x7
Ltmp4953:
	and	x24, x23, #0x7fffffffffffffff
Ltmp4954:
	cmp	x23, #0
	csinv	x23, x24, x23, lt
Ltmp4955:
	str	x23, [x22]
Ltmp4956:
	ldrb	w24, [x5, #52]
Ltmp4957:
	ldrb	w23, [x5, #53]
	cbz	w24, LBB57_54
Ltmp4958:
; %bb.52:                               ;   in Loop: Header=BB57_25 Depth=3
	cbz	w23, LBB57_55
Ltmp4959:
; %bb.53:                               ;   in Loop: Header=BB57_25 Depth=3
	ldrb	w25, [x5, #17]
	eor	x26, x20, #0xfffffffc
	add	x25, x26, x25
	b	LBB57_56
Ltmp4960:
LBB57_54:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	x24, #0                         ; =0x0
Ltmp4961:
	b	LBB57_24
Ltmp4962:
LBB57_55:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x25, x20, #3
Ltmp4963:
LBB57_56:                               ;   in Loop: Header=BB57_25 Depth=3
	mov	w25, w25
	umull	x27, w25, w24
Ltmp4964:
	lsr	x26, x27, #3
Ltmp4965:
	ldr	x25, [x19, x26]
Ltmp4966:
	and	x28, x27, #0x7
	lsr	x25, x25, x28
Ltmp4967:
	ands	w27, w27, #0x7
Ltmp4968:
	b.eq	LBB57_23
Ltmp4969:
; %bb.57:                               ;   in Loop: Header=BB57_25 Depth=3
	sub	w27, w15, w27
Ltmp4970:
	cmp	w27, w24
	b.hs	LBB57_23
Ltmp4971:
; %bb.58:                               ;   in Loop: Header=BB57_25 Depth=3
	add	x26, x26, x19
Ltmp4972:
	ldrb	w26, [x26, #8]
	lsl	x26, x26, x27
	orr	x25, x26, x25
Ltmp4973:
	b	LBB57_23
Ltmp4974:
LBB57_59:                               ;   in Loop: Header=BB57_6 Depth=2
	ldr	x5, [x5, #40]
Ltmp4975:
	and	x7, x5, #0x7fffffffffffffff
Ltmp4976:
	cmp	x5, #0
	csinv	x5, x7, x5, lt
Ltmp4977:
	cmp	x6, #8
	b.hs	LBB57_67
Ltmp4978:
; %bb.60:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x7, #0                          ; =0x0
	b	LBB57_70
Ltmp4979:
LBB57_61:                               ;   in Loop: Header=BB57_6 Depth=2
	lsl	x19, x14, x7
	cmp	w7, #64
	csinv	x19, x14, x19, eq
Ltmp4980:
	ldrb	w20, [x5, #19]
Ltmp4981:
	ldr	x21, [x5, #40]
Ltmp4982:
	ldrb	w24, [x5, #53]
Ltmp4983:
	add	x22, x5, #56
Ltmp4984:
	and	x23, x6, #0x7
	cmp	x6, #8
	cbz	w24, LBB57_89
Ltmp4985:
; %bb.62:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x24, #0                         ; =0x0
Ltmp4986:
	b.hs	LBB57_94
Ltmp4987:
LBB57_63:                               ;   in Loop: Header=BB57_6 Depth=2
	cbnz	x23, LBB57_65
	b	LBB57_72
Ltmp4988:
LBB57_64:                               ;   in Loop: Header=BB57_65 Depth=3
	mov	w6, w6
	umull	x6, w6, w7
Ltmp4989:
	lsr	x25, x6, #3
	ldr	x25, [x22, x25]
Ltmp4990:
	and	x6, x6, #0x7
Ltmp4991:
	lsr	x6, x25, x6
	and	x6, x6, x19
Ltmp4992:
	lsl	x6, x6, x20
Ltmp4993:
	sub	x6, x21, x6
Ltmp4994:
	and	x25, x6, #0x7fffffffffffffff
	cmp	x6, #0
	csinv	x6, x25, x6, lt
Ltmp4995:
	str	x6, [x10, x24, lsl #3]
Ltmp4996:
	add	x24, x24, #1
Ltmp4997:
	subs	x23, x23, #1
	b.eq	LBB57_72
Ltmp4998:
LBB57_65:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w25, [x5, #53]
	mov	x6, x24
	cbz	w25, LBB57_64
Ltmp4999:
; %bb.66:                               ;   in Loop: Header=BB57_65 Depth=3
	ldrb	w6, [x5, #17]
	eor	x25, x24, #0xffffffff
	add	x6, x25, x6
	b	LBB57_64
Ltmp5000:
LBB57_67:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x7, x6, #0xfffffff8
	dup.2d	v0, x5
	mov	x19, x7
	mov	x20, x11
Ltmp5001:
LBB57_68:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	stp	q0, q0, [x20, #-32]
	stp	q0, q0, [x20], #64
	subs	x19, x19, #8
	b.ne	LBB57_68
Ltmp5002:
; %bb.69:                               ;   in Loop: Header=BB57_6 Depth=2
	cmp	x7, x6
	b.eq	LBB57_72
Ltmp5003:
LBB57_70:                               ;   in Loop: Header=BB57_6 Depth=2
	sub	x6, x6, x7
Ltmp5004:
	add	x7, x10, x7, lsl #3
Ltmp5005:
LBB57_71:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	str	x5, [x7], #8
Ltmp5006:
	subs	x6, x6, #1
Ltmp5007:
	b.ne	LBB57_71
Ltmp5008:
LBB57_72:                               ;   in Loop: Header=BB57_6 Depth=2
	; InlineAsm Start
	; InlineAsm End
Ltmp5009:
	ldr	w6, [x0]
Ltmp5010:
	cmp	w6, #4
	b.lo	LBB57_75
Ltmp5011:
; %bb.73:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x5, x6, #0xfffffffc
	sub	x7, x6, #4
	cmp	x7, #27
	b.hi	LBB57_76
Ltmp5012:
; %bb.74:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x7, #0                          ; =0x0
	b	LBB57_79
Ltmp5013:
LBB57_75:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x5, #0                          ; =0x0
	b	LBB57_81
Ltmp5014:
LBB57_76:                               ;   in Loop: Header=BB57_6 Depth=2
	lsr	x7, x7, #2
	add	x19, x7, #1
	and	x20, x19, #0x7ffffffffffffff8
	lsl	x7, x20, #2
	movi.2d	v3, #0000000000000000
	movi.2d	v4, #0000000000000000
	mov.d	v4[0], x4
	movi.2d	v2, #0000000000000000
	mov.d	v2[0], x17
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x2
	movi.2d	v0, #0000000000000000
	mov.d	v0[0], x3
	mov	x17, x20
Ltmp5015:
	movi.2d	v22, #0000000000000000
	mov	x2, x13
Ltmp5016:
	movi.2d	v23, #0000000000000000
	movi.2d	v19, #0000000000000000
	movi.2d	v20, #0000000000000000
	movi.2d	v21, #0000000000000000
	movi.2d	v16, #0000000000000000
	movi.2d	v17, #0000000000000000
	movi.2d	v18, #0000000000000000
	movi.2d	v5, #0000000000000000
	movi.2d	v6, #0000000000000000
	movi.2d	v7, #0000000000000000
Ltmp5017:
LBB57_77:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	sub	x3, x2, #128
	sub	x4, x2, #64
	ld4.2d	{ v24, v25, v26, v27 }, [x3]
	ld4.2d	{ v28, v29, v30, v31 }, [x4]
	mov	x3, x2
	ld4.2d	{ v8, v9, v10, v11 }, [x3], #64
	ld4.2d	{ v12, v13, v14, v15 }, [x3]
	add.2d	v4, v24, v4
	add.2d	v3, v28, v3
	add.2d	v22, v8, v22
	add.2d	v23, v12, v23
	add.2d	v0, v25, v0
	add.2d	v5, v29, v5
	add.2d	v6, v9, v6
	add.2d	v7, v13, v7
	add.2d	v1, v26, v1
	add.2d	v16, v30, v16
	add.2d	v17, v10, v17
	add.2d	v18, v14, v18
	add.2d	v2, v27, v2
	add.2d	v19, v31, v19
	add.2d	v20, v11, v20
	add.2d	v21, v15, v21
	add	x2, x2, #256
	subs	x17, x17, #8
	b.ne	LBB57_77
Ltmp5018:
; %bb.78:                               ;   in Loop: Header=BB57_6 Depth=2
	add.2d	v3, v3, v4
	add.2d	v3, v22, v3
	add.2d	v3, v23, v3
	addp.2d	d3, v3
	fmov	x4, d3
	add.2d	v2, v19, v2
	add.2d	v2, v20, v2
	add.2d	v2, v21, v2
	addp.2d	d2, v2
	fmov	x17, d2
	add.2d	v1, v16, v1
	add.2d	v1, v17, v1
	add.2d	v1, v18, v1
	addp.2d	d1, v1
	fmov	x2, d1
	add.2d	v0, v5, v0
	add.2d	v0, v6, v0
	add.2d	v0, v7, v0
	addp.2d	d0, v0
	fmov	x3, d0
	cmp	x19, x20
	b.eq	LBB57_81
Ltmp5019:
LBB57_79:                               ;   in Loop: Header=BB57_6 Depth=2
	add	x19, x7, #3
	add	x7, x12, x7, lsl #3
Ltmp5020:
LBB57_80:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	x20, x21, [x7, #-16]
	add	x4, x20, x4
Ltmp5021:
	add	x3, x21, x3
Ltmp5022:
	ldp	x20, x21, [x7], #32
	add	x2, x20, x2
Ltmp5023:
	add	x17, x21, x17
Ltmp5024:
	add	x19, x19, #4
Ltmp5025:
	cmp	x19, x6
	b.lo	LBB57_80
Ltmp5026:
LBB57_81:                               ;   in Loop: Header=BB57_6 Depth=2
	cmp	x5, x6
	b.hs	LBB57_5
Ltmp5027:
; %bb.82:                               ;   in Loop: Header=BB57_6 Depth=2
	sub	x19, x6, x5
	cmp	x19, #7
	b.hi	LBB57_84
Ltmp5028:
; %bb.83:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x7, x5
	b	LBB57_87
Ltmp5029:
LBB57_84:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x20, x19, #0xfffffffffffffff8
	add	x7, x20, x5
	movi.2d	v0, #0000000000000000
	movi.2d	v1, #0000000000000000
	mov.d	v1[0], x4
	add	x4, x11, x5, lsl #3
Ltmp5030:
	mov	x5, x20
Ltmp5031:
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
Ltmp5032:
LBB57_85:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	q4, q5, [x4, #-32]
	ldp	q6, q7, [x4], #64
	add.2d	v1, v4, v1
	add.2d	v0, v5, v0
	add.2d	v2, v6, v2
	add.2d	v3, v7, v3
	subs	x5, x5, #8
	b.ne	LBB57_85
Ltmp5033:
; %bb.86:                               ;   in Loop: Header=BB57_6 Depth=2
	add.2d	v0, v0, v1
	add.2d	v0, v2, v0
	add.2d	v0, v3, v0
	addp.2d	d0, v0
	fmov	x4, d0
	cmp	x19, x20
	b.eq	LBB57_5
Ltmp5034:
LBB57_87:                               ;   in Loop: Header=BB57_6 Depth=2
	add	x5, x10, x7, lsl #3
	sub	x7, x6, x7
Ltmp5035:
LBB57_88:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	x19, [x5], #8
	add	x4, x19, x4
Ltmp5036:
	subs	x7, x7, #1
	b.ne	LBB57_88
	b	LBB57_5
Ltmp5037:
LBB57_89:                               ;   in Loop: Header=BB57_6 Depth=2
	mov	x24, #0                         ; =0x0
Ltmp5038:
	b.hs	LBB57_119
Ltmp5039:
LBB57_90:                               ;   in Loop: Header=BB57_6 Depth=2
	cbnz	x23, LBB57_92
	b	LBB57_72
Ltmp5040:
LBB57_91:                               ;   in Loop: Header=BB57_92 Depth=3
	mov	w6, w6
	umull	x6, w6, w7
Ltmp5041:
	lsr	x25, x6, #3
	ldr	x25, [x22, x25]
Ltmp5042:
	and	x6, x6, #0x7
Ltmp5043:
	lsr	x6, x25, x6
	and	x6, x6, x19
Ltmp5044:
	lsl	x6, x6, x20
Ltmp5045:
	add	x6, x6, x21
Ltmp5046:
	and	x25, x6, #0x7fffffffffffffff
	cmp	x6, #0
	csinv	x6, x25, x6, lt
Ltmp5047:
	str	x6, [x10, x24, lsl #3]
Ltmp5048:
	add	x24, x24, #1
Ltmp5049:
	subs	x23, x23, #1
	b.eq	LBB57_72
Ltmp5050:
LBB57_92:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w25, [x5, #53]
	mov	x6, x24
	cbz	w25, LBB57_91
Ltmp5051:
; %bb.93:                               ;   in Loop: Header=BB57_92 Depth=3
	ldrb	w6, [x5, #17]
	eor	x25, x24, #0xffffffff
	add	x6, x25, x6
	b	LBB57_91
Ltmp5052:
LBB57_94:                               ;   in Loop: Header=BB57_6 Depth=2
	and	x6, x6, #0xfffffff8
Ltmp5053:
	mov	x25, x11
	b	LBB57_97
Ltmp5054:
LBB57_95:                               ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #7
Ltmp5055:
LBB57_96:                               ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5056:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5057:
	and	x26, x26, #0x7
Ltmp5058:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5059:
	lsl	x26, x26, x20
Ltmp5060:
	sub	x26, x21, x26
Ltmp5061:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5062:
	str	x26, [x25, #24]
Ltmp5063:
	add	x24, x24, #8
Ltmp5064:
	add	x25, x25, #64
	cmp	x6, x24
	b.eq	LBB57_63
Ltmp5065:
LBB57_97:                               ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w27, [x5, #53]
	mov	x26, x24
	cbz	w27, LBB57_99
Ltmp5066:
; %bb.98:                               ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xffffffff
	add	x26, x27, x26
Ltmp5067:
LBB57_99:                               ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5068:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5069:
	and	x26, x26, #0x7
Ltmp5070:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5071:
	lsl	x26, x26, x20
Ltmp5072:
	sub	x26, x21, x26
Ltmp5073:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5074:
	stur	x26, [x25, #-32]
Ltmp5075:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_101
Ltmp5076:
; %bb.100:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffffe
	add	x26, x27, x26
	b	LBB57_102
Ltmp5077:
LBB57_101:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #1
Ltmp5078:
LBB57_102:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5079:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5080:
	and	x26, x26, #0x7
Ltmp5081:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5082:
	lsl	x26, x26, x20
Ltmp5083:
	sub	x26, x21, x26
Ltmp5084:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5085:
	stur	x26, [x25, #-24]
Ltmp5086:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_104
Ltmp5087:
; %bb.103:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, x9
	add	x26, x27, x26
	b	LBB57_105
Ltmp5088:
LBB57_104:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #2
Ltmp5089:
LBB57_105:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5090:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5091:
	and	x26, x26, #0x7
Ltmp5092:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5093:
	lsl	x26, x26, x20
Ltmp5094:
	sub	x26, x21, x26
Ltmp5095:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5096:
	stur	x26, [x25, #-16]
Ltmp5097:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_107
Ltmp5098:
; %bb.106:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffffc
	add	x26, x27, x26
	b	LBB57_108
Ltmp5099:
LBB57_107:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #3
Ltmp5100:
LBB57_108:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5101:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5102:
	and	x26, x26, #0x7
Ltmp5103:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5104:
	lsl	x26, x26, x20
Ltmp5105:
	sub	x26, x21, x26
Ltmp5106:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5107:
	stur	x26, [x25, #-8]
Ltmp5108:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_110
Ltmp5109:
; %bb.109:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #2
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_111
Ltmp5110:
LBB57_110:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #4
Ltmp5111:
LBB57_111:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5112:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5113:
	and	x26, x26, #0x7
Ltmp5114:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5115:
	lsl	x26, x26, x20
Ltmp5116:
	sub	x26, x21, x26
Ltmp5117:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5118:
	str	x26, [x25]
Ltmp5119:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_113
Ltmp5120:
; %bb.112:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #3
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_114
Ltmp5121:
LBB57_113:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #5
Ltmp5122:
LBB57_114:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5123:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5124:
	and	x26, x26, #0x7
Ltmp5125:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5126:
	lsl	x26, x26, x20
Ltmp5127:
	sub	x26, x21, x26
Ltmp5128:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5129:
	str	x26, [x25, #8]
Ltmp5130:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_116
Ltmp5131:
; %bb.115:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #4
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_117
Ltmp5132:
LBB57_116:                              ;   in Loop: Header=BB57_97 Depth=3
	add	x26, x24, #6
Ltmp5133:
LBB57_117:                              ;   in Loop: Header=BB57_97 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5134:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5135:
	and	x26, x26, #0x7
Ltmp5136:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5137:
	lsl	x26, x26, x20
Ltmp5138:
	sub	x26, x21, x26
Ltmp5139:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5140:
	str	x26, [x25, #16]
Ltmp5141:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_95
Ltmp5142:
; %bb.118:                              ;   in Loop: Header=BB57_97 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffff8
	add	x26, x27, x26
	b	LBB57_96
Ltmp5143:
LBB57_119:                              ;   in Loop: Header=BB57_6 Depth=2
	and	x6, x6, #0xfffffff8
Ltmp5144:
	mov	x25, x11
	b	LBB57_122
Ltmp5145:
LBB57_120:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffff8
	add	x26, x27, x26
Ltmp5146:
LBB57_121:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5147:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5148:
	and	x26, x26, #0x7
Ltmp5149:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5150:
	lsl	x26, x26, x20
Ltmp5151:
	add	x26, x26, x21
Ltmp5152:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5153:
	str	x26, [x25, #24]
Ltmp5154:
	add	x24, x24, #8
Ltmp5155:
	add	x25, x25, #64
	cmp	x6, x24
	b.eq	LBB57_90
Ltmp5156:
LBB57_122:                              ;   Parent Loop BB57_3 Depth=1
                                        ;     Parent Loop BB57_6 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrb	w27, [x5, #53]
	mov	x26, x24
	cbz	w27, LBB57_124
Ltmp5157:
; %bb.123:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xffffffff
	add	x26, x27, x26
Ltmp5158:
LBB57_124:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5159:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5160:
	and	x26, x26, #0x7
Ltmp5161:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5162:
	lsl	x26, x26, x20
Ltmp5163:
	add	x26, x26, x21
Ltmp5164:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5165:
	stur	x26, [x25, #-32]
Ltmp5166:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_126
Ltmp5167:
; %bb.125:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffffe
	add	x26, x27, x26
	b	LBB57_127
Ltmp5168:
LBB57_126:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #1
Ltmp5169:
LBB57_127:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5170:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5171:
	and	x26, x26, #0x7
Ltmp5172:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5173:
	lsl	x26, x26, x20
Ltmp5174:
	add	x26, x26, x21
Ltmp5175:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5176:
	stur	x26, [x25, #-24]
Ltmp5177:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_129
Ltmp5178:
; %bb.128:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, x9
	add	x26, x27, x26
	b	LBB57_130
Ltmp5179:
LBB57_129:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #2
Ltmp5180:
LBB57_130:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5181:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5182:
	and	x26, x26, #0x7
Ltmp5183:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5184:
	lsl	x26, x26, x20
Ltmp5185:
	add	x26, x26, x21
Ltmp5186:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5187:
	stur	x26, [x25, #-16]
Ltmp5188:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_132
Ltmp5189:
; %bb.131:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	eor	x27, x24, #0xfffffffc
	add	x26, x27, x26
	b	LBB57_133
Ltmp5190:
LBB57_132:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #3
Ltmp5191:
LBB57_133:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5192:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5193:
	and	x26, x26, #0x7
Ltmp5194:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5195:
	lsl	x26, x26, x20
Ltmp5196:
	add	x26, x26, x21
Ltmp5197:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5198:
	stur	x26, [x25, #-8]
Ltmp5199:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_135
Ltmp5200:
; %bb.134:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #2
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_136
Ltmp5201:
LBB57_135:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #4
Ltmp5202:
LBB57_136:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5203:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5204:
	and	x26, x26, #0x7
Ltmp5205:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5206:
	lsl	x26, x26, x20
Ltmp5207:
	add	x26, x26, x21
Ltmp5208:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5209:
	str	x26, [x25]
Ltmp5210:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_138
Ltmp5211:
; %bb.137:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #3
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_139
Ltmp5212:
LBB57_138:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #5
Ltmp5213:
LBB57_139:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5214:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5215:
	and	x26, x26, #0x7
Ltmp5216:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5217:
	lsl	x26, x26, x20
Ltmp5218:
	add	x26, x26, x21
Ltmp5219:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5220:
	str	x26, [x25, #8]
Ltmp5221:
	ldrb	w26, [x5, #53]
	cbz	w26, LBB57_141
Ltmp5222:
; %bb.140:                              ;   in Loop: Header=BB57_122 Depth=3
	ldrb	w26, [x5, #17]
	sub	x27, x9, #4
	eor	x27, x24, x27
	add	x26, x27, x26
	b	LBB57_142
Ltmp5223:
LBB57_141:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #6
Ltmp5224:
LBB57_142:                              ;   in Loop: Header=BB57_122 Depth=3
	mov	w26, w26
	umull	x26, w26, w7
Ltmp5225:
	lsr	x27, x26, #3
	ldr	x27, [x22, x27]
Ltmp5226:
	and	x26, x26, #0x7
Ltmp5227:
	lsr	x26, x27, x26
	and	x26, x26, x19
Ltmp5228:
	lsl	x26, x26, x20
Ltmp5229:
	add	x26, x26, x21
Ltmp5230:
	and	x27, x26, #0x7fffffffffffffff
	cmp	x26, #0
	csinv	x26, x27, x26, lt
Ltmp5231:
	str	x26, [x25, #16]
Ltmp5232:
	ldrb	w26, [x5, #53]
	cbnz	w26, LBB57_120
Ltmp5233:
; %bb.143:                              ;   in Loop: Header=BB57_122 Depth=3
	add	x26, x24, #7
	b	LBB57_121
Ltmp5234:
LBB57_144:
	add	x8, x2, x3
	add	x9, x17, x4
	add	x0, x8, x9
Ltmp5235:
	ldur	x8, [x29, #-160]
Lloh360:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh361:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh362:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB57_147
Ltmp5236:
LBB57_145:
	add	sp, sp, #784
	ldp	x29, x30, [sp, #144]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #128]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #112]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #96]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #80]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #64]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp, #48]               ; 16-byte Folded Reload
	ldp	d11, d10, [sp, #32]             ; 16-byte Folded Reload
	ldp	d13, d12, [sp, #16]             ; 16-byte Folded Reload
	ldp	d15, d14, [sp], #160            ; 16-byte Folded Reload
	ret
Ltmp5237:
LBB57_146:
	mov	x0, #0                          ; =0x0
Ltmp5238:
	ldur	x8, [x29, #-160]
Lloh363:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh364:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh365:
	ldr	x9, [x9]
	cmp	x9, x8
	b.eq	LBB57_145
Ltmp5239:
LBB57_147:
	bl	___stack_chk_fail
Ltmp5240:
	.loh AdrpLdrGotLdr	Lloh357, Lloh358, Lloh359
	.loh AdrpLdrGotLdr	Lloh360, Lloh361, Lloh362
	.loh AdrpLdrGotLdr	Lloh363, Lloh364, Lloh365
Lfunc_end57:
