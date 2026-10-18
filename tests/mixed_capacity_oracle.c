/* Additive semantic oracle. Capacity adapters are diagnostic, never timing hosts. */
#include "../src/zset_btree.c"
#include <float.h>
#include <inttypes.h>
#define MAXN 513
static sds keys[MAXN];
static double scores[MAXN];
static unsigned char live[MAXN];
static unsigned nkeys, stage;
static uint64_t checks, exact, fixtures, edits, scans, logical_hash=UINT64_C(14695981039346656037);
static uint64_t layout_hash=UINT64_C(14695981039346656037), widths[65], shifts[65], orientations[2];
static uint64_t growth, shrinkage, masks[8];
static uint64_t bits(double x) {uint64_t u;memcpy(&u,&x,8);return u;}
static double frombits(uint64_t u) {double x;memcpy(&x,&u,8);return x;}
static void mix(uint64_t *h,uint64_t u) {*h=(*h^u)*UINT64_C(1099511628211);}
static uint64_t rng_next(uint64_t *s) {
    uint64_t z=(*s+=UINT64_C(0x9e3779b97f4a7c15));
    z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);return z^(z>>31);
}
static void equal_score(double actual,double expected) {
    if(bits(actual)!=bits(expected)) {
        fprintf(stderr,"exact-score actual=%016"PRIx64" expected=%016"PRIx64" stage=%u\n",bits(actual),bits(expected),stage);abort();
    }
    exact++;
}
static int compare(const void *ap,const void *bp) {
    unsigned a=*(const unsigned *)ap,b=*(const unsigned *)bp;
    if(scores[a]<scores[b])return -1;if(scores[a]>scores[b])return 1;
    size_t an=sdslen(keys[a]),bn=sdslen(keys[b]);int c=memcmp(keys[a],keys[b],an<bn?an:bn);
    return c?c:(an>bn)-(an<bn);
}
static unsigned ordered(unsigned *order) {
    unsigned n=0;for(unsigned i=0;i<nkeys;i++)if(live[i])order[n++]=i;
    qsort(order,n,sizeof(*order),compare);return n;
}
/* No tree score conversion/bit-read helper participates in this decoder. */
static double scalar_score(const zbtScoreLeaf *leaf,unsigned logical) {
    unsigned physical=leaf->reversed?leaf->n.count-1-logical:logical;
    size_t pos=(size_t)physical*leaf->score_bits;uint64_t delta=0;
    for(unsigned b=0;b<leaf->score_bits;b++)delta|=(uint64_t)((leaf->data[(pos+b)/8]>>((pos+b)%8))&1)<<b;
    serverAssert(leaf->n.score_shift<=64 && (!delta || leaf->n.score_shift<64));
    delta=leaf->n.score_shift==64?0:delta<<leaf->n.score_shift;
    uint64_t value=leaf->reversed?leaf->score_base-delta:leaf->score_base+delta;
    return frombits(value>>63?value^UINT64_C(0x8000000000000000):~value);
}
static uint64_t node_count(zbtScoreNode *node,zbtScoreInner *parent,unsigned slot) {
    if(!node)return 0;
    serverAssert(node->parent==parent && (!parent || node->parent_index==slot));
    uint64_t n=0;
    if(node->isleaf)n=node->count;
    else {
        zbtScoreInner *inner=(zbtScoreInner *)node;
        for(unsigned i=0;i<node->count;i++) {
            uint64_t child=node_count(inner->child[i],inner,i);
            serverAssert(inner->child_count[i]==child);n+=child;
        }
    }
    serverAssert(node->subtree==n);return n;
}
static unsigned leaf_count(zbtreeSet *tree) {
    unsigned n=0;for(zbtScoreLeaf *p=tree->score_first;p;p=p->next)n++;return n;
}
static void observe_edit(zbtreeSet *tree,unsigned before) {
    unsigned after=leaf_count(tree);growth+=after>before;shrinkage+=after<before;edits++;
}
static void scan_cb(void *ctx,const unsigned char *ele,size_t len,double score) {
    unsigned *seen=ctx,id=MAXN;
    for(unsigned i=0;i<nkeys;i++)if(sdslen(keys[i])==len&&!memcmp(keys[i],ele,len)){id=i;break;}
    /* SCAN permits duplicates even after rehash settles: displaced home groups overlap. */
    serverAssert(id<nkeys && live[id]);seen[id]++;equal_score(score,scores[id]);scans++;
}
static void item(zbtreeIterator *it,int reverse,unsigned id,unsigned mask) {
    const unsigned char sentinel=21,*ele=&sentinel;size_t len=SIZE_MAX;double score=71.5;
    serverAssert(zbtreeIteratorNext(it,reverse,mask&1?&ele:NULL,mask&2?&len:NULL,mask&4?&score:NULL));
    if(mask&1)serverAssert(!memcmp(ele,keys[id],sdslen(keys[id])));else serverAssert(ele==&sentinel);
    if(mask&2)serverAssert(len==sdslen(keys[id]));else serverAssert(len==SIZE_MAX);
    if(mask&4)equal_score(score,scores[id]);else serverAssert(score==71.5);
    masks[mask]++;
}
static void verify(zbtreeSet *tree) {
    /* Settled read-only oracle: active-resize behavior has separate suites. */
    while(tree->member_rehash)zbtIndexRehashStep(tree,64);
    size_t owned=zbtreeAllocSize(tree);unsigned order[MAXN],n=ordered(order),at=0;
    serverAssert(zbtreeLength(tree)==n && node_count(tree->score_root,NULL,0)==n);
    zbtScoreLeaf *prev=NULL;
    for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next) {
        serverAssert(leaf->prev==prev && leaf->n.count && zbtScoreLeafById(tree,leaf->id)==leaf);
        prev=leaf;serverAssert(leaf->score_bits<=64);widths[leaf->score_bits]++;shifts[leaf->n.score_shift]++;orientations[!!leaf->reversed]++;
        mix(&layout_hash,leaf->n.count);mix(&layout_hash,leaf->score_bits);mix(&layout_hash,leaf->n.score_shift);
        mix(&layout_hash,leaf->reversed);mix(&layout_hash,leaf->score_base);mix(&layout_hash,zmalloc_usable_size(leaf));
        for(unsigned j=0;j<leaf->n.count;j++) {
            serverAssert(at<n);unsigned id=order[at++];
            equal_score(scalar_score(leaf,j),scores[id]);equal_score(zbtScoreLeafScore(leaf,j),scores[id]);
            size_t len;const unsigned char *ele=zbtScoreLeafElement(leaf,j,&len);
            serverAssert(len==sdslen(keys[id]) && !memcmp(ele,keys[id],len));
        }
    }
    serverAssert(at==n && prev==tree->score_last);mix(&logical_hash,n);
    for(unsigned j=0;j<n;j++){mix(&logical_hash,order[j]);mix(&logical_hash,bits(scores[order[j]]));}
    for(int reverse=0;reverse<2;reverse++) {
        zbtreeIterator it;serverAssert(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));
        for(unsigned j=0;j<n;j++) {
            unsigned k=reverse?n-1-j:j,id=order[k];item(&it,reverse,id,(j+stage)&7);
            double score;serverAssert(zbtreeRank(tree,keys[id],reverse,&score)==(long)j);equal_score(score,scores[id]);
            zbtreeIterator seek;serverAssert(zbtreeIteratorSeekRank(tree,k,&seek));item(&seek,reverse,id,7);
        }
        serverAssert(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    const double bounds[]={-DBL_MAX,-DBL_MIN,-0.0,+0.0,DBL_MIN,1.0,DBL_MAX};
    for(unsigned b=0;b<sizeof(bounds)/sizeof(*bounds);b++)for(int ex=0;ex<2;ex++) {
        unsigned want=0;for(unsigned j=0;j<n;j++)want+=ex?scores[order[j]]>bounds[b]:scores[order[j]]>=bounds[b];
        serverAssert(zbtreeCountByScore(tree,bounds[b],ex,DBL_MAX,0)==want);
        for(int reverse=0;reverse<2;reverse++) {
            unsigned k=n;
            for(unsigned j=0;j<n;j++) {
                unsigned p=reverse?n-1-j:j;double s=scores[order[p]];
                if(reverse?(ex?s<bounds[b]:s<=bounds[b]):(ex?s>bounds[b]:s>=bounds[b])){k=p;break;}
            }
            zbtreeIterator seek;unsigned long rank=ULONG_MAX;
            serverAssert(zbtreeIteratorSeekScore(tree,bounds[b],ex,reverse,&seek,&rank)==(k<n));
            if(k<n){serverAssert(rank==k);item(&seek,reverse,order[k],7);}
        }
    }
    for(unsigned i=0;i<nkeys;i++) {
        double score;serverAssert(zbtreeScore(tree,keys[i],&score)==live[i]);if(live[i])equal_score(score,scores[i]);
        serverAssert(zbtreeScoreRaw(tree,(const unsigned char *)keys[i],sdslen(keys[i]),&score)==live[i]);if(live[i])equal_score(score,scores[i]);
    }
    for(unsigned i=0;i<nkeys;i+=16) {
        unsigned count=nkeys-i<16?nkeys-i:16,want=0;double out[16];
        for(unsigned j=0;j<count;j++){out[j]=71.5;if(live[i+j])want|=1u<<j;}
        serverAssert(zbtreeScores(tree,keys+i,count,out)==want);
        for(unsigned j=0;j<count;j++)if(live[i+j])equal_score(out[j],scores[i+j]);
    }
    unsigned seen[MAXN]={0};uint64_t cursor=0;unsigned calls=0;
    do {cursor=zbtreeScan(tree,cursor,7,scan_cb,seen);serverAssert(++calls<10000);}while(cursor);
    for(unsigned i=0;i<nkeys;i++)serverAssert((seen[i]!=0)==live[i]);
    serverAssert(zbtreeAllocSize(tree)==owned);checks++;
}
static double value(unsigned family,unsigned i,unsigned turn) {
    static const double wide[]={-DBL_MAX,-0x1p53,-32769,-129,-1,-DBL_MIN,-DBL_TRUE_MIN,-0.0,+0.0,DBL_TRUE_MIN,DBL_MIN,0.25,127,128,32768,0x1p53,DBL_MAX};
    if(family==1)return wide[(i+turn)%17];
    if(family==2)return (double)((int)((i*127u+turn*13u)%65537)-32768);
    /* Adjacent exponent/mantissa boundaries; finite by construction. */
    uint64_t base=UINT64_C(0x3ff0000000000000),delta=(uint64_t)(i+turn)%129;
    return frombits(base+delta);
}
static void exercise(unsigned n,unsigned family,uint64_t seed) {
    nkeys=n;stage=0;uint64_t rng=seed;uint8_t hs[16];for(unsigned i=0;i<16;i++)hs[i]=rng_next(&rng);dictSetHashFunctionSeed(hs);
    const size_t lens[]={2,3,8,16,253,254,319,320,321,511};unsigned order[MAXN];
    for(unsigned i=0;i<n;i++) {
        unsigned char buf[511];size_t len=i?lens[i%10]:0;memset(buf,0,len);
        if(len){buf[0]=i>>8;buf[1]=i;for(size_t j=3;j<len;j++)buf[j]=(unsigned char)(j*17+i);}
        keys[i]=sdsnewlen(buf,len);scores[i]=value(family,i,0);live[i]=1;order[i]=i;
    }
    qsort(order,n,sizeof(*order),compare);zbtreeSet *tree=zbtreeCreate();
    /* Descending construction exercises prefix movement; later minimum drains reverse. */
    for(unsigned j=0;j<n;j++){unsigned i=order[n-1-j],before=leaf_count(tree);zbtreeInsertNew(tree,scores[i],keys[i],NULL);observe_edit(tree,before);}
    verify(tree);
    for(stage=1;stage<=256 && n;stage++) {
        unsigned id=rng_next(&rng)%n,action=rng_next(&rng)%4,before=leaf_count(tree);
        if(live[id] && action==0){serverAssert(zbtreeDelete(tree,keys[id]));live[id]=0;}
        else if(!live[id]){scores[id]=value((family+stage)%3,id,stage);zbtreeInsertNew(tree,scores[id],keys[id],NULL);live[id]=1;}
        else {zbtreeInsertPosition pos;double old;serverAssert(zbtreeFindForAdd(tree,keys[id],&old,&pos));equal_score(old,scores[id]);
            double target=value((family+stage)%3,id,stage);zbtreeUpdateScore(tree,keys[id],target,&pos);scores[id]=target;}
        observe_edit(tree,before);if(stage%16==0)verify(tree);
    }
    verify(tree);zbtreeSet *copy=zbtreeDup(tree);verify(copy);
    unsigned char saved[MAXN];memcpy(saved,live,sizeof(live));unsigned count=ordered(order);
    if(count) {
        unsigned lo=count/4,hi=count*3/4,before=leaf_count(copy);
        serverAssert(zbtreeDeleteRangeByRank(copy,lo,hi)==hi-lo+1);
        for(unsigned i=lo;i<=hi;i++)live[order[i]]=0;observe_edit(copy,before);verify(copy);
    }
    /* Refill only deleted/absent keys. The original clone source stays immutable. */
    for(unsigned i=0;i<n;i++)if(!live[i]){unsigned before=leaf_count(copy);zbtreeInsertNew(copy,scores[i],keys[i],NULL);live[i]=1;observe_edit(copy,before);}
    verify(copy);count=ordered(order);
    for(unsigned j=0;j<count;j++) {
        unsigned before=leaf_count(copy);zbtreeDeleteEdge(copy,0);live[order[j]]=0;observe_edit(copy,before);
        if(j%16==0 || j+1==count)verify(copy);
    }
    verify(copy);zbtreeFree(copy);memcpy(live,saved,sizeof(live));verify(tree);zbtreeFree(tree);
    for(unsigned i=0;i<n;i++)sdsfree(keys[i]);fixtures++;
#if CAPACITY_QUANTUM
    extern size_t diagnostic_outstanding(void);serverAssert(diagnostic_outstanding()==0);
#endif
    printf("FIXTURE n=%u family=%u seed=%"PRIu64" checks=%"PRIu64" logical=%016"PRIx64"\n",n,family,seed,checks,logical_hash);fflush(stdout);
}
int main(void) {
    const unsigned ns[]={0,1,2,31,32,33,63,64,65,95,96,97,127,128,129,513};
    const uint64_t seeds[]={42101,42109};
    for(unsigned s=0;s<2;s++)for(unsigned n=0;n<16;n++)for(unsigned f=0;f<3;f++)exercise(ns[n],f,seeds[s]);
    uint64_t partial=0,shifted=0;for(unsigned i=1;i<64;i++)partial+=widths[i];for(unsigned i=1;i<=64;i++)shifted+=shifts[i];
    serverAssert(fixtures==96 && widths[0] && widths[64] && partial && shifted && orientations[0] && orientations[1] && growth && shrinkage);
    for(unsigned i=0;i<8;i++)serverAssert(masks[i]);
    printf("PASS fixtures=%"PRIu64" checks=%"PRIu64" exact=%"PRIu64" edits=%"PRIu64" scans=%"PRIu64" logical=%016"PRIx64"\n",fixtures,checks,exact,edits,scans,logical_hash);
    printf("PHYSICAL layout=%016"PRIx64" zero=%"PRIu64" partial=%"PRIu64" full=%"PRIu64" shifted=%"PRIu64" forward=%"PRIu64" reversed=%"PRIu64" growth=%"PRIu64" shrinkage=%"PRIu64"\n",layout_hash,widths[0],partial,widths[64],shifted,orientations[0],orientations[1],growth,shrinkage);
}
