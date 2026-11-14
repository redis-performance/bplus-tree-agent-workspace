/* Correctness only: scalar truth tables, guard-ended scans and references. */
#define _GNU_SOURCE
#include <sys/mman.h>
#include <unistd.h>
#include "zset_btree.c"
int __failed_tests;
int __test_num;
static unsigned long masks, scans, references;

static uint64_t scalar_mask(uint64_t word, uint8_t tag) {
    uint64_t expected = 0;
    for (unsigned i = 0; i < 8; i++)
        if ((uint8_t)(word >> (8*i)) == tag)
            expected |= UINT64_C(0x80) << (8*i);
    return expected;
}

static void check_mask(uint64_t word, uint8_t tag) {
    uint64_t expected = scalar_mask(word, tag);
    uint64_t actual = zbtIndexTagMask(word, tag);
    serverAssert(actual == expected);
    unsigned next = 0;
    while (actual) {
        while (next < 8 && (uint8_t)(word >> (8*next)) != tag) next++;
        serverAssert(next < 8 && zbtIndexFirstTag(actual) == next);
        actual &= actual - 1;
        next++;
    }
    serverAssert((expected != 0) == (scalar_mask(word, tag) != 0));
    masks++;
}

static void truth_tables(void) {
    const uint64_t ones = UINT64_C(0x0101010101010101);
    for (unsigned tag = 0; tag < 256; tag++) {
        for (unsigned byte = 0; byte < 256; byte++) {
            check_mask(ones * byte, tag);
            for (unsigned lane = 0; lane < 8; lane++) {
                uint64_t mask = UINT64_C(0xff) << (8*lane);
                check_mask((ones * tag & ~mask) | (uint64_t)byte << (8*lane), tag);
                check_mask((ones * (tag ^ 1) & ~mask) | (uint64_t)byte << (8*lane), tag);
            }
        }
        /* Every zero/nonzero equality pattern, including long borrow chains. */
        for (unsigned bits = 0; bits < 256; bits++) {
            uint64_t word = 0;
            for (unsigned lane = 0; lane < 8; lane++)
                word |= (uint64_t)(tag ^ ((bits >> lane & 1) ? 0 : 1)) << (8*lane);
            check_mask(word, tag);
            check_mask(word ^ UINT64_C(0x8080808080808080), tag);
        }
    }
    /* Exhaust every adjacent byte pair at every boundary. Translate x by a
     * varied query byte; scalar truth never uses the candidate arithmetic. */
    for (unsigned lane = 0; lane < 7; lane++)
        for (unsigned pair = 0; pair < 65536; pair++) {
            uint8_t tag = (uint8_t)(pair * 37 + lane * 19);
            uint64_t word = ones * (tag ^ 1);
            uint64_t mask = UINT64_C(0xffff) << (8*lane);
            word = (word & ~mask) | ((uint64_t)pair << (8*lane));
            check_mask(word, tag);
            check_mask(word, 0);
            check_mask(word, 255);
        }
    uint64_t state = UINT64_C(0x6d49307a1c2b895f);
    for (unsigned i = 0; i < 100000; i++) {
        state ^= state << 13; state ^= state >> 7; state ^= state << 17;
        check_mask(state, (uint8_t)(state >> 32));
    }
}

