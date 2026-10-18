/* Structural coverage only. Tree implementation is included without modification. */
#include "../src/zset_btree.c"
#include "iterator_helpers.h"
static uint64_t read_bitwise(const unsigned char *p,size_t start,unsigned width) {
    uint64_t result=0;
    for(unsigned b=0;b<width;b++)result|=(uint64_t)((p[(start+b)/8]>>((start+b)%8))&1)<<b;
    return result;
}
static uint64_t ordered_bits(uint64_t value) {
    return value>>63 ? value^UINT64_C(0x8000000000000000) : ~value;
}
int main(int argc,char **argv) {
    serverAssert(argc==6);size_t n=number(argv[1]),bytes=number(argv[2]);uint64_t seed=number(argv[3]);
    const char *encoding=argv[4],*construction=argv[5];
    uint64_t rng=seed;uint8_t hs[16];for(size_t i=0;i<16;i++)hs[i]=(uint8_t)random64(&rng);dictSetHashFunctionSeed(hs);
    sds *keys=zmalloc(n*sizeof(*keys));size_t *order=zmalloc(n*sizeof(*order));char *buf=zmalloc(bytes);
    for(size_t i=0;i<n;i++) {memset(buf,'x',bytes);for(unsigned j=0;j<8;j++)buf[j]=(char)((uint64_t)i>>(8*(!strcmp(encoding,"alternating-zero") ? 7-j : j)));keys[i]=sdsnewlen(buf,bytes);order[i]=i;}
    if(!strcmp(construction,"shuffled"))for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}
    else if(!strcmp(construction,"descending"))for(size_t i=0;i<n;i++)order[i]=n-1-i;
    else serverAssert(!strcmp(construction,"ascending"));
    zbtreeSet *tree=zbtreeCreate();for(size_t i=0;i<n;i++){size_t k=order[i];insert(tree,keys[k],model_score(k,n,encoding));}
    size_t owned=zbtreeAllocSize(tree);uint64_t widths[65]={0},shifts[65]={0},reversed=0,record[3]={0},cross=0,total=0,leaves=0,small=0;
    zbtScoreLeaf *prev=NULL;
    for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next) {
        serverAssert(leaf->prev==prev && leaf->n.count>0 && leaf->n.count<=96);prev=leaf;leaves++;
        serverAssert(leaf->score_bits<=64 && leaf->n.score_shift<=64);
        widths[leaf->score_bits]+=leaf->n.count;shifts[leaf->n.score_shift]+=leaf->n.count;
        reversed+=leaf->reversed?leaf->n.count:0;
        if(leaf->score_bits && leaf->score_bits<=56)small+=leaf->n.count;
        for(unsigned logical=0;logical<leaf->n.count;logical++,total++) {
            unsigned physical=leaf->reversed?leaf->n.count-logical-1:logical;
            size_t bitpos=(size_t)physical*leaf->score_bits;
            uint64_t delta=read_bitwise(leaf->data,bitpos,leaf->score_bits);
            serverAssert(!delta || leaf->n.score_shift<64);
            delta=leaf->n.score_shift==64?0:delta<<leaf->n.score_shift;
            uint64_t ordered=leaf->reversed?leaf->score_base-delta:leaf->score_base+delta;
            serverAssert(ordered_bits(ordered)==score_bits(model_score(total,n,encoding)));
            serverAssert(score_bits(zbtScoreLeafScore(leaf,logical))==ordered_bits(ordered));
            cross+=leaf->score_bits>64-(bitpos&7);
            unsigned char *rec=zbtScoreLeafRecord(leaf,logical);
            unsigned kind=rec[0]<254?0:rec[0]==254?1:2;record[kind]++;
            serverAssert(kind==(bytes<254?0:bytes<320?1:2));
        }
    }
    serverAssert(total==n && prev==tree->score_last && record[0]+record[1]+record[2]==n);
    for(int reverse=0;reverse<2;reverse++)for(unsigned mask=0;mask<8;mask++)verify(tree,keys,n,reverse,mask,encoding);
    serverAssert(zbtreeAllocSize(tree)==owned);
    printf("{\"n\":%zu,\"bytes\":%zu,\"seed\":%"PRIu64",\"encoding\":\"%s\",\"construction\":\"%s\",\"owned\":%zu,\"leaves\":%"PRIu64",\"elements\":%"PRIu64",\"reversed\":%"PRIu64",\"cross_word\":%"PRIu64",\"narrow_nonzero\":%"PRIu64",\"records\":[%"PRIu64",%"PRIu64",%"PRIu64"],\"widths\":[",n,bytes,seed,encoding,construction,owned,leaves,total,reversed,cross,small,record[0],record[1],record[2]);
    for(unsigned i=0;i<65;i++)printf("%s%"PRIu64,i?",":"",widths[i]);printf("],\"shifts\":[");
    for(unsigned i=0;i<65;i++)printf("%s%"PRIu64,i?",":"",shifts[i]);puts("]}");
    zbtreeFree(tree);for(size_t i=0;i<n;i++)sdsfree(keys[i]);zfree(keys);zfree(order);zfree(buf);
}
