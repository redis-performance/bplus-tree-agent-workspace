/* Correctness-only deterministic callback/cursor trace, compared to baseline. */
#ifndef ZBT_SOURCE
#define ZBT_SOURCE "zset_btree.c"
#endif
#include ZBT_SOURCE
int __failed_tests;
int __test_num;
#define MEMBERS 300
static unsigned char keys[MEMBERS][12];
static unsigned present[MEMBERS], seen[MEMBERS];
static double scores[MEMBERS];
static unsigned long callbacks, phases, calls;
static uint64_t trace = UINT64_C(1469598103934665603);

static void trace_word(uint64_t value) {
    for (unsigned i = 0; i < 8; i++) {
        trace ^= (uint8_t)(value >> (8*i));
        trace *= UINT64_C(1099511628211);
    }
}

static void callback(void *unused, const unsigned char *ele, size_t len, double score) {
    (void)unused;
    uint32_t id;
    serverAssert(len == sizeof(keys[0]));
    memcpy(&id, ele, sizeof(id));
    serverAssert(id < MEMBERS && present[id] && memcmp(ele,keys[id],len) == 0);
    serverAssert(memcmp(&scores[id],&score,sizeof(score)) == 0);
    seen[id]++;
    callbacks++;
    trace_word(id);
    uint64_t bits;
    memcpy(&bits,&score,sizeof(bits));
    trace_word(bits);
}

static void scan(zbtreeSet *zs) {
    static const unsigned counts[] = {1,7,16,1000};
    serverAssert(zbtTestCheck(zs));
    for (unsigned c = 0; c < sizeof(counts)/sizeof(*counts); c++) {
        memset(seen,0,sizeof(seen));
        uint64_t cursor = 0;
        unsigned steps = 0;
        do {
            cursor = zbtreeScan(zs,cursor,counts[c],callback,NULL);
            trace_word(cursor);
            serverAssert(++steps < 10000);
            calls++;
        } while (cursor);
        for (unsigned i = 0; i < MEMBERS; i++)
            serverAssert(present[i] ? seen[i] > 0 : seen[i] == 0);
        trace_word(steps);
    }
    phases++;
}

static void finish_resize(zbtreeSet *zs) {
    while (zs->member_rehash) {
        scan(zs);
        zbtIndexRehashStep(zs,1);
    }
    scan(zs);
}

int main(void) {
    unsigned char seed[16] = {17,29,43};
    dictSetHashFunctionSeed(seed);
    zbtreeSet *zs = zbtreeCreate();
    zbtreeReserve(zs,MEMBERS);
    static const uint8_t tags[] = {0,1,127,128,254,255};
    for (uint32_t i = 0; i < MEMBERS; i++) {
        memcpy(keys[i],&i,sizeof(i));
        uint32_t salt = UINT32_C(0x80000000) | i;
        memcpy(keys[i]+8,&salt,sizeof(salt));
        uint32_t attempt;
        for (attempt = 0; attempt < 1000000; attempt++) {
            memcpy(keys[i]+4,&attempt,sizeof(attempt));
            if ((zbtreeMemberHash(keys[i],sizeof(keys[i])) >> 24) == tags[i%6]) break;
        }
        serverAssert(attempt < 1000000);
        scores[i] = (double)i;
        present[i] = 1;
        zbtreeInsertNewRaw(zs,scores[i],keys[i],sizeof(keys[i]),NULL);
    }
    finish_resize(zs);
    for (zbtScoreLeaf *leaf = zs->score_first; leaf; leaf = leaf->next)
        zbtScoreLeafReverseForPop(leaf);
    scan(zs);
    serverAssert(zbtIndexStartResize(zs,1200,1));
    finish_resize(zs);
    /* Score changes force reference repair and cross-leaf movement. */
    for (unsigned i = 0; i < MEMBERS; i += 3) {
        sds key = sdsnewlen(keys[i],sizeof(keys[i]));
        zbtreeInsertPosition position;
        double oldscore;
        serverAssert(zbtreeFindForAdd(zs,key,&oldscore,&position));
        serverAssert(memcmp(&oldscore,&scores[i],sizeof(oldscore)) == 0);
        scores[i] = -1000.0 - (double)i;
        zbtreeUpdateScore(zs,key,scores[i],&position);
        sdsfree(key);
        if (i % 30 == 0) scan(zs);
    }
    finish_resize(zs);
    for (unsigned i = 0; i < MEMBERS; i += 4) {
        sds key = sdsnewlen(keys[i],sizeof(keys[i]));
        serverAssert(zbtreeDelete(zs,key));
        present[i] = 0;
        sdsfree(key);
    }
    finish_resize(zs);
    zbtreeSet *copy = zbtreeDup(zs);
    scan(copy); zbtreeFree(copy);
    for (unsigned i = 0; i < MEMBERS; i += 4) {
        present[i] = 1;
        zbtreeInsertNewRaw(zs,scores[i],keys[i],sizeof(keys[i]),NULL);
    }
    finish_resize(zs);
    serverAssert(zbtIndexStartResize(zs,MEMBERS,1));
    finish_resize(zs);
    for (unsigned i = 0; i < MEMBERS; i++) {
        double score = 12345;
        serverAssert(zbtreeScoreRaw(zs,keys[i],sizeof(keys[i]),&score));
        serverAssert(memcmp(&scores[i],&score,sizeof(score)) == 0);
    }
    zbtreeFree(zs);
    printf("{\"passed\":true,\"phases\":%lu,\"scan_calls\":%lu,"
           "\"callbacks\":%lu,\"trace\":\"%016llx\"}\n",
           phases,calls,callbacks,(unsigned long long)trace);
    return 0;
}
