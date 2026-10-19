from pathlib import Path
import json,subprocess,time,datetime,sys
from common import ROOT,P,SOURCES,sha,check_execution,actual_identity,build_identity
start=time.monotonic();phase=sys.argv[1];assert phase in ['calibration','guard-aa','guard-b'];cap=60 if phase=='calibration' else 120;check_execution();assert json.loads((P/'preparation-summary.json').read_text())['status']=='pass';out=P/(phase+'.json');assert not out.exists();actual_identity('actual-before-'+phase);build_identity('build-before-'+phase)
if phase!='calibration':
 for f,h in json.loads((P/'guard-timing-freeze.json').read_text())['files'].items():assert sha(P/f)==h
if phase=='guard-b':
 control=json.loads((P/'guard-aa-audit.json').read_text());assert control['status']=='pass' and control['phase_status']=='complete' and control['qualified']
(P/'guard-raw').mkdir(exist_ok=True);models={x['seed']:x for x in json.loads((P/'fresh-guard-models.json').read_text())};m=dict(status='running',phase=phase,cap_seconds=cap,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),rows=[])
def save():out.write_text(json.dumps(m,indent=2)+'\n')
def run(spec):
 left=cap-(time.monotonic()-start);assert left>0;i=len(m['rows']);tag=f'{phase}-{i:03d}';cmd=[str(SOURCES/spec['binary']/'build/supplement/scan-supplement'),'run','trim','319',str(spec['seed']),'2',str(spec['passes']),'0'];t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=left)
 except subprocess.TimeoutExpired as e:
  for ext,val in [('stdout',e.stdout),('stderr',e.stderr)]:(P/'guard-raw'/(tag+'.'+ext)).write_text(val.decode(errors='replace') if isinstance(val,bytes) else val or '')
  (P/(tag+'-timeout.json')).write_text(json.dumps(dict(spec=spec,started_utc=t,timeout_seconds=e.timeout),indent=2)+'\n');raise
 (P/'guard-raw'/(tag+'.stdout')).write_text(r.stdout);(P/'guard-raw'/(tag+'.stderr')).write_text(r.stderr);r.check_returncode();row=json.loads(r.stdout);model=models[spec['seed']]
 for k in ['history','bytes','seed','encoding','n','callbacks_per_pass','checksum_per_pass']:assert row[k]==model[k]
 assert row['start_cpu']==row['end_cpu']==2 and row['passes']==spec['passes'] and row['logical_members']==7*spec['passes'];assert row['warmup_passes']==row['prepost_oracles']==2 and row['warmup_callback_parity'] and row['validation']=='pass';m['rows'].append(dict(index=i,**spec,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode,row=row));save();return row
try:
 if phase=='calibration':
  for seed in [701,702,703]:
   probe=1
   while True:
    row=run(dict(binary='base',seed=seed,passes=probe,kind='probe'))
    if row['elapsed_ns']>=20000000:break
    assert probe<10000000;probe*=10
   for repeat in range(3):run(dict(binary='base',seed=seed,passes=probe,kind='trial',repeat=repeat))
 else:
  for spec in json.loads((P/(phase+'-schedule.json')).read_text()):run(spec)
 m['status']='complete'
except Exception as e:m['status']='stopped';m['error']=repr(e);raise
finally:
 m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();build_identity('build-after-'+phase);actual_identity('actual-after-'+phase)
print('COMPLETE',phase,len(m['rows']))
