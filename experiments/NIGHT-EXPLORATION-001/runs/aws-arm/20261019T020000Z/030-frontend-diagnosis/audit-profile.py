#!/usr/bin/env python3
"""Raw integrity/scope/attribution reconstruction; hypothesis direction is separate."""
import collections,datetime,decimal,hashlib,json,pathlib,re,sys
from native_common import HERE,IDS,sha,same_semantics
from profile_common import row,counters,census,raw_samples,mapping,scope_validity,allocator_mode
sys.path.insert(0,str(HERE/'inputs'))
from arm_asm import parse
from profile_helpers import known_gate,report,samples
D=decimal.Decimal;decimal.getcontext().prec=40;dt=datetime.datetime.fromisoformat
out=HERE/'profile';s=json.loads((out/'result.json').read_text());contracts=json.loads((HERE/'profile-commands.json').read_text());freeze=json.loads((HERE/'profile-execution-freeze.json').read_text())
assert s['status']=='complete' and len(s['commands'])==len(contracts)==642 and s['cpu']==2
assert s['execution_freeze_sha256']==sha(HERE/'profile-execution-freeze.json');assert all(sha(HERE/n)==h for n,h in freeze['files'].items())
assert s['lease_scope']==dict(unit_prefix='bplus-frontjob-20261019-',slice='bplus-front-20261019.slice',cpu=2,deadline=s['lease_scope']['deadline']);deadline=dt(s['lease_scope']['deadline']);assert deadline==datetime.datetime(2026,10,19,11,45,tzinfo=datetime.timezone.utc)
assert 0<s['elapsed_seconds']<=1200 and 0<(dt(s['finished_utc'])-dt(s['started_utc'])).total_seconds()<=1200 and (deadline-dt(s['started_utc'])).total_seconds()>=1220 and dt(s['finished_utc'])<=deadline
assert s['identities_before']==s['identities_after'];assert set(s['identities_before']['sources'])==set(IDS['binaries']);assert s['identities_before']['binaries']=={n:v['sha256'] for n,v in IDS['binaries'].items()}
for name,got in s['identities_before']['sources'].items():
 expected=dict(IDS['source_hashes']);expected['src/zset_btree.c']=IDS['candidate_source_sha256'] if name.endswith('-A') else expected['src/zset_btree.c']
 if name.startswith('h4-'):expected['bench/iterator_modes.c']=sha(HERE/'inputs/iterator_modes.c')
 assert got==expected
assert s['sources_before']==s['sources_after'] and s['binaries_before']==s['binaries_after'];assert set(s['sources_before'])==set(s['binaries_before'])=={'control','A'}
for v,got in s['sources_before'].items():
 expected=dict(IDS['source_hashes']);expected.update({'bench/'+f.name:sha(f) for f in (HERE/'inputs').iterdir() if f.suffix in ['.c','.h']});expected['src/zset_btree.c']=IDS['candidate_source_sha256'] if v=='A' else IDS['source_hashes']['src/zset_btree.c'];assert got==expected
assert set(s['original_actual_text_identity'])==set(IDS['binaries'])
for k,x in s['original_actual_text_identity'].items():
 front,v=k.split('-');assert x['original_text_sha256']==x['actual_text_sha256'] and x['actual_binary_sha256']==IDS['binaries'][k]['sha256'] and x['original_binary_sha256']==s['binaries_before'][v]['build/'+front+'-original']
rows={};refs={};censuses={};counterdata={};previous=dt(s['started_utc']);warnings=[]
for r,c in zip(s['commands'],contracts):
 assert all(r[k]==v for k,v in c.items());assert r['returncode']==0 and previous<=dt(r['started_utc'])<=dt(r['finished_utc'])<=dt(s['finished_utc']) and 0<(dt(r['finished_utc'])-dt(r['started_utc'])).total_seconds()<=120;previous=dt(r['finished_utc']);text=(out/(c['name']+'.stdout')).read_text();err=(out/(c['name']+'.stderr')).read_text()
 if re.search(r'\b(lost|warning)\b',err,re.I):warnings.append(dict(command=c['name'],stderr=err))
 if c['kind']=='original43':assert '43 passed, 0 failed, 43 total' in re.sub(r'\x1b\[[0-9;]*m','',text)
 if c['fixture']:
  f=c['fixture'];z=row(text,f);assert z==r['row'];rows[c['name']]=z;key=(f['frontend'],f['direction'],f['size'],f['seed'],f['requested_ops'],allocator_mode(c));assert same_semantics(z,refs.setdefault(key,z))
  if c['kind']=='census':obs=census(err,f,z);assert obs==r['census']==censuses.setdefault(key,obs)
  elif c['kind'] in ['instrument','tree']:assert not err.strip()
 if c['kind'] in ['tree-stat','disabled-stat','known-stat']:
  enabled=c['kind']=='tree-stat' or c['name']=='known-enabled-stat';obs=counters(out/c['stat_file'],enabled);assert obs==r['counters'];counterdata[c['name']]=obs
 if c['kind'] in ['known','known-stat']:assert json.loads(text)==json.loads((HERE/'inputs/known-control-expectations.json').read_text())['expected_stdout']
