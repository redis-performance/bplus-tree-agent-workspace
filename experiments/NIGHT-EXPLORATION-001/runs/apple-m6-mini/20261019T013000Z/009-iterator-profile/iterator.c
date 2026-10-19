/* Separate iterator-mode referee; reuse frozen timing and fixture primitives. */
#define main legacy_microbench_main
#include "microbench.c"
#undef main
#include <math.h>

static uint64_t score_bits(double s) { uint64_t u; memcpy(&u, &s, sizeof u); return u; }
static double model_score(size_t i, size_t n, const char *encoding) {
    if (!strcmp(encoding, "fraction")) return (double)i - (double)(n/2) + 0.25;
    if (!strcmp(encoding, "wide")) return 0x1p53 + 2.0*(double)i;
    if (!strcmp(encoding, "zero")) return i ? (double)i : -0.0;
    return (double)i - (double)(n/2);
}
/* All returned data used by timing is consumed. Full byte/order oracle is outside
 * timing; no-output traversal checks count and the independent state walk below. */
static uint64_t traverse(zbtreeSet *tree, size_t n, size_t passes, int reverse, unsigned mask) {
    uint64_t sum = 0;
    for (size_t pass=0; pass<passes; pass++) {
        zbtreeIterator it;
        serverAssert(zbtreeIteratorStart(tree, reverse, &it));
        const unsigned char *ele = NULL;
        size_t len = 0, visited = 0;
        double score = 0;
        while (zbtreeIteratorNext(&it, reverse, mask&1 ? &ele : NULL,
                                 mask&2 ? &len : NULL, mask&4 ? &score : NULL)) {
            sum += 1;
            if (mask&1) sum += ele[0];
            if (mask&2) sum += len;
            if (mask&4) sum += score_bits(score);
            visited++;
        }
        serverAssert(visited == n);
    }
    return sum;
}
static void verify(zbtreeSet *tree, sds *keys, size_t n, int reverse, unsigned mask, const char *encoding) {
    zbtreeIterator it;
    serverAssert(zbtreeIteratorStart(tree, reverse, &it));
    for (size_t k=0; k<n; k++) {
        size_t i=reverse ? n-1-k : k;
        const unsigned char sentinel = 42;
        const unsigned char *ele = &sentinel;
        size_t len = SIZE_MAX;
        double score = -12345.5;
        serverAssert(zbtreeIteratorNext(&it, reverse, mask&1 ? &ele : NULL,
                                        mask&2 ? &len : NULL, mask&4 ? &score : NULL));
        if (mask&1) serverAssert(!memcmp(ele, keys[i], sdslen(keys[i])));
        else serverAssert(ele == &sentinel);
        if (mask&2) serverAssert(len == sdslen(keys[i]));
        else serverAssert(len == SIZE_MAX);
        if (mask&4) serverAssert(score_bits(score) == score_bits(model_score(i,n,encoding)));
        else serverAssert(score == -12345.5);
        /* Observe state with a copy and all outputs to validate even mask 0. */
        if (k+1<n) {
            zbtreeIterator copy=it; const unsigned char *next; size_t nextlen; double nextscore;
            size_t nexti=reverse ? n-2-k : k+1;
            serverAssert(zbtreeIteratorNext(&copy, reverse, &next, &nextlen, &nextscore));
            serverAssert(nextlen==sdslen(keys[nexti]) && !memcmp(next,keys[nexti],nextlen));
            serverAssert(score_bits(nextscore)==score_bits(model_score(nexti,n,encoding)));
        }
    }
    for (int k=0;k<2;k++) {
        const unsigned char sentinel=23,*ele=&sentinel;size_t len=SIZE_MAX;double score=-12345.5;
        serverAssert(!zbtreeIteratorNext(&it,reverse,&ele,&len,&score));
        serverAssert(ele==&sentinel && len==SIZE_MAX && score==-12345.5);
    }
}
#ifdef PROFILE_SAMPLE
extern void sample_begin(void);
extern void sample_end(void);
#endif
int main(int argc,char **argv) {
    size_t n=100000,ops=20000000,bytes=16,passes=3; uint64_t seed=7103;
    unsigned mask=4;int reverse=0;const char *encoding="integer";
    for(int i=1;i<argc;i+=2) {
        if(i+1==argc)return 2;
        const char *a=argv[i],*v=argv[i+1];
        if(!strcmp(a,"--size"))n=number(v);
        else if(!strcmp(a,"--ops"))ops=number(v);
        else if(!strcmp(a,"--member-bytes"))bytes=number(v);
        else if(!strcmp(a,"--seed"))seed=number(v);
        else if(!strcmp(a,"--warmup-passes"))passes=number(v);
        else if(!strcmp(a,"--direction")){if(!strcmp(v,"forward"))reverse=0;else if(!strcmp(v,"reverse"))reverse=1;else return 2;}
        else if(!strcmp(a,"--mask")){if(strlen(v)!=1 || *v<'0' || *v>'7')return 2;mask=*v-'0';}
        else if(!strcmp(a,"--encoding"))encoding=v;
        else return 2;
    }
    if(bytes<8 || bytes>65536 || (strcmp(encoding,"integer") && strcmp(encoding,"fraction") && strcmp(encoding,"wide") && strcmp(encoding,"zero")))return 2;
    uint64_t rng=seed;uint8_t hashseed[16];for(size_t i=0;i<16;i++)hashseed[i]=(uint8_t)random64(&rng);dictSetHashFunctionSeed(hashseed);
    sds *keys=zmalloc(n*sizeof(*keys));size_t *order=zmalloc(n*sizeof(*order));char *buf=zmalloc(bytes);
    uint64_t expected=0,fingerprint=UINT64_C(14695981039346656037);
    for(size_t i=0;i<n;i++) {
        memset(buf,'x',bytes);for(unsigned j=0;j<8;j++)buf[j]=(char)((uint64_t)i>>(8*j));
        keys[i]=sdsnewlen(buf,bytes);order[i]=i;
        expected+=1;if(mask&1)expected+=(unsigned char)buf[0];if(mask&2)expected+=bytes;
        if(mask&4)expected+=score_bits(model_score(i,n,encoding));
    }
    for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
    zbtreeSet *tree=zbtreeCreate();
    for(size_t i=0;i<n;i++){size_t k=order[i];insert(tree,keys[k],model_score(k,n,encoding));fingerprint=(fingerprint^k)*UINT64_C(1099511628211);}
    verify(tree,keys,n,reverse,mask,encoding);
    uint64_t warmstart=now_ns();serverAssert(traverse(tree,n,passes,reverse,mask)==expected*passes);uint64_t warm=now_ns()-warmstart;
    size_t traversals=1+(ops-1)/n,count=traversals*n,owned=zbtreeAllocSize(tree);
    #ifdef PROFILE_SAMPLE
    sample_begin();
    #endif
    int p0,p1;const char *q0=qos_reported(&p0);int cpu0=cpu_id();int64_t t0=thread_ns();uint64_t w0=now_ns();
    uint64_t checksum=traverse(tree,n,traversals,reverse,mask);
    uint64_t elapsed=now_ns()-w0;int64_t t1=thread_ns();int cpu1=cpu_id();const char *q1=qos_reported(&p1);
    #ifdef PROFILE_SAMPLE
    sample_end();
    #endif
    serverAssert(checksum==expected*traversals && zbtreeLength(tree)==n && zbtreeAllocSize(tree)==owned);
    verify(tree,keys,n,reverse,mask,encoding);sink^=checksum;
    puts("case,size,requested_ops,operations,member_bytes,seed,direction,mask,encoding,traversals,checksum,expected_checksum,tree_bytes,elapsed_ns,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,warmup_passes,warmup_elapsed_ns,construction_fingerprint");
    printf("iterator-modes,%zu,%zu,%zu,%zu,%"PRIu64",%s,%u,%s,%zu,%"PRIu64",%"PRIu64",%zu,%"PRIu64",%"PRId64",%d,%d,%s,%s,%d,%d,unknown,%zu,%"PRIu64",%"PRIu64"\n",n,ops,count,bytes,seed,reverse?"reverse":"forward",mask,encoding,traversals,checksum,expected*traversals,owned,elapsed,t0>=0&&t1>=t0?t1-t0:-1,cpu0,cpu1,q0,q1,p0,p1,passes,warm,fingerprint);
    zbtreeFree(tree);for(size_t i=0;i<n;i++)sdsfree(keys[i]);zfree(keys);zfree(order);zfree(buf);return 0;
}
