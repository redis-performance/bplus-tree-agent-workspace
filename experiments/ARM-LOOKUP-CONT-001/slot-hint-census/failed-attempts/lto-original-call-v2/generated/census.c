/* Generated from pinned lookup.c; untimed census only. */
#define _POSIX_C_SOURCE 200809L
#include "zset_btree.c"
#include "../emit.h"
#include <inttypes.h>
#define N 500
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
            censusQueryBegin(t);
            zbtreeInsertPosition p; double score=0;
            hits+=zbtreeFindForAdd(t,members[i],&score,&p);
            zbtreeUpdateScore(t,members[i],i+1+(r%2?0.0:0.125),&p);
            censusQueryEnd(t);
        }
    } else if(scored) {
        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++) {
            censusQueryBegin(t);
            double score=0; hits+=zbtreeScoreRaw(t,q[i],len[i],&score); sum+=score;
            censusQueryEnd(t);
        }
    } else {
        for(uint64_t r=0;r<sweeps;r++) for(int i=0;i<N;i++) {
            censusQueryBegin(t);
            hits+=zbtreeScoreRaw(t,q[i],len[i],NULL);
            censusQueryEnd(t);
        }
    }
    *score_sum=sum; return hits;
}
int main(int argc,char **argv) {
    serverAssert(argc==2);
    const char *case_name=argv[1];
    int scored=!strcmp(case_name,"score"),missing=!strcmp(case_name,"miss");
    int external=!strcmp(case_name,"external"),updating=!strcmp(case_name,"update");
    int longkeys=!strcmp(case_name,"long")||external;
    serverAssert(scored||missing||longkeys||updating||!strcmp(case_name,"hit"));
    unsigned seed=17;uint8_t key[16];
    for(unsigned i=0;i<16;i++)key[i]=(seed+i*29U)&255;
    dictSetHashFunctionSeed(key);
    uint64_t sweeps=updating ? 2:1;
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
    double sum;uint64_t hits;
    serverAssert(sh_phase==SH_SETUP && !sh_seed.active);
    sh_phase=SH_WARMUP;
    hits=lookup_loop(target,query,len,1000,scored,&sum,members,updating);
    serverAssert(hits==(missing ? 0:1000ULL*N));
    serverAssert(sum==(scored ? 125250000.0:0));
    /* Counter reset and enable occur only after the exact original warmup. */
    serverAssert(!sh_nqueries && !sh_ncalls);
    size_t owned_before=zbtreeAllocSize(target);
    int resize_before=target->member_rehash!=NULL;
    shCountStart();
    hits=lookup_loop(target,query,len,sweeps,scored,&sum,members,updating);
    shCountEnd();
    /* Immediate endpoints precede all validation lookups and output. */
    size_t owned_after=zbtreeAllocSize(target);
    int resize_after=target->member_rehash!=NULL;
    serverAssert(sh_query==UINT_MAX && sh_nqueries==sweeps*N);
    serverAssert(hits==(missing ? 0:sweeps*N));
    serverAssert(sum==(scored ? 125250.0*sweeps:0));
    serverAssert(owned_after==owned_before);
    zbtreeIterator final;
    serverAssert(zbtreeIteratorStart(target,0,&final));
    for (int i=0;i<N;i++) {
        const unsigned char *bytes;size_t n;double score=0;
        serverAssert(zbtreeIteratorNext(&final,0,&bytes,&n,&score));
        serverAssert(score==i+1 && n==sdslen(members[i]) && !memcmp(bytes,members[i],n));
        double got=0;
        serverAssert(zbtreeScore(target,members[i],&got) && got==i+1);
        got=-123;
        serverAssert(!zbtreeScore(target,miss[i],&got) && got==-123);
    }
    serverAssert(!zbtreeIteratorNext(&final,0,NULL,NULL,NULL));
    size_t owned_after_validation=zbtreeAllocSize(target);
    sh_phase=SH_CLEANUP;
    zbtreeFree(source);zbtreeFree(target);for(int i=0;i<N;i++){sdsfree(members[i]);sdsfree(miss[i]);}
    shCompletion();
    printf("{\"revision\":0,\"diagnostic\":\"slot-hint\",\"cleanup_complete\":true,\"live_generations_after_cleanup\":0,\"verified\":true,\"untimed\":true,\"case\":\"%s\",\"seed\":%u,"
           "\"members\":500,\"warmup_sweeps\":1000,\"sweeps\":%" PRIu64 ",\"ops\":%" PRIu64 ","
           "\"hits\":%" PRIu64 ",\"score_sum\":%.0f,\"owned_bytes_before\":%zu,"
           "\"owned_bytes_after\":%zu,\"owned_bytes_after_validation\":%zu,"
           "\"active_resize_before\":%d,\"active_resize_after\":%d,",
           case_name,seed,sweeps,sweeps*N,hits,sum,owned_before,owned_after,
           owned_after_validation,resize_before,resize_after);
    censusPrint();printf("}\n");
    return 0;
}
