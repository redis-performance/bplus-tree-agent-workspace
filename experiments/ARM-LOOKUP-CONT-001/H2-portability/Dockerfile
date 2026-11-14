# Equivalent recipe only. Canonical deployment uses a named preparation container
# and docker commit, so reviewed cleanup can identify every owned container.
FROM sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460
COPY prepare-image.sh /opt/prepare-image.sh
RUN sh /opt/prepare-image.sh
