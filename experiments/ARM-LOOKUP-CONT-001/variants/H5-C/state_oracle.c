/* Correctness-only paired-state oracle against baseline e13d9fc88. */
#include "zset_btree.c"
int __failed_tests;
int __test_num;
static int reference_find(zbtreeSet *zs, uint32_t hash,
                        const unsigned char *ele, size_t elelen,
                        double *score,
                        zbtScoreLeaf **found_score_leaf,
                        unsigned int *found_score_position,
                        zbtIndexBucket **found_bucket,
                        unsigned int *found_bucket_position)
{
    zbtIndexBucket *bucket = NULL, *hint_bucket = NULL;
    unsigned int pos = 0, hint_pos = 0;
    if (zs->member_rehash) zbtIndexRehashStep(zs, 1);

    if (zs->member_rehash &&
        zbtIndexTableFind(zs, &zs->member_rehash->table, hash, ele, elelen,
                          score,
                          found_score_leaf, found_score_position,
                          found_bucket ? &bucket : NULL,
                          found_bucket_position ? &pos : NULL,
                          found_bucket ? &hint_bucket : NULL,
                          found_bucket ? &hint_pos : NULL))
        goto found;

    /* During a resize new entries go to the new table, so an insertion slot
     * found in the old table would not be useful to the caller. */
    if (zbtIndexTableFind(zs, &zs->member_index, hash, ele, elelen, score,
                          found_score_leaf, found_score_position,
                          found_bucket ? &bucket : NULL,
                          found_bucket_position ? &pos : NULL,
                          zs->member_rehash || !found_bucket ? NULL : &hint_bucket,
                          zs->member_rehash || !found_bucket ? NULL : &hint_pos))
        goto found;

    if (found_bucket) *found_bucket = hint_bucket;
    if (found_bucket_position) *found_bucket_position = hint_pos;
    return 0;

found:
    if (found_bucket) *found_bucket = bucket;
    if (found_bucket_position) *found_bucket_position = pos;
    return 1;
}

static unsigned long comparisons, raw_pairs, completed_pairs, phases;
typedef struct {
    double score;
    zbtScoreLeaf *leaf;
    unsigned int score_pos;
    zbtIndexBucket *bucket;
    unsigned int bucket_pos;
} Result;

static unsigned long bucket_key(zbtreeSet *zs, zbtIndexBucket *bucket) {
    if (bucket == NULL) return ULONG_MAX;
    if (zbtIndexOwnsBucket(&zs->member_index, bucket))
        return ((uintptr_t)bucket - (uintptr_t)zs->member_index.buckets) /
               zbtIndexBucketBytes(&zs->member_index);
    serverAssert(zs->member_rehash &&
                  zbtIndexOwnsBucket(&zs->member_rehash->table, bucket));
    return (1UL << (sizeof(unsigned long) * CHAR_BIT - 1)) |
        (((uintptr_t)bucket - (uintptr_t)zs->member_rehash->table.buckets) /
         zbtIndexBucketBytes(&zs->member_rehash->table));
}

static void same_state(zbtreeSet *a, zbtreeSet *b, int was_resizing) {
    serverAssert(!!a->member_rehash == !!b->member_rehash);
    serverAssert(a->member_index.size == b->member_index.size);
    serverAssert(a->member_index.used == b->member_index.used);
    serverAssert(a->member_index.filled == b->member_index.filled);
    if (a->member_rehash) {
        serverAssert(a->member_rehash->next_leaf_id == b->member_rehash->next_leaf_id);
        serverAssert(a->member_rehash->table.used == b->member_rehash->table.used);
        serverAssert(a->member_rehash->resize_id == b->member_rehash->resize_id);
    } else if (was_resizing) completed_pairs++;
    serverAssert(zbtTestCheck(a) && zbtTestCheck(b));
}

static void compare(zbtreeSet *source, const unsigned char *key, size_t len) {
    uint32_t hash = zbtreeMemberHash(key, len);
    for (unsigned int mask = 0; mask < 32; mask++) {
        zbtreeSet *a = zbtreeDup(source), *b = zbtreeDup(source);
        Result x = {.score = -987, .score_pos = UINT_MAX, .bucket_pos = UINT_MAX};
        Result y = x;
        int old = reference_find(a, hash, key, len,
            mask & 1 ? &x.score : NULL, mask & 2 ? &x.leaf : NULL,
            mask & 4 ? &x.score_pos : NULL, mask & 8 ? &x.bucket : NULL,
            mask & 16 ? &x.bucket_pos : NULL);
        int fresh = zbtIndexFind(b, hash, key, len,
            mask & 1 ? &y.score : NULL, mask & 2 ? &y.leaf : NULL,
            mask & 4 ? &y.score_pos : NULL, mask & 8 ? &y.bucket : NULL,
            mask & 16 ? &y.bucket_pos : NULL);
        serverAssert(old == fresh && memcmp(&x.score, &y.score, sizeof(double)) == 0);
        serverAssert((x.leaf ? x.leaf->id : UINT32_MAX) ==
                     (y.leaf ? y.leaf->id : UINT32_MAX));
        serverAssert(x.score_pos == y.score_pos && x.bucket_pos == y.bucket_pos);
        serverAssert(bucket_key(a, x.bucket) == bucket_key(b, y.bucket));
        same_state(a, b, source->member_rehash != NULL);
        comparisons++;
        zbtreeFree(a);
        zbtreeFree(b);
    }
    for (unsigned int score_requested = 0; score_requested < 2; score_requested++) {
        zbtreeSet *a = zbtreeDup(source), *b = zbtreeDup(source);
        double x = -987, y = -987;
        int old = zbtreeScoreRaw(a, key, len, score_requested ? &x : NULL);
        int fresh = zbtreeScoreRawWithHash(b, hash, key, len,
                                          score_requested ? &y : NULL);
        serverAssert(old == fresh && memcmp(&x, &y, sizeof(x)) == 0);
        same_state(a, b, source->member_rehash != NULL);
        raw_pairs++;
        zbtreeFree(a);
        zbtreeFree(b);
    }
}

