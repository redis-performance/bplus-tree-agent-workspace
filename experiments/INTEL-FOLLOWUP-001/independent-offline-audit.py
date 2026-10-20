"""Independently reconstruct all retained periods; no runner commands."""
import collections,hashlib,io,json,math,re,subprocess,tarfile
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent
S=R/'scratch/intel-parked-symfs';D=S/'tmp/bplus-intel-parked-001'
P=R/'scratch/intel-perf7';analysis=json.loads((H/'offline.json').read_text())
old=json.loads((R/'experiments/INTEL-PARKED-PROFILES-001/results/summary.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args):
 r=subprocess.run([str(x) for x in args],capture_output=True,text=True)
 assert r.returncode==0,(args,r.stderr)
 return r.stdout
buildid='a4a7992a8e66555c8141ab2a08a8465ff6e0ea65'
lib=S/'usr/lib/x86_64-linux-gnu/libc.so.6'
debug=S/'usr/lib/debug/.build-id/a4/a7992a8e66555c8141ab2a08a8465ff6e0ea65.debug'
package=R/'scratch/intel-followup/libc6-dbg.deb'
metadata=(R/'scratch/intel-followup/libc-package.txt').read_text()
assert sha(package)==re.search(r'^SHA256: (\w+)$',metadata,re.M)[1]
assert run(['dpkg-deb','-f',package,'Version']).strip()=='2.39-0ubuntu8.9'
archive=subprocess.run(['dpkg-deb','--fsys-tarfile',str(package)],capture_output=True)
assert archive.returncode==0
with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
 member=tar.extractfile('./usr/lib/debug/.build-id/a4/a7992a8e66555c8141ab2a08a8465ff6e0ea65.debug')
 assert member is not None and hashlib.sha256(member.read()).hexdigest()==sha(debug)
for path,key in [(lib,'libc_sha256'),(debug,'debug_sha256'),(P,'decoder_sha256')]:
 assert sha(path)==analysis[key]
 if path!=P:assert re.search(r'Build ID: (\w+)',run(['readelf','-n',path]))[1]==buildid
debug_symbols=run(['nm','-n',debug])
assert re.search(r'\b__memchr_evex$',debug_symbols,re.M)
assert re.search(r'\b__memcmp_evex_movbe$',debug_symbols,re.M)
records=[];hot_count=0
for record,previous in zip(analysis['configurations'],old):
 tag=previous['cell']+'-'+previous['variant'];assert tag==record['tag']
 raw=D/'raw'/(tag+'.perf.data');binary=D/next(x for x in previous['workload_command'] if x.startswith('build/'))
 assert sha(raw)==record['raw_sha256']==previous['raw_perf_sha256']
 assert sha(binary)==record['binary_sha256']==previous['binary_sha256']
 ids=run([P,'buildid-list','-i',raw])
 if 'libc.so.6' in ids:assert buildid+' /usr/lib/x86_64-linux-gnu/libc.so.6' in ids
 events=run([P,'script','-i',raw,'--symfs',S,'-F','event,period,ip,sym,symoff,dso'])
 counts=collections.Counter();periods=collections.Counter();offsets=collections.Counter();total=0;n=0
 for line in events.splitlines():
  m=re.fullmatch(r'\s*(\d+)\s+cycles:u:\s+([0-9a-f]+)\s+(.+)\s+\(([^()]*)\)',line);assert m,line
  period=int(m[1]);symbol=m[3];suffix=re.search(r'\+0x([0-9a-f]+)$',symbol)
  offset=int(suffix[1],16) if suffix else None
  if suffix:symbol=symbol[:suffix.start()]
  key=symbol,m[4];periods[key]+=period;counts[key]+=1
  if offset is not None:offsets[(key,offset)]+=period
  total+=period;n+=1
 assert n==record['sample_count'] and total==record['whole_workload_period']
 report=(H/'decoded'/(tag+'.symbols')).read_text()
 assert int(re.search(r'# Samples: (\d+)',report)[1])==n
 assert int(re.search(r'# Event count \(approx.\): (\d+)',report)[1])==total
 assert set(periods)=={(x['symbol'],x['dso']) for x in record['symbols']}
 addresses={}
 for line in run(['nm','-n',binary]).splitlines():
  f=line.split()
  if len(f)==3 and f[1] in ('t','T'):addresses[f[2]]=int(f[0],16)
 for symbol in record['symbols']:
  key=symbol['symbol'],symbol['dso']
  assert periods[key]==symbol['period'] and counts[key]==symbol['sample_count']
  assert math.isclose(100*periods[key]/total,symbol['workload_period_percent'],abs_tol=1e-10)
  for instruction in symbol.get('hot_instructions',[]):
   offset=int(instruction['symbol_offset'],16)
   assert offsets[key,offset]==instruction['period']
   assert addresses[key[0]]+offset==int(instruction['elf_address'],16)
   assert math.isclose(100*instruction['period']/total,instruction['workload_period_percent'],abs_tol=1e-10)
   assert math.isclose(100*instruction['period']/periods[key],instruction['selected_symbol_period_percent'],abs_tol=1e-10)
   hot_count+=1
 records.append({'tag':tag,'samples':n,'period':total,'symbols':len(periods),'pass':True})
assert len(records)==len(old)==36
out={'reviewer':'/root/intel_b_review','backend':'Codex','model':'unknown','token_cost':'unknown','configurations':records,'selected_hot_instruction_periods_verified':hot_count,'libc_build_id':buildid,'libc_sha256':sha(lib),'debug_sha256':sha(debug),'debug_package_sha256':sha(package),'debug_package_version':'2.39-0ubuntu8.9','debug_package_sha_matches_retained_apt_metadata':True,'decoder_sha256':sha(P),'offline_json_sha256':sha(H/'offline.json'),'limitations':['Offline identity/period validation only; ownership limitation unchanged.','Package checksum matches retained metadata; reviewer did not independently fetch/validate apt repository signatures.','Instruction periods are sampled attribution, not causal latency or per-operation costs.','Bounded disassembly may truncate following instructions; only full starting instructions may be interpreted.']}
print(json.dumps(out,indent=2))
