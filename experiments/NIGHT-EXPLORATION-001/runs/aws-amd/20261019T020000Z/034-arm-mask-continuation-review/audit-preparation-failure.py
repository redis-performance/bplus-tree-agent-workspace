import pathlib,json,hashlib,csv,re,datetime,collections,sys
p=pathlib.Path(sys.argv[1]);j=lambda n:json.loads((p/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();r=j('validation/result.json');pub=j('validation/PUBLICATION.json');seal=j('preparation-evidence-seal.json');f=j('preparation-freeze.json');e=j('expected.json');commands=j('validation-commands.json');post=j('post-preparation-identity-idle.json')
for n,h in seal.items():assert sha(p/n)==h,n
for n,h in f['files'].items():assert sha(p/n)==h,n
for n,v in pub.items():
 if 'public_sha256' in v:assert sha(p/'validation'/n)==v['public_sha256'],n
assert r['status']=='failed' and len(r['commands'])==2118 and len(commands)==2124 and r['elapsed_seconds']<600
assert r['execution_freeze_sha256']==sha(p/'preparation-freeze.json')
assert r['actual_sources_before']==e['source_hashes'] and r['protected_before']==e['protected_binaries']
count=collections.Counter();previous=datetime.datetime.fromisoformat(r['started_utc'])
for i,(x,c) in enumerate(zip(r['commands'],commands)):
 assert all(x[k]==v for k,v in c.items());begin=datetime.datetime.fromisoformat(x['started_utc']);end=datetime.datetime.fromisoformat(x['finished_utc']);assert previous<=begin<=end and (end-begin).total_seconds()<121;previous=end
 stdout=(p/'validation'/(x['name']+'.stdout')).read_text();stderr=(p/'validation'/(x['name']+'.stderr')).read_text()
 if i==2117:
  assert not x.get('checked',False) and x['returncode']==-6 and x['kind']=='negative';assert 'score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))' in stderr and x['needles'][0] not in stderr;continue
 assert x['checked'];count[x['kind']]+=1
 if x['kind']=='negative':
  assert x['returncode'] not in [0,124];matches=[n in stderr for n in x['needles']];assert all(matches) if x['match']=='all' else any(matches)
 else:assert x['returncode']==0
 if x['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
 if x['kind']=='oracle':assert 'PASS' in stdout
 if x['kind'] in ['modes','modes5']:
  z,=csv.DictReader(stdout.splitlines());assert z['checksum']==z['expected_checksum'] and z['cpu_start']==z['cpu_end']=='2';fix=x['fixture'];assert all(z[k]==str(v) for k,v in fix.items());assert int(z['traversals'])==3
  if x['kind']=='modes':assert z['size']=='129' and z['requested_ops']=='259' and z['operations']=='387' and z['seed']=='1501'
  else:assert int(z['operations'])==3*fix['size']
assert count['modes']==512 and count['modes5']==1536 and count['original43']==4 and count['oracle']==12 and count['negative']==10
assert post['frozen_inputs']==f['files'] and post['protected_binaries']==e['protected_binaries'] and post['owned_units']==post['owned_cgroup_pids']==[] and post['lease_release_marker'] is False
for v,s in post['source_hashes'].items():assert s==dict(e['source_hashes'],**({'src/zset_btree.c':e['candidate_source_sha256']} if v in ['A','actualA'] else {}))
assert post['text_sha256']['actual']==post['text_sha256']['control']=='b17746defd935a8c4d1befc2277cbd06baa92d6ac9881ac3e0ab628a96f646e3'
assert post['text_sha256']['A']==post['text_sha256']['oldA']=='ec828508190ef261f7d45fdfcfa36ed17914377a962faebaa0d903f6808fa14d'
for n in ['actual','control','A','oldA']:assert pub[n+'.text']['raw_sha256']==post['text_sha256'][n]
remaining=[x['name'] for x in commands[2118:]]
assert all(not (p/'validation'/(n+'.stdout')).exists() and not (p/'validation'/(n+'.stderr')).exists() for n in remaining)
print(json.dumps({'revision':'8cdebdcba','review_status':'failure_registration_diagnosis_verified','original_phase_status':'FAILED','frozen_inputs':len(f['files']),'seal_entries':len(seal),'publication_entries':len(pub),'public_artifact_hashes':sum('public_sha256' in x for x in pub.values()),'attempted_commands':2118,'checked_commands':2117,'checked_counts':dict(count),'unregistered_fault_exit':-6,'remaining_commands':remaining,'post_identity_record_verified':True,'raw_text_bytes_read_by_this_reviewer':False,'limits':['Raw text hashes are producer/postinspection attestations; public hash joins independently checked','Copied snapshot oracle/fault source posthashes should be explicitly checked before any continuation','Original failed registration remains FAILED; no rerun or timing authorized']},indent=2))
