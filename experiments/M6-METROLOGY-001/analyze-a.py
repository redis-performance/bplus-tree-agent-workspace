#!/usr/bin/env python3
"""Independent offline clock decomposition. No workload execution or imports of peers."""
import csv
import hashlib
import io
import json
import signal
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

E = Path(__file__).resolve().parent
W = E.parents[1]
X = W / 'experiments/EXP-009'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pct(n, d):
    return float(Fraction(100 * n, d))

def main():
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('offline analysis bound')))
    signal.alarm(180)
    pins = json.loads((E / 'inputs.json').read_text())
    for p, h in pins['files'].items():
        assert digest(W / p) == h, p
    manifest = json.loads((X / 'bench-results/aa/public-raw-manifest.json').read_text())
    assert len(manifest['streams']) == 96
    hashes = {}
    for stream in manifest['streams']:
        p = W / stream['public']
        assert p.stat().st_size == stream['bytes']
        assert digest(p) == stream['sha256']
        hashes[stream['public']] = digest(p)
    journal = [json.loads(s) for s in (X / 'bench-results/aa/commands.jsonl').read_text().splitlines()]
    declared = json.loads((X / 'bench-results/calibrate/aa-schedule.json').read_text())
    assert len(journal) == len(declared) == 48
    rows, blocks = [], []
    prior_end = None
    for b in range(6):
        seed = b % 3 + 1
        for size in ([100000, 1000000] if b % 2 == 0 else [1000000, 100000]):
            subset = []
            count = {100000: 13834448, 1000000: 4978427}[size]
            for pos, side in enumerate('ABBA'):
                i = len(rows)
                name = f'{i:03d}'
                planned = dict(index=i, block=b, seed=seed, size=size, case='lookup-hit', member_bytes=16,
                               warmup_passes=1, position=pos, side=side, operations=count)
                assert declared[i] == planned
                j = journal[i]
                assert j['name'] == name
                assert j['command'] == ['build/exp009-baseline/native/lookup', '--case', 'lookup-hit',
                    '--size', str(size), '--ops', str(count), '--seed', str(seed), '--member-bytes', '16', '--warmup-passes', '1']
                assert j['returncode'] == 0 and not j['timed_out']
                assert all(j[k] for k in ['child_reaped', 'owned_group_empty', 'release_safe'])
                if prior_end:
                    assert j['started_utc'] >= prior_end
                prior_end = j['finished_utc']
                for kind in ['stdout', 'stderr']:
                    p = X / f'bench-results/aa/raw/{name}.{kind}'
                    assert digest(p) == j['raw'][kind]['sha256']
                    assert p.stat().st_size == j['raw'][kind]['bytes']
                assert not (X / f'bench-results/aa/raw/{name}.stderr').read_bytes()
                records = list(csv.DictReader(io.StringIO((X / f'bench-results/aa/raw/{name}.stdout').read_text())))
                assert len(records) == 1
                r = records[0]
                for key, value in [('size', size), ('seed', seed), ('requested_ops', count), ('operations', count), ('member_bytes',16), ('warmup_passes',1)]:
                    assert int(r[key]) == value
                assert r['case'] == 'lookup-hit'
                wall, thread = int(r['elapsed_ns']), int(r['thread_elapsed_ns'])
                assert wall >= 10000000 and thread > 0
                row = dict(index=i, block=b, seed=seed, size=size, position=pos, side=side,
                           wall_ns=wall, thread_ns=thread, residual_ns=wall-thread,
                           checksum=int(r['checksum']), tree_bytes=int(r['tree_bytes']),
                           cpu_start=int(r['cpu_start']), cpu_end=int(r['cpu_end']))
                rows.append(row)
                subset.append(row)
            assert len({(r['checksum'],r['tree_bytes']) for r in subset}) == 1
            aw, bw = [sum(subset[p]['wall_ns'] for p in positions) for positions in [(0,3),(1,2)]]
            at, bt = [sum(subset[p]['thread_ns'] for p in positions) for positions in [(0,3),(1,2)]]
            dw, dt = bw-aw, bt-at
            dr = dw-dt
            assert Fraction(dw,aw) == Fraction(dt,aw)+Fraction(dr,aw)
            blocks.append(dict(block=b, seed=seed, size=size, indices=[r['index'] for r in subset],
                A_wall_ns=aw, B_wall_ns=bw, A_thread_ns=at, B_thread_ns=bt,
                wall_delta_ns=dw, thread_delta_ns=dt, residual_delta_ns=dr,
                wall_percent=pct(dw,aw), thread_percent=pct(dt,at),
                thread_contribution_wall_pp=pct(dt,aw), residual_contribution_wall_pp=pct(dr,aw),
                signed_residual_share_percent=pct(dr,dw) if dw else None,
                residual_magnitude_share_percent=pct(abs(dr),abs(dw)) if dw else None,
                wall_qualifies=100*abs(dw)<=aw, thread_diagnostic_within_one_percent=100*abs(dt)<=at))
    failed = [b for b in blocks if not b['wall_qualifies']]
    assert len(rows)==48 and len(blocks)==12 and len(failed)==3
    assert all(b['size']==1000000 for b in failed)
    # Shared consultation is actual controller evidence; it is not an own ask.
    consultation = W.parents[1] / 'scratch/cpu-perf-m6-metrology-20261019/consult-calls.jsonl'
    calls = [json.loads(s) for s in consultation.read_text().splitlines()]
    # Store only hashes here: shared raw responses contain private library metadata.
    shared_calls = [{'index':i, 'sha256':hashlib.sha256(json.dumps(c,sort_keys=True).encode()).hexdigest()}
                    for i,c in enumerate(calls)]
    source = X / 'harness/lookup.c'
    text = source.read_text()
    assert text.index('int64_t thread_start = thread_ns();') < text.index('uint64_t start = now_ns();')
    assert text.index('uint64_t elapsed = now_ns() - start;') < text.index('int64_t thread_end = thread_ns();')
    out = dict(status='PASS_OFFLINE_RECONSTRUCTION', generated_utc=datetime.now(timezone.utc).isoformat(),
        participant='/root/followup_proposal_a', backend_family='Codex/GPT-6 inherited',
        exact_model=None, token_cost=None, currency_cost=None,
        independent_authorship='Independent clock analysis; prior EXP009 mapper and raw auditor author. No peer new reviews read.',
        availability={'own_catalog_discovery':'No callable cpu-perf/library_status/ask tools exposed; catalog search returned zero matches.',
          'checked_by_utc':'2026-10-19T11:35:06Z', 'consultation':'Explicitly shared controller stdio consultation, not an own ask.',
          'shared_journal_sha256':digest(consultation),'calls':shared_calls,
          'server':'cpu-perf 0.1.1', 'library_commit':'deb5a0bac467', 'indexed_sources':'0/287',
          'coverage':'Keyword-only, no direct passages matched ask; recommendations unread. LLVM Benchmarking primary source actually fetched.',
          'primary_source':'https://llvm.org/docs/Benchmarking.html'},
        pinned_inputs_verified=pins['files'], raw_streams_sha256=hashes, clock_source_sha256=digest(source),
        script_sha256=digest(Path(__file__)), native_workloads_executed=0,
        row_count=48, block_count=12, rows=rows, blocks=blocks,
        residual_ns_range=[min(r['residual_ns'] for r in rows),max(r['residual_ns'] for r in rows)],
        negative_residual_rows=sum(r['residual_ns']<0 for r in rows),
        failed_wall_blocks=failed,
        failed_wall_blocks_also_failed_thread_diagnostic=sum(not b['thread_diagnostic_within_one_percent'] for b in failed),
        decision='All three failed wall controls also fail the declared thread-clock diagnostic. Recorded residual alone is insufficient; strict causal descheduling-only remains unresolved without a clock/bracket error bound. Wall-clock PARK unchanged.',
        limits=['Residual is algebraic W-T, not exact off-CPU time: thread bracket is wider and clock errors/resolution are not independently calibrated.',
                'No finite physical descheduling bound follows without a bound on clock error/bracket overhead; reported residual shares are recorded-clock decomposition.',
                'No cycles, frequency, DVFS, cache, core type, continuous residency or migration count inferred. No alternative acceptance clock.'])
    (E/'reviews').mkdir(exist_ok=True)
    with (E/'reviews/A.json').open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(json.dumps({'blocks':blocks,'residual_ns_range':out['residual_ns_range'], 'negative_residual_rows':out['negative_residual_rows']},indent=2))
    signal.alarm(0)

if __name__ == '__main__':
    main()
