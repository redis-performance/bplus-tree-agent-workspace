#!/usr/bin/env python3
import difflib,hashlib,json,shutil,subprocess
from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent;REL=OUT.relative_to(Path.cwd());BASE=Path('scratch/m6-lookup/variants');BASE.mkdir(exist_ok=True)
src=Path('src/zset_btree.c').read_text();a=src.index('/* Decode the score at logical');b=src.index('/* Return the raw hash byte',a);old=src[a:b]
physical=old.replace('/* Decode the score at logical position \'pos\'. */','/* Decode directly from a physical packed-score slot. */').replace('zbtScoreLeafScore(zbtScoreLeaf *leaf, unsigned int pos)','zbtScoreLeafPhysicalScore(zbtScoreLeaf *leaf, unsigned int physical)').replace('zbtScoreLeafPhysicalPos(leaf, pos) * bits','physical * bits')
wrapper='''/* Decode the score at logical position 'pos'. */
static double zbtScoreLeafScore(zbtScoreLeaf *leaf, unsigned int pos) {
    return zbtScoreLeafPhysicalScore(leaf, zbtScoreLeafPhysicalPos(leaf, pos));
}

'''
compact='''/* Read-only lookup already knows the physical slot. */
static double zbtScoreLeafPhysicalScore(zbtScoreLeaf *leaf, unsigned int physical) {
    uint64_t delta = leaf->score_bits ?
        zbtReadBits(leaf->data, (size_t)physical * leaf->score_bits,
                    leaf->score_bits) << leaf->n.score_shift : 0;
    uint64_t ordered = leaf->reversed ? leaf->score_base - delta :
                                         leaf->score_base + delta;
    return zbtOrderedToScore(ordered);
}

'''
hit='''            unsigned int logical =
                zbtScoreLeafPhysicalPos(leaf, physical);
            if (score) *score = zbtScoreLeafScore(leaf, logical);
            if (position) *position = logical;'''
replacement='''            if (score) *score = zbtScoreLeafPhysicalScore(leaf, physical);
            if (position)
                *position = zbtScoreLeafPhysicalPos(leaf, physical);'''
body=physical[physical.index('    unsigned int bits'):physical.rindex('}')].replace('    return zbtOrderedToScore(ordered);','    *score = zbtOrderedToScore(ordered);')
local='            if (score) {\n'+''.join('            '+line+'\n' for line in body.splitlines())+'            }\n            if (position)\n                *position = zbtScoreLeafPhysicalPos(leaf, physical);'
choices={'A':src[:a]+physical+wrapper+src[b:],'B':src[:a]+compact+src[a:],'C':src}
choices={v:s.replace(hit,local if v=='C' else replacement) for v,s in choices.items()}
manifest=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_commit='e18d69d0',chair_commit='e1f3b73c',population='three sequential implementation passes by one worker, not independent agents',backend='Codex/GPT-6 family; exact serving variant/cost unknown',isolation='separate copied source/build directories; prior Git worktree denial not retried',variants={})
for v in ('0','A','B','C'):
 d=BASE/v;assert not d.exists();d.mkdir()
 for name in ('src','compat','vendor','tests','bench'):shutil.copytree(name,d/name)
 shutil.copy2('Makefile',d/'Makefile');(d/REL).mkdir(parents=True)
 for name in ('lookup-bench.c','physical-oracle.c'):shutil.copy2(OUT/name,d/REL/name)
 (d/REL/'../002-rank').mkdir(exist_ok=True);shutil.copy2(OUT/'../002-rank/night-rank-sampler.h',d/REL/'../002-rank/night-rank-sampler.h')
 s=src if v=='0' else choices[v];(d/'src/zset_btree.c').write_text(s)
 if v!='0':
  assert s!=src and s.count('memchr(next, tag, end - next)')==1
  p=OUT/'variants'/v;p.mkdir(parents=True)
  (p/'candidate.patch').write_text(''.join(difflib.unified_diff(src.splitlines(True),s.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  (p/'implementation.md').write_text('# Sequential implementation '+v+'\n\nM6-LOOKUP-PHYSICAL-001. '+{'A':'Extract exact physical decoder and retain logical wrapper.','B':'Use existing generic zbtReadBits for new physical decoder; logical decoder unchanged.','C':'Inline physical decoding locally in matched-member return; logical decoder unchanged.'}[v]+'\nOnly src/zset_btree.c changes. Keep memchr/full comparisons, finite/signed-zero/reversed base semantics, position outputs and memory. No independent agent; exact serving model/token cost unknown.\n')
 manifest['variants'][v]=dict(source_sha256=hashlib.sha256(s.encode()).hexdigest(),snapshot=str(d),referee_sha256=hashlib.sha256((d/REL/'lookup-bench.c').read_bytes()).hexdigest())
 if v!='0':manifest['variants'][v]['patch_sha256']=hashlib.sha256((OUT/'variants'/v/'candidate.patch').read_bytes()).hexdigest()
(OUT/'implementation-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print('isolated 0/A/B/C snapshots and three patches complete')
