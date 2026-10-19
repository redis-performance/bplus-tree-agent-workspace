/* Frozen standalone rank referee. Setup, oracle, warmup and checks are untimed. */
#define main historical_microbench_main
#include "microbench.c"
#undef main
#ifdef NIGHT_RANK_PROFILE
#include "night-rank-sampler.h"
#endif

typedef struct { size_t id; double score; sds key; } rank_item;
static int rank_item_compare(const void *a, const void *b) {
    const rank_item *x = a, *y = b;
    if (x->score < y->score) return -1;
    if (x->score > y->score) return 1;
    size_t nx = sdslen(x->key), ny = sdslen(y->key);
    int c = memcmp(x->key, y->key, nx < ny ? nx : ny);
    return c ? c : (nx > ny) - (nx < ny);
}
static uint64_t score_bits(double score) {
    uint64_t bits;
    memcpy(&bits, &score, sizeof(bits));
    return bits;
}
int main(int argc, char **argv) {
    size_t n = 100000, ops = 1000000, bytes = 16, batches = 1;
    uint64_t seed = 1;
    const char *mode = "rank", *layout = "integer";
    for (int i = 1; i < argc; i++) {
        serverAssert(i + 1 < argc);
        const char *arg = argv[i++], *v = argv[i];
        if (!strcmp(arg, "--size")) n = number(v);
        else if (!strcmp(arg, "--ops")) ops = number(v);
        else if (!strcmp(arg, "--seed")) seed = number(v);
        else if (!strcmp(arg, "--member-bytes")) bytes = number(v);
        else if (!strcmp(arg, "--batches")) batches = number(v);
        else if (!strcmp(arg, "--mode")) mode = v;
        else if (!strcmp(arg, "--layout")) layout = v;
        else { fputs("Unknown option\n", stderr); return 2; }
    }
    serverAssert(bytes >= 8 && bytes <= 65536);
    serverAssert(!strcmp(mode,"rank") || !strcmp(mode,"reverse") ||
                 !strcmp(mode,"score") || !strcmp(mode,"miss"));
    serverAssert(!strcmp(layout,"integer") || !strcmp(layout,"ties") || !strcmp(layout,"finite"));
    uint64_t rng = seed, query_rng = seed ^ UINT64_C(0x1e35a7bd9124f068);
    uint8_t hash_seed[16];
    for (size_t i=0;i<16;i++) hash_seed[i] = (uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys = zmalloc(2*n*sizeof(*keys));
    size_t *construction = zmalloc(n*sizeof(*construction));
    size_t *query = zmalloc(n*sizeof(*query));
    size_t *ranks = zmalloc(n*sizeof(*ranks));
    double *scores = zmalloc(n*sizeof(*scores));
    rank_item *oracle = zmalloc(n*sizeof(*oracle));
    unsigned char *buf = zmalloc(bytes);
    for (size_t i=0;i<2*n;i++) {
        memset(buf, 'x', bytes);
        for (unsigned j=0;j<8;j++) buf[j]=(unsigned char)((uint64_t)i>>(j*8));
        keys[i]=sdsnewlen(buf,bytes);
        if (i<n) {
            construction[i]=query[i]=i;
            double score=(double)i;
            if (!strcmp(layout,"ties")) score=(double)(i/17);
            if (!strcmp(layout,"finite")) {
                static const double values[]={-0x1.fffffffffffffp1023,-0x1p-1022,-0x1p-1074,-0.0,0.0,0x1p-1074,0x1p-1022,0x1.fffffffffffffp1023};
                score=values[i%8];
            }
            scores[i]=score;
            oracle[i]=(rank_item){i,score,keys[i]};
        }
    }
    zfree(buf);
    for(size_t i=n;i>1;i--) {
        size_t j=random64(&rng)%i,t=construction[i-1];construction[i-1]=construction[j];construction[j]=t;
        j=random64(&query_rng)%i;t=query[i-1];query[i-1]=query[j];query[j]=t;
    }
    qsort(oracle,n,sizeof(*oracle),rank_item_compare);
    for(size_t i=0;i<n;i++) ranks[oracle[i].id]=i;
    zbtreeSet *tree=zbtreeCreate();
    for(size_t i=0;i<n;i++) {size_t id=construction[i];insert(tree,keys[id],scores[id]);}
    serverAssert(zbtreeLength(tree)==n);
    /* Independent sorted oracle checks order, exact score bits, reverse and absence. */
    zbtreeIterator it; zbtreeIteratorStart(tree,0,&it);
    for(size_t i=0;i<n;i++) {
        const unsigned char *member; size_t len; double score;
        serverAssert(zbtreeIteratorNext(&it,0,&member,&len,&score));
        serverAssert(len==bytes && !memcmp(member,oracle[i].key,bytes));
        serverAssert(score_bits(score)==score_bits(oracle[i].score));
        size_t id=query[i];
        serverAssert(zbtreeRank(tree,keys[id],0,&score)==(long)ranks[id]);
        serverAssert(score_bits(score)==score_bits(scores[id]));
        serverAssert(zbtreeRank(tree,keys[id],1,NULL)==(long)(n-1-ranks[id]));
        serverAssert(zbtreeRank(tree,keys[id+n],0,NULL)==-1);
    }
    serverAssert(!zbtreeIteratorNext(&it,0,NULL,NULL,NULL));
    int reverse=!strcmp(mode,"reverse"), with_score=!strcmp(mode,"score"), miss=!strcmp(mode,"miss");
    uint64_t expected=0;
    for(size_t i=0;i<ops;i++) {
        size_t id=query[i%n];
        expected+=(uint64_t)(miss ? -1L : (long)(reverse ? n-1-ranks[id] : ranks[id]));
        if(with_score) expected^=score_bits(scores[id]);
    }
    uint64_t warm=0,warm_start=now_ns();
    for(size_t i=0;i<n;i++) {double score=0;long r=zbtreeRank(tree,keys[query[i]+(miss?n:0)],reverse,with_score?&score:NULL);warm+=(uint64_t)r;if(with_score)warm^=score_bits(score);}
    sink^=warm;
    uint64_t warm_ns=now_ns()-warm_start;
#ifdef NIGHT_RANK_PROFILE
    sample_init();
#endif
    puts("mode,layout,size,operations,member_bytes,seed,batch,elapsed_ns,ns_per_op,checksum,tree_bytes,warmup_ns,thread_elapsed_ns,cpu_start,cpu_end");
    size_t owned=zbtreeAllocSize(tree);
    for(size_t batch=0;batch<batches;batch++) {
        uint64_t sum=0;
        int cpu_start=cpu_id();int64_t thread_start=thread_ns();
#ifdef NIGHT_RANK_PROFILE
        sample_start();
#endif
        uint64_t start=now_ns();
        for(size_t i=0;i<ops;i++) {
            size_t id=query[i%n];double score=0;
            long r=zbtreeRank(tree,keys[id+(miss?n:0)],reverse,with_score?&score:NULL);
            sum+=(uint64_t)r;
            if(with_score)sum^=score_bits(score);
        }
        uint64_t elapsed=now_ns()-start;
#ifdef NIGHT_RANK_PROFILE
        sample_stop(mode);
#endif
        int64_t thread_end=thread_ns();int cpu_end=cpu_id();
        serverAssert(sum==expected && zbtreeLength(tree)==n && zbtreeAllocSize(tree)==owned);
        sink^=sum;
        printf("%s,%s,%zu,%zu,%zu,%" PRIu64 ",%zu,%" PRIu64 ",%.6f,%" PRIu64 ",%zu,%" PRIu64 ",%" PRId64 ",%d,%d\n",mode,layout,n,ops,bytes,seed,batch,elapsed,(double)elapsed/ops,sum,owned,warm_ns,thread_start>=0&&thread_end>=thread_start?thread_end-thread_start:-1,cpu_start,cpu_end);
    }
    zbtreeFree(tree);
    for(size_t i=0;i<2*n;i++)sdsfree(keys[i]);
    zfree(keys);zfree(construction);zfree(query);zfree(ranks);zfree(scores);zfree(oracle);
    return 0;
}
