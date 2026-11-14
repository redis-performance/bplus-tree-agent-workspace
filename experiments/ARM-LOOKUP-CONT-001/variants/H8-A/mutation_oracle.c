/* Correctness only: independent key/score model through representation churn. */
#define REDIS_TEST
#include "zset_btree.c"
int __failed_tests, __test_num;
enum { N = 600 };
static sds keys[N];
static double scores[N];
static unsigned char live[N];
static unsigned long checks, states, mutations, relocations;

static int order(const void *aa, const void *bb) {
    unsigned a = *(const unsigned *)aa, b = *(const unsigned *)bb;
    if (scores[a] < scores[b]) return -1;
    if (scores[a] > scores[b]) return 1;
    size_t alen = sdslen(keys[a]), blen = sdslen(keys[b]);
    int cmp = memcmp(keys[a], keys[b], alen < blen ? alen : blen);
    return cmp ? cmp : (alen > blen) - (alen < blen);
}
static void validate(zbtreeSet *t) {
    unsigned sorted[N], count = 0;
    for (unsigned i = 0; i < N; i++) {
        double score = 123456;
        int found = zbtreeScoreRaw(t, (unsigned char *)keys[i], sdslen(keys[i]), &score);
        serverAssert(found == live[i]);
        if (live[i]) {
            serverAssert(!memcmp(&score, &scores[i], sizeof(score)));
            sorted[count++] = i;
        } else serverAssert(score == 123456);
        checks++;
    }
    serverAssert(zbtreeLength(t) == count);
    qsort(sorted, count, sizeof(sorted[0]), order);
    for (int reverse = 0; reverse < 2; reverse++) {
        zbtreeIterator it;
        serverAssert(zbtreeIteratorStart(t, reverse, &it) == (count != 0));
        for (unsigned j = 0; j < count; j++) {
            unsigned id = sorted[reverse ? count - 1 - j : j];
            const unsigned char *ptr; size_t len; double score;
            serverAssert(zbtreeIteratorNext(&it, reverse, &ptr, &len, &score));
            serverAssert(len == sdslen(keys[id]) && !memcmp(ptr, keys[id], len));
            serverAssert(!memcmp(&score, &scores[id], sizeof(score)));
            score = 123456;
            serverAssert(zbtreeRank(t, keys[id], reverse, &score) == (long)j);
            serverAssert(!memcmp(&score, &scores[id], sizeof(score)));
            checks += 2;
        }
        serverAssert(!zbtreeIteratorNext(&it, reverse, NULL, NULL, NULL));
    }
    serverAssert(zbtTestCheck(t)); states++;
}
static void *copy_alloc(void *ptr) {
    size_t len = zmalloc_usable_size(ptr);
    void *copy = zmalloc(len + 16); memcpy(copy, ptr, len); relocations++;
    return copy;
}
static void *move_plain(void *ptr) { void *copy = copy_alloc(ptr); zfree(ptr); return copy; }
static void release(void *ptr) { zfree(ptr); }
static zbtreeSet *relocate(zbtreeSet *t) {
    t = zbtreeDefragStart(t, move_plain);
    zbtreeDefragState state; zbtreeDefragStateReset(&state);
    unsigned long scanned;
    while (!zbtreeDefragStep(t, &state, copy_alloc, release, &scanned)) validate(t);
    validate(t); return t;
}
int main(void) {
    uint8_t seed[16] = {17, 29, 43}; dictSetHashFunctionSeed(seed);
    for (unsigned i = 0; i < N; i++) {
        unsigned char bytes[384];
        size_t len = i <= 320 ? i : 384;
        for (size_t j = 0; j < len; j++) bytes[j] = j % 7 ? (unsigned char)(i * 13 + j * 37) : 0;
        if (len) bytes[0] = i;
        if (len > 1) bytes[1] = i >> 8;
        keys[i] = sdsnewlen(bytes, len); scores[i] = i ? i * 0.125 : -0.0;
    }
    zbtreeSet *t = zbtreeCreate(); validate(t);
    for (unsigned j = 0; j < N; j++) {
        unsigned i = j & 1 ? N - 1 - j / 2 : j / 2;
        zbtreeInsertNew(t, scores[i], keys[i], NULL); live[i] = 1;
        mutations++; validate(t);
    }
    for (unsigned i = 1; i < N; i += 4) {
        zbtreeInsertPosition pos; double old;
        serverAssert(zbtreeFindForAdd(t, keys[i], &old, &pos));
        serverAssert(!memcmp(&old, &scores[i], sizeof(old)));
        scores[i] = N - i + 0.25;
        zbtreeUpdateScore(t, keys[i], scores[i], &pos); mutations++; validate(t);
    }
    zbtreeSet *copy = zbtreeDup(t); validate(copy); copy = relocate(copy); zbtreeFree(copy);
    t = relocate(t);
    for (unsigned i = 0; i < N; i += 3) {
        serverAssert(zbtreeDelete(t, keys[i])); live[i] = 0; mutations++; validate(t);
    }
    for (unsigned i = 0; i < N; i += 3) {
        scores[i] = -(double)i - 1;
        zbtreeInsertNew(t, scores[i], keys[i], NULL); live[i] = 1; mutations++; validate(t);
    }
    zbtreeShrinkToFit(t); validate(t);
    while (zbtreeLength(t)) {
        unsigned sorted[N], count = 0;
        for (unsigned i = 0; i < N; i++) if (live[i]) sorted[count++] = i;
        qsort(sorted, count, sizeof(sorted[0]), order);
        int reverse = count & 1;
        unsigned id = sorted[reverse ? count - 1 : 0];
        zbtreeDeleteEdge(t, reverse); live[id] = 0; mutations++; validate(t);
    }
    zbtreeFree(t);
    for (unsigned i = 0; i < N; i++) sdsfree(keys[i]);
    printf("{\"passed\":true,\"model_checks\":%lu,\"states\":%lu,"
           "\"mutations\":%lu,\"relocations\":%lu}\n", checks, states, mutations, relocations);
    return 0;
}
