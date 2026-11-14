#define _GNU_SOURCE
/* Correctness only: independent decoder, optional validation and assertions. */
#include <sys/mman.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include "zset_btree.c"
static unsigned long checks, assertions;

static const unsigned char *reference(const unsigned char *r, size_t *len) {
    unsigned marker = r[0];
    if (marker < 254) { *len = marker; return r+1; }
    if (marker == 254) {
        uint16_t value; memcpy(&value,r+1,sizeof(value)); *len=value; return r+3;
    }
    uint64_t value; unsigned char *p;
    memcpy(&value,r+5,sizeof(value)); memcpy(&p,r+13,sizeof(p));
    serverAssert(p && value <= SIZE_MAX); *len=(size_t)value; return p;
}

static void external(unsigned char *r, unsigned char *p, size_t len, uint32_t hash) {
    uint64_t n=len; r[0]=255;
    memcpy(r+1,&hash,sizeof(hash)); memcpy(r+5,&n,sizeof(n)); memcpy(r+13,&p,sizeof(p));
}

static void check(const unsigned char *r, uint32_t hash) {
    size_t expected_len;
    const unsigned char *expected=reference(r,&expected_len);
    size_t n=SIZE_MAX;
    const unsigned char *p=zbtPackedData(r,&n);
    serverAssert(p==expected && n==expected_len); checks++;
    for (unsigned mode=0; mode<3; mode++) {
        uint32_t query=hash ^ (mode==2 ? 1 : 0);
        n=SIZE_MAX;
        p=zbtPackedDataChecked(r,&n,mode ? &query : NULL);
        int rejected=mode==2 && r[0]==255;
        serverAssert(rejected ? p==NULL && n==SIZE_MAX : p==expected && n==expected_len);
        checks++;
    }
}

static void assertion_children(unsigned char *record, uint32_t hash) {
    for (unsigned mode=0; mode<2; mode++) {
        pid_t child=fork(); serverAssert(child>=0);
        if (child==0) {
            struct rlimit limit={0,0}; setrlimit(RLIMIT_CORE,&limit);
            int fd=open("/dev/null",O_WRONLY);
            if (fd<0 || dup2(fd,STDERR_FILENO)<0) _exit(8);
            close(fd);
            size_t n=0;
            if (mode) zbtPackedDataChecked(record,&n,&hash);
            else zbtPackedData(record,&n);
            _exit(9);
        }
        int status; serverAssert(waitpid(child,&status,0)==child);
        serverAssert(WIFSIGNALED(status) && WTERMSIG(status)==SIGABRT);
        assertions++;
    }
}

int main(void) {
    unsigned char storage[1024], payload[384];
    for (unsigned i=0; i<sizeof(payload); i++) payload[i]=(uint8_t)(97*i);
    uint32_t hash=UINT32_C(0xffabcdef);
    for (unsigned alignment=0; alignment<16; alignment++) {
        unsigned char *r=storage+alignment;
        for (size_t n=0; n<=319; n++) {
            zbtPackedWriteInline(r,payload,n); check(r,hash);
        }
        /* Existing external storage may retain arbitrarily short lengths. */
        for (size_t n=0; n<=384; n++) {
            external(r,payload,n,hash); check(r,hash);
        }
    }
    external(storage,NULL,0,hash);
    uint32_t other=hash^1; size_t n=SIZE_MAX;
    serverAssert(zbtPackedDataChecked(storage,&n,&other)==NULL && n==SIZE_MAX);
    checks++;
    assertion_children(storage,hash);

    /* No pointer/length bytes are readable after the external header/hash.
     * A mismatching hash must reject before accessing that protected region. */
    size_t page=(size_t)sysconf(_SC_PAGESIZE);
    unsigned char *m=mmap(NULL,page*2,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);
    serverAssert(m!=MAP_FAILED && mprotect(m+page,page,PROT_NONE)==0);
    unsigned char *r=m+page-5; r[0]=255; memcpy(r+1,&hash,sizeof(hash));
    n=SIZE_MAX;
    serverAssert(zbtPackedDataChecked(r,&n,&other)==NULL && n==SIZE_MAX);
    checks++;
    serverAssert(munmap(m,page*2)==0);
    printf("{\"passed\":true,\"decoder_checks\":%lu,\"expected_null_assertions\":%lu,"
           "\"guarded_hash_rejection\":true}\n",checks,assertions);
    return 0;
}
