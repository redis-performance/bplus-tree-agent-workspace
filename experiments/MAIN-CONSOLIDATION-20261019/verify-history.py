#!/usr/bin/env python3
"""Verify merged ancestry, exact evidence blobs, and frozen baseline identity."""
import json
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = 'f46efccb3d14f1cf51797b80a4cb92680ea7b39a'
PINS = [
 ('aws-amd', 'f1ffd7e1741a036b8a5de0a6d5d4f430f205ddd2', 'experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z'),
 ('aws-arm', '59ef4391f2a5a5be3eda90c4f6ddfd56e1974c77', 'experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z'),
 ('aws-intel', '16118f4419a1d675f74117ae751ffbd973298de7', 'experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z'),
 ('apple-m6-mini', '85afa6c7b798130452ca9dbd63082337e8bd78b7', 'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z'),
 ('apple-m1', '2baeafcef68a39baabee15c6825f656a10d9b29a', 'experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z'),
 ('apple-m1-lookup-aa', '1d45ec70ced9f242e966b1899006462788ffe56e', 'experiments/EXP-009-M1-AA-001'),
]
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def tree(ref, *paths):
    return {path.decode(): meta.decode() for row in git('ls-tree', '-r', '-z', ref, '--', *paths).split(b'\0') if row for meta, path in [row.split(b'\t', 1)]}
def main():
    head = git('rev-parse', 'HEAD').decode().strip()
    merged = tree(head)
    records = []
    for host, revision, prefix in PINS:
        subprocess.run(['git', 'merge-base', '--is-ancestor', revision, head], cwd=ROOT, check=True)
        source = tree(revision, prefix)
        assert source, host
        mismatches = [path for path, blob in source.items() if merged.get(path) != blob]
        assert not mismatches, (host, mismatches[:20])
        records.append(dict(host=host, revision=revision, evidence_path=prefix, files=len(source), ancestor=True, exact_mode_and_blob=True))
    frozen = tree(BASE, 'src', 'compat', 'vendor', 'Makefile', 'bench', 'tests/upstream.c')
    assert all(merged.get(path) == blob for path, blob in frozen.items()), 'frozen baseline changed'
    snapshots = []
    for manifest in sorted(OUT.glob('*-merge.json')):
        data = json.loads(manifest.read_text())
        for record in data['shared_documents']:
            actual = git('hash-object', record['snapshot']).decode().strip()
            assert actual == record['branch_blob'], record['snapshot']
            snapshots.append(record['snapshot'])
    result = dict(checked_commit=head, baseline_commit=BASE, branches=records,
                  total_evidence_files=sum(row['files'] for row in records),
                  frozen_baseline_files=len(frozen), frozen_baseline_unchanged=True,
                  shared_snapshots_verified=len(snapshots), status='PASS')
    (OUT/'HISTORY-VALIDATION.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()
