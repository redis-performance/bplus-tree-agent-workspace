set -eu
cd @REPO@
P=experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator
for V in A B; do
 D="$P/build/$V-source";mkdir -p "$D"
 git archive 8fab511e src compat vendor/redis tests bench | tar -x -C "$D"
 patch -d "$D" -p1 < "$P/variants/$V/candidate.patch" > "$P/raw/$V-patch.stdout"
 for MODE in native sanitize; do
  FLAGS=-O3;NAME=$V
  if [ "$MODE" = sanitize ]; then FLAGS='-O1 -fsanitize=address,undefined -fno-sanitize-recover=all';NAME=$V-sanitize;fi
  for DRIVER in iterator cache-oracle cache-oracle-additive; do
   SUFFIX=''
   if [ "$DRIVER" = cache-oracle ]; then SUFFIX=-oracle;fi
   if [ "$DRIVER" = cache-oracle-additive ]; then SUFFIX=-additive;fi
   clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -fno-lto $FLAGS "$P/$DRIVER.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$NAME$SUFFIX"
  done
  clang -I"$D/src" -I"$D/compat" -I"$D/vendor/redis" -std=c11 -g -Wall -Wextra -Werror -fno-omit-frame-pointer -fno-lto -DREDIS_TEST -DREDIS_DEBUG $FLAGS "$D/tests/upstream.c" "$D/src/zset_btree.c" "$D/compat/standalone.c" "$D/vendor/redis/siphash.c" -lm -o "$P/build/$NAME-upstream"
  for KIND in upstream oracle additive; do
   "$P/build/$NAME-$KIND" > "$P/raw/$NAME-$KIND.stdout" 2> "$P/raw/$NAME-$KIND.stderr"
  done
 done
 python3 "$P/validate.py" "$V"
 sha256sum "$D/src/zset_btree.c" "$D/src/zset_btree.h" > "$P/raw/$V-source-sha256.txt"
done
python3 - <<'PY'
from pathlib import Path
import json,hashlib
p=Path('experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/005-iterator')
h={str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'build').glob('*') if f.is_file()}
for f in list(p.glob('*.c'))+list(p.glob('*.py'))+list((p/'variants').rglob('*.patch')):h[str(f.relative_to(p))]=hashlib.sha256(f.read_bytes()).hexdigest()
(p/'comparison-hashes.json').write_text(json.dumps(h,indent=2)+'\n')
PY
