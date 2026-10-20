"""Build, complete semantic checks, then execute the frozen profile sweep."""
import csv,hashlib,json,os,subprocess,time
from pathlib import Path
O=Path('results');O.mkdir(exist_ok=True);commands=[]
def run(tag,args,timeout=180):
 begin=time.time()
 try:r=subprocess.run(args,text=True,capture_output=True,timeout=timeout)
 except subprocess.TimeoutExpired as e:
  txt=lambda x:x.decode(errors='replace') if isinstance(x,bytes) else (x or '')
  r=subprocess.CompletedProcess(args,124,txt(e.stdout),txt(e.stderr)+'\nTIMEOUT\n')
 (O/(tag+'.stdout')).write_text(r.stdout);(O/(tag+'.stderr')).write_text(r.stderr)
 commands.append({'tag':tag,'args':args,'start':begin,'end':time.time(),'returncode':r.returncode})
 (O/'validation-commands.json').write_text(json.dumps(commands,indent=2)+'\n')
 assert r.returncode==0,tag
 return r.stdout
p=json.loads(Path('protocol.json').read_text())
env={'cpu':run('lscpu',['lscpu']),'compiler':run('compiler',['clang-18','--version']),
 'kernel':run('kernel',['uname','-r']),'numa':run('numa',['numactl','--hardware']),
 'states':{s:Path(s).read_text().strip() for s in ['/sys/devices/system/cpu/cpu2/topology/thread_siblings_list','/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor','/sys/devices/system/cpu/intel_pstate/no_turbo']}}
(O/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
for v in ['base','itA','itB','scanB']:
 d=Path('variants')/v;b=Path('build')/v;b.mkdir(parents=True,exist_ok=True)
 common=['clang-18',f'-I{d}/src',f'-I{d}/compat',f'-I{d}/vendor/redis','-Idriver','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer']
 sources=[f'{d}/src/zset_btree.c',f'{d}/compat/standalone.c',f'{d}/vendor/redis/siphash.c']
 drivers=['iterator'] if v in ['itA','itB'] else ['scan','guard'] if v=='scanB' else ['iterator','scan','guard','update']
 for mode,flags in [('native',['-O3']),('sanitize',['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])]:
  run(f'build-{v}-tests-{mode}',common+flags+['-DREDIS_TEST','-DREDIS_DEBUG',f'{d}/tests/upstream.c']+sources+['-lm','-o',str(b/f'tests-{mode}')])
  run(f'{v}-tests-{mode}',[str(b/f'tests-{mode}')])
  for driver in drivers:
   name=driver if mode=='native' else driver+'-sanitize'
   run(f'build-{v}-{name}',common+flags+['-DPROFILE_SAMPLE',f'driver/{driver}-profile.c','ready.c']+sources+['-lm','-o',str(b/name)])
  if v in ['base','itA','itB']:
   for oracle in ['cache-oracle','cache-oracle-additive']:
    run(f'build-{v}-{oracle}-{mode}',common+flags+[f'driver/{oracle}.c']+sources+['-lm','-o',str(b/f'{oracle}-{mode}')])
    run(f'{v}-{oracle}-{mode}',[str(b/f'{oracle}-{mode}')])
 # Completed original-vs-diagnostic model parity uses identical source/flags.
 for driver in drivers:
  original='iterator.c' if driver=='iterator' else driver+'-original.c'
  run(f'build-{v}-{driver}-original',common+['-O3',f'driver/{original}']+sources+['-lm','-o',str(b/(driver+'-original'))])

checks=[]
for cell in p['cells']:
 args=list(cell['args'])
 if cell['driver']=='guard':args[5]='10'
 else:args[args.index('--ops')+1]=str(2*int(args[args.index('--size')+1]))
 for v in cell['variants']:
  outputs=[]
  for suffix in ['-original','','-sanitize']:
   tag='check-'+cell['id']+'-'+v+(suffix or '-profile')
   raw=run(tag,[str(Path('build')/v/(cell['driver']+suffix))]+args)
   row=json.loads(raw) if cell['driver']=='guard' else list(csv.DictReader(raw.splitlines()))[0]
   # All semantic fields compared; only temporal and placement diagnostics excluded.
   comparable={k:str(val) for k,val in row.items() if not any(x in k for x in ['elapsed','ns_per','ops_per','cpu','qos','relpri'])}
   outputs.append(comparable)
  assert outputs[0]==outputs[1],(cell['id'],v,'native original/profile')
  logical=lambda x:{k:val for k,val in x.items() if k!='tree_bytes'}
  assert logical(outputs[1])==logical(outputs[2]),(cell['id'],v,'sanitizer logical fields')
  checks.append({'cell':cell['id'],'variant':v,'native':outputs[1],'sanitize':outputs[2],'parity':True})
 for mode in ['native','sanitize']:
  models=[r[mode] for r in checks if r['cell']==cell['id']]
  assert all(m==models[0] for m in models),(cell['id'],mode,'candidate semantic and owned-byte parity')
(O/'completed-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
(O/'build-sha256.json').write_text(json.dumps({str(x):hashlib.sha256(x.read_bytes()).hexdigest() for name in ['build','driver','variants'] for x in sorted(Path(name).rglob('*')) if x.is_file()},indent=2)+'\n')
run('perf-events',['/usr/lib/linux-tools/7.0.0-1014-aws/perf','list','--details','msr/aperf/'])
subprocess.run(['python3','collect.py'],check=True,env=dict(os.environ,PYTHONPATH='glue:pmu'))
