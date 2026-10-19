#!/usr/bin/env python3
"""Copy non-profile command streams byte for byte into reviewable Git evidence."""
from pathlib import Path
import argparse, hashlib, json, re

parser = argparse.ArgumentParser()
parser.add_argument('phase', choices=['build', 'calibrate', 'aa'])
args = parser.parse_args()
root = Path.cwd()
experiment = Path(__file__).resolve().parent
source = root/'scratch/exp009-driver'/args.phase/'raw'
phase = experiment/'bench-results'/args.phase
state = json.loads((phase/'status.json').read_text())
assert state['status'] != 'RUNNING', 'wait until phase completion or recorded failure'
destination = phase/'raw'
assert not destination.exists(), 'write once; do not replace existing evidence'
streams = sorted(source.iterdir())
assert streams and all(p.suffix in ['.stdout', '.stderr'] for p in streams)
for path in streams:
    content = path.read_bytes()
    assert not re.search(rb'/Users/|/home/|ssh://|BEGIN [A-Z ]*PRIVATE KEY|^PC,', content, re.M), \
        'public evidence review needed; original remains local: '+path.name
destination.mkdir()
manifest = []
for path in streams:
    content = path.read_bytes()
    target = destination/path.name
    with target.open('xb') as out:
        out.write(content)
    assert target.read_bytes() == content
    manifest.append(dict(original=str(path.relative_to(root)),
                         public=str(target.relative_to(root)), bytes=len(content),
                         sha256=hashlib.sha256(content).hexdigest()))
with (phase/'public-raw-manifest.json').open('x') as out:
    json.dump(dict(phase=args.phase, byte_identical=True, streams=manifest), out, indent=2)
    out.write('\n')
print(json.dumps(dict(phase=args.phase, public_streams=len(manifest), byte_identical=True)))
