from pathlib import Path
import json,hashlib,csv,statistics as st,math,sys
P=Path(__file__).resolve().parent;D=P/sys.argv[1];M=json.loads((D/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();results=[]
for v in ['A','B','C']:
 for c in M['cells']:
  for seed in M['seeds']:
   runs=[r for r in M['runs'] if r['variant']==v and r['cell']==c['name'] and r['seed']==seed];rows=[]
   for run in runs:
    for k in ['csv','stderr']:assert sha(D/run[k])==run[k+'_sha256']
    if run['returncode']!=0:continue
    data=list(csv.DictReader((D/run['csv']).open()));assert len(data)==1;r=data[0];r.update(block=run['block'],label=run['label']);rows.append(r)
   invariant=len(rows)==12 and all(len({r[k] for r in rows})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
   invariant &= all(int(r['size'])==100000 and r['operations']=='20000000' and r['traversals']=='200' and r['seed']==str(seed) and r['direction']==c['direction'] and r['encoding']==c['encoding'] and r['construction']==c['construction'] and int(r['mask'])==c['mask'] and int(r['member_bytes'])==c['bytes'] and r['checksum']==r['expected_checksum'] for r in rows)
   intervals={};effects={}
   for metric in ['elapsed_ns','thread_elapsed_ns']:
    e=[]
    for b in range(1,4):
     ab={l:[int(r[metric])/int(r['operations']) for r in rows if r['block']==b and r['label']==l] for l in 'AB'}
     if all(len(a)==2 and min(a)>0 for a in ab.values()):e.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
    if len(e)==3:m=st.mean(e);h=4.302652729696142*st.stdev(e)/math.sqrt(3);intervals[metric]=[m,m-h,m+h]
    else:intervals[metric]=[None,None,None]
    effects[metric]=e
   m,lo,hi=intervals['elapsed_ns'];ns={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rows if r['label']==l] for l in 'AB'}
   results.append(dict(variant=v,cell=c['name'],seed=seed,rows=len(rows),invariants=invariant,mean_pct=m,ci95_low_pct=lo,ci95_high_pct=hi,guard_pass=bool(invariant and hi is not None and hi<=1),guard_fail=bool(invariant and lo is not None and lo>1),intervals=intervals,effects_pct=effects,median_ns_op={l:st.median(a) if a else None for l,a in ns.items()},min_wall_ms=min(int(r['elapsed_ns']) for r in rows)/1e6 if rows else None,tree_bytes=sorted({r['tree_bytes'] for r in rows}),cpu_ids=sorted({r[k] for r in rows for k in ['cpu_start','cpu_end']}),boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in rows)))
(D/'summary.json').write_text(json.dumps(results,indent=2)+'\n');decisions=[]
for v in ['A','B','C']:
 failures=[c['name'] for c in M['cells'] if all(r['guard_fail'] for r in results if r['variant']==v and r['cell']==c['name'])];passing=[c['name'] for c in M['cells'] if all(r['guard_pass'] for r in results if r['variant']==v and r['cell']==c['name'])];decisions.append(dict(variant=v,both_seed_failures=failures,both_seed_passes=passing,status='REJECT' if M['phase']=='confirm' and failures else 'PARK'))
(D/'decisions.json').write_text(json.dumps(decisions,indent=2)+'\n')
lines=[f'# EXP-004 ordered guards — {M["phase"]}','','Wall ns/item paired effects; negative is faster.95%t df2 assumes independent normal blocks.','All guards share effective counts,exact checksums,construction fingerprints and tree bytes.','No primary substitution,headline speed claim or independent confirmation.','','| Variant | Cell | Seed | Effect% [95%CI] | Guard pass |','|---|---|---:|---|---|']
for r in results:lines.append(f"| {r['variant']} | {r['cell']} | {r['seed']} | {r['mean_pct']:+.3f} [{r['ci95_low_pct']:+.3f},{r['ci95_high_pct']:+.3f}] | {r['guard_pass']} |" if r['mean_pct'] is not None else '| incomplete |')
lines+=['','```json',json.dumps(decisions,indent=2),'```'];(D/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(json.dumps(decisions,indent=2));assert all(r['invariants'] for r in results)
