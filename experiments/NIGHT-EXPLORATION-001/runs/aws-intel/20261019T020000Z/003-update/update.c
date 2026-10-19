#define _GNU_SOURCE 1
#define _DARWIN_C_SOURCE 1
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <inttypes.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#if defined(__APPLE__)
#include <pthread.h>
#include <pthread/qos.h>
#elif defined(__linux__)
#include <sched.h>
#endif

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
/* Observations, not affinity or frequency controls. -1 means unavailable. */
static int64_t thread_ns(void) {
#if defined(CLOCK_THREAD_CPUTIME_ID)
    struct timespec ts;
    if (clock_gettime(CLOCK_THREAD_CPUTIME_ID, &ts) == 0)
        return (int64_t)ts.tv_sec * INT64_C(1000000000) + ts.tv_nsec;
#endif
    return -1;
}
static int cpu_id(void) {
#if defined(__APPLE__)
    size_t cpu;
    if (__builtin_available(macOS 11.0, *))
        return pthread_cpu_number_np(&cpu) == 0 ? (int)cpu : -1;
    return -1;
#elif defined(__linux__)
    return sched_getcpu();
#else
    return -1;
#endif
}
/* The public API reports requested QoS, not effective overrides/clamps. */
static const char *qos_reported(int *relative_priority) {
    *relative_priority = 0;
#if defined(__APPLE__)
    qos_class_t qos;
    if (pthread_get_qos_class_np(pthread_self(), &qos, relative_priority)) return "unknown";
    switch (qos) {
    case QOS_CLASS_USER_INTERACTIVE: return "user-interactive";
    case QOS_CLASS_USER_INITIATED: return "user-initiated";
    case QOS_CLASS_DEFAULT: return "default";
    case QOS_CLASS_UTILITY: return "utility";
    case QOS_CLASS_BACKGROUND: return "background";
    case QOS_CLASS_UNSPECIFIED: return "unspecified";
    default: return "unknown";
    }
#else
    return "unavailable";
#endif
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
typedef struct { uint64_t count, sum; } scan_result;
static void scan_count(void *ctx, const unsigned char *key, size_t len, double score) {
    UNUSED(key); UNUSED(len);
    scan_result *result = ctx;
    result->count++;
    result->sum += (uint64_t)score;
}
typedef struct { unsigned char *seen; size_t n; sds *keys; scan_result result; } scan_check;
static void scan_verify(void *ctx, const unsigned char *key, size_t len, double score) {
    scan_check *check = ctx;
    serverAssert(len >= 8);
    uint64_t id = 0;
    for (unsigned j = 0; j < 8; j++) id |= (uint64_t)key[j] << (j * 8);
    serverAssert(id < check->n && score == (double)id);
    serverAssert(len == sdslen(check->keys[id]) && !memcmp(key, check->keys[id], len));
    check->seen[id] = 1;
    scan_count(&check->result, key, len, score);
}
static const char *update_pattern = "position";
static double initial_score(size_t id) {
    return !strcmp(update_pattern, "original") ? (double)id : (double)(4*id+(id&1));
}
static double target_score(size_t id, size_t n, size_t round) {
    double base = initial_score(id);
    if (!strcmp(update_pattern, "same")) return base;
    if (!strcmp(update_pattern, "position")) return base + (double)(round&1);
    if (!strcmp(update_pattern, "nearby")) return (round&1) && (id^1)<n ? initial_score(id^1) : base;
    if (!strcmp(update_pattern, "distant")) return base + (double)((round&1)*8*n);
    return base + (double)(round*n);
}
#ifdef PROFILE_TIMED
extern void moncontrol(int mode);
#endif

int main(int argc, char **argv) {
#ifdef PROFILE_TIMED
    moncontrol(0);
#endif
    size_t n = 100000, ops = 1000000, bytes = 16, warmup_passes = 1;
    uint64_t seed = 1, query_seed = 2;
    const char *query_order = "coupled";
    const char *selected = "update";
    const char *cases[] = {"insert", "lookup-hit", "lookup-miss", "rank", "iterate", "scan", "update", "delete"};
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--help")) {
            puts("btree-bench [--size N] [--ops N] [--member-bytes N>=8] [--seed N] [--warmup-passes N>=1] [--query-order coupled|independent] [--query-seed N] [--case all|insert|lookup-hit|lookup-miss|rank|iterate|scan|update|delete]");
            return 0;
        }
        if (i + 1 == argc) { fprintf(stderr, "Missing value: %s\n", argv[i]); return 2; }
        const char *arg = argv[i++], *value = argv[i];
        if (!strcmp(arg, "--size")) n = number(value);
        else if (!strcmp(arg, "--ops")) ops = number(value);
        else if (!strcmp(arg, "--member-bytes")) bytes = number(value);
        else if (!strcmp(arg, "--seed")) seed = number(value);
        else if (!strcmp(arg, "--query-seed")) query_seed = number(value);
        else if (!strcmp(arg, "--query-order")) query_order = value;
        else if (!strcmp(arg, "--warmup-passes")) warmup_passes = number(value);
        else if (!strcmp(arg, "--case")) selected = value;
        else if (!strcmp(arg, "--pattern")) update_pattern = value;
        else { fprintf(stderr, "Unknown option: %s\n", arg); return 2; }
    }
    int valid_case = !strcmp(selected, "all");
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) valid_case |= !strcmp(selected, cases[c]);
    if (!valid_case || bytes < 8 || bytes > 65536) { fputs("Invalid case or member size (8..65536)\n", stderr); return 2; }
    if (strcmp(query_order, "coupled") && strcmp(query_order, "independent")) {
        fputs("Invalid query order (coupled|independent)\n", stderr); return 2;
    }
    if (strcmp(update_pattern,"same") && strcmp(update_pattern,"position") && strcmp(update_pattern,"nearby") && strcmp(update_pattern,"distant") && strcmp(update_pattern,"original")) return 2;
    uint64_t rng = seed;
    uint8_t hash_seed[16];
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys = zmalloc(2 * n * sizeof(*keys));
    size_t *order = zmalloc(n * sizeof(*order));
    size_t *query = zmalloc(n * sizeof(*query));
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
    /* Independent queries start from identity and their own PRNG state: neither
     * hash-seed draws nor insertion shuffle affect this permutation. Both modes
     * allocate/touch the same arrays. Coupled mode preserves historical order. */
    for (size_t i = 0; i < n; i++) query[i] = !strcmp(query_order, "coupled") ? order[i] : i;
    uint64_t query_rng = query_seed;
    if (!strcmp(query_order, "independent")) for (size_t i = n; i > 1; i--) {
        size_t j = random64(&query_rng) % i, tmp = query[i-1];
        query[i-1] = query[j]; query[j] = tmp;
    }
    uint64_t construction_fingerprint = UINT64_C(14695981039346656037);
    uint64_t query_fingerprint = UINT64_C(14695981039346656037);
    for (size_t i = 0; i < n; i++) {
        construction_fingerprint = (construction_fingerprint ^ order[i]) * UINT64_C(1099511628211);
        query_fingerprint = (query_fingerprint ^ query[i]) * UINT64_C(1099511628211);
    }
    puts("case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns,construction_order,construction_fingerprint,query_order,query_seed,query_fingerprint,warmup_case,pattern,final_score_sum");
    for (size_t c = 0; c < sizeof(cases)/sizeof(*cases); c++) {
        if (strcmp(selected, "all") && strcmp(selected, cases[c])) continue;
        zbtreeSet *tree = zbtreeCreate();
        if (c != 0) for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], c == 6 ? initial_score(order[i]) : (double)order[i]);
        /* Fixed-count warm-up; this does not establish stable placement/DVFS. */
        uint64_t warmup_start = now_ns();
        if (c != 0) for (size_t pass = 0; pass < warmup_passes; pass++) for (size_t i = 0; i < n; i++) {
            double score;
            if (c == 2) serverAssert(!zbtreeScore(tree, keys[query[i] + n], &score));
            else serverAssert(zbtreeScore(tree, keys[query[i]], &score) && score == (c == 6 ? initial_score(query[i]) : (double)query[i]));
        }
        uint64_t warmup_elapsed = now_ns() - warmup_start;
        size_t count = (c == 0 || c == 7) ? n : ops;
        uint64_t checksum = 0, expected = 0;
        size_t tree_bytes = zbtreeAllocSize(tree);
        size_t traversals = (c == 4 || c == 5) ? 1 + (ops - 1) / n : 0;
        if (c == 4 || c == 5) count = traversals * n;
        if (c == 1 || c == 3) for (size_t i = 0; i < count; i++) expected += query[i % n];
        else if (c == 6 || c == 7) expected = count;
        else if (c == 4) expected = ((uint64_t)n * (n - 1) / 2) * traversals;
        scan_result scanned = {0, 0};
        int relpri_start, relpri_end;
        const char *qos_start = qos_reported(&relpri_start);
        int cpu_start = cpu_id();
        int64_t thread_start = thread_ns();
