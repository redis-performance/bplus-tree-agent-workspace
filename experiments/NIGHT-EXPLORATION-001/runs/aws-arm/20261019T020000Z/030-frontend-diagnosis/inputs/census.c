/* Separate, untimed observation TU. Never linked into a timing/profile binary. */
#include "../src/zset_btree.c"
#include <inttypes.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void diagnostic_census(zbtreeSet *tree, size_t expected_n, int centered) {
    uint64_t joint[65][65][2] = {{{0}}}, occupants[ZBT_SCORE_LEAF_MAX+1] = {0};
    uint64_t widths[65] = {0}, shifts[65] = {0};
    uint64_t leaves=0, members=0, reversed_leaves=0, reversed_members=0;
    uint64_t zero=0, width64=0, aligned=0, unaligned=0, ninth=0, digest=UINT64_C(14695981039346656037);
    size_t owned=zbtreeAllocSize(tree); zbtScoreLeaf *previous=NULL;
    for(zbtScoreLeaf *leaf=tree->score_first;leaf;leaf=leaf->next) {
        serverAssert(leaf->prev==previous && leaf->n.isleaf && leaf->n.count>0 && leaf->n.count<=ZBT_SCORE_LEAF_MAX);
        unsigned bits=leaf->score_bits, shift=leaf->n.score_shift, rev=!!leaf->reversed;
        serverAssert(bits<=64 && shift<=64);
        leaves++;occupants[leaf->n.count]++;joint[bits][shift][rev]++;
        reversed_leaves+=rev;reversed_members+=(uint64_t)rev*leaf->n.count;
        for(unsigned pos=0;pos<leaf->n.count;pos++) {
            uint64_t id=0;size_t len;const unsigned char *key=zbtScoreLeafElement(leaf,pos,&len);
            serverAssert(len==16);for(unsigned j=0;j<8;j++)id|=(uint64_t)key[j]<<(8*j);
            serverAssert(id==members);for(unsigned j=8;j<16;j++)serverAssert(key[j]=='x');
            double model=(double)members-(centered?(double)(expected_n/2):0.0),actual=zbtScoreLeafScore(leaf,pos);
            uint64_t expected_bits,actual_bits;memcpy(&expected_bits,&model,8);memcpy(&actual_bits,&actual,8);
            serverAssert(actual_bits==expected_bits);digest=(digest^actual_bits)*UINT64_C(1099511628211);
            widths[bits]++;shifts[shift]++;
            unsigned bitshift=((size_t)zbtScoreLeafPhysicalPos(leaf,pos)*bits)&7;
            if(!bits)zero++;else {width64+=bits==64;aligned+=bitshift==0;unaligned+=bitshift!=0;ninth+=bitshift && bits>64-bitshift;}
            members++;
        }
        previous=leaf;
    }
    serverAssert(previous==tree->score_last && members==expected_n && members==zbtreeLength(tree) && owned==zbtreeAllocSize(tree));
    fprintf(stderr,"CENSUS {\"members\":%"PRIu64",\"leaves\":%"PRIu64",\"tree_bytes\":%zu,\"reversed_leaves\":%"PRIu64",\"reversed_members\":%"PRIu64",\"width0_entries\":%"PRIu64",\"width64_entries\":%"PRIu64",\"aligned_nonzero_entries\":%"PRIu64",\"unaligned_nonzero_entries\":%"PRIu64",\"ninth_byte_entries\":%"PRIu64",\"transitions_per_traversal\":%"PRIu64",\"score_digest\":%"PRIu64",\"width_entry_hist\":[",members,leaves,owned,reversed_leaves,reversed_members,zero,width64,aligned,unaligned,ninth,leaves?leaves-1:0,digest);
    for(unsigned i=0;i<=64;i++)fprintf(stderr,"%s%"PRIu64,i?",":"",widths[i]);
    fputs("],\"shift_entry_hist\":[",stderr);for(unsigned i=0;i<=64;i++)fprintf(stderr,"%s%"PRIu64,i?",":"",shifts[i]);
    fputs("],\"occupancy_leaf_hist\":[",stderr);for(unsigned i=0;i<=ZBT_SCORE_LEAF_MAX;i++)fprintf(stderr,"%s%"PRIu64,i?",":"",occupants[i]);
    fputs("],\"joint_leaf_hist\":[",stderr);int comma=0;
    for(unsigned bits=0;bits<=64;bits++)for(unsigned shift=0;shift<=64;shift++)for(unsigned rev=0;rev<2;rev++)if(joint[bits][shift][rev]) {fprintf(stderr,"%s[%u,%u,%u,%"PRIu64"]",comma?",":"",bits,shift,rev,joint[bits][shift][rev]);comma=1;}
    fputs("]}\n",stderr);
}
