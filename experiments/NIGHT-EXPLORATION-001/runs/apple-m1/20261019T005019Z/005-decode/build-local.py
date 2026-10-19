#!/usr/bin/env python3
"""Build isolated private decoder snapshots without writing Git metadata."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", required=True)
    p.add_argument("--sanitize", action="store_true")
    args = p.parse_args()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    base = ROOT / "src/zset_btree.c"
    bulk = ROOT / "experiments/EXP-008/referee/bulk.inc"
    control = ROOT / "experiments/EXP-008/referee/policy-control.inc"
    kernel = ROOT / "experiments/EXP-008/referee/kernel.c"
    files = [base, ROOT / "src/zset_btree.h", bulk, control, kernel,
             ROOT / "bench/decoder_bench.c", ROOT / "bench/decoder_kernel.h",
             ROOT / "compat/standalone.c", ROOT / "vendor/redis/siphash.c"]
    if sha(base) != "d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2":
        raise SystemExit("Launch tree source changed")
    flags = ["-std=c11", "-O1" if args.sanitize else "-O3", "-g", "-Wall",
             "-Wextra", "-Werror", "-fno-omit-frame-pointer", "-fno-lto",
             "-Isrc", "-Icompat", "-Ivendor/redis", "-Ibench",
             f"-ffile-prefix-map={ROOT}=."]
    if args.sanitize:
        flags += ["-fsanitize=address,undefined", "-fno-sanitize-recover=all"]
    manifest = {"compiler": subprocess.check_output(["clang", "--version"], text=True),
                "flags": flags, "sanitizers": args.sanitize,
                "inputs": {str(f.relative_to(ROOT)): sha(f) for f in files},
                "variants": {}, "commands": []}

    def run(command):
        q = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        manifest["commands"].append({"command": [str(x).replace(str(ROOT), "<workspace>") for x in command],
                                     "returncode": q.returncode, "stderr": q.stderr.replace(str(ROOT), "<workspace>")})
        if q.returncode:
            (out / "build.json").write_text(json.dumps(manifest, indent=2) + "\n")
            raise RuntimeError(q.stderr)

    common = []
    for name, source in (("driver", "bench/decoder_bench.c"),
                         ("standalone", "compat/standalone.c"),
                         ("siphash", "vendor/redis/siphash.c")):
        target = out / f"{name}.o"
        run(["clang", *flags, "-c", source, "-o", str(target)])
        common.append(str(target))
    prefix = base.read_text() + "\n" + bulk.read_text() + "\n"
    for variant in ("base", "A", "B", "C"):
        policy = control if variant == "base" else HERE / f"policy-{variant}.inc"
        if variant != "base":
            manifest["inputs"][str(policy.relative_to(ROOT))] = sha(policy)
        folder = out / variant
        folder.mkdir(exist_ok=True)
        source = folder / "zset_btree.c"
        source.write_text(prefix + policy.read_text())
        define = f'-DDECODER_TREE_SOURCE="{source}"'
        obj = folder / "kernel.o"
        binary = folder / "decoder-bench"
        run(["clang", *flags, define, "-c", str(kernel), "-o", str(obj)])
        run(["clang", *flags, *common, str(obj), "-lm", "-o", str(binary)])
        if not args.sanitize:
            run(["clang", *flags, define, "-S", str(kernel), "-o", str(folder / "kernel.s")])
        manifest["variants"][variant] = {"source_sha256": sha(source),
                                            "binary_sha256": sha(binary),
                                            "kernel_object_sha256": sha(obj),
                                            "binary": str(binary)}
    (out / "build.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("built", ",".join(manifest["variants"]), "sanitize", args.sanitize)


if __name__ == "__main__":
    main()
