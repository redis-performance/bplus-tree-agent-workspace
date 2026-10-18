from pathlib import Path
import csv,json,statistics as st,math,hashlib
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());result=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def interval(e):
 if len(e)!=6:return [None,None,None]
 m=st.mean(e);h=2.5705818366147395*st.stdev(e)/math.sqrt(6);return [m,m-h,m+h]
for cell in M['cells']:
 for seed in M['seeds']:
  rows=[];failures=[]
  for run in M['runs']:
   if run['cell']!=cell['name'] or run['seed']!=seed:continue
   for k in ['csv','stderr']:assert sha(P/run[k])==run[k+'_sha256']
   if run['returncode']!=0:failures.append(run);continue
   data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1
   row=data[0];row.update(block=run['block'],label=run['label']);rows.append(row)
  effects={k:[] for k in ['elapsed_ns','thread_elapsed_ns']}
  for metric in effects:
   for b in range(1,7):
    ab={l:[int(r[metric])/int(r['operations']) for r in rows if r['block']==b and r['label']==l] for l in 'AB'}
    if all(len(v)==2 and min(v)>0 for v in ab.values()):effects[metric].append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
  invariant=len(rows)==24 and not failures and all(len({r[k] for r in rows})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
  invariant &= all(int(r['size'])==95 and int(r['operations'])==((20000000+94)//95)*95 and int(r['traversals'])==(20000000+94)//95 and r['seed']==str(seed) and r['direction']==cell['direction'] and r['encoding']==cell['encoding'] and r['construction']==cell['construction'] and int(r['mask'])==cell['mask'] and int(r['member_bytes'])==cell['bytes'] and r['checksum']==r['expected_checksum'] for r in rows)
  mean,low,high=interval(effects['elapsed_ns']);times=[int(r['elapsed_ns']) for r in rows];ns=[int(r['elapsed_ns'])/int(r['operations']) for r in rows];shares=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in rows if int(r['thread_elapsed_ns'])>=0]
  result.append(dict(cell=cell['name'],seed=seed,rows=len(rows),invariants=invariant,qualified=bool(invariant and low is not None and low>=-1 and high<=1 and min(times)>=10000000),effects_pct=effects['elapsed_ns'],mean_pct=mean,ci95_low_pct=low,ci95_high_pct=high,thread_effects_pct=effects['thread_elapsed_ns'],thread_interval=interval(effects['thread_elapsed_ns']),median_ns_op=st.median(ns) if ns else None,min_wall_ms=min(times)/1e6 if times else None,thread_wall_min=min(shares) if shares else None,thread_wall_max=max(shares) if shares else None,cpu_ids=sorted({r[k] for r in rows for k in ['cpu_start','cpu_end']}),boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in rows),qos=sorted({r[k] for r in rows for k in ['qos_reported_start','qos_reported_end']}),tree_bytes=sorted({r['tree_bytes'] for r in rows}),failures=failures))
(P/'summary-corrected.json').write_text(json.dumps(result,indent=2)+'\n');eligible=[c for c in M['cells'] if all(r['qualified'] for r in result if r['cell']==c['name'])]
(P/'eligible-corrected.json').write_text(json.dumps(eligible,indent=2)+'\n')
lines=['# AA-011 — wall-time precision','','Fixed six-block A/A; all384 rows retained. 95%t intervals assume independent normal block effects.','Frequency/effective QoS/within-window placement unknown. No source speed claim.','','| Cell | Seed | Rows | B/A mean % [95% interval] | Qualified |','|---|---:|---:|---|---|']
for r in result:lines.append(f"| {r['cell']} | {r['seed']} | {r['rows']} | {r['mean_pct']:+.3f} [{r['ci95_low_pct']:+.3f},{r['ci95_high_pct']:+.3f}] | {r['qualified']} |" if r['mean_pct'] is not None and r['ci95_low_pct'] is not None else f"| {r['cell']} | {r['seed']} | {r['rows']} | incomplete | False |")
lines+=['','Both-seed eligible cells: '+', '.join(c['name'] for c in eligible)]
(P/'SUMMARY-CORRECTED.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
