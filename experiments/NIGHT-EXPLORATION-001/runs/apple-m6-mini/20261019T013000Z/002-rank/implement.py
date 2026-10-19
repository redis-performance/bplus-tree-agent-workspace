#!/usr/bin/env python3
"""Three sequential, isolated implementations of the selected rank hypothesis."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,difflib,subprocess
ROOT=Path.cwd();OUT=Path(__file__).resolve().parent
SNAP=Path('scratch/m6-rank/variants')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
old='''        for (unsigned int i = 0; i < node->parent_index; i++)
            rank += parent->child_count[i];'''
choices={
'A':'''        unsigned int index = node->parent_index;
        unsigned int trailing = parent->n.count - index - 1;
        if (index <= trailing) {
            for (unsigned int i = 0; i < index; i++)
                rank += parent->child_count[i];
        } else {
            rank += parent->n.subtree - node->subtree;
            for (unsigned int i = index + 1; i < parent->n.count; i++)
                rank -= parent->child_count[i];
        }''',
'B':'''        unsigned int index = node->parent_index;
        unsigned long sum = 0;
        if (index < (parent->n.count + 1U) / 2U) {
            for (unsigned int i = 0; i < index; i++)
                sum += parent->child_count[i];
            rank += sum;
        } else {
            for (unsigned int i = index + 1; i < parent->n.count; i++)
                sum += parent->child_count[i];
            rank += parent->n.subtree - node->subtree - sum;
        }''',
'C':'''        unsigned int index = node->parent_index;
        int from_right = index > parent->n.count - index - 1U;
        unsigned int first = from_right ? index + 1U : 0U;
        unsigned int end = from_right ? parent->n.count : index;
        unsigned long sum = 0;
        for (unsigned int i = first; i < end; i++)
            sum += parent->child_count[i];
        rank += from_right ? parent->n.subtree - node->subtree - sum : sum;'''}
assert not SNAP.exists();SNAP.mkdir(parents=True)
freeze=json.loads((OUT/'freeze.json').read_text())
for f,h in freeze['files'].items():
 if f.startswith(('src/','compat/','vendor/','bench/','tests/')) or f=='Makefile':assert sha(f)==h,f
source=Path('src/zset_btree.c').read_text();assert source.count(old)==1
manifest=dict(created_utc=datetime.now(timezone.utc).isoformat(),population='Three sequential implementations by one worker; not independent agents',backend='Codex/GPT-6 family; exact model unknown; measured token costs unknown',source_commit='b5ebd930',plan_publication=json.loads(Path('scratch/night-apple-m6-mini-20261019T013000Z/publish-ack.json').read_text()),variants={})
for ident in ['base','A','B','C']:
 dst=SNAP/ident;dst.mkdir()
 for directory in ['src','compat','vendor','bench','tests']:shutil.copytree(directory,dst/directory)
 shutil.copy2('Makefile',dst/'Makefile')
 if ident!='base':
  code=source.replace(old,choices[ident]);(dst/'src/zset_btree.c').write_text(code)
  v=OUT/'variants'/ident;v.mkdir(parents=True)
  (v/'candidate.patch').write_text(''.join(difflib.unified_diff(source.splitlines(True),code.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  descriptions={'A':'Branch-local direct accumulation. Prefix adds to existing rank; suffix subtracts after adding parent minus current subtree.','B':'Separate local sum in each branch; add prefix or parent/current/suffix correction once.','C':'One contiguous span chosen before a shared reduction loop; conditional correction after reduction.'}
  (v/'implementation.md').write_text(f'''# Sequential implementation {ident}\n\n{descriptions[ident]}\n\nOnly zbtScoreRank changes. Same shorter-side hypothesis, no layout, allocator,\nhash, assertion, mutation or API change. Requires parent and current node subtree\ncounts to equal child totals. Existing prefix + inner rank is preserved algebraically.\nUnsigned intermediate is bounded by parent subtree when invariants hold. Risks:\nstale subtree counts after mutation, different vectorization, extra metadata and\nbranch costs. Full upstream and targeted semantic native/sanitizer checks precede\ntiming. One worker, not an independent implementer. Exact model/cost unknown.\n''')
 files={str(f.relative_to(dst)):sha(f) for f in dst.rglob('*') if f.is_file()}
 manifest['variants'][ident]=dict(snapshot=str(dst),files=files,source_sha256=sha(dst/'src/zset_btree.c'),patch_sha256=sha(OUT/'variants'/ident/'candidate.patch') if ident!='base' else None)
base=manifest['variants']['base']['files']
for ident in ['A','B','C']:
 assert all(h==manifest['variants'][ident]['files'][f] for f,h in base.items() if f!='src/zset_btree.c')
(OUT/'implementation-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print({i:manifest['variants'][i]['source_sha256'] for i in manifest['variants']})
