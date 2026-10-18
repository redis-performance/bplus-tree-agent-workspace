/* Equal-score lexical bounds, binary prefixes and optional iterator outputs. */
#include "server.h"
#include "zset_btree.h"
#include <float.h>
#include <inttypes.h>
#include <string.h>
#define MAXN 1025
static sds keys[MAXN];
static double scores[MAXN];
static unsigned char live[MAXN];
static unsigned nkeys,case_no,stage;
static unsigned long verifies,seeks,nexts;
#define CHECK(x) do { if(!(x)){fprintf(stderr,"case=%u stage=%u line=%d: %s\n",case_no,stage,__LINE__,#x);abort();} } while(0)
static uint64_t bits(double x){uint64_t u;memcpy(&u,&x,8);return u;}
static int cmpbytes(const void *a,size_t an,const void *b,size_t bn){int c=memcmp(a,b,an<bn?an:bn);return c?c:(an>bn)-(an<bn);}
static int compare(const void *ap,const void *bp){unsigned a=*(const unsigned*)ap,b=*(const unsigned*)bp;return cmpbytes(keys[a],sdslen(keys[a]),keys[b],sdslen(keys[b]));}
static void checknext(zbtreeIterator *it,int reverse,unsigned id,unsigned mask){
 const unsigned char *key=(const unsigned char*)1;size_t len=SIZE_MAX;double score=123.5;
 CHECK(zbtreeIteratorNext(it,reverse,mask&1?&key:NULL,mask&2?&len:NULL,mask&4?&score:NULL));
 if(mask&1)CHECK(!memcmp(key,keys[id],sdslen(keys[id])));else CHECK(key==(const unsigned char*)1);
 if(mask&2)CHECK(len==sdslen(keys[id]));else CHECK(len==SIZE_MAX);
 if(mask&4)CHECK(bits(score)==bits(scores[id]));else CHECK(bits(score)==bits(123.5));nexts++;
}
static void bound(zbtreeSet *tree,unsigned *order,size_t n,sds probe,int sentinel){
 for(int reverse=0;reverse<2;reverse++)for(int exclusive=0;exclusive<2;exclusive++){
  size_t expected=n;
  for(size_t i=0;i<n;i++){
   size_t j=reverse?n-1-i:i;unsigned id=order[j];
   int c=sentinel==-1?1:sentinel==1?-1:cmpbytes(keys[id],sdslen(keys[id]),probe,sdslen(probe));
   if(reverse?(exclusive?c<0:c<=0):(exclusive?c>0:c>=0)){expected=j;break;}
  }
  for(unsigned mask=0;mask<8;mask++){
   zbtreeIterator it;unsigned long rank=ULONG_MAX;
   CHECK(zbtreeIteratorSeekLex(tree,probe,exclusive,reverse,&it,mask&1?&rank:NULL)==(expected!=n));seeks++;
   if(expected==n){CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));continue;}
   if(mask&1)CHECK(rank==expected);else CHECK(rank==ULONG_MAX);
   /* First Next returns seek result; subsequent Next crosses leaf boundaries. */
   for(unsigned step=0;step<3;step++){
    if((!reverse && expected+step>=n)||(reverse && step>expected)){
     CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));break;
    }
    checknext(&it,reverse,order[reverse?expected-step:expected+step],mask);
   }
  }
 }
}
static void verify(zbtreeSet *tree){
 unsigned order[MAXN];size_t n=0;for(unsigned i=0;i<nkeys;i++)if(live[i])order[n++]=i;
 qsort(order,n,sizeof(*order),compare);CHECK(zbtreeLength(tree)==n);
 for(size_t i=1;i<n;i++)CHECK(compare(order+i-1,order+i)<0);
 for(int reverse=0;reverse<2;reverse++){
  zbtreeIterator it;CHECK(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));
  for(size_t i=0;i<n;i++){unsigned id=order[reverse?n-i-1:i];checknext(&it,reverse,id,7);double score;CHECK(zbtreeRank(tree,keys[id],reverse,&score)==(long)i);CHECK(bits(score)==bits(scores[id]));}
  CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
 }
 bound(tree,order,n,shared.minstring,-1);bound(tree,order,n,shared.maxstring,1);
 for(unsigned i=0;i<nkeys;i++){
  bound(tree,order,n,keys[i],0);size_t len=sdslen(keys[i]);
  sds prefix=sdsnewlen(keys[i],len?len-1:0);bound(tree,order,n,prefix,0);sdsfree(prefix);
  unsigned char buf[512];memcpy(buf,keys[i],len);buf[len]=0;
  sds extension=sdsnewlen(buf,len+1);bound(tree,order,n,extension,0);sdsfree(extension);
 }
 verifies++;
}
static void exercise(unsigned n,int family,int reverse){
 case_no++;nkeys=n;stage=0;const size_t lens[]={2,3,8,16,319,320,321,511};
 for(unsigned i=0;i<n;i++){
  unsigned char buf[511];size_t len;
  if(i==0){len=0;}else if(i<3){len=1;buf[0]=i==1?'+':'-';}
  else{unsigned id=i-3;len=lens[id%8];memset(buf,0x80+(id%97),len);buf[0]=(id/8)>>8;buf[1]=(id/8)&255;}
  keys[i]=sdsnewlen(buf,len);scores[i]=family==0?-DBL_MAX:family==1?(i%2?-0.0:0.0):DBL_TRUE_MIN;live[i]=1;
 }
 zbtreeSet *tree=zbtreeCreate();
 for(unsigned j=0;j<n;j++){unsigned i=reverse?n-j-1:j;zbtreeInsertNew(tree,scores[i],keys[i],NULL);}verify(tree);
 stage=1;for(unsigned i=0;i<n;i+=3){CHECK(zbtreeDelete(tree,keys[i]));live[i]=0;}verify(tree);
 stage=2;for(unsigned j=n;j>0;j--){unsigned i=j-1;if(!live[i]){zbtreeInsertNew(tree,scores[i],keys[i],NULL);live[i]=1;}}verify(tree);
 stage=3;zbtreeSet *copy=zbtreeDup(tree);zbtreeFree(tree);tree=copy;verify(tree);
 CHECK(zbtreeDeleteRangeByRank(tree,0,ULONG_MAX)==n);memset(live,0,n);stage=4;verify(tree);zbtreeFree(tree);
 for(unsigned i=0;i<n;i++)sdsfree(keys[i]);
 printf("case=%u n=%u family=%d reverse_insert=%d PASS verifies=%lu seeks=%lu nexts=%lu\n",case_no,n,family,reverse,verifies,seeks,nexts);fflush(stdout);
}
int main(void){
 uint8_t seed[16]={29,71,191};dictSetHashFunctionSeed(seed);unsigned sizes[]={0,1,31,97,257,1025};
 for(unsigned j=0;j<6;j++)for(int family=0;family<3;family++)for(int reverse=0;reverse<2;reverse++)exercise(sizes[j],family,reverse);
 printf("PASS cases=%u verifies=%lu seeks=%lu nexts=%lu\n",case_no,verifies,seeks,nexts);
}
