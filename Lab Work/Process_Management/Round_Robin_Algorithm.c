#include <stdio.h>
#include <stdlib.h>

#define MAX_PROCESSES 10

typedef struct {
    int id;               // Process ID
    int burstTime;        // Burst time of the process
    int remainingTime;    // Remaining time for the process
} Process;

void roundRobin(Process processes[], int n, int timeQuantum) {
    int time = 0; // Current time
    int allDone;  // Flag to check if all processes are done

    do {
        allDone = 1; // Assume all processes are done

        for (int i = 0; i < n; i++) {
            if (processes[i].remainingTime > 0) {
                allDone = 0; // At least one process is not done

                if (processes[i].remainingTime > timeQuantum) {
                    // Process will run for the time quantum
                    time += timeQuantum;
                    processes[i].remainingTime -= timeQuantum;
                    printf("Process %d executed for %d time units. Remaining time: %d\n", 
                           processes[i].id, timeQuantum, processes[i].remainingTime);
                } else {
                    // Process will finish in this time slice
                    time += processes[i].remainingTime;
                    printf("Process %d executed for %d time units. Remaining time: 0\n", 
                           processes[i].id, processes[i].remainingTime);
                    processes[i].remainingTime = 0; // Process is finished
                }
            }
        }
    } while (!allDone); // Repeat until all processes are done

    printf("All processes have completed execution.\n");
}

int main() {
    Process processes[MAX_PROCESSES];
    int n, timeQuantum;

    // Input number of processes
    printf("Enter the number of processes (max %d): ", MAX_PROCESSES);
    scanf("%d", &n);

    // Input burst times for each process
    for (int i = 0; i < n; i++) {
        processes[i].id = i + 1; // Process ID starts from 1
        printf("Enter burst time for Process %d: ", processes[i].id);
        scanf("%d", &processes[i].burstTime);
        processes[i].remainingTime = processes[i].burstTime; // Initialize remaining time
    }

    // Input time quantum
    printf("Enter time quantum: ");
    scanf("%d", &timeQuantum);

    // Run Round Robin scheduling
    roundRobin(processes, n, timeQuantum);

    return 0;
}
