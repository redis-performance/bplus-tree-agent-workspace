"""Cross-check final reports against independently reconstructed capture evidence."""
import collections,hashlib,json,re,subprocess
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent
load=lambda n:json.loads((H/n).read_text())
a=load('analysis.json');audit=load('INDEPENDENT-AUDIT.json');records=load('results/summary.json');calls=load('topdown-mcp-calls.json')['calls']
assert len(records)==len(a['configurations'])==audit['records']==36
assert sum(c['interpretation_qualified'] for c in a['configurations'])==audit['all_l2_qualified_configurations']==32
assert sum(c['l2_qualified_windows'] for c in a['configurations'])==audit['qualified_l2_windows']==104
assert all(c['counters']['qualified'] and c['samples']['qualified'] for c in a['configurations'])
assert all(c['samples']['recorded_losses']=='none recorded' and c['samples']['available'] and c['counters']['available'] for c in audit['configurations'])
assert audit['all_profiled_binaries_copied_and_verified'] and audit['profile_windows_serial_by_recorded_wall_clock']
assert collections.Counter(c['tool'] for c in calls)=={'get_funnel':32,'compare_runs':12}
assert not any(c['result'].get('isError') for c in calls)
assert load('RELEASE-FINAL.json')['pass']
for c in a['configurations']:
 independent=next(x for x in audit['configurations'] if (x['cell'],x['variant'])==(c['cell'],c['variant']))
 assert independent['all_l2_qualified']==c['interpretation_qualified']
for p in [H/'README.md',H/'ASSESSMENT.md',H/'ITERATOR.md',H/'SCAN.md',H/'UPDATE.md',R/'README.md',R/'experiments/NEXT-STEPS.md',R/'experiments/TMA-COVERAGE.md']:
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in link and not link.startswith('#'):assert (p.parent/link.split('#')[0]).exists(),(p,link)
assert not subprocess.check_output(['git','diff','37efd287f','--','src','compat','vendor','bench','tests'],cwd=R)
sealed={str(p.relative_to(H)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(H.rglob('*')) if p.is_file() and p.name not in ['SHA256.json','FINAL-CHECKS.json'] and '__pycache__' not in p.parts}
(H/'SHA256.json').write_text(json.dumps(sealed,indent=2)+'\n')
(H/'FINAL-CHECKS.json').write_text(json.dumps({'result':'PASS','configuration_count':36,'qualified_configurations':32,'qualified_l2_windows':104,'counter_sample_scopes':36,'raw_loss_records':0,'actual_mcp_calls':len(calls),'source_and_referees_unchanged_from':'37efd287f','links_exist':True,'seal_files':len(sealed),'independent_audit_sha256':hashlib.sha256((H/'INDEPENDENT-AUDIT.json').read_bytes()).hexdigest(),'interpretation':'diagnostic only; four failed configurations preserved; no timing/source acceptance'},indent=2)+'\n')
print('PASS:',len(sealed),'sealed files;32/36 TMA configs;104/108 windows;source/referees unchanged')
