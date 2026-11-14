/* Diagnostic shadow state only. No original leaf call is skipped. */
#include <inttypes.h>
#define CENSUS_MAX_CALLS 4096
#define CENSUS_MAX_FAILED_LEAVES 4096
#define CENSUS_MAX_QUERIES 1000
#define CENSUS_COUNTERS(X) \
    X(bucket_visits) X(displaced_bucket_visits) X(approximate_candidates) \
    X(true_tag_candidates) X(tombstone_skips) X(free_reference_skips) \
    X(migration_skips) X(leaf_calls) X(leaf_successes) X(leaf_failures) \
    X(distinct_failed_leaves) X(repeat_failed_all) X(repeat_failed_consecutive) \
    X(repeat_failed_cross_bucket) X(leaf_entries_present) X(repeat_leaf_entries_present) \
    X(home_hit) X(filter_evaluated) X(filter_true) X(filter_false) \
    X(home_postfilter_fallback)
#define CENSUS_FIELD(name) uint64_t name;
typedef struct {
    CENSUS_COUNTERS(CENSUS_FIELD)
    unsigned int query, active_resize, destination_table, wide_ids, result;
    unsigned long table_buckets;
} censusCall;
#undef CENSUS_FIELD
typedef struct { uint32_t id; unsigned long first_bucket; } censusFailed;
typedef struct { unsigned int active_before, active_after; } censusQuery;
static int census_enabled;
static unsigned int census_call_count, census_query_count, census_failed_count;
static unsigned int census_current_query;
static uint32_t census_last_failed_id;
static int census_has_last_failed;
static censusCall census_calls[CENSUS_MAX_CALLS];
static censusFailed census_failed[CENSUS_MAX_FAILED_LEAVES];
static censusQuery census_queries[CENSUS_MAX_QUERIES];

static void censusReset(void) {
    serverAssert(!census_enabled);
    memset(census_calls,0,sizeof(census_calls));
    memset(census_queries,0,sizeof(census_queries));
    census_call_count=census_query_count=census_failed_count=0;
    census_current_query=UINT_MAX;census_has_last_failed=0;
}
static void censusQueryBegin(zbtreeSet *zs) {
    if (!census_enabled) return;
    serverAssert(census_current_query==UINT_MAX && census_query_count<CENSUS_MAX_QUERIES);
    census_current_query=census_query_count++;
    census_queries[census_current_query].active_before=zs->member_rehash!=NULL;
}
static void censusQueryEnd(zbtreeSet *zs) {
    if (!census_enabled) return;
    serverAssert(census_current_query!=UINT_MAX);
    census_queries[census_current_query].active_after=zs->member_rehash!=NULL;
    census_current_query=UINT_MAX;
}
static censusCall *censusBegin(zbtreeSet *zs,zbtIndexTable *table) {
    if (!census_enabled) return NULL;
    serverAssert(census_current_query!=UINT_MAX && census_call_count<CENSUS_MAX_CALLS);
    censusCall *c=&census_calls[census_call_count++];
    c->query=census_current_query;c->active_resize=zs->member_rehash!=NULL;
    c->destination_table=zs->member_rehash && table==&zs->member_rehash->table;
    c->wide_ids=table->wide_ids;c->table_buckets=table->size;
    census_failed_count=0;census_has_last_failed=0;
    return c;
}
static int censusEnd(censusCall *c,int result) {
    if (c) {
        c->result=result;
        serverAssert(c->leaf_calls==c->leaf_successes+c->leaf_failures);
        serverAssert(c->leaf_successes==(unsigned int)result);
        serverAssert(c->repeat_failed_all<=c->leaf_failures);
        serverAssert(c->repeat_failed_consecutive<=c->repeat_failed_all);
        serverAssert(c->repeat_failed_cross_bucket<=c->repeat_failed_all);
        serverAssert(c->distinct_failed_leaves+c->repeat_failed_all==c->leaf_failures);
        serverAssert(c->filter_evaluated==c->filter_true+c->filter_false);
        serverAssert(c->home_hit+c->filter_evaluated==(c->table_buckets!=0));
        serverAssert(c->home_postfilter_fallback==c->filter_true);
        serverAssert(c->true_tag_candidates==c->tombstone_skips+c->free_reference_skips+
                     c->migration_skips+c->leaf_calls);
    }
    return result;
}
#define CENSUS_INC(c,name) do { if (c) (c)->name++; } while (0)

