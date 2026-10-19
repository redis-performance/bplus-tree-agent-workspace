#define _GNU_SOURCE 1
#define _DARWIN_C_SOURCE 1
#include "decoder_kernel.h"
#include <errno.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#if defined(__APPLE__)
#include <mach/mach_time.h>
#include <pthread.h>
#elif defined(__linux__)
#include <sched.h>
#include <linux/perf_event.h>
#include <sys/ioctl.h>
#include <sys/syscall.h>
#include <unistd.h>
#endif

#ifdef DECODE_PROFILE
#include "server.h"
#include "../002-rank/night-rank-sampler.h"
#endif
static int extended_testing;
static volatile uint64_t sink;
static double tick_ns = 1;
static const char *clock_name;
static void fail(const char *message) { fprintf(stderr, "%s\n", message); exit(2); }
static uint64_t ticks(void) {
#if defined(__APPLE__)
    return mach_absolute_time();
#else
    struct timespec ts;
#if defined(CLOCK_MONOTONIC_RAW)
    if (clock_gettime(CLOCK_MONOTONIC_RAW, &ts)) fail("clock_gettime failed");
#else
    if (clock_gettime(CLOCK_MONOTONIC, &ts)) fail("clock_gettime failed");
#endif
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + ts.tv_nsec;
#endif
}
static int cpu_id(void) {
#if defined(__APPLE__)
    size_t cpu;
    if (__builtin_available(macOS 11.0, *))
        return pthread_cpu_number_np(&cpu) == 0 ? (int)cpu : -1;
    return -1;
#elif defined(__linux__)
    return sched_getcpu();
#else
    return -1;
#endif
}
static unsigned number(const char *s, unsigned low, unsigned high) {
    char *end; errno = 0;
    unsigned long v = strtoul(s, &end, 10);
    if (errno || !*s || *end || *s == '-' || v < low || v > high) fail("Invalid numeric argument");
    return (unsigned)v;
}
static void self_test(void) {
    const unsigned ordinary[] = {1, 2, 7, 8, 31, 95, 96};
    const unsigned extended[] = {1, 2, 4, 7, 8, 16, 32, 96};
    const unsigned *counts = extended_testing ? extended : ordinary;
    const unsigned ncounts = extended_testing ? 8 : 7;
    unsigned fixtures = 0;
    for (unsigned width = 0; width <= 64; width++)
        for (unsigned reversed = 0; reversed <= 1; reversed++)
            for (unsigned k = 0; k < ncounts; k++)
                for (unsigned highshift = 0; highshift <= 1; highshift++) {
                    unsigned shift = highshift ? (width ? 64 - width : 63) : 0;
                    decoder_fixture *f = decoder_create(width, shift, reversed, counts[k], 2, 104729 + fixtures);
                    decoder_info info = decoder_describe(f);
                    if (!decoder_validate(f) || decoder_batch(f, 0) != 0 ||
                        decoder_batch(f, 1) != info.expected_sum ||
                        decoder_batch(f, 3) != info.expected_sum * 3) fail("Decoder self-test failed");
                    decoder_destroy(f); fixtures++;
                }
    printf("PASS fixtures=%u widths=0..64 directions=2 counts=%u score_shifts=2\n", fixtures, ncounts);
}

/* Optional separate PMU pass. No wall-clock timer calls inside this bracket.
 * It includes the wrapper/checksum and user-space enable/disable call boundaries.
 * Never scale multiplexed events or infer cycles from wall-clock nanoseconds. */
