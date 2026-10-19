import pathlib,subprocess,json,difflib,time
p=pathlib.Path(__file__).parent
d=pathlib.Path('scratch/intel-iterator-variants/B')
s=(d/'src/zset_btree.c').read_text()
needles={'initial': '    iter->leaf = node;\n    iter->member_offsets = 0;', 'transition': '            leaf = leaf->next;\n            iter->leaf = leaf;\n            iter->member_offsets = 0;'}
results=[]
for name,needle in needles.items():
 assert s.count(needle)==1
 changed=s.replace(needle,needle.rsplit('\n',1)[0])
 fault=pathlib.Path('scratch/intel-iterator-variants/fault-'+name+'.c');fault.write_text(changed)
 (p/('fault-'+name+'.patch')).write_text(''.join(difflib.unified_diff(s.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 binary=p/'build'/('fault-'+name)
 command=['clang','-I'+str(d/'src'),'-I'+str(d/'compat'),'-I'+str(d/'vendor/redis'),'-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all',str(p/'cache-oracle.c'),str(fault),str(d/'compat/standalone.c'),str(d/'vendor/redis/siphash.c'),'-lm','-o',str(binary)]
 subprocess.run(command,check=True)
 with (p/'raw'/('fault-'+name+'.stdout')).open('w') as out,(p/'raw'/('fault-'+name+'.stderr')).open('w') as err:
  result=subprocess.run([str(binary)],stdout=out,stderr=err,timeout=30)
 results.append({'fault':name,'returncode':result.returncode,'detected':result.returncode!=0,'compile_command':command})
 (p/'fault-controls.json').write_text(json.dumps(results,indent=2)+'\n')
 assert result.returncode!=0, name+' fault was not detected'
