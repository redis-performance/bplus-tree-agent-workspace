from pathlib import Path
import datetime,difflib,hashlib,json,shutil
P=Path(__file__).resolve().parent;R=P.parents[1];H=R/'experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002';F=json.loads((H/'freeze.json').read_text());S=R/'scratch/experiment006';S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=(R/F['snapshot']/'src/zset_btree.c').read_text();anchor='/* Look for an exact member in one score leaf.';assert old.count(anchor)==1
common='''#define ZBT_INLINE_TAG_SEARCH 1
static inline uint8_t *zbtInlineTagSearch(uint8_t *p, uint8_t tag, size_t n) {
'''
tail='''    while (n--) { if (*p == tag) return p; p++; }
    return NULL;
}

'''
word='''        uint64_t word;
        memcpy(&word, p, sizeof(word));
        uint64_t x = word ^ repeated;
        uint64_t matches = (x - UINT64_C(0x0101010101010101)) &
                           ~x & UINT64_C(0x8080808080808080);
        if (matches) return p + (__builtin_ctzll(matches) >> 3);
'''
B=common+'''#if defined(__BYTE_ORDER__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
    const uint64_t repeated = (uint64_t)tag * UINT64_C(0x0101010101010101);
    while (n >= 8) {
'''+word+'''        p += 8; n -= 8;
    }
#endif
'''+tail
C=common+'''#if defined(__BYTE_ORDER__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
    const uint64_t repeated = (uint64_t)tag * UINT64_C(0x0101010101010101);
    while (n >= 16) {
      {
'''+word+'''      }
      p += 8;
      {
'''+word+'''      }
      p += 8; n -= 16;
    }
    if (n >= 8) {
'''+word+'''        p += 8; n -= 8;
    }
#endif
'''+tail
impl={'A':common+tail,'B':B,'C':C};files={}
for v in ['control','A','B','C']:
 D=S/v;D.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=D/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for n in ['tests/raw_guard_oracle.c','tests/tag_search_oracle.c']:shutil.copy2(R/n,D/n)
 if v!='control':
  changed=old.replace(anchor,impl[v]+anchor).replace('memchr(next, tag, end - next)','zbtInlineTagSearch(next, tag, (size_t)(end - next))');(D/'src/zset_btree.c').write_text(changed)
  V=P/'variants'/v;V.mkdir();(V/'candidate.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  (V/'implementation.md').write_text(f'''# Variant {v}

Sequential implementation pass, not an independent agent. Backend/model/cost unknown.
Exact baseline{F['base_commit']}plus frozen HARNESS-007attempt002; isolated ownsource/build.
Implementation: {dict(A='bytewise bounded scan, portable',B='8-byte memcpy/SWAR scan with scalar tail and non-little-endian fallback',C='two8-byte chunks per bounded16-byte iteration,8-byte cleanup and scalar tail/fallback')[v]}.
Only leaf tag search changes. Lowest matching byte is returned; packed layout/hash/
length/full-member comparison, score mapping, allocation and assertions unchanged.
Word zero-byte borrow may mark higher bytes after a zero, but ctz selects the first
true zero on little endian; non-little-endian uses byte loop. Loads require n>=8;
16-byte version checks n>=16 before both chunks. No unaligned typed loads or overread.
Risk: extra instructions/register pressure can outweigh avoided memchr boundary;
compiler/codegen and measured guards decide. Keep losing patch regardless of outcome.
''')
 files[v]={str(p.relative_to(D)):sha(p) for p in D.rglob('*') if p.is_file()}
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),provenance='uncommitted isolated snapshots; main unchanged; protected metadata not retried',frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),parent_freeze_sha256=sha(H/'freeze.json'),files=files),indent=2)+'\n')
