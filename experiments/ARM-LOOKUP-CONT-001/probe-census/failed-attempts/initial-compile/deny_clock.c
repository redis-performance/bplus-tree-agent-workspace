/* Link-time tripwires. Any explicit clock entry aborts before reading time. */
#include <unistd.h>
#define DENY(name) _Noreturn void __wrap_##name(void) { \
    static const char message[]="probe-census: forbidden clock/syscall " #name "\n"; \
    (void)write(STDERR_FILENO,message,sizeof(message)-1); _exit(125); }
DENY(clock_gettime)
DENY(clock_getres)
DENY(clock)
DENY(time)
DENY(gettimeofday)
DENY(times)
DENY(getrusage)
DENY(timespec_get)
DENY(timespec_getres)
DENY(__clock_gettime)
DENY(__clock_gettime64)
DENY(__gettimeofday)
DENY(syscall)
