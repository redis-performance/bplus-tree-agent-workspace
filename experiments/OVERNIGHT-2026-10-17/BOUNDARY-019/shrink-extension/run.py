from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'scratch/overnight-boundary-019-shrink'

assert not S.exists();S.mkdir();F=json.loads((R/'experiments/EXP-004/freeze.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
M=dict(status='preparing',base_commit=F['base_commit'],provenance='uncommitted isolated snapshots; unchanged ambient allocator',plan_sha256=sha(P/'PLAN.md'),snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (P/'public_shrink_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/public_shrink_oracle.c')))
for v in ['control','A','B','C']:
    B=S/v;B.mkdir()
    for n,h in F['files'][v].items():
        src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
    shutil.copy2(P/'public_shrink_oracle.c',B/'tests/public_shrink_oracle.c')
    M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M['status']='frozen';M['frozen_utc']=utc();save();start=time.monotonic()
for v,desc in M['snapshots'].items():
    B=R/desc['path']
    for kind in ['release','sanitize']:
        if time.monotonic()-start>600:M['status']='budget-exhausted';save();raise SystemExit(3)
        flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
        binary='build/'+kind
        cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'tests/public_shrink_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
        for stage,args in [('build',cmd),('run',[binary])]:
            tag=v+'-'+kind+'-'+stage;row=dict(name=tag,variant=v,kind=kind,stage=stage,command=args,cwd=desc['path'],started_utc=utc())
            with (P/(tag+'.stdout')).open('w') as out,(P/(tag+'.stderr')).open('w') as err:
                try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
                except subprocess.TimeoutExpired:rc='timeout'
            row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')));M['runs'].append(row);save()
            if rc!=0:M['status']='failed';save();raise SystemExit(tag+' failed '+str(rc))
        M.setdefault('binaries',{})[v+'-'+kind]=sha(B/binary);save();print(v,kind,'PASS',flush=True)
for desc in M['snapshots'].values():
    for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
M['status']='complete';save()
outputs=[(P/(r['name']+'.stdout')).read_bytes() for r in M['runs'] if r['stage']=='run']
assert len(outputs)==8
# Physical identifiers may vary with allocator; per-fixture coverage is asserted in C.
digests=[o.decode().split('digest=')[-1].strip() for o in outputs]
assert len(set(digests))==1
(P/'summary.json').write_text(json.dumps(dict(status='pass',cells=8,identical_output=len(set(outputs))==1,identical_logical_digest=True,output=outputs[0].decode()),indent=2)+'\n')
