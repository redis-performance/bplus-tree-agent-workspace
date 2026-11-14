/* Correctness only. Direct index fixtures plus full-tree resize transitions. */
#define REDIS_TEST
#include "zset_btree.c"
int __failed_tests, __test_num;
static unsigned long reference_checks, table_checks, resize_steps, completions;

static void wrapped(unsigned wide) {
    zbtreeSet *zs = zbtreeCreate();
    zbtIndexTable *table = &zs->member_index;
    zbtIndexTableInit(zs, table, 4, wide);
    uint32_t first_id = wide ? UINT32_C(0x10000) : 100;
    uint32_t hashes[24];
    serverAssert(zbtIndexTag(0) == 1 && zbtIndexTag(UINT32_C(0x01000000)) == 1);
    for (unsigned i = 0; i < 24; i++) {
        /* High bytes zero and one share folded tag1, and all homes are bucket3. */
        hashes[i] = (i & 1 ? UINT32_C(0x01000000) : 0) | (i << 2) | 3;
        zbtIndexTableInsertRaw(table, hashes[i], first_id + i);
    }
    for (unsigned i = 0; i < 24; i++) {
        zbtIndexBucket *bucket = NULL; unsigned pos = UINT_MAX;
        serverAssert(zbtIndexHomeMayContain(table, hashes[i]));
        serverAssert(zbtIndexTableFindReference(table, hashes[i], first_id+i, &bucket, &pos));
        serverAssert(bucket == zbtIndexBucketAt(table, (3 + i / 8) & 3) && pos == i % 8);
        reference_checks++;
    }
    zbtIndexBucket *bucket = NULL; unsigned pos = UINT_MAX;
    serverAssert(!zbtIndexTableFindReference(table, hashes[0], first_id + 99, &bucket, &pos));
    /* A distinct tag absent from the summary must be rejected before probing. */
    unsigned absent_tag;
    for (absent_tag = 2; absent_tag < 256; absent_tag++) {
        uint32_t absent = (absent_tag << 24) | 3;
        if (!zbtIndexHomeMayContain(table, absent)) break;
    }
    serverAssert(absent_tag < 256);
    serverAssert(!zbtIndexTableFindReference(table, (absent_tag << 24) | 3,
                                           first_id, &bucket, &pos));
    reference_checks += 2;

    /* Reuse a tombstone without changing filled or breaking later wrapped references. */
    bucket = zbtIndexBucketAt(table, 3);
    zbtIndexSetId(table, bucket, 2, ZBT_INDEX_DELETED_ID); table->used--;
    unsigned long filled = table->filled;
    zbtIndexTableInsertRaw(table, hashes[2], first_id + 50);
    serverAssert(table->filled == filled && table->used == 24);
    serverAssert(zbtIndexGetId(table, bucket, 2) == first_id + 50);
    serverAssert(zbtIndexTableFindReference(table, hashes[23], first_id + 23, &bucket, &pos));
    reference_checks++;

    /* A pure tombstone run exercises first-deleted insertion hints without leaf IDs. */
    for (unsigned i = 0; i < 24; i++)
        zbtIndexSetId(table, zbtIndexBucketAt(table, (3 + i / 8) & 3),
                      i % 8, ZBT_INDEX_DELETED_ID);
    table->used = 0;
    zbtIndexBucket *insert = NULL; unsigned insertion = UINT_MAX;
    unsigned char query[] = {0, 255, 1}; double score = 12345;
    serverAssert(!zbtIndexTableFind(zs, table, hashes[0], query, sizeof(query),
        &score, NULL, NULL, NULL, NULL, &insert, &insertion));
    serverAssert(score == 12345 && insert == zbtIndexBucketAt(table, 3) && insertion == 0);
    table_checks++;
    zbtreeFree(zs);
}

enum { MEMBERS = 600 };
static void key(unsigned i, unsigned char *buf) {
    buf[0] = i >> 8; buf[1] = i; buf[2] = 0; buf[3] = 255;
}
static void check_tables(zbtreeSet *zs) {
    for (unsigned i = 0; i < MEMBERS; i++) {
        unsigned char buf[4]; key(i, buf);
        uint32_t hash = zbtreeMemberHash(buf, sizeof(buf));
        double oldscore = -1, newscore = -1;
        int old = zbtIndexTableFind(zs, &zs->member_index, hash, buf, sizeof(buf),
            &oldscore, NULL, NULL, NULL, NULL, NULL, NULL);
        int added = zs->member_rehash ? zbtIndexTableFind(zs, &zs->member_rehash->table,
            hash, buf, sizeof(buf), &newscore, NULL, NULL, NULL, NULL, NULL, NULL) : 0;
        serverAssert(old + added == 1);
        serverAssert((old ? oldscore : newscore) == i * 0.125);
        table_checks += zs->member_rehash ? 2 : 1;
    }
    serverAssert(zbtTestCheck(zs));
}
static void resizing(unsigned wide) {
    zbtreeSet *zs = zbtreeCreate(); zbtreeReserve(zs, MEMBERS);
    for (unsigned i = 0; i < MEMBERS; i++) {
        unsigned char buf[4]; key(i, buf);
        zbtreeInsertNewRaw(zs, i * 0.125, buf, sizeof(buf), NULL);
    }
    serverAssert(!zs->member_rehash && !zs->member_index.wide_ids);
    /* Match the upstream test's bounded ID-gap setup to request a wide destination. */
    if (wide) zbtTestSkipLeafIds(zs, ZBT_INDEX_WIDE_ID_AT);
    serverAssert(zbtIndexStartResize(zs, MEMBERS * 2, 0));
    serverAssert(zs->member_rehash && zs->member_rehash->table.wide_ids == wide);
    check_tables(zs);
    unsigned steps = 0;
    while (zs->member_rehash) {
        zbtIndexRehashStep(zs, 1); resize_steps++; steps++;
        serverAssert(steps <= 100);
        check_tables(zs);
        if (!zs->member_rehash) completions++;
    }
    serverAssert(zs->member_index.wide_ids == wide);
    /* Queries after the final migration step must use the replacement table. */
    for (unsigned i = 0; i < MEMBERS; i++) {
        unsigned char buf[4]; key(i, buf); double score;
        serverAssert(zbtreeScoreRaw(zs, buf, sizeof(buf), &score) && score == i * 0.125);
        table_checks++;
    }
    zbtreeFree(zs);
}
int main(void) {
    uint8_t seed[16] = {17, 29, 43}; dictSetHashFunctionSeed(seed);
    wrapped(0); wrapped(1); resizing(0); resizing(1);
    serverAssert(completions == 2);
    printf("{\"passed\":true,\"reference_checks\":%lu,\"table_checks\":%lu,"
           "\"resize_steps\":%lu,\"completions\":%lu}\n",
           reference_checks, table_checks, resize_steps, completions);
    return 0;
}
