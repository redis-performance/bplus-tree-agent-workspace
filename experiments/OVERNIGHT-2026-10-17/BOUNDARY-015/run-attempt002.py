from pathlib import Path
import datetime, difflib, hashlib, json, shutil, subprocess, time

P = Path(__file__).resolve().parent
R = P.parents[2]
P = P / 'attempt-002'
P.mkdir()
shutil.copy2(P.parent/'PLAN.md',P/'PLAN.md')
S = R / 'scratch/overnight-boundary-015-attempt002'
assert not S.exists()
S.mkdir()
F = json.loads((P.parents[1] / 'COUNTERS-006/manifest.json').read_text())
G = json.loads((R / 'experiments/EXP-004/freeze.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
M = dict(status='preparing', base_commit=G['base_commit'],
         provenance='uncommitted isolated snapshots; diagnostic allocator only',
         plan_sha256=sha(P/'PLAN.md'), snapshots={}, runs=[],
         root_hashes={n:sha(R/n) for n in ['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c']})
def save():
    (P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')

(P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/mixed_capacity_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/mixed_capacity_oracle.c')))
for policy in ['ambient','exact','round16']:
    desc=F['snapshots'][policy]
    for variant in ['control','A','B','C']:
        name=policy+'-'+variant; B=S/name;B.mkdir()
        for n,h in desc['files'].items():
            src=R/desc['path']/n;assert sha(src)==h
            dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        if variant!='control':
            src=R/G['snapshot_root']/variant/'src/zset_btree.c'
            assert sha(src)==G['files'][variant]['src/zset_btree.c']
            shutil.copy2(src,B/'src/zset_btree.c')
        shutil.copy2(R/'tests/mixed_capacity_oracle.c',B/'tests/mixed_capacity_oracle.c')
        M['snapshots'][name]=dict(path=str(B.relative_to(R)),policy=policy,variant=variant,quantum=desc['quantum'],files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()})
        (B/'build').mkdir()
M['status']='frozen';M['frozen_utc']=utc();save()
start=time.monotonic()
for name,desc in M['snapshots'].items():
    B=R/desc['path']
    for kind in ['release','sanitize']:
        flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
        common=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',f'-DCAPACITY_QUANTUM={desc["quantum"]}',*flags]
        for target in ['oracle','upstream']:
            binary='build/'+kind+'-'+target
            sources=['tests/mixed_capacity_oracle.c'] if target=='oracle' else ['-DREDIS_TEST','tests/upstream.c','src/zset_btree.c']
            cmd=common+sources+['compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
            for stage,args in [('build',cmd),('run',[binary])]:
                tag=name+'-'+kind+'-'+target+'-'+stage
                if time.monotonic()-start>600:
                    M['status']='budget-exhausted';save();raise SystemExit(3)
                row=dict(name=tag,policy=desc['policy'],variant=desc['variant'],kind=kind,target=target,stage=stage,command=args,cwd=desc['path'],started_utc=utc())
                with (P/(tag+'.stdout')).open('w') as out,(P/(tag+'.stderr')).open('w') as err:
                    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
                    except subprocess.TimeoutExpired:rc='timeout'
                row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')))
                M['runs'].append(row);save()
                if rc!=0:
                    M['status']='failed';save();raise SystemExit(tag+' failed '+str(rc))
            M.setdefault('binaries',{})[name+'-'+kind+'-'+target]=sha(B/binary);save()
        print(name,kind,'PASS',flush=True)
for desc in M['snapshots'].values():
    for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
for n,h in M['root_hashes'].items():assert sha(R/n)==h
M['status']='complete';save()
