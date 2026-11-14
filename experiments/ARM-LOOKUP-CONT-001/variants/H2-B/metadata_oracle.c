/* Correctness only: no timers, PMU events or performance output. */
#include "zset_btree.c"
#include <float.h>
int __failed_tests;
int __test_num;
static unsigned long validations, leaves_checked, moves;
static unsigned int saw_zero, saw_full, saw_reversed;

static void check(zbtreeSet *zs) {
    serverAssert(zbtTestCheck(zs));
    for (zbtScoreLeaf *leaf = zs->score_first; leaf; leaf = leaf->next) {
        serverAssert(zbtScoreNodeIsLeaf(&leaf->n));
        serverAssert(leaf->n.score_bytes ==
                     zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
        serverAssert((unsigned char *)zbtScoreLeafOffsets(leaf) ==
                     leaf->data + leaf->n.score_bytes);
        serverAssert(leaf->score_bits <= 64 && zbtScoreLeafShift(leaf) <= 63);
        serverAssert((uintptr_t)zbtScoreLeafOffsets(leaf) % 2 == 0);
        for (unsigned int j = 0; j < leaf->n.count; j++) {
            if (zbtScoreLeafRecord(leaf, j)[0] == ZBT_PACKED_EXTERNAL)
                serverAssert(zbtScoreLeafHasExternal(leaf));
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
    if (!zbtScoreNodeIsLeaf(node)) {
        zbtScoreInner *inner = (zbtScoreInner *)node;
        for (unsigned int i = 0; i < inner->n.count; i++)
            relocate(zs, inner->child[i]);
    }
    zbtDefragScoreNode(zs, node, copy_page, zfree);
}

static void flag_cases(void) {
    zbtScoreLeaf leaf = {0};
    for (unsigned flags = 0; flags < 4; flags++) {
        leaf.n.flags = (flags & 1 ? ZBT_NODE_IS_LEAF : 0) |
                       (flags & 2 ? ZBT_NODE_HAS_EXTERNAL : 0);
        leaf.n.moved_out = UINT8_MAX;
        leaf.n.index_resize = UINT16_MAX;
        leaf.n.score_bytes = 776;
        for (unsigned shift = 0; shift < 64; shift++) {
            zbtScoreLeafSetShift(&leaf, shift);
            serverAssert(zbtScoreLeafShift(&leaf) == shift);
            serverAssert(zbtScoreNodeIsLeaf(&leaf.n) == !!(flags & 1));
            serverAssert(zbtScoreLeafHasExternal(&leaf) == !!(flags & 2));
            serverAssert(leaf.n.moved_out == UINT8_MAX);
            serverAssert(leaf.n.index_resize == UINT16_MAX);
            serverAssert(leaf.n.score_bytes == 776);
        }
    }
}

int main(void) {
    enum { N = 384 };
    flag_cases();
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
            size_t len = i % 3 == 0 ? 12 : i % 3 == 1 ? 256 : 384;
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
    serverAssert(saw_zero && saw_full && saw_reversed);
    printf("{\"passed\":true,\"zero_full_reversed\":true,\"flag_shift_cases\":256,\"validations\":%lu,"
           "\"leaves_checked\":%lu,\"relocated_pages\":%lu}\n",
           validations, leaves_checked, moves);
    return 0;
}
