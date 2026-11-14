/* Correctness-only differential oracle against baseline e13d9fc88. */
#include "zset_btree.c"
int __failed_tests;
int __test_num;
static int reference_find(zbtreeSet *zs, zbtIndexTable *table,
                             uint32_t hash, const unsigned char *ele,
                             size_t elelen, double *score,
                             zbtScoreLeaf **score_leaf,
                             unsigned int *score_pos,
                             zbtIndexBucket **found_bucket,
                             unsigned int *found_pos,
                             zbtIndexBucket **insert_bucket,
                             unsigned int *insert_pos)
{
    if (table->size == 0) return 0;
    uint8_t tag = zbtIndexTag(hash);
    unsigned long mask = table->size - 1;
    unsigned long index = hash & mask;
    zbtIndexBucket *first_deleted = NULL;
    unsigned int first_deleted_pos = 0;

    for (unsigned long probes = 0; probes < table->size; probes++) {
        zbtIndexBucket *bucket = zbtIndexBucketAt(table, index);
        uint64_t matches = zbtIndexTagMask(zbtIndexTags(bucket), tag);
        while (matches) {
            unsigned int pos = zbtIndexFirstTag(matches);
            if ((uint8_t)(zbtIndexTags(bucket) >> (pos * 8)) != tag) {
                matches &= matches - 1;
                continue;
            }
            uint32_t id = zbtIndexGetId(table, bucket, pos);
            if (id != ZBT_INDEX_DELETED_ID)
            {
                zbtScoreLeaf *leaf = id < zs->next_score_leaf_id ?
                    zs->score_leaf_by_id[id] : NULL;
                if (leaf == NULL || ZBT_IS_FREE_LEAF_ID(leaf)) {
                    serverAssert(zs->member_rehash &&
                                 table == &zs->member_index);
                    matches &= matches - 1;
                    continue;
                }
                serverAssert(leaf->id == id);
                if (zs->member_rehash) {
                    int in_new = table == &zs->member_rehash->table;
                    int migrated = leaf->n.index_resize ==
                                   zs->member_rehash->resize_id;
                    if (in_new != migrated) {
                        matches &= matches - 1;
                        continue;
                    }
                }
                if (zbtScoreLeafFindMember(leaf, hash, ele, elelen, score,
                                           score_pos))
                {
                    if (score_leaf) *score_leaf = leaf;
                    if (found_bucket) *found_bucket = bucket;
                    if (found_pos) *found_pos = pos;
                    return 1;
                }
            }
            matches &= matches - 1;
        }

        /* Hits in the home bucket need no missing-member filter. Check it
         * only after those candidates, before following the probe run. */
        if (probes == 0 && !zbtIndexHomeMayContain(table, hash)) return 0;

        /* Save the first tombstone for a possible insertion. An unused slot,
         * unlike a tombstone, proves that the member is not farther ahead. */
        for (unsigned int pos = 0; pos < ZBT_INDEX_BUCKET_ITEMS; pos++) {
            uint8_t oldtag = zbtIndexTags(bucket) >> (pos * 8);
            if (oldtag == 0) {
                if (insert_bucket) {
                    *insert_bucket = first_deleted ? first_deleted : bucket;
                    *insert_pos = first_deleted ? first_deleted_pos : pos;
                }
                return 0;
            }
            if (first_deleted == NULL &&
                zbtIndexGetId(table, bucket, pos) == ZBT_INDEX_DELETED_ID)
            {
                first_deleted = bucket;
                first_deleted_pos = pos;
            }
        }
        index = (index + 1) & mask;
    }

    if (insert_bucket && first_deleted) {
        *insert_bucket = first_deleted;
        *insert_pos = first_deleted_pos;
    }
    return 0;
}

static unsigned long comparisons, resize_steps, resize_completions;
typedef struct {
    double score;
    zbtScoreLeaf *leaf;
    unsigned int score_pos;
    zbtIndexBucket *found, *insert;
    unsigned int found_pos, insert_pos;
} Result;

