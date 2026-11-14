import argparse,pathlib,subprocess
p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();r=pathlib.Path(a.root);e=r/'experiments/ARM-LOOKUP-CONT-001'
for cohort in ['native','gcc15-lto']:
 subprocess.run(['python3',str(e/'fleet_intel_profile.py'),'--root',str(r),'--label','profile-'+cohort+'-v2','--binary','bin/'+cohort+'/lookup'],check=True)
for cohort,phase in [('native','H2-native'),('gcc15-lto','H2-lto')]:
 subprocess.run(['python3',str(e/'fleet_compare.py'),'--root',str(r),'--phase',phase,'--cohort',cohort,'--scale','5','--build-only'],check=True)
