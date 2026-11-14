/* Only called after original destruction and the completion fence. */
static void shPrintGeneration(uint64_t generation) {
    if(generation)printf("%" PRIu64,generation);else printf("null");
}
static void censusPrint(void) {
    shCompletion();
    printf("\"table_call_count\":%u,\"query_count\":%u,\"query_resize\":[",sh_ncalls,sh_nqueries);
    for(unsigned int i=0;i<sh_nqueries;i++)printf("%s[%u,%u]",i ? ",":"",sh_queries[i].before,sh_queries[i].after);
    printf("],\"query_bounds\":[");
    for(unsigned int i=0;i<sh_nqueries;i++)printf("%s[%" PRIu64 ",%" PRIu64 "]",i ? ",":"",sh_queries[i].seq,sh_queries[i].end_seq);
    printf("],\"count_start\":%" PRIu64 ",\"count_end\":%" PRIu64 ",\"initial_hints\":[",sh_count_start,sh_count_end);
    for(unsigned int i=0;i<sh_ninitial;i++) {
        shInitial *e=&sh_initial[i];
        printf("%s{\"generation\":%" PRIu64 ",\"bucket\":%lu,\"code\":%u,\"origin\":%u,\"id\":%" PRIu32 "}",
            i ? ",":"",e->generation,e->bucket,e->code,e->origin,e->id);
    }
    printf("],\"table_calls\":[");
    for(unsigned int i=0;i<sh_ncalls;i++) {
        censusCall *c=&sh_calls[i];
        printf("%s{\"call\":%u,\"query\":%u,\"seq\":%" PRIu64 ",\"end_seq\":%" PRIu64 ",\"generation\":",i ? ",":"",i,c->query,c->seq,c->end_seq);
        shPrintGeneration(c->generation);
        printf(",\"active_resize\":%u,\"destination_table\":%u,\"wide_ids\":%u,\"table_buckets\":%lu,\"result\":%u",
            c->active_resize,c->destination_table,c->wide_ids,c->table_buckets,c->result);
#define SH_PRINT(k) printf(",\"" #k "\":%" PRIu64,c->k);
        SH_COUNTERS(SH_PRINT)
#undef SH_PRINT
        printf("}");
    }
    printf("],\"lifecycle\":[");
    for(unsigned int i=0;i<sh_nlife;i++) {
        shLife *e=&sh_life[i];
        printf("%s{\"seq\":%" PRIu64 ",\"phase\":%u,\"kind\":%u,\"generation\":%" PRIu64 ",\"parent\":%" PRIu64 ",\"registry_slot\":%u,\"wide_ids\":%u,\"buckets\":%lu}",
            i ? ",":"",e->seq,e->phase,e->kind,e->generation,e->parent,e->slot,e->wide,e->size);
    }
    printf("],\"phase_totals\":[");
    for(unsigned int i=0;i<SH_PHASES;i++) {
        shTotals *t=&sh_totals[i];
        printf("%s{\"phase\":%u,\"id_writes\":%" PRIu64 ",\"invalidations\":%" PRIu64 ",\"seed_attempts\":%" PRIu64 ",\"seeds\":%" PRIu64 "}",
            i ? ",":"",i,t->id_writes,t->invalidations,t->seed_attempts,t->seeds);
    }
    printf("],\"mutations\":[");
    for(unsigned int i=0;i<sh_nmutations;i++) {
        shMutation *e=&sh_mutations[i];
        printf("%s{\"seq\":%" PRIu64 ",\"generation\":%" PRIu64 ",\"query\":%u,\"kind\":%u,\"bucket\":%lu,\"id\":%" PRIu32 ",\"code\":%u,\"origin\":%u}",
            i ? ",":"",e->seq,e->generation,e->query,e->kind,e->bucket,e->id,e->code,e->origin);
    }
    printf("],\"leaf_events\":[");
    uint64_t terminals[6]={0},stale[3]={0},useful=0;unsigned char seen[SH_QUERIES]={0};
    for(unsigned int i=0;i<sh_nleaves;i++) {
        shLeafEvent *e=&sh_leaves[i];
        shInc(&terminals[e->terminal]);shInc(&stale[e->stale+1]);
        if(e->useful && !seen[e->query]) {seen[e->query]=1;shInc(&useful);}
        printf("%s{\"event\":%u,\"seq\":%" PRIu64 ",\"generation\":%" PRIu64 ",\"query\":%u,\"call\":%u,\"bucket\":%lu,\"slot\":%u,\"code\":%u,\"count\":%u,\"terminal\":%u,\"stale\":%d,\"result\":%u,\"useful\":%u,\"leaf_id\":%" PRIu32 "}",
            i ? ",":"",i,e->seq,e->generation,e->query,e->call,e->bucket,e->slot,e->code,e->count,e->terminal,e->stale,e->result,e->useful,e->leaf_id);
    }
    printf("],\"filter_events\":[");
    uint64_t filter_totals[3][3]={{0}};
    for(unsigned int i=0;i<sh_nfilters;i++) {
        shFilter *e=&sh_filters[i];unsigned int outcome=e->original ? 0:e->folded ? 2:1;
        shInc(&filter_totals[e->consumer][outcome]);
        printf("%s{\"event\":%u,\"seq\":%" PRIu64 ",\"generation\":%" PRIu64 ",\"query\":%u,\"call\":",i ? ",":"",i,e->seq,e->generation,e->query);
        if(e->call==UINT_MAX)printf("null");else printf("%u",e->call);
        printf(",\"consumer\":%u,\"original\":%u,\"folded\":%u}",e->consumer,e->original,e->folded);
    }
    printf("],\"totals\":{\"terminals\":[");
    for(unsigned int i=0;i<6;i++)printf("%s%" PRIu64,i ? ",":"",terminals[i]);
    printf("],\"stale\":[%" PRIu64 ",%" PRIu64 ",%" PRIu64 "],\"useful_queries\":%" PRIu64 ",\"filters\":[",
        stale[0],stale[1],stale[2],useful);
    for(unsigned int i=0;i<3;i++)printf("%s[%" PRIu64 ",%" PRIu64 ",%" PRIu64 "]",i ? ",":"",filter_totals[i][0],filter_totals[i][1],filter_totals[i][2]);
    printf("]}");
}
