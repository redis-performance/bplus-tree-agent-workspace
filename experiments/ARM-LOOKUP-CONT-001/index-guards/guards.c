/* Public API referee. Diagnostics only read internals; they never mutate them. */
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <errno.h>
#include <inttypes.h>
#include <string.h>
#include <time.h>
#ifdef INDEX_DIAGNOSTIC
#include ZBT_SOURCE
#endif

#define HIGH 512
#define LOW 128
#define READ_MEMBERS 256
#define MISSES 32
#define KEYLEN 128
#define TOTAL (HIGH + MISSES)
static sds keys[TOTAL];
static uint32_t hashes[TOTAL];
static unsigned nonces[TOTAL];
static unsigned present[HIGH];
static double model[HIGH];
static uint64_t fixture_digest = UINT64_C(1469598103934665603);
static uint64_t active_before, active_after, growth_states, shrink_states;
static uint64_t completions, leaf_reassignments, displaced, home_hits, max_distance;
static uint64_t mixed_active_before, reassigned_during_active;
static uint32_t previous_leaf[HIGH];
static int previous_active;

static uint64_t number(const char *s, uint64_t max) {
    char *end;
    errno = 0;
    serverAssert(*s >= '0' && *s <= '9');
    uint64_t n = strtoull(s, &end, 10);
    serverAssert(!errno && !*end && n > 0 && n <= max);
    return n;
}
static unsigned member_id(const unsigned char *p, size_t len) {
    serverAssert(len == KEYLEN);
    return (unsigned)p[0] | (unsigned)p[1] << 8 |
           (unsigned)p[2] << 16 | (unsigned)p[3] << 24;
}
static void put32(unsigned char *p, uint32_t n) {
    for (unsigned k = 0; k < 4; k++) p[k] = n >> (8*k);
}
static void generate(unsigned seed) {
    unsigned char secret[16];
    for (unsigned i = 0; i < 16; i++) secret[i] = (seed + 29*i) & 255;
    dictSetHashFunctionSeed(secret);
    for (unsigned i = 0; i < TOTAL; i++) {
        unsigned char b[KEYLEN];
        for (unsigned j = 0; j < KEYLEN; j++)
            b[j] = j % 7 ? (unsigned char)(i*17 + j*29) : 0;
        put32(b, i);
        unsigned nonce;
        for (nonce = 0; nonce < 10000000; nonce++) {
            put32(b+4, nonce);
            uint32_t h = zbtreeMemberHash(b, sizeof(b));
            if ((h & 63) == 63 && (h >> 24) == (i & 1)) {
                hashes[i] = h;
                break;
            }
        }
        serverAssert(nonce < 10000000);
        nonces[i] = nonce;
        keys[i] = sdsnewlen(b, sizeof(b));
        for (unsigned j = 0; j < KEYLEN; j++) {
            fixture_digest ^= b[j];
            fixture_digest *= UINT64_C(1099511628211);
        }
    }
}