#if defined(PROFILE_TIMED) && PROFILE_TIMED == 1
        moncontrol(1);
#endif
        uint64_t start = now_ns();
        if (c == 0) {
            for (size_t i = 0; i < n; i++) insert(tree, keys[order[i]], c == 6 ? initial_score(order[i]) : (double)order[i]);
        } else if (c == 1 || c == 2) {
            for (size_t i = 0; i < count; i++) {
                double score = 0;
                int found = zbtreeScore(tree, keys[query[i % n] + (c == 2 ? n : 0)], &score);
                checksum += c == 1 ? (found ? (uint64_t)score : UINT64_MAX) : (uint64_t)found;
            }
        } else if (c == 3) {
            for (size_t i = 0; i < count; i++) checksum += (uint64_t)zbtreeRank(tree, keys[query[i % n]], 0, NULL);
        } else if (c == 4) {
            for (size_t pass = 0; pass < traversals; pass++) {
                zbtreeIterator it;
                zbtreeIteratorStart(tree, 0, &it);
                double score;
                size_t visited = 0;
                while (zbtreeIteratorNext(&it, 0, NULL, NULL, &score)) { checksum += (uint64_t)score; visited++; }
                serverAssert(visited == n);
            }
        } else if (c == 5) {
            for (size_t pass = 0; pass < traversals; pass++) {
                uint64_t cursor = 0;
                do { cursor = zbtreeScan(tree, cursor, 64, scan_count, &scanned); } while (cursor);
            }
            checksum = scanned.sum;
        } else if (c == 6) {
            for (size_t i = 0; i < count; i++) {
                sds key = keys[query[i % n]];
                zbtreeInsertPosition pos;
                double score;
                int found = zbtreeFindForAdd(tree, key, &score, &pos);
                serverAssert(found);
                zbtreeUpdateScore(tree, key, target_score(query[i % n], n, i/n+1), &pos);
                checksum += found;
            }
        } else {
            for (size_t i = 0; i < n; i++) checksum += zbtreeDelete(tree, keys[query[i]]);
        }
        uint64_t elapsed = now_ns() - start;
