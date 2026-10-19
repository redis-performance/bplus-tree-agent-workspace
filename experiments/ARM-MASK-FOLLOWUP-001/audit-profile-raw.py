"""Independent immutable provenance, semantics, PMU and sample-accounting audit.
Physical-byte mapping and known-work arithmetic also require AMD independent review.
"""
import subprocess,tarfile,io,json,csv,hashlib,datetime,decimal,collections,sys,re
from pathlib import Path
D=decimal.Decimal;rev=sys.argv[1];prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/029-mask-matched-profile/'
with tarfile.open(fileobj=io.BytesIO(subprocess.check_output(['git','archive',rev,prefix]))) as t:f={m.name[len(prefix):]:t.extractfile(m).read() for m in t if m.isfile()}
j=lambda n:json.loads(f[n]);sha=lambda b:hashlib.sha256(b).hexdigest();txt=lambda n:f[n].decode()
freeze=j('execution-freeze.json');e=j('expected.json');contracts=j('commands.json');r=j('profile/result.json');seal=j('profile-evidence-seal.json');claim=j('profile/audit.json');valid=j('profile/profile-validity.json')
assert sha(f['execution-freeze.json'])=='ecb0a87e282c93305fe77435ea264b9646bff79a3578623f763e81b0533cf1fe'
for n,h in freeze['files'].items():assert sha(f[n])==h
for n,h in seal.items():assert sha(f[n])==h
pub=j('profile/PUBLICATION.json')
for n,x in pub.items():
 if 'public_sha256' in x:assert sha(f['profile/'+n])==x['public_sha256']
 else:assert n.endswith('.data')
assert r['status']=='complete' and r['cpu']==2 and len(r['commands'])==len(contracts)==104 and 0<r['elapsed_seconds']<=600
assert r['execution_freeze_sha256']==sha(f['execution-freeze.json'])
assert r['protected_before']==r['protected_after']==e['protected_binaries']
assert r['actual_sources_before']==r['actual_sources_after'] and r['sources_before']==r['sources_after'] and r['binaries_before']==r['binaries_after']
for v in ['control','A']:
 x=dict(e['source_hashes']);x['src/zset_btree.c']=e['candidate_source_sha256'] if v=='A' else x['src/zset_btree.c'];assert r['actual_sources_before'][v]==x
 x.update({'bench/profile-scoped-fifo2.c':e['scope_sha256'],'bench/known-control.c':sha(f['known-control.c'])});assert r['sources_before'][v]==x
