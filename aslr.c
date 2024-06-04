#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include "aslr.h"

void do_memaddr_log(int fd)
{
    int i;
    int *a = (int *)malloc(sizeof(int));
    if(a == NULL){
        perror("malloc");
        return;
    }
    char buf[256];
    int len = sprintf(buf, "stack addr of PID %d: %p\n", getpid(), &i);
    if(write(fd, buf, len) == -1)
        perror("write1");
    memset(buf, 0, sizeof(buf));
    len = sprintf(buf, "heap addr of PID %d: %p\n", getpid(), (void *)a);
    if(write(fd, buf, len) == -1)
        perror("write2");
    free(a);
}