/* No API call here can advance a resize. Only correctness diagnostics use it. */
static void observe(zbtreeSet *t, int before) {
#ifdef INDEX_DIAGNOSTIC
    int active = t->member_rehash != NULL;
    if (active) {
        if (before) {
            active_before++;
            mixed_active_before += t->member_rehash->table.used > 0 &&
                                   t->member_index.used > 0;
        } else active_after++;
        growth_states += t->member_rehash->table.size > t->member_index.size;
        shrink_states += t->member_rehash->table.size < t->member_index.size;
    }
    completions += previous_active && !active;
    previous_active = active;
    if (!before) {
        uint32_t current[HIGH] = {0};
        for (zbtScoreLeaf *leaf = t->score_first; leaf; leaf = leaf->next) {
            for (unsigned pos = 0; pos < leaf->n.count; pos++) {
                size_t len;
                const unsigned char *p = zbtScoreLeafElement(leaf, pos, &len);
                unsigned id = member_id(p, len);
                serverAssert(id < HIGH);
                current[id] = leaf->id;
                if (previous_leaf[id] && previous_leaf[id] != leaf->id) {
                    leaf_reassignments++;
                    reassigned_during_active += active;
                }
            }
        }
        memcpy(previous_leaf, current, sizeof(current));
    }
#else
    (void)t; (void)before;
#endif
}
static void check_tree(zbtreeSet *t) {
    unsigned expected = 0;
    for (unsigned i = 0; i < HIGH; i++) {
        double score = -123;
        int found = zbtreeScoreRaw(t, (unsigned char *)keys[i], KEYLEN, &score);
        serverAssert(found == (int)present[i]);
        serverAssert(score == (present[i] ? model[i] : -123));
        expected += present[i];
    }
    serverAssert(zbtreeLength(t) == expected);
    zbtreeIterator it;
    serverAssert(zbtreeIteratorStart(t, 0, &it) == (expected != 0));
    unsigned count = 0, seen[HIGH] = {0};
    const unsigned char *p;
    size_t len;
    double score;
    while (zbtreeIteratorNext(&it, 0, &p, &len, &score)) {
        unsigned id = member_id(p, len);
        serverAssert(id < HIGH && present[id] && !seen[id]++);
        serverAssert(score == model[id] && !memcmp(p, keys[id], len));
        count++;
    }
    serverAssert(count == expected);
}
static void insert(zbtreeSet *t, unsigned i) {
    observe(t, 1);
    zbtreeInsertNewRaw(t, i+1, (unsigned char *)keys[i], KEYLEN, NULL);
    present[i] = 1;
    model[i] = i+1;
    observe(t, 0);
}
static zbtreeSet *fixture(int churn) {
    memset(present, 0, sizeof(present));
    memset(previous_leaf, 0, sizeof(previous_leaf));
    previous_active = 0;
    zbtreeSet *t = zbtreeCreate();
    if (!churn) zbtreeReserve(t, READ_MEMBERS);
    for (unsigned i = 0; i < (churn ? LOW : READ_MEMBERS); i++) insert(t, i);
    check_tree(t); /* Setup lookups deliberately finish any pending resize. */
    return t;
}
static void inspect_read_paths(zbtreeSet *t) {
#ifdef INDEX_DIAGNOSTIC
    serverAssert(!t->member_rehash && t->member_index.size == 64);
    zbtIndexTable *table = &t->member_index;
    for (unsigned i = 0; i < READ_MEMBERS; i++) {
        zbtIndexBucket *bucket = NULL;
        unsigned pos = 0;
        serverAssert(zbtIndexTableFind(t, table, hashes[i],
            (unsigned char *)keys[i], KEYLEN, NULL, NULL, NULL,
            &bucket, &pos, NULL, NULL));
        unsigned long physical = ((unsigned char *)bucket - (unsigned char *)table->buckets) /
                                 zbtIndexBucketBytes(table);
        unsigned long distance = (physical - (hashes[i] & (table->size-1))) &
                                 (table->size-1);
        if (distance) displaced++; else home_hits++;
        if (distance > max_distance) max_distance = distance;
    }
    serverAssert(displaced && home_hits && max_distance > 1);
    /* Every absent query passes the home filter and has a full home bucket. */
    for (unsigned i = HIGH; i < TOTAL; i++) {
        serverAssert(zbtIndexHomeMayContain(table, hashes[i]));
        zbtIndexBucket *home = zbtIndexBucketAt(table, hashes[i] & 63);
        for (unsigned p = 0; p < ZBT_INDEX_BUCKET_ITEMS; p++)
            serverAssert((uint8_t)(zbtIndexTags(home) >> (p*8)) != 0);
    }
#else
    (void)t;
#endif
}

