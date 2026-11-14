/* Correctness only: no timing, counter collection or throughput output. */
#include "zset_btree.c"

int __failed_tests, __test_num;
static unsigned long filter_checks, hit_checks, miss_checks, reference_checks;
static unsigned long wrapped_hits, wide_hits, tombstone_checks, resize_checks, final_steps;

/* Independent expression for the unchanged three-bit filter definition. */
static uint64_t expected_bits(unsigned int high) {
    uint64_t tag=high ? high : 1;
    uint64_t product=tag*UINT64_C(0x9e3779b97f4a7c15);
    unsigned int positions[3]={(unsigned int)(tag%64),
        (unsigned int)(product/UINT64_C(0x400000000000000)),
        (unsigned int)((product/UINT64_C(0x1000000000))%64)};
    uint64_t result=0;
    for (unsigned int i=0;i<3;i++) result|=UINT64_C(1)<<positions[i];
    return result;
}

static void filters(void) {
    for (int wide=0;wide<2;wide++) {
        zbtreeSet *zs=zbtreeCreate();
        zbtIndexTableInit(zs,&zs->member_index,4,wide);
        zbtIndexTable *table=&zs->member_index;
        unsigned long home=table->size-1;
        for (unsigned int recorded=0;recorded<256;recorded++) {
            *zbtIndexHomeTagsAt(table,home)=0;
            uint32_t hash=((uint32_t)recorded<<24)|(uint32_t)home;
            serverAssert(!zbtIndexHomeMayContain(table,hash));
            zbtIndexRecordHomeTag(table,hash);
            serverAssert(*zbtIndexHomeTagsAt(table,home)==expected_bits(recorded));
            for (unsigned int queried=0;queried<256;queried++) {
                uint64_t want=expected_bits(queried);
                uint32_t query=((uint32_t)queried<<24)|(uint32_t)home;
                int expected=(expected_bits(recorded)&want)==want;
                serverAssert(zbtIndexHomeMayContain(table,query)==expected);
                filter_checks++;
            }
        }
        /* A saturated filter is allowed to produce false positives. */
        *zbtIndexHomeTagsAt(table,home)=UINT64_MAX;
        unsigned char missing=0;
        for (unsigned int high=0;high<256;high++) {
            uint32_t hash=((uint32_t)high<<24)|(uint32_t)home;
            serverAssert(zbtIndexHomeMayContain(table,hash));
            serverAssert(!zbtIndexTableFind(zs,table,hash,&missing,1,
                NULL,NULL,NULL,NULL,NULL,NULL,NULL));
            filter_checks++;
        }
        zbtreeFree(zs);
    }
}

#define COLLIDERS (2*ZBT_INDEX_BUCKET_ITEMS+3)
static void lookup(zbtreeSet *zs, uint32_t hash, unsigned int number,
                     zbtScoreLeaf *expected_leaf, int expected,
                     zbtIndexBucket **hint, unsigned int *hint_pos) {
    uint64_t key=number;
    double score=12345.0;
    zbtScoreLeaf *leaf=NULL;
    unsigned int score_pos=UINT_MAX,pos=UINT_MAX;
    zbtIndexBucket *bucket=NULL;
    int found=zbtIndexTableFind(zs,&zs->member_index,hash,
        (unsigned char *)&key,sizeof(key),&score,&leaf,&score_pos,
        &bucket,&pos,hint,hint_pos);
    serverAssert(found==expected);
    if (found) {
        serverAssert(leaf==expected_leaf && score_pos==0 && score==(double)number+0.25);
        serverAssert(zbtIndexGetId(&zs->member_index,bucket,pos)==leaf->id);
        serverAssert(zbtIndexTableFind(zs,&zs->member_index,hash,
            (unsigned char *)&key,sizeof(key),NULL,NULL,NULL,NULL,NULL,NULL,NULL));
        zbtIndexBucket *reference=NULL;unsigned int reference_pos=UINT_MAX;
        serverAssert(zbtIndexTableFindReference(&zs->member_index,hash,leaf->id,
                                                &reference,&reference_pos));
        serverAssert(reference==bucket && reference_pos==pos);
        reference_checks++;
        if ((unsigned char *)bucket < (unsigned char *)zbtIndexBucketAt(
                &zs->member_index,hash&(zs->member_index.size-1))) wrapped_hits++;
        if (leaf->id>UINT16_MAX) wide_hits++;
        hit_checks++;
    } else {
        serverAssert(score==12345.0 && leaf==NULL && score_pos==UINT_MAX && bucket==NULL);
        miss_checks++;
    }
}

static zbtScoreLeaf *make_leaf(zbtreeSet *zs, unsigned int number, uint32_t hash) {
    uint64_t key=number;double score=(double)number+0.25;
    zbtBuildElement ele={.ptr=(unsigned char *)&key,.len=sizeof(key),.hash=hash};
    uint8_t tag=hash>>24;
    return zbtScoreLeafBuild(zs,1,&score,&ele,&tag,ZBT_NEW_LEAF_ID,0);
}

static void probing(int wide, unsigned int mode) {
    zbtreeSet *zs=zbtreeCreate();
    zbtIndexTableInit(zs,&zs->member_index,4,wide);
    zbtIndexTable *table=&zs->member_index;
    unsigned int base=wide ? 70000 : 0;
    zs->score_leaf_cap=base+COLLIDERS+4;
    zs->score_leaf_by_id=zbtAlloc(zs,zs->score_leaf_cap*sizeof(*zs->score_leaf_by_id));
    memset(zs->score_leaf_by_id,0,zs->score_leaf_cap*sizeof(*zs->score_leaf_by_id));
    zs->next_score_leaf_id=base;
    zbtScoreLeaf *leaves[COLLIDERS+1];
    uint32_t hashes[COLLIDERS+1];
    unsigned long home=table->size-1;
    for (unsigned int i=0;i<COLLIDERS;i++) {
        unsigned int high=mode==0 ? i%2 : mode==1 ? 7 : 255;
        hashes[i]=((uint32_t)high<<24)|(i<<2)|(uint32_t)home;
        leaves[i]=make_leaf(zs,i,hashes[i]);
        zbtIndexTableInsertRaw(table,hashes[i],leaves[i]->id);
    }
    serverAssert(table->used==COLLIDERS && table->filled==COLLIDERS);
    for (unsigned int i=0;i<COLLIDERS;i++) lookup(zs,hashes[i],i,leaves[i],1,NULL,NULL);

    zbtIndexBucket *first=zbtIndexBucketAt(table,home);
    zbtIndexBucket *later=zbtIndexBucketAt(table,0);
    zbtIndexSetId(table,first,2,ZBT_INDEX_DELETED_ID);
    zbtIndexSetId(table,later,1,ZBT_INDEX_DELETED_ID);
    table->used-=2;
    lookup(zs,hashes[2],2,NULL,0,NULL,NULL);
    lookup(zs,hashes[ZBT_INDEX_BUCKET_ITEMS+1],ZBT_INDEX_BUCKET_ITEMS+1,NULL,0,NULL,NULL);
    zbtIndexBucket *hint=NULL;unsigned int hint_pos=UINT_MAX;
    lookup(zs,hashes[0],999,NULL,0,&hint,&hint_pos);
    serverAssert(hint==first && hint_pos==2);tombstone_checks++;

    /* Same full hash, distinct member: exact leaf bytes still decide. */
    hashes[COLLIDERS]=hashes[0];
    leaves[COLLIDERS]=make_leaf(zs,COLLIDERS,hashes[COLLIDERS]);
    zbtIndexTableInsertRaw(table,hashes[COLLIDERS],leaves[COLLIDERS]->id);
    serverAssert(zbtIndexGetId(table,first,2)==leaves[COLLIDERS]->id);
    serverAssert(table->used==COLLIDERS-1 && table->filled==COLLIDERS);
    lookup(zs,hashes[COLLIDERS],COLLIDERS,leaves[COLLIDERS],1,NULL,NULL);
    hint=NULL;hint_pos=UINT_MAX;
    lookup(zs,hashes[0],999,NULL,0,&hint,&hint_pos);
    serverAssert(hint==later && hint_pos==1);tombstone_checks++;
    for (unsigned int i=0;i<COLLIDERS;i++)
        if (i!=2 && i!=ZBT_INDEX_BUCKET_ITEMS+1) lookup(zs,hashes[i],i,leaves[i],1,NULL,NULL);
    for (unsigned int i=0;i<=COLLIDERS;i++) zbtScoreLeafFreeOwned(zs,leaves[i]);
    zbtreeFree(zs);
}

static unsigned int migrated(zbtreeSet *zs) {
    unsigned int n=0;
    for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next)
        n+=zbtIndexLeafMigrated(zs,leaf)!=0;
    return n;
}

static void resizes(int wide) {
    const unsigned int count=384;
    zbtreeSet *zs=zbtreeCreate();zbtreeReserve(zs,count);
    for (unsigned int i=0;i<count;i++) {
        uint64_t key=i;
        zbtreeInsertNewRaw(zs,i,(unsigned char *)&key,sizeof(key),NULL);
    }
    while (zs->member_rehash) zbtIndexRehashStep(zs,64);
    if (wide) {
        zbtIndexTable old=zs->member_index;
        zbtIndexTableInit(zs,&zs->member_index,old.size,1);
        for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next)
            for (unsigned int i=0;i<leaf->n.count;i++)
                zbtIndexTableInsertRaw(&zs->member_index,zbtScoreLeafHash(leaf,i),leaf->id);
        zbtIndexTableRelease(zs,&old);
    }
    serverAssert(zbtTestCheck(zs));
    unsigned int leaves=0;
    for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next) leaves++;
    serverAssert(leaves>1);
    for (unsigned int round=0;round<2;round++) {
        serverAssert(zbtIndexStartResize(zs,round ? count : count*4,1));
        serverAssert(zs->member_rehash && migrated(zs)==0);
        uint64_t key=count-1;double score=-1;
        serverAssert(zbtreeScoreRaw(zs,(unsigned char *)&key,sizeof(key),&score));
        serverAssert(score==count-1 && migrated(zs)==1);
        unsigned int old_hits=0,new_hits=0;
        for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next) {
            size_t len;const unsigned char *ele=zbtScoreLeafElement(leaf,0,&len);
            uint32_t hash=zbtreeMemberHash(ele,len);
            int in_new=zbtIndexLeafMigrated(zs,leaf);
            int old=zbtIndexTableFind(zs,&zs->member_index,hash,ele,len,
                NULL,NULL,NULL,NULL,NULL,NULL,NULL);
            int new=zbtIndexTableFind(zs,&zs->member_rehash->table,hash,ele,len,
                NULL,NULL,NULL,NULL,NULL,NULL,NULL);
            serverAssert(old==!in_new && new==in_new);
            old_hits+=old;new_hits+=new;resize_checks++;
        }
        serverAssert(old_hits && new_hits && zbtTestCheck(zs));
        while (migrated(zs)<leaves) zbtIndexRehashStep(zs,1);
        serverAssert(zs->member_rehash && zs->member_rehash->table.used==count);
        zbtIndexBucket *destination=zs->member_rehash->table.buckets;
        uint32_t revision=zs->member_revision;
        key=round ? UINT64_MAX : 0;score=12345.0;
        int found=zbtreeScoreRaw(zs,(unsigned char *)&key,sizeof(key),&score);
        serverAssert(found==!round && score==(round ? 12345.0 : 0.0));
        serverAssert(!zs->member_rehash && zs->member_index.buckets==destination);
        serverAssert(zs->member_revision!=revision && zbtTestCheck(zs));
        final_steps++;
    }
    zbtreeFree(zs);
}

int main(void) {
    uint8_t seed[16];for (unsigned int i=0;i<16;i++) seed[i]=17+29*i;
    dictSetHashFunctionSeed(seed);
    filters();
    for (int wide=0;wide<2;wide++) {
        for (unsigned int mode=0;mode<3;mode++) probing(wide,mode);
        resizes(wide);
    }
    serverAssert(wrapped_hits && wide_hits && tombstone_checks==12 && final_steps==4);
    printf("{\"passed\":true,\"filter_checks\":%lu,\"hit_checks\":%lu,\"miss_checks\":%lu,"
           "\"reference_checks\":%lu,\"wrapped_hits\":%lu,\"wide_hits\":%lu,"
           "\"tombstone_checks\":%lu,\"resize_checks\":%lu,\"final_steps\":%lu}\n",
           filter_checks,hit_checks,miss_checks,reference_checks,wrapped_hits,wide_hits,
           tombstone_checks,resize_checks,final_steps);
    return 0;
}
