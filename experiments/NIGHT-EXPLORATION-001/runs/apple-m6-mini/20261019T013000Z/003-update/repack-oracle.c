/* Source-included bounded oracle; never link a second tree source copy. */
#include "src/zset_btree.c"
#include <inttypes.h>
static uint64_t exact(double d){uint64_t x;memcpy(&x,&d,8);return x;}
int main(void){const size_t lengths[]={8,16,319,320,321,1024};size_t success=0,failed=0,reversed=0;
for(size_t m=0;m<6;m++)for(int direction=0;direction<2;direction++){
 zbtreeSet *t=zbtreeCreate();sds keys[256];double expected[256];
 for(size_t i=0;i<256;i++){unsigned char key[1024];memset(key,0xa5,lengths[m]);memcpy(key,&i,8);keys[i]=sdsnewlen(key,lengths[m]);expected[i]=4*i+1;}
 for(size_t i=0;i<256;i++){size_t id=direction?255-i:i;zbtreeInsertPosition p;double old;serverAssert(!zbtreeFindForAdd(t,keys[id],&old,&p));zbtreeInsertNew(t,expected[id],keys[id],&p);}
 for(zbtScoreLeaf *leaf=t->score_first;leaf;leaf=leaf->next){if(leaf->n.count<3)continue;unsigned pos=leaf->n.count/2;size_t id;size_t len;const unsigned char *member=zbtScoreLeafElement(leaf,pos,&len);memcpy(&id,member,8);serverAssert(id<256);double value=expected[id]+1;
#ifdef CANDIDATE
  uint16_t offsets[ZBT_SCORE_LEAF_MAX];uint8_t tags[ZBT_SCORE_LEAF_MAX];for(unsigned i=0;i<leaf->n.count;i++){offsets[i]=zbtScoreLeafOffset(leaf,i);tags[i]=zbtScoreLeafTag(leaf,i);}uint32_t stable_id=leaf->id;uint16_t start=leaf->record_start;size_t owned=zbtreeAllocSize(t);unsigned count=leaf->n.count;
  if(zbtScoreUpdateReencode(leaf,pos,value)){success++;reversed+=leaf->reversed;expected[id]=value;serverAssert(stable_id==leaf->id&&start==leaf->record_start&&count==leaf->n.count&&owned==zbtreeAllocSize(t));for(unsigned i=0;i<count;i++){serverAssert(offsets[i]==zbtScoreLeafOffset(leaf,i)&&tags[i]==zbtScoreLeafTag(leaf,i));}if(pos+1==count)zbtScoreUpdatePath(&leaf->n,0);}else failed++;
  /* Inadequate metadata headroom must fail before writing any byte. */
  leaf->record_start=0;size_t bytes=zmalloc_usable_size(leaf);unsigned char *snapshot=zmalloc(bytes);memcpy(snapshot,leaf,bytes);serverAssert(!zbtScoreUpdateReencode(leaf,pos,value+1));serverAssert(!memcmp(snapshot,leaf,bytes));zfree(snapshot);leaf->record_start=start;
#else
  if(zbtScoreUpdateInPlace(leaf,pos,value,(unsigned char *)keys[id],sdslen(keys[id]))) expected[id]=value;
#endif
 }
 zbtreeIterator it;serverAssert(zbtreeIteratorStart(t,0,&it));for(size_t i=0;i<256;i++){const unsigned char *member;size_t len;double score;serverAssert(zbtreeIteratorNext(&it,0,&member,&len,&score)&&len==lengths[m]&&!memcmp(member,keys[i],len)&&exact(score)==exact(expected[i]));serverAssert(zbtreeRank(t,keys[i],0,NULL)==(long)i);serverAssert(zbtreeScore(t,keys[i],&score)&&exact(score)==exact(expected[i]));}serverAssert(!zbtreeIteratorNext(&it,0,NULL,NULL,NULL));zbtreeSet *dup=zbtreeDup(t);for(size_t i=0;i<256;i++){double score;serverAssert(zbtreeScore(dup,keys[i],&score)&&exact(score)==exact(expected[i]));}zbtreeFree(dup);zbtreeFree(t);for(size_t i=0;i<256;i++)sdsfree(keys[i]);
}
#ifdef CANDIDATE
serverAssert(success>0&&reversed>0);
#endif
printf("PASS success=%zu fallback=%zu reversed_success=%zu; metadata/headroom/records/ownership/order/exact bits\n",success,failed,reversed);
}
