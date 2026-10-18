from pathlib import Path
import json,hashlib,shutil,datetime,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'HARNESS-005/freeze.json').read_text());S=R/'scratch/overnight-harness-006/base';assert not S.exists();S.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in F['files'].items():
 src=R/F['snapshot']/n;assert sha(src)==h;dst=S/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
p=S/'bench/iterator_modes.c';original=p.read_text();s=original
pairs=[
(' && strcmp(construction,"descending"))return 2;', ' && strcmp(construction,"descending") && strcmp(construction,"trimmed") && strcmp(construction,"trimmed-clone") && strcmp(construction,"trimmed-cycle"))return 2;'),
('    zbtreeSet *tree=zbtreeCreate();', '''    int trimmed=!strncmp(construction,"trimmed",7);
    unsigned char sentinel_bytes[8];memset(sentinel_bytes,0xff,sizeof sentinel_bytes);
    sds sentinel=trimmed?sdsnewlen(sentinel_bytes,sizeof sentinel_bytes):NULL;
    double sentinel_score=nextafter(model_score(0,n,encoding),-INFINITY);
    serverAssert(isfinite(sentinel_score) && sentinel_score<model_score(0,n,encoding));
    zbtreeSet *tree=zbtreeCreate();
    if(trimmed)insert(tree,sentinel,sentinel_score);'''),
('    verify(tree,keys,n,reverse,mask,encoding);\n    uint64_t warmstart', '''    if(trimmed) {
        zbtreeDeleteEdge(tree,0);serverAssert(zbtreeLength(tree)==n);
        if(!strcmp(construction,"trimmed-clone")) {zbtreeSet *copy=zbtreeDup(tree);zbtreeFree(tree);tree=copy;}
        if(!strcmp(construction,"trimmed-cycle")) {insert(tree,sentinel,sentinel_score);zbtreeDeleteEdge(tree,0);}
        for(const char *p=construction;*p;p++)fingerprint=(fingerprint^(unsigned char)*p)*UINT64_C(1099511628211);
    }
    sdsfree(sentinel);
    verify(tree,keys,n,reverse,mask,encoding);
    uint64_t warmstart''')]
for a,b in pairs:assert s.count(a)==1,a;s=s.replace(a,b)
p.write_text(s);(P/'iterator_modes.c').write_text(s);(P/'harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/iterator_modes.c',tofile='b/bench/iterator_modes.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),provenance='uncommitted separate HARNESS-006 compact history revision',parent_freeze_sha256=sha(P.parent/'HARNESS-005/freeze.json'),files={str(p.relative_to(S)):sha(p) for p in S.rglob('*') if p.is_file()}),indent=2)+'\n')
