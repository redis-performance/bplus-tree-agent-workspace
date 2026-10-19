#!/usr/bin/env python3
"""Pure offline reviewer controls. Synthetic files only; never launch a child."""
from pathlib import Path
from types import SimpleNamespace
import csv, hashlib, json, os, runpy, struct, tempfile

E = Path(__file__).resolve().parents[1]
os.chdir(E.parents[1])
Path('scratch').mkdir(exist_ok=True)
checks = []
def check(name, condition):
    assert condition, name
    checks.append(name)

def mapper_controls():
    m = runpy.run_path(str(E/'profile-map.py'))
    mapping = dict(image=0x1000, text_lo=0x1200, text_hi=0x1240,
        sections=[dict(segment='__TEXT',section='__text',address=0x1200,size=64),
                  dict(segment='__TEXT',section='__stubs',address=0x1300,size=16)],
        symbols={0x1200:['_sampler_probe'],0x1220:['_a','_b']})
    def pc(rel, module='probe'):
        return ['PC',module,hex(0x10000000+rel),'0x10000000','misleading_nearest','0x10000200']
    c = lambda rel: m['classify'](pc(rel),'probe',mapping)
    check('actual nm beats dladdr',c(0x208)['symbol']=='_sampler_probe')
    check('aliases retained',c(0x228)['symbol_aliases']==['_a','_b'] and c(0x228)['symbol_ambiguous'])
    check('stub unknown',c(0x304)['classification']=='import-stub' and c(0x304)['own_image_pc_offset']==0x304)
    check('outside unknown retained',c(0x500)['classification']=='unmapped-own-image' and c(0x500)['own_image_pc_offset']==0x500)
    check('unaligned unknown',c(0x201)['classification']=='unmapped-own-image')
    check('external separated',m['classify'](pc(0x208,'libfoo.dylib'),'probe',mapping)['classification']=='external-dladdr-label')
    with tempfile.TemporaryDirectory(prefix='exp009-C-map-',dir='scratch') as td:
        d=Path(td); header=bytearray(32);struct.pack_into('<I',header,0,0xfeedfacf);struct.pack_into('<I',header,16,1)
        cmd=bytearray(232);struct.pack_into('<II',cmd,0,0x19,len(cmd));cmd[8:14]=b'__TEXT';struct.pack_into('<Q',cmd,24,0x1000);struct.pack_into('<I',cmd,64,2)
        for i,(name,addr,size) in enumerate([('__text',0x1200,64),('__stubs',0x1300,16)]):
            q=72+80*i;cmd[q:q+len(name)]=name.encode();cmd[q+16:q+22]=b'__TEXT';struct.pack_into('<QQ',cmd,q+32,addr,size)
        binary=d/'probe';binary.write_bytes(header+cmd);nm=d/'nm';nmtext='0000000000001200 t _sampler_probe\n0000000000001220 t _a\n0000000000001220 t _b\n';nm.write_text(nmtext)
        asm=d/'asm';asmtext='_sampler_probe:\n0000000000001200 add x0, x0, #1\n0000000000001204 ret\n_next:\n0000000000001208 nop\n';asm.write_text(asmtext)
        out=d/'out';out.write_text('result,1128443088728658433\n');err=d/'err';original='PROFILE,sampler_probe,1000,25,0\n'+('PC,probe,0x10000200,0x10000000,bad,0x10000200\n'*25);err.write_text(original)
        def call(): return m['map_profile'](out,err,binary,nm,asm)
        check('good strict25 probe control',call()['status']=='PASS')
        def reject(name,change,reset):
            change(); rejected=False
            try:
                r=call();rejected=r['status']=='FAIL' and len(r['observations'])==int(err.read_text().splitlines()[0].split(',')[3])
            except (AssertionError,ValueError):rejected=True
            finally:reset()
            check(name,rejected)
        reject('bad checksum FAIL',lambda:out.write_text('result,1\n'),lambda:out.write_text('result,1128443088728658433\n'))
        reject('outside probe FAIL',lambda:err.write_text(original.replace('0x10000200','0x10000208',1)),lambda:err.write_text(original))
        reject('short24 FAIL retains24',lambda:err.write_text('PROFILE,sampler_probe,1000,24,0\n'+'\n'.join(original.splitlines()[1:25])+'\n'),lambda:err.write_text(original))
        reject('capped reject',lambda:err.write_text(original.replace('25,0','25,1',1)),lambda:err.write_text(original))
        reject('non1000 interval reject',lambda:err.write_text(original.replace(',1000,',',999,',1)),lambda:err.write_text(original))
        reject('PC-count mismatch reject',lambda:err.write_text(original+'PC,probe,0x10000200,0x10000000,bad,0x10000200\n'),lambda:err.write_text(original))
        reject('duplicate probe label reject',lambda:asm.write_text(asmtext+'_sampler_probe:\n0000000000001200 ret\n'),lambda:asm.write_text(asmtext))
        reject('assembly gap reject',lambda:asm.write_text(asmtext.replace('0000000000001204','0000000000001210')),lambda:asm.write_text(asmtext))
        reject('nm anchor mismatch reject',lambda:nm.write_text(nmtext.replace('1200','1204',1)),lambda:nm.write_text(nmtext))
        reject('interior symbol reject',lambda:nm.write_text(nmtext+'0000000000001204 t _alien\n'),lambda:nm.write_text(nmtext))
        reject('probe beyond text reject',lambda:asm.write_text(asmtext.replace('0000000000001200','0000000000001300').replace('0000000000001204','0000000000001304')),lambda:asm.write_text(asmtext))

