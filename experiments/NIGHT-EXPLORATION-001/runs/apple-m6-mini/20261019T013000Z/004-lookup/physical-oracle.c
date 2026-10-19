/* Source included; link no second tree source. Independent expected score bits. */
#include "src/zset_btree.c"
#include <float.h>
#include <inttypes.h>
static uint64_t exact(double d){uint64_t u;memcpy(&u,&d,8);return u;}
static uint64_t rng=1234567;
static uint64_t random_word(void){rng^=rng<<13;rng^=rng>>7;rng^=rng<<17;return rng;}
int main(void){size_t checks=0,cells=0;
for(unsigned count=1;count<=96;count+= count<8?1:11)
for(unsigned width=0;width<=64;width++)for(unsigned reversed=0;reversed<2;reversed++)
for(unsigned sh=0;sh<2;sh++){
 unsigned shift=sh && width<61?3:0;
 zbtScoreLeaf *leaf=zcalloc(4096);leaf->n.isleaf=1;leaf->n.count=count;leaf->reversed=reversed;leaf->score_bits=width;leaf->n.score_shift=shift;
 uint64_t lo=zbtScoreToOrdered(-DBL_MAX),hi=zbtScoreToOrdered(DBL_MAX);
 leaf->score_base=width? (reversed?hi:lo) : zbtScoreToOrdered(sh?-0.0:0.0);
 uint16_t *offsets=zbtScoreLeafOffsets(leaf);uint8_t *tags=zbtScoreLeafHashTags(leaf);uint64_t expected[96];
 for(unsigned physical=0;physical<count;physical++){
  uint64_t mask=width==64?UINT64_MAX:width? (UINT64_C(1)<<width)-1:0;
  uint64_t delta=random_word()&mask;uint64_t limit=(hi-lo)>>shift;if(delta>limit)delta=limit;
  uint64_t distance=delta<<shift;uint64_t ordered=reversed?leaf->score_base-distance:leaf->score_base+distance;
  expected[physical]=ordered>>63?ordered&UINT64_C(0x7fffffffffffffff):~ordered;
  zbtWriteBits(leaf->data,(size_t)physical*width,width,delta);
  offsets[physical]=4096-(physical+1)*9;unsigned char *rec=(unsigned char*)leaf+offsets[physical];rec[0]=8;uint64_t id=physical;memcpy(rec+1,&id,8);tags[physical]=0xab;
 }
 for(unsigned physical=0;physical<count;physical++)for(unsigned outputs=0;outputs<4;outputs++){
  uint64_t key=physical;double score=123;unsigned pos=999;
  serverAssert(zbtScoreLeafFindMember(leaf,0xab000000,(unsigned char*)&key,8,outputs&1?&score:NULL,outputs&2?&pos:NULL));
  if(outputs&1)serverAssert(exact(score)==expected[physical]);
  if(outputs&2)serverAssert(pos==(reversed?count-physical-1:physical));
  checks++;
 }
 uint64_t missing=999;serverAssert(!zbtScoreLeafFindMember(leaf,0xab000000,(unsigned char*)&missing,8,NULL,NULL));
 zfree(leaf);cells++;
}
printf("PASS cells=%zu exact-score/position/output checks=%zu; widths0..64 shifts0/3 reversed both signed-zero ties colliding-tags first-match misses\n",cells,checks);return 0;}