known=known_gate(out,HERE/'inputs');assert known==s['known_gate'];fault_rows=raw_samples(out/'known-missing-disable-samples.stdout');fault_report=report(out/'known-missing-disable-report.stdout',fault_rows);assert fault_report['lost']==0 and sum(x['symbol']=='outside_work' for x in fault_rows)>0 and s['scope_fault_detected']
assert len(s['raw_data_sha256'])==38
# Reconstruct complete encoded .text from disassembly and pin protected originals.
def text_hash(functions):
 words={}
 for fn in functions.values():
  for off,x in fn['instructions'].items():words[fn['start']+off]=int(x['bytes'][0],16).to_bytes(4,'little')
 # Objdump includes non-.text sections; own original-vs-actual exact whole listing
 # comparison below does not substitute for the direct ELF .text producer proof.
 return words
maps={};map_summary={}
for front in ['primary','h4']:
 for v in ['control','A']:
  key=front+'-'+v;original=parse(out/(key+'-original-full-asm.stdout'));actual=parse(out/(key+'-actual-full-asm.stdout'));diag=parse(out/(key+'-profile-full-asm.stdout'));maps[key]=(diag,original,actual)
  # Addresses/encoded words in .text symbols must match actual; debug source labels may differ.
  assert text_hash(original)==text_hash(actual),(key,'reconstructed original/actual code differs')
  bodies={}
  for sym in sorted(set(diag)|set(original)|set(actual)):
   if sym.startswith('zbt') or sym in ['main','traverse']:
    ds=diag.get(sym,{}).get('instructions',{});os=original.get(sym,{}).get('instructions',{});ac=actual.get(sym,{}).get('instructions',{});bodies[sym]=dict(diagnostic=len(ds),original=len(os),actual=len(ac),same_offset_equal=sum(off in os and off in ac and x['bytes']==os[off]['bytes']==ac[off]['bytes'] for off,x in ds.items()),entries={str(off):dict(diagnostic=x,original=os.get(off),actual=ac.get(off)) for off,x in ds.items()})
  map_summary[key]=bodies
# A moved instruction is credited only through a unique exact seven-word window
# within the SAME symbol in both own original and actual. No mnemonic normalization.
source_ranges=json.loads((HERE/'source-ranges.json').read_text());profiles=[];all_tree=True;all_pc=True;all_losses=known['lost']==0;total_events=0;total_period=0
for c in contracts:
 if 'capture_file' not in c:continue
 label=c['capture_file'][:-5];raw=raw_samples(out/(label+'-samples.stdout'));rr=report(out/(label+'-report.stdout'),raw);assert raw and rr['raw_period']>0;all_losses &= rr['lost']==0;key=c['fixture']['frontend']+'-'+c['variant'];diag,original,actual=maps[key];categories=collections.Counter();periods=collections.Counter();linked=[];bases=set();tree_matches=True
 for x in raw:
  sym=x['symbol'];off=x['offset'];category='unknown';entry=dict(x)
  if sym in diag and off in diag[sym]['instructions']:
   instruction=diag[sym]['instructions'][off];pc=diag[sym]['start']+off;base=int(x['physical_ip'],16)-pc;assert base>=0 and base%4096==0; bases.add(base);entry.update(elf_address=pc,load_base=base,instruction=instruction,original=mapping(diag[sym]['instructions'],original.get(sym,{}).get('instructions',{}),off),actual=mapping(diag[sym]['instructions'],actual.get(sym,{}).get('instructions',{}),off))
   matched=entry['original']['status'] in ['same_offset_exact','unique_exact_seven_word_window'] and entry['actual']['status'] in ['same_offset_exact','unique_exact_seven_word_window']
   if sym.startswith('zbt'):
    category='IteratorNext_other' if sym=='zbtreeIteratorNext' else 'other_tree';tree_matches &= matched
    source=instruction['source_line'];sr=source_ranges[c['variant']]
    if source and source.startswith('zset_btree.c:'):
     line=int(source.split(':')[1])
     if sr['decoder_lines'][0]<=line<=sr['decoder_lines'][1]:category='packed_score_decoder'
     elif sym=='zbtreeIteratorNext' and line in sr['leaf_transition_lines']:category='IteratorNext_leaf_transition'
   elif sym=='traverse':category='H4_consumer_traverse'
   elif sym=='main':category='primary_consumer_main' if c['fixture']['frontend']=='primary' else 'H4_other_main'
   else:category='scope_or_other_own_code'
  elif sym not in ['[unknown]'] and not sym.startswith('0x'):category='external_or_unmapped'
  entry['exclusive_category']=category;categories[category]+=1;periods[category]+=x['period'];linked.append(entry)
 assert len(bases)<=1;all_pc &= bool(bases);all_tree &= tree_matches;total_events+=len(raw);total_period+=rr['raw_period'];profiles.append(dict(label=label,fixture=c['fixture'],variant=c['variant'],report=rr,all_sampled_tree_bytes_match_actual=tree_matches,load_bases=sorted(bases),exclusive_events=dict(categories),exclusive_periods=dict(periods),samples=linked))
