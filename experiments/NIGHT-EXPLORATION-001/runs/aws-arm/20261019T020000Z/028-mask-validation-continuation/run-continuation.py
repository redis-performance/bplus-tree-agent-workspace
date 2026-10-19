#!/usr/bin/env python3
"""Six never-started commands only. The original failed result is immutable."""
import argparse,datetime,hashlib,json,os,pathlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);p.add_argument('--prior',required=True,type=pathlib.Path);a=p.parse_args()
here=pathlib.Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
freeze=json.loads((here/'execution-freeze.json').read_text())
for n,h in freeze['files'].items():assert sha(here/n)==h,n
b=json.loads((here/'binding.json').read_text());contracts=json.loads((here/'remaining-commands.json').read_text())
assert os.sched_getaffinity(0)=={2}
assert (datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)-datetime.datetime.now(datetime.timezone.utc)).total_seconds()>180
out=here/'continuation';out.mkdir();start=time.monotonic()
s=dict(status='running',started_utc=now(),cpu=2,cap_seconds=180,execution_freeze_sha256=sha(here/'execution-freeze.json'),original_attempt_status='failed',commands=[])
def save():(out/'result.json').write_text(json.dumps(s,indent=2)+'\n')
def verify():
    result={}
    result['prior_artifacts']={n:sha(a.prior/'validation'/n) for n in b['prior_raw_artifacts']};assert result['prior_artifacts']==b['prior_raw_artifacts']
    result['prior_freeze_sha256']=sha(a.prior/'preparation-freeze.json');assert result['prior_freeze_sha256']==b['prior_freeze_sha256']
    result['prior_manifest_sha256']=sha(a.prior/'validation-commands.json');assert result['prior_manifest_sha256']==b['prior_manifest_sha256']
    result['prior_inputs']={n:sha(a.prior/n) for n in b['prior_inputs']};assert result['prior_inputs']==b['prior_inputs']
    result['snapshots']={v:{n:sha(a.prior/v/n) for n in files} for v,files in b['snapshots_before'].items()};assert result['snapshots']==b['snapshots_before']
    result['protected_binaries']={n:sha(a.checkout/n) for n in b['protected_binaries']};assert result['protected_binaries']==b['protected_binaries']
    result['guard_binary_sha256']={v:{n:sha(a.prior/v/'build/native'/n) for n in files} for v,files in b['guard_binary_sha256'].items()};assert result['guard_binary_sha256']==b['guard_binary_sha256']
    result['actual_source_sets']={}
    for v,rel in [('actual','scratch/adapter-worktree-13e459ff8'),('actualA','scratch/arm-exp005A-replication-13e459ff8/A')]:
        expected=dict(b['source_hashes'])
        if v=='actualA':expected['src/zset_btree.c']=b['candidate_source_sha256']
        result['actual_source_sets'][v]={n:sha(a.checkout/rel/n) for n in expected};assert result['actual_source_sets'][v]==expected
    result['text_sha256']={n:sha(a.prior/'validation'/(n+'.text')) for n in b['text_sha256']};assert result['text_sha256']==b['text_sha256']
    return result
save()
try:
    s['identity_before']=verify();save()
    old=json.loads((a.prior/'validation/result.json').read_text());manifest=json.loads((a.prior/'validation-commands.json').read_text())
    assert old['status']=='failed' and len(old['commands'])==2118 and len(manifest)==2124
    assert all(x.get('checked') is True for x in old['commands'][:2117])
    last=old['commands'][2117];assert last['name']=='h5-zero-sign-native-detect' and last['returncode']==-6 and not last.get('checked',False)
    for i,x in enumerate(old['commands']):
        assert all(x[k]==v for k,v in manifest[i].items()),i
    assert 'bench/iterator_modes_v5.c:62: score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))' in (a.prior/'validation/h5-zero-sign-native-detect.stderr').read_text()
    assert len(contracts)==6
    for i,x in enumerate(contracts):
        expected=dict(manifest[2118+i]);actual=dict(x);assert actual.pop('original_command_number')==2119+i
        if i==1:
            assert actual.pop('prior_needles')==expected['needles'];expected['needles']=['score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))']
        assert actual==expected
    s['outputs_absent_before']={n:not (a.prior/n).exists() for n in b['absent_outputs']};assert all(s['outputs_absent_before'].values());save()
    for contract in contracts:
        left=180-(time.monotonic()-start);assert left>0,'phase cap reached'
        r=dict(contract,started_utc=now());s['commands'].append(r);save()
        def expand(x):return x.replace('<job>',str(a.prior)).replace('<checkout>',str(a.checkout))
        try:
            q=subprocess.run([expand(x) for x in contract['command']],cwd=expand(contract['cwd']),capture_output=True,text=True,timeout=min(60,left))
            stdout,stderr,rc=q.stdout,q.stderr,q.returncode
        except subprocess.TimeoutExpired as ex:
            stdout,stderr,rc=ex.stdout,ex.stderr,124
            stdout=stdout.decode(errors='replace') if isinstance(stdout,bytes) else stdout or ''
            stderr=stderr.decode(errors='replace') if isinstance(stderr,bytes) else stderr or ''
        r.update(returncode=rc,finished_utc=now())
        (out/(r['name']+'.stdout')).write_text(stdout);(out/(r['name']+'.stderr')).write_text(stderr);save()
        if contract['kind']=='negative':
            assert rc not in [0,124],(r['name'],rc)
            matches=[n in stderr for n in contract['needles']]
            assert all(matches) if contract['match']=='all' else any(matches)
        else:assert rc==0,(r['name'],rc)
        r['checked']=True;save()
    s['created_output_hashes']={n:sha(a.prior/n) for n in b['absent_outputs']}
    s['status']='six_command_suffix_complete_pending_independent_closure'
except BaseException as ex:
    s.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:
    try:s['identity_after']=verify();s['identity_unchanged']=s.get('identity_before')==s['identity_after'];assert s['identity_unchanged']
    except BaseException as ex:s.update(status='failed',post_identity_error=type(ex).__name__+': '+str(ex))
    s.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
    assert s['status']!='failed',s.get('error',s.get('post_identity_error'))
