#!/usr/bin/env python3
"""Serial M6 rank referee preparation, public profiling and baseline qualification."""
import csv, hashlib, io, json, math, os, shutil, statistics, subprocess, sys, time
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
BUILD = Path('scratch/m6-rank/build')
BIN = BUILD/'night-rank'
SIZES=(10000,100000,1000000)
SEEDS=(1,2,3,1,2,3)
def utc(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d): Path(p).write_text(json.dumps(d,indent=2)+'\n')
def run(cmd,name,folder='validation',timeout=120,env=None,expect=0):
    p=OUT/folder;p.mkdir(exist_ok=True)
    start=utc(); t=time.monotonic()
    r=subprocess.run([str(x) for x in cmd],capture_output=True,text=True,timeout=timeout,env=env)
    (p/(name+'.stdout')).write_text(r.stdout)
    (p/(name+'.stderr')).write_text(r.stderr)
    with (OUT/'commands.jsonl').open('a') as f:
        f.write(json.dumps(dict(name=name,command=[str(x) for x in cmd],started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder))+'\n')
    if expect is not None: assert r.returncode==expect,(name,r.returncode,r.stderr[:400])
    return r

def build(name,source='src/zset_btree.c',san=False,extra=(),bench='bench/night-rank.c'):
    flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
    if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
    cmd=['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','-I'+str(OUT.relative_to(ROOT)),*extra,bench,source,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',BUILD/name]
    return run(cmd,'build-'+name)
def args(binary,n=1000,ops=2003,seed=1,mode='rank',layout='integer',member=16,batches=1):
    return [binary,'--size',n,'--ops',ops,'--seed',seed,'--mode',mode,'--layout',layout,'--member-bytes',member,'--batches',batches]
def prepare():
    BUILD.mkdir(parents=True,exist_ok=True)
    build('night-rank');build('night-rank-san',san=True)
    checks=[]
    for binary in [BIN,BUILD/'night-rank-san']:
        for n in [100,1000,10000,100000,1000000]:
            for layout in ['integer','ties','finite']:
                name=f'{binary.name}-n{n}-{layout}'
                run(args(binary,n=n,layout=layout),name);checks.append(name)
        for mode in ['reverse','score','miss']:
            for layout in ['integer','ties','finite']:
                for member in [8,16,319,320,321,1024]:
                    name=f'{binary.name}-{mode}-{layout}-m{member}'
                    run(args(binary,mode=mode,layout=layout,member=member,batches=2),name);checks.append(name)
    bad=Path('scratch/m6-rank/bad-rank.c');s=Path('src/zset_btree.c').read_text();needle='unsigned long rank = zbtScoreRank(leaf, pos);';assert s.count(needle)==1
    bad.write_text(s.replace(needle,needle+'\n    rank++;'))
    build('night-rank-fault',source=str(bad))
    r=run(args(BUILD/'night-rank-fault',n=100),'fault-rank-plus-one',expect=None)
    assert r.returncode!=0 and 'ranks[id]' in r.stderr
    profile_source=OUT/'accumulation-diagnostic.c'
    for name,extra in [('accumulation',[]),('census',['-DCOUNT_MODE']),('census-san',['-DCOUNT_MODE','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])]:
        run(['clang','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3','-Isrc','-Icompat','-Ivendor/redis',*extra,profile_source.relative_to(ROOT),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',BUILD/name],'build-'+name)
    build('night-rank-profile',extra=['-DNIGHT_RANK_PROFILE'])
    files=['src/zset_btree.c','src/zset_btree.h','bench/night-rank.c','bench/microbench.c','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','tests/upstream.c','Makefile',str(profile_source.relative_to(ROOT)),str((OUT/'night-rank-sampler.h').relative_to(ROOT)),str(Path(__file__).relative_to(ROOT))]
    save(OUT/'freeze.json',dict(prepared_utc=utc(),head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),host_metadata='../launch-manifest.json; launcher provenance; worker direct sysctl unavailable',checks=len(checks),checks_pass=True,fault_detected=True,files={p:sha(p) for p in files},binaries={str(p):sha(p) for p in BUILD.iterdir() if p.is_file()},compiler=subprocess.check_output(['clang','--version'],text=True)))
    print('prepared',len(checks),'checks and rank fault detected',flush=True)
def profile():
    p=OUT/'profile';p.mkdir(exist_ok=True)
    # One external attach attempt. Raw diagnostics may contain private process paths.
    if not (p/'external-profiler.json').exists():
        scratch=Path('scratch/m6-rank/external-sample');scratch.mkdir(exist_ok=True)
        with (scratch/'bench.csv').open('w') as f:
            child=subprocess.Popen([str(x) for x in args(BIN,n=100000,ops=30000000)],stdout=f,stderr=subprocess.PIPE,text=True)
            result=subprocess.run(['/usr/bin/sample',str(child.pid),'1','1','-file',str(scratch/'sample.txt')],capture_output=True,text=True,timeout=15)
            err=child.communicate(timeout=120)[1]
            (scratch/'sample.stdout').write_text(result.stdout);(scratch/'sample.stderr').write_text(result.stderr);(scratch/'bench.stderr').write_text(err)
            save(p/'external-profiler.json',dict(returncode=result.returncode,child_returncode=child.returncode,available=True,diagnostic_sha256=sha(scratch/'sample.stderr'),limitation='See ignored scratch/m6-rank/external-sample; external attach result recorded once. No permissions changed.'))
    run(['clang','-std=c11','-g','-O3','-Isrc','-Icompat','-Ivendor/redis',str((OUT/'sampler-calibration.c').relative_to(ROOT)),'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',BUILD/'sampler-calibration'],'build-sampler-calibration-attempt002')
    for i in range(2):run([BUILD/'sampler-calibration'],f'sampler-calibration-{i}','profile')
    for n in SIZES:
        run(args(BUILD/'night-rank-profile',n=n,ops=10000000),f'public-n{n}','profile')
        run([BUILD/'census',n,1],f'census-n{n}','profile')
        run([BUILD/'accumulation',n,5000000],f'accumulation-n{n}','profile')
    run([BUILD/'census-san',100000,1],'census-san-n100000','profile')
    for name in ['night-rank','night-rank-profile','accumulation']:
        r=run(['otool','-tvV',BUILD/name],name+'-assembly','profile')
        lines=r.stdout.splitlines();start=next(i for i,l in enumerate(lines) if l.strip()=='_zbtreeRank:')
        end=next(i for i in range(start+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':'))
        shutil.move(str(p/(name+'-assembly.stdout')),str(Path('scratch/m6-rank')/(name+'-assembly.txt')))
        (p/(name+'-zbtreeRank.asm')).write_text('\n'.join(lines[start:end])+'\n')
    print('profile captures complete',flush=True)
def measure(n,ops,seed,name,batches=3):
    r=run(args(BIN,n=n,ops=ops,seed=seed,batches=batches),name,'raw')
    rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==batches
    assert all(int(x['size'])==n and int(x['operations'])==ops and int(x['elapsed_ns'])>0 for x in rows)
    assert len({x['checksum'] for x in rows})==1 and len({x['tree_bytes'] for x in rows})==1
    return dict(name=name,size=n,ops=ops,seed=seed,windows_ns=[int(x['elapsed_ns']) for x in rows],ns_op=[int(x['elapsed_ns'])/ops for x in rows],checksum=rows[0]['checksum'],tree_bytes=int(rows[0]['tree_bytes']),csv='raw/'+name+'.stdout',sha256=sha(OUT/'raw'/(name+'.stdout')))
def calibrate():
    assert not (OUT/'calibration.json').exists()
    data=dict(started_utc=utc(),binary_sha256=sha(BIN),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),observations=[],fixed_ops={})
    for n in SIZES:
        for i in range(3):data['observations'].append(measure(n,1000000,1,f'cal-n{n}-{i}',1))
        fastest=min(r['ns_op'][0] for r in data['observations'] if r['size']==n)
        data['fixed_ops'][n]=min(100000000,math.ceil(50000000/fastest))
    data['finished_utc']=utc();save(OUT/'calibration.json',data);print(data['fixed_ops'],flush=True)
def qualify():
    assert not (OUT/'qualification.json').exists()
    cal=json.loads((OUT/'calibration.json').read_text());assert sha(BIN)==cal['binary_sha256']
    m=dict(status='running',started_utc=utc(),fixed_ops=cal['fixed_ops'],binary_sha256=sha(BIN),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),runs=[],results=[])
    total=0
    try:
        for block,seed in enumerate(SEEDS):
            ordered=SIZES[block%3:]+SIZES[:block%3]
            for n in ordered:
                for step,label in enumerate('ABBA'):
                    assert total<300
                    r=measure(n,int(cal['fixed_ops'][str(n)]),seed,f'b{block}-n{n}-s{step}-{label}')
                    r.update(block=block,step=step,label=label);m['runs'].append(r);total+=sum(r['windows_ns'])/1e9
                    save(OUT/'qualification.json',m)
                print(f'completed block {block+1} n{n}',flush=True)
        for n in SIZES:
            effects=[];windows=[];samples=[]
            for block in range(6):
                rs=[r for r in m['runs'] if r['size']==n and r['block']==block];assert len(rs)==4
                assert len({r['checksum'] for r in rs})==1 and len({r['tree_bytes'] for r in rs})==1
                a=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='A');b=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='B')
                effects.append(100*(b/a-1));windows.extend(w/1e6 for r in rs for w in r['windows_ns']);samples.extend(v for r in rs for v in r['ns_op'])
            m['results'].append(dict(size=n,effects_pct=effects,shortest_window_ms=min(windows),min_ns_op=min(samples),median_ns_op=statistics.median(samples),max_ns_op=max(samples),qualified=all(abs(e)<=1 for e in effects) and min(windows)>=10))
        m['status']='complete';print(json.dumps(m['results'],indent=2),flush=True)
    except BaseException as e:m['status']='failed';m['error']=repr(e);raise
    finally:m['finished_utc']=utc();m['timing_seconds']=total;save(OUT/'qualification.json',m)
if __name__=='__main__':globals()[sys.argv[1]]()
