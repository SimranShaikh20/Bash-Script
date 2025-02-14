#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>  // For pid_t
#include <sys/wait.h>   // For wait()

int main() {
    int pipefd[2]; // Array to hold the read and write file descriptors
    pid_t pid;
    char message[] = "Hello from Parent!";
    char buffer[100]; // Buffer to hold the message read by the child

    // Create a pipe
    if (pipe(pipefd) == -1) {
        perror("pipe failed");
        exit(1);
    }

    // Create a new process
    pid = fork();

    if (pid < 0) {
        perror("fork failed");
        exit(1);
    } 
    // Child process
    else if (pid == 0) {
        // Close the write end of the pipe
        close(pipefd[1]);

        // Read the message from the pipe
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);

        // Close the read end of the pipe
        close(pipefd[0]);
    } 
    // Parent process
    else {
        // Close the read end of the pipe
        close(pipefd[0]);

        // Write the message to the pipe
        write(pipefd[1], message, strlen(message) + 1); // +1 to include the null terminator
        printf("Parent sent: %s\n", message);

        // Close the write end of the pipe
        close(pipefd[1]);

        // Wait for the child process to finish
        wait(NULL); // Wait for any child process to finish
    }

    return 0;
}
