static size_t number(const char *s) {
    char *end; errno = 0;
    unsigned long long v = strtoull(s, &end, 10);
    serverAssert(!errno && s[0] != '-' && *s && !*end && v && v <= 100000000);
    return (size_t)v;
}
static void shuffle(size_t *a, size_t n, uint64_t *state) {
    for (size_t i = n; i > 1; i--) {
        size_t j = random64(state) % i, t = a[i-1];
        a[i-1] = a[j]; a[j] = t;
    }
}
static uint64_t lookup(zbtreeSet *tree, sds *keys, const size_t *access, size_t count) {
    uint64_t sum = 0;
    for (size_t i = 0; i < count; i++) {
        double score = 0;
        int found = zbtreeScore(tree, keys[access[i]], &score);
        sum += found ? (uint64_t)score : UINT64_MAX;
    }
    return sum;
}
int main(int argc, char **argv) {
    size_t block = argc > 1 ? number(argv[1]) : 1;
    size_t n = argc > 2 ? number(argv[2]) : 100000;
    size_t ops = argc > 3 ? number(argv[3]) : 5000000;
    serverAssert(argc <= 4 && ops % n == 0);
    uint64_t rng = 1, access_rng = 17 + block;
    uint8_t hash_seed[16];
    for (size_t i = 0; i < sizeof(hash_seed); i++) hash_seed[i] = (uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys = zmalloc(n * sizeof(*keys));
    size_t *order = zmalloc(n * sizeof(*order));
    size_t *storage[2] = {zmalloc(ops * sizeof(size_t)), zmalloc(ops * sizeof(size_t))};
    size_t *access[2] = {storage[block % 2], storage[1 - block % 2]};
    for (size_t i = 0; i < n; i++) {
        unsigned char buf[16]; memset(buf, 'x', sizeof(buf));
        for (unsigned j = 0; j < 8; j++) buf[j] = (unsigned char)((uint64_t)i >> (j*8));
        keys[i] = sdsnewlen(buf, sizeof(buf)); order[i] = i; access[0][i] = i;
    }
    shuffle(order, n, &rng);
    shuffle(access[0], n, &access_rng);
    for (size_t p = 0; p < ops/n; p++) {
        if (p) memcpy(access[0] + p*n, access[0], n * sizeof(size_t));
        memcpy(access[1] + p*n, access[0], n * sizeof(size_t));
        if (p) shuffle(access[1] + p*n, n, &access_rng);
    }
    /* Verify every pass contains each member exactly once, not just its sum. */
    unsigned char *seen = zmalloc(n);
    uint64_t fingerprints[2] = {UINT64_C(14695981039346656037),UINT64_C(14695981039346656037)};
    for (size_t a = 0; a < 2; a++) for (size_t p = 0; p < ops/n; p++) {
        memset(seen, 0, n);
        for (size_t i = 0; i < n; i++) {
            size_t id = access[a][p*n+i]; serverAssert(id < n && !seen[id]); seen[id] = 1;
            fingerprints[a] = (fingerprints[a] ^ (uint64_t)id) * UINT64_C(1099511628211);
        }
    }
    zfree(seen);
    zbtreeSet *tree = zbtreeCreate();
    for (size_t i = 0; i < n; i++) {
        zbtreeInsertPosition pos; double old;
        serverAssert(!zbtreeFindForAdd(tree, keys[order[i]], &old, &pos));
        zbtreeInsertNew(tree, (double)order[i], keys[order[i]], &pos);
    }
    size_t tree_bytes = zbtreeAllocSize(tree);
    uint64_t expected = ((uint64_t)n * (n-1)/2) * (ops/n);
    puts("block,sample,arm,size,operations,fixture_seed,stream_seed,member_bytes,access_bytes,access_storage,access_fingerprint,elapsed_ns,thread_elapsed_ns,cpu_start,cpu_end,qos_start,qos_end,relpri_start,relpri_end,qos_effective,tree_bytes,checksum,warmup_elapsed_ns");
    for (size_t sample = 0; sample < 4; sample++) {
        size_t a = ((sample == 0 || sample == 3) ? 0 : 1) ^ !(block % 2);
        uint64_t warm_start = now_ns();
        for (size_t p = 0; p < 10; p++) serverAssert(lookup(tree,keys,order,n) == (uint64_t)n*(n-1)/2);
        uint64_t warm_ns = now_ns() - warm_start;
        int rp0, rp1;
        const char *q0 = qos_reported(&rp0); int cpu0 = cpu_id();
        int64_t t0 = thread_ns(); uint64_t w0 = now_ns();
        uint64_t sum = lookup(tree, keys, access[a], ops);
        uint64_t elapsed = now_ns() - w0; int64_t t1 = thread_ns();
        int cpu1 = cpu_id(); const char *q1 = qos_reported(&rp1);
        serverAssert(sum == expected && zbtreeLength(tree) == n && zbtreeAllocSize(tree) == tree_bytes);
        sink ^= sum;
        printf("%zu,%zu,%c,%zu,%zu,1,%zu,16,%zu,%zu,%" PRIu64 ",%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%zu,%" PRIu64 ",%" PRIu64 "\n",
            block,sample,a ? 'I':'R',n,ops,17+block,ops*sizeof(size_t),a ? 1-block%2:block%2,
            fingerprints[a],elapsed,t0 >= 0 && t1 >= t0 ? t1-t0:-1,cpu0,cpu1,q0,q1,rp0,rp1,tree_bytes,sum,warm_ns);
    }
    for (size_t i=0;i<n;i++) { double score; serverAssert(zbtreeScore(tree,keys[i],&score) && score == (double)i); }
    zbtreeFree(tree); for(size_t i=0;i<n;i++) sdsfree(keys[i]);
    zfree(keys);zfree(order);zfree(storage[0]);zfree(storage[1]);
    return 0;
}
