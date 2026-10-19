#!/usr/bin/env python3
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys,time
p=Path(__file__).resolve().parent;o=p/'profiles';o.mkdir();perf=sys.argv[1];f=json.loads((p/'plan-freeze.json').read_text());prior=json.loads((p.parent/'017-corrected-neon/comparison-freeze.json').read_text());start=time.monotonic();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for file,h in f['inputs_sha256'].items():assert sha(p/file)==h
assert sha(p.parent/'017-corrected-neon/comparison-freeze.json')==f['comparison_freeze_sha256']
m={'status':'running','started_utc':now(),'commands':[],'captures':[]};save=lambda:(o/'result.json').write_text(json.dumps(m,indent=2)+'\n')
def identity():
 result={}
 for v in ['base','B']:
  x=prior['sources'][v];root=Path(x['root']);assert sha(root/x['timing_binary'])==x['binary_sha256']
  for file,h in x['source_hashes'].items():assert sha(root/file)==h
  result[v]={'binary_sha256':x['binary_sha256'],'source_referee_hashes_verified':len(x['source_hashes'])}
 return result
m['identity_before']=identity();save()
def run(name,cmd):
 remaining=600-(time.monotonic()-start);assert remaining>0
 a={'name':name,'command':cmd,'started_utc':now()}
 try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(90,remaining));a['returncode']=r.returncode;stdout,stderr=r.stdout,r.stderr
 except subprocess.TimeoutExpired as e:
  dec=lambda x:x.decode(errors='replace')if isinstance(x,bytes)else x or ''
  stdout,stderr=dec(e.stdout),dec(e.stderr);a.update(returncode=None,status='timeout')
  (o/(name+'.stdout')).write_text(stdout);(o/(name+'.stderr')).write_text(stderr);a['finished_utc']=now();m['commands'].append(a);save();raise
 (o/(name+'.stdout')).write_text(stdout);(o/(name+'.stderr')).write_text(stderr);a['finished_utc']=now();m['commands'].append(a);save();assert r.returncode==0,(name,r.returncode);return stdout
try:
 for v in ['base','B']:
  for n in [100000,1000000]:
   x=prior['sources'][v];binary=str(Path(x['root'])/x['timing_binary']);name=f'{v}-n{n}-s1-disabled';args=[binary,'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed','1'];run(name,[perf,'stat','-D','-1','-x,','-e','cycles:u','-o',str(o/(name+'.stat')),'--']+args)
 for item in f['capture_schedule']:
  v,n,seed=item['variant'],item['size'],item['seed'];x=prior['sources'][v];binary=str(Path(x['root'])/x['timing_binary']);name=f'{v}-n{n}-s{seed}';args=[binary,'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)];data=Path('scratch')/('arm-neon-matched-'+name+'.data');assert not data.exists()
  run(name+'-plain',args);run(name+'-sampled',[perf,'record','-q','-e','cycles:u','-F997','-g','--call-graph','fp','-o',str(data),'--']+args)
  run(name+'-samples',[perf,'script','-i',str(data),'-F','ip,sym,symoff,period']);run(name+'-report',[perf,'report','--stdio','--no-children','--sort','symbol','-i',str(data)])
  m['captures'].append(dict(item,raw_perf_sha256=sha(data),raw_perf_bytes=data.stat().st_size,raw_perf_file=str(data)));save()
 m['identity_after']=identity();m['status']='complete'
except BaseException as e:m.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:m.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
