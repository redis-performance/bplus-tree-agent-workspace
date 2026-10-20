"""Offline, whole-workload period normalization of retained samples. No profiling."""
import collections,hashlib,json,re,subprocess
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent;OLD=R/'experiments/INTEL-PARKED-PROFILES-001';SYM=R/'scratch/intel-parked-symfs';DATA=SYM/'tmp/bplus-intel-parked-001';PERF=R/'scratch/intel-perf7';OUT=H/'decoded';OUT.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
records=[];commands=[]
def run(args):
 p=subprocess.run([str(x) for x in args],capture_output=True,text=True);assert p.returncode==0,p.stderr
 commands.append({'args':[str(x).replace(str(R),'$REPO') for x in args],'returncode':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout.encode()).hexdigest(),'stderr':p.stderr.replace(str(R),'$REPO')});return p.stdout
libc=SYM/'usr/lib/x86_64-linux-gnu/libc.so.6';dbg=SYM/'usr/lib/debug/.build-id/a4/a7992a8e66555c8141ab2a08a8465ff6e0ea65.debug'
for p in [libc,dbg]:assert 'a4a7992a8e66555c8141ab2a08a8465ff6e0ea65' in run(['readelf','-n',p])
for old in json.loads((OLD/'results/summary.json').read_text()):
 tag=old['cell']+'-'+old['variant'];raw=DATA/'raw'/(tag+'.perf.data');assert sha(raw)==old['raw_perf_sha256']
 binary=DATA/next(x for x in old['workload_command'] if x.startswith('build/'));assert sha(binary)==old['binary_sha256']
 ids=run([PERF,'buildid-list','-i',raw]);(OUT/(tag+'.buildids')).write_text(ids)
 if 'libc.so.6' in ids:assert 'a4a7992a8e66555c8141ab2a08a8465ff6e0ea65 /usr/lib/x86_64-linux-gnu/libc.so.6' in ids
 events=run([PERF,'script','-i',raw,'-F','period,ip,sym,symoff,dso','--symfs',SYM]);(OUT/(tag+'.events')).write_text(events)
 groups=collections.defaultdict(lambda:{'period':0,'samples':0,'offsets':collections.Counter()});total=0;count=0
 for line in events.splitlines():
  m=re.fullmatch(r'\s*(\d+)\s+([0-9a-f]+)\s+(.+) \((.+)\)',line);assert m,line
  period=int(m[1]);symbol,sep,offset=m[3].rpartition('+0x')
  if not sep:symbol=m[3];offset=None
  key=(symbol,m[4]);groups[key]['period']+=period;groups[key]['samples']+=1
  if offset is not None:groups[key]['offsets'][int(offset,16)]+=period
  total+=period;count+=1
 report=run([PERF,'report','--stdio','--no-children','--percent-limit','0','--sort','symbol,dso','-i',raw,'--symfs',SYM]);(OUT/(tag+'.symbols')).write_text(report)
 assert int(re.search(r'# Samples: (\d+)',report)[1])==count
 assert int(re.search(r'# Event count \(approx.\): (\d+)',report)[1])==total
 wanted=['zbtreeFindForAdd','zbtScoreLeafFindMember'] if tag.startswith('update') else ['zbtreeIteratorNext'] if tag.startswith('iterator') else ['zbtIndexScanSlot']
 nm=run(['nm','-n',binary]);addresses={m[2]:int(m[1],16) for l in nm.splitlines() if (m:=re.fullmatch(r'([0-9a-f]+) [tT] (.+)',l))}
 symbols=[]
 for (name,dso),g in sorted(groups.items(),key=lambda p:-p[1]['period']):
  item={'symbol':name,'dso':dso,'period':g['period'],'sample_count':g['samples'],'workload_period_percent':100*g['period']/total}
  if name in wanted:
   assert name in addresses
   item['hot_instructions']=[]
   for off,period in g['offsets'].most_common(8):
    addr=addresses[name]+off;mapping=run(['addr2line','-f','-i','-e',binary,hex(addr)]);ins=run(['objdump','-d','--start-address='+hex(addr),'--stop-address='+hex(addr+16),binary])
    item['hot_instructions'].append({'symbol_offset':hex(off),'elf_address':hex(addr),'period':period,'workload_period_percent':100*period/total,'selected_symbol_period_percent':100*period/g['period'],'dwarf':mapping,'disassembly':ins.replace(str(R),'$REPO')})
  symbols.append(item)
 records.append({'tag':tag,'raw_sha256':sha(raw),'binary_sha256':sha(binary),'sample_count':count,'whole_workload_period':total,'symbols':symbols})
(H/'offline.json').write_text(json.dumps({'scope':'Reanalysis of prior raw cycles:u; not new captures. Whole-workload period denominator includes every exported sample. Ownership limitation applies.','libc_sha256':sha(libc),'debug_sha256':sha(dbg),'decoder_sha256':sha(PERF),'configurations':records},indent=2)+'\n')
(H/'offline-commands.json').write_text(json.dumps(commands,indent=2)+'\n')
print('Decoded',len(records),'retained profiles with exact libc and workload denominators')
