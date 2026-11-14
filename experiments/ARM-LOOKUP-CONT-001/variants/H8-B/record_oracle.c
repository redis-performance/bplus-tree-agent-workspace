/* Correctness only. No timers, PMU work or performance output. */
#define _GNU_SOURCE
#include "zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <signal.h>

static unsigned long checks, guarded_cases, heap_cases, collision_cases, fallback_cases;
static size_t page;
static unsigned char *leaf_map, *query_map;

static void fill(unsigned char *p, size_t n, unsigned int pattern) {
    for (size_t i=0; i<n; i++) p[i] = pattern==0 ? 0 : pattern==1 ? 255 : (unsigned char)(i*129);
}

static void init_leaf(zbtScoreLeaf *leaf, unsigned int count, int reversed) {
    memset(leaf,0,offsetof(zbtScoreLeaf,data)+count*3);
    leaf->n.isleaf=1; leaf->n.count=count; leaf->n.subtree=count;
    leaf->score_base=zbtScoreToOrdered(-0.0); leaf->reversed=reversed;
}

static void point_record(zbtScoreLeaf *leaf, unsigned int physical,
                          unsigned char *record, uint32_t hash) {
    ptrdiff_t offset=record-(unsigned char *)leaf;
    serverAssert(offset>=0 && offset<=UINT16_MAX);
    zbtScoreLeafOffsets(leaf)[physical]=(uint16_t)offset;
    zbtScoreLeafHashTags(leaf)[physical]=hash>>24;
}

static void external_record(unsigned char *record, uint32_t hash,
                             unsigned char *payload, size_t n) {
    uint64_t len=n;
    record[0]=ZBT_PACKED_EXTERNAL;
    memcpy(record+ZBT_EXTERNAL_HASH_OFFSET,&hash,sizeof(hash));
    memcpy(record+ZBT_EXTERNAL_LENGTH_OFFSET,&len,sizeof(len));
    memcpy(record+ZBT_EXTERNAL_POINTER_OFFSET,&payload,sizeof(payload));
}

static void check(zbtScoreLeaf *leaf, uint32_t hash,
                    const unsigned char *query, size_t len,
                    int expected, unsigned int logical) {
    for (unsigned int mask=0; mask<4; mask++) {
        double score=12345.0, wanted=-0.0;
        unsigned int position=UINT_MAX;
        int found=zbtScoreLeafFindMember(leaf,hash,query,len,
                         mask&1 ? &score : NULL,mask&2 ? &position : NULL);
        serverAssert(found==expected);
        if (found && (mask&1)) serverAssert(memcmp(&score,&wanted,sizeof(score))==0);
        else serverAssert(score==12345.0);
        serverAssert(position==(found && (mask&2) ? logical : UINT_MAX));
        checks++;
    }
}

/* Query mode0 starts directly after an inaccessible page; mode1 ends at an
 * inaccessible page; modes2..17 exercise every address residue modulo16. */
static unsigned char *query_at(size_t len, unsigned int mode) {
    if (mode==0) return query_map+page;
    if (mode==1) return query_map+2*page-len;
    return query_map+page+128+mode-2;
}

/* The leading stored marker must stay accessible. Mode0 places that marker
 * immediately after an inaccessible page; mode1 ends the payload at one. */
static unsigned char *payload_at(size_t len, unsigned int mode) {
    if (mode==0) return leaf_map+2*page+1;
    if (mode==1) return leaf_map+3*page-len;
    return leaf_map+2*page+128+mode-2;
}

