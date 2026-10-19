from pathlib import Path
import json,sys,datetime,statistics,math,hashlib
P=Path(__file__).parent;phase=sys.argv[1];assert phase in ['calibration','guard-aa','guard-b'];m=json.loads((P/(phase+'.json')).read_text());last=None;models={x['seed']:x for x in json.loads((P/'fresh-guard-models.json').read_text())};identity=['history','n','bytes','seed','encoding','passes','logical_members','callbacks_per_pass','checksum_per_pass','tree_bytes','warmup_passes','prepost_oracles','warmup_callback_parity','validation']
for i,x in enumerate(m['rows']):
 assert x['index']==i and x['returncode']==0;row=json.loads((P/'guard-raw'/f'{phase}-{i:03d}.stdout').read_text());assert row==x['row'] and row['start_cpu']==row['end_cpu']==2;model=models[x['seed']]
 for k in ['history','n','bytes','seed','encoding','callbacks_per_pass','checksum_per_pass']:assert row[k]==model[k]
 assert row['passes']==x['passes'] and row['logical_members']==7*x['passes'];assert row['warmup_passes']==row['prepost_oracles']==2 and row['warmup_callback_parity'] and row['validation']=='pass';a=datetime.datetime.fromisoformat(x['started_utc']);b=datetime.datetime.fromisoformat(x['finished_utc']);assert a<=b and (last is None or last<=a);last=b
for kind in ['actual','build']:
 before=json.loads((P/(kind+'-before-'+phase+'.json')).read_text());after=json.loads((P/(kind+'-after-'+phase+'.json')).read_text());assert before['status']==after['status']=='pass' and before['files']==after['files']
result=dict(status='pass',phase_status=m['status'],rows=len(m['rows']),serial=True,cpu_endpoints=2,source_adoption='NONE',elapsed_seconds=m['elapsed_seconds'])
if phase=='calibration':
 if m['status']=='complete':
  expected=[]
  for seed in [701,702,703]:
   group=[x for x in m['rows'] if x['seed']==seed];probes=[x for x in group if x['kind']=='probe'];trials=[x for x in group if x['kind']=='trial'];assert [x['passes'] for x in probes]==[10**i for i in range(len(probes))] and len(trials)==3 and [x['repeat'] for x in trials]==[0,1,2];assert probes[-1]['row']['elapsed_ns']>=20000000 and all(x['row']['elapsed_ns']<20000000 for x in probes[:-1]);assert all(x['passes']==probes[-1]['passes'] for x in trials) and all(x['binary']=='base' for x in group);assert len({tuple(x['row'][k] for k in identity if k not in ['passes','logical_members']) for x in group})==1;expected.extend(group)
  assert expected==m['rows']
else:
 schedule=json.loads((P/(phase+'-schedule.json')).read_text());assert all(all(x[k]==v for k,v in spec.items()) for x,spec in zip(m['rows'],schedule));effects=[]
 for i in range(0,len(m['rows'])-3,4):
  g=m['rows'][i:i+4];assert len({tuple(x['row'][k] for k in identity) for x in g})==1;v=[x['row']['elapsed_ns']/(x['row']['passes']*x['row']['callbacks_per_pass']) for x in g];effects.append(dict(block=g[0]['block'],seed=g[0]['seed'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),minimum_window_ns=min(x['row']['elapsed_ns'] for x in g)))
 if m['status']=='complete':assert len(m['rows'])==24 and len(effects)==6
 complete=m['status']=='complete' and len(effects)==6;qualified=complete and all(abs(x['percent'])<=1 and x['minimum_window_ns']>=100000000 for x in effects);result.update(effects=effects,qualified=qualified)
 if phase=='guard-aa':result.update(advance_allowed=qualified,decision='QUALIFIED' if qualified else 'PARK; advancement blocked')
 else:
  control=json.loads((P/'guard-aa-audit.json').read_text());assert control['qualified'];passes=complete and all(x['percent']<=1 and x['minimum_window_ns']>=100000000 for x in effects);rejected=complete and all(x['percent']>1 and x['minimum_window_ns']>=100000000 for x in effects);result.update(passes_guard=passes,demonstrated_regression=rejected,advance_allowed=False,primary_launch_authorized=False,decision='REJECT' if rejected else 'PASS guard; coordinator review required' if passes else 'PARK; advancement blocked')
(P/(phase+'-audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
