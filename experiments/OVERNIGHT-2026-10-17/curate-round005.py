"""Curate local method metadata; full MCP text stays in ignored scratch."""
from pathlib import Path
import hashlib,json,subprocess
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent;S=R/'scratch/overnight-round005-method'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'retrievals':{},'sdk_sources':{},'environment':{},'review':{}}
for f in sorted(S.glob('*.json')):record['retrievals'][f.name]={'path':str(f.relative_to(R)),'sha256':sha(f)}
sdk=Path('/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk')
for rel in ['usr/include/pthread/pthread.h','usr/include/pthread/qos.h','usr/share/man/man2/getitimer.2','usr/share/man/man2/sigaction.2']:
 record['sdk_sources'][rel]=sha(sdk/rel)
for cmd in [['cc','--version'],['uname','-m'],['sw_vers','-productVersion']]:
 p=subprocess.run(cmd,cwd=R,capture_output=True,text=True,timeout=30);assert p.returncode==0
 # Standard compiler/architecture/version output only; never hostname or private configs.
 output=p.stdout.replace(str(R),'<workspace>')
 record['environment'][' '.join(cmd)]={'returncode':p.returncode,'stdout':output,'stderr':p.stderr}
record['method_sources']=[{'url':'https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/05-measurement-pitfalls/README.md','use':'Retain fixed repeated observations and meaningful checksums. No M4 results copied.'},{'url':'https://github.com/usamahz/cpu-performance-engineering/blob/main/misc/benchmarks/14-pcore-vs-ecore/README.md','use':'Thread CPU and boundary CPU observations, method says nothing pinned. No topology,frequency or measurements transferred.'}]
record['review']={'ask':'Google Benchmark CPU timer scope passage relevant only to timer scope; Intel/OpenVINO/other retrievals not support for local diagnosis.','cpu_ids':'Installed pthread.h says CPU may change before return; IDs remain opaque.','qos':'Installed qos.h says overrides invisible to getter; effective QoS unknown.','signals':'Installed sigaction.2 list does not include clock_gettime and labels unlisted calls unsafe. No handler timestamp added.','evidence_checker':'DIAG-008 and AA-004 checker reports no_number; DIAG-009 reports drop_number, missing clock and heuristically missing explicitly stated fields. Retain raw local diagnostics, promote no portable performance/GHz/source-speed claim. DIAG-007 checker was consulted; its response was not separately persisted, so no invented raw hash.','provenance':'One attempted reviewer failed at thread-store context load before running. No independent participant/model/cost. Sequential coordinator audit only.'}
(P/'ROUND-005-METHOD.json').write_text(json.dumps(record,indent=2)+'\n')
# Preserve dSYM and atomic-import/UUID evidence hashes for corrected calibration.
B=R/'scratch/overnight-diag-009/base';artifacts={}
for f in (B/'build/release/calibrate.dSYM').rglob('*'):
 if f.is_file():artifacts[str(f.relative_to(R))]=sha(f)
(P/'DIAG-009/artifacts.json').write_text(json.dumps(artifacts,indent=2)+'\n')
print('PASS curated method/SDK/environment/artifact hashes; full retrievals remain ignored')
