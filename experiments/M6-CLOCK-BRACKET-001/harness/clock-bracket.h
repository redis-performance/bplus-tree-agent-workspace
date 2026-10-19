#ifndef ZBT_CLOCK_BRACKET_H
#define ZBT_CLOCK_BRACKET_H
#include "server.h"
#include <inttypes.h>
#include <time.h>

/* These are observations, not a calibration of clock accuracy/accounting lag. */
typedef struct {
    uint64_t w0, w1, w2, w3;
    int64_t t0, t1;
} clock_bracket;

#define CB_HEADER "w0_ns,t0_ns,w1_ns,w2_ns,t1_ns,w3_ns,wall_resolution_ns,thread_resolution_ns"

static inline uint64_t cb_clock(clockid_t id) {
    struct timespec ts;
    serverAssert(clock_gettime(id, &ts) == 0);
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + (uint64_t)ts.tv_nsec;
}

static inline uint64_t cb_resolution(clockid_t id) {
    struct timespec ts;
    serverAssert(clock_getres(id, &ts) == 0);
    return (uint64_t)ts.tv_sec * UINT64_C(1000000000) + (uint64_t)ts.tv_nsec;
}

static inline void cb_begin(clock_bracket *b) {
    b->w0 = cb_clock(CLOCK_MONOTONIC);
    b->t0 = (int64_t)cb_clock(CLOCK_THREAD_CPUTIME_ID);
    b->w1 = cb_clock(CLOCK_MONOTONIC);
}

static inline void cb_end(clock_bracket *b) {
    b->w2 = cb_clock(CLOCK_MONOTONIC);
    b->t1 = (int64_t)cb_clock(CLOCK_THREAD_CPUTIME_ID);
    b->w3 = cb_clock(CLOCK_MONOTONIC);
}

static inline void cb_emit(const clock_bracket *b, uint64_t wall_res, uint64_t thread_res) {
    printf("%" PRIu64 ",%" PRId64 ",%" PRIu64 ",%" PRIu64 ",%" PRId64 ",%" PRIu64 ",%" PRIu64 ",%" PRIu64,
           b->w0, b->t0, b->w1, b->w2, b->t1, b->w3, wall_res, thread_res);
}
#endif
