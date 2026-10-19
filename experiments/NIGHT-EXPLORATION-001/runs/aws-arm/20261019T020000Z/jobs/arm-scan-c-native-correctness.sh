set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/006-amd-scan-review/implementation-C
D="$P/build/native-arm"
mkdir -p "$D" "$P/native-arm-validation"
git archive 8fab511e src compat vendor/redis tests bench | tar -x -C "$D"
patch -d "$D" -p1 < "$P/candidate.patch" > "$P/native-arm-validation/patch.stdout"
cp "$P/all_match_guard_oracle.c" "$D/tests/all_match_guard_oracle.c"
uname -m > "$P/native-arm-validation/architecture.txt"
clang --version > "$P/native-arm-validation/compiler.txt"
for MODE in native sanitize; do
 FLAGS=-O3
 if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all';fi
 clang -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" "$D/tests/all_match_guard_oracle.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$D/oracle-$MODE" > "$P/native-arm-validation/$MODE-build.stdout" 2> "$P/native-arm-validation/$MODE-build.stderr"
 "$D/oracle-$MODE" > "$P/native-arm-validation/$MODE.stdout" 2> "$P/native-arm-validation/$MODE.stderr"
 clang -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer $FLAGS -DREDIS_TEST -DREDIS_DEBUG -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" "$D/tests/upstream.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$D/upstream-$MODE" > "$P/native-arm-validation/$MODE-upstream-build.stdout" 2> "$P/native-arm-validation/$MODE-upstream-build.stderr"
 "$D/upstream-$MODE" > "$P/native-arm-validation/$MODE-upstream.stdout" 2> "$P/native-arm-validation/$MODE-upstream.stderr"
done
sha256sum "$D/src/zset_btree.c" "$D/src/zset_btree.h" "$P/candidate.patch" "$P/all_match_guard_oracle.c" "$D"/oracle-* "$D"/upstream-* > "$P/native-arm-validation/hashes.txt"