start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);deadline=datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc)
assert 0<=(end-start).total_seconds()<=600 and end<=deadline and(deadline-start).total_seconds()>=600
previous=start;refs={};counters={};warnings=[];semantics=0
for c,z in zip(contracts,r['commands']):
 assert all(z[k]==v for k,v in c.items()) and z['returncode']==0 and z['checked']
 a=datetime.datetime.fromisoformat(z['started_utc']);b=datetime.datetime.fromisoformat(z['finished_utc']);assert previous<=a<=b<=end and(b-a).total_seconds()<=120;previous=b
 out=txt('profile/'+z['name']+'.stdout');err=txt('profile/'+z['name']+'.stderr')
 if err.strip():warnings.append({'command':z['name'],'stderr':err})
 if z['kind']=='compiler':assert 'clang version 18.1.3' in out and 'aarch64' in out
 if z['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',out)
 if z['kind'].startswith('tree'):
  rows=list(csv.DictReader(out.splitlines()));assert len(rows)==1;y=rows[0];q=z['fixture'];n=q['size'];laps=(q['requested_ops']+n-1)//n
  expect=dict(q,operations=n*laps,traversals=laps,checksum=n*(n-1)//2*laps,warmup_passes=1,cpu_start=2,cpu_end=2)
  assert all(y[k]==str(v) for k,v in expect.items());assert int(y['elapsed_ns'])>0 and int(y['tree_bytes'])>0
  same={k:y[k] for k in list(expect)+['tree_bytes']};key=(n,q['seed'],q['requested_ops']);assert same==refs.setdefault(key,same);semantics+=1
 if z['kind'] in ['tree-stat','tree-disabled-stat','known-stat']:
  enabled=z['kind']=='tree-stat' or z['name']=='known-enabled-stat';name=z['name'][:-5] if z['name'].endswith('-stat') else z['variant']+'-disabled'
  rows=[next(csv.reader([line])) for line in txt('profile/'+name+'.stat').splitlines() if line and not line.startswith('#')];stats={row[2]:row for row in rows};assert len(stats)==len(rows)==4 and set(stats)=={'cycles:u','instructions:u','branches:u','branch-misses:u'}
  for event,row in stats.items():
   if enabled:assert D(row[0])>=(0 if event=='branch-misses:u' else 1) and D(row[4])==100
   else:assert row[0].strip() in ['0','<not counted>']
  if z['kind']=='tree-stat':counters[(z['variant'],z['fixture']['size'],z['fixture']['seed'])]={k:D(row[0]) for k,row in stats.items()}
assert warnings==claim['all_nonempty_stderr'];captures=[]
for q in j('fixtures.json'):
 for variant in ['control','A']:
  name=f'{variant}-iterate-n{q["size"]}-s{q["seed"]}';counts=collections.Counter();events=collections.Counter();blocks=re.split(r'\n\s*\n',txt('profile/'+name+'-samples.stdout').strip())
  for block in blocks:
   lines=block.splitlines();weight=int(lines[0]);frames=[re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',line) for line in lines[1:]];assert frames and all(frames)
   label=frames[0][2];sym=re.sub(r'\+0x[0-9a-f]+(?: \(inlined\))?$','',label).replace(' (inlined)','');counts[sym]+=weight;events[sym]+=1
  report=txt('profile/'+name+'-report.stdout');lost=int(re.search(r'Total Lost Samples:\s*(\d+)',report)[1]);period=sum(counts.values());assert period==int(re.search(r'Event count \(approx\.\):\s*(\d+)',report)[1]) and period>0
  reported=next(x for x in claim['captures'] if x['variant']==variant and x['fixture']==q)
  assert reported['raw_events']==len(blocks) and reported['raw_period']==period and reported['lost']==lost and reported['exclusive_period']==dict(counts) and reported['exclusive_events']==dict(events)
  captures.append(dict(variant=variant,fixture=q,events=len(blocks),period=period,lost=lost,exclusive_period=dict(counts)))
pairs=[]
for q in j('fixtures.json'):
 a=counters[('control',q['size'],q['seed'])];b=counters[('A',q['size'],q['seed'])];direc=b['instructions:u']<a['instructions:u'];reported=next(x for x in claim['counter_pairs'] if x['fixture']==q)
 assert reported['instructions_direction_pass']==direc
 for event in a:
  m=reported['metrics'][event];assert D(m['control_count'])==a[event] and D(m['candidate_count'])==b[event] and D(m['difference_count'])==b[event]-a[event]
 pairs.append(dict(fixture=q,instruction_change_pct=str(100*(b['instructions:u']/a['instructions:u']-1)),instruction_direction_pass=direc,raw_counts={k:{'control':str(a[k]),'candidate':str(b[k])} for k in a}))
assert len(counters)==12 and len(captures)==12 and len(pairs)==6
assert claim['all_six_instruction_direction_pass']==all(x['instruction_direction_pass'] for x in pairs)
assert claim['total_lost_events']==sum(x['lost'] for x in captures)
for n,h in valid['input_sha256'].items():assert sha(f['profile/'+n])==h
assert valid['execution_freeze_sha256']==sha(f['execution-freeze.json'])
assert valid['failed_gates']==[k for k,v in valid['gates'].items() if not v]
assert valid['status']==('VALIDATED_MECHANISM_SUPPORT_NOT_ACCEPTANCE' if all(valid['gates'].values()) else 'PARK_PROFILE_VALIDITY_GATES')
report=dict(audit_status='PASS_INTEGRITY',revision=rev,reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sealed_public_artifacts=len(seal),frozen_inputs=len(freeze['files']),commands=104,semantic_rows=semantics,phase_seconds=r['elapsed_seconds'],captures=captures,counter_pairs=pairs,total_lost_events=claim['total_lost_events'],profile_validity=valid['status'],failed_profile_gates=valid['failed_gates'],source_selection='NONE',limits=['Known arithmetic and physical sampled-byte mapping require separate AMD independent raw review.','Operator identity records are immutable artifacts, not an additional live read.','Raw perf binaries may remain local; public exports and checksums are verified.','PMU directions and period shares do not quantify causal elapsed-time improvement or repair performance guards.'])
Path('experiments/ARM-MASK-FOLLOWUP-001/PROFILE-ROOT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['captures','counter_pairs']},indent=2))
