/* Supplemental public-API referee. Verify mode never reads a clock. */
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <errno.h>
#include <inttypes.h>
#include <string.h>
#include <time.h>

static const unsigned lengths[] = {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    24, 32, 64, 127, 128, 129, 252, 253, 254, 255, 318, 319,
    320, 321, 512, 1024
};
#define MEMBERS (1 + (sizeof(lengths) / sizeof(lengths[0]) - 1) * 16)
#define WARMUP_SWEEPS 1000
typedef enum { FORWARD, REVERSE, INLINE_LOOKUP, EXTERNAL_LOOKUP } guardCase;
typedef struct { sds hit, miss; } member;
typedef struct { uint64_t ops, hits, bytes, samples, weighted; int64_t scores; } sums;

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
    serverAssert(!clock_gettime(CLOCK_MONOTONIC_RAW, &t));
    return (uint64_t)t.tv_sec * UINT64_C(1000000000) + t.tv_nsec;
}
/* Three bounded byte reads consume the returned pointer without making a
 * full-string hash the timed workload. Full byte equality is checked outside. */
static uint64_t sample(const unsigned char *p, size_t n) {
    return n ? p[0] + 257u * p[n / 2] + 65537u * p[n - 1] : 0;
}
static int selected(guardCase kind, size_t n) {
    return kind == INLINE_LOOKUP ? n < 320 : n >= 320;
}
static zbtreeSet *fixture(member *m) {
    unsigned char buf[1024];
    size_t i = 0;
    for (size_t k = 0; k < sizeof(lengths) / sizeof(lengths[0]); k++) {
        size_t len = lengths[k];
        for (unsigned replica = 0; replica < (len ? 16u : 1u); replica++) {
            for (size_t b = 0; b < len; b++)
                buf[b] = b % 7 == 0 ? 0 : (unsigned char)(b * 37 + replica * 11);
            if (len) buf[0] = replica; /* unique within every length */
            m[i].hit = sdsnewlen(buf, len);
            if (len) {
                buf[0] ^= 128; /* absent: every stored first byte is 0..15 */
                m[i].miss = sdsnewlen(buf, len);
            } else {
                buf[0] = 254;
                m[i].miss = sdsnewlen(buf, 1);
            }
            i++;
        }
    }
    serverAssert(i == MEMBERS);
    zbtreeSet *t = zbtreeCreate();
    zbtreeReserve(t, MEMBERS);
    /* Alternating ends exercise insertion on both sides, with fixed scores. */
    for (size_t j = 0; j < MEMBERS; j++) {
        size_t id = j & 1 ? MEMBERS - 1 - j / 2 : j / 2;
        zbtreeInsertNewRaw(t, id + 1, (unsigned char *)m[id].hit,
                          sdslen(m[id].hit), NULL);
    }
    return t;
}
static void check_tree(zbtreeSet *t, const member *m) {
    serverAssert(zbtreeLength(t) == MEMBERS);
    for (int reverse = 0; reverse < 2; reverse++) {
        zbtreeIterator it;
        serverAssert(zbtreeIteratorStart(t, reverse, &it));
        for (size_t j = 0; j < MEMBERS; j++) {
            size_t id = reverse ? MEMBERS - 1 - j : j;
            const unsigned char *p;
            size_t n;
            double score = -1;
            serverAssert(zbtreeIteratorNext(&it, reverse, &p, &n, &score));
            serverAssert(n == sdslen(m[id].hit));
            serverAssert(!memcmp(p, m[id].hit, n) && score == id + 1);
        }
        serverAssert(!zbtreeIteratorNext(&it, reverse, NULL, NULL, NULL));
    }
    for (size_t id = 0; id < MEMBERS; id++) {
        double score = -123;
        serverAssert(zbtreeScoreRaw(t, (unsigned char *)m[id].hit,
                                    sdslen(m[id].hit), &score));
        serverAssert(score == id + 1);
        score = -123;
        serverAssert(!zbtreeScoreRaw(t, (unsigned char *)m[id].miss,
                                     sdslen(m[id].miss), &score));
        serverAssert(score == -123);
    }
}
static void add_member(sums *c, const unsigned char *p, size_t n,
                       double score, size_t ordinal) {
    c->ops++;
    c->hits++;
    c->bytes += n;
    c->samples += sample(p, n) * ordinal;
    c->scores += (int64_t)score;
    c->weighted += (uint64_t)score * ordinal;
}
__attribute__((noinline))
static sums run(zbtreeSet *t, const member *m, guardCase kind, uint64_t sweeps) {
    sums c = {0};
    for (uint64_t sweep = 0; sweep < sweeps; sweep++) {
        if (kind == FORWARD || kind == REVERSE) {
            int reverse = kind == REVERSE;
            zbtreeIterator it;
            serverAssert(zbtreeIteratorStart(t, reverse, &it));
            const unsigned char *p;
            size_t n, ordinal = 0;
            double score;
            while (zbtreeIteratorNext(&it, reverse, &p, &n, &score))
                add_member(&c, p, n, score, ++ordinal);
            serverAssert(ordinal == MEMBERS);
        } else {
            for (size_t id = 0; id < MEMBERS; id++) {
                if (!selected(kind, sdslen(m[id].hit))) continue;
                for (unsigned miss = 0; miss < 2; miss++) {
                    sds query = miss ? m[id].miss : m[id].hit;
                    double score = -123;
                    int found = zbtreeScoreRaw(t, (unsigned char *)query,
                                               sdslen(query), &score);
                    c.ops++;
                    c.hits += found;
                    c.scores += (int64_t)score;
                    c.weighted += found * (id + 1);
                }
            }
        }
    }
    return c;
}
/* Expectations use only generated caller-owned bytes and integer IDs. */
static sums expected(const member *m, guardCase kind, uint64_t sweeps) {
    sums c = {0};
    for (size_t j = 0; j < MEMBERS; j++) {
        size_t id = kind == REVERSE ? MEMBERS - 1 - j : j;
        if (kind == FORWARD || kind == REVERSE) {
            add_member(&c, (unsigned char *)m[id].hit, sdslen(m[id].hit),
                       id + 1, j + 1);
        } else if (selected(kind, sdslen(m[id].hit))) {
            c.ops += 2;
            c.hits++;
            c.scores += (int64_t)(id + 1) - 123;
            c.weighted += id + 1;
        }
    }
    c.ops *= sweeps; c.hits *= sweeps; c.bytes *= sweeps;
    c.samples *= sweeps; c.scores *= (int64_t)sweeps; c.weighted *= sweeps;
    return c;
}
static void check_sums(sums a, sums b) {
    serverAssert(a.ops == b.ops && a.hits == b.hits && a.bytes == b.bytes);
    serverAssert(a.samples == b.samples && a.scores == b.scores &&
                 a.weighted == b.weighted);
}
int main(int argc, char **argv) {
    serverAssert(argc == 5);
    int verify = !strcmp(argv[1], "verify");
    serverAssert(verify || !strcmp(argv[1], "measure"));
    guardCase kind;
    if (!strcmp(argv[2], "member-forward")) kind = FORWARD;
    else if (!strcmp(argv[2], "member-reverse")) kind = REVERSE;
    else if (!strcmp(argv[2], "lookup-inline")) kind = INLINE_LOOKUP;
    else { serverAssert(!strcmp(argv[2], "lookup-external")); kind = EXTERNAL_LOOKUP; }
    unsigned seed = number(argv[3], UINT32_MAX);
    uint64_t sweeps = number(argv[4], verify ? 8 : 2000000);
    serverAssert(sweeps > 0);
    uint8_t key[16];
    for (unsigned i = 0; i < 16; i++) key[i] = (seed + 29 * i) & 255;
    dictSetHashFunctionSeed(key);
    member m[MEMBERS];
    zbtreeSet *t = fixture(m);
    check_tree(t, m);
    if (!verify) {
        check_sums(run(t, m, kind, WARMUP_SWEEPS), expected(m, kind, WARMUP_SWEEPS));
        check_tree(t, m);
    }
    sums want = expected(m, kind, sweeps);
    size_t before = zbtreeAllocSize(t);
    uint64_t elapsed = 0, start = 0;
    if (!verify) start = now_ns();
    sums got = run(t, m, kind, sweeps);
    if (!verify) elapsed = now_ns() - start;
    /* Capture the real endpoint before validation can advance any rehash. */
    size_t after = zbtreeAllocSize(t);
    check_sums(got, want);
    check_tree(t, m);
    size_t after_validation = zbtreeAllocSize(t);
    printf("{\"verified\":true,\"revision\":0,\"mode\":\"%s\",\"case\":\"%s\","
           "\"seed\":%u,\"sweeps\":%" PRIu64 ",\"members\":%zu,"
           "\"ops\":%" PRIu64 ",\"hits\":%" PRIu64 ",\"bytes\":%" PRIu64 ","
           "\"samples\":%" PRIu64 ",\"scores\":%" PRId64 ",\"weighted\":%" PRIu64 ","
           "\"owned_bytes_before\":%zu,\"owned_bytes_after\":%zu,"
           "\"owned_bytes_after_validation\":%zu",
           argv[1], argv[2], seed, sweeps, (size_t)MEMBERS,
           got.ops, got.hits, got.bytes, got.samples, got.scores, got.weighted,
           before, after, after_validation);
    if (!verify) printf(",\"elapsed_ns\":%" PRIu64, elapsed);
    puts("}");
    zbtreeFree(t);
    for (size_t i = 0; i < MEMBERS; i++) { sdsfree(m[i].hit); sdsfree(m[i].miss); }
    return 0;
}