static int counter_open(int *instruction_fd) {
#if defined(__linux__)
    struct perf_event_attr a;
    memset(&a, 0, sizeof(a)); a.size = sizeof(a); a.type = PERF_TYPE_HARDWARE;
    a.config = PERF_COUNT_HW_CPU_CYCLES; a.disabled = 1;
    a.exclude_kernel = 1; a.exclude_hv = 1;
    a.read_format = PERF_FORMAT_GROUP | PERF_FORMAT_TOTAL_TIME_ENABLED | PERF_FORMAT_TOTAL_TIME_RUNNING;
    int leader = (int)syscall(SYS_perf_event_open, &a, 0, -1, -1, 0);
    if (leader < 0) return -1;
    a.config = PERF_COUNT_HW_INSTRUCTIONS; a.disabled = 0;
    *instruction_fd = (int)syscall(SYS_perf_event_open, &a, 0, -1, leader, 0);
    if (*instruction_fd < 0) { int error = errno; close(leader); errno = error; return -1; }
    return leader;
#else
    (void)instruction_fd; errno = ENOTSUP; return -1;
#endif
}
static int counter_sample(int fd, decoder_fixture *f, unsigned rounds,
                          uint64_t expected, uint64_t *cycles, uint64_t *instructions) {
#if defined(__linux__)
    if (ioctl(fd, PERF_EVENT_IOC_RESET, PERF_IOC_FLAG_GROUP) ||
        ioctl(fd, PERF_EVENT_IOC_ENABLE, PERF_IOC_FLAG_GROUP)) return 0;
    uint64_t result = decoder_batch(f, rounds);
    if (ioctl(fd, PERF_EVENT_IOC_DISABLE, PERF_IOC_FLAG_GROUP)) return 0;
    sink ^= result;
    if (result != expected) fail("Counter-pass checksum failed");
    struct { uint64_t nr, enabled, running, cycles, instructions; } values;
    if (read(fd, &values, sizeof(values)) != (ssize_t)sizeof(values) || values.nr != 2 ||
        !values.running || values.running != values.enabled) return 0;
    *cycles = values.cycles; *instructions = values.instructions; return 1;
#else
    (void)fd; (void)f; (void)rounds; (void)expected; (void)cycles; (void)instructions; return 0;
#endif
}

