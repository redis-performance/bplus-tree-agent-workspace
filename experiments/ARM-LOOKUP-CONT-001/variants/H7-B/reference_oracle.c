/* Correctness only: reference discrimination, repair and mutation in resize. */
#include "zset_btree.c"
int __failed_tests, __test_num;
static unsigned long repairs, mutations, active_updates, cross_leaf_updates;

static void synthetic(int wide) {
    zbtreeSet *zs=zbtreeCreate();
    zbtIndexTableInit(zs,&zs->member_index,4,wide);
    zbtIndexTable *table=&zs->member_index;
    uint32_t base=wide ? 70000 : 100;
    uint32_t hash=UINT32_C(0x02000003);
    /* XOR bytes 0,1,0 trigger a false approximate candidate in slot1. Its
     * ID deliberately equals the wanted ID, so removing validation without
     * an exact mask would corrupt the unrelated entry during repair. */
    zbtIndexTableInsertRaw(table,hash,base);
    zbtIndexTableInsertRaw(table,hash^UINT32_C(0x01000000),base+1);
    zbtIndexTableInsertRaw(table,hash,base+1);
    zbtIndexBucket *bucket=NULL;unsigned int pos=UINT_MAX;
    serverAssert(zbtIndexTableFindReference(table,hash,base+1,&bucket,&pos));
    serverAssert(bucket==zbtIndexBucketAt(table,3) && pos==2);
    serverAssert(zbtIndexMove(zs,hash,base+1,base+2,0,NULL));
    serverAssert(zbtIndexGetId(table,bucket,1)==base+1);
    serverAssert(zbtIndexGetId(table,bucket,2)==base+2);repairs++;
    bucket=NULL;pos=UINT_MAX;
    serverAssert(!zbtIndexTableFindReference(table,hash,base+1,&bucket,&pos));
    serverAssert(bucket==NULL && pos==UINT_MAX);
    serverAssert(!zbtIndexMove(zs,hash,base+1,base+3,0,NULL));
    serverAssert(zbtIndexTableFindReference(table,hash^UINT32_C(0x01000000),base+1,&bucket,&pos));
    serverAssert(pos==1);repairs++;
    zbtreeFree(zs);
}

static void mutate(int wide) {
    enum {N=700};
    zbtreeSet *zs=zbtreeCreate();zbtreeReserve(zs,N);
    if (wide) zbtTestSkipLeafIds(zs,70000);
    sds keys[N];double scores[N];
    for (unsigned int i=0;i<N;i++) {
        unsigned char b[12]={0};memcpy(b,&i,sizeof(i));b[7]=255;
        keys[i]=sdsnewlen(b,sizeof(b));scores[i]=i;
        zbtreeInsertNew(zs,scores[i],keys[i],NULL);
    }
    while (zs->member_rehash) zbtIndexRehashStep(zs,64);
    serverAssert(zbtTestCheck(zs));
    for (unsigned int round=0;round<3;round++) {
        if (round) serverAssert(zbtIndexStartResize(zs,N*(round==1 ? 4 : 1),1));
        for (unsigned int step=0;step<N;step++) {
            unsigned int i=(step*317)%N;
            double old;zbtreeInsertPosition p;
            serverAssert(zbtreeFindForAdd(zs,keys[i],&old,&p));
            serverAssert(old==scores[i]);
            uint32_t oldid=((zbtScoreLeaf *)p.score_leaf)->id;
            active_updates+=zs->member_rehash!=NULL;
            scores[i]=(double)(round+1)*10000-step*2.0;
            zbtreeUpdateScore(zs,keys[i],scores[i],&p);
            zbtScoreLeaf *leaf=NULL;
            serverAssert(zbtIndexFind(zs,zbtreeMemberHash((unsigned char *)keys[i],sdslen(keys[i])),
                (unsigned char *)keys[i],sdslen(keys[i]),&old,&leaf,NULL,NULL,NULL));
            serverAssert(old==scores[i]);cross_leaf_updates+=leaf->id!=oldid;
            serverAssert(zbtTestCheck(zs));mutations++;
        }
        while (zs->member_rehash) zbtIndexRehashStep(zs,64);
        serverAssert(zbtTestCheck(zs));
    }
    for (unsigned int i=0;i<N;i++) {
        double score=-1;serverAssert(zbtreeScore(zs,keys[i],&score));
        serverAssert(score==scores[i]);
        if (i%3==0) {serverAssert(zbtreeDelete(zs,keys[i]));mutations++;}
        serverAssert(zbtTestCheck(zs));sdsfree(keys[i]);
    }
    zbtreeFree(zs);
}

int main(void) {
    uint8_t seed[16];for (unsigned int i=0;i<16;i++) seed[i]=43+29*i;
    dictSetHashFunctionSeed(seed);
    for (int wide=0;wide<2;wide++) {synthetic(wide);mutate(wide);}
    serverAssert(active_updates && cross_leaf_updates);
    printf("{\"passed\":true,\"synthetic_repairs\":%lu,\"mutations\":%lu,\"active_resize_updates\":%lu,\"cross_leaf_updates\":%lu}\n",
           repairs,mutations,active_updates,cross_leaf_updates);
}
