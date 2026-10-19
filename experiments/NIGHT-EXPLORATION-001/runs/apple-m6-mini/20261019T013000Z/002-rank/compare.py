#!/usr/bin/env python3
"""Serial validation and single preregistered exploratory rank comparison."""
import csv,hashlib,io,json,os,statistics,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent
SNAP=Path('scratch/m6-rank/variants');BASE=Path('scratch/m6-rank/build/night-rank')
SIZES=(10000,100000,1000000);IDS=('A','B','C');DEADLINE='2026-10-19T02:03:00+00:00'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):Path(p).write_text(json.dumps(d,indent=2)+'\n')
def run(cmd,name,folder='candidate-validation',cwd=None,timeout=120):
    assert utc()<DEADLINE
    p=OUT/folder;p.mkdir(exist_ok=True);start=utc();t=time.monotonic()
    r=subprocess.run([str(x) for x in cmd],cwd=cwd,capture_output=True,text=True,timeout=timeout)
    (p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
    with (OUT/'candidate-commands.jsonl').open('a') as f:f.write(json.dumps(dict(name=name,command=[str(x) for x in cmd],cwd=str(cwd or '.'),started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder))+'\n')
    assert r.returncode==0,(name,r.returncode,r.stderr[:500]);return r

def validate():
    assert not (OUT/'candidate-validation.json').exists()
    m=dict(started_utc=utc(),status='running',variants={},baseline_binary_sha256=sha(BASE))
    manifest=json.loads((OUT/'implementation-manifest.json').read_text())
    for ident in IDS:
        dst=SNAP/ident
        assert all(sha(dst/f)==h for f,h in manifest['variants'][ident]['files'].items())
        (dst/'build').mkdir(exist_ok=True)
        commands=[]
        for san in [False,True]:
            suffix='-san' if san else ''
            flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
            if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
            common=['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis']
            sources=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
            run([*common,'bench/night-rank.c',*sources,'-o','build/rank'+suffix],f'{ident}-build-rank'+suffix,cwd=dst)
            run([*common,'-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c',*sources,'-o','build/test'+suffix],f'{ident}-build-upstream'+suffix,cwd=dst)
            run(['build/test'+suffix],f'{ident}-upstream'+suffix,cwd=dst)
            for n in [100,1000,10000,100000,1000000]:
                for layout in (['integer','ties','finite'] if n<=100000 else ['integer']):
                    name=f'{ident}{suffix}-n{n}-{layout}'
                    run(['build/rank'+suffix,'--size',n,'--ops',2003,'--layout',layout],name,cwd=dst);commands.append(name)
            for mode in ['reverse','score','miss']:
                for layout in ['ties','finite']:
                    name=f'{ident}{suffix}-{mode}-{layout}-long'
                    run(['build/rank'+suffix,'--size',1000,'--ops',2003,'--member-bytes',1024,'--mode',mode,'--layout',layout],name,cwd=dst);commands.append(name)
        m['variants'][ident]=dict(correctness='pass',targeted_checks=len(commands),source_sha256=sha(dst/'src/zset_btree.c'),binary_sha256=sha(dst/'build/rank'),sanitizer_binary_sha256=sha(dst/'build/rank-san'),upstream_native_and_sanitizer='pass',patch_sha256=sha(OUT/'variants'/ident/'candidate.patch'))
        save(OUT/'candidate-validation.json',m);print('validated',ident,len(commands),flush=True)
    assert sha(BASE)==m['baseline_binary_sha256'];m['status']='complete';m['finished_utc']=utc();save(OUT/'candidate-validation.json',m)
def measure(binary,n,ops,seed,name):
    r=run([binary,'--size',n,'--ops',ops,'--seed',seed,'--batches',3],name,'discovery')
    rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==3
    assert all(int(x['size'])==n and int(x['operations'])==ops and int(x['elapsed_ns'])>0 for x in rows)
    assert len({x['checksum'] for x in rows})==1 and len({x['tree_bytes'] for x in rows})==1
    return dict(name=name,size=n,ops=ops,seed=seed,windows_ns=[int(x['elapsed_ns']) for x in rows],ns_op=[int(x['elapsed_ns'])/ops for x in rows],checksum=rows[0]['checksum'],tree_bytes=int(rows[0]['tree_bytes']),csv='discovery/'+name+'.stdout',sha256=sha(OUT/'discovery'/(name+'.stdout')))
def discover():
    assert not (OUT/'discovery.json').exists()
    valid=json.loads((OUT/'candidate-validation.json').read_text());assert valid['status']=='complete'
    cal=json.loads((OUT/'calibration.json').read_text());assert sha(BASE)==cal['binary_sha256']==valid['baseline_binary_sha256']
    for ident in IDS:assert sha(SNAP/ident/'build/rank')==valid['variants'][ident]['binary_sha256']
    m=dict(status='running',started_utc=utc(),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),baseline_binary_sha256=sha(BASE),fixed_ops=cal['fixed_ops'],runs=[],results=[],interpretation='Exploratory only; controls fail; cannot accept from reduced guard screen.')
    total=0
    try:
        for block,seed in enumerate([1,2,3,1,2,3]):
            variants=IDS[block%3:]+IDS[:block%3];sizes=SIZES[block%3:]+SIZES[:block%3]
            for ident in variants:
                for n in sizes:
                    for step,label in enumerate('ABBA'):
                        assert total<300
                        binary=BASE if label=='A' else SNAP/ident/'build/rank'
                        r=measure(binary,n,int(cal['fixed_ops'][str(n)]),seed,f'{ident}-b{block}-n{n}-s{step}-{label}')
                        r.update(variant=ident,block=block,step=step,label=label);m['runs'].append(r);total+=sum(r['windows_ns'])/1e9
                        save(OUT/'discovery.json',m)
                    print(f'{ident} block{block+1}/6 n{n}',flush=True)
        for ident in IDS:
            for n in SIZES:
                effects=[];memory=[];windows=[]
                for block in range(6):
                    rs=[r for r in m['runs'] if r['variant']==ident and r['size']==n and r['block']==block];assert len(rs)==4
                    assert len({r['checksum'] for r in rs})==1
                    a=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='A');b=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='B')
                    ma=statistics.mean(r['tree_bytes'] for r in rs if r['label']=='A');mb=statistics.mean(r['tree_bytes'] for r in rs if r['label']=='B')
                    effects.append(100*(b/a-1));memory.append(100*(mb/ma-1));windows.extend(w/1e6 for r in rs for w in r['windows_ns'])
                m['results'].append(dict(variant=ident,size=n,effects_pct=effects,min_effect_pct=min(effects),median_effect_pct=statistics.median(effects),max_effect_pct=max(effects),max_memory_effect_pct=max(memory),shortest_window_ms=min(windows)))
        m['status']='complete';print(json.dumps(m['results'],indent=2),flush=True)
    except BaseException as e:m['status']='failed';m['error']=repr(e);raise
    finally:m['timing_seconds']=total;m['finished_utc']=utc();save(OUT/'discovery.json',m)
if __name__=='__main__':globals()[sys.argv[1]]()
