set -eu
cd @REPO@
out=scratch/amd-scoped-profile
PROFILE_DISABLE=1 @PERF@ stat -D -1 -x, -e cycles,instructions,branches,branch-misses -o "$out/disabled.stat" -- "$out/base-profile" --case update --size 100000 --ops 100000 --member-bytes 16 --seed 1 > "$out/disabled.csv" 2> "$out/disabled.stderr"
@PERF@ stat -D -1 -x, -e cycles,instructions,branches,branch-misses -o "$out/enabled.stat" -- "$out/base-profile" --case update --size 100000 --ops 100000 --member-bytes 16 --seed 1 > "$out/enabled.csv" 2> "$out/enabled.stderr"
python3 - <<'PY'
import pathlib,json,csv
p=pathlib.Path('scratch/amd-scoped-profile')
def counts(name):
 return {x.split(',')[2]:x.split(',')[0] for x in (p/name).read_text().splitlines() if x and not x.startswith('#')}
a=counts('disabled.stat');b=counts('enabled.stat');assert all(v in ['0','<not counted>'] for v in a.values()),a;assert all(float(v)>0 for v in b.values()),b
r=[list(csv.DictReader((p/name).read_text().splitlines()))[0] for name in ['disabled.csv','enabled.csv']]
assert r[0]['checksum']==r[1]['checksum'] and r[0]['tree_bytes']==r[1]['tree_bytes']
(p/'control.json').write_text(json.dumps(dict(disabled=a,enabled=b,semantic_match=True,status='PASS'),indent=2)+'\n')
PY