static void guarded_short(void) {
    zbtScoreLeaf *leaf=(zbtScoreLeaf *)leaf_map;
    for (size_t n=0; n<=8; n++)
        for (unsigned int qm=0; qm<18; qm++)
            for (unsigned int rm=0; rm<18; rm++)
                for (unsigned int pattern=0; pattern<3; pattern++)
                    for (unsigned int tag=0; tag<2; tag++) {
                        uint32_t hash=(tag ? UINT32_C(0xff000000) : 0)|UINT32_C(0x123456);
                        unsigned char *query=query_at(n,qm),*payload=payload_at(n,rm);
                        init_leaf(leaf,1,tag);
                        payload[-1]=n;fill(payload,n,pattern);fill(query,n,pattern);
                        point_record(leaf,0,payload-1,hash);
                        check(leaf,hash,query,n,1,0);
                        for (size_t i=0; i<n; i++) {
                            query[i]^=0x80;check(leaf,hash,query,n,0,0);query[i]^=0x80;
                            payload[i]^=0x80;check(leaf,hash,query,n,0,0);payload[i]^=0x80;
                        }
                        /* A tag hit is not enough when lengths differ. */
                        payload[-1]=n ? n-1 : 1;
                        check(leaf,hash,query,n,0,0);
                        payload[-1]=n;
                        guarded_cases++;
                    }
    init_leaf(leaf,0,0);
    unsigned char valid=0;
    check(leaf,0,&valid,0,0,0);
}

/* Exact allocation ends additionally let ASan catch sub-page overreads. */
static void heap_short(void) {
    for (size_t n=0; n<=8; n++) {
        size_t record_offset=offsetof(zbtScoreLeaf,data)+3;
        zbtScoreLeaf *leaf=calloc(1,record_offset+1+n);
        unsigned char *query=malloc(n ? n : 1);
        serverAssert(leaf && query);
        init_leaf(leaf,1,0);
        unsigned char *record=(unsigned char *)leaf+record_offset;
        record[0]=n;fill(record+1,n,2);fill(query,n,2);
        point_record(leaf,0,record,0);
        check(leaf,0,query,n,1,0);
        for (size_t i=0; i<n; i++) {
            record[i+1]^=0x40;check(leaf,0,query,n,0,0);record[i+1]^=0x40;
        }
        free(query);free(leaf);heap_cases++;
    }
}

static void collisions(void) {
    zbtScoreLeaf *leaf=(zbtScoreLeaf *)leaf_map;
    for (size_t n=0; n<=8; n++)
        for (int reversed=0; reversed<2; reversed++)
            for (unsigned int tag=0; tag<2; tag++) {
                uint32_t hash=(tag ? UINT32_C(0xff000000) : 0)|UINT32_C(0x654321);
                unsigned char *query=query_at(n,1),*payload=payload_at(n,1);
                fill(query,n,2);fill(payload,n,2);payload[-1]=n;
                init_leaf(leaf,6,reversed);
                unsigned char *r0=leaf_map+256,*r1=leaf_map+320;
                unsigned char *r2=leaf_map+384,*r3=leaf_map+448,*r5=leaf_map+512;
                r0[0]=9;fill(r0+1,9,2);
                r1[0]=n ? n-1 : 1;fill(r1+1,r1[0],2);
                if (n) {r2[0]=n;fill(r2+1,n,2);r2[1]^=0x80;}
                else external_record(r2,hash^1,leaf_map+page,0);
                /* Same tag, different full hash: inaccessible payload proves
                 * the existing full-hash filter runs before dereferencing it. */
                external_record(r3,hash^1,NULL,n);
                unsigned char *different=leaf_map+640;
                fill(different,n ? n : 1,2);different[0]^=0x40;
                external_record(r5,hash,different,n ? n : 1);
                unsigned char *records[]={r0,r1,r2,r3,payload-1,r5};
                for (unsigned int i=0; i<6; i++) point_record(leaf,i,records[i],hash);
                check(leaf,hash,query,n,1,reversed ? 1 : 4);
                /* The other candidates include same-full-hash unequal bytes. */
                if (n) payload[0]^=0x80; else payload[-1]=1;
                check(leaf,hash,query,n,0,0);
                if (n) payload[0]^=0x80; else payload[-1]=0;
                /* A preserved external representation of a short member must
                 * take the generic path, even for length0. */
                external_record(r5,hash,payload,n);
                zbtScoreLeafHashTags(leaf)[4]^=1;
                check(leaf,hash,query,n,1,reversed ? 0 : 5);
                collision_cases++;
            }
}

