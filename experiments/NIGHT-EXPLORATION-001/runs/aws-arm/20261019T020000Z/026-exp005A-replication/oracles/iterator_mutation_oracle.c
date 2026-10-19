/* Per-call masks, arbitrary nonzero reverse, iterator copies after mixed edits. */
#include "server.h"
#include "zset_btree.h"
#include <float.h>
#include <math.h>
#include <inttypes.h>
#include <string.h>
#define MAXN 513
static sds keys[MAXN];static double scores[MAXN];static unsigned char live[MAXN];
static unsigned nkeys,stage;static uint64_t checks,nexts,updates,deletes,inserts,mask_seen[8],reverse_seen[4];
static const int directions[]={0,1,-1,2};
static uint64_t bits(double x){uint64_t u;memcpy(&u,&x,8);return u;}
static uint64_t random64(uint64_t *s){uint64_t z=(*s+=UINT64_C(0x9e3779b97f4a7c15));z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);return z^(z>>31);}
static int compare(const void *ap,const void *bp){unsigned a=*(const unsigned*)ap,b=*(const unsigned*)bp;if(scores[a]<scores[b])return -1;if(scores[a]>scores[b])return 1;size_t an=sdslen(keys[a]),bn=sdslen(keys[b]);int c=memcmp(keys[a],keys[b],an<bn?an:bn);return c?c:(an>bn)-(an<bn);}
static void next(zbtreeIterator *it,int reverse,unsigned id,unsigned mask){
 const unsigned char sentinel=97,*ele=&sentinel;size_t len=SIZE_MAX;double score=12345.5;
 serverAssert(zbtreeIteratorNext(it,reverse,mask&1?&ele:NULL,mask&2?&len:NULL,mask&4?&score:NULL));
 if(mask&1)serverAssert(!memcmp(ele,keys[id],sdslen(keys[id])));else serverAssert(ele==&sentinel);
 if(mask&2)serverAssert(len==sdslen(keys[id]));else serverAssert(len==SIZE_MAX);
 if(mask&4)serverAssert(bits(score)==bits(scores[id]));else serverAssert(score==12345.5);
 nexts++;mask_seen[mask]++;
}
static void exhausted(zbtreeIterator *it,int reverse){
 for(unsigned k=0;k<3;k++){const unsigned char sentinel=53,*ele=&sentinel;size_t len=SIZE_MAX;double score=-12345.5;
 serverAssert(!zbtreeIteratorNext(it,reverse,&ele,&len,&score));serverAssert(ele==&sentinel&&len==SIZE_MAX&&score==-12345.5);}
}
static void verify(zbtreeSet *tree){
 unsigned order[MAXN];size_t n=0;for(unsigned i=0;i<nkeys;i++)if(live[i])order[n++]=i;
 qsort(order,n,sizeof(*order),compare);serverAssert(zbtreeLength(tree)==n);
 for(unsigned d=0;d<4;d++){
  int reverse=directions[d];zbtreeIterator it;serverAssert(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));reverse_seen[d]++;
  for(size_t j=0;j<n;j++){
   size_t k=reverse?n-1-j:j;unsigned id=order[k];unsigned mask=(j*5+stage+d)&7;
   /* Copy state before consuming; masks differ but both must yield the same item. */
   if(j%17==0){zbtreeIterator copy=it;next(&copy,reverse,id,mask^7);if(j+1<n)next(&copy,reverse,order[reverse?k-1:k+1],7);else exhausted(&copy,reverse);}
   next(&it,reverse,id,mask);
   double score;serverAssert(zbtreeRank(tree,keys[id],reverse,&score)==(long)j);serverAssert(bits(score)==bits(scores[id]));
   zbtreeIterator seek;serverAssert(zbtreeIteratorSeekRank(tree,k,&seek));next(&seek,reverse,id,7);
  }
  exhausted(&it,reverse);
  zbtreeIterator miss;serverAssert(!zbtreeIteratorSeekRank(tree,n,&miss));exhausted(&miss,reverse);
 }
 for(unsigned i=0;i<nkeys;i++){double score=13.25;serverAssert(zbtreeScore(tree,keys[i],&score)==live[i]);if(live[i])serverAssert(bits(score)==bits(scores[i]));}
 checks++;
}
static void exercise(unsigned n,uint64_t seed){
 nkeys=n;stage=0;uint64_t rng=seed;uint8_t hashseed[16];for(unsigned i=0;i<16;i++)hashseed[i]=random64(&rng);dictSetHashFunctionSeed(hashseed);
 const size_t lengths[]={2,3,8,16,319,320,321,511};
 double values[]={-DBL_MAX,-0x1p53,-32769,-129,-128,-1,-DBL_MIN,-DBL_TRUE_MIN,-0.0,0.0,DBL_TRUE_MIN,DBL_MIN,0.25,127,128,32768,0x1p53,DBL_MAX};
 zbtreeSet *tree=zbtreeCreate();
 for(unsigned i=0;i<n;i++){unsigned char buf[511];size_t len=i?lengths[i%8]:0;memset(buf,0xa5,len);if(len){buf[0]=i>>8;buf[1]=i;}keys[i]=sdsnewlen(buf,len);scores[i]=values[i%18];live[i]=1;zbtreeInsertNew(tree,scores[i],keys[i],NULL);inserts++;}
 verify(tree);
 for(stage=1;stage<=4096;stage++){
  unsigned id=random64(&rng)%n;unsigned action=random64(&rng)%4;
  if(live[id] && action==0){serverAssert(zbtreeDelete(tree,keys[id]));live[id]=0;deletes++;}
  else if(!live[id]){scores[id]=values[random64(&rng)%18];zbtreeInsertNew(tree,scores[id],keys[id],NULL);live[id]=1;inserts++;}
  else{zbtreeInsertPosition pos;double old;serverAssert(zbtreeFindForAdd(tree,keys[id],&old,&pos));serverAssert(bits(old)==bits(scores[id]));double target=values[random64(&rng)%18];zbtreeUpdateScore(tree,keys[id],target,&pos);scores[id]=target;updates++;}
  if(stage%16==0)verify(tree);
 }
 for(unsigned i=0;i<n;i++)if(live[i]){serverAssert(zbtreeDelete(tree,keys[i]));live[i]=0;deletes++;}verify(tree);zbtreeFree(tree);
 for(unsigned i=0;i<n;i++)sdsfree(keys[i]);
 printf("n=%u seed=%"PRIu64" PASS checks=%"PRIu64" nexts=%"PRIu64"\n",n,seed,checks,nexts);fflush(stdout);
}
int main(void){exercise(97,8303);exercise(513,8303);exercise(97,8311);exercise(513,8311);for(unsigned i=0;i<8;i++)serverAssert(mask_seen[i]>0);for(unsigned i=0;i<4;i++)serverAssert(reverse_seen[i]>0);printf("PASS checks=%"PRIu64" nexts=%"PRIu64" updates=%"PRIu64" deletes=%"PRIu64" inserts=%"PRIu64"\n",checks,nexts,updates,deletes,inserts);}
