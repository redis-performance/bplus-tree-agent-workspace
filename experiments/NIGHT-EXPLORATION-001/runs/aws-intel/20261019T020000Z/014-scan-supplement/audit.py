from pathlib import Path
import json,datetime,sys,itertools,statistics
p=Path(__file__).parent;phase=sys.argv[1];m=json.loads((p/(phase+'.json')).read_text());last=None;identity=['history','n','bytes','seed','encoding','passes','logical_members','callbacks_per_pass','checksum_per_pass','tree_bytes','warmup_passes','prepost_oracles','warmup_callback_parity','validation']
for i,x in enumerate(m['rows']):
 assert x['index']==i;row=json.loads((p/'raw'/f'{phase}-{i:04d}.stdout').read_text());assert row==x['row'] and row['start_cpu']==row['end_cpu']==2;start=datetime.datetime.fromisoformat(x['started_utc']);end=datetime.datetime.fromisoformat(x['finished_utc']);assert start<=end
 if last:assert last<=start
 last=end
 for k in ['history','bytes','seed','encoding','passes']:assert row[k]==x[k]
 assert row['validation']=='pass' and row['warmup_passes']==2 and row['prepost_oracles']==2 and row['warmup_callback_parity'] and row['logical_members']==row['n']*row['passes']
result=dict(status='pass',phase_status=m['status'],rows=len(m['rows']),serial=True,cpu_endpoints=2,source_adoption='NONE')
if phase=='calibration':
 if m['status']=='complete':
  for h,w,e,s in itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2],[201,202,203]):
   group=[x for x in m['rows'] if (x['history'],x['bytes'],x['encoding'],x['seed'])==(h,w,e,s)];probes=[x for x in group if x['kind']=='probe'];trials=[x for x in group if x['kind']=='trial'];assert [x['passes'] for x in probes]==[10**i for i in range(len(probes))] and len(trials)==3 and [x['repeat'] for x in trials]==[0,1,2];assert probes[-1]['row']['elapsed_ns']>=20000000 and all(x['row']['elapsed_ns']<20000000 for x in probes[:-1]);assert all(x['passes']==probes[-1]['passes'] for x in trials);assert len({tuple(x['row'][k] for k in identity if k not in ['passes','logical_members']) for x in group})==1
else:
 schedule=json.loads((p/(phase+'-schedule.json')).read_text());assert all(all(x[k]==v for k,v in spec.items()) for x,spec in zip(m['rows'],schedule));effects=[]
 for i in range(0,len(m['rows'])-3,4):
  g=m['rows'][i:i+4];assert len({tuple(x['row'][k] for k in identity) for x in g})==1;v=[x['row']['elapsed_ns']/(x['row']['passes']*x['row']['callbacks_per_pass']) for x in g];effects.append(dict(history=g[0]['history'],bytes=g[0]['bytes'],encoding=g[0]['encoding'],block=g[0]['block'],seed=g[0]['seed'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),minimum_window_ns=min(x['row']['elapsed_ns'] for x in g)))
 summary=[];controls={} if phase=='aa' else {(x['history'],x['bytes'],x['encoding']):x for x in json.loads((p/'aa-audit.json').read_text())['summary']}
 for h,w,e in itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2]):
  g=[x for x in effects if (x['history'],x['bytes'],x['encoding'])==(h,w,e)]
  if not g:continue
  vals=[x['percent'] for x in g];q=len(g)==6 and all(abs(x['percent'])<=1 and x['minimum_window_ns']>=100000000 for x in g);s=dict(history=h,bytes=w,encoding=e,blocks=len(g),effects=vals,median=statistics.median(vals),minimum_window_ns=min(x['minimum_window_ns'] for x in g),qualified=q)
  if phase=='b':s.update(baseline_qualified=controls[(h,w,e)]['qualified'],passes_guard=len(g)==6 and all(x['percent']<=1 and x['minimum_window_ns']>=100000000 for x in g),demonstrated_regression=controls[(h,w,e)]['qualified'] and len(g)==6 and all(v>1 for v in vals))
  summary.append(s)
 if m['status']=='complete':assert len(m['rows'])==720 and len(effects)==180 and len(summary)==30
 result.update(summary=summary,effects=effects)
 if phase=='aa':result['qualified_cells']=sum(x['qualified'] for x in summary)
 else:result.update(qualified_guard_pass_cells=sum(x['baseline_qualified'] and x['passes_guard'] for x in summary),demonstrated_regressions=sum(x['demonstrated_regression'] for x in summary),decision='REJECT' if any(x['demonstrated_regression'] for x in summary) else 'PARK; original guard gaps remain')
(p/(phase+'-audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['summary','effects']},indent=2))
