/* Diagnostic-only driver. Prefix observation helpers copied from HARNESS-002. */
typedef struct {
    uint64_t wall, sum, expected;
    int64_t thread;
    int cpu0, cpu1, rel0, rel1;
    const char *qos0, *qos1;
} window;
static size_t argnum(const char *s) {
    char *end; errno = 0;
    unsigned long long x = strtoull(s, &end, 10);
    serverAssert(!errno && *s && !*end && s[0] != '-' && x && x <= 100000000);
    return (size_t)x;
}
__attribute__((noinline)) static uint64_t query_loop(zbtreeSet *tree, sds *keys,
        const size_t *query, size_t n, size_t ops, size_t offset, int miss) {
    uint64_t sum = 0;
    for (size_t i = 0; i < ops; i++) {
        double score = 0;
        int found = zbtreeScore(tree, keys[query[(offset+i)%n] + (miss ? n : 0)], &score);
        sum += miss ? (uint64_t)found : (found ? (uint64_t)score : UINT64_MAX);
    }
    return sum;
}
int main(int argc, char **argv) {
    serverAssert(argc == 8);
    size_t n=argnum(argv[1]), ops=argnum(argv[2]), bytes=argnum(argv[3]);
    size_t windows=argnum(argv[4]); int miss=(int)argnum(argv[5])-1;
    uint64_t seed=1301, qs=argnum(argv[6]); size_t warm=argnum(argv[7]);
    serverAssert(bytes>=8 && bytes<=65536 && windows<=64 && miss>=0 && miss<=1);
    uint64_t rng=seed; uint8_t hash_seed[16];
    for(size_t i=0;i<16;i++) hash_seed[i]=(uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys=zmalloc(2*n*sizeof(*keys));
    size_t *order=zmalloc(n*sizeof(*order)), *query=zmalloc(n*sizeof(*query));
    unsigned char *buf=zmalloc(bytes);
    for(size_t i=0;i<2*n;i++) {
        memset(buf,'x',bytes);
        for(unsigned j=0;j<8;j++)buf[j]=(unsigned char)((uint64_t)i>>(8*j));
        keys[i]=sdsnewlen(buf,bytes);
        if(i<n)order[i]=query[i]=i;
    }
    zfree(buf);
    for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
    uint64_t qrng=qs;
    for(size_t i=n;i>1;i--){size_t j=random64(&qrng)%i,t=query[i-1];query[i-1]=query[j];query[j]=t;}
    uint64_t of=UINT64_C(14695981039346656037), qf=of;
    for(size_t i=0;i<n;i++){
        of=(of^order[i])*UINT64_C(1099511628211);
        qf=(qf^query[i])*UINT64_C(1099511628211);
    }
    zbtreeSet *tree=zbtreeCreate();
    for(size_t i=0;i<n;i++){
        zbtreeInsertPosition pos;double old;
        serverAssert(!zbtreeFindForAdd(tree,keys[order[i]],&old,&pos));
        zbtreeInsertNew(tree,(double)order[i],keys[order[i]],&pos);
    }
    window records[64];memset(records,0,sizeof(records));
    for(size_t w=0;w<windows;w++) if(!miss)
        for(size_t i=0;i<ops;i++)records[w].expected+=query[(w*ops+i)%n];
    size_t memory=zbtreeAllocSize(tree);
    uint64_t warm0=now_ns();
    for(size_t p=0;p<warm;p++) for(size_t i=0;i<n;i++){
        double score;serverAssert(zbtreeScore(tree,keys[query[i]],&score) && score==(double)query[i]);
    }
    uint64_t warm_ns=now_ns()-warm0;
    uint64_t outer0=now_ns();
    for(size_t w=0;w<windows;w++) {
        window *r=&records[w];
        r->qos0=qos_reported(&r->rel0);r->cpu0=cpu_id();
        int64_t t0=thread_ns();uint64_t w0=now_ns();
        uint64_t result=query_loop(tree,keys,query,n,ops,w*ops,miss);
        r->wall=now_ns()-w0;int64_t t1=thread_ns();
        r->cpu1=cpu_id();r->qos1=qos_reported(&r->rel1);
        r->thread=t0>=0 && t1>=t0 ? t1-t0 : -1;r->sum=result;
    }
    uint64_t outer=now_ns()-outer0,totalwall=0;
    for(size_t w=0;w<windows;w++){
        serverAssert(records[w].sum==records[w].expected);totalwall+=records[w].wall;
        sink^=records[w].sum;
    }
    serverAssert(outer>=totalwall && zbtreeLength(tree)==n && zbtreeAllocSize(tree)==memory);
    for(size_t i=0;i<n;i++){
        double score;serverAssert(zbtreeScore(tree,keys[i],&score) && score==(double)i);
        serverAssert(!zbtreeScore(tree,keys[i+n],&score));
    }
    puts("case,size,member_bytes,seed,query_seed,construction_fingerprint,query_fingerprint,window,windows,operations,elapsed_ns,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,checksum,expected,tree_bytes,outer_elapsed_ns,gap_ns,warmup_passes,warmup_elapsed_ns");
    for(size_t w=0;w<windows;w++){
        window *r=&records[w];
        printf("%s,%zu,%zu,%" PRIu64 ",%" PRIu64 ",%" PRIu64 ",%" PRIu64 ",%zu,%zu,%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%s,%d,%d,unknown,%" PRIu64 ",%" PRIu64 ",%zu,%" PRIu64 ",%" PRIu64 ",%zu,%" PRIu64 "\n",
            miss?"lookup-miss":"lookup-hit",n,bytes,seed,qs,of,qf,w,windows,ops,
            r->wall,r->thread,r->cpu0,r->cpu1,r->qos0,r->qos1,r->rel0,r->rel1,
            r->sum,r->expected,memory,outer,outer-totalwall,warm,warm_ns);
    }
    zbtreeFree(tree);for(size_t i=0;i<2*n;i++)sdsfree(keys[i]);
    zfree(keys);zfree(order);zfree(query);return 0;
}
