#define _GNU_SOURCE
#define REDIS_TEST
#include "zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
int __failed_tests, __test_num;
static unsigned long invariants, comparisons, relocations, mutations;
static unsigned max_offset, codes;
static void invariant(zbtreeSet *t) {
    for (zbtScoreLeaf *l = t->score_first; l; l = l->next) {
        size_t cap = zmalloc_usable_size(l);
        if (cap > ZBT_SCORE_LEAF_BYTES) cap = ZBT_SCORE_LEAF_BYTES;
        for (unsigned i = 0; i < l->n.count; i++) {
            uint16_t d = zbtScoreLeafOffsets(l)[i], off = zbtRecordOffset(d);
            unsigned char *r = (unsigned char *)l + off;
            serverAssert(off < cap && off + zbtRecordStorageBytes(r) <= cap);
            unsigned expected = r[0] < 15 ? r[0] + 1 : 0;
            serverAssert(zbtRecordLengthCode(d) == expected);
            codes |= 1U << expected;
            if (off > max_offset) max_offset = off;
            invariants++;
        }
    }
}
static void outputs(zbtScoreLeaf *l, uint32_t hash, const unsigned char *q,
                     size_t n, int found, unsigned pos) {
    for (unsigned mask = 0; mask < 4; mask++) {
        double score = 12345, expected = -0.0; unsigned at = UINT_MAX;
        serverAssert(zbtScoreLeafFindMember(l, hash, q, n, mask&1 ? &score : NULL,
                                           mask&2 ? &at : NULL) == found);
        if (found && (mask&1)) serverAssert(!memcmp(&score, &expected, sizeof(score)));
        else serverAssert(score == 12345);
        serverAssert(at == (found && (mask&2) ? pos : UINT_MAX)); comparisons++;
    }
}
static void synthetic(void) {
    size_t page = sysconf(_SC_PAGESIZE); serverAssert(page == 4096);
    unsigned char *m = mmap(NULL, page*3, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    unsigned char *qmap = mmap(NULL, page*3, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    serverAssert(m != MAP_FAILED && qmap != MAP_FAILED);
    serverAssert(!mprotect(m+page,page,PROT_READ|PROT_WRITE));
    serverAssert(!mprotect(qmap+page,page,PROT_READ|PROT_WRITE));
    for (unsigned n=0;n<=16;n++) for(unsigned edge=0;edge<2;edge++) {
        zbtScoreLeaf *l=(zbtScoreLeaf *)(m+page+8);
        memset(l,0,offsetof(zbtScoreLeaf,data)); l->n.count=2;
        l->score_base=zbtScoreToOrdered(-0.0);
        unsigned char *r=m+page*2-n-1, *q=edge?qmap+page*2-n:qmap+page;
        for(unsigned i=0;i<n;i++)q[i]=(unsigned char)(i*67);
        zbtPackedWriteInline(r,q,n);
        zbtScoreLeafOffsets(l)[1]=zbtScoreLeafEncodeOffset(l,r-(unsigned char *)l);
        unsigned char *wrong=(unsigned char *)l+80;
        zbtPackedWriteInline(wrong,q,n?n:1);
        if(n)wrong[n]^=128;
        zbtScoreLeafOffsets(l)[0]=zbtScoreLeafEncodeOffset(l,80);
        zbtScoreLeafHashTags(l)[0]=zbtScoreLeafHashTags(l)[1]=255;
        for(unsigned reverse=0;reverse<2;reverse++) {
            l->reversed=reverse; outputs(l,0xff123456,q,n,1,reverse?0:1);
            for(unsigned i=0;i<n;i++) {
                q[i]^=64; outputs(l,0xff123456,q,n,0,0); q[i]^=64;
            }
        }
    }
    serverAssert(!munmap(m,page*3) && !munmap(qmap,page*3));
    /* Exact allocation ends independently exercise all source/query alignments. */
    for(unsigned n=0;n<=16;n++)for(unsigned sa=0;sa<8;sa++)for(unsigned qa=0;qa<8;qa++) {
        size_t off=80+sa; zbtScoreLeaf *l=calloc(1,off+1+n);
        unsigned char *a=malloc(qa+n+1), *q=a+qa; serverAssert(l&&a);
        l->n.count=1; l->score_base=zbtScoreToOrdered(-0.0);
        for(unsigned i=0;i<n;i++)q[i]=(unsigned char)(i*67);
        zbtPackedWriteInline((unsigned char *)l+off,q,n);
        zbtScoreLeafOffsets(l)[0]=zbtScoreLeafEncodeOffset(l,off);
        outputs(l,0,q,n,1,0); free(a);free(l);
    }
}
static void external_short(void) {
    for(unsigned n=0;n<=14;n++) {
        zbtreeSet *t=zbtreeCreate(); unsigned char q[16]={0,255,128};
        uint32_t hash=zbtreeMemberHash(q,n); uint8_t tag=hash>>24; double score=-0.0;
        zbtBuildElement e={.ptr=q,.len=n,.hash=hash,.external=zbtExternalDup(t,q,n)};
        zbtScoreLeaf *l=zbtScoreLeafBuild(t,1,&score,&e,&tag,ZBT_NEW_LEAF_ID,1);
        t->score_root=&l->n;t->score_first=t->score_last=l;t->length=1;
        invariant(t);serverAssert(zbtScoreLeafRecord(l,0)[0]==ZBT_PACKED_EXTERNAL);
        serverAssert(zbtRecordLengthCode(zbtScoreLeafOffsets(l)[0])==0);
        outputs(l,hash,q,n,1,0);outputs(l,hash^1,q,n,0,0);zbtreeFree(t);
    }
}
static void *copy_alloc(void *p) {size_t n=zmalloc_usable_size(p);void *q=zmalloc(n+16);memcpy(q,p,n);relocations++;return q;}
static void *move_plain(void *p){void *q=copy_alloc(p);zfree(p);return q;}
static void release(void *p){zfree(p);}
static zbtreeSet *relocate(zbtreeSet *t) {
    t=zbtreeDefragStart(t,move_plain);zbtreeDefragState s;zbtreeDefragStateReset(&s);
    unsigned long scanned;while(!zbtreeDefragStep(t,&s,copy_alloc,release,&scanned))invariant(t);
    invariant(t);serverAssert(zbtTestCheck(t));return t;
}
static void mutate(void) {
    enum{N=600};sds keys[N];zbtreeSet *t=zbtreeCreate();
    const size_t lens[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,253,254,319,320,384};
    for(unsigned i=0;i<N;i++) {
        size_t n=lens[i%22];if(!n&&i)n=17;
        unsigned char b[384];memset(b,255,sizeof(b));b[0]=i;b[1]=i>>8;b[2]=0;
        keys[i]=sdsnewlen(b,n);zbtreeInsertNew(t,-(double)i,keys[i],NULL);
        invariant(t);serverAssert(zbtTestCheck(t));mutations++;
    }
    for(unsigned i=0;i<N;i++) {
        unsigned j=(i*137)%N;zbtreeInsertPosition p;double old;
        serverAssert(zbtreeFindForAdd(t,keys[j],&old,&p));
        zbtreeUpdateScore(t,keys[j],i*0.125,&p);invariant(t);serverAssert(zbtTestCheck(t));mutations++;
    }
    zbtreeSet *copy=zbtreeDup(t);invariant(copy);copy=relocate(copy);zbtreeFree(copy);t=relocate(t);
    for(unsigned i=0;i<N;i+=3){serverAssert(zbtreeDelete(t,keys[i]));invariant(t);serverAssert(zbtTestCheck(t));mutations++;}
    while(zbtreeLength(t)){zbtreeDeleteEdge(t,zbtreeLength(t)%2);invariant(t);serverAssert(zbtTestCheck(t));mutations++;}
    zbtreeFree(t);for(unsigned i=0;i<N;i++)sdsfree(keys[i]);
    /* Bulk leaf construction and capped edge allocation put an empty record near4095. */
    t=zbtreeCreate();zbtreeInsertNewRaw(t,0,(unsigned char *)"",0,NULL);invariant(t);
    zbtreeAppendBatch *batch=zbtreeAppendBatchCreate(t);
    for(unsigned i=1;i<N;i++){unsigned char b[4]={i>>8,i,0,255};zbtreeAppendBatchAdd(batch,i,b,4);}
    zbtreeAppendBatchFinish(batch);invariant(t);serverAssert(zbtTestCheck(t));zbtreeFree(t);
}
int main(void) {
    uint8_t seed[16]={17,29,43};dictSetHashFunctionSeed(seed);
    synthetic();external_short();mutate();
    serverAssert(codes==0xffff && max_offset>=4080);
    printf("{\"passed\":true,\"invariants\":%lu,\"comparisons\":%lu,\"mutations\":%lu,"
           "\"relocations\":%lu,\"codes\":%u,\"max_offset\":%u}\n",
           invariants,comparisons,mutations,relocations,codes,max_offset);return 0;
}
