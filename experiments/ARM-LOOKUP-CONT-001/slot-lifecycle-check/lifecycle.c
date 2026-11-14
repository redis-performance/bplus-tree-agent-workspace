#define _POSIX_C_SOURCE 200809L
#include "generated/zset_btree.c"
#define LC_N 2048
#define LC_LOOKUPS 65536
static sds lc_members[LC_N];
static unsigned char lc_original[LC_N],lc_duplicate[LC_N];
static uint64_t lc_lookups;
typedef struct { uint64_t enabled,eligible,unchanged,stale,out_of_range,ineligible,full_success; } lcAudit;
typedef struct { const char *name; uint64_t count,score_sum,id_sum,lookups,bytes; lcAudit audit; } lcCheckpoint;
static lcCheckpoint lc_points[7];
static unsigned int lc_npoints;
static void lcLookup(void) { serverAssert(lc_lookups<LC_LOOKUPS);lc_lookups++; }
static size_t lcBytes(unsigned int id,unsigned char *bytes) {
    size_t len=id%3==0 ? 16:id%3==1 ? 128:384;
    for(size_t j=0;j<len;j++)bytes[j]=(id*17+j*29+0x5a)&255;
    for(unsigned int j=0;j<4;j++)bytes[j]=(id>>(8*j))&255;
    bytes[7]=bytes[11]=0;return len;
}
static lcAudit lcAuditHints(zbtreeSet *zs) {
    lcAudit out={0};
    zbtIndexTable *tables[2]={&zs->member_index,zs->member_rehash ? &zs->member_rehash->table:NULL};
    for(unsigned int t=0;t<2;t++) {
        zbtIndexTable *table=tables[t];if(!table || !table->size)continue;
        shTable *shadow=shGet(table);serverAssert(shadow && shadow->owner==(uintptr_t)zs);
        for(unsigned long b=0;b<table->size;b++) {
            shHint *hint=&shadow->hints[b];if(!hint->code)continue;
            shInc(&out.enabled);serverAssert(hint->code<=96 && hint->len<=384);
            zbtIndexBucket *bucket=zbtIndexBucketAt(table,b);
            uint32_t id=zbtIndexGetId(table,bucket,0);
            serverAssert(id==hint->id && id!=ZBT_INDEX_DELETED_ID && (uint8_t)zbtIndexTags(bucket)!=0);
            zbtScoreLeaf *leaf=id<zs->next_score_leaf_id ? zs->score_leaf_by_id[id]:NULL;
            if(!leaf || ZBT_IS_FREE_LEAF_ID(leaf)) {
                serverAssert(zs->member_rehash && !t);shInc(&out.ineligible);continue;
            }
            serverAssert(leaf->id==id);
            if(zs->member_rehash && ((int)t!=(leaf->n.index_resize==zs->member_rehash->resize_id))) {
                shInc(&out.ineligible);continue;
            }
            shInc(&out.eligible);unsigned int physical=hint->code-1;
            int same=physical<leaf->n.count && shPredicate(leaf,physical,hint->hash,hint->bytes,hint->len);
            if(same)shInc(&out.unchanged);else shInc(&out.stale);
            if(physical>=leaf->n.count)shInc(&out.out_of_range);
            double score=-123;unsigned int pos=UINT_MAX;lcLookup();
            int found=zbtScoreLeafFindMember(leaf,hint->hash,hint->bytes,hint->len,&score,&pos);
            if(found)shInc(&out.full_success);
            if(same) {
                unsigned int logical=zbtScoreLeafPhysicalPos(leaf,physical);
                double expected=zbtScoreLeafScore(leaf,logical);
                serverAssert(found && pos==logical && !memcmp(&score,&expected,sizeof(score)));
            }
            if(!found)serverAssert(score==-123 && pos==UINT_MAX);
        }
    }
    serverAssert(out.enabled==out.eligible+out.ineligible && out.eligible==out.stale+out.unchanged);
    return out;
}
static void lcVerify(const char *name,zbtreeSet *zs,const unsigned char *alive) {
    serverAssert(lc_npoints<7);lcCheckpoint *p=&lc_points[lc_npoints++];p->name=name;
    /* Audit snapshots precede public reads, which may advance rehash. */
    p->audit=lcAuditHints(zs);uint64_t before=lc_lookups;
    unsigned int count=0;for(unsigned int i=0;i<LC_N;i++)count+=alive[i];
    serverAssert(zbtreeLength(zs)==count);p->count=count;p->bytes=zbtreeAllocSize(zs);
    unsigned int rank=0;
    for(unsigned int i=0;i<LC_N;i++) {
        unsigned char immutable[384];size_t expected_len=lcBytes(i,immutable);
        serverAssert(sdslen(lc_members[i])==expected_len && !memcmp(lc_members[i],immutable,expected_len));
        double score=-123,expected=i+1;lcLookup();
        int found=zbtreeScoreRaw(zs,(unsigned char *)lc_members[i],sdslen(lc_members[i]),&score);
        serverAssert(found==(int)alive[i]);
        if(found)serverAssert(!memcmp(&score,&expected,sizeof(score)));else serverAssert(score==-123);
        lcLookup();serverAssert(zbtreeScoreRaw(zs,(unsigned char *)lc_members[i],sdslen(lc_members[i]),NULL)==(int)alive[i]);
        score=-123;lcLookup();long forward=zbtreeRank(zs,lc_members[i],0,&score);
        lcLookup();long reverse=zbtreeRank(zs,lc_members[i],1,NULL);
        if(alive[i]) {
            serverAssert(forward==(long)rank && reverse==(long)(count-rank-1) && !memcmp(&score,&expected,sizeof(score)));
            rank++;p->score_sum+=i+1;p->id_sum+=i;
        } else serverAssert(forward==-1 && reverse==-1 && score==-123);
    }
    for(int reverse=0;reverse<2;reverse++) {
        zbtreeIterator it;serverAssert(zbtreeIteratorStart(zs,reverse,&it));
        for(unsigned int step=0;step<LC_N;step++) {
            unsigned int i=reverse ? LC_N-step-1:step;if(!alive[i])continue;
            const unsigned char *bytes;size_t len;double score,expected=i+1;
            serverAssert(zbtreeIteratorNext(&it,reverse,&bytes,&len,&score));
            serverAssert(len==sdslen(lc_members[i]) && !memcmp(bytes,lc_members[i],len) && !memcmp(&score,&expected,sizeof(score)));
        }
        serverAssert(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    p->lookups=lc_lookups-before;serverAssert(p->lookups==8192);
}
static void lcCopyTable(const zbtIndexTable *source,const zbtIndexTable *copy,uint64_t *tables,uint64_t *hints) {
    serverAssert(source->size==copy->size && source->wide_ids==copy->wide_ids);
    if(!source->size)return;
    shTable *s=shGet(source),*d=shGet(copy);
    serverAssert(s && d && s->generation!=d->generation && s->key!=d->key);
    serverAssert(!memcmp(s->hints,d->hints,sizeof(s->hints)));shInc(tables);
    for(unsigned long b=0;b<s->size;b++)if(s->hints[b].code)shInc(hints);
}
static shHint lc_saved_hints[2][SH_BUCKETS];
static uint64_t lc_saved_generations[2];
static void lcSaveDuplicate(zbtreeSet *zs,int compare) {
    zbtIndexTable *tables[2]={&zs->member_index,zs->member_rehash ? &zs->member_rehash->table:NULL};
    for(unsigned int t=0;t<2;t++) {
        shTable *state=tables[t] && tables[t]->size ? shGet(tables[t]):NULL;
        uint64_t generation=state ? state->generation:0;
        if(compare) {
            serverAssert(generation==lc_saved_generations[t]);
            if(state)serverAssert(!memcmp(lc_saved_hints[t],state->hints,sizeof(lc_saved_hints[t])));
        } else {
            lc_saved_generations[t]=generation;
            if(state)memcpy(lc_saved_hints[t],state->hints,sizeof(lc_saved_hints[t]));
        }
    }
}
static void lcPrintAudit(lcAudit a) {
    printf("{\"enabled\":%" PRIu64 ",\"eligible\":%" PRIu64 ",\"unchanged\":%" PRIu64 ",\"stale\":%" PRIu64 ",\"out_of_range\":%" PRIu64 ",\"ineligible\":%" PRIu64 ",\"full_success\":%" PRIu64 "}",
        a.enabled,a.eligible,a.unchanged,a.stale,a.out_of_range,a.ineligible,a.full_success);
}
int main(int argc,char **argv) {
    (void)argv;serverAssert(argc==1);
    /* Frozen hooks remain byte-identical; this harness never starts their census. */
    (void)censusQueryBegin;(void)censusQueryEnd;(void)shCountStart;(void)shCountEnd;
    uint8_t key[16];for(unsigned int i=0;i<16;i++)key[i]=(17+i*29U)&255;dictSetHashFunctionSeed(key);
    zbtreeSet *original=zbtreeCreate();
    for(unsigned int i=0;i<LC_N;i++) {
        unsigned char bytes[384];size_t len=lcBytes(i,bytes);
        lc_members[i]=sdsnewlen(bytes,len);lc_original[i]=1;
        zbtreeInsertPosition position;double score=-123;
        serverAssert(!zbtreeFindForAdd(original,lc_members[i],&score,&position));
        zbtreeInsertNew(original,i+1,lc_members[i],&position);
    }
    lcVerify("inserted",original,lc_original);
    uint64_t writes=sh_totals[SH_SETUP].id_writes,invalidations=sh_totals[SH_SETUP].invalidations;
    for(unsigned int i=0;i<128;i+=2) {serverAssert(zbtreeDelete(original,lc_members[i]));lc_original[i]=0;}
    uint64_t delete_writes=sh_totals[SH_SETUP].id_writes-writes;
    uint64_t delete_invalidations=sh_totals[SH_SETUP].invalidations-invalidations;
    lcVerify("deleted",original,lc_original);
    serverAssert(delete_writes && delete_invalidations && lc_points[1].audit.stale && lc_points[1].audit.unchanged);
    memcpy(lc_duplicate,lc_original,sizeof(lc_original));
    lcAudit predup=lcAuditHints(original);uint64_t seeds=sh_totals[SH_SETUP].seeds;
    zbtreeSet *duplicate=zbtreeDup(original);uint64_t copied_tables=0,copied_hints=0;
    serverAssert((original->member_rehash!=NULL)==(duplicate->member_rehash!=NULL));
    lcCopyTable(&original->member_index,&duplicate->member_index,&copied_tables,&copied_hints);
    if(original->member_rehash)lcCopyTable(&original->member_rehash->table,&duplicate->member_rehash->table,&copied_tables,&copied_hints);
    serverAssert(sh_totals[SH_SETUP].seeds==seeds && copied_hints && predup.stale);
    lcAudit dup_audit=lcAuditHints(duplicate);
    serverAssert(!memcmp(&predup,&dup_audit,sizeof(predup)));
    lcVerify("dup_original",original,lc_original);lcVerify("dup_copy",duplicate,lc_duplicate);
    /* Derive all 1025 victims from the independent model before the API call. */
    unsigned int rank=0,victims=0;
    for(unsigned int i=0;i<LC_N;i++)if(lc_original[i]) {
        if(rank>=512 && rank<=1536){lc_original[i]=0;victims++;}rank++;
    }
    serverAssert(rank==1984 && victims==1025);
    uint64_t old_gen[2]={shGet(&original->member_index)->generation,0};
    if(original->member_rehash)old_gen[1]=shGet(&original->member_rehash->table)->generation;
    uint64_t rebuild_begin=sh_sequence;unsigned int life_before=sh_nlife;seeds=sh_totals[SH_SETUP].seeds;
    lcSaveDuplicate(duplicate,0);
    serverAssert(zbtreeDeleteRangeByRank(original,512,1536)==1025);
    lcSaveDuplicate(duplicate,1);
    uint64_t rebuild_end=sh_sequence;uint64_t rebuild_seeds=sh_totals[SH_SETUP].seeds-seeds,retired=0,origin2=0;
    serverAssert(rebuild_seeds && !original->member_rehash);
    for(unsigned int i=life_before;i<sh_nlife;i++)if(sh_life[i].kind==SH_RELEASE &&
        (sh_life[i].generation==old_gen[0] || (old_gen[1] && sh_life[i].generation==old_gen[1])))retired++;
    serverAssert(retired==(old_gen[1] ? 2U:1U));
    shTable *rebuilt=shGet(&original->member_index);serverAssert(rebuilt->generation!=old_gen[0] && rebuilt->generation!=old_gen[1]);
    uint64_t rebuilt_generation=rebuilt->generation;
    for(unsigned long b=0;b<rebuilt->size;b++)if(rebuilt->hints[b].code) {serverAssert(rebuilt->hints[b].origin==2);origin2++;}
    serverAssert(origin2 && origin2==rebuild_seeds);
    lcVerify("rebuilt_original",original,lc_original);lcVerify("rebuilt_copy",duplicate,lc_duplicate);
    lcAudit fresh=lc_points[4].audit;
    serverAssert(!fresh.stale && !fresh.ineligible && !fresh.out_of_range &&
        fresh.enabled==origin2 && fresh.eligible==origin2 && fresh.unchanged==origin2 && fresh.full_success==origin2);
    lcSaveDuplicate(duplicate,0);zbtreeFree(original);original=NULL;
    lcSaveDuplicate(duplicate,1);lcVerify("freed_original_copy",duplicate,lc_duplicate);
    sh_phase=SH_CLEANUP;zbtreeFree(duplicate);duplicate=NULL;
    for(unsigned int i=0;i<LC_N;i++)sdsfree(lc_members[i]);
    shCompletion();serverAssert(lc_npoints==7 && !sh_nqueries && !sh_ncalls && !sh_nleaves && !sh_nfilters && !sh_nmutations);
    printf("{\"diagnostic\":\"slot-lifecycle\",\"revision\":0,\"verified\":true,\"untimed\":true,\"seed\":17,\"members\":2048,\"delete_count\":64,\"range_deleted\":1025,\"lookup_bound\":65536,\"verification_lookups\":%" PRIu64 ",\"delete_id_writes\":%" PRIu64 ",\"delete_invalidations\":%" PRIu64 ",\"copied_tables\":%" PRIu64 ",\"copied_hints\":%" PRIu64 ",\"copied_stale\":%" PRIu64 ",\"dup_reseeded\":0,\"rebuild_seeds\":%" PRIu64 ",\"rebuild_origin2\":%" PRIu64 ",\"retired_original_tables\":%" PRIu64 ",\"duplicate_unchanged\":true,\"cleanup_complete\":true,\"live_generations\":0,\"census_queries\":0,\"predup_audit\":",
        lc_lookups,delete_writes,delete_invalidations,copied_tables,copied_hints,predup.stale,rebuild_seeds,origin2,retired);
    lcPrintAudit(predup);printf(",\"dup_audit\":");lcPrintAudit(dup_audit);
    printf(",\"old_generations\":[%" PRIu64 ",%" PRIu64 "],\"rebuilt_generation\":%" PRIu64 ",\"rebuild_begin\":%" PRIu64 ",\"rebuild_end\":%" PRIu64 ",\"checkpoints\":[",old_gen[0],old_gen[1],rebuilt_generation,rebuild_begin,rebuild_end);
    for(unsigned int i=0;i<lc_npoints;i++) {
        lcCheckpoint *p=&lc_points[i];printf("%s{\"name\":\"%s\",\"count\":%" PRIu64 ",\"score_sum\":%" PRIu64 ",\"id_sum\":%" PRIu64 ",\"model_lookups\":%" PRIu64 ",\"owned_bytes\":%" PRIu64 ",\"audit\":",i ? ",":"",p->name,p->count,p->score_sum,p->id_sum,p->lookups,p->bytes);lcPrintAudit(p->audit);printf("}");
    }
    printf("],\"lifecycle\":[");
    for(unsigned int i=0;i<sh_nlife;i++) {shLife *e=&sh_life[i];printf("%s{\"seq\":%" PRIu64 ",\"phase\":%u,\"kind\":%u,\"generation\":%" PRIu64 ",\"parent\":%" PRIu64 ",\"registry_slot\":%u,\"wide_ids\":%u,\"buckets\":%lu}",i ? ",":"",e->seq,e->phase,e->kind,e->generation,e->parent,e->slot,e->wide,e->size);}
    printf("]}\n");return 0;
}
