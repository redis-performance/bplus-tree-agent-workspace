/* Diagnostic-only, macOS arm64 single-thread self-process sampler. */
#include <signal.h>
#include <sys/time.h>
#include <sys/ucontext.h>
#include <stdatomic.h>
#include <dlfcn.h>
#if !defined(__APPLE__) || !defined(__aarch64__)
#error This diagnostic is scoped to inspected macOS arm64 APIs
#endif
#define SAMPLE_CAP 65536
static _Atomic(uintptr_t) sample_pc[SAMPLE_CAP];
static _Atomic(unsigned) sample_count;
static volatile sig_atomic_t sample_active;
static unsigned sample_usec;
static sigset_t sample_mask;
static void sample_handler(int sig, siginfo_t *info, void *context) {
    (void)sig; (void)info;
    if (!sample_active) return;
    ucontext_t *uc = context;
    uintptr_t pc = (uintptr_t)__darwin_arm_thread_state64_get_pc(uc->uc_mcontext->__ss);
    unsigned i = atomic_fetch_add_explicit(&sample_count, 1, memory_order_relaxed);
    if (i < SAMPLE_CAP) atomic_store_explicit(&sample_pc[i], pc, memory_order_relaxed);
}
static void sample_init(void) {
    const char *arg = getenv("PROFILE_USEC");
    char *end = NULL;
    unsigned long value = arg ? strtoul(arg, &end, 10) : 1000;
    serverAssert(!arg || (end != arg && *end == 0));
    serverAssert(value >= 1 && value <= 999999);
    sample_usec = (unsigned)value;
    serverAssert(atomic_is_lock_free(&sample_count) && atomic_is_lock_free(&sample_pc[0]));
    struct itimerval prior;
    serverAssert(getitimer(ITIMER_PROF, &prior) == 0);
    serverAssert(prior.it_value.tv_sec == 0 && prior.it_value.tv_usec == 0);
    sigemptyset(&sample_mask); sigaddset(&sample_mask, SIGPROF);
    serverAssert(sigprocmask(SIG_BLOCK, &sample_mask, NULL) == 0);
    struct sigaction action = {0};
    action.sa_sigaction = sample_handler; action.sa_flags = SA_SIGINFO | SA_RESTART;
    sigemptyset(&action.sa_mask);
    serverAssert(sigaction(SIGPROF, &action, NULL) == 0);
}
static void sample_start(void) {
    atomic_store_explicit(&sample_count, 0, memory_order_relaxed);
    sample_active = 1;
    struct itimerval timer = {{0, sample_usec}, {0, sample_usec}};
    serverAssert(setitimer(ITIMER_PROF, &timer, NULL) == 0);
    serverAssert(sigprocmask(SIG_UNBLOCK, &sample_mask, NULL) == 0);
}
static void sample_stop(const char *scope) {
    struct itimerval timer = {{0,0},{0,0}};
    serverAssert(setitimer(ITIMER_PROF, &timer, NULL) == 0);
    serverAssert(sigprocmask(SIG_BLOCK, &sample_mask, NULL) == 0);
    sample_active = 0;
    unsigned n = atomic_load_explicit(&sample_count, memory_order_relaxed);
    fprintf(stderr,"PROFILE,%s,%u,%u,%u\n",scope,sample_usec,n,n > SAMPLE_CAP);
    for (unsigned i=0; i<n && i<SAMPLE_CAP; i++) {
        uintptr_t pc=atomic_load_explicit(&sample_pc[i], memory_order_relaxed);
        Dl_info info={0}; int found=dladdr((void*)pc,&info);
        const char *module=found && info.dli_fname ? strrchr(info.dli_fname,'/') : NULL;
        module=module ? module+1 : (found && info.dli_fname ? info.dli_fname : "unknown");
        fprintf(stderr,"PC,%s,0x%" PRIxPTR ",0x%" PRIxPTR ",%s,0x%" PRIxPTR "\n",
                module,pc,(uintptr_t)info.dli_fbase,
                found && info.dli_sname ? info.dli_sname : "unknown",(uintptr_t)info.dli_saddr);
    }
    serverAssert(n <= SAMPLE_CAP);
    /* Drain any pending delivery into an inactive handler before next scope. */
    serverAssert(sigprocmask(SIG_UNBLOCK, &sample_mask, NULL) == 0);
    serverAssert(sigprocmask(SIG_BLOCK, &sample_mask, NULL) == 0);
}
