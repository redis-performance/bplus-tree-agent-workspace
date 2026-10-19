from pathlib import Path
import json,csv,re,datetime,collections,bisect
p=Path(__file__).parent;records=json.loads((p/'processes.json').read_text());captures=json.loads((p/'captures.json').read_text());complete=json.loads((p/'complete.json').read_text());schedule=json.loads((p/'capture-schedule.json').read_text());assert complete['status']=='complete' and complete['captures']==len(captures)==len(schedule)==60 and complete['elapsed_seconds']<600
assert complete['metadata_correction'] and complete['initial_helper_returncode']==1
assert json.loads((p/'raw-before-metadata.json').read_text())==json.loads((p/'raw-after-metadata.json').read_text())
metadata_records=json.loads((p/'metadata-processes.json').read_text());records=records+metadata_records
last=None
for x in records:
 assert x['returncode']==0;a=datetime.datetime.fromisoformat(x['started_utc']);b=datetime.datetime.fromisoformat(x['finished_utc']);assert a<=b and (last is None or last<=a);last=b
known=json.loads((p/'known-control.json').read_text());assert known['enabled_samples']>=20 and known['known_work_samples']/known['enabled_samples']>=.9 and known['disabled_samples']==0 and known['checksum_equal']
meta={}
for f in (p/'profiles').glob('*.hist.csv'):
 tag=f.name.removesuffix('.hist.csv');hist={int(x['offset']):int(x['count']) for x in csv.DictReader(f.open())};stderr=(p/'profiles'/(tag+'.stderr')).read_text();data=dict((k,int(v)) for k,v in re.findall(r'([a-z_]+)=(\d+)',stderr));assert data['bin_bytes']==2 and data['scale']==65536 and data['text_offset_start']==0 and data['captured']==sum(hist.values()) and data['max_bin']==max(hist.values(),default=0)<65535;assert all(0<=o<data['text_offset_end'] and o%2==0 and 0<c<65535 for o,c in hist.items())
 if data['disabled']:assert not hist
 else:assert data['interval_ns']>0 and data['cpu_elapsed_ns']//data['interval_ns']+4<65535
 meta[tag]=dict(metadata=data,histogram=hist)
fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes'];controls=json.loads((p/'semantic-controls.json').read_text());assert len(controls)==7;fixtures={}
for x in controls:
 a,b=x['original'],x['disabled'];assert all(a[k]==b[k] for k in fields)
 for r in [a,b]:assert r['cpu_start']==r['cpu_end']=='2'
 if x['mode']=='native':
  fixtures[(x['size'],x['seed'])]=a
  for mode,row in [('original',a),('disabled',b)]:assert list(csv.DictReader((p/'profiles'/f'{mode}-control-{x["size"]}-{x["seed"]}.stdout').open()))==[row]
 else:
  for mode,row in [('original',a),('disabled',b)]:assert list(csv.DictReader((p/'profiles'/f'{mode}-san-control.stdout').open()))==[row]
assert set(fixtures)=={(n,s) for n in [100000,1000000] for s in [1,2,3]}
for c,s in zip(captures,schedule):
 assert all(c[k]==v for k,v in s.items()) and list(csv.DictReader((p/'profiles'/(c['tag']+'.stdout')).open()))==[c['row']];assert all(c['row'][k]==fixtures[(c['size'],c['seed'])][k] for k in fields) and c['row']['cpu_start']==c['row']['cpu_end']=='2'
base=json.loads((p/'mapping.json').read_text())['linker_base'];mapping={int(x['Address'],16)-base:x['Symbol'] for x in json.loads((p/'metadata/diagnostic-inline-map.stdout').read_text())};maps=json.loads((p/'instruction-maps.json').read_text());actualmap=json.loads((p/'actual-attribution-map.json').read_text());ins=maps['diagnostic']['instructions'];starts=[x['offset'] for x in ins];byoffset={x['offset']:x for x in actualmap['instructions']}
def framekey(frames):return {(s['FunctionName'],s.get('Line'),s.get('Column')) for s in frames}
precise=[]
for item in actualmap['instructions']:
 okay=actualmap['same_function_size'] and item['exact_bytes'] and framekey(item['diagnostic']['frames'])==framekey(item['actual']['frames'])
 precise.append(dict(offset=item['offset'],exact_opcode_and_source_mapping=okay,diagnostic_frames=item['diagnostic']['frames'],actual_frames=item['actual']['frames'] if item['actual'] else []))
preciseby={x['offset']:x for x in precise};aggregate={};details=[]
for n in [100000,1000000]:
 counts=collections.Counter();total=callbacks=actualhelper=unmappedslot=slot=0
 for c in captures:
  if c['size']!=n:continue
  tag=c['tag'];hist=meta[tag]['histogram'];one=collections.Counter();mapped=unmapped=inslot=0
  for offset,count in hist.items():
   assert offset in mapping;frames=mapping[offset];names={s['FunctionName'] or '<unknown>' for s in frames} or {'<unknown>'}
   for name in names:one[name]+=count
   relative=base+offset-maps['diagnostic']['address']
   if 0<=relative<maps['diagnostic']['size']:
    inslot+=count;i=bisect.bisect_right(starts,relative)-1;entry=ins[i] if i>=0 else None
    if entry and relative<entry['offset']+len(entry['bytes']) and preciseby[entry['offset']]['exact_opcode_and_source_mapping']:
     if any(f['FunctionName']=='zbtLeafTagMatches' for f in preciseby[entry['offset']]['actual_frames']):mapped+=count
    else:unmapped+=count
  samples=sum(hist.values());assert samples>0;counts.update(one);total+=samples;callbacks+=int(c['row']['operations']);actualhelper+=mapped;unmappedslot+=unmapped;slot+=inslot;details.append(dict(tag=tag,captured=samples,inline_inclusive_samples=dict(one),actual_exact_mapped_helper_samples=mapped,scan_slot_address_samples=inslot,unmapped_scan_slot_samples=unmapped,sampler=meta[tag]['metadata']))
 aggregate[str(n)]=dict(captured=total,actual_callbacks=callbacks,diagnostic_helper_samples=counts['zbtLeafTagMatches'],diagnostic_helper_pct=100*counts['zbtLeafTagMatches']/total,diagnostic_helper_per_million_callbacks=1e6*counts['zbtLeafTagMatches']/callbacks,actual_exact_mapped_helper_samples=actualhelper,actual_exact_mapped_helper_pct=100*actualhelper/total,actual_exact_mapped_helper_per_million_callbacks=1e6*actualhelper/callbacks,scan_slot_address_samples=slot,unmapped_scan_slot_samples=unmappedslot,inline_inclusive_samples=dict(counts))
assert json.loads((p/'actual-before.json').read_text())==json.loads((p/'actual-after.json').read_text());assert json.loads((p/'diagnostic-after.json').read_text())['files']==json.loads((p/'build-freeze.json').read_text())['base'];result=dict(status='pass',captures=60,matched_controls=7,schedule_exact=True,serial_commands=len(records),overflow_bound_checked=True,phase_elapsed_seconds=complete['elapsed_seconds'],same_scan_slot_function_size=actualmap['same_function_size'],exact_opcode_source_mapped_instructions=sum(x['exact_opcode_and_source_mapping'] for x in precise),scan_slot_instructions=len(precise),denominator='Only captured in-range executable text; outside/library/missed/lost samples excluded or unknown. Inline shares overlap. Two-byte bucket boundaries and sampled PCs are approximate.',source_adoption='NONE',aggregate=aggregate,details=details,instruction_mapping=precise);(p/'profile-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['details','instruction_mapping']},indent=2))
