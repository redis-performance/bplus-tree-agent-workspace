/* Separate-TU public-API supplemental referee. Private census is
 * diagnostic-only. */
#define _GNU_SOURCE
#include "census.h"
#include "server.h"
#include "zset_btree.h"
#include <errno.h>
#include <inttypes.h>
#include <math.h>
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
static void require(int ok, const char *s) {
  if (!ok) {
    fprintf(stderr, "preflight: %s\n", s);
    exit(2);
  }
}
#define CHECK(x) require(!!(x), #x)
static uint64_t mix(uint64_t *s) {
  uint64_t z = (*s += UINT64_C(0x9e3779b97f4a7c15));
  z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
  z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
  return z ^ (z >> 31);
}
static void put64(unsigned char *p, uint64_t x) {
  for (int j = 7; j >= 0; j--) {
    p[j] = (unsigned char)x;
    x >>= 8;
  }
}
static uint64_t get64(const unsigned char *p) {
  uint64_t x = 0;
  for (int j = 0; j < 8; j++)
    x = (x << 8) | p[j];
  return x;
}
static uint64_t bits(double x) {
  uint64_t b;
  memcpy(&b, &x, 8);
  return b;
}
static double score(size_t id, unsigned mode) {
  return mode == 0   ? (double)id + 0.25
         : mode == 1 ? 0.25
                     : (id & 1 ? -0.0 : 0.0);
}
static sds key(size_t id, size_t width, uint64_t seed) {
  sds s = sdsnewlen(NULL, width);
  CHECK(s);
  put64((unsigned char *)s, id);
  for (size_t j = 8; j < width; j++)
    s[j] = (char)((id * 37 + seed * 13 + j * 19) & 255);
  if (width > 8)
    s[8] = 0;
  return s;
}
static void insert(zbtreeSet *t, sds s, double d) {
  zbtreeInsertPosition p;
  double old;
  CHECK(!zbtreeFindForAdd(t, s, &old, &p));
  zbtreeInsertNew(t, d, s, &p);
}
typedef struct {
  sds *keys;
  size_t n, width;
  unsigned mode;
  unsigned char *seen;
  uint64_t callbacks, checksum;
  unsigned fault;
} oracle;
static void callback(void *v, const unsigned char *s, size_t len, double d) {
  oracle *o = v;
  unsigned char damaged[1024];
  if (o->fault == 1)
    d += 1.0;
  if (o->fault == 2)
    len--;
  if (o->fault == 4) {
    CHECK(len <= sizeof(damaged));
    memcpy(damaged, s, len);
    damaged[len - 1] ^= 1;
    s = damaged;
  }
  CHECK(len == o->width);
  uint64_t id = get64(s);
  CHECK(id < o->n);
  if (o->fault == 3 && id == 0)
    return;
  if (o->fault == 7 && (id & 1))
    d = 0.0;
  CHECK(!memcmp(s, o->keys[id], len));
  CHECK(bits(d) == bits(score(id, o->mode)));
  o->seen[id] = 1;
  o->callbacks++;
  o->checksum += id ^ bits(d) ^ ((uint64_t)len * UINT64_C(0x9e3779b97f4a7c15));
}
static oracle validate(zbtreeSet *t, sds *keys, size_t n, size_t width,
                       unsigned mode, unsigned fault) {
  oracle o = {.keys = keys,
              .n = n,
              .width = width,
              .mode = mode,
              .seen = calloc(n, 1),
              .fault = fault};
  CHECK(o.seen);
  uint64_t cursor = 0, calls = 0;
  do {
    cursor = zbtreeScan(t, cursor, 64, callback, &o);
    CHECK(++calls < 1000000);
  } while (cursor);
  for (size_t id = 0; id < n; id++)
    CHECK(o.seen[id]);
  free(o.seen);
  o.seen = NULL;
  zbtreeIterator it;
  CHECK(zbtreeIteratorStart(t, 0, &it));
  for (size_t id = 0; id < n; id++) {
    const unsigned char *s;
    size_t len;
    double d;
    CHECK(zbtreeIteratorNext(&it, 0, &s, &len, &d));
    CHECK(len == width && !memcmp(s, keys[id], len));
    CHECK(bits(d) == bits(score(id, mode)));
  }
  CHECK(!zbtreeIteratorNext(&it, 0, NULL, NULL, NULL));
  return o;
}

