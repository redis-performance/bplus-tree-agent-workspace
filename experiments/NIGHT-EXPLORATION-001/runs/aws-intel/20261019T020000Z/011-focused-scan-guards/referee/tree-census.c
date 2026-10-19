/* DIAGNOSTIC ONLY. Include exact selected source in this separate binary.
 * The performance binary never links this file and keeps its original tree TU.
 */
#include "zset_btree.c"
#include <inttypes.h>
void scan_guard_census(zbtreeSet *t) {
  uint64_t leaves = 0, reversed = 0, members = 0, reverse_members = 0,
           external = 0, hist[256] = {0}, counts[97] = {0};
  for (zbtScoreLeaf *l = t->score_first; l; l = l->next) {
    leaves++;
    reversed += !!l->reversed;
    members += l->n.count;
    reverse_members += l->reversed ? l->n.count : 0;
    serverAssert(l->n.count <= 96);
    counts[l->n.count]++;
    for (unsigned i = 0; i < l->n.count; i++) {
      size_t len;
      const unsigned char *key = zbtScoreLeafElement(l, i, &len);
      uint8_t tag = (uint32_t)dictGenHashFunction(key, len) >> 24;
      serverAssert(zbtScoreLeafHashTags(l)[zbtScoreLeafPhysicalPos(l, i)] ==
                   tag);
      hist[tag]++;
      external += zbtScoreLeafRecord(l, i)[0] == ZBT_PACKED_EXTERNAL;
    }
  }
  serverAssert(members == zbtreeLength(t));
  printf("{\"kind\":\"census\",\"leaves\":%" PRIu64
         ",\"reversed_leaves\":%" PRIu64 ",\"members\":%" PRIu64
         ",\"reversed_members\":%" PRIu64 ",\"external_members\":%" PRIu64
         ",\"active_rehash\":%s,\"index_size\":%lu,\"wide_ids\":%d,\"tag_"
         "histogram\":[",
         leaves, reversed, members, reverse_members, external,
         t->member_rehash ? "true" : "false", t->member_index.size,
         t->member_index.wide_ids);
  for (int i = 0; i < 256; i++)
    printf("%s%" PRIu64, i ? "," : "", hist[i]);
  printf("],\"leaf_count_histogram\":[");
  for (int i = 0; i < 97; i++)
    printf("%s%" PRIu64, i ? "," : "", counts[i]);
  printf("]}\n");
}
