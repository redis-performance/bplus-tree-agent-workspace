from pathlib import Path
import csv,hashlib,json,math,statistics as st
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert M['status']=='complete' and len(M['runs'])==48 and len(M['warmup'])==1
def ci(e):
    assert len(e)==6;m=st.mean(e);h=2.5705818366147395*st.stdev(e)/math.sqrt(6);return[m,m-h,m+h]
parsed=[]
for r in M['warmup']+M['runs']:
    assert r['returncode']==0
    for k in ['csv','stderr','completion']:assert sha(P/r[k])==r[k+'_sha256']
    ds=list(csv.DictReader((P/r['csv']).open()));assert len(ds)==1;d=ds[0];c=json.loads((P/r['completion']).read_text())
    assert c['child_status']==0 and c['timed_out']==0
    delay=r['parent_clock_return_ns']-c['waitpid_observed_ns'];assert delay>=0
    ops=1000000 if r['block']==0 else 20000000
    assert int(d['operations'])==((ops+94)//95)*95 and int(d['traversals'])==(ops+94)//95 and d['checksum']==d['expected_checksum']
    assert d['seed']==str(r['seed']) and d['size']=='95' and d['member_bytes']=='16' and d['mask']=='6' and d['encoding']=='alternating-zero' and d['construction']=='trimmed' and d['direction']=='forward' and d['warmup_passes']=='3'
    if r['block']:parsed.append((r,d,delay/1e6))
results=[]
for seed in M['seeds']:
    rows=[t for t in parsed if t[0]['seed']==seed];assert len(rows)==24
    for k in ['checksum','operations','tree_bytes','construction_fingerprint']:assert len({d[k] for r,d,g in rows})==1
    effects={k:[] for k in ['observed_delay_ms','elapsed_ns','thread_elapsed_ns']}
    for block in range(1,7):
        pair={l:[(d,g) for r,d,g in rows if r['block']==block and r['label']==l] for l in 'AB'};assert all(len(x)==2 for x in pair.values())
        effects['observed_delay_ms'].append(st.mean(g for d,g in pair['A'])-st.mean(g for d,g in pair['B']))
        for metric in ['elapsed_ns','thread_elapsed_ns']:effects[metric].append(100*(st.mean(int(d[metric])/int(d['operations']) for d,g in pair['B'])/st.mean(int(d[metric])/int(d['operations']) for d,g in pair['A'])-1))
    intervals={k:ci(v) for k,v in effects.items()};dur=min(int(d['elapsed_ns']) for r,d,g in rows)/1e6
    results.append(dict(seed=seed,effects=effects,intervals=intervals,passes=intervals['observed_delay_ms'][1]>5,min_wall_ms=dur,observed_delay_ms={l:[g for r,d,g in rows if r['label']==l] for l in 'AB'},cpu_ids=sorted({d[k] for r,d,g in rows for k in ['cpu_start','cpu_end']})))
valid=all(r['min_wall_ms']>=10 for r in results);summary=dict(status='supported' if valid and all(r['passes'] for r in results) else 'unsupported' if valid else 'invalid',invariants=True,results=results)
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));assert valid
