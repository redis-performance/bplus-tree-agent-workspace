/* Exact score-bound semantics and copied-member ownership, standalone API. */
#include "server.h"
#include "zset_btree.h"
#include <float.h>
#include <inttypes.h>
#include <math.h>
#include <string.h>

#define N 129
typedef struct { sds key; double score; int live; } entry;
static entry model[N];
static double bounds[13];
static unsigned checks;
static uint64_t bits(double x) { uint64_t u; memcpy(&u, &x, sizeof(u)); return u; }
static int compare(const void *a, const void *b) {
    const entry *x = *(entry *const *)a, *y = *(entry *const *)b;
    if (x->score < y->score) return -1;
    if (x->score > y->score) return 1;
    size_t nx = sdslen(x->key), ny = sdslen(y->key);
    int c = memcmp(x->key, y->key, nx < ny ? nx : ny);
    return c ? c : (nx > ny) - (nx < ny);
}
static size_t sorted(entry **order) {
    size_t n = 0;
    for (unsigned i = 0; i < N; i++) if (model[i].live) order[n++] = &model[i];
    qsort(order, n, sizeof(*order), compare);
    return n;
}
static void next_matches(zbtreeIterator *it, int reverse, entry *expected) {
    const unsigned char *key;
    size_t len;
    double value;
    serverAssert(zbtreeIteratorNext(it, reverse, &key, &len, &value));
    serverAssert(len == sdslen(expected->key) && !memcmp(key, expected->key, len));
    serverAssert(bits(value) == bits(expected->score));
}
static void verify(zbtreeSet *tree) {
    entry *order[N];
    size_t n = sorted(order);
    serverAssert(zbtreeLength(tree) == n);
    for (unsigned i = 0; i < N; i++) {
        double value;
        serverAssert(zbtreeScore(tree, model[i].key, &value) == model[i].live);
        if (model[i].live) serverAssert(bits(value) == bits(model[i].score));
    }
    for (int reverse = 0; reverse < 2; reverse++) {
        zbtreeIterator it;
        serverAssert(zbtreeIteratorStart(tree, reverse, &it) == (n != 0));
        for (size_t i = 0; i < n; i++) next_matches(&it, reverse, order[reverse ? n-i-1 : i]);
        serverAssert(!zbtreeIteratorNext(&it, reverse, NULL, NULL, NULL));
    }
    for (unsigned b = 0; b < 13; b++) for (int exclusive = 0; exclusive < 2; exclusive++) {
        for (int reverse = 0; reverse < 2; reverse++) {
            size_t expected = n;
            for (size_t i = 0; i < n; i++) {
                size_t k = reverse ? n-i-1 : i;
                double s = order[k]->score;
                int match = reverse ? (exclusive ? s < bounds[b] : s <= bounds[b]) :
                                      (exclusive ? s > bounds[b] : s >= bounds[b]);
                if (match) { expected = k; break; }
            }
            zbtreeIterator it;
            unsigned long rank = ULONG_MAX;
            serverAssert(zbtreeIteratorSeekScore(tree, bounds[b], exclusive, reverse, &it, &rank) == (expected != n));
            if (expected != n) {
                serverAssert(rank == expected);
                next_matches(&it, reverse, order[expected]);
            } else {
                serverAssert(!zbtreeIteratorNext(&it, reverse, NULL, NULL, NULL));
            }
        }
    }
    checks++;
}
static int in_range(double score, double low, int lowex, double high, int highex) {
    return (lowex ? score > low : score >= low) && (highex ? score < high : score <= high);
}
static void exercise(int reverse_insert) {
    const size_t lengths[] = {1, 7, 8, 16, 319, 320, 321};
    uint8_t seed[16] = {17, 31, 41, 59};
    dictSetHashFunctionSeed(seed);
    for (unsigned i = 0; i < N; i++) {
        size_t len = i ? lengths[i % 7] : 0;
        unsigned char buf[321];
        memset(buf, 0, sizeof(buf));
        buf[0] = (unsigned char)i;
        for (size_t j = 2; j < len; j++) buf[j] = (unsigned char)(j + i);
        model[i] = (entry){sdsnewlen(buf, len), bounds[i % 13], 1};
    }
    zbtreeSet *tree = zbtreeCreate();
    for (unsigned j = 0; j < N; j++) {
        unsigned i = reverse_insert ? N-j-1 : j;
        sds temporary = sdsnewlen(model[i].key, sdslen(model[i].key));
        zbtreeInsertPosition pos;
        double old;
        serverAssert(!zbtreeFindForAdd(tree, temporary, &old, &pos));
        zbtreeInsertNew(tree, model[i].score, temporary, &pos);
        /* A borrowed pointer would now corrupt tree-owned binary members. */
        memset(temporary, 0xa5, sdslen(temporary));
        sdsfree(temporary);
    }
    verify(tree);
    for (unsigned lo = 0; lo < 13; lo++) for (unsigned hi = 0; hi < 13; hi++) {
        for (int lowex = 0; lowex < 2; lowex++) for (int highex = 0; highex < 2; highex++) {
            unsigned long expected = 0;
            for (unsigned i = 0; i < N; i++)
                expected += in_range(model[i].score, bounds[lo], lowex, bounds[hi], highex);
            serverAssert(zbtreeCountByScore(tree, bounds[lo], lowex, bounds[hi], highex) == expected);
            zbtreeSet *copy = zbtreeDup(tree);
            serverAssert(zbtreeDeleteRangeByScore(copy, bounds[lo], lowex, bounds[hi], highex) == expected);
            for (unsigned i = 0; i < N; i++)
                model[i].live = !in_range(model[i].score, bounds[lo], lowex, bounds[hi], highex);
            verify(copy);
            zbtreeFree(copy);
            for (unsigned i = 0; i < N; i++) model[i].live = 1;
            verify(tree); /* clone modifications must not affect the original */
        }
    }
    zbtreeFree(tree);
    for (unsigned i = 0; i < N; i++) sdsfree(model[i].key);
    printf("insertion_direction=%d PASS cumulative_checks=%u\n", reverse_insert, checks);
}
int main(void) {
    double values[] = {-DBL_MAX, -DBL_MIN, -DBL_TRUE_MIN, -0.0, 0.0,
        DBL_TRUE_MIN, DBL_MIN, 0.5, nextafter(1.0, 0.0), 1.0,
        nextafter(1.0, 2.0), 2.0, DBL_MAX};
    memcpy(bounds, values, sizeof(bounds));
    exercise(0);
    exercise(1);
    printf("PASS: 1352 range deletions on clones; %u full bound/ownership checks\n", checks);
    return 0;
}
