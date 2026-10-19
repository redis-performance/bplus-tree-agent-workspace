import pathlib,json,hashlib,ast,sys
p=pathlib.Path(sys.argv[1]);old=pathlib.Path(sys.argv[2]);j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();f=j(p/'execution-freeze.json');b=j(p/'binding.json');r=j(old/'validation/result.json');pub=j(old/'validation/PUBLICATION.json');post=j(old/'post-preparation-identity-idle.json')
for n,h in f['files'].items():assert sha(p/n)==h,n
assert b['prior_raw_artifacts']=={n:v['raw_sha256'] for n,v in pub.items()}
assert b['snapshots_before']==r['snapshots_before']
assert b['prior_inputs']==j(old/'preparation-freeze.json')['files']
assert b['protected_binaries']==post['protected_binaries'] and b['guard_binary_sha256']==post['guard_binary_sha256'] and b['text_sha256']==post['text_sha256']
assert b['prior_freeze_sha256']==sha(old/'preparation-freeze.json') and b['prior_manifest_sha256']==sha(old/'validation-commands.json')
assert b['absent_outputs']==['fault-h5-zero-sign/build/san/modes5','fault-h5-state/build/native/modes5','fault-h5-state/build/san/modes5']
assert b['source_hashes']==post['source_hashes']['actual'] and b['candidate_source_sha256']==post['source_hashes']['A']['src/zset_btree.c']
c=j(p/'remaining-commands.json');prev=j(old/'validation-commands.json')[2118:];assert len(c)==len(prev)==6
for i,(x,y) in enumerate(zip(c,prev)):
 z=dict(x);assert z.pop('original_command_number')==2119+i
 if i==1:assert z.pop('prior_needles')==y['needles'];y=dict(y,needles=['score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))'])
 assert z==y
ast.parse((p/'run-continuation.py').read_text());assert f['cap_seconds']==b['cap_seconds']==180 and f['child_cap_seconds']==b['child_cap_seconds']==60
print(json.dumps({'revision':'39d84533f','status':'static_six_only_review_pass','freeze_inputs':len(f['files']),'raw_artifact_bindings':len(b['prior_raw_artifacts']),'snapshot_bindings':sum(len(x) for x in b['snapshots_before'].values()),'snapshot_sources':len(b['snapshots_before']),'prior_frozen_inputs':len(b['prior_inputs']),'protected_binaries':len(b['protected_binaries']),'guard_binaries':sum(len(x) for x in b['guard_binary_sha256'].values()),'new_output_absence_requirements':b['absent_outputs'],'commands':6,'original_commands_repeated':0,'original_failed_result_preserved':True,'driver_executed':False,'root_grant_required':True,'performance_authorized':False},indent=2))
