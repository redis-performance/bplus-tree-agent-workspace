from pathlib import Path
import json,hashlib,shutil,difflib
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-003/freeze.json').read_text());S=R/'scratch/exp-002';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
original=(R/F['snapshot']/'src/zset_btree.c').read_text();start=original.index('int zbtreeIteratorNext(');end=original.index('/* Return the rank where a score bound',start);body=original[start:end]
fast='''    zbtScoreLeaf *leaf = iter->leaf;
    if (leaf == NULL) return 0;
    unsigned int pos = iter->pos;
    *score = zbtScoreLeafScore(leaf, pos);
    if (pos + 1 < leaf->n.count) iter->pos = pos + 1;
    else { iter->leaf = leaf->next; iter->pos = 0; }
    return 1;
'''
variants={}
guard='!reverse && ele == NULL && len == NULL && score != NULL'
a=body.replace('    zbtScoreLeaf *leaf = iter->leaf;',f'    if ({guard}) {{\n'+fast+'    }\n    zbtScoreLeaf *leaf = iter->leaf;',1);variants['A']=a
fallback=body.replace('int zbtreeIteratorNext(', 'static __attribute__((noinline)) int zbtIteratorGeneric(' ,1)
wrapper='''int zbtreeIteratorNext(zbtreeIterator *iter, int reverse,
                       const unsigned char **ele, size_t *len, double *score)
{
    if (GUARD) return zbtIteratorForwardScore(iter, score);
    return zbtIteratorGeneric(iter, reverse, ele, len, score);
}

'''.replace('GUARD',guard)
for v,attr in [('B','__attribute__((noinline))'),('C','inline')]:variants[v]=fallback+f'static {attr} int zbtIteratorForwardScore(zbtreeIterator *iter, double *score)\n{{\n'+fast+'}\n\n'+wrapper
allfiles={}
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for name,h in F['files'].items():
  src=R/F['snapshot']/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for name in ['tests/lex_boundary_oracle.c','tests/score_boundary_oracle.c','tests/boundary_oracle.c']:shutil.copy2(R/name,B/name)
 if v!='control':
  changed=original[:start]+variants[v]+original[end:];(B/'src/zset_btree.c').write_text(changed)
  D=P/'variants'/v;D.mkdir();(D/'candidate.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  (D/'implementation.md').write_text(f'# Variant {v}\n\nSequential coordinator implementation pass {v}; not independent agent. Same frozen base.\n'+{'A':'Inline early-return specialized body; generic body retained verbatim after guard.','B':'Separate noinline specialized/generic helpers; public function dispatches.','C':'Inline specialized helper and noinline generic fallback; public dispatch.'}[v]+'\nOnly iterator dispatch changed; decoder/state representation unchanged. End-of-leaf and\noptional-output/reverse behavior require existing tests. Tree memory unchanged by design.\nExact backend/model/cost unknown. Patch preserved regardless of outcome.\n')
 allfiles[v]={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],parent_freeze_sha256=sha(R/'experiments/OVERNIGHT-2026-10-17/HARNESS-003/freeze.json'),snapshot_root=str(S.relative_to(R)),provenance='uncommitted isolated variants; root untouched',files=allfiles),indent=2)+'\n')
