/* Correctness only: compare exact masks and enumeration against byte equality. */
#include "zset_btree.c"
static unsigned long checks, positions;

static void check(uint64_t word, uint8_t tag) {
    uint64_t expected = 0;
    unsigned wanted[8], count = 0;
    for (unsigned lane = 0; lane < 8; lane++) {
        if ((uint8_t)(word >> (lane * 8)) == tag) {
            expected |= UINT64_C(0x80) << (lane * 8);
            wanted[count++] = lane;
        }
    }
    uint64_t mask = zbtIndexExactTagMask(word, tag);
    serverAssert(mask == expected);
    unsigned got = 0;
    while (mask) {
        serverAssert(got < count);
        serverAssert(zbtIndexFirstTag(mask) == wanted[got]);
        mask &= mask - 1;
        got++; positions++;
    }
    serverAssert(got == count);
    checks++;
}
int main(void) {
    const uint64_t broadcast = UINT64_C(0x0101010101010101);
    /* All 256 query tags, 256 byte values and 8 positions. Other bytes
     * intentionally alternate real matches and high-bit nonmatches. */
    for (unsigned tag = 0; tag < 256; tag++) {
        for (unsigned byte = 0; byte < 256; byte++) {
            for (unsigned lane = 0; lane < 8; lane++) {
                uint64_t word = broadcast * tag;
                word ^= UINT64_C(0x8000800080008000);
                word &= ~(UINT64_C(0xff) << (lane * 8));
                word |= (uint64_t)byte << (lane * 8);
                check(word, tag);
            }
        }
    }
    /* Exhaust every adjacent pair of XOR bytes at all 7 boundaries.
     * Four surrounding XOR backgrounds cover borrow chains, high-bit
     * neighbors and no matches. Translation covers all query tags. */
    static const uint8_t backgrounds[] = {0, 1, 128, 255};
    for (unsigned bg = 0; bg < sizeof(backgrounds); bg++) {
        for (unsigned lane = 0; lane < 7; lane++) {
            for (unsigned pair = 0; pair < 65536; pair++) {
                uint8_t tag = (pair + (pair >> 8) + lane) & 255;
                uint64_t x = broadcast * backgrounds[bg];
                x &= ~(UINT64_C(0xffff) << (lane * 8));
                x |= (uint64_t)pair << (lane * 8);
                check(x ^ (broadcast * tag), tag);
            }
        }
    }
    uint64_t state = UINT64_C(0xa1d359f024687bce);
    for (unsigned i = 0; i < 100000; i++) {
        state ^= state << 13; state ^= state >> 7; state ^= state << 17;
        check(state, (uint8_t)(state >> 23));
        check(state, (uint8_t)state);
    }
    for (unsigned tag = 0; tag < 256; tag++) {
        check(broadcast * tag, tag);
        check(broadcast * (uint8_t)(tag ^ 128), tag);
    }
    serverAssert(zbtIndexTag(0) == 1);
    serverAssert(zbtIndexTag(UINT32_C(0x01000000)) == 1);
    printf("{\"passed\":true,\"mask_checks\":%lu,\"enumerated_positions\":%lu}\n",
           checks, positions);
    return 0;
}
