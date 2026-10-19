import csv,json,hashlib,re,subprocess,sys
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime
P=Path(sys.argv[1]);O=Path(sys.argv[2]);R=P/'profile'
sha=lambda b:hashlib.sha256(b).hexdigest()
J=lambda n:json.loads((P/n).read_text())
pub=J('profile/PUBLICATION.json'); sealed=0
for n,v in pub.items():
 if 'public_sha256' in v:
  assert sha((R/n).read_bytes())==v['public_sha256'],n;sealed+=1
freeze=J('execution-freeze.json')
for n,h in freeze['files'].items(): assert sha((P/n).read_bytes())==h,n
build=J('profile/build-freeze.json');done=J('profile/complete.json')
assert build['commit']==freeze['source_commit'];assert build['cpu_affinity']==[2]
for n,h in build['source_hashes'].items(): assert sha(subprocess.check_output(['git','show',build['commit']+':'+n]))==h,n
assert build['source_hashes']==done['source_hashes_after']
assert build['binary_sha256']==done['binary_hashes_after']
assert done['protected_binaries_before']==done['protected_binaries_after']
assert freeze['actual_timing_binary_sha256'] in done['protected_binaries_before'].values()
for n,h in done['raw_data_sha256'].items():assert pub[n]['raw_sha256']==h
assert len(done['raw_data_sha256'])==7
commands=J('commands.json');process=J('profile/processes.json');assert len(commands)==len(process)==51
last=None
for e,r in zip(commands,process):
 for k in ['name','command','cwd','profile_env']: assert r[k]==e[k],(r['name'],k)
 assert r['returncode']==0
 a=datetime.fromisoformat(r['started_utc']);b=datetime.fromisoformat(r['finished_utc']);assert a<=b
 if last:assert last<=a
 last=b
assert (last-datetime.fromisoformat(process[0]['started_utc'])).total_seconds()<600
assert len(re.findall(r'^\d+ - .*PASSED', (R/'original43.stdout').read_text(),re.M))==43

