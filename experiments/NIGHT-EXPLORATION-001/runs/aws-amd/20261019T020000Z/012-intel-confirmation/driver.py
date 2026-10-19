#!/usr/bin/env python3
"""Independently authored fixed held-out primary schedule; invoke under owned lease."""
import argparse,csv,datetime,hashlib,io,json,pathlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--phase',choices=['aa','confirm'],required=True);p.add_argument('--base',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
here=pathlib.Path(__file__).resolve().parent; expected=json.loads((here/'expected-hashes.json').read_text())
roots={'base':a.base.resolve(),'B':a.candidate.resolve()}
out=a.out;out.mkdir(parents=True,exist_ok=False);raw=out/'raw';raw.mkdir();started=time.monotonic();end_limit=started+300
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
state={'phase':a.phase,'status':'running','started_utc':now(),'processes':[],'source_adoption':'NONE'}
def save():
    tmp=out/'result.tmp';tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(out/'result.json')
def verify():
    got={v:{k:hashlib.sha256((root/k).read_bytes()).hexdigest() for k in expected[v]} for v,root in roots.items()}
    assert got==expected,'source/referee/binary hash mismatch'
    return got
save()
try:
    state['initial_hashes']=verify();save()
    for n in [100000,1000000]:
        for block in range(6):
            seed=201+block%3
            names=['base']*4 if a.phase=='aa' else ['base','B','B','base']
            for position,variant in enumerate(names):
                idx=len(state['processes']);name=f'{idx:03d}';seconds=end_limit-time.monotonic()
                if seconds<=0:raise TimeoutError('fixed total phase cap reached')
                cmd=[str(roots[variant]/'build/btree-bench'),'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)]
                row={'index':idx,'size':n,'block':block,'seed':seed,'position':position,'binary':variant,'started_utc':now(),'argv':['<'+variant+'>/build/btree-bench',*cmd[1:]]}
                state['processes'].append(row);save()
                try:
                    r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(30,seconds))
                    stdout,stderr=r.stdout,r.stderr;row['returncode']=r.returncode
                except subprocess.TimeoutExpired as e:
                    stdout=e.stdout or b'';stderr=e.stderr or b''
                    if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
                    if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
                    row['returncode']=124
                row['finished_utc']=now();(raw/(name+'.stdout')).write_text(stdout);(raw/(name+'.stderr')).write_text(stderr);save()
                assert row['returncode']==0 and not stderr, 'process failure or stderr'
                rows=list(csv.DictReader(io.StringIO(stdout)));assert len(rows)==1
                row['row']=rows[0];save()
    state['final_hashes']=verify();state['status']='complete'
except BaseException as e:
    state['status']='failed';state['failure_type']=type(e).__name__;state['failure']=str(e);raise
finally:
    state['finished_utc']=now();state['wall_seconds']=time.monotonic()-started;save()
