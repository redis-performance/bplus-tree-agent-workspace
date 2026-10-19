#define main legacy_main
#include "microbench.c"
#undef main
#include <limits.h>
static unsigned long checks;
static uint64_t bits(double d){uint64_t u;memcpy(&u,&d,8);return u;}
static int lexical(sds a,sds b){size_t an=sdslen(a),bn=sdslen(b),n=an<bn?an:bn;int c=memcmp(a,b,n);return c?c:(an>bn)-(an<bn);}
static void step(zbtreeIterator *it,sds *keys,double *scores,int n,int rank,int reverse,unsigned mask){
 static const unsigned char sentinel=23;
 const unsigned char *ele=&sentinel;size_t len=SIZE_MAX;double score=-12345.5;
 int ok=zbtreeIteratorNext(it,reverse,mask&1?&ele:NULL,mask&2?&len:NULL,mask&4?&score:NULL);
 serverAssert(ok==(rank>=0&&rank<n));
 if(ok){
  if(mask&1)serverAssert(!memcmp(ele,keys[rank],sdslen(keys[rank])));else serverAssert(ele==&sentinel);
  if(mask&2)serverAssert(len==sdslen(keys[rank]));else serverAssert(len==SIZE_MAX);
  if(mask&4)serverAssert(bits(score)==bits(scores[rank]));else serverAssert(score==-12345.5);
 }else serverAssert(ele==&sentinel&&len==SIZE_MAX&&score==-12345.5);
 checks++;
}
static sds keymake(unsigned id,size_t n){char *b=zmalloc(n);memset(b,'x',n);for(unsigned j=0;j<8;j++)b[7-j]=(char)((uint64_t)id>>(8*j));sds k=sdsnewlen(b,n);zfree(b);return k;}
int main(void){
 const int n=257;uint8_t hashseed[16]={0};dictSetHashFunctionSeed(hashseed);
 for(int pattern=0;pattern<3;pattern++)for(size_t bytes=16;bytes<=321;bytes+=305){
  sds keys[n];double scores[n];size_t order[n];uint64_t rng=37;
  for(int i=0;i<n;i++){keys[i]=keymake((unsigned)i,bytes);scores[i]=pattern==0?(double)(i-128):pattern==1?1.0:(i&1?-0.0:+0.0);order[i]=(size_t)i;}
  for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
  zbtreeSet *tree=zbtreeCreate();for(int i=0;i<n;i++)insert(tree,keys[order[i]],scores[order[i]]);
  for(int reverse=0;reverse<2;reverse++){
   zbtreeIterator it;memset(&it,0xa5,sizeof(it));serverAssert(zbtreeIteratorStart(tree,reverse,&it));
   int rank=reverse?n-1:0;
   for(int i=0;i<n+2;i++){if(i==n/2){zbtreeIterator copy=it;step(&copy,keys,scores,n,rank,reverse,7);}step(&it,keys,scores,n,rank,reverse,(unsigned)i%8);rank+=reverse?-1:1;}
   for(int start=0;start<=n;start++){
    memset(&it,0xa5,sizeof(it));serverAssert(zbtreeIteratorSeekRank(tree,(unsigned long)start,&it)==(start<n));rank=start;
    for(unsigned mask=0;mask<8;mask++){step(&it,keys,scores,n,rank,reverse,mask);if(rank>=0&&rank<n)rank+=reverse?-1:1;}
   }
   const double bounds[]={-1000,-128,-1,-0.0,+0.0,1,128,1000};
   for(size_t b=0;b<sizeof(bounds)/sizeof(*bounds);b++)for(int exclusive=0;exclusive<2;exclusive++){
    int want=-1;
    for(int i=reverse?n-1:0;i>=0&&i<n;i+=reverse?-1:1){int match=reverse?(exclusive?scores[i]<bounds[b]:scores[i]<=bounds[b]):(exclusive?scores[i]>bounds[b]:scores[i]>=bounds[b]);if(match){want=i;break;}}
    unsigned long actual=ULONG_MAX;memset(&it,0xa5,sizeof(it));int ok=zbtreeIteratorSeekScore(tree,bounds[b],exclusive,reverse,&it,&actual);serverAssert(ok==(want>=0));if(ok)serverAssert(actual==(unsigned long)want);
    step(&it,keys,scores,n,want,reverse,7);
   }
   if(pattern!=0){
   sds extra=keymake(n+1,bytes),empty=sdsnewlen("",0);sds boundskey[]={empty,keys[0],keys[128],keys[256],extra};
   for(size_t b=0;b<sizeof(boundskey)/sizeof(*boundskey);b++)for(int exclusive=0;exclusive<2;exclusive++){
    int want=-1;for(int i=reverse?n-1:0;i>=0&&i<n;i+=reverse?-1:1){int c=lexical(keys[i],boundskey[b]);int match=reverse?(exclusive?c<0:c<=0):(exclusive?c>0:c>=0);if(match){want=i;break;}}
    unsigned long actual=ULONG_MAX;memset(&it,0xa5,sizeof(it));int ok=zbtreeIteratorSeekLex(tree,boundskey[b],exclusive,reverse,&it,&actual);serverAssert(ok==(want>=0));if(ok)serverAssert(actual==(unsigned long)want);step(&it,keys,scores,n,want,reverse,7);
   }
   sdsfree(extra);sdsfree(empty);
   }
   for(int sentinel=0;sentinel<2;sentinel++){
    unsigned long actual=ULONG_MAX;int want=(reverse!=sentinel)?-1:(reverse?n-1:0);
    memset(&it,0xa5,sizeof(it));int ok=zbtreeIteratorSeekLex(tree,sentinel?shared.maxstring:shared.minstring,0,reverse,&it,&actual);
    serverAssert(ok==(want>=0));if(ok)serverAssert(actual==(unsigned long)want);step(&it,keys,scores,n,want,reverse,7);
   }
  }
  /* Additive compatibility: direction toggles operate on the current position. */
  for(int start=0;start<n;start++){
   zbtreeIterator it;memset(&it,0xa5,sizeof(it));serverAssert(zbtreeIteratorSeekRank(tree,(unsigned long)start,&it));
   int rank=start;
   for(int i=0;i<32&&rank>=0&&rank<n;i++){
    int reverse=(i/3)%2;step(&it,keys,scores,n,rank,reverse,(unsigned)i%8);rank+=reverse?-1:1;
   }
  }
  /* Mutation invalidates old state. Never inspect or use it until reinitialized. */
  for(int reverse=0;reverse<2;reverse++)for(int entry=0;entry<4;entry++){
   zbtreeIterator it;memset(&it,0xa5,sizeof(it));serverAssert(zbtreeIteratorStart(tree,reverse,&it));
   step(&it,keys,scores,n,reverse?n-1:0,reverse,7);
   serverAssert(zbtreeDelete(tree,keys[128]));insert(tree,keys[128],scores[128]);
   int rank=reverse?n-1:0;unsigned long actual=ULONG_MAX;
   if(entry==0)serverAssert(zbtreeIteratorStart(tree,reverse,&it));
   if(entry==1)serverAssert(zbtreeIteratorSeekRank(tree,(unsigned long)rank,&it));
   if(entry==2){serverAssert(zbtreeIteratorSeekScore(tree,scores[rank],0,reverse,&it,&actual));serverAssert(actual==(unsigned long)rank);}
   if(entry==3){serverAssert(zbtreeIteratorSeekLex(tree,reverse?shared.maxstring:shared.minstring,0,reverse,&it,&actual));serverAssert(actual==(unsigned long)rank);}
   for(int i=0;i<n+1;i++){step(&it,keys,scores,n,rank,reverse,(unsigned)i%8);rank+=reverse?-1:1;}
  }
  zbtreeFree(tree);for(int i=0;i<n;i++)sdsfree(keys[i]);
 }
 zbtreeSet *empty=zbtreeCreate();zbtreeIterator it;sds bound=sdsnewlen("",0);
 for(int reverse=0;reverse<2;reverse++){
  memset(&it,0xa5,sizeof(it));serverAssert(!zbtreeIteratorStart(empty,reverse,&it));step(&it,NULL,NULL,0,-1,reverse,7);
  memset(&it,0xa5,sizeof(it));serverAssert(!zbtreeIteratorSeekRank(empty,0,&it));step(&it,NULL,NULL,0,-1,reverse,7);
  memset(&it,0xa5,sizeof(it));serverAssert(!zbtreeIteratorSeekScore(empty,0,0,reverse,&it,NULL));step(&it,NULL,NULL,0,-1,reverse,7);
  memset(&it,0xa5,sizeof(it));serverAssert(!zbtreeIteratorSeekLex(empty,bound,0,reverse,&it,NULL));step(&it,NULL,NULL,0,-1,reverse,7);
 }
 sdsfree(bound);zbtreeFree(empty);printf("PASS %lu iterator state checks sizeof=%zu\n",checks,sizeof(zbtreeIterator));return 0;
}
