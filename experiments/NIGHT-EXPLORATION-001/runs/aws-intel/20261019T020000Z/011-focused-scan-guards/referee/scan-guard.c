#define _GNU_SOURCE
#include "server.h"
#include "zset_btree.h"
#include <errno.h>
#include <inttypes.h>
#include <sched.h>
#include <string.h>
#include <time.h>

/* Referee model is independent of tree contents. No private source is included.
 */
static uint64_t mix(uint64_t *s) {
  uint64_t z = (*s += UINT64_C(0x9e3779b97f4a7c15));
  z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
  z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
  return z ^ (z >> 31);
}
static void fail(const char *s) {
  fprintf(stderr, "scan-guard: %s\n", s);
  exit(2);
}
#define CHECK(x)                                                               \
  do {                                                                         \
    if (!(x))                                                                  \
      fail(#x);                                                                \
  } while (0)
static uint64_t number(const char *s) {
  char *e;
  errno = 0;
  unsigned long long x = strtoull(s, &e, 10);
  CHECK(!errno && *s && !*e && s[0] != '-');
  return x;
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
static void write64(FILE *f, uint64_t x) {
  unsigned char p[8];
  put64(p, x);
  CHECK(fwrite(p, 1, 8, f) == 8);
}
static uint64_t read64(FILE *f) {
  unsigned char p[8];
  CHECK(fread(p, 1, 8, f) == 8);
  return get64(p);
}
static void hash_seed(uint64_t seed) {
  uint8_t bytes[16];
  uint64_t s = seed ^ UINT64_C(0xa82310b52e97c641);
  put64(bytes, mix(&s));
  put64(bytes + 8, mix(&s));
  dictSetHashFunctionSeed(bytes);
}
static void key_fill(unsigned char *p, size_t len, uint64_t id, uint64_t nonce,
                     uint64_t seed) {
  put64(p, id);
  put64(p + 8, nonce);
  for (size_t j = 16; j < len; j++)
    p[j] = (unsigned char)((id * 37 + seed * 13 + j * 19) & 255);
  if (len > 16)
    p[16] = 0;
}
static unsigned tag(const unsigned char *p, size_t len) {
  return (uint32_t)dictGenHashFunction(p, len) >> 24;
}
static int matches(unsigned t, unsigned dist) {
  return dist == 0 || (dist == 1 ? t == 17 : t <= 1);
}
static double expected_score(size_t id, int order) {
  return order == 2 ? 0.25 : (double)id + 0.25;
}
static uint64_t score_bits(double d) {
  uint64_t u;
  memcpy(&u, &d, 8);
  return u;
}
typedef struct {
  size_t n, len;
  uint64_t seed;
  unsigned dist;
  uint32_t *nonces;
  sds *keys;
} fixture;
static fixture load(const char *path) {
  fixture f = {0};
  FILE *in = fopen(path, "rb");
  CHECK(in);
  unsigned char magic[8];
  CHECK(fread(magic, 1, 8, in) == 8 && !memcmp(magic, "SCANG001", 8));
  f.n = read64(in);
  f.len = read64(in);
  f.seed = read64(in);
  f.dist = read64(in);
  CHECK(f.n && f.n <= 100000 && f.len >= 16 && f.len <= 1024 && f.dist <= 2);
  f.nonces = calloc(f.n, sizeof(*f.nonces));
  f.keys = calloc(f.n, sizeof(*f.keys));
  CHECK(f.nonces && f.keys);
  hash_seed(f.seed);
  for (size_t i = 0; i < f.n; i++) {
    unsigned char b[4];
    CHECK(fread(b, 1, 4, in) == 4);
    f.nonces[i] = ((uint32_t)b[0] << 24) | ((uint32_t)b[1] << 16) |
                  ((uint32_t)b[2] << 8) | b[3];
    f.keys[i] = sdsnewlen(NULL, f.len);
    CHECK(f.keys[i]);
    key_fill((unsigned char *)f.keys[i], f.len, i, f.nonces[i], f.seed);
    CHECK(matches(tag((unsigned char *)f.keys[i], f.len), f.dist));
  }
  CHECK(fgetc(in) == EOF);
  CHECK(!ferror(in) && !fclose(in));
  return f;
}
static void generate(const char *path, size_t n, size_t len, uint64_t seed,
                     unsigned dist) {
  CHECK(n && n <= 100000 && len >= 16 && len <= 1024 && dist <= 2);
  hash_seed(seed);
  unsigned char *key = malloc(len);
  CHECK(key);
  FILE *out = fopen(path, "wb");
  CHECK(out);
  CHECK(fwrite("SCANG001", 1, 8, out) == 8);
  write64(out, n);
  write64(out, len);
  write64(out, seed);
  write64(out, dist);
  uint64_t attempts = 0, hist[256] = {0};
  for (size_t id = 0; id < n; id++) {
    uint32_t nonce = 0;
    for (;;) {
      key_fill(key, len, id, nonce, seed);
      unsigned t = tag(key, len);
      attempts++;
      if (matches(t, dist)) {
        hist[t]++;
        break;
      }
      CHECK(nonce < 1000000);
      nonce++;
    }
    unsigned char b[4] = {(unsigned char)(nonce >> 24),
                          (unsigned char)(nonce >> 16),
                          (unsigned char)(nonce >> 8), (unsigned char)nonce};
    CHECK(fwrite(b, 1, 4, out) == 4);
  }
  CHECK(!fclose(out));
  printf("{\"kind\":\"fixture\",\"n\":%zu,\"bytes\":%zu,\"seed\":%" PRIu64
         ",\"distribution\":%u,\"attempts\":%" PRIu64 ",\"tag0\":%" PRIu64
         ",\"tag1\":%" PRIu64 ",\"tag17\":%" PRIu64 "}\n",
         n, len, seed, dist, attempts, hist[0], hist[1], hist[17]);
  free(key);
}
typedef struct {
  uint64_t count, sum;
} result;
static void consume(void *v, const unsigned char *key, size_t len,
                    double score) {
  result *r = v;
  r->count++;
  r->sum += get64(key) ^ score_bits(score) ^
            ((uint64_t)len * UINT64_C(0x9e3779b97f4a7c15));
}
typedef struct {
  fixture *f;
  int order;
  unsigned char *seen;
  result r;
  int fault;
  int injected;
} oracle;
static void verify(void *v, const unsigned char *key, size_t len,
                   double score) {
  oracle *o = v;
  if (o->fault && !o->injected) {
    o->injected = 1;
    if (o->fault == 1)
      score += 1;
    if (o->fault == 2)
      len--;
    if (o->fault == 4) {
      static unsigned char damaged[1024];
      CHECK(len <= sizeof(damaged));
      memcpy(damaged, key, len);
      damaged[8] ^= 1;
      key = damaged;
    }
  }
  CHECK(len == o->f->len);
  uint64_t id = get64(key);
  CHECK(id < o->f->n);
  if (o->fault == 3 && id == 0)
    return; /* Drop every actual callback for member zero, including duplicates. */
  CHECK(!memcmp(key, o->f->keys[id], len));
  CHECK(score_bits(score) == score_bits(expected_score(id, o->order)));
  o->seen[id] = 1;
  consume(&o->r, key, len, score);
}
static void complete(zbtreeSet *t, zbtreeScanFunction *fn, void *ctx) {
  uint64_t cursor = 0, steps = 0;
  do {
    cursor = zbtreeScan(t, cursor, 64, fn, ctx);
    CHECK(++steps < 10000000);
  } while (cursor);
}
static result validate(zbtreeSet *t, fixture *f, int order, int fault) {
  oracle o = {.f = f, .order = order, .seen = calloc(f->n, 1), .fault = fault};
  CHECK(o.seen);
  complete(t, verify, &o);
  for (size_t i = 0; i < f->n; i++)
    CHECK(o.seen[i]);
  free(o.seen);
  zbtreeIterator it;
  CHECK(zbtreeIteratorStart(t, 0, &it));
  for (size_t id = 0; id < f->n; id++) {
    const unsigned char *key;
    size_t len;
    double score;
    CHECK(zbtreeIteratorNext(&it, 0, &key, &len, &score));
    CHECK(len == f->len && !memcmp(key, f->keys[id], len));
    CHECK(score_bits(score) == score_bits(expected_score(id, order)));
  }
  CHECK(!zbtreeIteratorNext(&it, 0, NULL, NULL, NULL));
  CHECK(zbtreeLength(t) == f->n);
  return o.r;
}
static uint64_t now(clockid_t clock) {
  struct timespec t;
  CHECK(!clock_gettime(clock, &t));
  return (uint64_t)t.tv_sec * 1000000000 + t.tv_nsec;
}
#ifdef SCAN_CENSUS
void scan_guard_census(zbtreeSet *t);
#endif
int main(int argc, char **argv) {
  if (argc == 8 && !strcmp(argv[1], "generate")) {
    generate(argv[2], number(argv[3]), number(argv[4]), number(argv[5]),
             number(argv[6]));
    CHECK(!strcmp(argv[7], "v1"));
    return 0;
  }
  if (argc != 6) {
    fprintf(stderr, "usage: scan-guard generate FILE N BYTES SEED DIST v1 | "
                    "run FILE ORDER PASSES FAULT\n");
    return 2;
  }
  CHECK(!strcmp(argv[1], "run"));
  fixture f = load(argv[2]);
  int order = (int)number(argv[3]);
  uint64_t passes = number(argv[4]);
  int fault = (int)number(argv[5]);
  CHECK(order >= 0 && order <= 2 && passes <= 100000 && fault >= 0 &&
        fault <= 4);
#ifdef SCAN_CENSUS
  CHECK(passes == 0); /* Census binary cannot produce timing observations. */
#endif
  size_t *ids = malloc(f.n * sizeof(*ids));
  CHECK(ids);
  for (size_t i = 0; i < f.n; i++)
    ids[i] = i;
  uint64_t rng = f.seed ^ UINT64_C(0xd1053a72c49b8e6f);
  if (order != 1)
    for (size_t i = f.n - 1; i; i--) {
      size_t j = mix(&rng) % (i + 1), x = ids[i];
      ids[i] = ids[j];
      ids[j] = x;
    }
  zbtreeSet *tree = zbtreeCreate();
  CHECK(tree);
  for (size_t i = 0; i < f.n; i++) {
    size_t id = order == 1 ? f.n - 1 - i : ids[i];
    zbtreeInsertPosition pos;
    double old;
    CHECK(!zbtreeFindForAdd(tree, f.keys[id], &old, &pos));
    zbtreeInsertNew(tree, expected_score(id, order), f.keys[id], &pos);
  }
  free(ids);
  result expect = validate(tree, &f, order, fault);
  size_t owned = zbtreeAllocSize(tree);
#ifdef SCAN_CENSUS
  scan_guard_census(tree);
#endif
  uint64_t elapsed = 0, cpu = 0;
  int start_cpu = -1, end_cpu = -1;
  result got = {0};
  if (passes) {
    for (int j = 0; j < 2; j++) {
      result warm = {0};
      complete(tree, consume, &warm);
      CHECK(warm.count == expect.count && warm.sum == expect.sum);
    }
    start_cpu = sched_getcpu();
    uint64_t c = now(CLOCK_THREAD_CPUTIME_ID), t = now(CLOCK_MONOTONIC);
    for (uint64_t p = 0; p < passes; p++)
      complete(tree, consume, &got);
    elapsed = now(CLOCK_MONOTONIC) - t;
    cpu = now(CLOCK_THREAD_CPUTIME_ID) - c;
    end_cpu = sched_getcpu();
    CHECK(got.count == expect.count * passes && got.sum == expect.sum * passes);
  }
  result after = validate(tree, &f, order, 0);
  CHECK(after.count == expect.count && after.sum == expect.sum &&
        zbtreeAllocSize(tree) == owned);
  printf("{\"kind\":\"run\",\"n\":%zu,\"bytes\":%zu,\"seed\":%" PRIu64
         ",\"distribution\":%u,\"order\":%d,\"passes\":%" PRIu64
         ",\"logical_members\":%" PRIu64 ",\"callbacks_per_pass\":%" PRIu64
         ",\"checksum_per_pass\":\"%016" PRIx64
         "\",\"tree_bytes\":%zu,\"elapsed_ns\":%" PRIu64
         ",\"thread_cpu_ns\":%" PRIu64
         ",\"start_cpu\":%d,\"end_cpu\":%d,\"validation\":\"pass\"}\n",
         f.n, f.len, f.seed, f.dist, order, passes, passes * f.n, expect.count,
         expect.sum, owned, elapsed, cpu, start_cpu, end_cpu);
  zbtreeFree(tree);
  for (size_t i = 0; i < f.n; i++)
    sdsfree(f.keys[i]);
  free(f.keys);
  free(f.nonces);
  return 0;
}
