#define _GNU_SOURCE 1
#define _DARWIN_C_SOURCE 1
#define _POSIX_C_SOURCE 200809L
#include "clock-bracket.h"
#include <errno.h>

static volatile uint64_t sink;

int main(void) {
    const uint64_t wall_res = cb_resolution(CLOCK_MONOTONIC);
    const uint64_t thread_res = cb_resolution(CLOCK_THREAD_CPUTIME_ID);
    puts("control,repetition,iterations,requested_block_ns,sleep_wall_ns,sleep_interruptions,checksum," CB_HEADER);
    for (unsigned repetition = 0; repetition < 24; repetition++) {
        for (unsigned control = 0; control < 3; control++) {
            uint64_t value = 1, sleep_wall = 0;
            unsigned interruptions = 0;
            clock_bracket bracket;
            cb_begin(&bracket);
            if (control == 1) {
                for (unsigned i = 0; i < 2000000; i++)
                    value = value * UINT64_C(1664525) + UINT64_C(1013904223);
            } else if (control == 2) {
                struct timespec requested = {0, 20000000}, remaining;
                uint64_t sleep_start = cb_clock(CLOCK_MONOTONIC);
                while (nanosleep(&requested, &remaining) != 0) {
                    serverAssert(errno == EINTR);
                    requested = remaining;
                    interruptions++;
                }
                sleep_wall = cb_clock(CLOCK_MONOTONIC) - sleep_start;
            }
            cb_end(&bracket);
            sink ^= value;
            printf("%s,%u,%u,%u,%" PRIu64 ",%u,%" PRIu64 ",",
                   control == 0 ? "empty" : control == 1 ? "cpu" : "block",
                   repetition, control == 1 ? 2000000 : 0,
                   control == 2 ? 20000000 : 0, sleep_wall, interruptions, value);
            cb_emit(&bracket, wall_res, thread_res);
            putchar('\n');
        }
    }
    return 0;
}
