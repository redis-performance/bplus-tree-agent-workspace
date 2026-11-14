#!/bin/sh
set -eu
mkdir /out/image-preparation-receipts
for item in apt-update.log apt-install.log packages.tsv apt-config apt-lists package-archives.sha256; do
 cp -a /opt/h2-portability-receipts/"$item" /out/image-preparation-receipts/
done
test -s /out/image-preparation-receipts/package-archives.sha256
