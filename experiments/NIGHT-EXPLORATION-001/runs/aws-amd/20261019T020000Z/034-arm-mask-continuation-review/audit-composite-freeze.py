import subprocess,json,hashlib,ast,sys
rev='380ef3109';base='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/';p=base+'027-mask-followup/';s=base+'028-mask-validation-continuation/'
def raw(r,n):return subprocess.check_output(['git','show',r+':'+n])
def j(r,n):return json.loads(raw(r,n))
def h(b):return hashlib.sha256(b).hexdigest()
f=j(rev,p+'timing-freeze.json');receipt=j(rev,p+'composite-correctness.json');binding=j('19fd53594',s+'binding.json');old=j('8cdebdcba',p+'validation/result.json');new=j('19fd53594',s+'continuation/result.json');pub=j('19fd53594',s+'continuation/PUBLICATION.json')
for n,v in f['files'].items():assert h(raw(rev,p+n))==v,n
for n in ['composite-gate.py','run-phase.py','audit-phase.py']:ast.parse(raw(rev,p+n))
assert receipt['status']=='PASS_COMPOSITE_CORRECTNESS' and receipt['original_attempt_status']==old['status']=='failed' and receipt['source_selection']=='NONE' and receipt['performance_authority'] is False
assert receipt['binding_sha256']==h(raw('19fd53594',s+'binding.json'))
assert receipt['suffix_execution_freeze_sha256']==h(raw('39d84533f',s+'execution-freeze.json'))
oldpub=j('8cdebdcba',p+'validation/PUBLICATION.json')
assert receipt['original_raw_result_sha256']==oldpub['result.json']['raw_sha256']
assert receipt['suffix_raw_result_sha256']==pub['result.json']['raw_sha256']
assert receipt['suffix_raw_artifacts']=={n:v['raw_sha256'] for n,v in pub.items()}
for field in ['protected_binaries','guard_binary_sha256','snapshots_before','source_hashes','candidate_source_sha256','text_sha256']:assert receipt[field]==binding[field],field
assert receipt['original_registered_commands']==2117 and receipt['original_additional_audited_fault_detection']==2118 and receipt['suffix_commands']==list(range(2119,2125))
assert [receipt[k] for k in ['normal_mode_cells','original43_runs','additional_oracle_runs','intended_negative_detections']]==[2048,4,12,14]
assert receipt['independent_closure_review']=='dc9d915fe' and receipt['independent_failure_review']=='7cf304361'
for k in ['root_closure_review','root_failure_review','independent_closure_review','independent_failure_review']:subprocess.check_output(['git','rev-parse','--verify',receipt[k]+'^{commit}'])
counts={}
for name in f['files']:
 if name.startswith('schedules/'):
  b=raw(rev,p+name);assert b==raw('8d11db31a',p+name);counts[name]=len(json.loads(b))
assert sum(counts.values())==4272
for n in ['PLAN.md','phase-budgets.json','original-guards.json','iterator-guards.json','identities.json','expected.json','preparation-freeze.json','validation-commands.json']:
 assert raw(rev,p+n)==raw('8d11db31a',p+n),n
# Every original published artifact remains identical, including the FAILED result.
oldfiles=subprocess.check_output(['git','ls-tree','-r','--name-only','8cdebdcba','--',p+'validation']).decode().splitlines()
for n in oldfiles:assert raw(rev,n)==raw('8cdebdcba',n),n
print(json.dumps(dict(revision=rev,freeze_sha256=h(raw(rev,p+'timing-freeze.json')),frozen_inputs=len(f['files']),status='STATIC_COMPOSITE_AND_TIMING_FREEZE_REVIEW_PASS',original_status='FAILED',original_artifacts_unchanged=len(oldfiles),schedules=counts,schedule_entries=sum(counts.values()),receipt_raw_bindings=len(receipt['suffix_raw_artifacts']),snapshot_bindings=sum(map(len,receipt['snapshots_before'].values())),no_remote_access=True,no_driver_execution=True,no_timing_grant=True),indent=2))