static uint64_t number(const char *s) {
  char *end;
  errno = 0;
  uint64_t x = strtoull(s, &end, 10);
  CHECK(!errno && *s && !*end && s[0] != '-');
  return x;
}
static uint64_t clock_ns(clockid_t clock) {
  struct timespec t;
  CHECK(!clock_gettime(clock, &t));
  return (uint64_t)t.tv_sec * 1000000000 + t.tv_nsec;
}
typedef struct {
  uint64_t callbacks, checksum;
} result;
static void consume(void *v, const unsigned char *s, size_t len, double d) {
  result *r = v;
  r->callbacks++;
  r->checksum +=
      get64(s) ^ bits(d) ^ ((uint64_t)len * UINT64_C(0x9e3779b97f4a7c15));
}
static void traverse(zbtreeSet *t, zbtreeScanFunction *fn, void *context) {
  uint64_t cursor = 0, calls = 0;
  do {
    cursor = zbtreeScan(t, cursor, 64, fn, context);
    CHECK(++calls < 1000000);
  } while (cursor);
}
int main(int argc, char **argv) {
  CHECK(argc == 8 && !strcmp(argv[1], "run"));
  const char *history = argv[2];
  int resize = !strcmp(history, "resize"), trim = !strcmp(history, "trim");
  CHECK(resize || trim);
  size_t width = number(argv[3]);
  uint64_t seed = number(argv[4]);
  unsigned mode = number(argv[5]);
  uint64_t passes = number(argv[6]);
  unsigned fault = number(argv[7]);
  CHECK((width == 8 || width == 319 || width == 320 || width == 321 ||
         width == 1024) &&
        mode <= 2 && passes <= 10000000 && fault <= 7);
  CHECK(fault != 7 || mode == 2);
  CHECK(fault != 5 || trim);
  CHECK(fault != 6 || resize);
#ifdef SCAN_CENSUS
  CHECK(passes == 0);
#else
  CHECK(fault != 5 &&
        fault != 6); /* Structural negative controls require actual census. */
#endif
  size_t n = resize ? 7169 : width == 319 ? 7 : 31;
  uint8_t hs[16];
  uint64_t rng = seed ^ UINT64_C(0x382cfe7495a610bd);
  put64(hs, mix(&rng));
  put64(hs + 8, mix(&rng));
  dictSetHashFunctionSeed(hs);
  sds *keys = calloc(n, sizeof(*keys));
  CHECK(keys);
  zbtreeSet *t = zbtreeCreate();
  CHECK(t);
  if (resize)
    zbtreeReserve(t, 4096);
  sds sentinel = NULL;
  if (trim && fault != 5) {
    unsigned char bytes[8];
    memset(bytes, 255, 8);
    sentinel = sdsnewlen(bytes, 8);
    double d = nextafter(score(0, mode), -INFINITY);
    CHECK(isfinite(d) && d < score(0, mode));
    insert(t, sentinel, d);
  }
  for (size_t id = 0; id < n; id++) {
    keys[id] = key(id, width, seed);
    insert(t, keys[id], score(id, mode));
  }
  if (trim && fault != 5) {
    zbtreeDeleteEdge(t, 0);
    sdsfree(sentinel);
  }
  if (fault == 6) {
    /* Fixed public lookup sweep completes migration without changing the model. */
    for (size_t id = 0; id < n; id++) {
      double d;
      CHECK(zbtreeScore(t, keys[id], &d));
      CHECK(bits(d) == bits(score(id, mode)));
    }
  }
#ifdef SCAN_CENSUS
  census before = supplement_census(t);
  if (trim)
    CHECK(before.members == n && before.leaves == 1 &&
          before.reversed_members == n);
  if (resize)
    CHECK(before.rehash && before.old_live > 0 && before.new_live > 0 &&
          before.new_live < n / 2 && before.old_live + before.new_live == n);
  supplement_print_census(&before);
#endif
  size_t owned = zbtreeAllocSize(t);
  oracle expected = validate(t, keys, n, width, mode, fault);
  result got = {0};
  uint64_t elapsed = 0, thread_elapsed = 0;
  int start_cpu = -1, end_cpu = -1;
  {
    for (int warm = 0; warm < 2; warm++) {
      result r = {0};
      traverse(t, consume, &r);
      CHECK(r.callbacks == expected.callbacks &&
            r.checksum == expected.checksum);
    }
  }
  if (passes) {
    start_cpu = sched_getcpu();
    uint64_t cpu = clock_ns(CLOCK_THREAD_CPUTIME_ID),
             start = clock_ns(CLOCK_MONOTONIC);
    for (uint64_t pass = 0; pass < passes; pass++)
      traverse(t, consume, &got);
    elapsed = clock_ns(CLOCK_MONOTONIC) - start;
    thread_elapsed = clock_ns(CLOCK_THREAD_CPUTIME_ID) - cpu;
    end_cpu = sched_getcpu();
    CHECK(got.callbacks == expected.callbacks * passes &&
          got.checksum == expected.checksum * passes);
  }
  oracle after = validate(t, keys, n, width, mode, 0);
  CHECK(after.callbacks == expected.callbacks &&
        after.checksum == expected.checksum && zbtreeAllocSize(t) == owned);
#ifdef SCAN_CENSUS
  census final = supplement_census(t);
  CHECK(!memcmp(&before, &final, sizeof(census)));
#endif
  printf("{\"kind\":\"run\",\"history\":\"%s\",\"n\":%zu,\"bytes\":%zu,"
         "\"seed\":%" PRIu64 ",\"encoding\":%u,\"passes\":%" PRIu64
         ",\"logical_members\":%" PRIu64 ",\"callbacks_per_pass\":%" PRIu64
         ",\"checksum_per_pass\":\"%016" PRIx64
         "\",\"tree_bytes\":%zu,\"elapsed_ns\":%" PRIu64
         ",\"thread_elapsed_ns\":%" PRIu64
         ",\"start_cpu\":%d,\"end_cpu\":%d,\"warmup_passes\":2,\"prepost_oracles\":2,\"warmup_callback_parity\":true,\"validation\":\"pass\"}\n",
         history, n, width, seed, mode, passes, n * passes, expected.callbacks,
         expected.checksum, owned, elapsed, thread_elapsed, start_cpu, end_cpu);
  zbtreeFree(t);
  for (size_t i = 0; i < n; i++)
    sdsfree(keys[i]);
  free(keys);
  return 0;
}
