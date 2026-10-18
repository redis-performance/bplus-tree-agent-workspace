"""Read-only audit of round13 raw data, schedules, source isolation and decisions."""
from pathlib import Path
import csv,datetime,hashlib,json,math,statistics as st
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();dt=lambda s:datetime.datetime.fromisoformat(s).timestamp()
windows=[];checks=[];intervals_checked=0
def window(r,kind,name):
 a,b=dt(r['started_utc']),dt(r['ended_utc']);assert 0<=b-a<=121;windows.append((a,b,kind,name))
def snapshot(m):
 for desc in m['snapshots'].values():
  for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h

def output(folder,r,name):
 for k in ['stdout','stderr']:assert sha(folder/(name+'.'+k))==r[k+'_sha256']
for relative in ['BOUNDARY-017','BOUNDARY-018','BOUNDARY-018/attempt-002']:
 folder=P/relative;m=json.loads((folder/'manifest.json').read_text());snapshot(m)
 for row in m['runs']:output(folder,row,row['name']);window(row,'validation',relative+'/'+row['name'])
 if relative=='BOUNDARY-018':assert m['status']=='failed' and m['runs'][0]['returncode']==1
 else:assert m['status']=='complete' and len(m['runs'])==16 and all(r['returncode']==0 for r in m['runs'])
 checks.append(relative+' frozen sources/output hashes')
for relative,needle in [('BOUNDARY-017','stores=1048624 tags=4096 masks=524288'),('BOUNDARY-018/attempt-002','fixtures=38 registrations=1458668 releases=1458668')]:
 folder=P/relative;s=json.loads((folder/'summary.json').read_text());assert s['status']=='pass' and s['cells']==8 and s['identical_output'] and needle in s['output']
 m=json.loads((folder/'manifest.json').read_text());outs=[(folder/(r['name']+'.stdout')).read_bytes() for r in m['runs'] if r['stage']=='run'];assert len(set(outs))==1
 faults=json.loads((folder/'faults/manifest.json').read_text());assert len(faults)==2
 for fault in faults:
  assert fault['detected'] and sha(R/fault['snapshot']/'src/zset_btree.c')==fault['source_sha256']
  assert fault['runs'][0]['returncode']==0 and fault['runs'][1]['returncode']!=0
  for row in fault['runs']:output(folder/'faults',row,fault['name']+'-'+row['stage']);window(row,'validation',relative+'/'+fault['name']+'-'+row['stage'])
old=json.loads((P/'BOUNDARY-018/manifest.json').read_text())['snapshots']['control'];new=json.loads((P/'BOUNDARY-018/attempt-002/manifest.json').read_text())['snapshots']['control']
oldtext=(R/old['path']/'tests/leaf_id_registry_oracle.c').read_text();newtext=(R/new['path']/'tests/leaf_id_registry_oracle.c').read_text()
assert oldtext.replace('zmalloc_size(', 'zmalloc_usable_size(')==newtext
checks.append('Allocator API erratum changes one call, no weakened assertion')
for row in json.loads((P/'DIAG-017/transport-validation.json').read_text())['records']:window(row,'validation','DIAG-017/transport-'+row['policy']+'-'+row['mode'])
v=json.loads((P/'DIAG-018/validation.json').read_text());assert v['status']=='pass' and len(v['runs'])==7
for row in v['runs']:output(P/'DIAG-018',row,row['name']);window(row,'validation','DIAG-018/'+row['name'])

def ci(v):
 assert len(v)==6;m=st.mean(v);h=2.5705818366147395*st.stdev(v)/math.sqrt(6);return[m,m-h,m+h]
def same(a,b):assert len(a)==len(b) and all(abs(x-y)<1e-9 for x,y in zip(a,b)),(a,b)
def interval(v,reported):
 global intervals_checked
 same(ci(v),reported);intervals_checked+=1

