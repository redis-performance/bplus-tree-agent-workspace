/* Exhaustive compact-ID stores and tag-mask coverage; private integer domain. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#include <stddef.h>
#define GUARD 32
#define BYTES (GUARD*2+sizeof(zbtIndexBucket32)*4)
static uint64_t stores,tags,masks,false_bits,digest=UINT64_C(14695981039346656037);
static void equal(const unsigned char *a,const unsigned char *b,size_t n) {
    for(size_t i=0;i<n;i++)if(a[i]!=b[i]){fprintf(stderr,"index-storage byte=%zu got=%u want=%u\n",i,a[i],b[i]);abort();}
    for(size_t i=0;i<n;i++)digest=(digest^a[i])*UINT64_C(1099511628211);
}
static void storage(int wide) {
    /* malloc alignment +32 keeps both bucket forms naturally aligned. */
    unsigned char *actual=zmalloc(BYTES),expected[BYTES];
    for(size_t i=0;i<BYTES;i++)actual[i]=expected[i]=(unsigned char)(i*53+19);
    zbtIndexTable table={0};table.size=4;table.wide_ids=wide;table.buckets=(zbtIndexBucket*)(actual+GUARD);
    size_t stride=wide?sizeof(zbtIndexBucket32):sizeof(zbtIndexBucket16);
    for(unsigned b=0;b<4;b++)serverAssert((unsigned char*)zbtIndexBucketAt(&table,b)==actual+GUARD+b*stride);
    zbtIndexBucket *bucket=zbtIndexBucketAt(&table,2);
    const uint32_t edges[]={65536,65537,0x7fffffff,0x80000000,0xfffffffe,UINT32_MAX};
    unsigned limit=wide?65536+6:65536;
    for(unsigned pos=0;pos<8;pos++)for(unsigned k=0;k<limit;k++) {
        uint32_t id=wide?(k<65536?k:edges[k-65536]):(k<65535?k:UINT32_MAX);
        size_t offset=GUARD+2*stride+(wide?offsetof(zbtIndexBucket32,id):offsetof(zbtIndexBucket16,id))+pos*(wide?4:2);
        if(wide)memcpy(expected+offset,&id,4);
        else {uint16_t value=id==UINT32_MAX?UINT16_MAX:(uint16_t)id;memcpy(expected+offset,&value,2);}
        zbtIndexSetId(&table,bucket,pos,id);equal(actual,expected,BYTES);
        if(zbtIndexGetId(&table,bucket,pos)!=id){fprintf(stderr,"index-storage decode wide=%d pos=%u id=%u\n",wide,pos,id);abort();}stores++;
    }
    for(unsigned pos=0;pos<8;pos++)for(unsigned t=0;t<256;t++) {
        uint64_t value;size_t off=GUARD+2*stride;memcpy(&value,expected+off,8);
        unsigned char bytes[8];for(unsigned i=0;i<8;i++)bytes[i]=(unsigned char)(value>>(8*i));bytes[pos]=(unsigned char)t;
        value=0;for(unsigned i=0;i<8;i++)value|=(uint64_t)bytes[i]<<(8*i);
        memcpy(expected+off,&value,8);zbtIndexSetTag(bucket,pos,t);equal(actual,expected,BYTES);tags++;
    }
    zfree(actual);
}
static void tag_masks(void) {
    for(unsigned query=0;query<256;query++)for(unsigned pivot=0;pivot<8;pivot++)for(unsigned pattern=0;pattern<256;pattern++) {
        uint64_t value=0,exact=0;
        for(unsigned i=0;i<8;i++) {unsigned t=i==pivot?query:(pattern>>(i%8)&1?query^1:query^255);value|=(uint64_t)t<<(8*i);if(t==query)exact|=UINT64_C(128)<<(8*i);}
        uint64_t mask=zbtIndexTagMask(value,query);serverAssert((mask&exact)==exact && !(mask&~UINT64_C(0x8080808080808080)));
        unsigned previous=0,seen=0;
        while(mask){unsigned first=8;for(unsigned i=0;i<8;i++)if(mask&(UINT64_C(128)<<(8*i))){first=i;break;}
            serverAssert(zbtIndexFirstTag(mask)==first && (!seen||first>previous));previous=first;seen++;
            false_bits+=((value>>(8*first))&255)!=query;mask&=~(UINT64_C(128)<<(8*first));}
        digest=(digest^value)*UINT64_C(1099511628211);masks++;
    }
}
int main(void) {
    storage(0);storage(1);tag_masks();
    serverAssert(stores==UINT64_C(1048624) && tags==4096 && masks==524288 && false_bits);
    printf("PASS stores=%"PRIu64" tags=%"PRIu64" masks=%"PRIu64" false_bits=%"PRIu64" digest=%016"PRIx64"\n",stores,tags,masks,false_bits,digest);
}