def driver_controls():
    m=runpy.run_path(str(E/'driver.py'));g=m['aa'].__globals__
    check('known affine checksum',m['control_checksum']()==1128443088728658433)
    n=1000;ops=2003;seed=1
    order,_=m['model'](n,seed);check('query permutation is complete',sorted(order)==list(range(n)))
    for case in ['lookup-hit','lookup-miss','lookup-mixed']:
        want=sum((order[i%n] if case=='lookup-hit' else order[i%n]+1 if case=='lookup-mixed' and i%2==0 else 0) for i in range(ops))
        check(case+' independent direct checksum',m['expected_checksum'](case,n,ops,seed)[0]==want)
    with tempfile.TemporaryDirectory(prefix='exp009-C-csv-',dir='scratch') as td:
        d=Path(td);out=d/'out';err=d/'err';err.write_text('');header=m['CSV_HEADER'];checksum=m['expected_checksum']('lookup-hit',n,ops,seed)[0]
        row=dict(zip(header,['lookup-hit',str(n),str(ops),'16','1',str(ops),'2003000','1000.000','1000000.000','123456',str(checksum),'2000000','6','7','user-interactive','user-interactive','0','0','unknown','0','1','1000']))
        def write(r,fields=None):
            with out.open('w') as f:
                w=csv.DictWriter(f,fieldnames=fields or header);w.writeheader();w.writerow(r)
        write(row);check('canonical CSV accepted',m['parse_csv']({'stdout':out,'stderr':err},n,ops,seed)['checksum']==str(checksum))
        for field,value in [('seed','2'),('operations','2004'),('checksum',str(checksum+1)),('tree_bytes','0'),('elapsed_ns','0'),('warmup_passes','2'),('ns_per_op','nan'),('ops_per_sec','1000001.000'),('thread_elapsed_ns','-2')]:
            bad=dict(row);bad[field]=value;write(bad);rejected=False
            try:m['parse_csv']({'stdout':out,'stderr':err},n,ops,seed)
            except (AssertionError,ValueError):rejected=True
            check('CSV rejects '+field,rejected)
        for name,fields,r in [('extra',header+['extra'],dict(row,extra='1')),('duplicate',header+[header[-1]],row),('missing',header[:-1],{k:v for k,v in row.items() if k!=header[-1]})]:
            write(r,fields);rejected=False
            try:m['parse_csv']({'stdout':out,'stderr':err},n,ops,seed)
            except (AssertionError,ValueError):rejected=True
            check('CSV rejects '+name+' header',rejected)
    # Exercise actual AA function with only in-memory data/run/IO stubs. Never run main/Owner/Popen.
    original=dict(g)
    try:
        for label,bns,short,want in [('plus exact1percent',101000000,False,True),('minus exact1percent',99000000,False,True),('plus outside1ns',101000001,False,False),('minus outside1ns',98999999,False,False),('short window',100000000,True,False)]:
            schedule=[]
            for block,seed in enumerate([1,2,3,1,2,3]):
                for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
                    for pos,side in enumerate('ABBA'):schedule.append(dict(index=len(schedule),block=block,seed=seed,size=n,case='lookup-hit',member_bytes=16,warmup_passes=1,position=pos,side=side,operations=5000))
            bm=dict(status='COMPLETE',files_sha256={},binaries={'native':'fake-not-executed'})
            counts=dict(status='COMPLETE',build_manifest_sha256='fakehash',fixed={str(n):{'operations':5000} for n in [100000,1000000]})
            status=dict(status='COMPLETE',release_safe=True,all_sufficient=True,lookup_captures=2,sampler_controls=2)
            names={'build_manifest_path':'build','counts_path':'counts','schedule_path':'schedule','profile_status_path':'profile','build_status_path':'build-status','calibration_status_path':'cal-status','calibrate_status_path':'cal-status'}
            manifest=dict(names,files_sha256={p:'fakehash' for p in names.values()});loaded={'build':bm,'counts':counts,'schedule':schedule,'profile':status,'build-status':status,'cal-status':status};calls=[]
            def fake_run(o,cmd,name,**kwargs):calls.append(int(name));return int(name)
            def fake_parse(index,n,ops,seed,**kwargs):
                item=schedule[index];elapsed=bns if item['side']=='B' else 100000000
                if short and index==0:elapsed=9999999
                return dict(elapsed_ns=elapsed,operations=ops,fingerprint={'seed':seed,'ops':ops},tree_bytes=123)
            g.update(load=lambda p:loaded[p],sha=lambda p:'fakehash',model=lambda *a:None,run=fake_run,parse_csv=fake_parse,save=lambda *a:None)
            owner=SimpleNamespace(manifest=manifest,state={},out=Path('unused-no-write'),bound=lambda:None)
            m['aa'](owner);check('AA '+label,owner.state['qualified']==want and calls==list(range(48)))
    finally:g.clear();g.update(original)

if __name__=='__main__':
    mapper_controls();driver_controls()
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [E/'driver.py',E/'profile-map.py',E/'seal.py',Path(__file__)]}
    result=dict(status='PASS',scope='Pure Python synthetic inputs; no subprocess/native execution',controls=len(checks),checks=checks,files_sha256=hashes,initial_review_expectation_failure='An earlier interactive control expected an exception for wrong checksum; mapper returned FAIL with conserved observations. Corrected reviewer expectation accepts FAIL/rejection only, never PASS; no native rerun.')
    with (E/'review/C-offline-controls.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(dict(status='PASS',controls=len(checks),files_sha256=hashes)))
