from pathlib import Path
import json,hashlib,shutil,difflib,datetime
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-004/freeze.json').read_text());S=R/'scratch/exp-003';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();original=(R/F['snapshot']/'src/zset_btree.c').read_text();start=original.index('int zbtreeIteratorNext(');end=original.index('/* Return the rank where a score bound',start);body=original[start:end];begin=body.index('    if (ele || len) {');stop=body.index('    if (score)',begin);old=body[begin:stop]
helpers={
'A':'''static __attribute__((noinline)) const unsigned char *zbtIteratorMember(zbtScoreLeaf *leaf, unsigned int pos, size_t *len) {
    return zbtScoreLeafElement(leaf, pos, len);
}

''',
'B':'''static __attribute__((noinline)) void zbtIteratorMember(zbtScoreLeaf *leaf, unsigned int pos, const unsigned char **ele, size_t *len) {
    size_t actual;
    const unsigned char *p = zbtScoreLeafElement(leaf, pos, &actual);
    if (ele) *ele = p;
    if (len) *len = actual;
}

''',
'C':'''typedef struct { const unsigned char *ele; size_t len; } zbtIteratorMemberResult;
static __attribute__((noinline)) zbtIteratorMemberResult zbtIteratorMember(zbtScoreLeaf *leaf, unsigned int pos) {
    zbtIteratorMemberResult result;
    result.ele = zbtScoreLeafElement(leaf, pos, &result.len);
    return result;
}

'''}
blocks={'A':old.replace('zbtScoreLeafElement(leaf, pos, &elelen)','zbtIteratorMember(leaf, pos, &elelen)'), 'B':'    if (ele || len) zbtIteratorMember(leaf, pos, ele, len);\n', 'C':'''    if (ele || len) {
        zbtIteratorMemberResult result = zbtIteratorMember(leaf, pos);
        if (ele) *ele = result.ele;
        if (len) *len = result.len;
    }
'''};allfiles={}
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(R/'tests/iterator_mutation_oracle.c',B/'tests/iterator_mutation_oracle.c')
 if v!='control':
  changed=original[:start]+helpers[v]+body[:begin]+blocks[v]+body[stop:]+original[end:];(B/'src/zset_btree.c').write_text(changed);D=P/'variants'/v;D.mkdir();(D/'candidate.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')));(D/'implementation.md').write_text(f'# Variant {v}\n\nSequential implementation pass,not independent agent.\n'+{'A':'Pointer-return helper,local output length.','B':'Void helper handles optional member/length outputs.','C':'Struct-return helper returns pointer/length in aggregate.'}[v]+'\nOnly member decode isolation;original condition/score/state unchanged. Helper call may\nregress member modes;no guard tradeoff. Backend/model/cost unknown. Patch retained.\n')
 allfiles[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};D=P/v;D.mkdir();(D/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),files=allfiles[v]),indent=2)+'\n')
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),parent_freeze_sha256=sha(R/'experiments/OVERNIGHT-2026-10-17/HARNESS-004/freeze.json'),provenance='uncommitted isolated EXP-003 member-decoder variants over frozen HARNESS-004',files=allfiles),indent=2)+'\n')
# Keep original referee validation logic;use preregistered n129 mode matrix plus new mutation oracle.
code=(R/'experiments/EXP-002/guard-extension/validate-one.py').read_text().replace('[1,31,32,33,129]','[129]').replace(" print(kind,'640 fixture cells plus original tests PASS',flush=True)"," run(kind+'-mutation-build',common+['-DREDIS_DEBUG','tests/iterator_mutation_oracle.c',*support,'-o',f'build/{kind}/mutation'])\n run(kind+'-mutation',[f'build/{kind}/mutation'])\n print(kind,'128 fixture cells plus original and mutation tests PASS',flush=True)")
(P/'validate-one.py').write_text(code)
# Reuse exact serial guard protocol;replace only paths and validation expectation.
code=(R/'experiments/EXP-002/guard-extension/run.py').read_text().replace('R=P.parents[2]','R=P.parents[1]').replace('len(val)==1286','len(val)==266');(P/'run.py').write_text(code)
code=(R/'experiments/EXP-002/guard-extension/analyse.py').read_text().replace('R=P.parents[2]','R=P.parents[1]').replace("P.parent/'variants'","P/'variants'")
code=code.replace("eligible=not regress and all(c['controls'] for c in cells) and primary['high_pct']<=-2","eligible=not regress and all(c['controls'] for c in cells) and primary['high_pct']<=-2 and all(c['high_pct']<=1 for c in cells if c['qualified'] and c['cell']!='f-int16-m4')").replace('EXP-002 expanded guards','EXP-003 member-decoder screening');(P/'analyse.py').write_text(code)
