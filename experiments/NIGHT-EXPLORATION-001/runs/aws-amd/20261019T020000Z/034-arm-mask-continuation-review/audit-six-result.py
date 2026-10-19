import pathlib,json,hashlib,datetime,subprocess,sys
p=pathlib.Path(sys.argv[1]);old=pathlib.Path(sys.argv[2]);j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();r=j(p/'continuation/result.json');b=j(p/'binding.json');f=j(p/'execution-freeze.json');c=j(p/'remaining-commands.json');seal=j(p/'evidence-seal.json');pub=j(p/'continuation/PUBLICATION.json');post=j(p/'post-continuation-identity-idle.json');oldr=j(old/'validation/result.json')
for n,h in seal.items():assert sha(p/n)==h,n
for n,h in f['files'].items():assert sha(p/n)==h,n
for n,h in pub.items():assert sha(p/'continuation'/n)==h['public_sha256'],n
assert r['status']=='six_command_suffix_complete_pending_independent_closure' and r['original_attempt_status']==oldr['status']=='failed';assert len(r['commands'])==6 and r['cpu']==2 and r['cap_seconds']==180 and 0<r['elapsed_seconds']<180
assert r['execution_freeze_sha256']==sha(p/'execution-freeze.json') and r['identity_before']==r['identity_after'] and r['identity_unchanged']
i=r['identity_before'];assert i['prior_artifacts']==b['prior_raw_artifacts']=={n:h['raw_sha256'] for n,h in j(old/'validation/PUBLICATION.json').items()};assert i['snapshots']==b['snapshots_before']==oldr['snapshots_before']
for k in ['prior_freeze_sha256','prior_manifest_sha256','prior_inputs','protected_binaries','guard_binary_sha256','text_sha256']:assert i[k]==b[k],k
for n,files in i['actual_source_sets'].items():assert files==dict(b['source_hashes'],**({'src/zset_btree.c':b['candidate_source_sha256']} if n=='actualA' else {}))
assert r['outputs_absent_before']==dict.fromkeys(b['absent_outputs'],True);assert set(r['created_output_hashes'])==set(b['absent_outputs']) and all(len(h)==64 for h in r['created_output_hashes'].values())
start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert 0<(end-start).total_seconds()<180 and end<datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc);previous=start;exitcodes=[]
for x,contract in zip(r['commands'],c):
 assert all(x[k]==v for k,v in contract.items()) and x['checked'];t0=datetime.datetime.fromisoformat(x['started_utc']);t1=datetime.datetime.fromisoformat(x['finished_utc']);assert previous<=t0<=t1<=end and (t1-t0).total_seconds()<=60;previous=t1;stderr=(p/'continuation'/(x['name']+'.stderr')).read_text();exitcodes.append(x['returncode'])
 if x['kind']=='negative':assert x['returncode']==-6 and any(n in stderr for n in x['needles'])
 else:assert x['returncode']==0
assert exitcodes==[0,-6,0,-6,0,-6]
assert post['prior_raw_artifacts']==b['prior_raw_artifacts'] and post['snapshots']==b['snapshots_before']
for k in ['protected_binaries','guard_binary_sha256','prior_inputs','prior_freeze_sha256','prior_manifest_sha256']:assert post[k]==b[k],k
assert post['continuation_inputs']==f['files'] and post['continuation_freeze_sha256']==sha(p/'execution-freeze.json') and post['owned_units']==post['owned_cgroup_pids']==[]
assert datetime.datetime.fromisoformat(post['checked_utc'])>end
pre='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup';trees={rev:subprocess.check_output(['git','rev-parse',rev+':'+pre]).decode().strip() for rev in ['39d84533f','19fd53594']};assert len(set(trees.values()))==1
print(json.dumps({'revision':'19fd53594','status':'six_suffix_raw_and_identity_audit_pass','original_attempt_status':'FAILED','evidence_seal_entries':len(seal),'public_new_artifacts':len(pub),'commands':6,'command_numbers':[x['original_command_number'] for x in c],'exit_codes':exitcodes,'elapsed_seconds':r['elapsed_seconds'],'prior_raw_bindings':len(b['prior_raw_artifacts']),'snapshot_bindings':sum(len(v) for v in b['snapshots_before'].values()),'original027_tree_ids':trees,'original027_public_tree_unchanged':True,'post_idle_record_pass':True,'combined_intended_negative_detections':{'original_registered':10,'original_independently_assessed':1,'new_registered':3},'scope':'Correctness closure eligibility only; composite receipt and any timing gate remain separate','remote_access':False,'limits':['Operator pre/post hashes independently joined; reviewer did not read live binaries','Disclosed localcollector overwrite restored before publication; entire original027 Git tree unchanged','No current timing/guard/profile/confirmation qualification follows']},indent=2))
