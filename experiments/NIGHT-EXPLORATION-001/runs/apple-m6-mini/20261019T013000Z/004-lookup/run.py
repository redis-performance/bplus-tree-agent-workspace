#!/usr/bin/env python3
import csv, hashlib, io, json, math, statistics, subprocess, sys, time
from pathlib import Path
from datetime import datetime, timezone
OUT=Path(__file__).resolve().parent
REL=OUT.relative_to(Path.cwd())
BUILD=Path('scratch/m6-lookup/build')
SIZES=(100,1000,10000,100000,1000000)
CASES=('lookup-hit','lookup-miss')
def utc(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x): Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,name,folder='validation',expect=0,timeout=120):
    dest=OUT/folder;dest.mkdir(exist_ok=True);start=utc();t=time.monotonic()
    r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=timeout)
    (dest/(name+'.stdout')).write_text(r.stdout);(dest/(name+'.stderr')).write_text(r.stderr)
    with (OUT/'commands.jsonl').open('a') as f:
        f.write(json.dumps(dict(name=name,command=list(map(str,cmd)),started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder))+'\n')
    if expect is not None: assert r.returncode==expect,(name,r.returncode,r.stderr[:500])
    return r
def args(binary='lookup',n=100000,case='lookup-hit',ops=200000,seed=1,member=16):
    return [BUILD/binary,'--case',case,'--size',n,'--ops',ops,'--seed',seed,'--member-bytes',member]
def build(name,san=False,source='src/zset_btree.c',extra=(),bench=None):
    flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1' if san else '-O3']
    if san: flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
    run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis',*extra,bench or REL/'lookup-bench.c',source,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',BUILD/name],'build-'+name)
def prepare():
    records=[]
    for name,san in [('lookup',False),('lookup-san',True)]:
        build(name,san)
        for n in SIZES:
            for case in CASES:
                for seed in (1,2):
                    r=run(args(name,n,case,2003,seed),f'{name}-n{n}-{case}-s{seed}')
                    records.append(dict(binary=name,size=n,case=case,seed=seed,status='pass'))
        for member in (8,16,319,320,321,1024):
            for case in CASES:
                run(args(name,1000,case,2003,1,member),f'{name}-m{member}-{case}')
        for bad in ('all','bogus'):
            run(args(name,100,bad,2003),f'{name}-invalid-{bad}',expect=2)
    build('lookup-profile',extra=['-DLOOKUP_PROFILE'])
    build('lookup-counts',source='scratch/m6-lookup/instrumented.c',extra=['-DLOOKUP_COUNTS'])
    build('sampler-calibration',bench=REL/'../002-rank/sampler-calibration.c')
    save(OUT/'validation.json',dict(status='pass',size_seed_records=records,length_checks=24,invalid_checks=4,original_tests='Reuse launcher complete native/sanitizer validation, same source/referee hashes.'))
    files=['src/zset_btree.c','src/zset_btree.h','Makefile','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','tests/upstream.c','bench/microbench.c',str(REL/'lookup-bench.c'),str(REL/'run.py'),str(REL/'instrumentation.patch'),str(REL/'../002-rank/night-rank-sampler.h')]
    save(OUT/'freeze.json',dict(head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),prepared_utc=utc(),host_provenance='../launch-manifest.json; launcher-verified Apple M6; direct sysctl unavailable',compiler=subprocess.check_output(['clang','--version'],text=True).split('InstalledDir:')[0].strip(),files={f:sha(f) for f in files},binaries={str(p):sha(p) for p in BUILD.iterdir() if p.is_file()}))
    print('prepare PASS',flush=True)
def faults():
    src=Path('src/zset_btree.c').read_text()
    old='return zbtreeScoreRaw(zs, (unsigned char *)ele, sdslen(ele), score);'
    assert src.count(old)==1
    results=[]
    for name,body,case in [
        ('wrong-hit','int found=zbtreeScoreRaw(zs, (unsigned char *)ele, sdslen(ele), score); if(found && score) *score += 1; return found;','lookup-hit'),
        ('wrong-miss','int found=zbtreeScoreRaw(zs, (unsigned char *)ele, sdslen(ele), score); return found ? found : 1;','lookup-miss')]:
        path=Path('scratch/m6-lookup')/(name+'.c');path.write_text(src.replace(old,body))
        previous=[json.loads(l) for l in (OUT/'commands.jsonl').read_text().splitlines() if json.loads(l)['name']==name]
        if previous:
            code=previous[-1]['returncode'];err=(OUT/'validation'/(name+'.stderr')).read_text()
        else:
            build(name,source=path)
            r=run(args(name,1000,case,2003),name,expect=None);code=r.returncode;err=r.stderr
        expected='score == (double)query_order[i]' if name=='wrong-hit' else 'found == (c == 2 ? 0 : 1)'
        assert code!=0 and expected in err
        results.append(dict(fault=name,case=case,detected=True,returncode=code,source_sha256=sha(path)))
    save(OUT/'fault-controls.json',results)
    freeze=json.loads((OUT/'freeze.json').read_text());freeze['files'][str(REL/'run.py')]=sha(REL/'run.py');save(OUT/'freeze.json',freeze)
    print('faults PASS',flush=True)
