#!/usr/bin/env python3
import argparse,datetime,json,decimal
from native_common import HERE,CELLS,IDS,sha,check_row,same_semantics
p=argparse.ArgumentParser();p.add_argument('--phase',required=True,choices=['native-AA','native-comparison']);a=p.parse_args();out=HERE/a.phase;s=json.loads((out/'result.json').read_text());schedule=json.loads((HERE/'schedules.json').read_text())[a.phase];D=decimal.Decimal;decimal.getcontext().prec=40;dt=datetime.datetime.fromisoformat
assert s['status']=='complete' and len(s['runs'])==len(schedule)==144 and s['cpu']==2
assert s['freeze_sha256']==sha(HERE/'native-execution-freeze.json');f=json.loads((HERE/'native-execution-freeze.json').read_text());assert all(sha(HERE/n)==h for n,h in f['files'].items())
assert s['identities_before']==s['identities_after'];assert s['identities_before']['binaries']=={n:v['sha256'] for n,v in IDS['binaries'].items()}
for name,got in s['identities_before']['sources'].items():
 expected=dict(IDS['source_hashes'])
 if name.endswith('-A'):expected['src/zset_btree.c']=IDS['candidate_source_sha256']
 if name.startswith('h4-'):expected['bench/iterator_modes.c']=sha(HERE/'inputs/iterator_modes.c')
 assert got==expected
assert (dt(s['finished_utc'])-dt(s['started_utc'])).total_seconds()<=600 and s['elapsed_seconds']<=600 and dt(s['finished_utc'])<=dt(s['deadline'])
refs={};aa=None
if a.phase=='native-comparison':
 assert s['AA_result_sha256']==sha(HERE/'native-AA/result.json') and s['AA_audit_sha256']==sha(HERE/'native-AA/audit.json');aa=json.loads((HERE/'native-AA/audit.json').read_text());assert aa['status']=='integrity_pass';assert len(aa['raw_files_sha256'])==288 and all(sha(HERE/'native-AA'/n)==h for n,h in aa['raw_files_sha256'].items())
 for r in json.loads((HERE/'native-AA/result.json').read_text())['runs']:refs[(r['cell'],r['seed'])]=check_row((HERE/'native-AA'/r['stdout']).read_text(),r)
rows=[];previous=dt(s['started_utc'])
for r,c in zip(s['runs'],schedule):
 assert all(r[k]==v for k,v in c.items());assert r['returncode']==0 and not (out/r['stderr']).read_text().strip();assert previous<=dt(r['started_utc'])<=dt(r['finished_utc'])<=dt(s['finished_utc']);assert (dt(r['finished_utc'])-dt(r['started_utc'])).total_seconds()<=60;previous=dt(r['finished_utc']);row=check_row((out/r['stdout']).read_text(),c);ref=refs.setdefault((c['cell'],c['seed']),row);assert same_semantics(row,ref);rows.append(row)
report=[]
for cell in CELLS:
 blocks=[]
 for block in range(6):
  ix=[i for i,c in enumerate(schedule) if c['cell']==cell and c['block']==block];assert len(ix)==4;v=[D(rows[i]['elapsed_ns'])/D(rows[i]['operations']) for i in ix];effect=((v[1]+v[2])/(v[0]+v[3])-1)*100;blocks.append(dict(block=block,seed=schedule[ix[0]]['seed'],effect_pct=str(effect),minimum_window_ns=min(int(rows[i]['elapsed_ns']) for i in ix)))
 qualified=all(abs(D(x['effect_pct']))<=1 and x['minimum_window_ns']>=10000000 for x in blocks) if aa is None else next(x['qualified'] for x in aa['cells'] if x['id']==cell)
 report.append(dict(id=cell,qualified=qualified,blocks=blocks,scope='fresh diagnostic replication; priorREJECT unchanged'))
r=dict(status='integrity_pass',phase=a.phase,processes=144,rows=144,blocks=36,cells=report,all_cells_qualified=all(x['qualified'] for x in report),source_selection='NONE',prior_decision='REJECT',raw_files_sha256={r[k]:sha(out/r[k]) for r in s['runs'] for k in ['stdout','stderr']},result_sha256=sha(out/'result.json'));(out/'audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
