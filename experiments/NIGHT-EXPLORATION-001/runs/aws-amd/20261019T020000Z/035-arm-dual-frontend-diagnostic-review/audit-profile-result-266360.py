import pathlib,json,re,csv,decimal,collections,hashlib,datetime,sys,subprocess
P=pathlib.Path(sys.argv[1]); O=P/'profile';D=decimal.Decimal;decimal.getcontext().prec=40;read=lambda n:json.loads((O/n).read_text());digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
revision='266360cfbea81808a05c0570453dd4d68b182e7e';prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/';assert (P/'profile-evidence-seal.json').read_bytes()==subprocess.check_output(['git','show',revision+':'+prefix+'profile-evidence-seal.json'])
s=read('result.json');a=read('audit.json');contracts=json.loads((P/'profile-commands.json').read_text());freeze=json.loads((P/'profile-execution-freeze.json').read_text());publication=read('PUBLICATION.json');assert len(contracts)==642 and s['status']=='complete' and len(s['commands'])==642
assert s['execution_freeze_sha256']==digest(P/'profile-execution-freeze.json')=='c27d072f437b96bfb08a34160b0e6d8164a65a9752a00238445d6bdc0654ceae'
for n,h in freeze['files'].items():assert digest(P/n)==h,n
ids=json.loads((P/'identities.json').read_text());assert s['identities_before']['binaries']=={k:v['sha256'] for k,v in ids['binaries'].items()};post=json.loads((P/'profile-postcheck.json').read_text());assert post['identities']==s['identities_after'] and post['owned_units']==post['owned_cgroup_pids']==[];assert s['raw_data_sha256']==a['raw_data_sha256'];assert all(publication[n]['raw_sha256']==h for n,h in s['raw_data_sha256'].items());assert json.loads((P/'profile-evidence-seal.json').read_text())['raw_data']==publication
public_count=0;private_data=[]
for n,h in publication.items():
 if n.endswith('.data'):private_data.append(n);continue
 assert digest(O/n)==h['public_sha256'],n;public_count+=1
assert s['identities_before']==s['identities_after'] and s['sources_before']==s['sources_after'] and s['binaries_before']==s['binaries_after']
prev=datetime.datetime.fromisoformat(s['started_utc']);dt=datetime.datetime.fromisoformat
for c,r in zip(contracts,s['commands']):
 assert all(r[k]==v for k,v in c.items());assert r['returncode']==0 and r['checked'];beg,end=dt(r['started_utc']),dt(r['finished_utc']);assert prev<=beg<end<=dt(s['finished_utc']) and (end-beg).total_seconds()<=120;prev=end
assert 0<s['elapsed_seconds']<=1200 and dt(s['finished_utc'])<dt(s['lease_scope']['deadline'])
def sample_file(label):
 result=[]
 for b in re.split(r'\n\s*\n',(O/(label+'-samples.stdout')).read_text().strip()):
  lines=b.splitlines();period=int(lines[0]);assert period>0;frames=[]
  for l in lines[1:]:
   m=re.fullmatch(r'\s*([0-9a-f]+)\s+(.+)',l);assert m;frames.append((int(m[1],16),m[2]))
  assert frames;ip=frames[0][0];physical=next((name for addr,name in reversed(frames) if addr==ip and '(inlined)' not in name),'[unknown]');mm=re.fullmatch(r'(.*?)\+0x([0-9a-f]+)',physical);symbol=mm[1] if mm else physical;offset=int(mm[2],16) if mm else None
  result.append(dict(period=period,ip=ip,symbol=symbol,offset=offset,physical=physical))
 report=(O/(label+'-report.stdout')).read_text();lost=int(re.search(r'Total Lost Samples:\s*(\d+)',report)[1]);total=int(re.search(r'Event count \(approx\.\):\s*(\d+)',report)[1]);assert total==sum(r['period'] for r in result);count=re.search(r'# Samples:\s*(\S+)',report)[1];assert not count.isdigit() or int(count)==len(result)
 return result,dict(events=len(result),period=total,lost=lost)
known,k=sample_file('known');fault,f=sample_file('known-missing-disable');ke=[x for x in known if x['symbol']=='known_work'];ko=[x for x in known if x['symbol']=='outside_work'];fe=[x for x in fault if x['symbol']=='outside_work'];kp=100*D(sum(x['period'] for x in ke))/D(k['period']);assert len(ke)>=20 and kp>80 and len(ko)==0 and k['lost']==0 and len(fe)>0 and f['lost']==0
EVENTS={'cycles:u','instructions:u','branches:u','branch-misses:u'};stats={}
for c in contracts:
 if c['kind'] not in ['tree-stat','disabled-stat','known-stat']:continue
 entries=list(csv.reader(l for l in (O/c['stat_file']).read_text().splitlines() if l and not l.startswith('#')));assert len(entries)==4;rows={z[2]:z for z in entries};assert len(rows)==4 and set(rows)==EVENTS;enabled=c['kind']=='tree-stat' or c['name']=='known-enabled-stat';vals={}
 for key,z in rows.items():
  if enabled:
   assert re.fullmatch(r'\d+',z[0]);value=int(z[0]);assert value>=0 and (key=='branch-misses:u' or value>0);assert D(z[3]).is_finite() and D(z[3])>0 and D(z[4])==100;vals[key]=value
  else:assert z[0] in ['0','<not counted>']
 if c['kind']=='tree-stat':
  row=list(csv.DictReader((O/(c['name']+'.stdout')).read_text().splitlines()));assert len(row)==1;operations=int(row[0]['operations']);assert operations==c['fixture']['requested_ops'];stats[(c['fixture']['id'],c['fixture']['seed'],c['variant'])]=(operations,vals)
