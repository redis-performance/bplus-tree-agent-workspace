import argparse,pathlib,subprocess
p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();r=pathlib.Path(a.root);e=r/'experiments/ARM-LOOKUP-CONT-001'
for cohort in ['native','gcc15-lto']:
 cmd=['python3',str(e/'fleet_intel_profile.py'),'--root',str(r),'--label','profile-'+cohort+'-v3','--binary','bin/'+cohort+'/lookup']
 if cohort=='native':cmd+=['--start-rep','1','--resume-from','profile-native-v2']
 subprocess.run(cmd,check=True)
for cohort,phase in [('native','H2-native'),('gcc15-lto','H2-lto')]:
 subprocess.run(['python3',str(e/'fleet_compare.py'),'--root',str(r),'--phase',phase,'--cohort',cohort,'--scale','5','--build-only'],check=True)
