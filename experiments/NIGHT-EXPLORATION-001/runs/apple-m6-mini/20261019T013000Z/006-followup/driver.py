#!/usr/bin/env python3
"""Frozen serial orchestration for M6-LOOKUP-CALLER-001. No automatic retries."""
import sys
sys.dont_write_bytecode=True
import csv,hashlib,io,json,math,os,statistics,subprocess,time
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path.cwd(); OUT=Path(__file__).resolve().parent; BUILD=ROOT/'scratch/m6-caller/build'
PLAN=json.loads((OUT/'PLAN.json').read_text()); CELLS=PLAN['cells']; BYID={c['id']:c for c in CELLS}
SOURCES={'0':ROOT/'worktrees/m6-caller-control',**{v:ROOT/f'worktrees/m6-caller-{v}' for v in 'ABC'}}
DEADLINE=datetime.fromisoformat(PLAN['deadline_utc']).timestamp()
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def clean(s):return s.replace(str(ROOT),'<workspace>')
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def command(cmd,name,folder='validation',expect=0,timeout=120):
    assert time.time()<DEADLINE,'experiment deadline'
    dest=OUT/folder;dest.mkdir(parents=True,exist_ok=True)
    assert not (dest/(name+'.stdout')).exists(),('no retry',name)
    start=utc();t=time.monotonic()
    timeout=max(0.001,min(timeout,DEADLINE-time.time()))
    try:r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=timeout)
    except subprocess.TimeoutExpired as e:
        def decoded(x):return x.decode(errors='replace') if isinstance(x,bytes) else x or ''
        (dest/(name+'.stdout')).write_text(clean(decoded(e.stdout)))
        (dest/(name+'.stderr')).write_text(clean(decoded(e.stderr))+'\nTIMEOUT '+clean(str(e))+'\n')
        with (OUT/'driver-commands.jsonl').open('a') as f:
            f.write(json.dumps(dict(name=name,command=[clean(str(a)) for a in cmd],start_utc=start,finish_utc=utc(),wall_seconds=time.monotonic()-t,returncode=None,timeout_seconds=timeout,folder=folder))+'\n')
        raise
    (dest/(name+'.stdout')).write_text(clean(r.stdout));(dest/(name+'.stderr')).write_text(clean(r.stderr))
    rec=dict(name=name,command=[clean(str(a)) for a in cmd],start_utc=start,finish_utc=utc(),wall_seconds=time.monotonic()-t,returncode=r.returncode,folder=folder)
    with (OUT/'driver-commands.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
    if expect is not None:assert r.returncode==expect,(name,r.returncode,clean(r.stderr[-1000:]))
    return r

def build():
    assert not (OUT/'build.json').exists()
    records=[];BUILD.mkdir(parents=True,exist_ok=True)
    for variant,tree in SOURCES.items():
        assert sha(tree/'src/zset_btree.h')==sha(ROOT/'src/zset_btree.h')
        for referee in ('standard','lookup','batch','update'):
            source=OUT/'referees'/f'{referee}.c'
            for san in (False,True):
                name=f'{variant}-{referee}'+('-san' if san else '')
                flags=['-ffile-prefix-map='+str(tree)+'=<source>','-fdebug-prefix-map='+str(tree)+'=<source>','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-O1' if san else '-O3']
                if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
                command(['clang',*flags,'-I'+str(tree/'src'),'-I'+str(tree/'compat'),'-I'+str(tree/'vendor/redis'),source,tree/'src/zset_btree.c',tree/'compat/standalone.c',tree/'vendor/redis/siphash.c','-lm','-o',BUILD/name],'build-'+name)
                records.append(dict(binary=name,sha256=sha(BUILD/name),variant=variant,referee=referee,sanitized=san,flags=[clean(f) for f in flags],source_sha256=sha(tree/'src/zset_btree.c')))
    save(OUT/'build.json',dict(finished_utc=utc(),binaries=records))

def args(variant,cell,ops,seed,replicas=1,san=False):
    ref=cell['referee'];cmd=[BUILD/(f'{variant}-{ref}'+('-san' if san else '')),'--case',cell['case'],'--size',cell['size'],'--ops',ops,'--seed',seed]
    if ref!='update':cmd+=['--member-bytes',cell['member_bytes']]
    if ref=='standard':cmd+=['--replicas',replicas]
    if ref=='batch':cmd+=['--batch-size',cell['batch'],'--query-seed',seed+1000]
    return cmd

def measure(variant,cell,ops,seed,name,folder,replicas=1,san=False,timeout=120):
    r=command(args(variant,cell,ops,seed,replicas,san),name,folder,timeout=timeout)
    rows=list(csv.DictReader(io.StringIO(r.stdout)));assert len(rows)==1,(name,rows)
    row=rows[0];actual=int(row.get('operations',row.get('ops',0)));elapsed=int(row['elapsed_ns'])
    assert actual>0 and elapsed>0 and int(row['size'])==cell['size'],(name,row)
    assert row['case']==cell['case'],(name,row)
    assert int(row['seed'])==seed,(name,row)
    if 'member_bytes' in row:assert int(row['member_bytes'])==cell['member_bytes'],(name,row)
    if 'requested_ops' in row:assert int(row['requested_ops'])==ops,(name,row)
    ref=cell['referee'];case=cell['case'];n=cell['size']
    if ref=='standard' and case in ('insert','delete'):
        assert int(row['replicas'])==replicas and actual==n*replicas and int(row['total_operations'])==actual,(name,row)
    elif ref=='standard' and case=='iterate':assert actual==math.ceil(ops/n)*n,(name,row)
    elif ref=='standard' and case=='scan':
        assert int(row['traversals'])==math.ceil(ops/n) and actual>=math.ceil(ops/n)*n,(name,row)
    else:assert actual==ops,(name,row)
    if ref=='batch':
        assert int(row['batch_size'])==cell['batch'] and int(row['query_seed'])==seed+1000,(name,row)
        assert int(row['api_calls'])==math.ceil(ops/cell['batch']),(name,row)
    return dict(name=name,variant=variant,cell=cell['id'],requested_ops=ops,operations=actual,seed=seed,replicas=replicas,elapsed_ns=elapsed,ns_op=elapsed/actual,checksum=row['checksum'],tree_bytes=float(row.get('mean_tree_bytes',row['tree_bytes'])),csv=row,file=folder+'/'+name+'.stdout',sha256=sha(OUT/folder/(name+'.stdout')))

def validate():
    assert not (OUT/'validation.json').exists();runs=[]
    # Every operation family, query mode, boundary length and batch size; original
    # full correctness/score-oracle matrices are retained separately per variant.
    selected=[]
    for ref in ('standard','lookup','batch','update'):
        seen=set()
        for c in CELLS:
            if c['referee']!=ref:continue
            key=(c['case'],c['member_bytes'],c['batch'])
            if key not in seen:
                seen.add(key);d=dict(c);d['size']=100;selected.append(d)
    for variant in SOURCES:
        for san in (False,True):
            for i,c in enumerate(selected):
                row=measure(variant,c,203,11,f'{variant}-san{int(san)}-{i}','validation',san=san);runs.append(row)
            for op in ('insert','delete'):
                c=next(c for c in CELLS if c['referee']=='standard' and c['case']==op and c['size']==100)
                runs.append(measure(variant,c,203,11,f'{variant}-san{int(san)}-{op}-replicas3','validation',replicas=3,san=san))
    for i in range(len(runs)//4):
        group=[runs[i+j*(len(runs)//4)] for j in range(4)]
        assert len({(r['cell'],r['seed'],r['operations'],r['checksum']) for r in group})==1,('cross-source semantic mismatch',group)
    save(OUT/'validation.json',dict(status='pass',finished_utc=utc(),runs=runs,scope='common frontend semantic checks plus separately sealed full variant tests/oracles'))

def freeze():
    assert not (OUT/'freeze.json').exists()
    assert json.loads((OUT/'validation.json').read_text())['status']=='pass'
    files=[OUT/'driver.py',OUT/'PLAN.json',*sorted((OUT/'referees').glob('*.c'))]
    files += [tree/p for tree in SOURCES.values() for p in ('src/zset_btree.c','src/zset_btree.h','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','bench/microbench.c','tests/upstream.c')]
    save(OUT/'freeze.json',dict(frozen_utc=utc(),files={str(p.relative_to(ROOT)):sha(p) for p in files},binaries={str(p.relative_to(ROOT)):sha(p) for p in BUILD.iterdir() if p.is_file()},compiler=clean(subprocess.check_output(['clang','--version'],text=True)),source_commit=PLAN['source_commit'],host='launcher-verified Apple M6; host-specific results only'))

def verify():
    d=json.loads((OUT/'freeze.json').read_text())
    for p,h in {**d['files'],**d['binaries']}.items():assert sha(ROOT/p)==h,('freeze changed',p)

def calibrate():
    verify();assert not (OUT/'calibration.json').exists()
    d=dict(started_utc=utc(),status='running',observations=[],fixed={})
    try:
        for i,c in enumerate(CELLS):
            rs=[measure('0',c,200000,1,f'cal-{i}-{j}','calibration') for j in range(3)];d['observations']+=rs
            fastest=min(r['ns_op'] for r in rs);ops=min(100000000,math.ceil(100000000/fastest));replicas=1;cap=False
            if c['referee']=='standard' and c['case'] in ('insert','delete'):
                per_tree=max(float(r['csv'].get('estimated_working_set_tree_bytes',r['tree_bytes'])) for r in rs)
                limit=max(1,min(4096,int(64*1024*1024/per_tree)))
                desired=math.ceil(100000000/(fastest*c['size']));replicas=min(limit,desired);cap=desired>limit;ops=c['size']
            d['fixed'][c['id']]=dict(ops=ops,replicas=replicas,capped=cap or ops==100000000,target_ms=100,calibrated_ns_op=fastest)
            save(OUT/'calibration.json',d);print('calibrated',i+1,'/',len(CELLS),c['id'],flush=True)
        d['status']='complete'
    finally:d['finished_utc']=utc();save(OUT/'calibration.json',d)

def results(runs,cells,aa=False):
    out=[]
    for c in cells:
        rs=[r for r in runs if r['cell']==c['id']];effects=[];memory=[]
        for block in range(6):
            blockrows=[r for r in rs if r['block']==block];assert len(blockrows)==4
            assert len({r['checksum'] for r in blockrows})==1,('checksum differs',c['id'],block)
            assert len({r['operations'] for r in blockrows})==1
            a=[r for r in blockrows if r['label']=='A'];b=[r for r in blockrows if r['label']=='B']
            effects.append(100*(statistics.mean(r['ns_op'] for r in b)/statistics.mean(r['ns_op'] for r in a)-1))
            memory.append(100*(statistics.mean(r['tree_bytes'] for r in b)/statistics.mean(r['tree_bytes'] for r in a)-1))
        shortest=min(r['elapsed_ns'] for r in rs)/1e6
        out.append(dict(cell=c['id'],effects_pct=effects,median_pct=statistics.median(effects),memory_pct=memory,shortest_ms=shortest,qualified=(max(map(abs,effects))<=1 and shortest>=10) if aa else None,primary_pass=max(effects)<=-2 and shortest>=10,memory_pass=max(memory)<=1,guard_pass=max(effects)<=1 and shortest>=10,consistent_regression=min(effects)>1))
    return out

def phase(kind,variant='0'):
    verify();cal=json.loads((OUT/'calibration.json').read_text());assert cal['status']=='complete'
    name=kind+('' if kind=='aa' else '-'+variant);path=OUT/(name+'.json');assert not path.exists(),('no retry',path)
    cells=[BYID[x] for x in PLAN['primaries']] if kind=='screen' else CELLS
    seeds=PLAN['confirmation_seeds'] if kind=='confirm' else PLAN['discovery_seeds']
    prior=0;prior_wall=0
    if kind=='guards':
        for v in 'ABC':prior+=json.loads((OUT/f'screen-{v}.json').read_text())['timing_seconds']
        prior_wall=json.loads((OUT/'screen-A.json').read_text())['phase_wall_seconds']
    d=dict(kind=kind,variant=variant,status='running',started_utc=utc(),runs=[],results=[],timing_seconds=0,earlier_primary_screen_seconds=prior,earlier_primary_screen_wall_seconds=prior_wall);start=time.monotonic()
    save(path,d)
    try:
        for block,seed in enumerate(seeds):
            rotation=block%len(cells);order=cells[rotation:]+cells[:rotation]
            if block%2:order=list(reversed(order))
            for i,c in enumerate(order):
                cfg=cal['fixed'][c['id']]
                for step,label in enumerate('ABBA'):
                    assert time.monotonic()-start+prior_wall<900,'phase wall budget'
                    assert d['timing_seconds']+prior<300,'phase timed budget'
                    v='0' if kind=='aa' or label=='A' else variant
                    row=measure(v,c,cfg['ops'],seed,f'{name}-b{block}-c{CELLS.index(c)}-p{step}-{label}','raw',cfg['replicas'],timeout=min(120,900-prior_wall-(time.monotonic()-start)));row.update(block=block,step=step,label=label)
                    d['runs'].append(row);d['timing_seconds']+=row['elapsed_ns']/1e9
                    with (OUT/(name+'-runs.jsonl')).open('a') as f:f.write(json.dumps(row)+'\n')
                    assert d['timing_seconds']+prior<=300,'phase timed budget exceeded by child'
                    assert time.monotonic()-start+prior_wall<=900,'phase wall budget exceeded by child'
                    assert time.time()<=DEADLINE,'experiment deadline exceeded by child'
                save(path,d)
            print(name,'block',block+1,'/',6,'rows',len(d['runs']),'timed',round(d['timing_seconds'],2),'wall',round(time.monotonic()-start,2),flush=True)
        d['results']=results(d['runs'],cells,kind=='aa');d['status']='complete'
    except BaseException as e:d['status']='incomplete';d['failure']=str(e);raise
    finally:d['finished_utc']=utc();d['wall_seconds']=time.monotonic()-start;save(path,d)
    print(json.dumps(d['results']),flush=True)

def screens():
    verify();cal=json.loads((OUT/'calibration.json').read_text());assert cal['status']=='complete'
    cells=[BYID[x] for x in PLAN['primaries']];start=time.monotonic();total=0;records={}
    for v in 'ABC':
        assert not (OUT/f'screen-{v}.json').exists(),'no screen retry'
        records[v]=dict(kind='screen',variant=v,status='running',started_utc=utc(),runs=[],results=[],timing_seconds=0,schedule='three variants rotate by block within single serial phase')
        save(OUT/f'screen-{v}.json',records[v])
    try:
        for block,seed in enumerate(PLAN['discovery_seeds']):
            order='ABC'[block%3:]+'ABC'[:block%3]
            for v in order:
                d=records[v]
                for c in cells if block%2==0 else list(reversed(cells)):
                    cfg=cal['fixed'][c['id']]
                    for step,label in enumerate('ABBA'):
                        assert total<300 and time.monotonic()-start<900,'screen phase budget'
                        row=measure('0' if label=='A' else v,c,cfg['ops'],seed,f'screen-{v}-b{block}-c{CELLS.index(c)}-p{step}-{label}','raw',cfg['replicas'],timeout=min(120,900-(time.monotonic()-start)))
                        row.update(block=block,step=step,label=label);d['runs'].append(row);elapsed=row['elapsed_ns']/1e9;d['timing_seconds']+=elapsed;total+=elapsed
                        with (OUT/f'screen-{v}-runs.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
                        assert total<=300 and time.monotonic()-start<=900 and time.time()<=DEADLINE,'screen child exceeded budget/deadline'
                    save(OUT/f'screen-{v}.json',d)
            print('primary screens block',block+1,'/6 total seconds',round(total,2),flush=True)
        for d in records.values():d['results']=results(d['runs'],cells);d['status']='complete'
    except BaseException as e:
        for d in records.values():d['status']='incomplete';d['failure']=str(e)
        raise
    finally:
        for v,d in records.items():d['finished_utc']=utc();d['phase_wall_seconds']=time.monotonic()-start;save(OUT/f'screen-{v}.json',d)
    print(json.dumps({v:d['results'] for v,d in records.items()}),flush=True)

if __name__=='__main__':
    action=sys.argv[1]
    if action in ('build','validate','freeze','calibrate','screens'):globals()[action]()
    else:
        assert action!='screen','use screens for per-block variant rotation'
        phase(action,sys.argv[2] if len(sys.argv)>2 else '0')
