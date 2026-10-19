
scratch/arm-corrected-neon/B/build/btree-bench:     file format elf64-littleaarch64


Disassembly of section .init:

Disassembly of section .plt:

Disassembly of section .text:

0000000000000f18 <main>:
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:103
    serverAssert(id < check->n && score == (double)id);
    serverAssert(len == sdslen(check->keys[id]) && !memcmp(key, check->keys[id], len));
    check->seen[id] = 1;
    scan_count(&check->result, key, len, score);
}
int main(int argc, char **argv) {
     f18:	d10743ff 	sub	sp, sp, #0x1d0
     f1c:	fd00b3e8 	str	d8, [sp, #352]
     f20:	a9177bfd 	stp	x29, x30, [sp, #368]
     f24:	a9186ffc 	stp	x28, x27, [sp, #384]
     f28:	a91967fa 	stp	x26, x25, [sp, #400]
     f2c:	a91a5ff8 	stp	x24, x23, [sp, #416]
     f30:	a91b57f6 	stp	x22, x21, [sp, #432]
     f34:	a91c4ff4 	stp	x20, x19, [sp, #448]
     f38:	9105c3fd 	add	x29, sp, #0x170
     f3c:	52884817 	mov	w23, #0x4240                	// #16960
     f40:	5290d413 	mov	w19, #0x86a0                	// #34464
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:108
    size_t n = 100000, ops = 1000000, bytes = 16, warmup_passes = 1;
    uint64_t seed = 1;
    const char *selected = "all";
    const char *cases[] = {"insert", "lookup-hit", "lookup-miss", "rank", "iterate", "scan", "update", "delete"};
    for (int i = 1; i < argc; i++) {
     f44:	7100081f 	cmp	w0, #0x2
     f48:	72a001f7 	movk	w23, #0xf, lsl #16
     f4c:	72a00033 	movk	w19, #0x1, lsl #16
     f50:	5400178b 	b.lt	1240 <main+0x328>  // b.tstop
     f54:	2a0003e8 	mov	w8, w0
     f58:	529c201a 	mov	w26, #0xe100                	// #57600
     f5c:	aa0103f5 	mov	x21, x1
     f60:	d1000908 	sub	x8, x8, #0x2
     f64:	2a0003f6 	mov	w22, w0
     f68:	aa1f03fb 	mov	x27, xzr
     f6c:	f81983a8 	stur	x8, [x29, #-104]
     f70:	52800028 	mov	w8, #0x1                   	// #1
     f74:	b0000099 	adrp	x25, 11000 <sdsnew+0x94>
     f78:	9115d339 	add	x25, x25, #0x574
     f7c:	f90047e8 	str	x8, [sp, #136]
     f80:	52800208 	mov	w8, #0x10                  	// #16
     f84:	b0000098 	adrp	x24, 11000 <sdsnew+0x94>
     f88:	9116db18 	add	x24, x24, #0x5b6
     f8c:	72a0beba 	movk	w26, #0x5f5, lsl #16
     f90:	f90043e8 	str	x8, [sp, #128]
     f94:	52800028 	mov	w8, #0x1                   	// #1
     f98:	f9004be8 	str	x8, [sp, #144]
     f9c:	14000008 	b	fbc <main+0xa4>
     fa0:	f90043e0 	str	x0, [sp, #128]
     fa4:	aa1903f4 	mov	x20, x25
     fa8:	91000b7b 	add	x27, x27, #0x2
     fac:	aa1403f9 	mov	x25, x20
     fb0:	11000768 	add	w8, w27, #0x1
     fb4:	6b16011f 	cmp	w8, w22
     fb8:	5400154a 	b.ge	1260 <main+0x348>  // b.tcont
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:109
        if (!strcmp(argv[i], "--help")) {
     fbc:	8b1b0eb4 	add	x20, x21, x27, lsl #3
     fc0:	aa1803e1 	mov	x1, x24
     fc4:	f940069c 	ldr	x28, [x20, #8]
     fc8:	aa1c03e0 	mov	x0, x28
     fcc:	97ffff65 	bl	d60 <strcmp@plt>
     fd0:	34008020 	cbz	w0, 1fd4 <main+0x10bc>
     fd4:	f85983a8 	ldur	x8, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:113
            puts("btree-bench [--size N] [--ops N] [--member-bytes N>=8] [--seed N] [--warmup-passes N>=1] [--case all|insert|lookup-hit|lookup-miss|rank|iterate|scan|update|delete]");
            return 0;
        }
        if (i + 1 == argc) { fprintf(stderr, "Missing value: %s\n", argv[i]); return 2; }
     fd8:	eb1b011f 	cmp	x8, x27
     fdc:	54008280 	b.eq	202c <main+0x1114>  // b.none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:114
        const char *arg = argv[i++], *value = argv[i];
     fe0:	f9400a94 	ldr	x20, [x20, #16]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:115
        if (!strcmp(arg, "--size")) n = number(value);
     fe4:	aa1c03e0 	mov	x0, x28
     fe8:	b0000081 	adrp	x1, 11000 <sdsnew+0x94>
     fec:	9119d021 	add	x1, x1, #0x674
     ff0:	97ffff5c 	bl	d60 <strcmp@plt>
     ff4:	34000360 	cbz	w0, 1060 <main+0x148>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:116
        else if (!strcmp(arg, "--ops")) ops = number(value);
     ff8:	aa1c03e0 	mov	x0, x28
     ffc:	b0000081 	adrp	x1, 11000 <sdsnew+0x94>
    1000:	9119ec21 	add	x1, x1, #0x67b
    1004:	97ffff57 	bl	d60 <strcmp@plt>
    1008:	34000560 	cbz	w0, 10b4 <main+0x19c>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:117
        else if (!strcmp(arg, "--member-bytes")) bytes = number(value);
    100c:	aa1c03e0 	mov	x0, x28
    1010:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1014:	911a0421 	add	x1, x1, #0x681
    1018:	97ffff52 	bl	d60 <strcmp@plt>
    101c:	340007a0 	cbz	w0, 1110 <main+0x1f8>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:118
        else if (!strcmp(arg, "--seed")) seed = number(value);
    1020:	aa1c03e0 	mov	x0, x28
    1024:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1028:	911a4021 	add	x1, x1, #0x690
    102c:	97ffff4d 	bl	d60 <strcmp@plt>
    1030:	34000980 	cbz	w0, 1160 <main+0x248>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:119
        else if (!strcmp(arg, "--warmup-passes")) warmup_passes = number(value);
    1034:	aa1c03e0 	mov	x0, x28
    1038:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    103c:	911a5c21 	add	x1, x1, #0x697
    1040:	97ffff48 	bl	d60 <strcmp@plt>
    1044:	34000bc0 	cbz	w0, 11bc <main+0x2a4>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:120
        else if (!strcmp(arg, "--case")) selected = value;
    1048:	aa1c03e0 	mov	x0, x28
    104c:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1050:	911a9c21 	add	x1, x1, #0x6a7
    1054:	97ffff43 	bl	d60 <strcmp@plt>
    1058:	34fffa80 	cbz	w0, fa8 <main+0x90>
    105c:	14000403 	b	2068 <main+0x1150>
number():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:71
    errno = 0;
    1060:	97ffff54 	bl	db0 <__errno_location@plt>
    1064:	aa0003f3 	mov	x19, x0
    1068:	b900001f 	str	wzr, [x0]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:72
    unsigned long long v = strtoull(s, &end, 10);
    106c:	d10103a1 	sub	x1, x29, #0x40
    1070:	aa1403e0 	mov	x0, x20
    1074:	52800142 	mov	w2, #0xa                   	// #10
    1078:	97ffff02 	bl	c80 <__isoc23_strtoull@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:73
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
    107c:	b9400268 	ldr	w8, [x19]
    1080:	35008448 	cbnz	w8, 2108 <main+0x11f0>
    1084:	39400288 	ldrb	w8, [x20]
    1088:	7100b51f 	cmp	w8, #0x2d
    108c:	540083e0 	b.eq	2108 <main+0x11f0>  // b.none
    1090:	f85c03a9 	ldur	x9, [x29, #-64]
    1094:	39400129 	ldrb	w9, [x9]
    1098:	35008389 	cbnz	w9, 2108 <main+0x11f0>
    109c:	34008368 	cbz	w8, 2108 <main+0x11f0>
    10a0:	aa0003f3 	mov	x19, x0
    10a4:	b4008320 	cbz	x0, 2108 <main+0x11f0>
    10a8:	eb1a027f 	cmp	x19, x26
    10ac:	54fff7c9 	b.ls	fa4 <main+0x8c>  // b.plast
    10b0:	14000416 	b	2108 <main+0x11f0>
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:71
    errno = 0;
    10b4:	97ffff3f 	bl	db0 <__errno_location@plt>
    10b8:	aa1403f7 	mov	x23, x20
    10bc:	aa0003f4 	mov	x20, x0
    10c0:	b900001f 	str	wzr, [x0]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:72
    unsigned long long v = strtoull(s, &end, 10);
    10c4:	d10103a1 	sub	x1, x29, #0x40
    10c8:	aa1703e0 	mov	x0, x23
    10cc:	52800142 	mov	w2, #0xa                   	// #10
    10d0:	97fffeec 	bl	c80 <__isoc23_strtoull@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:73
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
    10d4:	b9400288 	ldr	w8, [x20]
    10d8:	aa1703e2 	mov	x2, x23
    10dc:	35008408 	cbnz	w8, 215c <main+0x1244>
    10e0:	39400048 	ldrb	w8, [x2]
    10e4:	7100b51f 	cmp	w8, #0x2d
    10e8:	540083a0 	b.eq	215c <main+0x1244>  // b.none
    10ec:	f85c03a9 	ldur	x9, [x29, #-64]
    10f0:	39400129 	ldrb	w9, [x9]
    10f4:	35008349 	cbnz	w9, 215c <main+0x1244>
    10f8:	34008328 	cbz	w8, 215c <main+0x1244>
    10fc:	aa0003f7 	mov	x23, x0
    1100:	b40082e0 	cbz	x0, 215c <main+0x1244>
    1104:	eb1a02ff 	cmp	x23, x26
    1108:	54fff4e9 	b.ls	fa4 <main+0x8c>  // b.plast
    110c:	14000414 	b	215c <main+0x1244>
number():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:71
    errno = 0;
    1110:	97ffff28 	bl	db0 <__errno_location@plt>
    1114:	aa0003fc 	mov	x28, x0
    1118:	b900001f 	str	wzr, [x0]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:72
    unsigned long long v = strtoull(s, &end, 10);
    111c:	d10103a1 	sub	x1, x29, #0x40
    1120:	aa1403e0 	mov	x0, x20
    1124:	52800142 	mov	w2, #0xa                   	// #10
    1128:	97fffed6 	bl	c80 <__isoc23_strtoull@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:73
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
    112c:	b9400388 	ldr	w8, [x28]
    1130:	35007ec8 	cbnz	w8, 2108 <main+0x11f0>
    1134:	39400288 	ldrb	w8, [x20]
    1138:	7100b51f 	cmp	w8, #0x2d
    113c:	54007e60 	b.eq	2108 <main+0x11f0>  // b.none
    1140:	f85c03a9 	ldur	x9, [x29, #-64]
    1144:	39400129 	ldrb	w9, [x9]
    1148:	35007e09 	cbnz	w9, 2108 <main+0x11f0>
    114c:	34007de8 	cbz	w8, 2108 <main+0x11f0>
    1150:	b4007dc0 	cbz	x0, 2108 <main+0x11f0>
    1154:	eb1a001f 	cmp	x0, x26
    1158:	54fff249 	b.ls	fa0 <main+0x88>  // b.plast
    115c:	140003eb 	b	2108 <main+0x11f0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:71
    errno = 0;
    1160:	97ffff14 	bl	db0 <__errno_location@plt>
    1164:	aa0003fc 	mov	x28, x0
    1168:	b900001f 	str	wzr, [x0]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:72
    unsigned long long v = strtoull(s, &end, 10);
    116c:	d10103a1 	sub	x1, x29, #0x40
    1170:	aa1403e0 	mov	x0, x20
    1174:	52800142 	mov	w2, #0xa                   	// #10
    1178:	97fffec2 	bl	c80 <__isoc23_strtoull@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:73
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
    117c:	b9400388 	ldr	w8, [x28]
    1180:	f9004be0 	str	x0, [sp, #144]
    1184:	35007c28 	cbnz	w8, 2108 <main+0x11f0>
    1188:	39400288 	ldrb	w8, [x20]
    118c:	7100b51f 	cmp	w8, #0x2d
    1190:	54007bc0 	b.eq	2108 <main+0x11f0>  // b.none
    1194:	f85c03a9 	ldur	x9, [x29, #-64]
    1198:	39400129 	ldrb	w9, [x9]
    119c:	35007b69 	cbnz	w9, 2108 <main+0x11f0>
    11a0:	34007b48 	cbz	w8, 2108 <main+0x11f0>
    11a4:	f9404be8 	ldr	x8, [sp, #144]
    11a8:	b4007b08 	cbz	x8, 2108 <main+0x11f0>
    11ac:	f9404be8 	ldr	x8, [sp, #144]
    11b0:	eb1a011f 	cmp	x8, x26
    11b4:	54ffef89 	b.ls	fa4 <main+0x8c>  // b.plast
    11b8:	140003d4 	b	2108 <main+0x11f0>
main():
    11bc:	aa1803fa 	mov	x26, x24
    11c0:	aa1703f8 	mov	x24, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:71
    errno = 0;
    11c4:	97fffefb 	bl	db0 <__errno_location@plt>
    11c8:	aa0003f7 	mov	x23, x0
    11cc:	b900001f 	str	wzr, [x0]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:72
    unsigned long long v = strtoull(s, &end, 10);
    11d0:	d10103a1 	sub	x1, x29, #0x40
    11d4:	aa1403e0 	mov	x0, x20
    11d8:	52800142 	mov	w2, #0xa                   	// #10
    11dc:	aa1403fc 	mov	x28, x20
    11e0:	97fffea8 	bl	c80 <__isoc23_strtoull@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:73
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
    11e4:	b94002e8 	ldr	w8, [x23]
    11e8:	f90047e0 	str	x0, [sp, #136]
    11ec:	35007ec8 	cbnz	w8, 21c4 <main+0x12ac>
    11f0:	39400388 	ldrb	w8, [x28]
    11f4:	7100b51f 	cmp	w8, #0x2d
    11f8:	54007e60 	b.eq	21c4 <main+0x12ac>  // b.none
    11fc:	f85c03a9 	ldur	x9, [x29, #-64]
    1200:	39400129 	ldrb	w9, [x9]
    1204:	35007e09 	cbnz	w9, 21c4 <main+0x12ac>
    1208:	34007de8 	cbz	w8, 21c4 <main+0x12ac>
    120c:	f94047e8 	ldr	x8, [sp, #136]
    1210:	b4007da8 	cbz	x8, 21c4 <main+0x12ac>
    1214:	f94047e8 	ldr	x8, [sp, #136]
    1218:	529c2009 	mov	w9, #0xe100                	// #57600
    121c:	72a0bea9 	movk	w9, #0x5f5, lsl #16
    1220:	eb09011f 	cmp	x8, x9
    1224:	54007d08 	b.hi	21c4 <main+0x12ac>  // b.pmore
    1228:	aa1803f7 	mov	x23, x24
    122c:	aa1a03f8 	mov	x24, x26
    1230:	529c201a 	mov	w26, #0xe100                	// #57600
    1234:	aa1903f4 	mov	x20, x25
    1238:	72a0beba 	movk	w26, #0x5f5, lsl #16
    123c:	17ffff5b 	b	fa8 <main+0x90>
    1240:	52800208 	mov	w8, #0x10                  	// #16
    1244:	90000094 	adrp	x20, 11000 <sdsnew+0x94>
    1248:	9115d294 	add	x20, x20, #0x574
    124c:	f90043e8 	str	x8, [sp, #128]
    1250:	52800028 	mov	w8, #0x1                   	// #1
    1254:	f9004be8 	str	x8, [sp, #144]
    1258:	52800028 	mov	w8, #0x1                   	// #1
    125c:	f90047e8 	str	x8, [sp, #136]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:123
        else { fprintf(stderr, "Unknown option: %s\n", arg); return 2; }
    }
    int valid_case = !strcmp(selected, "all");
    1260:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1264:	9115d021 	add	x1, x1, #0x574
    1268:	aa1403e0 	mov	x0, x20
    126c:	97fffebd 	bl	d60 <strcmp@plt>
    1270:	b81983a0 	stur	w0, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:124
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) valid_case |= !strcmp(selected, cases[c]);
    1274:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1278:	9115e021 	add	x1, x1, #0x578
    127c:	aa1403e0 	mov	x0, x20
    1280:	97fffeb8 	bl	d60 <strcmp@plt>
    1284:	2a0003f6 	mov	w22, w0
    1288:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    128c:	9115fc21 	add	x1, x1, #0x57f
    1290:	aa1403e0 	mov	x0, x20
    1294:	97fffeb3 	bl	d60 <strcmp@plt>
    1298:	2a0003f8 	mov	w24, w0
    129c:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    12a0:	91162821 	add	x1, x1, #0x58a
    12a4:	aa1403e0 	mov	x0, x20
    12a8:	97fffeae 	bl	d60 <strcmp@plt>
    12ac:	2a0003f9 	mov	w25, w0
    12b0:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    12b4:	91165821 	add	x1, x1, #0x596
    12b8:	aa1403e0 	mov	x0, x20
    12bc:	97fffea9 	bl	d60 <strcmp@plt>
    12c0:	2a0003fa 	mov	w26, w0
    12c4:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    12c8:	91166c21 	add	x1, x1, #0x59b
    12cc:	aa1403e0 	mov	x0, x20
    12d0:	97fffea4 	bl	d60 <strcmp@plt>
    12d4:	2a0003fb 	mov	w27, w0
    12d8:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    12dc:	91168c21 	add	x1, x1, #0x5a3
    12e0:	aa1403e0 	mov	x0, x20
    12e4:	97fffe9f 	bl	d60 <strcmp@plt>
    12e8:	2a0003fc 	mov	w28, w0
    12ec:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    12f0:	9116a021 	add	x1, x1, #0x5a8
    12f4:	aa1403e0 	mov	x0, x20
    12f8:	97fffe9a 	bl	d60 <strcmp@plt>
    12fc:	2a0003f5 	mov	w21, w0
    1300:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    1304:	9116bc21 	add	x1, x1, #0x5af
    1308:	aa1403e0 	mov	x0, x20
    130c:	97fffe95 	bl	d60 <strcmp@plt>
    1310:	b85983a8 	ldur	w8, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:123
    int valid_case = !strcmp(selected, "all");
    1314:	7100011f 	cmp	w8, #0x0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:124
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) valid_case |= !strcmp(selected, cases[c]);
    1318:	7a401ac4 	ccmp	w22, #0x0, #0x4, ne	// ne = any
    131c:	7a401b04 	ccmp	w24, #0x0, #0x4, ne	// ne = any
    1320:	7a401b24 	ccmp	w25, #0x0, #0x4, ne	// ne = any
    1324:	7a401b44 	ccmp	w26, #0x0, #0x4, ne	// ne = any
    1328:	7a401b64 	ccmp	w27, #0x0, #0x4, ne	// ne = any
    132c:	7a401b84 	ccmp	w28, #0x0, #0x4, ne	// ne = any
    1330:	f94043fc 	ldr	x28, [sp, #128]
    1334:	7a401aa4 	ccmp	w21, #0x0, #0x4, ne	// ne = any
    1338:	7a401804 	ccmp	w0, #0x0, #0x4, ne	// ne = any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:125
    if (!valid_case || bytes < 8 || bytes > 65536) { fputs("Invalid case or member size (8..65536)\n", stderr); return 2; }
    133c:	54006661 	b.ne	2008 <main+0x10f0>  // b.any
    1340:	f100239f 	cmp	x28, #0x8
    1344:	54006623 	b.cc	2008 <main+0x10f0>  // b.lo, b.ul, b.last
    1348:	f140439f 	cmp	x28, #0x10, lsl #12
    134c:	540065e8 	b.hi	2008 <main+0x10f0>  // b.pmore
    1350:	f9004ff4 	str	x20, [sp, #152]
    1354:	d28f82b4 	mov	x20, #0x7c15                	// #31765
    1358:	f9404be4 	ldr	x4, [sp, #144]
    135c:	f2afe954 	movk	x20, #0x7f4a, lsl #16
    1360:	d29f0549 	mov	x9, #0xf82a                	// #63530
    1364:	d28e87ea 	mov	x10, #0x743f                	// #29759
    1368:	f2cf3734 	movk	x20, #0x79b9, lsl #32
    136c:	f2bfd289 	movk	x9, #0xfe94, lsl #16
    1370:	d29cb736 	mov	x22, #0xe5b9                	// #58809
    1374:	f2f3c6f4 	movk	x20, #0x9e37, lsl #48
    1378:	f2afbbea 	movk	x10, #0x7ddf, lsl #16
    137c:	f2de6e49 	movk	x9, #0xf372, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1380:	8b140088 	add	x8, x4, x20
    1384:	f2a39c96 	movk	x22, #0x1ce4, lsl #16
    1388:	f2cda58a 	movk	x10, #0x6d2c, lsl #32
    138c:	d29e0a8b 	mov	x11, #0xf054                	// #61524
    1390:	f2e78dc9 	movk	x9, #0x3c6e, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1394:	ca487908 	eor	x8, x8, x8, lsr #30
    1398:	f2c8edb6 	movk	x22, #0x476d, lsl #32
    139c:	f2fb54ca 	movk	x10, #0xdaa6, lsl #48
    13a0:	f2bfa52b 	movk	x11, #0xfd29, lsl #16
    13a4:	f2f7eb16 	movk	x22, #0xbf58, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    13a8:	8b090089 	add	x9, x4, x9
    13ac:	8b0a008a 	add	x10, x4, x10
    13b0:	f2dcdcab 	movk	x11, #0xe6e5, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    13b4:	ca497929 	eor	x9, x9, x9, lsr #30
    13b8:	9b167d08 	mul	x8, x8, x22
    13bc:	f2ef1bab 	movk	x11, #0x78dd, lsl #48
    13c0:	ca4a794a 	eor	x10, x10, x10, lsr #30
    13c4:	f81803b7 	stur	x23, [x29, #-128]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    13c8:	8b0b008b 	add	x11, x4, x11
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    13cc:	9b167d29 	mul	x9, x9, x22
    13d0:	d2823d77 	mov	x23, #0x11eb                	// #4587
    13d4:	ca4b796b 	eor	x11, x11, x11, lsr #30
    13d8:	f2a26637 	movk	x23, #0x1331, lsl #16
    13dc:	d28c926d 	mov	x13, #0x6493                	// #25747
    13e0:	9b167d4a 	mul	x10, x10, x22
    13e4:	f2c93777 	movk	x23, #0x49bb, lsl #32
    13e8:	f2af612d 	movk	x13, #0x7b09, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    13ec:	ca486d08 	eor	x8, x8, x8, lsr #27
    13f0:	f2f29a17 	movk	x23, #0x94d0, lsl #48
    13f4:	f2ca824d 	movk	x13, #0x5412, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    13f8:	9b167d6c 	mul	x12, x11, x22
    13fc:	f2ea708d 	movk	x13, #0x5384, lsl #48
    1400:	d29c150e 	mov	x14, #0xe0a8                	// #57512
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1404:	ca496d29 	eor	x9, x9, x9, lsr #27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1408:	8b0d008d 	add	x13, x4, x13
    140c:	f2bf4a6e 	movk	x14, #0xfa53, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1410:	9b177d0f 	mul	x15, x8, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1414:	ca4d79ad 	eor	x13, x13, x13, lsr #30
    1418:	f2d9b96e 	movk	x14, #0xcdcb, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    141c:	ca4a6d48 	eor	x8, x10, x10, lsr #27
    1420:	d28d8d2a 	mov	x10, #0x6c69                	// #27753
    1424:	f2fe376e 	movk	x14, #0xf1bb, lsl #48
    1428:	f2af8e8a 	movk	x10, #0x7c74, lsl #16
    142c:	9b177d2b 	mul	x11, x9, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1430:	8b0e008e 	add	x14, x4, x14
    1434:	f2cc13ea 	movk	x10, #0x609f, lsl #32
    1438:	d29b1a51 	mov	x17, #0xd8d2                	// #55506
    143c:	d28a9cf2 	mov	x18, #0x54e7                	// #21735
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1440:	9b177d09 	mul	x9, x8, x23
    1444:	ca4c6d88 	eor	x8, x12, x12, lsr #27
    1448:	d29d0fcc 	mov	x12, #0xe87e                	// #59518
    144c:	f2e2e2aa 	movk	x10, #0x1715, lsl #48
    1450:	f2bf77cc 	movk	x12, #0xfbbe, lsl #16
    1454:	f2bf1d11 	movk	x17, #0xf8e8, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1458:	8b0a008a 	add	x10, x4, x10
    145c:	f2db4b0c 	movk	x12, #0xda58, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1460:	9b167db0 	mul	x16, x13, x22
    1464:	ca4a794a 	eor	x10, x10, x10, lsr #30
    1468:	f2f6a98c 	movk	x12, #0xb54c, lsl #48
    146c:	ca4e79cd 	eor	x13, x14, x14, lsr #30
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1470:	8b0c008c 	add	x12, x4, x12
    1474:	f2d827d1 	movk	x17, #0xc13e, lsl #32
    1478:	f2af0672 	movk	x18, #0x7833, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    147c:	9b167d4a 	mul	x10, x10, x22
    1480:	ca4c798c 	eor	x12, x12, x12, lsr #30
    1484:	f2e5c551 	movk	x17, #0x2e2a, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1488:	8b110091 	add	x17, x4, x17
    148c:	f2c75f12 	movk	x18, #0x3af8, lsl #32
    1490:	d29a1f80 	mov	x0, #0xd0fc                	// #53500
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1494:	9b167d8c 	mul	x12, x12, x22
    1498:	ca517a31 	eor	x17, x17, x17, lsr #30
    149c:	f2f98c52 	movk	x18, #0xcc62, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    14a0:	8b120092 	add	x18, x4, x18
    14a4:	f2beefa0 	movk	x0, #0xf77d, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    14a8:	d35ffde2 	lsr	x2, x15, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    14ac:	9b167dae 	mul	x14, x13, x22
    14b0:	ca527a52 	eor	x18, x18, x18, lsr #30
    14b4:	f2d69620 	movk	x0, #0xb4b1, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    14b8:	ca4a6d4a 	eor	x10, x10, x10, lsr #27
    14bc:	f2ed5320 	movk	x0, #0x6a99, lsl #48
    14c0:	d289a223 	mov	x3, #0x4d11                	// #19729
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    14c4:	9b167e31 	mul	x17, x17, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    14c8:	8b000080 	add	x0, x4, x0
    14cc:	f2aed903 	movk	x3, #0x76c8, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    14d0:	ca407800 	eor	x0, x0, x0, lsr #30
    14d4:	f2c5cd63 	movk	x3, #0x2e6b, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    14d8:	9b177d4d 	mul	x13, x10, x23
    14dc:	ca4c6d8a 	eor	x10, x12, x12, lsr #27
    14e0:	f2e11a23 	movk	x3, #0x8d1, lsl #48
    14e4:	ca4e6dce 	eor	x14, x14, x14, lsr #27
    14e8:	9b177d4c 	mul	x12, x10, x23
    14ec:	ca506e0a 	eor	x10, x16, x16, lsr #27
    14f0:	d28b97b0 	mov	x16, #0x5cbd                	// #23741
    14f4:	f2af33d0 	movk	x16, #0x799e, lsl #16
    14f8:	ca516e21 	eor	x1, x17, x17, lsr #27
    14fc:	f2c8f0b0 	movk	x16, #0x4785, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1500:	9b167e52 	mul	x18, x18, x22
    1504:	f2f1fe70 	movk	x16, #0x8ff3, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1508:	8b100090 	add	x16, x4, x16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    150c:	9b167c00 	mul	x0, x0, x22
    1510:	ca507a10 	eor	x16, x16, x16, lsr #30
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1514:	9b177d08 	mul	x8, x8, x23
    1518:	ca526e52 	eor	x18, x18, x18, lsr #27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    151c:	9b167e10 	mul	x16, x16, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1520:	ca406c00 	eor	x0, x0, x0, lsr #27
    1524:	9b177d4a 	mul	x10, x10, x23
    1528:	9b177dce 	mul	x14, x14, x23
    152c:	ca506e10 	eor	x16, x16, x16, lsr #27
    1530:	9b177e11 	mul	x17, x16, x23
    1534:	9b177c30 	mul	x16, x1, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1538:	4a0f0041 	eor	w1, w2, w15
    153c:	d35ffd62 	lsr	x2, x11, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    uint64_t rng = seed;
    uint8_t hash_seed[16];
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1540:	381b03a1 	sturb	w1, [x29, #-80]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1544:	9b177e4f 	mul	x15, x18, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1548:	4a0b0052 	eor	w18, w2, w11
    154c:	d29924c2 	mov	x2, #0xc926                	// #51494
    1550:	f2bec242 	movk	x2, #0xf612, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1554:	8b03008b 	add	x11, x4, x3
    1558:	d2982a03 	mov	x3, #0xc150                	// #49488
    155c:	f2d50482 	movk	x2, #0xa824, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1560:	ca4b7961 	eor	x1, x11, x11, lsr #30
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1564:	9b177c0b 	mul	x11, x0, x23
    1568:	f2f4e102 	movk	x2, #0xa708, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    156c:	381b13b2 	sturb	w18, [x29, #-79]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1570:	d35ffd32 	lsr	x18, x9, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    1574:	8b020080 	add	x0, x4, x2
    1578:	d288a762 	mov	x2, #0x453b                	// #17723
    157c:	f2be94e3 	movk	x3, #0xf4a7, lsl #16
    1580:	f2aeaba2 	movk	x2, #0x755d, lsl #16
    1584:	f2d372e3 	movk	x3, #0x9b97, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1588:	ca407800 	eor	x0, x0, x0, lsr #30
    158c:	f2c43bc2 	movk	x2, #0x21de, lsl #32
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1590:	4a090249 	eor	w9, w18, w9
    1594:	f2fc6ee3 	movk	x3, #0xe377, lsl #48
    1598:	f2e8a802 	movk	x2, #0x4540, lsl #48
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    159c:	9b167c21 	mul	x1, x1, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15a0:	d35ffd12 	lsr	x18, x8, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    15a4:	8b020082 	add	x2, x4, x2
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    15a8:	381b23a9 	sturb	w9, [x29, #-78]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:19
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    15ac:	8b030089 	add	x9, x4, x3
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    15b0:	ca427842 	eor	x2, x2, x2, lsr #30
    15b4:	9b167c00 	mul	x0, x0, x22
    15b8:	ca497929 	eor	x9, x9, x9, lsr #30
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15bc:	4a080248 	eor	w8, w18, w8
    15c0:	d35ffdb2 	lsr	x18, x13, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    15c4:	9b167c42 	mul	x2, x2, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    15c8:	381b33a8 	sturb	w8, [x29, #-77]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15cc:	d35ffd88 	lsr	x8, x12, #31
    15d0:	4a0d024d 	eor	w13, w18, w13
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    15d4:	ca416c32 	eor	x18, x1, x1, lsr #27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    15d8:	9b167d29 	mul	x9, x9, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15dc:	4a0c0108 	eor	w8, w8, w12
    15e0:	d35ffd4c 	lsr	x12, x10, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    15e4:	381b43ad 	sturb	w13, [x29, #-76]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    15e8:	ca406c0d 	eor	x13, x0, x0, lsr #27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:129
    dictSetHashFunctionSeed(hash_seed);
    15ec:	d10143a0 	sub	x0, x29, #0x50
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    15f0:	381b53a8 	sturb	w8, [x29, #-75]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15f4:	d35ffdc8 	lsr	x8, x14, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    15f8:	9b177e52 	mul	x18, x18, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    15fc:	4a0a018a 	eor	w10, w12, w10
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1600:	ca426c4c 	eor	x12, x2, x2, lsr #27
    1604:	9b177dad 	mul	x13, x13, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1608:	381b63aa 	sturb	w10, [x29, #-74]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    160c:	4a0e0108 	eor	w8, w8, w14
    1610:	d35ffe2a 	lsr	x10, x17, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1614:	ca496d29 	eor	x9, x9, x9, lsr #27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1618:	381b73a8 	sturb	w8, [x29, #-73]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    161c:	9b177d8c 	mul	x12, x12, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1620:	d35ffe08 	lsr	x8, x16, #31
    1624:	d35ffdee 	lsr	x14, x15, #31
    1628:	4a11014a 	eor	w10, w10, w17
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    162c:	9b177d29 	mul	x9, x9, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1630:	381b83aa 	sturb	w10, [x29, #-72]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1634:	4a100108 	eor	w8, w8, w16
    1638:	d35ffd6a 	lsr	x10, x11, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    163c:	381b93a8 	sturb	w8, [x29, #-71]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1640:	4a0f01c8 	eor	w8, w14, w15
    1644:	d35ffe4e 	lsr	x14, x18, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1648:	381ba3a8 	sturb	w8, [x29, #-70]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    164c:	4a0b0148 	eor	w8, w10, w11
    1650:	d35ffdaa 	lsr	x10, x13, #31
    1654:	d35ffd8b 	lsr	x11, x12, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1658:	381bb3a8 	sturb	w8, [x29, #-69]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    165c:	4a1201c8 	eor	w8, w14, w18
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1660:	381bc3a8 	sturb	w8, [x29, #-68]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1664:	4a0d0148 	eor	w8, w10, w13
    1668:	d35ffd2a 	lsr	x10, x9, #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    166c:	381bd3a8 	sturb	w8, [x29, #-67]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1670:	4a0c0168 	eor	w8, w11, w12
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    1674:	381be3a8 	sturb	w8, [x29, #-66]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1678:	4a090148 	eor	w8, w10, w9
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:128
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    167c:	381bf3a8 	sturb	w8, [x29, #-65]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:129
    dictSetHashFunctionSeed(hash_seed);
    1680:	94003e03 	bl	10e8c <dictSetHashFunctionSeed>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:130
    sds *keys = zmalloc(2 * n * sizeof(*keys));
    1684:	d37cee60 	lsl	x0, x19, #4
    1688:	d37ffa7b 	lsl	x27, x19, #1
    168c:	94003d95 	bl	10ce0 <zmalloc>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:131
    size_t *order = zmalloc(n * sizeof(*order));
    1690:	d37df268 	lsl	x8, x19, #3
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:130
    sds *keys = zmalloc(2 * n * sizeof(*keys));
    1694:	aa0003f9 	mov	x25, x0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:131
    size_t *order = zmalloc(n * sizeof(*order));
    1698:	aa0803e0 	mov	x0, x8
    169c:	94003d91 	bl	10ce0 <zmalloc>
    16a0:	aa0003fa 	mov	x26, x0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:132
    char *buf = zmalloc(bytes);
    16a4:	aa1c03e0 	mov	x0, x28
    16a8:	94003d8e 	bl	10ce0 <zmalloc>
    16ac:	aa0003f5 	mov	x21, x0
    16b0:	f9003ffb 	str	x27, [sp, #120]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:133
    for (size_t i = 0; i < 2 * n; i++) {
    16b4:	b4000693 	cbz	x19, 1784 <main+0x86c>
    16b8:	f100077f 	cmp	x27, #0x1
    16bc:	aa1f03f8 	mov	x24, xzr
    16c0:	9a9f877b 	csinc	x27, x27, xzr, hi	// hi = pmore
    16c4:	14000004 	b	16d4 <main+0x7bc>
    16c8:	91000718 	add	x24, x24, #0x1
    16cc:	eb18037f 	cmp	x27, x24
    16d0:	540001c0 	b.eq	1708 <main+0x7f0>  // b.none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:134
        memset(buf, 'x', bytes);
    16d4:	aa1503e0 	mov	x0, x21
    16d8:	52800f01 	mov	w1, #0x78                  	// #120
    16dc:	aa1c03e2 	mov	x2, x28
    16e0:	97fffd80 	bl	ce0 <memset@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:137
        /* Fixed-endian unique binary members, including embedded NUL bytes. */
        for (unsigned j = 0; j < 8; j++) buf[j] = (char)((uint64_t)i >> (j * 8));
        keys[i] = sdsnewlen(buf, bytes);
    16e4:	aa1503e0 	mov	x0, x21
    16e8:	aa1c03e1 	mov	x1, x28
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:136
        for (unsigned j = 0; j < 8; j++) buf[j] = (char)((uint64_t)i >> (j * 8));
    16ec:	f90002b8 	str	x24, [x21]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:137
        keys[i] = sdsnewlen(buf, bytes);
    16f0:	94003df0 	bl	10eb0 <sdsnewlen>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:138
        if (i < n) order[i] = i;
    16f4:	eb13031f 	cmp	x24, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:137
        keys[i] = sdsnewlen(buf, bytes);
    16f8:	f8387b20 	str	x0, [x25, x24, lsl #3]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:138
        if (i < n) order[i] = i;
    16fc:	54fffe62 	b.cs	16c8 <main+0x7b0>  // b.hs, b.nlast
    1700:	f8387b58 	str	x24, [x26, x24, lsl #3]
    1704:	17fffff1 	b	16c8 <main+0x7b0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:140
    }
    zfree(buf);
    1708:	aa1503e0 	mov	x0, x21
    170c:	94003d92 	bl	10d54 <zfree>
    1710:	f9403ffb 	ldr	x27, [sp, #120]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:141
    for (size_t i = n; i > 1; i--) {
    1714:	f100067f 	cmp	x19, #0x1
    1718:	540003a0 	b.eq	178c <main+0x874>  // b.none
    171c:	d287aca9 	mov	x9, #0x3d65                	// #15717
    1720:	f9404bea 	ldr	x10, [sp, #144]
    1724:	d1002348 	sub	x8, x26, #0x8
    1728:	f2ae7e49 	movk	x9, #0x73f2, lsl #16
    172c:	f2c2aa29 	movk	x9, #0x1551, lsl #32
    1730:	f2f035e9 	movk	x9, #0x81af, lsl #48
    1734:	8b090149 	add	x9, x10, x9
    1738:	aa1303ea 	mov	x10, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    173c:	ca49792b 	eor	x11, x9, x9, lsr #30
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:141
    for (size_t i = n; i > 1; i--) {
    1740:	8b140129 	add	x9, x9, x20
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:20
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    1744:	9b167d6b 	mul	x11, x11, x22
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:21
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    1748:	ca4b6d6b 	eor	x11, x11, x11, lsr #27
    174c:	9b177d6b 	mul	x11, x11, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:22
    return z ^ (z >> 31);
    1750:	ca4b7d6b 	eor	x11, x11, x11, lsr #31
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:142
        size_t j = random64(&rng) % i, tmp = order[i - 1];
    1754:	9aca096c 	udiv	x12, x11, x10
    1758:	9b0aad8b 	msub	x11, x12, x10, x11
    175c:	d37df14c 	lsl	x12, x10, #3
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:141
    for (size_t i = n; i > 1; i--) {
    1760:	d100054a 	sub	x10, x10, #0x1
    1764:	f100055f 	cmp	x10, #0x1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:142
        size_t j = random64(&rng) % i, tmp = order[i - 1];
    1768:	f86c690e 	ldr	x14, [x8, x12]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:143
        order[i - 1] = order[j]; order[j] = tmp;
    176c:	d37df16b 	lsl	x11, x11, #3
    1770:	f86b6b4d 	ldr	x13, [x26, x11]
    1774:	f82c690d 	str	x13, [x8, x12]
    1778:	f82b6b4e 	str	x14, [x26, x11]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:141
    for (size_t i = n; i > 1; i--) {
    177c:	54fffe08 	b.hi	173c <main+0x824>  // b.pmore
    1780:	14000003 	b	178c <main+0x874>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:140
    zfree(buf);
    1784:	aa1503e0 	mov	x0, x21
    1788:	94003d73 	bl	10d54 <zfree>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:145
    }
    puts("case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns");
    178c:	90000080 	adrp	x0, 11000 <sdsnew+0x94>
    1790:	911ba800 	add	x0, x0, #0x6ea
    1794:	97fffd6b 	bl	d40 <puts@plt>
    1798:	f85803a8 	ldur	x8, [x29, #-128]
    179c:	9e630268 	ucvtf	d8, x19
    17a0:	f9404ff4 	ldr	x20, [sp, #152]
    17a4:	f94047fc 	ldr	x28, [sp, #136]
    17a8:	aa1f03f5 	mov	x21, xzr
    17ac:	d1000508 	sub	x8, x8, #0x1
    17b0:	9ad30909 	udiv	x9, x8, x19
    17b4:	d1000668 	sub	x8, x19, #0x1
    17b8:	9b137d08 	mul	x8, x8, x19
    17bc:	d341fd08 	lsr	x8, x8, #1
    17c0:	a906a7e8 	stp	x8, x9, [sp, #104]
    17c4:	14000042 	b	18cc <main+0x9b4>
    17c8:	f9404ff4 	ldr	x20, [sp, #152]
    17cc:	f85983b5 	ldur	x21, [x29, #-104]
    17d0:	a94b23e9 	ldp	x9, x8, [sp, #176]
    17d4:	5299400b 	mov	w11, #0xca00                	// #51712
    17d8:	72a7734b 	movk	w11, #0x3b9a, lsl #16
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:237
            serverAssert(zbtreeScore(tree, keys[order[i]], &score));
            serverAssert(score == (double)order[i] + (double)(repeats * n));
        }
        sink ^= checksum;
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%zu,%" PRIu64 "\n",
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
    17dc:	9e6302c1 	ucvtf	d1, x22
    17e0:	f000016c 	adrp	x12, 30000 <memcpy@GLIBC_2.17>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:236
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%zu,%" PRIu64 "\n",
    17e4:	90000080 	adrp	x0, 11000 <sdsnew+0x94>
    17e8:	9125b400 	add	x0, x0, #0x96d
    17ec:	aa1303e2 	mov	x2, x19
    17f0:	9b0b2508 	madd	x8, x8, x11, x9
    17f4:	f94057e9 	ldr	x9, [sp, #168]
    17f8:	aa1703e3 	mov	x3, x23
    17fc:	aa1603e6 	mov	x6, x22
    1800:	9b0b7129 	madd	x9, x9, x11, x28
    1804:	cb080127 	sub	x7, x9, x8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:238
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum,
    1808:	eb08013f 	cmp	x9, x8
    180c:	d2d9aca8 	mov	x8, #0xcd6500000000        	// #225833675390976
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:237
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
    1810:	9e6300e0 	ucvtf	d0, x7
    1814:	f2e839a8 	movk	x8, #0x41cd, lsl #48
    1818:	f85683a9 	ldur	x9, [x29, #-152]
    181c:	9e670102 	fmov	d2, x8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:238
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum,
    1820:	9a9f14e8 	csinc	x8, x7, xzr, ne	// ne = any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:240
               thread_elapsed, cpu_start, cpu_end, qos_start, qos_end, relpri_start, relpri_end,
               traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed);
    1824:	f10002bf 	cmp	x21, #0x0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:237
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
    1828:	1e611800 	fdiv	d0, d0, d1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:238
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum,
    182c:	1e620821 	fmul	d1, d1, d2
    1830:	9e630102 	ucvtf	d2, x8
    1834:	f85783a8 	ldur	x8, [x29, #-136]
    1838:	cb080128 	sub	x8, x9, x8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:235
        sink ^= checksum;
    183c:	f9407d89 	ldr	x9, [x12, #248]
    1840:	a9752bad 	ldp	x13, x10, [x29, #-176]
    1844:	ca1b0129 	eor	x9, x9, x27
    1848:	f9007d89 	str	x9, [x12, #248]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:237
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
    184c:	d0000169 	adrp	x9, 2f000 <__FRAME_END__+0x1b6fc>
    1850:	9135e129 	add	x9, x9, #0xd78
    1854:	cb0a01aa 	sub	x10, x13, x10
    1858:	9b0b2908 	madd	x8, x8, x11, x10
    185c:	a94873e4 	ldp	x4, x28, [sp, #128]
    1860:	f8757921 	ldr	x1, [x9, x21, lsl #3]
    1864:	f9404be5 	ldr	x5, [sp, #144]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:240
               traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed);
    1868:	9a9c03e9 	csel	x9, xzr, x28, eq	// eq = none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:236
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%zu,%" PRIu64 "\n",
    186c:	b90043ff 	str	wzr, [sp, #64]
    1870:	b9003bff 	str	wzr, [sp, #56]
    1874:	a90523e9 	stp	x9, x8, [sp, #80]
    1878:	f85903a8 	ldur	x8, [x29, #-112]
    187c:	f90027e8 	str	x8, [sp, #72]
    1880:	90000088 	adrp	x8, 11000 <sdsnew+0x94>
    1884:	9128fd08 	add	x8, x8, #0xa3f
    1888:	a902a3e8 	stp	x8, x8, [sp, #40]
    188c:	b85703a8 	ldur	w8, [x29, #-144]
    1890:	b90023e8 	str	w8, [sp, #32]
    1894:	b85643a8 	ldur	w8, [x29, #-156]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:238
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum,
    1898:	1e621821 	fdiv	d1, d1, d2
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:236
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%zu,%" PRIu64 "\n",
    189c:	b9001be8 	str	w8, [sp, #24]
    18a0:	f94053e8 	ldr	x8, [sp, #160]
    18a4:	a900a3fb 	stp	x27, x8, [sp, #8]
    18a8:	f85883a8 	ldur	x8, [x29, #-120]
    18ac:	f90003e8 	str	x8, [sp]
    18b0:	97fffd3c 	bl	da0 <printf@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:241
        zbtreeFree(tree);
    18b4:	aa1803e0 	mov	x0, x24
    18b8:	94000462 	bl	2a40 <zbtreeFree>
    18bc:	f9403ffb 	ldr	x27, [sp, #120]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:146
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) {
    18c0:	910006b5 	add	x21, x21, #0x1
    18c4:	f10022bf 	cmp	x21, #0x8
    18c8:	540036c0 	b.eq	1fa0 <main+0x1088>  // b.none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:147
        if (strcmp(selected, "all") && strcmp(selected, cases[c])) continue;
    18cc:	aa1403e0 	mov	x0, x20
    18d0:	90000081 	adrp	x1, 11000 <sdsnew+0x94>
    18d4:	9115d021 	add	x1, x1, #0x574
    18d8:	97fffd22 	bl	d60 <strcmp@plt>
    18dc:	340000e0 	cbz	w0, 18f8 <main+0x9e0>
    18e0:	d0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    18e4:	9135e108 	add	x8, x8, #0xd78
    18e8:	aa1403e0 	mov	x0, x20
    18ec:	f8757901 	ldr	x1, [x8, x21, lsl #3]
    18f0:	97fffd1c 	bl	d60 <strcmp@plt>
    18f4:	35fffe60 	cbnz	w0, 18c0 <main+0x9a8>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:148
        zbtreeSet *tree = zbtreeCreate();
    18f8:	94000290 	bl	2338 <zbtreeCreate>
    18fc:	aa0003f8 	mov	x24, x0
    1900:	f81983b5 	stur	x21, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:149
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1904:	b4000275 	cbz	x21, 1950 <main+0xa38>
    1908:	b4000253 	cbz	x19, 1950 <main+0xa38>
    190c:	aa1a03f4 	mov	x20, x26
    1910:	aa1303f6 	mov	x22, x19
    1914:	f8408697 	ldr	x23, [x20], #8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:82
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    1918:	d10183a2 	sub	x2, x29, #0x60
    191c:	d10103a3 	sub	x3, x29, #0x40
    1920:	aa1803e0 	mov	x0, x24
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:149
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1924:	f8777b35 	ldr	x21, [x25, x23, lsl #3]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:82
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    1928:	aa1503e1 	mov	x1, x21
    192c:	94000bc7 	bl	4848 <zbtreeFindForAdd>
    1930:	35003a40 	cbnz	w0, 2078 <main+0x1160>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:149
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1934:	9e6302e0 	ucvtf	d0, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:83
    zbtreeInsertNew(tree, score, key, &pos);
    1938:	d10103a2 	sub	x2, x29, #0x40
    193c:	aa1803e0 	mov	x0, x24
    1940:	aa1503e1 	mov	x1, x21
    1944:	940011bd 	bl	6038 <zbtreeInsertNew>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:149
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1948:	f10006d6 	subs	x22, x22, #0x1
    194c:	54fffe41 	b.ne	1914 <main+0x9fc>  // b.any
now_ns():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1950:	d10103a1 	sub	x1, x29, #0x40
    1954:	52800020 	mov	w0, #0x1                   	// #1
    1958:	97fffcd2 	bl	ca0 <clock_gettime@plt>
    195c:	35003be0 	cbnz	w0, 20d8 <main+0x11c0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:27
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
    1960:	a97c6fa8 	ldp	x8, x27, [x29, #-64]
    1964:	f85803b7 	ldur	x23, [x29, #-128]
    1968:	f81783a8 	stur	x8, [x29, #-136]
    196c:	f85983a8 	ldur	x8, [x29, #-104]
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:152
        if (c != 0) for (size_t pass = 0; pass < warmup_passes; pass++) for (size_t i = 0; i < n; i++) {
    1970:	b4000328 	cbz	x8, 19d4 <main+0xabc>
    1974:	b400031c 	cbz	x28, 19d4 <main+0xabc>
    1978:	aa1f03f4 	mov	x20, xzr
    197c:	14000004 	b	198c <main+0xa74>
    1980:	91000694 	add	x20, x20, #0x1
    1984:	eb1c029f 	cmp	x20, x28
    1988:	54000260 	b.eq	19d4 <main+0xabc>  // b.none
    198c:	aa1a03f5 	mov	x21, x26
    1990:	aa1303f6 	mov	x22, x19
    1994:	b4ffff73 	cbz	x19, 1980 <main+0xa68>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:154
            serverAssert(zbtreeScore(tree, keys[order[i]], &score) && score == (double)order[i]);
    1998:	f94002a8 	ldr	x8, [x21]
    199c:	d10103a2 	sub	x2, x29, #0x40
    19a0:	aa1803e0 	mov	x0, x24
    19a4:	f8687b21 	ldr	x1, [x25, x8, lsl #3]
    19a8:	9400084e 	bl	3ae0 <zbtreeScore>
    19ac:	34003520 	cbz	w0, 2050 <main+0x1138>
    19b0:	fd4002a0 	ldr	d0, [x21]
    19b4:	fc5c03a1 	ldur	d1, [x29, #-64]
    19b8:	7e61d800 	ucvtf	d0, d0
    19bc:	1e602020 	fcmp	d1, d0
    19c0:	54003481 	b.ne	2050 <main+0x1138>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:152
        if (c != 0) for (size_t pass = 0; pass < warmup_passes; pass++) for (size_t i = 0; i < n; i++) {
    19c4:	f10006d6 	subs	x22, x22, #0x1
    19c8:	910022b5 	add	x21, x21, #0x8
    19cc:	54fffe61 	b.ne	1998 <main+0xa80>  // b.any
    19d0:	17ffffec 	b	1980 <main+0xa68>
now_ns():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    19d4:	d10103a1 	sub	x1, x29, #0x40
    19d8:	52800020 	mov	w0, #0x1                   	// #1
    19dc:	97fffcb1 	bl	ca0 <clock_gettime@plt>
    19e0:	350037c0 	cbnz	w0, 20d8 <main+0x11c0>
    19e4:	f85983a8 	ldur	x8, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:27
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
    19e8:	a97c73b4 	ldp	x20, x28, [x29, #-64]
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:159
        size_t tree_bytes = zbtreeAllocSize(tree);
    19ec:	aa1803e0 	mov	x0, x24
    19f0:	f1001d1f 	cmp	x8, #0x7
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:149
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    19f4:	fa401904 	ccmp	x8, #0x0, #0x4, ne	// ne = any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:157
        size_t count = (c == 0 || c == 7) ? n : ops;
    19f8:	9a970275 	csel	x21, x19, x23, eq	// eq = none
    19fc:	aa0803f7 	mov	x23, x8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:159
        size_t tree_bytes = zbtreeAllocSize(tree);
    1a00:	94000493 	bl	2c4c <zbtreeAllocSize>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:160
        size_t traversals = (c == 4 || c == 5) ? 1 + (ops - 1) / n : 0;
    1a04:	927f06e8 	and	x8, x23, #0x6
    1a08:	f81883a0 	stur	x0, [x29, #-120]
    1a0c:	f100111f 	cmp	x8, #0x4
    1a10:	54000081 	b.ne	1a20 <main+0xb08>  // b.any
    1a14:	f9403be9 	ldr	x9, [sp, #112]
    1a18:	9100052a 	add	x10, x9, #0x1
    1a1c:	14000002 	b	1a24 <main+0xb0c>
    1a20:	aa1f03ea 	mov	x10, xzr
    1a24:	9b137d4b 	mul	x11, x10, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:161
        if (c == 4 || c == 5) count = traversals * n;
    1a28:	f100111f 	cmp	x8, #0x4
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:162
        if (c == 1 || c == 3) for (size_t i = 0; i < count; i++) expected += order[i % n];
    1a2c:	b27f02e9 	orr	x9, x23, #0x2
    1a30:	f81903aa 	stur	x10, [x29, #-112]
    1a34:	f81683b4 	stur	x20, [x29, #-152]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:161
        if (c == 4 || c == 5) count = traversals * n;
    1a38:	9a950176 	csel	x22, x11, x21, eq	// eq = none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:162
        if (c == 1 || c == 3) for (size_t i = 0; i < count; i++) expected += order[i % n];
    1a3c:	f1000d3f 	cmp	x9, #0x3
    1a40:	f90053eb 	str	x11, [sp, #160]
    1a44:	540000e1 	b.ne	1a60 <main+0xb48>  // b.any
    1a48:	b40001b5 	cbz	x21, 1a7c <main+0xb64>
    1a4c:	f1000adf 	cmp	x22, #0x2
    1a50:	540001a2 	b.cs	1a84 <main+0xb6c>  // b.hs, b.nlast
    1a54:	aa1f03e8 	mov	x8, xzr
    1a58:	aa1f03f4 	mov	x20, xzr
    1a5c:	1400001d 	b	1ad0 <main+0xbb8>
    1a60:	f94037e9 	ldr	x9, [sp, #104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:163
        else if (c == 6 || c == 7) expected = count;
    1a64:	f100191f 	cmp	x8, #0x6
    1a68:	9a9f02a8 	csel	x8, x21, xzr, eq	// eq = none
    1a6c:	f10012ff 	cmp	x23, #0x4
    1a70:	9b097d49 	mul	x9, x10, x9
    1a74:	9a880134 	csel	x20, x9, x8, eq	// eq = none
    1a78:	1400001d 	b	1aec <main+0xbd4>
    1a7c:	aa1f03f4 	mov	x20, xzr
    1a80:	1400001b 	b	1aec <main+0xbd4>
    1a84:	aa1f03eb 	mov	x11, xzr
    1a88:	aa1f03e9 	mov	x9, xzr
    1a8c:	aa1f03ea 	mov	x10, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:162
        if (c == 1 || c == 3) for (size_t i = 0; i < count; i++) expected += order[i % n];
    1a90:	927ffac8 	and	x8, x22, #0xfffffffffffffffe
    1a94:	9100056d 	add	x13, x11, #0x1
    1a98:	9ad3096c 	udiv	x12, x11, x19
    1a9c:	9ad309ae 	udiv	x14, x13, x19
    1aa0:	9b13ad8c 	msub	x12, x12, x19, x11
    1aa4:	9100096b 	add	x11, x11, #0x2
    1aa8:	eb0b011f 	cmp	x8, x11
    1aac:	f86c7b4c 	ldr	x12, [x26, x12, lsl #3]
    1ab0:	8b090189 	add	x9, x12, x9
    1ab4:	9b13b5cd 	msub	x13, x14, x19, x13
    1ab8:	f86d7b4d 	ldr	x13, [x26, x13, lsl #3]
    1abc:	8b0a01aa 	add	x10, x13, x10
    1ac0:	54fffea1 	b.ne	1a94 <main+0xb7c>  // b.any
    1ac4:	eb0802df 	cmp	x22, x8
    1ac8:	8b090154 	add	x20, x10, x9
    1acc:	54000100 	b.eq	1aec <main+0xbd4>  // b.none
    1ad0:	9ad30909 	udiv	x9, x8, x19
    1ad4:	9b13a129 	msub	x9, x9, x19, x8
    1ad8:	91000508 	add	x8, x8, #0x1
    1adc:	eb0802df 	cmp	x22, x8
    1ae0:	f8697b49 	ldr	x9, [x26, x9, lsl #3]
    1ae4:	8b140134 	add	x20, x9, x20
    1ae8:	54ffff41 	b.ne	1ad0 <main+0xbb8>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:165
        scan_result scanned = {0, 0};
    1aec:	a93a7fbf 	stp	xzr, xzr, [x29, #-96]
cpu_id():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:45
    return sched_getcpu();
    1af0:	97fffc70 	bl	cb0 <sched_getcpu@plt>
    1af4:	b81643a0 	stur	w0, [x29, #-156]
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:33
    if (clock_gettime(CLOCK_THREAD_CPUTIME_ID, &ts) == 0)
    1af8:	d10103a1 	sub	x1, x29, #0x40
    1afc:	52800060 	mov	w0, #0x3                   	// #3
    1b00:	97fffc68 	bl	ca0 <clock_gettime@plt>
    1b04:	a97c27a8 	ldp	x8, x9, [x29, #-64]
    1b08:	5299400a 	mov	w10, #0xca00                	// #51712
    1b0c:	72a7734a 	movk	w10, #0x3b9a, lsl #16
    1b10:	7100001f 	cmp	w0, #0x0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1b14:	d10103a1 	sub	x1, x29, #0x40
    1b18:	52800020 	mov	w0, #0x1                   	// #1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:33
    if (clock_gettime(CLOCK_THREAD_CPUTIME_ID, &ts) == 0)
    1b1c:	9b0a2508 	madd	x8, x8, x10, x9
    1b20:	da9f0108 	csinv	x8, x8, xzr, eq	// eq = none
    1b24:	f81703a8 	stur	x8, [x29, #-144]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1b28:	97fffc5e 	bl	ca0 <clock_gettime@plt>
    1b2c:	35002d60 	cbnz	w0, 20d8 <main+0x11c0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:27
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
    1b30:	a97c2ba9 	ldp	x9, x10, [x29, #-64]
    1b34:	a9356fbc 	stp	x28, x27, [x29, #-176]
    1b38:	a90b27ea 	stp	x10, x9, [sp, #176]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:171
        if (c == 0) {
    1b3c:	b4000477 	cbz	x23, 1bc8 <main+0xcb0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:173
        } else if (c == 1 || c == 2) {
    1b40:	f1000aff 	cmp	x23, #0x2
    1b44:	54000688 	b.hi	1c14 <main+0xcfc>  // b.pmore
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:174
            for (size_t i = 0; i < count; i++) {
    1b48:	b4001396 	cbz	x22, 1db8 <main+0xea0>
    1b4c:	f1000aff 	cmp	x23, #0x2
    1b50:	aa1f03f5 	mov	x21, xzr
    1b54:	aa1f03fb 	mov	x27, xzr
    1b58:	9a9f0268 	csel	x8, x19, xzr, eq	// eq = none
    1b5c:	8b080f3c 	add	x28, x25, x8, lsl #3
    1b60:	14000006 	b	1b78 <main+0xc60>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:177
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
    1b64:	93407c08 	sxtw	x8, w0
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:174
            for (size_t i = 0; i < count; i++) {
    1b68:	910006b5 	add	x21, x21, #0x1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:177
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
    1b6c:	8b1b011b 	add	x27, x8, x27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:174
            for (size_t i = 0; i < count; i++) {
    1b70:	eb1502df 	cmp	x22, x21
    1b74:	54001440 	b.eq	1dfc <main+0xee4>  // b.none
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:176
                int found = zbtreeScore(tree, keys[order[i % n] + (c == 2 ? n : 0)], &score);
    1b78:	9ad30aa8 	udiv	x8, x21, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:175
                double score = 0;
    1b7c:	f81c03bf 	stur	xzr, [x29, #-64]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:176
                int found = zbtreeScore(tree, keys[order[i % n] + (c == 2 ? n : 0)], &score);
    1b80:	d10103a2 	sub	x2, x29, #0x40
    1b84:	aa1803e0 	mov	x0, x24
    1b88:	9b13d508 	msub	x8, x8, x19, x21
    1b8c:	f8687b48 	ldr	x8, [x26, x8, lsl #3]
    1b90:	f8687b81 	ldr	x1, [x28, x8, lsl #3]
    1b94:	940007d3 	bl	3ae0 <zbtreeScore>
    1b98:	f85983a8 	ldur	x8, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:177
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
    1b9c:	f100051f 	cmp	x8, #0x1
    1ba0:	54fffe21 	b.ne	1b64 <main+0xc4c>  // b.any
    1ba4:	fc5c03a0 	ldur	d0, [x29, #-64]
    1ba8:	7100001f 	cmp	w0, #0x0
    1bac:	9e790008 	fcvtzu	x8, d0
    1bb0:	da9f1108 	csinv	x8, x8, xzr, ne	// ne = any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:174
            for (size_t i = 0; i < count; i++) {
    1bb4:	910006b5 	add	x21, x21, #0x1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:177
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
    1bb8:	8b1b011b 	add	x27, x8, x27
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:174
            for (size_t i = 0; i < count; i++) {
    1bbc:	eb1502df 	cmp	x22, x21
    1bc0:	54fffdc1 	b.ne	1b78 <main+0xc60>  // b.any
    1bc4:	1400008e 	b	1dfc <main+0xee4>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:172
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1bc8:	b4000f93 	cbz	x19, 1db8 <main+0xea0>
    1bcc:	aa1a03f7 	mov	x23, x26
    1bd0:	aa1303fb 	mov	x27, x19
    1bd4:	f84086fc 	ldr	x28, [x23], #8
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:82
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    1bd8:	d10023a2 	sub	x2, x29, #0x8
    1bdc:	d10103a3 	sub	x3, x29, #0x40
    1be0:	aa1803e0 	mov	x0, x24
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:172
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1be4:	f87c7b35 	ldr	x21, [x25, x28, lsl #3]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:82
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    1be8:	aa1503e1 	mov	x1, x21
    1bec:	94000b17 	bl	4848 <zbtreeFindForAdd>
    1bf0:	35002440 	cbnz	w0, 2078 <main+0x1160>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:172
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1bf4:	9e630380 	ucvtf	d0, x28
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:83
    zbtreeInsertNew(tree, score, key, &pos);
    1bf8:	d10103a2 	sub	x2, x29, #0x40
    1bfc:	aa1803e0 	mov	x0, x24
    1c00:	aa1503e1 	mov	x1, x21
    1c04:	9400110d 	bl	6038 <zbtreeInsertNew>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:172
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
    1c08:	f100077b 	subs	x27, x27, #0x1
    1c0c:	54fffe41 	b.ne	1bd4 <main+0xcbc>  // b.any
    1c10:	1400007b 	b	1dfc <main+0xee4>
    1c14:	f85903a8 	ldur	x8, [x29, #-112]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:179
        } else if (c == 3) {
    1c18:	f1000eff 	cmp	x23, #0x3
    1c1c:	54000221 	b.ne	1c60 <main+0xd48>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:180
            for (size_t i = 0; i < count; i++) checksum += (uint64_t)zbtreeRank(tree, keys[order[i % n]], 0, NULL);
    1c20:	b4000cd5 	cbz	x21, 1db8 <main+0xea0>
    1c24:	aa1f03f5 	mov	x21, xzr
    1c28:	aa1f03fb 	mov	x27, xzr
    1c2c:	9ad30aa8 	udiv	x8, x21, x19
    1c30:	aa1803e0 	mov	x0, x24
    1c34:	2a1f03e2 	mov	w2, wzr
    1c38:	aa1f03e3 	mov	x3, xzr
    1c3c:	9b13d508 	msub	x8, x8, x19, x21
    1c40:	f8687b48 	ldr	x8, [x26, x8, lsl #3]
    1c44:	f8687b21 	ldr	x1, [x25, x8, lsl #3]
    1c48:	94000db0 	bl	5308 <zbtreeRank>
    1c4c:	910006b5 	add	x21, x21, #0x1
    1c50:	8b1b001b 	add	x27, x0, x27
    1c54:	eb1502df 	cmp	x22, x21
    1c58:	54fffea1 	b.ne	1c2c <main+0xd14>  // b.any
    1c5c:	14000068 	b	1dfc <main+0xee4>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:181
        } else if (c == 4) {
    1c60:	f10012ff 	cmp	x23, #0x4
    1c64:	b000001b 	adrp	x27, 2000 <main+0x10e8>
    1c68:	9107a37b 	add	x27, x27, #0x1e8
    1c6c:	54000441 	b.ne	1cf4 <main+0xddc>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:182
            for (size_t pass = 0; pass < traversals; pass++) {
    1c70:	b4000a48 	cbz	x8, 1db8 <main+0xea0>
    1c74:	aa1f03f5 	mov	x21, xzr
    1c78:	aa1f03fb 	mov	x27, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:184
                zbtreeIteratorStart(tree, 0, &it);
    1c7c:	d10103a2 	sub	x2, x29, #0x40
    1c80:	aa1803e0 	mov	x0, x24
    1c84:	2a1f03e1 	mov	w1, wzr
    1c88:	94002115 	bl	a0dc <zbtreeIteratorStart>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:187
                while (zbtreeIteratorNext(&it, 0, NULL, NULL, &score)) { checksum += (uint64_t)score; visited++; }
    1c8c:	d10103a0 	sub	x0, x29, #0x40
    1c90:	d10023a4 	sub	x4, x29, #0x8
    1c94:	2a1f03e1 	mov	w1, wzr
    1c98:	aa1f03e2 	mov	x2, xzr
    1c9c:	aa1f03e3 	mov	x3, xzr
    1ca0:	94002205 	bl	a4b4 <zbtreeIteratorNext>
    1ca4:	aa1f03f7 	mov	x23, xzr
    1ca8:	34000180 	cbz	w0, 1cd8 <main+0xdc0>
    1cac:	fc5f83a0 	ldur	d0, [x29, #-8]
    1cb0:	d10103a0 	sub	x0, x29, #0x40
    1cb4:	d10023a4 	sub	x4, x29, #0x8
    1cb8:	2a1f03e1 	mov	w1, wzr
    1cbc:	aa1f03e2 	mov	x2, xzr
    1cc0:	aa1f03e3 	mov	x3, xzr
    1cc4:	9e790008 	fcvtzu	x8, d0
    1cc8:	910006f7 	add	x23, x23, #0x1
    1ccc:	8b08037b 	add	x27, x27, x8
    1cd0:	940021f9 	bl	a4b4 <zbtreeIteratorNext>
    1cd4:	35fffec0 	cbnz	w0, 1cac <main+0xd94>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:188
                serverAssert(visited == n);
    1cd8:	eb1302ff 	cmp	x23, x19
    1cdc:	540020a1 	b.ne	20f0 <main+0x11d8>  // b.any
    1ce0:	f85903a8 	ldur	x8, [x29, #-112]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:182
            for (size_t pass = 0; pass < traversals; pass++) {
    1ce4:	910006b5 	add	x21, x21, #0x1
    1ce8:	eb0802bf 	cmp	x21, x8
    1cec:	54fffc81 	b.ne	1c7c <main+0xd64>  // b.any
    1cf0:	14000043 	b	1dfc <main+0xee4>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:190
        } else if (c == 5) {
    1cf4:	f10016ff 	cmp	x23, #0x5
    1cf8:	540002a1 	b.ne	1d4c <main+0xe34>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:191
            for (size_t pass = 0; pass < traversals; pass++) {
    1cfc:	b40001c8 	cbz	x8, 1d34 <main+0xe1c>
    1d00:	aa1f03f5 	mov	x21, xzr
    1d04:	aa1f03e1 	mov	x1, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:193
                do { cursor = zbtreeScan(tree, cursor, 64, scan_count, &scanned); } while (cursor);
    1d08:	d10183a4 	sub	x4, x29, #0x60
    1d0c:	aa1803e0 	mov	x0, x24
    1d10:	52800802 	mov	w2, #0x40                  	// #64
    1d14:	aa1b03e3 	mov	x3, x27
    1d18:	940022e4 	bl	a8a8 <zbtreeScan>
    1d1c:	aa0003e1 	mov	x1, x0
    1d20:	b5ffff40 	cbnz	x0, 1d08 <main+0xdf0>
    1d24:	f85903a8 	ldur	x8, [x29, #-112]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:191
            for (size_t pass = 0; pass < traversals; pass++) {
    1d28:	910006b5 	add	x21, x21, #0x1
    1d2c:	eb0802bf 	cmp	x21, x8
    1d30:	54fffea1 	b.ne	1d04 <main+0xdec>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:195
            checksum = scanned.sum;
    1d34:	f85a83bb 	ldur	x27, [x29, #-88]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1d38:	d10103a1 	sub	x1, x29, #0x40
    1d3c:	52800020 	mov	w0, #0x1                   	// #1
    1d40:	97fffbd8 	bl	ca0 <clock_gettime@plt>
    1d44:	34000640 	cbz	w0, 1e0c <main+0xef4>
    1d48:	140000e4 	b	20d8 <main+0x11c0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:196
        } else if (c == 6) {
    1d4c:	f1001aff 	cmp	x23, #0x6
    1d50:	54000401 	b.ne	1dd0 <main+0xeb8>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:197
            for (size_t i = 0; i < count; i++) {
    1d54:	b4000335 	cbz	x21, 1db8 <main+0xea0>
    1d58:	aa1f03f7 	mov	x23, xzr
    1d5c:	aa1f03fb 	mov	x27, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:198
                sds key = keys[order[i % n]];
    1d60:	9ad30ae8 	udiv	x8, x23, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:201
                int found = zbtreeFindForAdd(tree, key, &score, &pos);
    1d64:	d10023a2 	sub	x2, x29, #0x8
    1d68:	d10103a3 	sub	x3, x29, #0x40
    1d6c:	aa1803e0 	mov	x0, x24
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:198
                sds key = keys[order[i % n]];
    1d70:	9b13dd08 	msub	x8, x8, x19, x23
    1d74:	f8687b48 	ldr	x8, [x26, x8, lsl #3]
    1d78:	f8687b35 	ldr	x21, [x25, x8, lsl #3]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:201
                int found = zbtreeFindForAdd(tree, key, &score, &pos);
    1d7c:	aa1503e1 	mov	x1, x21
    1d80:	94000ab2 	bl	4848 <zbtreeFindForAdd>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:202
                serverAssert(found);
    1d84:	34002140 	cbz	w0, 21ac <main+0x1294>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:203
                zbtreeUpdateScore(tree, key, score + (double)n, &pos);
    1d88:	fc5f83a0 	ldur	d0, [x29, #-8]
    1d8c:	2a0003fc 	mov	w28, w0
    1d90:	d10103a2 	sub	x2, x29, #0x40
    1d94:	aa1803e0 	mov	x0, x24
    1d98:	aa1503e1 	mov	x1, x21
    1d9c:	1e682800 	fadd	d0, d0, d8
    1da0:	9400194f 	bl	82dc <zbtreeUpdateScore>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:197
            for (size_t i = 0; i < count; i++) {
    1da4:	910006f7 	add	x23, x23, #0x1
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:204
                checksum += found;
    1da8:	8b3cc37b 	add	x27, x27, w28, sxtw
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:197
            for (size_t i = 0; i < count; i++) {
    1dac:	eb1702df 	cmp	x22, x23
    1db0:	54fffd81 	b.ne	1d60 <main+0xe48>  // b.any
    1db4:	14000012 	b	1dfc <main+0xee4>
    1db8:	aa1f03fb 	mov	x27, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1dbc:	d10103a1 	sub	x1, x29, #0x40
    1dc0:	52800020 	mov	w0, #0x1                   	// #1
    1dc4:	97fffbb7 	bl	ca0 <clock_gettime@plt>
    1dc8:	34000220 	cbz	w0, 1e0c <main+0xef4>
    1dcc:	140000c3 	b	20d8 <main+0x11c0>
    1dd0:	aa1f03fb 	mov	x27, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:207
            for (size_t i = 0; i < n; i++) checksum += zbtreeDelete(tree, keys[order[i]]);
    1dd4:	b4000153 	cbz	x19, 1dfc <main+0xee4>
    1dd8:	aa1a03f5 	mov	x21, x26
    1ddc:	aa1303f7 	mov	x23, x19
    1de0:	f84086a8 	ldr	x8, [x21], #8
    1de4:	aa1803e0 	mov	x0, x24
    1de8:	f8687b21 	ldr	x1, [x25, x8, lsl #3]
    1dec:	94001218 	bl	664c <zbtreeDelete>
    1df0:	8b20c37b 	add	x27, x27, w0, sxtw
    1df4:	f10006f7 	subs	x23, x23, #0x1
    1df8:	54ffff41 	b.ne	1de0 <main+0xec8>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    1dfc:	d10103a1 	sub	x1, x29, #0x40
    1e00:	52800020 	mov	w0, #0x1                   	// #1
    1e04:	97fffba7 	bl	ca0 <clock_gettime@plt>
    1e08:	35001680 	cbnz	w0, 20d8 <main+0x11c0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:27
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
    1e0c:	a97c73a8 	ldp	x8, x28, [x29, #-64]
thread_ns():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:33
    if (clock_gettime(CLOCK_THREAD_CPUTIME_ID, &ts) == 0)
    1e10:	d10103a1 	sub	x1, x29, #0x40
    1e14:	52800060 	mov	w0, #0x3                   	// #3
    1e18:	f90057e8 	str	x8, [sp, #168]
    1e1c:	97fffba1 	bl	ca0 <clock_gettime@plt>
    1e20:	a97c27a8 	ldp	x8, x9, [x29, #-64]
    1e24:	5299400a 	mov	w10, #0xca00                	// #51712
    1e28:	72a7734a 	movk	w10, #0x3b9a, lsl #16
    1e2c:	7100001f 	cmp	w0, #0x0
    1e30:	9b0a2508 	madd	x8, x8, x10, x9
    1e34:	da9f0117 	csinv	x23, x8, xzr, eq	// eq = none
cpu_id():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:45
    return sched_getcpu();
    1e38:	97fffb9e 	bl	cb0 <sched_getcpu@plt>
    1e3c:	f85703a9 	ldur	x9, [x29, #-144]
    1e40:	b81703a0 	stur	w0, [x29, #-144]
    1e44:	eb0902e8 	subs	x8, x23, x9
    1e48:	f85803b7 	ldur	x23, [x29, #-128]
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:213
        int64_t thread_elapsed = thread_start >= 0 && thread_end >= thread_start ? thread_end - thread_start : -1;
    1e4c:	fa40a928 	ccmp	x9, #0x0, #0x8, ge	// ge = tcont
    1e50:	da9fa115 	csinv	x21, x8, xzr, ge	// ge = tcont
    1e54:	f85983a8 	ldur	x8, [x29, #-104]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:214
        if (c == 5) {
    1e58:	f100151f 	cmp	x8, #0x5
    1e5c:	540004c1 	b.ne	1ef4 <main+0xfdc>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:216
            serverAssert(scanned.count >= count && scanned.count <= SIZE_MAX);
    1e60:	f85a03b6 	ldur	x22, [x29, #-96]
    1e64:	f94053e8 	ldr	x8, [sp, #160]
    1e68:	eb0802df 	cmp	x22, x8
    1e6c:	54001883 	b.cc	217c <main+0x1264>  // b.lo, b.ul, b.last
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:218
            scan_check check = {zcalloc(n), n, keys, {0, 0}};
    1e70:	aa1303e0 	mov	x0, x19
    1e74:	94003ba9 	bl	10d18 <zcalloc>
    1e78:	aa1f03e1 	mov	x1, xzr
    1e7c:	d10103a8 	sub	x8, x29, #0x40
    1e80:	b0000014 	adrp	x20, 2000 <main+0x10e8>
    1e84:	91082294 	add	x20, x20, #0x208
    1e88:	a93c4fa0 	stp	x0, x19, [x29, #-64]
    1e8c:	f81d03b9 	stur	x25, [x29, #-48]
    1e90:	a901fd1f 	stp	xzr, xzr, [x8, #24]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:220
            do { cursor = zbtreeScan(tree, cursor, 64, scan_verify, &check); } while (cursor);
    1e94:	d10103a4 	sub	x4, x29, #0x40
    1e98:	aa1803e0 	mov	x0, x24
    1e9c:	52800802 	mov	w2, #0x40                  	// #64
    1ea0:	aa1403e3 	mov	x3, x20
    1ea4:	94002281 	bl	a8a8 <zbtreeScan>
    1ea8:	aa0003e1 	mov	x1, x0
    1eac:	b5ffff40 	cbnz	x0, 1e94 <main+0xf7c>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:221
            for (size_t i = 0; i < n; i++) serverAssert(check.seen[i]);
    1eb0:	b40000f3 	cbz	x19, 1ecc <main+0xfb4>
    1eb4:	f85c03a8 	ldur	x8, [x29, #-64]
    1eb8:	aa1303e9 	mov	x9, x19
    1ebc:	3840150a 	ldrb	w10, [x8], #1
    1ec0:	34000e8a 	cbz	w10, 2090 <main+0x1178>
    1ec4:	f1000529 	subs	x9, x9, #0x1
    1ec8:	54ffffa1 	b.ne	1ebc <main+0xfa4>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:222
            serverAssert(scanned.count == check.result.count * traversals);
    1ecc:	f85d83a8 	ldur	x8, [x29, #-40]
    1ed0:	f85903aa 	ldur	x10, [x29, #-112]
    1ed4:	f85a03a9 	ldur	x9, [x29, #-96]
    1ed8:	9b0a7d08 	mul	x8, x8, x10
    1edc:	eb08013f 	cmp	x9, x8
    1ee0:	540015a1 	b.ne	2194 <main+0x127c>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:223
            expected = check.result.sum * traversals;
    1ee4:	f85e03a8 	ldur	x8, [x29, #-32]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:224
            zfree(check.seen);
    1ee8:	f85c03a0 	ldur	x0, [x29, #-64]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:223
            expected = check.result.sum * traversals;
    1eec:	9b0a7d14 	mul	x20, x8, x10
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:224
            zfree(check.seen);
    1ef0:	94003b99 	bl	10d54 <zfree>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:226
        serverAssert(checksum == expected);
    1ef4:	eb14037f 	cmp	x27, x20
    1ef8:	f90053f5 	str	x21, [sp, #160]
    1efc:	54001241 	b.ne	2144 <main+0x122c>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:227
        serverAssert(zbtreeLength(tree) == (c == 7 ? 0 : n));
    1f00:	aa1803e0 	mov	x0, x24
    1f04:	94000350 	bl	2c44 <zbtreeLength>
    1f08:	f85983b5 	ldur	x21, [x29, #-104]
    1f0c:	f9404ff4 	ldr	x20, [sp, #152]
    1f10:	f1001ebf 	cmp	x21, #0x7
    1f14:	9a9303e8 	csel	x8, xzr, x19, eq	// eq = none
    1f18:	eb08001f 	cmp	x0, x8
    1f1c:	54001081 	b.ne	212c <main+0x1214>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:228
        if (c != 7) tree_bytes = zbtreeAllocSize(tree);
    1f20:	f1001ebf 	cmp	x21, #0x7
    1f24:	54ffc560 	b.eq	17d0 <main+0x8b8>  // b.none
    1f28:	aa1803e0 	mov	x0, x24
    1f2c:	94000348 	bl	2c4c <zbtreeAllocSize>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:229
        if (c == 6) for (size_t i = 0; i < n; i++) {
    1f30:	f1001abf 	cmp	x21, #0x6
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:228
        if (c != 7) tree_bytes = zbtreeAllocSize(tree);
    1f34:	aa0003f5 	mov	x21, x0
    1f38:	f81883a0 	stur	x0, [x29, #-120]
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:229
        if (c == 6) for (size_t i = 0; i < n; i++) {
    1f3c:	54ffc481 	b.ne	17cc <main+0x8b4>  // b.any
    1f40:	b4ffc473 	cbz	x19, 17cc <main+0x8b4>
    1f44:	aa1f03f4 	mov	x20, xzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:232
            serverAssert(zbtreeScore(tree, keys[order[i]], &score));
    1f48:	f8747b48 	ldr	x8, [x26, x20, lsl #3]
    1f4c:	d10103a2 	sub	x2, x29, #0x40
    1f50:	aa1803e0 	mov	x0, x24
    1f54:	f8687b21 	ldr	x1, [x25, x8, lsl #3]
    1f58:	940006e2 	bl	3ae0 <zbtreeScore>
    1f5c:	34000b20 	cbz	w0, 20c0 <main+0x11a8>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:231
            size_t repeats = ops / n + (i < ops % n);
    1f60:	9ad30ae8 	udiv	x8, x23, x19
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:233
            serverAssert(score == (double)order[i] + (double)(repeats * n));
    1f64:	fc747b40 	ldr	d0, [x26, x20, lsl #3]
    1f68:	7e61d800 	ucvtf	d0, d0
    1f6c:	9b13dd09 	msub	x9, x8, x19, x23
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:231
            size_t repeats = ops / n + (i < ops % n);
    1f70:	eb09029f 	cmp	x20, x9
    1f74:	9a882508 	cinc	x8, x8, cc	// cc = lo, ul, last
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:233
            serverAssert(score == (double)order[i] + (double)(repeats * n));
    1f78:	9b137d08 	mul	x8, x8, x19
    1f7c:	9e630101 	ucvtf	d1, x8
    1f80:	1e612800 	fadd	d0, d0, d1
    1f84:	fc5c03a1 	ldur	d1, [x29, #-64]
    1f88:	1e602020 	fcmp	d1, d0
    1f8c:	540008e1 	b.ne	20a8 <main+0x1190>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:229
        if (c == 6) for (size_t i = 0; i < n; i++) {
    1f90:	91000694 	add	x20, x20, #0x1
    1f94:	eb14027f 	cmp	x19, x20
    1f98:	54fffd81 	b.ne	1f48 <main+0x1030>  // b.any
    1f9c:	17fffe0b 	b	17c8 <main+0x8b0>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:243
    }
    for (size_t i = 0; i < 2 * n; i++) sdsfree(keys[i]);
    1fa0:	b4000113 	cbz	x19, 1fc0 <main+0x10a8>
    1fa4:	f100077f 	cmp	x27, #0x1
    1fa8:	aa1903f4 	mov	x20, x25
    1fac:	9a9f8773 	csinc	x19, x27, xzr, hi	// hi = pmore
    1fb0:	f8408680 	ldr	x0, [x20], #8
    1fb4:	94003c24 	bl	11044 <sdsfree>
    1fb8:	f1000673 	subs	x19, x19, #0x1
    1fbc:	54ffffa1 	b.ne	1fb0 <main+0x1098>  // b.any
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:244
    zfree(keys); zfree(order);
    1fc0:	aa1903e0 	mov	x0, x25
    1fc4:	94003b64 	bl	10d54 <zfree>
    1fc8:	aa1a03e0 	mov	x0, x26
    1fcc:	94003b62 	bl	10d54 <zfree>
    1fd0:	14000004 	b	1fe0 <main+0x10c8>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:110
            puts("btree-bench [--size N] [--ops N] [--member-bytes N>=8] [--seed N] [--warmup-passes N>=1] [--case all|insert|lookup-hit|lookup-miss|rank|iterate|scan|update|delete]");
    1fd4:	90000080 	adrp	x0, 11000 <sdsnew+0x94>
    1fd8:	9116f400 	add	x0, x0, #0x5bd
    1fdc:	97fffb59 	bl	d40 <puts@plt>
    1fe0:	2a1f03e0 	mov	w0, wzr
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:246
    return 0;
}
    1fe4:	a95c4ff4 	ldp	x20, x19, [sp, #448]
    1fe8:	fd40b3e8 	ldr	d8, [sp, #352]
    1fec:	a95b57f6 	ldp	x22, x21, [sp, #432]
    1ff0:	a95a5ff8 	ldp	x24, x23, [sp, #416]
    1ff4:	a95967fa 	ldp	x26, x25, [sp, #400]
    1ff8:	a9586ffc 	ldp	x28, x27, [sp, #384]
    1ffc:	a9577bfd 	ldp	x29, x30, [sp, #368]
    2000:	910743ff 	add	sp, sp, #0x1d0
    2004:	d65f03c0 	ret
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:125
    if (!valid_case || bytes < 8 || bytes > 65536) { fputs("Invalid case or member size (8..65536)\n", stderr); return 2; }
    2008:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    200c:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2010:	911b0800 	add	x0, x0, #0x6c2
    2014:	f947e108 	ldr	x8, [x8, #4032]
    2018:	528004e1 	mov	w1, #0x27                  	// #39
    201c:	52800022 	mov	w2, #0x1                   	// #1
    2020:	f9400103 	ldr	x3, [x8]
    2024:	97fffb57 	bl	d80 <fwrite@plt>
    2028:	14000008 	b	2048 <main+0x1130>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:113
        if (i + 1 == argc) { fprintf(stderr, "Missing value: %s\n", argv[i]); return 2; }
    202c:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    2030:	f0000061 	adrp	x1, 11000 <sdsnew+0x94>
    2034:	91198421 	add	x1, x1, #0x661
    2038:	f947e108 	ldr	x8, [x8, #4032]
    203c:	f9400100 	ldr	x0, [x8]
    2040:	aa1c03e2 	mov	x2, x28
    2044:	97fffb5f 	bl	dc0 <fprintf@plt>
    2048:	52800040 	mov	w0, #0x2                   	// #2
    204c:	17ffffe6 	b	1fe4 <main+0x10cc>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:154
            serverAssert(zbtreeScore(tree, keys[order[i]], &score) && score == (double)order[i]);
    2050:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2054:	911fd400 	add	x0, x0, #0x7f5
    2058:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    205c:	91202042 	add	x2, x2, #0x808
    2060:	52801341 	mov	w1, #0x9a                  	// #154
    2064:	94003b0f 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:121
        else { fprintf(stderr, "Unknown option: %s\n", arg); return 2; }
    2068:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    206c:	f0000061 	adrp	x1, 11000 <sdsnew+0x94>
    2070:	911ab821 	add	x1, x1, #0x6ae
    2074:	17fffff1 	b	2038 <main+0x1120>
insert():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:82
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    2078:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    207c:	911fd400 	add	x0, x0, #0x7f5
    2080:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    2084:	9127b442 	add	x2, x2, #0x9ed
    2088:	52800a41 	mov	w1, #0x52                  	// #82
    208c:	94003b05 	bl	10ca0 <standalone_panic>
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:221
            for (size_t i = 0; i < n; i++) serverAssert(check.seen[i]);
    2090:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2094:	911fd400 	add	x0, x0, #0x7f5
    2098:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    209c:	91225842 	add	x2, x2, #0x896
    20a0:	52801ba1 	mov	w1, #0xdd                  	// #221
    20a4:	94003aff 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:233
            serverAssert(score == (double)order[i] + (double)(repeats * n));
    20a8:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    20ac:	911fd400 	add	x0, x0, #0x7f5
    20b0:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    20b4:	9124ec42 	add	x2, x2, #0x93b
    20b8:	52801d21 	mov	w1, #0xe9                  	// #233
    20bc:	94003af9 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:232
            serverAssert(zbtreeScore(tree, keys[order[i]], &score));
    20c0:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    20c4:	911fd400 	add	x0, x0, #0x7f5
    20c8:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    20cc:	91244442 	add	x2, x2, #0x911
    20d0:	52801d01 	mov	w1, #0xe8                  	// #232
    20d4:	94003af3 	bl	10ca0 <standalone_panic>
now_ns():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:26
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    20d8:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    20dc:	911fd400 	add	x0, x0, #0x7f5
    20e0:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    20e4:	91285842 	add	x2, x2, #0xa16
    20e8:	52800341 	mov	w1, #0x1a                  	// #26
    20ec:	94003aed 	bl	10ca0 <standalone_panic>
main():
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:188
                serverAssert(visited == n);
    20f0:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    20f4:	911fd400 	add	x0, x0, #0x7f5
    20f8:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    20fc:	91213c42 	add	x2, x2, #0x84f
    2100:	52801781 	mov	w1, #0xbc                  	// #188
    2104:	94003ae7 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:74
        fprintf(stderr, "Expected integer in [1, 100000000]: %s\n", s);
    2108:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    210c:	f0000061 	adrp	x1, 11000 <sdsnew+0x94>
    2110:	91271421 	add	x1, x1, #0x9c5
    2114:	f947e108 	ldr	x8, [x8, #4032]
    2118:	aa1403e2 	mov	x2, x20
    211c:	f9400100 	ldr	x0, [x8]
    2120:	97fffb28 	bl	dc0 <fprintf@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:75
        exit(2);
    2124:	52800040 	mov	w0, #0x2                   	// #2
    2128:	97ffface 	bl	c60 <exit@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:227
        serverAssert(zbtreeLength(tree) == (c == 7 ? 0 : n));
    212c:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2130:	911fd400 	add	x0, x0, #0x7f5
    2134:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    2138:	9123a842 	add	x2, x2, #0x8ea
    213c:	52801c61 	mov	w1, #0xe3                  	// #227
    2140:	94003ad8 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:226
        serverAssert(checksum == expected);
    2144:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2148:	911fd400 	add	x0, x0, #0x7f5
    214c:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    2150:	91235442 	add	x2, x2, #0x8d5
    2154:	52801c41 	mov	w1, #0xe2                  	// #226
    2158:	94003ad2 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:74
        fprintf(stderr, "Expected integer in [1, 100000000]: %s\n", s);
    215c:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    2160:	f0000061 	adrp	x1, 11000 <sdsnew+0x94>
    2164:	91271421 	add	x1, x1, #0x9c5
    2168:	f947e108 	ldr	x8, [x8, #4032]
    216c:	f9400100 	ldr	x0, [x8]
    2170:	97fffb14 	bl	dc0 <fprintf@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:75
        exit(2);
    2174:	52800040 	mov	w0, #0x2                   	// #2
    2178:	97fffaba 	bl	c60 <exit@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:216
            serverAssert(scanned.count >= count && scanned.count <= SIZE_MAX);
    217c:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2180:	911fd400 	add	x0, x0, #0x7f5
    2184:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    2188:	91218842 	add	x2, x2, #0x862
    218c:	52801b01 	mov	w1, #0xd8                  	// #216
    2190:	94003ac4 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:222
            serverAssert(scanned.count == check.result.count * traversals);
    2194:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    2198:	911fd400 	add	x0, x0, #0x7f5
    219c:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    21a0:	91229042 	add	x2, x2, #0x8a4
    21a4:	52801bc1 	mov	w1, #0xde                  	// #222
    21a8:	94003abe 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:202
                serverAssert(found);
    21ac:	f0000060 	adrp	x0, 11000 <sdsnew+0x94>
    21b0:	911fd400 	add	x0, x0, #0x7f5
    21b4:	f0000062 	adrp	x2, 11000 <sdsnew+0x94>
    21b8:	91217042 	add	x2, x2, #0x85c
    21bc:	52801941 	mov	w1, #0xca                  	// #202
    21c0:	94003ab8 	bl	10ca0 <standalone_panic>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:74
        fprintf(stderr, "Expected integer in [1, 100000000]: %s\n", s);
    21c4:	b0000168 	adrp	x8, 2f000 <__FRAME_END__+0x1b6fc>
    21c8:	f0000061 	adrp	x1, 11000 <sdsnew+0x94>
    21cc:	91271421 	add	x1, x1, #0x9c5
    21d0:	f947e108 	ldr	x8, [x8, #4032]
    21d4:	aa1c03e2 	mov	x2, x28
    21d8:	f9400100 	ldr	x0, [x8]
    21dc:	97fffaf9 	bl	dc0 <fprintf@plt>
<remote_repo>/scratch/arm-corrected-neon/B/bench/microbench.c:75
        exit(2);
    21e0:	52800040 	mov	w0, #0x2                   	// #2
    21e4:	97fffa9f 	bl	c60 <exit@plt>

Disassembly of section .fini:
