/* Correctness only: no timers, PMU collection or performance output. */
#include "zset_btree.c"
int __failed_tests, __test_num;
static unsigned long api_checks, stable_checks, active_checks, final_checks;
static unsigned long wide_checks, stale_checks, hint_checks;
enum { STABLE, ACTIVE, FINAL };
#define MEMBERS 384

static unsigned int leaf_count(zbtreeSet *zs) {
    unsigned int n=0;
    for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next) n++;
    return n;
}

static unsigned int migrated_count(zbtreeSet *zs) {
    unsigned int n=0;
    for (zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next)
        n+=zbtIndexLeafMigrated(zs,leaf)!=0;
    return n;
}

static zbtreeSet *make_tree(int wide) {
    zbtreeSet *zs=zbtreeCreate();
    if (wide) {
        /* Sparse high IDs exercise the actual 32-bit table field without
         * making the correctness fixture allocate tens of thousands of leaves. */
        zs->score_leaf_cap=70064;
        zs->score_leaf_by_id=zbtAlloc(zs,zs->score_leaf_cap*sizeof(*zs->score_leaf_by_id));
        memset(zs->score_leaf_by_id,0,zs->score_leaf_cap*sizeof(*zs->score_leaf_by_id));
        zs->next_score_leaf_id=70000;
    }
    zbtIndexTableInit(zs,&zs->member_index,zbtIndexBucketsForElements(MEMBERS),wide);
    for (uint64_t key=0;key<MEMBERS;key++) {
        double score=key ? (double)key+0.25 : -0.0;
        zbtreeInsertNewRaw(zs,score,(unsigned char *)&key,sizeof(key),NULL);
    }
    while (zs->member_rehash) zbtIndexRehashStep(zs,64);
    serverAssert(zbtTestCheck(zs) && leaf_count(zs)>2);
    serverAssert(zs->member_index.wide_ids==wide);
    if (wide) serverAssert(zs->score_first->id>UINT16_MAX);
    return zs;
}

/* Four independent copies start from the same exact index/resize state. */
static void check_apis(zbtreeSet *prepared, uint64_t key, int expected,
                        double wanted, int state) {
    uint32_t hash=zbtreeMemberHash((unsigned char *)&key,sizeof(key));
    for (unsigned int prehashed=0;prehashed<2;prehashed++)
        for (unsigned int scored=0;scored<2;scored++) {
            zbtreeSet *zs=zbtreeDup(prepared);
            serverAssert(zbtTestCheck(zs));
            unsigned int before=migrated_count(zs);
            uint32_t revision=zs->member_revision;
            zbtIndexBucket *destination=zs->member_rehash ?
                zs->member_rehash->table.buckets : NULL;
            double score=12345.0;
            int found=prehashed ?
                zbtreeScoreRawWithHash(zs,hash,(unsigned char *)&key,sizeof(key),
                                       scored ? &score : NULL) :
                zbtreeScoreRaw(zs,(unsigned char *)&key,sizeof(key),scored ? &score : NULL);
            serverAssert(found==expected);
            if (found && scored) serverAssert(memcmp(&score,&wanted,sizeof(score))==0);
            else serverAssert(score==12345.0);
            if (state==STABLE) {
                serverAssert(!zs->member_rehash && zs->member_revision==revision);
                stable_checks++;
            } else if (state==ACTIVE) {
                serverAssert(zs->member_rehash && migrated_count(zs)==before+1);
                serverAssert(zs->member_revision!=revision);active_checks++;
            } else {
                serverAssert(!zs->member_rehash && zs->member_index.buckets==destination);
                serverAssert(zs->member_revision!=revision);final_checks++;
            }
            serverAssert(zbtTestCheck(zs));
            if (zs->score_first->id>UINT16_MAX) wide_checks++;
            api_checks++;
            zbtreeFree(zs);
        }
}

static void tombstone_hint(zbtreeSet *prepared) {
    zbtreeSet *zs=zbtreeDup(prepared);
    uint64_t key=MEMBERS/2;
    sds member=sdsnewlen(&key,sizeof(key));
    zbtreeInsertPosition before,after;
    serverAssert(zbtreeFindForAdd(zs,member,NULL,&before));
    zbtIndexBucket *allocation=zs->member_index.buckets;
    serverAssert(zbtreeDelete(zs,member));
    serverAssert(!zs->member_rehash && zs->member_index.buckets==allocation);
    serverAssert(!zbtreeFindForAdd(zs,member,NULL,&after));
    serverAssert(after.bucket==before.bucket && after.pos==before.pos);
    serverAssert(zbtIndexGetId(&zs->member_index,after.bucket,after.pos)==ZBT_INDEX_DELETED_ID);
    serverAssert(zbtTestCheck(zs));hint_checks++;
    check_apis(zs,key,0,0,STABLE);
    sdsfree(member);zbtreeFree(zs);
}

/* Old tables may retain stale references while a resize owns migration.
 * Add one deleted slot and one same-tag reference to a released leaf ID. */
static void add_stale_old_entries(zbtreeSet *zs, uint64_t missing) {
    serverAssert(zs->member_rehash && zs->next_score_leaf_id<zs->score_leaf_cap);
    uint32_t free_id=zs->next_score_leaf_id++;
    zs->score_leaf_by_id[free_id]=ZBT_FREE_LEAF_ID(zs->free_score_leaf_id);
    zs->free_score_leaf_id=free_id+1;
    uint32_t hash=zbtreeMemberHash((unsigned char *)&missing,sizeof(missing));
    zbtIndexTableInsertRaw(&zs->member_index,hash,free_id);
    zbtIndexBucket *bucket=NULL;unsigned int position=UINT_MAX;
    serverAssert(zbtIndexTableFindReference(&zs->member_index,hash,free_id,&bucket,&position));
    zbtIndexTableInsertRaw(&zs->member_index,hash,free_id);
    zbtIndexSetId(&zs->member_index,bucket,position,ZBT_INDEX_DELETED_ID);
    zs->member_index.used--;
    serverAssert(zbtTestCheck(zs));stale_checks++;
}

static void run_width(int wide) {
    zbtreeSet *zs=make_tree(wide);
    check_apis(zs,0,1,-0.0,STABLE);
    check_apis(zs,MEMBERS-1,1,MEMBERS-1+0.25,STABLE);
    check_apis(zs,UINT64_MAX,0,0,STABLE);
    tombstone_hint(zs);

    serverAssert(zbtIndexStartResize(zs,MEMBERS*4,1));
    serverAssert(zs->member_rehash && migrated_count(zs)==0);
    /* The first lookup migrates the first leaf: one hit is in the new table,
     * the tail hit remains in the old table, and misses still advance once. */
    check_apis(zs,0,1,-0.0,ACTIVE);
    check_apis(zs,MEMBERS-1,1,MEMBERS-1+0.25,ACTIVE);
    check_apis(zs,UINT64_MAX,0,0,ACTIVE);
    zbtIndexRehashStep(zs,1);
    serverAssert(migrated_count(zs)==1);
    check_apis(zs,0,1,-0.0,ACTIVE);
    check_apis(zs,MEMBERS-1,1,MEMBERS-1+0.25,ACTIVE);
    add_stale_old_entries(zs,UINT64_MAX);
    check_apis(zs,UINT64_MAX,0,0,ACTIVE);

    while (migrated_count(zs)<leaf_count(zs)) zbtIndexRehashStep(zs,1);
    serverAssert(zs->member_rehash && zs->member_rehash->next_leaf_id==ZBT_NO_LEAF_ID);
    check_apis(zs,0,1,-0.0,FINAL);
    check_apis(zs,MEMBERS-1,1,MEMBERS-1+0.25,FINAL);
    check_apis(zs,UINT64_MAX,0,0,FINAL);
    zbtreeFree(zs);
}

int main(void) {
    uint8_t seed[16];for (unsigned int i=0;i<16;i++) seed[i]=17+29*i;
    dictSetHashFunctionSeed(seed);
    run_width(0);run_width(1);
    serverAssert(wide_checks && stale_checks==2 && hint_checks==2);
    printf("{\"passed\":true,\"api_checks\":%lu,\"stable_checks\":%lu,"
           "\"active_checks\":%lu,\"final_checks\":%lu,\"wide_checks\":%lu,"
           "\"stale_checks\":%lu,\"hint_checks\":%lu}\n",
           api_checks,stable_checks,active_checks,final_checks,wide_checks,stale_checks,hint_checks);
    return 0;
}
