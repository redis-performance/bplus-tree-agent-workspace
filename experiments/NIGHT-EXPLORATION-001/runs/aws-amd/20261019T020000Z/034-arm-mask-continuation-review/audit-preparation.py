import pathlib,json,hashlib,subprocess,itertools,collections,ast,sys,re
p=pathlib.Path(sys.argv[1]);j=lambda n:json.loads((p/n).read_text());sha=lambda b:hashlib.sha256(b).hexdigest();f=j('preparation-freeze.json');e=j('expected.json');c=j('validation-commands.json')
for n,h in f['files'].items():assert sha((p/n).read_bytes())==h,n
for n,h in j('plan-freeze.json')['files'].items():assert sha((p/n).read_bytes())==h,n
for n,h in e['source_hashes'].items():assert sha(subprocess.check_output(['git','show',e['commit']+':'+n]))==h,n
assert len(c)==2124 and len({x['name'] for x in c})==2124
counts=collections.Counter(x['kind'] for x in c);assert counts==dict(archive=1,plain=45,original43=4,modes=512,modes5=1536,oracle=12,negative=14)
for src,build in itertools.product(['control','A'],['native','san']):
 h4=[x for x in c if x['cwd']=='<job>/'+src and x['kind']=='modes' and x['command'][0]=='build/'+build+'/modes'];h5=[x for x in c if x['cwd']=='<job>/'+src and x['kind']=='modes5' and x['command'][0]=='build/'+build+'/modes5'];assert len(h4)==128 and len(h5)==384
 keys=lambda x:(x['fixture']['member_bytes'],x['fixture']['encoding'],x['fixture']['direction'],x['fixture']['mask'])
 assert {keys(x) for x in h4}==set(itertools.product([16,320],['integer','fraction','wide','zero'],['forward','reverse'],range(8)))
 assert {(x['fixture']['size'],*keys(x),x['fixture']['construction']) for x in h5}==set(itertools.product([32,129],[16,320],['integer','alternating-zero'],['forward','reverse'],range(8),['shuffled','ascending','descending']))
 for x in h5:
  fi=x['fixture'];assert fi['seed']==1502 and fi['requested_ops']==2*fi['size']+1
  argv=dict(zip(x['command'][1::2],x['command'][2::2]));assert all(argv['--'+k.replace('_','-')]==str(v) for k,v in fi.items() if k!='requested_ops');assert argv['--ops']==str(fi['requested_ops'])
for n,h in e['oracles'].items():assert sha((p/'oracles'/n).read_bytes())==h
for n,v in e['faults'].items():
 assert sha((p/'faults'/(n+'.patch')).read_bytes())==v['patch'];neg=[x for x in c if x['kind']=='negative' and x['cwd']=='<job>/fault-'+n];assert len(neg)==2 and all(x['needles'] and x['match'] in ['any','all'] for x in neg)
assert len(e['protected_binaries'])==6 and e['candidate_binary_sha256'] in e['protected_binaries'].values()
for n in ['run-validation.py','apply_exact.py']:ast.parse((p/n).read_text())
base=subprocess.check_output(['git','show',e['commit']+':src/zset_btree.c']).decode();patch=(p/'candidate.patch').read_text();old='        if (bits < 64)\n            delta &= (UINT64_C(1) << bits) - 1;';new='        delta &= UINT64_MAX >> (64 - bits);';assert base.count(old)==1 and sha(base.replace(old,new).encode())==e['candidate_source_sha256'];assert sha(patch.encode())==e['candidate_patch_sha256']
print(json.dumps({'status':'preparation_static_review_pass','revision':'ca16799da','inputs':len(f['files']),'commands':len(c),'counts':dict(counts),'original_source_hashes':len(e['source_hashes']),'oracles':len(e['oracles']),'fault_families':len(e['faults']),'protected_binaries':6,'candidate_source_exact':True,'native_or_sanitizer_work_executed':False,'performance_grant':False,'limits':['Root must bind full600s fresh lease helper invocation','Failure needs separate postidentity/idle proof','Correctness result and timing drivers still require review']},indent=2))
