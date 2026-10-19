#!/bin/bash
set -euo pipefail
exec taskset -c 2 python3 '@REPO@/scratch/arm-mask-continuation-20261019/run-continuation.py' --checkout '@REPO@' --prior '@REPO@/scratch/arm-mask-followup-20261019'
