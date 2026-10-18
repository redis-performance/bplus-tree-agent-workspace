import csv,hashlib,json,math,statistics as st
from pathlib import Path
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text())
rows=[];failed=[]
for run in m['runs']:
 for f in ['csv','stderr']:assert hashlib.sha256((P/run[f]).read_bytes()).hexdigest()==run[f+'_sha256']
 if run['returncode']!=0:failed.append(run);continue
 for row in csv.DictReader((P/run['csv']).open()):row['process']=run['process'];rows.append(row)
def cv(v):return st.stdev(v)/st.mean(v) if len(v)>1 and st.mean(v)!=0 else None
def corr(x,y):
 if len(x)<2 or st.stdev(x)==0 or st.stdev(y)==0:return None
 return sum((a-st.mean(x))*(b-st.mean(y)) for a,b in zip(x,y))/math.sqrt(sum((a-st.mean(x))**2 for a in x)*sum((b-st.mean(y))**2 for b in y))
x=[(int(r['pre_wall_ns'])+int(r['post_wall_ns']))/(2*int(r['adds'])) for r in rows]
y=[int(r['wall_ns'])/int(r['operations']) for r in rows]
z=[a/b for a,b in zip(y,x)]
invariant=all(len({r[k] for r in rows})==1 for k in ['size','member_bytes','seed','operations','adds','checksum','tree_bytes'])
duration=min(int(r[k]) for r in rows for k in ['wall_ns','pre_wall_ns','post_wall_ns'])
r=corr(x,y);ratio=cv(z)/cv(y) if cv(y) else None
perprocess=[]
for process in range(1,7):
 ids=[i for i,row in enumerate(rows) if row['process']==process]
 if not ids:continue
 xx=[x[i] for i in ids];yy=[y[i] for i in ids]
 perprocess.append({'process':process,'rows':len(ids),'mean_add_wall_ns':st.mean(xx),'mean_lookup_wall_ns':st.mean(yy),'lookup_cv':cv(yy),'lookup_min_ns':min(yy),'lookup_max_ns':max(yy),'within_process_correlation':corr(xx,yy)})
summary={'status':m['status'],'rows':len(rows),'failures':failed,'invariants':invariant,'minimum_region_ms':duration/1e6,'pearson_wall_r':r,'lookup_wall_cv':cv(y),'bracket_wall_cv':cv(x),'normalized_cv_ratio':ratio,'criterion_met':len(rows)==24 and not failed and invariant and duration>=10000000 and r is not None and r>=.70 and ratio is not None and ratio<=.50,'process_mean_correlation':corr([p['mean_add_wall_ns'] for p in perprocess],[p['mean_lookup_wall_ns'] for p in perprocess]),'processes':perprocess,'boundary_ids':sorted({int(row[k]) for row in rows for k in ['cpu_start','cpu_end','pre_cpu_start','pre_cpu_end','post_cpu_start','post_cpu_end']}),'different_lookup_boundary_ids':sum(row['cpu_start']!=row['cpu_end'] for row in rows),'qos_reported':sorted({row['qos_reported'] for row in rows})}
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(P/'SUMMARY.md').write_text(f'''# DIAG-002 descriptive association results

All {len(rows)} fixed lookup windows retained, no exclusions. Primary wall-time
correlation r={r:.4f}; CV(Y/X)/CV(Y)={ratio:.4f}. Preregistered criterion
(r>=0.70 AND ratio<=0.50): **{'met' if summary['criterion_met'] else 'not met'}**.
Invariants stable: {invariant}; minimum region {duration/1e6:.3f}ms.
Process-mean correlation {summary['process_mean_correlation']:.4f}; see summary.json
for all within-process ranges and correlations. Four repeated windows/process are
clustered observations, not independent random samples. No p-value or causal claim.

X is mean before/after dependent-add wall duration per add; Y is lookup wall duration
per operation. Y/X is a diagnostic ratio, never a replacement for wall-time gates.
No measured GHz, core type or CPU-cycle count; instruction latency and runtime
placement not independently established. Brackets do not measure the lookup's clock.
''')
print(json.dumps({k:v for k,v in summary.items() if k!='processes'},indent=2))
