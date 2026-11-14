/* Diagnostic state only. All original table/leaf decisions remain authoritative. */
#include <inttypes.h>
#define SH_TABLES 16
#define SH_BUCKETS 1024
#define SH_BYTES 384
#define SH_LIFE 4096
#define SH_EVENTS 65536
#define SH_CALLS 4096
#define SH_QUERIES 1000
enum { SH_SETUP, SH_WARMUP, SH_COUNT, SH_VALIDATE, SH_CLEANUP, SH_PHASES };
enum { SH_ALLOC, SH_RELEASE, SH_DUP, SH_REBIND, SH_PROMOTE };
enum { SH_OTHER, SH_DISABLED, SH_RANGE, SH_TAG, SH_FAIL, SH_SUCCESS };
typedef struct { uint8_t code,origin; uint32_t hash,id; size_t len; unsigned char bytes[SH_BYTES]; } shHint;
typedef struct { uint64_t generation; unsigned long bucket; unsigned int code,origin; uint32_t id; } shInitial;
typedef struct {
    uintptr_t key,owner; uint64_t generation; unsigned long size; unsigned int wide;
    shHint hints[SH_BUCKETS];
} shTable;
typedef struct { uint64_t seq,generation,parent; unsigned int phase,kind,slot,wide; unsigned long size; } shLife;
typedef struct { uint64_t id_writes,invalidations,seed_attempts,seeds; } shTotals;
typedef struct {
    uint64_t seq,generation; unsigned int query,kind; unsigned long bucket;
    uint32_t id; unsigned int code,origin;
} shMutation;
typedef struct {
    int active,consumed; uintptr_t owner; uint64_t generation; uint32_t leaf_id;
    unsigned int physical; shHint hint;
} shSeed;
typedef struct {
    uint64_t seq,generation; unsigned int query,call,slot,code,count,terminal;
    int stale; unsigned int result,useful; unsigned long bucket; uint32_t leaf_id;
} shLeafEvent;
typedef struct {
    uint64_t seq,generation; unsigned int query,call,scan,original,folded;
} shFilter;
#define SH_COUNTERS(X) X(bucket_visits) X(displaced_bucket_visits) \
    X(approximate_candidates) X(true_tag_candidates) X(tombstone_skips) \
    X(free_reference_skips) X(migration_skips) X(leaf_calls) X(leaf_successes) \
    X(leaf_failures) X(home_hit) X(filter_evaluated) X(filter_true) \
    X(filter_false) X(home_postfilter_fallback)
