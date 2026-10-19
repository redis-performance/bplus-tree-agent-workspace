from pathlib import Path
import subprocess,json,hashlib,datetime,time,re,csv,os
root=Path.cwd();p=Path(__file__).parent.resolve();d=root/'scratch/intel-corrected-scan-profile/base';actual=root/'scratch/intel-corrected-adapter';start=time.monotonic();records=[];deadline=datetime.datetime.fromisoformat('2026-10-19T05:42:18.759322+00:00');assert not (p/'complete.json').exists();assert len(json.loads((p/'captures.json').read_text()))==60;assert os.sched_getaffinity(0)=={2}
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for f,h in json.loads((p/'metadata-freeze.json').read_text())['files'].items():assert sha(p/f)==h
assert sha(p/'execution-freeze.json')==json.loads((p/'metadata-freeze.json').read_text())['original_execution_freeze_sha256']
build_before=json.loads((p/'build-freeze.json').read_text())['base'];assert {f:sha(d/f) for f in build_before}==build_before
(p/'diagnostic-before-metadata.json').write_text(json.dumps(dict(status='pass',files=build_before),indent=2)+'\n')
expected=json.loads((p.parent/'013-corrected-adapter-baseline/source-after.json').read_text())['files'];assert {f:sha(actual/f) for f in expected}==expected
rawfiles=[p/'captures.json',p/'semantic-controls.json',p/'known-control.json']+sorted((p/'profiles').glob('*.hist.csv'));rawfreeze={str(f.relative_to(p)):sha(f) for f in rawfiles};(p/'raw-before-metadata.json').write_text(json.dumps(rawfreeze,indent=2)+'\n');(p/'metadata').mkdir(exist_ok=False)
def run(cmd,tag):
 left=min(180-(time.monotonic()-start),(deadline-datetime.datetime.now(datetime.timezone.utc)).total_seconds());assert left>0;t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,cwd=d,capture_output=True,text=True,timeout=left);(p/'metadata'/(tag+'.stdout')).write_text(r.stdout);(p/'metadata'/(tag+'.stderr')).write_text(r.stderr);records.append(dict(tag=tag,command=cmd,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'metadata-processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode();return r.stdout
maps={}
for tag,binary in {'diagnostic':'build/profile','actual':str(actual/'build/corrected-adapter-intel/btree-bench')}.items():
 syms=[x.split() for x in (p/'profiles'/(tag+'-symbols.stdout')).read_text().splitlines()];sym=next(x for x in syms if x[-1]=='zbtIndexScanSlot');address,size=int(sym[0],16),int(sym[1],16);bases=[int(x[0],16) for x in syms if x[-1]=='__executable_start'];linkbase=bases[0] if bases else None
 if tag=='diagnostic':
  assert linkbase is not None;asm=(p/'profiles/diagnostic-scan-slot.stdout').read_text();mapping=json.loads((p/'profiles/diagnostic-instruction-map.stdout').read_text());layout=None
 else:
  assert linkbase is None;programs=run(['readelf','-lW',binary],'actual-program-headers');sections=run(['readelf','-SW',binary],'actual-section-headers');loads=[]
  for line in programs.splitlines():
   fields=line.split()
   if fields and fields[0]=='LOAD':loads.append(dict(file_offset=int(fields[1],16),virtual_address=int(fields[2],16),file_size=int(fields[4],16),memory_size=int(fields[5],16),flags=fields[6:-1],alignment=int(fields[-1],16)))
  assert loads and any(x['virtual_address']<=address and address+size<=x['virtual_address']+x['memory_size'] and 'E' in x['flags'] for x in loads);layout=dict(load_segments=loads,lowest_load_virtual_address=min(x['virtual_address'] for x in loads),linker_symbol_absent=True,actual_binary_never_sampled=True)
  asm=run(['objdump','-d','--insn-width=16','--disassemble=zbtIndexScanSlot',binary],'actual-scan-slot');run(['objdump','-dSl','--disassemble=zbtIndexScanSlot',binary],'actual-scan-slot-source');mapping=None
 instructions=[]
 for line in asm.splitlines():
  match=re.match(r'^\s*([0-9a-f]+):\s+((?:[0-9a-f]{2}\s+)+)\s*(.*)$',line)
  if match:
   pc=int(match[1],16);instructions.append(dict(address=pc,offset=pc-address,bytes=match[2].split(),assembly=match[3]))
 assert instructions
 if mapping is None:mapping=json.loads(run(['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj='+binary]+[hex(x['address']) for x in instructions],'actual-instruction-map'))
 assert len(mapping)==len(instructions)
 for ins,sym in zip(instructions,mapping):assert int(sym['Address'],16)==ins['address'];ins['frames']=sym['Symbol']
 maps[tag]=dict(binary=binary,linker_base=linkbase,address=address,size=size,instructions=instructions,layout=layout)
(p/'instruction-maps.json').write_text(json.dumps(maps,indent=2)+'\n');byoffset={x['offset']:x for x in maps['actual']['instructions']};matched=[]
for ins in maps['diagnostic']['instructions']:
 other=byoffset.get(ins['offset']);matched.append(dict(offset=ins['offset'],diagnostic=ins,actual=other,exact_bytes=bool(other and ins['bytes']==other['bytes'])))
(p/'actual-attribution-map.json').write_text(json.dumps(dict(method='Same ScanSlot function-relative instruction offset and exact opcode bytes; mismatches retained. Actual text layout comes from ELF headers; its absent linker symbol is null.',same_function_size=maps['actual']['size']==maps['diagnostic']['size'],instructions=matched),indent=2)+'\n');offsets=set()
for c in json.loads((p/'captures.json').read_text()):offsets.update(int(r['offset']) for r in csv.DictReader((p/'profiles'/(c['tag']+'.hist.csv')).open()))
base=maps['diagnostic']['linker_base'];run(['llvm-symbolizer-18','--inlining','--output-style=JSON','--obj=build/profile']+[hex(base+x) for x in sorted(offsets)],'diagnostic-inline-map');(p/'mapping.json').write_text(json.dumps(dict(linker_base=base,bucket_count=len(offsets)),indent=2)+'\n');assert {f:sha(actual/f) for f in expected}==expected;(p/'actual-after.json').write_text(json.dumps(dict(status='pass',files=expected),indent=2)+'\n');build=json.loads((p/'build-freeze.json').read_text())['base'];assert {f:sha(d/f) for f in build}==build;(p/'diagnostic-after.json').write_text(json.dumps(dict(status='pass',files=build),indent=2)+'\n');assert {str(f.relative_to(p)):sha(f) for f in rawfiles}==rawfreeze;(p/'raw-after-metadata.json').write_text(json.dumps(rawfreeze,indent=2)+'\n');now=datetime.datetime.now(datetime.timezone.utc);assert now<deadline;elapsed=(now-(deadline-datetime.timedelta(seconds=600))).total_seconds();(p/'complete.json').write_text(json.dumps(dict(status='complete',captures=60,elapsed_seconds=elapsed,metadata_correction=True,metadata_elapsed_seconds=time.monotonic()-start,initial_helper_returncode=1,initial_helper_elapsed_seconds=91.91529,finished_utc=now.isoformat(),original_deadline_utc=deadline.isoformat()),indent=2)+'\n');print('PASS metadata-only correction; no measurements repeated')
