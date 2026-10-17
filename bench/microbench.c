#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <inttypes.h>
#include <string.h>
#include <time.h>
#include <errno.h>

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
static size_t number(const char *s) {
    char *end;
    errno = 0;
    unsigned long long v = strtoull(s, &end, 10);
    if (errno || s[0] == '-' || *end || !*s || !v || v > 100000000) {
        fprintf(stderr, "Expected integer in [1, 100000000]: %s\n", s);
        exit(2);
    }
    return (size_t)v;
}
static void insert(zbtreeSet *tree, sds key, double score) {
    zbtreeInsertPosition pos;
    double old;
    serverAssert(!zbtreeFindForAdd(tree, key, &old, &pos));
    zbtreeInsertNew(tree, score, key, &pos);
}
static void scan_count(void *ctx, const unsigned char *key, size_t len, double score) {
    UNUSED(key); UNUSED(len); UNUSED(score);
    (*(uint64_t *)ctx)++;
}
typedef struct { unsigned char *seen; size_t n; } scan_check;
static void scan_verify(void *ctx, const unsigned char *key, size_t len, double score) {
    scan_check *check = ctx;
    serverAssert(len >= 8);
    uint64_t id = 0;
    for (unsigned j = 0; j < 8; j++) id |= (uint64_t)key[j] << (j * 8);
    serverAssert(id < check->n && score == (double)id);
    check->seen[id] = 1;
}
int main(int argc, char **argv) {
    size_t n = 100000, ops = 1000000, bytes = 16;
    uint64_t seed = 1;
    const char *selected = "all";
    const char *cases[] = {"insert", "lookup-hit", "lookup-miss", "rank", "iterate", "scan", "update", "delete"};
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--help")) {
            puts("btree-bench [--size N] [--ops N] [--member-bytes N>=8] [--seed N] [--case all|insert|lookup-hit|lookup-miss|rank|iterate|scan|update|delete]");
            return 0;
        }
        if (i + 1 == argc) { fprintf(stderr, "Missing value: %s\n", argv[i]); return 2; }
        const char *arg = argv[i++], *value = argv[i];
        if (!strcmp(arg, "--size")) n = number(value);
        else if (!strcmp(arg, "--ops")) ops = number(value);
        else if (!strcmp(arg, "--member-bytes")) bytes = number(value);
        else if (!strcmp(arg, "--seed")) seed = number(value);
        else if (!strcmp(arg, "--case")) selected = value;
        else { fprintf(stderr, "Unknown option: %s\n", arg); return 2; }
    }
    int valid_case = !strcmp(selected, "all");
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) valid_case |= !strcmp(selected, cases[c]);
    if (!valid_case || bytes < 8 || bytes > 65536) { fputs("Invalid case or member size (8..65536)\n", stderr); return 2; }
    uint64_t rng = seed;
    uint8_t hash_seed[16];
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys = zmalloc(2 * n * sizeof(*keys));
    size_t *order = zmalloc(n * sizeof(*order));
    char *buf = zmalloc(bytes);
    for (size_t i = 0; i < 2 * n; i++) {
        memset(buf, 'x', bytes);
        /* Fixed-endian unique binary members, including embedded NUL bytes. */
        for (unsigned j = 0; j < 8; j++) buf[j] = (char)((uint64_t)i >> (j * 8));
        keys[i] = sdsnewlen(buf, bytes);
        if (i < n) order[i] = i;
    }
    zfree(buf);
    for (size_t i = n; i > 1; i--) {
        size_t j = random64(&rng) % i, tmp = order[i - 1];
        order[i - 1] = order[j]; order[j] = tmp;
    }
    puts("case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum");
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) {
        if (strcmp(selected, "all") && strcmp(selected, cases[c])) continue;
        zbtreeSet *tree = zbtreeCreate();
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
        /* One complete untimed lookup pass defines a warm, resident workload. */
        if (c != 0) for (size_t i = 0; i < n; i++) {
            double score;
            serverAssert(zbtreeScore(tree, keys[order[i]], &score) && score == (double)order[i]);
        }
        size_t count = (c == 0 || c == 7) ? n : ops;
        uint64_t checksum = 0, expected = 0;
        size_t tree_bytes = zbtreeAllocSize(tree);
        if (c == 4 || c == 5) count = n;
        if (c == 1 || c == 3) for (size_t i = 0; i < count; i++) expected += order[i % n];
        else if (c == 5 || c == 6 || c == 7) expected = count;
        else if (c == 4) expected = (uint64_t)n * (n - 1) / 2;
        uint64_t start = now_ns();
        if (c == 0) {
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], (double)order[i]);
        } else if (c == 1 || c == 2) {
            for (size_t i = 0; i < count; i++) {
                double score = 0;
                int found = zbtreeScore(tree, keys[order[i % n] + (c == 2 ? n : 0)], &score);
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
            }
        } else if (c == 3) {
            for (size_t i = 0; i < count; i++) checksum += (uint64_t)zbtreeRank(tree, keys[order[i % n]], 0, NULL);
        } else if (c == 4) {
            zbtreeIterator it;
            zbtreeIteratorStart(tree, 0, &it);
            double score;
            size_t visited = 0;
            while (zbtreeIteratorNext(&it, 0, NULL, NULL, &score)) { checksum += (uint64_t)score; visited++; }
            serverAssert(visited == n);
        } else if (c == 5) {
            uint64_t cursor = 0;
            do { cursor = zbtreeScan(tree, cursor, 64, scan_count, &checksum); } while (cursor);
        } else if (c == 6) {
            for (size_t i = 0; i < count; i++) {
                sds key = keys[order[i % n]];
                zbtreeInsertPosition pos;
                double score;
                int found = zbtreeFindForAdd(tree, key, &score, &pos);
                serverAssert(found);
                zbtreeUpdateScore(tree, key, score + (double)n, &pos);
                checksum += found;
            }
        } else {
            for (size_t i = 0; i < n; i++) checksum += zbtreeDelete(tree, keys[order[i]]);
        }
        uint64_t elapsed = now_ns() - start;
        if (c == 5) {
            /* Cursor scans may legitimately emit duplicates even without edits. */
            serverAssert(checksum >= n);
            count = (size_t)checksum;
            expected = checksum;
            scan_check check = {zcalloc(n), n};
            uint64_t cursor = 0;
            do { cursor = zbtreeScan(tree, cursor, 64, scan_verify, &check); } while (cursor);
            for (size_t i = 0; i < n; i++) serverAssert(check.seen[i]);
            zfree(check.seen);
        }
        serverAssert(checksum == expected);
        serverAssert(zbtreeLength(tree) == (c == 7 ? 0 : n));
        if (c != 7) tree_bytes = zbtreeAllocSize(tree);
        if (c == 6) for (size_t i = 0; i < n; i++) {
            double score;
            size_t repeats = ops / n + (i < ops % n);
            serverAssert(zbtreeScore(tree, keys[order[i]], &score));
            serverAssert(score == (double)order[i] + (double)(repeats * n));
        }
        sink ^= checksum;
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 "\n",
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum);
        zbtreeFree(tree);
    }
    for (size_t i = 0; i < 2 * n; i++) sdsfree(keys[i]);
    zfree(keys); zfree(order);
    return 0;
}
