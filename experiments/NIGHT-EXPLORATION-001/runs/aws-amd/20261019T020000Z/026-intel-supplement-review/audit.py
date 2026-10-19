#!/usr/bin/env python3
"""Independently reconstruct supplemental calibration, all controls and guard verdicts."""
import argparse,datetime,hashlib,itertools,json,math,pathlib,statistics,subprocess
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--original-freeze',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();d=a.evidence
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=datetime.datetime.fromisoformat
cells=list(itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2]));key=lambda r:(r['history'],r['bytes'],r['encoding'])
semantic=['kind','history','n','bytes','seed','encoding','callbacks_per_pass','checksum_per_pass','tree_bytes','warmup_passes','prepost_oracles','warmup_callback_parity','validation']
# Verify seals without consulting or importing the worker audit source.
freeze=read(d/'timing-freeze.json');build=read(d/'build-freeze.json');imported=read(d/'import-freeze.json');execution=read(d/'execution-freeze.json')
for manifest in [freeze['files'],imported['files'],execution]:
    for name,h in manifest.items():assert sha(d/name)==h,(name,h)
assert imported['commit']=='ec21ce601'
relative='experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/014-scan-supplement/'
for name in ['timing-freeze.json','pass-counts.json','aa-schedule.json','b-schedule.json']:
    assert subprocess.check_output(['git','show','6ed4d361e:'+relative+name])==(d/name).read_bytes(),name
original={k:v for k,v in read(a.original_freeze).items() if k in ['base','B']}
for phase in ['preparation','calibration','aa','b']:
    q=read(d/f'post-{phase}-hashes.json');assert q['status']=='pass' and not q['mismatches'] and q['observed']==build and q['expected_manifest_sha256']==sha(d/'build-freeze.json')
q=read(d/'original-post-b-hashes.json');assert q['status']=='pass' and not q['mismatches'] and q['observed']==original and q['expected_manifest_sha256']==sha(a.original_freeze)
assert build['base']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'
assert build['B']['src/zset_btree.c']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
for name in ['src/zset_btree.h','compat/standalone.c','compat/server.h','vendor/redis/siphash.c','tests/upstream.c','bench/microbench.c']:
    assert build['base'][name]==build['B'][name]
for name,h in build['base'].items():
    if '/inputs/' in name:
        source='referee/'+name.split('/inputs/')[1];assert h==build['B'][name]==sha(d/source)
assert build['base']['compat/standalone.c']=='adf0f87cd7cd7bc043eeb1743b47f90e4484459c090024ffa837cfd34d9b3d63'
results={};fixture={};raw_hashes={}
for phase,cap,count in [('calibration',180,684),('aa',480,720),('b',480,720)]:
    x=read(d/(phase+'.json'));assert x['status']=='complete' and x['phase']==phase and x['cap_seconds']==cap and x['elapsed_seconds']<=cap and len(x['rows'])==count
    for i,r in enumerate(x['rows']):
        assert r['index']==i
        expected=['scratch/intel-scan-supplement/'+r['binary']+'/build/supplement/scan-supplement','run',r['history'],str(r['bytes']),str(r['seed']),str(r['encoding']),str(r['passes']),'0'];assert r['command']==expected
        op=d/'raw'/f'{phase}-{i:04d}.stdout';ep=op.with_suffix('.stderr');assert read(op)==r['row'] and not ep.read_bytes()
        raw_hashes[str(op.relative_to(d))]=sha(op);raw_hashes[str(ep.relative_to(d))]=sha(ep)
        z=r['row'];assert all(z[k]==r[k] for k in ['history','bytes','seed','encoding','passes']);assert z['start_cpu']==z['end_cpu']==2 and z['validation']=='pass' and z['warmup_callback_parity'] is True and z['warmup_passes']==z['prepost_oracles']==2
        assert z['elapsed_ns']>0 and z['logical_members']==z['passes']*z['n'] and z['callbacks_per_pass']>=z['n']
        assert z['n']==(7169 if r['history']=='resize' else 7 if r['bytes']==319 else 31)
        assert utc(r['started_utc'])<=utc(r['finished_utc'])
        if i:assert utc(x['rows'][i-1]['finished_utc'])<=utc(r['started_utc'])
        fk=key(r)+(r['seed'],);sem=tuple(z[k] for k in semantic)
        if fk in fixture:assert fixture[fk]==sem,(phase,fk)
        else:fixture[fk]=sem
    results[phase]=x
assert utc(results['calibration']['finished_utc'])<=utc(results['aa']['started_utc']) and utc(results['aa']['finished_utc'])<=utc(results['b']['started_utc'])
# Reconstruct the exact probe stop rule and nine fixed trial windows per cell.
cal=results['calibration']['rows'];idx=0;passes=[]
for history,width,encoding in cells:
    trial=[]
    for seed in [201,202,203]:
        probe=1
        while True:
            r=cal[idx];idx+=1;assert (key(r),r['seed'],r['binary'],r['kind'],r['passes'])==((history,width,encoding),seed,'base','probe',probe)
            if r['row']['elapsed_ns']>=20000000:break
            assert probe<10000000;probe*=10
        for repeat in range(3):
            r=cal[idx];idx+=1;assert (key(r),r['seed'],r['binary'],r['kind'],r['passes'],r['repeat'])==((history,width,encoding),seed,'base','trial',probe,repeat)
            trial.append(r['row']['elapsed_ns']/probe)
    minimum=min(trial);n=math.ceil(200000000/minimum);assert n<=10000000
    passes.append(dict(history=history,bytes=width,encoding=encoding,passes=n,minimum_ns_per_pass=minimum))
