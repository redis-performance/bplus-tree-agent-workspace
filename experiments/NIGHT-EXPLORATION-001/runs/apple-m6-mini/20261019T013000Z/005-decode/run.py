#!/usr/bin/env python3
"""Serial M6 DECODE-001 preparation and fixed comparisons. Run from repository root."""
import csv,difflib,hashlib,io,json,math,os,statistics,subprocess,sys,time
from pathlib import Path
from datetime import datetime,timezone
E=Path(__file__).resolve().parent; R=Path.cwd(); REL=E.relative_to(R); S=Path('scratch/m6-decode')
WIDTHS=(0,8,31,57,58,59,60,61,62,63,64); COUNTS=(1,2,4,7,8,16,32,96)
CELLS=[(w,r,c) for w in WIDTHS for r in (0,1) for c in COUNTS]
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,name,folder='validation',timeout=120,expect=0):
    (E/folder).mkdir(exist_ok=True); start=utc();t=time.monotonic()
    q=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,timeout=timeout)
    out=q.stdout.replace(str(R),'<workspace>');err=q.stderr.replace(str(R),'<workspace>')
    (E/folder/(name+'.stdout')).write_text(out);(E/folder/(name+'.stderr')).write_text(err)
    with (E/'commands.jsonl').open('a') as f:f.write(json.dumps(dict(command=[str(x).replace(str(R),'<workspace>') for x in cmd],name=name,folder=folder,started_utc=start,finished_utc=utc(),wall_seconds=time.monotonic()-t,returncode=q.returncode))+'\n')
    if expect is not None:assert q.returncode==expect,(name,q.returncode,err[:1000])
    return q

def source(v):
    root=Path('src/zset_btree.c').read_text();bulk=Path('experiments/EXP-008/referee/bulk.inc').read_text()
    policy=(E/('profile-control.inc' if v=='base' else f'variants/{v}/policy.inc')).read_text()
    return root+'\n'+bulk+'\n'+policy

