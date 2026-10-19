set -eu
cd @REPO@
git fetch origin main
D=@REPO@/scratch/adapter-worktree-13e459ff8
P=@REPO@/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/013-corrected-adapter-baseline
mkdir -p "$P"
git worktree add --detach "$D" 13e459ff8800be3f02b6b45c87dd7b0c39453fa9
cd "$D"
test "$(git rev-parse HEAD)" = "13e459ff8800be3f02b6b45c87dd7b0c39453fa9"
python3 scripts/run-size-matrix.py --out "$P/result" --build build/adapter-requalification --ops 1000000 --member-bytes 16 --budget-seconds 1200
python3 scripts/analyse-size-matrix.py "$P/result"
