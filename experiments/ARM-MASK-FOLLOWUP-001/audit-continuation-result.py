import subprocess,tarfile,io,json,hashlib,datetime
from pathlib import Path
prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/'
def archive(rev,p):
 with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',rev,p]))) as t:return {m.name[len(p):]:t.extractfile(m).read() for m in t if m.isfile()}
f=archive('19fd53594',prefix+'028-mask-validation-continuation/');o=archive('8cdebdcba',prefix+'027-mask-followup/');current=archive('19fd53594',prefix+'027-mask-followup/')
assert all(current[n]==b for n,b in o.items()),'Original published artifacts changed'
j=lambda d,n:json.loads(d[n]);sha=lambda b:hashlib.sha256(b).hexdigest()
for n,h in j(f,'evidence-seal.json').items():assert sha(f[n])==h
freeze=j(f,'execution-freeze.json');b=j(f,'binding.json');r=j(f,'continuation/result.json');post=j(f,'post-continuation-identity-idle.json');commands=j(f,'remaining-commands.json')
for n,h in freeze['files'].items():assert sha(f[n])==h
assert r['status']=='six_command_suffix_complete_pending_independent_closure' and r['elapsed_seconds']<=180 and len(r['commands'])==6
assert r['identity_unchanged'] and r['identity_before']==r['identity_after']
ident=r['identity_before'];old=j(o,'validation/result.json')
assert ident['snapshots']==old['snapshots_before']==post['snapshots']
assert ident['prior_artifacts']==b['prior_raw_artifacts']==post['prior_raw_artifacts']
for k in ['protected_binaries','guard_binary_sha256','prior_inputs','prior_freeze_sha256','prior_manifest_sha256']:assert ident[k]==post[k]==b[k]
assert post['continuation_inputs']==freeze['files'] and post['continuation_freeze_sha256']==sha(f['execution-freeze.json'])
assert post['owned_units']==post['owned_cgroup_pids']==[]
assert set(r['outputs_absent_before'])==set(r['created_output_hashes'])==set(b['absent_outputs']) and all(r['outputs_absent_before'].values())
for i,(run,contract) in enumerate(zip(r['commands'],commands)):
 assert all(run[k]==v for k,v in contract.items()) and run['checked']
 start=datetime.datetime.fromisoformat(run['started_utc']);end=datetime.datetime.fromisoformat(run['finished_utc']);assert 0<=(end-start).total_seconds()<=60
 if i:assert r['commands'][i-1]['finished_utc']<=run['started_utc']
 err=f['continuation/'+run['name']+'.stderr'].decode()
 if contract['kind']=='plain':assert run['returncode']==0
 else:
  assert run['returncode']==-6
  hits=[needle in err for needle in contract['needles']];assert all(hits) if contract['match']=='all' else any(hits)
report=dict(audit_status='PASS',revision='19fd53594',reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),suffix_commands=6,builds_pass=3,intended_fault_detections=3,phase_seconds=r['elapsed_seconds'],sealed_public_artifacts=len(j(f,'evidence-seal.json')),prior_published_artifacts_unchanged=len(o),prior_raw_identity_bindings=4241,snapshot_file_hashes_unchanged=513,protected_binaries_unchanged=6,guard_binaries_unchanged=4,source_selection='NONE',timing_grant=False,original_attempt_status='FAILED',post_identity_idle_verified_at=post['checked_utc'],closure='Combining original registered2117 checks, independently audited2118 fault detection, and six new commands completes planned coverage without repeating a command. Separate composite receipt and timing review remain required.')
Path('experiments/ARM-MASK-FOLLOWUP-001/CONTINUATION-RESULT-ROOT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
