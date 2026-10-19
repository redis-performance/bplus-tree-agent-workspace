/* Read-only diagnostic TU, NEVER linked into timing binary. */
#include "census.h"
#include "zset_btree.c"
#include <inttypes.h>
census supplement_census(zbtreeSet *t) {
  census c = {0};
  c.rehash = t->member_rehash != NULL;
  c.old_used = t->member_index.used;
  c.old_size = t->member_index.size;
  c.wide_old = t->member_index.wide_ids;
  if (c.rehash) {
    c.new_used = t->member_rehash->table.used;
    c.new_size = t->member_rehash->table.size;
    c.wide_new = t->member_rehash->table.wide_ids;
  }
  for (zbtScoreLeaf *l = t->score_first; l; l = l->next) {
    c.leaves++;
    c.members += l->n.count;
    c.full16_chunks += l->n.count / 16;
    c.full8_chunks += l->n.count / 8;
    c.full16_members += (l->n.count / 16) * 16;
    c.reversed_full16_chunks += l->reversed ? l->n.count / 16 : 0;
    c.reversed_leaves += !!l->reversed;
    c.reversed_members += l->reversed ? l->n.count : 0;
    int migrated = c.rehash && zbtIndexLeafMigrated(t, l);
    if (migrated) {
      c.new_live += l->n.count;
      c.new_leaves++;
    } else {
      c.old_live += l->n.count;
      c.old_leaves++;
    }
    for (unsigned i = 0; i < l->n.count; i++) {
      size_t len;
      const unsigned char *s = zbtScoreLeafElement(l, i, &len);
      uint8_t tag = (uint32_t)dictGenHashFunction(s, len) >> 24;
      serverAssert(zbtScoreLeafHashTags(l)[zbtScoreLeafPhysicalPos(l, i)] ==
                   tag);
      c.tags[tag]++;
      unsigned char kind = zbtScoreLeafRecord(l, i)[0];
      c.external += kind == ZBT_PACKED_EXTERNAL;
      c.long_records += kind == ZBT_PACKED_SHORT;
      c.short_records += kind < ZBT_PACKED_SHORT;
    }
  }
  serverAssert(c.members == zbtreeLength(t));
  return c;
}

void supplement_print_census(const census *c) {
  printf("{\"kind\":\"census\",\"leaves\":%" PRIu64 ",\"members\":%" PRIu64
         ",\"reversed_leaves\":%" PRIu64 ",\"reversed_members\":%" PRIu64
         ",\"external\":%" PRIu64 ",\"short_records\":%" PRIu64
         ",\"long_records\":%" PRIu64
         ",\"active_rehash\":%s,\"old_live\":%" PRIu64 ",\"new_live\":%" PRIu64
         ",\"old_leaves\":%" PRIu64 ",\"new_leaves\":%" PRIu64
         ",\"old_used\":%" PRIu64 ",\"new_used\":%" PRIu64
         ",\"old_size\":%" PRIu64 ",\"new_size\":%" PRIu64
         ",\"wide_old\":%" PRIu64 ",\"wide_new\":%" PRIu64
         ",\"full16_chunks\":%" PRIu64 ",\"full8_chunks\":%" PRIu64
         ",\"reversed_full16_chunks\":%" PRIu64 ",\"full16_members\":%" PRIu64
         ",\"tag_histogram\":[",
         c->leaves, c->members, c->reversed_leaves, c->reversed_members,
         c->external, c->short_records, c->long_records,
         c->rehash ? "true" : "false", c->old_live, c->new_live, c->old_leaves,
         c->new_leaves, c->old_used, c->new_used, c->old_size, c->new_size,
         c->wide_old, c->wide_new, c->full16_chunks, c->full8_chunks,
         c->reversed_full16_chunks, c->full16_members);
  for (unsigned i = 0; i < 256; i++)
    printf("%s%" PRIu64, i ? "," : "", c->tags[i]);
  printf("]}\n");
}
