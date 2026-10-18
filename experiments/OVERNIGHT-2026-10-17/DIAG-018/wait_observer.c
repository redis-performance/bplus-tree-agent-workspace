#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>
static volatile sig_atomic_t timed_out;
static pid_t child=-1;
static void expire(int sig){(void)sig;timed_out=1;if(child>0)kill(child,SIGKILL);}
static uint64_t now(void){struct timespec t;if(clock_gettime(CLOCK_MONOTONIC,&t))_exit(124);return(uint64_t)t.tv_sec*1000000000+(uint64_t)t.tv_nsec;}
int main(int argc,char **argv){
    if(argc<5)return 2;
    char *end;unsigned long seconds=strtoul(argv[2],&end,10);if(*end||!seconds||seconds>110)return 2;
    int fd=open(argv[1],O_WRONLY|O_CREAT|O_EXCL,0600);if(fd<0){perror("observer open");return 3;}
    struct sigaction sa={0};sa.sa_handler=expire;sigemptyset(&sa.sa_mask);if(sigaction(SIGALRM,&sa,NULL))return 4;
    child=fork();if(child<0)return 5;
    if(child==0){close(fd);execvp(argv[3],argv+3);_exit(127);}
    alarm((unsigned)seconds);int status;pid_t waited;
    do{waited=waitpid(child,&status,0);}while(waited<0&&errno==EINTR);
    uint64_t observed=now();alarm(0);if(waited!=child)return 6;
    int rc=WIFEXITED(status)?WEXITSTATUS(status):WIFSIGNALED(status)?128+WTERMSIG(status):125;
    dprintf(fd,"{\"waitpid_observed_ns\":%"PRIu64",\"child_status\":%d,\"timed_out\":%d}\n",observed,rc,(int)timed_out);close(fd);
    return rc;
}
