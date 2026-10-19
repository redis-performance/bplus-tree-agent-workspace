import csv,datetime,hashlib,json,statistics
from pathlib import Path
p=Path(__file__).parent
m=json.loads((p/'discovery.json').read_text());rows=m['rows'];previous=None;groups=[]
for i,r in enumerate(rows):
 raw=list(csv.DictReader((p/'raw'/f'discovery-{i:04d}.stdout').read_text().splitlines()));assert len(raw)==1 and raw[0]==r['row']
 row=r['row'];assert row['checksum']==row['expected_checksum'];assert row['cpu_start']==row['cpu_end']=='2'
 start=datetime.datetime.fromisoformat(r['started_utc']);end=datetime.datetime.fromisoformat(r['finished_utc']);assert start<=end
 if previous is not None:assert previous<=start
 previous=end
 assert r['position']==i%4
for i in range(0,len(rows)-3,4):
 r=rows[i:i+4];assert len({(x['cell'],x['block']) for x in r})==1
 assert [x['variant'] for x in r]==['release',r[1]['variant'],r[1]['variant'],'release']
 assert r[1]['variant'] in ['A','B','C']
 assert len({(x['row']['seed'],x['row']['operations'],x['row']['checksum'],x['row']['tree_bytes']) for x in r})==1
 v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r]
 groups.append(dict(cell=r[0]['cell'],variant=r[1]['variant'],block=r[0]['block'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),memory_equal=True,min_elapsed_ns=min(int(x['row']['elapsed_ns']) for x in r)))
if 'effects' in m:assert groups==m['effects']
summary=[]
for cell in sorted({x['cell'] for x in groups}):
 for variant in ['A','B','C']:
  g=[x for x in groups if x['cell']==cell and x['variant']==variant];effects=[x['percent'] for x in g]
  if not effects:continue
  summary.append(dict(cell=cell,variant=variant,blocks=len(g),blocks_present=[x['block'] for x in g],median=statistics.median(effects),minimum=min(effects),maximum=max(effects),effects=effects,all_speed_gate= len(g)==6 and max(effects)<=-2,all_guard_gate=len(g)==6 and max(effects)<=1))
freeze=json.loads((p/'comparison-freeze.json').read_text())
for f,h in freeze['sha256'].items():assert hashlib.sha256((p/f).read_bytes()).hexdigest()==h,f
result=dict(status='pass',screen_status=m['status'],raw_rows=len(rows),complete_blocks=len(groups),partial_rows=len(rows)%4,serial_windows_verified=True,fixture_checks=True,memory_equal=True,freeze_verified=True,summary=summary)
(p/'discovery-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='summary'}))
for x in summary:print(x['cell'],x['variant'],x['blocks'],round(x['median'],3),round(x['minimum'],3),round(x['maximum'],3))
