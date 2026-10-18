from pathlib import Path
from collections import defaultdict
import csv,json,hashlib,statistics as s
P=Path(__file__).resolve().parent;m=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(P/'PLAN.md')==m['plan_sha256'] and m['status']=='complete' and len(m['runs'])==48
blocks=defaultdict(list);structures=defaultdict(set);fingerprints=defaultdict(set);duration_ok=True;allrows=[]
for run in m['runs']:
 assert run['returncode']==0
 for f in ['csv','stderr']:assert sha(P/run[f])==run[f+'_sha256']
 data=list(csv.DictReader((P/run['csv']).open()));assert len(data)==1;r=data[0]
 b=run['block'];seed=run['seed'];cell=run['cell']
 assert seed==[211,211,307,307,401,401][b-1] and int(r['seed'])==seed
 assert r['fixture_order']==('ascending' if cell[0]=='A' else 'shuffled')
 assert r['query_order']==('coupled' if cell[1]=='S' else 'independent')
 assert int(r['member_bytes'])==320 and int(r['size'])==100000 and int(r['operations'])==5000000
 assert int(r['checksum'])==249997500000 and int(r['warmup_passes'])==10
 duration_ok &= int(r['elapsed_ns'])>=10000000
 r.update(block=b,seed=seed,cell=cell,slot=run['slot'],ns_op=int(r['elapsed_ns'])/5000000)
 structures[seed,cell[0]].add(tuple(int(r[k]) for k in ['tree_bytes','leaf_count','leaf_min','leaf_max']))
 fingerprints[seed,cell[1]].add(r['query_fingerprint'])
 blocks[b].append(r);allrows.append(r)
assert all(len(v)==1 for v in structures.values()) and all(len(v)==1 for v in fingerprints.values())
for seed in [211,307,401]:assert fingerprints[seed,'S']!=fingerprints[seed,'I']
results=[]
for b,rows in sorted(blocks.items()):
 first=['AS','BS','BI','AI'] if b%2 else ['AI','BI','BS','AS']
 assert [r['cell'] for r in rows]==first+list(reversed(first))
 means={c:s.mean(r['ns_op'] for r in rows if r['cell']==c) for c in ['AS','BS','BI','AI']}
 cv={c:s.stdev(r['ns_op'] for r in rows if r['cell']==c)/means[c] for c in means}
 rs=means['AS']/means['BS'];ri=means['AI']/means['BI']
 results.append(dict(block=b,seed=rows[0]['seed'],means=means,cv=cv,ratio_coupled=rs,ratio_independent=ri,interaction=rs/ri))
interactions=[r['interaction'] for r in results];median=s.median(interactions);positive=sum(x>1 for x in interactions)
summary=dict(rows=48,blocks=results,median_interaction=median,blocks_interaction_above_one=positive,durations_valid=duration_ok,
 criterion_met=duration_ok and median>=1.10 and positive>=5,
 structures={str(k):list(next(iter(v))) for k,v in structures.items()},query_fingerprints={str(k):next(iter(v)) for k,v in fingerprints.items()},
 boundary_changes=sum(r['cpu_start']!=r['cpu_end'] for r in allrows),thread_wall_ratios=[int(r['thread_elapsed_ns'])/int(r['elapsed_ns']) for r in allrows])
(P/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# DIAG-005 descriptive results','','Six balanced process blocks; all cells use320-byte members. Wall time primary.', 'Interaction = (ascending/shuffled under coupled queries)/(ascending/shuffled under independent queries).','', '| Block | Seed | AS ns/op | BS ns/op | AI ns/op | BI ns/op | Coupled ratio | Independent ratio | Interaction |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
for r in results:
 v=r['means'];lines.append(f"| {r['block']} | {r['seed']} | {v['AS']:.3f} | {v['BS']:.3f} | {v['AI']:.3f} | {v['BI']:.3f} | {r['ratio_coupled']:.6f} | {r['ratio_independent']:.6f} | {r['interaction']:.6f} |")
lines+=['',f'Median interaction {median:.6f}; above one in {positive}/6 blocks. Fixed criterion met: {summary["criterion_met"]}.',f'All48 counts/checksums/structure/fingerprint controls pass. Boundary CPU changes: {summary["boundary_changes"]}.','Frequency/effective QoS/residency unknown. No causal cache mechanism, source speedup or qualification claimed.']
(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print('\n'.join(lines))
