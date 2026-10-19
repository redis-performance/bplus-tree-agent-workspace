import ast,hashlib,importlib.util,json,pathlib,subprocess,sys,tempfile
arm=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads(p.read_text());freeze=read(arm/'execution-freeze.json')
assert sha(arm/'execution-freeze.json')=='52169964c692b8accb350efaeebfa95d7ca87832db306722114254ca40a6ffe4'
assert len(freeze['files'])==24
for n,h in freeze['files'].items():assert sha(arm/n)==h,n
for n,h in read(arm/'plan-freeze.json')['files'].items():assert sha(arm/n)==h,n
for p in arm.glob('*.py'):ast.parse(p.read_text())
e=read(arm/'expected.json');assert e['commit']=='13e459ff8800be3f02b6b45c87dd7b0c39453fa9'
for n,h in e['source_hashes'].items():assert hashlib.sha256(subprocess.check_output(['git','show',e['commit']+':'+n])).hexdigest()==h,n
orig=read(arm/'IMPORT-PROVENANCE.json');prefix=orig['origin_path']
for n,h in orig['original_sha256'].items():assert hashlib.sha256(subprocess.check_output(['git','show',orig['origin_commit']+':'+prefix+'/'+n])).hexdigest()==h,n
manifest=read(pathlib.Path(sys.argv[3]));assert manifest['commit']==e['commit'];assert manifest['binary_sha256_after']==e['aa_binary_sha256']=='330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc'
assert e['protected_binaries']['scratch/adapter-worktree-13e459ff8/build/adapter-requalification/btree-bench']==e['aa_binary_sha256'];assert len(e['protected_binaries'])==5
assert hashlib.sha256(subprocess.check_output(['git','show','d5105925e:experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/014-corrected-scan-profile/profile-scoped-fifo2.c'])).hexdigest()==e['scope_sha256']
cmdraw=subprocess.check_output(['git','show','234f70f44:'+prefix+'/commands.json']).decode().replace('amd-corrected-iterator-13e459ff8','arm-corrected-iterator-13e459ff8').replace('scratch/amd-adapter-requalification-13e459ff8/source','scratch/adapter-worktree-13e459ff8')
assert json.loads(cmdraw)==read(arm/'commands.json');assert len(read(arm/'commands.json'))==51
for n in ['aa-schedule.json','profile-schedule.json','known-control.c','known-oracle.py','known-control-expectations.json','profile-scoped-fifo2.c','profile_helpers.py','run-aa.py']:assert sha(arm/n)==orig['original_sha256'][n],n
spec=importlib.util.spec_from_file_location('review_arm_parser',arm/'arm_asm.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
valid='x: file format elf64-littleaarch64\n0000000000001000 <zbtreeIteratorNext>:\nx.c:4023\n 1000:\td503201f \tnop\n 1004:\td65f03c0 \tret\n'
tests=[]
with tempfile.TemporaryDirectory() as d:
 p=pathlib.Path(d)/'asm';p.write_text(valid);x=module.parse(p);assert x['zbtreeIteratorNext']['instructions'][4]['bytes']==['d65f03c0'];tests.append('native exact-word/source offset parse')
 for name,text in [('wrong architecture',valid.replace('elf64-littleaarch64','elf64-x86-64')),('short encoded word',valid.replace('d503201f','d50320')),('x86 split bytes',valid.replace('d503201f','d5 03 20 1f')),('unaligned IP',valid.replace(' 1004:',' 1006:')),('duplicate IP',valid.replace(' 1004:',' 1000:')),('negative offset',valid.replace(' 1004:',' 0ffc:')),('duplicate function',valid+valid.split('\n',1)[1])]:
  p.write_text(text)
  try:module.parse(p)
  except AssertionError:tests.append(name+' rejected')
  else:raise AssertionError(name)
result={'status':'no execution blocker found','reviewed_commit':'d5105925e','execution_sha256':sha(arm/'execution-freeze.json'),'frozen_files':24,'source_hashes_verified':len(e['source_hashes']),'imported_hashes_verified':len(orig['original_sha256']),'actual013_binary_sha256':e['aa_binary_sha256'],'protected_binary_pins':5,'command_manifest_records':51,'scientific_captures':6,'aa_processes':48,'local_parser_checks':tests,'scope':'local static/synthetic only; no runner or benchmark','limits':['I authored the imported AMD029 protocol; this is independent review of ARM adaptation, not an independently authored base harness','Mapping records exact instruction words and full-body differences, not automatic causal or runtime equivalence','Root idle handoff and phase grants still required']}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
