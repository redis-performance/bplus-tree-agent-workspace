import pathlib,json,hashlib,datetime,csv,re,collections,sys
p=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);v=p/'validation';j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();e=j(p/'expected.json');f=j(p/'execution-freeze.json');r=j(v/'result.json');commands=j(p/'validation-commands.json');pub=j(v/'PUBLICATION.json')
for n,h in f['files'].items():assert sha(p/n)==h
for n,h in pub.items():
 if 'public_sha256' in h:assert sha(v/n)==h['public_sha256'],n
assert r['status']=='correctness_complete_static_gate_pending' and r['elapsed_seconds']<=600 and len(r['commands'])==570
assert r['actual_sources_before']==r['actual_sources_after']==e['source_hashes'];assert r['protected_before']==r['protected_after']==e['protected_binaries'];assert r['actual_binary_before']==r['actual_binary_after']==e['aa_binary_sha256'];assert r['snapshots_before']==r['snapshots_after'];assert r['snapshots_after']['A']['src/zset_btree.c']==e['candidate_source_sha256'];assert r['execution_freeze_sha256']==sha(p/'execution-freeze.json');assert r['text_sha256']['actual']==r['text_sha256']['control']
for variant,files in r['snapshots_after'].items():
 for n,h in e['source_hashes'].items():
  if n!='src/zset_btree.c':assert files[n]==h
 for n,h in e['oracles'].items():assert files[('bench/' if n=='iterator_modes.c' else 'tests/')+n]==h
counts=collections.Counter()
for i,(x,c) in enumerate(zip(r['commands'],commands)):
 assert all(x[k]==v for k,v in c.items()) and x['checked'];t0=datetime.datetime.fromisoformat(x['started_utc']);t1=datetime.datetime.fromisoformat(x['finished_utc']);assert t0<=t1 and (t1-t0).total_seconds()<=121
 if i:assert datetime.datetime.fromisoformat(r['commands'][i-1]['finished_utc'])<=t0
 stdout=(v/(x['name']+'.stdout')).read_text();stderr=(v/(x['name']+'.stderr')).read_text();counts[x['kind']]+=1
 if x['kind']=='negative':
  assert x['returncode'] not in [0,124];found=[s in stderr for s in x['needles']];assert all(found) if x['match']=='all' else any(found)
 else:assert x['returncode']==0
 if x['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',stdout)
 if x['kind']=='oracle':assert 'PASS' in stdout
 if x['kind']=='modes':
  rows=list(csv.DictReader(stdout.splitlines()));assert len(rows)==1;z=rows[0]
  vals=dict(size=129,requested_ops=259,operations=387,traversals=3,seed=7103,cpu_start=2,cpu_end=2,**x['fixture']);assert all(z[k]==str(val) for k,val in vals.items());assert z['checksum']==z['expected_checksum']
def asm(n):
 fs={};name=None
 for line in (v/(n+'-asm.stdout')).read_text().splitlines():
  m=re.fullmatch(r'([0-9a-f]+) <([^>]+)>:',line)
  if m:name=m[2];fs[name]={'start':int(m[1],16),'ins':{}}
  m=re.match(r'\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)',line)
  if m and name:fs[name]['ins'][int(m[1],16)-fs[name]['start']]={'word':m[2],'asm':m[3].split('//')[0].strip()}
 return fs
asmset={n:asm(n) for n in ['actual','control','A']};base=asmset['control']['zbtreeIteratorNext'];cand=asmset['A']['zbtreeIteratorNext'];assert asmset['actual']['zbtreeIteratorNext']['ins']==base['ins'];assert len(base['ins'])==114 and len(cand['ins'])==113
bmask=[base['ins'][x] for x in [0x100,0x104,0x108,0x10c]];amask=[cand['ins'][x] for x in [0x100,0x104,0x108]];assert [x['asm'].split()[0] for x in bmask]==['mov','cmp','lsl','csinv'];assert [x['asm'].split()[0] for x in amask]==['neg','mov','lsr'];assert base['ins'][0x114]['word']==cand['ins'][0x110]['word'];assert base['ins'][0x110]['word']==cand['ins'][0x10c]['word']
def trace(fn,taken):
 off=0;path=[]
 while True:
  x=fn['ins'][off]['asm'];path.append({'offset':hex(off),'asm':x});op=x.split()[0]
  if op=='ret':return path
  if op=='b' or op.startswith('b.') or op in ['cbz','cbnz','tbz','tbnz']:
   target=int(re.search(r'([0-9a-f]+) <',x)[1],16)-fn['start']
   if op=='b' or off in taken:off=target;continue
  assert op not in ['bl','blr','br'];off+=4;assert len(path)<200
paths={}
for label,extras in [('shift0',{0xdc}),('shift_nonzero_no_cross',{0xec}),('shift_nonzero_cross',set())]:
 b=trace(base,{0x10,0xb0,0x144,0x160}|extras);a=trace(cand,{0x10,0xb0,0x140,0x15c}|extras);assert len(a)==len(b)-1;paths[label]={'baseline_count':len(b),'candidate_count':len(a),'baseline':b,'candidate':a}
shared={}
for name in ['zbtreeIteratorNext','zbtreeScore','zbtreeScoreRaw','zbtreeRank','zbtreeFindForAdd','zbtIndexScanSlot']:
 b=asmset['control'][name]['ins'];a=asmset['A'][name]['ins'];cb=collections.Counter(x['asm'].split()[0] for x in b.values());ca=collections.Counter(x['asm'].split()[0] for x in a.values());branches=lambda c:sum(n for k,n in c.items() if k.startswith('b.') or k in ['cbz','cbnz','tbz','tbnz']);loads=lambda c:{k:n for k,n in c.items() if k.startswith(('ld','st'))};assert branches(cb)==branches(ca);assert loads(cb)==loads(ca)
 shared[name]={'baseline_instructions':len(b),'candidate_instructions':len(a),'conditional_branches':branches(cb),'memory_mnemonics':loads(cb),'mnemonic_changes':{k:[cb[k],ca[k]] for k in cb.keys()|ca.keys() if cb[k]!=ca[k]}}
result={'status':'validation_and_iterator_static_gate_pass','revision':'d99bc1077','public_hashes_verified':sum('public_sha256' in x for x in pub.values()),'commands':dict(counts),'text_sha256':r['text_sha256'],'timing_binary_sha256':{'baseline':e['aa_binary_sha256'],'candidate':r['binary_sha256']['A']},'assembly_public_sha256':{n:sha(v/(n+'-asm.stdout')) for n in asmset},'assembly_raw_sha256':{n:pub[n+'-asm.stdout']['raw_sha256'] for n in asmset},'baseline_mask_instructions':bmask,'candidate_mask_instructions':amask,'ordinary_paths':paths,'shared_callers':shared,'limits':['Instruction counts are not cycles or performance evidence','Memory/branch mnemonic parity is structural evidence, supplemented by explicit source/operand review','Raw .text identity attested by frozen successful driver, not reconstructed from normalized text','Separate root timing grant required; dissent NONE unchanged']};out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['ordinary_paths','baseline_mask_instructions','candidate_mask_instructions']},indent=2))
