#ifndef SCAN_SUPPLEMENT_CENSUS_H
#define SCAN_SUPPLEMENT_CENSUS_H
#include "zset_btree.h"
#include <stdint.h>
typedef struct {
  uint64_t leaves, members, reversed_leaves, reversed_members, external,
      short_records, long_records, old_live, new_live, old_leaves, new_leaves,
      old_used, new_used, old_size, new_size, wide_old, wide_new, rehash;
  uint64_t full16_chunks, full8_chunks, reversed_full16_chunks, full16_members;
  uint64_t tags[256];
} census;
census supplement_census(zbtreeSet *t);
void supplement_print_census(const census *c);
#endif
