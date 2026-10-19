import pathlib,json,hashlib,subprocess,sys,tempfile,itertools,collections,ast
p=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text());f=j(p/'execution-freeze.json');e=j(p/'expected.json')
assert sha(p/'execution-freeze.json')=='328c21556bc285df97fedca7a212148be107c0c827793bb16a05b0505ce806b2'
for n,h in f['files'].items():assert sha(p/n)==h
assert len(f['files'])==20
for n,h in e['source_hashes'].items():assert hashlib.sha256(subprocess.check_output(['git','show',e['commit']+':'+n])).hexdigest()==h
assert (p/'candidate.patch').read_bytes()==pathlib.Path('experiments/EXP-005/variants/A/candidate.patch').read_bytes()
source=subprocess.check_output(['git','show',e['commit']+':src/zset_btree.c'])
with tempfile.TemporaryDirectory() as d:
 t=pathlib.Path(d);(t/'src').mkdir();(t/'src/zset_btree.c').write_bytes(source)
 subprocess.run(['patch','--batch','--fuzz=0','-s','-p1'],cwd=t,input=(p/'candidate.patch').read_bytes(),check=True)
 assert sha(t/'src/zset_btree.c')==e['candidate_source_sha256']=='aa834a771284bed367400a8f54538cd366b2791666d9711a8e160aaa93f62fc4'
for n,h in e['oracles'].items():
 old=pathlib.Path('experiments/OVERNIGHT-2026-10-17/HARNESS-004/iterator_modes.c') if n=='iterator_modes.c' else pathlib.Path('tests')/n
 assert sha(old)==sha(p/'oracles'/n)==h
for name,v in e['faults'].items():
 boundary='BOUNDARY-013' if name in ['missing-ninth-byte','width64-mask'] else 'BOUNDARY-014'
 assert sha(pathlib.Path('experiments/OVERNIGHT-2026-10-17')/boundary/(name+'.patch'))==sha(p/'faults'/(name+'.patch'))==v['patch']
for q in p.glob('*.py'):ast.parse(q.read_text())
commands=j(p/'validation-commands.json');counts=collections.Counter(c['kind'] for c in commands);assert len(commands)==570 and counts=={'archive':1,'plain':33,'original43':4,'modes':512,'oracle':12,'negative':8};assert len({c['name'] for c in commands})==570
for variant,mode in itertools.product(['control','A'],['native','san']):
 rows=[c for c in commands if c['kind']=='modes' and c['cwd']=='<job>/'+variant and c['command'][0]=='build/'+mode+'/modes'];assert len(rows)==128
 got=set()
 for c in rows:
  argv=c['command'];args=dict(zip(argv[1::2],argv[2::2]));assert args['--size']=='129' and args['--ops']=='259' and args['--seed']=='7103';v=(int(args['--member-bytes']),args['--encoding'],args['--direction'],int(args['--mask']));got.add(v);assert c['fixture']==dict(member_bytes=v[0],encoding=v[1],direction=v[2],mask=v[3])
 assert got==set(itertools.product([16,320],['integer','fraction','wide','zero'],['forward','reverse'],range(8)))
 for kind in ['mutation','packed','zero']:assert len([c for c in commands if c['name']==variant+'-'+mode+'-'+kind and c['kind']=='oracle'])==1
for name,v in e['faults'].items():
 for mode in ['native','san']:
  c=next(c for c in commands if c['name']==name+'-'+mode);assert c['kind']=='negative' and c['needles']==v['needles'] and c['match']==v['match']
base=next(c for c in commands if c['name']=='control-timing-build');a=next(c for c in commands if c['name']=='A-timing-build');assert base['command']==a['command'];assert not any('REDIS_DEBUG' in v or 'NDEBUG' in v or 'REDIS_TEST' in v for v in a['command'])
schedule=j(p/'screen-schedule.json');want=[]
for b in range(6):
 for n in ([100000,1000000] if b%2==0 else [1000000,100000]):
  for pos,label in enumerate('ABBA'):want.append((b,n,401+b%3,pos,label,'baseline' if label=='A' else 'candidate'))
assert len(schedule)==48
for s,v in zip(schedule,want):assert tuple(s[k] for k in ['block','size','seed','position','label','binary'])==v
for width in range(1,65):assert ((1<<64)-1)>>(64-width)==sum(1<<i for i in range(width))
result=dict(status='no static execution blocker found',reviewed_revision='a9b09cadc',freeze_sha256=sha(p/'execution-freeze.json'),inputs=20,source_hashes=10,exact_historical_patch_sha256=sha(p/'candidate.patch'),candidate_source_sha256=e['candidate_source_sha256'],retained_oracles=4,retained_faults=4,validation_commands=dict(counts),correctness_mode_cells=512,conditional_comparison_rows=48,valid_mask_widths_proved=64,source_selection='NONE',limits=['Static preparation review only; all validation outcomes and codegen gate remain unexecuted','Four generation instructions include constant materialization; common AND excluded symmetrically','Existing NONE proposal dissent remains unchanged','No runner access, build or measurements'])
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
