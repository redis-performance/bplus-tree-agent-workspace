/* Public mutations only; private state is read solely to require lifecycle coverage. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#define LIMIT 66000U
static unsigned char live[LIMIT],seen[LIMIT];
static double scores[LIMIT];
static unsigned total,seed,mode,stage;
static uint64_t checks,results,fixtures,active_allocations,reuses,retired_cursors;
static uint64_t digest=UINT64_C(14695981039346656037);
#define CHECK(c) do{if(!(c)){fprintf(stderr,"leaf-id-lifecycle seed=%u mode=%u stage=%u line=%d condition=%s\n",seed,mode,stage,__LINE__,#c);abort();}}while(0)
static uint64_t bits(double d){uint64_t b;memcpy(&b,&d,8);return b;}
static void mix(uint64_t u){digest=(digest^u)*UINT64_C(1099511628211);}
static void key(unsigned id,unsigned char *buf){
    for(unsigned j=0;j<319;j++)buf[j]=(unsigned char)(seed+id*17+j*37);
    for(unsigned j=0;j<4;j++)buf[j]=(unsigned char)(id>>(24-8*j));
    buf[7]=0;buf[31]=255;
}
static unsigned identify(const unsigned char *buf,size_t len,double score){
    CHECK(len==319);unsigned id=0;for(unsigned j=0;j<4;j++)id=(id<<8)|buf[j];
    CHECK(id<total && live[id]);unsigned char expected[319];key(id,expected);
    CHECK(!memcmp(buf,expected,319) && bits(score)==bits(scores[id]));results++;return id;
}
static int compare(const void *a,const void *b){
    unsigned x=*(const unsigned *)a,y=*(const unsigned *)b;
    if(scores[x]<scores[y])return -1;if(scores[x]>scores[y])return 1;
    unsigned char bx[319],by[319];key(x,bx);key(y,by);return memcmp(bx,by,319);
}
static unsigned ordered(unsigned *order){unsigned n=0;for(unsigned i=0;i<total;i++)if(live[i])order[n++]=i;qsort(order,n,sizeof(*order),compare);return n;}
static uint64_t node(zbtScoreNode *p,zbtScoreInner *parent,unsigned slot,size_t *bytes){
    if(!p)return 0;CHECK(p->parent==parent && (!parent||p->parent_index==slot));
    *bytes+=zmalloc_usable_size(p);uint64_t n=0;
    if(p->isleaf){n=p->count;CHECK(n && !p->has_external);}
    else{zbtScoreInner *in=(zbtScoreInner *)p;CHECK(p->count);for(unsigned i=0;i<p->count;i++){uint64_t sub=node(in->child[i],in,i,bytes);CHECK(sub==in->child_count[i]);n+=sub;}}
    CHECK(p->subtree==n);return n;
}
static void structural(zbtreeSet *t){
    size_t bytes=zmalloc_usable_size(t)+zmalloc_usable_size(t->score_leaf_by_id)+zmalloc_usable_size(t->member_index.buckets);
    if(t->member_rehash)bytes+=zmalloc_usable_size(t->member_rehash)+zmalloc_usable_size(t->member_rehash->table.buckets);
    CHECK(node(t->score_root,NULL,0,&bytes)==t->length);CHECK(bytes==zbtreeAllocSize(t));
    unsigned char *ids=calloc(t->next_score_leaf_id? t->next_score_leaf_id:1,1);CHECK(ids);
    zbtScoreLeaf *prev=NULL;unsigned n=0;
    for(zbtScoreLeaf *p=t->score_first;p;p=p->next){CHECK(p->prev==prev && p->id<t->next_score_leaf_id && !ids[p->id]);CHECK(t->score_leaf_by_id[p->id]==p);ids[p->id]=1;prev=p;n+=p->n.count;}
    CHECK(prev==t->score_last && n==t->length);
    uint32_t link=t->free_score_leaf_id;unsigned free_n=0;
    while(link){uint32_t id=link-1;CHECK(id<t->next_score_leaf_id && !ids[id]);ids[id]=2;uintptr_t word=(uintptr_t)t->score_leaf_by_id[id];CHECK(word&1);link=(uint32_t)(word>>1);CHECK(++free_n<=t->next_score_leaf_id);}
    for(uint32_t id=0;id<t->next_score_leaf_id;id++)CHECK(ids[id]);
    for(uint32_t id=t->next_score_leaf_id;id<t->score_leaf_cap;id++)CHECK(t->score_leaf_by_id[id]==NULL);
    free(ids);
}
static void visit(void *ctx,const unsigned char *buf,size_t len,double score){UNUSED(ctx);seen[identify(buf,len,score)]=1;}
static void verify(zbtreeSet *t,int lookup){
    unsigned *order=malloc(LIMIT*sizeof(*order));CHECK(order);unsigned n=ordered(order);CHECK(n==zbtreeLength(t));structural(t);
    zbtIndexRehash *rehash=t->member_rehash;uint32_t next=rehash?rehash->next_leaf_id:0;uint64_t revision=t->member_revision;
    size_t owned=zbtreeAllocSize(t);
    for(int reverse=0;reverse<2;reverse++){
        zbtreeIterator it;CHECK(zbtreeIteratorStart(t,reverse,&it)==(n!=0));
        for(unsigned j=0;j<n;j++){
            unsigned rank=reverse?n-1-j:j,id=order[rank];const unsigned char *buf;size_t len;double score;
            CHECK(zbtreeIteratorNext(&it,reverse,&buf,&len,&score));CHECK(identify(buf,len,score)==id);
            zbtreeIterator seek;CHECK(zbtreeIteratorSeekRank(t,rank,&seek));CHECK(zbtreeIteratorNext(&seek,reverse,&buf,&len,&score));CHECK(identify(buf,len,score)==id);
            if(!reverse){mix(id);mix(bits(score));}
        }
        CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
    }
    memset(seen,0,sizeof(seen));uint64_t cursor=0;unsigned calls=0;
    do{cursor=zbtreeScan(t,cursor,7,visit,NULL);CHECK(++calls<65536);}while(cursor);
    for(unsigned i=0;i<total;i++)CHECK(seen[i]==live[i]);
    CHECK(t->member_rehash==rehash && (!rehash||rehash->next_leaf_id==next) && t->member_revision==revision && zbtreeAllocSize(t)==owned);
    if(lookup){
        for(unsigned i=0;i<total;i++){unsigned char buf[319];key(i,buf);double score;CHECK(zbtreeScoreRaw(t,buf,319,&score)==live[i]);if(live[i])CHECK(bits(score)==bits(scores[i]));}
        for(unsigned j=0;j<n;j++){unsigned char buf[319];key(order[j],buf);sds s=sdsnewlen(buf,319);double score;
            CHECK(zbtreeRank(t,s,0,&score)==(long)j && bits(score)==bits(scores[order[j]]));
            CHECK(zbtreeRank(t,s,1,&score)==(long)(n-1-j) && bits(score)==bits(scores[order[j]]));sdsfree(s);}
        structural(t);
    }
    checks++;free(order);
}
static void append(zbtreeSet *t){
    CHECK(total<LIMIT);unsigned id=total++;unsigned char buf[319];key(id,buf);
    double score=mode?(double)((int)(id/4)-100):(double)((int)id-100);
    if(score==0)score=(id&1)?-0.0:0.0;
    scores[id]=score;live[id]=1;
    if(stage==1)zbtreeInsertNewAppend(t,score,buf,319);else zbtreeInsertNewRaw(t,score,buf,319,NULL);
}
static unsigned uncopied(zbtreeSet *t){unsigned n=0;if(t->member_rehash)for(zbtScoreLeaf *p=t->score_first;p;p=p->next)n+=p->n.index_resize!=t->member_rehash->resize_id;return n;}
static void exercise(unsigned s,unsigned m){
    seed=s;mode=m;stage=1;total=0;memset(live,0,sizeof(live));uint8_t hs[16];uint64_t r=s;
    for(unsigned i=0;i<16;i++){r^=r<<13;r^=r>>7;r^=r<<17;hs[i]=r;}dictSetHashFunctionSeed(hs);
    zbtreeSet *t=zbtreeCreate();while(total<65536){append(t);if(uncopied(t)>=128)break;}
    CHECK(total<65536 && t->member_rehash && uncopied(t)>=128);verify(t,0);
    zbtIndexRehash *rehash=t->member_rehash;uint16_t resize=rehash->resize_id;
    uint32_t target=rehash->next_leaf_id;
    if(mode){zbtScoreLeaf *p=t->score_first;while(p && p->n.index_resize!=resize)p=p->next;CHECK(p);target=p->id;}
    CHECK(target<t->next_score_leaf_id);zbtScoreLeaf *victim=t->score_leaf_by_id[target];CHECK(victim && !((uintptr_t)victim&1));
    unsigned start=0;zbtScoreLeaf *p=t->score_first;while(p!=victim){CHECK(p);start+=p->n.count;p=p->next;}
    uint32_t successor=victim->next?victim->next->id:ZBT_NO_LEAF_ID;
    unsigned count=victim->n.count;CHECK(count && count<=96);unsigned *order=malloc(LIMIT*sizeof(*order));CHECK(order);ordered(order);
    uint32_t water=t->next_score_leaf_id;unsigned before=total;stage=2;
    CHECK(zbtreeDeleteRangeByRank(t,start,start+count-1)==count);for(unsigned j=start;j<start+count;j++)live[order[j]]=0;free(order);
    CHECK(t->member_rehash==rehash && rehash->resize_id==resize && t->next_score_leaf_id==water);
    CHECK(((uintptr_t)t->score_leaf_by_id[target]&1) && t->free_score_leaf_id==target+1);
    if(!mode){CHECK(rehash->next_leaf_id==successor && successor!=ZBT_NO_LEAF_ID);retired_cursors++;}
    verify(t,0);stage=3;unsigned added=0;
    while(t->next_score_leaf_id<water+4 && added<128){append(t);added++;CHECK(t->member_rehash==rehash && rehash->resize_id==resize);CHECK((uintptr_t)t->score_leaf_by_id[target]&1);}
    CHECK(t->next_score_leaf_id==water+4 && t->free_score_leaf_id==target+1);active_allocations+=4;verify(t,0);
    /* Copy preserves the active state but owns independent pages/tables. */
    zbtreeSet *copy=zbtreeDup(t);CHECK(copy!=t && copy->member_rehash && copy->member_rehash!=t->member_rehash);
    CHECK(copy->score_first!=t->score_first && copy->member_index.buckets!=t->member_index.buckets);verify(copy,0);verify(copy,1);zbtreeFree(copy);
    CHECK(t->member_rehash==rehash && ((uintptr_t)t->score_leaf_by_id[target]&1));
    stage=4;unsigned finish=0;while(t->member_rehash && finish<65536){unsigned char buf[319];key(total-1,buf);double score;CHECK(zbtreeScoreRaw(t,buf,319,&score));CHECK(bits(score)==bits(scores[total-1]));finish++;}
    CHECK(!t->member_rehash && finish<65536);verify(t,1);
    uint32_t head=t->free_score_leaf_id;water=t->next_score_leaf_id;CHECK(head==target+1);stage=5;unsigned reuse_inserts=0;
    while(t->free_score_leaf_id==head && reuse_inserts<128){append(t);reuse_inserts++;CHECK(!t->member_rehash && t->next_score_leaf_id==water);}
    CHECK(t->free_score_leaf_id!=head && !((uintptr_t)t->score_leaf_by_id[target]&1));CHECK(t->score_leaf_by_id[target]->id==target);reuses++;verify(t,1);
    copy=zbtreeDup(t);zbtreeFree(t);verify(copy,1);zbtreeFree(copy);fixtures++;
    printf("FIXTURE seed=%u mode=%u initial=%u deleted=%u target=%u active_inserts=%u completion_lookups=%u reuse_inserts=%u checks=%"PRIu64" digest=%016"PRIx64"\n",seed,mode,before,count,target,added,finish,reuse_inserts,checks,digest);fflush(stdout);
}
int main(void){const unsigned seeds[]={60101,60127};for(unsigned s=0;s<2;s++)for(unsigned m=0;m<2;m++)exercise(seeds[s],m);
    CHECK(fixtures==4 && retired_cursors==2 && active_allocations==16 && reuses==4);
    printf("PASS fixtures=%"PRIu64" checks=%"PRIu64" results=%"PRIu64" active_allocations=%"PRIu64" retired_cursors=%"PRIu64" reuses=%"PRIu64" digest=%016"PRIx64"\n",fixtures,checks,results,active_allocations,retired_cursors,reuses,digest);
}
