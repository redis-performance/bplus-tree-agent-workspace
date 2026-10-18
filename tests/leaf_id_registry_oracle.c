/* Private leaf-ID state machine. The synthetic registry is never a public tree. */
#include "../src/zset_btree.c"
#include <inttypes.h>
static uint64_t registrations,releases,replacements,audits,active_new,reuses;
static uint64_t digest=UINT64_C(14695981039346656037);
#define CHECK(c) do{if(!(c)){fprintf(stderr,"leaf-id-registry line=%d condition=%s\n",__LINE__,#c);abort();}}while(0)
static uint64_t next_random(uint64_t *s){*s^=*s<<13;*s^=*s>>7;*s^=*s<<17;return *s;}
static void audit(zbtreeSet *zs,zbtScoreLeaf **model,uint32_t *stack,size_t depth,uint32_t next) {
    CHECK(zs->next_score_leaf_id==next && zs->score_leaf_cap>=next);
    CHECK(zs->alloc_size==(zs->score_leaf_by_id?zmalloc_usable_size(zs->score_leaf_by_id):0));
    CHECK(zs->free_score_leaf_id==(depth?stack[depth-1]+1:0));
    unsigned char *seen=calloc(next?next:1,1);CHECK(seen);
    uint32_t link=zs->free_score_leaf_id;
    for(size_t i=depth;i>0;i--){uint32_t id=stack[i-1];CHECK(link==id+1 && id<next && !seen[id] && model[id]==NULL);seen[id]=1;
        uintptr_t marker=(uintptr_t)zs->score_leaf_by_id[id];CHECK(marker&1);link=(uint32_t)(marker>>1);
        CHECK(link==(i>1?stack[i-2]+1:0));}
    CHECK(link==0);
    for(uint32_t id=0;id<next;id++){
        if(model[id])CHECK(zs->score_leaf_by_id[id]==model[id] && model[id]->id==id && !seen[id]);
        else CHECK(seen[id]);
        digest=(digest^((uint64_t)id*2+(model[id]!=NULL)))*UINT64_C(1099511628211);
    }
    for(uint32_t id=next;id<zs->score_leaf_cap;id++)CHECK(zs->score_leaf_by_id[id]==NULL);
    free(seen);audits++;
}
static void put_new(zbtreeSet *zs,zbtScoreLeaf *leaf,zbtScoreLeaf **model,uint32_t id){
    zbtScoreRegisterLeaf(zs,leaf,ZBT_NEW_LEAF_ID);CHECK(leaf->id==id);model[id]=leaf;registrations++;
}
static void retire(zbtreeSet *zs,zbtScoreLeaf **model,uint32_t *stack,size_t *depth,uint32_t id){
    CHECK(model[id]);zbtScoreReleaseLeafId(zs,id);model[id]=NULL;stack[(*depth)++]=id;releases++;
}
static void fixture(unsigned n,uint64_t seed){
    zbtreeSet zs={0};zbtIndexRehash marker={0};size_t max=2*(size_t)n+64,used=0,depth=0;uint32_t next=0;
    zbtScoreLeaf *leaves=calloc(4*(size_t)n+128,sizeof(*leaves));zbtScoreLeaf **model=calloc(max,sizeof(*model));
    uint32_t *stack=calloc(max,sizeof(*stack)),*order=calloc(n?n:1,sizeof(*order));CHECK(leaves&&model&&stack&&order);
    for(unsigned i=0;i<n;i++){put_new(&zs,&leaves[used++],model,next++);order[i]=i;if((i&(i+1))==0)audit(&zs,model,stack,depth,next);}
    for(unsigned i=n;i>1;i--){unsigned j=(unsigned)(next_random(&seed)%i);uint32_t t=order[i-1];order[i-1]=order[j];order[j]=t;}
    for(unsigned i=0;i<n;i+=3)retire(&zs,model,stack,&depth,order[i]);
    audit(&zs,model,stack,depth,next);
    for(unsigned i=0;i<n;i+=7)if(model[order[i]]){
        uint32_t id=order[i],head=zs.free_score_leaf_id,watermark=zs.next_score_leaf_id;
        zbtScoreRegisterLeaf(&zs,&leaves[used],id);model[id]=&leaves[used++];replacements++;
        CHECK(zs.free_score_leaf_id==head && zs.next_score_leaf_id==watermark);
    }
    audit(&zs,model,stack,depth,next);zs.member_rehash=&marker;
    unsigned count=n/4+3;uint32_t start=next;
    for(unsigned i=0;i<count;i++){put_new(&zs,&leaves[used++],model,next++);active_new++;}
    for(unsigned i=0;i<count;i+=2)retire(&zs,model,stack,&depth,start+i);
    audit(&zs,model,stack,depth,next);zs.member_rehash=NULL;
    size_t bytes=zs.alloc_size;uint32_t cap=zs.score_leaf_cap;
    while(depth){uint32_t id=stack[--depth];put_new(&zs,&leaves[used++],model,id);reuses++;CHECK(zs.next_score_leaf_id==next && zs.score_leaf_cap==cap && zs.alloc_size==bytes);}
    audit(&zs,model,stack,depth,next);put_new(&zs,&leaves[used++],model,next++);
    audit(&zs,model,stack,depth,next);
    /* Alternating ends make links include both low IDs and values above65535. */
    for(uint32_t i=0;i<next;i++){uint32_t id=(i&1)?next-1-i/2:i/2;retire(&zs,model,stack,&depth,id);}
    audit(&zs,model,stack,depth,next);CHECK(used<4*(size_t)n+128);
    zfree(zs.score_leaf_by_id);free(leaves);free(model);free(stack);free(order);
}
int main(void){
    const unsigned sizes[]={0,1,15,16,17,31,32,33,255,256,257,32767,32768,32769,65519,65520,65535,65536,65537};
    const uint64_t seeds[]={51109,51131};
    for(unsigned s=0;s<2;s++)for(unsigned i=0;i<sizeof(sizes)/sizeof(*sizes);i++)fixture(sizes[i],seeds[s]);
    CHECK(active_new && reuses && replacements);
    printf("PASS fixtures=38 registrations=%"PRIu64" releases=%"PRIu64" replacements=%"PRIu64" audits=%"PRIu64" active_new=%"PRIu64" reuses=%"PRIu64" digest=%016"PRIx64"\n",registrations,releases,replacements,audits,active_new,reuses,digest);
}
