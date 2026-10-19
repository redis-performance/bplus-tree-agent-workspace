#!/usr/bin/env python3
"""Read-only reconstruction of M6 rank controls, candidate rows and provenance."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,io,json,statistics,difflib
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze=json.loads((OUT/'freeze.json').read_text());manifest=json.loads((OUT/'implementation-manifest.json').read_text());valid=json.loads((OUT/'candidate-validation.json').read_text());cf=json.loads((OUT/'comparison-freeze.json').read_text())
for f,h in freeze['files'].items():
 if f.startswith(('src/','compat/','vendor/','bench/','tests/')) or f=='Makefile':assert sha(f)==h,f
assert sha(OUT/'compare.py')==cf['driver_sha256']
assert sha(OUT/'DISCOVERY-PLAN.md')==cf['plan_sha256']
source=Path('src/zset_btree.c').read_text()
for ident in ['base','A','B','C']:
 dst=Path(manifest['variants'][ident]['snapshot'])
 for f,h in manifest['variants'][ident]['files'].items():assert sha(dst/f)==h,(ident,f)
 if ident!='base':
  code=(dst/'src/zset_btree.c').read_text();patch=''.join(difflib.unified_diff(source.splitlines(True),code.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'))
  assert (OUT/'variants'/ident/'candidate.patch').read_text()==patch
  assert sha(OUT/'variants'/ident/'candidate.patch')==manifest['variants'][ident]['patch_sha256']==cf['candidates'][ident]['patch_sha256']
  assert sha(dst/'build/rank')==valid['variants'][ident]['binary_sha256']==cf['candidates'][ident]['binary_sha256']
assert sha('scratch/m6-rank/build/night-rank')==cf['baseline_binary_sha256']
phases=[]
for filename in ['qualification.json','discovery.json']:
 m=json.loads((OUT/filename).read_text());assert m['status']=='complete'
 for r in m['runs']:
  path=OUT/r['csv'];assert sha(path)==r['sha256'];rows=list(csv.DictReader(io.StringIO(path.read_text())))
  assert len(rows)==3 and [int(x['elapsed_ns']) for x in rows]==r['windows_ns']
  assert [int(x['elapsed_ns'])/int(x['operations']) for x in rows]==r['ns_op']
  assert all(int(x['operations'])==r['ops'] and int(x['size'])==r['size'] and int(x['seed'])==r['seed'] for x in rows)
 for result in m['results']:
  for block,effect in enumerate(result['effects_pct']):
   rs=[r for r in m['runs'] if r['size']==result['size'] and r['block']==block and ('variant' not in result or r['variant']==result['variant'])]
   assert len(rs)==4 and ''.join(r['label'] for r in rs)=='ABBA' and len({r['checksum'] for r in rs})==1 and len({r['tree_bytes'] for r in rs})==1
   a=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='A');b=statistics.mean(statistics.mean(r['ns_op']) for r in rs if r['label']=='B');assert abs(100*(b/a-1)-effect)<1e-12
 phases.append(dict(file=filename,processes=len(m['runs']),batches=sum(len(r['windows_ns']) for r in m['runs']),timing_seconds=m['timing_seconds']))
commands=[]
for f in ['commands.jsonl','candidate-commands.jsonl']:
 for line in (OUT/f).read_text().splitlines():commands.append(json.loads(line))
commands.sort(key=lambda c:c['started_utc'])
for a,b in zip(commands,commands[1:]):assert a['finished_utc']<=b['started_utc'],(a['name'],b['name'])
# Calibration summary overlap was an unlogged inline analysis and remains explicitly
# disclosed; command chronology cannot certify absence of arbitrary other processes.
for filename in ['qualification.json','discovery.json']:
 m=json.loads((OUT/filename).read_text())
 for c in commands:
  if c['folder'] not in ['raw','discovery']:
   assert c['finished_utc']<=m['started_utc'] or c['started_utc']>=m['finished_utc'],(filename,c['name'])
result=dict(status='pass',audited_utc=datetime.now(timezone.utc).isoformat(),phases=phases,source_and_referee_hashes=True,three_patches_reconstructed=True,isolated_snapshot_hashes=True,recorded_commands_serial=True,recorded_build_test_profile_commands_disjoint_from_control_and_candidate_phases=True,unobserved_external_processes='unknown',calibration_limitation='CALIBRATION-LIMITATION.md; summary analysis overlapped calibration orchestration, preserved',independent_review='not performed',acceptance='not eligible',source_selection='NONE')
(OUT/'final-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
