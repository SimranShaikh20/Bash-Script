# Banker's Algorithm Simulator

## Problem Statement
The Banker's Algorithm is used in operating systems to allocate resources safely among multiple processes while preventing deadlocks. This project simulates the Banker's Algorithm for resource allocation and management.

## Approach
The algorithm follows these steps:
1. **Initialize Resources**: Available resources and maximum claims are set.
2. **Request Handling**: Users can request or release resources.
3. **Safety Check**: Requests are granted only if the system remains in a safe state.
4. **Status Display**: Users can view the current allocation status.

## Features
- Handles multiple processes and resource types.
- Ensures safe state before granting requests.
- Provides a command-line interface for interaction.

## Code
```python
import sys
import numpy as np

NUMBER_OF_CUSTOMERS = 5
NUMBER_OF_RESOURCES = 4

available = np.zeros(NUMBER_OF_RESOURCES, dtype=int)
maximum = np.zeros((NUMBER_OF_CUSTOMERS, NUMBER_OF_RESOURCES), dtype=int)
allocation = np.zeros((NUMBER_OF_CUSTOMERS, NUMBER_OF_RESOURCES), dtype=int)
need = np.zeros((NUMBER_OF_CUSTOMERS, NUMBER_OF_RESOURCES), dtype=int)

def initialize_system():
    global available, maximum, need
    available[:] = [10, 5, 7, 8]  # Default available resources
    maximum[:] = np.random.randint(1, 6, (NUMBER_OF_CUSTOMERS, NUMBER_OF_RESOURCES))
    need[:] = maximum - allocation

def is_safe():
    work = available.copy()
    finish = [False] * NUMBER_OF_CUSTOMERS
    safe_sequence = []
    
    while len(safe_sequence) < NUMBER_OF_CUSTOMERS:
        allocated = False
        for i in range(NUMBER_OF_CUSTOMERS):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(i)
                allocated = True
        if not allocated:
            return False, []
    return True, safe_sequence

def request_resources(customer_num, request):
    global available, allocation, need
    request = np.array(request)
    
    if any(request > need[customer_num]) or any(request > available):
        print("Request denied.")
        return -1
    
    available -= request
    allocation[customer_num] += request
    need[customer_num] -= request
    
    safe, _ = is_safe()
    if safe:
        print("Request granted.")
        return 0
    else:
        available += request
        allocation[customer_num] -= request
        need[customer_num] += request
        print("Request denied (unsafe state).")
        return -1

def release_resources(customer_num, release):
    global available, allocation, need
    release = np.array(release)
    
    if any(release > allocation[customer_num]):
        print("Error: Cannot release more than allocated.")
        return
    
    available += release
    allocation[customer_num] -= release
    need[customer_num] += release
    print("Resources released successfully.")

def print_status():
    print("\nSystem State:")
    print("Available:", available)
    print("Max Claims:\n", maximum)
    print("Allocation:\n", allocation)
    print("Need:\n", need)

def main():
    initialize_system()
    print("\nBanker's Algorithm Simulation Started")
    while True:
        command = input("Enter command (RQ/RL/STATUS/EXIT): ").split()
        if not command:
            continue
        
        if command[0] == "RQ":
            cust_id = int(command[1])
            req_resources = list(map(int, command[2:]))
            request_resources(cust_id, req_resources)
        elif command[0] == "RL":
            cust_id = int(command[1])
            rel_resources = list(map(int, command[2:]))
            release_resources(cust_id, rel_resources)
        elif command[0] == "STATUS":
            print_status()
        elif command[0] == "EXIT":
            print("Exiting program.")
            break
        else:
            print("Invalid command! Use RQ, RL, STATUS, or EXIT.")

if __name__ == "__main__":
    main()
```

## How to Run
1. Ensure Python is installed.
2. Run the script:
   ```sh
   python banker.py
   ```
3. Use commands:
   - `RQ <customer_id> <res1> <res2> ...` to request resources.
   - `RL <customer_id> <res1> <res2> ...` to release resources.
   - `STATUS` to check the current state.
   - `EXIT` to quit.

## Expected Output
- Displays available resources, allocation, and need matrices.
- Grants or denies requests based on safety.

## License
This project is open-source under the MIT License.
