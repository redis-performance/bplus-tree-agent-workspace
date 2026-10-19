from pathlib import Path
import json,csv,datetime,hashlib,statistics
p=Path(__file__).parent;m=json.loads((p/'b-comparison.json').read_text());schedule=json.loads((p/'b-schedule.json').read_text());freeze=json.loads((p/'b-freeze.json').read_text());processes=m['processes'];last=None
for f,h in freeze['files'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h
assert len(processes)<=120
cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
for i,x in enumerate(processes):
 assert all(x[k]==v for k,v in schedule[i].items());rows=list(csv.DictReader((p/'raw'/f'b-{i:03d}.stdout').open()));assert rows==x['rows'];assert [r['case'] for r in rows]==cases
 for r in rows:assert r['cpu_start']==r['cpu_end']=='2' and int(r['size'])==x['size'] and int(r['member_bytes'])==x['member_bytes'] and int(r['seed'])==x['seed'] and r['requested_ops']=='5000000'
 start=datetime.datetime.fromisoformat(x['started_utc']);end=datetime.datetime.fromisoformat(x['finished_utc']);assert start<=end
 if last is not None:assert last<=start
 last=end
effects=[]
for i in range(0,len(processes)-3,4):
 group=processes[i:i+4]
 for c,case in enumerate(cases):
  rows=[x['rows'][c] for x in group];assert len({(r['checksum'],r['operations'],r['tree_bytes']) for r in rows})==1
  values=[int(r['elapsed_ns'])/int(r['operations']) for r in rows];effect=100*((values[1]+values[2])/(values[0]+values[3])-1);minimum=min(int(r['elapsed_ns']) for r in rows)
  effects.append(dict(size=group[0]['size'],member_bytes=group[0]['member_bytes'],case=case,block=group[0]['block'],seed=group[0]['seed'],percent=effect,min_window_ns=minimum,passes_guard=effect<=1 and minimum>=10000000))
summary=[]
for size in [100,1000,10000,100000,1000000]:
 for keybytes in [16,128]:
  for case in cases:
   group=[x for x in effects if (x['size'],x['member_bytes'],x['case'])==(size,keybytes,case)];values=[x['percent'] for x in group]
   if group:summary.append(dict(size=size,member_bytes=keybytes,case=case,blocks=len(group),minimum=min(values),maximum=max(values),median=statistics.median(values),min_window_ns=min(x['min_window_ns'] for x in group),passes_guard=len(group)==3 and all(x['passes_guard'] for x in group),effects=values))
if m['status']=='complete':assert len(processes)==120 and len(summary)==80 and len(effects)==240
aa=json.loads((p/'aa-audit.json').read_text());controls={(x['size'],x['member_bytes'],x['case']):x for x in aa['summary']}
for x in summary:
 c=controls[(x['size'],x['member_bytes'],x['case'])];x['baseline_qualified']=c['qualified'];x['control_effects']=c['effects'];x['qualified_guard_pass']=c['qualified'] and x['passes_guard'];x['demonstrated_regression']=c['qualified'] and x['blocks']==3 and x['minimum']>1
complete=m['status']=='complete' and len(processes)==120;regressed=[x for x in summary if x['demonstrated_regression']];unresolved=[x for x in summary if not x['baseline_qualified'] or not x['passes_guard']]
result=dict(status='pass',phase_status=m['status'],processes=len(processes),raw_rows=len(processes)*8,blocks=len(effects),serial=True,schedule_prefix_exact=True,fixture_identity=True,owned_bytes_equal=True,baseline_qualified_cells=aa['qualified_cells'],qualified_guard_pass_cells=sum(x['qualified_guard_pass'] for x in summary),demonstrated_regression_cells=len(regressed),unresolved_cells=len(unresolved),source_adoption='NONE',decision='REJECT' if regressed else ('PARK' if unresolved or not complete else 'original guards passed; broader gates pending'),summary=summary,effects=effects)
(p/'b-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['summary','effects']},indent=2))
