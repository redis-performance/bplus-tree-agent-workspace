/* Correctness only: no timer, iteration throughput, PMU or performance output.
 * Compile with H2_ROTATED for H2-C, without it for the unchanged baseline. */
#include "zset_btree.c"
#include <float.h>

int __failed_tests, __test_num;
static unsigned long leaf_checks, matrix_cases, tree_checks;
static unsigned long odd_score_bases, external_records, rehash_states;

static unsigned char *score_data(zbtScoreLeaf *leaf) {
#ifdef H2_ROTATED
    return zbtScoreLeafScores(leaf);
#else
    return leaf->data;
#endif
}

static void layout_check(zbtScoreLeaf *leaf) {
    unsigned int n = leaf->n.count;
    size_t bytes = zbtScoreLeafScoreBytes(n, leaf->score_bits);
    unsigned char *offsets = (unsigned char *)zbtScoreLeafOffsets(leaf);
    unsigned char *tags = zbtScoreLeafHashTags(leaf);
    unsigned char *scores = score_data(leaf);
    serverAssert(n && n <= ZBT_SCORE_LEAF_MAX);
    serverAssert(sizeof(zbtScoreNode) == 24 && offsetof(zbtScoreLeaf, data) == 56);
    serverAssert((uintptr_t)offsets % _Alignof(uint16_t) == 0);
#ifdef H2_ROTATED
    serverAssert(offsets == leaf->data && tags == leaf->data + 2*n);
    serverAssert(scores == leaf->data + 3*n);
    serverAssert(scores + bytes <= (unsigned char *)leaf + leaf->record_start);
#else
    serverAssert(scores == leaf->data && offsets == scores + bytes);
    serverAssert(tags == offsets + 2*n);
    serverAssert(tags + n <= (unsigned char *)leaf + leaf->record_start);
#endif
    if ((uintptr_t)scores & 1) odd_score_bases++;
    serverAssert(leaf->n.subtree == n);
    for (unsigned int i = 0; i < n; i++) {
        uint16_t offset = zbtScoreLeafOffset(leaf, i);
        unsigned char *record = (unsigned char *)leaf + offset;
        size_t record_bytes = zbtRecordStorageBytes(record);
        serverAssert(offset >= leaf->record_start);
        serverAssert(offset + record_bytes <= ZBT_SCORE_LEAF_BYTES);
        serverAssert(offset + record_bytes <= zmalloc_usable_size(leaf));
        if (record[0] == ZBT_PACKED_EXTERNAL) {
            serverAssert(leaf->n.has_external && zbtExternalPointer(record));
            external_records++;
        }
        for (unsigned int j = 0; j < i; j++) {
            uint16_t other = zbtScoreLeafOffset(leaf, j);
            size_t other_bytes = zbtRecordStorageBytes((unsigned char *)leaf + other);
            serverAssert(offset + record_bytes <= other || other + other_bytes <= offset);
        }
    }
    leaf_checks++;
}

static void encode_id(unsigned char key[2], unsigned int id) {
    key[0] = id >> 8;
    key[1] = id & 255;
}

static void matrix_check(zbtScoreLeaf *leaf, unsigned int n,
                         const double *scores, const unsigned int *ids) {
    layout_check(leaf);
    serverAssert(leaf->n.count == n);
    for (unsigned int i = 0; i < n; i++) {
        unsigned char key[2]; encode_id(key, ids[i]);
        double actual = zbtScoreLeafScore(leaf, i);
        serverAssert(memcmp(&actual, &scores[i], sizeof(actual)) == 0);
        size_t len;
        const unsigned char *ele = zbtScoreLeafElement(leaf, i, &len);
        serverAssert(len == 2 && memcmp(ele, key, 2) == 0);
        uint32_t hash = zbtreeMemberHash(key, 2);
        serverAssert(zbtScoreLeafTag(leaf, i) == hash >> 24);
        unsigned int pos = UINT_MAX;
        serverAssert(zbtScoreLeafFindMember(leaf, hash, key, 2, &actual, &pos));
        serverAssert(pos == i && memcmp(&actual, &scores[i], sizeof(actual)) == 0);
    }
}

