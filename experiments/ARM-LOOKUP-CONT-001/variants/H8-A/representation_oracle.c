#define _GNU_SOURCE
/* Correctness only: guarded and exact-sized ranges, no timing. */
#include "zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/resource.h>

static unsigned long checks, guarded_checks, exact_checks, collision_checks;
static unsigned long external_guard_checks, null_rejections, expected_assertions;
static void expect(zbtScoreLeaf *leaf, uint32_t hash, const unsigned char *q,
                   size_t len, int found, unsigned pos) {
    for (unsigned mask = 0; mask < 4; mask++) {
        double score = 12345.0, wanted = -0.0;
        unsigned position = UINT_MAX;
        int actual = zbtScoreLeafFindMember(leaf, hash, q, len,
            mask & 1 ? &score : NULL, mask & 2 ? &position : NULL);
        serverAssert(actual == found);
        if (found && (mask & 1)) serverAssert(!memcmp(&score, &wanted, sizeof(score)));
        else serverAssert(score == 12345.0);
        serverAssert(position == (found && (mask & 2) ? pos : UINT_MAX));
        checks++;
    }
}
static void init_leaf(zbtScoreLeaf *leaf, unsigned count, int reversed) {
    memset(leaf, 0, offsetof(zbtScoreLeaf, data));
    leaf->n.isleaf = 1; leaf->n.count = count; leaf->n.subtree = count;
    leaf->score_base = zbtScoreToOrdered(-0.0); leaf->reversed = reversed;
}
static unsigned char *page_range(size_t page) {
    unsigned char *map = mmap(NULL, page * 3, PROT_NONE,
        MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    serverAssert(map != MAP_FAILED);
    serverAssert(mprotect(map + page, page, PROT_READ | PROT_WRITE) == 0);
    return map;
}
static void bytes(unsigned char *p, size_t n, unsigned pattern) {
    for (size_t i = 0; i < n; i++) p[i] = pattern == 0 ? 0 :
        (pattern == 1 ? 255 : (unsigned char)(i * 67));
}
static void compare_and_mismatch(zbtScoreLeaf *leaf, uint32_t hash,
                                 unsigned char *q, size_t n, unsigned pos) {
    expect(leaf, hash, q, n, 1, pos);
    for (size_t i = 0; i < n; i++) {
        q[i] ^= 128; expect(leaf, hash, q, n, 0, 0); q[i] ^= 128;
    }
}
static void guarded(void) {
    size_t page = (size_t)sysconf(_SC_PAGESIZE);
    serverAssert(page >= 4096 && page < UINT16_MAX);
    unsigned char *source = page_range(page), *query = page_range(page);
    for (unsigned n = 0; n < 320; n++) for (unsigned pattern = 0; pattern < 3; pattern++) {
        for (unsigned edge = 0; edge < 2; edge++) {
            zbtScoreLeaf *leaf = (zbtScoreLeaf *)(source + page);
            init_leaf(leaf, 1, 0);
            size_t header = n < 254 ? 1 : 3;
            unsigned char *record = source + page * 2 - n - header;
            unsigned char contents[320]; bytes(contents, n, pattern);
            zbtPackedWriteInline(record, contents, n);
            zbtScoreLeafOffsets(leaf)[0] = record - (unsigned char *)leaf;
            uint32_t hash = UINT32_C(0xffabcdef);
            zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
            /* n=0 uses a non-null one-past readable-range pointer; no NULL API claim. */
            unsigned char *q = edge ? query + page * 2 - n : query + page;
            bytes(q, n, pattern);
            unsigned long before = checks;
            compare_and_mismatch(leaf, hash, q, n, 0);
            guarded_checks += checks - before;
        }
    }
    serverAssert(munmap(source, page * 3) == 0);
    serverAssert(munmap(query, page * 3) == 0);
}
static void exact_ranges(void) {
    for (unsigned n = 0; n < 320; n++) for (unsigned sa = 0; sa < 8; sa++) {
        unsigned qa = (sa + 3) % 8;
        for (unsigned pattern = 0; pattern < 3; pattern++) {
            size_t off = 64 + sa, header = n < 254 ? 1 : 3;
            zbtScoreLeaf *leaf = malloc(off + header + n);
            unsigned char *allocation = malloc(qa + n + 1);
            serverAssert(leaf && allocation);
            init_leaf(leaf, 1, sa & 1);
            unsigned char *record = (unsigned char *)leaf + off;
            unsigned char *q = allocation + qa;
            bytes(q, n + 1, pattern); zbtPackedWriteInline(record, q, n);
            zbtScoreLeafOffsets(leaf)[0] = off;
            zbtScoreLeafHashTags(leaf)[0] = 0;
            unsigned long before = checks;
            compare_and_mismatch(leaf, UINT32_C(0x00abcdef), q, n, 0);
            if (n) expect(leaf, UINT32_C(0x00abcdef), q, n - 1, 0, 0);
            expect(leaf, UINT32_C(0x00abcdef), q, n + 1, 0, 0);
            exact_checks += checks - before;
            free(allocation); free(leaf);
        }
    }
}
static void external_record(unsigned char *record, unsigned char *data,
                            size_t n, uint32_t hash) {
    uint64_t length = n;
    record[0] = ZBT_PACKED_EXTERNAL;
    memcpy(record + ZBT_EXTERNAL_HASH_OFFSET, &hash, sizeof(hash));
    memcpy(record + ZBT_EXTERNAL_LENGTH_OFFSET, &length, sizeof(length));
    memcpy(record + ZBT_EXTERNAL_POINTER_OFFSET, &data, sizeof(data));
}
static void collisions(void) {
    for (unsigned n = 0; n <= 8; n++) for (unsigned reverse = 0; reverse < 2; reverse++) {
        for (unsigned tag = 0; tag <= 255; tag += 255) {
            unsigned char q[9]; bytes(q, sizeof(q), 2);
            zbtScoreLeaf *leaf = calloc(1, 4096); serverAssert(leaf);
            init_leaf(leaf, 5, reverse);
            uint32_t hash = ((uint32_t)tag << 24) | UINT32_C(0xabcdef);
            uint16_t *offsets = zbtScoreLeafOffsets(leaf);
            uint8_t *tags = zbtScoreLeafHashTags(leaf);
            for (unsigned i = 0; i < 5; i++) { offsets[i] = 128 + i * 32; tags[i] = tag; }
            unsigned char *base = (unsigned char *)leaf;
            /* Same-tag wrong full hash must reject before following this NULL pointer. */
            external_record(base + offsets[0], NULL, n, hash ^ 1);
            zbtPackedWriteInline(base + offsets[1], q, 9);
            zbtPackedWriteInline(base + offsets[2], q, n ? n - 1 : 1);
            zbtPackedWriteInline(base + offsets[3], q, n ? n : 1);
            if (n) base[offsets[3] + n] ^= 64;
            zbtPackedWriteInline(base + offsets[4], q, n);
            unsigned long before = checks;
            compare_and_mismatch(leaf, hash, q, n, reverse ? 0 : 4);
            tags[4] ^= 1; expect(leaf, hash, q, n, 0, 0);
            collision_checks += checks - before;
            free(leaf);
        }
    }
}
static void fallback(void) {
    const size_t lengths[] = {0, 1, 8, 9, 15, 16, 253, 254, 255, 256, 319, 320, 321, 384};
    for (unsigned i = 0; i < sizeof(lengths) / sizeof(lengths[0]); i++) {
        size_t n = lengths[i];
        unsigned char data[384], q[384]; bytes(data, n, 2); memcpy(q, data, n);
        zbtScoreLeaf *leaf = calloc(1, 4096); serverAssert(leaf);
        init_leaf(leaf, 1, 0);
        zbtScoreLeafOffsets(leaf)[0] = 128;
        uint32_t hash = UINT32_C(0xffabcdef); zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
        unsigned char *record = (unsigned char *)leaf + 128;
        if (n < ZBT_EXTERNAL_MEMBER_AT) {
            zbtPackedWriteInline(record, data, n);
            serverAssert(record[0] == (n < ZBT_PACKED_SHORT ? n : ZBT_PACKED_SHORT));
            compare_and_mismatch(leaf, hash, q, n, 0);
        }
        /* Also cover synthetic externally represented short values without weakening fallback. */
        external_record(record, data, n, hash);
        compare_and_mismatch(leaf, hash, q, n, 0);
        expect(leaf, hash ^ 1, q, n, 0, 0);
        free(leaf);
    }
    /* Empty and full synthetic leaves exercise the unchanged scanner bounds. */
    zbtScoreLeaf *leaf = calloc(1, 4096); serverAssert(leaf);
    init_leaf(leaf, 0, 0); unsigned char q[8] = {0}; expect(leaf, 0, q, 8, 0, 0);
    init_leaf(leaf, ZBT_SCORE_LEAF_MAX, 1);
    for (unsigned i = 0; i < ZBT_SCORE_LEAF_MAX; i++) {
        zbtScoreLeafOffsets(leaf)[i] = 512 + i * 9;
        zbtScoreLeafHashTags(leaf)[i] = 0;
        q[7] = i; zbtPackedWriteInline((unsigned char *)leaf + 512 + i * 9, q, 8);
    }
    compare_and_mismatch(leaf, 0, q, 8, 0);
    free(leaf);
}
static void external_guards(void) {
    const size_t lengths[] = {0, 1, 7, 8, 253, 254, 255, 256, 319, 320, 384};
    size_t page = (size_t)sysconf(_SC_PAGESIZE);
    unsigned char *source = page_range(page), *data = page_range(page), *query = page_range(page);
    zbtScoreLeaf *leaf = (zbtScoreLeaf *)(source + page);
    for (unsigned j = 0; j < sizeof(lengths) / sizeof(lengths[0]); j++) {
        size_t n = lengths[j];
        for (unsigned reversed = 0; reversed < 2; reversed++) {
            init_leaf(leaf, 1, reversed);
            unsigned char *record = source + page * 2 - ZBT_EXTERNAL_RECORD_BYTES;
            unsigned char *stored = data + page * 2 - n;
            unsigned char *q = query + page * 2 - n;
            bytes(stored, n, 2); bytes(q, n, 2);
            uint32_t hash = UINT32_C(0xffabcdef);
            zbtScoreLeafOffsets(leaf)[0] = record - (unsigned char *)leaf;
            zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
            external_record(record, stored, n, hash);
            unsigned long before = checks;
            compare_and_mismatch(leaf, hash, q, n, 0);
            if (n) expect(leaf, hash, q, n - 1, 0, 0);
            expect(leaf, hash ^ 1, q, n, 0, 0);
            external_guard_checks += checks - before;
            zbtExternalSetPointer(record, NULL);
            expect(leaf, hash ^ 1, q, n, 0, 0); null_rejections++;
        }
    }
    /* Only the marker and full hash are readable. A mismatching hash must
     * reject before any length/pointer field is touched. */
    init_leaf(leaf, 1, 0);
    unsigned char *record = source + page * 2 - 5;
    uint32_t hash = UINT32_C(0xffabcdef), wrong = hash ^ 1;
    record[0] = ZBT_PACKED_EXTERNAL;
    memcpy(record + 1, &wrong, sizeof(wrong));
    zbtScoreLeafOffsets(leaf)[0] = record - (unsigned char *)leaf;
    zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
    expect(leaf, hash, query + page * 2, 0, 0, 0); null_rejections++;
    /* Matching external hashes must still enforce the original nonnull
     * pointer assertion, even for zero length. Check the child's text. */
    record = source + page * 2 - ZBT_EXTERNAL_RECORD_BYTES;
    zbtScoreLeafOffsets(leaf)[0] = record - (unsigned char *)leaf;
    external_record(record, NULL, 0, hash);
    int pipefd[2]; serverAssert(pipe(pipefd) == 0);
    pid_t child = fork(); serverAssert(child >= 0);
    if (child == 0) {
        struct rlimit no_core = {0, 0}; serverAssert(setrlimit(RLIMIT_CORE, &no_core) == 0);
        close(pipefd[0]); serverAssert(dup2(pipefd[1], STDERR_FILENO) >= 0); close(pipefd[1]);
        zbtScoreLeafFindMember(leaf, hash, query + page * 2, 0, NULL, NULL);
        _exit(42);
    }
    close(pipefd[1]);
    char message[2048]; ssize_t size = read(pipefd[0], message, sizeof(message) - 1);
    serverAssert(size > 0); message[size] = 0; close(pipefd[0]);
    int status; serverAssert(waitpid(child, &status, 0) == child);
    serverAssert(WIFSIGNALED(status) && WTERMSIG(status) == SIGABRT);
    serverAssert(strstr(message, "ptr != NULL")); expected_assertions++;
    printf("{\"expected_assertion\":true,\"condition\":\"ptr != NULL\",\"signal\":%d}\n", SIGABRT);
    serverAssert(munmap(source, page * 3) == 0);
    serverAssert(munmap(data, page * 3) == 0);
    serverAssert(munmap(query, page * 3) == 0);
}
int main(void) {
    guarded(); exact_ranges(); collisions(); fallback(); external_guards();
    printf("{\"passed\":true,\"checks\":%lu,\"guarded_checks\":%lu,"
           "\"exact_checks\":%lu,\"collision_checks\":%lu,"
           "\"external_guard_checks\":%lu,\"null_rejections\":%lu,\"expected_assertions\":%lu}\n",
           checks, guarded_checks, exact_checks, collision_checks,
           external_guard_checks, null_rejections, expected_assertions);
    return 0;
}
