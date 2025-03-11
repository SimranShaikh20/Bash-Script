import numpy as np

# Constants
NUMBER_OF_CUSTOMERS = 5
NUMBER_OF_RESOURCES = 4

# Resource management matrices
available = np.array([10, 5, 7, 8])  # Default available resources
maximum = np.array([
    [7, 5, 3, 4],
    [3, 2, 2, 2],
    [9, 0, 2, 2],
    [2, 2, 2, 2],
    [4, 3, 3, 3]
])  # Default max demand
allocation = np.zeros((NUMBER_OF_CUSTOMERS, NUMBER_OF_RESOURCES), dtype=int)
need = maximum - allocation  # Calculate initial need

def is_safe():
    """Check if the system is in a safe state."""
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
    """Process a resource request from a customer."""
    global available, allocation, need
    request = np.array(request)
    
    if any(request > need[customer_num]):
        print("Error: Request exceeds maximum claim.")
        return -1
    if any(request > available):
        print("Resources not available. Request denied.")
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
    """Release allocated resources."""
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
    """Display the current system state."""
    print("\nCurrent System State:")
    print("Available Resources:", available)
    print("Maximum Claim Matrix:\n", maximum)
    print("Allocation Matrix:\n", allocation)
    print("Need Matrix:\n", need)

def main():
    print("\nBanker's Algorithm Simulation Started")
    while True:
        command = input("\nEnter command (RQ/RL/STATUS/EXIT): ").strip().upper().split()
        
        if not command:
            print("Invalid command! Use RQ, RL, STATUS, or EXIT.")
            continue
        
        if command[0] == "RQ":
            if len(command) < NUMBER_OF_RESOURCES + 2:
                print("Error: Invalid RQ format. Use 'RQ <customer_id> <r1> <r2> <r3> <r4>'")
                continue
            cust_id = int(command[1])
            req_resources = list(map(int, command[2:]))
            request_resources(cust_id, req_resources)
        
        elif command[0] == "RL":
            if len(command) < NUMBER_OF_RESOURCES + 2:
                print("Error: Invalid RL format. Use 'RL <customer_id> <r1> <r2> <r3> <r4>'")
                continue
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