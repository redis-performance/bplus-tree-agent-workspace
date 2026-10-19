set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/006-scan-profile
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all bench/microbench.c src/zset_btree.c compat/standalone.c vendor/redis/siphash.c "$P/sampler.c" -lm -o "$P/build/original-sanitize"
sha256sum "$P/build/original-sanitize" > "$P/resume-sha256.txt"
python3 "$P/run-diagnostic.py"
objdump -d --disassemble=zbtIndexScanSlot "$P/build/profile" > "$P/scan-slot-assembly.txt"
