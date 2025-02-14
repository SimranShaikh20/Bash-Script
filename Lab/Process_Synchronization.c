#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork(); // Create a new process

    if (pid < 0) {
        perror("fork failed");
        exit(1);
    } else if (pid == 0) {
        // Child process
        printf("Hello from Child! PID: %d, Parent PID: %d\n", getpid(), getppid());
        fflush(stdout); // Force output to be printed
        sleep(2); // Simulate some work
        printf("Child process (PID: %d) is exiting.\n", getpid());
        fflush(stdout); // Force output to be printed
        exit(0); // Exit child process
    } else {
        // Parent process
        printf("Hello from Parent! PID: %d, Child PID: %d\n", getpid(), pid);
        fflush(stdout); // Force output to be printed
        wait(NULL); // Wait for the child process to finish
        printf("Parent process (PID: %d) has finished waiting for the child.\n", getpid());
        fflush(stdout); // Force output to be printed
    }

    return 0;
}
