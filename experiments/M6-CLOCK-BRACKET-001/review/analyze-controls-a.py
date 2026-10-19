#!/usr/bin/env python3
"""Offline, loss-preserving validation of the fixed 72-row clock controls."""
import argparse
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

HEADER = 'control,repetition,iterations,requested_block_ns,sleep_wall_ns,sleep_interruptions,checksum,w0_ns,t0_ns,w1_ns,w2_ns,t1_ns,w3_ns,wall_resolution_ns,thread_resolution_ns'.split(',')
MASK = (1 << 64) - 1

def affine_lcg(n, seed=1, a=1664525, c=1013904223):
    """Compose f(x)=a*x+c by exponentiation, independently of the C loop."""
    mul, add = 1, 0
    while n:
        if n & 1:
            mul, add = a * mul & MASK, (a * add + c) & MASK
        a, c = a * a & MASK, (a * c + c) & MASK
        n >>= 1
    return (mul * seed + add) & MASK

def analyze(raw):
    result = dict(status='FAIL', sensitivity_status='FAIL', physical_attribution='UNVALIDATED',
        zero_error_model_status='INCONCLUSIVE_INVALID_ROWS',model_inconsistency_count=0,
        input_sha256=hashlib.sha256(raw).hexdigest(),
        input_bytes=len(raw), expected_rows=72, expected_cpu_checksum=affine_lcg(2000000), rows=[], errors=[],
        model={'I':'w2-w1', 'T':'t1-t0', 'M':'(w1-w0)+(w3-w2)',
          'conditional_cpu_interval':'[max(0,T-M),min(T,I)]',
          'conditional_off_cpu_interval':'[I-min(T,I),I-max(0,T-M)]',
          'assumptions':'Zero clock/accounting error; CPU cannot exceed enclosing wall margins or body wall. These assumptions are not experimentally established.',
          'unknown_accuracy':'Nominal clock resolution and empirical controls do not bound worst-case accuracy/accounting lag. No validated physical CPU/off-CPU interval follows.'})
    def error(message):
        result['errors'].append(message)
    try:
        text = raw.decode('utf-8', errors='strict')
        parsed = list(csv.reader(io.StringIO(text), strict=True))
    except (UnicodeError, csv.Error) as ex:
        error('CSV decoding/parsing failed: '+str(ex))
        return result
    # Preserve every parsed cell even if header, count, or numeric validation fails.
    result['raw_records'] = parsed
    if not parsed or parsed[0] != HEADER:
        error('Header must exactly match the frozen control schema')
        return result
    records = parsed[1:]
    result['actual_rows'] = len(records)
    if len(records) != 72:
        error('Expected exactly 72 rows; no rows excluded')
    prior_w, prior_t = None, None
    for index, values in enumerate(records):
        row = dict(index=index, raw=values, errors=[])
        result['rows'].append(row)
        def fail(message):
            row['errors'].append(message)
        if len(values) != len(HEADER):
            fail('Wrong field count')
            continue
        d = dict(zip(HEADER, values))
        row['control'] = d['control']
        nums = {}
        for key in HEADER[1:]:
            v = d[key]
            if not re.fullmatch(r'[0-9]+', v, flags=re.ASCII):
                fail('Invalid unsigned integer: '+key)
                continue
            n = int(v)
            limit = (1 << 63)-1 if key in ('t0_ns','t1_ns') else MASK
            if n > limit:
                fail('Integer out of frozen C range: '+key)
            nums[key] = n
        if row['errors']:
            continue
        row['observations'] = nums
        kind = ('empty','cpu','block')[index % 3]
        if d['control'] != kind or nums['repetition'] != index // 3:
            fail('Fixed empty/cpu/block repetition order mismatch')
        expected = dict(iterations=2000000 if kind=='cpu' else 0,
            requested_block_ns=20000000 if kind=='block' else 0,
            checksum=affine_lcg(2000000) if kind=='cpu' else 1)
        for key, value in expected.items():
            if nums[key] != value:
                fail('Exact fixture/output mismatch: '+key)
        w0,w1,w2,w3 = [nums[k] for k in ('w0_ns','w1_ns','w2_ns','w3_ns')]
        t0,t1 = nums['t0_ns'],nums['t1_ns']
        ordered = w0<=w1<=w2<=w3 and t0<=t1
        if not ordered:
            fail('Nonmonotonic clock ordering within a clock domain')
        if prior_w is not None and (w0 < prior_w or t0 < prior_t):
            fail('Nonmonotonic same-process successive bracket clocks')
        prior_w,prior_t = w3,t1
        if nums['wall_resolution_ns'] == 0 or nums['thread_resolution_ns'] == 0:
            fail('Nominal resolution must be positive; it is not an accuracy bound')
        if not ordered:
            continue
        I,T,M = w2-w1,t1-t0,(w1-w0)+(w3-w2)
        L,U = max(0,T-M),min(T,I)
        row.update(inner_wall_ns=I, thread_ns=T, margin_wall_ns=M, recorded_residual_ns=I-T,
                   conditional_cpu_lower_ns=L,conditional_cpu_upper_ns=U,
                   conditional_interval_nonempty=L<=U)
        if L>U:
            row['model_note']='Empty zero-error conditional interval: model INCONCLUSIVE; not a structural/sensitivity failure'
        else:
            row.update(conditional_off_cpu_lower_ns=I-U,conditional_off_cpu_upper_ns=I-L)
        if kind=='block':
            if nums['sleep_wall_ns'] < 20000000:
                fail('Blocking sleep wall below 20ms')
            if nums['sleep_wall_ns'] > I:
                fail('Independent sleep wall exceeds enclosing body wall')
            if I-T < 18000000:
                fail('Recorded blocking residual below 18ms')
        elif nums['sleep_wall_ns'] != 0 or nums['sleep_interruptions'] != 0:
            fail('Nonblocking control reports sleep metadata')
    result['failed_row_indices'] = [r['index'] for r in result['rows'] if r['errors']]
    result['all_zero_error_intervals_nonempty'] = len(result['rows'])==72 and all(r.get('conditional_interval_nonempty',False) for r in result['rows'])
    result['model_inconsistency_count'] = sum(r.get('conditional_interval_nonempty') is False for r in result['rows'])
    result['zero_error_model_status'] = 'INCONCLUSIVE' if result['model_inconsistency_count'] else 'NOT_FALSIFIED_BY_RECORDED_INTERVALS'
    if any('conditional_interval_nonempty' not in r for r in result['rows']):
        result['zero_error_model_status']='INCONCLUSIVE_INVALID_ROWS'
    result['observed_control_counts'] = {k:sum(r.get('control')==k for r in result['rows']) for k in ('empty','cpu','block')}
    if result['observed_control_counts'] != {'empty':24,'cpu':24,'block':24}:
        error('Expected 24 observations of each control')
    if not result['errors'] and not result['failed_row_indices']:
        result['status']='PASS_EMPIRICAL_SENSITIVITY'
    result['sensitivity_status']='PASS' if result['status'].startswith('PASS') else 'FAIL'
    return result

