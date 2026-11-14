"""Exact source hooks; no execution of the generated C."""
def one(text,old,new):
    assert text.count(old)==1,repr(old)
    return text.replace(old,new)

def region(text,start,end,old,new):
    a=text.index(start);b=text.index(end,a)
    return text[:a]+one(text[a:b],old,new)+text[b:]

def lifecycle_hooks(text):
    # Diagnostic-only retention: LTO v2 inlined this body and failed the real-call
    # gate. Preserve a real, un-cloned original call without changing its body.
    text=one(text,'static int zbtScoreLeafFindMember(',
        'static __attribute__((noinline,noipa)) int zbtScoreLeafFindMember(')
    text=one(text,'/* --------------------------- Member index ------------------------------- */',
        '#include "../shadow.h"\n\n/* --------------------------- Member index ------------------------------- */')
    text=region(text,'static inline void zbtIndexSetId(', '/* Fold tag zero',
        '{\n    if (table->wide_ids)', '{\n    shIdWrite(table,bucket,pos,id);\n    if (table->wide_ids)')
    text=one(text,'    *table = t;\n    return 1;', '    *table = t;\n    shAlloc(zs,table);\n    return 1;')
    text=one(text,'static void zbtIndexTableRelease(zbtreeSet *zs, zbtIndexTable *table) {',
        'static void zbtIndexTableRelease(zbtreeSet *zs, zbtIndexTable *table) {\n    shRelease(table);')
    text=region(text,'static void zbtIndexTableInsertRaw(', '/* Search one table.',
        '                zbtIndexRecordHomeTag(table, hash);',
        '                zbtIndexRecordHomeTag(table, hash);\n                shSeedInsert(table,bucket,pos,hash,id);')
    for origin,(start,end,table) in enumerate([('static void zbtIndexCopyLeaf(', '/* Copy complete score leaves', '&rehash->table'),
                            ('static void zbtIndexRebuild(', '/* Delete the inclusive', '&zs->member_index')],1):
        old=f'zbtIndexTableInsertRaw({table}, hash, leaf->id);'
        new=(f'shSeedBegin(zs,{table},leaf,zbtScoreLeafPhysicalPos(leaf,i),hash,{origin});\n'
             f'        {old}\n'
             f'        shSeedEnd(zs,{table},leaf,zbtScoreLeafPhysicalPos(leaf,i),hash);')
        text=region(text,start,end,old,new)
    text=one(text,'            zs->member_index = rehash->table;',
        '            zs->member_index = rehash->table;\n            shPromote(&zs->member_index);')
    text=one(text,'        memcpy(copy->buckets, source->buckets, bytes);',
        '        memcpy(copy->buckets, source->buckets, bytes);\n        shDup(dst,copy,source);')
    text=region(text,'static void *zbtDefragPlainAllocation(', '/* The header, leaf table,',
        '    size_t old_size = zmalloc_usable_size(ptr);',
        '    uintptr_t sh_oldkey=(uintptr_t)ptr;\n    size_t old_size = zmalloc_usable_size(ptr);')
    text=region(text,'static void *zbtDefragPlainAllocation(', '/* The header, leaf table,',
        '    zbtDefragAdjustSize(zs, old_size, newptr);',
        '    zbtDefragAdjustSize(zs, old_size, newptr);\n    shRebind(sh_oldkey,newptr);')
    text=region(text,'zbtreeSet *zbtreeDefragStart(', '/* Forget an incremental scan.',
        '    size_t old_size = zmalloc_usable_size(zs);',
        '    uintptr_t sh_oldowner=(uintptr_t)zs;\n    size_t old_size = zmalloc_usable_size(zs);')
    text=region(text,'zbtreeSet *zbtreeDefragStart(', '/* Forget an incremental scan.',
        '        zs = newzs;', '        zs = newzs;\n        shReowner(sh_oldowner,zs);')
    text=one(text,'    return (*zbtIndexHomeTagsAt(table, home) & bits) == bits;',
        '    return shFilterObserve(table,*zbtIndexHomeTagsAt(table,home),bits,0);')
    text=one(text,'            if ((*zbtIndexHomeTagsAt(table, home) & bits) == bits) break;',
        '            if (shFilterObserve(table,*zbtIndexHomeTagsAt(table,home),bits,1)) break;')
    return text
