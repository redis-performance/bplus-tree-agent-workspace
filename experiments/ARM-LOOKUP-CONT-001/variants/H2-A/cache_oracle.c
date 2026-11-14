/* Correctness only: no timers or performance counters. */
#include "zset_btree.c"
#include <float.h>

static unsigned long cache_checks, mutations, relocations;
static void check_leaf(zbtScoreLeaf *leaf) {
    serverAssert(leaf->score_bytes ==
        zbtScoreLeafScoreBytes(leaf->n.count, leaf->score_bits));
    serverAssert((unsigned char *)zbtScoreLeafOffsets(leaf) ==
                 leaf->data + leaf->score_bytes);
    cache_checks++;
}
static void check_tree(zbtreeSet *t) {
    unsigned long count = 0;
    for (zbtScoreLeaf *leaf = t->score_first; leaf; leaf = leaf->next) {
        check_leaf(leaf);
        count += leaf->n.count;
        for (unsigned i = 0; i < leaf->n.count; i++) {
            size_t len;
            const unsigned char *key = zbtScoreLeafElement(leaf, i, &len);
            double expected = zbtScoreLeafScore(leaf, i), actual;
            serverAssert(zbtreeScoreRaw(t, key, len, &actual));
            serverAssert(memcmp(&actual, &expected, sizeof(actual)) == 0);
        }
    }
    serverAssert(count == zbtreeLength(t));
}

/* Exercise every width and count transition directly, including reversal.
 * This isolated leaf fixture does not construct a member index. */
static void all_widths(void) {
    for (unsigned bits = 0; bits <= 64; bits++) {
        for (unsigned reversed = 0; reversed < 2; reversed++) {
            zbtreeSet *t = zbtreeCreate();
            double scores[ZBT_SCORE_LEAF_MAX];
            unsigned char keys[ZBT_SCORE_LEAF_MAX][4];
            zbtBuildElement elems[ZBT_SCORE_LEAF_MAX] = {{0}};
            uint8_t tags[ZBT_SCORE_LEAF_MAX];
            uint64_t low = UINT64_C(0x0010000000000000);
            uint64_t high = bits == 64 ? UINT64_C(0xffefffffffffffff) :
                            low + (bits ? (UINT64_C(1) << bits) - 1 : 0);
            for (unsigned i = 0; i < ZBT_SCORE_LEAF_MAX; i++) {
                scores[i] = zbtOrderedToScore(i + 1 == ZBT_SCORE_LEAF_MAX ? high : low);
                keys[i][0] = 0; keys[i][1] = 255;
                keys[i][2] = i; keys[i][3] = bits;
                elems[i].ptr = keys[i]; elems[i].len = sizeof(keys[i]);
                elems[i].hash = zbtreeMemberHash(keys[i], sizeof(keys[i]));
                tags[i] = elems[i].hash >> 24;
            }
            zbtScoreLeaf *leaf = zbtScoreLeafBuild(t, ZBT_SCORE_LEAF_MAX,
                scores, elems, tags, ZBT_NEW_LEAF_ID, 1);
            t->score_root = &leaf->n; t->score_first = t->score_last = leaf;
            serverAssert(leaf->score_bits == bits);
            if (reversed) zbtScoreLeafReverseForPop(leaf);
            check_leaf(leaf);
            for (unsigned i = 0; i + 1 < ZBT_SCORE_LEAF_MAX; i++) {
                zbtScoreDeleteInPlace(t, leaf, 0, 1);
                check_leaf(leaf); mutations++;
            }
            for (unsigned i = ZBT_SCORE_LEAF_MAX - 1; i > 0; i--) {
                serverAssert(zbtScoreInsertFast(t, leaf, scores[i-1],
                                               &elems[i-1], tags[i-1], 0));
                check_leaf(leaf); mutations++;
            }
            for (unsigned i = 0; i < ZBT_SCORE_LEAF_MAX; i++) {
                size_t len;
                const unsigned char *key = zbtScoreLeafElement(leaf, i, &len);
                double score = zbtScoreLeafScore(leaf, i);
                serverAssert(len == sizeof(keys[i]) && !memcmp(key, keys[i], len));
                serverAssert(!memcmp(&score, &scores[i], sizeof(score)));
            }
            zbtreeFree(t);
        }
    }
}

