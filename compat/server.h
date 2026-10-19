/* Standalone host adapter; no Redis server is linked. */
#ifndef BPLUS_STANDALONE_SERVER_H
#define BPLUS_STANDALONE_SERVER_H
#include <stdint.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "sds.h"
struct standalone_shared { sds minstring, maxstring; };
extern struct standalone_shared shared;

#define UNUSED(x) ((void)(x))
_Noreturn void standalone_panic(const char *file, int line, const char *message);
#define serverAssert(x) do { if (!(x)) standalone_panic(__FILE__, __LINE__, #x); } while (0)
#define serverPanic(msg) standalone_panic(__FILE__, __LINE__, (msg))
#ifdef REDIS_DEBUG
#define debugServerAssert(x) serverAssert(x)
#else
#define debugServerAssert(x) ((void)0)
#endif
#define redis_prefetch_read(p) __builtin_prefetch((p), 0, 3)
#define redis_prefetch_write(p) __builtin_prefetch((p), 1, 3)
#if __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__
#define intrev64ifbe(v) __builtin_bswap64(v)
#else
#define intrev64ifbe(v) (v)
#endif

void *zmalloc(size_t size);
void *zcalloc(size_t size);
void zfree(void *ptr);
size_t zmalloc_usable_size(void *ptr);
void *zmalloc_usable(size_t size, size_t *usable);
void *zrealloc_usable(void *ptr, size_t size, size_t *usable, size_t *old_usable);
void zfree_usable(void *ptr, size_t *usable);
uint64_t dictGenHashFunction(const void *key, size_t len);
void dictSetHashFunctionSeed(uint8_t *seed);
void dismissMemory(void *ptr, size_t size);
#endif
