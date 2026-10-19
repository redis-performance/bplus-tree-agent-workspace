from pathlib import Path
import difflib,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent
source=subprocess.check_output(['git','show','8fab511e:src/zset_btree.c'],text=True)
header=subprocess.check_output(['git','show','8fab511e:src/zset_btree.h'],text=True)
for name in 'ABC':
 decl={'A':'    const void *member_offsets; /* Lazy per-leaf member-offset base. */','B':'    uint32_t member_offsets; /* Lazy byte offset from leaf; zero means unset. */','C':'    uint16_t member_offsets; /* Lazy byte offset from leaf; zero means unset. */'}[name]
 h=header.replace('    unsigned int pos;\n} zbtreeIterator;','    unsigned int pos;\n'+decl+'\n} zbtreeIterator;');assert h!=header
 reset='NULL' if name=='A' else '0'
 s,count=re.subn(r'^([ \t]*)iter->leaf = ([^;]+);',lambda m:m[0]+'\n'+m[1]+'iter->member_offsets = '+reset+';',source,flags=re.M);assert count==11,count
 if name=='A':cache='''        if (iter->member_offsets == NULL)
            iter->member_offsets = zbtScoreLeafOffsets(leaf);
        const uint16_t *offsets = iter->member_offsets;
'''
 else:cache=f'''        if (iter->member_offsets == 0)
            iter->member_offsets = (uint{'32' if name=='B' else '16'}_t)
                ((unsigned char *)zbtScoreLeafOffsets(leaf) - (unsigned char *)leaf);
        const uint16_t *offsets = (const uint16_t *)
            ((unsigned char *)leaf + iter->member_offsets);
'''
 target='''        size_t elelen;
        const unsigned char *element =
            zbtScoreLeafElement(leaf, pos, &elelen);'''
 replace=cache+'''        size_t elelen;
        const unsigned char *element = zbtPackedData(
            (unsigned char *)leaf + offsets[zbtScoreLeafPhysicalPos(leaf, pos)],
            &elelen);'''
 assert s.count(target)==1;s=s.replace(target,replace)
 if name=='C':s=s.replace('int zbtreeIteratorNext(zbtreeIterator *iter, int reverse,','_Static_assert(ZBT_SCORE_LEAF_BYTES <= UINT16_MAX, "iterator member offset fits");\n\nint zbtreeIteratorNext(zbtreeIterator *iter, int reverse,')
 d=P/'variants'/name;d.mkdir(parents=True,exist_ok=True)
 patch=''.join(difflib.unified_diff(source.splitlines(True),s.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'))+''.join(difflib.unified_diff(header.splitlines(True),h.splitlines(True),fromfile='a/src/zset_btree.h',tofile='b/src/zset_btree.h'))
 (d/'candidate.patch').write_text(patch)
 (d/'source-sha256.json').write_text(json.dumps({'source':hashlib.sha256(s.encode()).hexdigest(),'header':hashlib.sha256(h.encode()).hexdigest(),'leaf_resets':count},indent=2)+'\n')
 (d/'implementation.md').write_text('# Sequential implementation'+name+'\n\nOne nativeworker, not independentimplementer; model/costunknown. '+{'A':'Pointercache;64bititerator grows16→24bytes, explicitlydeclared+8byte state tradeoff.','B':'uint32byteoffsetcache occupies64bitpadding;sizeof16 unchanged.','C':'uint16byteoffsetcache occupies64bitpadding;sizeof16 unchanged, leafboundstaticassert.'}[name]+' All11leafassignments resetcache; member/lengthlazyinit; originaldecoder/physicalorder retained. Matchingvariantheader used torecompile allreferees.\n')
