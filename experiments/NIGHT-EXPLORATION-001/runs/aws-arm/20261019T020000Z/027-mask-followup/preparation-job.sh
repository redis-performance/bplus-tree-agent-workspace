set -eu
cd @REPO@
python3 scratch/arm-mask-followup-20261019/run-validation.py --checkout "$PWD"
