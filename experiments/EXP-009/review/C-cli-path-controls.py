#!/usr/bin/env python3
"""Offline real-main/path regression control: native run/compile/signals are stubbed."""
from pathlib import Path
from types import SimpleNamespace
from datetime import datetime, timezone, timedelta
import copy, csv, hashlib, json, os, runpy, sys, tempfile

E=Path(__file__).resolve().parents[1]
W=E.parents[1]
os.chdir(W)
driver=E/'driver.py'
plan=json.loads((E/'PLAN.json').read_text())
checks=[]
def relative(p):
    p=Path(p)
    assert not p.is_absolute() and '..' not in p.parts, str(p)

for phase,override in [('build',None),('build','experiments/EXP-009/input-manifest-v2.json'),('calibrate',None),('profile',None),('aa',None)]:
    os.chdir(W)
    m=runpy.run_path(str(driver));g=m['main'].__globals__
    relative(g['E']);relative(g['REL'])
    rel=g['REL'];mp=Path(override) if override else rel/('input-manifest.json' if phase=='build' else 'timing-manifest.json' if phase=='aa' else 'bench-results/build/build-manifest.json')
    phaseplan=copy.deepcopy(plan);phaseplan['overall_stop_utc']=(datetime.now(timezone.utc)+timedelta(hours=1)).isoformat()
    manifest={'files_sha256':{str(rel/'driver.py'):'mock',str(rel/'PLAN.json'):'mock'}}
    ack=dict(status='authorized',phase=phase,exclusive_runner=True,all_other_work_idle=True,manifest_sha256='mock',driver_sha256='mock',plan_sha256='mock',published_commit='a'*40,reviews=[dict(reviewer='/root',status='PASS'),dict(reviewer='/root/followup_proposal_c',status='PASS')],absolute_stop_utc=phaseplan['overall_stop_utc'])
    def load(p):
        p=Path(p);relative(p)
        if p==Path('ack.json'):return ack
        if p==rel/'PLAN.json':return phaseplan
        if p==mp:return manifest
        if p.name=='status.json':return dict(status='COMPLETE',release_safe=True)
        raise AssertionError('unexpected mocked load '+str(p))
    def verify(table):
        for p in table:relative(p)
    # Real Owner/main/save/build execute. Only external work, hashes and inputs are mocks.
    g.update(load=load,verify=verify,sha=lambda p:'mock',signal=SimpleNamespace(SIG_BLOCK=0,SIG_SETMASK=1,ITIMER_REAL=0,signal=lambda *a:None,setitimer=lambda *a:None,pthread_sigmask=lambda *a:set()))
    with tempfile.TemporaryDirectory(prefix='exp009-C-cli-',dir=W/'scratch') as td:
        os.chdir(td)
        def compile_fake(o,name,source,mode='native',include_tree=True,defines=()):
            p=g['BUILD']/mode/name;relative(p);relative(source);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'SYNTHETIC NONEXECUTABLE FILE');return p
        def run_fake(o,cmd,name,extra_env=None,expect=0,max_seconds=60):
            paths={k:o.raw/(name+'.'+k) for k in ['stdout','stderr']}
            text='';err=''
            if cmd[0]=='clang':text='SYNTHETIC compiler metadata\n'
            elif cmd[0]=='nm':text='0000000100001000 t _zbtreeScoreRaw\n'
            elif cmd[0]=='otool':text='_zbtreeScoreRaw:\n0000000100001000 ret\n'
            elif str(cmd[0]).endswith('original43'):text=''.join(f'{i} - test PASSED\n' for i in range(1,44))+'43 passed, 0 failed, 43 total\n'
            elif str(cmd[0]).endswith('physical-oracle'):text='PASS cells=4160 exact-score/position/output checks=515840; widths0..64 shifts0/3 reversed both signed-zero ties colliding-tags first-match misses\n'
            elif expect==2:err='synthetic invalid CLI\n'
            else:
                args=dict(zip(cmd[1::2],cmd[2::2]));n=int(args['--size']);ops=int(args['--ops']);seed=int(args['--seed']);case=args['--case'];checksum=g['expected_checksum'](case,n,ops,seed)[0]
                row=[case,str(n),str(ops),args['--member-bytes'],str(seed),str(ops),str(ops*1000),'1000.000','1000000.000','123456',str(checksum),'2000000','6','7','user-interactive','user-interactive','0','0','unknown','0','1','1000']
                text=','.join(g['CSV_HEADER'])+'\n'+','.join(row)+'\n'
            paths['stdout'].write_text(text);paths['stderr'].write_text(err)
            for p in paths.values():relative(p)
            o.records.append(dict(release_safe=True,raw={k:dict(path=str(p),sha256='mock',bytes=p.stat().st_size) for k,p in paths.items()}))
            with (o.out/'commands.jsonl').open('a') as f:f.write('{}\n')
            return paths
        g.update(compile_binary=compile_fake,run=run_fake)
        if phase!='build':
            def phase_fake(o):
                relative(o.out);relative(o.raw);relative(o.manifest_path);o.state['status']='COMPLETE'
            g[phase]=phase_fake
        before=sys.argv
        try:
            sys.argv=[str(driver),phase,'--ack','ack.json']+(['--manifest',override] if override else [])
            m['main']()
        finally:sys.argv=before
        out=rel/('profile-results/run' if phase=='profile' else 'bench-results/'+phase)
        state=json.loads((out/'status.json').read_text());assert state['status']=='COMPLETE' and state['release_safe']
        if phase=='build':
            built=json.loads((out/'build-manifest.json').read_text())
            for p in built['files_sha256']:relative(p)
            for p in built['binaries'].values():relative(p)
            for paths in built['metadata'].values():
                for p in paths.values():relative(p)
            assert built['input_manifest_path']==str(mp)
            checks.append(dict(phase=phase,manifest=str(mp),real_build_function=True,all_manifest_keys_relative=True,entries=len(built['files_sha256']),input_manifest_propagated=True))
        else:checks.append(dict(phase=phase,manifest=str(mp),real_main_and_owner=True,native_phase_stubbed=True,relative_outputs=True))
os.chdir(W)
result=dict(status='PASS',scope='Real main/Owner/build with mocked hashes/manifest inputs/compile/run/signals; no external child or native command',driver_sha256=hashlib.sha256(driver.read_bytes()).hexdigest(),control_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,prior_gap='Initial41 pure controls did not invoke main/default paths or real build manifest construction, so did not expose absolute-E defect. First real invocation failed before Owner/output/child; old controls remain valid only for their stated scope.')
with (E/'review/C-cli-path-controls.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result))
