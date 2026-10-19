/* M6 count-one policy referee: compile separately from the shared driver, without LTO.
 * All variants include the same original tree plus their private bulk helper. */
#ifndef DECODER_TREE_SOURCE
#define DECODER_TREE_SOURCE "../src/zset_btree.c"
#endif
#include DECODER_TREE_SOURCE
#include "decoder_kernel.h"
#include <math.h>

struct decoder_fixture {
    unsigned count, leaves;
    zbtScoreLeaf **leaf;
    uint64_t *expected;
    decoder_info info;
};

static uint64_t double_bits(double x) {
    uint64_t bits;
    memcpy(&bits, &x, sizeof(bits));
    return bits;
}

static uint64_t next_random(uint64_t *state) {
    uint64_t x = (*state += UINT64_C(0x9e3779b97f4a7c15));
    x = (x ^ (x >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    x = (x ^ (x >> 27)) * UINT64_C(0x94d049bb133111eb);
    return x ^ (x >> 31);
}

/* Independent, bit-at-a-time packing; never call the production score writer. */
static void put_bits(unsigned char *data, size_t offset, unsigned width, uint64_t x) {
    for (unsigned bit = 0; bit < width; bit++) {
        size_t pos = offset + bit;
        unsigned char mask = (unsigned char)(1u << (pos % 8));
        data[pos / 8] = (data[pos / 8] & ~mask) | (((x >> bit) & 1) ? mask : 0);
    }
}

decoder_fixture *decoder_create(unsigned width, unsigned shift, unsigned reversed,
                                unsigned count, unsigned leaves, uint64_t seed) {
    serverAssert(width <= 64 && shift <= 63 && width + shift <= 64);
    serverAssert(reversed <= 1 && count >= 1 && count <= 96 && leaves >= 1);
    decoder_fixture *f = zcalloc(sizeof(*f));
    f->count = count; f->leaves = leaves;
    f->leaf = zcalloc(leaves * sizeof(*f->leaf));
    f->expected = zmalloc((size_t)count * leaves * sizeof(*f->expected));
    f->info.fingerprint = UINT64_C(14695981039346656037);
    uint64_t mask = width == 64 ? UINT64_MAX : (UINT64_C(1) << width) - 1;
    const uint64_t low = UINT64_C(0x0010000000000000);
    const uint64_t high = UINT64_C(0xffefffffffffffff);
    for (unsigned j = 0; j < leaves; j++) {
        size_t bytes = sizeof(zbtScoreLeaf) + zbtScoreLeafScoreBytes(count, width);
        zbtScoreLeaf *leaf = f->leaf[j] = zcalloc(bytes);
        leaf->n.count = count; leaf->n.isleaf = 1;
        leaf->score_bits = width; leaf->n.score_shift = shift;
        leaf->reversed = reversed;
        leaf->score_base = reversed ? high - j * 1024 : low + j * 1024;
        /* Explicit finite boundaries, including both zero bit patterns. */
        const uint64_t boundaries[] = {UINT64_C(0x7fffffffffffffff),
            UINT64_C(0x8000000000000000), UINT64_C(0x7ffffffffffffffe),
            UINT64_C(0x8000000000000001)};
        if (j % 8 >= 1 && j % 8 <= 4) leaf->score_base = boundaries[j % 8 - 1];
        uint64_t limit = (reversed ? leaf->score_base - low : high - leaf->score_base) >> shift;
        memset(leaf->data, 0xa5, bytes - sizeof(*leaf));
        f->info.leaf_bytes += bytes;
        for (unsigned i = 0; i < count; i++) {
            uint64_t delta = next_random(&seed) & mask;
            if (i % 4 == 0) delta = 0;
            else if (i % 4 == 1) delta = mask;
            if (delta > limit) delta %= limit + 1;
            unsigned physical = reversed ? count - 1 - i : i;
            size_t offset = (size_t)physical * width;
            put_bits(leaf->data, offset, width, delta);
            uint64_t ordered = reversed ? leaf->score_base - (delta << shift) :
                                          leaf->score_base + (delta << shift);
            uint64_t expected = ordered >> 63 ? ordered ^ (UINT64_C(1) << 63) : ~ordered;
            f->expected[(size_t)j * count + i] = expected;
            f->info.expected_sum += expected;
            f->info.fingerprint = (f->info.fingerprint ^ expected) * UINT64_C(1099511628211);
            f->info.offset_mask |= 1u << (offset & 7);
            f->info.crossings_per_round += width > 64 - (offset & 7);
        }
    }
    f->info.decodes_per_round = (size_t)count * leaves;
    return f;
}

decoder_info decoder_describe(const decoder_fixture *f) { return f->info; }

int decoder_validate(decoder_fixture *f) {
    for (unsigned j = 0; j < f->leaves; j++) {
        zbtScoreLeaf *leaf = f->leaf[j];
        for (unsigned i = 0; i < f->count; i++) {
            double value = zbtScoreLeafScore(leaf, i);
            if (!isfinite(value) || double_bits(value) != f->expected[(size_t)j * f->count + i])
                return 0;
        }
        const unsigned starts[] = {0, f->count / 2, f->count};
        for (unsigned k = 0; k < 3; k++) {
            unsigned start = starts[k];
            const unsigned counts[] = {0, start < f->count ? 1 : 0, f->count - start};
            for (unsigned n = 0; n < 3; n++) {
                double out[98];
                for (unsigned i = 0; i < 98; i++) out[i] = 123.25;
                zbtScoreLeafDecodePolicy(leaf, start, counts[n], out + 1);
                for (unsigned i = 0; i < 98; i++) {
                    uint64_t expected = (i >= 1 && i <= counts[n]) ?
                        f->expected[(size_t)j * f->count + start + i - 1] : double_bits(123.25);
                    if (double_bits(out[i]) != expected) return 0;
                }
            }
        }
    }
    return 1;
}

/* Throughput loop with four independent unsigned checksum chains. This is not
 * dependent-operation latency. The compiler may inline/unroll/vectorise normally. A materialization barrier
 * forces the same output writes before checksum consumption in every variant.
 * The round barrier stops repeat-invariant load hoisting; it emits no instruction
 * on GCC/Clang. There are no timers, allocation, I/O or assertions in this loop. */
__attribute__((noinline)) uint64_t decoder_batch(decoder_fixture *f, unsigned rounds) {
    uint64_t a = 0, b = 0, c = 0, d = 0;
    for (unsigned r = 0; r < rounds; r++) {
        __asm__ volatile("" : : "r"(f) : "memory");
        for (unsigned j = 0; j < f->leaves; j++) {
            zbtScoreLeaf *leaf = f->leaf[j];
            double values[96];
            zbtScoreLeafDecodePolicy(leaf, 0, f->count, values);
            __asm__ volatile("" : : "r"(values) : "memory");
            unsigned i = 0;
            for (; i + 3 < f->count; i += 4) {
                a += double_bits(values[i]);
                b += double_bits(values[i + 1]);
                c += double_bits(values[i + 2]);
                d += double_bits(values[i + 3]);
            }
            for (; i < f->count; i++) a += double_bits(values[i]);
        }
    }
    return a + b + c + d;
}

void decoder_destroy(decoder_fixture *f) {
    for (unsigned j = 0; j < f->leaves; j++) zfree(f->leaf[j]);
    zfree(f->leaf); zfree(f->expected); zfree(f);
}
