from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/overnight-counters-006';assert not S.exists();S.mkdir()
F=json.loads((P.parent/'BOUNDARY-014/compact-extension/manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
M=dict(status='preparing',base_commit=F['base_commit'],provenance='uncommitted diagnostic adapters; unchanged baseline source',plan_sha256=sha(P/'PLAN.md'),snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for policy,q in [('ambient',0),('exact',1),('round16',16)]:
 B=S/policy;B.mkdir()
 desc=F['snapshots']['control']
 for name,h in desc['files'].items():
  src=R/desc['path']/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 adapter=(B/'compat/standalone.c').read_text()
 if q:
  before,rest=adapter.split('size_t zmalloc_usable_size(void *ptr) {',1)
  after=rest.split('uint64_t siphash(',1)[1]
  revised=before+(P/'allocator.inc').read_text()+'\nuint64_t siphash('+after
  assert revised.count('free(s - sizeof(struct sdshdr64));')==1
  revised=revised.replace('free(s - sizeof(struct sdshdr64));','zfree(s - sizeof(struct sdshdr64));')
  (B/'compat/standalone.c').write_text(revised)
  (P/(policy+'.patch')).write_text(''.join(difflib.unified_diff(adapter.splitlines(True),revised.splitlines(True),fromfile='a/compat/standalone.c',tofile='b/compat/standalone.c')))
 oracle=(B/'tests/zero_physical_oracle.c').read_text().split('int main(void) {')[0]
 oracle=oracle.replace('static void verify(zbtreeSet *tree) {','static uint64_t layout_hash,capacity_hash;\nstatic void mix(uint64_t *h,uint64_t x) {*h=(*h^x)*UINT64_C(1099511628211);}\nstatic void verify(zbtreeSet *tree) {')
 oracle=oracle.replace('prev=leaf; forward_leaves', 'mix(&layout_hash,leaf->n.count);mix(&layout_hash,leaf->reversed);mix(&layout_hash,leaf->score_bits);mix(&layout_hash,leaf->n.score_shift);mix(&layout_hash,leaf->score_base);mix(&layout_hash,leaf->record_start);mix(&capacity_hash,zmalloc_usable_size(leaf));\n        prev=leaf; forward_leaves')
 oracle=oracle.replace('nkeys=n;uint8_t hs[16];','layout_hash=capacity_hash=UINT64_C(14695981039346656037);\n    uint64_t f0=forward_leaves,r0=reversed_leaves,o0=reversal_opportunities;\n    nkeys=n;uint8_t hs[16];')
 oracle=oracle.replace('    printf("PASS n=', '    printf("LAYOUT hash=%016"PRIx64" capacity=%016"PRIx64" forward=%"PRIu64" reversed=%"PRIu64" opportunities=%"PRIu64"\\n",layout_hash,capacity_hash,forward_leaves-f0,reversed_leaves-r0,reversal_opportunities-o0);\n    printf("PASS n=')
 main=(P.parent/'BOUNDARY-014/compact-extension/compact_zero.c').read_text().split('int main(void) {')[1]
 (B/'tests/diagnostic.c').write_text(oracle+'int main(void) {'+main)
 shutil.copy2(P/'unit.c',B/'tests/unit.c');(B/'build').mkdir()
 M['snapshots'][policy]=dict(path=str(B.relative_to(R)),quantum=q,files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()})
M['status']='frozen';M['frozen_utc']=utc();save()
def run(name,cmd,B):
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),started_utc=utc())
 with (P/(name+'.stdout')).open('w') as out,(P/(name+'.stderr')).open('w') as err:
  try:rc=subprocess.run(cmd,cwd=B,stdout=out,stderr=err,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(name+'.stdout')),stderr_sha256=sha(P/(name+'.stderr')));M['runs'].append(row);save()
 assert rc==0,name
for policy,desc in M['snapshots'].items():
 B=R/desc['path']
 for opt in ['O1','O3']:
  for san in ['native','sanitize']:
   name=f'{policy}-{opt}-{san}';flags=['-'+opt]+([] if san=='native' else ['-fsanitize=address,undefined','-fno-sanitize-recover=all'])
   common=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',f'-DCAPACITY_QUANTUM={desc["quantum"]}',*flags]
   for kind in ['unit','diagnostic']:
    binary=f'build/{name}-{kind}'
    run(name+'-'+kind+'-build',common+[f'tests/{kind}.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],B)
    run(name+'-'+kind,[binary],B)
    M.setdefault('binaries',{})[binary]=sha(B/binary);save()
   print(name,'PASS',flush=True)
for desc in M['snapshots'].values():
 for name,h in desc['files'].items():assert sha(R/desc['path']/name)==h
M['status']='complete';save()
