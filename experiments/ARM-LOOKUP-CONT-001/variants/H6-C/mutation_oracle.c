/* Correctness only: no timers, PMU events or performance output. */
#include "zset_btree.c"
#include <float.h>
int __failed_tests;
int __test_num;
static unsigned long validations, leaves_checked, moves;
static unsigned int saw_zero, saw_full, saw_reversed, codes_seen;

static unsigned int expected_code(unsigned int marker) {
    static const uint8_t lengths[] = {0,1,2,3,4,5,6,7,8,12,16,24,32,64,128};
    for (unsigned int i = 0; i < sizeof(lengths); i++)
        if (marker == lengths[i]) return i + 1;
    return 0;
}

static void check(zbtreeSet *zs) {
    serverAssert(zbtTestCheck(zs));
    for (zbtScoreLeaf *leaf = zs->score_first; leaf; leaf = leaf->next) {
        size_t capacity = zmalloc_usable_size(leaf);
        if (capacity > ZBT_SCORE_LEAF_BYTES) capacity = ZBT_SCORE_LEAF_BYTES;
        for (unsigned int i = 0; i < leaf->n.count; i++) {
            uint16_t descriptor = zbtScoreLeafOffsets(leaf)[i];
            unsigned int offset = zbtRecordOffset(descriptor);
            unsigned int code = zbtRecordLengthCode(descriptor);
            const unsigned char *record = (unsigned char *)leaf + offset;
            serverAssert(offset >= leaf->record_start && offset < capacity);
            serverAssert(offset + zbtRecordStorageBytes(record) <= capacity);
            serverAssert(code == expected_code(record[0]));
            serverAssert(!code || record[0] == zbtRecordInlineLengths[code]);
            serverAssert(zbtScoreLeafOffset(leaf, zbtScoreLeafPhysicalPos(leaf, i)) == offset);
            codes_seen |= 1u << code;
        }
        saw_zero |= leaf->score_bits == 0;
        saw_full |= leaf->score_bits == 64;
        saw_reversed |= leaf->reversed != 0;
        leaves_checked++;
    }
    validations++;
}

static void *copy_page(void *ptr) {
    size_t bytes = zmalloc_usable_size(ptr);
    void *copy = zmalloc(bytes);
    memcpy(copy, ptr, bytes);
    moves++;
    return copy;
}

/* Exercise the actual page relocation/repair helper, including inner pages. */
static void relocate(zbtreeSet *zs, zbtScoreNode *node) {
    if (!node->isleaf) {
        zbtScoreInner *inner = (zbtScoreInner *)node;
        for (unsigned int i = 0; i < inner->n.count; i++)
            relocate(zs, inner->child[i]);
    }
    zbtDefragScoreNode(zs, node, copy_page, zfree);
}

int main(void) {
    enum { N = 384 };
#if UINTPTR_MAX == UINT64_MAX
    serverAssert(sizeof(zbtScoreNode) == 24 && offsetof(zbtScoreLeaf, data) == 56);
#endif
    for (unsigned mode = 0; mode < 4; mode++) {
        uint8_t key[16];
        for (unsigned j = 0; j < sizeof(key); j++) key[j] = mode + 31 * j;
        dictSetHashFunctionSeed(key);
        zbtreeSet *zs = zbtreeCreate();
        sds members[N];
        for (unsigned i = 0; i < N; i++) {
            unsigned char buf[384];
            memset(buf, i, sizeof(buf));
            memcpy(buf, &i, sizeof(i));
            static const size_t lengths[] = {1,2,3,4,5,6,7,8,12,16,24,32,64,128,
                                              9,14,15,256,319,320,384};
            size_t len = i == 0 ? 0 : lengths[(i - 1) % (sizeof(lengths)/sizeof(*lengths))];
            members[i] = sdsnewlen(buf, len);
            double score = mode == 0 ? (double)i : mode == 1 ? -(double)i :
                           mode == 2 ? (i % 2 ? DBL_MAX : -DBL_MAX) : 0.0;
            zbtreeInsertNew(zs, score, members[i], NULL);
            check(zs);
        }
        /* Exercise copy ownership and page relocation before destructive work. */
        zbtreeSet *copy = zbtreeDup(zs);
        check(copy);
        relocate(copy, copy->score_root);
        check(copy);
        zbtreeFree(copy);
        for (unsigned round = 0; round < 3; round++) {
            for (unsigned i = 0; i < N; i++) {
                unsigned slot = (i * 193) % N;
                double score = round == 0 ? (double)(N - i) + 0.125 :
                               round == 1 ? ldexp((double)(i + 1), (int)(i % 80) - 40) :
                               (i % 2 ? INFINITY : -INFINITY);
                zbtTestSet(zs, members[slot], sdslen(members[slot]), score);
                check(zs);
            }
        }
        for (unsigned i = 0; i < N; i += 2) {
            serverAssert(zbtreeDelete(zs, members[i]));
            check(zs);
        }
        zbtreeShrinkToFit(zs);
        check(zs);
        unsigned edge = 0;
        while (zbtreeLength(zs)) {
            zbtreeDeleteEdge(zs, edge++ & 1);
            check(zs);
        }
        zbtreeFree(zs);
        for (unsigned i = 0; i < N; i++) sdsfree(members[i]);
    }
    /* A flush/rebuild path independent of ordinary insertion. */
    zbtreeSet *bulk = zbtreeCreate();
    zbtreeAppendBatch *batch = zbtreeAppendBatchCreate(bulk);
    for (unsigned i = 0; i < N; i++) {
        unsigned char key[16] = {0};
        memcpy(key, &i, sizeof(i));
        zbtreeAppendBatchAdd(batch, (double)i, key, sizeof(key));
    }
    zbtreeAppendBatchFinish(batch);
    check(bulk);
    zbtreeFree(bulk);
    serverAssert(saw_zero && saw_full && saw_reversed && codes_seen == 0xffff);
    printf("{\"passed\":true,\"zero_full_reversed\":true,\"all_descriptor_codes_seen\":true,\"validations\":%lu,"
           "\"leaves_checked\":%lu,\"relocated_pages\":%lu}\n",
           validations, leaves_checked, moves);
    return 0;
}
