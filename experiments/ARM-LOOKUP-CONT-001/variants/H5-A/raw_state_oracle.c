/* Correctness only. Compare reader dispatch with the unchanged generic finder. */
#define REDIS_TEST
#include "zset_btree.c"
int __failed_tests, __test_num;
enum { COUNT = 600 };
static unsigned long lookups, active_steps, completions, old_hits, new_hits, free_id_cases;

static void same_state(const zbtreeSet *a, const zbtreeSet *b) {
    serverAssert(a->length == b->length && a->next_score_leaf_id == b->next_score_leaf_id);
    serverAssert(a->member_index.size == b->member_index.size);
    serverAssert(a->member_index.wide_ids == b->member_index.wide_ids);
    serverAssert(a->member_index.used == b->member_index.used);
    serverAssert(a->member_index.filled == b->member_index.filled);
    serverAssert((a->member_rehash != NULL) == (b->member_rehash != NULL));
    if (a->member_rehash) {
        serverAssert(a->member_rehash->next_leaf_id == b->member_rehash->next_leaf_id);
        serverAssert(a->member_rehash->resize_id == b->member_rehash->resize_id);
        serverAssert(a->member_rehash->table.size == b->member_rehash->table.size);
        serverAssert(a->member_rehash->table.wide_ids == b->member_rehash->table.wide_ids);
        serverAssert(a->member_rehash->table.used == b->member_rehash->table.used);
        serverAssert(a->member_rehash->table.filled == b->member_rehash->table.filled);
    }
}
static int deleted(unsigned i) { return i < 120 || i % 11 == 0; }
static void compare(zbtreeSet *raw, zbtreeSet *pre, zbtreeSet *ref,
                    sds key, unsigned id, unsigned scored, int removed) {
    uint32_t hash = zbtreeMemberHash((const unsigned char *)key, sdslen(key));
    int expected = !removed;
    if (ref->member_rehash && expected) {
        int old = zbtIndexTableFind(ref, &ref->member_index, hash,
            (unsigned char *)key, sdslen(key), NULL, NULL, NULL, NULL, NULL, NULL, NULL);
        int fresh = zbtIndexTableFind(ref, &ref->member_rehash->table, hash,
            (unsigned char *)key, sdslen(key), NULL, NULL, NULL, NULL, NULL, NULL, NULL);
        serverAssert(old + fresh == 1); old_hits += old; new_hits += fresh;
    }
    double a = 12345.0, b = 12345.0, c = 12345.0;
    int was_active = ref->member_rehash != NULL;
    int ar = zbtreeScoreRaw(raw, (unsigned char *)key, sdslen(key), scored ? &a : NULL);
    int br = zbtreeScoreRawWithHash(pre, hash, (unsigned char *)key, sdslen(key), scored ? &b : NULL);
    int cr = zbtIndexFind(ref, hash, (unsigned char *)key, sdslen(key),
                          scored ? &c : NULL, NULL, NULL, NULL, NULL);
    serverAssert(ar == expected && br == expected && cr == expected);
    serverAssert(!memcmp(&a, &b, sizeof(a)) && !memcmp(&a, &c, sizeof(a)));
    serverAssert(a == (expected && scored ? id * 0.125 : 12345.0));
    same_state(raw, ref); same_state(pre, ref);
    if (was_active) { active_steps++; if (!ref->member_rehash) completions++; }
    lookups += 3;
}
static void exercise(int wide, int removed) {
    sds keys[COUNT]; zbtreeSet *base = zbtreeCreate(); zbtreeReserve(base, COUNT);
    const size_t lengths[] = {4, 256, 384};
    for (unsigned i = 0; i < COUNT; i++) {
        unsigned char buf[384]; memset(buf, i, sizeof(buf));
        buf[0] = i >> 8; buf[1] = i; buf[2] = 0; buf[3] = 255;
        keys[i] = sdsnewlen(buf, lengths[i % 3]);
        zbtreeInsertNew(base, i * 0.125, keys[i], NULL);
    }
    if (removed) {
        for (unsigned i = 0; i < COUNT; i++) if (deleted(i))
            serverAssert(zbtreeDelete(base, keys[i]));
        if (base->free_score_leaf_id) free_id_cases++;
    }
    while (base->member_rehash) zbtIndexRehashStep(base, 1);
    serverAssert(zbtTestCheck(base));

    /* Stable state: scored/non-scored and hit/miss results match generic behavior. */
    zbtreeSet *raw = zbtreeDup(base), *pre = zbtreeDup(base), *ref = zbtreeDup(base);
    for (unsigned i = 0; i < COUNT; i++)
        compare(raw, pre, ref, keys[i], i, i % 2, removed && deleted(i));
    zbtreeFree(raw); zbtreeFree(pre); zbtreeFree(ref);

    if (wide) zbtTestSkipLeafIds(base, ZBT_INDEX_WIDE_ID_AT);
    serverAssert(zbtIndexStartResize(base, COUNT * 2, 0));
    serverAssert(base->member_rehash && base->member_rehash->table.wide_ids == wide);
    raw = zbtreeDup(base); pre = zbtreeDup(base); ref = zbtreeDup(base);
    /* Alternating low/high live keys exercises migrated/new and not-yet-migrated/old leaves. */
    for (unsigned i = 0; i < COUNT * 2; i++) {
        unsigned at = i < 100 ? (i % 2 ? COUNT - 1 : (removed ? 120 : 0)) : (i * 137) % COUNT;
        compare(raw, pre, ref, keys[at], at, (i / 2) % 2, removed && deleted(at));
    }
    serverAssert(!ref->member_rehash && ref->member_index.wide_ids == wide);
    serverAssert(zbtTestCheck(raw) && zbtTestCheck(pre) && zbtTestCheck(ref));
    /* A missing binary member must leave the optional score untouched. */
    sds missing = sdsnewlen("absent\0binary", 13);
    compare(raw, pre, ref, missing, 0, 1, 1); sdsfree(missing);
    zbtreeFree(raw); zbtreeFree(pre); zbtreeFree(ref); zbtreeFree(base);
    for (unsigned i = 0; i < COUNT; i++) sdsfree(keys[i]);
}
int main(void) {
    uint8_t seed[16] = {17, 29, 43}; dictSetHashFunctionSeed(seed);
    exercise(0, 0); exercise(1, 0); exercise(0, 1); exercise(1, 1);
    serverAssert(completions == 4 && old_hits && new_hits && free_id_cases == 2);
    printf("{\"passed\":true,\"lookups\":%lu,\"active_steps\":%lu,"
           "\"completions\":%lu,\"old_table_hits\":%lu,\"new_table_hits\":%lu,"
           "\"free_id_cases\":%lu}\n", lookups, active_steps, completions,
           old_hits, new_hits, free_id_cases);
    return 0;
}
