/* Read-only structural observations; every mutation uses the public API. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#define MAX_KEYS 14337
static sds keys[MAX_KEYS];
static double values[MAX_KEYS];
static unsigned char live[MAX_KEYS],seen[MAX_KEYS];
static unsigned count_keys,seed,case_no,stage;
static unsigned long checks,scan_calls,rebuild_cases,incremental_cases,active_cases;
#define CHECK(x) do{if(!(x)){fprintf(stderr,"seed=%u case=%u stage=%u line=%d: %s\n",seed,case_no,stage,__LINE__,#x);abort();}}while(0)
static uint64_t bits(double x){uint64_t v;memcpy(&v,&x,8);return v;}
static int compare(const void *ap,const void *bp){
    unsigned a=*(const unsigned*)ap,b=*(const unsigned*)bp;
    if(values[a]<values[b])return -1;if(values[a]>values[b])return 1;
    size_t al=sdslen(keys[a]),bl=sdslen(keys[b]);int c=memcmp(keys[a],keys[b],al<bl?al:bl);
    return c?c:(al>bl)-(al<bl);
}
static size_t sorted(unsigned *order){size_t n=0;for(unsigned i=0;i<count_keys;i++)if(live[i])order[n++]=i;qsort(order,n,sizeof(*order),compare);return n;}
static unsigned identify(const unsigned char *key,size_t len,double value){
    CHECK(len>=4);unsigned id=0;for(unsigned j=0;j<4;j++)id|=(unsigned)key[j]<<(8*j);
    CHECK(id<count_keys && live[id] && len==sdslen(keys[id]));
    CHECK(!memcmp(key,keys[id],len) && bits(value)==bits(values[id]));return id;
}
static void visit(void *ctx,const unsigned char *key,size_t len,double value){UNUSED(ctx);seen[identify(key,len,value)]=1;scan_calls++;}
static void scan(zbtreeSet *tree){
    memset(seen,0,count_keys);uint64_t cursor=0;unsigned steps=0;
    do{cursor=zbtreeScan(tree,cursor,7,visit,NULL);CHECK(++steps<100000);}while(cursor);
    for(unsigned i=0;i<count_keys;i++)CHECK(seen[i]==live[i]);
}
static void verify(zbtreeSet *tree){
    unsigned *order=zmalloc(count_keys*sizeof(*order));size_t n=sorted(order);
    CHECK(zbtreeLength(tree)==n);
    for(unsigned i=0;i<count_keys;i++){
        double score;CHECK(zbtreeScore(tree,keys[i],&score)==live[i]);
        if(live[i])CHECK(bits(score)==bits(values[i]));
        CHECK(zbtreeScoreRaw(tree,(unsigned char*)keys[i],sdslen(keys[i]),&score)==live[i]);
        if(live[i])CHECK(bits(score)==bits(values[i]));
    }
    CHECK(zbtreeScores(tree,NULL,0,NULL)==0);
    for(unsigned batch=0;batch<=16;batch++){
        sds members[16];double scores[18];unsigned mask=0;
        for(unsigned j=0;j<18;j++)scores[j]=-12345.5;
        for(unsigned j=0;j<batch;j++){unsigned id=(j%3==0?0:(j*997+case_no)%count_keys);members[j]=keys[id];if(live[id])mask|=1U<<j;}
        CHECK(zbtreeScores(tree,members,batch,scores+1)==mask);
        CHECK(bits(scores[0])==bits(-12345.5));
        for(unsigned j=batch+1;j<18;j++)CHECK(bits(scores[j])==bits(-12345.5));
        for(unsigned j=0;j<batch;j++)if(mask&(1U<<j)){
            unsigned id=(j%3==0?0:(j*997+case_no)%count_keys);CHECK(bits(scores[j+1])==bits(values[id]));
        }
    }
    for(int reverse=0;reverse<2;reverse++){
        zbtreeIterator it;CHECK(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));
        for(size_t i=0;i<n;i++){
            const unsigned char *key;size_t len;double value;unsigned id=order[reverse?n-1-i:i];
            CHECK(zbtreeIteratorNext(&it,reverse,&key,&len,&value));CHECK(identify(key,len,value)==id);
            if(i%97==0 || i+1==n){CHECK(zbtreeRank(tree,keys[id],reverse,&value)==(long)i);CHECK(bits(value)==bits(values[id]));}
        }
        CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    for(size_t i=0;i<n;i+=97){zbtreeIterator it;const unsigned char *key;size_t len;double value;
        CHECK(zbtreeIteratorSeekRank(tree,i,&it));CHECK(zbtreeIteratorNext(&it,0,&key,&len,&value));CHECK(identify(key,len,value)==order[i]);}
    zbtreeIterator end;CHECK(!zbtreeIteratorSeekRank(tree,n,&end));scan(tree);zfree(order);checks++;
}
static void exercise(unsigned n,unsigned deleted,unsigned position){
    count_keys=n;case_no++;stage=0;memset(live,0,sizeof(live));
    zbtreeSet *tree=zbtreeCreate();
    for(unsigned i=0;i<n;i++){zbtreeInsertNew(tree,values[i],keys[i],NULL);live[i]=1;}
    int active=tree->member_rehash!=NULL;
    CHECK(active==(n==7169 || n==14337));if(active)active_cases++;
    zbtreeSet *copy=zbtreeDup(tree);verify(copy);zbtreeFree(copy);
    scan(tree);CHECK((tree->member_rehash!=NULL)==active);
    unsigned *order=zmalloc(n*sizeof(*order));CHECK(sorted(order)==n);
    unsigned start=position==0?0:position==1?(n-deleted)/2:n-deleted;
    uint32_t before_id=tree->next_score_leaf_id;
    int rebuild=deleted>1024 && deleted>=n/10;stage=1;
    CHECK(zbtreeDeleteRangeByRank(tree,start,start+deleted-1)==deleted);
    for(unsigned i=start;i<start+deleted;i++)live[order[i]]=0;
    unsigned leaves=0;
    for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next){if(rebuild)CHECK(leaf->id==leaves);leaves++;}
    if(rebuild){CHECK(!tree->member_rehash && tree->next_score_leaf_id==leaves);rebuild_cases++;}
    else{CHECK(tree->next_score_leaf_id==before_id && leaves<before_id);incremental_cases++;}
    verify(tree);stage=2;copy=zbtreeDup(tree);zbtreeFree(tree);tree=copy;verify(tree);
    for(unsigned i=start;i<start+deleted;i++){unsigned id=order[i];zbtreeInsertNew(tree,values[id],keys[id],NULL);live[id]=1;}
    stage=3;verify(tree);CHECK(zbtreeLength(tree)==n);
    CHECK(zbtreeDeleteRangeByRank(tree,0,ULONG_MAX)==n);memset(live,0,n);stage=4;verify(tree);
    zbtreeFree(tree);zfree(order);
    printf("seed=%u case=%u n=%u cut=%u position=%u active=%d rebuild=%d PASS checks=%lu\n",seed,case_no,n,deleted,position,active,rebuild,checks);fflush(stdout);
}
int main(void){
    const unsigned sizes[]={7169,10240,10260,14337};
    const unsigned cuts[][2]={{1024,1025},{1024,1025},{1025,1026},{1432,1433}};
    const size_t lengths[]={8,319,320,321,1024};
    for(unsigned pass=0;pass<2;pass++){
        seed=pass?111:11;uint8_t hash_seed[16];for(unsigned i=0;i<16;i++)hash_seed[i]=(uint8_t)(seed+i*37);dictSetHashFunctionSeed(hash_seed);
        for(unsigned i=0;i<MAX_KEYS;i++){
            unsigned char buf[1024];size_t len=lengths[i%5];for(size_t j=0;j<len;j++)buf[j]=(unsigned char)(seed+i*13+j*37);
            for(unsigned j=0;j<4;j++)buf[j]=(unsigned char)(i>>(8*j));keys[i]=sdsnewlen(buf,len);values[i]=i<3?(i&1?-0.0:0.0):(double)(i/3);
        }
        for(unsigned s=0;s<4;s++)for(unsigned c=0;c<2;c++)for(unsigned p=0;p<3;p++)exercise(sizes[s],cuts[s][c],p);
        for(unsigned i=0;i<MAX_KEYS;i++)sdsfree(keys[i]);
    }
    CHECK(case_no==48 && rebuild_cases==24 && incremental_cases==24 && active_cases==24);
    printf("PASS cases=%u verifications=%lu rebuild=%lu incremental=%lu active_resize=%lu callbacks=%lu\n",case_no,checks,rebuild_cases,incremental_cases,active_cases,scan_calls);return 0;
}
