#!/usr/bin/env python3
"""Independent original-guard audit. No imports from either Intel audit script."""
import argparse,csv,datetime,hashlib,itertools,json,pathlib,statistics,collections
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);p.add_argument('--aa-only',action='store_true');p.add_argument('--commit',required=True);a=p.parse_args();root=a.evidence
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda n:json.loads((root/n).read_text())
clock=datetime.datetime.fromisoformat
cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
fixtures=list(itertools.product([100,1000,10000,100000,1000000],[16,128]));sequences=[fixtures,list(reversed(fixtures)),fixtures[5:]+fixtures[:5]]
original_schedule=[]
for block,seq in enumerate(sequences):
 for n,width in seq:
  for pos in range(4):original_schedule.append(dict(index=len(original_schedule),block=block,size=n,member_bytes=width,seed=151+block,position=pos))
assert len(original_schedule)==120
identity=['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes']
all_rows={};phase_results={};frozen_hashes={}
for phase in (['aa'] if a.aa_only else ['aa','b']):
 freeze=read(phase+'-freeze.json');assert freeze['phase_cap_seconds']==1440
 for file,h in freeze['files'].items():assert sha(root/file)==h,(phase,file)
 frozen_hashes[phase]={file:sha(root/file) for file in freeze['files']}
 if phase=='aa':assert freeze['baseline_binary_sha256']=='b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2'
 else:assert freeze['binary_sha256']=={'base':'b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2','B':'12a19e50d7ec0d59b9d9b509433f9d14be42ea166bfdad8c4758c608e890fb24'}
 schedule=read(phase+'-schedule.json');expected=[dict(s,**({'binary':['base','B','B','base'][s['position']]} if phase=='b' else {})) for s in original_schedule];assert schedule==expected
 data=read('aa.json' if phase=='aa' else 'b-comparison.json');processes=data['processes'];assert len(processes)<=120
 assert clock(freeze['frozen_utc'])<clock(data['started_utc']);assert data['elapsed_seconds']<=1440
 assert data['status']=='complete' and len(processes)==120,'incomplete phase: retain raw output; no full verdict'
 groups=collections.defaultdict(list);keyed={}
 for i,proc in enumerate(processes):
  spec=schedule[i];assert all(proc[k]==v for k,v in spec.items());assert clock(proc['started_utc'])<=clock(proc['finished_utc']);assert proc['duration_seconds']<=120
  if i:assert clock(processes[i-1]['finished_utc'])<=clock(proc['started_utc'])
  variant=spec.get('binary','base');cmd=['scratch/intel-scan-replication/'+variant+'/build/btree-bench','--case','all','--size',str(spec['size']),'--ops','5000000','--member-bytes',str(spec['member_bytes']),'--seed',str(spec['seed'])];assert proc['command']==cmd
  rawfile=root/'raw'/f'{phase}-{i:03d}.stdout';raw=list(csv.DictReader(rawfile.read_text().splitlines()));assert raw==proc['rows'];assert [r['case'] for r in raw]==cases;assert not (root/'raw'/f'{phase}-{i:03d}.stderr').read_text()
  for r in raw:
   assert int(r['size'])==spec['size'] and int(r['member_bytes'])==spec['member_bytes'] and int(r['seed'])==spec['seed'] and int(r['requested_ops'])==5000000
   assert r['cpu_start']==r['cpu_end']=='2';assert int(r['elapsed_ns'])>0 and int(r['operations'])>0
   if r['case'] in ['insert','delete']:assert int(r['operations'])==spec['size']
   key=(spec['size'],spec['member_bytes'],r['case'],spec['block']);groups[key].append((spec['position'],r));keyed[(i,r['case'])]=r
 all_rows[phase]=keyed
 cells=collections.defaultdict(list);effects=[]
 for (n,width,case,block),group in sorted(groups.items()):
  assert [pos for pos,r in group]==[0,1,2,3]
  rr=[r for pos,r in group]
  for k in identity:assert len({r[k] for r in rr})==1,(phase,n,width,case,block,k)
  rates=[int(r['elapsed_ns'])/int(r['operations']) for r in rr];e=100*((rates[1]+rates[2])/(rates[0]+rates[3])-1);window=min(int(r['elapsed_ns']) for r in rr)
  item=dict(size=n,member_bytes=width,case=case,block=block,seed=151+block,effect_pct=e,min_window_ns=window)
  effects.append(item);cells[(n,width,case)].append(item)
 assert len(effects)==240 and len(cells)==80
 summary=[]
 for (n,width,case),ee in sorted(cells.items()):
  assert [e['block'] for e in ee]==[0,1,2];values=[e['effect_pct'] for e in ee];window=min(e['min_window_ns'] for e in ee)
  item=dict(size=n,member_bytes=width,case=case,effects_pct=values,median_effect_pct=statistics.median(values),min_window_ns=window)
  if phase=='aa':item.update(qualified=window>=10000000 and all(abs(v)<=1 for v in values),short=window<10000000)
  summary.append(item)
 phase_results[phase]=dict(processes=120,rows=960,blocks=240,cells=80,effects=effects,summary=summary,started_utc=data['started_utc'],finished_utc=data['finished_utc'])
aa=phase_results['aa'];lookup={(c['size'],c['member_bytes'],c['case']):c for c in aa['summary']}
aa['qualified_cells']=sum(c['qualified'] for c in lookup.values());aa['short_cells']=sum(c['short'] for c in lookup.values());aa['other_failed_cells']=sum(not c['short'] and not c['qualified'] for c in lookup.values())
assert [aa['qualified_cells'],aa['short_cells'],aa['other_failed_cells']]==[57,12,11]
if not a.aa_only:
 for key,after in all_rows['b'].items():
  before=all_rows['aa'][key]
  for field in identity:assert before[field]==after[field],('crossphase',key,field)
 b=phase_results['b'];counts=collections.Counter()
 for cell in b['summary']:
  control=lookup[(cell['size'],cell['member_bytes'],cell['case'])];cell['aa_qualified']=control['qualified'];cell['aa_effects_pct']=control['effects_pct'];cell['aa_short']=control['short'];values=cell['effects_pct'];bad=sum(v>1 for v in values)
  if not control['qualified']:verdict='exploratory_unqualified'
  elif cell['min_window_ns']<10000000:verdict='park_short_candidate_window'
  elif bad==3:verdict='reject_demonstrated_regression'
  elif bad:verdict='park_mixed_bound_exceedance'
  else:verdict='guard_pass'
  cell['blocks_exceeding_positive_one_percent']=bad;cell['verdict']=verdict;counts[verdict]+=1
 b['verdict_counts']=dict(counts);b['overall']='REJECT' if counts['reject_demonstrated_regression'] else 'PARK'
output={'auditor':'one independently authoring AMD native agent; exact model and measured costs unknown','reviewed_commit':a.commit,'status':'reconstructed','source_adoption':'NONE','frozen_files':frozen_hashes,'raw_hashes':{str(p.relative_to(root)):sha(p) for p in sorted((root/'raw').glob('*')) if p.name.startswith(('aa-','b-'))},'phase_results':phase_results,'scope_notes':['No Intel audit-b.py read or imported','Startup hashes are enforced by frozen driver; post-phase source/referee/binary evidence must be audited separately when published','Full80-cell acceptance blocked by23 unqualified controls regardless of candidate outcome','Every effects calculation uses unrounded elapsed_ns / actual operations']}
a.out.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps({'aa_qualified':aa['qualified_cells'],'aa_short':aa['short_cells'],'aa_other_failures':aa['other_failed_cells'],'b_verdicts':phase_results.get('b',{}).get('verdict_counts','pending')}))