static void scan_words(void) {
    long page = sysconf(_SC_PAGESIZE);
    serverAssert(page >= ZBT_SCORE_LEAF_MAX);
    unsigned char *map = mmap(NULL, (size_t)page * 2, PROT_READ | PROT_WRITE,
                              MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    serverAssert(map != MAP_FAILED);
    serverAssert(mprotect(map + page, (size_t)page, PROT_NONE) == 0);
    for (unsigned count = 0; count <= ZBT_SCORE_LEAF_MAX; count++) {
        unsigned char *tags = map + page - count;
        for (unsigned pattern = 0; pattern < 4; pattern++) {
            for (unsigned i = 0; i < count; i++) {
                static const uint8_t adversary[] = {0,1,0,1,127,128,254,255};
                tags[i] = pattern == 0 ? adversary[i % 8] :
                          pattern == 1 ? (uint8_t)(37*i + count) :
                          pattern == 2 ? 0 : 1;
            }
            for (unsigned tag = 0; tag < 256; tag++)
                for (unsigned reversed = 0; reversed < 2; reversed++) {
                    unsigned actual[ZBT_SCORE_LEAF_MAX+1], expected[ZBT_SCORE_LEAF_MAX];
                    for (unsigned i = 0; i <= ZBT_SCORE_LEAF_MAX; i++) actual[i] = UINT_MAX;
                    unsigned n = 0;
                    for (unsigned i = 0; i < count; i++)
                        if (tags[i] == tag || (tag == 1 && tags[i] == 0))
                            expected[n++] = reversed ? count-1-i : i;
                    unsigned got = zbtLeafTagMatches(tags, count, reversed, tag, actual);
                    serverAssert(got == n && actual[n] == UINT_MAX);
                    for (unsigned i = 0; i < n; i++) serverAssert(actual[i] == expected[i]);
                    scans++;
                }
        }
    }
    serverAssert(munmap(map, (size_t)page * 2) == 0);
}

static int scalar_reference(zbtIndexTable *t, uint32_t hash, uint32_t id,
                             zbtIndexBucket **bucket, unsigned *slot) {
    if (!t->size || !zbtIndexHomeMayContain(t, hash)) return 0;
    unsigned long index = hash & (t->size-1);
    for (unsigned long probe = 0; probe < t->size; probe++) {
        zbtIndexBucket *b = zbtIndexBucketAt(t, index);
        int empty = 0;
        for (unsigned i = 0; i < 8; i++) {
            uint8_t tag = (uint8_t)(zbtIndexTags(b) >> (8*i));
            if (tag == zbtIndexTag(hash) && zbtIndexGetId(t, b, i) == id) {
                *bucket = b; *slot = i; return 1;
            }
            empty |= tag == 0;
        }
        if (empty) return 0;
        index = (index+1) & (t->size-1);
    }
    return 0;
}

static void reference_pairs(void) {
    for (unsigned wide = 0; wide < 2; wide++) {
        zbtIndexTable table = {.size=4, .wide_ids=(int)wide};
        table.buckets = calloc(table.size, zbtIndexBucketBytes(&table));
        serverAssert(table.buckets);
        for (unsigned pattern = 0; pattern < 256; pattern++) {
            for (unsigned b = 0; b < 4; b++) {
                zbtIndexBucket *bucket = zbtIndexBucketAt(&table,b);
                bucket->narrow.tags = 0;
                bucket->narrow.home_tags = UINT64_MAX;
                for (unsigned i = 0; i < 8; i++) {
                    uint8_t tag = (uint8_t)(pattern + (i % 3));
                    zbtIndexSetTag(bucket,i,tag);
                    uint32_t id = wide ? 70000 + i + b : 1 + i + b;
                    if (i == 2) id = ZBT_INDEX_DELETED_ID;
                    zbtIndexSetId(&table,bucket,i,id);
                }
            }
            for (unsigned tag = 0; tag < 256; tag++)
                for (unsigned q = 0; q < 12; q++) {
                    uint32_t hash = (uint32_t)tag << 24 | 3;
                    uint32_t id = (wide ? 70000 : 1) + q;
                    if (q == 11) id = ZBT_INDEX_DELETED_ID;
                    zbtIndexBucket *a = NULL, *b = NULL;
                    unsigned ap = UINT_MAX, bp = UINT_MAX;
                    int x = scalar_reference(&table,hash,id,&a,&ap);
                    int y = zbtIndexTableFindReference(&table,hash,id,&b,&bp);
                    serverAssert(x == y && a == b && ap == bp);
                    references++;
                }
        }
        free(table.buckets);
    }
}

int main(void) {
    truth_tables(); scan_words(); reference_pairs();
    printf("{\"passed\":true,\"exact_masks\":%lu,\"guard_ended_scans\":%lu,"
           "\"reference_pairs\":%lu}\n", masks,scans,references);
    return 0;
}
