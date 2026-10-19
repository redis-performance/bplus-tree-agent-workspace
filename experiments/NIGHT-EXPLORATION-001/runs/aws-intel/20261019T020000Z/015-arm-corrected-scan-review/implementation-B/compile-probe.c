#include <stdint.h>
#if defined(__aarch64__) && defined(__ARM_NEON) && \
    defined(__BYTE_ORDER__) && defined(__ORDER_LITTLE_ENDIAN__) && \
    __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__ && \
    !defined(ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE)
#include <arm_neon.h>
#define ZBT_LEAF_TAG_MATCHES_NEON 1
#endif


/* Compile-only declarations: no link, execution, timing or whole-program codegen claim. */
extern uint64_t zbtLeafTagWord(const uint8_t *tags);
extern uint64_t zbtIndexTagMask(uint64_t word, uint8_t tag);
extern unsigned int zbtIndexFirstTag(uint64_t mask);
static inline unsigned int zbtLeafTagMatches(const uint8_t *tags,
                                             unsigned int count, int reversed,
                                             uint8_t tag,
                                             unsigned int *positions)
{
    unsigned int found = 0;
    unsigned int words = count / 8;
    unsigned int last = reversed ? count - 1 : 0;
    unsigned int w = 0;
#ifdef ZBT_LEAF_TAG_MATCHES_NEON
    uint8x16_t wanted = vdupq_n_u8(tag);
    for (; w + 1 < words; w += 2) {
        uint8x16_t bytes = vld1q_u8(tags + w * 8);
        uint8x16_t equal = vceqq_u8(bytes, wanted);
        if (tag == 1) equal = vorrq_u8(equal, vceqq_u8(bytes, vdupq_n_u8(0)));
        /* On little endian, narrowing each shifted pair packs its two
         * 00/ff bytes into adjacent 0/f nibbles in physical byte order. */
        uint8x8_t packed = vshrn_n_u16(vreinterpretq_u16_u8(equal), 4);
        uint64_t matches = vget_lane_u64(vreinterpret_u64_u8(packed), 0);
        while (matches) {
            unsigned int lane = __builtin_ctzll(matches) / 4;
            unsigned int pos = w * 8 + lane;
            positions[found++] = reversed ? last - pos : pos;
            matches &= ~(UINT64_C(15) << (lane * 4));
        }
    }
#endif
    for (; w < words; w++) {
        uint64_t word = zbtLeafTagWord(tags + w * 8);
        uint64_t mask = zbtIndexTagMask(word, tag);
        if (tag == 1) mask |= zbtIndexTagMask(word, 0);
        while (mask) {
            unsigned int pos = w * 8 + zbtIndexFirstTag(mask);
            if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
                positions[found++] = reversed ? last - pos : pos;
            mask &= mask - 1;
        }
    }
    for (unsigned int pos = words * 8; pos < count; pos++) {
        if (tags[pos] == tag || (tag == 1 && tags[pos] == 0))
            positions[found++] = reversed ? last - pos : pos;
    }
    return found;
}


unsigned int compile_probe(const uint8_t *tags, unsigned int count, int reversed, uint8_t tag, unsigned int *positions) { return zbtLeafTagMatches(tags, count, reversed, tag, positions); }
