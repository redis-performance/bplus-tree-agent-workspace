import pathlib,json,hashlib,importlib.util,sys,tempfile,datetime,csv,io,copy
p=pathlib.Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
spec=importlib.util.spec_from_file_location('arm_audit',p/'audit.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
_,schedule=m.inputs();assert len(schedule)==48
with tempfile.TemporaryDirectory() as d:
    d=pathlib.Path(d);(d/'raw').mkdir();grant=dict(selected='B',selection_revision='SYNTHETIC-ONLY',root_grant='SYNTHETIC-NO-RUNNER',idle_handoff_utc='2026-10-19T00:00:00+00:00',root_authorized=True);gt=json.dumps(grant)
    x=dict(phase='aa',selected='B',status='complete',wall_seconds=48,driver_affinity=[2],initial_hashes=m.expected('B'),final_hashes=m.expected('B'),input_hashes={n:m.sha(p/n) for n in ['freeze.json','driver.py','audit.py','schedule.json','discovery-freeze.json']},grant=grant,grant_text=gt,grant_sha256=sha(gt.encode()),processes=[])
    for s in schedule:
        z=dict(case='scan',size=str(s['size']),requested_ops='5000000',member_bytes='16',seed=str(s['seed']),operations='5000000',checksum='123',tree_bytes='123456',traversals='50',warmup_passes='1',cpu_start='2',cpu_end='2',elapsed_ns='20000000')
        r=dict(s,binary='base',returncode=0,argv=['<base>/build/btree-bench','--case','scan','--size',str(s['size']),'--ops','5000000','--member-bytes','16','--seed',str(s['seed'])],started_utc=f'2026-10-19T00:00:{s["index"]:02d}+00:00',finished_utc=f'2026-10-19T00:00:{s["index"]:02d}.500000+00:00',row=z)
        x['processes'].append(r)
    def emit(obj):
        for r in obj['processes']:
            b=io.StringIO();w=csv.DictWriter(b,fieldnames=r['row']);w.writeheader();w.writerow(r['row']);op=d/'raw'/f'{r["index"]:03d}.stdout';op.write_text(b.getvalue());ep=op.with_suffix('.stderr');ep.write_bytes(b'');r['stdout_sha256']=m.sha(op);r['stderr_sha256']=m.sha(ep)
        (d/'result.json').write_text(json.dumps(obj))
    checks=[];emit(x);assert m.audit(d)['qualified'];checks.append('synthetic valid control accepted')
    for name,modify,assertion in [
        ('noisy block unqualified',lambda q:q['processes'][1]['row'].update(elapsed_ns='22000000'),False),
        ('short window unqualified',lambda q:q['processes'][0]['row'].update(elapsed_ns='9999999'),False),
        ('CPU mismatch rejected',lambda q:q['processes'][1]['row'].update(cpu_end='3'),True),
        ('checksum mismatch rejected',lambda q:q['processes'][1]['row'].update(checksum='124'),True),
        ('schedule mismatch rejected',lambda q:q['processes'][1].update(seed=999),True),
        ('hash mismatch rejected',lambda q:q['final_hashes']['base'].update({'Makefile':'wrong'}),True)]:
        q=copy.deepcopy(x);modify(q);emit(q)
        try:result=m.audit(d)
        except AssertionError:assert assertion
        else:assert not assertion and not result['qualified']
        checks.append(name)
(p/'LOCAL-CHECKS.json').write_text(json.dumps(dict(scope='Synthetic local audit fixtures only; no runner or held-out benchmark execution',checks=checks),indent=2)+'\n')
print(json.dumps(checks))