#ifdef PROFILE_TIMED
        moncontrol(0);
#endif
        int64_t thread_end = thread_ns();
        int cpu_end = cpu_id();
        const char *qos_end = qos_reported(&relpri_end);
        int64_t thread_elapsed = thread_start >= 0 && thread_end >= thread_start ? thread_end - thread_start : -1;
        if (c == 5) {
            /* Cursor scans may legitimately emit duplicates even without edits. */
            serverAssert(scanned.count >= count && scanned.count <= SIZE_MAX);
            count = (size_t)scanned.count;
            scan_check check = {zcalloc(n), n, keys, {0, 0}};
            uint64_t cursor = 0;
            do { cursor = zbtreeScan(tree, cursor, 64, scan_verify, &check); } while (cursor);
            for (size_t i = 0; i < n; i++) serverAssert(check.seen[i]);
            serverAssert(scanned.count == check.result.count * traversals);
            expected = check.result.sum * traversals;
            zfree(check.seen);
        }
        serverAssert(checksum == expected);
        serverAssert(zbtreeLength(tree) == (c == 7 ? 0 : n));
        if (c != 7) tree_bytes = zbtreeAllocSize(tree);
        uint64_t final_score_sum = 0;
        if (c == 6) for (size_t i = 0; i < n; i++) {
            double score;
            size_t repeats = ops / n + (i < ops % n);
            serverAssert(zbtreeScore(tree, keys[query[i]], &score));
            double expected_score = target_score(query[i], n, repeats);
            serverAssert(memcmp(&score, &expected_score, sizeof(score)) == 0);
            final_score_sum += (uint64_t)score;
        }
        if (c == 6) {
            unsigned char *seen = zcalloc(n);
            size_t *query_position = zmalloc(n*sizeof(*query_position));
            for (size_t j=0;j<n;j++) query_position[query[j]]=j;
            zbtreeIterator it; zbtreeIteratorStart(tree,0,&it);
            const unsigned char *member; size_t len,visited=0,previous_id=0;
            double value,previous_score=0;
            while (zbtreeIteratorNext(&it,0,&member,&len,&value)) {
                uint64_t id=0;serverAssert(len==bytes);
                for(unsigned j=0;j<8;j++)id|=(uint64_t)member[j]<<(j*8);
                serverAssert(id<n && !seen[id] && !memcmp(member,keys[id],bytes));seen[id]=1;
                size_t rounds=ops/n+(query_position[id]<ops%n);
                double want=target_score(id,n,rounds);serverAssert(!memcmp(&value,&want,sizeof(value)));
                if(visited)serverAssert(value>previous_score || (value==previous_score && memcmp(keys[previous_id],member,bytes)<0));
                previous_score=value;previous_id=id;visited++;
            }
            serverAssert(visited==n);zfree(seen);zfree(query_position);
        }
        sink ^= checksum;
        printf("%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.3f,%.3f,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%zu,%" PRIu64 ",shuffled,%" PRIu64 ",%s,%" PRIu64 ",%" PRIu64 ",%s,%s,%" PRIu64 "\n",
               cases[c], n, ops, bytes, seed, count, elapsed, (double)elapsed/count,
               (double)count * 1e9 / (elapsed ? elapsed : 1), tree_bytes, checksum,
               thread_elapsed, cpu_start, cpu_end, qos_start, qos_end, relpri_start, relpri_end,
               traversals, c == 0 ? 0 : warmup_passes, warmup_elapsed,
               construction_fingerprint, query_order, query_seed, query_fingerprint,
               c == 0 ? "none" : c == 2 ? "lookup-miss" : "lookup-hit", update_pattern, final_score_sum);
        zbtreeFree(tree);
    }
    for (size_t i = 0; i < 2 * n; i++) sdsfree(keys[i]);
    zfree(keys); zfree(order); zfree(query);
    return 0;
}
