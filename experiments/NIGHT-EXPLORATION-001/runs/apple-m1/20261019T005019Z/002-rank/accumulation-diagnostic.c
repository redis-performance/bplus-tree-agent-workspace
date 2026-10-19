#define _GNU_SOURCE 1
#define _DARWIN_C_SOURCE 1
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.c"
#include <inttypes.h>
#include <string.h>
#include <time.h>

typedef struct { zbtScoreLeaf *leaf; unsigned int pos; } resolved;
static volatile uint64_t sink;

static uint64_t random64(uint64_t *state) {
    uint64_t z = (*state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
static uint64_t now_ns(void) {
    struct timespec ts;
    serverAssert(clock_gettime(CLOCK_MONOTONIC, &ts) == 0);
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
}
static size_t parse(const char *s) {
    char *end;
    unsigned long long n = strtoull(s, &end, 10);
    serverAssert(*s && !*end && n > 0 && n <= 100000000);
    return (size_t)n;
}

int main(int argc, char **argv) {
    serverAssert(argc == 3);
    size_t n = parse(argv[1]), ops = parse(argv[2]);
    uint64_t rng = 1;
    uint8_t hash_seed[16];
    for (size_t j = 0; j < sizeof(hash_seed); j++) hash_seed[j] = (uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys = zmalloc(n * sizeof(*keys));
    size_t *order = zmalloc(n * sizeof(*order));
    resolved *refs = zmalloc(n * sizeof(*refs));
    unsigned char buf[16];
    for (size_t i = 0; i < n; i++) {
        memset(buf, 'x', sizeof(buf));
        for (unsigned j = 0; j < 8; j++) buf[j] = (unsigned char)((uint64_t)i >> (j*8));
        keys[i] = sdsnewlen(buf, sizeof(buf));
        order[i] = i;
    }
    for (size_t i = n; i > 1; i--) {
        size_t j = random64(&rng) % i, t = order[i-1];
        order[i-1] = order[j]; order[j] = t;
    }
    zbtreeSet *tree = zbtreeCreate();
    for (size_t i = 0; i < n; i++) {
        sds key = keys[order[i]];
        zbtreeInsertPosition p;
        double old;
        serverAssert(!zbtreeFindForAdd(tree, key, &old, &p));
        zbtreeInsertNew(tree, (double)order[i], key, &p);
    }
    uint64_t parents = 0, siblings = 0, max_parents = 0, max_siblings = 0;
    for (size_t i = 0; i < n; i++) {
        zbtreeInsertPosition p;
        double score;
        serverAssert(zbtreeFindForAdd(tree, keys[i], &score, &p));
        serverAssert(score == (double)i);
        refs[i] = (resolved){(zbtScoreLeaf *)p.score_leaf, p.score_pos};
        serverAssert(zbtScoreRank(refs[i].leaf, refs[i].pos) == i);
#ifdef COUNT_MODE
        uint64_t this_parents = 0, this_siblings = 0;
        zbtScoreNode *node = &refs[i].leaf->n;
        while (node->parent) {
            this_parents++;
            this_siblings += node->parent_index;
            node = &node->parent->n;
        }
        parents += this_parents; siblings += this_siblings;
        if (this_parents > max_parents) max_parents = this_parents;
        if (this_siblings > max_siblings) max_siblings = this_siblings;
#endif
    }
#ifdef COUNT_MODE
    printf("size,parents_total,siblings_total,max_parents,max_siblings,mean_parents,mean_siblings,tree_bytes\n");
    printf("%zu,%" PRIu64 ",%" PRIu64 ",%" PRIu64 ",%" PRIu64 ",%.3f,%.3f,%zu\n",
           n, parents, siblings, max_parents, max_siblings,
           (double)parents/n, (double)siblings/n, zbtreeAllocSize(tree));
#else
    uint64_t warm = 0;
    for (size_t i = 0; i < n; i++) {
        resolved r = refs[order[i]];
        warm += zbtScoreRank(r.leaf, r.pos);
    }
    serverAssert(warm == (uint64_t)n*(n-1)/2);
    uint64_t sum = 0, expected = 0, start = now_ns();
    for (size_t i = 0; i < ops; i++) {
        size_t id = order[i % n];
        resolved r = refs[id];
        sum += zbtScoreRank(r.leaf, r.pos);
        expected += id;
    }
    uint64_t elapsed = now_ns() - start;
    serverAssert(sum == expected);
    sink ^= sum;
    printf("size,operations,elapsed_ns,ns_per_op,checksum,tree_bytes\n");
    printf("%zu,%zu,%" PRIu64 ",%.3f,%" PRIu64 ",%zu\n",
           n, ops, elapsed, (double)elapsed/ops, sum, zbtreeAllocSize(tree));
#endif
    zbtreeFree(tree);
    for (size_t i = 0; i < n; i++) sdsfree(keys[i]);
    zfree(keys); zfree(order); zfree(refs);
    return 0;
}
