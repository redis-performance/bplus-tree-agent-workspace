from pathlib import Path
import csv,hashlib,json,math,statistics as st
P=Path(__file__).resolve().parent/'confirm';M=json.loads((P/'manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert M['status']=='complete' and len(M['runs'])==192 and len(M['warmup'])==1
data=[]
for r in M['runs']:
    assert r['returncode']==0
    for k in ['csv','stderr']:assert sha(P/r[k])==r[k+'_sha256']
    rows=list(csv.DictReader((P/r['csv']).open()));assert len(rows)==1
    d=rows[0];c=next(c for c in M['cells'] if c['name']==r['cell'])
    assert int(d['operations'])==20000065 and int(d['traversals'])==210527 and d['checksum']==d['expected_checksum']
    assert d['seed']==str(r['seed']) and d['direction']=='forward' and d['construction']=='trimmed'
    assert d['encoding']==c['encoding'] and int(d['mask'])==c['mask'] and int(d['warmup_passes'])==3 and int(d['member_bytes'])==16 and int(d['size'])==95
    data.append((r,d))
for c in M['cells']:
    for seed in M['seeds']:
        subset=[d for r,d in data if r['cell']==c['name'] and r['seed']==seed]
        for k in ['checksum','construction_fingerprint','tree_bytes','operations']:assert len({d[k] for d in subset})==1
def interval(e):
    assert len(e)==6;m=st.mean(e);h=2.5705818366147395*st.stdev(e)/math.sqrt(6);return [m,m-h,m+h]
results=[]
for protocol in M['protocols']:
    for seed in M['seeds']:
        rows=[(r,d) for r,d in data if r['role']=='target' and r['protocol']==protocol and r['seed']==seed];assert len(rows)==24
        effects={};intervals={}
        for metric in ['elapsed_ns','thread_elapsed_ns']:
            e=[]
            for b in range(1,7):
                ab={l:[int(d[metric])/int(d['operations']) for r,d in rows if r['block']==b and r['label']==l] for l in 'AB'}
                assert all(len(v)==2 and min(v)>0 for v in ab.values())
                e.append(100*((st.mean(ab['A'])/st.mean(ab['B'])) if protocol=='contrast' else (st.mean(ab['B'])/st.mean(ab['A'])))-100)
            effects[metric]=e;intervals[metric]=interval(e)
        ci=intervals['elapsed_ns'];wall=[int(d['elapsed_ns']) for r,d in rows]
        passes=ci[2]<-1 if protocol=='contrast' else ci[1]>=-1 and ci[2]<=1
        results.append(dict(protocol=protocol,seed=seed,rows=len(rows),effects_pct=effects,intervals=intervals,passes=passes,min_wall_ms=min(wall)/1e6,launch_gaps_ns=[r['coordinator_launch_gap_ns'] for r,d in rows],cpu_ids=sorted({d[k] for r,d in rows for k in ['cpu_start','cpu_end']}),boundary_changes=sum(d['cpu_start']!=d['cpu_end'] for r,d in rows),qos=sorted({d[k] for r,d in rows for k in ['qos_reported_start','qos_reported_end']})))
valid=all(r['min_wall_ms']>=10 for r in results)
contrast=all(r['passes'] for r in results if r['protocol']=='contrast');placebo=all(r['passes'] for r in results if r['protocol']=='placebo')
summary=dict(status='confirmed' if valid and contrast and placebo else 'PARK',invariants=True,duration_gate=valid,contrast_passes=contrast,placebo_passes=placebo,results=results)
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2));assert valid
