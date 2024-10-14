#include <stdlib.h>
#include <unistd.h>
#include <syslog.h>
#include <wait.h>

int service(void)
{
    while(1) {
        syslog (LOG_NOTICE, "Test daemon work at every 10 sec.");
        sleep(10);
    }
    return 0;
}

void main() {
    pid_t  pid;

    // fork
    pid = fork();
 
    // log for fork error
    if(pid < 0) exit(EXIT_FAILURE);
    
    // log for  parrent process kill
    if (pid > 0) exit(EXIT_SUCCESS);


    signal(SIGCHLD, SIG_IGN);
    signal(SIGHUP, SIG_IGN);

    int x; 
    for (x = sysconf(_SC_OPEN_MAX); x>=0; x--)
        close (x);
    chdir("/");
    openlog ("my-daemon", LOG_PID, LOG_DAEMON);
 
    // assing new session id
    if ( setsid() < 0) exit(EXIT_FAILURE);

    while(1) {
        if((pid = fork()) < 0) {
                exit(EXIT_FAILURE);
        }else if(pid == 0) {
                service();
                exit(0);
        }else if(pid > 0) {
                int ret;
                wait(&ret); 
        }
    }
}

