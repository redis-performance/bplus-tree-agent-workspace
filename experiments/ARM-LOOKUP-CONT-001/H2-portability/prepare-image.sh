#!/bin/sh
# Canonical image preparation, root-controlled in one reviewed named container.
set -eu
# Failure evidence survives container cleanup; complete files stay in the image.
trap 'prepare_status=$?; trap - 0; if [ "$prepare_status" -ne 0 ]; then
 for prepare_log in /opt/h2-portability-receipts/apt-update.log /opt/h2-portability-receipts/apt-install.log; do
  if [ -f "$prepare_log" ]; then tail -n 200 "$prepare_log" >&2; fi
 done
fi; exit "$prepare_status"' 0
export LC_ALL=C LANG=C DEBIAN_FRONTEND=noninteractive
mkdir /opt/h2-portability-receipts
apt-get update > /opt/h2-portability-receipts/apt-update.log 2>&1
mkdir -p /opt/h2-portability-receipts/debs/partial
apt-get -o Dir::Cache::archives=/opt/h2-portability-receipts/debs install -y --no-install-recommends gcc-i686-linux-gnu gcc-s390x-linux-gnu libc6-dev-i386-cross libc6-dev-s390x-cross binutils-i686-linux-gnu binutils-s390x-linux-gnu qemu-user > /opt/h2-portability-receipts/apt-install.log 2>&1
# Retain resolved dependency versions and repository identities in the committed image.
dpkg-query -W -f='${binary:Package}\t${Version}\t${Architecture}\n' > /opt/h2-portability-receipts/packages.tsv
cp -a /etc/apt /opt/h2-portability-receipts/apt-config
cp -a /var/lib/apt/lists /opt/h2-portability-receipts/apt-lists
find /opt/h2-portability-receipts/debs -name '*.deb' -type f -exec sha256sum '{}' + > /opt/h2-portability-receipts/package-archives.sha256
test -s /opt/h2-portability-receipts/package-archives.sha256
