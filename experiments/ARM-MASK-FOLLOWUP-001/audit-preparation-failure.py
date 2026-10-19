import subprocess,tarfile,io,json,hashlib,csv,re,datetime,collections,sys
from pathlib import Path
rev=sys.argv[1];base='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/027-mask-followup/'
archive=subprocess.check_output(['git','archive',rev,base]);files={}
with tarfile.open(fileobj=io.BytesIO(archive)) as t:
 for member in t:
  if member.isfile():files[member.name[len(base):]]=t.extractfile(member).read()
def data(n):return json.loads(files[n])
def sha(b):return hashlib.sha256(b).hexdigest()
seal=data('preparation-evidence-seal.json');pub=data('validation/PUBLICATION.json');r=data('validation/result.json');manifest=data('validation-commands.json');e=data('expected.json')
for n,h in seal.items():assert sha(files[n])==h,n
for n,record in pub.items():
 if 'public_sha256' in record:assert sha(files['validation/'+n])==record['public_sha256']
post=data('post-preparation-identity-idle.json')
assert r['status']=='failed' and r['elapsed_seconds']<=600 and len(r['commands'])==2118 and len(manifest)==2124
assert post['protected_binaries']==r['protected_before']==e['protected_binaries']
assert r['actual_binary_before']==e['aa_binary_sha256']
assert r['actual_sources_before']==e['source_hashes']
for expected in manifest[2118:]:
 assert 'validation/'+expected['name']+'.stdout' not in files
 assert 'validation/'+expected['name']+'.stderr' not in files
for i,(observed,expected) in enumerate(zip(r['commands'],manifest)):
 assert all(observed[k]==v for k,v in expected.items()),observed['name']
 assert observed.get('checked',False)==(i<2117)
 assert observed['started_utc']<=observed['finished_utc']
 if i:assert r['commands'][i-1]['finished_utc']<=observed['started_utc']
 out=files['validation/'+observed['name']+'.stdout'].decode();err=files['validation/'+observed['name']+'.stderr'].decode();kind=expected['kind']
 if kind=='negative':
  assert observed['returncode'] not in (0,124)
  matches=[n in err for n in expected['needles']]
  if i<2117: assert all(matches) if expected['match']=='all' else any(matches)
  else:
   assert observed['returncode']==-6 and not any(matches)
   assert 'score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))' in err
 else:assert observed['returncode']==0
 if kind=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',out)
 if kind=='oracle':assert 'PASS' in out
 if kind=='modes':
  rows=list(csv.DictReader(out.splitlines()));assert len(rows)==1;z=rows[0];assert z['operations']=='387' and z['traversals']=='3' and z['checksum']==z['expected_checksum']
  for k,v in dict(size=129,requested_ops=259,seed=1501,cpu_start=2,cpu_end=2,**expected['fixture']).items():assert z[k]==str(v)
 if kind=='modes5':
  rows=list(csv.DictReader(out.splitlines()));assert len(rows)==1;z=rows[0];f=expected['fixture']
  assert int(z['operations'])==3*f['size'] and z['traversals']=='3' and z['checksum']==z['expected_checksum']
  assert z['cpu_start']==z['cpu_end']=='2'
  for k,v in f.items():assert z[k]==str(v)
text_reports={}
for v in ['actual','control','A','oldA']:
 raw=files['validation/'+v+'-asm.stdout'].decode();section=raw.split('Disassembly of section .text:\n',1)[1].split('Disassembly of section ',1)[0]
 words=[(int(m[1],16),m[2]) for line in section.splitlines() if (m:=re.match(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+',line))]
 assert all(words[i][0]==words[i-1][0]+4 for i in range(1,len(words))),v
 b=b''.join(bytes.fromhex(w)[::-1] for a,w in words);assert sha(b)==pub[v+'.text']['raw_sha256'];text_reports[v]={'bytes':len(b),'sha256':sha(b)}
assert text_reports['actual']==text_reports['control'] and text_reports['A']==text_reports['oldA']
report={'audit_status':'PASS','original_phase_status':'FAILED','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'revision':rev,'public_artifact_hashes_verified':len(seal),'executed_prefix_commands':2118,'registered_checks_passed':2117,'unstarted_commands':[x['name'] for x in manifest[2118:]],'command_kinds':dict(collections.Counter(x['kind'] for x in r['commands'])),'elapsed_seconds':r['elapsed_seconds'],'protected_binaries_unchanged':True,'text_reconstructed_from_public_encoded_instructions':text_reports,'finding':'Command2118 deliberately injected fabs sign fault aborted at earlier copied-next exact score assertion, not the registered current-score assertion. Original FAILED remains unchanged. No measurements. Full copied snapshot identity must be checked before and after any six-command continuation.'}
Path('experiments/ARM-MASK-FOLLOWUP-001/PREPARATION-FAILURE-ROOT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
