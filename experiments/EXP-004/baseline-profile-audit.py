from pathlib import Path
import json,csv,hashlib,collections,re
P=Path(__file__).resolve().parent;R=P.parents[1];D=R/'experiments/EXP-003/profiles';M=json.loads((D/'manifest.json').read_text());S=json.loads((D/'summary.json').read_text());row=next(r for r in M['runs'] if r['name']=='control-m4');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();assert sha(R/row['stderr'])==row['stderr_sha256'];pcs=[r for r in csv.reader((R/row['stderr']).open()) if r[0]=='PC'];data=next(r for r in S if r['name']=='control-m4');addresses=data['symbolization_command'][5:];mapping=dict(zip(addresses,data['symbols']));counts=collections.Counter()
for pc in pcs:
 symbol=mapping.get(pc[2],pc[4]);m=re.search(r'zbtreeIteratorNext .* \+ (\d+)',symbol)
 if m:
  offset=int(m[1]);counts['iterator_total']+=1
  if 336<=offset<500:counts['score_decode_range']+=1
  if 392<=offset<432:counts['cross_word_scaffold_range']+=1
 else:counts['other']+=1
assert sum([counts['iterator_total'],counts['other']])==len(pcs)
a=next(r for r in M['preparation'] if r['name']=='control-assembly');assert sha(R/a['stdout'])==a['stdout_sha256'];text=(R/a['stdout']).read_text();start=text.index('_zbtreeIteratorNext:');end=text.index('\n_',start+1);body=text[start:end];(P/'BASELINE-ASSEMBLY.md').write_text('# Existing control iterator codegen\n\nSource EXP-003 control profile binary; source matches frozen HARNESS-004.\nSample counts descriptive; no unbiased time attribution or cycle claim.\n\n```asm\n'+body+'\n```\n');(P/'baseline-profile-audit.json').write_text(json.dumps(dict(profile_source='experiments/EXP-003/profiles/manifest.json',profile_manifest_sha256=sha(D/'manifest.json'),sample_count=len(pcs),counts=dict(counts),sample_raw_sha256=row['stderr_sha256'],assembly_raw_sha256=a['stdout_sha256'],interpretation='Descriptive interrupted-PC offsets from exact prior control binary; decoder/scaffold observed, not sole bottleneck or quantitative cost attribution.'),indent=2)+'\n');print(counts)
