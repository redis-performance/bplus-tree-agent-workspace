#define _POSIX_C_SOURCE 200809L
#include <assert.h>
#include <fcntl.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Same acknowledged FIFO transport as the validated tree profile frontend. */
static void profile_control(const char *cmd) {
    const char *ctl_path = getenv("BPLUS_PERF_CTL");
    const char *ack_path = getenv("BPLUS_PERF_ACK");
    assert(ctl_path && ack_path);
    int ctl = open(ctl_path, O_WRONLY), ack = open(ack_path, O_RDONLY);
    assert(ctl >= 0 && ack >= 0);
    assert(write(ctl, cmd, strlen(cmd)) == (ssize_t)strlen(cmd));
    char reply[4]; size_t used = 0;
    while (used < sizeof(reply)) {
        char byte; ssize_t n = read(ack, &byte, 1); assert(n == 1);
        if (byte == '\0' && used == 0) continue;
        reply[used++] = byte;
    }
    assert(!memcmp(reply, "ack\n", 4));
    close(ctl); close(ack);
}

/* Volatile recurrence prevents algebraic removal; different constants keep the
 * outside region distinguishable from the scoped positive-control function. */
__attribute__((noinline)) static uint64_t known_work(uint64_t initial) {
    volatile uint64_t value = initial;
    for (uint64_t i = 0; i < UINT64_C(100000000); i++)
        value = value * UINT64_C(2862933555777941757) + UINT64_C(3037000493);
    return value;
}
__attribute__((noinline)) static uint64_t outside_work(uint64_t initial) {
    volatile uint64_t value = initial;
    for (uint64_t i = 0; i < UINT64_C(100000000); i++)
        value = value * UINT64_C(6364136223846793005) + UINT64_C(1442695040888963407);
    return value;
}
int main(void) {
    uint64_t before = outside_work(1);
    int enabled = getenv("PROFILE_DISABLE") == NULL;
    if (enabled) profile_control("enable\n");
    uint64_t inside = known_work(3);
    if (enabled) profile_control("disable\n");
    uint64_t after = outside_work(7);
    printf("{\"rounds\":100000000,\"before\":\"%016" PRIx64
           "\",\"inside\":\"%016" PRIx64 "\",\"after\":\"%016" PRIx64 "\"}\n",
           before, inside, after);
    return 0;
}
