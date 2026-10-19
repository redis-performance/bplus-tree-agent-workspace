"""Independent ARM024 public-artifact reconstruction; imports no worker analyzers."""
import collections,csv,datetime,hashlib,json,pathlib,re,sys
root=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);p=root/'profile';read=lambda f:json.loads(f.read_text());sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();seal=read(root/'profile-evidence-seal.json');frozen=read(root/'execution-freeze.json');expected=read(root/'expected.json');checks=[]
assert sha(root/'execution-freeze.json')=='52169964c692b8accb350efaeebfa95d7ca87832db306722114254ca40a6ffe4'
for n,h in frozen['files'].items():assert sha(root/n)==h,n
for n,h in seal['files'].items():assert sha(root/n)==h,n
publication=read(p/'PUBLICATION.json');raw_unavailable={}
for n,x in publication.items():
 if 'public_sha256' in x:assert sha(p/n)==x['public_sha256'],n
 else:raw_unavailable[n]=x['raw_sha256']
complete=read(p/'complete.json');build=read(p/'build-freeze.json');assert complete['status']=='complete' and complete['elapsed_seconds']<600
assert complete['source_hashes_after']==build['source_hashes']==expected['source_hashes']
assert complete['protected_binaries_before']==complete['protected_binaries_after']==expected['protected_binaries']
assert complete['binary_hashes_after']==build['binary_sha256'];assert build['commit']==expected['commit'];assert build['scope_sha256']==sha(root/'profile-scoped-fifo2.c')==expected['scope_sha256'];assert build['known_source_sha256']==sha(root/'known-control.c');assert build['cpu_affinity']==[2]
assert complete['execution_freeze_sha256']==sha(root/'execution-freeze.json');assert complete['raw_data_sha256']==raw_unavailable and len(raw_unavailable)==7
assert 'clang version 18.1.3' in build['compiler'] and 'aarch64' in build['compiler']
commands=read(root/'commands.json');runs=read(p/'processes.json');assert len(runs)==len(commands)==51
for i,(r,c) in enumerate(zip(runs,commands)):
 assert all(r[k]==v for k,v in c.items()),r['name'];assert r['returncode']==0
 t0=datetime.datetime.fromisoformat(r['started_utc']);t1=datetime.datetime.fromisoformat(r['finished_utc']);assert t0<=t1 and (t1-t0).total_seconds()<=121
 if i:assert datetime.datetime.fromisoformat(runs[i-1]['finished_utc'])<=t0
 for ext in ['stdout','stderr']:assert (p/(r['name']+'.'+ext)).exists()