def row(name,n,seed,ops=50000000):
 a=list(csv.DictReader((R/(name+'.stdout')).read_text().strip().splitlines()));assert len(a)==1;r=a[0]
 for k,v in dict(case='iterate',size=n,seed=seed,requested_ops=ops,member_bytes=16,operations=((ops+n-1)//n)*n,traversals=(ops+n-1)//n,warmup_passes=1,cpu_start=2,cpu_end=2,checksum=((ops+n-1)//n)*n*(n-1)//2).items():assert r[k]==str(v),(name,k,r[k],v)
 return r
semantic=[]
for seed in [1,2,3]:
 for n in [100000,1000000]:
  name=f'iterate-n{n}-s{seed}';rr=[row(name+'-'+mode,n,seed) for mode in ['original','disabled','record']]
  assert len({r['tree_bytes'] for r in rr})==1
  semantic.append(dict(size=n,seed=seed,tree_bytes=int(rr[0]['tree_bytes']),checksum=int(rr[0]['checksum'])))
row('iterate-disabled-zero',100000,1)
a=row('iterate-san-original',1000,101,2001);b=row('iterate-san-disabled',1000,101,2001);assert a['tree_bytes']==b['tree_bytes']
expect=dict(rounds=100000000,before='576d9c942c494901',inside='dcbca4dc3edf4303',after='6557d69def72a107')
for n in ['known-plain','known-disabled-stat','known-enabled-stat','known-record']: assert json.loads((R/(n+'.stdout')).read_text())==expect
stats={}
for name,enabled in [('known-disabled',False),('iterate-disabled',False),('known-enabled',True)]:
 d={}
 for line in (R/(name+'.stat')).read_text().splitlines():
  if not line or line.startswith('#'):continue
  cols=line.split(',');v=cols[0];event=cols[2];assert event in ['cycles:u','instructions:u','branches:u','branch-misses:u'];assert event not in d
  if enabled:assert v.isdigit() and int(v)>=(0 if event=='branch-misses:u' else 1)
  else:assert v in ['0','<not counted>']
  d[event]=v
 assert len(d)==4;stats[name]=d

def samples(name):
 out=[]
 for chunk in re.split(r'\n\s*\n',(R/(name+'-samples.stdout')).read_text().strip()):
  lines=chunk.splitlines();assert re.fullmatch(r'\s*\d+\s*',lines[0]);period=int(lines[0]);frames=[]
  for line in lines[1:]:
   m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+?)\s*',line);assert m,line;frames.append((int(m[1],16),m[2]))
  assert frames
  same=[f for f in frames if f[0]==frames[0][0]]
  physical=next((f[1] for f in reversed(same) if not f[1].endswith(' (inlined)')),same[-1][1])
  exclusive=same[0][1].removesuffix(' (inlined)')
  out.append(dict(period=period,physical=physical,exclusive=exclusive,ip=frames[0][0]))
 report=(R/(name+'-report.stdout')).read_text()
 assert int(re.search(r'Total Lost Samples:\s*(\d+)',report)[1])==0
 assert int(re.search(r'^# Samples:\s*(\d+)\s',report,re.M)[1])==len(out)
 assert int(re.search(r'Event count \(approx\.\):\s*(\d+)',report)[1])==sum(x['period'] for x in out)
 return out
known=samples('known');kp=sum(x['period'] for x in known if x['physical'].startswith('known_work+'));kn=sum(x['physical'].startswith('known_work+') for x in known);kt=sum(x['period'] for x in known)
assert kn>=20 and kp/kt>.8 and not any(x['physical'].startswith('outside_work+') for x in known)

def asm(name):
 funcs={};cur=None;source=None
 for l in (R/(name+'-full-asm.stdout')).read_text().splitlines():
  m=re.match(r'^([0-9a-f]+) <([^>]+)>:',l)
  if m:cur=m[2];funcs[cur]={'start':int(m[1],16),'instructions':{}};source=None;continue
  m=re.search(r'/([^/]+\.[ch]):(\d+)(?:\s|$)',l)
  if m:source=m[1]+':'+m[2]
  m=re.match(r'^\s*([0-9a-f]+):\s*((?:[0-9a-f]{2}(?:\s+|$))+)(.*)$',l)
  if m and cur:
   # objdump continuation lines are retained as bytes at their offset.
   addr=int(m[1],16);b=' '.join(m[2].split());funcs[cur]['instructions'][addr-funcs[cur]['start']]={'bytes':b,'asm':m[3].strip(),'source':source,'address':addr}
 return funcs
assemblies={name:asm(name) for name in ['profile','original','timing']}
bycapture={};groups=defaultdict(lambda:Counter());details={};excl=defaultdict(Counter)
for seed in [1,2,3]:
 for n in [100000,1000000]:
  name=f'iterate-n{n}-s{seed}';ss=samples(name);c=Counter()
  for s in ss:
   c['events']+=1;c['period']+=s['period'];excl[str(n)][s['exclusive'].split('+')[0]]+=s['period']
   m=re.fullmatch(r'(.+)\+0x([0-9a-f]+)',s['physical']);record=[]
   if m:
    symbol=m[1];offset=int(m[2],16)
    for tag,a in assemblies.items():record.append(a.get(symbol,{}).get('instructions',{}).get(offset))
   else:symbol=s['physical'];offset=None
   exists=len(record)==3 and all(record)
   equal=exists and len({r['bytes'] for r in record})==1
   category='equal' if equal else ('different' if exists else 'missing')
   c[category+'_events']+=1;c[category+'_period']+=s['period']
   tree=symbol.startswith('zbt')
   if tree:
    assert exists and equal,(symbol,offset,record)
    c['tree_events']+=1;c['tree_period']+=s['period']
   key=s['physical'];d=details.setdefault(key,dict(events=0,period=0,category=category,records=dict(zip(assemblies,record)) if record else {},tree=tree));assert d['category']==category
   d['events']+=1;d['period']+=s['period']
  bycapture[name]=dict(c);groups[str(n)].update(c)
assert sum(g['events'] for g in groups.values())==1218
# A full function comparison is separate from sampled-instruction equivalence.
f='zbtreeIteratorNext'; bodies={k:v[f]['instructions'] for k,v in assemblies.items()}; offsets=set.union(*(set(b) for b in bodies.values()));diff=[]
for off in sorted(offsets):
 vals={k:b.get(off,{}).get('bytes') for k,b in bodies.items()}
 if len(set(vals.values()))!=1:diff.append(dict(offset=hex(off),bytes=vals))
# Cross-check operator summaries only after independent reconstruction.
cm=J('profile/code-map.json')
for n,c in groups.items():
 reported=cm['groups']['iterate/'+n]
 for mine,theirs in [('events','events'),('period','total_period'),('equal_events','mapped_equal_events'),('equal_period','mapped_equal_period'),('different_events','mapped_different_events'),('different_period','mapped_different_period'),('missing_events','missing_events'),('missing_period','missing_period'),('tree_events','tree_equal_events'),('tree_period','tree_equal_period')]:assert c[mine]==reported[theirs],(n,mine)
for key,d in details.items():
 if d['category']=='missing':continue
 r=cm['sampled_instruction_map'][key];assert r['events']==d['events'] and r['period']==d['period'];assert r['all_three_encoded_bytes_equal']==(d['category']=='equal')
 for tag,x in d['records'].items():assert r['bytes'][tag]==x['bytes'];assert int(r['addresses'][tag],16)==x['address'];assert r['source_lines'][tag]==x['source']
result=dict(status='PASS',reviewer='/root/aws_arm',input_revision='9230fb3d4',execution_freeze_sha256=sha((P/'execution-freeze.json').read_bytes()),public_hashes_verified=sealed,execution_freeze_files_verified=len(freeze['files']),source_hashes_verified=len(build['source_hashes']),commands=51,serial=True,original_tests=43,semantic_cells=semantic,protected_identity_manifest_verified=True,live_binary_read=False,raw_perf_binary_hashes_manifest_verified=7,raw_perf_binary_bytes_read=False,stats=stats,known=dict(events=len(known),known_events=kn,period=kt,known_period=kp,known_period_pct=100*kp/kt,outside_events=0),captures=bycapture,groups={k:dict(v) for k,v in groups.items()},exclusive_periods={k:dict(v) for k,v in excl.items()},sampled_mapping=details,full_iterator_body=dict(offset_entries=len(offsets),different_entries=len(diff),differences=diff),losses_reported=0,limitations=['Published exported samples/assembly independently parsed; raw perf binaries and live runner binaries not read.','Manifest identity is not an independent live identity measurement.','Same-offset instruction equivalence alone does not establish caller equivalence; differing and missing caller mappings retained.','PMU edge/control/unknown samples remain in full denominators; zero reported losses does not prove absence of sampling error.','Baseline profile is not speed or removable-cost evidence.'])
O.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','public_hashes_verified','known','groups','full_iterator_body']},indent=2))
