CC ?= cc
BUILD ?= build
OPT ?= -O3
CPPFLAGS += -Isrc -Icompat -Ivendor/redis
CFLAGS += -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer $(OPT)
LDLIBS += -lm
COMMON = src/zset_btree.c compat/standalone.c vendor/redis/siphash.c
HEADERS = src/zset_btree.h compat/server.h vendor/redis/sds.h vendor/redis/testhelp.h

.PHONY: all check sanitize smoke clean
all: $(BUILD)/btree-bench $(BUILD)/btree-test
$(BUILD):
	mkdir -p $@
$(BUILD)/btree-bench: bench/microbench.c $(COMMON) $(HEADERS) Makefile | $(BUILD)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(LDFLAGS) bench/microbench.c $(COMMON) $(LDLIBS) -o $@
$(BUILD)/btree-test: tests/upstream.c $(COMMON) $(HEADERS) Makefile | $(BUILD)
	$(CC) $(CPPFLAGS) $(CFLAGS) -DREDIS_TEST -DREDIS_DEBUG $(LDFLAGS) tests/upstream.c $(COMMON) $(LDLIBS) -o $@
check: $(BUILD)/btree-test
	$(BUILD)/btree-test
sanitize:
	$(MAKE) BUILD=build/sanitize OPT=-O1 CFLAGS='-std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all' LDFLAGS='-fsanitize=address,undefined' check
smoke: $(BUILD)/btree-bench
	$(BUILD)/btree-bench --size 1000 --ops 1000 --member-bytes 16 --seed 1
clean:
	rm -rf build
