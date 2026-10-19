#!/usr/bin/env python3
"""One explicitly granted held-out ARM phase; no rebuild, retry or auto-progression."""
import argparse
import csv
import datetime as dt
from decimal import Decimal
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import time

DEADLINE = dt.datetime(2026, 10, 19, 10, 15, tzinfo=dt.timezone.utc)
PREFIX = 'bplus-maskjob-20261019-'
SLICE = 'bplus-mask-20261019.slice'
HERE = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text())

def now():
    return dt.datetime.now(dt.timezone.utc)

def relative(root, name):
    path = (root / name).resolve()
    require(not Path(name).is_absolute() and path.is_relative_to(root), 'artifact outside evidence root')
    return path

def bound_file(root, entry):
    path = relative(root, entry['path'])
    require(sha(path) == entry['sha256'], 'receipt artifact hash mismatch')
    return path

def receipt_artifacts(value):
    if isinstance(value, dict):
        if set(value) >= {'path','sha256'}:
            yield value
        for child in value.values():
            yield from receipt_artifacts(child)
    elif isinstance(value, list):
        for child in value:
            yield from receipt_artifacts(child)

def expected_schedule(phase):
    rows = []
    for block in range(6):
        for size in ((100000, 1000000) if block % 2 == 0 else (1000000, 100000)):
            for position, label in enumerate('ABBA'):
                seed = 1201 + block % 3
                rows.append(dict(ordinal=len(rows), name=f'b{block}-n{size}-p{position}-{label}',
                    block=block, size=size, seed=seed, position=position, label=label,
                    binary='baseline' if phase == 'aa' or label == 'A' else 'historical_candidate_A',
                    argv=['--case','iterate','--size',str(size),'--ops','50000000',
                          '--member-bytes','16','--seed',str(seed)]))
    return rows

def snapshot(roots, identities):
    expected_sources = {
        'baseline': identities['source_hashes'],
        'historical_candidate_A': dict(identities['source_hashes'], **{'src/zset_btree.c': identities['candidate_source_sha256']})}
    result = {}
    for label, root in roots.items():
        sources = {name: sha(root / name) for name in identities['source_hashes']}
        binary = sha(root / 'build/adapter-requalification/btree-bench')
        expected_binary = identities['baseline_binary_sha256'] if label == 'baseline' else identities['candidate_binary_sha256']
        require(sources == expected_sources[label] and binary == expected_binary, 'protected source or binary identity mismatch')
        result[label] = dict(sources=sources, binary_sha256=binary)
    return result

