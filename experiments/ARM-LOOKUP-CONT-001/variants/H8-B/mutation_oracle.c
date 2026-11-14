/* Correctness only; lifecycle fixture adapted from this author's H6-B oracle.
 * No descriptor implementation or hypothesis is used here. */
#include "zset_btree.c"
int __failed_tests, __test_num;
static unsigned long tree_checks, lookup_checks, relocations, reversed_leaves;
static const unsigned lens[]={0,1,2,3,4,5,6,7,8,9,14,15,16,24,32,64,128,253,254,255,256,319,320,321,384};
static void check_find(zbtScoreLeaf *leaf,uint32_t hash,unsigned char *q,size_t n,int expected) {
    for (unsigned mask=0;mask<4;mask++) {
        double score=12345.0,want=-0.0;unsigned pos=UINT_MAX;
        int found=zbtScoreLeafFindMember(leaf,hash,q,n,mask&1 ? &score:NULL,mask&2 ? &pos:NULL);
        serverAssert(found==expected);
        serverAssert(found && (mask&1) ? memcmp(&score,&want,sizeof(score))==0:score==12345.0);
        serverAssert(pos==(found && (mask&2) ? 0:UINT_MAX));lookup_checks++;
    }
}
static unsigned inspect(zbtreeSet *zs) {
    serverAssert(zbtTestCheck(zs));unsigned leaves=0;
    for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next) {
        leaves++;reversed_leaves+=leaf->reversed!=0;
        for (unsigned i=0;i<leaf->n.count;i++) {
            size_t n;const unsigned char *q=zbtScoreLeafElement(leaf,i,&n);
            double want=zbtScoreLeafScore(leaf,i);
            uint32_t hash=zbtScoreLeafHash(leaf,i);
            for (unsigned mask=0;mask<4;mask++) {
                double score=12345.0;unsigned pos=UINT_MAX;
                serverAssert(zbtScoreLeafFindMember(leaf,hash,q,n,mask&1 ? &score:NULL,mask&2 ? &pos:NULL));
                serverAssert(mask&1 ? memcmp(&score,&want,sizeof(score))==0:score==12345.0);
                serverAssert(pos==(mask&2 ? i:UINT_MAX));lookup_checks++;
            }
        }
    }
    tree_checks++;return leaves;
}
static void *copy_allocation(void *old) {
    size_t n=zmalloc_usable_size(old);void *p=malloc(n);serverAssert(p);
    memcpy(p,old,n);relocations++;return p;
}
static void *move_plain(void *old) {void *p=copy_allocation(old);free(old);return p;}
static void external_short_writers(void) {
    unsigned char bytes[8]={0,255,0,1,2,3,4,5};
    for(unsigned int len=0;len<=8;len++) {
        zbtreeSet *zs=zbtreeCreate();
        uint32_t hash=zbtreeMemberHash(bytes,len);
        zbtBuildElement element;zbtBuildElementFromBytes(&element,bytes,len,hash);
        element.external=zbtExternalDup(zs,bytes,len);
        zbtIndexExpandIfNeeded(zs,1);
        zbtScoreLeaf *leaf=zbtScoreInsert(zs,-0.0,&element);
        zs->length++;zbtIndexInsert(zs,hash,leaf->id,NULL);inspect(zs);
        for(unsigned int stage=0;stage<3;stage++) {
            leaf=zs->score_first;
            serverAssert(zbtScoreLeafRecord(leaf,0)[0]==ZBT_PACKED_EXTERNAL);
            check_find(leaf,hash,bytes,len,1);check_find(leaf,hash^1,bytes,len,0);
            if(stage==0)zbtScoreCompactLeaf(zs,leaf);
            if(stage==1) {zbtreeSet *copy=zbtreeDup(zs);zbtreeFree(zs);zs=copy;}
            inspect(zs);
        }
        zbtreeFree(zs);
    }
}

static void mutations(void) {
    enum {N=600};sds keys[N];double scores[N];int alive[N];
    zbtreeSet *zs=zbtreeCreate();
    for(unsigned int i=0;i<N;i++) {
        unsigned int len=i<8 ? i:lens[4+i%(sizeof(lens)/sizeof(lens[0])-4)];
        unsigned char bytes[512];memset(bytes,(i%255)+1,sizeof(bytes));
        if(i>=8)memcpy(bytes,&i,sizeof(i));
        keys[i]=sdsnewlen(bytes,len);alive[i]=1;scores[i]=i%2 ? -(double)i:(double)i;
        zbtreeInsertNewRaw(zs,scores[i],(unsigned char *)keys[i],len,NULL);
        inspect(zs);
    }
    unsigned int full_leaves=inspect(zs);serverAssert(full_leaves>=3);
    for(unsigned int i=0;i<N;i+=3) {
        zbtreeInsertPosition position;
        serverAssert(zbtreeFindForAdd(zs,keys[i],NULL,&position));
        scores[i]=(i%2 ? 1e40:-1e40)+(double)i;
        zbtreeUpdateScore(zs,keys[i],scores[i],&position);inspect(zs);
    }
    /* Explicitly rebuild every leaf and check hints against its new records. */
    for(zbtScoreLeaf *leaf=zs->score_first;leaf;) {
        leaf=zbtScoreCompactLeaf(zs,leaf);inspect(zs);leaf=leaf->next;
    }
    zbtreeSet *copy=zbtreeDup(zs);inspect(copy);zbtreeFree(zs);zs=copy;
    while(zs->member_rehash)zbtIndexRehashStep(zs,1);
    serverAssert(zbtIndexStartResize(zs,N*4,1));
    zs=zbtreeDefragStart(zs,move_plain);inspect(zs);
    zbtreeDefragState state;zbtreeDefragStateReset(&state);
    unsigned long scanned;int done;
    do {done=zbtreeDefragStep(zs,&state,copy_allocation,free,&scanned);inspect(zs);} while(!done);
    for(unsigned int i=0;i<N;i++) {
        double score=0;serverAssert(zbtreeScoreRaw(zs,(unsigned char *)keys[i],sdslen(keys[i]),&score));
        serverAssert(memcmp(&score,&scores[i],sizeof(score))==0);
        if(i%5) {serverAssert(zbtreeDelete(zs,keys[i]));alive[i]=0;inspect(zs);}
    }
    serverAssert(inspect(zs)<full_leaves);
    for(unsigned int i=0;i<N;i++) {
        double score=123;int found=zbtreeScoreRaw(zs,(unsigned char *)keys[i],sdslen(keys[i]),&score);
        serverAssert(found==alive[i]);if(!found)serverAssert(score==123);
    }
    zbtreeDeleteRangeByRank(zs,20,40);inspect(zs);
    unsigned int reverse=0;
    while(zs->length) {zbtreeDeleteEdge(zs,reverse++%2);inspect(zs);}
    zbtreeFree(zs);for(unsigned int i=0;i<N;i++)sdsfree(keys[i]);
}

int main(void) {
    uint8_t seed[16];for(unsigned i=0;i<16;i++)seed[i]=i*29+17;
    dictSetHashFunctionSeed(seed);external_short_writers();mutations();
    serverAssert(relocations && reversed_leaves);
    printf("{\"passed\":true,\"tree_checks\":%lu,\"lookup_checks\":%lu,\"relocations\":%lu,\"reversed_leaves\":%lu}\n",tree_checks,lookup_checks,relocations,reversed_leaves);
}
