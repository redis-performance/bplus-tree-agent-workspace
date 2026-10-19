from pathlib import Path
import json,subprocess,time,datetime,hashlib,sys,itertools
p=Path(__file__).parent;phase=sys.argv[1];assert phase in ['calibration','aa','b'];cap=180 if phase=='calibration' else 480;out=p/(phase+'.json');assert not out.exists();assert json.loads((p/'preparation-summary.json').read_text())['status']=='pass';(p/'raw').mkdir(exist_ok=True)
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for v,files in json.loads((p/'build-freeze.json').read_text()).items():
 for f,h in files.items():assert sha(Path('scratch/intel-scan-supplement')/v/f)==h
if phase!='calibration':
 for f,h in json.loads((p/'timing-freeze.json').read_text())['files'].items():assert sha(p/f)==h
if phase=='b':assert json.loads((p/'aa-audit.json').read_text())['phase_status']=='complete'
start=time.monotonic();m=dict(status='running',phase=phase,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cap_seconds=cap,rows=[])
def save():out.write_text(json.dumps(m,indent=2)+'\n')
def run(spec):
 left=cap-(time.monotonic()-start);assert left>0,'fixed phase cap';index=len(m['rows']);tag=f'{phase}-{index:04d}';cmd=['scratch/intel-scan-supplement/'+spec['binary']+'/build/supplement/scan-supplement','run',spec['history'],str(spec['bytes']),str(spec['seed']),str(spec['encoding']),str(spec['passes']),'0'];begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,left))
 except subprocess.TimeoutExpired as e:
  for ext,v in [('stdout',e.stdout),('stderr',e.stderr)]:(p/'raw'/(tag+'.'+ext)).write_text(v.decode(errors='replace') if isinstance(v,bytes) else v or '')
  (p/(tag+'-timeout.json')).write_text(json.dumps(dict(spec=spec,command=cmd,started_utc=begin,timeout_seconds=e.timeout),indent=2)+'\n');raise
 (p/'raw'/(tag+'.stdout')).write_text(r.stdout);(p/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr;row=json.loads(r.stdout);assert row['start_cpu']==row['end_cpu']==2 and row['validation']=='pass'
 for k in ['history','bytes','seed','encoding','passes']:assert row[k]==spec[k]
 assert row['warmup_passes']==2 and row['prepost_oracles']==2 and row['warmup_callback_parity'];m['rows'].append(dict(index=index,**spec,command=cmd,started_utc=begin,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));save();return row
try:
 if phase=='calibration':
  for history,width,encoding in itertools.product(['trim','resize'],[8,319,320,321,1024],[0,1,2]):
   for seed in [201,202,203]:
    spec=dict(binary='base',history=history,bytes=width,encoding=encoding,seed=seed);probe=1
    while True:
     r=run(dict(**spec,passes=probe,kind='probe'))
     if r['elapsed_ns']>=20000000:break
     assert probe<10000000,'probe cap without20ms';probe*=10
    for repeat in range(3):run(dict(**spec,passes=probe,kind='trial',repeat=repeat))
 else:
  for spec in json.loads((p/(phase+'-schedule.json')).read_text()):run(spec)
 m['status']='complete'
except Exception as e:m['status']='stopped';m['error']=repr(e);raise
finally:m.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save()
print('COMPLETE',phase,len(m['rows']))
