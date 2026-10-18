from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert M['status']=='complete'
cells={}
for r in M['runs']:
 for k in ['stdout','stderr']:assert sha(P/(r['name']+'.'+k))==r[k+'_sha256']
 assert r['returncode']==0
 if r['name'].endswith('-diagnostic'):
  lines=(P/(r['name']+'.stdout')).read_text().splitlines();assert len(lines)==3881
  layouts=lines[0:-1:2];semantic=lines[1:-1:2]
  assert all(x.startswith('LAYOUT ') for x in layouts) and len(layouts)==1940
  assert lines[-1].startswith('PASS checks=289060 exact=86570560 ')
  cells[r['name'].removesuffix('-diagnostic')]=dict(layouts=layouts,semantic=semantic,final=lines[-1])
assert len({tuple(c['semantic']) for c in cells.values()})==1
comparisons=[]
for policy in ['ambient','exact','round16']:
 names=[n for n in cells if n.startswith(policy+'-')];reference=cells[names[0]]
 eq=all(c['layouts']==reference['layouts'] and c['final']==reference['final'] for n,c in cells.items() if n in names)
 comparisons.append(dict(policy=policy,all_four_builds_identical=eq,finals={n:cells[n]['final'] for n in names}))
differences=[]
for opt in ['O1','O3']:
 a=cells[f'ambient-{opt}-native'];b=cells[f'ambient-{opt}-sanitize'];diff=[i for i,(x,y) in enumerate(zip(a['layouts'],b['layouts'])) if x!=y]
 physical=[i for i in diff if re.sub(r'capacity=\w+ ','',a['layouts'][i])!=re.sub(r'capacity=\w+ ','',b['layouts'][i])]
 differences.append(dict(opt=opt,different_fixtures=len(diff),physical_different_fixtures=len(physical),first=(dict(index=physical[0],fixture=a['semantic'][physical[0]],native=a['layouts'][physical[0]],sanitize=b['layouts'][physical[0]]) if physical else None)))
a=cells['exact-O1-native'];b=cells['round16-O1-native'];intervention=[i for i,(x,y) in enumerate(zip(a['layouts'],b['layouts'])) if re.sub(r'capacity=\w+ ','',x)!=re.sub(r'capacity=\w+ ','',y)]
supported=all(x['all_four_builds_identical'] for x in comparisons if x['policy']!='ambient') and all(x['physical_different_fixtures'] for x in differences) and bool(intervention)
result=dict(status='supported' if supported else 'unsupported',semantic_cells=12,unit_cells=12,fixtures_per_cell=1940,checks_per_cell=289060,exact_per_cell=86570560,comparisons=comparisons,ambient_differences=differences,intervention_different_fixtures=len(intervention),intervention_first=dict(index=intervention[0],fixture=a['semantic'][intervention[0]],exact=a['layouts'][intervention[0]],round16=b['layouts'][intervention[0]]) if intervention else None)
(P/'summary.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
