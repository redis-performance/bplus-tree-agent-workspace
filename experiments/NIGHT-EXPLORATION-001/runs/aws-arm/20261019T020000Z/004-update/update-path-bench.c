/* UPDATE-001 path referee. Setup and verification are outside the timer. */
#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <inttypes.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

static volatile uint64_t consumed;
static uint64_t rng(uint64_t *s) {
    uint64_t z=(*s+=UINT64_C(0x9e3779b97f4a7c15));
    z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);
    z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);
    return z^(z>>31);
}
static uint64_t nanos(void) {
    struct timespec t; serverAssert(clock_gettime(CLOCK_MONOTONIC,&t)==0);
    return (uint64_t)t.tv_sec*UINT64_C(1000000000)+t.tv_nsec;
}
static uint64_t bits(double x) { uint64_t u; memcpy(&u,&x,8); return u; }
static size_t number(const char *s) {
    char *end; unsigned long long n=strtoull(s,&end,10);
    if (!*s || *end || !n || n>100000000) { fprintf(stderr,"bad number: %s\n",s); exit(2); }
    return (size_t)n;
}
static void shuffle(size_t *p,size_t n,uint64_t *s) {
    for(size_t i=n;i>1;i--){size_t j=rng(s)%i,tmp=p[i-1];p[i-1]=p[j];p[j]=tmp;}
}
static double initial(const char *mode,size_t id) {
    if(!strcmp(mode,"nearby")) return (double)(4*(id/2)+(id&1?2:1));
    return (double)(4*id+1);
}
static size_t member_id(const unsigned char *p) {
    size_t id=0;for(unsigned j=0;j<8;j++)id|=(size_t)p[j]<<(8*j);return id;
}
int main(int argc,char **argv) {
    if(argc!=9||strcmp(argv[1],"--case")||strcmp(argv[3],"--size")||
       strcmp(argv[5],"--ops")||strcmp(argv[7],"--seed")) {
        fputs("usage: update-path-bench --case same|preserve|nearby|distant|plus-n --size N --ops N --seed N\n",stderr);return 2;
    }
    const char *mode=argv[2];
    int same=!strcmp(mode,"same"),preserve=!strcmp(mode,"preserve"),
        nearby=!strcmp(mode,"nearby"),distant=!strcmp(mode,"distant"),
        plusn=!strcmp(mode,"plus-n");
    if(!(same||preserve||nearby||distant||plusn))return 2;
    size_t n=number(argv[4]),ops=number(argv[6]);uint64_t seed=number(argv[8]);
    size_t movers=nearby?n/2:distant?n/4:n;
    if(!movers||n>1000000)return 2;
    uint64_t build_seed=seed^UINT64_C(0x06e7ac0cc4c8c0c7);
    uint64_t query_seed=seed^UINT64_C(0x94de3024a87f495d);
    uint64_t hash_rng=seed^UINT64_C(0xfed2a8c219f6130e);
    uint8_t hash_seed[16];for(unsigned i=0;i<16;i++)hash_seed[i]=(uint8_t)rng(&hash_rng);
    dictSetHashFunctionSeed(hash_seed);
    sds *keys=zmalloc(n*sizeof(*keys));size_t *build=zmalloc(n*sizeof(*build));
    size_t *query=zmalloc(movers*sizeof(*query));
    for(size_t id=0;id<n;id++){
        unsigned char member[16];memset(member,0xa5,sizeof(member));
        for(unsigned j=0;j<8;j++)member[j]=(unsigned char)(id>>(8*j));
        keys[id]=sdsnewlen(member,sizeof(member));build[id]=id;
    }
    for(size_t i=0;i<movers;i++)query[i]=i;
    shuffle(build,n,&build_seed);shuffle(query,movers,&query_seed);
    zbtreeSet *tree=zbtreeCreate();
    for(size_t i=0;i<n;i++){
        size_t id=build[i];zbtreeInsertPosition pos;double old;
        serverAssert(!zbtreeFindForAdd(tree,keys[id],&old,&pos));
        zbtreeInsertNew(tree,initial(mode,id),keys[id],&pos);
    }
    for(size_t i=0;i<n;i++){double v;serverAssert(zbtreeScore(tree,keys[i],&v));serverAssert(bits(v)==bits(initial(mode,i)));}
    uint64_t checksum=0,start=nanos();
    for(size_t op=0;op<ops;op++){
        size_t id=query[op%movers];if(nearby)id*=2;
        zbtreeInsertPosition pos;double old,next;
        serverAssert(zbtreeFindForAdd(tree,keys[id],&old,&pos));
        if(same)next=old;
        else if(preserve)next=((uint64_t)old&3)==1?old+1:old-1;
        else if(nearby)next=old==(double)(4*(id/2)+1)?old+2:old-2;
        else if(distant)next=old==(double)(4*id+1)?(double)(4*(n+id)+1):(double)(4*id+1);
        else next=old+(double)n;
        zbtreeUpdateScore(tree,keys[id],next,&pos);
        checksum+=bits(next)^(uint64_t)id;
    }
    uint64_t elapsed=nanos()-start;consumed^=checksum;
    size_t *repeats=zcalloc(n*sizeof(*repeats));
    for(size_t i=0;i<movers;i++){
        size_t id=query[i];if(nearby)id*=2;
        repeats[id]=ops/movers+(i<ops%movers);
    }
    for(size_t id=0;id<n;id++){
        double want=initial(mode,id),got;
        if(preserve&&(repeats[id]&1))want+=1;
        if(nearby&&(repeats[id]&1))want+=2;
        if(distant&&(repeats[id]&1))want=(double)(4*(n+id)+1);
        if(plusn)want+=(double)(repeats[id]*n);
        serverAssert(zbtreeScore(tree,keys[id],&got)&&bits(got)==bits(want));
    }
    unsigned char *seen=zcalloc(n);zbtreeIterator it;
    serverAssert(zbtreeIteratorStart(tree,0,&it));
    double prev=0;size_t prev_id=0;
    for(size_t rank=0;rank<n;rank++){
        const unsigned char *p;size_t len;double score;
        serverAssert(zbtreeIteratorNext(&it,0,&p,&len,&score)&&len==16);
        size_t id=member_id(p);serverAssert(id<n&&!seen[id]);seen[id]=1;
        if(rank)serverAssert(prev<score||(prev==score&&memcmp(keys[prev_id],p,16)<0));
        if(n<=10000||rank%997==0)serverAssert(zbtreeRank(tree,keys[id],0,NULL)==(long)rank);
        prev=score;prev_id=id;
    }
    serverAssert(!zbtreeIteratorNext(&it,0,NULL,NULL,NULL));
    serverAssert(zbtreeLength(tree)==n);
    printf("case,size,ops,seed,elapsed_ns,ns_per_op,tree_bytes,checksum,movers\n");
    printf("%s,%zu,%zu,%"PRIu64",%"PRIu64",%.3f,%zu,%"PRIu64",%zu\n",
        mode,n,ops,seed,elapsed,(double)elapsed/ops,zbtreeAllocSize(tree),checksum,movers);
    zbtreeFree(tree);for(size_t i=0;i<n;i++)sdsfree(keys[i]);
    zfree(keys);zfree(build);zfree(query);zfree(repeats);zfree(seen);
    return 0;
}