static void generic_fallback(void) {
    
    zbtScoreLeaf *leaf=(zbtScoreLeaf *)leaf_map;
    for (size_t n=0; n<=384; n++) {
        if (n>256 && n!=319 && n!=320 && n!=384) continue;
        unsigned char *query=query_at(n,1),*payload=payload_at(n,1);
        fill(query,n,2);fill(payload,n,2);
        init_leaf(leaf,1,0);
        unsigned char *record;
        if (n<ZBT_EXTERNAL_MEMBER_AT) {
            record=payload-zbtPackedLengthBytes(n);
            zbtPackedWriteInline(record,query,n);
            serverAssert(record[0]==(n<ZBT_PACKED_SHORT ? n : ZBT_PACKED_SHORT));
        } else {
            record=leaf_map+512;external_record(record,0xabcdef,payload,n);
        }
        point_record(leaf,0,record,0xabcdef);
        check(leaf,0xabcdef,query,n,1,0);
        /* Length rejection must not read the inaccessible query, while a
         * shorter equal prefix must not count as an exact member. */
        check(leaf,0xabcdef,query_map+2*page,n+1,0,0);
        if (n) check(leaf,0xabcdef,query,n-1,0,0);
        for (size_t i=0; i<n; i++) {
            query[i]^=0x80;check(leaf,0xabcdef,query,n,0,0);query[i]^=0x80;
            payload[i]^=0x40;check(leaf,0xabcdef,query,n,0,0);payload[i]^=0x40;
        }
        fallback_cases++;
    }
}

/* A rejected external header/hash ends exactly at inaccessible storage.
 * No length/pointer field is accessible, even for an unaligned record. */
static void null_rejection(void) {
    zbtScoreLeaf *leaf=(zbtScoreLeaf *)leaf_map;
    uint32_t hash=UINT32_C(0x7f654321),other=hash^1;
    unsigned char *record=leaf_map+page-5;
    record[0]=ZBT_PACKED_EXTERNAL;
    memcpy(record+1,&other,4);
    init_leaf(leaf,1,0);point_record(leaf,0,record,hash);
    check(leaf,hash,query_map+2*page,0,0,0);
    record=leaf_map+512;
    external_record(record,other,NULL,0);point_record(leaf,0,record,hash);
    check(leaf,hash,query_map+2*page,0,0,0);
    /* Matching external NULL must still assert even when logical length0.
     * Isolate that deliberate contract violation and require SIGABRT. */
    external_record(record,hash,NULL,0);
    pid_t child=fork();serverAssert(child>=0);
    if (child==0) {
        struct rlimit limit={0,0};serverAssert(setrlimit(RLIMIT_CORE,&limit)==0);
        zbtScoreLeafFindMember(leaf,hash,query_map+2*page,0,NULL,NULL);
        _exit(2);
    }
    int status;serverAssert(waitpid(child,&status,0)==child);
    serverAssert(WIFSIGNALED(status) && WTERMSIG(status)==SIGABRT);
}

int main(void) {
    long size=sysconf(_SC_PAGESIZE);serverAssert(size>0);page=(size_t)size;
    serverAssert(page>=4096 && 3*page<=UINT16_MAX);
    leaf_map=mmap(NULL,4*page,PROT_NONE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
    query_map=mmap(NULL,3*page,PROT_NONE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
    serverAssert(leaf_map!=MAP_FAILED && query_map!=MAP_FAILED);
    serverAssert(mprotect(leaf_map,page,PROT_READ|PROT_WRITE)==0);
    serverAssert(mprotect(leaf_map+2*page,page,PROT_READ|PROT_WRITE)==0);
    serverAssert(mprotect(query_map+page,page,PROT_READ|PROT_WRITE)==0);
    guarded_short();heap_short();collisions();generic_fallback();null_rejection();
    serverAssert(munmap(leaf_map,4*page)==0 && munmap(query_map,3*page)==0);
    printf("{\"passed\":true,\"checks\":%lu,\"guarded_cases\":%lu,\"heap_cases\":%lu,"
           "\"collision_cases\":%lu,\"fallback_cases\":%lu}\n",
           checks,guarded_cases,heap_cases,collision_cases,fallback_cases);
    return 0;
}
