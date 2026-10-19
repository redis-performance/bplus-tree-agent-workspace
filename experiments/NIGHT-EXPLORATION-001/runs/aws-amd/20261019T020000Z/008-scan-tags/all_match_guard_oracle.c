#define _GNU_SOURCE 1
#include "../src/zset_btree.c"
#include <inttypes.h>
#include <sys/mman.h>
#include <unistd.h>

/* Independent byte reference, guarded input edges and untouched output slots. */
int main(void) {
    long pagesize = sysconf(_SC_PAGESIZE);
    serverAssert(pagesize >= 4096);
    unsigned char *region = mmap(NULL, (size_t)pagesize * 3, PROT_NONE,
                                MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    serverAssert(region != MAP_FAILED);
    serverAssert(mprotect(region + pagesize, pagesize, PROT_READ | PROT_WRITE) == 0);
    uint64_t checks = 0, positions = 0, zero_spans = 0;
    uint64_t digest = UINT64_C(14695981039346656037);
    for (unsigned edge = 0; edge < 2; edge++) {
        for (unsigned pattern = 0; pattern < 3; pattern++) {
            for (unsigned count = 0; count <= ZBT_SCORE_LEAF_MAX; count++) {
                unsigned char *tags = edge ? region + pagesize * 2 - count : region + pagesize;
                for (unsigned i = 0; i < count; i++) {
                    tags[i] = pattern == 0 ? 0 : pattern == 1 ? 17 :
                        (unsigned char)((i % 5 == 0) ? 0 : (i % 5 == 1) ? 1 : i * 73);
                }
                for (unsigned tag = 0; tag < 256; tag++) {
                    for (unsigned reversed = 0; reversed < 2; reversed++) {
                        unsigned int expected[ZBT_SCORE_LEAF_MAX];
                        unsigned int actual[ZBT_SCORE_LEAF_MAX + 2];
                        const unsigned int canary = 0xa5c3e17bU;
                        unsigned int want = 0;
                        for (unsigned i = 0; i < ZBT_SCORE_LEAF_MAX + 2; i++) actual[i] = canary;
                        for (unsigned i = 0; i < count; i++) {
                            if (tags[i] == tag || (tag == 1 && tags[i] == 0))
                                expected[want++] = reversed ? count - 1 - i : i;
                        }
                        unsigned int got = zbtLeafTagMatches(tags, count, reversed,
                                                            (uint8_t)tag, actual + 1);
                        serverAssert(got == want && actual[0] == canary);
                        for (unsigned i = 0; i < got; i++) {
                            serverAssert(actual[i + 1] == expected[i]);
                            digest = (digest ^ actual[i + 1]) * UINT64_C(1099511628211);
                        }
                        for (unsigned i = got + 1; i < ZBT_SCORE_LEAF_MAX + 2; i++)
                            serverAssert(actual[i] == canary);
                        checks++; positions += got; zero_spans += count == 0;
                    }
                }
            }
        }
    }
    serverAssert(munmap(region, (size_t)pagesize * 3) == 0);
    printf("PASS checks=%" PRIu64 " positions=%" PRIu64 " zero_spans=%" PRIu64
           " digest=%016" PRIx64 "\n", checks, positions, zero_spans, digest);
    return 0;
}