static int censusLeaf(censusCall *c,zbtScoreLeaf *leaf,uint32_t hash,
                      const unsigned char *ele,size_t elelen,double *score,
                      unsigned int *position,unsigned long bucket) {
    if (!c) return zbtScoreLeafFindMember(leaf,hash,ele,elelen,score,position);
    int repeat=0,cross=0;
    for (unsigned int i=0;i<census_failed_count;i++) {
        if (census_failed[i].id==leaf->id) {
            repeat=1;cross=census_failed[i].first_bucket!=bucket;break;
        }
    }
    unsigned char score_before[sizeof(double)],position_before[sizeof(unsigned int)];
    /* Copy object bytes, without evaluating a potentially uninitialized score
     * value supplied by an ordinary caller. No floating-point interpretation. */
    if (repeat && score) memcpy(score_before,score,sizeof(score_before));
    if (repeat && position) memcpy(position_before,position,sizeof(position_before));
    c->leaf_calls++;c->leaf_entries_present+=leaf->n.count;
    int result=zbtScoreLeafFindMember(leaf,hash,ele,elelen,score,position);
    if (repeat) {
        serverAssert(!result);
        if (score) serverAssert(memcmp(score_before,score,sizeof(score_before))==0);
        if (position) serverAssert(memcmp(position_before,position,sizeof(position_before))==0);
        c->repeat_failed_all++;c->repeat_failed_cross_bucket+=cross;
        c->repeat_failed_consecutive+=census_has_last_failed && census_last_failed_id==leaf->id;
        c->repeat_leaf_entries_present+=leaf->n.count;
    }
    if (result) c->leaf_successes++;
    else {
        c->leaf_failures++;
        if (!repeat) {
            serverAssert(census_failed_count<CENSUS_MAX_FAILED_LEAVES);
            census_failed[census_failed_count++]=(censusFailed){leaf->id,bucket};
            c->distinct_failed_leaves++;
        }
        census_has_last_failed=1;census_last_failed_id=leaf->id;
    }
    return result;
}

static void censusPrintCounters(const censusCall *c) {
    int comma=0;
#define CENSUS_PRINT(name) do { printf("%s\"" #name "\":%" PRIu64,comma ? ",":"",c->name);comma=1; } while (0);
    CENSUS_COUNTERS(CENSUS_PRINT)
#undef CENSUS_PRINT
}
static void censusPrint(void) {
    censusCall total={0};
    for (unsigned int i=0;i<census_call_count;i++) {
#define CENSUS_ADD(name) total.name+=census_calls[i].name;
        CENSUS_COUNTERS(CENSUS_ADD)
#undef CENSUS_ADD
    }
    printf("\"table_call_count\":%u,\"query_count\":%u,\"totals\":{",census_call_count,census_query_count);
    censusPrintCounters(&total);printf("},\"table_calls\":[");
    for (unsigned int i=0;i<census_call_count;i++) {
        censusCall *c=&census_calls[i];
        printf("%s{\"call\":%u,\"query\":%u,\"active_resize\":%u,\"destination_table\":%u,"
               "\"wide_ids\":%u,\"table_buckets\":%lu,\"result\":%u,",i ? ",":"",i,c->query,
               c->active_resize,c->destination_table,c->wide_ids,c->table_buckets,c->result);
        censusPrintCounters(c);printf("}");
    }
    printf("],\"query_resize\":[");
    for (unsigned int i=0;i<census_query_count;i++)
        printf("%s[%u,%u]",i ? ",":"",census_queries[i].active_before,census_queries[i].active_after);
    printf("]");
}
