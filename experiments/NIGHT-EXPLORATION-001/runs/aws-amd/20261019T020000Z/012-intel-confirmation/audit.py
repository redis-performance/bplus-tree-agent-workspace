#!/usr/bin/env python3
"""Independent reconstruction of the fixed held-out AA/confirmation raw evidence."""
import argparse,csv,json,pathlib,statistics,datetime
p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);p.add_argument('--aa',type=pathlib.Path);a=p.parse_args()
x=json.loads((a.evidence/'result.json').read_text());phase=x['phase'];assert phase in ['aa','confirm'];assert x['status']=='complete'
expected=json.loads((pathlib.Path(__file__).parent/'expected-hashes.json').read_text());assert x['initial_hashes']==x['final_hashes']==expected
rows=x['processes'];assert len(rows)==48;assert x['wall_seconds']<=300
semantics=['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes'];effects=[]
for i,r in enumerate(rows):
    size=[100000,1000000][i//24];block=i%24//4;position=i%4;seed=201+block%3
    assert [r['index'],r['size'],r['block'],r['position'],r['seed']]==[i,size,block,position,seed]
    assert r['binary']==('B' if phase=='confirm' and position in [1,2] else 'base')
    assert r['returncode']==0
    t0=datetime.datetime.fromisoformat(r['started_utc']);t1=datetime.datetime.fromisoformat(r['finished_utc']);assert t0<=t1
    if i:assert datetime.datetime.fromisoformat(rows[i-1]['finished_utc'])<=t0
    data=list(csv.DictReader((a.evidence/'raw'/f'{i:03d}.stdout').read_text().splitlines()));assert len(data)==1 and data[0]==r['row'];assert not (a.evidence/'raw'/f'{i:03d}.stderr').read_text()
    z=r['row'];assert [z['case'],int(z['size']),int(z['requested_ops']),int(z['member_bytes']),int(z['seed'])]==['scan',size,5000000,16,seed]
    assert int(z['cpu_start'])==int(z['cpu_end'])==2;assert int(z['elapsed_ns'])>=10000000;assert int(z['operations'])>=5000000
for start in range(0,48,4):
    group=rows[start:start+4]
    for k in semantics:assert len({r['row'][k] for r in group})==1,(start,k)
    q=[int(r['row']['elapsed_ns'])/int(r['row']['operations']) for r in group]
    effect=((q[1]+q[2])/(q[0]+q[3])-1)*100
    effects.append({'size':group[0]['size'],'block':group[0]['block'],'seed':group[0]['seed'],'effect_pct':effect,'passes':abs(effect)<=1 if phase=='aa' else effect<=-2})
if phase=='confirm':
    assert a.aa,'qualification evidence required'
    aa=json.loads((a.aa/'audit.json').read_text());assert aa['phase']=='aa' and aa['qualified'] and aa['processes']==48
    ar=json.loads((a.aa/'result.json').read_text())['processes']
    for before,after in zip(ar,rows):
        for k in semantics:assert before['row'][k]==after['row'][k],k
result={'phase':phase,'status':'audited','qualified':all(e['passes'] for e in effects),'processes':48,'blocks':12,'effects':effects,'median_effect_pct':{str(n):statistics.median(e['effect_pct'] for e in effects if e['size']==n) for n in [100000,1000000]},'minimum_elapsed_ns':min(int(r['row']['elapsed_ns']) for r in rows),'source_adoption':'NONE','reviewer':'independent AMD native agent; exact model and costs unknown'}
a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'phase':phase,'qualified':result['qualified'],'median_effect_pct':result['median_effect_pct']}))