assert idx==684 and passes==read(d/'pass-counts.json');pc={key(r):r['passes'] for r in passes}
phase_effects={}
for phase in ['aa','b']:
    schedule=[]
    for block in range(6):
        for history,width,encoding in (cells if block%2==0 else cells[::-1]):
            for step,label in enumerate('ABBA'):
                schedule.append(dict(history=history,bytes=width,encoding=encoding,passes=pc[history,width,encoding],seed=201+block%3,block=block,step=step,label=label,binary='B' if phase=='b' and label=='B' else 'base'))
    assert schedule==read(d/(phase+'-schedule.json'));rr=results[phase]['rows']
    for s,r in zip(schedule,rr):assert {k:r[k] for k in s}==s
    effects=[]
    for i in range(0,720,4):
        group=rr[i:i+4]
        for k in semantic+['passes','logical_members']:assert len({r['row'][k] for r in group})==1
        q=[r['row']['elapsed_ns']/r['row']['passes'] for r in group];effect=100*((q[1]+q[2])/(q[0]+q[3])-1)
        effects.append(dict(history=group[0]['history'],bytes=group[0]['bytes'],encoding=group[0]['encoding'],block=group[0]['block'],seed=group[0]['seed'],effect_pct=effect,minimum_elapsed_ns=min(r['row']['elapsed_ns'] for r in group)))
    phase_effects[phase]=effects
verdicts=[]
for cell in cells:
    aa=[r for r in phase_effects['aa'] if key(r)==cell];bb=[r for r in phase_effects['b'] if key(r)==cell];assert len(aa)==len(bb)==6
    qualified=all(abs(r['effect_pct'])<=1 and r['minimum_elapsed_ns']>=100000000 for r in aa)
    short=any(r['minimum_elapsed_ns']<100000000 for r in aa+bb)
    if not qualified or short:verdict='PARK_CONTROL' if not qualified else 'PARK_SHORT'
    elif all(r['effect_pct']<=1 for r in bb):verdict='PASS'
    elif all(r['effect_pct']>1 for r in bb):verdict='REJECT'
    else:verdict='PARK_MIXED'
    verdicts.append(dict(history=cell[0],bytes=cell[1],encoding=cell[2],aa_qualified=qualified,short=short,aa_effects_pct=[r['effect_pct'] for r in aa],b_effects_pct=[r['effect_pct'] for r in bb],median_b_pct=statistics.median(r['effect_pct'] for r in bb),verdict=verdict))
# Structural evidence for the decisive guard; census is separate from timing.
model=read(d/'referee/baseline-validation/fixture-model-manifest.json')
assert model==read(d/'validation-base/fixture-model-manifest.json')==read(d/'validation-B/fixture-model-manifest.json') and len(model)==90
bc=read(d/'validation-base/cells.json');cc=read(d/'validation-B/cells.json');assert len(bc)==len(cc)==180
for left,right in zip(bc,cc):
    assert left==right
for variant,records in [('base',bc),('B',cc)]:
    for r in records:
        path=d/('validation-'+variant)/(r['cell']+'-'+r['build']+'-census.stdout')
        lines=[json.loads(z) for z in path.read_text().splitlines()];assert lines==[r['census'],r['run']]
        assert not path.with_suffix('.stderr').read_bytes()
        if r['build']=='native':
            z=r['run'];assert tuple(z[k] for k in semantic)==fixture[(z['history'],z['bytes'],z['encoding'],z['seed'])]
decisive=[r for r in bc if r['cell'].startswith('trim-b319-e2-')]
assert len(decisive)==6
for r in decisive:
    z=r['census'];assert z['members']==z['reversed_members']==7 and z['leaves']==z['reversed_leaves']==1
    assert z['full16_chunks']==z['full8_chunks']==z['external']==z['wide_old']==z['wide_new']==0 and z['active_rehash'] is False
out=dict(status='pass',revision='fcb17380a',processes={k:len(v['rows']) for k,v in results.items()},phase_seconds={k:v['elapsed_seconds'] for k,v in results.items()},total_processes=sum(len(v['rows']) for v in results.values()),raw_file_hashes=raw_hashes,calibration_pass_counts=passes,aa_blocks=180,b_blocks=180,qualified=sum(v['aa_qualified'] for v in verdicts),verdict_counts={v:sum(r['verdict']==v for r in verdicts) for v in ['PASS','REJECT','PARK_MIXED','PARK_CONTROL','PARK_SHORT']},cells=verdicts,effects=phase_effects,source_adoption='NONE',decision='REJECT' if any(r['verdict']=='REJECT' for r in verdicts) else 'PARK',hash_entries_each_post_phase=sum(len(v) for v in build.values()),original_post_hash_entries=sum(len(v) for v in original.values()),structural_census_rows=360,independent_model_cells=90,decisive_guard_census='Seven reversed inline members; zero full16 or full8 chunks, no active resize or wide IDs',limits='No per-process returncode column; frozen driver asserts zero before recording each row. No runner access/live rehash. Correctness referee separately reviewed, not reexecuted. Source identity is original8fab adapter, not corrected13e.')
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['cells','effects','raw_file_hashes','calibration_pass_counts']}));print(json.dumps([v for v in verdicts if v['verdict'] in ['REJECT','PARK_MIXED']],indent=2))
