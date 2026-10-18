from pathlib import Path
import json,hashlib,shutil,datetime,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'HARNESS-004/freeze.json').read_text());S=R/'scratch/overnight-harness-005/base';assert not S.exists();S.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in F['files'].items():
 src=R/F['snapshot']/n;assert sha(src)==h;dst=S/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
p=S/'bench/iterator_modes.c';original=p.read_text();s=original
pairs=[
('static double model_score(', '/* Fold high bits so alternating zero signs do not cancel in an even sum. */\nstatic uint64_t score_checksum(double s) { uint64_t u=score_bits(s); return u ^ (u>>32); }\nstatic double model_score('),
('    if (!strcmp(encoding, "fraction"))','    if (!strcmp(encoding, "alternating-zero")) return i&1 ? -0.0 : 0.0;\n    if (!strcmp(encoding, "fraction"))'),
('sum += score_bits(score);','sum += score_checksum(score);'),
('const char *encoding="integer";', 'const char *encoding="integer",*construction="shuffled";'),
('        else if(!strcmp(a,"--encoding"))encoding=v;', '        else if(!strcmp(a,"--encoding"))encoding=v;\n        else if(!strcmp(a,"--construction"))construction=v;'),
(' && strcmp(encoding,"zero")))return 2;', ' && strcmp(encoding,"zero") && strcmp(encoding,"alternating-zero")))return 2;\n    if(strcmp(construction,"shuffled") && strcmp(construction,"ascending") && strcmp(construction,"descending"))return 2;'),
('buf[j]=(char)((uint64_t)i>>(8*j));', 'buf[j]=(char)((uint64_t)i>>(8*(!strcmp(encoding,"alternating-zero") ? 7-j : j)));'),
('expected+=score_bits(model_score(i,n,encoding));','expected+=score_checksum(model_score(i,n,encoding));'),
('    for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}', '    if(!strcmp(construction,"shuffled")) {\n        for(size_t i=n;i>1;i--){size_t j=random64(&rng)%i,t=order[i-1];order[i-1]=order[j];order[j]=t;}\n    } else if(!strcmp(construction,"descending")) {\n        for(size_t i=0;i<n;i++)order[i]=n-1-i;\n    }'),
('warmup_elapsed_ns,construction_fingerprint");','warmup_elapsed_ns,construction_fingerprint,construction");'),
('PRIu64"\\n",n,ops,count,bytes,seed,','PRIu64",%s\\n",n,ops,count,bytes,seed,'),
('passes,warm,fingerprint);','passes,warm,fingerprint,construction);')]
for a,b in pairs:assert s.count(a)==1,a;s=s.replace(a,b)
p.write_text(s);(P/'iterator_modes.c').write_text(s);(P/'harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/iterator_modes.c',tofile='b/bench/iterator_modes.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),provenance='uncommitted separate HARNESS-005 fixture revision; root/referee and prior snapshots preserved',parent_freeze_sha256=sha(P.parent/'HARNESS-004/freeze.json'),files={str(p.relative_to(S)):sha(p) for p in S.rglob('*') if p.is_file()}),indent=2)+'\n')
