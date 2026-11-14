/* Separate public-API guard referee. verify never reads a clock. */
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <errno.h>
#include <inttypes.h>
#include <string.h>
#include <time.h>

#define MEMBERS 500
#define WARMUP_SWEEPS 1000

typedef enum {
    GUARD_ITERATOR_FORWARD, GUARD_ITERATOR_REVERSE,
    GUARD_RANK_FORWARD, GUARD_RANK_REVERSE, GUARD_CHURN
} guardCase;
typedef struct {
    uint64_t items;
    uint64_t rank_sum;
    double score_sum;
    double weighted_sum;
} checksums;

static uint64_t number(const char *s, uint64_t limit) {
    char *end;
    serverAssert(*s >= '0' && *s <= '9');
    errno = 0;
    unsigned long long n = strtoull(s, &end, 10);
    serverAssert(!errno && !*end && n <= limit);
    return n;
}

static uint64_t now_ns(void) {
    struct timespec t;
    serverAssert(clock_gettime(CLOCK_MONOTONIC_RAW, &t) == 0);
    return (uint64_t)t.tv_sec * UINT64_C(1000000000) + t.tv_nsec;
}

/* Match the short-member construction in the frozen lookup fixture. */
static zbtreeSet *fixture(sds *members) {
    zbtreeSet *t = zbtreeCreate();
    zbtreeReserve(t, 129);
    for (int i = 0; i < MEMBERS; i++) {
        if (i < 128) {
            serverAssert(!zbtreeScoreRaw(t, (unsigned char *)members[i],
                                        sdslen(members[i]), NULL));
            zbtreeInsertNewRaw(t, i + 1, (unsigned char *)members[i],
                              sdslen(members[i]), NULL);
        } else {
            zbtreeInsertPosition pos;
            double score;
            serverAssert(!zbtreeFindForAdd(t, members[i], &score, &pos));
            zbtreeInsertNew(t, i + 1, members[i], &pos);
        }
    }
    return t;
}

/* Exact public-API model checks live outside every measured interval. */
static void check_tree(zbtreeSet *t, sds *members, const double *scores) {
    serverAssert(zbtreeLength(t) == MEMBERS);
    for (int reverse = 0; reverse < 2; reverse++) {
        zbtreeIterator it;
        serverAssert(zbtreeIteratorStart(t, reverse, &it));
        for (int j = 0; j < MEMBERS; j++) {
            int i = reverse ? MEMBERS - 1 - j : j;
            const unsigned char *ele;
            size_t len;
            double score = -1;
            serverAssert(zbtreeIteratorNext(&it, reverse, &ele, &len, &score));
            serverAssert(len == sdslen(members[i]));
            serverAssert(!memcmp(ele, members[i], len));
            serverAssert(score == scores[i]);
            score = -1;
            serverAssert(zbtreeRank(t, members[i], reverse, &score) == j);
            serverAssert(score == scores[i]);
            score = -1;
            serverAssert(zbtreeScore(t, members[i], &score));
            serverAssert(score == scores[i]);
        }
        serverAssert(!zbtreeIteratorNext(&it, reverse, NULL, NULL, NULL));
    }
    sds absent = sdsnew("not-a-member");
    double untouched = -123;
    serverAssert(zbtreeRank(t, absent, 0, &untouched) == -1);
    serverAssert(untouched == -123);
    serverAssert(!zbtreeScore(t, absent, NULL));
    sdsfree(absent);
}

__attribute__((noinline))
static checksums run_guard(zbtreeSet *t, sds *members, guardCase kind,
                          uint64_t sweeps, int verify, double *model) {
    checksums c = {0};
    for (uint64_t r = 0; r < sweeps; r++) {
        int reverse = kind == GUARD_ITERATOR_REVERSE || kind == GUARD_RANK_REVERSE;
        if (kind == GUARD_ITERATOR_FORWARD || kind == GUARD_ITERATOR_REVERSE) {
            zbtreeIterator it;
            int started = zbtreeIteratorStart(t, reverse, &it);
            serverAssert(started);
            uint64_t ordinal = 0;
            double score;
            while (zbtreeIteratorNext(&it, reverse, NULL, NULL, &score)) {
                ordinal++;
                c.items++;
                c.score_sum += score;
                c.weighted_sum += score * ordinal;
                if (verify) {
                    serverAssert(ordinal <= MEMBERS);
                    int i = reverse ? MEMBERS - ordinal : ordinal - 1;
                    serverAssert(score == model[i]);
                }
            }
            serverAssert(ordinal == MEMBERS);
        } else if (kind == GUARD_RANK_FORWARD || kind == GUARD_RANK_REVERSE) {
            for (int i = 0; i < MEMBERS; i++) {
                double score = 0;
                long rank = zbtreeRank(t, members[i], reverse, &score);
                c.items += rank >= 0;
                c.rank_sum += (uint64_t)(rank + 1);
                c.score_sum += score;
                c.weighted_sum += (double)(rank + 1) * (i + 1);
                if (verify) {
                    serverAssert(rank == (reverse ? MEMBERS - 1 - i : i));
                    serverAssert(score == model[i]);
                }
            }
        } else {
            for (int i = 0; i < MEMBERS; i++) {
                int deleted = zbtreeDelete(t, members[i]);
                /* InsertNew requires absence, so keep this safety check timed. */
                serverAssert(deleted);
                c.items += deleted;
                if (verify) {
                    serverAssert(zbtreeLength(t) == MEMBERS - 1);
                    serverAssert(!zbtreeScore(t, members[i], NULL));
                    serverAssert(zbtreeRank(t, members[i], 0, NULL) == -1);
                }
                double score = i + 1 + (r & 1 ? 0.0 : 0.125);
                zbtreeInsertNew(t, score, members[i], NULL);
                /* These are input checksums; final state is checked separately. */
                c.score_sum += score;
                c.weighted_sum += score * (i + 1);
                if (verify) {
                    model[i] = score;
                    double actual = -1;
                    serverAssert(zbtreeLength(t) == MEMBERS);
                    serverAssert(zbtreeScore(t, members[i], &actual));
                    serverAssert(actual == score);
                    serverAssert(zbtreeRank(t, members[i], 0, NULL) == i);
                    serverAssert(zbtreeRank(t, members[i], 1, NULL) == MEMBERS - 1 - i);
                }
            }
            if (verify) check_tree(t, members, model);
        }
    }
    return c;
}

