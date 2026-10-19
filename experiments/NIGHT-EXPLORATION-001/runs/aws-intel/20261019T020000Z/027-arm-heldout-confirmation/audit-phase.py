#!/usr/bin/env python3
"""Independent raw-file reconstruction; imports no execution-driver code."""
import argparse
import csv
import datetime
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def check(value,description):
    if not value: raise ValueError(description)
def timestamp(value): return datetime.datetime.fromisoformat(value)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',required=True,type=Path)
    p.add_argument('--phase',required=True,choices=['aa','confirmation'])
    p.add_argument('--aa-directory',type=Path)
    a=p.parse_args();result_path=a.directory/'result.json';result=json.loads(result_path.read_text())
    identities=json.loads((HERE/'identities.json').read_text())
    check(result['phase']==a.phase and result['status']=='complete','phase did not complete')
    check(result['execution_freeze_sha256']==digest(HERE/'execution-freeze.json'),'execution freeze mismatch')
    check(len(result['runs'])==48,'incomplete run count')
    start=timestamp(result['started_utc']);end=timestamp(result['finished_utc'])
    check(0 < (end-start).total_seconds() <= 300 and 0 < result['elapsed_seconds'] <= 300,'phase cap exceeded')
    check(end < datetime.datetime(2026,10,19,10,15,tzinfo=datetime.timezone.utc),'lease deadline exceeded')
    check(result['before']==result['after'],'before/after differs')
    for label,binary in [('baseline',identities['baseline_binary_sha256']),('historical_candidate_A',identities['candidate_binary_sha256'])]:
        expected=dict(identities['source_hashes'])
        if label!='baseline':expected['src/zset_btree.c']=identities['candidate_source_sha256']
        check(result['before'][label]=={'sources':expected,'binary_sha256':binary},'protected artifact mismatch')
    memory={};raw={};effects=[];previous=start;index=0
    if a.phase=='confirmation':
        check(a.aa_directory is not None,'confirmation requires preceding raw AA directory')
        aa=json.loads((a.aa_directory/'result.json').read_text());aa_audit=json.loads((a.aa_directory/'independent-audit.json').read_text())
        check(aa_audit['status']=='PASS' and aa_audit['gate_pass'] and aa_audit['result_sha256']==digest(a.aa_directory/'result.json'),'AA not qualified by bound independent audit')
        check(timestamp(aa['finished_utc']) < start,'AA not earlier than confirmation')
        for old in aa['runs']:
            record,=csv.DictReader(io.StringIO((a.aa_directory/(old['name']+'.csv')).read_text()))
            check(record==old['row'],'AA CSV altered')
            memory[(old['size'],old['seed'])]=record['tree_bytes']
    for block in range(6):
        sizes=[100000,1000000] if block%2==0 else [1000000,100000]
        for size in sizes:
            seed=1201+block%3;times=[]
            for position,label in enumerate(['A','B','B','A']):
                item=result['runs'][index];binary='baseline' if a.phase=='aa' or label=='A' else 'historical_candidate_A'
                expected=dict(ordinal=index,name=f'b{block}-n{size}-p{position}-{label}',block=block,size=size,seed=seed,position=position,label=label,binary=binary,
                    argv=['--case','iterate','--size',str(size),'--ops','50000000','--member-bytes','16','--seed',str(seed)])
                for key,value in expected.items():check(item[key]==value,'schedule mismatch '+key)
                check(item['command']==['<'+binary+'>/build/adapter-requalification/btree-bench',*expected['argv']],'command mismatch')
                begin,finish=timestamp(item['started_utc']),timestamp(item['finished_utc'])
                check(previous <= begin <= finish <= end,'nonserial timestamps');previous=finish
                check(item['returncode']==0,'child nonzero')
                for suffix in ('csv','stderr'):
                    file=a.directory/(item['name']+'.'+suffix);raw[file.name]=digest(file)
                row,=csv.DictReader(io.StringIO((a.directory/(item['name']+'.csv')).read_text()))
                check(row==item['row'],'raw/record mismatch')
                required={'case':'iterate','size':str(size),'seed':str(seed),'requested_ops':'50000000','operations':'50000000','member_bytes':'16','traversals':str(50000000//size),'checksum':str(50000000*(size-1)//2),'warmup_passes':'1','cpu_start':'2','cpu_end':'2'}
                check(all(row[k]==v for k,v in required.items()),'semantic/CPU mismatch')
                key=(size,seed);check(key not in memory or memory[key]==row['tree_bytes'],'owned-memory mismatch')
                check(int(row['tree_bytes'])>0,'invalid owned bytes');memory[key]=row['tree_bytes']
                times.append(int(row['elapsed_ns']));index+=1
            value=Decimal(100)*(Decimal(times[1]+times[2])/Decimal(times[0]+times[3])-1)
            passed=min(times)>=10000000 and (abs(value)<=1 if a.phase=='aa' else value<=-2)
            effects.append(dict(size=size,block=block,seed=seed,effect_pct_decimal=str(value),minimum_window_ns=min(times),pass_gate=passed))
    check(effects==result['effects'],'summary effects mismatch')
    gate=all(e['pass_gate'] for e in effects);check(gate==result['gate_pass'],'gate mismatch')
    report=dict(status='PASS',phase=a.phase,gate_pass=gate,raw_rows=48,blocks=12,effects=effects,
        result_sha256=digest(result_path),execution_freeze_sha256=result['execution_freeze_sha256'],raw_file_sha256=raw,
        limits=['Local raw reconstruction only; no new live source/binary inspection.','No producer driver code imported.','Primary confirmation does not establish acceptance or causal instruction savings.'])
    (a.directory/'independent-audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'PASS','phase':a.phase,'gate_pass':gate,'rows':48,'blocks':12}))
    return 0 if gate else 2

if __name__=='__main__':raise SystemExit(main())