static void *copy_alloc(void *old) {
    size_t bytes = zmalloc_usable_size(old);
    void *copy = zmalloc(bytes);
    memcpy(copy, old, bytes); relocations++;
    return copy;
}
static void *move_plain(void *old) {
    void *copy = copy_alloc(old); zfree(old); return copy;
}
static void free_old(void *old) { zfree(old); }
static zbtreeSet *relocate(zbtreeSet *t) {
    t = zbtreeDefragStart(t, move_plain);
    zbtreeDefragState state;
    zbtreeDefragStateReset(&state);
    unsigned long scanned;
    while (!zbtreeDefragStep(t, &state, copy_alloc, free_old, &scanned))
        check_tree(t);
    check_tree(t);
    return t;
}

static void public_mutations(void) {
    enum { N = 600 };
    sds keys[N];
    const size_t lens[] = {4, 255, 256, 319, 320, 384};
    zbtreeSet *t = zbtreeCreate();
    for (unsigned i = 0; i < N; i++) {
        unsigned char key[384]; memset(key, i, sizeof(key));
        key[0] = i >> 8; key[1] = i; key[2] = 0; key[3] = 255;
        keys[i] = sdsnewlen(key, lens[i % 6]);
        zbtreeInsertNew(t, -(double)i, keys[i], NULL);
        check_tree(t); mutations++;
    }
    /* Re-encode, relocate in score order, preserve both zero signs and extremes. */
    const double values[] = {-DBL_MAX, -1.125, -0.0, 0.0, 0.125, DBL_MAX};
    for (unsigned i = 0; i < N; i++) {
        unsigned at = (i * 137) % N;
        zbtreeInsertPosition pos; double score;
        serverAssert(zbtreeFindForAdd(t, keys[at], &score, &pos));
        zbtreeUpdateScore(t, keys[at], values[i % 6], &pos);
        check_tree(t); mutations++;
    }
    zbtreeSet *copy = zbtreeDup(t); check_tree(copy);
    copy = relocate(copy); zbtreeFree(copy);
    t = relocate(t);
    for (unsigned i = 0; i < N; i += 3) {
        serverAssert(zbtreeDelete(t, keys[i]));
        check_tree(t); mutations++;
    }
    while (zbtreeLength(t)) {
        zbtreeDeleteEdge(t, zbtreeLength(t) % 2);
        check_tree(t); mutations++;
    }
    zbtreeFree(t);
    for (unsigned i = 0; i < N; i++) sdsfree(keys[i]);

    /* Bulk building and duplicate/relocation of equal-width pages. */
    t = zbtreeCreate();
    zbtreeAppendBatch *batch = zbtreeAppendBatchCreate(t);
    for (unsigned i = 0; i < N; i++) {
        unsigned char key[] = {i >> 8, i, 0, 255};
        zbtreeAppendBatchAdd(batch, i * 0.125, key, sizeof(key));
    }
    zbtreeAppendBatchFinish(batch); check_tree(t);
    copy = zbtreeDup(t); check_tree(copy); zbtreeFree(copy);
    t = relocate(t); zbtreeFree(t);
}

int main(void) {
    _Static_assert(sizeof(zbtScoreNode) == 24, "unchanged node header");
    _Static_assert(offsetof(zbtScoreLeaf, data) == 64, "declared leaf header cost");
    uint8_t seed[16] = {17, 29, 43}; dictSetHashFunctionSeed(seed);
    all_widths(); public_mutations();
    printf("{\"passed\":true,\"widths\":65,\"counts\":96,\"cache_checks\":%lu,"
           "\"mutations\":%lu,\"relocations\":%lu,\"leaf_header\":%zu}\n",
           cache_checks, mutations, relocations, offsetof(zbtScoreLeaf, data));
    return 0;
}
