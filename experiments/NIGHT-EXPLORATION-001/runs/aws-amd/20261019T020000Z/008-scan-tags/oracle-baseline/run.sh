set -eu
cd @REPO@
out=scratch/amd-scan-oracle
cp -r src "$out/src"
for mode in native san; do
 flags='-O3'
 if [ "$mode" = san ]; then flags='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all'; fi
 clang -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $flags -Isrc -Icompat -Ivendor/redis "$out/tests/all_match_guard_oracle.c" compat/standalone.c vendor/redis/siphash.c -lm -o "$out/oracle-$mode" > "$out/build-$mode.stdout" 2> "$out/build-$mode.stderr"
 "$out/oracle-$mode" > "$out/$mode.stdout" 2> "$out/$mode.stderr"
done
