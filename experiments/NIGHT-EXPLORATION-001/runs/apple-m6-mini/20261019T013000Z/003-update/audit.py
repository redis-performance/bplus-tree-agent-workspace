#!/usr/bin/env python3
from pathlib import Path
import csv,hashlib,io,json,statistics,subprocess
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent
ROOT=Path.cwd();BASE=Path('scratch/m6-update/variants')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze=json.loads((OUT/'comparison-freeze.json').read_text());assert all(sha(OUT/f)==h for f,h in freeze['files'].items())
original=json.loads((OUT/'freeze.json').read_text());assert all(sha(f)==h for f,h in original['files'].items())
implementation=json.loads((OUT/'implementation-manifest.json').read_text())
for v in ('0','A','B','C'):
 assert sha(BASE/v/'src/zset_btree.c')==freeze['source_binaries'][v]['source']
 assert sha(BASE/v/'build/update')==freeze['source_binaries'][v]['binary']
 for f,h in implementation['common_referee_hashes'].items():assert sha(BASE/v/f)==h,(v,f)
 if v!='0':
  target=Path('scratch/m6-update/reconstruct')/v;(target/'src').mkdir(parents=True,exist_ok=True);(target/'src/zset_btree.c').write_bytes(Path('src/zset_btree.c').read_bytes());r=subprocess.run(['patch','-p1','--batch','-i',str((OUT/'variants'/v/'candidate.patch').resolve())],cwd=target,capture_output=True,text=True);assert r.returncode==0 and sha(target/'src/zset_btree.c')==freeze['source_binaries'][v]['source']
d=json.loads((OUT/'discovery.json').read_text());q=json.loads((OUT/'qualification.json').read_text());cal=json.loads((OUT/'calibration.json').read_text());assert d['status']==q['status']=='complete';assert len(d['runs'])==144 and len(q['runs'])==48 and len(cal['observations'])==75
for r in d['runs']+q['runs']+cal['observations']:
 file=OUT/r['file'];assert sha(file)==r['sha256'];x=list(csv.DictReader(io.StringIO(file.read_text())));assert len(x)==1;x=x[0];assert int(x['ops'])==r['ops'] and int(x['size'])==r['size'] and int(x['elapsed_ns'])==r['elapsed_ns'] and x['checksum']==r['checksum'] and int(x['tree_bytes'])==r['tree_bytes']
for result in d['results']:
 for block,effect in enumerate(result['effects_pct']):
  rs=[r for r in d['runs'] if r['variant']==result['variant'] and r['size']==result['size'] and r['block']==block];a=statistics.mean(r['ns_op'] for r in rs if r['label']=='A');b=statistics.mean(r['ns_op'] for r in rs if r['label']=='B');assert abs(effect-100*(b/a-1))<1e-12
records=[]
for log in ('commands.jsonl','candidate-commands.jsonl'):
 records += [json.loads(l) for l in (OUT/log).read_text().splitlines()]
records.sort(key=lambda r:r['started_utc']);assert all(a['finished_utc']<=b['started_utc'] for a,b in zip(records,records[1:]))
errors=[r['name'] for r in records if r['returncode']!=0];assert set(errors)=={'0-repack-san','fault-offset','fault-headroom'}
private=[]
for f in OUT.rglob('*'):
 if f.is_file() and f.suffix not in ('.patch',):
  content=f.read_text();assert ('/'+'Users/') not in content and ('/'+'private/') not in content,str(f)
summary=dict(status='PASS',checked_utc=datetime.now(timezone.utc).isoformat(),source_referee_binary_hashes=True,patch_reconstructions=3,calibration_rows=75,AA_rows=48,discovery_rows=144,paired_effects_reconstructed=36,serial_command_windows=len(records),expected_nonzero_commands=errors,shortest_discovery_window_ms=min(r['elapsed_ns'] for r in d['runs'])/1e6,adoption=False,independent_review=False)
(OUT/'final-audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)