def build(v='base',san=False,prof=False):
    mode='sanitize' if san else ('profile' if prof else 'release'); dest=S/'build'/mode/v;dest.mkdir(parents=True,exist_ok=True)
    wt=S/'variants'/v/'src';wt.mkdir(parents=True,exist_ok=True)
    target=wt/'zset_btree.c'; text=source(v);target.write_text(text);(wt/'zset_btree.h').write_bytes(Path('src/zset_btree.h').read_bytes())
    flags=['-std=c11','-O1' if san else '-O3','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench',f'-ffile-prefix-map={R}=.']
    if san:flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
    if prof:flags+=['-DDECODE_PROFILE']
    flags+=['-DDECODER_TREE_SOURCE="'+os.path.relpath(target.resolve(),E)+'"']
    cmd=['clang',*flags,REL/'driver.c',REL/'kernel.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',dest/'decoder-bench']
    run(cmd,f'build-{mode}-{v}')
    if not san:run(['clang',*flags,'-S',REL/'kernel.c','-o',dest/'kernel.s'],f'assembly-{mode}-{v}')
    if v!='base':
        patch=''.join(difflib.unified_diff(source('base').splitlines(True),text.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'))
        (E/f'variants/{v}/candidate.patch').write_text(patch)
    ident=dict(mode=mode,variant=v,source_sha256=sha(target),binary=str(dest/'decoder-bench'),binary_sha256=sha(dest/'decoder-bench'),kernel_assembly_sha256=sha(dest/'kernel.s') if not san else None)
    save(E/f'build-{mode}-{v}.json',ident);return ident

def args(v='base',cell=(60,0,1),rounds=10000,seed=1,mode='release'):
    w,r,c=cell
    return [S/'build'/mode/v/'decoder-bench','--width',w,'--reversed',r,'--count',c,'--leaves',8,'--samples',1,'--warmup',1,'--rounds',rounds,'--seed',seed]
def observe(v,cell,rounds,seed,name,folder='raw',mode='release'):
    q=run(args(v,cell,rounds,seed,mode),name,folder);rs=list(csv.DictReader(io.StringIO(q.stdout)));assert len(rs)==1
    x=rs[0];assert int(x['operations'])==rounds*8*cell[2]
    return dict(name=name,variant=v,cell=list(cell),rounds=rounds,seed=seed,operations=int(x['operations']),elapsed_ns=float(x['elapsed_ns']),ns_op=float(x['ns_per_decode']),checksum=x['checksum'],fixture_hash=x['fixture_hash'],leaf_bytes=int(x['leaf_bytes']),file=f'{folder}/{name}.stdout',sha256=sha(E/folder/(name+'.stdout')))

def prepare():
    launch=json.loads((E.parent/'launch-manifest.json').read_text()); assert all(sha(p)==h for p,h in launch['source_hashes'].items())
    build(); build(san=True); build(prof=True)
    for mode in ('release','sanitize'):
        run(['python3','tests/test_decoder.py',S/'build'/mode/'base/decoder-bench'],f'base-{mode}-existing-oracle')
        run([S/'build'/mode/'base/decoder-bench','--extended-test'],f'base-{mode}-extended')
    save(E/'preflight.json',dict(utc=utc(),head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),cpu='Apple M6',provenance='../launch-manifest.json; launcher verified; worker direct sysctl denied previously and not retried',launch_hashes=launch['source_hashes'],compiler=subprocess.check_output(['clang','--version'],text=True).split('InstalledDir:')[0].strip(),bulk_sha256=sha('experiments/EXP-008/referee/bulk.inc'),copied_sources=True,worktree_denial='Previously recorded; not retried',model='Codex, GPT-6 family visible; exact serving backend/model unknown',cost='unknown'))
    print('prepare PASS',flush=True)

def profile(v='base'):
    if v!='base':build(v,prof=True)
    records=[]
    for c in (1,96):
      for rev in (0,1):
        cell=(60,rev,c);rounds=6000000 if c==1 else 100000
        name=f'{v}-w60-r{rev}-c{c}'
        observe(v,cell,rounds,1,name,'profile','profile')
        raw=E/'profile'/(name+'.stderr');counts={}
        for l in raw.read_text().splitlines():
            if l.startswith('PC,'):
                symbol=l.split(',')[4];counts[symbol]=counts.get(symbol,0)+1
        records.append(dict(variant=v,cell=cell,samples=sum(counts.values()),sufficient=sum(counts.values())>=25,symbols=counts,raw_sha256=sha(raw),scope='measurement loop bracket; signals include timer/checksum, no cost shares or PMU counters'))
        raw.rename(S/(name+'-profile.txt'))
    q=run(['otool','-tvV',S/'build/release'/v/'decoder-bench'],v+'-release-assembly','profile')
    lines=q.stdout.splitlines()
    for func in ('decoder_batch','zbtScoreLeafDecodeRange'):
        hits=[i for i,l in enumerate(lines) if l.strip()=='_'+func+':']
        if not hits:continue
        a=hits[0];b=next((i for i in range(a+1,len(lines)) if lines[i].startswith('_') and lines[i].endswith(':')),len(lines))
        (E/'profile'/(v+'-'+func+'.asm')).write_text('\n'.join(lines[a:b])+'\n')
    (E/'profile'/(v+'-release-assembly.stdout')).rename(S/(v+'-release-assembly.txt'))
    save(E/f'profile-{v}.json',records);print(json.dumps(records),flush=True)

def calibrate():
    assert not (E/'calibration.json').exists();d=dict(started_utc=utc(),observations=[],fixed_rounds={},binary_sha256=sha(S/'build/release/base/decoder-bench'))
    for i,cell in enumerate(CELLS):
        rows=[observe('base',cell,10000,1,f'cal-{i}-{j}','calibration') for j in range(3)];d['observations']+=rows
        n=min(100000000//(8*cell[2]),math.ceil(50000000/min(x['elapsed_ns']/10000 for x in rows)))
        d['fixed_rounds']['-'.join(map(str,cell))]=n
    d['finished_utc']=utc();save(E/'calibration.json',d);print('calibration PASS',flush=True)

def compare(v):
    phase='aa' if v=='base' else v;out=E/f'comparison-{phase}.json';assert not out.exists()
    cal=json.loads((E/'calibration.json').read_text());assert sha(S/'build/release/base/decoder-bench')==cal['binary_sha256']
    d=dict(phase=phase,started_utc=utc(),publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),runs=[],results=[],status='running');t=time.monotonic()
    try:
      for block,seed in enumerate((1,2,3,1,2,3)):
        cells=CELLS[block:]+CELLS[:block]
        if block%2:cells=list(reversed(cells))
        for cell in cells:
          rounds=cal['fixed_rounds']['-'.join(map(str,cell))]
          for step,label in enumerate('ABBA'):
            assert time.monotonic()-t<300,'phase budget exhausted'
            assert datetime.now(timezone.utc)<datetime(2026,10,19,3,6,30,tzinfo=timezone.utc),'round cleanup cutoff'
            variant='base' if label=='A' else v
            name=f'{phase}-b{block}-w{cell[0]}-r{cell[1]}-c{cell[2]}-{step}{label}'
            row=observe(variant,cell,rounds,seed,name);row.update(block=block,step=step,label=label);d['runs'].append(row)
        save(out,d);print(phase,'block',block+1,round(time.monotonic()-t,2),flush=True)
      for cell in CELLS:
        effects=[];rs=[r for r in d['runs'] if r['cell']==list(cell)]
        for block in range(6):
            rr=[r for r in rs if r['block']==block];assert len(rr)==4 and len({r['checksum'] for r in rr})==1 and len({r['fixture_hash'] for r in rr})==1 and len({r['leaf_bytes'] for r in rr})==1
            effects.append(100*(statistics.mean(r['ns_op'] for r in rr if r['label']=='B')/statistics.mean(r['ns_op'] for r in rr if r['label']=='A')-1))
        d['results'].append(dict(cell=cell,effects_pct=effects,median_pct=statistics.median(effects),min_pct=min(effects),max_pct=max(effects),shortest_ms=min(r['elapsed_ns'] for r in rs)/1e6,qualified=max(map(abs,effects))<=1 and min(r['elapsed_ns'] for r in rs)>=10000000,baseline_ns_op=dict(min=min(r['ns_op'] for r in rs if r['label']=='A'),median=statistics.median(r['ns_op'] for r in rs if r['label']=='A'),max=max(r['ns_op'] for r in rs if r['label']=='A')),candidate_ns_op=dict(min=min(r['ns_op'] for r in rs if r['label']=='B'),median=statistics.median(r['ns_op'] for r in rs if r['label']=='B'),max=max(r['ns_op'] for r in rs if r['label']=='B'))))
      d['status']='complete'
    finally:d['finished_utc']=utc();d['wall_seconds']=time.monotonic()-t;save(out,d)
    print(phase,'COMPLETE',d['wall_seconds'],flush=True)

def candidates():
    records=[]
    for v in ('A','B','C'):
        records.append(build(v));records.append(build(v,san=True))
        for mode in ('release','sanitize'):
            run(['python3','tests/test_decoder.py',S/'build'/mode/v/'decoder-bench'],f'{v}-{mode}-existing-oracle')
            run([S/'build'/mode/v/'decoder-bench','--extended-test'],f'{v}-{mode}-extended')
    save(E/'candidate-validation.json',dict(status='pass',builds=records,oracle='unchanged tests/test_decoder.py plus 2080-cell extended fixture suite per build; partial/empty/canary exact-bit checks inside decoder_validate'))
    print('candidate validation PASS',flush=True)
if __name__=='__main__':globals()[sys.argv[1]](*sys.argv[2:])