static void phase(zbtreeSet *zs) {
    size_t len;
    const unsigned char *key = zbtScoreLeafElement(zs->score_first, 0, &len);
    compare(zs, key, len);
    key = zbtScoreLeafElement(zs->score_last, zs->score_last->n.count - 1, &len);
    compare(zs, key, len);
    static const unsigned char absent[] = "definitely-absent";
    compare(zs, absent, sizeof(absent) - 1);
    phases++;
}

/* Real hashes with the same folded tag and home bucket. Separate score
 * extremes put the members in different leaves, forcing candidate rejection. */
static void add_collision_pair(zbtreeSet *zs) {
    unsigned long size = zs->member_index.size;
    unsigned int *seen = calloc(size * 256, sizeof(*seen));
    int found = 0;
    for (unsigned int i = 0; i < 16384 && !found; i++) {
        char key[32];
        int len = snprintf(key, sizeof(key), "collision:%u", i);
        uint32_t hash = zbtreeMemberHash((unsigned char *)key, len);
        unsigned long bin = (hash & (size - 1)) * 256 + zbtIndexTag(hash);
        if (seen[bin]) {
            char first[32];
            int firstlen = snprintf(first, sizeof(first), "collision:%u", seen[bin] - 1);
            zbtreeInsertNewRaw(zs, -1, (unsigned char *)first, firstlen, NULL);
            zbtreeInsertNewRaw(zs, 1000, (unsigned char *)key, len, NULL);
            serverAssert(zs->member_index.size == size && !zs->member_rehash);
            found = 1;
        } else seen[bin] = i + 1;
    }
    free(seen);
    serverAssert(found);
}

int main(void) {
    uint8_t seed[16] = {17,29,43};
    dictSetHashFunctionSeed(seed);
    unsigned int tombstone_states = 0, free_id_states = 0;
    for (unsigned int wide = 0; wide < 2; wide++) {
        zbtreeSet *zs = zbtreeCreate();
        if (wide) zbtTestSkipLeafIds(zs, 70000);
        zbtreeReserve(zs, 400);
        char keys[200][16];
        for (unsigned int i = 0; i < 200; i++) {
            snprintf(keys[i], sizeof(keys[i]), "member:%03u", i);
            zbtreeInsertNewRaw(zs, (double)i, (unsigned char *)keys[i],
                               strlen(keys[i]), NULL);
        }
        serverAssert(!zs->member_rehash && zs->member_index.wide_ids == (int)wide);
        add_collision_pair(zs);
        phase(zs);
        sds removed = sdsnew(keys[100]);
        serverAssert(zbtreeDelete(zs, removed));
        sdsfree(removed);
        serverAssert(!zs->member_rehash && zs->member_index.filled > zs->member_index.used);
        tombstone_states++;
        phase(zs);
        compare(zs, (unsigned char *)keys[100], strlen(keys[100]));

        serverAssert(zbtIndexStartResize(zs, 800, 1));
        phase(zs); /* Entry active: each copied pair must advance exactly once. */
        zbtIndexRehashStep(zs, 1);
        serverAssert(zs->member_rehash && zs->member_rehash->table.used > 0 &&
                      zs->member_rehash->table.used < zs->length);
        phase(zs); /* Both migrated and unmigrated leaves are present. */
        while (zs->member_rehash->table.used < zs->length)
            zbtIndexRehashStep(zs, 1);
        phase(zs); /* The next lookup frees the old resize context. */
        zbtIndexRehashStep(zs, 1);
        serverAssert(!zs->member_rehash);
        phase(zs);

        uint32_t released = zs->score_first->id;
        while (zs->score_first && zs->score_first->id == released)
            zbtreeDeleteEdge(zs, 0);
        serverAssert(zs->score_leaf_by_id[released] == NULL ||
                      ZBT_IS_FREE_LEAF_ID(zs->score_leaf_by_id[released]));
        free_id_states++;
        while (zs->member_rehash) zbtIndexRehashStep(zs, 1);
        phase(zs);
        zbtreeFree(zs);
    }
    serverAssert(completed_pairs > 0);
    printf("{\"passed\":true,\"comparisons\":%lu,\"raw_prehashed_pairs\":%lu,"
           "\"completed_resize_pairs\":%lu,\"phases\":%lu,"
           "\"tombstone_states\":%u,\"free_id_states\":%u,\"real_collision_pairs\":2}\n",
           comparisons, raw_pairs, completed_pairs, phases,
           tombstone_states, free_id_states);
    return 0;
}

