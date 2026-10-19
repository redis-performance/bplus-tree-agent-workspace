#!/usr/bin/env python3
"""Independent, offline-only controls; synthetic PCs are not measured observations."""
import ast
from collections import Counter
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True
E = Path(__file__).resolve().parent
R = Path.cwd()
PRIOR = E.parent / '019-corrected-member-index-profile'
OUT = E / 'CLASSIFIER-CONTROLS.json'
REPORT = dict(participant='/root/followup_proposal_a', backend='Inherited Codex/GPT-6 family; exact serving model, token and currency costs unknown', status='RUNNING', bound_seconds=180, binary_executions=0, profile_captures=0, synthetic_controls=[], actual_captures=[])

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def check(name, condition, **details):
    assert condition, name
    REPORT['synthetic_controls'].append(dict(name=name, result='PASS', **details))

def blocked_spawn(*args, **kwargs):
    raise RuntimeError('Offline control prohibited subprocess creation')

def alarm(*args):
    raise TimeoutError('Offline 180-second bound')

def functions(p):
    return {n.name: hashlib.sha256(ast.dump(n, include_attributes=False).encode()).hexdigest() for n in ast.parse(p.read_text()).body if isinstance(n, ast.FunctionDef)}

def main():
    start = time.monotonic()
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(180)
    freeze = json.loads((E / 'freeze.json').read_text())['files_sha256']
    before = {p: sha(p) for p in freeze}
    mismatches = [p for p in freeze if before[p] != freeze[p]]
    expected = {str(E.relative_to(R) / n) for n in ['capture.py', 'PLAN.json']}
    assert set(mismatches) == expected
    REPORT['pre_reseal_freeze'] = dict(entries=len(freeze), unchanged_against_old_freeze=len(freeze)-len(mismatches), root_review_edits={p: before[p] for p in mismatches}, freeze_sha256=sha(E/'freeze.json'))
    current, prior = functions(E/'capture.py'), functions(E/'pre-review/capture.py')
    assert all(current[k] == prior[k] for k in ['classify_pc', 'derive', 'run'])
    REPORT['function_ast_sha256'] = {k: current[k] for k in ['classify_pc', 'derive', 'run']}
    REPORT['driver_sha256'] = sha(E/'capture.py')
    REPORT['plan_sha256'] = sha(E/'PLAN.json')
    subprocess.Popen = blocked_spawn
    spec = importlib.util.spec_from_file_location('offline_capture_controls', E/'capture.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mapping = json.loads((E/'codegen.json').read_text())['enabled_mapping']
    image = mapping['image_vmaddr']
    text_start, text_end = mapping['text_start'], mapping['text_end']
    stub = next(x for x in mapping['sections'] if x['segment']=='__TEXT' and x['section']=='__stubs')
    stub_start, stub_end = stub['address'], stub['address']+stub['size']
    REPORT['static_image_geometry'] = dict(text_relative_bounds=[text_start-image,text_end-image], stub_relative_bounds=[stub_start-image,stub_end-image], section_count=len(mapping['sections']), binary_sha256=mapping['binary_sha256'])
    cold = next(s for s in mapping['symbols'] if '.cold.' in s['name'])
    def row(address, base=image):
        return ['PC', Path(mod.PLAN['binary']).name, hex(address), hex(base), cold['name'], hex(cold['address'])]
    def classify(address):
        return mod.classify_pc(row(address), mapping)
    for name, address in [('text-first',text_start),('text-first-plus-four',text_start+4),('text-last-four',text_end-4)]:
        k = classify(address)
        check(name, k[5]=='text-symbol' and k[7]=='__TEXT,__text' and bool(k[4]), relative_offset=address-image)
    for name, address in [('text-before',text_start-4),('unknown-image',stub_end+1048576),('text-unaligned-first',text_start+1),('text-unaligned-last',text_end-1)]:
        k = classify(address)
        check(name, k[5]=='unmapped-own-image' and k[1]=='unknown-own-image' and not k[4] and k[8] and k[2] is None, relative_offset=address-image)
    for name, address in [('text-end-is-stub-first',text_end),('stub-first',stub_start),('stub-last-four',stub_end-4),('stub-unaligned',stub_start+1)]:
        k = classify(address)
        check(name, k[5]=='import-stub' and k[1]=='import-stub-unknown-target' and not k[4] and k[8] and k[7]=='__TEXT,__stubs', relative_offset=address-image)
    for name,address in [('stub-end',stub_end),('stub-after-four',stub_end+4)]:
        k=classify(address)
        check(name,k[5]=='unmapped-own-image' and not k[4] and k[8] and k[1]=='unknown-own-image',relative_offset=address-image)
    for section in mapping['sections']:
        if section['section'] in ['__text','__stubs']:
            continue
        for position,address in [('first',section['address']),('last-four',section['address']+section['size']-4)]:
            k=classify(address)
            check('non-code-'+section['segment']+'-'+section['section']+'-'+position,k[5]=='unmapped-own-image' and not k[4] and k[8] and k[2] is None,relative_offset=address-image)
    for name, r in [('zero-base',row(text_start,0)),('pc-before-base',row(image-4,image))]:
        k=mod.classify_pc(r,mapping)
        check(name,k[5]=='unmapped-own-image' and not k[4] and k[8] and k[6] is None)
    aliases=[]
    for s in mapping['symbols']:
        if len(s.get('aliases',[]))>1:
            k=classify(s['address'])
            check('all-coalesced-aliases-'+s['name'],k[5]=='text-symbol' and k[1]=='ambiguous-coalesced-symbol' and list(k[4])==s['aliases'] and k[8],aliases=s['aliases'])
            aliases.append(s['aliases'])
    REPORT['coalesced_alias_groups_tested']=len(aliases)
    external=['PC','invalid module name','0x1000','0x0','invalid symbol name','0x0']
    k=mod.classify_pc(external,mapping)
    check('external-unknown-name-sanitization',k[0]=='other-module' and k[1]=='unknown' and k[4]==('unknown',) and k[5]=='external-symbol' and k[2] is None)
    REPORT['external_unknown_limit_note']='External naming is sanitized; external-symbol mapping_limit remains false. It does not establish an own-image symbol or event cost.'
    records=[json.loads(s) for s in (PRIOR/'commands.jsonl').read_text().splitlines()]
    old=json.loads((PRIOR/'summary.json').read_text())
    offline=json.loads((E/'offline-summary.json').read_text())
    assert len(records)==3 and len(old)==2 and len(offline)==3
    actual=[]
    oldkeys=['module','symbol','offset_bytes','symbol_image_offset','symbol_aliases','symbol_ambiguous','samples']
    def projection(bins):
        return sorted([json.dumps({k:b[k] for k in oldkeys},sort_keys=True) for b in bins])
    for i, rec in enumerate(records):
        paths={ch:R/v['path'] for ch,v in rec['raw'].items()}
        assert all(sha(paths[ch])==v['sha256'] for ch,v in rec['raw'].items())
        item={k:offline[i][k] for k in ['case','size','seed','original_index','origin_campaign']}
        d=mod.derive(rec,paths,item,mapping)
        assert d==offline[i]
        assert sum(b['samples'] for b in d['pc_bins'])==d['sample_count']
        if i<2:
            assert projection(d['pc_bins'])==projection(old[i]['pc_bins'])
            for key,value in old[i].items():
                if key!='pc_bins':
                    assert d[key]==value
        counts=Counter()
        for b in d['pc_bins']:
            counts[b['classification']]+=b['samples']
        REPORT['actual_captures'].append(dict(original_index=i,sample_count=d['sample_count'],classifications=dict(counts),raw_sha256={ch:v['sha256'] for ch,v in rec['raw'].items()},exact_offline_projection=True,exact_original019_projection=i<2))
        actual.append(d)
    assert sum(x['sample_count'] for x in actual)==455
    stubs=[b for b in actual[2]['pc_bins'] if b['classification']=='import-stub']
    assert {b['own_image_pc_offset']:b['samples'] for b in stubs}=={74604:2,74616:1}
    assert all(b['mapping_limit'] and b['symbol']=='import-stub-unknown-target' and not b['symbol_aliases'] and not b['symbol_ambiguous'] for b in stubs)
    REPORT['actual_retained_pc_total']=455
    REPORT['third_stub_bins']=[dict(relative_offset=b['own_image_pc_offset'],samples=b['samples'],symbol=b['symbol'],mapping_limit=b['mapping_limit']) for b in stubs]
    source_paths={ch:R/v['path'] for ch,v in records[0]['raw'].items()}
    good_csv=source_paths['stdout'].read_text()
    valid_lines=source_paths['stderr'].read_text().splitlines()
    item={k:offline[0][k] for k in ['case','size','seed','original_index','origin_campaign']}
    scratch=R/'scratch/m6-corrected-member-index-profile-continuation'
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='synthetic-classifier-',dir=scratch) as tmp:
        p={ch:Path(tmp)/ch for ch in ['stdout','stderr']}
        def derive_csv_log(text=good_csv,lines=valid_lines):
            p['stdout'].write_text(text)
            p['stderr'].write_text('\n'.join(lines)+'\n')
            return mod.derive({},p,item,mapping)
        def reject(name,text=good_csv,lines=valid_lines):
            try:
                derive_csv_log(text,lines)
            except (AssertionError,ValueError,KeyError,TypeError) as ex:
                REPORT['synthetic_controls'].append(dict(name=name,result='PASS',expected_rejection=type(ex).__name__))
            else:
                raise AssertionError('Synthetic invalid input accepted: '+name)
        for name,header in [('wrong-case','PROFILE,rank,1000,84,0'),('wrong-interval','PROFILE,lookup-hit,1001,84,0'),('capped','PROFILE,lookup-hit,1000,84,1'),('count-too-small','PROFILE,lookup-hit,1000,83,0'),('count-too-large','PROFILE,lookup-hit,1000,85,0'),('count-over-cap','PROFILE,lookup-hit,1000,65537,0'),('count-nonfinite','PROFILE,lookup-hit,1000,NaN,0'),('header-extra-field','PROFILE,lookup-hit,1000,84,0,extra')]:
            reject(name,lines=[header]+valid_lines[1:])
        reject('missing-header',lines=valid_lines[1:])
        reject('duplicate-header',lines=[valid_lines[0]]+valid_lines)
        reject('extra-log-line',lines=valid_lines+['synthetic noise'])
        for name,mutate in [('pc-missing-field',lambda r:r[:-1]),('pc-extra-field',lambda r:r+['extra']),('pc-bad-hex',lambda r:r[:2]+['not-hex']+r[3:])]:
            lines=list(valid_lines);lines[1]=','.join(mutate(lines[1].split(',')));reject(name,lines=lines)
        rows=list(csv.DictReader(io.StringIO(good_csv)))
        fields=list(rows[0])
        def csv_text(row):
            out=io.StringIO();writer=csv.DictWriter(out,fieldnames=fields);writer.writeheader();writer.writerow(row);return out.getvalue()
        for key,value in [('operations','9999999'),('checksum','0'),('checksum','NaN'),('tree_bytes','0'),('tree_bytes','-1'),('case','rank'),('seed','2'),('member_bytes','17'),('warmup_passes','2'),('traversals','1')]:
            r=dict(rows[0]);r[key]=value;reject('csv-'+key+'-'+value,text=csv_text(r))
        reject('csv-no-row',text=good_csv.splitlines()[0]+'\n')
        reject('csv-extra-row',text=good_csv+good_csv.splitlines()[1]+'\n')
        reject('csv-extra-value',text=good_csv.rstrip() + ',extra\n')
        synthetic=[','.join(row(text_start))]*7+[','.join(row(stub_start+1))]*3
        d=derive_csv_log(lines=['PROFILE,lookup-hit,1000,10,0']+synthetic)
        check('synthetic-duplicate-conservation',d['sample_count']==10 and sum(b['samples'] for b in d['pc_bins'])==10 and len(d['pc_bins'])==2 and d['mapping_limit'] and d['sufficient'])
        d=derive_csv_log(lines=['PROFILE,lookup-hit,1000,0,0'])
        check('zero-count-retained-insufficient',d['sample_count']==0 and not d['sufficient'] and d['pc_bins']==[])
        maximum=[','.join(row(text_start))]*65536
        d=derive_csv_log(lines=['PROFILE,lookup-hit,1000,65536,0']+maximum)
        check('maximum-count-conserved',d['sample_count']==65536 and len(d['pc_bins'])==1 and d['pc_bins'][0]['samples']==65536)
        reject('over-maximum-with-exact-row-count',lines=['PROFILE,lookup-hit,1000,65537,0']+maximum+[maximum[0]])
    after={p:sha(p) for p in freeze}
    assert before==after
    REPORT.update(status='PASS',frozen_input_snapshots_unchanged=len(before),offline_wall_seconds=time.monotonic()-start,controls_count=len(REPORT['synthetic_controls']),timing_fields_used=False,no_candidate_or_performance_claim=True)
    signal.alarm(0)

if __name__=='__main__':
    try:
        main()
    except BaseException as ex:
        REPORT.update(status='FAIL',error_type=type(ex).__name__,error=str(ex))
        raise
    finally:
        REPORT['control_source_sha256']=sha(__file__)
        REPORT['command']='PYTHONDONTWRITEBYTECODE=1 python3 '+str(Path(__file__).relative_to(R))
        OUT.write_text(json.dumps(REPORT,indent=2)+'\n')