typedef struct {
    uint64_t calls, hits, score_sum, byte_sum, scan_calls, callbacks;
    uint64_t seen[HIGH];
    int verify;
} sums;
static void callback(void *arg, const unsigned char *p, size_t len, double score) {
    sums *s = arg;
    unsigned id = member_id(p, len);
    serverAssert(id < READ_MEMBERS && score == id+1);
    if (s->verify) serverAssert(!memcmp(p, keys[id], len));
    s->callbacks++;
    s->seen[id]++;
    s->score_sum += (uint64_t)score;
    s->byte_sum += p[0] + 3u*p[len/2] + 7u*p[len-1] + len;
}
__attribute__((noinline))
static sums run(zbtreeSet *t, const char *kind, uint64_t sweeps, int verify) {
    sums s = {.verify = verify};
    for (uint64_t r = 0; r < sweeps; r++) {
        if (!strcmp(kind, "collision-hit") || !strcmp(kind, "collision-miss")) {
            int hit = !strcmp(kind, "collision-hit");
            unsigned first = hit ? 0 : HIGH;
            unsigned last = hit ? READ_MEMBERS : TOTAL;
            for (unsigned i = first; i < last; i++) {
                double score = -123;
                int found = zbtreeScoreRaw(t, (unsigned char *)keys[i], KEYLEN, &score);
                serverAssert(found == hit);
                if (verify) serverAssert(score == (hit ? (double)i+1 : -123));
                s.calls++;
                s.hits += found;
                if (found) s.score_sum += (uint64_t)score;
            }
        } else if (!strcmp(kind, "scan-members")) {
            uint64_t prior[READ_MEMBERS];
            if (verify) memcpy(prior, s.seen, sizeof(prior));
            uint64_t cursor = 0;
            unsigned steps = 0;
            do {
                cursor = zbtreeScan(t, cursor, 16, callback, &s);
                s.calls++; s.scan_calls++;
                serverAssert(++steps <= 1024);
            } while (cursor);
            if (verify) for (unsigned i = 0; i < READ_MEMBERS; i++)
                serverAssert(s.seen[i] > prior[i]);
        } else {
            serverAssert(!strcmp(kind, "repair-churn"));
            for (unsigned i = LOW; i < HIGH; i++) { insert(t, i); s.calls++; }
            /* Move every score across leaf boundaries, preserving unique keys. */
            for (unsigned i = 0; i < HIGH; i++) {
                observe(t, 1);
                zbtreeInsertPosition pos;
                double old;
                serverAssert(zbtreeFindForAdd(t, keys[i], &old, &pos));
                double score = HIGH + i + 1;
                zbtreeUpdateScore(t, keys[i], score, &pos);
                model[i] = score;
                observe(t, 0);
                s.calls += 2;
                s.score_sum += (uint64_t)score;
            }
            for (unsigned i = HIGH; i-- > LOW;) {
                observe(t, 1);
                serverAssert(zbtreeDelete(t, keys[i]));
                present[i] = 0;
                observe(t, 0);
                s.calls++; s.hits++;
            }
        }
    }
    return s;
}
static uint64_t now_ns(void) {
    struct timespec t;
    serverAssert(clock_gettime(CLOCK_MONOTONIC_RAW, &t) == 0);
    return (uint64_t)t.tv_sec*1000000000 + t.tv_nsec;
}
int main(int argc, char **argv) {
    if (argc == 3 && !strcmp(argv[1], "fixture")) {
        unsigned seed = number(argv[2], UINT32_MAX);
        generate(seed);
        printf("{\"seed\":%u,\"digest\":\"%016" PRIx64 "\",\"nonces\":[", seed, fixture_digest);
        for (unsigned i = 0; i < TOTAL; i++) printf("%s%u", i ? "," : "", nonces[i]);
        printf("],\"hashes\":[");
        for (unsigned i = 0; i < TOTAL; i++) printf("%s%u", i ? "," : "", hashes[i]);
        printf("]}\n");
        for (unsigned i = 0; i < TOTAL; i++) sdsfree(keys[i]);
        return 0;
    }
    serverAssert(argc == 5);
    int verify = !strcmp(argv[1], "verify");
    serverAssert(verify || !strcmp(argv[1], "measure"));
#ifdef INDEX_DIAGNOSTIC
    serverAssert(verify); /* Diagnostic code is categorically ineligible for timing. */
#endif
    const char *kind = argv[2];
    serverAssert(!strcmp(kind, "collision-hit") || !strcmp(kind, "collision-miss") ||
                 !strcmp(kind, "repair-churn") || !strcmp(kind, "scan-members"));
    unsigned seed = number(argv[3], UINT32_MAX);
    uint64_t sweeps = number(argv[4], verify ? 8 : 2000000);
    generate(seed);
    int churn = !strcmp(kind, "repair-churn");
    zbtreeSet *t = fixture(churn);
    if (!churn) inspect_read_paths(t);
    /* No warmup mutates the fixture. Future fleet collector must qualify this boundary. */
    active_before = active_after = growth_states = shrink_states = 0;
    completions = leaf_reassignments = 0;
    mixed_active_before = reassigned_during_active = 0;
    size_t before = zbtreeAllocSize(t);
    uint64_t elapsed = 0;
    sums s;
    if (verify) s = run(t, kind, sweeps, 1);
    else {
        uint64_t start = now_ns();
        s = run(t, kind, sweeps, 0);
        elapsed = now_ns() - start;
    }
    size_t after = zbtreeAllocSize(t); /* Before any validating lookup advances rehash. */
    if (!strcmp(kind, "collision-hit")) {
        serverAssert(s.calls == sweeps*READ_MEMBERS && s.hits == s.calls);
        serverAssert(s.score_sum == sweeps*READ_MEMBERS*(READ_MEMBERS+1)/2);
    } else if (!strcmp(kind, "collision-miss")) {
        serverAssert(s.calls == sweeps*MISSES && !s.hits && !s.score_sum);
    } else if (churn) {
        serverAssert(s.calls == sweeps*(2*(HIGH-LOW)+2*HIGH));
        serverAssert(s.hits == sweeps*(HIGH-LOW));
        serverAssert(s.score_sum == sweeps*(HIGH*(HIGH+1)/2+HIGH*HIGH));
    } else {
        uint64_t expected_score = 0, expected_bytes = 0, count = 0;
        for (unsigned i = 0; i < READ_MEMBERS; i++) {
            serverAssert(s.seen[i] >= sweeps);
            const unsigned char *p = (unsigned char *)keys[i];
            expected_score += (i+1)*s.seen[i];
            expected_bytes += (p[0]+3u*p[KEYLEN/2]+7u*p[KEYLEN-1]+KEYLEN)*s.seen[i];
            count += s.seen[i];
        }
        serverAssert(s.callbacks == count && s.score_sum == expected_score &&
                     s.byte_sum == expected_bytes && s.calls == s.scan_calls);
    }
    check_tree(t);
    size_t after_validation = zbtreeAllocSize(t);
    printf("{\"verified\":true,\"mode\":\"%s\",\"case\":\"%s\",\"seed\":%u,"
           "\"sweeps\":%" PRIu64 ",\"calls\":%" PRIu64 ",\"hits\":%" PRIu64
           ",\"score_sum\":%" PRIu64 ",\"byte_sum\":%" PRIu64
           ",\"scan_calls\":%" PRIu64 ",\"callbacks\":%" PRIu64
           ",\"fixture_digest\":\"%016" PRIx64 "\",\"owned_bytes_before\":%zu,"
           "\"owned_bytes_after\":%zu,\"owned_bytes_after_validation\":%zu,"
           "\"diagnostic\":%s,\"home_hits\":%" PRIu64 ",\"displaced_hits\":%" PRIu64
           ",\"max_displacement\":%" PRIu64 ",\"active_before\":%" PRIu64
           ",\"active_after\":%" PRIu64 ",\"growth_states\":%" PRIu64
           ",\"shrink_states\":%" PRIu64 ",\"completions\":%" PRIu64
           ",\"leaf_reassignments\":%" PRIu64 ",\"mixed_active_before\":%" PRIu64
           ",\"reassigned_during_active\":%" PRIu64 ",\"seen\":[",
           argv[1], kind, seed, sweeps, s.calls, s.hits, s.score_sum, s.byte_sum,
           s.scan_calls, s.callbacks, fixture_digest, before, after, after_validation,
#ifdef INDEX_DIAGNOSTIC
           "true",
#else
           "false",
#endif
           home_hits, displaced, max_distance, active_before, active_after,
           growth_states, shrink_states, completions, leaf_reassignments,
           mixed_active_before, reassigned_during_active);
    for (unsigned i = 0; i < READ_MEMBERS; i++) printf("%s%" PRIu64, i ? "," : "", s.seen[i]);
    printf("]");
    if (!verify) printf(",\"elapsed_ns\":%" PRIu64, elapsed);
    printf("}\n");
    zbtreeFree(t);
    for (unsigned i = 0; i < TOTAL; i++) sdsfree(keys[i]);
    return 0;
}
