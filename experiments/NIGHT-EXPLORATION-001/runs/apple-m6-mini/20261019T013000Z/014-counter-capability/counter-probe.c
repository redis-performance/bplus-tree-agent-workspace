/* Qualification workload only. Not a data-structure benchmark. */
#define _DARWIN_C_SOURCE 1
#define _POSIX_C_SOURCE 200809L
#include <os/log.h>
#include <os/signpost.h>
#include <errno.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
static volatile uint64_t probe_sink;
__attribute__((noinline)) uint64_t qualification_alu(uint64_t items, uint64_t x) {
    for (uint64_t i = 0; i < items; i++) {
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
    }
    probe_sink = x;
    return x;
}
static int sleep_ms(long ms) {
    struct timespec request = {ms / 1000, (ms % 1000) * 1000000};
    while (nanosleep(&request, &request)) if (errno != EINTR) return 0;
    return 1;
}
int main(int argc, char **argv) {
    alarm(6); /* Bounds even a launched target if tracing stops unexpectedly. */
    if (argc != 5 || strcmp(argv[1], "--case") || strcmp(argv[3], "--items")) return 2;
    const char *kind = argv[2];
    char *end = NULL; errno = 0;
    uint64_t items = strtoull(argv[4], &end, 10);
    if (errno || end == argv[4] || *end) return 2;
    int idle = !strcmp(kind, "idle");
    if ((!idle && strcmp(kind, "alu")) || (idle && items) ||
        (!idle && items != UINT64_C(268435456) && items != UINT64_C(536870912))) return 2;
    printf("{\"event\":\"started\",\"own_pid\":%d}\n", (int)getpid());
    if (fflush(stdout)) return 5;
    os_log_t log = os_log_create("org.redis-performance.bplus-tree.counter-qualification", OS_LOG_CATEGORY_POINTS_OF_INTEREST);
    if (!sleep_ms(250)) return 3;
    int enabled = os_signpost_enabled(log);
    os_signpost_id_t interval = os_signpost_id_generate(log);
    os_signpost_interval_begin(log, interval, "qualification-work", "kind=%{public}s items=%{public}llu", kind, (unsigned long long)items);
    uint64_t checksum = 1;
    if (idle) { if (!sleep_ms(1000)) return 3; }
    else checksum = qualification_alu(items, 1);
    os_signpost_interval_end(log, interval, "qualification-work", "checksum=%{public}llu", (unsigned long long)checksum);
    if (!checksum) return 4; /* Nonzero xorshift state remains nonzero. */
    printf("{\"event\":\"completed\",\"case\":\"%s\",\"items\":%" PRIu64 ",\"seed\":1,\"checksum\":%" PRIu64 ",\"own_pid\":%d,\"signposts_enabled\":%s}\n", kind, items, checksum, (int)getpid(), enabled ? "true" : "false");
    if (fflush(stdout)) return 5;
    return 0;
}
