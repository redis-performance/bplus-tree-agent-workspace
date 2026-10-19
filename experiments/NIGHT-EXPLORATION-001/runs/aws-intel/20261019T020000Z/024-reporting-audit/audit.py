"""Reporting audit: immutable metadata, exact patch context and summary arithmetic only."""
import collections,hashlib,json,re,subprocess,posixpath
from pathlib import Path
REV='fd4b5d2cb';ROOT='experiments/NIGHT-EXPLORATION-001/';CHART=ROOT+'corrected-adapter-charts/'
inputs={}
def read(rev,path):
    data=subprocess.check_output(['git','show',rev+':'+path]);inputs[rev+':'+path]=hashlib.sha256(data).hexdigest();return data
def obj(path):return json.loads(read(REV,path))
def check_context(patch):
    """Match every original hunk line at its declared baseline position; no source writes."""
    lines=patch.decode().splitlines(keepends=True);i=0;source=None;hunks=0;errors=[]
    while i<len(lines):
        line=lines[i]
        if line.startswith('--- '):
            path=line[4:].strip().split('\t')[0]
            assert path.startswith('a/'),path
            source=read('13e459ff8800be3f02b6b45c87dd7b0c39453fa9',path[2:]).decode().splitlines(keepends=True)
        if line.startswith('@@ '):
            m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',line);assert m,line
            start=int(m[1]);count=int(m[2] or 1);newcount=int(m[4] or 1);old=[];new=[];i+=1
            while i<len(lines) and lines[i][:1] in [' ','+','-'] and not lines[i].startswith(('--- ','+++ ')):
                ln=lines[i]
                if ln[0] in ' -':old.append(ln[1:])
                if ln[0] in ' +':new.append(ln[1:])
                i+=1
            assert len(old)==count and len(new)==newcount
            if source[start-1:start-1+count]!=old:errors.append({'old_start':start,'old_count':count,'reason':'exact baseline context mismatch'})
            hunks+=1;continue
        i+=1
    assert hunks
    return {'hunks':hunks,'exact_public_context_matches':not errors,'errors':errors}
idx=obj(ROOT+'AWS-PATCH-INDEX.json');md=read(REV,ROOT+'AWS-PATCH-INDEX.md').decode();pop={};patches=[]
for r in idx['records']:
    key=(r['architecture'],r['population']);pop.setdefault(key,[]).append(r)
    data=read(r['evidence_revision'],r['path']);assert hashlib.sha256(data).hexdigest()==r['patch_sha256']
    link='https://github.com/redis-performance/bplus-tree-agent-workspace/blob/'+r['evidence_revision']+'/'+r['path'];assert link in md
    result=check_context(data);assert result['exact_public_context_matches']==r['applies_to_unchanged_public_tree'],(r,result)
    patches.append(dict(architecture=r['architecture'],population=r['population'],variant=r['variant'],sha256=r['patch_sha256'],**result))
for rows in pop.values():assert sorted(r['variant'] for r in rows)==list('ABC') and len({r['decision'] for r in rows})==1
decisions=collections.Counter(rows[0]['decision'] for rows in pop.values());assert decisions=={'REJECT':5,'PARK':3}
assert len(pop)==idx['populations']==8 and len(patches)==idx['patch_records']==24
assert len({r['sha256'] for r in patches})==idx['distinct_patch_hashes']==24
assert sum(r['exact_public_context_matches'] for r in patches)==idx['public_tree_apply_checks']==21
assert sum(not r['exact_public_context_matches'] for r in patches)==idx['private_augmented_control_records']==3
sources=obj(CHART+'sources.json');parity=obj(CHART+'source-parity.json');validation=obj(CHART+'chart-validation.json');chartreadme=read(REV,CHART+'README.md').decode();hosts={};allcells=0
for host in sources['hosts']:
    raw=read(REV,CHART+host['file']);source=read(host['source_commit'],host['source_path']);assert raw==source and hashlib.sha256(raw).hexdigest()==host['sha256'];cells=json.loads(raw)
    assert len(cells)==40 and len({(r['size'],r['case']) for r in cells})==40
    qualified=short=noisy=0
    for row in cells:
        assert row['observations']==24 and len(row['aa_block_effects_pct'])==6
        assert row['aa_max_abs_pct']==max(abs(v) for v in row['aa_block_effects_pct'])
        if row['shortest_timed_ms']<10:short+=1
        elif row['aa_max_abs_pct']>1:noisy+=1
        else:qualified+=1
    assert qualified==host['qualified_cells'] and short==host['short_cells']
    line=f"| {host['label']} | {qualified}/40 | {short}/40 | {noisy}/40 |";assert line in chartreadme
    ap=posixpath.normpath(CHART+host['independent_audit']);read(REV,ap)
    hosts[host['host']]={'cells':40,'observations':960,'qualified':qualified,'short':short,'other_noisy':noisy,'source_summary_identical':True}
    allcells+=len(cells)
assert allcells==validation['cells']==160 and validation['observations_per_cell']==24
for host in parity['hosts']:
    for path,sha in host['source_hashes'].items():assert hashlib.sha256(read(host['source_commit'],path)).hexdigest()==sha
for path,sha in parity['identical_files'].items():assert {h['source_hashes'][path] for h in parity['hosts']}=={sha}
assert hashlib.sha256(read(REV,CHART+'runner-metadata-only.diff')).hexdigest()==parity['runner_diff_sha256']
for path,sha in validation['artifact_sha256'].items():assert hashlib.sha256(read(REV,CHART+path)).hexdigest()==sha
assert hashlib.sha256(read(REV,'scripts/plot-host-baselines.py')).hexdigest()==validation['renderer_sha256']
assert hashlib.sha256(read(REV,ROOT+'baseline-charts/m1-m6-baseline.png')).hexdigest()==validation['original_png_sha256']
# Compare table rounded medians to all four source summaries without renderer execution.
labels=['Insert','Hit lookup','Miss lookup','Rank','Forward iteration','Scan','Score update','Delete'];cases=['insert','lookup-hit','lookup-miss','rank','iterate','scan','update','delete']
for size in [100000,1000000]:
    for label,case in zip(labels,cases):
        vals=[]
        for host in sources['hosts']:
            cell=next(r for r in obj(CHART+host['file']) if r['size']==size and r['case']==case);vals.append(f"{cell['median_ns_op']:.2f}")
        assert '| '+label+' | '+' | '.join(vals)+' |' in chartreadme
read(REV,'README.md');read(REV,ROOT+'AWS-DECISIONS.md')
result={'immutable_revision':REV,'metadata_checks':'pass','reporting_finding':'README.md:213-223 retains stale current-PARK claim for rejected old-source Intel replication','populations':len(pop),'decisions':dict(decisions),'patch_records':len(patches),'public_context_matches':21,'private_control_context_mismatches':3,'patch_checks':patches,'corrected_chart_hosts':hosts,'corrected_chart_cells':allcells,'corrected_chart_rows':allcells*24,'input_sha256':inputs,'limits':['No benchmark, test, compiler, patch application, renderer or runner execution. Patch checks are exact original hunk context reconstruction in memory.','Summary qualification/table arithmetic checked; raw benchmark rows not independently reconstructed in this reporting review.','Reviewer authored Intel results and some shared candidate sources; not independent revalidation of own measurements.','Release deadline/timer preflight is not completed release proof.']}
Path(__file__).with_name('audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k in ['metadata_checks','populations','decisions','patch_records','public_context_matches','private_control_context_mismatches','corrected_chart_cells']}))
