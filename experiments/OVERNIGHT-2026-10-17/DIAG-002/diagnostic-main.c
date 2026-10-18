/* Diagnostic only; inspired by CPU Performance Engineering benchmark14 brackets.
 * No conversion to clock GHz: dependent-add elapsed time is just a second workload. */
#if !defined(__aarch64__)
#error "This diagnostic's inspected assembly is AArch64-only"
#endif
__attribute__((noinline)) static uint64_t dependent_adds(uint64_t count) {
    uint64_t x=0;
    for (uint64_t i=0;i<count;i+=8) {
        __asm__ volatile(
            "add %0, %0, #1\n\tadd %0, %0, #1\n\t"
            "add %0, %0, #1\n\tadd %0, %0, #1\n\t"
            "add %0, %0, #1\n\tadd %0, %0, #1\n\t"
            "add %0, %0, #1\n\tadd %0, %0, #1\n\t" : "+r"(x));
    }
    return x;
}
typedef struct {uint64_t wall;int64_t thread;int start,end;} observation;
static observation bracket(uint64_t adds) {
    observation s; s.start=cpu_id();int64_t c=thread_ns();uint64_t w=now_ns();
    uint64_t result=dependent_adds(adds);
    s.wall=now_ns()-w;int64_t end=thread_ns();s.end=cpu_id();
    s.thread=c>=0&&end>=c?end-c:-1;
    serverAssert(result==adds);sink^=result;return s;
}
int main(int argc,char **argv) {
    int smoke=argc==2&&!strcmp(argv[1],"--smoke");
    if (argc!=1&&!smoke) return 2;
    size_t n=smoke?1000:1000000,ops=smoke?10000:5000000,reps=smoke?2:4;
    uint64_t adds=smoke?80000:128000000,rng=1;
    uint8_t hash_seed[16];
    for (unsigned i=0;i<16;i++) hash_seed[i]=(uint8_t)random64(&rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys=zmalloc(2*n*sizeof(*keys));size_t *order=zmalloc(n*sizeof(*order));
    for (size_t i=0;i<2*n;i++) {
        unsigned char buf[16];memset(buf,'x',16);
        for (unsigned j=0;j<8;j++) buf[j]=(unsigned char)((uint64_t)i>>(8*j));
        keys[i]=sdsnewlen(buf,16);if(i<n)order[i]=i;
    }
    for (size_t i=n;i>1;i--) {size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
    zbtreeSet *tree=zbtreeCreate();
    for (size_t i=0;i<n;i++) {
        zbtreeInsertPosition pos;double old;
        serverAssert(!zbtreeFindForAdd(tree,keys[order[i]],&old,&pos));
        zbtreeInsertNew(tree,(double)order[i],keys[order[i]],&pos);
    }
    uint64_t warm_start=now_ns();
    for(unsigned pass=0;pass<10;pass++) for(size_t i=0;i<n;i++) {
        double score;serverAssert(zbtreeScore(tree,keys[order[i]],&score)&&score==(double)order[i]);
    }
    uint64_t warm_ns=now_ns()-warm_start,expected=0;
    for(size_t i=0;i<ops;i++)expected+=order[i%n];
    size_t memory=zbtreeAllocSize(tree);
    puts("sample,size,member_bytes,seed,operations,adds,checksum,tree_bytes,wall_ns,thread_ns,cpu_start,cpu_end,pre_wall_ns,pre_thread_ns,pre_cpu_start,pre_cpu_end,post_wall_ns,post_thread_ns,post_cpu_start,post_cpu_end,qos_reported,qos_relpri,qos_effective,warmup_ns");
    for(size_t sample=0;sample<reps;sample++) {
        int relpri;const char *qos=qos_reported(&relpri);
        observation pre=bracket(adds),s;uint64_t checksum=0;
        s.start=cpu_id();int64_t c=thread_ns();uint64_t w=now_ns();
        for(size_t i=0;i<ops;i++) {
            double score=0;int found=zbtreeScore(tree,keys[order[i%n]],&score);
            checksum+=found?(uint64_t)score:UINT64_MAX;
        }
        s.wall=now_ns()-w;int64_t end=thread_ns();s.end=cpu_id();
        s.thread=c>=0&&end>=c?end-c:-1;
        observation post=bracket(adds);
        serverAssert(checksum==expected&&zbtreeLength(tree)==n&&zbtreeAllocSize(tree)==memory);
        sink^=checksum;
        printf("%zu,%zu,16,1,%zu,%" PRIu64 ",%" PRIu64 ",%zu,%" PRIu64 ",%" PRId64 ",%d,%d,%" PRIu64 ",%" PRId64 ",%d,%d,%" PRIu64 ",%" PRId64 ",%d,%d,%s,%d,unknown,%" PRIu64 "\n",
            sample,n,ops,adds,checksum,memory,s.wall,s.thread,s.start,s.end,
            pre.wall,pre.thread,pre.start,pre.end,post.wall,post.thread,post.start,post.end,qos,relpri,warm_ns);
    }
    zbtreeFree(tree);for(size_t i=0;i<2*n;i++)sdsfree(keys[i]);zfree(keys);zfree(order);return 0;
}
