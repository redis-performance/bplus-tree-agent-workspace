#include "src/zset_btree.c"
int main(void) {
    zbtreeSet *zs=zbtreeCreate();sds key=sdsnewlen("abc",3);double score;
    zbtreeInsertPosition pos;serverAssert(!zbtreeFindForAdd(zs,key,&score,&pos));
    uint32_t hash=pos.hash;zbtreeInsertNew(zs,5,key,&pos);
    zbtScoreLeaf *leaf=zs->score_first;unsigned place=999;
    serverAssert(zbtScoreLeafFindMember(leaf,hash,(unsigned char*)key,3,&score,&place));
    serverAssert(geo.leaf_calls==0 && geo.queries==0 && !geo_active);
    zbt_geometry_begin(zs);
    serverAssert(geo.leaf_calls==0 && geo.queries==0 && geo.snapshot_leaves==1);
    serverAssert(zbtScoreLeafFindMember(leaf,hash,(unsigned char*)key,3,&score,&place));
    serverAssert(score==5 && place==0 && geo.leaf_calls==1 && geo.unique_leaves==1);
    serverAssert(geo.queries==0 && geo.index_candidates==0 && geo.matches==1 && geo.tag_candidates==1 && geo.full_compares==1);
    serverAssert(geo.width[0][0]==1 && geo.width[1][0]==1 && geo.width[2][0]==1);
    serverAssert(geo.score_samples[0]==0 && geo.score_samples[1]==0);
    zbt_geometry_end();geometry_counts before=geo;
    serverAssert(zbtreeScore(zs,key,&score));serverAssert(!memcmp(&geo,&before,sizeof(geo)));
    sds other=sdsnewlen("def",3);serverAssert(!zbtreeFindForAdd(zs,other,&score,&pos));zbtreeInsertNew(zs,7,other,&pos);
    leaf=zs->score_first;serverAssert(leaf->score_bits>0);
    zbt_geometry_begin(zs);serverAssert(zbtreeScore(zs,key,&score) && score==5);
    serverAssert(geo.queries==1 && geo.index_candidates==1 && geo.leaf_calls==1 && geo.matches==1);
    serverAssert(geo.score_samples[1]==1);
    zbt_geometry_end();before=geo;
    serverAssert(zbtScoreLeafFindMember(leaf,hash,(unsigned char*)key,3,&score,&place));
    serverAssert(!memcmp(&geo,&before,sizeof(geo)));
    zbtreeFree(zs);sdsfree(key);sdsfree(other);
    puts("PASS private-helper hit/score/position width0 and nonzero; inactive-before/after; reset-after-setup; public query scope; exact decoder unchanged");return 0;
}
