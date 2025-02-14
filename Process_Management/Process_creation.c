#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t pid = fork(); // Create a new process

    if (pid < 0) {
        // Error handling
        perror("fork failed");
        exit(1);
    } else if (pid == 0) {
        // Child process
        printf("Hello from Child! PID: %d, Parent PID: %d\n", getpid(), getppid());
    } else {
        // Parent process
        printf("Hello from Parent! PID: %d, Child PID: %d\n", getpid(), pid);
    }

    return 0;
}
