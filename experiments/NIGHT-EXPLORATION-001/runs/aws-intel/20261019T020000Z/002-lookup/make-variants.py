from pathlib import Path
import difflib,hashlib,json,subprocess
P=Path(__file__).resolve().parent
source=subprocess.check_output(['git','show','8fab511e:src/zset_btree.c'],text=True)
start='''#if defined(__SSE2__)
#include <emmintrin.h>
#endif

/* Bounded inline tag search; never reads outside [next, next + count). */
static inline uint8_t *zbtFindTagSIMD(uint8_t *next, uint8_t tag, size_t count)
{
#if defined(__SSE2__)
'''
loop='''    __m128i needle = _mm_set1_epi8((char)tag);
    while (count >= 16) {
        __m128i bytes = _mm_loadu_si128((const __m128i *)(const void *)next);
        unsigned mask = (unsigned)_mm_movemask_epi8(_mm_cmpeq_epi8(bytes, needle));
        if (mask) return next + __builtin_ctz(mask);
        next += 16;
        count -= 16;
    }
'''
scalar='''    while (count) {
        if (*next == tag) return next;
        next++;
        count--;
    }
    return NULL;
'''
tail='''#else
    return memchr(next, tag, count);
#endif
}

'''
for name in ['A','B','C']:
 helper=start
 if name=='C':helper+='    size_t original_count = count;\n'
 helper+=loop
 if name=='A':helper+=scalar
 elif name=='B':helper+='    return count ? memchr(next, tag, count) : NULL;\n'
 else:helper+='''    if (count && original_count >= 16) {
        uint8_t *last = next + count - 16;
        __m128i bytes = _mm_loadu_si128((const __m128i *)(const void *)last);
        unsigned mask = (unsigned)_mm_movemask_epi8(_mm_cmpeq_epi8(bytes, needle));
        mask &= 0xffffu << (16 - count);
        return mask ? last + __builtin_ctz(mask) : NULL;
    }
'''+scalar
 helper+=tail
 anchor='/* Look for an exact member in one score leaf.'
 modified=source.replace(anchor,helper+anchor).replace('uint8_t *found = memchr(next, tag, end - next);','uint8_t *found = zbtFindTagSIMD(next, tag, end - next);')
 assert modified!=source
 d=P/'variants'/name;d.mkdir(parents=True,exist_ok=True)
 (d/'candidate.patch').write_text(''.join(difflib.unified_diff(source.splitlines(True),modified.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 (d/'implementation.md').write_text(f'# Sequential implementation {name}\n\nOne native worker, not an independent implementer. Exact model/cost unknown. Only bounded tag scanner and callsite change. Baseline8fab511e. Choice'+{'A':' scalar tail','B':' libc tail','C':' overlapping masked tail'}[name]+'. First-match, exact length and page-boundary risks tested before timing.\n')
 (d/'source-sha256.json').write_text(json.dumps({'baseline':hashlib.sha256(source.encode()).hexdigest(),'candidate':hashlib.sha256(modified.encode()).hexdigest()},indent=2)+'\n')
