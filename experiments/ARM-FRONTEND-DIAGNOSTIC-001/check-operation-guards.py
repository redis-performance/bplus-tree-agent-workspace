"""Exercise the exact prepared query/release checks with local command stubs only."""
import argparse,json,pathlib,subprocess,hashlib
p=argparse.ArgumentParser();p.add_argument('acquisition_script',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();s=a.acquisition_script.read_text();cases=[]
def run(name,commands,stubs,should_pass):
 q=subprocess.run(['bash','-eu','-o','pipefail','-c',stubs+'\n'+commands+'\necho REACHED_END'],capture_output=True,text=True,timeout=3)
 passed=q.returncode==0 and 'REACHED_END' in q.stdout;assert passed==should_pass,(name,q.returncode,q.stdout,q.stderr)
 cases.append(dict(case=name,exit_code=q.returncode,reached_end=passed,expected_pass=should_pass))
for assignment,fn in [('containers=$(sudo -n docker ps -q)','docker'),('active_units=$(systemctl list-units','systemctl')]:
 line=next(x for x in s.splitlines() if x.startswith(assignment));var=line.split('=')[0];check='test -z "$'+var+'"';assert check in s
 for state,body,allowed in [('empty-success','return 0',True),('nonempty-success','echo occupied; return 0',False),('empty-query-failure','return 7',False)]:
  run(fn+'-'+state,line+'\n'+check,'sudo(){ test "$1" = -n; shift; "$@"; }; '+fn+'(){ '+body+'; }',allowed)
release=s.split("<<'RELEASE'\n",1)[1].split('\nRELEASE\n',1)[0]
lines=release.splitlines();stop=next(x for x in lines if x.startswith('systemctl stop '));query=next(x for x in lines if x.startswith('state=$('));assert 'test "$state" = inactive' in release
release_check='stop_rc=0\n'+stop+'\n'+query+'\ntest "$state" = inactive\necho WOULD_RESTORE'
for name,stop_rc,state_rc,state,allowed in [('inactive',0,0,'inactive',True),('stop-error-inactive-confirmed',5,0,'inactive',True),('active',0,0,'active',False),('state-query-error',0,7,'',False),('stop-and-state-errors',5,7,'',False)]:
 stubs='systemctl(){ if test "$1" = stop; then return '+str(stop_rc)+'; else echo '+repr(state)+'; return '+str(state_rc)+'; fi; }'
 run('release-'+name,release_check,stubs,allowed)
a.out.write_text(json.dumps({'status':'PASS','scope':'Local stub execution of exact prepared query/state checks; no SSH, service mutation or scientific data.','acquisition_script_sha256':hashlib.sha256(s.encode()).hexdigest(),'cases':cases},indent=2)+'\n');print(json.dumps({'status':'PASS','cases':len(cases)}))