static void matrix_case(unsigned int bits, unsigned int shift,
                         unsigned int n, int reverse, unsigned int insertion) {
    double expected[ZBT_SCORE_LEAF_MAX] = {0};
    unsigned int ids[ZBT_SCORE_LEAF_MAX] = {0};
    zbtreeSet *zs = zbtreeCreate();
    zbtScoreLeaf *leaf = zbtAlloc(zs, ZBT_SCORE_LEAF_BYTES);
    memset(leaf, 0, ZBT_SCORE_LEAF_BYTES);
    leaf->n.isleaf = 1;
    leaf->n.count = leaf->n.subtree = n;
    leaf->n.score_shift = shift;
    leaf->score_bits = bits;
    leaf->reversed = reverse;
    uint64_t low = zbtScoreToOrdered(-DBL_MAX), high = zbtScoreToOrdered(DBL_MAX);
    leaf->score_base = reverse ? high : low;
    uint64_t maximum = bits == 64 ? UINT64_MAX : (UINT64_C(1) << bits) - 1;
    if (maximum > ((high - low) >> shift)) maximum = (high - low) >> shift;
    unsigned char *record = (unsigned char *)leaf + ZBT_SCORE_LEAF_BYTES;
    for (unsigned int i = 0; i < n; i++) {
        /* Use a wide intermediate only in the independent expected-value model. */
        uint64_t delta = (__uint128_t)maximum * (reverse ? n-i : i) / n;
        uint64_t ordered = reverse ? high - (delta << shift) : low + (delta << shift);
        expected[i] = zbtOrderedToScore(ordered);
        serverAssert(isfinite(expected[i]));
        ids[i] = 4*i + 2;
        record -= 3; record[0] = 2; encode_id(record + 1, ids[i]);
        unsigned int physical = zbtScoreLeafPhysicalPos(leaf, i);
        zbtScoreLeafOffsets(leaf)[physical] = record - (unsigned char *)leaf;
        zbtScoreLeafHashTags(leaf)[physical] = zbtreeMemberHash(record+1, 2) >> 24;
        zbtScoreLeafWriteScore(leaf, i, expected[i]);
    }
    leaf->record_start = record - (unsigned char *)leaf;
    matrix_check(leaf, n, expected, ids);

    unsigned char key[2]; encode_id(key, 4*insertion + 1);
    double value = expected[insertion < n ? insertion : n-1];
    zbtBuildElement item = {.ptr=key, .len=2, .hash=zbtreeMemberHash(key, 2)};
    serverAssert(zbtScoreInsertFast(zs, leaf, value, &item, item.hash >> 24, insertion));
    memmove(expected+insertion+1, expected+insertion, (n-insertion)*sizeof(*expected));
    memmove(ids+insertion+1, ids+insertion, (n-insertion)*sizeof(*ids));
    expected[insertion] = value; ids[insertion] = 4*insertion + 1; n++;
    matrix_check(leaf, n, expected, ids);

    zbtScoreDeleteInPlace(zs, leaf, insertion, (bits+n)&1);
    n--;
    memmove(expected+insertion, expected+insertion+1, (n-insertion)*sizeof(*expected));
    memmove(ids+insertion, ids+insertion+1, (n-insertion)*sizeof(*ids));
    matrix_check(leaf, n, expected, ids);
    if (!reverse) {
        zbtScoreLeafReverseForPop(leaf);
        matrix_check(leaf, n, expected, ids);
    }
    while (n > 1) {
        unsigned int pos = n % 3 == 0 ? 0 : n % 3 == 1 ? n/2 : n-1;
        zbtScoreDeleteInPlace(zs, leaf, pos, n&1);
        n--;
        memmove(expected+pos, expected+pos+1, (n-pos)*sizeof(*expected));
        memmove(ids+pos, ids+pos+1, (n-pos)*sizeof(*ids));
        matrix_check(leaf, n, expected, ids);
    }
    zbtScoreLeafFreeOwned(zs, leaf);
    zbtreeFree(zs);
    matrix_cases++;
}

#define ITEMS 384
static sds keys[ITEMS];
static double model[ITEMS];
static unsigned char present[ITEMS];

static void tree_check(zbtreeSet *zs) {
    unsigned int count = 0;
    serverAssert(zbtTestCheck(zs));
    if (zs->member_rehash) rehash_states++;
    for (zbtScoreLeaf *leaf = zs->score_first; leaf; leaf = leaf->next)
        layout_check(leaf);
    for (unsigned int i = 0; i < ITEMS; i++) {
        double score = 42;
        int found = zbtreeScore(zs, keys[i], &score);
        serverAssert(found == present[i]);
        if (found) {
            count++;
            serverAssert(memcmp(&score, &model[i], sizeof(score)) == 0);
        }
    }
    serverAssert(zbtreeLength(zs) == count);
    tree_checks++;
}

static void *move_copy(void *old) {
    size_t bytes = zmalloc_usable_size(old);
    void *copy = zmalloc(bytes);
    memcpy(copy, old, bytes);
    return copy;
}

static void *move_and_free(void *old) {
    void *copy = move_copy(old);
    zfree(old);
    return copy;
}

