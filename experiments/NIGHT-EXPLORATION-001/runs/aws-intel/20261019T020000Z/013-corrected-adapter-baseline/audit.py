from pathlib import Path
import json,csv,hashlib,statistics,datetime
p=Path(__file__).parent;d=p/'results';m=json.loads((d/'manifest.json').read_text());assert m['status']=='complete' and m['commit']=='13e459ff8800be3f02b6b45c87dd7b0c39453fa9';assert m['arguments']['ops']==1000000 and m['arguments']['member_bytes']==16 and m['arguments']['budget_seconds']==1200 and m['arguments']['build']=='build/corrected-adapter-intel';assert m['machine']['affinity']==[2];assert len(m['validation'])==7 and all(x['returncode']==0 for x in m['validation']);assert m['binary_sha256']==m['binary_sha256_after'] and m['timing_seconds']<=1200
freeze=json.loads((p/'source-freeze.json').read_text());assert all(freeze['files'][f]==h for f,h in m['source_hashes'].items());assert json.loads((p/'source-before.json').read_text())['files']==freeze['files'];after=json.loads((p/'source-after.json').read_text())['files'];assert all(after[f]==h for f,h in freeze['files'].items()) and after['build/corrected-adapter-intel/btree-bench']==m['binary_sha256'];assert all(json.loads((p/(tag+'.json')).read_text())['status']=='pass' for tag in ['original-before-hashes','original-after-hashes'])
sizes=[100,1000,10000,100000,1000000];cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete'];expected=[]
for block in range(6):
 for n in sizes[block%5:]+sizes[:block%5]:
  for step,label in enumerate('ABBA'):expected.append((block,1+block%3,n,step,label))
assert len(m['runs'])==120;rows=[]
for r,e in zip(m['runs'],expected):
 assert tuple(r[k] for k in ['block','seed','size','step','label'])==e and r['returncode']==0
 for field in ['csv','stderr']:assert hashlib.sha256((d/r[field]).read_bytes()).hexdigest()==r[field+'_sha256']
 one=list(csv.DictReader((d/r['csv']).open()));assert [x['case'] for x in one]==cases
 for x in one:assert x['cpu_start']==x['cpu_end']=='2' and int(x['requested_ops'])==1000000 and int(x['size'])==r['size'] and int(x['seed'])==r['seed'] and int(x['member_bytes'])==16
 rows.append(one)
effects=[]
for i in range(0,120,4):
 for k,case in enumerate(cases):
  group=[x[k] for x in rows[i:i+4]];assert len({(x['operations'],x['checksum'],x['tree_bytes']) for x in group})==1;v=[int(x['elapsed_ns'])/int(x['operations']) for x in group];effects.append(dict(size=int(group[0]['size']),case=case,block=expected[i][0],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),min_window_ns=min(int(x['elapsed_ns']) for x in group)))
summary=[]
for n in sizes:
 for case in cases:
  g=[x for x in effects if x['size']==n and x['case']==case];assert len(g)==6;summary.append(dict(size=n,case=case,effects=[x['percent'] for x in g],min_window_ns=min(x['min_window_ns'] for x in g),qualified=all(abs(x['percent'])<=1 and x['min_window_ns']>=10000000 for x in g)))
result=dict(status='pass',processes=120,raw_rows=960,blocks=240,cells=40,qualified_cells=sum(x['qualified'] for x in summary),short_cells=sum(x['min_window_ns']<10000000 for x in summary),source='13e459ff8800be3f02b6b45c87dd7b0c39453fa9',cpu_endpoints=2,serial='Unchanged serial driver; original manifest has no per-process UTC boundaries',source_adoption='NONE',new_population=False,summary=summary,effects=effects);(p/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['summary','effects']},indent=2))