static int compare(zbtreeSet *zs, zbtIndexTable *t, uint32_t hash,
                    const unsigned char *key, size_t len) {
    int last = 0;
    for (unsigned int mask = 0; mask < 32; mask++) {
        Result a = {.score = -987.0, .score_pos = UINT_MAX,
                    .found_pos = UINT_MAX, .insert_pos = UINT_MAX};
        Result b = a;
        int x = reference_find(zs, t, hash, key, len,
            mask & 1 ? &a.score : NULL, mask & 2 ? &a.leaf : NULL,
            mask & 4 ? &a.score_pos : NULL, mask & 8 ? &a.found : NULL,
            mask & 8 ? &a.found_pos : NULL, mask & 16 ? &a.insert : NULL,
            mask & 16 ? &a.insert_pos : NULL);
        int y = zbtIndexTableFind(zs, t, hash, key, len,
            mask & 1 ? &b.score : NULL, mask & 2 ? &b.leaf : NULL,
            mask & 4 ? &b.score_pos : NULL, mask & 8 ? &b.found : NULL,
            mask & 8 ? &b.found_pos : NULL, mask & 16 ? &b.insert : NULL,
            mask & 16 ? &b.insert_pos : NULL);
        serverAssert(x == y && memcmp(&a.score, &b.score, sizeof(double)) == 0);
        serverAssert(a.leaf == b.leaf && a.score_pos == b.score_pos);
        serverAssert(a.found == b.found && a.found_pos == b.found_pos);
        serverAssert(a.insert == b.insert && a.insert_pos == b.insert_pos);
        comparisons++;
        last = y;
    }
    return last;
}

static void synthetic(void) {
    const unsigned int counts[] = {0,1,7,8,9,17,24,32};
    for (unsigned int wide = 0; wide < 2; wide++) {
        for (unsigned int high = 0; high < 2; high++) {
            uint32_t hash = (high ? UINT32_C(0xff000000) : 0) | 3;
            uint32_t first = wide ? 70000 : 1;
            zbtreeSet zs = {0};
            zs.next_score_leaf_id = first + 32;
            zs.score_leaf_by_id = calloc(zs.next_score_leaf_id, sizeof(void *));
            zbtIndexTable *t = &zs.member_index;
            t->size = 4;
            t->wide_ids = wide;
            t->buckets = calloc(t->size, zbtIndexBucketBytes(t));
            for (unsigned int i = 0; i < 32; i++) {
                zbtScoreLeaf *leaf = calloc(1, 256);
                leaf->n.isleaf = 1;
                leaf->n.count = 1;
                leaf->n.subtree = 1;
                leaf->score_base = zbtScoreToOrdered((double)i);
                leaf->id = first + i;
                uint32_t value = i + 42;
                zbtScoreLeafOffsets(leaf)[0] = 128;
                zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
                zbtPackedWriteInline((unsigned char *)leaf + 128,
                                      (unsigned char *)&value, sizeof(value));
                zs.score_leaf_by_id[leaf->id] = leaf;
            }
            for (unsigned int c = 0; c < sizeof(counts)/sizeof(*counts); c++) {
                unsigned int n = counts[c];
                memset(t->buckets, 0, zbtIndexTableBytes(t));
                t->used = t->filled = 0;
                for (unsigned int i = 0; i < n; i++)
                    zbtIndexTableInsertRaw(t, hash, first + i);
                for (unsigned int i = 0; i <= 32; i++) {
                    uint32_t value = i + 42;
                    serverAssert(compare(&zs, t, hash, (unsigned char *)&value,
                                         sizeof(value)) == (i < n));
                }
                /* A failed filter must not suppress a home hit, but retains
                 * the baseline's rejection of candidates farther in the run. */
                uint64_t saved = *zbtIndexHomeTagsAt(t, 3);
                *zbtIndexHomeTagsAt(t, 3) = 0;
                for (unsigned int i = 0; i < 32; i++) {
                    uint32_t value = i + 42;
                    serverAssert(compare(&zs, t, hash, (unsigned char *)&value,
                                         sizeof(value)) == (i < n && i < 8));
                }
                *zbtIndexHomeTagsAt(t, 3) = saved;
                if (n >= 3) {
                    zbtIndexBucket *home = zbtIndexBucketAt(t, 3);
                    zbtIndexSetId(t, home, 2, ZBT_INDEX_DELETED_ID);
                    if (n >= 10)
                        zbtIndexSetId(t, zbtIndexBucketAt(t, 0), 1,
                                      ZBT_INDEX_DELETED_ID);
                    uint32_t missing = 9999;
                    serverAssert(!compare(&zs, t, hash, (unsigned char *)&missing,
                                          sizeof(missing)));
                    zbtIndexBucket *insert = NULL;
                    unsigned int pos = UINT_MAX;
                    serverAssert(!zbtIndexTableFind(&zs, t, hash,
                        (unsigned char *)&missing, sizeof(missing), NULL,
                        NULL, NULL, NULL, NULL, &insert, &pos));
                    serverAssert(insert == home && pos == 2);
                    for (unsigned int i = 0; i < n; i++) {
                        uint32_t value = i + 42;
                        compare(&zs, t, hash, (unsigned char *)&value, sizeof(value));
                    }
                }
                /* Saturated filter false positives still require exact bytes. */
                *zbtIndexHomeTagsAt(t, 3) = UINT64_MAX;
                uint32_t absent = 9999;
                compare(&zs, t, hash ^ UINT32_C(0x01000000),
                        (unsigned char *)&absent, sizeof(absent));
            }
            t->size = 0;
            uint32_t absent = 9999;
            compare(&zs, t, hash, (unsigned char *)&absent, sizeof(absent));
            for (unsigned int i = 0; i < 32; i++) free(zs.score_leaf_by_id[first + i]);
            free(zs.score_leaf_by_id);
            free(t->buckets);
        }
    }
}

