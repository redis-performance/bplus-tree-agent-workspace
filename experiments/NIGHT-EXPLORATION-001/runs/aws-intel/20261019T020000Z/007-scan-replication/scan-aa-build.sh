set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/007-scan-replication
D=scratch/intel-scan-replication/base
mkdir -p "$D" "$P/raw"
git archive 8fab511e src compat vendor/redis tests bench Makefile | tar -x -C "$D"
make -C "$D" CC=clang BUILD=build OPT=-O3 build/btree-bench > "$P/build.stdout" 2> "$P/build.stderr"
clang --version > "$P/compiler.txt"
sha256sum "$D"/src/zset_btree.c "$D"/src/zset_btree.h "$D"/bench/microbench.c "$D"/compat/standalone.c "$D"/vendor/redis/siphash.c "$D"/Makefile "$D"/build/btree-bench > "$P/build-sha256.txt"