assert len(profiles)==36
# Instrument precision and original-versus-disabled perturbation stay source/fixture scoped.
instrument=[]
for key in sorted({(c['variant'],c['fixture']['id']) for c in contracts if c['kind']=='instrument'}):
 phases={}
 for phase in ['instrument-AA','instrument-perturbation']:
  blocks=[]
  for block in range(3):
   cs=[c for c in contracts if c['kind']=='instrument' and (c['variant'],c['fixture']['id'])==key and c['instrument_phase']==phase and c['instrument_contract']['block']==block];assert len(cs)==4;zs=[rows[c['name']] for c in cs];v=[D(z['elapsed_ns'])/D(z['operations']) for z in zs];effect=((v[1]+v[2])/(v[0]+v[3])-1)*100;blocks.append(dict(block=block,effect_pct=str(effect),minimum_window_ns=min(int(z['elapsed_ns']) for z in zs)))
  phases[phase]=dict(blocks=blocks,qualified=all(abs(D(b['effect_pct']))<=1 and b['minimum_window_ns']>=10000000 for b in blocks))
 instrument.append(dict(source=key[0],cell=key[1],phases=phases,elapsed_transfer_qualified=all(x['qualified'] for x in phases.values())))
pairs=[]
for cell in json.loads((HERE/'cells.json').read_text()):
 for seed in [1701,1702,1703]:
  names=[f'{v}-{cell["id"]}-s{seed}-stat' for v in ['control','A']];values={v:{event:str(D(counterdata[n]['values'][event])/D(rows[n]['operations'])) for event in sorted(counterdata[n]['values'])} for v,n in zip(['control','A'],names)};delta={event:str((D(values['A'][event])/D(values['control'][event])-1)*100) if D(values['control'][event]) else None for event in values['control']};pairs.append(dict(cell=cell['id'],seed=seed,per_visit=values,change_pct=delta,instructions_decreased=D(values['A']['instructions:u'])<D(values['control']['instructions:u'])))
valid_scope=scope_validity(all_losses,warnings,all_pc)
hypothesis='SUPPORTED' if valid_scope and all(x['instructions_decreased'] for x in pairs) else 'FALSIFIED' if valid_scope else 'INCONCLUSIVE'
result=dict(status='integrity_pass',source_selection='NONE',prior_decision='REJECT',command_count=642,scope_valid=valid_scope,known_control=known,negative_scope_detected=True,all_known_scientific_losses_zero=all_losses,perf_warnings=warnings,all_sampled_tree_bytes_match_actual=all_tree,code_attribution_valid=valid_scope and all_tree,caller_mapping_limits='All unmatched/different caller bytes retained; no causal elapsed attribution or equivalence across frontends.',instruction_hypothesis=hypothesis,matched_counter_pairs=pairs,instrumentation_qualification=instrument,census_cells=len(censuses),census=censuses and [{'key':list(k),'census':v} for k,v in censuses.items()],profiles=profiles,total_scientific_events=total_events,total_scientific_period=total_period,complete_code_map=map_summary,result_sha256=sha(out/'result.json'),raw_files_sha256={x.name:sha(x) for x in sorted(out.iterdir()) if x.is_file() and x.name not in ['audit.json','result.json'] and x.suffix!='.data'},raw_data_sha256=s['raw_data_sha256'])
(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','scope_valid','code_attribution_valid','instruction_hypothesis','total_scientific_events']}))
