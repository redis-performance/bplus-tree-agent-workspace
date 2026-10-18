#define _DARWIN_C_SOURCE 1
#define _GNU_SOURCE 1
#include "../src/zset_btree.c"
#include <sys/mman.h>
#include <unistd.h>
#include <inttypes.h>
#ifndef MAP_ANONYMOUS
#define MAP_ANONYMOUS MAP_ANON
#endif
int main(void){
 long page=sysconf(_SC_PAGESIZE);serverAssert(page>256);
 uint8_t *base=mmap(NULL,(size_t)page*3,PROT_NONE,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);serverAssert(base!=MAP_FAILED);
 serverAssert(!mprotect(base+page,(size_t)page,PROT_READ|PROT_WRITE));uint64_t checks=0,digest=14695981039346656037ULL;
 for(unsigned edge=0;edge<2;edge++)for(unsigned pattern=0;pattern<3;pattern++)for(size_t n=0;n<=128;n++){
  uint8_t *p=edge?base+page*2-n:base+page;
  for(size_t j=0;j<n;j++)p[j]=pattern==0?(uint8_t)(j*73U^(j>>1)):pattern==1?255:(uint8_t)(j%2);
  for(unsigned tag=0;tag<256;tag++){
   uint8_t *expected=NULL;for(size_t j=0;j<n;j++)if(p[j]==tag){expected=p+j;break;}
#ifdef ZBT_INLINE_TAG_SEARCH
   uint8_t *found=zbtInlineTagSearch(p,(uint8_t)tag,n);
#else
   uint8_t *found=memchr(p,(uint8_t)tag,n);
#endif
   serverAssert(found==expected);digest=(digest^(found?(uint64_t)(found-p)+1:0))*1099511628211ULL;checks++;
  }
 }
 serverAssert(!munmap(base,(size_t)page*3));printf("PASS guardchecks=%"PRIu64" digest=%016"PRIx64"\n",checks,digest);return 0;
}