static void check_sums(checksums c, guardCase kind, uint64_t sweeps) {
    /* Compute expectations from integer fixture IDs, not another tree. */
    double sum = 0, forward = 0, backward = 0;
    for (int i = 1; i <= MEMBERS; i++) {
        sum += i;
        forward += (double)i * i;
        backward += (double)i * (MEMBERS + 1 - i);
    }
    uint64_t first = (sweeps + 1) / 2;
    int reverse = kind == GUARD_ITERATOR_REVERSE || kind == GUARD_RANK_REVERSE;
    double score = sum * sweeps;
    double weighted = (reverse ? backward : forward) * sweeps;
    uint64_t ranks = (kind == GUARD_RANK_FORWARD || kind == GUARD_RANK_REVERSE) ?
                     (uint64_t)sum * sweeps : 0;
    if (kind == GUARD_CHURN) {
        score += MEMBERS * 0.125 * first;
        weighted = forward * sweeps + sum * 0.125 * first;
    }
    serverAssert(c.items == sweeps * MEMBERS);
    serverAssert(c.rank_sum == ranks);
    serverAssert(c.score_sum == score);
    serverAssert(c.weighted_sum == weighted);
}

int main(int argc, char **argv) {
    serverAssert(argc == 5);
    int verify = !strcmp(argv[1], "verify");
    serverAssert(verify || !strcmp(argv[1], "measure"));
    guardCase kind;
    if (!strcmp(argv[2], "iterator-forward")) kind = GUARD_ITERATOR_FORWARD;
    else if (!strcmp(argv[2], "iterator-reverse")) kind = GUARD_ITERATOR_REVERSE;
    else if (!strcmp(argv[2], "rank-forward")) kind = GUARD_RANK_FORWARD;
    else if (!strcmp(argv[2], "rank-reverse")) kind = GUARD_RANK_REVERSE;
    else { serverAssert(!strcmp(argv[2], "churn")); kind = GUARD_CHURN; }
    unsigned seed = number(argv[3], UINT32_MAX);
    uint64_t sweeps = number(argv[4], verify ? 8 : 2000000);
    serverAssert(sweeps > 0 && (verify || sweeps % 2 == 0));
    uint8_t key[16];
    for (unsigned i = 0; i < 16; i++) key[i] = (seed + 29 * i) & 255;
    dictSetHashFunctionSeed(key);
    sds members[MEMBERS];
    double model[MEMBERS];
    for (int i = 0; i < MEMBERS; i++) {
        char b[32];
        int len = snprintf(b, sizeof(b), "m:%d", i + 1);
        members[i] = sdsnewlen(b, len);
        model[i] = i + 1;
    }
    zbtreeSet *t = fixture(members);
    check_tree(t, members, model);
    uint64_t elapsed = 0;
    size_t before;
    checksums c;
    if (verify) {
        before = zbtreeAllocSize(t);
        c = run_guard(t, members, kind, sweeps, 1, model);
    } else {
        check_sums(run_guard(t, members, kind, WARMUP_SWEEPS, 0, NULL),
                   kind, WARMUP_SWEEPS);
        check_tree(t, members, model);
        before = zbtreeAllocSize(t);
        uint64_t start = now_ns();
        c = run_guard(t, members, kind, sweeps, 0, NULL);
        elapsed = now_ns() - start;
    }
    /* Validation lookups may advance rehash: sample the real loop endpoint first. */
    size_t after = zbtreeAllocSize(t);
    check_sums(c, kind, sweeps);
    check_tree(t, members, model);
    size_t after_validation = zbtreeAllocSize(t);
    printf("{\"verified\":true,\"mode\":\"%s\",\"case\":\"%s\","
           "\"seed\":%u,\"sweeps\":%" PRIu64 ",\"ops\":%" PRIu64 ","
           "\"mutation_api_calls\":%" PRIu64 ",\"items\":%" PRIu64 ","
           "\"rank_sum\":%" PRIu64 ",\"score_sum\":%.3f,\"weighted_sum\":%.3f,"
           "\"owned_bytes_before\":%zu,\"owned_bytes_after\":%zu,"
           "\"owned_bytes_after_validation\":%zu",
           argv[1], argv[2], seed, sweeps, sweeps * MEMBERS,
           kind == GUARD_CHURN ? sweeps * MEMBERS * 2 : 0,
           c.items, c.rank_sum, c.score_sum, c.weighted_sum, before, after,
           after_validation);
    if (!verify) printf(",\"elapsed_ns\":%" PRIu64, elapsed);
    printf("}\n");
    zbtreeFree(t);
    for (int i = 0; i < MEMBERS; i++) sdsfree(members[i]);
    return 0;
}
