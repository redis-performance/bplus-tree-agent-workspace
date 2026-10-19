from pathlib import Path
import json
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis');ids=json.loads((p/'identities.json').read_text());cells={c['id']:c for c in json.loads((p/'cells.json').read_text())};schedules=json.loads((p/'schedules.json').read_text());C=[]
def add(name,cmd,v='control',kind='plain',fixture=None,env='plain',cwd=None,extra=None):
 en={k:None for k in ['PROFILE_DISABLE','BPLUS_PERF_CTL','BPLUS_PERF_ACK']}
 if env in ['disabled','disabledperf']:en['PROFILE_DISABLE']='1'
 if env in ['enabled','disabledperf']:en.update(BPLUS_PERF_CTL='<job>/control.fifo',BPLUS_PERF_ACK='<job>/ack.fifo')
 C.append(dict(name=name,command=cmd,cwd=cwd or '<job>/'+v,profile_env=en,kind=kind,variant=v,fixture=fixture,**(extra or {})))
def args(c,seed):
 x=['--size',str(c['size']),'--ops',str(c['requested_ops']),'--member-bytes','16','--seed',str(seed),'--warmup-passes',str(c['warmup_passes'])]
 return x+(['--case','iterate'] if c['frontend']=='primary' else ['--direction',c['direction'],'--mask','4','--encoding','integer'])