static void real_resize(void) {
    uint8_t seed[16] = {17,29,43};
    dictSetHashFunctionSeed(seed);
    zbtreeSet *zs = zbtreeCreate();
    zbtreeReserve(zs, 400);
    char keys[200][16];
    for (unsigned int i = 0; i < 200; i++) {
        snprintf(keys[i], sizeof(keys[i]), "member:%03u", i);
        zbtreeInsertNewRaw(zs, (double)i, (unsigned char *)keys[i],
                           strlen(keys[i]), NULL);
    }
    serverAssert(zbtIndexStartResize(zs, 800, 1));
    int saw_both = 0;
    while (zs->member_rehash) {
        unsigned int old_hits = 0, new_hits = 0;
        for (unsigned int i = 0; i < 200; i++) {
            size_t len = strlen(keys[i]);
            uint32_t hash = zbtreeMemberHash((unsigned char *)keys[i], len);
            int old = compare(zs, &zs->member_index, hash,
                              (unsigned char *)keys[i], len);
            int fresh = compare(zs, &zs->member_rehash->table, hash,
                                (unsigned char *)keys[i], len);
            serverAssert(old + fresh == 1);
            old_hits += old;
            new_hits += fresh;
        }
        saw_both |= old_hits && new_hits;
        if (zs->member_rehash->table.used == zs->length) {
            double score = -1;
            serverAssert(zbtreeScoreRaw(zs, (unsigned char *)keys[0],
                                       strlen(keys[0]), &score));
            serverAssert(score == 0 && zs->member_rehash == NULL);
            resize_completions++;
        } else {
            zbtIndexRehashStep(zs, 1);
            resize_steps++;
        }
    }
    serverAssert(saw_both && zbtTestCheck(zs));
    for (unsigned int i = 0; i < 200; i++) {
        size_t len = strlen(keys[i]);
        uint32_t hash = zbtreeMemberHash((unsigned char *)keys[i], len);
        serverAssert(compare(zs, &zs->member_index, hash,
                             (unsigned char *)keys[i], len));
    }
    zbtreeFree(zs);
}

int main(void) {
    synthetic();
    real_resize();
    printf("{\"passed\":true,\"comparisons\":%lu,\"resize_steps\":%lu,"
           "\"resize_completions\":%lu,\"wide_ids\":true,\"wrapped_probe\":true}\n",
           comparisons, resize_steps, resize_completions);
    return 0;
}

