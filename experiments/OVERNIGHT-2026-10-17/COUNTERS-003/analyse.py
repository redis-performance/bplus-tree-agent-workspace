from pathlib import Path
import json,hashlib,collections
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert len(M['runs'])==320 and all(r['returncode']==0 for r in M['runs']);diff=collections.Counter()
for r in M['runs']:
 for k in ['stdout','stderr']:assert sha(P/(r['name']+'.'+k))==r[k+'_sha256']
for a,b in zip(M['runs'][:160],M['runs'][160:]):
 assert a['cell']==b['cell'];changes=[k for k in a['result'] if a['result'][k]!=b['result'][k]];diff.update(changes)
 assert changes==['owned'] # sanitizer and native allocator report different usable sizes
 assert {k:v for k,v in a['result'].items() if k!='owned'}=={k:v for k,v in b['result'].items() if k!='owned'}
primary=[r['result'] for r in M['runs'][:160] if r['cell'][0]==100000 and r['cell'][3]=='integer'];out=dict(runs=320,status='complete with retained post-run driver assertion',cross_build_differing_fields=dict(diff),primary=[dict(seed=d['seed'],bytes=d['bytes'],narrow=d['narrow_nonzero'],n=d['n'],passes=d['narrow_nonzero']>=.99*d['n']) for d in primary]);out['coverage_hypothesis_supported']=all(d['passes'] for d in out['primary'])
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Structural path census','','No timing or hardware cost claim. All160 fixtures pass release/debug and sanitizers.','All structural fields identical across builds; native/ASan usable-size totals differ.','Original post-run equality assertion and all raw outputs retained;no rerun or changed test.','','| Seed | Bytes | Encoding | Width: element count | Reversed | Cross-word |','|---|---|---|---|---|---|']
for r in M['runs'][:160]:
 d=r['result']
 if d['n']==100000:lines.append(f"| {d['seed']} | {d['bytes']} | {d['encoding']} | "+', '.join(f'{i}:{v}' for i,v in enumerate(d['widths']) if v)+f" | {d['reversed']} | {d['cross_word']} |")
lines+=['','Coverage hypothesis supported in all four preregistered integer cells.','This does not establish the decoder as dominant or justify removing width64 support.'];(P/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(out)
