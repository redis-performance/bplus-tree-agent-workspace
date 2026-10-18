#ifndef DECODER_KERNEL_H
#define DECODER_KERNEL_H
#include <stddef.h>
#include <stdint.h>
typedef struct decoder_fixture decoder_fixture;
typedef struct {
    uint64_t expected_sum, fingerprint;
    size_t leaf_bytes, decodes_per_round, crossings_per_round;
    unsigned offset_mask;
} decoder_info;
decoder_fixture *decoder_create(unsigned width, unsigned shift, unsigned reversed,
                                unsigned count, unsigned leaves, uint64_t seed);
decoder_info decoder_describe(const decoder_fixture *fixture);
int decoder_validate(decoder_fixture *fixture);
uint64_t decoder_batch(decoder_fixture *fixture, unsigned rounds);
void decoder_destroy(decoder_fixture *fixture);
#endif
