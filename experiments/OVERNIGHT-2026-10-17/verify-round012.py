"""Read-only raw evidence audit, separate from the original decision analyses."""
from pathlib import Path
import csv,datetime,hashlib,json,math,statistics as st
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dt=lambda s:datetime.datetime.fromisoformat(s).timestamp()
windows=[];checks=[];interval_count=0
def checked_output(folder,row,stem=None):
    for stream in ['stdout','stderr']:
        path=folder/(stem+'.'+stream) if stem else folder/row[stream]
        assert sha(path)==row[stream+'_sha256'],str(path)
def snapshots(manifest):
    for desc in manifest['snapshots'].values():
        for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
def window(row,kind,label):
    a,b=dt(row['started_utc']),dt(row['ended_utc']);assert 0<=b-a<=121
    windows.append((a,b,kind,label))

for folder in [P/'BOUNDARY-015',P/'BOUNDARY-015/attempt-002',P/'BOUNDARY-016']:
    m=json.loads((folder/'manifest.json').read_text());snapshots(m)
    for r in m['runs']:
        checked_output(folder,r,r['name']);window(r,'validation',str(folder.relative_to(P))+'/'+r['name'])
    checks.append(str(folder.relative_to(P))+': snapshot and raw hashes')
for folder in [P/'BOUNDARY-015/faults',P/'BOUNDARY-016/faults']:
    faults=json.loads((folder/'manifest.json').read_text());assert len(faults)==2
    for fault in faults:
        assert fault['detected'] and sha(R/fault['snapshot']/'src/zset_btree.c')==fault['source_sha256']
        for r in fault['runs']:
            checked_output(folder,r,fault['name']+'-'+r['stage']);window(r,'validation',fault['name']+'-'+r['stage'])
        assert fault['runs'][0]['returncode']==0 and fault['runs'][1]['returncode']!=0
    checks.append(str(folder.relative_to(P))+': distinct patches and expected failures')
fifteen=json.loads((P/'BOUNDARY-015/summary.json').read_text())
assert len(fifteen['rows'])==24 and fifteen['status']=='pass'
for r in fifteen['rows']:
    assert r['summary']['checks']=='2751' and r['summary']['exact']=='2721586'
    assert r['summary']['edits']=='45993' and r['summary']['logical']=='be91811078f52d30'
assert all(fifteen['controlled_output_equality'].values())
m=json.loads((P/'BOUNDARY-015/attempt-002/manifest.json').read_text())
for n,h in m['root_hashes'].items():assert sha(R/n)==h
root_hashes=m['root_hashes']
sixteen=json.loads((P/'BOUNDARY-016/summary.json').read_text())
assert sixteen['status']=='pass' and sixteen['cells']==8 and 'operations=146250' in sixteen['output']
assert 'insertions=67860' in sixteen['output'] and 'deletions=78390' in sixteen['output']
assert 'digest=f1e55fd35eece517' in sixteen['output']

def ci(e):
    assert len(e)==6;m=st.mean(e);h=2.5705818366147395*st.stdev(e)/math.sqrt(6);return [m,m-h,m+h]
def near(a,b):
    assert len(a)==len(b) and all(abs(x-y)<1e-9 for x,y in zip(a,b)),(a,b)
