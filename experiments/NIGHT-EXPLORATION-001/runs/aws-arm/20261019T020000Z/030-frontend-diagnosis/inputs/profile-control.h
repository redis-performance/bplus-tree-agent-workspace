#include <unistd.h>
#include <fcntl.h>
static void profile_control(const char *cmd) {
    int ctl=open(getenv("BPLUS_PERF_CTL"),O_WRONLY);
    int ack=open(getenv("BPLUS_PERF_ACK"),O_RDONLY);
    serverAssert(ctl>=0 && ack>=0);
    serverAssert(write(ctl,cmd,strlen(cmd))==(ssize_t)strlen(cmd));
    char reply[4]; size_t used=0;
    while(used<4) {
        char byte; ssize_t n=read(ack,&byte,1); serverAssert(n==1);
        if (byte == '\0' && used == 0) continue;
        reply[used++]=byte;
    }
    serverAssert(!memcmp(reply,"ack\n",4));
    close(ctl);close(ack);
}
