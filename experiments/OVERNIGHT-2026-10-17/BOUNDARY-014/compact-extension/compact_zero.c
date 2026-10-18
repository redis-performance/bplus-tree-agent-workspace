/* Additive complete small-count matrix over the unchanged independent oracle. */
#define main original_zero_oracle_main
#include "zero_physical_oracle.c"
#undef main
int main(void) {
    unsigned seeds[]={31121,31123};size_t lengths[]={16,253,254,319,320};
    for(unsigned s=0;s<2;s++)for(unsigned n=0;n<=96;n++)for(unsigned l=0;l<5;l++)
        for(int d=0;d<2;d++)exercise(n,lengths[l],d,seeds[s]);
    serverAssert(forward_leaves && reversed_leaves && reversal_opportunities);
    serverAssert(checks==UINT64_C(289060) && exact==UINT64_C(86570560));
    printf("PASS checks=%"PRIu64" exact=%"PRIu64" forward_leaves=%"PRIu64" reversed_leaves=%"PRIu64" reversal_opportunities=%"PRIu64"\n",checks,exact,forward_leaves,reversed_leaves,reversal_opportunities);
}