def synthetic_fixture():
    records=[HEADER]
    wall,thread=1000000000,1000  # Distinct clock epochs: never compare cross-clock values.
    for repetition in range(24):
        for kind in ('empty','cpu','block'):
            I,T = {'empty':(100,150),'cpu':(1000000,900000),'block':(20100000,100000)}[kind]
            records.append([kind,repetition,2000000 if kind=='cpu' else 0,20000000 if kind=='block' else 0,
                20000000 if kind=='block' else 0,0,affine_lcg(2000000) if kind=='cpu' else 1,
                wall,thread,wall+50,wall+50+I,thread+T,wall+100+I,1,1])
            wall+=I+1000
            thread+=T+100
    return records

def encode(records):
    stream=io.StringIO()
    csv.writer(stream,lineterminator='\n').writerows(records)
    return stream.getvalue().encode()

def self_test():
    cases=[]
    # An independent direct recurrence at small cardinalities checks composition order and modulo wrap.
    for n in (0,1,2,7,64,1001):
        value=1
        for _ in range(n):
            value=(value*1664525+1013904223)&MASK
        assert affine_lcg(n)==value
    base=synthetic_fixture()
    def check(name,records,expect_pass):
        r=analyze(encode(records))
        ok=(r['status']=='PASS_EMPIRICAL_SENSITIVITY')==expect_pass
        if name=='empty_conditional_interval':
            ok=ok and r['model_inconsistency_count']==1 and r['zero_error_model_status']=='INCONCLUSIVE'
        cases.append(dict(name=name,passed=ok,expected_pass=expect_pass,analysis=r))
    check('valid_distinct_clock_epochs',base,True)
    def changed(row,key,value):
        clone=[r[:] for r in base]
        clone[row][HEADER.index(key)]=value
        return clone
    check('wrong_lcg_checksum',changed(2,'checksum',0),False)
    check('sleep_too_short',changed(3,'sleep_wall_ns',19999999),False)
    check('residual_too_small',changed(3,'t1_ns',int(base[3][HEADER.index('t0_ns')])+3000000),False)
    check('nonmonotonic_wall',changed(1,'w2_ns',0),False)
    check('empty_conditional_interval',changed(1,'t1_ns',int(base[1][HEADER.index('t0_ns')])+201),True)
    check('malformed_integer',changed(2,'iterations','2e6'),False)
    check('wrong_schedule',changed(4,'repetition',99),False)
    check('missing_row',base[:-1],False)
    check('extra_row',base+[base[-1]],False)
    broken=[r[:] for r in base]
    broken[0][0]='wrong'
    check('wrong_header',broken,False)
    return dict(status='PASS' if all(c['passed'] for c in cases) else 'FAIL',synthetic_only=True,
                native_processes_executed=0,affine_small_recurrence_checks=6,cases=cases)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.self_test == bool(args.input):
        parser.error('Choose exactly one of --input and --self-test')
    if args.output.exists():
        parser.error('Output already exists; no overwrite permitted')
    result=self_test() if args.self_test else analyze(args.input.read_bytes())
    result['analyzer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['participant']='/root/followup_proposal_a'
    result['backend']='Inherited Codex/GPT-6 family; exact model/token/currency unknown'
    # Exclusive creation protects even against an exists/open race.
    with args.output.open('x') as handle:
        json.dump(result,handle,indent=2)
        handle.write('\n')
    return 0 if result['status'].startswith('PASS') else 1

if __name__=='__main__':
    sys.exit(main())
