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
        printf("Child process (PID: %d) is executing 'ls'.\n", getpid());
        fflush(stdout); // Force output to be printed

        // Execute the 'ls' command
        execlp("ls", "ls", NULL);

        // If execlp fails, print an error message
        perror("execlp failed");
        exit(1); // Exit child process if execlp fails
    } else {
        // Parent process
        printf("Parent process (PID: %d) is waiting for the child to complete.\n", getpid());
        fflush(stdout); // Force output to be printed
