#!/usr/bin/env python3
"""Independent raw AA/discovery reconstruction; reviewer authored C."""
import argparse,csv,datetime,hashlib,json,pathlib,statistics
p=argparse.ArgumentParser();p.add_argument('campaign',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args();d=a.campaign/'017-corrected-neon';ad=a.campaign/'015-corrected-scan-aa'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text())
f=read(d/'comparison-freeze.json');af=read(ad/'comparison-freeze.json');x=read(d/'screen/result.json');ax=read(ad/'aa.json')
assert f['source_commit']==af['source_commit']=='13e459ff8800be3f02b6b45c87dd7b0c39453fa9' and f['compiler']==af['compiler']
for name,h in af['sha256'].items():assert h==(f['sources']['base']['binary_sha256'] if name=='build/btree-bench' else f['sources']['base']['source_hashes'][name])
assert sha(d/'run-screen.py')==f['driver_sha256'] and sha(d/'screen-schedule.json')==f['schedule_sha256'] and sha(ad/'run-aa.py')==af['aa_driver_sha256']
schedule=[];aas=[]
for block in range(6):
    sizes=[100000,1000000] if block%2==0 else [1000000,100000]
    for n in sizes:
        for pos in range(4):aas.append(dict(block=block,size=n,seed=401+block%3,position=pos))
    order=['A','B','C'];order=order[block%3:]+order[:block%3]
    for v in order:
        for n in sizes:
            for pos,side in enumerate(['baseline','candidate','candidate','baseline']):schedule.append(dict(index=len(schedule),block=block,variant=v,size=n,seed=401+block%3,position=pos,side=side))
assert read(d/'screen-schedule.json')==schedule
sem=['case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes']
def check_rows(state,slots,raw,prefix):
    assert state['status']=='complete' and state['elapsed_seconds']<=300
    assert len(state['rows'])==len(state['attempts'])==len(slots)
    for i,(r,s,t) in enumerate(zip(state['rows'],slots,state['attempts'])):
        assert {k:r[k] for k in s}==s and t['returncode']==0
        assert all(t[k]==val for k,val in r.items() if k!='row')
        v=s['variant'] if s.get('side')=='candidate' else 'base';src=f['sources'][v]
        assert r['command']==[str(pathlib.Path(src['root'])/src['timing_binary']),'--case','scan','--size',str(s['size']),'--ops','5000000','--member-bytes','16','--seed',str(s['seed'])]
        t0=datetime.datetime.fromisoformat(r['started_utc']);t1=datetime.datetime.fromisoformat(r['finished_utc']);assert t0<=t1
        if i:assert datetime.datetime.fromisoformat(state['rows'][i-1]['finished_utc'])<=t0
        op=raw/f'{prefix}-{i:03d}.stdout';data=list(csv.DictReader(op.read_text().splitlines()));assert len(data)==1 and data[0]==r['row'] and not op.with_suffix('.stderr').read_bytes()
        z=r['row'];assert [z['case'],int(z['size']),int(z['requested_ops']),int(z['member_bytes']),int(z['seed'])]==['scan',s['size'],5000000,16,s['seed']]
        assert int(z['cpu_start'])==int(z['cpu_end'])==2 and int(z['operations'])>=5000000
    effects=[]
    for i in range(0,len(slots),4):
        g=state['rows'][i:i+4]
        for k in sem:assert len({r['row'][k] for r in g})==1
        q=[int(r['row']['elapsed_ns'])/int(r['row']['operations']) for r in g];e=100*((q[1]+q[2])/(q[0]+q[3])-1);minimum=min(int(r['row']['elapsed_ns']) for r in g)
        effects.append(dict(variant=g[0].get('variant','AA'),size=g[0]['size'],seed=g[0]['seed'],block=g[0]['block'],effect_pct=e,min_window_ns=minimum,passes=minimum>=10000000 and (abs(e)<=1 if prefix=='aa' else e<=-2)))
    return effects
ae=check_rows(ax,aas,ad/'raw','aa');effects=check_rows(x,schedule,d/'screen/raw','screen');assert all(e['passes'] for e in ae)
for e,worker in zip(ae,ax['effects']):assert e['effect_pct']==worker['percent'] and e['passes']==worker['qualified']
for e,worker in zip(effects,x['effects']):assert e['effect_pct']==worker['effect_pct'] and e['passes']==worker['primary_gate']
fixtures={(r['size'],r['seed']):tuple(r['row'][k] for k in sem) for r in ax['rows']}
for r in x['rows']:assert tuple(r['row'][k] for k in sem)==fixtures[r['size'],r['seed']]
manifest_counts={}
for root,name in [(ad,'evidence-sha256.json'),(d,'screen-evidence-sha256.json')]:
    manifest=read(root/name)
    for file,h in manifest.items():assert sha(root/file)==h
    manifest_counts[name]=len(manifest)
post=read(d/'post-discovery-live-identity.json');assert post['status']=='pass'
for v,src in f['sources'].items():assert post['sources'][v]==dict(binary_sha256=src['binary_sha256'],source_referee_hashes_verified=len(src['source_hashes']))
summary={v:{str(n):dict(median_pct=statistics.median(e['effect_pct'] for e in effects if e['variant']==v and e['size']==n),passes=sum(e['passes'] for e in effects if e['variant']==v and e['size']==n)) for n in [100000,1000000]} for v in ['A','B','C']}
survivors=[v for v in ['B','C','A'] if all(e['passes'] for e in effects if e['variant']==v)]
r=dict(status='pass',revision='144ee7e0d',rows=144,blocks=36,aa_rows=48,aa_blocks=12,aa_qualified=True,manifest_entries=manifest_counts,summary=summary,effects=effects,aa_effects=ae,survivors=survivors,all_blocks_slower=all(e['effect_pct']>0 for e in effects),confirmation_eligible=bool(survivors),decision='REJECT/NONE' if not survivors else 'FURTHER_GATES',source_adoption='NONE',limits='C authored by reviewer; binary/source execution checks supported by pinned driver completion and published post identity, not independent remote rehash; no host access')
a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k not in ['effects','aa_effects']}))
