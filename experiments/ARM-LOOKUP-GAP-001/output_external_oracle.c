/* Correctness-only oracle. No timers, PMU work or performance output. */
#include "zset_btree.c"
int main(void) {
    unsigned long checks=0;
    for(unsigned seed=17;seed<=43;seed+=13) for(int wide=1;wide<2;wide++) for(int mode=0;mode<3;mode++) {
        uint8_t key[16]; for(int i=0;i<16;i++)key[i]=(seed+29*i)&255;dictSetHashFunctionSeed(key);
        zbtreeSet *t=zbtreeCreate();zbtreeReserve(t,500);
        for(int i=0;i<500;i++) {
            unsigned char b[384];memset(b,'a'+i%26,sizeof(b));
            int n=snprintf((char*)b,32,"m:%05d",i);if(wide){b[n]=0;b[383]=(unsigned char)i;n=384;}
            double score=mode==0?i:mode==1?i*0.125:(i%2?-0.0:0.0);
            zbtreeInsertNewRaw(t,score,b,n,NULL);
        }
        for(zbtScoreLeaf *leaf=t->score_first;leaf;leaf=leaf->next) {
            size_t lens[ZBT_SCORE_LEAF_MAX];unsigned char *keys[ZBT_SCORE_LEAF_MAX];double scores[ZBT_SCORE_LEAF_MAX];
            for(unsigned i=0;i<leaf->n.count;i++) {
                serverAssert(zbtScoreLeafRecord(leaf,i)[0]==ZBT_PACKED_EXTERNAL);
                const unsigned char *q=zbtScoreLeafElement(leaf,i,&lens[i]);keys[i]=malloc(lens[i]);serverAssert(keys[i]);memcpy(keys[i],q,lens[i]);scores[i]=zbtScoreLeafScore(leaf,i);
            }
            for(int reversed=0;reversed<2;reversed++) {
                if(reversed)zbtScoreLeafReverseForPop(leaf);
                for(unsigned i=0;i<leaf->n.count;i++) {
                    uint32_t hash=zbtreeMemberHash(keys[i],lens[i]);
                    for(unsigned mask=0;mask<4;mask++) {
                        double score=123456.0;unsigned pos=UINT_MAX;
                        serverAssert(zbtScoreLeafFindMember(leaf,hash,keys[i],lens[i],mask&1?&score:NULL,mask&2?&pos:NULL));
                        serverAssert((mask&1)?memcmp(&score,&scores[i],sizeof(score))==0:score==123456.0);
                        serverAssert((mask&2)?pos==i:pos==UINT_MAX);checks++;
                    }
                    keys[i][0]^=0x40;double score=987654.0;unsigned pos=UINT_MAX;
                    serverAssert(!zbtScoreLeafFindMember(leaf,zbtreeMemberHash(keys[i],lens[i]),keys[i],lens[i],&score,&pos));
                    serverAssert(score==987654.0 && pos==UINT_MAX);keys[i][0]^=0x40;checks++;
                }
            }
            for(unsigned i=0;i<leaf->n.count;i++)free(keys[i]);
        }
        zbtreeFree(t);
    }
    printf("{\"output_checks\":%lu,\"passed\":true}\n",checks);
    return 0;
}
