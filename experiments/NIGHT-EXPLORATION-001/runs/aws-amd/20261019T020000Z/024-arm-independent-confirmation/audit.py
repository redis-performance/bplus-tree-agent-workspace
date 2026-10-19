#!/usr/bin/env python3
"""Held-out raw reconstruction; no dependency on the ARM worker's audit."""
import argparse,csv,datetime,hashlib,json,pathlib,statistics
HERE=pathlib.Path(__file__).resolve().parent
SEMANTICS=('case','size','requested_ops','member_bytes','seed','operations','checksum','tree_bytes','traversals','warmup_passes')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inputs():
    f=json.loads((HERE/'freeze.json').read_text())
    for name,h in f['files'].items():assert sha(HERE/name)==h,('frozen input changed',name)
    return json.loads((HERE/'discovery-freeze.json').read_text()),json.loads((HERE/'schedule.json').read_text())
def expected(selected):
    f,_=inputs();return {v:{**f['sources'][v]['source_hashes'],f['sources'][v]['timing_binary']:f['sources'][v]['binary_sha256']} for v in ['base',selected]}
def audit(folder,aa=None):
    folder=pathlib.Path(folder);x=json.loads((folder/'result.json').read_text());phase=x['phase'];v=x['selected']
    assert phase in ('aa','confirm') and v in ('A','B','C') and x['status']=='complete'
    _,schedule=inputs();pins=expected(v);assert x['initial_hashes']==x['final_hashes']==pins
    assert x['wall_seconds']<=300 and x['driver_affinity']==[2]
    assert x['input_hashes']=={n:sha(HERE/n) for n in ['freeze.json','driver.py','audit.py','schedule.json','discovery-freeze.json']}
    grant=x['grant'];assert grant['selected']==v and grant['root_authorized'] is True
    for k in ['selection_revision','root_grant','idle_handoff_utc']:assert isinstance(grant[k],str) and grant[k]
    assert x['grant_sha256']==hashlib.sha256(x['grant_text'].encode()).hexdigest() and json.loads(x['grant_text'])==grant
    rows=x['processes'];assert len(rows)==48
    for i,(r,s) in enumerate(zip(rows,schedule)):
        assert all(r[k]==val for k,val in s.items());target=v if phase=='confirm' and s['position'] in [1,2] else 'base'
        assert r['binary']==target and r['returncode']==0
        assert r['argv']==['<'+target+'>/build/btree-bench','--case','scan','--size',str(s['size']),'--ops','5000000','--member-bytes','16','--seed',str(s['seed'])]
        t0=datetime.datetime.fromisoformat(r['started_utc']);t1=datetime.datetime.fromisoformat(r['finished_utc']);assert t0<=t1
        if i:assert datetime.datetime.fromisoformat(rows[i-1]['finished_utc'])<=t0
        raw=folder/'raw'/f'{i:03d}.stdout';err=raw.with_suffix('.stderr')
        data=list(csv.DictReader(raw.read_text().splitlines()));assert len(data)==1 and data[0]==r['row'] and not err.read_bytes()
        assert sha(raw)==r['stdout_sha256'] and sha(err)==r['stderr_sha256']
        z=r['row'];assert [z['case'],int(z['size']),int(z['requested_ops']),int(z['member_bytes']),int(z['seed'])]==['scan',s['size'],5000000,16,s['seed']]
        assert int(z['cpu_start'])==int(z['cpu_end'])==2 and int(z['operations'])>=5000000
        assert int(z['elapsed_ns'])>0
    effects=[]
    for start in range(0,48,4):
        g=rows[start:start+4]
        for k in SEMANTICS:assert len({r['row'][k] for r in g})==1,(start,k)
        q=[int(r['row']['elapsed_ns'])/int(r['row']['operations']) for r in g];e=100*((q[1]+q[2])/(q[0]+q[3])-1)
        window=min(int(r['row']['elapsed_ns']) for r in g)
        effects.append(dict(size=g[0]['size'],block=g[0]['block'],seed=g[0]['seed'],effect_pct=e,minimum_elapsed_ns=window,passes=window>=10000000 and (abs(e)<=1 if phase=='aa' else e<=-2)))
    if phase=='confirm':
        assert aa is not None;control=audit(aa);assert control['qualified'] and control['selected']==v
        ar=json.loads((pathlib.Path(aa)/'result.json').read_text())
        assert ar['grant']==grant and x['aa_result_sha256']==sha(pathlib.Path(aa)/'result.json')
        assert datetime.datetime.fromisoformat(ar['finished_utc'])<=datetime.datetime.fromisoformat(x['started_utc'])
        for before,after in zip(ar['processes'],rows):
            for k in SEMANTICS:assert before['row'][k]==after['row'][k],k
    return dict(phase=phase,selected=v,status='audited',qualified=all(e['passes'] for e in effects),processes=48,blocks=12,effects=effects,median_effect_pct={str(n):statistics.median(e['effect_pct'] for e in effects if e['size']==n) for n in [100000,1000000]},source_adoption='NONE',reviewer='AMD native agent; authored C; exact model/cost unknown')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('evidence',type=pathlib.Path);p.add_argument('--aa',type=pathlib.Path);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
    result=audit(a.evidence,a.aa);a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