static void mixed_tree(void) {
    const size_t lengths[] = {2,3,7,8,9,253,254,255,256,319,320,321,384};
    for (unsigned int i = 0; i < ITEMS; i++) {
        size_t len = i < 2 ? i : lengths[i % (sizeof(lengths)/sizeof(*lengths))];
        unsigned char buf[384];
        for (size_t j = 0; j < sizeof(buf); j++) buf[j] = (unsigned char)(j*17+i);
        encode_id(buf, i);
        keys[i] = sdsnewlen(buf, len);
        model[i] = (int)((i*137)%ITEMS) - ITEMS/2;
    }
    model[0] = -INFINITY; model[1] = INFINITY; model[2] = -0.0; model[3] = 0.0;
    zbtreeSet *zs = zbtreeCreate();
    for (unsigned int k = 0; k < ITEMS; k++) {
        unsigned int i = (k*313)%ITEMS;
        zbtreeInsertNew(zs, model[i], keys[i], NULL); present[i] = 1;
        if (k % 16 == 0) tree_check(zs);
    }
    tree_check(zs);
    for (unsigned int k = 0; k < ITEMS*2; k++) {
        unsigned int i = (k*251)%ITEMS;
        zbtreeInsertPosition position;
        serverAssert(zbtreeFindForAdd(zs, keys[i], NULL, &position));
        model[i] = k % 4 == 0 ? -0.0 : k % 4 == 1 ? 0.0 : ((int)ITEMS-(int)k)*0.125;
        zbtreeUpdateScore(zs, keys[i], model[i], &position);
        if (k % 16 == 0) tree_check(zs);
    }
    tree_check(zs);
    zbtreeSet *copy = zbtreeDup(zs);
    tree_check(copy);
    copy = zbtreeDefragStart(copy, move_and_free);
    zbtreeDefragState state = {0};
    unsigned long scanned = 0, steps = 0;
    while (!zbtreeDefragStep(copy, &state, move_copy, zfree, &scanned))
        serverAssert(++steps < 100000);
    tree_check(copy);
    zbtreeFree(copy);
    for (unsigned int k = 0; k < ITEMS; k++) {
        unsigned int i = (k*313)%ITEMS;
        serverAssert(zbtreeDelete(zs, keys[i])); present[i] = 0;
        if (k % 16 == 0 || k + 16 >= ITEMS) tree_check(zs);
    }
    tree_check(zs);
    zbtreeFree(zs);

    zs = zbtreeCreate();
    zbtreeAppendBatch *batch = zbtreeAppendBatchCreate(zs);
    for (unsigned int i = 0; i < ITEMS; i++) {
        model[i] = i; present[i] = 1;
        zbtreeAppendBatchAdd(batch, model[i], (unsigned char *)keys[i], sdslen(keys[i]));
    }
    zbtreeAppendBatchFinish(batch);
    tree_check(zs);
    for (unsigned int i = 0; i < ITEMS; i++) {
        zbtreeDeleteEdge(zs, 0); present[i] = 0;
        if (i % 16 == 0 || i+16 >= ITEMS) tree_check(zs);
    }
    zbtreeFree(zs);
    for (unsigned int i = 0; i < ITEMS; i++) sdsfree(keys[i]);
}

int main(void) {
    const unsigned int counts[] = {1,2,3,7,8,9,15,16,31,32,63,64,94,95};
    uint8_t seed[16]; for (unsigned int i=0; i<16; i++) seed[i]=17+29*i;
    dictSetHashFunctionSeed(seed);
    for (unsigned int bits=0; bits<=64; bits++)
        for (unsigned int sh=0; sh<2; sh++) {
            if (sh && (bits==0 || bits==64)) continue;
            unsigned int shift = sh ? 64-bits : 0;
            for (unsigned int k=0; k<sizeof(counts)/sizeof(*counts); k++)
                for (int reverse=0; reverse<2; reverse++)
                    for (unsigned int where=0; where<3; where++) {
                        unsigned int n=counts[k];
                        unsigned int pos=where==0 ? 0 : where==1 ? n/2 : n;
                        matrix_case(bits,shift,n,reverse,pos);
                    }
        }
    mixed_tree();
#ifdef H2_ROTATED
    serverAssert(odd_score_bases > 0);
#endif
    serverAssert(external_records > 0 && rehash_states > 0);
    printf("{\"passed\":true,\"matrix_cases\":%lu,\"leaf_checks\":%lu,"
           "\"tree_checks\":%lu,\"odd_score_bases\":%lu,\"external_record_checks\":%lu,"
           "\"rehash_states\":%lu}\n",matrix_cases,leaf_checks,tree_checks,
           odd_score_bases,external_records,rehash_states);
    return 0;
}
