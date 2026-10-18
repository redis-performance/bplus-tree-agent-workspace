#!/usr/bin/env python3
"""Build the exact EXP-004 control/A sources with one identical decoder referee."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sanitize', action='store_true')
    p.add_argument('--out', default='build/decoder')
    a = p.parse_args()
    os.chdir(ROOT)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    frozen = json.loads(Path('experiments/EXP-004/freeze.json').read_text())
    source = Path('src/zset_btree.c').read_text()
    assert sha('src/zset_btree.c') == frozen['files']['control']['src/zset_btree.c'], 'Baseline source differs from EXP-004'
    start = source.index('static double zbtScoreLeafScore(')
    end = source.index('/* Return the raw hash byte', start)
    function = source[start:end]
    old, new = 'if (shift && bits > 64 - shift)', 'if (bits + shift > 64)'
    assert function.count(old) == 1
    candidate = source[:start] + function.replace(old, new) + source[end:]
    assert hashlib.sha256(candidate.encode()).hexdigest() == frozen['files']['A']['src/zset_btree.c']
    cc = shlex.split(os.environ.get('CC', 'cc'))
    flags = ['-std=c11', '-O1' if a.sanitize else '-O3', '-g', '-Wall', '-Wextra', '-Werror',
             '-fno-omit-frame-pointer', '-fno-lto', '-Isrc', '-Icompat', '-Ivendor/redis', '-Ibench',
             f'-ffile-prefix-map={ROOT}=.']
    if a.sanitize:
        flags += ['-fsanitize=address,undefined', '-fno-sanitize-recover=all']
    manifest = {'compiler': subprocess.run(cc + ['--version'], capture_output=True, text=True, check=True).stdout,
                'flags': [x.replace(str(ROOT), '<workspace>') for x in flags],
                'base_commit': subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip(),
                'sanitizers': a.sanitize, 'commands': [], 'files': {}, 'variants': {}}

    def run(command):
        result = subprocess.run(command, capture_output=True, text=True)
        manifest['commands'].append({'command': [str(x).replace(str(ROOT), '<workspace>') for x in command],
                                     'returncode': result.returncode, 'stdout': result.stdout.replace(str(ROOT), '<workspace>'),
                                     'stderr': result.stderr.replace(str(ROOT), '<workspace>')})
        (out/'build.json').write_text(json.dumps(manifest, indent=2)+'\n')
        if result.returncode:
            raise SystemExit(result.stderr)

    # Compile the driver/adapter once. Their exact object bytes are shared by both links.
    objects = []
    for name, path in [('driver', 'bench/decoder_bench.c'), ('standalone', 'compat/standalone.c'), ('siphash', 'vendor/redis/siphash.c')]:
        obj = out/(name+'.o')
        run(cc + flags + ['-c', path, '-o', str(obj)])
        objects.append(str(obj))
    for variant, text in [('base', source), ('A', candidate)]:
        dest = out/variant
        (dest/'src').mkdir(parents=True, exist_ok=True)
        target = dest/'src/zset_btree.c'; target.write_text(text)
        shutil.copyfile('src/zset_btree.h', dest/'src/zset_btree.h')
        include = os.path.relpath(target.resolve(), (ROOT/'bench').resolve())
        variant_flags = flags + ['-DDECODER_TREE_SOURCE="'+include+'"']
        run(cc + variant_flags + ['-c', 'bench/decoder_kernel.c', '-o', str(dest/'kernel.o')])
        run(cc + flags + objects + [str(dest/'kernel.o'), '-lm', '-o', str(dest/'decoder-bench')])
        if not a.sanitize:
            run(cc + variant_flags + ['-S', 'bench/decoder_kernel.c', '-o', str(dest/'kernel.s')])
        manifest['variants'][variant] = {'source_sha256': sha(target),
                                         'binary': str(dest/'decoder-bench'), 'binary_sha256': sha(dest/'decoder-bench'),
                                         'kernel_object_sha256': sha(dest/'kernel.o')}
    for name in ['bench/decoder_bench.c', 'bench/decoder_kernel.c', 'bench/decoder_kernel.h',
                 'scripts/build-decoder.py', 'compat/server.h', 'compat/standalone.c',
                 'vendor/redis/siphash.c', 'src/zset_btree.h', 'experiments/EXP-004/variants/A/candidate.patch']:
        manifest['files'][name] = sha(name)
    (out/'build.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(f'Built baseline and exact EXP-004 A in {out}; sanitizers={a.sanitize}')


if __name__ == '__main__':
    main()