pairs=[]
for cell in json.loads((P/'cells.json').read_text()):
 for seed in [1701,1702,1703]:
  x,y=stats[cell['id'],seed,'control'],stats[cell['id'],seed,'A'];effects={e:((D(y[1][e])/y[0])/(D(x[1][e])/x[0])-1)*100 if x[1][e] else None for e in EVENTS};claim=next(t for t in a['matched_counter_pairs'] if t['cell']==cell['id'] and t['seed']==seed)
  for e,v in effects.items():assert v is None and claim['change_pct'][e] is None or abs(v-D(claim['change_pct'][e]))<D('1e-30')
  pairs.append(dict(cell=cell['id'],seed=seed,effects={e:str(v) for e,v in effects.items()}))
science=[];treebad=collections.Counter();unknown=collections.Counter();raw_total=0;period_total=0;pc_reasons=collections.Counter()
for c in contracts:
 if 'capture_file' not in c:continue
 label=c['capture_file'][:-5];raw,rep=sample_file(label);pub=next(x for x in a['profiles'] if x['label']==label);assert len(raw)==len(pub['samples']) and rep=={k:pub['report'][{'events':'raw_events','period':'raw_period','lost':'lost'}[k]] for k in rep};raw_total+=rep['events'];period_total+=rep['period'];assert rep['lost']==0
 for r,z in zip(raw,pub['samples']):
  assert r['period']==z['period'] and r['ip']==int(z['physical_ip'],16) and r['symbol']==z['symbol'] and r['offset']==z['offset'];unknown[z['exclusive_category']]+=1
  if r['symbol'].startswith('zbt') and 'actual' in z:
   if z['actual']['status'] not in ['same_offset_exact','unique_exact_seven_word_window']:treebad[r['symbol']]+=1
 science.append(dict(label=label,**rep,tree_mapping_pass=pub['all_sampled_tree_bytes_match_actual']))
assert raw_total==a['total_scientific_events'] and period_total==a['total_scientific_period']
# Independently recompute all72 instrumentation ABBA effects and pair-specific transfer gates.
instrument=[]
for v in ['control','A']:
 for cell in json.loads((P/'cells.json').read_text()):
  good={};effects={}
  for phase in ['instrument-AA','instrument-perturbation']:
   bs=[]
   for block in range(3):
    cmds=[c for c in contracts if c.get('instrument_phase')==phase and c['variant']==v and c['fixture']['id']==cell['id'] and c['instrument_contract']['block']==block];assert len(cmds)==4 and [x['instrument_contract']['position'] for x in cmds]==[0,1,2,3];rs=[next(csv.DictReader((O/(c['name']+'.stdout')).read_text().splitlines())) for c in cmds];times=[D(r['elapsed_ns'])/D(r['operations']) for r in rs];effect=((times[1]+times[2])/(times[0]+times[3])-1)*100;minimum=min(int(r['elapsed_ns']) for r in rs);bs.append(dict(effect_pct=str(effect),minimum_ns=minimum))
   good[phase]=all(abs(D(x['effect_pct']))<=1 and x['minimum_ns']>=10000000 for x in bs);effects[phase]=bs
  qualified=all(good.values());claimed=next(x for x in a['instrumentation_qualification'] if x['source']==v and x['cell']==cell['id']);assert claimed['elapsed_transfer_qualified']==qualified;instrument.append(dict(source=v,cell=cell['id'],qualified=qualified,phases=good,blocks=effects))
print(json.dumps(dict(revision=revision,scope='Independent local raw reconstruction; no producer imports, no measurements',commands=642,public_file_hashes=public_count,private_perf_hash_receipts=len(private_data),known=dict(**k,known_events=len(ke),outside_events=len(ko),known_period_pct=str(kp)),missing_disable=dict(**f,outside_events=len(fe)),scientific_events=raw_total,scientific_period=period_total,zero_scientific_losses=True,category_event_totals=dict(unknown),reported_unmatched_tree_events=dict(treebad),pairs=pairs,instrumentation=instrument,qualified_instrumentation_cells=sum(x['qualified'] for x in instrument),paired_control_A_elapsed_transfer_cells=sum(all(next(x['qualified'] for x in instrument if x['source']==v and x['cell']==cell['id']) for v in ['control','A']) for cell in json.loads((P/'cells.json').read_text())),all_instruction_pairs_decreased=all(D(x['effects']['instructions:u'])<0 for x in pairs),producer_scope_valid=a['scope_valid'],producer_code_attribution_valid=a['code_attribution_valid']),indent=2))
