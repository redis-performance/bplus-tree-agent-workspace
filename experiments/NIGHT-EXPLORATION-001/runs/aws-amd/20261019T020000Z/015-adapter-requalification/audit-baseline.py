#!/usr/bin/env python3
"""Reconstruct isolated corrected-adapter baseline qualification from all raw rows."""
import argparse,csv,hashlib,json,pathlib,statistics,collections
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);a=p.parse_args();root=a.results;here=pathlib.Path(__file__).parent;expected=json.loads((here/'expected-inputs.json').read_text());m=json.loads((root/'manifest.json').read_text());op=json.loads((root/'operational-provenance.json').read_text());sizes=[100,1000,10000,100000,1000000];cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete'];assert m['status']=='complete' and len(m['runs'])==120
assert m['commit']==op['source_commit']==op['source_commit_after']==expected['commit'];assert m['source_hashes']==op['input_hashes_before']==op['input_hashes_after']==expected['files'];assert op['original_head_before']==op['original_head_after'];assert m['binary_sha256']==m['binary_sha256_after']==op['binary_sha256_after'];assert m['machine']['affinity']==op['inherited_affinity']==[2]
assert [m['arguments'][k] for k in ['ops','member_bytes','budget_seconds']]==[1000000,16,1200];assert m['timing_seconds']<=1200
names=['release-build-check','sanitize-build-check']+[f'sanitize-size-{n}' for n in sizes];assert [x['name'] for x in m['validation']]==names;assert all(x['returncode']==0 for x in m['validation'])
assert expected['files']['src/zset_btree.c']=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2';assert expected['files']['src/zset_btree.h']=='496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83'
schedule=[]
for b in range(6):
 for n in sizes[b%5:]+sizes[:b%5]:
  for step,label in enumerate('ABBA'):schedule.append((b,n,1+b%3,step,label))
groups=collections.defaultdict(list)
for run,spec in zip(m['runs'],schedule):
 assert tuple(run[k] for k in ['block','size','seed','step','label'])==spec
 assert run['returncode']==0
 for k in ['csv','stderr']:assert hashlib.sha256((root/run[k]).read_bytes()).hexdigest()==run[k+'_sha256']
 assert not (root/run['stderr']).read_text();rows=list(csv.DictReader((root/run['csv']).read_text().splitlines()));assert [r['case'] for r in rows]==cases
 for r in rows:
  assert [int(r[k]) for k in ['size','seed','member_bytes','requested_ops']]==[run['size'],run['seed'],16,1000000];assert r['cpu_start']==r['cpu_end']=='2';assert int(r['elapsed_ns'])>0 and int(r['operations'])>0
  groups[(run['size'],r['case'],run['block'])].append(r)
cells=collections.defaultdict(list)
for (n,case,b),rr in sorted(groups.items()):
 assert len(rr)==4
 for key in ['checksum','operations','tree_bytes','traversals','warmup_passes']:assert len({r[key] for r in rr})==1,(n,case,b,key)
 v=[int(r['elapsed_ns'])/int(r['operations']) for r in rr];e=100*((v[1]+v[2])/(v[0]+v[3])-1);cells[(n,case)].append({'block':b,'seed':1+b%3,'effect_pct':e,'min_window_ns':min(int(r['elapsed_ns']) for r in rr)})
assert len(groups)==240 and len(cells)==40
summary=[]
for (n,case),ee in sorted(cells.items()):
 assert [e['block'] for e in ee]==list(range(6));short=min(e['min_window_ns'] for e in ee)<10000000;noisy=any(abs(e['effect_pct'])>1 for e in ee)
 summary.append({'size':n,'case':case,'qualified':not short and not noisy,'short':short,'noisy':noisy,'max_abs_effect_pct':max(abs(e['effect_pct']) for e in ee),'minimum_window_ns':min(e['min_window_ns'] for e in ee),'blocks':ee})
out={'status':'complete_identity_and_raw_audit_pass','commit':expected['commit'],'source_selection':'NONE','processes':120,'raw_rows':960,'effects':240,'cells':40,'qualified_cells':sum(c['qualified'] for c in summary),'short_cells':sum(c['short'] for c in summary),'other_unqualified_cells':sum(not c['short'] and not c['qualified'] for c in summary),'all_validation_stages':7,'cpu':2,'binary_sha256':m['binary_sha256'],'cells_detail':summary,'limits':['Separate corrected-adapter baseline; no old/new speed comparison','Original matrix records serial execution order but not individual process wall timestamps; bounded-job and driver boundaries are retained','No retries or repair of short/noisy controls']}
(root/'independent-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['cells_detail','limits']}))
