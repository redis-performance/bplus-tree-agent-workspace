/* libc allocation, upstream SipHash, and the three SDS constructors needed here. */
#include "server.h"
#include <string.h>
#ifdef __APPLE__
#include <malloc/malloc.h>
#elif defined(__linux__)
#include <malloc.h>
#else
#error "Allocator usable-size adapter currently supports macOS and Linux"
#endif

/* Identity-only sentinels for unbounded lexicographical seeks; never free. */
static char min_sentinel, max_sentinel;
struct standalone_shared shared = { &min_sentinel, &max_sentinel };

_Noreturn void standalone_panic(const char *file, int line, const char *message) {
    fprintf(stderr, "%s:%d: %s\n", file, line, message);
    abort();
}

size_t zmalloc_usable_size(void *ptr) {
    if (!ptr) return 0;
#ifdef __APPLE__
    return malloc_size(ptr);
#else
    return malloc_usable_size(ptr);
#endif
}
void *zmalloc(size_t size) {
    void *p = malloc(size ? size : 1);
    serverAssert(p != NULL);
    return p;
}
void *zcalloc(size_t size) {
    void *p = calloc(1, size ? size : 1);
    serverAssert(p != NULL);
    return p;
}
void zfree(void *ptr) { free(ptr); }
void *zmalloc_usable(size_t size, size_t *usable) {
    void *p = zmalloc(size);
    *usable = zmalloc_usable_size(p);
    return p;
}
void *zrealloc_usable(void *ptr, size_t size, size_t *usable, size_t *old_usable) {
    *old_usable = zmalloc_usable_size(ptr);
    void *p = realloc(ptr, size ? size : 1);
    serverAssert(p != NULL);
    *usable = zmalloc_usable_size(p);
    return p;
}
void zfree_usable(void *ptr, size_t *usable) {
    *usable = zmalloc_usable_size(ptr);
    free(ptr);
}

uint64_t siphash(const uint8_t *, size_t, const uint8_t *);
static uint8_t hash_seed[16];
void dictSetHashFunctionSeed(uint8_t *seed) { memcpy(hash_seed, seed, sizeof(hash_seed)); }
uint64_t dictGenHashFunction(const void *key, size_t len) { return siphash(key, len, hash_seed); }

/* Fork-child page dismissal is outside the standalone API under test. */
void dismissMemory(void *ptr, size_t size) { UNUSED(ptr); UNUSED(size); }

/* Fixture strings use the upstream SDS64 layout. The tree copies member bytes. */
sds sdsnewlen(const void *init, size_t len) {
    serverAssert(len <= SIZE_MAX - sizeof(struct sdshdr64) - 1);
    struct sdshdr64 *h = zmalloc(sizeof(*h) + len + 1);
    h->len = len;
    h->alloc = len;
    h->flags = SDS_TYPE_64;
    if (init) memcpy(h->buf, init, len);
    else memset(h->buf, 0, len);
    h->buf[len] = '\0';
    return h->buf;
}
sds sdsnew(const char *init) { return sdsnewlen(init, init ? strlen(init) : 0); }
void sdsfree(sds s) {
    if (!s) return;
    serverAssert((s[-1] & SDS_TYPE_MASK) == SDS_TYPE_64);
    free(s - sizeof(struct sdshdr64));
}
