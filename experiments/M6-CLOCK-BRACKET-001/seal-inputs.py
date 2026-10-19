#!/usr/bin/env python3
"""Freeze published inputs before any native phase, never overwrite an existing seal."""
from pathlib import Path
import hashlib,json
E=Path(__file__).resolve().parent; R=Path.cwd()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=[R/'Makefile',R/'experiments/EXP-009/driver.py',R/'experiments/EXP-009/harness/lookup.c']
for folder in ['src','compat','vendor','bench','tests']:
 paths.extend(p for p in (R/folder).rglob('*') if p.is_file() and p.suffix in ['.c','.h'])
paths.extend(p for p in E.rglob('*') if p.is_file() and p.suffix in ['.py','.json','.md','.c','.h','.patch'] and p.name not in ['inputs.json','STATUS.md'] and '__pycache__' not in p.parts and 'results' not in p.parts)
expected={'src/zset_btree.c':'d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2','src/zset_btree.h':'496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83','compat/server.h':'468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7','compat/standalone.c':'c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3'}
for f,h in expected.items(): assert sha(R/f)==h,f
payload={'status':'SEALED_BEFORE_NATIVE','files_sha256':{str(p.relative_to(R)):sha(p) for p in sorted(set(paths))}}
with (E/'inputs.json').open('x') as f:json.dump(payload,f,indent=2);f.write('\n')
print(json.dumps({'entries':len(payload['files_sha256']),'manifest_sha256':sha(E/'inputs.json')}))
