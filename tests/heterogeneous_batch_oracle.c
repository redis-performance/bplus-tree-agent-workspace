/* Public-API oracle: variable binary lengths and aliased/equal duplicate lanes. */
#include "server.h"
#include "zset_btree.h"
#include <float.h>
#include <math.h>
#include <inttypes.h>
#include <string.h>
#define GROUPS 64
#define WIDTHS 21
#define N (1 + GROUPS * WIDTHS)
#define CHECK(x) do { if (!(x)) { fprintf(stderr,"stage=%u line=%d: %s\n",stage,__LINE__,#x); abort(); } } while(0)
static sds keys[N];
static double values[N];
static unsigned char live[N];
static unsigned stage;
static uint64_t batches,lanes,exact,models,aliases,copies,heterogeneous,digest=UINT64_C(14695981039346656037);
static const size_t lens[WIDTHS]={1,2,3,7,8,15,16,17,31,32,63,64,127,128,255,256,319,320,321,1024,4096};
static uint64_t bits(double x){uint64_t u;memcpy(&u,&x,8);return u;}
static void mix(uint64_t x){digest=(digest^x)*UINT64_C(1099511628211);}
static void eq(double a,double b){CHECK(bits(a)==bits(b));exact++;mix(bits(a));}
static uint64_t random64(uint64_t *s){uint64_t z=(*s+=UINT64_C(0x9e3779b97f4a7c15));z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);return z^(z>>31);}
static int cmp(const void *ap,const void *bp){
 unsigned a=*(const unsigned*)ap,b=*(const unsigned*)bp;
 if(values[a]<values[b])return -1;if(values[a]>values[b])return 1;
 size_t na=sdslen(keys[a]),nb=sdslen(keys[b]);int c=memcmp(keys[a],keys[b],na<nb?na:nb);return c?c:(na>nb)-(na<nb);
}
static void verify(zbtreeSet *tree){
 unsigned order[N],n=0;
 for(unsigned id=0;id<N;id++){
  double score=123;CHECK(zbtreeScore(tree,keys[id],&score)==live[id]);if(live[id]){eq(score,values[id]);order[n++]=id;}
  CHECK(zbtreeScoreRaw(tree,(unsigned char*)keys[id],sdslen(keys[id]),&score)==live[id]);if(live[id])eq(score,values[id]);
 }
 CHECK(zbtreeLength(tree)==n);qsort(order,n,sizeof(*order),cmp);
 for(int rev=0;rev<2;rev++){
  zbtreeIterator it;CHECK(zbtreeIteratorStart(tree,rev,&it)==(n!=0));
  for(unsigned j=0;j<n;j++){
   unsigned id=order[rev?n-1-j:j];const unsigned char *ele;size_t len;double score;
   CHECK(zbtreeIteratorNext(&it,rev,&ele,&len,&score));CHECK(len==sdslen(keys[id])&&!memcmp(ele,keys[id],len));eq(score,values[id]);
   CHECK(zbtreeRank(tree,keys[id],rev,&score)==(long)j);eq(score,values[id]);mix(id);
  }
  CHECK(!zbtreeIteratorNext(&it,rev,NULL,NULL,NULL));
 }
 models++;mix(n);
}
static void query(zbtreeSet *tree,const unsigned *ids,unsigned count){
 sds members[16];double scores[20];const double guard=-7654321.25;unsigned expected=0;int varied=0;
 for(unsigned i=0;i<20;i++)scores[i]=guard;
 for(unsigned i=0;i<count;i++){
  unsigned id=ids[i];CHECK(id<N);members[i]=(i&1)?sdsnewlen(keys[id],sdslen(keys[id])):keys[id];
  if(i&1)copies++;else aliases++;if(live[id])expected|=1U<<i;
  if(i&&sdslen(members[i])!=sdslen(members[0]))varied=1;
 }
 unsigned found=zbtreeScores(tree,count?members:NULL,count,count?scores+2:NULL);CHECK(found==expected);
 for(unsigned i=0;i<20;i++){
  if(i<2||i>=count+2)CHECK(bits(scores[i])==bits(guard));
  else if(found&(1U<<(i-2)))eq(scores[i],values[ids[i-2]]);
 }
 for(unsigned i=0;i<count;i++){
  CHECK(sdslen(members[i])==sdslen(keys[ids[i]])&&!memcmp(members[i],keys[ids[i]],sdslen(members[i])));
  if(i&1)sdsfree(members[i]);
 }
 batches++;lanes+=count;heterogeneous+=varied;mix(found);
}
static uint64_t input_hash(void){uint64_t h=UINT64_C(14695981039346656037);for(unsigned id=0;id<N;id++){h=(h^sdslen(keys[id]))*UINT64_C(1099511628211);for(size_t j=0;j<sdslen(keys[id]);j++)h=(h^(unsigned char)keys[id][j])*UINT64_C(1099511628211);}return h;}
static void grid(zbtreeSet *tree){
 uint64_t before=input_hash();
 size_t owned=zbtreeAllocSize(tree);unsigned ids[16];
 for(unsigned round=0;round<N;round++)for(unsigned count=0;count<=16;count++)for(unsigned pattern=0;pattern<3;pattern++){
  unsigned base=(round*37+stage)%N;
  for(unsigned j=0;j<count;j++){
   if(pattern==0)ids[j]=base;
   else if(pattern==1)ids[j]=(base+(j/2)*17)%N;
   else ids[j]=1+((round%GROUPS)*WIDTHS)+(j%WIDTHS);
  }
  query(tree,ids,count);
 }
 CHECK(input_hash()==before);CHECK(zbtreeAllocSize(tree)==owned);printf("stage=%u owned=%zu batches=%"PRIu64"\n",stage,owned,batches);fflush(stdout);
}
static void insert(zbtreeSet *tree,unsigned id){
 sds temporary=sdsnewlen(keys[id],sdslen(keys[id]));zbtreeInsertPosition pos;double old;
 CHECK(!zbtreeFindForAdd(tree,temporary,&old,&pos));zbtreeInsertNew(tree,values[id],temporary,&pos);live[id]=1;
 memset(temporary,0xa5,sdslen(temporary));sdsfree(temporary);
}
int main(int argc,char **argv){
 CHECK(argc==2);uint64_t seed=strtoull(argv[1],NULL,10),rng=seed;CHECK(seed);uint8_t hs[16];for(unsigned j=0;j<16;j++)hs[j]=(uint8_t)random64(&rng);dictSetHashFunctionSeed(hs);
 double special[16]={-0.0,0.0,-DBL_MAX,DBL_MAX,-DBL_MIN,DBL_MIN,-DBL_TRUE_MIN,DBL_TRUE_MIN,nextafter(1.0,0.0),1.0,nextafter(1.0,2.0),-1.0,0.5,-0.5,42.0,-42.0};
 keys[0]=sdsnewlen("",0);values[0]=-0.0;
 for(unsigned group=0;group<GROUPS;group++)for(unsigned k=0;k<WIDTHS;k++){
  unsigned id=1+group*WIDTHS+k;unsigned char buf[4096];memset(buf,0,sizeof(buf));buf[0]=(unsigned char)(group*3);keys[id]=sdsnewlen(buf,lens[k]);values[id]=special[id%16];
 }
 unsigned order[N];for(unsigned i=0;i<N;i++)order[i]=i;
 for(unsigned i=N;i>1;i--){unsigned j=(unsigned)(random64(&rng)%i),t=order[i-1];order[i-1]=order[j];order[j]=t;}
 zbtreeSet *tree=zbtreeCreate();stage=0;verify(tree);grid(tree);
 for(unsigned i=0;i<N;i++)insert(tree,order[i]);stage=1;verify(tree);grid(tree);
 for(unsigned id=0;id<N;id++){
  if(id%5==0){CHECK(zbtreeDelete(tree,keys[id]));live[id]=0;}
  else if(id%7==0){zbtreeInsertPosition pos;double old;CHECK(zbtreeFindForAdd(tree,keys[id],&old,&pos));values[id]=special[(id+3)%16];zbtreeUpdateScore(tree,keys[id],values[id],&pos);}
 }
 stage=2;verify(tree);grid(tree);
 for(unsigned id=0;id<N;id++)if(!live[id]){values[id]=special[(id+5)%16];insert(tree,id);}
 stage=3;verify(tree);zbtreeSet *clone=zbtreeDup(tree);zbtreeFree(tree);tree=clone;verify(tree);grid(tree);
 CHECK(zbtreeDeleteRangeByRank(tree,0,ULONG_MAX)==N);memset(live,0,sizeof(live));stage=4;verify(tree);grid(tree);zbtreeFree(tree);
 for(unsigned id=0;id<N;id++)sdsfree(keys[id]);
 CHECK(heterogeneous>0&&aliases>0&&copies>0);printf("PASS seed=%"PRIu64" keys=%u models=%"PRIu64" batches=%"PRIu64" lanes=%"PRIu64" exact=%"PRIu64" aliases=%"PRIu64" copies=%"PRIu64" heterogeneous=%"PRIu64" digest=%016"PRIx64"\n",seed,N,models,batches,lanes,exact,aliases,copies,heterogeneous,digest);return 0;
}