def census():
    records=[]
    for n in (10000,100000,1000000):
        for case in CASES:
            for seed in (1,2):
                name=f'n{n}-{case}-s{seed}';r=run(args('lookup-counts',n,case,100000,seed),name,'census')
                counts=next(l for l in r.stderr.splitlines() if l.startswith('COUNTS,')).split(',')[1:]
                row=dict(zip(('leaf_calls','tag_candidates','full_comparisons','index_candidates','scan_calls','scan_bytes','scan_distance'),map(int,counts)))
                hist={int(l.split(',')[1]):int(l.split(',')[2]) for l in r.stderr.splitlines() if l.startswith('LEAF_SIZE,')}
                assert sum(hist.values())==row['leaf_calls']
                records.append(dict(size=n,case=case,seed=seed,queries=100000,**row,leaf_size_histogram=hist))
    save(OUT/'census.json',records);print('census PASS',flush=True)
def profile():
    records=[]
    for i in range(2):
        r=run([BUILD/'sampler-calibration'],f'calibration-{i}','profile')
        pcs=[l for l in r.stderr.splitlines() if l.startswith('PC,')]
        assert pcs and all('sampler_probe' in l for l in pcs)
    for n in (10000,100000,1000000):
        for case in CASES:
            name=f'n{n}-{case}';r=run(args('lookup-profile',n,case,10000000),name,'profile')
            counts={}
            for l in r.stderr.splitlines():
                if l.startswith('PC,'):
                    symbol=l.split(',')[4];counts[symbol]=counts.get(symbol,0)+1
            assert sum(counts.values())>=25
            raw=OUT/'profile'/(name+'.stderr');raw_hash=sha(raw)
            raw.rename(Path('scratch/m6-lookup')/(name+'-profile.txt'))
            save(OUT/'profile'/(name+'.json'),dict(samples=sum(counts.values()),symbols=counts,raw_sha256=raw_hash,raw_location='ignored scratch/m6-lookup/',requested_interval_us=1000,scope='public query loop only; sampled symbol PCs are not exact cost shares'))
            records.append(dict(size=n,case=case,samples=sum(counts.values()),symbols=counts,raw_sha256=raw_hash))
    r=run(['otool','-tvV',BUILD/'lookup'],'release-assembly','profile');lines=r.stdout.splitlines()
    for func in ('zbtScoreLeafFindMember','zbtreeScore'):
        a=next(i for i,l in enumerate(lines) if l.strip()=='_'+func+':')
        b=next((i for i in range(a+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':')),len(lines))
        (OUT/'profile'/(func+'.asm')).write_text('\n'.join(lines[a:b])+'\n')
    (OUT/'profile/release-assembly.stdout').rename(Path('scratch/m6-lookup/release-assembly.txt'))
    save(OUT/'profile-summary.json',records);print('profile PASS',flush=True)
def measure(n,case,ops,seed,name):
    r=run(args('lookup',n,case,ops,seed),name,'raw');rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==1
    row=rows[0];assert int(row['operations'])==ops and int(row['size'])==n
    return dict(name=name,size=n,case=case,ops=ops,seed=seed,elapsed_ns=int(row['elapsed_ns']),ns_op=int(row['elapsed_ns'])/ops,checksum=row['checksum'],tree_bytes=int(row['tree_bytes']),file='raw/'+name+'.stdout',sha256=sha(OUT/'raw'/(name+'.stdout')))
def calibrate():
    assert not (OUT/'calibration.json').exists();d=dict(started_utc=utc(),observations=[],fixed_ops={},binary_sha256=sha(BUILD/'lookup'),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()))
    for n in SIZES:
        for case in CASES:
            rows=[measure(n,case,200000,1,f'cal-n{n}-{case}-{i}') for i in range(3)];d['observations']+=rows
            d['fixed_ops'][f'{n}-{case}']=min(100000000,math.ceil(50000000/min(x['ns_op'] for x in rows)))
    d['finished_utc']=utc();save(OUT/'calibration.json',d);print('calibration PASS',flush=True)
def qualify():
    assert not (OUT/'qualification.json').exists();cal=json.loads((OUT/'calibration.json').read_text());assert sha(BUILD/'lookup')==cal['binary_sha256']
    d=dict(started_utc=utc(),runs=[],results=[],status='running');total=0
    try:
        for block,seed in enumerate((1,2,3,1,2,3)):
            for n in ((100000,1000000) if block%2==0 else (1000000,100000)):
                for step,label in enumerate('ABBA'):
                    assert total<300
                    row=measure(n,'lookup-hit',cal['fixed_ops'][f'{n}-lookup-hit'],seed,f'b{block}-n{n}-{step}-{label}')
                    row.update(block=block,step=step,label=label);d['runs'].append(row);total+=row['elapsed_ns']/1e9;save(OUT/'qualification.json',d)
            print('block',block+1,flush=True)
        for n in (100000,1000000):
            effects=[]
            for block in range(6):
                rs=[r for r in d['runs'] if r['size']==n and r['block']==block];assert len(rs)==4 and len({r['checksum'] for r in rs})==1 and len({r['tree_bytes'] for r in rs})==1
                effects.append(100*(statistics.mean(r['ns_op'] for r in rs if r['label']=='B')/statistics.mean(r['ns_op'] for r in rs if r['label']=='A')-1))
            shortest=min(r['elapsed_ns'] for r in d['runs'] if r['size']==n)/1e6
            d['results'].append(dict(size=n,effects_pct=effects,shortest_ms=shortest,qualified=max(map(abs,effects))<=1 and shortest>=10))
        d['status']='complete'
    finally:
        d['finished_utc']=utc();d['timing_seconds']=total;save(OUT/'qualification.json',d)
    print(json.dumps(d['results']),flush=True)
if __name__=='__main__': globals()[sys.argv[1]]()