int main(int argc, char **argv) {
    unsigned width = 63, shift = 0, reversed = 0, count = 96, leaves = 8;
    unsigned rounds = 64, samples = 129, warmup = 16, seed = 1;
    int counters = 0, testing = 0;
    for (int i = 1; i < argc; i++) {
        const char *arg = argv[i];
        if (!strcmp(arg, "--help")) {
            puts("decoder-bench [--width 0..64] [--score-shift 0..63] [--reversed 0|1] [--count 1..96] [--leaves 1..64] [--rounds 1..65536] [--samples 1..4096] [--warmup 1..1024] [--seed 1..100000000] [--counters] [--self-test]"); return 0;
        }
        if (!strcmp(arg, "--counters")) { counters = 1; continue; }
        if (!strcmp(arg, "--extended-test")) { testing = 1; extended_testing = 1; continue; }
        if (!strcmp(arg, "--self-test")) { testing = 1; continue; }
        if (++i == argc) fail("Missing option value");
        const char *value = argv[i];
        if (!strcmp(arg, "--width")) width = number(value, 0, 64);
        else if (!strcmp(arg, "--score-shift")) shift = number(value, 0, 63);
        else if (!strcmp(arg, "--reversed")) reversed = number(value, 0, 1);
        else if (!strcmp(arg, "--count")) count = number(value, 1, 96);
        else if (!strcmp(arg, "--leaves")) leaves = number(value, 1, 64);
        else if (!strcmp(arg, "--rounds")) rounds = number(value, 1, 100000000);
        else if (!strcmp(arg, "--samples")) samples = number(value, 1, 4096);
        else if (!strcmp(arg, "--warmup")) warmup = number(value, 1, 1024);
        else if (!strcmp(arg, "--seed")) seed = number(value, 1, 100000000);
        else fail("Unknown option");
    }
    if (width + shift > 64) fail("width + score-shift must be <=64");
    if (testing) { self_test(); return 0; }
#if defined(__APPLE__)
    mach_timebase_info_data_t timebase;
    if (mach_timebase_info(&timebase) || !timebase.denom) fail("Timebase unavailable");
    tick_ns = (double)timebase.numer / timebase.denom; clock_name = "mach_absolute_time";
#elif defined(CLOCK_MONOTONIC_RAW)
    clock_name = "CLOCK_MONOTONIC_RAW";
#else
    clock_name = "CLOCK_MONOTONIC";
#endif
    decoder_fixture *f = decoder_create(width, shift, reversed, count, leaves, seed);
    decoder_info info = decoder_describe(f);
    if (!decoder_validate(f)) fail("Fixture validation failed");
    uint64_t expected = info.expected_sum * rounds;
    typedef struct { uint64_t elapsed, checksum; int cpu_start, cpu_end; } sample;
    sample *rows = calloc(samples, sizeof(*rows));
    if (!rows) fail("Allocation failed");
    /* Observed timer floor only; never subtract this from kernel measurements. */
    uint64_t min_tick = UINT64_MAX, empty_min = UINT64_MAX;
    for (unsigned i = 0; i < 1024; i++) {
        uint64_t t = ticks(), dt = ticks() - t;
        if (dt && dt < min_tick) min_tick = dt;
        t = ticks(); uint64_t result = decoder_batch(f, 0); dt = ticks() - t;
        sink ^= result;
        if (dt < empty_min) empty_min = dt;
    }
    for (unsigned i = 0; i < warmup; i++) {
        unsigned warm_rounds = rounds < 1024 ? rounds : 1024;
        uint64_t result = decoder_batch(f, warm_rounds);
        if (result != info.expected_sum * warm_rounds) fail("Warmup checksum failed");
        sink ^= result;
    }
#ifdef DECODE_PROFILE
    sample_init(); sample_start();
#endif
    for (unsigned i = 0; i < samples; i++) {
        rows[i].cpu_start = cpu_id();
        uint64_t begin = ticks();
        uint64_t result = decoder_batch(f, rounds);
        rows[i].elapsed = ticks() - begin;
        rows[i].cpu_end = cpu_id(); rows[i].checksum = result;
        if (result != expected) fail("Timed checksum failed");
        sink ^= result;
    }
#ifdef DECODE_PROFILE
    sample_stop("decoder-measurement-loop");
#endif
    if (!decoder_validate(f)) fail("Post-run validation failed");
    uint64_t operations = (uint64_t)info.decodes_per_round * rounds;
    fprintf(stderr, "clock=%s tick_ns=%.9g observed_min_nonzero_ns=%.9g empty_call_min_ns=%.9g counters=%s\n",
            clock_name, tick_ns, min_tick == UINT64_MAX ? -1 : min_tick * tick_ns,
            empty_min * tick_ns, counters ? "requested-separate-pass" : "not-requested");
    puts("kind,sample,width,score_shift,reversed,count,leaves,rounds,seed,operations,leaf_bytes,offset_mask,crossings_per_round,fixture_hash,checksum,elapsed_ns,ns_per_decode,cpu_start,cpu_end,cycles,instructions");
    for (unsigned i = 0; i < samples; i++)
        printf("time,%u,%u,%u,%u,%u,%u,%u,%u,%"PRIu64",%zu,%u,%zu,%"PRIu64",%"PRIu64",%.3f,%.9f,%d,%d,,\n",
               i, width, shift, reversed, count, leaves, rounds, seed, operations,
               info.leaf_bytes, info.offset_mask, info.crossings_per_round, info.fingerprint,
               rows[i].checksum, rows[i].elapsed * tick_ns, rows[i].elapsed * tick_ns / operations,
               rows[i].cpu_start, rows[i].cpu_end);
    if (counters) {
        int instruction_fd = -1, fd = counter_open(&instruction_fd);
        if (fd < 0) fprintf(stderr, "counter_status=unavailable errno=%d\n", errno);
        else {
            uint64_t cycles = 0, instructions = 0;
            for (unsigned i = 0; i < samples; i++) {
                if (!counter_sample(fd, f, rounds, expected, &cycles, &instructions)) {
                    fprintf(stderr, "counter_status=invalid_or_multiplexed sample=%u\n", i); break;
                }
                printf("counter,%u,%u,%u,%u,%u,%u,%u,%u,%"PRIu64",%zu,%u,%zu,%"PRIu64",%"PRIu64",,,,,%"PRIu64",%"PRIu64"\n",
                       i, width, shift, reversed, count, leaves, rounds, seed, operations,
                       info.leaf_bytes, info.offset_mask, info.crossings_per_round,
                       info.fingerprint, expected, cycles, instructions);
            }
#if defined(__linux__)
            close(instruction_fd); close(fd);
#endif
        }
    }
    free(rows); decoder_destroy(f); return 0;
}
