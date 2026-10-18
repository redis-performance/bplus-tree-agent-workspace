from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-010/base'
F=json.loads((P.parent/'HARNESS-003/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
changes=[('const char *selected = "all";','const char *selected = "all";\n    const char *requested_qos = NULL;'),('else if (!strcmp(arg, "--case")) selected = value;','else if (!strcmp(arg, "--case")) selected = value;\n        else if (!strcmp(arg, "--requested-qos")) requested_qos = value;'),('    uint64_t rng = seed;','''    /* Diagnostic-only intervention; both arms take exactly one setter call. */
    if (requested_qos) {
#if defined(__APPLE__)
        qos_class_t requested;
        if (!strcmp(requested_qos, "user-interactive")) requested=QOS_CLASS_USER_INTERACTIVE;
        else if (!strcmp(requested_qos, "user-initiated")) requested=QOS_CLASS_USER_INITIATED;
        else { fputs("Invalid requested QoS\\n",stderr); return 2; }
        int rc=pthread_set_qos_class_self_np(requested,0);
        if (rc) { fprintf(stderr,"QoS request failed: %d\\n",rc); return 3; }
        int relative=0;
        if (strcmp(qos_reported(&relative),requested_qos) || relative!=0) return 4;
#else
        fputs("Requested QoS unavailable\\n",stderr); return 3;
#endif
    }
    uint64_t rng = seed;''')]
for a,b in changes:assert s.count(a)==1,a;s=s.replace(a,b)
(B/'bench/microbench.c').write_text(s)
(P/'diagnostic.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=sha(P.parent/'HARNESS-003/freeze.json'),provenance='uncommitted diagnostic-only QoS wrapper over HARNESS-003; target/root unchanged',files={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
