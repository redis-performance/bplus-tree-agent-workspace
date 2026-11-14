import argparse,pathlib,subprocess
p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();r=pathlib.Path(a.root)
for case in ['hit','score','miss']:
 for label,binary in [('base','bin/native/lookup'),('B','bin/H1-B')]:
  subprocess.run(['python3',str(r/'experiments/ARM-LOOKUP-CONT-001/fleet_profile.py'),'--root',str(r),'--output','H1-diagnostic-'+case+'-'+label,'--binary',binary,'--case',case,'--stat-repeats','1'],check=True)
