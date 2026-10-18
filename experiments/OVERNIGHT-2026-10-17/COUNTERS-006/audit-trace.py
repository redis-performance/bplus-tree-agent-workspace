from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent;D=P/'trace';M=json.loads((D/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();cells={}
assert M['status']=='complete'
for row in M['runs']:
 for k in ['stdout','stderr']:assert sha(D/(row['name']+'.'+k))==row[k+'_sha256']
 if not row['name'].endswith('-run'):continue
 name=row['name'].removesuffix('-run');policy,san=name.rsplit('-',1)
 baseline=(P/f'{policy}-O1-{san}-diagnostic.stdout').read_text().splitlines();raw=(D/(row['name']+'.stdout')).read_text().splitlines()
 for i,fixture in enumerate(['PASS n=6 bytes=320 descending=0 seed=31121','PASS n=7 bytes=16 descending=0 seed=31121']):
  ix=next(i for i,s in enumerate(baseline) if s.startswith(fixture));assert raw[2*i]==baseline[ix-1]
 states={};predicates=[];last=None
 for line in (D/(row['name']+'.stderr')).read_text().splitlines():
  if line.startswith('COMPACT_CHECK'):
   last={k:int(v) for k,v in re.findall(r'(\w+)=(\d+)',line)}
   assert last['decision']==int(last['usable']>=2*last['live']+last['reserve']);predicates.append(last)
  if line.startswith('STATE'):
   state={k:int(v) for k,v in re.findall(r'(\w+)=(\d+)',line)};state['previous_predicate']=last;states[state['check']]=state;last=None
 cells[name]=dict(states=states,predicates=predicates)
contrasts=[]
for a,b in [('ambient-native','ambient-sanitize'),('exact-native','round16-native')]:
 sa=cells[a]['states'];sb=cells[b]['states'];diff=[i for i in sa if sa[i]['reversed']!=sb[i]['reversed']]
 assert diff
 first=diff[0];x=sa[first];y=sb[first];pa=x['previous_predicate'];pb=y['previous_predicate']
 supported=bool(pa and pb and pa['count']==pb['count'] and pa['decision']!=pb['decision'])
 contrasts.append(dict(a=a,b=b,first_orientation_divergence_check=first,a_state=x,b_state=y,threshold_prediction_supported=supported))
result=dict(status='supported' if all(c['threshold_prediction_supported'] for c in contrasts) else 'unsupported',six_trace_cells_match_prior_fixture_layouts=True,contrasts=contrasts,scope='exploratory first observed fixtures; no fresh-seed claim')
(D/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
