#!/bin/sh
# Absolute operational ceiling is fixed by the reviewed driver before Docker
# launch. Recompute after container startup; delayed launches cannot extend it.
set -eu
export LC_ALL=C LANG=C
portability_ceiling=$1
shift
case "$portability_ceiling" in ''|*[!0-9]*) exit 2;; esac
test "$#" -gt 0
test -x /usr/bin/date
test -x /usr/bin/timeout
portability_now=$(/usr/bin/date +%s)
portability_remaining=$((portability_ceiling - portability_now - 17))
# Reserve15 seconds for KILL escalation and2 seconds for client/exit margin.
test "$portability_remaining" -gt 0
exec /usr/bin/timeout --signal=TERM --kill-after=15s "${portability_remaining}s" "$@"
