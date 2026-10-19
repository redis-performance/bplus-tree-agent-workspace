#define _GNU_SOURCE 1
#include "zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
int main(void) {
    size_t page = (size_t)sysconf(_SC_PAGESIZE), checks = 0;
    unsigned char *base = mmap(NULL, page*3, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
    serverAssert(base != MAP_FAILED);
    serverAssert(mprotect(base+page,page,PROT_READ|PROT_WRITE)==0);
    for (unsigned tag=0;tag<256;tag++) for(size_t n=0;n<=96;n++) {
        for (int edge=0;edge<2;edge++) {
            uint8_t *p=edge ? base+2*page-n : base+page;
            memset(p,(uint8_t)(tag+1),n);
            serverAssert(zbtFindTagSIMD(p,(uint8_t)tag,n)==NULL);checks++;
            for (size_t pos=0;pos<n;pos++) {
                memset(p,(uint8_t)(tag+1),n);p[pos]=(uint8_t)tag;
                if(pos+1<n)p[n-1]=(uint8_t)tag;
                serverAssert(zbtFindTagSIMD(p,(uint8_t)tag,n)==p+pos);checks++;
                if(pos+1<n)serverAssert(zbtFindTagSIMD(p+pos+1,(uint8_t)tag,n-pos-1)==p+n-1);
            }
        }
    }
    serverAssert(zbtFindTagSIMD(base,(uint8_t)1,0)==NULL);
    serverAssert(munmap(base,page*3)==0);
    printf("PASS %zu first-match/page-boundary cases\n", checks);
    return 0;
}
