#define _POSIX_C_SOURCE 200809L
#include "server.h"
#include "zset_btree.h"
#include <string.h>
#include <time.h>
#include <inttypes.h>
#include <errno.h>
#define N 500
static uint64_t now_ns(void) {
    struct timespec t; serverAssert(clock_gettime(CLOCK_MONOTONIC_RAW,&t)==0);
    return (uint64_t)t.tv_sec*1000000000ULL+t.tv_nsec;
}
static zbtreeSet *fixture(sds *members, int longkeys) {
    zbtreeSet *t=zbtreeCreate();
    /* Single-pair ZADD converts the short-member listpack before member 129.
     * Longer-than-64B members start as a tree with the first single-pair hint. */
    zbtreeReserve(t,longkeys ? 1 : 129);
    for(int i=0;i<N;i++) {
        if(!longkeys && i<128) {
            serverAssert(!zbtreeScoreRaw(t,(unsigned char*)members[i],sdslen(members[i]),NULL));
            zbtreeInsertNewRaw(t,i+1,(unsigned char*)members[i],sdslen(members[i]),NULL);
        } else {
            zbtreeInsertPosition p; double score;
            serverAssert(!zbtreeFindForAdd(t,members[i],&score,&p));
            zbtreeInsertNew(t,i+1,members[i],&p);
        }
    }
    serverAssert(zbtreeLength(t)==N); return t;
}
__attribute__((noinline))
static uint64_t lookup_loop(zbtreeSet *t,const unsigned char **q,size_t *len,
                            uint64_t sweeps,int scored,double *score_sum,sds *members,int updating) {
    uint64_t hits=0; double sum=0;
    if(updating) {
        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++) {
            zbtreeInsertPosition p; double score;
            hits+=zbtreeFindForAdd(t,members[i],&score,&p);
            zbtreeUpdateScore(t,members[i],i+1+(r%2?0.0:0.125),&p);
        }
    } else if(scored) {
        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++) {
            double score=0; hits+=zbtreeScoreRaw(t,q[i],len[i],&score); sum+=score;
        }
    } else {
        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++)
            hits+=zbtreeScoreRaw(t,q[i],len[i],NULL);
    }
    *score_sum=sum; return hits;
}
int main(int argc,char **argv) {
    serverAssert(argc==5);
    int verify=!strcmp(argv[1],"verify"); serverAssert(verify||!strcmp(argv[1],"measure"));
    int scored=!strcmp(argv[2],"score"),missing=!strcmp(argv[2],"miss"),external=!strcmp(argv[2],"external"),updating=!strcmp(argv[2],"update");
    int longkeys=!strcmp(argv[2],"long")||external;
    serverAssert(scored||missing||longkeys||updating||!strcmp(argv[2],"hit"));
    unsigned seed=(unsigned)strtoul(argv[3],NULL,10); uint8_t key[16];
    for(unsigned i=0;i<16;i++)key[i]=(seed+i*29U)&255;
    dictSetHashFunctionSeed(key);
    uint64_t sweeps=strtoull(argv[4],NULL,10); serverAssert(sweeps>0 && sweeps<=10000000);
    sds members[N],miss[N]; const unsigned char *query[N]; size_t len[N];
    for(int i=0;i<N;i++) {
        char b[384]; memset(b,'a'+i%26,sizeof(b)); int l=snprintf(b,32,"m:%d",i+1);
        if(longkeys){b[l]=':';l=external?384:256;} members[i]=sdsnewlen(b,l);
        b[0]='x';miss[i]=sdsnewlen(b,l);
    }
    zbtreeSet *source=fixture(members,longkeys),*target=fixture(members,longkeys);
    zbtreeIterator it; serverAssert(zbtreeIteratorStart(source,0,&it));
    for(int i=0;i<N;i++) {
        double score; serverAssert(zbtreeIteratorNext(&it,0,&query[i],&len[i],&score));
        serverAssert(score==i+1 && len[i]==sdslen(members[i]) && !memcmp(query[i],members[i],len[i]));
        serverAssert(query[i]!=(unsigned char*)members[i]);
        double found=0;serverAssert(zbtreeScoreRaw(target,query[i],len[i],&found)&&found==i+1);
        serverAssert(zbtreeScoreRaw(target,query[i],len[i],NULL));
        serverAssert(!zbtreeScoreRaw(target,(unsigned char*)miss[i],sdslen(miss[i]),NULL));
        if(missing){query[i]=(unsigned char*)miss[i];len[i]=sdslen(miss[i]);}
    }
    serverAssert(!zbtreeIteratorNext(&it,0,NULL,NULL,NULL));
    size_t bytes=zbtreeAllocSize(target); double sum; uint64_t hits;
    if(verify) {
        hits=lookup_loop(target,query,len,1,scored,&sum,members,updating);
        serverAssert(hits==(missing?0:N)); serverAssert(sum==(scored?125250:0));
        if(updating) for(int i=0;i<N;i++) {
            double got=0; serverAssert(zbtreeScore(target,members[i],&got));
            serverAssert(got==i+1.125);
        }
        printf("{\"verified\":true,\"case\":\"%s\",\"seed\":%u,\"members\":500,\"owned_bytes\":%zu}\n",argv[2],seed,bytes);
    } else {
        hits=lookup_loop(target,query,len,1000,scored,&sum,members,updating);
        serverAssert(hits==(missing?0:1000ULL*N));
        bytes=zbtreeAllocSize(target);
        serverAssert(!updating || sweeps%2==0);
        uint64_t begin=now_ns(); hits=lookup_loop(target,query,len,sweeps,scored,&sum,members,updating); uint64_t elapsed=now_ns()-begin;
        serverAssert(hits==(missing?0:sweeps*N));serverAssert(sum==(scored?125250.0*sweeps:0));
        serverAssert(zbtreeAllocSize(target)==bytes);
        if(updating) for(int i=0;i<N;i++) { double got=0;serverAssert(zbtreeScore(target,members[i],&got)&&got==i+1); }
        printf("{\"case\":\"%s\",\"seed\":%u,\"ops\":%" PRIu64 ",\"elapsed_ns\":%" PRIu64 ",\"hits\":%" PRIu64 ",\"score_sum\":%.0f,\"owned_bytes\":%zu}\n",argv[2],seed,sweeps*N,elapsed,hits,sum,bytes);
    }
    zbtreeFree(source);zbtreeFree(target);for(int i=0;i<N;i++){sdsfree(members[i]);sdsfree(miss[i]);} return 0;
}
