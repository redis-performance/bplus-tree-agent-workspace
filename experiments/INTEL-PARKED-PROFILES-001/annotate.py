"""Offline exact-ELF annotation; no new measurements or source modifications."""
import hashlib,json,subprocess
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent
symfs=R/'scratch/intel-parked-symfs';root=symfs/'tmp/bplus-intel-parked-001';perf=R/'scratch/intel-perf7';out=H/'annotation';out.mkdir(exist_ok=True)
records=[]
for v in ['base','itA','itB']:
 tag=f'iterator-1000000-forward-integer-7-{v}';raw=root/'raw'/(tag+'.perf.data');binary=root/'build'/v/'iterator'
 cmd=[str(perf), 'annotate','-i',str(raw),'--stdio','--no-source','--symbol','zbtreeIteratorNext','--percent-type','global-period','--print-line','--full-paths','--symfs',str(symfs)]
 r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr
 (out/(tag+'.txt')).write_text(r.stdout);(out/(tag+'.stderr')).write_text(r.stderr)
 records.append({'tag':tag,'raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'binary_sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),'command':[x.replace(str(R),'$REPO') for x in cmd],'returncode':r.returncode})
(out/'commands.json').write_text(json.dumps({'decoder_version':subprocess.check_output([str(perf),'--version'],text=True).strip(),'decoder_sha256':hashlib.sha256(perf.read_bytes()).hexdigest(),'records':records,'scope':'Offline cycles:u global-period shares, symbol selected; exact ELF DWARF line attribution, not causal latency. Optimized lines and sampling skid limit attribution.'},indent=2)+'\n')
