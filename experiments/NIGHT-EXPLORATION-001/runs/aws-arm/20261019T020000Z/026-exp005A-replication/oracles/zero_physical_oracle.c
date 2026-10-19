/* Real mutation paths with equal numeric scores and distinct IEEE zero bits. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#define MAXN 513
static sds keys[MAXN];
static double scores[MAXN];
static unsigned char live[MAXN];
static unsigned nkeys;
static uint64_t checks, exact, forward_leaves, reversed_leaves, reversal_opportunities;
static uint64_t bits(double x) { uint64_t u; memcpy(&u,&x,8); return u; }
static uint64_t scalar(const unsigned char *p,size_t pos,unsigned width) {
    uint64_t u=0;
    for(unsigned b=0;b<width;b++) u|=(uint64_t)((p[(pos+b)/8]>>((pos+b)%8))&1)<<b;
    return u;
}
static void equal_bits(double actual,double expected) {
    if(bits(actual)!=bits(expected)) {
        fprintf(stderr,"exact-score actual=%016"PRIx64" expected=%016"PRIx64"\n",bits(actual),bits(expected));
        abort();
    }
    exact++;
}
static void verify(zbtreeSet *tree) {
    /* Queries can advance rehash; settle that mutation before read-only memory guard. */
    while(tree->member_rehash) zbtIndexRehashStep(tree,64);
    size_t owned=zbtreeAllocSize(tree); unsigned order[MAXN],n=0;
    for(unsigned i=0;i<nkeys;i++) if(live[i]) order[n++]=i;
    serverAssert(zbtreeLength(tree)==n);
    unsigned at=0; zbtScoreLeaf *prev=NULL;
    for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next) {
        serverAssert(leaf->prev==prev && leaf->n.count && zbtScoreLeafById(tree,leaf->id)==leaf);
        prev=leaf; forward_leaves+=!leaf->reversed; reversed_leaves+=!!leaf->reversed;
        for(unsigned j=0;j<leaf->n.count;j++) {
            serverAssert(at<n); unsigned id=order[at++];
            unsigned physical=leaf->reversed?leaf->n.count-1-j:j;
            uint64_t delta=scalar(leaf->data,(size_t)physical*leaf->score_bits,leaf->score_bits);
            serverAssert(!delta || leaf->n.score_shift<64);
            delta=leaf->n.score_shift==64?0:delta<<leaf->n.score_shift;
            uint64_t ordered=leaf->reversed?leaf->score_base-delta:leaf->score_base+delta;
            uint64_t ieee=ordered>>63?ordered^UINT64_C(0x8000000000000000):~ordered;
            double decoded;memcpy(&decoded,&ieee,8);equal_bits(decoded,scores[id]);
            equal_bits(zbtScoreLeafScore(leaf,j),scores[id]);
            size_t len;const unsigned char *ele=zbtScoreLeafElement(leaf,j,&len);
            serverAssert(len==sdslen(keys[id])&&!memcmp(ele,keys[id],len));
        }
    }
    serverAssert(at==n && prev==tree->score_last);
    for(int reverse=0;reverse<2;reverse++) {
        zbtreeIterator it;serverAssert(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));
        for(unsigned j=0;j<n;j++) {
            unsigned id=order[reverse?n-1-j:j];const unsigned char *ele;size_t len;double score;
            serverAssert(zbtreeIteratorNext(&it,reverse,&ele,&len,&score));
            serverAssert(len==sdslen(keys[id])&&!memcmp(ele,keys[id],len));equal_bits(score,scores[id]);
            serverAssert(zbtreeRank(tree,keys[id],reverse,&score)==(long)j);equal_bits(score,scores[id]);
        }
        serverAssert(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    for(unsigned i=0;i<nkeys;i++) {
        double score;serverAssert(zbtreeScore(tree,keys[i],&score)==live[i]);
        if(live[i])equal_bits(score,scores[i]);
    }
    serverAssert(zbtreeCountByScore(tree,-0.0,0,+0.0,0)==n);
    serverAssert(zbtreeCountByScore(tree,-0.0,1,+0.0,0)==0);
    serverAssert(zbtreeAllocSize(tree)==owned);checks++;
}
static void exercise(unsigned n,size_t bytes,int descending,unsigned seed) {
    nkeys=n;uint8_t hs[16];for(unsigned i=0;i<16;i++)hs[i]=(seed>>(i%4*8))^i;dictSetHashFunctionSeed(hs);
    zbtreeSet *tree=zbtreeCreate();
    for(unsigned i=0;i<n;i++) {
        unsigned char buf[320];memset(buf,0,bytes);buf[0]=i>>8;buf[1]=i;
        for(size_t j=3;j<bytes;j++)buf[j]=(unsigned char)(j*17+i);
        keys[i]=sdsnewlen(buf,bytes);scores[i]=(i%2)?+0.0:-0.0;live[i]=1;
    }
    for(unsigned j=0;j<n;j++){unsigned i=descending?n-1-j:j;zbtreeInsertNew(tree,scores[i],keys[i],NULL);}
    verify(tree);
    /* Both signs are present in each dense leaf; numeric-equality early return is wrong. */
    for(unsigned i=0;i<n;i++) {
        zbtreeInsertPosition pos;double old;serverAssert(zbtreeFindForAdd(tree,keys[i],&old,&pos));equal_bits(old,scores[i]);
        scores[i]=-scores[i];zbtreeUpdateScore(tree,keys[i],scores[i],&pos);verify(tree);
    }
    zbtreeSet *copy=zbtreeDup(tree);verify(copy);
    for(unsigned i=0;i<n;i++) {
        zbtScoreLeaf *first=copy->score_first;
        reversal_opportunities+=first->n.count>1&&!first->reversed;
        serverAssert(zbtreeDelete(copy,keys[i]));live[i]=0;verify(copy);
    }
    zbtreeFree(copy);for(unsigned i=0;i<n;i++)live[i]=1;verify(tree);
    /* Refill emptied clone via descending insertion, then consume alternating ends. */
    copy=zbtreeCreate();for(unsigned j=0;j<n;j++){unsigned i=n-1-j;zbtreeInsertNew(copy,scores[i],keys[i],NULL);}verify(copy);
    unsigned lo=0,hi=n-1;
    for(unsigned j=0;j<n;j++){int rev=j&1;unsigned i=rev?hi--:lo++;zbtreeDeleteEdge(copy,rev);live[i]=0;verify(copy);}
    zbtreeFree(copy);for(unsigned i=0;i<n;i++)live[i]=1;verify(tree);zbtreeFree(tree);
    for(unsigned i=0;i<n;i++)sdsfree(keys[i]);
    printf("PASS n=%u bytes=%zu descending=%d seed=%u checks=%"PRIu64" exact=%"PRIu64"\n",n,bytes,descending,seed,checks,exact);fflush(stdout);
}
int main(void) {
    unsigned ns[]={97,513},seeds[]={19001,19009};size_t lengths[]={16,319,320};
    for(unsigned s=0;s<2;s++)for(unsigned n=0;n<2;n++)for(unsigned l=0;l<3;l++)for(int d=0;d<2;d++)exercise(ns[n],lengths[l],d,seeds[s]);
    serverAssert(forward_leaves && reversed_leaves && reversal_opportunities);
    printf("PASS checks=%"PRIu64" exact=%"PRIu64" forward_leaves=%"PRIu64" reversed_leaves=%"PRIu64" reversal_opportunities=%"PRIu64"\n",checks,exact,forward_leaves,reversed_leaves,reversal_opportunities);
}
