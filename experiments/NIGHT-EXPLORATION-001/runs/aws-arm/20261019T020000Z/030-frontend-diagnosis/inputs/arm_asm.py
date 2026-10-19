"""Fail-closed GNU AArch64 objdump parsing; encoded words are never relocation-normalized."""
import re

def parse(file):
    text=file.read_text()
    assert 'file format elf64-littleaarch64' in text, 'expected native little-endian AArch64 disassembly'
    funcs={};current=None;source=None;count=0
    for line in text.splitlines():
        fn=re.fullmatch(r'([0-9a-f]+) <([^>]+)>:',line)
        if fn:
            assert fn[2] not in funcs
            current={'start':int(fn[1],16),'instructions':{}};funcs[fn[2]]=current;source=None
            continue
        src=re.search(r'([^/\s]+\.[ch]):(\d+)',line)
        if src:source=src[1]+':'+src[2]
        m=re.match(r'^\s*([0-9a-f]+):\s*\t([^\t]+)\t(.*)$',line)
        if m:
            assert current is not None
            encoded=m[2].strip();assert re.fullmatch(r'[0-9a-f]{8}',encoded),(line,'not one AArch64 word')
            addr=int(m[1],16);offset=addr-current['start'];assert addr%4==0 and offset>=0 and offset not in current['instructions']
            current['instructions'][offset]={'bytes':[encoded],'assembly':m[3],'source_line':source};count+=1
        elif re.match(r'^\s*[0-9a-f]+:\s*\t',line):
            raise AssertionError((line,'unparsed AArch64 instruction'))
    assert count>0 and funcs
    return funcs