def verify_receipt(receipt, args, freeze_sha, lease_sha, identities):
    require(receipt['kind'] == 'ROOT_REVIEWED_PHASE_GRANT' and receipt['author'] == '/root', 'wrong receipt type/author')
    require(receipt['decision'] == 'ALLOW_CONFIRMATION_PHASE_ONLY', 'receipt is not a phase-only grant')
    require(receipt['phase'] == args.phase and receipt['execution_freeze_sha256'] == freeze_sha, 'phase/freeze not granted')
    require(receipt['protocol_freeze_sha256'] == sha(HERE/'protocol-freeze.json'), 'protocol receipt mismatch')
    require(receipt['lease_sha256'] == lease_sha and receipt['deadline'] == DEADLINE.isoformat(), 'lease receipt mismatch')
    require(receipt['baseline_binary_sha256'] == identities['baseline_binary_sha256'], 'receipt baseline mismatch')
    require(receipt['candidate_binary_sha256'] == identities['candidate_binary_sha256'], 'receipt candidate mismatch')
    require(receipt['idle_handoff']['verified'] is True and receipt['idle_handoff']['owner'] == '/root/aws_intel', 'no explicit idle handoff')
    bound_file(args.evidence_root, receipt['idle_handoff']['evidence'])
    require(receipt['new_seed_ranges']['confirmation'] == [1201,1202,1203], 'wrong held-out seeds')
    for key in ('discovery','guard','profile','correctness'):
        require(not set(receipt['new_seed_ranges'][key]) & {1201,1202,1203}, 'held-out seed overlap')
    inventory_path = bound_file(args.evidence_root, receipt['required_guard_inventory'])
    require(sha(inventory_path) == receipt['required_guard_inventory_sha256'], 'required guard inventory mismatch')
    inventory = read(inventory_path)
    ids = inventory['required_cell_ids']
    require(ids and len(ids) == len(set(ids)), 'empty or duplicate required guard inventory')
    require(isinstance(inventory['coverage_only_diagnostics'], list) and isinstance(inventory['coverage_disclosures'], list), 'missing coverage disclosures')
    require(receipt['coverage_disclosures'] == inventory['coverage_disclosures'], 'coverage disclosures changed')
    cells = receipt['required_guard_results']
    require(set(cells) == set(ids), 'required guard cells missing or altered')
    for cell in cells.values():
        require(cell == {'qualified':True,'guard_pass':True,'memory_pass':True}, 'required guard did not pass')
    keys = ('correctness','guard_aa','guard_comparison','primary_aa','discovery','coverage_review','root_driver_review','amd_driver_review')
    require(set(receipt['prerequisites']) == set(keys), 'prerequisite set differs')
    for key in keys:
        item = receipt['prerequisites'][key]
        require(item['status'] == 'PASS' and item['evidence'], 'unmet prerequisite '+key)
        for artifact in item['evidence']:
            bound_file(args.evidence_root, artifact)
    if args.phase == 'confirmation':
        aa = receipt['heldout_aa']
        audit_path = bound_file(args.evidence_root, aa['independent_audit'])
        result_path = bound_file(args.evidence_root, aa['result'])
        audit, result = read(audit_path), read(result_path)
        require(audit['status'] == 'PASS' and audit['phase'] == 'aa' and audit['gate_pass'] is True, 'held-out AA audit failed')
        require(audit['raw_rows'] == 48 and audit['blocks'] == 12, 'incomplete held-out AA audit')
        require(audit['result_sha256'] == sha(result_path) and audit['execution_freeze_sha256'] == freeze_sha, 'AA audit provenance mismatch')
        require(result['status'] == 'complete' and result['gate_pass'] is True and result['phase'] == 'aa', 'held-out AA result failed')
        require(len(result['runs']) == 48 and result['execution_freeze_sha256'] == freeze_sha, 'AA result incomplete')
        for artifact in aa['raw_files']:
            bound_file(args.evidence_root, artifact)
        expected = {run['name']+'.'+suffix for run in result['runs'] for suffix in ('csv','stderr')}
        actual = {Path(x['path']).name for x in aa['raw_files']}
        require(len(aa['raw_files']) == 96 and actual == expected, 'AA raw file receipt incomplete')
        return {(run['size'],run['seed']):run['row']['tree_bytes'] for run in result['runs']}
    require('heldout_aa' not in receipt, 'unexpected earlier held-out AA reuse')
    return {}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--phase',choices=['aa','confirmation'],required=True)
    for name in ('lease','baseline-root','candidate-root','evidence-root','receipt','output'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--receipt-sha256',required=True)
    args=p.parse_args()
    for name in ('lease','baseline_root','candidate_root','evidence_root','receipt','output'):
        setattr(args,name,getattr(args,name).resolve())
    started=now(); monotonic_start=time.monotonic()
    require((DEADLINE-started).total_seconds() >= 320, 'full phase plus handback margin cannot fit deadline')
    lease=read(args.lease)
    require(dt.datetime.fromisoformat(lease['deadline']) == DEADLINE and lease['cpu'] == 2, 'wrong lease deadline/CPU')
    require(lease['unit_prefix'] == PREFIX and lease['slice'] == SLICE, 'wrong lease campaign')
    require(not (args.lease.parent/'LEASE-RELEASED').exists(), 'lease already released')
    require(args.output.is_relative_to(Path(lease['root']).resolve()), 'output outside leased root')
    require(sorted(os.sched_getaffinity(0)) == [2], 'affinity must be CPU2 only')
    cgroup=Path('/proc/self/cgroup').read_text()
    require('/'+SLICE+'/' in cgroup and PREFIX in cgroup, 'not inside new owned helper cgroup')
    args.output.mkdir()  # Existing output is an attempt marker: never overwrite/retry.
    state=dict(status='preflight',phase=args.phase,started_utc=started.isoformat(),runs=[])
    def save():
        target=args.output/'result.json'; tmp=args.output/'result.json.tmp'
        tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(target)
    save()
    roots={'baseline':args.baseline_root,'historical_candidate_A':args.candidate_root}
    identities=None
    receipt=None
    try:
        freeze=read(HERE/'execution-freeze.json');freeze_sha=sha(HERE/'execution-freeze.json')
        for name,digest in freeze['files'].items():
            require(sha(relative(HERE,name)) == digest, 'execution input mismatch')
        require(freeze['phase_cap_seconds'] == 300 and freeze['child_cap_seconds'] == 30, 'wrong frozen cap')
        identities=read(HERE/'identities.json')
        schedule=read(HERE/(args.phase+'-schedule.json'))
        require(schedule == expected_schedule(args.phase), 'schedule differs from fixed protocol')
        require(sha(args.receipt) == args.receipt_sha256, 'receipt does not match explicitly granted hash')
        receipt=read(args.receipt)
        aa_memory=verify_receipt(receipt,args,freeze_sha,sha(args.lease),identities)
        state.update(execution_freeze_sha256=freeze_sha,receipt_sha256=args.receipt_sha256,
                     lease_sha256=sha(args.lease),deadline=DEADLINE.isoformat(),before=snapshot(roots,identities),status='running')
        state['receipt_artifacts']={entry['path']:entry['sha256'] for entry in receipt_artifacts(receipt)}
        save();seen_memory=dict(aa_memory)
        for entry in schedule:
            left=min(300-(time.monotonic()-monotonic_start),(DEADLINE-now()).total_seconds()-10)
            require(left > 0 and not (args.lease.parent/'LEASE-RELEASED').exists(), 'phase/lease budget exhausted')
            require(sorted(os.sched_getaffinity(0)) == [2], 'affinity changed')
            rec=dict(entry,started_utc=now().isoformat(),command=['<'+entry['binary']+'>/build/adapter-requalification/btree-bench',*entry['argv']])
            state['runs'].append(rec);save()
            binary=roots[entry['binary']]/'build/adapter-requalification/btree-bench'
            try:
                run=subprocess.run([str(binary),*entry['argv']],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=min(30,left),check=False)
                out,err,code=run.stdout,run.stderr,run.returncode
            except subprocess.TimeoutExpired as exc:
                out,err,code=exc.stdout or b'',exc.stderr or b'',124
            rec.update(finished_utc=now().isoformat(),returncode=code)
            (args.output/(entry['name']+'.csv')).write_bytes(out)
            (args.output/(entry['name']+'.stderr')).write_bytes(err)
            save();require(code == 0, 'benchmark child failed or timed out')
            rows=list(csv.DictReader(io.StringIO(out.decode())))
            require(len(rows) == 1, 'expected exactly one CSV row')
            row=rows[0]; n=entry['size']
            exact=dict(case='iterate',size=n,seed=entry['seed'],requested_ops=50000000,operations=50000000,member_bytes=16,
                       traversals=50000000//n,checksum=50000000*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
            require(all(row.get(k)==str(v) for k,v in exact.items()), 'row semantic/CPU/fixture mismatch')
            require(int(row['elapsed_ns']) > 0 and int(row['tree_bytes']) > 0, 'invalid elapsed or owned memory')
            key=(n,entry['seed']);require(key not in seen_memory or seen_memory[key]==row['tree_bytes'], 'owned memory changed')
            seen_memory[key]=row['tree_bytes'];rec['row']=row;save()
        effects=[]
        for offset in range(0,48,4):
            block=state['runs'][offset:offset+4]; times=[int(r['row']['elapsed_ns']) for r in block]
            effect=Decimal(100)*(Decimal(times[1]+times[2])/Decimal(times[0]+times[3])-1)
            passed=min(times)>=10000000 and (abs(effect)<=1 if args.phase=='aa' else effect<=-2)
            effects.append(dict(size=block[0]['size'],block=block[0]['block'],seed=block[0]['seed'],effect_pct_decimal=str(effect),minimum_window_ns=min(times),pass_gate=passed))
        state.update(status='complete',effects=effects,gate_pass=all(e['pass_gate'] for e in effects))
    except BaseException as exc:
        state.update(status='failed',gate_pass=False,error_type=type(exc).__name__,error=str(exc))
        raise
    finally:
        if identities is not None:
            try:
                for name,digest in freeze['files'].items():
                    require(sha(relative(HERE,name)) == digest, 'post-phase execution input mismatch')
                require(sha(HERE/'execution-freeze.json') == freeze_sha, 'execution freeze changed')
                require(sha(args.receipt) == args.receipt_sha256, 'phase receipt changed')
                require(sha(args.lease) == state.get('lease_sha256'), 'lease identity changed')
                if receipt is not None:
                    for artifact in receipt_artifacts(receipt):
                        bound_file(args.evidence_root,artifact)
                state['after']=snapshot(roots,identities)
                require(state.get('before') == state['after'], 'post-phase identity differs')
            except BaseException as exc:
                state.update(status='failed',gate_pass=False,post_identity_error=type(exc).__name__+': '+str(exc))
        state.update(finished_utc=now().isoformat(),elapsed_seconds=time.monotonic()-monotonic_start)
        if state['elapsed_seconds'] > 300 or now() >= DEADLINE:
            state.update(status='failed',gate_pass=False,budget_exceeded=True)
        save()
    return 0 if state['status']=='complete' and state['gate_pass'] else 2

if __name__=='__main__':
    raise SystemExit(main())
