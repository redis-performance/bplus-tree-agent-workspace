/* Exact first-match oracle; source-included for helper sensitivity only, never timing. */
#include "../src/zset_btree.c"
#include <inttypes.h>
int main(void){
 uint8_t storage[256];uint64_t checks=0,digest=14695981039346656037ULL;
 for(unsigned pattern=0;pattern<3;pattern++)for(unsigned align=0;align<16;align++){
  for(unsigned i=0;i<256;i++)storage[i]=pattern==0?(uint8_t)((i*73U)^(i>>1)):pattern==1?255:(uint8_t)(i%2);
  uint8_t *p=storage+align;
  for(size_t n=0;n<=128;n++)for(unsigned tag=0;tag<256;tag++){
   uint8_t *expected=NULL;for(size_t j=0;j<n;j++)if(p[j]==tag){expected=p+j;break;}
#ifdef ZBT_INLINE_TAG_SEARCH
   uint8_t *found=zbtInlineTagSearch(p,(uint8_t)tag,n);
#else
   uint8_t *found=memchr(p,(uint8_t)tag,n);
#endif
   serverAssert(found==expected);digest=(digest^(found?(uint64_t)(found-p)+1:0))*1099511628211ULL;checks++;
  }
 }
 printf("PASS tagchecks=%"PRIu64" digest=%016"PRIx64"\n",checks,digest);return 0;
}
