#define _GNU_SOURCE
/* Correctness only: exact allocations, protected pages and forced collisions. */
#include "zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
static unsigned long checks;

static void expect(zbtScoreLeaf *leaf, uint32_t hash, const unsigned char *query,
                   size_t len, int present, unsigned int physical) {
    for (unsigned int mask = 0; mask < 4; mask++) {
        double score = -123.0;
        unsigned int pos = UINT_MAX;
        int found = zbtScoreLeafFindMember(leaf, hash, query, len,
                                          mask & 1 ? &score : NULL,
                                          mask & 2 ? &pos : NULL);
        serverAssert(found == present);
        serverAssert(score == (present && (mask & 1) ? 42.0 : -123.0));
        unsigned int wanted = present && (mask & 2) ?
            zbtScoreLeafPhysicalPos(leaf, physical) : UINT_MAX;
        serverAssert(pos == wanted);
        checks++;
    }
}

static void init_leaf(zbtScoreLeaf *leaf, unsigned int count) {
    memset(leaf, 0, offsetof(zbtScoreLeaf, data) + count * 3);
    leaf->n.isleaf = 1;
    leaf->n.count = count;
    leaf->n.subtree = count;
    leaf->score_base = zbtScoreToOrdered(42.0);
}

static void record(zbtScoreLeaf *leaf, unsigned int slot, size_t offset,
                   const unsigned char *bytes, size_t len, uint32_t hash) {
    serverAssert(offset <= UINT16_MAX);
    zbtScoreLeafOffsets(leaf)[slot] = offset;
    zbtScoreLeafHashTags(leaf)[slot] = hash >> 24;
    zbtPackedWriteInline((unsigned char *)leaf + offset, bytes, len);
}

static void external_record(zbtScoreLeaf *leaf, unsigned char *bytes,
                            size_t len, uint32_t hash) {
    unsigned char *r = (unsigned char *)leaf + 128;
    zbtScoreLeafOffsets(leaf)[0] = 128;
    zbtScoreLeafHashTags(leaf)[0] = hash >> 24;
    r[0] = ZBT_PACKED_EXTERNAL;
    uint64_t stored_len = len;
    memcpy(r + ZBT_EXTERNAL_HASH_OFFSET, &hash, sizeof(hash));
    memcpy(r + ZBT_EXTERNAL_LENGTH_OFFSET, &stored_len, sizeof(stored_len));
    memcpy(r + ZBT_EXTERNAL_POINTER_OFFSET, &bytes, sizeof(bytes));
}

int main(void) {
    size_t page = sysconf(_SC_PAGESIZE);
    serverAssert(page >= 4096 && page <= UINT16_MAX);
    unsigned char *lm = mmap(NULL, 3 * page, PROT_NONE,
                             MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    unsigned char *qm = mmap(NULL, 3 * page, PROT_NONE,
                             MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    serverAssert(lm != MAP_FAILED && qm != MAP_FAILED);
    serverAssert(mprotect(lm + page, page, PROT_READ | PROT_WRITE) == 0);
    serverAssert(mprotect(qm + page, page, PROT_READ | PROT_WRITE) == 0);
    zbtScoreLeaf *guard = (zbtScoreLeaf *)(lm + page);
    size_t lengths[258];
    for (unsigned i = 0; i < 254; i++) lengths[i] = i;
    lengths[254] = 254; lengths[255] = 255; lengths[256] = 256; lengths[257] = 319;
    unsigned char bytes[384];
    for (unsigned int pattern = 0; pattern < 2; pattern++) {
        for (size_t i = 0; i < sizeof(bytes); i++)
            bytes[i] = pattern ? (unsigned char)(i * 97) : 0;
        for (unsigned int tag = 0; tag < 2; tag++) {
            uint32_t hash = (tag ? UINT32_C(0xff000000) : 0) | 0x1234;
            for (size_t k = 0; k < sizeof(lengths)/sizeof(*lengths); k++) {
                size_t n = lengths[k];
                init_leaf(guard, 1);
                record(guard, 0, page - n - zbtPackedLengthBytes(n), bytes, n, hash);
                expect(guard, hash, bytes, n + 1, 0, 0);
                if (n) expect(guard, hash, bytes, n - 1, 0, 0);
                for (unsigned int edge = 0; edge < 2; edge++) {
                    unsigned char *query = edge ? qm + 2 * page - n : qm + page;
                    if (n) memcpy(query, bytes, n);
                    expect(guard, hash, query, n, 1, 0);
                    for (size_t j = 0; j < n; j++) {
                        query[j] ^= 0x80;
                        expect(guard, hash, query, n, 0, 0);
                        query[j] ^= 0x80;
                    }
                }
            }
            for (size_t n = 0; n <= 8; n++) {
                /* Exact allocation end catches overread under ASan. Vary both
                 * starts independently to cover every modulo16 alignment. */
                for (size_t a = 0; a < 16; a++) for (size_t b = 0; b < 16; b++) {
                    size_t off = 128 + a;
                    zbtScoreLeaf *leaf = malloc(off + n + 1);
                    unsigned char *storage = malloc(b + n + 1);
                    unsigned char *query = storage + b + 1;
                    init_leaf(leaf, 1);
                    record(leaf, 0, off, bytes, n, hash);
                    if (n) memcpy(query, bytes, n);
                    expect(leaf, hash, query, n, 1, 0);
                    for (size_t j = 0; j < n; j++) {
                        query[j] ^= 1;
                        expect(leaf, hash, query, n, 0, 0);
                        query[j] ^= 1;
                    }
                    free(storage);
                    free(leaf);
                }
                /* Three same-tag candidates: generic mismatch, short
                 * mismatch, exact match. Equality must decide every hit. */
                init_leaf(guard, 3);
                record(guard, 0, 128, bytes, 9, hash);
                record(guard, 1, 160, bytes, n ? n : 1, hash);
                ((unsigned char *)guard)[161] ^= 1;
                record(guard, 2, 192, bytes, n, hash);
                for (unsigned int reversed = 0; reversed < 2; reversed++) {
                    guard->reversed = reversed;
                    expect(guard, hash, bytes, n, 1, 2);
                    if (n) {
                        unsigned char absent[8];
                        memcpy(absent, bytes, n);
                        absent[n - 1] ^= 0x40;
                        expect(guard, hash, absent, n, 0, 0);
                    }
                }
                /* Artificial external short representation: fallback must
                 * work, and a full-hash mismatch with the same tag must fail. */
                init_leaf(guard, 1);
                external_record(guard, bytes, n, hash);
                expect(guard, hash, bytes, n, 1, 0);
                expect(guard, hash ^ 1, bytes, n, 0, 0);
                /* Moved-out pointer is never inspected after hash rejection. */
                external_record(guard, NULL, n, hash);
                expect(guard, hash ^ 1, bytes, n, 0, 0);
            }
            for (size_t n = 320; n <= 384; n += 64) {
                init_leaf(guard, 1);
                external_record(guard, bytes, n, hash);
                expect(guard, hash, bytes, n, 1, 0);
                expect(guard, hash ^ 1, bytes, n, 0, 0);
            }
        }
    }
    munmap(lm, 3 * page);
    munmap(qm, 3 * page);
    printf("{\"passed\":true,\"checks\":%lu,\"guard_pages\":true,"
           "\"alignments_per_input\":16,\"ordinary_headers\":254}\n", checks);
    return 0;
}
