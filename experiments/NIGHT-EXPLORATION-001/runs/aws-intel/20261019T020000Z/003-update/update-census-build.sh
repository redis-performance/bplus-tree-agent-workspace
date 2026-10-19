set -eu
P=experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/003-update
python3 "$P/make-census.py"
clang -Isrc -Icompat -Ivendor/redis -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -O3 scratch/intel-update-census/harness.c scratch/intel-update-census/source.c compat/standalone.c vendor/redis/siphash.c -lm -o "$P/build/census"
