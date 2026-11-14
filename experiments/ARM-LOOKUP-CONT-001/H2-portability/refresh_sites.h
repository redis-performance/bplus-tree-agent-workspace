/* Direct calls prove the four cache-refresh sites, independently of packing
 * choices in the retained mutation schedule. This is not source instrumentation. */
static void refresh_leaf(zbtScoreLeaf *leaf, unsigned count, unsigned bits) {
    serverAssert(leaf->n.count==count && leaf->score_bits==bits);
    size_t bytes=zbtScoreLeafScoreBytes(count,bits);
#ifdef H2_B
    serverAssert(leaf->n.score_bytes==bytes);
#endif
    serverAssert((unsigned char *)zbtScoreLeafOffsets(leaf)==leaf->data+bytes);
    serverAssert((uintptr_t)zbtScoreLeafOffsets(leaf)%2==0);
    for (unsigned i=0;i<count;i++) {
        size_t len; const unsigned char *key=zbtScoreLeafElement(leaf,i,&len);
        serverAssert(len==1 && key[0]=='a'+i);
        serverAssert(zbtScoreLeafScore(leaf,i)==(i ? DBL_MAX : -DBL_MAX));
    }
}
static void refresh_sites(void) {
    zbtreeSet *zs=zbtreeCreate();
    double scores[33];
    zbtBuildElement elems[33]; uint8_t tags[33]; uint16_t locations[33]={0};
    unsigned char names[33];
    for (unsigned i=0;i<33;i++) {
        names[i]=(unsigned char)('a'+i);
        scores[i]=i ? DBL_MAX : -DBL_MAX;
        uint32_t hash=zbtreeMemberHash(names+i,1);
        tags[i]=(uint8_t)(hash>>24);
        zbtBuildElementFromBytes(elems+i,names+i,1,hash);
    }
    zbtScoreLeaf *leaf=zbtScoreLeafBuild(zs,1,scores,elems,tags,ZBT_NEW_LEAF_ID,1);
    refresh_leaf(leaf,1,0);
    size_t built=zbtScoreLeafScoreBytes(1,leaf->score_bits);
    locations[0]=zbtScoreLeafOffset(leaf,0);
    serverAssert(zbtScoreInsertInPlace(zs,leaf,2,scores,elems,tags,locations,1));
    refresh_leaf(leaf,2,64);
    size_t reencoded=zbtScoreLeafScoreBytes(2,leaf->score_bits);
    serverAssert(reencoded!=built);
    for (unsigned i=2;i<33;i++) {
        size_t previous=zbtScoreLeafScoreBytes(i,leaf->score_bits);
        serverAssert(zbtScoreInsertFast(zs,leaf,DBL_MAX,elems+i,tags[i],i));
        refresh_leaf(leaf,i+1,64);
        serverAssert(zbtScoreLeafScoreBytes(i+1,leaf->score_bits)!=previous);
    }
    /* 33 full-width scores need272 bytes, then32 need264: both cached bytes
     * are nonzero and deletion must change the rounded offset displacement. */
    serverAssert(zbtScoreLeafScoreBytes(33,leaf->score_bits)==272);
    zbtScoreDeleteInPlace(zs,leaf,32,1);
    refresh_leaf(leaf,32,64);
    serverAssert(zbtScoreLeafScoreBytes(32,leaf->score_bits)==264);
    zbtScoreReleaseLeafId(zs,leaf->id);
    zbtScoreLeafFreeOwned(zs,leaf);
    zbtreeFree(zs);
}
