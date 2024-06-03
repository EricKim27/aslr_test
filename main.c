#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include "aslr.h"

int main(int argc, char *argv[])
{
    if(argc < 2)
    {
        printf("usage: %s <number of loops>\n", argv[0]);
        return EXIT_FAILURE;
    }
    printf("starting ASLR test\n");
    printf("The parent PID is %d\n", getpid());
    sleep(1);
    char filename[128];
    sprintf(filename, "logfile_%s.txt", argv[1]);
    for(int i=0; i<atoi(argv[1]); i++)
    {
        pid_t child = fork();
        if(child < 0)
        {
            fprintf(stderr, "Error occured\n");
            return EXIT_FAILURE;
        } else if(child == 0)
        {
            execl("./child", "child", filename, NULL);
            perror("execl failed");
            return EXIT_SUCCESS;
        } else
        {
            int status;
            waitpid(child, &status, 0);
        }
    }
    printf("Done.\n");
    return EXIT_SUCCESS;
}