#!/usr/bin/env python3
import csv,hashlib,json,statistics as st
from pathlib import Path
HERE=Path(__file__).resolve().parent
m=json.loads((HERE/'manifest.json').read_text())
rows=[]
for r in m['runs']:
    for key in ['csv','stderr']:
        assert hashlib.sha256((HERE/r[key]).read_bytes()).hexdigest()==r[key+'_sha256']
    if r['returncode'] != 0: continue
    for row in csv.DictReader((HERE/r['csv']).open()):
        row.update(block=r['block'],arm=r['arm'],process=r['process'])
        rows.append(row)
invariants=all(len({r[k] for r in rows})==1 for k in ['operations','checksum','tree_bytes'])
blocks=[]
for block in range(1,7):
    result={'block':block}
    for arm in ['fresh','reuse']:
        selected=[r for r in rows if r['block']==block and r['arm']==arm]
        values=[int(r['elapsed_ns'])/int(r['operations']) for r in selected]
        assert len(values)==6
        result[arm]={'ns_per_op':values,'mean':st.mean(values),'cv_pct':100*st.stdev(values)/st.mean(values),
                     'min':min(values),'max':max(values),
                     'different_boundary_ids':sum(r['cpu_start']!=r['cpu_end'] for r in selected),
                     'thread_wall_ratios':[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in selected]}
    result['reuse_over_fresh_mean']=result['reuse']['mean']/result['fresh']['mean']
    result['half_cv']=result['reuse']['cv_pct']<=result['fresh']['cv_pct']/2
    result['reuse_last_over_first']=result['reuse']['ns_per_op'][-1]/result['reuse']['ns_per_op'][0]
    blocks.append(result)
support=invariants and len(rows)==72 and m['status']=='complete' and sum(b['half_cv'] for b in blocks)>=4
out={'status':m['status'],'rows':len(rows),'invariants_stable':invariants,'blocks_meeting_half_cv':sum(b['half_cv'] for b in blocks),
     'hypothesis_supported':support,'blocks':blocks}
(HERE/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# DIAG-001 descriptive results','','Identical lookup code; process/fixture reuse diagnostic, not speedup or A/A qualification.','',
       '| Block | Fresh CV % | Reuse CV % | Reuse/fresh mean | Reuse last/first | Half CV? |',
       '|---|---:|---:|---:|---:|---|']
for b in blocks:
    lines.append(f"| {b['block']} | {b['fresh']['cv_pct']:.3f} | {b['reuse']['cv_pct']:.3f} | {b['reuse_over_fresh_mean']:.4f} | {b['reuse_last_over_first']:.4f} | {'yes' if b['half_cv'] else 'no'} |")
lines+=['',f"All {len(rows)} windows retained; invariants stable: {invariants}. Criterion met in {out['blocks_meeting_half_cv']}/6 blocks; hypothesis supported: {support}.",
        'Frequency, effective QoS, within-window residency and the causal contribution of each reuse effect remain unknown.']
(HERE/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