all_parsed={}
for folder,n in [(P/'DIAG-014',192),(P/'DIAG-014/confirm',192),(P/'DIAG-015',288)]:
    m=json.loads((folder/'manifest.json').read_text());assert m['status']=='complete' and len(m['runs'])==n and len(m['warmup'])==1
    assert sha(R/m['binary'])==m['binary_sha256']==m['binary_sha256_after']
    parsed=[]
    for r in m['warmup']+m['runs']:
        assert r['returncode']==0
        for k in ['csv','stderr']:assert sha(folder/r[k])==r[k+'_sha256']
        rows=list(csv.DictReader((folder/r['csv']).open()));assert len(rows)==1;d=rows[0]
        requested=1000000 if r in m['warmup'] else 20000000
        assert int(d['operations'])==((requested+94)//95)*95 and int(d['traversals'])==(requested+94)//95
        assert d['checksum']==d['expected_checksum'] and int(d['warmup_passes'])==3 and d['size']=='95'
        window(r,'measurement',str(folder.relative_to(P))+'/'+r['csv'])
        if r not in m['warmup']:parsed.append((r,d))
    for i in range(0,len(parsed),2):
        pre,pd=parsed[i];target,td=parsed[i+1]
        assert pre['role']=='predecessor' and target['role']=='target'
        for key in ['target','seed','block','step','label']:assert pre[key]==target[key]
        assert target['cell']==target['target']
        if folder==P/'DIAG-014':same=target['label']=='A'
        elif folder==P/'DIAG-014/confirm':same=target['protocol']=='placebo' or target['label']=='B'
        else:same=target['protocol']=='placebo100' or target['label']=='A'
        assert (pre['cell']==target['cell'])==same
        assert target['coordinator_launch_gap_ns']==target['start_monotonic_ns']-pre['end_monotonic_ns']
        if folder==P/'DIAG-015' and target['protocol']!='gap0':assert target['coordinator_launch_gap_ns']>=100000000
    summary=json.loads((folder/'summary.json').read_text());recomputed={}
    for result in summary['results']:
        subset=[(r,d) for r,d in parsed if r['role']=='target' and r['seed']==result['seed'] and (r['cell']==result['cell'] if 'cell' in result else r['protocol']==result['protocol'])]
        assert len(subset)==24
        for k in ['tree_bytes','checksum','construction_fingerprint','operations']:assert len({d[k] for r,d in subset})==1
        for metric in ['elapsed_ns','thread_elapsed_ns']:
            effects=[]
            for block in range(1,7):
                rs=sorted([(r,d) for r,d in subset if r['block']==block],key=lambda x:x[0]['step'])
                assert ''.join(r['label'] for r,d in rs)=='ABBA'
                rates={l:st.mean(int(d[metric])/int(d['operations']) for r,d in rs if r['label']==l) for l in 'AB'}
                ratio=rates['A']/rates['B'] if folder==P/'DIAG-014/confirm' and result['protocol']=='contrast' else rates['B']/rates['A']
                effects.append(100*(ratio-1))
            near(effects,result['effects_pct'][metric]);near(ci(effects),result['intervals'][metric]);interval_count+=1
            recomputed[(result.get('cell',result.get('protocol')),result['seed'],metric)]=effects
    if folder==P/'DIAG-015':
        for result in summary['interactions']:
            for metric in ['elapsed_ns','thread_elapsed_ns']:
                zero=recomputed[('gap0',result['seed'],metric)];gap=recomputed[('gap100',result['seed'],metric)]
                e=[y-x for x,y in zip(zero,gap)];near(e,result['effects_pct'][metric]);near(ci(e),result['intervals'][metric]);interval_count+=1
    all_parsed[str(folder.relative_to(P))]=len(parsed)
    checks.append(str(folder.relative_to(P))+': counts, schedule, intervention, raw-derived intervals')
f=json.loads((P/'HARNESS-006/freeze.json').read_text())
for n,h in f['files'].items():assert sha(R/f['snapshot']/n)==h
windows.sort()
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
assert sum(w[2]=='measurement' for w in windows)==675
assert sum(w[2]=='validation' for w in windows)==122
assert interval_count==32
report=dict(status='PASS',measured_rows=672,prospective_warmups=3,measurement_windows=675,validation_windows=122,all_windows_serial=True,raw_derived_intervals=interval_count,checks=checks,rows=all_parsed,first_window_utc=datetime.datetime.fromtimestamp(windows[0][0],datetime.timezone.utc).isoformat(),last_window_utc=datetime.datetime.fromtimestamp(windows[-1][1],datetime.timezone.utc).isoformat(),root_hashes=root_hashes)
(P/'ROUND-012-VERIFY.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