all_data={}
for relative,count in [('DIAG-016',384),('DIAG-017',384),('DIAG-018',48),('DIAG-018/confirm',48)]:
 folder=P/relative;m=json.loads((folder/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==count and len(m['warmup'])==1
 assert m['seeds']=={'DIAG-016':[47111,47123],'DIAG-017':[49109,49121],'DIAG-018':[53101,53113],'DIAG-018/confirm':[55103,55117]}[relative]
 assert sha(R/m['binary'])==m['binary_sha256']==m['binary_sha256_after'];assert sha(folder/'PLAN.md')==m['plan_sha256']
 assert sha(folder/'schedule.json')==m['schedule_sha256'];schedule=json.loads((folder/'schedule.json').read_text())
 if count==384:schedule=[r for group in schedule for pair in group for r in pair]
 assert len(schedule)==count
 parsed=[]
 for row in m['warmup']+m['runs']:
  assert row['returncode']==0
  for k in ['csv','stderr']+(['completion'] if count==48 else []):assert sha(folder/row[k])==row[k+'_sha256']
  rows=list(csv.DictReader((folder/row['csv']).open()));assert len(rows)==1;d=rows[0]
  requested=1000000 if row in m['warmup'] else 20000000
  assert int(d['requested_ops'])==requested and int(d['operations'])==((requested+94)//95)*95 and int(d['traversals'])==(requested+94)//95
  assert d['checksum']==d['expected_checksum'] and d['warmup_passes']=='3' and d['size']=='95' and d['member_bytes']=='16' and d['construction']=='trimmed' and d['direction']=='forward'
  assert int(d['thread_elapsed_ns'])>0
  window(row,'measurement',relative+'/'+row['csv'])
  if row not in m['warmup']:parsed.append((row,d))
 for scheduled,(row,d) in zip(schedule,parsed):
  for key,value in scheduled.items():assert row[key]==value
  args=row['command'];actual={args[i]:args[i+1] for i in range(args.index('--size'),len(args),2)}
  assert actual=={'--size':'95','--ops':'20000000','--seed':str(row['seed']),'--warmup-passes':'3','--direction':'forward','--encoding':d['encoding'],'--construction':'trimmed','--member-bytes':'16','--mask':d['mask']}
  assert d['seed']==str(row['seed'])
 s=json.loads((folder/'summary.json').read_text());assert s['invariants'];assert s['status']==('unsupported' if count==384 else 'supported')
 if count==384:
  journal=[r for line in (folder/'journal.jsonl').read_text().splitlines() for r in json.loads(line)];assert len(journal)==count
  for j,(r,d) in zip(journal,parsed):
   for k,v in j.items():assert r[k]==v
  for i in range(0,count,2):
   pre,pd=parsed[i];target,td=parsed[i+1];assert pre['role']=='predecessor' and target['role']=='target'
   for k in ['seed','block','step','label','policy','protocol']:assert pre[k]==target[k]
   assert target['label']=='ABBA'[target['step']-1]
   assert target['cell']=='zero-trim-f6' and td['mask']=='6' and td['encoding']=='alternating-zero'
   is_other=target['protocol']=='contrast' and target['label']=='B';assert (pre['cell']=='int-trim-f0')==is_other
   assert pd['mask']==('0' if is_other else '6') and pd['encoding']==('integer' if is_other else 'alternating-zero')
   assert target['coordinator_launch_gap_ns']==target['start_monotonic_ns']-pre['end_monotonic_ns']>=0
  for result in s['results']:
   rows=[(r,d) for r,d in parsed if r['role']=='target' and all(r[k]==result[k] for k in ['seed','policy','protocol'])];assert len(rows)==24
   for k in ['checksum','operations','tree_bytes','construction_fingerprint']:assert len({d[k] for r,d in rows})==1
   for metric in ['elapsed_ns','thread_elapsed_ns']:
    e=[]
    for block in range(1,7):
     ab={l:[int(d[metric])/int(d['operations']) for r,d in rows if r['block']==block and r['label']==l] for l in 'AB'};assert all(len(v)==2 for v in ab.values());e.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
    same(e,result['effects_pct'][metric]);interval(e,result['intervals'][metric])
   assert min(int(d['elapsed_ns']) for r,d in rows)>=10000000
  baseline='pair' if relative=='DIAG-016' else 'file';treatment='block' if relative=='DIAG-016' else 'pipe'
  for result in s['interactions']:
   cells={r['policy']:r for r in s['results'] if r['seed']==result['seed'] and r['protocol']=='contrast'}
   for metric in ['elapsed_ns','thread_elapsed_ns']:
    e=[b-a for a,b in zip(cells[baseline]['effects_pct'][metric],cells[treatment]['effects_pct'][metric])];same(e,result['effects_pct'][metric]);interval(e,result['intervals'][metric])
  for result in s['results']:
   bound=result['intervals']['elapsed_ns'];passes=bound[2]<-1 if result['policy']==baseline and result['protocol']=='contrast' else bound[1]>=-1 and bound[2]<=1
   assert result['passes']==passes
  for result in s['interactions']:
   cells={r['policy']:r for r in s['results'] if r['seed']==result['seed'] and r['protocol']=='contrast'}
   halved=abs(cells[treatment]['intervals']['elapsed_ns'][0])<=.5*abs(cells[baseline]['intervals']['elapsed_ns'][0])
   assert result['halved']==halved and result['passes']==(halved and result['intervals']['elapsed_ns'][1]>1)
  required=[r for r in s['results'] if not(r['policy']==baseline and r['protocol']=='placebo')]+s['interactions']+s.get('manipulation',[])
  assert s['status']==('supported' if all(r['passes'] for r in required) else 'unsupported')
  if relative=='DIAG-016':
   for item in s['manipulation']:
    med={policy:st.median(r['previous_target_parent_cpu_ns'] for r,d in parsed if r['role']=='predecessor' and r['policy']==policy and r['seed']==item['seed'] and r['protocol']==item['protocol'] and r['step']>1) for policy in m['policies']}
    assert med==item['median_parent_cpu_ns'] and item['passes']==(med['block']<=.75*med['pair'])
 else:
  o=m['observer'];assert sha(R/o['binary'])==o['binary_sha256'] and sha(R/o['source'])==o['source_sha256']
  for result in s['results']:
   rows=[(r,d) for r,d in parsed if r['seed']==result['seed']];assert len(rows)==24
   for k in ['checksum','operations','tree_bytes','construction_fingerprint']:assert len({d[k] for r,d in rows})==1
   delay={}
   for r,d in rows:
    c=json.loads((folder/r['completion']).read_text());assert c['child_status']==0 and c['timed_out']==0
    assert r['parent_clock_start_ns']<=c['waitpid_observed_ns']<=r['parent_clock_return_ns'];delay[r['csv']]=(r['parent_clock_return_ns']-c['waitpid_observed_ns'])/1e6
    assert r['policy']==('file' if (r['label']=='A')==(relative=='DIAG-018') else 'pipe')
    assert r['label']=='ABBA'[r['step']-1]
   for metric in ['observed_delay_ms','elapsed_ns','thread_elapsed_ns']:
    e=[]
    for block in range(1,7):
     ab={l:[(r,d) for r,d in rows if r['block']==block and r['label']==l] for l in 'AB'};assert all(len(v)==2 for v in ab.values())
     if metric=='observed_delay_ms':
      a=st.mean(delay[r['csv']] for r,d in ab['A']);b=st.mean(delay[r['csv']] for r,d in ab['B']);e.append(a-b if relative=='DIAG-018' else b-a)
     else:e.append(100*(st.mean(int(d[metric])/int(d['operations']) for r,d in ab['B'])/st.mean(int(d[metric])/int(d['operations']) for r,d in ab['A'])-1))
    same(e,result['effects'][metric]);interval(e,result['intervals'][metric])
   assert ci(result['effects']['observed_delay_ms'])[1]>5 and result['passes']
   assert min(int(d['elapsed_ns']) for r,d in rows)>=10000000
 checks.append(relative+' raw rows, effective counts, checksums, scheduling and recomputed intervals')
 all_data[relative]=dict(rows=count,warmups=1,status=s['status'])
windows.sort()
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
root_hashes=json.loads((P/'BOUNDARY-015/attempt-002/manifest.json').read_text())['root_hashes']
for n,h in root_hashes.items():assert sha(R/n)==h
f=json.loads((P/'HARNESS-006/freeze.json').read_text())
for n,h in f['files'].items():assert sha(R/f['snapshot']/n)==h
summary=dict(status='pass',measurements=sum(w[2]=='measurement' for w in windows),validation_windows=sum(w[2]=='validation' for w in windows),intervals_checked=intervals_checked,all_serial=True,root_hashes=root_hashes,checks=checks,data=all_data)
(P/'ROUND-013-VERIFY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
