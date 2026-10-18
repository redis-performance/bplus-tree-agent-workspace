/* Natural ID widening and mutation-scan oracle. Private fields are read-only
 * observations; all construction/mutation goes through the public API. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#include <math.h>

#define INLINE_N 850000U
#define EXTERNAL_N 4096U
#define TOTAL (INLINE_N + EXTERNAL_N)
static unsigned char live[TOTAL], seen[TOTAL], continuous[TOTAL];
static double scores[TOTAL];
static unsigned seed, stage;
static uint64_t random_state, callbacks, scans, validations, mutations;
#define CHECK(x) do { if (!(x)) { fprintf(stderr, "seed=%u stage=%u line=%d: %s\n", seed, stage, __LINE__, #x); abort(); } } while (0)

static uint64_t random64(void) {
    uint64_t z = (random_state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
static uint64_t bits(double d) { uint64_t b; memcpy(&b, &d, sizeof b); return b; }
static size_t key(unsigned id, unsigned char *buf) {
    static const size_t external[] = {320, 321, 1024};
    size_t len = id < INLINE_N ? 319 : external[(id-INLINE_N)%3];
    for (size_t j=0; j<len; j++) buf[j] = (unsigned char)(id*17U + j*37U + seed);
    for (unsigned j=0; j<8; j++) buf[j] = (unsigned char)((uint64_t)id >> (8*j));
    return len;
}
static unsigned identify(const unsigned char *buf, size_t len, double score) {
    CHECK(len >= 8);
    uint64_t id=0;
    for (unsigned j=0; j<8; j++) id |= (uint64_t)buf[j] << (8*j);
    CHECK(id < TOTAL && live[id]);
    unsigned char expected[1024];
    CHECK(len == key((unsigned)id, expected));
    CHECK(!memcmp(buf, expected, len));
    CHECK(bits(score) == bits(scores[id]));
    return (unsigned)id;
}
static void visit(void *ctx, const unsigned char *buf, size_t len, double score) {
    UNUSED(ctx);
    seen[identify(buf,len,score)] = 1;
    callbacks++;
}
static uint64_t groups(const zbtreeSet *tree) {
    uint64_t n = tree->member_index.size / ZBT_SCAN_BUCKETS_PER_STEP;
    if (tree->member_rehash) {
        uint64_t other=tree->member_rehash->table.size / ZBT_SCAN_BUCKETS_PER_STEP;
        if (other>n) n=other;
    }
    return n > ZBT_SCAN_MAX_GROUPS ? ZBT_SCAN_MAX_GROUPS : n;
}
static void scan_all(zbtreeSet *tree, unsigned long hint) {
    memset(seen,0,sizeof seen);
    uint64_t cursor=0, calls=0, limit=groups(tree)+1;
    do {
        cursor=zbtreeScan(tree,cursor,hint,visit,NULL);
        CHECK(++calls<=limit);
    } while (cursor);
    for (unsigned i=0;i<TOTAL;i++) CHECK(seen[i]==live[i]);
    scans++;
}
static int cmp(const void *ap, const void *bp) {
    unsigned a=*(const unsigned *)ap, b=*(const unsigned *)bp;
    if (scores[a]<scores[b]) return -1;
    if (scores[a]>scores[b]) return 1;
    unsigned char ka[1024],kb[1024];
    size_t la=key(a,ka),lb=key(b,kb);
    int c=memcmp(ka,kb,la<lb?la:lb);
    return c?c:(la>lb)-(la<lb);
}
static void verify(zbtreeSet *tree) {
    unsigned *order=zmalloc(TOTAL*sizeof(*order));
    size_t count=0;
    for (unsigned i=0;i<TOTAL;i++) {
        unsigned char buf[1024]; size_t len=key(i,buf); double value;
        CHECK(zbtreeScoreRaw(tree,buf,len,&value)==live[i]);
        if (live[i]) { CHECK(bits(value)==bits(scores[i])); order[count++]=i; }
    }
    CHECK(zbtreeLength(tree)==count);
    qsort(order,count,sizeof(*order),cmp);
    for (int reverse=0;reverse<2;reverse++) {
        zbtreeIterator it;
        CHECK(zbtreeIteratorStart(tree,reverse,&it)==(count!=0));
        for (size_t j=0;j<count;j++) {
            const unsigned char *buf; size_t len; double value;
            unsigned id=order[reverse?count-j-1:j];
            CHECK(zbtreeIteratorNext(&it,reverse,&buf,&len,&value));
            CHECK(identify(buf,len,value)==id);
            if (j%997==0) {
                unsigned char expected[1024]; size_t elen=key(id,expected);
                sds s=sdsnewlen(expected,elen);
                CHECK(zbtreeRank(tree,s,reverse,&value)==(long)j);
                CHECK(bits(value)==bits(scores[id])); sdsfree(s);
                zbtreeIterator seek;
                CHECK(zbtreeIteratorSeekRank(tree,reverse?count-j-1:j,&seek));
                CHECK(zbtreeIteratorNext(&seek,reverse,&buf,&len,&value));
                CHECK(identify(buf,len,value)==id);
            }
        }
        CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    scan_all(tree,256);
    zfree(order); validations++;
}
static void put(zbtreeSet *tree,unsigned id,double value) {
    unsigned char buf[1024]; size_t len=key(id,buf);
    sds s=sdsnewlen(buf,len); zbtreeInsertPosition pos; double old;
    CHECK(zbtreeFindForAdd(tree,s,&old,&pos)==live[id]);
    if (live[id]) { CHECK(bits(old)==bits(scores[id])); zbtreeUpdateScore(tree,s,value,&pos); }
    else zbtreeInsertNewRaw(tree,value,buf,len,&pos);
    sdsfree(s); live[id]=1; scores[id]=value; mutations++;
}
static void remove_id(zbtreeSet *tree,unsigned id) {
    unsigned char buf[1024]; size_t len=key(id,buf); sds s=sdsnewlen(buf,len);
    CHECK(zbtreeDelete(tree,s)==live[id]); sdsfree(s); live[id]=0; mutations++;
}
static void mutable_scan(zbtreeSet *tree) {
    memcpy(continuous,live,sizeof live); memset(seen,0,sizeof seen);
    uint64_t cursor=0,calls=0,largest=groups(tree);
    do {
        cursor=zbtreeScan(tree,cursor,256,visit,NULL); calls++;
        if (!cursor) break;
        unsigned anchor=(unsigned)(random64()%4096);
        put(tree,anchor,(calls&1)?-0.0:0.0);
        unsigned id=INLINE_N+(unsigned)(random64()%EXTERNAL_N);
        if (live[id]) { remove_id(tree,id); continuous[id]=0; }
        else put(tree,id,(double)id);
        uint64_t current=groups(tree); if (current>largest) largest=current;
        CHECK(calls<=largest+1);
    } while (cursor);
    CHECK(calls<=largest+1);
    for (unsigned i=0;i<TOTAL;i++) if (continuous[i]) CHECK(seen[i]);
    printf("mutable_scan calls=%" PRIu64 " largest_groups=%" PRIu64 "\n",calls,largest);
    scans++;
}
int main(int argc,char **argv) {
    CHECK(argc==2); seed=(unsigned)strtoul(argv[1],NULL,10); CHECK(seed==7||seed==19);
    random_state=seed; uint8_t hash_seed[16];
    for (unsigned i=0;i<16;i++) hash_seed[i]=(uint8_t)random64();
    dictSetHashFunctionSeed(hash_seed);
    zbtreeSet *tree=zbtreeCreate(); zbtreeReserve(tree,1024);
    unsigned observed_widening=0;
    stage=1;
    for (unsigned i=0;i<INLINE_N;i++) {
        unsigned char buf[1024];size_t len=key(i,buf);
        zbtreeInsertNewAppend(tree,(double)i,buf,len);live[i]=1;scores[i]=(double)i;
        if (!observed_widening && tree->member_rehash &&
            !tree->member_index.wide_ids && tree->member_rehash->table.wide_ids) {
            observed_widening=1;
            CHECK(tree->member_rehash->table.used<tree->length);
            scan_all(tree,256);
            CHECK(tree->member_rehash && tree->member_rehash->table.wide_ids);
            printf("active_widening members=%u next_leaf_id=%u\n",i+1,tree->next_score_leaf_id);
        }
    }
    CHECK(observed_widening); CHECK(tree->next_score_leaf_id>UINT16_MAX);
    CHECK(tree->member_index.wide_ids || (tree->member_rehash&&tree->member_rehash->table.wide_ids));
    printf("natural_ids members=%u next_leaf_id=%u\n",INLINE_N,tree->next_score_leaf_id);
    stage=2;
    for (unsigned i=INLINE_N;i<TOTAL;i++) {
        unsigned char buf[1024];size_t len=key(i,buf);
        zbtreeInsertNewAppend(tree,(double)i,buf,len);live[i]=1;scores[i]=(double)i;
    }
    verify(tree);
    stage=3;
    unsigned first=INLINE_N/4,last=INLINE_N/2;
    CHECK(zbtreeDeleteRangeByRank(tree,first,last-1)==last-first);
    for (unsigned i=first;i<last;i++) live[i]=0;
    verify(tree);
    stage=4;
    for (unsigned i=first;i<last;i++) put(tree,i,-(double)(i+1));
    verify(tree);
    stage=5; mutable_scan(tree); verify(tree);
    stage=6;
    zbtreeSet *copy=zbtreeDup(tree);zbtreeFree(tree);verify(copy);zbtreeFree(copy);
    printf("PASS seed=%u validations=%" PRIu64 " scans=%" PRIu64 " callbacks=%" PRIu64 " mutations=%" PRIu64 "\n",seed,validations,scans,callbacks,mutations);
    return 0;
}
