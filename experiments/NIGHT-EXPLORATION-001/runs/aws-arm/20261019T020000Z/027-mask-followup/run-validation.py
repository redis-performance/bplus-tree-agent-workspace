#!/usr/bin/env python3
import argparse,pathlib,json,hashlib,subprocess,datetime,time,os,tarfile,shutil,csv,re
from apply_exact import apply
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);a=p.parse_args();assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc);here=pathlib.Path(__file__).resolve().parent;out=here/'validation';out.mkdir();assert sorted(os.sched_getaffinity(0))==[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();e=json.loads((here/'expected.json').read_text());freeze=json.loads((here/'preparation-freeze.json').read_text());commands=json.loads((here/'validation-commands.json').read_text())
for name,h in freeze['files'].items():assert sha(here/name)==h,name
actual=a.checkout/'scratch/adapter-worktree-13e459ff8';binary=actual/'build/adapter-requalification/btree-bench'
assert sha(binary)==e['aa_binary_sha256'];original_sources={n:sha(actual/n) for n in e['source_hashes']};assert original_sources==e['source_hashes'];protected={n:sha(a.checkout/n) for n in e['protected_binaries']};assert protected==e['protected_binaries']
state=dict(status='running',started_utc=now(),cpu=2,execution_freeze_sha256=sha(here/'preparation-freeze.json'),actual_binary_before=sha(binary),actual_sources_before=original_sources,protected_before=protected,commands=[])
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
def expand(s):return s.replace('<job>',str(here)).replace('<checkout>',str(a.checkout))
def prepare():
    for variant in ['control','A']+['fault-'+n for n in e['faults']]:
        root=here/variant;root.mkdir()
        with tarfile.open(here/'source.tar') as t:t.extractall(root,filter='data')
        assert {n:sha(root/n) for n in e['source_hashes']}==e['source_hashes']
        for n,h in e['oracles'].items():
            assert sha(here/'oracles'/n)==h;shutil.copyfile(here/'oracles'/n,root/('bench' if n in ['iterator_modes.c','iterator_modes_v5.c'] else 'tests')/n)
        text=(root/'src/zset_btree.c').read_text()
        if variant=='A':
            assert sha(here/'candidate.patch')==e['candidate_patch_sha256'];text=apply(text,(here/'candidate.patch').read_text());(root/'src/zset_btree.c').write_text(text);assert sha(root/'src/zset_btree.c')==e['candidate_source_sha256']
        elif variant.startswith('fault-'):
            name=variant[6:];q=here/'faults'/(name+'.patch');assert sha(q)==e['faults'][name]['patch'];(root/'src/zset_btree.c').write_text(apply(text,q.read_text()))
        for mode in ['native','san']:(root/'build'/mode).mkdir(parents=True)
    state['snapshots_before']={v:{str(q.relative_to(here/v)):sha(q) for q in (here/v).rglob('*') if q.is_file()} for v in ['control','A']+['fault-'+n for n in e['faults']]};save()
save()
try:
    for contract in commands:
        left=600-(time.monotonic()-start);assert left>0,'validation600s cap reached';r=dict(contract,started_utc=now());state['commands'].append(r);save()
        try:proc=subprocess.run([expand(x) for x in contract['command']],cwd=expand(contract['cwd']),capture_output=True,text=True,timeout=min(120,left))
        except subprocess.TimeoutExpired as ex:
            r.update(returncode=124,finished_utc=now())
            for suffix,val in [('stdout',ex.stdout),('stderr',ex.stderr)]:(out/(r['name']+'.'+suffix)).write_text((val.decode(errors='replace') if isinstance(val,bytes) else val) or '')
            save();raise
        r.update(returncode=proc.returncode,finished_utc=now());(out/(r['name']+'.stdout')).write_text(proc.stdout);(out/(r['name']+'.stderr')).write_text(proc.stderr);save()
        if contract['kind']=='negative':
            assert proc.returncode not in [0,124];matches=[n in proc.stderr for n in contract['needles']];assert all(matches) if contract['match']=='all' else any(matches)
        else:proc.check_returncode()
        if contract['kind']=='archive':prepare()
        elif contract['name']=='compiler':assert 'clang version 18.1.3' in proc.stdout and 'aarch64' in proc.stdout
        elif contract['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',proc.stdout)
        elif contract['kind']=='oracle':assert 'PASS' in proc.stdout
        elif contract['kind']=='modes':
            rows=list(csv.DictReader(proc.stdout.splitlines()));assert len(rows)==1;z=rows[0];f=contract['fixture'];assert z['operations']=='387' and z['traversals']=='3' and z['checksum']==z['expected_checksum']
            assert z['size']=='129' and z['requested_ops']=='259' and z['seed']=='1501' and all(z[k]==str(v) for k,v in f.items());assert z['cpu_start']==z['cpu_end']=='2'
        if contract['kind']=='modes5':
            rows=list(csv.DictReader(proc.stdout.splitlines()));assert len(rows)==1;z=rows[0];f=contract['fixture'];assert int(z['operations'])==3*f['size'] and z['traversals']=='3' and z['checksum']==z['expected_checksum'];assert all(z[k]==str(v) for k,v in f.items());assert z['cpu_start']==z['cpu_end']=='2'
        r['checked']=True;save()
    assert len(state['commands'])==len(commands)
    assert (out/'actual.text').read_bytes()==(out/'control.text').read_bytes(),'rebuilt control.text differs from actual013'
    assert (out/'oldA.text').read_bytes()==(out/'A.text').read_bytes(),'rebuilt A.text differs from unchanged old A'
    state['text_sha256']={n:sha(out/(n+'.text')) for n in ['actual','control','A','oldA']}
    state['guard_binary_sha256']={v:{h:sha(here/v/'build/native'/h) for h in ['modes','modes5']} for v in ['control','A']}
    state['binary_sha256']={n:sha(here/n/'build/adapter-requalification/btree-bench') for n in ['control','A']}
    state['snapshots_after']={v:{n:sha(here/v/n) for n in files} for v,files in state['snapshots_before'].items()};assert state['snapshots_before']==state['snapshots_after']
    state.update(actual_binary_after=sha(binary),actual_sources_after={n:sha(actual/n) for n in e['source_hashes']},protected_after={n:sha(a.checkout/n) for n in e['protected_binaries']});assert state['actual_binary_after']==e['aa_binary_sha256'] and state['actual_sources_after']==original_sources and state['protected_after']==protected
    state.update(status='correctness_complete',original_tests_runs=4,mode_cells=512,mode5_cells=1536,oracle_runs=12,negative_detections=14)
except BaseException as ex:state.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
