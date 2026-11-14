/* Correctness only: no timing, profiling or instruction measurements. */
#define _GNU_SOURCE
#include <sys/mman.h>
#include <unistd.h>
#include "zset_btree.c"
int __failed_tests, __test_num;
static unsigned long descriptor_checks, lookup_checks, tree_checks, relocations;
static unsigned int observed_codes, near_limit, unaligned_records, reversed_leaves;
static const unsigned lens[] = {0,1,2,3,4,5,6,7,8,9,14,15,16,24,32,64,128,253,254,255,319,320,321,384};

static void check_descriptor(uint16_t descriptor, unsigned char *record) {
    unsigned int offset=zbtRecordOffset(descriptor);
    serverAssert(descriptor==zbtRecordDescriptor(offset,record));
    if (record[0]<=7) {
        serverAssert(zbtRecordHasInlineLength(descriptor));
        serverAssert(zbtRecordInlineLength(descriptor)==record[0]);
        observed_codes|=1u<<record[0];
    } else serverAssert((descriptor & ~ZBT_RECORD_OFFSET_MASK)==0);
    if (offset>=4080) near_limit++;
    if ((uintptr_t)record%8) unaligned_records++;
    descriptor_checks++;
}

static void check_find(zbtScoreLeaf *leaf,uint32_t hash,unsigned char *query,
                       size_t len,int expected) {
    for (unsigned int mask=0;mask<4;mask++) {
        double score=987654.0;unsigned int position=UINT_MAX;
        int found=zbtScoreLeafFindMember(leaf,hash,query,len,
            mask&1 ? &score:NULL,mask&2 ? &position:NULL);
        serverAssert(found==expected);
        if (expected) {
            serverAssert(mask&1 ? score==0.0 && signbit(score):score==987654.0);
            serverAssert(mask&2 ? position==0:position==UINT_MAX);
        } else serverAssert(score==987654.0 && position==UINT_MAX);
        lookup_checks++;
    }
}

/* The final byte of each synthetic record and query is followed immediately
 * by PROT_NONE. This deliberately also tests representable offset 4095 for
 * an empty record; production's capped 4095-byte allocation uses <=4094. */