#define SH_FIELD(k) uint64_t k;
typedef struct {
    SH_COUNTERS(SH_FIELD)
    uint64_t seq,end_seq,generation; unsigned int query,active_resize,destination_table,wide_ids,result;
    unsigned long table_buckets;
} censusCall;
#undef SH_FIELD
typedef struct { unsigned int before,after; uint64_t seq,end_seq; } shQuery;
static shTable sh_tables[SH_TABLES];
static shLife sh_life[SH_LIFE];
static shMutation sh_mutations[SH_EVENTS];
static shLeafEvent sh_leaves[SH_EVENTS];
static shFilter sh_filters[SH_EVENTS];
static censusCall sh_calls[SH_CALLS];
static shQuery sh_queries[SH_QUERIES];
static shTotals sh_totals[SH_PHASES];
static shInitial sh_initial[SH_TABLES*SH_BUCKETS];
static shSeed sh_seed;
static unsigned int sh_phase,sh_nlife,sh_nmutations,sh_nleaves,sh_nfilters,sh_ncalls,sh_nqueries;
static unsigned int sh_query=UINT_MAX,sh_call=UINT_MAX;
static uint64_t sh_generation,sh_sequence;
static uint64_t sh_count_start,sh_count_end;
static unsigned int sh_ninitial;
static void shInc(uint64_t *v) { serverAssert(*v<UINT64_MAX); ++*v; }
static uint64_t shNext(void) { shInc(&sh_sequence); return sh_sequence; }
static uint64_t shFold(uint64_t v) { return (v & UINT64_C(0x00ffffffffffffff)) | (v>>56); }
static shTable *shFind(uintptr_t key) {
    for(unsigned int i=0;i<SH_TABLES;i++) if(sh_tables[i].key==key && key) return &sh_tables[i];
    return NULL;
}
static shTable *shGet(const zbtIndexTable *table) {
    if(!table->size) { serverAssert(table->buckets==NULL); return NULL; }
    shTable *s=shFind((uintptr_t)table->buckets);
    serverAssert(s && s->size==table->size && s->wide==(unsigned int)table->wide_ids); return s;
}
static unsigned long shBucket(const shTable *s,const zbtIndexBucket *bucket) {
    uintptr_t address=(uintptr_t)bucket;
    size_t width=s->wide ? sizeof(zbtIndexBucket32):sizeof(zbtIndexBucket16);
    serverAssert(address>=s->key && (address-s->key)%width==0);
    unsigned long i=(address-s->key)/width;serverAssert(i<s->size);return i;
}
static void shLifeAdd(shTable *s,unsigned int kind,uint64_t parent) {
    serverAssert(sh_nlife<SH_LIFE);
    sh_life[sh_nlife++]=(shLife){.seq=shNext(),.generation=s->generation,.parent=parent,
        .phase=sh_phase,.kind=kind,.slot=(unsigned int)(s-sh_tables),.wide=s->wide,.size=s->size};
}
static shTable *shRegister(zbtreeSet *owner,const zbtIndexTable *table,unsigned int kind,uint64_t parent) {
    serverAssert(table->buckets && table->size && table->size<=SH_BUCKETS);
    serverAssert(!shFind((uintptr_t)table->buckets));
    shTable *s=NULL;
    for(unsigned int i=0;i<SH_TABLES;i++) if(!sh_tables[i].key) {s=&sh_tables[i];break;}
    serverAssert(s);memset(s,0,sizeof(*s));shInc(&sh_generation);
    s->key=(uintptr_t)table->buckets;s->owner=(uintptr_t)owner;s->generation=sh_generation;
    s->size=table->size;s->wide=table->wide_ids;shLifeAdd(s,kind,parent);return s;
}
static void shAlloc(zbtreeSet *zs,const zbtIndexTable *table) { (void)shRegister(zs,table,SH_ALLOC,0); }
static void shRelease(const zbtIndexTable *table) {
    shTable *s=shGet(table);if(!s)return;
    serverAssert(!sh_seed.active || sh_seed.generation!=s->generation);
    shLifeAdd(s,SH_RELEASE,0);memset(s,0,sizeof(*s));
}
static void shDup(zbtreeSet *owner,const zbtIndexTable *copy,const zbtIndexTable *source) {
    shTable *s=shGet(source);serverAssert(s);
    shTable *d=shRegister(owner,copy,SH_DUP,s->generation);
    memcpy(d->hints,s->hints,sizeof(d->hints));
}
static void shPromote(const zbtIndexTable *table) { shTable *s=shGet(table);serverAssert(s);shLifeAdd(s,SH_PROMOTE,0); }
static void shRebind(uintptr_t oldkey,void *newptr) {
    shTable *s=shFind(oldkey);if(!s || oldkey==(uintptr_t)newptr)return;
    serverAssert(newptr && !shFind((uintptr_t)newptr));s->key=(uintptr_t)newptr;shLifeAdd(s,SH_REBIND,0);
}
static void shReowner(uintptr_t oldkey,zbtreeSet *newzs) {
    for(unsigned int i=0;i<SH_TABLES;i++)
        if(sh_tables[i].key && sh_tables[i].owner==oldkey)sh_tables[i].owner=(uintptr_t)newzs;
}
static void shMutationAdd(shTable *s,unsigned long bucket,unsigned int kind,uint32_t id,unsigned int code) {
    if(sh_phase!=SH_COUNT)return;
    serverAssert(sh_query!=UINT_MAX && sh_nmutations<SH_EVENTS);
    sh_mutations[sh_nmutations++]=(shMutation){.seq=shNext(),.generation=s->generation,
        .query=sh_query,.kind=kind,.bucket=bucket,.id=id,.code=code,.origin=kind ? sh_seed.hint.origin:0};
}
static void shIdWrite(const zbtIndexTable *table,zbtIndexBucket *bucket,unsigned int pos,uint32_t id) {
    if(pos)return;
    shTable *s=shGet(table);serverAssert(s);unsigned long b=shBucket(s,bucket);
    shInc(&sh_totals[sh_phase].id_writes);
    if(s->hints[b].code)shInc(&sh_totals[sh_phase].invalidations);
    shMutationAdd(s,b,0,id,s->hints[b].code);memset(&s->hints[b],0,sizeof(s->hints[b]));
}
static void shSeedBegin(zbtreeSet *owner,const zbtIndexTable *table,zbtScoreLeaf *leaf,
                        unsigned int physical,uint32_t hash,unsigned int origin) {
    serverAssert(!sh_seed.active && physical<leaf->n.count && physical<96);
    serverAssert(origin==1 || origin==2);
    shTable *s=shGet(table);serverAssert(s && s->owner==(uintptr_t)owner);
    serverAssert(zbtScoreLeafHashTags(leaf)[physical]==(uint8_t)(hash>>24));
    unsigned char *record=(unsigned char *)leaf+zbtScoreLeafOffsets(leaf)[physical];
    if(record[0]==ZBT_PACKED_EXTERNAL)serverAssert(zbtExternalHash(record)==hash);
    size_t len;const unsigned char *bytes=zbtPackedData(record,&len);serverAssert(len<=SH_BYTES);
    sh_seed=(shSeed){.active=1,.owner=(uintptr_t)owner,.generation=s->generation,
                    .leaf_id=leaf->id,.physical=physical};
    sh_seed.hint.code=physical+1;sh_seed.hint.hash=hash;sh_seed.hint.len=len;
    sh_seed.hint.origin=origin;sh_seed.hint.id=leaf->id;
    memcpy(sh_seed.hint.bytes,bytes,len);
}
static void shSeedInsert(const zbtIndexTable *table,zbtIndexBucket *bucket,
                         unsigned int pos,uint32_t hash,uint32_t id) {
    if(!sh_seed.active)return;
    shTable *s=shGet(table);
    serverAssert(s && !sh_seed.consumed && s->owner==sh_seed.owner &&
        s->generation==sh_seed.generation && hash==sh_seed.hint.hash && id==sh_seed.leaf_id &&
        sh_seed.physical+1==sh_seed.hint.code && sh_seed.hint.code<=96);
    sh_seed.consumed=1;shInc(&sh_totals[sh_phase].seed_attempts);
    if(!pos) {
        unsigned long b=shBucket(s,bucket);serverAssert(!s->hints[b].code);
        s->hints[b]=sh_seed.hint;shInc(&sh_totals[sh_phase].seeds);
        shMutationAdd(s,b,1,id,s->hints[b].code);
    }
}
static void shSeedEnd(zbtreeSet *owner,const zbtIndexTable *table,zbtScoreLeaf *leaf,
                      unsigned int physical,uint32_t hash) {
    shTable *s=shGet(table);
    serverAssert(sh_seed.active && sh_seed.consumed && s && s->owner==(uintptr_t)owner &&
        sh_seed.owner==(uintptr_t)owner && sh_seed.generation==s->generation &&
        sh_seed.leaf_id==leaf->id && sh_seed.physical==physical && sh_seed.hint.hash==hash);
    memset(&sh_seed,0,sizeof(sh_seed));
}
static void censusQueryBegin(zbtreeSet *zs) {
    if(sh_phase!=SH_COUNT)return;
    serverAssert(!sh_seed.active && sh_query==UINT_MAX && sh_call==UINT_MAX && sh_nqueries<SH_QUERIES);
    sh_query=sh_nqueries++;sh_queries[sh_query].before=zs->member_rehash!=NULL;
    sh_queries[sh_query].seq=shNext();
}
static void censusQueryEnd(zbtreeSet *zs) {
    if(sh_phase!=SH_COUNT)return;
    serverAssert(!sh_seed.active && sh_query!=UINT_MAX && sh_call==UINT_MAX);
    sh_queries[sh_query].after=zs->member_rehash!=NULL;sh_queries[sh_query].end_seq=shNext();sh_query=UINT_MAX;
}
static censusCall *censusBegin(zbtreeSet *zs,zbtIndexTable *table) {
    if(sh_phase!=SH_COUNT)return NULL;
    serverAssert(sh_query!=UINT_MAX && sh_call==UINT_MAX && !sh_seed.active && sh_ncalls<SH_CALLS);
    shTable *s=shGet(table);sh_call=sh_ncalls++;
    censusCall *c=&sh_calls[sh_call];c->seq=shNext();c->generation=s ? s->generation:0;
    c->query=sh_query;c->active_resize=zs->member_rehash!=NULL;
    c->destination_table=zs->member_rehash && table==&zs->member_rehash->table;
    c->wide_ids=table->wide_ids;c->table_buckets=table->size;return c;
}
static void censusEnd(censusCall *c,int result) {
    if(!c)return;
    serverAssert(c==&sh_calls[sh_call]);c->result=result;c->end_seq=shNext();sh_call=UINT_MAX;
    serverAssert(c->leaf_calls==c->leaf_successes+c->leaf_failures && c->leaf_successes==(unsigned int)result);
}
#define CENSUS_INC(c,k) do { if(c)shInc(&(c)->k); } while(0)
#define CENSUS_RETURN(c,r) do { censusEnd(c,r);return (r); } while(0)
static int shPredicate(zbtScoreLeaf *leaf,unsigned int physical,uint32_t hash,const unsigned char *bytes,size_t len) {
    serverAssert(physical<leaf->n.count);
    if(zbtScoreLeafHashTags(leaf)[physical]!=(uint8_t)(hash>>24))return 0;
    unsigned char *record=(unsigned char *)leaf+zbtScoreLeafOffsets(leaf)[physical];
    if(record[0]==ZBT_PACKED_EXTERNAL && zbtExternalHash(record)!=hash)return 0;
    size_t n;const unsigned char *current=zbtPackedData(record,&n);
    return n==len && memcmp(current,bytes,n)==0;
}
static __attribute__((noinline)) int shLeaf(censusCall *c,const zbtIndexTable *table,
    zbtIndexBucket *bucket,unsigned int slot,zbtScoreLeaf *leaf,uint32_t hash,
    const unsigned char *ele,size_t elelen,double *score,unsigned int *position) {
    shLeafEvent *e=NULL;double hinted_score=0;unsigned int hinted_position=0;
    if(c) {
        serverAssert(sh_nleaves<SH_EVENTS);shTable *s=shGet(table);serverAssert(s);
        unsigned long b=shBucket(s,bucket);shHint *hint=&s->hints[b];serverAssert(hint->code<=96);
        e=&sh_leaves[sh_nleaves++];*e=(shLeafEvent){.seq=shNext(),.generation=s->generation,
            .query=sh_query,.call=sh_call,.slot=slot,.code=slot ? 0:hint->code,
            .count=leaf->n.count,.terminal=SH_OTHER,.stale=-1,.bucket=b,.leaf_id=leaf->id};
        if(!slot) {
            if(!hint->code)e->terminal=SH_DISABLED;
            else if(hint->code-1U>=leaf->n.count) {e->terminal=SH_RANGE;e->stale=1;}
            else {
                unsigned int physical=hint->code-1;
                e->stale=!shPredicate(leaf,physical,hint->hash,hint->bytes,hint->len);
                if(zbtScoreLeafHashTags(leaf)[physical]!=(uint8_t)(hash>>24))e->terminal=SH_TAG;
                else if(!shPredicate(leaf,physical,hash,ele,elelen))e->terminal=SH_FAIL;
                else {
                    e->terminal=SH_SUCCESS;hinted_position=zbtScoreLeafPhysicalPos(leaf,physical);
                    if(score)hinted_score=zbtScoreLeafScore(leaf,hinted_position);
                }
            }
        }
        CENSUS_INC(c,leaf_calls);
    }
    /* Mandatory original search: exactly one source call, for every outcome. */
    int result=zbtScoreLeafFindMember(leaf,hash,ele,elelen,score,position);
    if(e) {
        e->result=result;e->useful=e->terminal==SH_SUCCESS && result;
        if(e->terminal==SH_SUCCESS) {
            serverAssert(result);
            if(position)serverAssert(*position==hinted_position);
            if(score)serverAssert(memcmp(score,&hinted_score,sizeof(double))==0);
        }
        if(result)CENSUS_INC(c,leaf_successes);else CENSUS_INC(c,leaf_failures);
    }
    return result;
}
static int shFilterObserve(const zbtIndexTable *table,uint64_t word,uint64_t bits,unsigned int scan) {
    int original=(word&bits)==bits;uint64_t folded=shFold(bits);
    int reduced=(shFold(word)&folded)==folded;serverAssert(!original || reduced);
    if(sh_phase==SH_COUNT) {
        serverAssert(sh_nfilters<SH_EVENTS && sh_query!=UINT_MAX);
        shTable *s=shGet(table);serverAssert(s);
        sh_filters[sh_nfilters++]=(shFilter){.seq=shNext(),.generation=s->generation,
            .query=sh_query,.call=sh_call,.scan=scan,.original=original,.folded=reduced};
    }
    return original;
}
static void shCountStart(void) {
    serverAssert(sh_phase==SH_WARMUP && !sh_seed.active && sh_query==UINT_MAX && sh_call==UINT_MAX);
    serverAssert(!sh_ncalls && !sh_nqueries && !sh_nleaves && !sh_nfilters && !sh_nmutations);
    for(unsigned int i=0;i<SH_TABLES;i++) if(sh_tables[i].key) {
        shTable *s=&sh_tables[i];
        for(unsigned long b=0;b<s->size;b++)if(s->hints[b].code) {
            serverAssert(sh_ninitial<SH_TABLES*SH_BUCKETS);shHint *h=&s->hints[b];
            sh_initial[sh_ninitial++]=(shInitial){.generation=s->generation,.bucket=b,
                .code=h->code,.origin=h->origin,.id=h->id};
        }
    }
    memset(&sh_totals[SH_COUNT],0,sizeof(sh_totals[SH_COUNT]));sh_phase=SH_COUNT;sh_count_start=shNext();
}
static void shCountEnd(void) {
    serverAssert(sh_phase==SH_COUNT && sh_query==UINT_MAX && sh_call==UINT_MAX && !sh_seed.active);
    sh_count_end=shNext();sh_phase=SH_VALIDATE;
}
static void shCompletion(void) {
    serverAssert(sh_phase==SH_CLEANUP && !sh_seed.active && sh_query==UINT_MAX && sh_call==UINT_MAX);
    for(unsigned int i=0;i<SH_TABLES;i++)serverAssert(!sh_tables[i].key);
}
