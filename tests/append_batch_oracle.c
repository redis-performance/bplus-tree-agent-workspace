/* Public append mutations with read-only flush/rehash observations. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#define TOTAL 8193
static sds keys[TOTAL];
static double scores[TOTAL];
static unsigned case_no,stage,hash_seed;
static unsigned long checks,count_flushes,byte_flushes,active_adds;
static unsigned char seen[TOTAL];
#define CHECK(x) do{if(!(x)){fprintf(stderr,"case=%u stage=%u seed=%u line=%d: %s\n",case_no,stage,hash_seed,__LINE__,#x);abort();}}while(0)
static uint64_t bits(double x){uint64_t u;memcpy(&u,&x,8);return u;}
static unsigned identify(const unsigned char *key,size_t len,double score,unsigned n){
 CHECK(len>=4);unsigned id=0;for(unsigned j=0;j<4;j++)id=(id<<8)|key[j];
 CHECK(id<n && len==sdslen(keys[id]) && !memcmp(key,keys[id],len));CHECK(bits(score)==bits(scores[id]));return id;
}
static void visit(void *ctx,const unsigned char *key,size_t len,double score){unsigned n=*(unsigned*)ctx;seen[identify(key,len,score,n)]=1;}
static void verify(zbtreeSet *tree,unsigned n){
 CHECK(zbtreeLength(tree)==n);
 for(unsigned i=0;i<n;i++){
  double score;CHECK(zbtreeScore(tree,keys[i],&score));CHECK(bits(score)==bits(scores[i]));
  CHECK(zbtreeScoreRaw(tree,(unsigned char*)keys[i],sdslen(keys[i]),&score));CHECK(bits(score)==bits(scores[i]));
  CHECK(zbtreeRank(tree,keys[i],0,&score)==(long)i);CHECK(bits(score)==bits(scores[i]));
 }
 for(int reverse=0;reverse<2;reverse++){
  zbtreeIterator it;CHECK(zbtreeIteratorStart(tree,reverse,&it)==(n!=0));
  for(unsigned i=0;i<n;i++){const unsigned char *key;size_t len;double score;CHECK(zbtreeIteratorNext(&it,reverse,&key,&len,&score));CHECK(identify(key,len,score,n)==(reverse?n-i-1:i));}
  CHECK(!zbtreeIteratorNext(&it,reverse,NULL,NULL,NULL));
 }
 memset(seen,0,sizeof(seen));uint64_t cursor=0;unsigned steps=0;
 do{cursor=zbtreeScan(tree,cursor,7,visit,&n);CHECK(++steps<100000);}while(cursor);
 for(unsigned i=0;i<n;i++)CHECK(seen[i]);checks++;
}
static void exercise(unsigned prefix,int mode){
 case_no++;stage=0;uint8_t seed[16]={0};seed[0]=hash_seed;dictSetHashFunctionSeed(seed);
 for(unsigned i=0;i<TOTAL;i++){
  const size_t mixed[]={8,319,320,321,1024};size_t len=mode==0?8:mode==1?319:mixed[i%5];
  unsigned char buf[1024];memset(buf,(i%2)?0xff:0,len);for(unsigned j=0;j<4;j++)buf[j]=(i>>(24-8*j))&255;
  keys[i]=sdsnewlen(buf,len);scores[i]=i%2?-0.0:0.0;
 }
 zbtreeSet *tree=zbtreeCreate();
 for(unsigned i=0;i<prefix;i++)zbtreeInsertNewAppend(tree,scores[i],(unsigned char*)keys[i],sdslen(keys[i]));
 /* Observe natural resize before lookups can advance it. */
 int initial_active=tree->member_rehash!=NULL;
 if(prefix==7169)CHECK(initial_active);
 unsigned done=prefix;unsigned groups[]={0,1,95,96,97,193,TOTAL};
 for(unsigned g=0;g<7;g++){
  unsigned take=groups[g]<(TOTAL-done)?groups[g]:TOTAL-done;size_t oldbytes=zbtreeAllocSize(tree);
  zbtreeAppendBatch *batch=zbtreeAppendBatchCreate(tree);unsigned char temp[1024];
  for(unsigned j=0;j<take;j++){
   unsigned id=done+j;size_t len=sdslen(keys[id]);memcpy(temp,keys[id],len);
   unsigned before=batch->count;int active=tree->member_rehash!=NULL;if(active)active_adds++;
   if(id%2)zbtreeAppendBatchAddWithHash(batch,scores[id],temp,len,(uint32_t)dictGenHashFunction(temp,len));
   else zbtreeAppendBatchAdd(batch,scores[id],temp,len);
   if(before && batch->count==1){if(before==ZBT_SCORE_LEAF_MAX)count_flushes++;else byte_flushes++;}
   memset(temp,0xa5,sizeof(temp)); /* Both inline/external paths must own a copy. */
  }
  zbtreeAppendBatchFinish(batch);done+=take;stage++;
  if(!take)CHECK(zbtreeAllocSize(tree)==oldbytes);
  verify(tree,done);
 }
 CHECK(done==TOTAL);stage++;zbtreeSet *copy=zbtreeDup(tree);zbtreeFree(tree);tree=copy;verify(tree,TOTAL);
 CHECK(zbtreeDeleteRangeByRank(tree,0,ULONG_MAX)==TOTAL);stage++;verify(tree,0);zbtreeFree(tree);
 for(unsigned i=0;i<TOTAL;i++)sdsfree(keys[i]);
 printf("case=%u seed=%u prefix=%u mode=%d initial_active=%d PASS checks=%lu count_flushes=%lu byte_flushes=%lu active_adds=%lu\n",case_no,hash_seed,prefix,mode,initial_active,checks,count_flushes,byte_flushes,active_adds);fflush(stdout);
}
int main(void){
 unsigned seeds[]={17,101},prefixes[]={0,95,7169};
 for(unsigned s=0;s<2;s++){hash_seed=seeds[s];for(unsigned p=0;p<3;p++)for(int mode=0;mode<3;mode++)exercise(prefixes[p],mode);}
 CHECK(count_flushes>0 && byte_flushes>0 && active_adds>0);
 printf("PASS cases=%u checks=%lu count_flushes=%lu byte_flushes=%lu active_adds=%lu\n",case_no,checks,count_flushes,byte_flushes,active_adds);
}
