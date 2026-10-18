from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent;R=P.parents[3];M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert len(M['runs'])==16;outputs={};binaries={}
for v,ss in M['snapshots'].items():
 for n,h in ss['files'].items():assert sha(R/ss['path']/n)==h
 binaries[v]={k:sha(R/ss['path']/f'build/{k}') for k in ['release','sanitize']}
for r in M['runs']:
 assert r['returncode']==0
 for k in ['stdout','stderr']:assert sha(P/f'{r["name"]}.{k}')==r[k+'_sha256']
 if r['stage']=='run':
  lines=(P/f'{r["name"]}.stdout').read_text().splitlines();assert len(lines)==1941;d=dict((k,int(v)) for k,v in re.findall(r'(\w+)=(\d+)',lines[-1]));assert d['checks']==289060 and d['exact']==86570560;outputs[r['variant'],r['kind']]=lines
for k in ['release','sanitize']:assert all(outputs[v,k]==outputs['control',k] for v in ['A','B','C'])
a=outputs['control','release'];b=outputs['control','sanitize'];assert a[:-1]==b[:-1] and a[-1]!=b[-1]
for f in json.loads((P/'faults.json').read_text()):
 assert f['detected'] and f['commands'][0]['returncode']==0 and f['commands'][1]['returncode']!=0
 for r in f['commands']:
  for k in ['stdout','stderr']:assert sha(P/r[k])==r[k+'_sha256']
result=dict(status='semantic_controls_pass;preregistered_cross_build_whole_output_equality_unsupported',original_manifest_status=M['status'],children_passed=8,fixtures_per_child=1940,checks_per_child=289060,exact_per_child=86570560,within_build_all_variants_identical=True,cross_build_fixture_lines_identical=1940,different_lines=[dict(line=1941,release=a[-1],sanitize=b[-1])],cause='Unknown; allocator usable sizes and compiler/instrumentation differ between builds. Allocator influence is plausible, not established by this comparison.',no_reruns=True,warning='Renamed original main lacks explicit return; never called. Original oracle unchanged; no runtime UBSan failure.',binaries=binaries)
(P/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