assert (datetime.datetime.fromisoformat(runs[-1]['finished_utc'])-datetime.datetime.fromisoformat(runs[0]['started_utc'])).total_seconds()<=600
assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',(p/'original43.stdout').read_text())
semantics=[]
def row(name,n,ops,seed):
 rows=list(csv.DictReader((p/(name+'.stdout')).read_text().splitlines()));assert len(rows)==1;x=rows[0];traversals=(ops+n-1)//n
 want=dict(case='iterate',size=n,requested_ops=ops,member_bytes=16,seed=seed,operations=traversals*n,traversals=traversals,checksum=traversals*n*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
 for k,v in want.items():assert x[k]==str(v),(name,k)
 assert int(x['elapsed_ns'])>0;semantics.append(name);return x
for seed in [1,2,3]:
 for n in [100000,1000000]:
  label=f'iterate-n{n}-s{seed}';rows=[row(label+'-'+mode,n,50000000,seed) for mode in ['original','disabled','record']];assert len({x['tree_bytes'] for x in rows})==1;assert rows[0]==complete['controls'][label]
ss=[row('iterate-san-'+mode,1000,2001,101) for mode in ['original','disabled']];assert ss[0]['tree_bytes']==ss[1]['tree_bytes']
z=row('iterate-disabled-zero',100000,50000000,1);assert z['tree_bytes']==complete['controls']['iterate-n100000-s1']['tree_bytes']
known_expected=read(root/'known-control-expectations.json')['expected_stdout']
def affine(a,b,seed,n):
 mask=(1<<64)-1;ra,rb=1,0
 while n:
  if n&1:ra,rb=(a*ra)&mask,(a*rb+b)&mask
  a,b=(a*a)&mask,(a*b+b)&mask;n>>=1
 return (ra*seed+rb)&mask
assert known_expected=={'rounds':100000000,'before':f'{affine(6364136223846793005,1442695040888963407,1,100000000):016x}','inside':f'{affine(2862933555777941757,3037000493,3,100000000):016x}','after':f'{affine(6364136223846793005,1442695040888963407,7,100000000):016x}'}
for a,b in [(6364136223846793005,1442695040888963407),(2862933555777941757,3037000493)]:
 for count in [0,1,2,7,16,31,99]:
  v=3
  for _ in range(count):v=(a*v+b)&((1<<64)-1)
  assert v==affine(a,b,3,count)
for name in ['known-plain','known-disabled-stat','known-enabled-stat','known-record']:assert read(p/(name+'.stdout'))==known_expected
counter_results={}
for n in ['iterate-disabled','known-disabled','known-enabled']:
 rows=list(csv.reader(x for x in (p/(n+'.stat')).read_text().splitlines() if x and not x.startswith('#')));counts={x[2]:x[0].strip() for x in rows};assert len(rows)==4 and set(counts)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
 if n.endswith('disabled'):assert all(x in ['0','<not counted>'] for x in counts.values())
 else:assert all(float(counts[x])>0 for x in ['cycles:u','instructions:u','branches:u']) and float(counts['branch-misses:u'])>=0
 counter_results[n]=counts

def parse_samples(text):
 result=[]
 for b in re.split(r'\n\s*\n',text.strip()):
  lines=b.splitlines();period=int(lines[0]);frames=[]
  for line in lines[1:]:
   m=re.fullmatch(r'\s*([a-f0-9]+)\s+(.+)',line);assert m,line;frames.append((int(m[1],16),m[2]))
  assert period>=0 and frames;top=frames[0][0];same=[sym for ip,sym in frames if ip==top];physical=[x for x in same if not x.endswith(' (inlined)')];assert physical
  sym=physical[-1];parts=re.fullmatch(r'(.+)\+0x([0-9a-f]+)',sym);exclusive=re.sub(r'\+0x[0-9a-f]+(?: \(inlined\))?$','',same[0]);result.append(dict(period=period,exclusive=exclusive,physical=parts[1] if parts else sym,offset=int(parts[2],16) if parts else None))
 return result

def report(name,rows):
 text=(p/(name+'-report.stdout')).read_text();lost=int(re.search(r'Total Lost Samples:\s*(\d+)',text)[1]);label=re.search(r'# Samples:\s*([\d,]+)\s+of event',text)[1];period=int(re.search(r'Event count \(approx\.\):\s*(\d+)',text)[1]);assert int(label.replace(',',''))==len(rows);assert sum(x['period'] for x in rows)==period
 return {'events':len(rows),'period':period,'lost':lost}
synthetic=parse_samples('100\n 100 decoder+0x4 (inlined)\n 100 zbtreeIteratorNext+0x4\n 200 known_work+0x8\n\n5\n 300 [unknown]\n 400 outside_work+0x4\n')
assert synthetic[0]['exclusive']=='decoder' and synthetic[0]['physical']=='zbtreeIteratorNext' and synthetic[1]['physical']=='[unknown]'
known_rows=parse_samples((p/'known-samples.stdout').read_text());known=report('known',known_rows);known['known_events']=sum(x['physical']=='known_work' for x in known_rows);known['outside_events']=sum(x['physical']=='outside_work' for x in known_rows);known['known_period']=sum(x['period'] for x in known_rows if x['physical']=='known_work');known['known_pct']=100*known['known_period']/known['period'];assert known['known_events']>=20 and known['outside_events']==0 and known['known_pct']>80
# Parse AArch64 words independently, without importing the worker's parser.
def assembly(path):
 text=path.read_text();assert 'file format elf64-littleaarch64' in text;funcs={};current=None
 for line in text.splitlines():
  m=re.fullmatch(r'([0-9a-f]+) <([^>]+)>:',line)
  if m:current=m[2];assert current not in funcs;funcs[current]={'start':int(m[1],16),'words':{}};continue
  m=re.match(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)',line)
  if m:
   assert current;ip=int(m[1],16);off=ip-funcs[current]['start'];assert ip%4==0 and off>=0 and off not in funcs[current]['words'];funcs[current]['words'][off]={'word':m[2],'assembly':m[3]}
 return funcs
asm={n:assembly(p/(n+'-full-asm.stdout')) for n in ['original','profile','timing']};captures=[];totals={};mapped_rows={}
for seed in [1,2,3]:
 for n in [100000,1000000]:
  label=f'iterate-n{n}-s{seed}';rows=parse_samples((p/(label+'-samples.stdout')).read_text());r=report(label,rows);captures.append(dict(size=n,seed=seed,**r));g=totals.setdefault(str(n),{'events':0,'period':0,'lost':0,'exclusive':collections.Counter(),'exclusive_events':collections.Counter(),'mapping':collections.Counter()});g['events']+=r['events'];g['period']+=r['period'];g['lost']+=r['lost']
  for x in rows:
   g['exclusive'][x['exclusive']]+=x['period'];g['exclusive_events'][x['exclusive']]+=1;entries={a:v.get(x['physical'],{}).get('words',{}).get(x['offset']) for a,v in asm.items()};cat='missing'
   if all(entries.values()):
    eq=len({v['word'] for v in entries.values()})==1;cat='equal' if eq else 'different';key=x['physical']+'+'+hex(x['offset']);q=mapped_rows.setdefault(key,{'events':0,'period':0,'equal':eq,'words':{a:v['word'] for a,v in entries.items()}});q['events']+=1;q['period']+=x['period']
    if x['physical'].startswith('zbt'):g['mapping']['tree_'+cat+'_events']+=1;g['mapping']['tree_'+cat+'_period']+=x['period']
   g['mapping'][cat+'_events']+=1;g['mapping'][cat+'_period']+=x['period']
for g in totals.values():assert sum(g['exclusive'].values())==g['period'];g['exclusive_pct']={k:100*v/g['period'] for k,v in g['exclusive'].items()};g['mapping_pct']={k:100*v/g['period'] for k,v in g['mapping'].items() if k.endswith('_period')}
offsets=set.union(*(set(x['zbtreeIteratorNext']['words']) for x in asm.values()));diff=[]
for o in sorted(offsets):
 vals={k:v['zbtreeIteratorNext']['words'].get(o) for k,v in asm.items()}
 if any(v is None for v in vals.values()) or len({v['word'] for v in vals.values() if v})!=1:diff.append({'offset':hex(o),'entries':vals,'sampled':('zbtreeIteratorNext+'+hex(o)) in mapped_rows})
# Compare output data only after independent reconstruction, never import analyzer code.
audit=read(p/'audit.json');mapping=read(p/'code-map.json')
for n,g in totals.items():
 a=audit['summary'][n];assert a['events']==g['events'] and a['total_period']==g['period'] and a['lost']==g['lost'];assert a['exclusive_period']==dict(g['exclusive']) and a['exclusive_events']==dict(g['exclusive_events']);m=mapping['groups']['iterate/'+n]
 for cat in ['equal','different','missing']:
  for unit in ['events','period']:assert m[(('mapped_' if cat!='missing' else '')+cat+'_'+unit)]==g['mapping'].get(cat+'_'+unit,0)
 for cat in ['equal','different']:
  for unit in ['events','period']:assert m['tree_'+cat+'_'+unit]==g['mapping'].get('tree_'+cat+'_'+unit,0)
for k,v in mapped_rows.items():
 m=mapping['sampled_instruction_map'][k];assert (m['events'],m['period'],m['all_three_encoded_bytes_equal'])==(v['events'],v['period'],v['equal']);assert m['bytes']==v['words']
assert set(mapped_rows)==set(mapping['sampled_instruction_map']);assert mapping['full_tree_body_comparison']['zbtreeIteratorNext']['different_entries']==len(diff);assert mapping['actual_timing_binary_sha256']==expected['aa_binary_sha256']
result={'status':'pass','reviewed_revision':'4e43c9f59','command_records':len(runs),'public_seal_hashes':len(seal['files']),'raw_perf_hashes_attested_not_independently_rehashed':raw_unavailable,'semantic_rows':len(semantics),'arithmetic_checks':14,'public_artifact_hashes':sum('public_sha256' in x for x in publication.values()),'counter_controls':counter_results,'known':known,'scientific_samples':sum(g['events'] for g in totals.values()),'captures':captures,'totals':totals,'mapped_physical_instruction_locations':len(mapped_rows),'full_iterator_body_words':len(offsets),'body_differences':diff,'source_selection':'NONE','limits':['No runner access or new measurement','Imported AMD protocol author reviewing ARM adaptation and raw evidence; root separately reviews','Raw perf files private; public full text verified','Exact instruction words do not establish removable cycle cost or whole-runtime equivalence','AA remains separately gated and has not run']};out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','command_records','public_seal_hashes','semantic_rows','known','scientific_samples','full_iterator_body_words','body_differences']},indent=2))
