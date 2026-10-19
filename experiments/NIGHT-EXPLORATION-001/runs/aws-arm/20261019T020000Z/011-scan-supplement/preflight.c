/* Baseline-only structural diagnostic. Includes unmodified tree, never timed.
 * Private state is READ ONLY; every fixture change uses the public API. */
#define _GNU_SOURCE
#include "zset_btree.c"
#include <inttypes.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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
  uint64_t leaves, members, reversed_leaves, reversed_members, external,
      short_records, long_records, old_live, new_live, old_leaves, new_leaves,
      old_used, new_used, old_size, new_size, wide_old, wide_new, rehash;
  uint64_t tags[256];
} census;
static census inspect(zbtreeSet *t) {
  census c = {0};
  c.rehash = t->member_rehash != NULL;
  c.old_used = t->member_index.used;
  c.old_size = t->member_index.size;
  c.wide_old = t->member_index.wide_ids;
  if (c.rehash) {
    c.new_used = t->member_rehash->table.used;
    c.new_size = t->member_rehash->table.size;
    c.wide_new = t->member_rehash->table.wide_ids;
  }
  for (zbtScoreLeaf *l = t->score_first; l; l = l->next) {
    c.leaves++;
    c.members += l->n.count;
    c.reversed_leaves += !!l->reversed;
    c.reversed_members += l->reversed ? l->n.count : 0;
    int migrated = c.rehash && zbtIndexLeafMigrated(t, l);
    if (migrated) {
      c.new_live += l->n.count;
      c.new_leaves++;
    } else {
      c.old_live += l->n.count;
      c.old_leaves++;
    }
    for (unsigned i = 0; i < l->n.count; i++) {
      size_t len;
      const unsigned char *s = zbtScoreLeafElement(l, i, &len);
      uint8_t tag = (uint32_t)dictGenHashFunction(s, len) >> 24;
      CHECK(zbtScoreLeafHashTags(l)[zbtScoreLeafPhysicalPos(l, i)] == tag);
      c.tags[tag]++;
      unsigned char kind = zbtScoreLeafRecord(l, i)[0];
      c.external += kind == ZBT_PACKED_EXTERNAL;
      c.long_records += kind == ZBT_PACKED_SHORT;
      c.short_records += kind < ZBT_PACKED_SHORT;
    }
  }
  CHECK(c.members == zbtreeLength(t));
  return c;
}
typedef struct {
  sds *keys;
  size_t n, width;
  unsigned mode;
  unsigned char *seen;
  uint64_t callbacks, checksum;
} oracle;
static void callback(void *v, const unsigned char *s, size_t len, double d) {
  oracle *o = v;
  CHECK(len == o->width);
  uint64_t id = get64(s);
  CHECK(id < o->n);
  CHECK(!memcmp(s, o->keys[id], len));
  CHECK(bits(d) == bits(score(id, o->mode)));
  o->seen[id] = 1;
  o->callbacks++;
  o->checksum += id ^ bits(d) ^ ((uint64_t)len * UINT64_C(0x9e3779b97f4a7c15));
}
static oracle validate(zbtreeSet *t, sds *keys, size_t n, size_t width,
                       unsigned mode) {
  oracle o = {
      .keys = keys, .n = n, .width = width, .mode = mode, .seen = calloc(n, 1)};
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
int main(int argc, char **argv) {
  CHECK(argc == 7);
  const char *history = argv[1];
  size_t requested = strtoull(argv[2], NULL, 10),
         width = strtoull(argv[3], NULL, 10);
  uint64_t seed = strtoull(argv[4], NULL, 10);
  unsigned mode = strtoul(argv[5], NULL, 10);
  size_t maximum = strtoull(argv[6], NULL, 10);
  CHECK(width >= 8 && width <= 1024 && mode <= 2 && requested > 0 &&
        maximum >= requested && maximum <= 100000);
  int resize = !strcmp(history, "resize"), trim = !strcmp(history, "trim");
  CHECK(resize || trim || !strcmp(history, "ascending"));
  uint8_t hs[16];
  uint64_t rng = seed ^ UINT64_C(0x382cfe7495a610bd);
  put64(hs, mix(&rng));
  put64(hs + 8, mix(&rng));
  dictSetHashFunctionSeed(hs);
  sds *keys = calloc(maximum, sizeof(*keys));
  CHECK(keys);
  zbtreeSet *t = zbtreeCreate();
  CHECK(t);
  sds sentinel = NULL;
  if (resize)
    zbtreeReserve(t, requested);
  if (trim) {
    unsigned char bytes[8];
    memset(bytes, 255, 8);
    sentinel = sdsnewlen(bytes, 8);
    double d = nextafter(score(0, mode), -INFINITY);
    CHECK(isfinite(d) && d < score(0, mode));
    insert(t, sentinel, d);
  }
  size_t n = 0;
  int supported = 0;
  for (; n < (resize ? maximum : requested);) {
    keys[n] = key(n, width, seed);
    insert(t, keys[n], score(n, mode));
    n++;
    if (resize && n >= requested && t->member_rehash) {
      census c = inspect(t);
      if (c.rehash && c.old_live > 0 && c.new_live > 0 && c.new_live < n / 2) {
        supported = 1;
        break;
      }
    }
  }
  if (trim)
    zbtreeDeleteEdge(t, 0);
  if (sentinel)
    sdsfree(sentinel);
  census before = inspect(t);
  if (!resize)
    supported = trim ? (before.leaves == 1 && before.reversed_members == n)
                     : (before.reversed_members == 0);
  size_t owned = zbtreeAllocSize(t);
  oracle o = validate(t, keys, n, width, mode);
  census after = inspect(t);
  CHECK(!memcmp(&before, &after, sizeof(census)));
  CHECK(zbtreeAllocSize(t) == owned);
  printf("{\"history\":\"%s\",\"requested\":%zu,\"n\":%zu,\"bytes\":%zu,"
         "\"seed\":%" PRIu64 ",\"mode\":%u,\"supported\":%s,\"leaves\":%" PRIu64
         ",\"reversed_leaves\":%" PRIu64 ",\"reversed_members\":%" PRIu64
         ",\"external\":%" PRIu64 ",\"short_records\":%" PRIu64
         ",\"long_records\":%" PRIu64
         ",\"active_rehash\":%s,\"old_live\":%" PRIu64 ",\"new_live\":%" PRIu64
         ",\"old_leaves\":%" PRIu64 ",\"new_leaves\":%" PRIu64
         ",\"old_used\":%" PRIu64 ",\"new_used\":%" PRIu64
         ",\"old_size\":%" PRIu64 ",\"new_size\":%" PRIu64
         ",\"wide_old\":%" PRIu64 ",\"wide_new\":%" PRIu64
         ",\"tree_bytes\":%zu,\"callbacks\":%" PRIu64
         ",\"checksum\":\"%016" PRIx64 "\",\"validation\":\"pass\"}\n",
         history, requested, n, width, seed, mode, supported ? "true" : "false",
         before.leaves, before.reversed_leaves, before.reversed_members,
         before.external, before.short_records, before.long_records,
         before.rehash ? "true" : "false", before.old_live, before.new_live,
         before.old_leaves, before.new_leaves, before.old_used, before.new_used,
         before.old_size, before.new_size, before.wide_old, before.wide_new,
         owned, o.callbacks, o.checksum);
  zbtreeFree(t);
  for (size_t i = 0; i < n; i++)
    sdsfree(keys[i]);
  free(keys);
  return supported ? 0 : 3;
}
