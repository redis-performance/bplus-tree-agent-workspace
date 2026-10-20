"""Reconstruct profile-only evidence without modifying frozen input/results.

Usage: python3 independent-audit.py RESULTS [RAW_PERF_DIRECTORY]
Prints a JSON review. PERF may select the exact runner-compatible decoder.
Optional raw data are read with perf script -D to inspect
recorded losses; missing raw data/loss information remain explicitly unknown.
"""
import collections,csv,hashlib,json,math,os,re,shutil,subprocess,sys
from pathlib import Path
H=Path(__file__).resolve().parent; D=Path(sys.argv[1]); RAW=Path(sys.argv[2]) if len(sys.argv)>2 else D.parent/'raw'
V2=(D/'resume-provenance.json').exists()
P=json.loads((H/('protocol-v2.json' if V2 else 'protocol.json')).read_text()); manifest=json.loads((H/'input-manifest.json').read_text())
ROOTS={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def load(path): return json.loads(path.read_text())
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def finite(v):
 try:return math.isfinite(float(v))
 except (ValueError,TypeError):return False
def scope(path):
 if not path.exists():return {'available':False,'pass':False}
 s=load(path);a=s['before'];b=s['after']
 def busy(cpu):
  ds=[y-x for x,y in zip(a['cpu'][str(cpu)],b['cpu'][str(cpu)])];return sum(ds),sum(ds)-ds[3]-ds[4]
 def ticks(text):
  f=text.rsplit(')',1)[1].split();return int(f[11])+int(f[12])
 total,work=busy(2);stotal,sbusy=busy(50);delta=ticks(b['proc'])-ticks(a['proc'])
 sibling=100*sbusy/stotal if stotal else None;error=100*abs(work-delta)/max(work,1)
 ok=a['affinity']==b['affinity']==[2] and sibling is not None and sibling<=1 and error<=1
 assert abs(error-s['accounting_error_percent'])<1e-8
 assert sibling is None or abs(sibling-s['sibling_busy_percent'])<1e-8
 assert ok==s['pass']
 return {'available':True,'pass':ok,'sibling_busy_percent':sibling,'accounting_error_percent':error,'start':a['time'],'end':b['time'],'frequency_khz_before':a['frequency_khz'],'frequency_khz_after':b['frequency_khz'],'schedstat_before':a['schedstat'],'schedstat_after':b['schedstat']}
def tma(tag,level,rep):
 path=D/(tag+'.stderr');info={'tag':tag,'level':level,'rep':rep,'available':path.exists()}
 if not path.exists():return dict(info,qualified=False,reason='raw capture missing')
 lines=path.read_text().splitlines();heads=[i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,')]
 info.update(raw_sha256=digest(path),header_count=len(heads),scope=scope(D/(tag+'.scope.json')))
 if len(heads)!=1:return dict(info,qualified=False,reason='CSV header missing or duplicated',preamble=lines)
 parsed=list(csv.DictReader(lines[heads[0]:]));rows=[r for r in parsed if r.get('Area')]
 bytime=collections.defaultdict(list);metrics=collections.defaultdict(list)
 valid_numeric=True
 for r in rows:
  if r['Area'] in ROOTS:bytime[r['Timestamp']].append(r)
  if finite(r['Value']):metrics[(r['Area'],r['Unit'])].append(float(r['Value']))
  else:valid_numeric=False
 partition=len(bytime)==5 and all(len(rs)==4 and {r['Area'] for r in rs}==ROOTS and all(r['Unit'] in ('% Slots','% Slots <') and finite(r['Value']) and 0<=float(r['Value'])<=100 for r in rs) and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in bytime.values())
 mux=[float(r['Multiplex']) for r in rows if finite(r.get('Multiplex'))]
 muxok=bool(rows) and len(mux)==len(rows) and all(v==100 for v in mux)
 info.update(preamble=lines[:heads[0]],nondata_tail_rows=[r for r in parsed if not r.get('Area')],metric_rows=len(rows),intervals=len(bytime),root_partition_pass=partition,all_numeric=valid_numeric,all_mux_100=muxok,multiplex_min=min(mux) if mux else None,qualified=level==2 and partition and muxok and info['scope']['pass'],metrics=[{'metric':k[0],'unit':k[1],'count':len(v),'mean':sum(v)/len(v),'min':min(v),'max':max(v)} for k,v in sorted(metrics.items())])
 return info
def counter(tag):
 cmd=D/(tag+'.command.json');path=D/(tag+'.stderr')
 if not cmd.exists() or not path.exists():return {'available':False,'reason':'counter command/raw missing'}
 command=load(cmd);assert command['args'][command['args'].index('-C')+1]=='2'
 events={};other=[]
 for r in csv.reader(path.read_text().splitlines()):
  if len(r)>=5 and r[2].strip() in P['counter']['events']:
   name=r[2].strip();assert name not in events,(tag,'duplicate event')
   events[name]={'value':float(r[0]) if finite(r[0]) else None,'raw_value':r[0],'runtime':r[3],'scheduling_percent':float(r[4].strip().rstrip('%')) if finite(r[4].strip().rstrip('%')) else None}
  elif r:other.append(r)
 s=scope(D/(tag+'.scope.json'));supported=set(events)==set(P['counter']['events']) and all(v['value'] is not None and v['value']>=0 for v in events.values())
 scheduled=supported and all(v['scheduling_percent']==100 for v in events.values())
 return {'available':command['returncode']==0 and supported and scheduled and s['pass'],'returncode':command['returncode'],'events':events,'other_rows':other,'scope':s,'all_event_scheduling_100':scheduled,'raw_sha256':digest(path)}
def sample(tag,record):
 cmd=D/(tag+'-samples.command.json');stderr=D/(tag+'-samples.stderr');eventfile=D/(tag+'-sample-events.stdout')
 info={'command_available':cmd.exists(),'scope':scope(D/(tag+'-samples.scope.json')),'raw_perf_available':False,'recorded_losses':'unknown'}
 if cmd.exists():
  command=load(cmd);info['returncode']=command['returncode']
  if (D/(tag+'-samples.scope.json')).exists():
   sampled=load(D/(tag+'-samples.scope.json'))['before']['proc'].split()[0]
   assert command['args'][command['args'].index('-p')+1]==sampled
 if stderr.exists():info['record_stderr']=stderr.read_text();info['record_stderr_sha256']=digest(stderr)
 if eventfile.exists():
  lines=eventfile.read_text().splitlines();info['exported_event_lines']=sum(bool(x.strip()) for x in lines);info['exported_cycles_samples']=sum(l.lstrip().startswith('cycles:u:') for l in lines);info['exported_event_sha256']=digest(eventfile)
 reportpath=D/(tag+'-symbols.stdout')
 if reportpath.exists():
  report=reportpath.read_text();lost=re.search(r'Total Lost Samples:\s*(\d+)',report);count=re.search(r'# Samples:\s*(\d+)\s+of event',report)
  info['runner_report_lost_samples']=int(lost.group(1)) if lost else None
  info['runner_report_sample_count']=int(count.group(1)) if count else None
  if count and 'exported_cycles_samples' in info:info['sample_export_count_agrees']=int(count.group(1))==info['exported_cycles_samples']
 for suffix in ['symbols','sample-events']:
  path=D/(tag+'-'+suffix+'.command.json')
  if path.exists():info[suffix+'_returncode']=load(path)['returncode']
 raw=RAW/(tag+'.perf.data')
 if raw.exists():
  info.update(raw_perf_available=True,raw_sha256=digest(raw),raw_bytes=raw.stat().st_size)
  assert info['raw_sha256']==record['raw_perf_sha256'] and info['raw_bytes']==record['raw_perf_bytes']
  perf=os.environ.get('PERF') or shutil.which('perf')
  if perf:
   info['decoder_name']=Path(perf).name
   if Path(perf).is_file():info['decoder_sha256']=digest(Path(perf))
   try:
    r=subprocess.run([perf,'script','-D','-i',str(raw)],capture_output=True,text=True,timeout=30)
    lost=[l for l in r.stdout.splitlines() if 'PERF_RECORD_LOST' in l]
    info.update(raw_decode_returncode=r.returncode,raw_decode_stderr=r.stderr,recorded_loss_records=lost)
    if r.returncode==0:info['recorded_losses']='none recorded' if not lost else 'loss records present; see raw_decode_loss_records'
   except subprocess.TimeoutExpired:info['raw_decode_error']='timeout; recorded losses unknown'
 info['available']=info.get('returncode')==0 and info.get('symbols_returncode')==0 and info.get('sample-events_returncode')==0 and info['scope']['pass']
 return info
expected=[]
for i,c in enumerate(P['cells']):
 for v in c['variants'] if i%2==0 else list(reversed(c['variants'])):expected.append({'index':len(expected),'cell':c,'variant':v})
schedule=load(D/'schedule.json');assert schedule==expected and len(expected)==36
builds=load(D/'build-sha256.json');checked_hashes=0
for name,value in builds.items():
 if name in manifest:assert value==manifest[name],name;checked_hashes+=1
assert checked_hashes>0
preparation_copy_count=0
if V2:
 provenance=load(D/'resume-provenance.json');assert provenance['launcher_probe']['returncode']==0 and provenance['controller_affinity']==[0] and provenance['launcher_probe']['stdout'].strip()=='[2]'
 archived=H/'attempt1/results'
 names={'validation-commands.json','completed-checks.json','build-sha256.json','environment.json'}
 for record in load(D/'validation-commands.json'):
  for suffix in ['.stdout','.stderr']:names.add(record['tag']+suffix)
 for name in names:
  assert (D/name).read_bytes()==(archived/name).read_bytes(),name;preparation_copy_count+=1
validation=load(D/'validation-commands.json');assert all(r['returncode']==0 for r in validation)
assert all(a['end']<=b['start'] for a,b in zip(validation,validation[1:]))
checks=load(D/'completed-checks.json');assert len(checks)==36 and all(x['parity'] for x in checks)
# Recompute original/profile/native/sanitizer comparisons from raw outputs.
raw_semantics=[]
def semantic(path,driver):
 raw=path.read_text();row=json.loads(raw) if driver=='guard' else list(csv.DictReader(raw.splitlines()))[0]
 return {k:str(v) for k,v in row.items() if not any(x in k for x in ['elapsed','ns_per','ops_per','cpu','qos','relpri'])}
for c in P['cells']:
 per_mode=collections.defaultdict(list)
 for v in c['variants']:
  tag='check-'+c['id']+'-'+v
  original=semantic(D/(tag+'-original.stdout'),c['driver']);native=semantic(D/(tag+'-profile.stdout'),c['driver']);san=semantic(D/(tag+'-sanitize.stdout'),c['driver'])
  assert original==native
  assert {k:v for k,v in native.items() if k!='tree_bytes'}=={k:v for k,v in san.items() if k!='tree_bytes'}
  saved=next(x for x in checks if x['cell']==c['id'] and x['variant']==v);assert saved['native']==native and saved['sanitize']==san
  per_mode['native'].append(native);per_mode['sanitize'].append(san);raw_semantics.append({'cell':c['id'],'variant':v,'pass':True})
 assert all(all(x==ms[0] for x in ms) for ms in per_mode.values())
for v in ['base','itA','itB','scanB']:
 for mode in ['native','sanitize']:
  text=(D/f'{v}-tests-{mode}.stdout').read_text();assert '43 passed' in text and '0 failed, 43 total' in text
  if v in ['base','itA','itB']:
   for oracle,num in [('cache-oracle',28192),('cache-oracle-additive',89428)]:
    text=(D/f'{v}-{oracle}-{mode}.stdout').read_text().strip();assert text==f'PASS {num} iterator state checks sizeof={24 if v=="itA" else 16}'
configs=[]
for item in expected:
 c=item['cell'];v=item['variant'];tag=c['id']+'-'+v;path=D/(tag+'.record.json')
 if not path.exists():configs.append({'cell':c['id'],'variant':v,'status':'UNATTEMPTED','all_l2_qualified':False});continue
 r=load(path);assert r['cell']==c['id'] and r['variant']==v and r['index']==item['index']
 assert r['binary_sha256']==builds['build/'+v+'/'+c['driver']]
 assert r['workload_command']==['numactl']+(['--all'] if V2 else [])+['--physcpubind=2','--membind=0','build/'+v+'/'+c['driver']]+c['args']
 captures=[tma(tag+f'-L2-{rep}',2,rep) for rep in range(1,4)]+[tma(tag+'-L3-1',3,1)]
 for cap in captures:
  saved=next((x for x in r['captures'] if x['tag']==cap['tag']),None)
  if saved:
   assert cap['raw_sha256']==saved['raw_sha256']
   assert saved['command'][saved['command'].index('-C')+1]=='2' and '-l'+str(cap['level']) in saved['command']
   assert cap['qualified']==saved['l2_qualified'],cap['tag']
 configs.append({'cell':c['id'],'variant':v,'status':r['status'],'error':r.get('error'),'binary_sha256':r['binary_sha256'],'all_l2_qualified':all(x['qualified'] for x in captures[:3]),'captures':captures,'counters':counter(tag+'-counters'),'samples':sample(tag,r),'raw_record_sha256':digest(path)})
windows=[]
for x in configs:
 for cap in x.get('captures',[]):
  sc=cap.get('scope',{})
  if sc.get('available'):windows.append((sc['start'],sc['end']))
 for stage in ['counters','samples']:
  sc=x.get(stage,{}).get('scope',{})
  if sc.get('available'):windows.append((sc['start'],sc['end']))
window_serial=all(a[1]<=b[0] for a,b in zip(windows,windows[1:]))
comparisons=[]
for c in P['cells']:
 cs=[x for x in configs if x['cell']==c['id']]
 base=next(x for x in cs if x['variant']=='base')
 comparisons.append({'cell':c['id'],'variants':[x['variant'] for x in cs],'matched_l2_available':all(x['all_l2_qualified'] for x in cs),'pairs':[{'baseline':'base','candidate':x['variant'],'matched_l2_available':base['all_l2_qualified'] and x['all_l2_qualified']} for x in cs if x['variant']!='base'],'stateful_update_windows':c['family']=='update','timing_qualified':False})
result={'reviewer':'/root/intel_b_review','scope':'independent raw reconstruction, no runner commands or measurements','launcher_correction_v2':V2,'unchanged_preparation_files_verified':preparation_copy_count,'expected_configurations':36,'records':sum(x['status']!='UNATTEMPTED' for x in configs),'all_l2_qualified_configurations':sum(x['all_l2_qualified'] for x in configs),'qualified_l2_windows':sum(cap['qualified'] for x in configs for cap in x.get('captures',[]) if cap['level']==2),'raw_semantic_configurations':len(raw_semantics),'source_driver_hashes_checked':checked_hashes,'validation_commands':len(validation),'profile_windows_serial_by_recorded_wall_clock':window_serial,'comparisons':comparisons,'configurations':configs,'automated_result':load(D/'RESULT.json') if (D/'RESULT.json').exists() else None,'source_adoption':'NONE','timing_acceptance':False,'limits':['File hashes cross-check recorded build provenance; live binaries were not independently downloaded by reviewer.','Missing raw perf data leaves loss verification unknown.','Update windows evolve in state; counts are not per-operation costs.','Each candidate/baseline comparison requires all its captures valid; unavailable captures excluded from interpretation, not silently dropped.']}
local_binaries=[]
for relative,expected_hash in builds.items():
 path=RAW.parent/relative
 if path.is_file():
  actual=digest(path);assert actual==expected_hash,(relative,actual,expected_hash)
  local_binaries.append({'path':relative,'sha256':actual})
result['copied_binaries_verified']=local_binaries
result['all_profiled_binaries_copied_and_verified']=all(x['binary_sha256'] in {b['sha256'] for b in local_binaries} for x in configs)
result['limits'][0]='Recorded provenance cross-checked; downloaded ELF bytes independently hashed where listed. No independent remote reads by reviewer.'
print(json.dumps(result,indent=2))
