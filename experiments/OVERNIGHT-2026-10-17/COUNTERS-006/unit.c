#include "server.h"
#include <string.h>
#include <stdalign.h>
#if CAPACITY_QUANTUM
size_t diagnostic_outstanding(void);
#endif
int main(void) {
    for(size_t n=0;n<=8192;n++) {
        size_t a,b,old;unsigned char *p=zmalloc_usable(n,&a);
        serverAssert((uintptr_t)p%alignof(max_align_t)==0 && a>=n && a);
#if CAPACITY_QUANTUM
        serverAssert(a==((n?n:1)+CAPACITY_QUANTUM-1)/CAPACITY_QUANTUM*CAPACITY_QUANTUM);
#endif
        memset(p,0x5a,a);p=zrealloc_usable(p,a+17,&b,&old);serverAssert(old==a && b>=a+17);
        for(size_t i=0;i<a;i++)serverAssert(p[i]==0x5a);
        memset(p,0x3c,b);p=zrealloc_usable(p,1,&a,&old);serverAssert(old==b && a>=1);
        serverAssert(p[0]==0x3c);zfree_usable(p,&old);serverAssert(old==a);
        p=zcalloc(n);for(size_t i=0;i<n;i++)serverAssert(p[i]==0);zfree(p);
        sds s=sdsnewlen(NULL,n);serverAssert(sdslen(s)==n);sdsfree(s);
    }
    size_t old,b;void *p=zrealloc_usable(NULL,31,&b,&old);serverAssert(old==0 && b>=31);zfree(p);zfree(NULL);
#if CAPACITY_QUANTUM
    serverAssert(diagnostic_outstanding()==0);
#endif
    puts("PASS allocator requests=8193 alignment capacity realloc calloc sds ownership");
}
