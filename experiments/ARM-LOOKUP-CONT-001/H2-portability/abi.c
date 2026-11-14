/* Correctness-only guest ABI proof. No timers or work loops. */
#include "zset_btree.c"
#include <float.h>
int main(void) {
    const uint32_t word=0x01020304;
    const unsigned char *p=(const unsigned char *)&word;
    const char *endian=p[0]==1 ? "big" : p[0]==4 ? "little" : "unknown";
    printf("{\"pointer\":%zu,\"size_t\":%zu,\"ulong\":%zu,\"u64\":%zu,\"double\":%zu,"
           "\"char_bit\":%d,\"radix\":%d,\"mantissa\":%d,\"max_exp\":%d,\"endian\":\"%s\","
           "\"compiler_endian\":%d,\"compiler_little\":%d,\"compiler_big\":%d,"
           "\"node\":%zu,\"leaf_data\":%zu,\"align_u64\":%zu,\"align_leaf\":%zu,"
           "\"moved_offset\":%zu,\"moved_size\":%zu,\"resize_offset\":%zu,\"resize_size\":%zu,"
           "\"cache_offset\":%d,\"cache_size\":%d,\"flags_offset\":%d,\"variant\":\"%s\"}\n",
           sizeof(void *),sizeof(size_t),sizeof(unsigned long),sizeof(uint64_t),sizeof(double),
           CHAR_BIT,FLT_RADIX,DBL_MANT_DIG,DBL_MAX_EXP,endian,
           __BYTE_ORDER__,__ORDER_LITTLE_ENDIAN__,__ORDER_BIG_ENDIAN__,
           sizeof(zbtScoreNode),offsetof(zbtScoreLeaf,data),_Alignof(uint64_t),_Alignof(zbtScoreLeaf),
           offsetof(zbtScoreNode,moved_out),sizeof(((zbtScoreNode *)0)->moved_out),
           offsetof(zbtScoreNode,index_resize),sizeof(((zbtScoreNode *)0)->index_resize),
#ifdef H2_B
           (int)offsetof(zbtScoreNode,score_bytes),(int)sizeof(((zbtScoreNode *)0)->score_bytes),
           (int)offsetof(zbtScoreNode,flags),"B"
#else
           -1,0,-1,"base"
#endif
    );
    return 0;
}