static void guard_records(void) {
    size_t page=sysconf(_SC_PAGESIZE);serverAssert(page==4096);
    unsigned char *memory=mmap(NULL,page*4,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
    serverAssert(memory!=MAP_FAILED);
    serverAssert(mprotect(memory+page,page,PROT_NONE)==0);
    serverAssert(mprotect(memory+3*page,page,PROT_NONE)==0);
    zbtScoreLeaf *leaf=(zbtScoreLeaf *)memory;
    unsigned char bytes[512];for(unsigned int i=0;i<sizeof(bytes);i++)bytes[i]=(i*17)^0xff;
    bytes[0]=0;
    for (unsigned int n=0;n<sizeof(lens)/sizeof(lens[0]);n++) {
        size_t len=lens[n];
        for (unsigned int external=0;external<2;external++) {
            memset(memory,0,page);
            leaf->n.isleaf=1;leaf->n.count=1;leaf->n.subtree=1;
            leaf->score_base=zbtScoreToOrdered(-0.0);
            size_t storage=external ? ZBT_EXTERNAL_RECORD_BYTES:zbtPackedLengthBytes(len)+len;
            unsigned char *record=memory+page-storage;
            unsigned char *query=memory+3*page-len;
            memcpy(query,bytes,len);
            uint32_t hash=0x735a1829;
            if (external) {
                record[0]=ZBT_PACKED_EXTERNAL;
                uint64_t size=len;
                memcpy(record+ZBT_EXTERNAL_LENGTH_OFFSET,&size,sizeof(size));
                memcpy(record+ZBT_EXTERNAL_HASH_OFFSET,&hash,sizeof(hash));
                zbtExternalSetPointer(record,query);
            } else zbtPackedWriteInline(record,bytes,len);
            uint16_t descriptor=zbtRecordDescriptor(record-memory,record);
            zbtScoreLeafOffsets(leaf)[0]=descriptor;
            zbtScoreLeafHashTags(leaf)[0]=hash>>24;
            check_descriptor(descriptor,record);
            for (unsigned int reverse=0;reverse<2;reverse++) {
                leaf->reversed=reverse;
                check_find(leaf,hash,query,len,1);
                /* Same tag but a different full hash rejects external records. */
                check_find(leaf,hash^1,query,len,!external);
                check_find(leaf,hash,memory+3*page,len+1,0);
                if (len) {
                    if (external) {
                        /* Use a distinct query so changing it cannot change the stored member. */
                        unsigned char *different=malloc(len);serverAssert(different);
                        memcpy(different,query,len);different[len-1]^=1;
                        check_find(leaf,hash,different,len,0);free(different);
                    } else {
                        query[len-1]^=1;check_find(leaf,hash,query,len,0);query[len-1]^=1;
                    }
                }
            }
            /* Address relocation must preserve every descriptor code. */
            for (unsigned int offset=0;offset<=4095;offset++) {
                uint16_t moved=zbtRecordMoveDescriptor(descriptor,offset);
                serverAssert(zbtRecordOffset(moved)==offset);
                serverAssert((moved & ~ZBT_RECORD_OFFSET_MASK)==(descriptor & ~ZBT_RECORD_OFFSET_MASK));
                descriptor_checks++;
            }
        }
    }
    munmap(memory,page*4);
}

static unsigned int inspect(zbtreeSet *zs) {
    serverAssert(zbtTestCheck(zs));
    unsigned int leaves=0;
    for(zbtScoreLeaf *leaf=zs->score_first;leaf;leaf=leaf->next) {
        leaves++;if(leaf->reversed)reversed_leaves++;
        size_t capacity=zmalloc_usable_size(leaf);
        if(capacity>ZBT_SCORE_LEAF_BYTES)capacity=ZBT_SCORE_LEAF_BYTES;
        for(unsigned int i=0;i<leaf->n.count;i++) {
            uint16_t descriptor=zbtScoreLeafDescriptor(leaf,i);
            unsigned int offset=zbtRecordOffset(descriptor);
            unsigned char *record=(unsigned char *)leaf+offset;
            serverAssert(offset>=leaf->record_start);
            serverAssert(offset+zbtRecordStorageBytes(record)<=capacity);
            check_descriptor(descriptor,record);
        }
    }
    tree_checks++;return leaves;
}

static void *copy_allocation(void *old) {
    size_t bytes=zmalloc_usable_size(old);void *new=malloc(bytes);serverAssert(new);
    memcpy(new,old,bytes);relocations++;return new;
}
static void *move_plain(void *old) {void *new=copy_allocation(old);free(old);return new;}

static void mutations(void) {
    enum {N=600};sds keys[N];double scores[N];int alive[N];
    zbtreeSet *zs=zbtreeCreate();
    for(unsigned int i=0;i<N;i++) {
        unsigned int len=i<8 ? i:lens[4+i%(sizeof(lens)/sizeof(lens[0])-4)];
        unsigned char bytes[512];memset(bytes,(i%255)+1,sizeof(bytes));
        if(i>=8)memcpy(bytes,&i,sizeof(i));
        keys[i]=sdsnewlen(bytes,len);alive[i]=1;scores[i]=i%2 ? -(double)i:(double)i;
        zbtreeInsertNewRaw(zs,scores[i],(unsigned char *)keys[i],len,NULL);
        inspect(zs);
    }
    unsigned int full_leaves=inspect(zs);serverAssert(full_leaves>=3);
    for(unsigned int i=0;i<N;i+=3) {
        zbtreeInsertPosition position;
        serverAssert(zbtreeFindForAdd(zs,keys[i],NULL,&position));
        scores[i]=(i%2 ? 1e40:-1e40)+(double)i;
        zbtreeUpdateScore(zs,keys[i],scores[i],&position);inspect(zs);
    }
    /* Explicitly rebuild every leaf and check hints against its new records. */
    for(zbtScoreLeaf *leaf=zs->score_first;leaf;) {
        leaf=zbtScoreCompactLeaf(zs,leaf);inspect(zs);leaf=leaf->next;
    }
    zbtreeSet *copy=zbtreeDup(zs);inspect(copy);zbtreeFree(zs);zs=copy;
    while(zs->member_rehash)zbtIndexRehashStep(zs,1);
    serverAssert(zbtIndexStartResize(zs,N*4,1));
    zs=zbtreeDefragStart(zs,move_plain);inspect(zs);
    zbtreeDefragState state;zbtreeDefragStateReset(&state);
    unsigned long scanned;int done;
    do {done=zbtreeDefragStep(zs,&state,copy_allocation,free,&scanned);inspect(zs);} while(!done);
    for(unsigned int i=0;i<N;i++) {
        double score=0;serverAssert(zbtreeScoreRaw(zs,(unsigned char *)keys[i],sdslen(keys[i]),&score));
        serverAssert(memcmp(&score,&scores[i],sizeof(score))==0);
        if(i%5) {serverAssert(zbtreeDelete(zs,keys[i]));alive[i]=0;inspect(zs);}
    }
    serverAssert(inspect(zs)<full_leaves);
    for(unsigned int i=0;i<N;i++) {
        double score=123;int found=zbtreeScoreRaw(zs,(unsigned char *)keys[i],sdslen(keys[i]),&score);
        serverAssert(found==alive[i]);if(!found)serverAssert(score==123);
    }
    zbtreeDeleteRangeByRank(zs,20,40);inspect(zs);
    unsigned int reverse=0;
    while(zs->length) {zbtreeDeleteEdge(zs,reverse++%2);inspect(zs);}
    zbtreeFree(zs);for(unsigned int i=0;i<N;i++)sdsfree(keys[i]);
}

int main(void) {
    uint8_t seed[16];for(unsigned int i=0;i<16;i++)seed[i]=i*29+17;
    dictSetHashFunctionSeed(seed);
    guard_records();mutations();
    serverAssert(observed_codes==255 && near_limit && unaligned_records && reversed_leaves && relocations);
    printf("{\"passed\":true,\"descriptor_checks\":%lu,\"lookup_checks\":%lu,\"tree_checks\":%lu,\"relocations\":%lu,\"observed_codes\":%u,\"near_limit\":%u,\"unaligned_records\":%u,\"reversed_leaves\":%u}\n",
        descriptor_checks,lookup_checks,tree_checks,relocations,observed_codes,near_limit,unaligned_records,reversed_leaves);
    return 0;
}
