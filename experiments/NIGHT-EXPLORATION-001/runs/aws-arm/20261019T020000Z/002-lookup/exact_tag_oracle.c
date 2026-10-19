#include "../src/zset_btree.c"
#include <inttypes.h>
static uint64_t rng = UINT64_C(0x1847419834a5e091);
static uint64_t next_word(void) {
    rng ^= rng >> 12; rng ^= rng << 25; rng ^= rng >> 27;
    return rng * UINT64_C(2685821657736338717);
}
static uint64_t checked;
static void check(uint64_t word, uint8_t query) {
    uint64_t exact = 0;
    for (unsigned i = 0; i < 8; i++)
        if (((word >> (8*i)) & 255) == query) exact |= UINT64_C(128) << (8*i);
    uint64_t got = zbtIndexExactTagMask(word, query);
    serverAssert(got == exact);
    while (got) {
        unsigned first = zbtIndexFirstTag(got);
        serverAssert(first < 8 && ((word >> (8*first)) & 255) == query);
        got &= got - 1;
    }
    checked++;
}
int main(void) {
    for (unsigned query = 0; query < 256; query++) {
        check(0, query); check(UINT64_MAX, query);
        check(UINT64_C(0x0101010101010101)*query, query);
        for (unsigned pivot = 0; pivot < 8; pivot++)
            for (unsigned pattern = 0; pattern < 256; pattern++) {
                uint64_t word = 0;
                for (unsigned i = 0; i < 8; i++) {
                    unsigned byte = i == pivot ? query : ((pattern >> i) & 1 ? query ^ 1 : query ^ 255);
                    word |= (uint64_t)byte << (8*i);
                }
                check(word, query);
            }
    }
    for (unsigned i = 0; i < 1000000; i++) {
        uint64_t word = next_word(); check(word, (uint8_t)next_word());
    }
    printf("PASS exact-mask checks=%" PRIu64 "\n", checked);
}