def fix(c,seed):return dict(c,seed=seed)
add('source-archive',['git','archive','--format=tar','--output','<job>/source.tar',ids['source_commit'],'src','compat','vendor/redis','tests','bench','Makefile'],kind='archive',cwd='<checkout>');add('compiler-version',['clang','--version'],kind='compiler')
flags=['-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
for v in ['control','A']:
 for front in ['primary','h4']:
  for mode in ['original','profile','census']:
   src=('microbench.c' if front=='primary' else 'iterator_modes.c') if mode=='original' else front+('-scoped.c' if mode=='profile' else '-census.c')
   for san in [False,True]:
    name=front+'-'+mode+('-san' if san else '');opt=['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if san else ['-O3'];target='bench/census.c' if mode=='census' else 'src/zset_btree.c'
    add(v+'-'+name+'-build',['clang',*flags,*opt,'bench/'+src,target,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+name],v,'build')
 for san in [False,True]:
  name='original-check'+('-san' if san else '');fl='-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer '+('-O1 -fsanitize=address,undefined -fno-sanitize-recover=all' if san else '-O3');add(v+'-'+name,['make','CC=clang','BUILD=build/'+name,'CFLAGS='+fl,'check'],v,'original43')
add('known-control-build',['clang',*flags,'-O3','bench/known-control.c','-o','build/known-control'],kind='build')
add('known-missing-disable-build',['clang',*flags,'-O3','bench/known-missing-disable.c','-o','build/known-missing-disable'],kind='build')
# Full exact semantic parity before instrumentation qualification/captures.
for seed in [1701,1702,1703]:
 for c in cells.values():
  for v in ['control','A']:
   for mode,env in [('original','plain'),('profile','disabled')]:add(f'{v}-{c["id"]}-s{seed}-{mode}-parity',['build/'+c['frontend']+'-'+mode,*args(c,seed)],v,'tree',fix(c,seed),env)
for c0 in list(cells.values())[::2]:
 c=dict(c0,size=129,requested_ops=259,id=c0['id'].rsplit('-',1)[0]+'-129')
 for v in ['control','A']:
  for san in [False,True]:
   for mode,env in [('original','plain'),('profile','disabled')]:add(f'{v}-{c["id"]}-{mode}'+('-san' if san else '-native'),['build/'+c['frontend']+'-'+mode+('-san' if san else ''),*args(c,1801)],v,'tree',fix(c,1801),env)
# Separate observational copies preserve full original loops; all elapsed output ignored.
for seed in [1601,1602,1603,1701,1702,1703]:
 for c in cells.values():
  if c['direction']=='reverse':continue
  for v in ['control','A']:add(f'{v}-{c["id"]}-s{seed}-census',['build/'+c['frontend']+'-census',*args(c,seed)],v,'census',fix(c,seed))
for front in ['primary','h4']:
 c=dict(next(c for c in cells.values() if c['frontend']==front),size=129,requested_ops=259,id=front+'-forward-129')
 for v in ['control','A']:
  for san in [False,True]:add(f'{v}-{front}-census-small'+('-san' if san else '-native'),['build/'+front+'-census'+('-san' if san else ''),*args(c,1801)],v,'census',fix(c,1801))
ctl=['-D','-1','--control=fifo:<job>/control.fifo,<job>/ack.fifo'];events='cycles:u,instructions:u,branches:u,branch-misses:u'
def stat(label,binary,argv):return ['<perf>','stat',*ctl,'-x,','-e',events,'-o','<job>/profile/'+label+'.stat','--',binary,*argv]
def record(label,binary,argv):return ['<perf>','record','-q',*ctl,'-e','cycles:u','-F997','-g','--call-graph','fp','-o','<job>/profile/'+label+'.data','--',binary,*argv]
for v in ['control','A']:
 for front in ['primary','h4']:
  c=next(c for c in cells.values() if c['frontend']==front);label=v+'-'+front+'-disabled';add(label+'-zero',stat(label,'build/'+front+'-profile',args(c,1701)),v,'disabled-stat',fix(c,1701),'disabledperf',extra={'stat_file':label+'.stat'})
add('known-plain',['build/known-control'],kind='known',env='disabled')
for mode,env in [('disabled','disabledperf'),('enabled','enabled')]:add('known-'+mode+'-stat',stat('known-'+mode,'build/known-control',[]),kind='known-stat',env=env,extra={'stat_file':'known-'+mode+'.stat'})
add('known-record',record('known','build/known-control',[]),kind='known',env='enabled');add('known-report',['<perf>','report','--stdio','--no-children','--sort','symbol','-i','<job>/profile/known.data']);add('known-samples',['<perf>','script','-i','<job>/profile/known.data','-F','ip,sym,symoff,period'],kind='known-gate');add('known-full-asm',['objdump','-dSl','build/known-control'])
add('known-missing-disable-record',record('known-missing-disable','build/known-missing-disable',[]),kind='known',env='enabled')
add('known-missing-disable-report',['<perf>','report','--stdio','--no-children','--sort','symbol','-i','<job>/profile/known-missing-disable.data'])
add('known-missing-disable-samples',['<perf>','script','-i','<job>/profile/known-missing-disable.data','-F','ip,sym,symoff,period'],kind='fault-scope')
for v in ['control','A']:
 for front in ['primary','h4']:
  for mode,binary in [('original','build/'+front+'-original'),('profile','build/'+front+'-profile'),('actual','<checkout>/'+ids['binaries'][front+'-'+v]['path'])]:add(f'{front}-{v}-{mode}-full-asm',['objdump','-dSl',binary],v)
for phase in ['instrument-AA','instrument-perturbation']:
 for row in schedules[phase]:
  c=cells[row['cell']];v=row['source'];binary='<checkout>/'+ids['binaries'][c['frontend']+'-'+v]['path'] if row['binary']=='actual' else 'build/'+c['frontend']+'-profile';add(f'{phase}-{row["index"]:04d}',[binary,*row['args']],v,'instrument',fix(c,row['seed']),'disabled' if row['binary']!='actual' else 'plain',extra={'instrument_contract':row,'instrument_phase':phase})
# Preserve declared capture/stat ordering; no outcome-dependent choices.
for row in schedules['cycle-captures']:
 c=cells[row['cell']];v=row['source'];seed=row['seed'];label=f'{v}-{c["id"]}-s{seed}';add(label+'-record',record(label,'build/'+c['frontend']+'-profile',row['args']),v,'tree',fix(c,seed),'enabled',extra={'capture_file':label+'.data'})
 add(label+'-report',['<perf>','report','--stdio','--no-children','--sort','symbol','-i','<job>/profile/'+label+'.data'],v)
 add(label+'-samples',['<perf>','script','-i','<job>/profile/'+label+'.data','-F','ip,sym,symoff,period'],v)
for row in schedules['scoped-stats']:
 c=cells[row['cell']];v=row['source'];seed=row['seed'];label=f'{v}-{c["id"]}-s{seed}';add(label+'-stat',stat(label,'build/'+c['frontend']+'-profile',row['args']),v,'tree-stat',fix(c,seed),'enabled',extra={'stat_file':label+'.stat'})
assert len(C)==642,len(C);(p/'profile-commands.json').write_text(json.dumps(C,indent=2)+'\n');print('Fixed profile commands',len(C))
