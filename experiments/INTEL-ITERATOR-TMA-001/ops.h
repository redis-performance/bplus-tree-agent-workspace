/* Separate long-window referee: only --ops accepts the wider range. */
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static size_t long_ops(const char *s) {
    char *end;
    errno = 0;
    unsigned long long value = strtoull(s, &end, 10);
    if (errno || !*s || s[0] == '-' || *end || !value ||
        value > UINT64_C(100000000000) || value > SIZE_MAX) {
        fprintf(stderr, "Invalid --ops: %s\n", s);
        exit(2);
    }
    return (size_t)value;
}
