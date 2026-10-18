from pathlib import Path
import subprocess,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-profile-002/base'
assert not (P/'api-and-code-review.json').exists();record={'commands':[],'artifact_hashes':{},'sdk_sources':{}}
commands=[['xcrun','dwarfdump','--uuid',str((B/'build/release/btree-bench').relative_to(R)),str((B/'build/release/btree-bench.dSYM').relative_to(R))],['xcrun','dwarfdump','--uuid',str((B/'build/release/calibrate').relative_to(R)),str((B/'build/release/calibrate.dSYM').relative_to(R))],['nm','-u',str((B/'build/release/btree-bench').relative_to(R))]]
for command in commands:
 p=subprocess.run(command,cwd=R,capture_output=True,text=True,timeout=120);assert p.returncode==0
 record['commands'].append({'command':command,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 if command[0]=='nm':assert 'atomic' not in p.stdout
for d in ['btree-bench.dSYM','calibrate.dSYM']:
 for path in (B/'build/release'/d).rglob('*'):
  if path.is_file():record['artifact_hashes'][str(path.relative_to(R))]=hashlib.sha256(path.read_bytes()).hexdigest()
sdk=Path('/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk')
for rel in ['usr/share/man/man2/getitimer.2','usr/share/man/man2/sigaction.2','usr/include/sys/time.h','usr/include/sys/_types/_ucontext.h','usr/include/arm/_mcontext.h','usr/include/mach/arm/_structs.h','usr/include/dlfcn.h']:
 record['sdk_sources'][rel]=hashlib.sha256((sdk/rel).read_bytes()).hexdigest()
record['review']={'timer':'Installed getitimer(2) states process virtual+system CPU accounting, interval rounding and interrupted syscalls. Requested interval is not measured cadence.','signal':'Installed sigaction(2) documents SA_SIGINFO ucontext argument. Checked public arm64 PC accessor and context layout.','handler':'Only lock-free atomic counter/PC stores plus ucontext reads; atomic_is_lock_free checked at startup. nm imports contain no out-of-line atomic support. This does not prove absence of sampling bias.','scope':'Timer armed before operation clock and disabled after operation clock; small boundary helpers may be sampled. Fixture construction and warmup excluded.','thread_timer':'PROFILE-002 dumps before thread clock ends; never interpret its thread/wall ratio. DIAG-006 moves dump after endpoint.','provenance':'Sequential coordinator inspection; not independent review. No process attach, privileged APIs or permission changes.'}
(P/'api-and-code-review.json').write_text(json.dumps(record,indent=2)+'\n');print('PASS SDK hashes, dSYM/binary UUID output and atomic import audit')
