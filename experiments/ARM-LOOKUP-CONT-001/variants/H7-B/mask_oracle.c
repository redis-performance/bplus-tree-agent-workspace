/* Correctness only. Exhaustive byte/lane and adjacent-XOR-byte checks. */
#include "zset_btree.c"
static unsigned long checks, enumerated, false_approx;

static void check(uint64_t tags, uint8_t tag) {
    uint64_t want=0;
    for (unsigned int lane=0;lane<8;lane++)
        if ((uint8_t)(tags>>(lane*8))==tag) want|=UINT64_C(0x80)<<(lane*8);
    uint64_t mask=zbtIndexExactTagMask(tags,tag);
    serverAssert(mask==want);
    uint64_t approximate=zbtIndexTagMask(tags,tag);
    serverAssert((approximate & want)==want && !!approximate==!!want);
    false_approx+=approximate!=want;
    unsigned int last=0, count=0;
    while (mask) {
        unsigned int lane=zbtIndexFirstTag(mask);
        serverAssert(lane<8 && (!count || lane>last));
        serverAssert((uint8_t)(tags>>(lane*8))==tag);
        last=lane;count++;enumerated++;
        want &= ~(UINT64_C(0x80)<<(lane*8));
        mask &= mask-1;
    }
    serverAssert(want==0);checks++;
}

int main(void) {
    const uint64_t broadcast=UINT64_C(0x0101010101010101);
    for (unsigned int tag=0;tag<256;tag++) {
        serverAssert(zbtIndexTag(tag<<24)==(tag ? tag : 1));
        for (unsigned int byte=0;byte<256;byte++) {
            check(broadcast*byte,tag);
            for (unsigned int lane=0;lane<8;lane++) {
                uint64_t lane_mask=UINT64_C(0xff)<<(lane*8);
                /* All other lanes equal and all other lanes unequal. */
                check(((broadcast*tag)&~lane_mask)|((uint64_t)byte<<(lane*8)),tag);
                check(((broadcast*(tag^1))&~lane_mask)|((uint64_t)byte<<(lane*8)),tag);
            }
        }
    }
    /* Exhaust every adjacent pair of XOR bytes in every numeric lane pair,
     * under five query translations. Backgrounds exercise long borrow chains
     * and high-bit bytes; equality is still recomputed from actual tags. */
    const uint8_t translations[]={0,1,127,128,255};
    for (unsigned int t=0;t<sizeof(translations);t++)
        for (unsigned int lane=0;lane<7;lane++)
            for (unsigned int pair=0;pair<65536;pair++) {
                uint64_t x=(lane&1) ? UINT64_C(0x8181818181818181) : UINT64_C(0x0101010101010100);
                x=(x&~(UINT64_C(0xffff)<<(lane*8)))|((uint64_t)pair<<(lane*8));
                check(x^(broadcast*translations[t]),translations[t]);
            }
    uint64_t state=UINT64_C(0x812736451aef498d);
    for (unsigned int i=0;i<100000;i++) {
        state=state*UINT64_C(6364136223846793005)+UINT64_C(1442695040888963407);
        check(state,(uint8_t)(i*71));
    }
    serverAssert(false_approx && enumerated);
    printf("{\"passed\":true,\"mask_checks\":%lu,\"enumerated_lanes\":%lu,\"approximate_false_masks\":%lu}\n",
           checks,enumerated,false_approx);
}
